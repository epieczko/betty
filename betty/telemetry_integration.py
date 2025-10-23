"""
Telemetry integration helper for Betty Framework.
Provides easy-to-use wrappers for capturing telemetry in CLI entrypoints.
"""

import functools
import json
import os
import sys
import time
from typing import Any, Callable, List, Optional

# Add parent to path if needed
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def capture_cli_telemetry(
    skill_name: str,
    inputs: dict,
    status: str,
    duration_ms: int,
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: str = "cli",
) -> None:
    """
    Capture telemetry for a CLI execution.

    This is a convenience wrapper that calls the telemetry.capture skill.
    If telemetry capture fails, it logs a warning but doesn't interrupt execution.

    Args:
        skill_name: Name of the skill being executed
        inputs: Input parameters (will be JSON serialized)
        status: Execution status (success, failed, etc.)
        duration_ms: Execution duration in milliseconds
        agent: Optional agent name
        workflow: Optional workflow name
        caller: Caller identifier (default: "cli")
    """
    try:
        # Import here to avoid circular dependencies
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
        spec = importlib.util.spec_from_file_location("telemetry_capture", telemetry_module_path)
        telemetry_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(telemetry_module)

        # Create and capture telemetry entry
        entry = telemetry_module.create_telemetry_entry(
            skill_name=skill_name,
            inputs=inputs,
            status=status,
            duration_ms=duration_ms,
            agent=agent,
            workflow=workflow,
            caller=caller,
        )

        telemetry_module.capture_telemetry(entry)
        logger.debug(f"Telemetry captured for {skill_name}")

    except Exception as e:
        # Don't let telemetry failures break the main execution
        logger.debug(f"Failed to capture telemetry: {e}")


def telemetry_tracked(skill_name: str, caller: str = "cli"):
    """
    Decorator for CLI main() functions to automatically capture telemetry.

    Usage:
        @telemetry_tracked(skill_name="workflow.validate", caller="cli")
        def main(argv: Optional[List[str]] = None) -> int:
            # Your CLI logic here
            return 0

    The decorator will:
    - Measure execution time
    - Capture success/failure status based on return code
    - Log telemetry data automatically

    Args:
        skill_name: Name of the skill
        caller: Caller identifier (default: "cli")

    Returns:
        Decorated function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            return_code = 1
            status = "failed"

            try:
                return_code = func(*args, **kwargs)
                status = "success" if return_code == 0 else "failed"
                return return_code
            except Exception as e:
                status = "failed"
                logger.error(f"Exception in {skill_name}: {e}")
                raise
            finally:
                # Calculate duration
                duration_ms = int((time.time() - start_time) * 1000)

                # Extract inputs from args - first element is usually argv
                inputs = {}
                if args:
                    argv = args[0] if args[0] is not None else []
                    inputs = {
                        "arg_count": len(argv),
                        "args": argv[:5] if len(argv) <= 5 else argv[:5] + ["..."],  # Limit to first 5
                    }

                # Capture telemetry (non-blocking)
                capture_cli_telemetry(
                    skill_name=skill_name,
                    inputs=inputs,
                    status=status,
                    duration_ms=duration_ms,
                    caller=caller,
                )

        return wrapper
    return decorator


def track_skill_execution(
    skill_name: str,
    func: Callable,
    inputs: dict,
    workflow: Optional[str] = None,
    agent: Optional[str] = None,
    caller: str = "workflow",
) -> Any:
    """
    Execute a function and track its telemetry.

    This is useful for workflow/agent execution where you want to track
    individual skill invocations.

    Usage:
        result = track_skill_execution(
            skill_name="policy.enforce",
            func=lambda: enforce_policy(policy_name),
            inputs={"policy": policy_name},
            workflow="validation-pipeline"
        )

    Args:
        skill_name: Name of the skill being executed
        func: Function to execute
        inputs: Input parameters dict
        workflow: Optional workflow name
        agent: Optional agent name
        caller: Caller identifier (default: "workflow")

    Returns:
        Result of the function execution

    Raises:
        Any exception raised by func
    """
    start_time = time.time()
    error = None
    result = None

    try:
        result = func()
        status = "success"
        return result
    except Exception as e:
        status = "failed"
        error = str(e)
        raise
    finally:
        duration_ms = int((time.time() - start_time) * 1000)

        # Capture telemetry
        capture_cli_telemetry(
            skill_name=skill_name,
            inputs=inputs,
            status=status,
            duration_ms=duration_ms,
            agent=agent,
            workflow=workflow,
            caller=caller,
        )
