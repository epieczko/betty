#!/usr/bin/env python3
"""
Hook Simulation Skill for Betty Framework

Allows developers to test a hook manifest before registering it by simulating
hook triggers and validating behavior.
"""

import argparse
import json
import os
import subprocess
import sys
import time
import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional
import glob as glob_module

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.config import (
    REQUIRED_HOOK_FIELDS,
)
from betty.enums import HookEvent, HookStatus
from betty.validation import (
    validate_hook_name,
    validate_version,
    validate_hook_event,
    validate_manifest_fields,
    ValidationError,
)
from betty.errors import BettyError


def load_hook_manifest(manifest_path: str) -> Dict[str, Any]:
    """
    Load and parse a hook manifest from a YAML file.

    Args:
        manifest_path: Path to the hook.yaml file

    Returns:
        Parsed manifest dictionary

    Raises:
        BettyError: If file doesn't exist or YAML is invalid
    """
    path = Path(manifest_path)

    if not path.exists():
        raise BettyError(f"Manifest file not found: {manifest_path}")

    try:
        with open(path, 'r') as f:
            manifest = yaml.safe_load(f)

        if not isinstance(manifest, dict):
            raise BettyError("Manifest must be a YAML dictionary")

        return manifest
    except yaml.YAMLError as e:
        raise BettyError(f"Invalid YAML in manifest: {e}")


def validate_manifest(manifest: Dict[str, Any]) -> List[str]:
    """
    Validate a hook manifest against Betty's requirements.

    Args:
        manifest: The hook manifest to validate

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    # 1. Required fields check
    try:
        missing_fields = validate_manifest_fields(manifest, REQUIRED_HOOK_FIELDS)
        if missing_fields:
            errors.append(f"Missing required fields: {', '.join(missing_fields)}")
    except (ValidationError, BettyError) as e:
        errors.append(str(e))

    # 2. Name format validation
    if "name" in manifest:
        try:
            validate_hook_name(manifest["name"])
        except (ValidationError, BettyError) as e:
            errors.append(str(e))

    # 3. Version format validation
    if "version" in manifest:
        try:
            # Convert to string if it's a number (YAML may parse "1.0" as float)
            version = manifest["version"]
            if isinstance(version, (int, float)):
                version = str(version)
                manifest["version"] = version  # Update manifest with string version
            validate_version(version)
        except (ValidationError, BettyError) as e:
            errors.append(str(e))

    # 4. Event type validation
    if "event" in manifest:
        try:
            validate_hook_event(manifest["event"])
        except (ValidationError, BettyError) as e:
            errors.append(str(e))

    # 5. Command validation
    command = manifest.get("command", "")
    if not command or not command.strip():
        errors.append("command cannot be empty")

    # 6. Blocking type validation
    if "blocking" in manifest:
        if not isinstance(manifest["blocking"], bool):
            errors.append("blocking must be a boolean (true/false)")

    # 7. Timeout validation
    if "timeout" in manifest:
        timeout = manifest["timeout"]
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            errors.append("timeout must be a positive number (in milliseconds)")

    # 8. Status validation
    if "status" in manifest:
        valid_statuses = [s.value for s in HookStatus]
        if manifest["status"] not in valid_statuses:
            errors.append(f"Invalid status: '{manifest['status']}'. Must be one of: {', '.join(valid_statuses)}")

    # 9. Pattern validation
    if "when" in manifest and "pattern" in manifest["when"]:
        pattern = manifest["when"]["pattern"]
        if not pattern or not isinstance(pattern, str):
            errors.append("when.pattern must be a non-empty string")

    return errors


def find_matching_files(pattern: str, base_path: str = ".") -> List[str]:
    """
    Find files matching a glob pattern.

    Args:
        pattern: Glob pattern to match (e.g., "*.yaml", "src/**/*.py")
        base_path: Base directory to search from

    Returns:
        List of matching file paths (relative to base_path)
    """
    base = Path(base_path).resolve()
    matches = []

    # Handle both simple patterns and recursive patterns
    if "**" in pattern:
        # Recursive glob
        for match in base.glob(pattern):
            if match.is_file():
                try:
                    rel_path = match.relative_to(base)
                    matches.append(str(rel_path))
                except ValueError:
                    matches.append(str(match))
    else:
        # Non-recursive glob
        for match in base.glob(pattern):
            if match.is_file():
                try:
                    rel_path = match.relative_to(base)
                    matches.append(str(rel_path))
                except ValueError:
                    matches.append(str(match))

    return sorted(matches)


def simulate_on_file_edit(manifest: Dict[str, Any], base_path: str = ".") -> Dict[str, Any]:
    """
    Simulate an on_file_edit hook trigger.

    Args:
        manifest: The hook manifest
        base_path: Base directory to search for matching files

    Returns:
        Simulation results dictionary
    """
    pattern = manifest.get("when", {}).get("pattern")

    if not pattern:
        return {
            "would_trigger": False,
            "reason": "No pattern specified - hook would not trigger for specific files",
            "matching_files": []
        }

    matching_files = find_matching_files(pattern, base_path)

    if not matching_files:
        return {
            "would_trigger": False,
            "reason": f"No files match pattern: {pattern}",
            "matching_files": [],
            "pattern": pattern
        }

    return {
        "would_trigger": True,
        "reason": f"Found {len(matching_files)} file(s) matching pattern: {pattern}",
        "matching_files": matching_files,
        "pattern": pattern
    }


def simulate_on_commit(manifest: Dict[str, Any], base_path: str = ".") -> Dict[str, Any]:
    """
    Simulate an on_commit hook trigger.

    Args:
        manifest: The hook manifest
        base_path: Base directory (git repository root)

    Returns:
        Simulation results dictionary
    """
    # Check if we're in a git repository
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=base_path,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            return {
                "would_trigger": False,
                "reason": "Not in a git repository",
                "git_status": None
            }
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return {
            "would_trigger": False,
            "reason": "Git not available or timeout",
            "git_status": None
        }

    # Get git status to see what would be committed
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=base_path,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            status_lines = result.stdout.strip().split("\n") if result.stdout.strip() else []
            changed_files = [line[3:] for line in status_lines if line.strip()]

            return {
                "would_trigger": True,
                "reason": f"on_commit hook would trigger with {len(changed_files)} changed file(s)",
                "changed_files": changed_files,
                "git_status": result.stdout.strip()
            }
        else:
            return {
                "would_trigger": False,
                "reason": "Could not get git status",
                "git_status": result.stderr.strip()
            }
    except subprocess.TimeoutExpired:
        return {
            "would_trigger": False,
            "reason": "Git status command timed out",
            "git_status": None
        }


def execute_command(
    command: str,
    file_path: Optional[str] = None,
    timeout_ms: int = 30000,
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Execute a hook command (or simulate execution in dry-run mode).

    Args:
        command: The command to execute
        file_path: Optional file path to substitute {file_path} placeholder
        timeout_ms: Timeout in milliseconds
        dry_run: If True, don't actually execute the command

    Returns:
        Execution results dictionary
    """
    # Substitute placeholders
    if file_path:
        command = command.replace("{file_path}", file_path)

    if dry_run:
        return {
            "command": command,
            "executed": False,
            "dry_run": True,
            "stdout": "",
            "stderr": "",
            "return_code": None,
            "execution_time_ms": 0
        }

    # Execute the command
    start_time = time.time()
    timeout_sec = timeout_ms / 1000.0

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )

        execution_time = (time.time() - start_time) * 1000

        return {
            "command": command,
            "executed": True,
            "dry_run": False,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
            "execution_time_ms": round(execution_time, 2),
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        execution_time = (time.time() - start_time) * 1000
        return {
            "command": command,
            "executed": True,
            "dry_run": False,
            "stdout": "",
            "stderr": f"Command timed out after {timeout_ms}ms",
            "return_code": -1,
            "execution_time_ms": round(execution_time, 2),
            "success": False,
            "timeout": True
        }
    except Exception as e:
        execution_time = (time.time() - start_time) * 1000
        return {
            "command": command,
            "executed": True,
            "dry_run": False,
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": -1,
            "execution_time_ms": round(execution_time, 2),
            "success": False,
            "error": str(e)
        }


def simulate_hook(manifest_path: str, dry_run: bool = True, execute: bool = False) -> Dict[str, Any]:
    """
    Main function to simulate a hook.

    Args:
        manifest_path: Path to the hook.yaml file
        dry_run: If True, don't actually execute commands
        execute: If True, execute the command on matching files

    Returns:
        Complete simulation results
    """
    results = {
        "manifest_path": manifest_path,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "valid": False,
        "validation_errors": [],
        "manifest": {},
        "trigger_simulation": {},
        "command_executions": []
    }

    # Load manifest
    try:
        manifest = load_hook_manifest(manifest_path)
        results["manifest"] = manifest
    except BettyError as e:
        results["validation_errors"].append(str(e))
        return results

    # Validate manifest
    validation_errors = validate_manifest(manifest)
    if validation_errors:
        results["validation_errors"] = validation_errors
        return results

    results["valid"] = True

    # Get base path (directory containing the manifest)
    base_path = Path(manifest_path).parent.resolve()

    # Simulate based on event type
    event = manifest.get("event")

    if event == HookEvent.ON_FILE_EDIT.value:
        trigger_result = simulate_on_file_edit(manifest, str(base_path))
        results["trigger_simulation"] = trigger_result

        # Execute command on matching files if requested
        if execute and trigger_result.get("would_trigger"):
            command = manifest.get("command", "")
            timeout = manifest.get("timeout", 30000)

            for file_path in trigger_result.get("matching_files", []):
                exec_result = execute_command(command, file_path, timeout, dry_run)
                exec_result["file"] = file_path
                results["command_executions"].append(exec_result)

    elif event == HookEvent.ON_COMMIT.value:
        trigger_result = simulate_on_commit(manifest, str(base_path))
        results["trigger_simulation"] = trigger_result

        # Execute command if requested
        if execute and trigger_result.get("would_trigger"):
            command = manifest.get("command", "")
            timeout = manifest.get("timeout", 30000)

            exec_result = execute_command(command, None, timeout, dry_run)
            results["command_executions"].append(exec_result)

    elif event == HookEvent.ON_FILE_SAVE.value:
        # Similar to on_file_edit
        trigger_result = simulate_on_file_edit(manifest, str(base_path))
        trigger_result["event_note"] = "on_file_save behaves similarly to on_file_edit for simulation purposes"
        results["trigger_simulation"] = trigger_result

        if execute and trigger_result.get("would_trigger"):
            command = manifest.get("command", "")
            timeout = manifest.get("timeout", 30000)

            for file_path in trigger_result.get("matching_files", [])[:3]:  # Limit to 3 files
                exec_result = execute_command(command, file_path, timeout, dry_run)
                exec_result["file"] = file_path
                results["command_executions"].append(exec_result)

    else:
        # For other events, just note that they would trigger
        results["trigger_simulation"] = {
            "would_trigger": True,
            "reason": f"Event '{event}' would trigger in appropriate context",
            "note": f"Full simulation not implemented for {event} events"
        }

        if execute:
            command = manifest.get("command", "")
            timeout = manifest.get("timeout", 30000)
            exec_result = execute_command(command, None, timeout, dry_run)
            results["command_executions"].append(exec_result)

    # Add metadata about blocking behavior
    results["blocking"] = manifest.get("blocking", False)
    results["timeout_ms"] = manifest.get("timeout", 30000)

    return results


def main():
    """Command-line interface for hook simulation."""
    parser = argparse.ArgumentParser(
        description="Simulate Betty Framework hook execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate and simulate hook trigger
  python hook_simulate.py examples/test-hook.yaml

  # Simulate with dry-run command execution
  python hook_simulate.py examples/test-hook.yaml --execute --dry-run

  # Actually execute the command
  python hook_simulate.py examples/test-hook.yaml --execute --no-dry-run
        """
    )

    parser.add_argument(
        "manifest",
        help="Path to hook.yaml manifest file"
    )

    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute the hook command (simulated by default)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Dry-run mode: show what would be executed without running it (default)"
    )

    parser.add_argument(
        "--no-dry-run",
        dest="dry_run",
        action="store_false",
        help="Actually execute the command"
    )

    parser.add_argument(
        "--output",
        choices=["json", "summary"],
        default="summary",
        help="Output format (default: summary)"
    )

    args = parser.parse_args()

    try:
        results = simulate_hook(args.manifest, dry_run=args.dry_run, execute=args.execute)

        if args.output == "json":
            print(json.dumps(results, indent=2))
        else:
            # Print summary
            print(f"\n=== Hook Simulation Results ===")
            print(f"Manifest: {results['manifest_path']}")
            print(f"Timestamp: {results['timestamp']}")
            print()

            if results["validation_errors"]:
                print("❌ VALIDATION FAILED")
                print("\nErrors:")
                for error in results["validation_errors"]:
                    print(f"  - {error}")
                sys.exit(1)

            print("✅ VALIDATION PASSED")
            print()

            manifest = results["manifest"]
            print(f"Hook: {manifest.get('name')} v{manifest.get('version')}")
            print(f"Event: {manifest.get('event')}")
            print(f"Command: {manifest.get('command')}")
            print(f"Blocking: {results.get('blocking')}")
            print(f"Timeout: {results.get('timeout_ms')}ms")
            print()

            trigger = results["trigger_simulation"]
            if trigger.get("would_trigger"):
                print("✅ WOULD TRIGGER")
                print(f"Reason: {trigger.get('reason')}")

                if "matching_files" in trigger and trigger["matching_files"]:
                    print(f"\nMatching files ({len(trigger['matching_files'])}):")
                    for f in trigger["matching_files"][:10]:
                        print(f"  - {f}")
                    if len(trigger["matching_files"]) > 10:
                        print(f"  ... and {len(trigger['matching_files']) - 10} more")

                if "changed_files" in trigger and trigger["changed_files"]:
                    print(f"\nChanged files ({len(trigger['changed_files'])}):")
                    for f in trigger["changed_files"][:10]:
                        print(f"  - {f}")
                    if len(trigger["changed_files"]) > 10:
                        print(f"  ... and {len(trigger['changed_files']) - 10} more")
            else:
                print("❌ WOULD NOT TRIGGER")
                print(f"Reason: {trigger.get('reason')}")

            print()

            if results["command_executions"]:
                print(f"\n=== Command Execution Results ({len(results['command_executions'])}) ===")
                for i, exec_result in enumerate(results["command_executions"], 1):
                    print(f"\n[{i}] {exec_result.get('file', 'N/A')}")
                    print(f"Command: {exec_result['command']}")

                    if exec_result.get("dry_run"):
                        print("Mode: DRY RUN (not executed)")
                    else:
                        print(f"Executed: Yes")
                        print(f"Return code: {exec_result.get('return_code')}")
                        print(f"Execution time: {exec_result.get('execution_time_ms')}ms")

                        if exec_result.get("success"):
                            print("Status: ✅ SUCCESS")
                        else:
                            print("Status: ❌ FAILED")

                        if exec_result.get("stdout"):
                            print(f"\nStdout:\n{exec_result['stdout']}")
                        if exec_result.get("stderr"):
                            print(f"\nStderr:\n{exec_result['stderr']}")

            print()

        sys.exit(0 if results["valid"] else 1)

    except BettyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
