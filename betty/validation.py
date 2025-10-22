"""
Input validation utilities for Betty Framework.
"""

import re
import os
from typing import Optional, List, Dict, Any


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_skill_name(name: str) -> None:
    """
    Validate that a skill name follows Betty's naming convention.

    Valid names:
    - Start with lowercase letter
    - Contain only lowercase letters, numbers, dots, hyphens, underscores
    - Examples: skill.create, registry.update, runtime-execute

    Args:
        name: Skill name to validate

    Raises:
        ValidationError: If name is invalid
    """
    if not name:
        raise ValidationError("Skill name cannot be empty")

    if not re.match(r'^[a-z][a-z0-9._-]*$', name):
        raise ValidationError(
            f"Invalid skill name: '{name}'. "
            "Must start with lowercase letter and contain only "
            "lowercase letters, numbers, dots, hyphens, and underscores."
        )


def validate_path(path: str, must_exist: bool = False) -> None:
    """
    Validate a file path.

    Checks for:
    - Path traversal attacks (../)
    - Null bytes
    - Optionally checks if path exists

    Args:
        path: Path to validate
        must_exist: If True, raise error if path doesn't exist

    Raises:
        ValidationError: If path is invalid or doesn't exist when required
    """
    if not path:
        raise ValidationError("Path cannot be empty")

    # Check for path traversal
    if ".." in path:
        raise ValidationError(f"Path traversal detected in: {path}")

    # Check for null bytes
    if "\x00" in path:
        raise ValidationError(f"Null byte detected in path: {path}")

    # Check if path exists if required
    if must_exist and not os.path.exists(path):
        raise ValidationError(f"Path does not exist: {path}")


def validate_manifest_fields(manifest: Dict[str, Any], required_fields: List[str]) -> List[str]:
    """
    Validate that a manifest contains all required fields.

    Args:
        manifest: Manifest dictionary to validate
        required_fields: List of required field names

    Returns:
        List of missing fields (empty if all required fields are present)
    """
    if not isinstance(manifest, dict):
        raise ValidationError("Manifest must be a dictionary")

    missing = [field for field in required_fields if field not in manifest]
    return missing


def validate_version(version: str) -> None:
    """
    Validate that a version string follows semantic versioning.

    Args:
        version: Version string (e.g., "1.0.0", "0.1.0-alpha")

    Raises:
        ValidationError: If version is invalid
    """
    if not version:
        raise ValidationError("Version cannot be empty")

    # Basic semver pattern
    pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$'
    if not re.match(pattern, version):
        raise ValidationError(
            f"Invalid version: '{version}'. "
            "Must follow semantic versioning (e.g., 1.0.0, 0.1.0-alpha)"
        )
