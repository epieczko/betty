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


def validate_command_name(name: str) -> None:
    """
    Validate that a command name follows Betty's naming convention.

    Valid names:
    - Start with slash (/)
    - Followed by lowercase letter
    - Contain only lowercase letters, numbers, hyphens
    - Examples: /api-design, /api-validate, /workflow-run

    Args:
        name: Command name to validate

    Raises:
        ValidationError: If name is invalid
    """
    if not name:
        raise ValidationError("Command name cannot be empty")

    if not name.startswith("/"):
        raise ValidationError(
            f"Invalid command name: '{name}'. "
            "Command names must start with '/'"
        )

    # Remove leading slash for pattern matching
    name_without_slash = name[1:]

    if not re.match(r'^[a-z][a-z0-9-]*$', name_without_slash):
        raise ValidationError(
            f"Invalid command name: '{name}'. "
            "Must start with '/' followed by lowercase letter and contain only "
            "lowercase letters, numbers, and hyphens."
        )


def validate_hook_name(name: str) -> None:
    """
    Validate that a hook name follows Betty's naming convention.

    Valid names:
    - Start with lowercase letter
    - Contain only lowercase letters, numbers, hyphens, underscores
    - Examples: validate-openapi-spec, check-api-compatibility

    Args:
        name: Hook name to validate

    Raises:
        ValidationError: If name is invalid
    """
    if not name:
        raise ValidationError("Hook name cannot be empty")

    if not re.match(r'^[a-z][a-z0-9_-]*$', name):
        raise ValidationError(
            f"Invalid hook name: '{name}'. "
            "Must start with lowercase letter and contain only "
            "lowercase letters, numbers, hyphens, and underscores."
        )


def validate_command_execution_type(execution_type: str) -> None:
    """
    Validate that command execution type is valid.

    Valid types:
    - agent: Command delegates to an agent
    - skill: Command calls a skill directly
    - workflow: Command executes a workflow

    Args:
        execution_type: Execution type to validate

    Raises:
        ValidationError: If execution type is invalid
    """
    valid_types = ["agent", "skill", "workflow"]
    if execution_type not in valid_types:
        raise ValidationError(
            f"Invalid execution type: '{execution_type}'. "
            f"Must be one of: {', '.join(valid_types)}"
        )


def validate_hook_event(event: str) -> None:
    """
    Validate that hook event is valid.

    Valid events:
    - on_file_edit: Triggered when a file is edited
    - on_file_save: Triggered when a file is saved
    - on_commit: Triggered on git commit
    - on_push: Triggered on git push
    - on_tool_use: Triggered when a tool is used
    - on_agent_start: Triggered when an agent starts
    - on_workflow_end: Triggered when a workflow completes

    Args:
        event: Event type to validate

    Raises:
        ValidationError: If event is invalid
    """
    valid_events = [
        "on_file_edit", "on_file_save", "on_commit", "on_push",
        "on_tool_use", "on_agent_start", "on_workflow_end"
    ]
    if event not in valid_events:
        raise ValidationError(
            f"Invalid event: '{event}'. "
            f"Must be one of: {', '.join(valid_events)}"
        )
