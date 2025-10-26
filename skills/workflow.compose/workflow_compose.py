#!/usr/bin/env python3
"""
workflow_compose.py – Implementation of the workflow.compose Skill
Executes multi-step Betty Framework workflows by chaining existing skills.
"""
import os
import sys
import yaml
import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone
from pydantic import ValidationError as PydanticValidationError
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from betty.config import BASE_DIR, WORKFLOW_HISTORY_FILE, get_skill_handler_path
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import WorkflowError, format_error_response
from betty.telemetry_capture import capture_skill_execution
from betty.models import WorkflowDefinition
from betty.skill_executor import execute_skill_in_process
from utils.telemetry_utils import capture_telemetry
logger = setup_logger(__name__)


def log_audit_entry(
    skill_name: str,
    status: str,
    duration_ms: Optional[int] = None,
    errors: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Log an audit entry for skill execution.

    Args:
        skill_name: Name of the skill
        status: Execution status (success, failed, etc.)
        duration_ms: Execution duration in milliseconds
        errors: List of errors (if any)
        metadata: Additional metadata
    """
    try:
        args = [skill_name, status]

        if duration_ms is not None:
            args.append(str(duration_ms))
        else:
            args.append("")

        if errors:
            args.append(json.dumps(errors))
        else:
            args.append("[]")

        if metadata:
            args.append(json.dumps(metadata))

        result = execute_skill_in_process("audit.log", args, timeout=10)

        if result["returncode"] != 0:
            logger.warning(f"Failed to log audit entry for {skill_name}: {result['stderr']}")
    except Exception as e:
        logger.warning(f"Failed to log audit entry for {skill_name}: {e}")
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
def load_workflow(workflow_file: str) -> Dict[str, Any]:
    """
    Load and parse a workflow YAML file.
    Args:
        workflow_file: Path to workflow YAML file
    Returns:
        Parsed workflow dictionary
    Raises:
        WorkflowError: If workflow cannot be loaded
    """
    try:
        with open(workflow_file) as f:
            workflow = yaml.safe_load(f)

        # Validate with Pydantic schema
        try:
            WorkflowDefinition.model_validate(workflow)
            logger.info("Pydantic schema validation passed for workflow")
        except PydanticValidationError as exc:
            errors = []
            for error in exc.errors():
                field = ".".join(str(loc) for loc in error["loc"])
                message = error["msg"]
                errors.append(f"{field}: {message}")
            raise WorkflowError(f"Workflow schema validation failed: {'; '.join(errors)}")

        return workflow
    except FileNotFoundError:
        raise WorkflowError(f"Workflow file not found: {workflow_file}")
    except yaml.YAMLError as e:
        raise WorkflowError(f"Invalid YAML in workflow: {e}")
def run_skill(skill_name: str, args: List[str]) -> Dict[str, Any]:
    """
    Run a skill handler in-process using dynamic imports.

    Args:
        skill_name: Name of the skill (e.g., "workflow.validate", "audit.log")
        args: Arguments to pass to the skill

    Returns:
        Dictionary with stdout, stderr, and return code

    Raises:
        WorkflowError: If skill execution fails
    """
    logger.info(f"▶ Running skill {skill_name} with args: {' '.join(args)}")

    # Verify skill handler exists
    skill_path = get_skill_handler_path(skill_name)
    if not os.path.exists(skill_path):
        raise WorkflowError(f"Skill handler not found: {skill_path}")

    try:
        # Execute skill in-process with 5 minute timeout
        result = execute_skill_in_process(skill_name, args, timeout=300)
        return result
    except Exception as e:
        raise WorkflowError(f"Failed to execute skill: {e}")
def save_workflow_history(log: Dict[str, Any]) -> None:
    """
    Save workflow execution history.
    Args:
        log: Workflow execution log
    """
    def update_fn(history_data):
        """Update function for safe_update_json."""
        if not isinstance(history_data, list):
            history_data = []
        history_data.append(log)
        # Keep only last 100 workflow runs
        return history_data[-100:]
    try:
        safe_update_json(WORKFLOW_HISTORY_FILE, update_fn, default=[])
        logger.info(f"Workflow history saved to {WORKFLOW_HISTORY_FILE}")
    except Exception as e:
        logger.warning(f"Failed to save workflow history: {e}")
def execute_workflow(workflow_file: str) -> Dict[str, Any]:
    """Read a workflow YAML and execute skills sequentially."""
    validate_path(workflow_file, must_exist=True)
    workflow = load_workflow(workflow_file)
    fail_fast = workflow.get("fail_fast", True)
    log: Dict[str, Any] = {
        "workflow": os.path.basename(workflow_file),
        "workflow_path": workflow_file,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "fail_fast": fail_fast,
        "steps": [],
        "status": "running",
    }
    aggregated_errors: List[str] = []
    # Validate workflow definition before executing steps
    validation_result = run_skill("workflow.validate", [workflow_file])
    validation_log: Dict[str, Any] = {
        "step": "validation",
        "skill": "workflow.validate",
        "args": [workflow_file],
        "returncode": validation_result["returncode"],
        "stdout": validation_result["stdout"],
        "stderr": validation_result["stderr"],
        "parsed": validation_result.get("parsed"),
        "parse_error": validation_result.get("parse_error"),
        "status": "success" if validation_result["returncode"] == 0 else "failed",
        "errors": [],
    }
    parsed_validation = validation_result.get("parsed")
    if isinstance(parsed_validation, dict) and parsed_validation.get("errors"):
        validation_log["errors"] = [str(err) for err in parsed_validation.get("errors", [])]
    if validation_result.get("parse_error") and not validation_log["errors"]:
        validation_log["errors"] = [validation_result["parse_error"]]
    log["validation"] = validation_log
    if validation_log["status"] != "success" or (
        isinstance(parsed_validation, dict) and not parsed_validation.get("ok", True)
    ):
        if validation_log["errors"]:
            aggregated_errors.extend(validation_log["errors"])
        else:
            aggregated_errors.append(
                f"workflow.validate failed with return code {validation_result['returncode']}"
            )
        log["status"] = "failed"
        log["errors"] = aggregated_errors
        log["completed_at"] = datetime.now(timezone.utc).isoformat()
        save_workflow_history(log)
        return log
    steps = workflow.get("steps", [])
    if not isinstance(steps, list) or not steps:
        raise WorkflowError("Workflow has no steps defined")
    logger.info(f"Executing workflow: {workflow_file}")
    logger.info(f"Total steps: {len(steps)}")
    failed_steps: List[Dict[str, Any]] = []
    for i, step in enumerate(steps, 1):
        # Support both 'skill' and 'agent' step types
        is_agent_step = "agent" in step
        is_skill_step = "skill" in step

        step_log: Dict[str, Any] = {
            "step_number": i,
            "skill": step.get("skill") if is_skill_step else None,
            "agent": step.get("agent") if is_agent_step else None,
            "args": step.get("args", []),
            "status": "pending",
        }

        # Validate step has either skill or agent field
        if not is_skill_step and not is_agent_step:
            error = f"Step {i} missing required 'skill' or 'agent' field"
            logger.error(error)
            step_log["status"] = "failed"
            step_log["errors"] = [error]
            aggregated_errors.append(error)
            failed_steps.append({"step": i, "error": error})
            log["steps"].append(step_log)
            if fail_fast:
                break
            continue

        if is_skill_step and is_agent_step:
            error = f"Step {i} cannot have both 'skill' and 'agent' fields"
            logger.error(error)
            step_log["status"] = "failed"
            step_log["errors"] = [error]
            aggregated_errors.append(error)
            failed_steps.append({"step": i, "error": error})
            log["steps"].append(step_log)
            if fail_fast:
                break
            continue

        # Handle agent steps by delegating to run.agent skill
        if is_agent_step:
            agent_name = step["agent"]
            input_text = step.get("input", "")
            skill_name = "run.agent"
            args = [agent_name]
            if input_text:
                args.append(input_text)
            logger.info(f"\n=== Step {i}/{len(steps)}: Executing agent {agent_name} via run.agent ===")
        else:
            skill_name = step["skill"]
            args = step.get("args", [])
            logger.info(f"\n=== Step {i}/{len(steps)}: Executing {skill_name} ===")
        try:
            step_start_time = datetime.now(timezone.utc)
            execution_result = run_skill(skill_name, args)
            step_end_time = datetime.now(timezone.utc)
            step_duration_ms = int((step_end_time - step_start_time).total_seconds() * 1000)

            parsed_step = execution_result.get("parsed")
            step_errors: List[str] = []
            if isinstance(parsed_step, dict) and parsed_step.get("errors"):
                step_errors = [str(err) for err in parsed_step.get("errors", [])]
            elif execution_result["returncode"] != 0:
                step_errors = [
                    f"Step {i} failed with return code {execution_result['returncode']}"
                ]
            step_log.update(
                {
                    "skill": skill_name,
                    "args": args,
                    "returncode": execution_result["returncode"],
                    "stdout": execution_result["stdout"],
                    "stderr": execution_result["stderr"],
                    "parsed": parsed_step,
                    "parse_error": execution_result.get("parse_error"),
                    "status": "success" if execution_result["returncode"] == 0 else "failed",
                    "errors": step_errors,
                    "duration_ms": step_duration_ms,
                }
            )
            log["steps"].append(step_log)

            # Log audit entry for this step
            log_audit_entry(
                skill_name=skill_name,
                status="success" if execution_result["returncode"] == 0 else "failed",
                duration_ms=step_duration_ms,
                errors=step_errors if step_errors else None,
                metadata={
                    "workflow": os.path.basename(workflow_file),
                    "step_number": i,
                    "total_steps": len(steps),
                }
            )

            # Capture telemetry for this step
            capture_skill_execution(
                skill_name=skill_name,
                inputs={"args": args},
                status="success" if execution_result["returncode"] == 0 else "failed",
                duration_ms=step_duration_ms,
                workflow=os.path.basename(workflow_file),
                caller="workflow.compose",
                error=step_errors[0] if step_errors else None,
                step_number=i,
                total_steps=len(steps),
            )
            if execution_result["returncode"] != 0:
                failed_steps.append({
                    "step": i,
                    "skill": skill_name,
                    "returncode": execution_result["returncode"],
                    "errors": step_errors,
                })
                aggregated_errors.extend(step_errors or [
                    f"Step {i} ({skill_name}) failed with return code {execution_result['returncode']}"
                ])
                logger.error(
                    f"❌ Step {i} failed with return code {execution_result['returncode']}"
                )
                if fail_fast:
                    logger.error("Stopping workflow due to failure (fail_fast=true)")
                    break
            else:
                logger.info(f"✅ Step {i} completed successfully")
        except WorkflowError as e:
            error_msg = str(e)
            logger.error(f"❌ Step {i} failed: {error_msg}")
            step_log.update(
                {
                    "returncode": None,
                    "stdout": "",
                    "stderr": "",
                    "parsed": None,
                    "parse_error": None,
                    "status": "failed",
                    "errors": [error_msg],
                }
            )
            aggregated_errors.append(error_msg)
            failed_steps.append({"step": i, "skill": skill_name, "error": error_msg})
            log["steps"].append(step_log)

            # Log audit entry for failed step
            log_audit_entry(
                skill_name=skill_name,
                status="failed",
                errors=[error_msg],
                metadata={
                    "workflow": os.path.basename(workflow_file),
                    "step_number": i,
                    "total_steps": len(steps),
                    "error_type": "WorkflowError",
                }
            )

            # Capture telemetry for failed step
            capture_skill_execution(
                skill_name=skill_name,
                inputs={"args": args},
                status="failed",
                duration_ms=0,  # No duration available for exception cases
                workflow=os.path.basename(workflow_file),
                caller="workflow.compose",
                error=error_msg,
                step_number=i,
                total_steps=len(steps),
                error_type="WorkflowError",
            )

            if fail_fast:
                break
    if failed_steps:
        log["status"] = "failed"
        log["failed_steps"] = failed_steps
    else:
        log["status"] = "success"
    log["errors"] = aggregated_errors
    log["completed_at"] = datetime.now(timezone.utc).isoformat()
    save_workflow_history(log)

    # Calculate total workflow duration
    workflow_duration_ms = None
    if "started_at" in log and "completed_at" in log:
        start = datetime.fromisoformat(log["started_at"])
        end = datetime.fromisoformat(log["completed_at"])
        workflow_duration_ms = int((end - start).total_seconds() * 1000)

    # Log audit entry for overall workflow
    log_audit_entry(
        skill_name="workflow.compose",
        status=log["status"],
        duration_ms=workflow_duration_ms,
        errors=aggregated_errors if aggregated_errors else None,
        metadata={
            "workflow": os.path.basename(workflow_file),
            "total_steps": len(steps),
            "failed_steps": len(failed_steps),
        }
    )

    # Capture telemetry for overall workflow
    capture_skill_execution(
        skill_name="workflow.compose",
        inputs={"workflow_file": workflow_file},
        status=log["status"],
        duration_ms=workflow_duration_ms or 0,
        caller="cli",
        error=aggregated_errors[0] if aggregated_errors else None,
        workflow=os.path.basename(workflow_file),
        total_steps=len(steps),
        failed_steps=len(failed_steps),
        completed_steps=len(steps) - len(failed_steps),
    )

    if log["status"] == "success":
        logger.info("\n✅ Workflow completed successfully")
    else:
        logger.error(f"\n❌ Workflow completed with {len(failed_steps)} failed step(s)")
    return log


@capture_telemetry(skill_name="workflow.compose", caller="cli")
def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: workflow_compose.py <workflow.yaml>"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)
    workflow_file = sys.argv[1]
    try:
        details = execute_workflow(workflow_file)
        response = build_response(
            details.get("status") == "success",
            path=WORKFLOW_HISTORY_FILE,
            errors=details.get("errors", []),
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0 if response["ok"] else 1)
    except WorkflowError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=workflow_file,
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
            path=workflow_file,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)
if __name__ == "__main__":
    main()
