#!/usr/bin/env python3
"""
command_define.py – Implementation of the command.define Skill
Validates command manifests and registers them in the Command Registry.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    BASE_DIR,
    REQUIRED_COMMAND_FIELDS,
    COMMANDS_REGISTRY_FILE,
    REGISTRY_FILE,
    AGENTS_REGISTRY_FILE,
    CommandExecutionType,
    CommandStatus
)
from betty.validation import (
    validate_path,
    validate_manifest_fields,
    validate_command_name,
    validate_version,
    validate_command_execution_type
)
from betty.logging_utils import setup_logger
from betty.errors import format_error_response
from betty.file_utils import atomic_write_json

logger = setup_logger(__name__)


class CommandValidationError(Exception):
    """Raised when command validation fails."""
    pass


class CommandRegistryError(Exception):
    """Raised when command registry operations fail."""
    pass


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Build standardized response dictionary.

    Args:
        ok: Whether operation succeeded
        path: Path to command manifest
        errors: List of error messages
        details: Additional details

    Returns:
        Response dictionary
    """
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "path": path,
    }

    if details is not None:
        response["details"] = details

    return response


def load_command_manifest(path: str) -> Dict[str, Any]:
    """
    Load and parse a command manifest from YAML file.

    Args:
        path: Path to command manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        CommandValidationError: If manifest cannot be loaded or parsed
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise CommandValidationError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise CommandValidationError(f"Failed to parse YAML: {e}")


def load_skill_registry() -> Dict[str, Any]:
    """
    Load skill registry for validation.

    Returns:
        Skill registry dictionary

    Raises:
        CommandValidationError: If registry cannot be loaded
    """
    try:
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        raise CommandValidationError(f"Skill registry not found: {REGISTRY_FILE}")
    except json.JSONDecodeError as e:
        raise CommandValidationError(f"Failed to parse skill registry: {e}")


def load_agent_registry() -> Dict[str, Any]:
    """
    Load agent registry for validation.

    Returns:
        Agent registry dictionary

    Raises:
        CommandValidationError: If registry cannot be loaded
    """
    try:
        with open(AGENTS_REGISTRY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        raise CommandValidationError(f"Agent registry not found: {AGENTS_REGISTRY_FILE}")
    except json.JSONDecodeError as e:
        raise CommandValidationError(f"Failed to parse agent registry: {e}")


def validate_execution_target(execution: Dict[str, Any]) -> List[str]:
    """
    Validate that the execution target exists in the appropriate registry.

    Args:
        execution: Execution configuration from manifest

    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    exec_type = execution.get("type")
    target = execution.get("target")

    if not target:
        errors.append("execution.target is required")
        return errors

    try:
        if exec_type == "skill":
            # Validate skill exists
            skill_registry = load_skill_registry()
            registered_skills = {skill["name"] for skill in skill_registry.get("skills", [])}
            if target not in registered_skills:
                errors.append(f"Skill '{target}' not found in skill registry")

        elif exec_type == "agent":
            # Validate agent exists
            agent_registry = load_agent_registry()
            registered_agents = {agent["name"] for agent in agent_registry.get("agents", [])}
            if target not in registered_agents:
                errors.append(f"Agent '{target}' not found in agent registry")

        elif exec_type == "workflow":
            # Validate workflow file exists
            workflow_path = os.path.join(BASE_DIR, "workflows", f"{target}.yaml")
            if not os.path.exists(workflow_path):
                errors.append(f"Workflow file not found: {workflow_path}")

    except CommandValidationError as e:
        errors.append(f"Could not validate target: {str(e)}")

    return errors


def validate_manifest(path: str) -> Dict[str, Any]:
    """
    Validate that a command manifest meets all requirements.

    Validation checks:
    1. Required fields are present
    2. Name format is valid
    3. Version format is valid
    4. Execution type is valid
    5. Execution target exists in appropriate registry
    6. Parameters are properly formatted (if present)

    Args:
        path: Path to command manifest file

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if manifest is valid
        - errors: List of validation errors (if any)
        - manifest: The parsed manifest (if valid)
        - path: Path to the manifest file
    """
    validate_path(path, must_exist=True)

    logger.info(f"Validating command manifest: {path}")

    errors = []

    # Load manifest
    try:
        manifest = load_command_manifest(path)
    except CommandValidationError as e:
        return {
            "valid": False,
            "errors": [str(e)],
            "path": path
        }

    # Check required fields
    missing = validate_manifest_fields(manifest, REQUIRED_COMMAND_FIELDS)
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")
        logger.warning(f"Missing required fields: {missing}")

    # If missing required fields, return early
    if errors:
        return {
            "valid": False,
            "errors": errors,
            "path": path
        }

    # Validate name format
    try:
        validate_command_name(manifest["name"])
    except Exception as e:
        errors.append(f"Invalid name: {str(e)}")
        logger.warning(f"Invalid name: {e}")

    # Validate version format
    try:
        validate_version(manifest["version"])
    except Exception as e:
        errors.append(f"Invalid version: {str(e)}")
        logger.warning(f"Invalid version: {e}")

    # Validate execution configuration
    execution = manifest.get("execution", {})
    if not isinstance(execution, dict):
        errors.append("execution must be an object")
    else:
        # Validate execution type
        exec_type = execution.get("type")
        if not exec_type:
            errors.append("execution.type is required")
        else:
            try:
                validate_command_execution_type(exec_type)
            except Exception as e:
                errors.append(f"Invalid execution.type: {str(e)}")
                logger.warning(f"Invalid execution type: {e}")

        # Validate execution target exists
        if exec_type:
            target_errors = validate_execution_target(execution)
            errors.extend(target_errors)

    # Validate status if present
    if "status" in manifest:
        valid_statuses = [s.value for s in CommandStatus]
        if manifest["status"] not in valid_statuses:
            errors.append(f"Invalid status: '{manifest['status']}'. Must be one of: {', '.join(valid_statuses)}")
            logger.warning(f"Invalid status: {manifest['status']}")

    # Validate parameters if present
    if "parameters" in manifest:
        params = manifest["parameters"]
        if not isinstance(params, list):
            errors.append("parameters must be an array")
        else:
            for i, param in enumerate(params):
                if not isinstance(param, dict):
                    errors.append(f"parameters[{i}] must be an object")
                    continue
                if "name" not in param:
                    errors.append(f"parameters[{i}] missing required field: name")
                if "type" not in param:
                    errors.append(f"parameters[{i}] missing required field: type")

    if errors:
        logger.warning(f"Validation failed with {len(errors)} error(s)")
        return {
            "valid": False,
            "errors": errors,
            "path": path
        }

    logger.info("✅ Command manifest validation passed")
    return {
        "valid": True,
        "errors": [],
        "path": path,
        "manifest": manifest
    }


def load_command_registry() -> Dict[str, Any]:
    """
    Load existing command registry.

    Returns:
        Command registry dictionary, or new empty registry if file doesn't exist
    """
    if not os.path.exists(COMMANDS_REGISTRY_FILE):
        logger.info("Command registry not found, creating new registry")
        return {
            "registry_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "commands": []
        }

    try:
        with open(COMMANDS_REGISTRY_FILE) as f:
            registry = json.load(f)
            logger.info(f"Loaded command registry with {len(registry.get('commands', []))} command(s)")
            return registry
    except json.JSONDecodeError as e:
        raise CommandRegistryError(f"Failed to parse command registry: {e}")


def update_command_registry(manifest: Dict[str, Any]) -> bool:
    """
    Add or update command in the command registry.

    Args:
        manifest: Validated command manifest

    Returns:
        True if registry was updated successfully

    Raises:
        CommandRegistryError: If registry update fails
    """
    logger.info(f"Updating command registry for: {manifest['name']}")

    # Load existing registry
    registry = load_command_registry()

    # Create registry entry
    entry = {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "execution": manifest["execution"],
        "parameters": manifest.get("parameters", []),
        "status": manifest.get("status", "draft"),
        "tags": manifest.get("tags", [])
    }

    # Check if command already exists
    commands = registry.get("commands", [])
    existing_index = None
    for i, command in enumerate(commands):
        if command["name"] == manifest["name"]:
            existing_index = i
            break

    if existing_index is not None:
        # Update existing command
        commands[existing_index] = entry
        logger.info(f"Updated existing command: {manifest['name']}")
    else:
        # Add new command
        commands.append(entry)
        logger.info(f"Added new command: {manifest['name']}")

    registry["commands"] = commands
    registry["generated_at"] = datetime.now(timezone.utc).isoformat()

    # Write registry back to disk atomically
    try:
        atomic_write_json(COMMANDS_REGISTRY_FILE, registry)
        logger.info(f"Command registry updated successfully")
        return True
    except Exception as e:
        raise CommandRegistryError(f"Failed to write command registry: {e}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: command_define.py <path_to_command.yaml>"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    path = sys.argv[1]

    try:
        # Validate manifest
        validation = validate_manifest(path)
        details = dict(validation)

        if validation.get("valid"):
            # Update registry
            try:
                registry_updated = update_command_registry(validation["manifest"])
                details["status"] = "registered"
                details["registry_updated"] = registry_updated
            except CommandRegistryError as e:
                logger.error(f"Registry update failed: {e}")
                details["status"] = "validated"
                details["registry_updated"] = False
                details["registry_error"] = str(e)

        # Build response
        response = build_response(
            bool(validation.get("valid")),
            path=path,
            errors=validation.get("errors", []),
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0 if response["ok"] else 1)

    except CommandValidationError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=path,
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
            path=path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
