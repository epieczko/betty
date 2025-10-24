#!/usr/bin/env python3
"""
registry.diff - Compare current and previous versions of skills/agents.

This skill compares a skill or agent manifest against its registry entry
to detect changes and determine appropriate actions.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime, timezone
from packaging import version as version_parser

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Betty framework imports
from betty.config import BASE_DIR, REGISTRY_DIR
from betty.file_utils import safe_read_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import RegistryError, format_error_response

logger = setup_logger(__name__)

SKILLS_REGISTRY = os.path.join(REGISTRY_DIR, "skills.json")
AGENTS_REGISTRY = os.path.join(REGISTRY_DIR, "agents.json")


def build_response(
    ok: bool,
    path: str,
    errors: Optional[List[str]] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Standard response format used across all skills."""
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
    """Load YAML manifest file with error handling."""
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        if not manifest:
            raise RegistryError(f"Empty manifest file: {path}")
        return manifest
    except FileNotFoundError:
        raise RegistryError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise RegistryError(f"Invalid YAML in manifest: {e}")


def determine_manifest_type(manifest: Dict[str, Any]) -> str:
    """Determine if manifest is a skill or agent based on fields."""
    if "entrypoints" in manifest or "handler" in manifest:
        return "skill"
    elif "capabilities" in manifest or "reasoning_mode" in manifest:
        return "agent"
    else:
        # Default to skill if unclear
        return "skill"


def find_registry_entry(name: str, manifest_type: str) -> Optional[Dict[str, Any]]:
    """Find existing entry in the appropriate registry."""
    registry_file = SKILLS_REGISTRY if manifest_type == "skill" else AGENTS_REGISTRY

    if not os.path.exists(registry_file):
        logger.warning(f"Registry file not found: {registry_file}")
        return None

    registry = safe_read_json(registry_file, default={})
    entries_key = "skills" if manifest_type == "skill" else "agents"
    entries = registry.get(entries_key, [])

    for entry in entries:
        if entry.get("name") == name:
            return entry

    return None


def compare_versions(current: str, previous: str) -> str:
    """
    Compare semantic versions.

    Returns:
        "upgrade" if current > previous
        "downgrade" if current < previous
        "same" if current == previous
    """
    try:
        curr_ver = version_parser.parse(current)
        prev_ver = version_parser.parse(previous)

        if curr_ver > prev_ver:
            return "upgrade"
        elif curr_ver < prev_ver:
            return "downgrade"
        else:
            return "same"
    except Exception as e:
        logger.warning(f"Error comparing versions: {e}")
        return "unknown"


def get_permissions(manifest: Dict[str, Any]) -> set:
    """Extract permissions from manifest."""
    permissions = set()

    # For skills, permissions are in entrypoints
    if "entrypoints" in manifest:
        for ep in manifest["entrypoints"]:
            if "permissions" in ep:
                permissions.update(ep["permissions"])

    # For agents, might have permissions at top level
    if "permissions" in manifest:
        perms = manifest["permissions"]
        if isinstance(perms, list):
            permissions.update(perms)

    return permissions


def detect_removed_fields(current: Dict[str, Any], previous: Dict[str, Any]) -> List[str]:
    """Detect fields that were removed from the manifest."""
    removed = []

    # Check top-level fields
    for key in previous:
        if key not in current:
            removed.append(key)

    # Check nested structures like inputs, outputs
    for list_field in ["inputs", "outputs", "dependencies", "capabilities", "skills_available"]:
        if list_field in previous and list_field in current:
            prev_list = previous[list_field] if isinstance(previous[list_field], list) else []
            curr_list = current[list_field] if isinstance(current[list_field], list) else []

            # For simple lists (strings), use set comparison
            if prev_list and all(isinstance(x, (str, int, float, bool)) for x in prev_list):
                prev_items = set(prev_list)
                curr_items = set(curr_list)
                removed_items = prev_items - curr_items
                if removed_items:
                    removed.append(f"{list_field}: {', '.join(str(x) for x in removed_items)}")
            # For complex lists (dicts), compare by key fields like 'name'
            elif prev_list and all(isinstance(x, dict) for x in prev_list):
                prev_names = {item.get('name', item.get('command', str(item))) for item in prev_list}
                curr_names = {item.get('name', item.get('command', str(item))) for item in curr_list}
                removed_names = prev_names - curr_names
                if removed_names:
                    removed.append(f"{list_field}: {', '.join(removed_names)}")

    return removed


def analyze_diff(
    manifest: Dict[str, Any],
    registry_entry: Optional[Dict[str, Any]],
    manifest_type: str
) -> Tuple[str, str, List[str], Dict[str, Any], List[str], bool]:
    """
    Analyze differences between current manifest and registry entry.

    Returns:
        (diff_type, required_action, suggestions, details, changed_fields, breaking)
    """
    name = manifest.get("name", "unknown")
    current_version = manifest.get("version", "0.0.0")
    changed_fields: List[str] = []
    breaking = False

    # Case 1: New entry (not in registry)
    if registry_entry is None:
        return (
            "new",
            "register",
            [f"New {manifest_type} '{name}' ready for registration"],
            {
                "name": name,
                "version": current_version,
                "is_new": True
            },
            [],  # No changed fields for new entries
            False  # Not breaking for new entries
        )

    # Extract previous values
    previous_version = registry_entry.get("version", "0.0.0")
    version_comparison = compare_versions(current_version, previous_version)

    # Track version changes
    if version_comparison != "same":
        changed_fields.append("version")

    # Detect permission changes
    current_perms = get_permissions(manifest)
    previous_perms = get_permissions(registry_entry)
    added_perms = current_perms - previous_perms
    removed_perms = previous_perms - current_perms
    permission_changed = bool(added_perms or removed_perms)

    if permission_changed:
        changed_fields.append("permissions")

    # Detect removed fields
    removed_fields = detect_removed_fields(manifest, registry_entry)

    # Track field removals in changed_fields
    for field in removed_fields:
        # Extract field name (e.g., "inputs: ..." -> "inputs")
        field_name = field.split(":")[0] if ":" in field else field
        if field_name not in changed_fields:
            changed_fields.append(field_name)

    # Detect status changes
    current_status = manifest.get("status", "draft")
    previous_status = registry_entry.get("status", "draft")
    status_changed = current_status != previous_status

    if status_changed:
        changed_fields.append("status")

    # Check for description changes
    if manifest.get("description") != registry_entry.get("description"):
        changed_fields.append("description")

    # Check for other field changes based on manifest type
    if manifest_type == "skill":
        # Check inputs
        if json.dumps(manifest.get("inputs", []), sort_keys=True) != json.dumps(registry_entry.get("inputs", []), sort_keys=True):
            if "inputs" not in changed_fields:
                changed_fields.append("inputs")
        # Check outputs
        if json.dumps(manifest.get("outputs", []), sort_keys=True) != json.dumps(registry_entry.get("outputs", []), sort_keys=True):
            if "outputs" not in changed_fields:
                changed_fields.append("outputs")
        # Check entrypoints
        if json.dumps(manifest.get("entrypoints", []), sort_keys=True) != json.dumps(registry_entry.get("entrypoints", []), sort_keys=True):
            if "entrypoints" not in changed_fields:
                changed_fields.append("entrypoints")
    elif manifest_type == "agent":
        # Check capabilities
        if json.dumps(manifest.get("capabilities", []), sort_keys=True) != json.dumps(registry_entry.get("capabilities", []), sort_keys=True):
            if "capabilities" not in changed_fields:
                changed_fields.append("capabilities")
        # Check skills_available
        if json.dumps(manifest.get("skills_available", []), sort_keys=True) != json.dumps(registry_entry.get("skills_available", []), sort_keys=True):
            if "skills_available" not in changed_fields:
                changed_fields.append("skills_available")
        # Check reasoning_mode
        if manifest.get("reasoning_mode") != registry_entry.get("reasoning_mode"):
            changed_fields.append("reasoning_mode")

    # Check dependencies
    if json.dumps(manifest.get("dependencies", []), sort_keys=True) != json.dumps(registry_entry.get("dependencies", []), sort_keys=True):
        if "dependencies" not in changed_fields:
            changed_fields.append("dependencies")

    # Check tags
    if json.dumps(sorted(manifest.get("tags", []))) != json.dumps(sorted(registry_entry.get("tags", []))):
        if "tags" not in changed_fields:
            changed_fields.append("tags")

    # Build details
    details = {
        "name": name,
        "current_version": current_version,
        "previous_version": previous_version,
        "version_comparison": version_comparison,
        "permission_changed": permission_changed,
        "added_permissions": list(added_perms),
        "removed_permissions": list(removed_perms),
        "removed_fields": removed_fields,
        "status_changed": status_changed,
        "current_status": current_status,
        "previous_status": previous_status
    }

    suggestions = []

    # Determine diff type and required action

    # Case 2: Version downgrade (breaking change)
    if version_comparison == "downgrade":
        breaking = True
        return (
            "version_downgrade",
            "reject",
            [
                f"Version downgrade detected: {previous_version} -> {current_version}",
                "Version downgrades are not permitted",
                f"Suggested action: Restore version to at least {previous_version}"
            ],
            details,
            changed_fields,
            breaking
        )

    # Case 3: Removed fields without version bump (breaking change)
    if removed_fields and version_comparison == "same":
        breaking = True
        suggestions.extend([
            f"Fields removed without version bump: {', '.join(removed_fields)}",
            "Removing fields requires a version bump",
            f"Suggested version: {increment_version(current_version, 'minor')}"
        ])
        return (
            "breaking_change",
            "reject",
            suggestions,
            details,
            changed_fields,
            breaking
        )

    # Case 4: Permission changes
    if permission_changed:
        if removed_perms and version_comparison == "same":
            breaking = True
            suggestions.extend([
                f"Permissions removed without version bump: {', '.join(removed_perms)}",
                f"Suggested version: {increment_version(current_version, 'minor')}"
            ])

        if added_perms:
            suggestions.append(f"New permissions added: {', '.join(added_perms)}")
            suggestions.append("Review: Ensure new permissions are necessary and documented")

        return (
            "permission_change",
            "review",
            suggestions if suggestions else [f"Permission changes detected in {name}"],
            details,
            changed_fields,
            breaking
        )

    # Case 5: Status change to deprecated/archived without version bump
    if status_changed and current_status in ["deprecated", "archived"] and version_comparison == "same":
        suggestions.extend([
            f"Status changed to '{current_status}' without version bump",
            f"Suggested version: {increment_version(current_version, 'minor')}"
        ])
        return (
            "status_change",
            "review",
            suggestions,
            details,
            changed_fields,
            breaking
        )

    # Case 6: Version bump (normal change)
    if version_comparison == "upgrade":
        suggestions.append(f"Version upgraded: {previous_version} -> {current_version}")
        if not permission_changed and not removed_fields:
            suggestions.append("Clean version bump with no breaking changes")
        return (
            "version_bump",
            "register",
            suggestions,
            details,
            changed_fields,
            breaking
        )

    # Case 7: No significant changes
    if version_comparison == "same" and not permission_changed and not removed_fields and not status_changed:
        return (
            "no_change",
            "skip",
            [f"No significant changes detected in {name}"],
            details,
            changed_fields,
            breaking
        )

    # Case 8: Changes without version bump (needs review)
    suggestions.extend([
        "Changes detected without version bump",
        f"Current version: {current_version}",
        f"Suggested version: {increment_version(current_version, 'patch')}"
    ])
    return (
        "needs_version_bump",
        "review",
        suggestions,
        details,
        changed_fields,
        breaking
    )


def increment_version(version_str: str, bump_type: str = "patch") -> str:
    """Increment semantic version."""
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
    except Exception:
        return version_str


def diff_manifest(manifest_path: str) -> Dict[str, Any]:
    """
    Compare manifest against registry entry.

    Args:
        manifest_path: Path to skill.yaml or agent.yaml

    Returns:
        Dictionary with diff analysis
    """
    # Validate input
    validate_path(manifest_path, must_exist=True)

    # Load manifest
    logger.info(f"Loading manifest: {manifest_path}")
    manifest = load_manifest(manifest_path)

    # Determine type
    manifest_type = determine_manifest_type(manifest)
    logger.info(f"Detected manifest type: {manifest_type}")

    # Get name
    name = manifest.get("name")
    if not name:
        raise RegistryError("Manifest missing required 'name' field")

    # Find registry entry
    registry_entry = find_registry_entry(name, manifest_type)

    # Analyze differences
    diff_type, required_action, suggestions, details, changed_fields, breaking = analyze_diff(
        manifest, registry_entry, manifest_type
    )

    # Build result
    result = {
        "manifest_path": manifest_path,
        "manifest_type": manifest_type,
        "diff_type": diff_type,
        "required_action": required_action,
        "changed_fields": changed_fields,
        "breaking": breaking,
        "suggestions": suggestions,
        "details": details,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    logger.info(f"Diff analysis complete: {diff_type} -> {required_action} (breaking: {breaking}, changed: {changed_fields})")

    return result


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: registry_diff.py <manifest_path>"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={
                "error": {
                    "error": "UsageError",
                    "message": message,
                    "details": {
                        "usage": "registry_diff.py <path/to/skill.yaml or agent.yaml>"
                    }
                }
            },
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    try:
        manifest_path = sys.argv[1]
        result = diff_manifest(manifest_path)

        # Determine exit code based on required action
        should_reject = result["required_action"] == "reject"
        exit_code = 1 if should_reject else 0

        response = build_response(
            ok=not should_reject,
            path=manifest_path,
            errors=result["suggestions"] if should_reject else [],
            details=result
        )

        # Print formatted output
        print(json.dumps(response, indent=2))

        # Also print human-readable summary
        print("\n" + "="*60, file=sys.stderr)
        print(f"Registry Diff Analysis", file=sys.stderr)
        print("="*60, file=sys.stderr)
        print(f"Manifest: {manifest_path}", file=sys.stderr)
        print(f"Type: {result['manifest_type']}", file=sys.stderr)
        print(f"Diff Type: {result['diff_type']}", file=sys.stderr)
        print(f"Required Action: {result['required_action']}", file=sys.stderr)
        print(f"Breaking: {result['breaking']}", file=sys.stderr)
        if result['changed_fields']:
            print(f"Changed Fields: {', '.join(result['changed_fields'])}", file=sys.stderr)
        print("\nSuggestions:", file=sys.stderr)
        for suggestion in result["suggestions"]:
            print(f"  • {suggestion}", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)

        sys.exit(exit_code)

    except RegistryError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=manifest_path if len(sys.argv) > 1 else "",
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        error_info = format_error_response(e, include_traceback=True)
        response = build_response(
            False,
            path=manifest_path if len(sys.argv) > 1 else "",
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
