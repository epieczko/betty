#!/usr/bin/env python3
"""
Define and register validation hooks for Claude Code.

This skill creates hook configurations in .claude/hooks.yaml that automatically
trigger validation skills on events like file edits, commits, and pushes.
"""

import sys
import json
import argparse
import os
from pathlib import Path
from typing import Dict, Any, Optional

# Add betty module to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_path
from betty.file_utils import safe_read_json, safe_write_json

logger = setup_logger(__name__)

# Valid hook events
VALID_EVENTS = [
    "on_file_edit",
    "on_file_save",
    "on_commit",
    "on_push",
    "on_tool_use",
    "on_agent_start",
    "on_workflow_end"
]


def create_hooks_directory() -> Path:
    """
    Create .claude directory if it doesn't exist.

    Returns:
        Path to .claude directory
    """
    claude_dir = Path.cwd() / ".claude"
    claude_dir.mkdir(exist_ok=True)
    logger.info(f"Ensured .claude directory exists at {claude_dir}")
    return claude_dir


def load_existing_hooks(hooks_file: Path) -> Dict[str, Any]:
    """
    Load existing hooks configuration if it exists.

    Args:
        hooks_file: Path to hooks.yaml file

    Returns:
        Existing hooks configuration or empty structure
    """
    if hooks_file.exists():
        try:
            import yaml
            with open(hooks_file, 'r') as f:
                config = yaml.safe_load(f) or {}
            logger.info(f"Loaded existing hooks from {hooks_file}")
            return config
        except Exception as e:
            logger.warning(f"Could not load existing hooks: {e}")
            return {"hooks": {}}
    else:
        logger.info(f"No existing hooks file found at {hooks_file}")
        return {"hooks": {}}


def create_hook_config(
    event: str,
    command: str,
    pattern: Optional[str] = None,
    blocking: bool = True,
    timeout: int = 30000,
    description: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a hook configuration object.

    Args:
        event: Hook event trigger
        command: Command to execute
        pattern: File pattern to match (optional)
        blocking: Whether hook should block on failure
        timeout: Timeout in milliseconds
        description: Human-readable description

    Returns:
        Hook configuration dictionary
    """
    # Generate a name from the command and pattern
    if pattern:
        name = f"{command.replace('/', '-').replace('.', '-')}-{pattern.replace('*', 'all').replace('/', '-')}"
    else:
        name = command.replace('/', '-').replace('.', '-')

    hook_config = {
        "name": name,
        "command": command,
        "blocking": blocking,
        "timeout": timeout
    }

    if pattern:
        hook_config["when"] = {"pattern": pattern}

    if description:
        hook_config["description"] = description
    else:
        hook_config["description"] = f"Auto-generated hook for {command}"

    return hook_config


def add_hook_to_config(
    config: Dict[str, Any],
    event: str,
    hook_config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Add a hook to the configuration, avoiding duplicates.

    Args:
        config: Existing hooks configuration
        event: Event to add hook to
        hook_config: Hook configuration to add

    Returns:
        Updated configuration
    """
    if "hooks" not in config:
        config["hooks"] = {}

    if event not in config["hooks"]:
        config["hooks"][event] = []

    # Check if hook with same name already exists
    existing_names = [h.get("name") for h in config["hooks"][event]]
    if hook_config["name"] in existing_names:
        # Update existing hook
        for i, hook in enumerate(config["hooks"][event]):
            if hook.get("name") == hook_config["name"]:
                config["hooks"][event][i] = hook_config
                logger.info(f"Updated existing hook: {hook_config['name']}")
                break
    else:
        # Add new hook
        config["hooks"][event].append(hook_config)
        logger.info(f"Added new hook: {hook_config['name']}")

    return config


def save_hooks_config(hooks_file: Path, config: Dict[str, Any]) -> None:
    """
    Save hooks configuration to YAML file.

    Args:
        hooks_file: Path to hooks.yaml file
        config: Configuration to save
    """
    try:
        import yaml
        with open(hooks_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        logger.info(f"Saved hooks configuration to {hooks_file}")
    except Exception as e:
        raise BettyError(f"Failed to save hooks configuration: {e}")


def define_hook(
    event: str,
    command: str,
    pattern: Optional[str] = None,
    blocking: bool = True,
    timeout: int = 30000,
    description: Optional[str] = None
) -> Dict[str, Any]:
    """
    Define a new hook or update an existing one.

    Args:
        event: Hook event trigger
        command: Command to execute
        pattern: File pattern to match
        blocking: Whether hook should block on failure
        timeout: Timeout in milliseconds
        description: Human-readable description

    Returns:
        Result dictionary with hook config and file path
    """
    # Validate event
    if event not in VALID_EVENTS:
        raise BettyError(
            f"Invalid event '{event}'. Valid events: {', '.join(VALID_EVENTS)}"
        )

    # Create .claude directory
    claude_dir = create_hooks_directory()
    hooks_file = claude_dir / "hooks.yaml"

    # Load existing hooks
    config = load_existing_hooks(hooks_file)

    # Create new hook config
    hook_config = create_hook_config(
        event=event,
        command=command,
        pattern=pattern,
        blocking=blocking,
        timeout=timeout,
        description=description
    )

    # Add to configuration
    config = add_hook_to_config(config, event, hook_config)

    # Save configuration
    save_hooks_config(hooks_file, config)

    return {
        "hook_config": hook_config,
        "hooks_file_path": str(hooks_file),
        "event": event,
        "total_hooks": len(config.get("hooks", {}).get(event, []))
    }


def main():
    parser = argparse.ArgumentParser(
        description="Define and register validation hooks for Claude Code"
    )
    parser.add_argument(
        "event",
        type=str,
        choices=VALID_EVENTS,
        help="Hook event trigger"
    )
    parser.add_argument(
        "command",
        type=str,
        help="Command to execute when hook triggers"
    )
    parser.add_argument(
        "--pattern",
        type=str,
        help="File pattern to match (e.g., '*.openapi.yaml')"
    )
    parser.add_argument(
        "--blocking",
        type=lambda x: x.lower() in ['true', '1', 'yes'],
        default=True,
        help="Whether hook should block on failure (default: true)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30000,
        help="Timeout in milliseconds (default: 30000)"
    )
    parser.add_argument(
        "--description",
        type=str,
        help="Human-readable description of what the hook does"
    )

    args = parser.parse_args()

    try:
        # Check if PyYAML is installed
        try:
            import yaml
        except ImportError:
            raise BettyError(
                "PyYAML is required for hook.define. Install with: pip install pyyaml"
            )

        # Define the hook
        logger.info(f"Defining hook for event '{args.event}' with command '{args.command}'")
        result = define_hook(
            event=args.event,
            command=args.command,
            pattern=args.pattern,
            blocking=args.blocking,
            timeout=args.timeout,
            description=args.description
        )

        # Return structured result
        output = {
            "status": "success",
            "data": result
        }
        print(json.dumps(output, indent=2))

    except Exception as e:
        logger.error(f"Failed to define hook: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
