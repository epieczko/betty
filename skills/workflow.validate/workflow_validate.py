#!/usr/bin/env python3
"""workflow_validate.py – Implementation of the workflow.validate Skill."""

import json
import os
import sys
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

import yaml
from pydantic import ValidationError as PydanticValidationError

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.errors import SkillValidationError, WorkflowError  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402
from betty.validation import ValidationError, validate_path  # noqa: E402
from betty.telemetry_integration import telemetry_tracked  # noqa: E402
from betty.models import WorkflowDefinition  # noqa: E402
from betty.config import REGISTRY_DIR  # noqa: E402
from betty.versioning import satisfies  # noqa: E402

logger = setup_logger(__name__)

REQUIRED_FIELDS = ["steps"]
# Steps can have either 'skill' or 'agent' (not both)
# For skill steps: 'skill', 'version', and 'args' are required
# For agent steps: 'agent' is required, 'input' is optional

SKILLS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "skills.json")
LOCKFILE_DIR = os.path.join(REGISTRY_DIR, "runs")


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


def _load_workflow(path: str) -> Dict[str, Any]:
    """Load a workflow YAML file into a dictionary."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except FileNotFoundError as exc:
        raise WorkflowError(f"Workflow file not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise SkillValidationError(f"Invalid YAML syntax: {exc}") from exc

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise SkillValidationError("Workflow root must be a mapping")

    return data


def _validate_required_fields(data: Dict[str, Any]) -> List[str]:
    """Validate presence of required top-level workflow fields."""
    errors: List[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def _load_skills_registry() -> Dict[str, Any]:
    """Load the skills registry from disk."""
    try:
        if not os.path.exists(SKILLS_REGISTRY_FILE):
            logger.warning(f"Skills registry not found at {SKILLS_REGISTRY_FILE}")
            return {"skills": []}

        with open(SKILLS_REGISTRY_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load skills registry: {e}")
        return {"skills": []}


def _resolve_skill_version(skill_name: str, version_constraint: str, registry: Dict[str, Any]) -> Optional[str]:
    """
    Resolve a skill version from the registry that satisfies the constraint.

    Args:
        skill_name: Name of the skill to resolve
        version_constraint: Version constraint (e.g., ">=1.0.0 <2.0.0")
        registry: Skills registry data

    Returns:
        Resolved version string, or None if no matching version found
    """
    matching_versions = []

    for skill in registry.get("skills", []):
        if skill.get("name") == skill_name:
            skill_version = skill.get("version")
            if skill_version and satisfies(skill_version, version_constraint):
                matching_versions.append(skill_version)

    if not matching_versions:
        return None

    # Return the latest version that satisfies the constraint
    # (assuming versions are stored in order, or we could sort them)
    return matching_versions[-1]


def _validate_steps(steps: Any) -> List[str]:
    """Validate the steps section of the workflow."""
    errors: List[str] = []

    if not isinstance(steps, list):
        errors.append("`steps` must be a list")
        return errors

    for index, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            errors.append(f"Step {index} must be a mapping")
            continue

        # Check if step has skill or agent field
        has_skill = "skill" in step
        has_agent = "agent" in step

        if not has_skill and not has_agent:
            errors.append(f"Step {index} must have either 'skill' or 'agent' field")
            continue

        if has_skill and has_agent:
            errors.append(f"Step {index} cannot have both 'skill' and 'agent' fields")
            continue

        # Validate skill steps
        if has_skill:
            skill_value = step.get("skill")
            if not isinstance(skill_value, str):
                errors.append(f"Step {index} 'skill' must be a string")

            # version field is required for skill steps
            if "version" not in step:
                errors.append(f"Step {index} missing 'version' constraint (required for skill steps)")
            else:
                version_value = step.get("version")
                if not isinstance(version_value, str):
                    errors.append(f"Step {index} 'version' must be a string")

            # args field is required for skill steps
            if "args" not in step:
                errors.append(f"Step {index} missing 'args' field (required for skill steps)")
            else:
                args_value = step.get("args")
                if not isinstance(args_value, list):
                    errors.append(f"Step {index} 'args' must be a list")

        # Validate agent steps
        if has_agent:
            agent_value = step.get("agent")
            if not isinstance(agent_value, str):
                errors.append(f"Step {index} 'agent' must be a string")

            # input field is optional for agent steps, but if present must be a string
            input_value = step.get("input")
            if input_value is not None and not isinstance(input_value, str):
                errors.append(f"Step {index} 'input' must be a string")

    return errors


def _validate_with_pydantic(data: Dict[str, Any]) -> List[str]:
    """
    Validate workflow data using Pydantic schema.

    Args:
        data: Workflow data dictionary

    Returns:
        List of validation errors (empty if valid)
    """
    errors: List[str] = []

    try:
        # Attempt Pydantic validation
        WorkflowDefinition.model_validate(data)
        logger.info("Pydantic schema validation passed")
    except PydanticValidationError as exc:
        logger.warning("Pydantic schema validation failed")
        # Convert Pydantic errors to human-readable messages
        for error in exc.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            message = error["msg"]
            error_type = error["type"]
            errors.append(f"Schema validation error at '{field}': {message} (type: {error_type})")

    return errors


def _resolve_versions_and_create_lockfile(
    workflow_name: str,
    workflow_data: Dict[str, Any],
    registry: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Resolve skill versions from registry and create a lockfile.

    Args:
        workflow_name: Name of the workflow
        workflow_data: Workflow definition data
        registry: Skills registry data

    Returns:
        Dictionary with resolved versions and lockfile path

    Raises:
        WorkflowError: If version resolution fails
    """
    resolved = []
    errors = []

    for index, step in enumerate(workflow_data.get("steps", []), start=1):
        if "skill" in step:
            skill_name = step.get("skill")
            version_constraint = step.get("version")

            if skill_name and version_constraint:
                resolved_version = _resolve_skill_version(skill_name, version_constraint, registry)

                if resolved_version:
                    resolved.append({
                        "skill": skill_name,
                        "version": resolved_version,
                        "constraint": version_constraint
                    })
                else:
                    errors.append(
                        f"Step {index}: No version of skill '{skill_name}' "
                        f"satisfies constraint '{version_constraint}'"
                    )

    if errors:
        raise WorkflowError(
            f"Version resolution failed for workflow '{workflow_name}':\n" +
            "\n".join(f"  - {err}" for err in errors)
        )

    # Create lockfile
    timestamp = datetime.now(timezone.utc).isoformat()
    lockfile_data = {
        "workflow": workflow_name,
        "timestamp": timestamp,
        "resolved": resolved
    }

    # Ensure lockfile directory exists
    os.makedirs(LOCKFILE_DIR, exist_ok=True)

    # Generate lockfile name
    lockfile_name = f"{timestamp.replace(':', '-').replace('.', '-')}.lock.json"
    lockfile_path = os.path.join(LOCKFILE_DIR, lockfile_name)

    # Write lockfile
    try:
        with open(lockfile_path, 'w') as f:
            json.dump(lockfile_data, f, indent=2)
        logger.info(f"Lockfile created at {lockfile_path}")
    except Exception as e:
        logger.error(f"Failed to create lockfile: {e}")
        raise WorkflowError(f"Failed to create lockfile: {e}")

    return {
        "resolved": resolved,
        "lockfile_path": lockfile_path,
        "lockfile_data": lockfile_data
    }


def validate_workflow(path: str) -> Dict[str, Any]:
    """
    Validate a workflow definition file.

    Validates workflow structure, version constraints, and resolves skill versions
    from the registry. On success, creates a lockfile under registry/runs/.

    Args:
        path: Path to workflow YAML file

    Returns:
        Validation result dictionary

    Raises:
        SkillValidationError: If validation fails
        WorkflowError: If version resolution fails
    """
    try:
        validate_path(path, must_exist=True)
    except ValidationError as exc:
        raise SkillValidationError(str(exc)) from exc

    workflow_data = _load_workflow(path)

    errors: List[str] = []

    # First, validate with Pydantic schema
    schema_errors = _validate_with_pydantic(workflow_data)
    errors.extend(schema_errors)

    # Then run existing validation for more specific checks
    errors.extend(_validate_required_fields(workflow_data))
    errors.extend(_validate_steps(workflow_data.get("steps", [])))

    if errors:
        status = "failed"
        result = {
            "valid": False,
            "errors": errors,
            "status": status,
            "path": path,
        }
        return result

    # If validation passed, resolve versions and create lockfile
    workflow_name = workflow_data.get("name", os.path.basename(path).replace(".yaml", ""))
    registry = _load_skills_registry()

    try:
        lockfile_info = _resolve_versions_and_create_lockfile(workflow_name, workflow_data, registry)

        result = {
            "valid": True,
            "errors": [],
            "status": "validated",
            "path": path,
            "lockfile": lockfile_info["lockfile_path"],
            "resolved_versions": lockfile_info["resolved"],
        }
    except WorkflowError as e:
        # Version resolution failed
        result = {
            "valid": False,
            "errors": [str(e)],
            "status": "failed",
            "path": path,
        }

    return result


@telemetry_tracked(skill_name="workflow.validate", caller="cli")
def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    if len(argv) != 1:
        message = "Usage: workflow_validate.py <workflow.yaml>"
        logger.error(message)
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1

    workflow_path = argv[0]

    try:
        result = validate_workflow(workflow_path)

        # Check if there are schema validation errors
        has_schema_errors = any("Schema validation error" in err for err in result.get("errors", []))

        details = result.copy()
        if not result.get("valid", False) and has_schema_errors:
            details["error"] = {
                "type": "SchemaError",
                "error": "SchemaError",
                "message": "Workflow schema validation failed",
                "details": {"errors": result.get("errors", [])}
            }

        response = build_response(
            result.get("valid", False),
            path=result.get("path", workflow_path),
            errors=result.get("errors", []),
            details=details,
        )
        print(json.dumps(response, indent=2))
        return 0 if response["ok"] else 1
    except (SkillValidationError, WorkflowError) as exc:
        logger.error("Validation failed: %s", exc)
        response = build_response(
            False,
            path=workflow_path,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc), "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1
    except Exception as exc:  # pragma: no cover - unexpected failures
        logger.exception("Unexpected error during workflow validation")
        response = build_response(
            False,
            path=workflow_path,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc)}},
        )
        print(json.dumps(response, indent=2))
        return 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main(sys.argv[1:]))
