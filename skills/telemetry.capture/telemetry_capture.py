#!/usr/bin/env python3
"""
Betty Framework - Telemetry Capture Skill
Logs usage of core Betty components to /registry/telemetry.json
"""

import json
import os
import sys
import fcntl
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


class TelemetryCapture:
    """Thread-safe telemetry capture for Betty Framework components."""

    def __init__(self, telemetry_file: str = "/home/user/betty/registry/telemetry.json"):
        self.telemetry_file = Path(telemetry_file)
        self._ensure_telemetry_file()

    def _ensure_telemetry_file(self) -> None:
        """Ensure telemetry file exists with valid JSON structure."""
        self.telemetry_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.telemetry_file.exists():
            # Use simple list format to match existing telemetry.json
            initial_data = []
            with open(self.telemetry_file, 'w') as f:
                json.dump(initial_data, f, indent=2)

    def capture(
        self,
        skill: str,
        status: str,
        duration_ms: float,
        caller: str,
        inputs: Optional[Dict[str, Any]] = None,
        error_message: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Capture telemetry event and append to telemetry.json (thread-safe).

        Args:
            skill: Name of the skill/component (e.g., 'plugin.build', 'agent.run')
            status: Execution status ('success', 'failure', 'timeout', 'error')
            duration_ms: Execution duration in milliseconds
            caller: Source of the call (e.g., 'CLI', 'API', 'workflow.compose')
            inputs: Input parameters (sanitized, no secrets)
            error_message: Error message if status is failure/error
            metadata: Additional context (e.g., user, session_id, environment)

        Returns:
            Dict containing the captured telemetry entry
        """
        # Validate inputs
        if status not in ['success', 'failure', 'timeout', 'error', 'pending']:
            raise ValueError(f"Invalid status: {status}. Must be one of: success, failure, timeout, error, pending")

        # Build telemetry entry
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "skill": skill,
            "status": status,
            "duration_ms": float(duration_ms),
            "caller": caller,
            "inputs": inputs or {},
            "error_message": error_message,
            "metadata": metadata or {}
        }

        # Thread-safe append to telemetry.json
        self._append_entry(entry)

        return entry

    def _append_entry(self, entry: Dict[str, Any]) -> None:
        """
        Append entry to telemetry file with file locking for thread safety.

        Uses fcntl.flock for POSIX systems to ensure atomic writes.
        """
        with open(self.telemetry_file, 'r+') as f:
            # Acquire exclusive lock
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)

            try:
                # Read current data (simple list format)
                f.seek(0)
                data = json.load(f)

                # Ensure data is a list
                if not isinstance(data, list):
                    data = []

                # Append new entry
                data.append(entry)

                # Keep last 100,000 entries (safety limit)
                if len(data) > 100000:
                    data = data[-100000:]

                # Write back (truncate and rewrite)
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=2)
                f.write('\n')  # Add newline at end

            finally:
                # Release lock
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def query(
        self,
        skill: Optional[str] = None,
        status: Optional[str] = None,
        caller: Optional[str] = None,
        limit: Optional[int] = None
    ) -> list:
        """
        Query telemetry entries with optional filters.

        Args:
            skill: Filter by skill name
            status: Filter by status
            caller: Filter by caller
            limit: Maximum number of entries to return (most recent first)

        Returns:
            List of matching telemetry entries
        """
        with open(self.telemetry_file, 'r') as f:
            data = json.load(f)

        # Data is a simple list
        entries = data if isinstance(data, list) else []

        # Apply filters
        if skill:
            entries = [e for e in entries if e.get("skill") == skill]
        if status:
            entries = [e for e in entries if e.get("status") == status]
        if caller:
            entries = [e for e in entries if e.get("caller") == caller]

        # Sort by timestamp (most recent first) and limit
        entries = sorted(entries, key=lambda e: e.get("timestamp", ""), reverse=True)

        if limit:
            entries = entries[:limit]

        return entries


def main():
    """CLI entrypoint for telemetry capture."""
    if len(sys.argv) < 5:
        print("Usage: python telemetry_capture.py <skill> <status> <duration_ms> <caller> [inputs_json]")
        print("\nExample:")
        print('  python telemetry_capture.py plugin.build success 320 CLI')
        print('  python telemetry_capture.py agent.run failure 1500 API \'{"agent": "api.designer"}\'')
        sys.exit(1)

    skill = sys.argv[1]
    status = sys.argv[2]
    duration_ms = float(sys.argv[3])
    caller = sys.argv[4]

    # Parse inputs if provided
    inputs = {}
    if len(sys.argv) > 5:
        try:
            inputs = json.loads(sys.argv[5])
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON for inputs: {e}", file=sys.stderr)
            sys.exit(1)

    # Parse error message if provided
    error_message = None
    if len(sys.argv) > 6:
        error_message = sys.argv[6]

    # Capture telemetry
    try:
        telemetry = TelemetryCapture()
        entry = telemetry.capture(
            skill=skill,
            status=status,
            duration_ms=duration_ms,
            caller=caller,
            inputs=inputs,
            error_message=error_message
        )

        print(json.dumps(entry, indent=2))
        print(f"\n✓ Telemetry captured to {telemetry.telemetry_file}")

    except Exception as e:
        print(f"Error capturing telemetry: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
