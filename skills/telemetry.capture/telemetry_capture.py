#!/usr/bin/env python3
"""telemetry_capture.py – Implementation of the telemetry.capture Skill."""

import functools
import json
import os
import sys
import time
from typing import Any, Callable, Dict, List, Optional
from datetime import datetime, timezone, timedelta

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import REGISTRY_DIR  # noqa: E402
from betty.errors import SkillValidationError  # noqa: E402
from betty.file_utils import safe_update_json  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402

logger = setup_logger(__name__)

# Telemetry log file path
TELEMETRY_FILE = os.path.join(REGISTRY_DIR, "telemetry.json")
TELEMETRY_ARCHIVE_DIR = os.path.join(REGISTRY_DIR, "telemetry_archive")

# Rotation settings
ROTATION_DAYS = 7  # Rotate weekly
MAX_ENTRIES = 100000  # Safety limit to prevent unbounded growth


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Build a standard response dictionary."""
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "path": path,
    }

    if details is not None:
        response["details"] = details

    return response


def create_telemetry_entry(
    skill_name: str,
    inputs: Dict[str, Any],
    status: str,
    duration_ms: int,
    agent: Optional[str] = None,
    workflow: Optional[str] = None,
    caller: Optional[str] = None,
    **extra_fields: Any,
) -> Dict[str, Any]:
    """
    Create a telemetry entry.

    Args:
        skill_name: Name of the skill being tracked
        inputs: Input parameters passed to the skill
        status: Execution status (success, failed, timeout, etc.)
        duration_ms: Execution duration in milliseconds
        agent: Optional agent name that invoked the skill
        workflow: Optional workflow name in which the skill was executed
        caller: Optional caller identifier (CLI, API, etc.)
        **extra_fields: Additional custom fields to include

    Returns:
        Telemetry entry dictionary
    """
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
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


def rotate_telemetry_if_needed(telemetry_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Rotate telemetry data if the oldest entries are more than ROTATION_DAYS old.

    Archives old entries to dated archive files and returns recent entries.

    Args:
        telemetry_data: List of telemetry entries

    Returns:
        List of recent telemetry entries (within ROTATION_DAYS)
    """
    if not telemetry_data:
        return telemetry_data

    # Calculate cutoff date (entries older than this will be archived)
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=ROTATION_DAYS)

    # Separate old and recent entries
    old_entries = []
    recent_entries = []

    for entry in telemetry_data:
        try:
            entry_timestamp = datetime.fromisoformat(entry.get("timestamp", ""))
            if entry_timestamp < cutoff_date:
                old_entries.append(entry)
            else:
                recent_entries.append(entry)
        except (ValueError, TypeError):
            # If timestamp is invalid, keep it in recent entries
            recent_entries.append(entry)

    # Archive old entries if any exist
    if old_entries:
        try:
            os.makedirs(TELEMETRY_ARCHIVE_DIR, exist_ok=True)

            # Group old entries by week
            entries_by_week = {}
            for entry in old_entries:
                try:
                    timestamp = datetime.fromisoformat(entry.get("timestamp", ""))
                    # Use ISO week date format (YYYY-Www)
                    week_key = timestamp.strftime("%Y-W%W")
                    if week_key not in entries_by_week:
                        entries_by_week[week_key] = []
                    entries_by_week[week_key].append(entry)
                except (ValueError, TypeError):
                    # Skip entries with invalid timestamps
                    continue

            # Write each week's entries to separate archive files
            for week_key, entries in entries_by_week.items():
                archive_file = os.path.join(TELEMETRY_ARCHIVE_DIR, f"telemetry-{week_key}.json")

                # If archive file exists, append to it; otherwise create new
                existing_entries = []
                if os.path.exists(archive_file):
                    try:
                        with open(archive_file, 'r') as f:
                            existing_entries = json.load(f)
                            if not isinstance(existing_entries, list):
                                existing_entries = []
                    except (json.JSONDecodeError, IOError):
                        existing_entries = []

                # Combine and write
                all_archived_entries = existing_entries + entries
                with open(archive_file, 'w') as f:
                    json.dump(all_archived_entries, f, indent=2)

                logger.info(f"Archived {len(entries)} entries to {archive_file}")

        except Exception as e:
            logger.warning(f"Failed to archive old telemetry entries: {e}")
            # On archive failure, keep old entries in the main file
            return telemetry_data

    return recent_entries


def capture_telemetry(entry: Dict[str, Any]) -> Dict[str, Any]:
    """
    Append a telemetry entry to the telemetry log file.

    Uses thread-safe file operations with locking.
    Implements weekly rotation: entries older than 7 days are archived.

    Args:
        entry: Telemetry entry to append

    Returns:
        Result dictionary with capture status
    """
    def update_fn(telemetry_data):
        """Update function for safe_update_json."""
        if not isinstance(telemetry_data, list):
            telemetry_data = []

        # Perform weekly rotation check
        telemetry_data = rotate_telemetry_if_needed(telemetry_data)

        # Append new entry
        telemetry_data.append(entry)

        # Safety limit: keep only last MAX_ENTRIES to prevent unbounded growth
        # This is a fallback in case rotation doesn't work or entries accumulate too quickly
        if len(telemetry_data) > MAX_ENTRIES:
            telemetry_data = telemetry_data[-MAX_ENTRIES:]
            logger.warning(f"Telemetry log exceeded {MAX_ENTRIES} entries, truncating to safety limit")

        return telemetry_data

    try:
        # Ensure registry directory exists
        os.makedirs(REGISTRY_DIR, exist_ok=True)

        # Use safe atomic update with file locking
        updated_log = safe_update_json(TELEMETRY_FILE, update_fn, default=[])

        result = {
            "status": "success",
            "telemetry_entry": entry,
            "telemetry_path": TELEMETRY_FILE,
            "total_entries": len(updated_log),
        }

        logger.info(f"Telemetry captured for: {entry.get('skill')}")
        return result

    except Exception as e:
        logger.error(f"Failed to capture telemetry: {e}")
        raise SkillValidationError(f"Failed to capture telemetry: {e}")


def telemetry_decorator(skill_name: Optional[str] = None, caller: Optional[str] = None):
    """
    Decorator to automatically capture telemetry for function calls.

    Usage:
        @telemetry_decorator(skill_name="my.skill", caller="cli")
        def my_function(arg1, arg2):
            return result

    Args:
        skill_name: Name of the skill (defaults to function name)
        caller: Caller identifier (CLI, API, etc.)

    Returns:
        Decorated function that captures telemetry
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            error = None
            result = None

            # Use skill_name if provided, otherwise use function name
            actual_skill_name = skill_name or func.__name__

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

                # Prepare inputs - sanitize to avoid capturing sensitive data
                inputs = {
                    "args_count": len(args),
                    "kwargs_keys": list(kwargs.keys()),
                }

                # Create telemetry entry
                try:
                    entry = create_telemetry_entry(
                        skill_name=actual_skill_name,
                        inputs=inputs,
                        status=status,
                        duration_ms=duration_ms,
                        caller=caller,
                        error=error if error else None,
                    )

                    # Capture telemetry (non-blocking, errors are logged but don't affect execution)
                    capture_telemetry(entry)
                except Exception as telemetry_error:
                    logger.warning(f"Failed to capture telemetry for {actual_skill_name}: {telemetry_error}")

        return wrapper
    return decorator


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    if len(argv) < 4:
        message = "Usage: telemetry_capture.py <skill_name> <inputs_json> <status> <duration_ms> [agent] [workflow] [caller]"
        logger.error(message)
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1

    skill_name = argv[0]
    status = argv[2]

    # Parse inputs JSON
    try:
        inputs = json.loads(argv[1])
        if not isinstance(inputs, dict):
            inputs = {"value": inputs}
    except json.JSONDecodeError:
        logger.error(f"Invalid inputs JSON: {argv[1]}")
        response = build_response(
            False,
            path="",
            errors=[f"Invalid inputs JSON: {argv[1]}"],
        )
        print(json.dumps(response, indent=2))
        return 1

    # Parse duration_ms
    try:
        duration_ms = int(argv[3])
    except ValueError:
        logger.error(f"Invalid duration_ms value: {argv[3]}")
        response = build_response(
            False,
            path="",
            errors=[f"Invalid duration_ms value: {argv[3]}"],
        )
        print(json.dumps(response, indent=2))
        return 1

    # Parse optional arguments
    agent = argv[4] if len(argv) > 4 and argv[4] else None
    workflow = argv[5] if len(argv) > 5 and argv[5] else None
    caller = argv[6] if len(argv) > 6 and argv[6] else None

    try:
        # Create telemetry entry
        entry = create_telemetry_entry(
            skill_name=skill_name,
            inputs=inputs,
            status=status,
            duration_ms=duration_ms,
            agent=agent,
            workflow=workflow,
            caller=caller,
        )

        # Capture telemetry
        result = capture_telemetry(entry)

        response = build_response(
            True,
            path=result.get("telemetry_path", TELEMETRY_FILE),
            errors=[],
            details=result,
        )
        print(json.dumps(response, indent=2))
        return 0

    except SkillValidationError as exc:
        logger.error("Telemetry capture failed: %s", exc)
        response = build_response(
            False,
            path=TELEMETRY_FILE,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc), "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1
    except Exception as exc:  # pragma: no cover - unexpected failures
        logger.exception("Unexpected error during telemetry capture")
        response = build_response(
            False,
            path=TELEMETRY_FILE,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc)}},
        )
        print(json.dumps(response, indent=2))
        return 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main(sys.argv[1:]))
