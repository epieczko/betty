#!/usr/bin/env python3
"""
agent_define.py – Implementation of the agent.define Skill
Validates agent manifests (agent.yaml) and registers them in the Agent Registry.
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
    REQUIRED_AGENT_FIELDS,
    AGENTS_REGISTRY_FILE,
    REGISTRY_FILE,
    ReasoningMode,
    AgentStatus
)
from betty.validation import (
    validate_path,
    validate_manifest_fields,
    validate_agent_name,
    validate_version,
    validate_reasoning_mode,
    validate_skills_exist
)
from betty.logging_utils import setup_logger
from betty.errors import AgentValidationError, AgentRegistryError, format_error_response
from betty.file_utils import atomic_write_json

logger = setup_logger(__name__)


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Build standardized response dictionary.

    Args:
        ok: Whether operation succeeded
        path: Path to agent manifest
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


def load_agent_manifest(path: str) -> Dict[str, Any]:
    """
    Load and parse an agent manifest from YAML file.

    Args:
        path: Path to agent manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        AgentValidationError: If manifest cannot be loaded or parsed
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise AgentValidationError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise AgentValidationError(f"Failed to parse YAML: {e}")


def load_skill_registry() -> Dict[str, Any]:
    """
    Load skill registry for validation.

    Returns:
        Skill registry dictionary

    Raises:
        AgentValidationError: If registry cannot be loaded
    """
    try:
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        raise AgentValidationError(f"Skill registry not found: {REGISTRY_FILE}")
    except json.JSONDecodeError as e:
        raise AgentValidationError(f"Failed to parse skill registry: {e}")


def validate_manifest(path: str) -> Dict[str, Any]:
    """
    Validate that an agent manifest meets all requirements.

    Validation checks:
    1. Required fields are present
    2. Name format is valid
    3. Version format is valid
    4. Reasoning mode is valid
    5. All referenced skills exist in skill registry
    6. Capabilities list is non-empty
    7. Skills list is non-empty

    Args:
        path: Path to agent manifest file

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if manifest is valid
        - errors: List of validation errors (if any)
        - manifest: The parsed manifest (if valid)
        - path: Path to the manifest file
    """
    validate_path(path, must_exist=True)

    logger.info(f"Validating agent manifest: {path}")

    errors = []

    # Load manifest
    try:
        manifest = load_agent_manifest(path)
    except AgentValidationError as e:
        return {
            "valid": False,
            "errors": [str(e)],
            "path": path
        }

    # Check required fields
    missing = validate_manifest_fields(manifest, REQUIRED_AGENT_FIELDS)
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
        validate_agent_name(manifest["name"])
    except Exception as e:
        errors.append(f"Invalid name: {str(e)}")
        logger.warning(f"Invalid name: {e}")

    # Validate version format
    try:
        validate_version(manifest["version"])
    except Exception as e:
        errors.append(f"Invalid version: {str(e)}")
        logger.warning(f"Invalid version: {e}")

    # Validate reasoning mode
    try:
        validate_reasoning_mode(manifest["reasoning_mode"])
    except Exception as e:
        errors.append(f"Invalid reasoning_mode: {str(e)}")
        logger.warning(f"Invalid reasoning_mode: {e}")

    # Validate capabilities is non-empty
    capabilities = manifest.get("capabilities", [])
    if not capabilities or len(capabilities) == 0:
        errors.append("capabilities must contain at least one item")
        logger.warning("Empty capabilities list")

    # Validate skills_available is non-empty
    skills_available = manifest.get("skills_available", [])
    if not skills_available or len(skills_available) == 0:
        errors.append("skills_available must contain at least one item")
        logger.warning("Empty skills_available list")

    # Validate all skills exist in skill registry
    if skills_available:
        try:
            skill_registry = load_skill_registry()
            missing_skills = validate_skills_exist(skills_available, skill_registry)
            if missing_skills:
                errors.append(f"Skills not found in registry: {', '.join(missing_skills)}")
                logger.warning(f"Missing skills: {missing_skills}")
        except AgentValidationError as e:
            errors.append(f"Could not validate skills: {str(e)}")
            logger.error(f"Skill validation error: {e}")

    # Validate status if present
    if "status" in manifest:
        valid_statuses = [s.value for s in AgentStatus]
        if manifest["status"] not in valid_statuses:
            errors.append(f"Invalid status: '{manifest['status']}'. Must be one of: {', '.join(valid_statuses)}")
            logger.warning(f"Invalid status: {manifest['status']}")

    if errors:
        logger.warning(f"Validation failed with {len(errors)} error(s)")
        return {
            "valid": False,
            "errors": errors,
            "path": path
        }

    logger.info("✅ Agent manifest validation passed")
    return {
        "valid": True,
        "errors": [],
        "path": path,
        "manifest": manifest
    }


def load_agent_registry() -> Dict[str, Any]:
    """
    Load existing agent registry.

    Returns:
        Agent registry dictionary, or new empty registry if file doesn't exist
    """
    if not os.path.exists(AGENTS_REGISTRY_FILE):
        logger.info("Agent registry not found, creating new registry")
        return {
            "registry_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "agents": []
        }

    try:
        with open(AGENTS_REGISTRY_FILE) as f:
            registry = json.load(f)
            logger.info(f"Loaded agent registry with {len(registry.get('agents', []))} agent(s)")
            return registry
    except json.JSONDecodeError as e:
        raise AgentRegistryError(f"Failed to parse agent registry: {e}")


def update_agent_registry(manifest: Dict[str, Any]) -> bool:
    """
    Add or update agent in the agent registry.

    Args:
        manifest: Validated agent manifest

    Returns:
        True if registry was updated successfully

    Raises:
        AgentRegistryError: If registry update fails
    """
    logger.info(f"Updating agent registry for: {manifest['name']}")

    # Load existing registry
    registry = load_agent_registry()

    # Create registry entry
    entry = {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "reasoning_mode": manifest["reasoning_mode"],
        "skills_available": manifest["skills_available"],
        "capabilities": manifest.get("capabilities", []),
        "status": manifest.get("status", "draft"),
        "tags": manifest.get("tags", []),
        "dependencies": manifest.get("dependencies", [])
    }

    # Check if agent already exists
    agents = registry.get("agents", [])
    existing_index = None
    for i, agent in enumerate(agents):
        if agent["name"] == manifest["name"]:
            existing_index = i
            break

    if existing_index is not None:
        # Update existing agent
        agents[existing_index] = entry
        logger.info(f"Updated existing agent: {manifest['name']}")
    else:
        # Add new agent
        agents.append(entry)
        logger.info(f"Added new agent: {manifest['name']}")

    registry["agents"] = agents
    registry["generated_at"] = datetime.now(timezone.utc).isoformat()

    # Write registry back to disk atomically
    try:
        atomic_write_json(AGENTS_REGISTRY_FILE, registry)
        logger.info(f"Agent registry updated successfully")
        return True
    except Exception as e:
        raise AgentRegistryError(f"Failed to write agent registry: {e}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: agent_define.py <path_to_agent.yaml>"
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
                registry_updated = update_agent_registry(validation["manifest"])
                details["status"] = "registered"
                details["registry_updated"] = registry_updated
            except AgentRegistryError as e:
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

    except AgentValidationError as e:
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
