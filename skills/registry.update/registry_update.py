#!/usr/bin/env python3
"""
registry_update.py – Implementation of the registry.update Skill
Adds, updates, or removes entries in the Betty Framework Skill Registry.
"""

import os
import sys
import json
import yaml
import subprocess
from typing import Dict, Any, Optional, List
from datetime import datetime, timezone
from packaging import version as version_parser

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REGISTRY_FILE, REGISTRY_VERSION, get_skill_handler_path, REGISTRY_DIR
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import RegistryError, format_error_response
from betty.telemetry_capture import capture_execution

logger = setup_logger(__name__)

AGENTS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "agents.json")


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "path": path,
    }

    if details is not None:
        response["details"] = details

    return response


def load_manifest(path: str) -> Dict[str, Any]:
    """
    Load a skill manifest from YAML file.

    Args:
        path: Path to skill manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        RegistryError: If manifest cannot be loaded
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise RegistryError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise RegistryError(f"Invalid YAML in manifest: {e}")


def enforce_policy(manifest_path: str) -> Dict[str, Any]:
    """
    Run policy enforcement on the manifest before registry update.

    Args:
        manifest_path: Path to skill manifest file

    Returns:
        Policy enforcement result

    Raises:
        RegistryError: If policy enforcement fails or violations are detected
    """
    try:
        policy_handler = get_skill_handler_path("policy.enforce")
        logger.info(f"Running policy enforcement on: {manifest_path}")

        result = subprocess.run(
            [sys.executable, policy_handler, manifest_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Try to parse JSON output
        policy_result = None
        if result.stdout.strip():
            try:
                policy_result = json.loads(result.stdout.strip())
            except json.JSONDecodeError:
                logger.warning("Failed to parse policy enforcement output as JSON")

        # Check if policy enforcement passed
        if result.returncode != 0:
            errors = []
            if policy_result and isinstance(policy_result, dict):
                errors = policy_result.get("errors", [])
            if not errors:
                errors = [f"Policy enforcement failed with return code {result.returncode}"]

            error_msg = "Policy violations detected:\n" + "\n".join(f"  - {err}" for err in errors)
            logger.error(error_msg)
            raise RegistryError(error_msg)

        if policy_result and not policy_result.get("ok", False):
            errors = policy_result.get("errors", ["Unknown policy violation"])
            error_msg = "Policy violations detected:\n" + "\n".join(f"  - {err}" for err in errors)
            logger.error(error_msg)
            raise RegistryError(error_msg)

        logger.info("✅ Policy enforcement passed")
        return policy_result or {}

    except subprocess.TimeoutExpired:
        raise RegistryError("Policy enforcement timed out")
    except FileNotFoundError:
        logger.warning("policy.enforce skill not found, skipping policy enforcement")
        return {}
    except Exception as e:
        if isinstance(e, RegistryError):
            raise
        logger.error(f"Failed to run policy enforcement: {e}")
        raise RegistryError(f"Failed to run policy enforcement: {e}")


def increment_version(version_str: str, bump_type: str = "patch") -> str:
    """
    Increment semantic version.

    Args:
        version_str: Current version string (e.g., "1.2.3")
        bump_type: Type of version bump ("major", "minor", or "patch")

    Returns:
        Incremented version string
    """
    try:
        ver = version_parser.parse(version_str)
        major, minor, patch = ver.major, ver.minor, ver.micro

        if bump_type == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump_type == "minor":
            minor += 1
            patch = 0
        else:  # patch
            patch += 1

        return f"{major}.{minor}.{patch}"
    except Exception as e:
        logger.warning(f"Error incrementing version {version_str}: {e}")
        return version_str


def run_registry_diff(manifest_path: str) -> Optional[Dict[str, Any]]:
    """
    Run registry.diff to analyze changes in the manifest.

    Args:
        manifest_path: Path to skill manifest file

    Returns:
        Diff analysis result or None if diff fails
    """
    try:
        diff_handler = get_skill_handler_path("registry.diff")
        logger.info(f"Running registry.diff on: {manifest_path}")

        result = subprocess.run(
            [sys.executable, diff_handler, manifest_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Parse JSON output - registry.diff prints JSON as first output
        if result.stdout.strip():
            try:
                # Split by newlines and get the first JSON block
                lines = result.stdout.strip().split('\n')
                json_lines = []
                in_json = False
                brace_count = 0

                for line in lines:
                    if line.strip().startswith('{'):
                        in_json = True
                    if in_json:
                        json_lines.append(line)
                        brace_count += line.count('{') - line.count('}')
                        if brace_count == 0:
                            break

                json_str = '\n'.join(json_lines)
                diff_result = json.loads(json_str)

                if diff_result and "details" in diff_result:
                    return diff_result["details"]
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse registry.diff output as JSON: {e}")

        return None

    except subprocess.TimeoutExpired:
        logger.warning("registry.diff timed out")
        return None
    except FileNotFoundError:
        logger.warning("registry.diff skill not found, skipping diff analysis")
        return None
    except Exception as e:
        logger.warning(f"Failed to run registry.diff: {e}")
        return None


def determine_version_bump(diff_result: Dict[str, Any]) -> tuple[str, str]:
    """
    Determine the type of version bump needed based on diff analysis.

    Rules:
    - Field removed → major bump
    - Field or permission added → minor bump
    - No breaking change → patch bump

    Args:
        diff_result: Result from registry.diff

    Returns:
        Tuple of (bump_type, reason)
    """
    diff_type = diff_result.get("diff_type", "")
    breaking = diff_result.get("breaking", False)
    changed_fields = diff_result.get("changed_fields", [])
    details = diff_result.get("details", {})

    # Extract specific changes
    removed_fields = details.get("removed_fields", [])
    removed_perms = details.get("removed_permissions", [])
    added_perms = details.get("added_permissions", [])

    # Filter out metadata fields that are added by registry (not user-defined)
    # These fields should not trigger version bumps
    metadata_fields = ["updated_at", "version_bump_reason"]
    removed_fields = [f for f in removed_fields if f not in metadata_fields]
    changed_fields = [f for f in changed_fields if f not in metadata_fields]

    reasons = []

    # Rule 1: Field removed → major bump
    if removed_fields:
        reasons.append(f"Removed fields: {', '.join(removed_fields)}")
        return "major", "; ".join(reasons)

    # Rule 2: Permission removed → major bump (breaking change)
    if removed_perms:
        reasons.append(f"Removed permissions: {', '.join(removed_perms)}")
        return "major", "; ".join(reasons)

    # Rule 3: Field or permission added → minor bump
    if added_perms:
        reasons.append(f"Added permissions: {', '.join(added_perms)}")
        return "minor", "; ".join(reasons)

    # Check for new fields (compare changed_fields)
    # Fields that are in changed_fields but not version/description/status
    non_trivial_changes = [
        f for f in changed_fields
        if f not in ["version", "description", "updated_at", "tags"]
    ]

    if non_trivial_changes:
        # Check if fields were added (not just modified)
        # This would need more sophisticated detection, but for now
        # we'll treat new inputs/outputs/capabilities as minor bumps
        if any(f in non_trivial_changes for f in ["inputs", "outputs", "capabilities", "skills_available", "entrypoints"]):
            reasons.append(f"Modified fields: {', '.join(non_trivial_changes)}")
            return "minor", "; ".join(reasons)

    # Rule 4: No breaking change → patch bump
    if changed_fields and not breaking:
        reasons.append(f"Updated fields: {', '.join(changed_fields)}")
        return "patch", "; ".join(reasons)

    # Default to patch for any other changes
    if diff_type not in ["new", "no_change"]:
        return "patch", "General updates"

    return "patch", "No significant changes"


def apply_auto_version(manifest_path: str, manifest: Dict[str, Any]) -> tuple[Dict[str, Any], Optional[str]]:
    """
    Apply automatic version bumping to the manifest.

    Args:
        manifest_path: Path to manifest file
        manifest: Loaded manifest data

    Returns:
        Tuple of (updated_manifest, version_bump_reason) or (manifest, None) if no bump
    """
    # Run diff analysis
    diff_result = run_registry_diff(manifest_path)

    if not diff_result:
        logger.info("No diff result available, skipping auto-version")
        return manifest, None

    diff_type = diff_result.get("diff_type", "")

    # Skip auto-versioning for new entries or no changes
    if diff_type in ["new", "no_change"]:
        logger.info(f"Diff type '{diff_type}' does not require auto-versioning")
        return manifest, None

    # Skip if version was already bumped
    if diff_type == "version_bump":
        logger.info("Version already bumped manually, skipping auto-version")
        return manifest, None

    # Determine version bump type
    bump_type, reason = determine_version_bump(diff_result)

    current_version = manifest.get("version", "0.0.0")
    new_version = increment_version(current_version, bump_type)

    logger.info(f"Auto-versioning: {current_version} → {new_version} ({bump_type} bump)")
    logger.info(f"Reason: {reason}")

    # Update manifest
    updated_manifest = manifest.copy()
    updated_manifest["version"] = new_version
    updated_manifest["updated_at"] = datetime.now(timezone.utc).isoformat()

    # Save updated manifest back to file
    try:
        with open(manifest_path, 'w') as f:
            yaml.safe_dump(updated_manifest, f, default_flow_style=False, sort_keys=False)
        logger.info(f"Updated manifest file with new version: {manifest_path}")
    except Exception as e:
        logger.warning(f"Failed to write updated manifest: {e}")

    return updated_manifest, reason


def update_registry_data(manifest_path: str, auto_version: bool = False) -> Dict[str, Any]:
    """
    Update the registry with a skill manifest.

    Uses file locking to ensure thread-safe updates.

    Args:
        manifest_path: Path to skill manifest file
        auto_version: Whether to automatically increment version based on changes

    Returns:
        Result dictionary with update status

    Raises:
        RegistryError: If update fails
    """
    # Validate path
    validate_path(manifest_path, must_exist=True)

    # Enforce policy before updating registry
    policy_result = enforce_policy(manifest_path)

    # Load manifest
    manifest = load_manifest(manifest_path)

    if not manifest.get("name"):
        raise RegistryError("Manifest missing required 'name' field")

    skill_name = manifest["name"]
    logger.info(f"Updating registry with skill: {skill_name}")

    # Apply auto-versioning if enabled
    version_bump_reason = None
    if auto_version:
        logger.info("Auto-versioning enabled")
        manifest, version_bump_reason = apply_auto_version(manifest_path, manifest)
        if version_bump_reason:
            logger.info(f"Auto-version applied: {manifest.get('version')} - {version_bump_reason}")

    # Capture registry state before update for diff tracking
    registry_before = None
    try:
        if os.path.exists(REGISTRY_FILE):
            with open(REGISTRY_FILE, 'r') as f:
                registry_before = json.load(f)
    except Exception:
        pass  # Ignore errors reading before state

    def update_fn(registry_data):
        """Update function for safe_update_json."""
        # Ensure registry has proper structure
        if not registry_data or "skills" not in registry_data:
            registry_data = {
                "registry_version": REGISTRY_VERSION,
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "skills": []
            }

        # Remove existing entry if present
        registry_data["skills"] = [
            s for s in registry_data["skills"]
            if s.get("name") != skill_name
        ]

        # Prepare registry entry
        registry_entry = manifest.copy()

        # Add version bump metadata if auto-versioned
        if version_bump_reason:
            registry_entry["version_bump_reason"] = version_bump_reason

        # Ensure updated_at timestamp
        if "updated_at" not in registry_entry:
            registry_entry["updated_at"] = datetime.now(timezone.utc).isoformat()

        # Add new entry
        registry_data["skills"].append(registry_entry)

        # Update timestamp
        registry_data["generated_at"] = datetime.now(timezone.utc).isoformat()

        return registry_data

    # Default registry structure
    default_registry = {
        "registry_version": REGISTRY_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skills": []
    }

    try:
        # Capture telemetry with diff tracking
        with capture_execution(
            skill_name="registry.update",
            inputs={"manifest_path": manifest_path, "skill_name": skill_name},
            caller="cli"
        ) as ctx:
            # Use safe atomic update with file locking
            updated_registry = safe_update_json(REGISTRY_FILE, update_fn, default=default_registry)

            # Calculate diff for telemetry
            registry_diff = None
            if registry_before:
                skills_before = {s.get("name"): s for s in registry_before.get("skills", [])}
                skills_after = {s.get("name"): s for s in updated_registry.get("skills", [])}

                # Determine if this was an add, update, or no change
                if skill_name not in skills_before:
                    operation = "add"
                elif skills_before.get(skill_name) != skills_after.get(skill_name):
                    operation = "update"
                else:
                    operation = "no_change"

                registry_diff = {
                    "operation": operation,
                    "skill_name": skill_name,
                    "skills_before": len(skills_before),
                    "skills_after": len(skills_after),
                }

            # Add metadata to telemetry
            ctx.set_metadata(
                registry_path=REGISTRY_FILE,
                total_skills=len(updated_registry["skills"]),
                policy_enforced=True,
                diff=registry_diff,
            )

            result = {
                "status": "success",
                "updated": skill_name,
                "registry_path": REGISTRY_FILE,
                "total_skills": len(updated_registry["skills"]),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

            # Add auto-versioning info if applicable
            if version_bump_reason:
                result["auto_versioned"] = True
                result["version"] = manifest.get("version")
                result["version_bump_reason"] = version_bump_reason

            logger.info(f"✅ Successfully updated registry for: {skill_name}")
            return result

    except Exception as e:
        logger.error(f"Failed to update registry: {e}")
        raise RegistryError(f"Failed to update registry: {e}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: registry_update.py <path_to_skill.yaml> [--auto-version]"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    manifest_path = sys.argv[1]
    auto_version = "--auto-version" in sys.argv

    try:
        details = update_registry_data(manifest_path, auto_version=auto_version)
        response = build_response(
            True,
            path=details.get("registry_path", REGISTRY_FILE),
            errors=[],
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0)
    except RegistryError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=manifest_path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_info = format_error_response(e, include_traceback=True)
        response = build_response(
            False,
            path=manifest_path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
