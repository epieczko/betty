#!/usr/bin/env python3
"""
Betty Framework - Auto-Injection Telemetry Decorator
Automatically capture telemetry for skill execution without manual instrumentation.

This module provides decorators that automatically inject telemetry capture
into skill handlers and workflows, eliminating the need for manual telemetry calls.

Usage:
    from utils.telemetry_utils import capture_telemetry

    @capture_telemetry(skill_name="plugin.publish")
    def main():
        # Your skill implementation
        return result
"""

import functools
import os
import sys
import time
import inspect
from typing import Any, Callable, Dict, Optional
from pathlib import Path

# Add betty module to path
BETTY_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BETTY_HOME not in sys.path:
    sys.path.insert(0, BETTY_HOME)

from betty.telemetry_capture import create_telemetry_entry, _append_telemetry_entry
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def capture_telemetry(
    skill_name: Optional[str] = None,
    caller: str = "cli",
    capture_args: bool = True,
    detect_caller: bool = True,
):
    """
    Auto-injection decorator for telemetry capture.

    Automatically captures telemetry for skill execution by wrapping the main()
    function or any skill handler. This decorator handles:
    - Execution timing (duration_ms)
    - Status detection (success/failure based on return code or exceptions)
    - Caller detection (CLI, workflow, agent, runtime)
    - Input parameter capture (CLI arguments)
    - Automatic telemetry.json entry creation

    Usage:
        @capture_telemetry(skill_name="plugin.publish")
        def main():
            result = publish_plugin(...)
            return result

        @capture_telemetry(skill_name="agent.run", caller="cli")
        def run_agent(agent_name, task_context):
            # ... implementation
            sys.exit(0)

    Args:
        skill_name: Name of the skill (e.g., "plugin.publish", "agent.run").
                   If None, auto-detected from function or file path.
        caller: Execution context - "cli", "workflow", "agent", or "runtime".
                Default is "cli". Can be auto-detected if detect_caller=True.
        capture_args: Whether to capture function arguments and CLI args.
                     Default is True.
        detect_caller: Attempt to auto-detect caller from environment.
                      Looks for BETTY_CALLER env var or workflow context.
                      Default is True.

    Return Value Handling:
        - If the function returns an integer, it's treated as an exit code:
          * 0 = success
          * Non-zero = failed
        - If the function returns a dict with 'ok' or 'status' keys:
          * {'ok': True} = success
          * {'ok': False} = failed
          * {'status': 'success'} = success
          * {'status': 'failed'} = failed
        - If the function calls sys.exit():
          * sys.exit(0) = success (captured via SystemExit)
          * sys.exit(N) = failed
        - If an exception is raised:
          * Status = "failed", error message captured
        - Any other return value:
          * Status = "success"

    Environment Variables:
        - BETTY_CALLER: Override caller detection (e.g., "workflow", "agent")
        - BETTY_WORKFLOW: Name of the executing workflow (if any)
        - BETTY_AGENT: Name of the executing agent (if any)
        - BETTY_EXECUTION_ID: Parent execution ID for tracing

    Example:
        # Basic usage - auto-detects skill name
        @capture_telemetry()
        def main():
            print("Running skill...")
            return 0

        # Explicit skill name and caller
        @capture_telemetry(skill_name="plugin.build", caller="cli")
        def main():
            result = build_plugin()
            return result

        # Workflow execution context
        @capture_telemetry(skill_name="workflow.step", detect_caller=True)
        def execute_step():
            # BETTY_CALLER env var will be detected
            return {"ok": True}
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Auto-detect skill name if not provided
            actual_skill_name = skill_name
            if not actual_skill_name:
                # Try to infer from function name or file path
                actual_skill_name = _infer_skill_name(func)

            # Auto-detect caller from environment
            actual_caller = caller
            workflow_name = None
            agent_name = None

            if detect_caller:
                actual_caller = os.environ.get("BETTY_CALLER", caller)
                workflow_name = os.environ.get("BETTY_WORKFLOW")
                agent_name = os.environ.get("BETTY_AGENT")

            # Capture input arguments
            inputs = {}
            if capture_args:
                inputs = _capture_inputs(func, args, kwargs)

            # Start timing
            start_time = time.time()
            status = "success"
            error_message = None
            result = None
            exit_code = 0

            try:
                # Execute the wrapped function
                result = func(*args, **kwargs)

                # Determine status from return value
                status, exit_code = _determine_status_from_result(result)

                return result

            except SystemExit as e:
                # Handle sys.exit() calls
                exit_code = e.code if e.code is not None else 0
                status = "success" if exit_code == 0 else "failed"
                error_message = f"Exited with code {exit_code}" if exit_code != 0 else None
                raise  # Re-raise to maintain exit behavior

            except Exception as e:
                # Handle exceptions
                status = "failed"
                error_message = f"{type(e).__name__}: {str(e)}"
                exit_code = 1
                raise  # Re-raise the exception

            finally:
                # Calculate duration
                duration_ms = int((time.time() - start_time) * 1000)

                # Build telemetry entry
                try:
                    # Add metadata
                    metadata = {
                        "exit_code": exit_code,
                    }

                    # Add optional context fields
                    if workflow_name:
                        metadata["workflow"] = workflow_name
                    if agent_name:
                        metadata["agent"] = agent_name

                    # Create and append telemetry entry
                    entry = create_telemetry_entry(
                        skill_name=actual_skill_name,
                        inputs=inputs,
                        status=status,
                        duration_ms=duration_ms,
                        caller=actual_caller,
                        agent=agent_name,
                        workflow=workflow_name,
                        error=error_message,
                        **metadata
                    )

                    _append_telemetry_entry(entry)
                    logger.debug(f"Telemetry captured for {actual_skill_name}: {status} ({duration_ms}ms)")

                except Exception as telemetry_error:
                    # Don't let telemetry failures break execution
                    logger.warning(f"Failed to capture telemetry for {actual_skill_name}: {telemetry_error}")

        return wrapper
    return decorator


def _infer_skill_name(func: Callable) -> str:
    """
    Infer skill name from function or file path.

    Attempts to extract skill name using:
    1. Function module path (e.g., skills.plugin.publish.plugin_publish -> plugin.publish)
    2. File path (e.g., /skills/plugin.publish/plugin_publish.py -> plugin.publish)
    3. Function name as fallback

    Args:
        func: Function to infer name from

    Returns:
        Inferred skill name
    """
    try:
        # Try to get module name
        module = func.__module__
        if module and module != "__main__":
            # Extract skill name from module path
            # e.g., "skills.plugin.publish.plugin_publish" -> "plugin.publish"
            parts = module.split(".")
            if "skills" in parts:
                skill_idx = parts.index("skills")
                if len(parts) > skill_idx + 1:
                    # Take the directory name after "skills"
                    skill_name = parts[skill_idx + 1]
                    return skill_name

        # Try to get from file path
        if hasattr(func, "__code__"):
            file_path = func.__code__.co_filename
            path = Path(file_path)

            # Check if in skills directory
            if "skills" in path.parts:
                skill_idx = path.parts.index("skills")
                if len(path.parts) > skill_idx + 1:
                    skill_name = path.parts[skill_idx + 1]
                    return skill_name

        # Fallback to function name
        return func.__name__

    except Exception as e:
        logger.debug(f"Failed to infer skill name: {e}")
        return func.__name__


def _capture_inputs(func: Callable, args: tuple, kwargs: dict) -> Dict[str, Any]:
    """
    Capture function inputs including CLI arguments.

    Args:
        func: Function being called
        args: Positional arguments
        kwargs: Keyword arguments

    Returns:
        Dictionary of captured inputs
    """
    inputs = {}

    try:
        # Capture CLI arguments if available
        if sys.argv:
            inputs["cli_args"] = sys.argv[1:]  # Exclude script name

        # Capture function arguments
        if args or kwargs:
            sig = inspect.signature(func)
            try:
                bound_args = sig.bind_partial(*args, **kwargs)
                bound_args.apply_defaults()
                inputs["function_args"] = dict(bound_args.arguments)
            except Exception:
                # If binding fails, just capture raw args
                if args:
                    inputs["args"] = list(args)
                if kwargs:
                    inputs["kwargs"] = kwargs

        # Sanitize sensitive data
        inputs = _sanitize_inputs(inputs)

    except Exception as e:
        logger.debug(f"Failed to capture inputs: {e}")
        inputs = {"error": "Failed to capture inputs"}

    return inputs


def _sanitize_inputs(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize sensitive data from inputs.

    Redacts common sensitive parameter names like:
    - password, passwd, pwd
    - token, api_key, secret, auth
    - credentials, private_key

    Args:
        inputs: Input dictionary

    Returns:
        Sanitized input dictionary
    """
    sensitive_keys = {
        "password", "passwd", "pwd",
        "token", "api_key", "apikey", "secret", "auth",
        "credentials", "private_key", "privatekey",
        "access_token", "refresh_token",
    }

    def sanitize_dict(d: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively sanitize dictionary."""
        result = {}
        for key, value in d.items():
            # Check if key is sensitive (case-insensitive)
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                result[key] = "***REDACTED***"
            elif isinstance(value, dict):
                result[key] = sanitize_dict(value)
            else:
                result[key] = value
        return result

    return sanitize_dict(inputs)


def _determine_status_from_result(result: Any) -> tuple[str, int]:
    """
    Determine execution status from function return value.

    Args:
        result: Function return value

    Returns:
        Tuple of (status, exit_code)
    """
    # Check if result is an integer (exit code)
    if isinstance(result, int):
        return ("success" if result == 0 else "failed", result)

    # Check if result is a dict with 'ok' or 'status' keys
    if isinstance(result, dict):
        if "ok" in result:
            status = "success" if result["ok"] else "failed"
            return (status, 0 if result["ok"] else 1)

        if "status" in result:
            status = result["status"]
            # Normalize status values
            if status in ["success", "succeeded", "ok", "passed"]:
                return ("success", 0)
            elif status in ["failed", "failure", "error", "timeout"]:
                return ("failed", 1)
            else:
                return (status, 0)

    # Default: any return value without error = success
    return ("success", 0)


# Convenience alias for backward compatibility
auto_telemetry = capture_telemetry


if __name__ == "__main__":
    # Example usage and testing
    print("Testing auto-injection telemetry decorator...")

    @capture_telemetry(skill_name="test.example", caller="cli")
    def test_success():
        """Test successful execution."""
        print("Executing test_success...")
        time.sleep(0.1)
        return {"ok": True, "message": "Test completed"}

    @capture_telemetry(skill_name="test.failure")
    def test_failure():
        """Test failed execution."""
        print("Executing test_failure...")
        return {"ok": False, "error": "Something went wrong"}

    @capture_telemetry()
    def test_auto_detect():
        """Test auto-detection of skill name."""
        print("Executing test_auto_detect...")
        return 0

    # Run tests
    print("\n1. Testing successful execution:")
    result1 = test_success()
    print(f"Result: {result1}\n")

    print("2. Testing failed execution:")
    result2 = test_failure()
    print(f"Result: {result2}\n")

    print("3. Testing auto-detection:")
    result3 = test_auto_detect()
    print(f"Result: {result3}\n")

    print("Telemetry decorator tests complete!")
    print(f"Check telemetry entries in: {os.path.join(BETTY_HOME, 'registry', 'telemetry.json')}")
