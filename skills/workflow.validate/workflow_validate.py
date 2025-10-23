#!/usr/bin/env python3
"""workflow_validate.py – Implementation of the workflow.validate Skill."""

import json
import os
import sys
from typing import Any, Dict, List, Optional

import yaml

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.errors import SkillValidationError, WorkflowError  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402
from betty.validation import ValidationError, validate_path  # noqa: E402

logger = setup_logger(__name__)

REQUIRED_FIELDS = ["steps"]
# Steps can have either 'skill' or 'agent' (not both)
# For skill steps: 'skill' and 'args' are required
# For agent steps: 'agent' is required, 'input' is optional


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


def validate_workflow(path: str) -> Dict[str, Any]:
    """Validate a workflow definition file."""
    try:
        validate_path(path, must_exist=True)
    except ValidationError as exc:
        raise SkillValidationError(str(exc)) from exc

    workflow_data = _load_workflow(path)

    errors: List[str] = []
    errors.extend(_validate_required_fields(workflow_data))
    errors.extend(_validate_steps(workflow_data.get("steps", [])))

    status = "validated" if not errors else "failed"
    result = {
        "valid": not errors,
        "errors": errors,
        "status": status,
        "path": path,
    }

    return result


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
        response = build_response(
            result.get("valid", False),
            path=result.get("path", workflow_path),
            errors=result.get("errors", []),
            details=result,
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
