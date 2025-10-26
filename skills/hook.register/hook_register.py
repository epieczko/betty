#!/usr/bin/env python3
"""
hook_register.py – Implementation of the hook.register Skill
Validates hook manifests and registers them in the Hook Registry.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pydantic import ValidationError as PydanticValidationError

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    BASE_DIR,
    REQUIRED_HOOK_FIELDS,
    HOOKS_REGISTRY_FILE,
    HookEvent,
    HookStatus
)
from betty.validation import (
    validate_path,
    validate_manifest_fields,
    validate_hook_name,
    validate_version,
    validate_hook_event
)
from betty.logging_utils import setup_logger
from betty.errors import format_error_response
from betty.models import HookManifest

logger = setup_logger(__name__)


class HookValidationError(Exception):
    """Raised when hook validation fails."""
    pass


class HookRegistryError(Exception):
    """Raised when hook registry operations fail."""
    pass


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Build standardized response dictionary.

    Args:
        ok: Whether operation succeeded
        path: Path to hook manifest
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


def load_hook_manifest(path: str) -> Dict[str, Any]:
    """
    Load and parse a hook manifest from YAML file.

    Args:
        path: Path to hook manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        HookValidationError: If manifest cannot be loaded or parsed
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise HookValidationError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise HookValidationError(f"Failed to parse YAML: {e}")


def validate_hook_schema(manifest: Dict[str, Any]) -> List[str]:
    """
    Validate hook manifest using Pydantic schema.

    Args:
        manifest: Hook manifest dictionary

    Returns:
        List of validation errors (empty if valid)
    """
    errors: List[str] = []

    try:
        HookManifest.model_validate(manifest)
        logger.info("Pydantic schema validation passed for hook manifest")
    except PydanticValidationError as exc:
        logger.warning("Pydantic schema validation failed for hook manifest")
        for error in exc.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            message = error["msg"]
            error_type = error["type"]
            errors.append(f"Schema validation error at '{field}': {message} (type: {error_type})")

    return errors


def validate_manifest(path: str) -> Dict[str, Any]:
    """
    Validate that a hook manifest meets all requirements.

    Validation checks:
    1. Required fields are present
    2. Name format is valid
    3. Version format is valid
    4. Event type is valid
    5. Command is specified
    6. Pattern is valid (if present)
    7. Blocking mode is boolean (if present)

    Args:
        path: Path to hook manifest file

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if manifest is valid
        - errors: List of validation errors (if any)
        - manifest: The parsed manifest (if valid)
        - path: Path to the manifest file
    """
    validate_path(path, must_exist=True)

    logger.info(f"Validating hook manifest: {path}")

    errors = []

    # Load manifest
    try:
        manifest = load_hook_manifest(path)
    except HookValidationError as e:
        return {
            "valid": False,
            "errors": [str(e)],
            "path": path
        }

    # Validate with Pydantic schema first
    schema_errors = validate_hook_schema(manifest)
    errors.extend(schema_errors)

    # Check required fields
    missing = validate_manifest_fields(manifest, REQUIRED_HOOK_FIELDS)
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
        validate_hook_name(manifest["name"])
    except Exception as e:
        errors.append(f"Invalid name: {str(e)}")
        logger.warning(f"Invalid name: {e}")

    # Validate version format
    try:
        validate_version(manifest["version"])
    except Exception as e:
        errors.append(f"Invalid version: {str(e)}")
        logger.warning(f"Invalid version: {e}")

    # Validate event type
    try:
        validate_hook_event(manifest["event"])
    except Exception as e:
        errors.append(f"Invalid event: {str(e)}")
        logger.warning(f"Invalid event: {e}")

    # Validate command is not empty
    command = manifest.get("command", "")
    if not command or not command.strip():
        errors.append("command cannot be empty")
        logger.warning("Empty command field")

    # Validate blocking if present
    if "blocking" in manifest:
        if not isinstance(manifest["blocking"], bool):
            errors.append("blocking must be a boolean (true/false)")
            logger.warning(f"Invalid blocking type: {type(manifest['blocking'])}")

    # Validate timeout if present
    if "timeout" in manifest:
        timeout = manifest["timeout"]
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            errors.append("timeout must be a positive number (in milliseconds)")
            logger.warning(f"Invalid timeout: {timeout}")

    # Validate status if present
    if "status" in manifest:
        valid_statuses = [s.value for s in HookStatus]
        if manifest["status"] not in valid_statuses:
            errors.append(f"Invalid status: '{manifest['status']}'. Must be one of: {', '.join(valid_statuses)}")
            logger.warning(f"Invalid status: {manifest['status']}")

    # Validate when.pattern if present
    if "when" in manifest:
        when = manifest["when"]
        if not isinstance(when, dict):
            errors.append("when must be an object")
        elif "pattern" in when:
            pattern = when["pattern"]
            if not pattern or not isinstance(pattern, str):
                errors.append("when.pattern must be a non-empty string")

    if errors:
        logger.warning(f"Validation failed with {len(errors)} error(s)")
        return {
            "valid": False,
            "errors": errors,
            "path": path
        }

    logger.info("✅ Hook manifest validation passed")
    return {
        "valid": True,
        "errors": [],
        "path": path,
        "manifest": manifest
    }


def load_hook_registry() -> Dict[str, Any]:
    """
    Load existing hook registry.

    Returns:
        Hook registry dictionary, or new empty registry if file doesn't exist
    """
    if not os.path.exists(HOOKS_REGISTRY_FILE):
        logger.info("Hook registry not found, creating new registry")
        return {
            "registry_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "hooks": []
        }

    try:
        with open(HOOKS_REGISTRY_FILE) as f:
            registry = json.load(f)
            logger.info(f"Loaded hook registry with {len(registry.get('hooks', []))} hook(s)")
            return registry
    except json.JSONDecodeError as e:
        raise HookRegistryError(f"Failed to parse hook registry: {e}")


def update_hook_registry(manifest: Dict[str, Any]) -> bool:
    """
    Add or update hook in the hook registry.

    Args:
        manifest: Validated hook manifest

    Returns:
        True if registry was updated successfully

    Raises:
        HookRegistryError: If registry update fails
    """
    logger.info(f"Updating hook registry for: {manifest['name']}")

    # Load existing registry
    registry = load_hook_registry()

    # Create registry entry
    entry = {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "event": manifest["event"],
        "command": manifest["command"],
        "when": manifest.get("when", {}),
        "blocking": manifest.get("blocking", False),
        "timeout": manifest.get("timeout", 30000),
        "on_failure": manifest.get("on_failure", "show_errors"),
        "status": manifest.get("status", "draft"),
        "tags": manifest.get("tags", [])
    }

    # Check if hook already exists
    hooks = registry.get("hooks", [])
    existing_index = None
    for i, hook in enumerate(hooks):
        if hook["name"] == manifest["name"]:
            existing_index = i
            break

    if existing_index is not None:
        # Update existing hook
        hooks[existing_index] = entry
        logger.info(f"Updated existing hook: {manifest['name']}")
    else:
        # Add new hook
        hooks.append(entry)
        logger.info(f"Added new hook: {manifest['name']}")

    registry["hooks"] = hooks
    registry["generated_at"] = datetime.now(timezone.utc).isoformat()

    # Write registry back to disk
    try:
        os.makedirs(os.path.dirname(HOOKS_REGISTRY_FILE), exist_ok=True)
        with open(HOOKS_REGISTRY_FILE, 'w') as f:
            json.dump(registry, f, indent=2)
        logger.info(f"Hook registry updated successfully")
        return True
    except Exception as e:
        raise HookRegistryError(f"Failed to write hook registry: {e}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: hook_register.py <path_to_hook.yaml>"
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
                registry_updated = update_hook_registry(validation["manifest"])
                details["status"] = "registered"
                details["registry_updated"] = registry_updated
            except HookRegistryError as e:
                logger.error(f"Registry update failed: {e}")
                details["status"] = "validated"
                details["registry_updated"] = False
                details["registry_error"] = str(e)
        else:
            # Check if there are schema validation errors
            has_schema_errors = any("Schema validation error" in err for err in validation.get("errors", []))
            if has_schema_errors:
                details["error"] = {
                    "type": "SchemaError",
                    "error": "SchemaError",
                    "message": "Hook manifest schema validation failed",
                    "details": {"errors": validation.get("errors", [])}
                }

        # Build response
        response = build_response(
            bool(validation.get("valid")),
            path=path,
            errors=validation.get("errors", []),
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0 if response["ok"] else 1)

    except HookValidationError as e:
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
