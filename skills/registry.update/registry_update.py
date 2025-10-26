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
from pydantic import ValidationError as PydanticValidationError

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REGISTRY_FILE, REGISTRY_VERSION, get_skill_handler_path, REGISTRY_DIR
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import RegistryError, VersionConflictError, format_error_response
from betty.telemetry_capture import capture_execution
from betty.models import SkillManifest
from betty.provenance import compute_hash, get_provenance_logger
from betty.versioning import is_monotonic_increase, parse_version

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


def validate_manifest_schema(manifest: Dict[str, Any]) -> None:
    """
    Validate manifest using Pydantic schema.

    Args:
        manifest: Manifest data dictionary

    Raises:
        RegistryError: If schema validation fails with type "SchemaError"
    """
    try:
        SkillManifest.model_validate(manifest)
        logger.info("Pydantic schema validation passed for manifest")
    except PydanticValidationError as exc:
        logger.error("Pydantic schema validation failed")
        # Convert Pydantic errors to human-readable messages
        error_messages = []
        for error in exc.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            message = error["msg"]
            error_type = error["type"]
            error_messages.append(f"Schema validation error at '{field}': {message} (type: {error_type})")

        error_detail = "\n".join(error_messages)
        raise RegistryError(
            f"Manifest schema validation failed:\n{error_detail}"
        ) from exc


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


def enforce_version_constraints(manifest: Dict[str, Any], registry_data: Dict[str, Any]) -> None:
    """
    Enforce semantic version constraints on manifest updates.

    Rules:
    - Version field is required on all entries
    - Cannot overwrite an active version with the same version number
    - Version must be monotonically increasing (no downgrades)

    Args:
        manifest: Skill manifest to validate
        registry_data: Current registry data

    Raises:
        RegistryError: If version field is missing
        VersionConflictError: If version constraints are violated
    """
    skill_name = manifest.get("name")
    new_version = manifest.get("version")

    # Rule 1: Require explicit version field
    if not new_version:
        raise RegistryError(
            f"Manifest for '{skill_name}' missing required 'version' field. "
            "All registry entries must have an explicit semantic version."
        )

    # Validate version format
    try:
        parse_version(new_version)
    except Exception as e:
        raise RegistryError(f"Invalid version format '{new_version}': {e}")

    # Find existing entry in registry
    existing_entry = None
    for skill in registry_data.get("skills", []):
        if skill.get("name") == skill_name:
            existing_entry = skill
            break

    if existing_entry:
        old_version = existing_entry.get("version")
        old_status = existing_entry.get("status", "draft")

        if old_version:
            # Rule 2: Refuse overwriting an active version with same version
            if new_version == old_version and old_status == "active":
                raise VersionConflictError(
                    f"Cannot overwrite active version {old_version} of '{skill_name}'. "
                    f"Active versions are immutable. Please increment the version number."
                )

            # Rule 3: Enforce monotonic SemVer order (no downgrades)
            if not is_monotonic_increase(old_version, new_version):
                # Allow same version if status is draft (for iterative development)
                if new_version == old_version and old_status == "draft":
                    logger.info(f"Allowing same version {new_version} for draft skill '{skill_name}'")
                else:
                    raise VersionConflictError(
                        f"Version downgrade or same version detected for '{skill_name}': "
                        f"{old_version} -> {new_version}. "
                        f"Versions must follow monotonic SemVer order (e.g., 0.2.0 < 0.3.0)."
                    )


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
        VersionConflictError: If version constraints are violated
    """
    # Validate path
    validate_path(manifest_path, must_exist=True)

    # Load manifest
    manifest = load_manifest(manifest_path)

    # Validate manifest schema with Pydantic
    validate_manifest_schema(manifest)

    # Enforce policy before updating registry
    policy_result = enforce_policy(manifest_path)

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

    # Enforce version constraints before update
    # Use registry_before if available, otherwise use default empty structure
    registry_for_validation = registry_before if registry_before else {
        "registry_version": REGISTRY_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skills": []
    }
    enforce_version_constraints(manifest, registry_for_validation)

    def update_fn(registry_data):
        """Update function for safe_update_json with provenance tracking."""
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

        # Compute content hash for provenance tracking
        content_hash = compute_hash(registry_data)
        registry_data["content_hash"] = content_hash

        # Log to provenance system
        try:
            provenance = get_provenance_logger()
            provenance.log_artifact(
                artifact_id="skills.json",
                version=registry_data.get("registry_version", "unknown"),
                content_hash=content_hash,
                artifact_type="registry",
                metadata={
                    "total_skills": len(registry_data.get("skills", [])),
                    "updated_skill": skill_name,
                    "skill_version": manifest.get("version", "unknown"),
                }
            )
            logger.info(f"Provenance logged: skills.json -> {content_hash[:8]}...")
        except Exception as e:
            logger.warning(f"Failed to log provenance: {e}")

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

    except VersionConflictError as e:
        # Re-raise version conflicts without wrapping
        logger.error(f"Version conflict: {e}")
        raise
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
    except (RegistryError, VersionConflictError) as e:
        logger.error(str(e))
        error_info = format_error_response(e)

        # Check if this is a schema validation error
        is_schema_error = "schema validation failed" in str(e).lower()
        if is_schema_error:
            error_info["type"] = "SchemaError"

        # Mark version conflicts with appropriate error type
        if isinstance(e, VersionConflictError):
            error_info["type"] = "VersionConflictError"

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
