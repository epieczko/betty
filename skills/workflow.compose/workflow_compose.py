#!/usr/bin/env python3
"""
workflow_compose.py – Implementation of the workflow.compose Skill
Executes multi-step Betty Framework workflows by chaining existing skills.
"""
import os
import sys
import yaml
import subprocess
import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from betty.config import BASE_DIR, WORKFLOW_HISTORY_FILE, get_skill_handler_path
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import WorkflowError, format_error_response
logger = setup_logger(__name__)
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
def parse_json_output(output: str) -> Tuple[Optional[Any], Optional[str]]:
    """Attempt to parse JSON from subprocess stdout."""
    stripped = output.strip()
    if not stripped:
        return None, None
    try:
        return json.loads(stripped), None
    except json.JSONDecodeError as exc:
        lines = stripped.splitlines()
        for idx in range(len(lines)):
            candidate = "\n".join(lines[idx:])
            try:
                return json.loads(candidate), None
            except json.JSONDecodeError:
                continue
        return None, str(exc)
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
        return workflow
    except FileNotFoundError:
        raise WorkflowError(f"Workflow file not found: {workflow_file}")
    except yaml.YAMLError as e:
        raise WorkflowError(f"Invalid YAML in workflow: {e}")
def run_skill(skill_path: str, args: List[str]) -> Dict[str, Any]:
    """
    Run a skill handler as a subprocess.
    Args:
        skill_path: Path to skill handler script
        args: Arguments to pass to the skill
    Returns:
        Dictionary with stdout, stderr, and return code
    Raises:
        WorkflowError: If skill execution fails
    """
    logger.info(f"▶ Running {skill_path} {' '.join(args)}")
    if not os.path.exists(skill_path):
        raise WorkflowError(f"Skill handler not found: {skill_path}")
    try:
        result = subprocess.run(
            [sys.executable, skill_path] + args,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        logger.info(result.stdout)
        if result.stderr:
            logger.warning(f"Stderr: {result.stderr}")
        parsed, parse_error = parse_json_output(result.stdout)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "parsed": parsed,
            "parse_error": parse_error,
        }
    except subprocess.TimeoutExpired:
        raise WorkflowError(f"Skill execution timed out: {skill_path}")
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
    validator_handler = get_skill_handler_path("workflow.validate")
    validation_result = run_skill(validator_handler, [workflow_file])
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
        step_log: Dict[str, Any] = {
            "step_number": i,
            "skill": step.get("skill"),
            "args": step.get("args", []),
            "status": "pending",
        }
        if "skill" not in step:
            error = f"Step {i} missing required 'skill' field"
            logger.error(error)
            step_log["status"] = "failed"
            step_log["errors"] = [error]
            aggregated_errors.append(error)
            failed_steps.append({"step": i, "error": error})
            log["steps"].append(step_log)
            if fail_fast:
                break
            continue
        skill_name = step["skill"]
        handler = get_skill_handler_path(skill_name)
        args = step.get("args", [])
        logger.info(f"\n=== Step {i}/{len(steps)}: Executing {skill_name} ===")
        try:
            execution_result = run_skill(handler, args)
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
                }
            )
            log["steps"].append(step_log)
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
    if log["status"] == "success":
        logger.info("\n✅ Workflow completed successfully")
    else:
        logger.error(f"\n❌ Workflow completed with {len(failed_steps)} failed step(s)")
    return log


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
