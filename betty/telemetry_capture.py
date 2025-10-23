"""
Centralized telemetry capture decorator for Betty Framework.
Provides easy-to-use decorators and functions for tracking skill, workflow, and agent executions.
"""

import functools
import json
import os
import sys
import time
import uuid
from typing import Any, Callable, Dict, List, Optional
from datetime import datetime, timezone

# Ensure imports work
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def create_telemetry_entry(
    skill_name: str,
    inputs: Dict[str, Any],
    status: str,
    duration_ms: int,
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: Optional[str] = None,
    execution_id: Optional[str] = None,
    **extra_fields: Any,
) -> Dict[str, Any]:
    """
    Create a telemetry entry with consistent schema.

    Args:
        skill_name: Name of the skill/workflow/agent being tracked
        inputs: Input parameters passed
        status: Execution status (success, failed, timeout, etc.)
        duration_ms: Execution duration in milliseconds
        agent: Optional agent name that invoked the skill
        workflow: Optional workflow name in which the skill was executed
        caller: Optional caller identifier (CLI, API, workflow, etc.)
        execution_id: Optional UUID for tracking execution (auto-generated if not provided)
        **extra_fields: Additional custom fields to include

    Returns:
        Telemetry entry dictionary with consistent schema
    """
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "execution_id": execution_id or str(uuid.uuid4()),
        "skill": skill_name,
        "inputs": inputs,
        "status": status,
        "duration_ms": duration_ms,
    }

    # Add optional fields if provided
    if agent is not None:
        entry["agent"] = agent

    if workflow is not None:
        entry["workflow"] = workflow

    if caller is not None:
        entry["caller"] = caller

    # Add any extra fields
    if extra_fields:
        entry.update(extra_fields)

    return entry


def capture_telemetry_entry(entry: Dict[str, Any]) -> None:
    """
    Capture a telemetry entry by calling the telemetry.capture skill.

    This is a non-blocking operation - failures are logged but don't interrupt execution.

    Args:
        entry: Telemetry entry to capture
    """
    try:
        # Import telemetry module dynamically to avoid circular dependencies
        telemetry_module_path = os.path.join(
            parent_dir,
            "skills",
            "telemetry.capture",
            "telemetry_capture.py"
        )

        if not os.path.exists(telemetry_module_path):
            logger.debug("telemetry.capture skill not found, skipping telemetry")
            return

        # Import the telemetry functions
        import importlib.util
        spec = importlib.util.spec_from_file_location("telemetry_capture_skill", telemetry_module_path)
        telemetry_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(telemetry_module)

        # Capture telemetry using the skill's function
        telemetry_module.capture_telemetry(entry)
        logger.debug(f"Telemetry captured for {entry.get('skill')}")

    except Exception as e:
        # Don't let telemetry failures break the main execution
        logger.debug(f"Failed to capture telemetry: {e}")


def telemetry_tracked(
    skill_name: Optional[str] = None,
    caller: str = "cli",
    capture_inputs: bool = False
):
    """
    Decorator to automatically capture telemetry for function executions.

    Usage:
        @telemetry_tracked(skill_name="workflow.validate", caller="cli")
        def main(argv: Optional[List[str]] = None) -> int:
            # Your logic here
            return 0

    Or for regular functions:
        @telemetry_tracked(skill_name="my_function", caller="internal")
        def my_function(arg1, arg2):
            return result

    Args:
        skill_name: Name of the skill (defaults to function name)
        caller: Caller identifier (cli, workflow, api, internal, etc.)
        capture_inputs: Whether to capture full input arguments (default: False for privacy)

    Returns:
        Decorated function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            return_value = None
            status = "failed"
            error_msg = None
            execution_id = str(uuid.uuid4())

            # Use skill_name if provided, otherwise use function name
            actual_skill_name = skill_name or func.__name__

            try:
                return_value = func(*args, **kwargs)

                # Determine status based on return type
                if isinstance(return_value, int):
                    # Return code: 0 = success, non-zero = failed
                    status = "success" if return_value == 0 else "failed"
                elif isinstance(return_value, dict) and "ok" in return_value:
                    # Dict with 'ok' field
                    status = "success" if return_value.get("ok") else "failed"
                elif isinstance(return_value, dict) and "status" in return_value:
                    # Dict with 'status' field
                    status = return_value.get("status", "unknown")
                else:
                    # Assume success if no exception was raised
                    status = "success"

                return return_value

            except Exception as e:
                status = "failed"
                error_msg = str(e)
                raise

            finally:
                # Calculate duration
                duration_ms = int((time.time() - start_time) * 1000)

                # Prepare inputs
                inputs = {}
                if capture_inputs:
                    # Capture full inputs (use with caution for sensitive data)
                    inputs = {
                        "args": [str(a) for a in args[:10]],  # Limit to first 10
                        "kwargs": {k: str(v) for k, v in list(kwargs.items())[:10]}  # Limit to first 10
                    }
                else:
                    # Capture only counts (safer for privacy)
                    if args and isinstance(args[0], list):
                        # First arg is argv for CLI functions
                        argv = args[0] if args[0] is not None else []
                        inputs = {
                            "arg_count": len(argv),
                            "args_preview": argv[:3] if len(argv) <= 3 else argv[:3] + ["..."],
                        }
                    else:
                        inputs = {
                            "args_count": len(args),
                            "kwargs_keys": list(kwargs.keys()),
                        }

                # Create telemetry entry
                entry = create_telemetry_entry(
                    skill_name=actual_skill_name,
                    inputs=inputs,
                    status=status,
                    duration_ms=duration_ms,
                    caller=caller,
                    execution_id=execution_id,
                    error=error_msg if error_msg else None,
                )

                # Capture telemetry (non-blocking)
                capture_telemetry_entry(entry)

        return wrapper
    return decorator


def track_execution(
    name: str,
    func: Callable,
    inputs: Dict[str, Any],
    workflow: Optional[str] = None,
    agent: Optional[str] = None,
    caller: str = "workflow",
    execution_id: Optional[str] = None,
) -> Any:
    """
    Execute a function and track its telemetry.

    This is useful for workflow/agent execution where you want to track
    individual skill invocations inline.

    Usage:
        result = track_execution(
            name="policy.enforce",
            func=lambda: enforce_policy(policy_name),
            inputs={"policy": policy_name},
            workflow="validation-pipeline",
            execution_id=workflow_execution_id
        )

    Args:
        name: Name of the skill/function being executed
        func: Function to execute
        inputs: Input parameters dict
        workflow: Optional workflow name
        agent: Optional agent name
        caller: Caller identifier (default: "workflow")
        execution_id: Optional UUID for tracking (auto-generated if not provided)

    Returns:
        Result of the function execution

    Raises:
        Any exception raised by func
    """
    start_time = time.time()
    error_msg = None
    result = None
    actual_execution_id = execution_id or str(uuid.uuid4())

    try:
        result = func()
        status = "success"
        return result
    except Exception as e:
        status = "failed"
        error_msg = str(e)
        raise
    finally:
        duration_ms = int((time.time() - start_time) * 1000)

        # Create telemetry entry
        entry = create_telemetry_entry(
            skill_name=name,
            inputs=inputs,
            status=status,
            duration_ms=duration_ms,
            agent=agent,
            workflow=workflow,
            caller=caller,
            execution_id=actual_execution_id,
            error=error_msg if error_msg else None,
        )

        # Capture telemetry (non-blocking)
        capture_telemetry_entry(entry)
