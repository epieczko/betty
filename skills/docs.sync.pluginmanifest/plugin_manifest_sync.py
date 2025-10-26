#!/usr/bin/env python3
"""
plugin_manifest_sync.py – Implementation of the docs.sync.plugin_manifest Skill
Reconciles plugin.yaml with registry files to ensure consistency and completeness.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Tuple, Optional
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Load a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Parsed JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {file_path}: {e}")
        raise


def load_yaml_file(file_path: str) -> Dict[str, Any]:
    """
    Load a YAML file.

    Args:
        file_path: Path to the YAML file

    Returns:
        Parsed YAML data

    Raises:
        FileNotFoundError: If file doesn't exist
        yaml.YAMLError: If YAML is invalid
    """
    try:
        with open(file_path) as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        logger.error(f"Failed to parse YAML from {file_path}: {e}")
        raise


def normalize_command_name(name: str) -> str:
    """
    Normalize command name by removing leading slash and converting to consistent format.

    Args:
        name: Command name (e.g., "/skill/define" or "skill/define")

    Returns:
        Normalized command name (e.g., "skill/define")
    """
    return name.lstrip("/")


def build_registry_index(skills_data: Dict[str, Any], commands_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Build an index of all active entrypoints from registries.

    Args:
        skills_data: Parsed skills.json
        commands_data: Parsed commands.json

    Returns:
        Dictionary mapping command names to their source data
    """
    index = {}

    # Index skills with entrypoints
    for skill in skills_data.get("skills", []):
        if skill.get("status") != "active":
            continue

        skill_name = skill.get("name")
        entrypoints = skill.get("entrypoints", [])

        for entrypoint in entrypoints:
            command = normalize_command_name(entrypoint.get("command", ""))
            if command:
                index[command] = {
                    "type": "skill",
                    "source": skill_name,
                    "skill": skill,
                    "entrypoint": entrypoint
                }

    # Index commands
    for command in commands_data.get("commands", []):
        if command.get("status") != "active":
            continue

        command_name = normalize_command_name(command.get("name", ""))
        if command_name and command_name not in index:
            index[command_name] = {
                "type": "command",
                "source": command_name,
                "command": command
            }

    return index


def build_plugin_index(plugin_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Build an index of all commands in plugin.yaml.

    Args:
        plugin_data: Parsed plugin.yaml

    Returns:
        Dictionary mapping command names to their plugin data
    """
    index = {}

    for command in plugin_data.get("commands", []):
        command_name = normalize_command_name(command.get("name", ""))
        if command_name:
            index[command_name] = command

    return index


def compare_permissions(registry_perms: List[str], plugin_perms: List[str]) -> Tuple[bool, List[str]]:
    """
    Compare permissions between registry and plugin.

    Args:
        registry_perms: Permissions from registry
        plugin_perms: Permissions from plugin

    Returns:
        Tuple of (match, differences)
    """
    if not registry_perms and not plugin_perms:
        return True, []

    registry_set = set(registry_perms or [])
    plugin_set = set(plugin_perms or [])

    if registry_set == plugin_set:
        return True, []

    differences = []
    missing = registry_set - plugin_set
    extra = plugin_set - registry_set

    if missing:
        differences.append(f"Missing: {', '.join(sorted(missing))}")
    if extra:
        differences.append(f"Extra: {', '.join(sorted(extra))}")

    return False, differences


def analyze_command_metadata(
    command_name: str,
    registry_entry: Dict[str, Any],
    plugin_entry: Optional[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Analyze metadata differences between registry and plugin entries.

    Args:
        command_name: Name of the command
        registry_entry: Entry from registry index
        plugin_entry: Entry from plugin index (if exists)

    Returns:
        List of metadata issues
    """
    issues = []

    if not plugin_entry:
        return issues

    # Extract registry metadata based on type
    if registry_entry["type"] == "skill":
        entrypoint = registry_entry["entrypoint"]
        registry_runtime = entrypoint.get("runtime", "python")
        registry_perms = entrypoint.get("permissions", [])
        registry_handler = entrypoint.get("handler", "")
        registry_desc = entrypoint.get("description") or registry_entry["skill"].get("description", "")
    else:
        command = registry_entry["command"]
        registry_runtime = command.get("execution", {}).get("runtime", "python")
        registry_perms = command.get("permissions", [])
        registry_handler = None
        registry_desc = command.get("description", "")

    # Extract plugin metadata
    plugin_runtime = plugin_entry.get("handler", {}).get("runtime", "python")
    plugin_perms = plugin_entry.get("permissions", [])
    plugin_handler = plugin_entry.get("handler", {}).get("script", "")
    plugin_desc = plugin_entry.get("description", "")

    # Check runtime
    if registry_runtime != plugin_runtime:
        issues.append({
            "type": "runtime_mismatch",
            "command": command_name,
            "registry_value": registry_runtime,
            "plugin_value": plugin_runtime
        })

    # Check permissions
    perms_match, perms_diff = compare_permissions(registry_perms, plugin_perms)
    if not perms_match:
        issues.append({
            "type": "permissions_mismatch",
            "command": command_name,
            "differences": perms_diff,
            "registry_value": registry_perms,
            "plugin_value": plugin_perms
        })

    # Check handler path (for skills only)
    if registry_handler and registry_entry["type"] == "skill":
        expected_handler = f"skills/{registry_entry['source']}/{registry_handler}"
        if plugin_handler != expected_handler:
            issues.append({
                "type": "handler_mismatch",
                "command": command_name,
                "registry_value": expected_handler,
                "plugin_value": plugin_handler
            })

    # Check description
    if registry_desc and plugin_desc and registry_desc.strip() != plugin_desc.strip():
        issues.append({
            "type": "description_mismatch",
            "command": command_name,
            "registry_value": registry_desc,
            "plugin_value": plugin_desc
        })

    return issues


def reconcile_registries_with_plugin(
    skills_data: Dict[str, Any],
    commands_data: Dict[str, Any],
    plugin_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Compare registries with plugin.yaml and identify discrepancies.

    Args:
        skills_data: Parsed skills.json
        commands_data: Parsed commands.json
        plugin_data: Parsed plugin.yaml

    Returns:
        Dictionary containing analysis results
    """
    logger.info("Building registry index...")
    registry_index = build_registry_index(skills_data, commands_data)

    logger.info("Building plugin index...")
    plugin_index = build_plugin_index(plugin_data)

    logger.info("Comparing registries with plugin.yaml...")

    # Find missing commands (in registry but not in plugin)
    missing_commands = []
    for cmd_name, registry_entry in registry_index.items():
        if cmd_name not in plugin_index:
            missing_commands.append({
                "command": cmd_name,
                "type": registry_entry["type"],
                "source": registry_entry["source"],
                "registry_entry": registry_entry
            })

    # Find orphaned commands (in plugin but not in registry)
    orphaned_commands = []
    for cmd_name, plugin_entry in plugin_index.items():
        if cmd_name not in registry_index:
            orphaned_commands.append({
                "command": cmd_name,
                "plugin_entry": plugin_entry
            })

    # Find metadata mismatches
    metadata_issues = []
    for cmd_name, registry_entry in registry_index.items():
        if cmd_name in plugin_index:
            issues = analyze_command_metadata(cmd_name, registry_entry, plugin_index[cmd_name])
            metadata_issues.extend(issues)

    # Check for missing metadata suggestions
    metadata_suggestions = []
    for cmd_name, registry_entry in registry_index.items():
        if registry_entry["type"] == "skill":
            entrypoint = registry_entry["entrypoint"]
            if not entrypoint.get("permissions"):
                metadata_suggestions.append({
                    "command": cmd_name,
                    "field": "permissions",
                    "suggestion": "Consider adding permissions metadata"
                })
            if not entrypoint.get("description"):
                metadata_suggestions.append({
                    "command": cmd_name,
                    "field": "description",
                    "suggestion": "Consider adding description"
                })

    return {
        "missing_commands": missing_commands,
        "orphaned_commands": orphaned_commands,
        "metadata_issues": metadata_issues,
        "metadata_suggestions": metadata_suggestions,
        "total_registry_commands": len(registry_index),
        "total_plugin_commands": len(plugin_index)
    }


def generate_updated_plugin_yaml(
    plugin_data: Dict[str, Any],
    registry_index: Dict[str, Dict[str, Any]],
    reconciliation: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Generate an updated plugin.yaml based on reconciliation results.

    Args:
        plugin_data: Current plugin.yaml data
        registry_index: Index of registry entries
        reconciliation: Reconciliation results

    Returns:
        Updated plugin.yaml data
    """
    updated_plugin = {**plugin_data}

    # Build new commands list
    commands = []
    plugin_index = build_plugin_index(plugin_data)

    # Add all commands from registry
    for cmd_name, registry_entry in registry_index.items():
        if registry_entry["type"] == "skill":
            skill = registry_entry["skill"]
            entrypoint = registry_entry["entrypoint"]

            command = {
                "name": cmd_name,
                "description": entrypoint.get("description") or skill.get("description", ""),
                "handler": {
                    "runtime": entrypoint.get("runtime", "python"),
                    "script": f"skills/{skill['name']}/{entrypoint.get('handler', '')}"
                }
            }

            # Add parameters if present
            if "parameters" in entrypoint:
                command["parameters"] = entrypoint["parameters"]

            # Add permissions if present
            if "permissions" in entrypoint:
                command["permissions"] = entrypoint["permissions"]

            commands.append(command)

        elif registry_entry["type"] == "command":
            # Convert command registry format to plugin format
            cmd = registry_entry["command"]
            command = {
                "name": cmd_name,
                "description": cmd.get("description", ""),
                "handler": {
                    "runtime": cmd.get("execution", {}).get("runtime", "python"),
                    "script": cmd.get("execution", {}).get("target", "")
                }
            }

            if "parameters" in cmd:
                command["parameters"] = cmd["parameters"]

            if "permissions" in cmd:
                command["permissions"] = cmd["permissions"]

            commands.append(command)

    updated_plugin["commands"] = commands

    # Update metadata
    if "metadata" not in updated_plugin:
        updated_plugin["metadata"] = {}

    updated_plugin["metadata"]["updated_at"] = datetime.now(timezone.utc).isoformat()
    updated_plugin["metadata"]["updated_by"] = "docs.sync.plugin_manifest skill"
    updated_plugin["metadata"]["command_count"] = len(commands)

    return updated_plugin


def write_yaml_file(data: Dict[str, Any], file_path: str, header: Optional[str] = None):
    """
    Write data to YAML file with optional header.

    Args:
        data: Dictionary to write
        file_path: Path to write to
        header: Optional header comment
    """
    with open(file_path, 'w') as f:
        if header:
            f.write(header)
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, indent=2)

    logger.info(f"✅ Written file to {file_path}")


def generate_diff_report(reconciliation: Dict[str, Any]) -> str:
    """
    Generate a human-readable diff report.

    Args:
        reconciliation: Reconciliation results

    Returns:
        Formatted report string
    """
    lines = []
    lines.append("# Plugin Manifest Reconciliation Report")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}\n")

    # Summary
    lines.append("## Summary")
    lines.append(f"- Total commands in registry: {reconciliation['total_registry_commands']}")
    lines.append(f"- Total commands in plugin.yaml: {reconciliation['total_plugin_commands']}")
    lines.append(f"- Missing from plugin.yaml: {len(reconciliation['missing_commands'])}")
    lines.append(f"- Orphaned in plugin.yaml: {len(reconciliation['orphaned_commands'])}")
    lines.append(f"- Metadata issues: {len(reconciliation['metadata_issues'])}")
    lines.append(f"- Metadata suggestions: {len(reconciliation['metadata_suggestions'])}\n")

    # Missing commands
    if reconciliation['missing_commands']:
        lines.append("## Missing Commands (in registry but not in plugin.yaml)")
        for item in reconciliation['missing_commands']:
            lines.append(f"- **{item['command']}** ({item['type']}: {item['source']})")
        lines.append("")

    # Orphaned commands
    if reconciliation['orphaned_commands']:
        lines.append("## Orphaned Commands (in plugin.yaml but not in registry)")
        for item in reconciliation['orphaned_commands']:
            lines.append(f"- **{item['command']}**")
        lines.append("")

    # Metadata issues
    if reconciliation['metadata_issues']:
        lines.append("## Metadata Issues")
        for issue in reconciliation['metadata_issues']:
            issue_type = issue['type'].replace('_', ' ').title()
            lines.append(f"- **{issue['command']}**: {issue_type}")
            if 'differences' in issue:
                for diff in issue['differences']:
                    lines.append(f"  - {diff}")
            elif 'registry_value' in issue and 'plugin_value' in issue:
                lines.append(f"  - Registry: `{issue['registry_value']}`")
                lines.append(f"  - Plugin: `{issue['plugin_value']}`")
        lines.append("")

    # Suggestions
    if reconciliation['metadata_suggestions']:
        lines.append("## Metadata Suggestions")
        for suggestion in reconciliation['metadata_suggestions']:
            lines.append(f"- **{suggestion['command']}** ({suggestion['field']}): {suggestion['suggestion']}")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main CLI entry point."""
    logger.info("Starting plugin manifest reconciliation...")

    # Define file paths
    skills_path = os.path.join(BASE_DIR, "registry", "skills.json")
    commands_path = os.path.join(BASE_DIR, "registry", "commands.json")
    plugin_path = os.path.join(BASE_DIR, "plugin.yaml")
    preview_path = os.path.join(BASE_DIR, "plugin.preview.yaml")
    report_path = os.path.join(BASE_DIR, "plugin_manifest_diff.md")

    try:
        # Load files
        logger.info("Loading registry files...")
        skills_data = load_json_file(skills_path)
        commands_data = load_json_file(commands_path)

        logger.info("Loading plugin.yaml...")
        plugin_data = load_yaml_file(plugin_path)

        # Reconcile
        logger.info("Reconciling registries with plugin.yaml...")
        reconciliation = reconcile_registries_with_plugin(skills_data, commands_data, plugin_data)

        # Generate updated plugin.yaml
        logger.info("Generating updated plugin.yaml...")
        registry_index = build_registry_index(skills_data, commands_data)
        updated_plugin = generate_updated_plugin_yaml(plugin_data, registry_index, reconciliation)

        # Write preview file
        header = """# Betty Framework - Claude Code Plugin (Preview)
# Generated by docs.sync.plugin_manifest skill
# Review changes before applying to plugin.yaml

"""
        write_yaml_file(updated_plugin, preview_path, header)

        # Generate diff report
        logger.info("Generating diff report...")
        diff_report = generate_diff_report(reconciliation)
        with open(report_path, 'w') as f:
            f.write(diff_report)
        logger.info(f"✅ Written diff report to {report_path}")

        # Print summary
        print("\n" + "="*60)
        print("PLUGIN MANIFEST RECONCILIATION COMPLETE")
        print("="*60)
        print(f"\n📊 Summary:")
        print(f"  - Commands in registry: {reconciliation['total_registry_commands']}")
        print(f"  - Commands in plugin.yaml: {reconciliation['total_plugin_commands']}")
        print(f"  - Missing from plugin.yaml: {len(reconciliation['missing_commands'])}")
        print(f"  - Orphaned in plugin.yaml: {len(reconciliation['orphaned_commands'])}")
        print(f"  - Metadata issues: {len(reconciliation['metadata_issues'])}")
        print(f"  - Metadata suggestions: {len(reconciliation['metadata_suggestions'])}")

        print(f"\n📄 Output files:")
        print(f"  - Preview: {preview_path}")
        print(f"  - Diff report: {report_path}")

        if reconciliation['missing_commands']:
            print(f"\n⚠️  {len(reconciliation['missing_commands'])} command(s) missing from plugin.yaml:")
            for item in reconciliation['missing_commands'][:5]:
                print(f"    - {item['command']} ({item['source']})")
            if len(reconciliation['missing_commands']) > 5:
                print(f"    ... and {len(reconciliation['missing_commands']) - 5} more")

        if reconciliation['orphaned_commands']:
            print(f"\n⚠️  {len(reconciliation['orphaned_commands'])} orphaned command(s) in plugin.yaml:")
            for item in reconciliation['orphaned_commands'][:5]:
                print(f"    - {item['command']}")
            if len(reconciliation['orphaned_commands']) > 5:
                print(f"    ... and {len(reconciliation['orphaned_commands']) - 5} more")

        print(f"\n✅ Review {report_path} for full details")
        print("="*60 + "\n")

        # Return result
        result = {
            "ok": True,
            "status": "success",
            "preview_path": preview_path,
            "report_path": report_path,
            "reconciliation": reconciliation
        }

        print(json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to reconcile plugin manifest: {e}")
        import traceback
        traceback.print_exc()
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
