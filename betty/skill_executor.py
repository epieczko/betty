"""
skill_executor.py - In-process skill execution utilities.

This module provides utilities to execute Betty skills in-process using dynamic
imports instead of subprocess calls. This is essential for compatibility with
environments like Claude Code that don't support forking or background processes.
"""

import importlib.util
import sys
import json
import os
from typing import Dict, Any, List, Optional
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

from betty.config import get_skill_handler_path
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def execute_skill_in_process(
    skill_name: str,
    args: Optional[List[str]] = None,
    timeout: Optional[int] = None
) -> Dict[str, Any]:
    """
    Execute a Betty skill in-process using dynamic imports.

    Args:
        skill_name: Name of the skill (e.g., "audit.log", "workflow.validate")
        args: List of command-line arguments to pass to the skill
        timeout: Optional timeout in seconds (currently not implemented for in-process)

    Returns:
        Dictionary with execution results:
        {
            "stdout": str,
            "stderr": str,
            "returncode": int,
            "parsed": Optional[Dict],  # Parsed JSON output if available
            "parse_error": Optional[str]  # JSON parse error if parsing failed
        }

    Raises:
        Exception: If the skill module cannot be imported or execution fails
    """
    args = args or []

    # Get the file path to the skill handler
    handler_path = get_skill_handler_path(skill_name)

    logger.info(f"▶ Executing skill {skill_name} in-process from {handler_path}")

    try:
        # Check if the skill handler file exists
        if not os.path.exists(handler_path):
            error_msg = f"Skill handler not found: {handler_path}"
            logger.error(error_msg)
            return {
                "stdout": "",
                "stderr": error_msg,
                "returncode": 1,
                "parsed": None,
                "parse_error": None
            }

        # Dynamically import the skill module from file path
        module_name = skill_name.replace('.', '_')
        spec = importlib.util.spec_from_file_location(module_name, handler_path)

        if spec is None or spec.loader is None:
            error_msg = f"Failed to load module spec for {handler_path}"
            logger.error(error_msg)
            return {
                "stdout": "",
                "stderr": error_msg,
                "returncode": 1,
                "parsed": None,
                "parse_error": None
            }

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        # Check if the module has a main() function
        if not hasattr(module, "main"):
            error_msg = f"Skill module {handler_path} has no main() function"
            logger.error(error_msg)
            return {
                "stdout": "",
                "stderr": error_msg,
                "returncode": 1,
                "parsed": None,
                "parse_error": None
            }

        # Capture stdout and stderr
        stdout_capture = StringIO()
        stderr_capture = StringIO()

        # Save original sys.argv
        original_argv = sys.argv
        returncode = 0

        try:
            # Set sys.argv to simulate command-line invocation
            # The skill handler path would be argv[0], followed by arguments
            handler_path = get_skill_handler_path(skill_name)
            sys.argv = [handler_path] + args

            # Redirect stdout/stderr and execute the main function
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                try:
                    # Call the main function
                    result = module.main()

                    # If main() returns an int, use it as return code
                    if isinstance(result, int):
                        returncode = result
                    else:
                        returncode = 0

                except SystemExit as e:
                    # Catch sys.exit() calls and use the exit code
                    returncode = e.code if isinstance(e.code, int) else 1

        finally:
            # Restore original sys.argv
            sys.argv = original_argv

        # Get captured output
        stdout_str = stdout_capture.getvalue()
        stderr_str = stderr_capture.getvalue()

        logger.info(stdout_str)
        if stderr_str:
            logger.warning(f"Stderr: {stderr_str}")

        # Try to parse JSON output
        parsed, parse_error = _parse_json_output(stdout_str)

        return {
            "stdout": stdout_str,
            "stderr": stderr_str,
            "returncode": returncode,
            "parsed": parsed,
            "parse_error": parse_error
        }

    except Exception as e:
        error_msg = f"Failed to execute skill {skill_name}: {str(e)}"
        logger.error(error_msg)
        import traceback
        traceback.print_exc()
        return {
            "stdout": "",
            "stderr": error_msg,
            "returncode": 1,
            "parsed": None,
            "parse_error": None
        }


def _parse_json_output(output: str) -> tuple[Optional[Any], Optional[str]]:
    """
    Attempt to parse JSON from skill output.

    Args:
        output: String output from skill execution

    Returns:
        Tuple of (parsed_json, error_message)
    """
    stripped = output.strip()
    if not stripped:
        return None, None

    try:
        return json.loads(stripped), None
    except json.JSONDecodeError as exc:
        # Try to find JSON by removing lines from the start
        lines = stripped.splitlines()
        for idx in range(len(lines)):
            candidate = "\n".join(lines[idx:])
            try:
                return json.loads(candidate), None
            except json.JSONDecodeError:
                continue
        return None, str(exc)


def execute_skill_with_inputs(
    skill_name: str,
    inputs: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Execute a skill with structured inputs instead of command-line arguments.

    This is useful for workflow steps that have structured input parameters.
    Converts the inputs dict into command-line arguments.

    Args:
        skill_name: Name of the skill to execute
        inputs: Dictionary of input parameters

    Returns:
        Execution result dictionary (same format as execute_skill_in_process)
    """
    inputs = inputs or {}

    # Convert inputs dict to command-line arguments
    args = []
    for key, value in inputs.items():
        if isinstance(value, bool):
            if value:
                args.append(f"--{key}")
        elif isinstance(value, list):
            for item in value:
                args.extend([f"--{key}", str(item)])
        else:
            args.extend([f"--{key}", str(value)])

    return execute_skill_in_process(skill_name, args)
