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
from typing import Dict, Any, List
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, WORKFLOW_HISTORY_FILE, get_skill_handler_path
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import WorkflowError, format_error_response

logger = setup_logger(__name__)


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

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
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
    """
    Read a workflow YAML and execute skills in order.

    Args:
        workflow_file: Path to workflow YAML file

    Returns:
        Dictionary with workflow execution results

    Raises:
        WorkflowError: If workflow execution fails
    """
    validate_path(workflow_file, must_exist=True)

    workflow = load_workflow(workflow_file)

    log = {
        "workflow": os.path.basename(workflow_file),
        "workflow_path": workflow_file,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "steps": [],
        "status": "running"
    }

    steps = workflow.get("steps", [])
    if not steps:
        raise WorkflowError("Workflow has no steps defined")

    logger.info(f"Executing workflow: {workflow_file}")
    logger.info(f"Total steps: {len(steps)}")

    failed_steps = []

    for i, step in enumerate(steps, 1):
        if "skill" not in step:
            error = f"Step {i} missing required 'skill' field"
            logger.error(error)
            failed_steps.append({"step": i, "error": error})
            continue

        skill_name = step["skill"]
        handler = get_skill_handler_path(skill_name)
        args = step.get("args", [])

        logger.info(f"\n=== Step {i}/{len(steps)}: Executing {skill_name} ===")

        try:
            execution_result = run_skill(handler, args)

            step_log = {
                "step_number": i,
                "skill": skill_name,
                "args": args,
                "output": execution_result["stdout"].strip(),
                "stderr": execution_result["stderr"].strip() if execution_result["stderr"] else None,
                "returncode": execution_result["returncode"],
                "status": "success" if execution_result["returncode"] == 0 else "failed"
            }

            log["steps"].append(step_log)

            if execution_result["returncode"] != 0:
                failed_steps.append({
                    "step": i,
                    "skill": skill_name,
                    "returncode": execution_result["returncode"]
                })
                logger.error(f"❌ Step {i} failed with return code {execution_result['returncode']}")

                # Stop on first failure if fail_fast is true
                if workflow.get("fail_fast", True):
                    logger.error("Stopping workflow due to failure (fail_fast=true)")
                    break
            else:
                logger.info(f"✅ Step {i} completed successfully")

        except WorkflowError as e:
            error_msg = str(e)
            logger.error(f"❌ Step {i} failed: {error_msg}")
            failed_steps.append({"step": i, "skill": skill_name, "error": error_msg})
            log["steps"].append({
                "step_number": i,
                "skill": skill_name,
                "args": args,
                "error": error_msg,
                "status": "failed"
            })

            if workflow.get("fail_fast", True):
                break

    # Determine overall status
    if failed_steps:
        log["status"] = "failed"
        log["failed_steps"] = failed_steps
    else:
        log["status"] = "success"

    log["completed_at"] = datetime.now(timezone.utc).isoformat()

    # Save workflow history
    save_workflow_history(log)

    if log["status"] == "success":
        logger.info(f"\n✅ Workflow completed successfully")
    else:
        logger.error(f"\n❌ Workflow completed with {len(failed_steps)} failed step(s)")

    return log


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        error = {
            "error": "UsageError",
            "message": "Usage: workflow_compose.py <workflow.yaml>",
            "details": {}
        }
        print(json.dumps(error, indent=2))
        sys.exit(1)

    workflow_file = sys.argv[1]

    try:
        result = execute_workflow(workflow_file)
        print(json.dumps(result, indent=2))

        # Exit with error if workflow failed
        if result["status"] == "failed":
            sys.exit(1)

    except WorkflowError as e:
        logger.error(str(e))
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(json.dumps(format_error_response(e, include_traceback=True), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
