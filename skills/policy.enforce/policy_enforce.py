#!/usr/bin/env python3
"""
policy_enforce.py - Implementation of the policy.enforce Skill

Enforces policy rules for skill and agent manifests including:
- Naming conventions (lowercase, dot-separated, no spaces)
- Semantic versioning
- Permissions validation (only filesystem, network, read, write)
- Status lifecycle checks (draft, active, deprecated, archived)

Supports both single-file validation and batch mode.
"""

import os
import sys
import json
import yaml
import re
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, SKILLS_DIR, AGENTS_DIR
from betty.validation import validate_path, validate_version, ValidationError
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)

# Policy definitions
ALLOWED_PERMISSIONS = {"filesystem", "network", "read", "write"}
ALLOWED_STATUSES = {"draft", "active", "deprecated", "archived"}
VALID_NAME_PATTERN = r"^[a-z][a-z0-9.]*[a-z0-9]$"  # lowercase, dots allowed, no spaces


class PolicyViolation:
    """Represents a single policy violation."""

    def __init__(self, field: str, rule: str, message: str, severity: str = "error"):
        self.field = field
        self.rule = rule
        self.message = message
        self.severity = severity  # "error" or "warning"

    def to_dict(self) -> Dict[str, str]:
        return {
            "field": self.field,
            "rule": self.rule,
            "message": self.message,
            "severity": self.severity
        }


def load_manifest(path: str) -> Dict[str, Any]:
    """
    Load and parse a manifest from YAML file.

    Args:
        path: Path to manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        Exception: If manifest cannot be loaded or parsed
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise Exception(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise Exception(f"Failed to parse YAML: {e}")


def validate_name_format(name: str) -> Optional[PolicyViolation]:
    """
    Validate that name follows naming convention:
    - lowercase letters and numbers only
    - dots allowed for namespacing
    - no spaces, underscores, or hyphens (except in skill directory names for backwards compatibility)

    Args:
        name: Name to validate

    Returns:
        PolicyViolation if invalid, None if valid
    """
    if not name:
        return PolicyViolation(
            field="name",
            rule="naming_convention",
            message="Name cannot be empty"
        )

    # Check for spaces
    if ' ' in name:
        return PolicyViolation(
            field="name",
            rule="naming_convention",
            message=f"Name contains spaces: '{name}'. Names must not contain spaces."
        )

    # Check for uppercase
    if name != name.lower():
        return PolicyViolation(
            field="name",
            rule="naming_convention",
            message=f"Name contains uppercase letters: '{name}'. Names must be lowercase."
        )

    # Check format: lowercase, dots allowed, must start with letter
    if not re.match(VALID_NAME_PATTERN, name):
        return PolicyViolation(
            field="name",
            rule="naming_convention",
            message=f"Invalid name format: '{name}'. "
                   "Names must start with a lowercase letter, contain only lowercase letters, "
                   "numbers, and dots for namespacing, and end with a letter or number."
        )

    return None


def validate_version_format(version: str) -> Optional[PolicyViolation]:
    """
    Validate that version follows semantic versioning.

    Args:
        version: Version string to validate

    Returns:
        PolicyViolation if invalid, None if valid
    """
    try:
        validate_version(version)
        return None
    except ValidationError as e:
        return PolicyViolation(
            field="version",
            rule="semantic_versioning",
            message=str(e)
        )


def validate_permissions(manifest: Dict[str, Any], manifest_type: str) -> List[PolicyViolation]:
    """
    Validate that all permissions are in the allowed set.

    Args:
        manifest: Manifest dictionary
        manifest_type: "skill" or "agent"

    Returns:
        List of PolicyViolations for invalid permissions
    """
    violations = []

    # For skills, check entrypoints permissions
    if manifest_type == "skill":
        entrypoints = manifest.get("entrypoints", [])
        for idx, entrypoint in enumerate(entrypoints):
            permissions = entrypoint.get("permissions", [])
            for perm in permissions:
                # Handle both simple permissions and scoped permissions (e.g., "filesystem:read")
                base_perm = perm.split(':')[0] if ':' in perm else perm

                if base_perm not in ALLOWED_PERMISSIONS:
                    violations.append(PolicyViolation(
                        field=f"entrypoints[{idx}].permissions",
                        rule="allowed_permissions",
                        message=f"Invalid permission: '{perm}'. "
                               f"Only {', '.join(sorted(ALLOWED_PERMISSIONS))} are allowed."
                    ))

    # For agents, permissions might be in a different location
    # (checking if there's a permissions field at the top level)
    elif manifest_type == "agent":
        permissions = manifest.get("permissions", [])
        for perm in permissions:
            base_perm = perm.split(':')[0] if ':' in perm else perm

            if base_perm not in ALLOWED_PERMISSIONS:
                violations.append(PolicyViolation(
                    field="permissions",
                    rule="allowed_permissions",
                    message=f"Invalid permission: '{perm}'. "
                           f"Only {', '.join(sorted(ALLOWED_PERMISSIONS))} are allowed."
                ))

    return violations


def validate_status(status: str) -> Optional[PolicyViolation]:
    """
    Validate that status is one of the allowed values.

    Args:
        status: Status string to validate

    Returns:
        PolicyViolation if invalid, None if valid
    """
    if not status:
        return PolicyViolation(
            field="status",
            rule="allowed_status",
            message="Status field is required"
        )

    if status not in ALLOWED_STATUSES:
        return PolicyViolation(
            field="status",
            rule="allowed_status",
            message=f"Invalid status: '{status}'. "
                   f"Must be one of: {', '.join(sorted(ALLOWED_STATUSES))}"
        )

    return None


def validate_manifest_policies(path: str, manifest_type: str = None) -> Dict[str, Any]:
    """
    Validate a single manifest against all policy rules.

    Args:
        path: Path to manifest file
        manifest_type: "skill" or "agent" (auto-detected if None)

    Returns:
        Dictionary with validation results
    """
    violations = []

    try:
        # Validate path
        validate_path(path, must_exist=True)

        # Load manifest
        manifest = load_manifest(path)

        # Auto-detect manifest type if not specified
        if manifest_type is None:
            if "skill.yaml" in path or path.endswith(".yaml") and "skills/" in path:
                manifest_type = "skill"
            elif "agent.yaml" in path or path.endswith(".yaml") and "agents/" in path:
                manifest_type = "agent"
            else:
                # Try to detect from content
                if "entrypoints" in manifest or "inputs" in manifest:
                    manifest_type = "skill"
                elif "capabilities" in manifest or "reasoning_mode" in manifest:
                    manifest_type = "agent"
                else:
                    manifest_type = "unknown"

        # Validate name
        name = manifest.get("name")
        if name:
            violation = validate_name_format(name)
            if violation:
                violations.append(violation)
        else:
            violations.append(PolicyViolation(
                field="name",
                rule="required_field",
                message="Name field is required"
            ))

        # Validate version
        version = manifest.get("version")
        if version:
            violation = validate_version_format(version)
            if violation:
                violations.append(violation)
        else:
            violations.append(PolicyViolation(
                field="version",
                rule="required_field",
                message="Version field is required"
            ))

        # Validate permissions
        perm_violations = validate_permissions(manifest, manifest_type)
        violations.extend(perm_violations)

        # Validate status
        status = manifest.get("status")
        violation = validate_status(status)
        if violation:
            violations.append(violation)

        # Build result
        success = len(violations) == 0

        result = {
            "success": success,
            "path": path,
            "manifest_type": manifest_type,
            "violations": [v.to_dict() for v in violations],
            "violation_count": len(violations)
        }

        if success:
            result["message"] = "All policy checks passed"
        else:
            result["message"] = f"Found {len(violations)} policy violation(s)"

        return result

    except Exception as e:
        logger.error(f"Error validating manifest {path}: {e}")
        return {
            "success": False,
            "path": path,
            "error": str(e),
            "violations": [],
            "violation_count": 0
        }


def find_all_manifests() -> List[Tuple[str, str]]:
    """
    Find all skill and agent manifests in the repository.

    Returns:
        List of tuples (path, type) where type is "skill" or "agent"
    """
    manifests = []

    # Find skill manifests
    skills_dir = Path(SKILLS_DIR)
    if skills_dir.exists():
        for skill_yaml in skills_dir.glob("*/skill.yaml"):
            manifests.append((str(skill_yaml), "skill"))

    # Find agent manifests
    agents_dir = Path(AGENTS_DIR)
    if agents_dir.exists():
        for agent_yaml in agents_dir.glob("*/agent.yaml"):
            manifests.append((str(agent_yaml), "agent"))

    return manifests


def validate_batch(strict: bool = False) -> Dict[str, Any]:
    """
    Validate all manifests in batch mode.

    Args:
        strict: If True, treat warnings as errors

    Returns:
        Dictionary with batch validation results
    """
    manifests = find_all_manifests()

    if not manifests:
        return {
            "success": True,
            "mode": "batch",
            "message": "No manifests found to validate",
            "total_manifests": 0,
            "passed": 0,
            "failed": 0,
            "results": []
        }

    results = []
    passed = 0
    failed = 0

    for path, manifest_type in manifests:
        logger.info(f"Validating {manifest_type}: {path}")
        result = validate_manifest_policies(path, manifest_type)
        results.append(result)

        if result.get("success"):
            passed += 1
        else:
            failed += 1

    overall_success = failed == 0

    return {
        "success": overall_success,
        "mode": "batch",
        "message": f"Validated {len(manifests)} manifest(s): {passed} passed, {failed} failed",
        "total_manifests": len(manifests),
        "passed": passed,
        "failed": failed,
        "results": results
    }


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Enforce policy rules for skill and agent manifests"
    )
    parser.add_argument(
        "manifest_path",
        nargs="?",
        help="Path to manifest file to validate (omit for batch mode)"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Validate all manifests in skills/ and agents/ directories"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )

    args = parser.parse_args()

    try:
        # Batch mode
        if args.batch or not args.manifest_path:
            logger.info("Running in batch mode")
            result = validate_batch(strict=args.strict)
        else:
            # Single file mode
            logger.info(f"Validating single manifest: {args.manifest_path}")
            result = validate_manifest_policies(args.manifest_path)

        # Output JSON result
        print(json.dumps(result, indent=2))

        # Exit with appropriate code
        sys.exit(0 if result.get("success") else 1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_result = {
            "success": False,
            "error": str(e),
            "message": "Unexpected error during policy enforcement"
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
