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


def validate_agent_name(name: str) -> None:
    """
    Validate that an agent name follows Betty's naming convention.

    Valid names:
    - Start with lowercase letter
    - Contain only lowercase letters, numbers, dots, hyphens, underscores
    - Examples: api.designer, compliance.checker, data-migrator

    Args:
        name: Agent name to validate

    Raises:
        ValidationError: If name is invalid
    """
    if not name:
        raise ValidationError("Agent name cannot be empty")

    if not re.match(r'^[a-z][a-z0-9._-]*$', name):
        raise ValidationError(
            f"Invalid agent name: '{name}'. "
            "Must start with lowercase letter and contain only "
            "lowercase letters, numbers, dots, hyphens, and underscores."
        )


def validate_reasoning_mode(mode: str) -> None:
    """
    Validate that reasoning mode is valid.

    Valid modes:
    - iterative: Agent can retry with feedback
    - oneshot: Agent executes once without retry

    Args:
        mode: Reasoning mode to validate

    Raises:
        ValidationError: If mode is invalid
    """
    valid_modes = ["iterative", "oneshot"]
    if mode not in valid_modes:
        raise ValidationError(
            f"Invalid reasoning_mode: '{mode}'. "
            f"Must be one of: {', '.join(valid_modes)}"
        )


def validate_skills_exist(skills: List[str], skill_registry: Dict[str, Any]) -> List[str]:
    """
    Validate that all skills exist in the skill registry.

    Args:
        skills: List of skill names to validate
        skill_registry: Skill registry dictionary

    Returns:
        List of missing skills (empty if all skills exist)
    """
    if not skills:
        return []

    # Extract skill names from registry
    registered_skills = {skill["name"] for skill in skill_registry.get("skills", [])}

    # Find missing skills
    missing = [skill for skill in skills if skill not in registered_skills]
    return missing
