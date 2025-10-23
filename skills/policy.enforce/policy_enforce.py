#!/usr/bin/env python3
"""policy_enforce.py – Implementation of the policy.enforce Skill."""

import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

import yaml

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.errors import SkillValidationError  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402
from betty.validation import ValidationError, validate_path  # noqa: E402

logger = setup_logger(__name__)

# Policy rules
VALID_STATUS_VALUES = {"draft", "active", "deprecated", "archived"}
VALID_PERMISSIONS = {"filesystem", "read", "write", "network", "execute"}
SKILL_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*$")


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


def _load_manifest(path: str) -> Dict[str, Any]:
    """Load a skill manifest YAML file into a dictionary."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except FileNotFoundError as exc:
        raise SkillValidationError(f"Manifest file not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise SkillValidationError(f"Invalid YAML syntax: {exc}") from exc

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise SkillValidationError("Manifest root must be a mapping")

    return data


def _validate_skill_naming(name: str) -> List[str]:
    """
    Validate skill naming convention.

    Rules:
    - Must be lowercase
    - Must use dot notation (e.g., skill.name)
    - Must start with a letter
    - Can contain letters, numbers, and dots
    """
    errors: List[str] = []

    if not name:
        errors.append("Skill name cannot be empty")
        return errors

    if not SKILL_NAME_PATTERN.match(name):
        errors.append(
            f"Skill name '{name}' violates naming policy. "
            "Must be lowercase with dot notation (e.g., 'skill.name'). "
            "Only letters, numbers, and dots allowed. Must start with a letter."
        )

    # Additional check: recommend using at least one dot for namespacing
    if "." not in name:
        logger.warning(
            f"Skill name '{name}' doesn't use dot notation for namespacing. "
            "Consider using format 'category.name' for better organization."
        )

    return errors


def _validate_status(status: str) -> List[str]:
    """
    Validate status value.

    Rules:
    - Must be one of: draft, active, deprecated, archived
    """
    errors: List[str] = []

    if not status:
        errors.append("Status field is required")
        return errors

    if status not in VALID_STATUS_VALUES:
        errors.append(
            f"Invalid status '{status}'. "
            f"Must be one of: {', '.join(sorted(VALID_STATUS_VALUES))}"
        )

    return errors


def _validate_permissions(entrypoints: List[Dict[str, Any]]) -> List[str]:
    """
    Validate permissions for all entrypoints.

    Rules:
    - Permissions must be from allowed set: filesystem, read, write, network, execute
    - Warn about potentially risky permission combinations
    """
    errors: List[str] = []

    if not isinstance(entrypoints, list):
        errors.append("Entrypoints must be a list")
        return errors

    for idx, entrypoint in enumerate(entrypoints, start=1):
        if not isinstance(entrypoint, dict):
            errors.append(f"Entrypoint {idx} must be a mapping")
            continue

        permissions = entrypoint.get("permissions", [])

        if not isinstance(permissions, list):
            errors.append(f"Entrypoint {idx} permissions must be a list")
            continue

        # Validate each permission
        for permission in permissions:
            if permission not in VALID_PERMISSIONS:
                errors.append(
                    f"Entrypoint {idx} has invalid permission '{permission}'. "
                    f"Must be one of: {', '.join(sorted(VALID_PERMISSIONS))}"
                )

        # Check for risky permission combinations
        if "network" in permissions and "write" in permissions and "filesystem" in permissions:
            logger.warning(
                f"Entrypoint {idx} has risky permission combination: "
                "network + write + filesystem. Ensure this skill requires all three."
            )

        # Check for write without read
        if "write" in permissions and "filesystem" not in permissions:
            logger.warning(
                f"Entrypoint {idx} has 'write' permission without 'filesystem'. "
                "This may be intentional but is unusual."
            )

    return errors


def enforce_policy(manifest_path: str) -> Dict[str, Any]:
    """
    Enforce policy rules on a skill manifest.

    Checks:
    1. Skill naming convention (lowercase, dot notation)
    2. Status values (draft|active|deprecated|archived)
    3. Permissions (filesystem, read, write, network, execute)

    Args:
        manifest_path: Path to skill.yaml manifest

    Returns:
        Dict with validation results
    """
    try:
        validate_path(manifest_path, must_exist=True)
    except ValidationError as exc:
        raise SkillValidationError(str(exc)) from exc

    manifest = _load_manifest(manifest_path)

    errors: List[str] = []
    warnings: List[str] = []

    # Validate skill name
    name = manifest.get("name")
    if name:
        errors.extend(_validate_skill_naming(name))
    else:
        errors.append("Manifest missing required 'name' field")

    # Validate status
    status = manifest.get("status")
    if status:
        errors.extend(_validate_status(status))
    else:
        errors.append("Manifest missing required 'status' field")

    # Validate permissions
    entrypoints = manifest.get("entrypoints", [])
    errors.extend(_validate_permissions(entrypoints))

    policy_status = "compliant" if not errors else "violation"
    result = {
        "compliant": not errors,
        "errors": errors,
        "warnings": warnings,
        "status": policy_status,
        "path": manifest_path,
        "manifest": {
            "name": name,
            "status": status,
            "version": manifest.get("version"),
        },
    }

    return result


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    if len(argv) != 1:
        message = "Usage: policy_enforce.py <skill.yaml>"
        logger.error(message)
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1

    manifest_path = argv[0]

    try:
        result = enforce_policy(manifest_path)
        response = build_response(
            result.get("compliant", False),
            path=result.get("path", manifest_path),
            errors=result.get("errors", []),
            details=result,
        )
        print(json.dumps(response, indent=2))
        return 0 if response["ok"] else 1
    except SkillValidationError as exc:
        logger.error("Policy enforcement failed: %s", exc)
        response = build_response(
            False,
            path=manifest_path,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc), "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1
    except Exception as exc:  # pragma: no cover - unexpected failures
        logger.exception("Unexpected error during policy enforcement")
        response = build_response(
            False,
            path=manifest_path,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc)}},
        )
        print(json.dumps(response, indent=2))
        return 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main(sys.argv[1:]))
