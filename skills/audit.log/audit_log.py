#!/usr/bin/env python3
"""audit_log.py – Implementation of the audit.log Skill."""

import json
import os
import sys
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import REGISTRY_DIR  # noqa: E402
from betty.errors import SkillValidationError  # noqa: E402
from betty.file_utils import safe_update_json  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402

logger = setup_logger(__name__)

# Audit log file path
AUDIT_LOG_FILE = os.path.join(REGISTRY_DIR, "audit_log.json")


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


def create_audit_entry(
    skill_name: str,
    status: str,
    duration_ms: Optional[int] = None,
    errors: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create an audit log entry.

    Args:
        skill_name: Name of the skill being audited
        status: Execution status (success, failed, timeout, etc.)
        duration_ms: Execution duration in milliseconds
        errors: List of errors (if any)
        metadata: Additional metadata about the execution

    Returns:
        Audit entry dictionary
    """
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "skill": skill_name,
        "status": status,
    }

    if duration_ms is not None:
        entry["duration_ms"] = duration_ms

    if errors:
        entry["errors"] = errors

    if metadata:
        entry["metadata"] = metadata

    return entry


def append_audit_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    """
    Append an audit entry to the audit log file.

    Uses thread-safe file operations with locking.

    Args:
        entry: Audit entry to append

    Returns:
        Result dictionary with append status
    """
    def update_fn(audit_data):
        """Update function for safe_update_json."""
        if not isinstance(audit_data, list):
            audit_data = []

        audit_data.append(entry)

        # Keep only last 10000 entries to prevent unbounded growth
        return audit_data[-10000:]

    try:
        # Ensure registry directory exists
        os.makedirs(REGISTRY_DIR, exist_ok=True)

        # Use safe atomic update with file locking
        updated_log = safe_update_json(AUDIT_LOG_FILE, update_fn, default=[])

        result = {
            "status": "success",
            "audit_entry": entry,
            "audit_log_path": AUDIT_LOG_FILE,
            "total_entries": len(updated_log),
        }

        logger.info(f"✅ Audit entry logged for: {entry.get('skill')}")
        return result

    except Exception as e:
        logger.error(f"Failed to append audit entry: {e}")
        raise SkillValidationError(f"Failed to append audit entry: {e}")


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    if len(argv) < 2:
        message = "Usage: audit_log.py <skill_name> <status> [duration_ms] [errors_json] [metadata_json]"
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
    status = argv[1]
    duration_ms = None
    errors = None
    metadata = None

    # Parse optional arguments
    if len(argv) > 2 and argv[2]:
        try:
            duration_ms = int(argv[2])
        except ValueError:
            logger.warning(f"Invalid duration_ms value: {argv[2]}, ignoring")

    if len(argv) > 3 and argv[3]:
        try:
            errors = json.loads(argv[3])
            if not isinstance(errors, list):
                errors = [str(errors)]
        except json.JSONDecodeError:
            logger.warning(f"Invalid errors JSON: {argv[3]}, treating as single error")
            errors = [argv[3]]

    if len(argv) > 4 and argv[4]:
        try:
            metadata = json.loads(argv[4])
            if not isinstance(metadata, dict):
                metadata = {"value": metadata}
        except json.JSONDecodeError:
            logger.warning(f"Invalid metadata JSON: {argv[4]}, ignoring")

    try:
        # Create audit entry
        entry = create_audit_entry(
            skill_name=skill_name,
            status=status,
            duration_ms=duration_ms,
            errors=errors,
            metadata=metadata,
        )

        # Append to audit log
        result = append_audit_entry(entry)

        response = build_response(
            True,
            path=result.get("audit_log_path", AUDIT_LOG_FILE),
            errors=[],
            details=result,
        )
        print(json.dumps(response, indent=2))
        return 0

    except SkillValidationError as exc:
        logger.error("Audit logging failed: %s", exc)
        response = build_response(
            False,
            path=AUDIT_LOG_FILE,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc), "details": {}}},
        )
        print(json.dumps(response, indent=2))
        return 1
    except Exception as exc:  # pragma: no cover - unexpected failures
        logger.exception("Unexpected error during audit logging")
        response = build_response(
            False,
            path=AUDIT_LOG_FILE,
            errors=[str(exc)],
            details={"error": {"error": type(exc).__name__, "message": str(exc)}},
        )
        print(json.dumps(response, indent=2))
        return 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main(sys.argv[1:]))
