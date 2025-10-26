#!/usr/bin/env python3
"""
Betty Framework - Telemetry Utilities
Decorator and utilities for automatic execution logging
"""

import functools
import time
import inspect
from typing import Any, Callable, Dict, Optional
from pathlib import Path
from .telemetry_capture import TelemetryCapture


def capture_telemetry(
    skill_name: Optional[str] = None,
    caller: str = "runtime",
    capture_inputs: bool = False,
    sanitize_keys: Optional[list] = None
):
    """
    Decorator to automatically capture telemetry for function execution.

    Usage:
        @capture_telemetry(skill_name="agent.run", caller="CLI", capture_inputs=True)
        def run_agent(agent_path, task_context=None):
            # ... implementation
            return result

    Args:
        skill_name: Name of the skill/component. If None, uses function name.
        caller: Source of the call (e.g., 'CLI', 'API', 'workflow')
        capture_inputs: Whether to capture function arguments (default: False)
        sanitize_keys: List of parameter names to exclude (e.g., ['password', 'api_key'])

    The decorated function can:
    - Return a dict with 'status' key to set telemetry status
    - Raise exceptions (captured as 'error' status)
    - Return any value (captured as 'success' status)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Determine skill name
            skill = skill_name or f"{func.__module__}.{func.__name__}"

            # Capture inputs if requested
            inputs = {}
            if capture_inputs:
                # Get function signature
                sig = inspect.signature(func)
                bound_args = sig.bind_partial(*args, **kwargs)
                bound_args.apply_defaults()

                # Sanitize inputs
                inputs = dict(bound_args.arguments)
                if sanitize_keys:
                    for key in sanitize_keys:
                        if key in inputs:
                            inputs[key] = "***REDACTED***"

            # Start timing
            start_time = time.time()
            status = "success"
            error_message = None
            result = None

            try:
                # Execute function
                result = func(*args, **kwargs)

                # Check if result contains status
                if isinstance(result, dict) and 'status' in result:
                    status = result['status']

                return result

            except Exception as e:
                status = "error"
                error_message = str(e)
                raise  # Re-raise the exception

            finally:
                # Calculate duration
                duration_ms = (time.time() - start_time) * 1000

                # Capture telemetry
                try:
                    telemetry = TelemetryCapture()
                    telemetry.capture(
                        skill=skill,
                        status=status,
                        duration_ms=duration_ms,
                        caller=caller,
                        inputs=inputs,
                        error_message=error_message
                    )
                except Exception as telemetry_error:
                    # Don't let telemetry errors break the actual function
                    print(f"Warning: Telemetry capture failed: {telemetry_error}", file=sys.stderr)

        return wrapper
    return decorator


class TelemetryContext:
    """
    Context manager for capturing telemetry around code blocks.

    Usage:
        with TelemetryContext(skill="plugin.build", caller="CLI") as ctx:
            # ... do work
            ctx.set_inputs({"plugin_path": "./plugin.yaml"})
            result = build_plugin()
            ctx.set_status("success")
    """

    def __init__(
        self,
        skill: str,
        caller: str = "runtime",
        inputs: Optional[Dict[str, Any]] = None
    ):
        self.skill = skill
        self.caller = caller
        self.inputs = inputs or {}
        self.status = "success"
        self.error_message = None
        self.start_time = None
        self.telemetry = TelemetryCapture()

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Calculate duration
        duration_ms = (time.time() - self.start_time) * 1000

        # Set status based on exception
        if exc_type is not None:
            self.status = "error"
            self.error_message = str(exc_val)

        # Capture telemetry
        try:
            self.telemetry.capture(
                skill=self.skill,
                status=self.status,
                duration_ms=duration_ms,
                caller=self.caller,
                inputs=self.inputs,
                error_message=self.error_message
            )
        except Exception as telemetry_error:
            print(f"Warning: Telemetry capture failed: {telemetry_error}", file=sys.stderr)

        # Don't suppress exceptions
        return False

    def set_status(self, status: str):
        """Update the execution status."""
        self.status = status

    def set_inputs(self, inputs: Dict[str, Any]):
        """Update the captured inputs."""
        self.inputs.update(inputs)

    def set_error(self, error_message: str):
        """Set error message."""
        self.error_message = error_message
        self.status = "error"


# Example usage for testing
if __name__ == "__main__":
    # Test decorator
    @capture_telemetry(skill_name="test.function", caller="CLI", capture_inputs=True)
    def test_function(name: str, value: int = 10):
        """Test function for telemetry capture."""
        print(f"Executing test_function with name={name}, value={value}")
        time.sleep(0.1)  # Simulate work
        return {"status": "success", "result": value * 2}

    # Test context manager
    def test_context():
        """Test context manager for telemetry capture."""
        with TelemetryContext(skill="test.context", caller="CLI") as ctx:
            ctx.set_inputs({"operation": "test"})
            print("Executing within context")
            time.sleep(0.05)  # Simulate work
            ctx.set_status("success")

    print("Testing decorator...")
    result = test_function("example", value=42)
    print(f"Result: {result}\n")

    print("Testing context manager...")
    test_context()
    print("\nTelemetry tests complete!")
