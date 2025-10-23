"""
Centralized telemetry capture module for Betty Framework.

This module provides decorators and utilities for capturing execution telemetry
across skills, workflows, and agents. All telemetry is stored in registry/telemetry.json
with consistent schema (ISO timestamps, UUIDs, structured data).

Usage:
    from betty.telemetry_capture import capture_execution, telemetry_decorator

    # As a decorator
    @telemetry_decorator(skill_name="my.skill", caller="cli")
    def my_function():
        pass

    # As a context manager
    with capture_execution(skill_name="my.skill", inputs={...}) as ctx:
        result = do_work()
        ctx.set_metadata(result_info=result)
"""

import functools
import json
import os
import sys
import time
import uuid
from contextlib import contextmanager
from typing import Any, Callable, Dict, List, Optional
from datetime import datetime, timezone

# Add parent to path if needed
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from betty.config import REGISTRY_DIR, TELEMETRY_FILE
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


class TelemetryContext:
    """Context manager for telemetry capture."""

    def __init__(
        self,
        skill_name: str,
        inputs: Dict[str, Any],
        agent: Optional[str] = None,
        workflow: Optional[str] = None,
        caller: Optional[str] = None,
        execution_id: Optional[str] = None,
    ):
        self.skill_name = skill_name
        self.inputs = inputs
        self.agent = agent
        self.workflow = workflow
        self.caller = caller
        self.execution_id = execution_id or str(uuid.uuid4())
        self.start_time = None
        self.metadata = {}
        self.status = "success"
        self.error = None

    def set_metadata(self, **kwargs):
        """Add metadata to the telemetry entry."""
        self.metadata.update(kwargs)

    def set_status(self, status: str):
        """Set execution status."""
        self.status = status

    def set_error(self, error: str):
        """Set error information."""
        self.error = error
        self.status = "failed"

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration_ms = int((time.time() - self.start_time) * 1000)

        # Set status based on exception
        if exc_type is not None:
            self.status = "failed"
            self.error = str(exc_val)

        # Capture telemetry
        try:
            entry = create_telemetry_entry(
                skill_name=self.skill_name,
                inputs=self.inputs,
                status=self.status,
                duration_ms=duration_ms,
                agent=self.agent,
                workflow=self.workflow,
                caller=self.caller,
                execution_id=self.execution_id,
                error=self.error,
                **self.metadata
            )
            _append_telemetry_entry(entry)
        except Exception as e:
            logger.warning(f"Failed to capture telemetry: {e}")

        return False  # Don't suppress exceptions


@contextmanager
def capture_execution(
    skill_name: str,
    inputs: Dict[str, Any],
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: Optional[str] = None,
    execution_id: Optional[str] = None,
):
    """
    Context manager for capturing telemetry.

    Usage:
        with capture_execution(skill_name="api.validate", inputs={"strict": True}) as ctx:
            result = validate_api()
            ctx.set_metadata(issues_found=len(result.issues))

    Args:
        skill_name: Name of the skill being executed
        inputs: Input parameters
        agent: Optional agent name
        workflow: Optional workflow name
        caller: Optional caller identifier
        execution_id: Optional execution UUID (generated if not provided)

    Yields:
        TelemetryContext instance
    """
    ctx = TelemetryContext(
        skill_name=skill_name,
        inputs=inputs,
        agent=agent,
        workflow=workflow,
        caller=caller,
        execution_id=execution_id,
    )

    with ctx:
        yield ctx


def telemetry_decorator(
    skill_name: Optional[str] = None,
    caller: Optional[str] = None,
    capture_inputs: bool = False,
    capture_output: bool = False,
):
    """
    Decorator for automatic telemetry capture.

    Usage:
        @telemetry_decorator(skill_name="workflow.compose", caller="cli")
        def execute_workflow(workflow_file: str):
            return workflow_result

    Args:
        skill_name: Name of the skill (defaults to function name)
        caller: Caller identifier (CLI, API, workflow, agent, etc.)
        capture_inputs: If True, capture function arguments (use cautiously)
        capture_output: If True, capture return value (use cautiously)

    Returns:
        Decorated function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            error = None
            result = None
            execution_id = str(uuid.uuid4())

            # Use skill_name if provided, otherwise use function name
            actual_skill_name = skill_name or func.__name__

            # Prepare inputs
            if capture_inputs:
                inputs = {
                    "args": args,
                    "kwargs": kwargs,
                }
            else:
                inputs = {
                    "args_count": len(args),
                    "kwargs_keys": list(kwargs.keys()),
                }

            try:
                result = func(*args, **kwargs)
                status = "success"
                return result
            except Exception as e:
                status = "failed"
                error = str(e)
                raise
            finally:
                # Calculate duration
                duration_ms = int((time.time() - start_time) * 1000)

                # Add output to metadata if requested
                metadata = {}
                if capture_output and result is not None:
                    try:
                        # Try to serialize result
                        json.dumps(result)
                        metadata["output"] = result
                    except (TypeError, ValueError):
                        metadata["output"] = str(result)

                # Create telemetry entry
                try:
                    entry = create_telemetry_entry(
                        skill_name=actual_skill_name,
                        inputs=inputs,
                        status=status,
                        duration_ms=duration_ms,
                        caller=caller,
                        execution_id=execution_id,
                        error=error,
                        **metadata
                    )

                    # Capture telemetry (non-blocking)
                    _append_telemetry_entry(entry)
                except Exception as telemetry_error:
                    logger.warning(f"Failed to capture telemetry for {actual_skill_name}: {telemetry_error}")

        return wrapper
    return decorator


def create_telemetry_entry(
    skill_name: str,
    inputs: Dict[str, Any],
    status: str,
    duration_ms: int,
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: Optional[str] = None,
    execution_id: Optional[str] = None,
    error: Optional[str] = None,
    **extra_fields: Any,
) -> Dict[str, Any]:
    """
    Create a telemetry entry with consistent schema.

    Schema:
        - timestamp: ISO 8601 timestamp with timezone
        - execution_id: Unique UUID for this execution
        - skill: Skill name
        - inputs: Input parameters
        - status: Execution status (success, failed, timeout, etc.)
        - duration_ms: Execution duration in milliseconds
        - agent: (optional) Agent name
        - workflow: (optional) Workflow name
        - caller: (optional) Caller identifier
        - error: (optional) Error message
        - **extra_fields: Any additional custom fields

    Args:
        skill_name: Name of the skill being tracked
        inputs: Input parameters passed to the skill
        status: Execution status (success, failed, timeout, etc.)
        duration_ms: Execution duration in milliseconds
        agent: Optional agent name that invoked the skill
        workflow: Optional workflow name in which the skill was executed
        caller: Optional caller identifier (CLI, API, etc.)
        execution_id: Optional execution UUID
        error: Optional error message
        **extra_fields: Additional custom fields to include

    Returns:
        Telemetry entry dictionary
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

    if error is not None:
        entry["error"] = error

    # Add any extra fields
    if extra_fields:
        entry.update(extra_fields)

    return entry


def _append_telemetry_entry(entry: Dict[str, Any]) -> None:
    """
    Append telemetry entry to registry/telemetry.json.

    This is an internal function that writes directly without using
    the telemetry.capture skill (to avoid circular dependencies).

    Args:
        entry: Telemetry entry to append
    """
    try:
        # Import here to avoid circular dependencies
        from betty.file_utils import safe_update_json

        def update_fn(telemetry_data):
            """Update function for safe_update_json."""
            if not isinstance(telemetry_data, list):
                telemetry_data = []

            telemetry_data.append(entry)

            # Keep last 100,000 entries (safety limit)
            if len(telemetry_data) > 100000:
                telemetry_data = telemetry_data[-100000:]

            return telemetry_data

        # Ensure registry directory exists
        os.makedirs(REGISTRY_DIR, exist_ok=True)

        # Use safe atomic update with file locking
        safe_update_json(TELEMETRY_FILE, update_fn, default=[])

        logger.debug(f"Telemetry captured for: {entry.get('skill')}")

    except Exception as e:
        # Don't let telemetry failures break execution
        logger.debug(f"Failed to append telemetry entry: {e}")


def capture_skill_execution(
    skill_name: str,
    inputs: Dict[str, Any],
    status: str,
    duration_ms: int,
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: Optional[str] = None,
    execution_id: Optional[str] = None,
    error: Optional[str] = None,
    **extra_fields: Any,
) -> None:
    """
    Directly capture a telemetry entry (convenience function).

    This is useful when you need to manually capture telemetry
    without using decorators or context managers.

    Usage:
        capture_skill_execution(
            skill_name="api.validate",
            inputs={"spec": "openapi.yaml"},
            status="success",
            duration_ms=1234,
            workflow="api-workflow",
            issues_found=5
        )

    Args:
        skill_name: Name of the skill
        inputs: Input parameters
        status: Execution status
        duration_ms: Duration in milliseconds
        agent: Optional agent name
        workflow: Optional workflow name
        caller: Optional caller identifier
        execution_id: Optional execution UUID
        error: Optional error message
        **extra_fields: Additional custom fields
    """
    entry = create_telemetry_entry(
        skill_name=skill_name,
        inputs=inputs,
        status=status,
        duration_ms=duration_ms,
        agent=agent,
        workflow=workflow,
        caller=caller,
        execution_id=execution_id,
        error=error,
        **extra_fields
    )

    _append_telemetry_entry(entry)


def capture_audit_entry(
    skill_name: str,
    status: str,
    duration_ms: Optional[int] = None,
    errors: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Capture an audit log entry.

    This is a convenience wrapper that calls the audit.log skill.
    If audit logging fails, it logs a warning but doesn't interrupt execution.

    Args:
        skill_name: Name of the skill
        status: Execution status (success, failed, etc.)
        duration_ms: Execution duration in milliseconds
        errors: List of errors (if any)
        metadata: Additional metadata
    """
    try:
        from betty.config import get_skill_handler_path
        import subprocess

        audit_handler = get_skill_handler_path("audit.log")
        args = [sys.executable, audit_handler, skill_name, status]

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

        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            logger.debug(f"Failed to log audit entry for {skill_name}: {result.stderr}")
    except FileNotFoundError:
        # audit.log skill not found, skip audit logging
        pass
    except Exception as e:
        logger.debug(f"Failed to log audit entry for {skill_name}: {e}")
