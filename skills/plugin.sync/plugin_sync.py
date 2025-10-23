#!/usr/bin/env python3
"""
plugin_sync.py – Implementation of the plugin.sync Skill
Generates plugin.yaml from registry files (skills.json, commands.json, hooks.json).
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_registry_file(registry_path: str) -> Dict[str, Any]:
    """
    Load a JSON registry file.

    Args:
        registry_path: Path to the registry JSON file

    Returns:
        Parsed registry data

    Raises:
        FileNotFoundError: If registry file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    try:
        with open(registry_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Registry file not found: {registry_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {registry_path}: {e}")
        raise


def check_handler_exists(handler_path: str, skill_name: str) -> Dict[str, Any]:
    """
    Check if a handler file exists on disk.

    Args:
        handler_path: Relative path to handler file
        skill_name: Name of the skill

    Returns:
        Dictionary with exists flag and full path
    """
    full_path = os.path.join(BASE_DIR, "skills", skill_name, handler_path)
    exists = os.path.exists(full_path)

    return {
        "exists": exists,
        "path": full_path,
        "relative_path": f"skills/{skill_name}/{handler_path}"
    }


def convert_skill_to_command(skill: Dict[str, Any], entrypoint: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a skill registry entry with entrypoint to a plugin.yaml command format.

    Args:
        skill: Skill entry from skills.json
        entrypoint: Entrypoint entry from the skill

    Returns:
        Command dictionary in plugin.yaml format
    """
    # Extract command name (remove leading slash if present)
    command_name = entrypoint.get("command", "").lstrip("/")

    # Build handler section
    handler_path = f"skills/{skill['name']}/{entrypoint.get('handler', '')}"

    command = {
        "name": command_name,
        "description": entrypoint.get("description") or skill.get("description", ""),
        "handler": {
            "runtime": entrypoint.get("runtime", "python"),
            "script": handler_path
        }
    }

    # Add parameters if present
    if "parameters" in entrypoint:
        command["parameters"] = entrypoint["parameters"]

    # Add permissions if present
    if "permissions" in entrypoint:
        # Convert permissions list to proper format if needed
        permissions = entrypoint["permissions"]
        if isinstance(permissions, list):
            command["permissions"] = permissions

    return command


def generate_plugin_yaml(
    skills_data: Dict[str, Any],
    commands_data: Dict[str, Any],
    hooks_data: Dict[str, Any]
) -> tuple[Dict[str, Any], List[str]]:
    """
    Generate plugin.yaml content from registry data.

    Args:
        skills_data: Parsed skills.json
        commands_data: Parsed commands.json
        hooks_data: Parsed hooks.json

    Returns:
        Tuple of (plugin_yaml_dict, list of warnings)
    """
    warnings = []
    commands = []

    # Load existing plugin.yaml to preserve header content
    plugin_yaml_path = os.path.join(BASE_DIR, "plugin.yaml")
    base_config = {}

    try:
        with open(plugin_yaml_path) as f:
            base_config = yaml.safe_load(f) or {}
            logger.info(f"Loaded existing plugin.yaml as template")
    except FileNotFoundError:
        logger.warning("No existing plugin.yaml found, creating from scratch")
        base_config = {
            "name": "betty-framework",
            "version": "1.0.0",
            "description": "Betty Framework - Structured AI-assisted engineering",
            "author": {
                "name": "RiskExec",
                "email": "platform@riskexec.com",
                "url": "https://github.com/epieczko/betty"
            },
            "license": "MIT"
        }

    # Process active skills with entrypoints
    skills = skills_data.get("skills", [])
    for skill in skills:
        if skill.get("status") != "active":
            continue

        entrypoints = skill.get("entrypoints", [])
        if not entrypoints:
            continue

        skill_name = skill.get("name")

        for entrypoint in entrypoints:
            handler = entrypoint.get("handler")
            if not handler:
                warnings.append(f"Skill '{skill_name}' has entrypoint without handler")
                continue

            # Check if handler exists on disk
            handler_check = check_handler_exists(handler, skill_name)
            if not handler_check["exists"]:
                warnings.append(
                    f"Handler not found for '{skill_name}': {handler_check['relative_path']}"
                )

            # Convert to plugin command format
            command = convert_skill_to_command(skill, entrypoint)
            commands.append(command)

            logger.info(f"Added command: /{command['name']} from skill {skill_name}")

    # Process commands from commands.json (if any need to be added)
    # Note: Most commands should already be represented via skills
    # This is mainly for custom commands that don't map to skills
    registry_commands = commands_data.get("commands", [])
    for cmd in registry_commands:
        if cmd.get("status") == "active":
            # Check if this command is already in our list
            cmd_name = cmd.get("name", "").lstrip("/")
            if not any(c["name"] == cmd_name for c in commands):
                logger.info(f"Command '{cmd_name}' in registry but no matching active skill found")

    # Build final plugin.yaml structure
    plugin_config = {
        **base_config,
        "commands": commands
    }

    # Add metadata about generation
    if "metadata" not in plugin_config:
        plugin_config["metadata"] = {}

    plugin_config["metadata"]["generated_at"] = datetime.now(timezone.utc).isoformat()
    plugin_config["metadata"]["generated_by"] = "plugin.sync skill"
    plugin_config["metadata"]["skill_count"] = len([s for s in skills if s.get("status") == "active"])
    plugin_config["metadata"]["command_count"] = len(commands)

    return plugin_config, warnings


def write_plugin_yaml(plugin_config: Dict[str, Any], output_path: str):
    """
    Write plugin.yaml to disk with proper formatting.

    Args:
        plugin_config: Plugin configuration dictionary
        output_path: Path where to write plugin.yaml
    """
    # Add header comment
    header = """# Betty Framework - Claude Code Plugin
# Auto-generated by plugin.sync skill
# DO NOT EDIT MANUALLY - Run plugin.sync to regenerate

"""

    with open(output_path, 'w') as f:
        f.write(header)
        yaml.dump(plugin_config, f, default_flow_style=False, sort_keys=False, indent=2)

    logger.info(f"✅ Written plugin.yaml to {output_path}")


def main():
    """Main CLI entry point."""
    logger.info("Starting plugin.yaml generation from registries...")

    # Define registry paths
    skills_path = os.path.join(BASE_DIR, "registry", "skills.json")
    commands_path = os.path.join(BASE_DIR, "registry", "commands.json")
    hooks_path = os.path.join(BASE_DIR, "registry", "hooks.json")

    try:
        # Load registry files
        logger.info("Loading registry files...")
        skills_data = load_registry_file(skills_path)
        commands_data = load_registry_file(commands_path)
        hooks_data = load_registry_file(hooks_path)

        # Generate plugin.yaml content
        logger.info("Generating plugin.yaml configuration...")
        plugin_config, warnings = generate_plugin_yaml(skills_data, commands_data, hooks_data)

        # Write to file
        output_path = os.path.join(BASE_DIR, "plugin.yaml")
        write_plugin_yaml(plugin_config, output_path)

        # Report results
        result = {
            "ok": True,
            "status": "success",
            "output_path": output_path,
            "commands_generated": len(plugin_config.get("commands", [])),
            "warnings": warnings
        }

        # Print warnings if any
        if warnings:
            logger.warning("⚠️  Warnings during generation:")
            for warning in warnings:
                logger.warning(f"  - {warning}")

        # Print summary
        logger.info(f"✅ Generated {result['commands_generated']} commands")
        logger.info(f"📄 Output: {output_path}")

        print(json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to generate plugin.yaml: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
