#!/usr/bin/env python3
"""
registry_query.py - Implementation of the registry.query Skill

Search Betty registries programmatically by filtering skills, agents, and commands.
Supports filtering by tags, domain, status, name, version, and capability.
"""

import os
import sys
import json
import re
from typing import Dict, Any, List, Optional, Set
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    REGISTRY_FILE,
    AGENTS_REGISTRY_FILE,
    COMMANDS_REGISTRY_FILE,
    HOOKS_REGISTRY_FILE,
    BASE_DIR
)
from betty.logging_utils import setup_logger
from betty.errors import BettyError

logger = setup_logger(__name__)


def build_response(
    ok: bool,
    errors: Optional[List[str]] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Build standardized response.

    Args:
        ok: Whether the operation was successful
        errors: List of error messages
        details: Additional details to include

    Returns:
        Standardized response dictionary
    """
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    if details is not None:
        response["details"] = details
    return response


def load_registry(registry_type: str) -> Dict[str, Any]:
    """
    Load a registry file.

    Args:
        registry_type: Type of registry ('skills', 'agents', 'commands')

    Returns:
        Registry data dictionary

    Raises:
        BettyError: If registry cannot be loaded
    """
    registry_paths = {
        'skills': REGISTRY_FILE,
        'agents': AGENTS_REGISTRY_FILE,
        'commands': COMMANDS_REGISTRY_FILE,
        'hooks': HOOKS_REGISTRY_FILE
    }

    if registry_type not in registry_paths:
        raise BettyError(
            f"Invalid registry type: {registry_type}",
            details={
                "valid_types": list(registry_paths.keys()),
                "provided": registry_type
            }
        )

    registry_path = registry_paths[registry_type]

    if not os.path.exists(registry_path):
        logger.warning(f"Registry not found: {registry_path}")
        return {
            "version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            registry_type: []
        }

    try:
        with open(registry_path) as f:
            data = json.load(f)
            logger.debug(f"Loaded {registry_type} registry: {len(data.get(registry_type, []))} entries")
            return data
    except json.JSONDecodeError as e:
        raise BettyError(f"Invalid JSON in {registry_type} registry: {e}")
    except Exception as e:
        raise BettyError(f"Failed to load {registry_type} registry: {e}")


def normalize_filter_value(value: Any) -> str:
    """
    Normalize a filter value for case-insensitive comparison.

    Args:
        value: Value to normalize

    Returns:
        Normalized string value
    """
    if value is None:
        return ""
    return str(value).lower().strip()


def matches_pattern(text: str, pattern: str, fuzzy: bool = False) -> bool:
    """
    Check if text matches a pattern.

    Args:
        text: Text to match
        pattern: Pattern to match against
        fuzzy: Whether to use fuzzy matching

    Returns:
        True if text matches pattern
    """
    text = normalize_filter_value(text)
    pattern = normalize_filter_value(pattern)

    if not pattern:
        return True

    if fuzzy:
        # Fuzzy match: all characters of pattern appear in order in text
        pattern_idx = 0
        for char in text:
            if pattern_idx < len(pattern) and char == pattern[pattern_idx]:
                pattern_idx += 1
        return pattern_idx == len(pattern)
    else:
        # Exact substring match
        return pattern in text


def matches_tags(entry_tags: List[str], filter_tags: List[str]) -> bool:
    """
    Check if entry tags match any of the filter tags.

    Args:
        entry_tags: Tags from the entry
        filter_tags: Tags to filter by

    Returns:
        True if any filter tag is in entry tags
    """
    if not filter_tags:
        return True

    if not entry_tags:
        return False

    entry_tags_normalized = [normalize_filter_value(tag) for tag in entry_tags]
    filter_tags_normalized = [normalize_filter_value(tag) for tag in filter_tags]

    return any(filter_tag in entry_tags_normalized for filter_tag in filter_tags_normalized)


def matches_capabilities(entry_capabilities: List[str], filter_capabilities: List[str], fuzzy: bool = False) -> bool:
    """
    Check if entry capabilities match any of the filter capabilities.

    Args:
        entry_capabilities: Capabilities from the entry
        filter_capabilities: Capabilities to filter by
        fuzzy: Whether to use fuzzy matching

    Returns:
        True if any capability matches
    """
    if not filter_capabilities:
        return True

    if not entry_capabilities:
        return False

    for filter_cap in filter_capabilities:
        for entry_cap in entry_capabilities:
            if matches_pattern(entry_cap, filter_cap, fuzzy):
                return True

    return False


def extract_key_metadata(entry: Dict[str, Any], registry_type: str) -> Dict[str, Any]:
    """
    Extract key metadata from an entry based on registry type.

    Args:
        entry: Registry entry
        registry_type: Type of registry

    Returns:
        Dictionary with key metadata
    """
    metadata = {
        "name": entry.get("name"),
        "version": entry.get("version"),
        "description": entry.get("description"),
        "status": entry.get("status"),
        "tags": entry.get("tags", [])
    }

    # Add registry-specific metadata
    if registry_type == "skills":
        # Handle inputs - can be strings or objects
        inputs = entry.get("inputs", [])
        formatted_inputs = []
        for inp in inputs:
            if isinstance(inp, str):
                formatted_inputs.append({"name": inp, "type": "string", "required": False})
            elif isinstance(inp, dict):
                formatted_inputs.append({
                    "name": inp.get("name"),
                    "type": inp.get("type"),
                    "required": inp.get("required", False)
                })

        # Handle outputs - can be strings or objects
        outputs = entry.get("outputs", [])
        formatted_outputs = []
        for out in outputs:
            if isinstance(out, str):
                formatted_outputs.append({"name": out, "type": "string"})
            elif isinstance(out, dict):
                formatted_outputs.append({
                    "name": out.get("name"),
                    "type": out.get("type")
                })

        metadata.update({
            "dependencies": entry.get("dependencies", []),
            "entrypoints": [
                {
                    "command": ep.get("command"),
                    "runtime": ep.get("runtime"),
                    "description": ep.get("description")
                }
                for ep in entry.get("entrypoints", [])
            ],
            "inputs": formatted_inputs,
            "outputs": formatted_outputs
        })

    elif registry_type == "agents":
        metadata.update({
            "capabilities": entry.get("capabilities", []),
            "skills_available": entry.get("skills_available", []),
            "reasoning_mode": entry.get("reasoning_mode"),
            "context_requirements": entry.get("context_requirements", {})
        })

    elif registry_type == "commands":
        metadata.update({
            "execution": entry.get("execution", {}),
            "parameters": entry.get("parameters", [])
        })

    elif registry_type == "hooks":
        metadata.update({
            "event": entry.get("event"),
            "command": entry.get("command"),
            "enabled": entry.get("enabled", True)
        })

    return metadata


def filter_entries(
    entries: List[Dict[str, Any]],
    registry_type: str,
    name: Optional[str] = None,
    version: Optional[str] = None,
    status: Optional[str] = None,
    tags: Optional[List[str]] = None,
    capability: Optional[str] = None,
    domain: Optional[str] = None,
    fuzzy: bool = False
) -> List[Dict[str, Any]]:
    """
    Filter entries based on criteria.

    Args:
        entries: List of registry entries
        registry_type: Type of registry
        name: Filter by name (substring match)
        version: Filter by version (exact match)
        status: Filter by status (exact match)
        tags: Filter by tags (any match)
        capability: Filter by capability (for agents, substring match)
        domain: Filter by domain/tag (alias for tags filter)
        fuzzy: Use fuzzy matching for name and capability

    Returns:
        List of matching entries with key metadata
    """
    results = []

    # Convert domain to tags if provided
    if domain:
        tags = tags or []
        if domain not in tags:
            tags.append(domain)

    logger.debug(f"Filtering {len(entries)} entries with criteria:")
    logger.debug(f"  name={name}, version={version}, status={status}")
    logger.debug(f"  tags={tags}, capability={capability}, fuzzy={fuzzy}")

    for entry in entries:
        # Filter by name
        if name and not matches_pattern(entry.get("name", ""), name, fuzzy):
            continue

        # Filter by version (exact match)
        if version and normalize_filter_value(entry.get("version")) != normalize_filter_value(version):
            continue

        # Filter by status (exact match)
        if status and normalize_filter_value(entry.get("status")) != normalize_filter_value(status):
            continue

        # Filter by tags
        if tags and not matches_tags(entry.get("tags", []), tags):
            continue

        # Filter by capability (agents only)
        if capability:
            if registry_type == "agents":
                capabilities = entry.get("capabilities", [])
                if not matches_capabilities(capabilities, [capability], fuzzy):
                    continue
            else:
                # For non-agents, skip capability filter
                logger.debug(f"Capability filter only applies to agents, skipping for {registry_type}")

        # Entry matches all criteria
        metadata = extract_key_metadata(entry, registry_type)
        results.append(metadata)

    logger.info(f"Found {len(results)} matching entries")
    return results


def query_registry(
    registry: str,
    name: Optional[str] = None,
    version: Optional[str] = None,
    status: Optional[str] = None,
    tag: Optional[str] = None,
    tags: Optional[List[str]] = None,
    capability: Optional[str] = None,
    domain: Optional[str] = None,
    fuzzy: bool = False,
    limit: Optional[int] = None
) -> Dict[str, Any]:
    """
    Query a Betty registry with filters.

    Args:
        registry: Registry to query ('skills', 'agents', 'commands')
        name: Filter by name
        version: Filter by version
        status: Filter by status
        tag: Single tag filter (convenience parameter)
        tags: List of tags to filter by
        capability: Filter by capability (agents only)
        domain: Domain/tag filter (alias for tags)
        fuzzy: Use fuzzy matching
        limit: Maximum number of results to return

    Returns:
        Query result with matching entries
    """
    logger.info(f"Querying {registry} registry")

    # Normalize registry type
    registry = registry.lower()
    if registry not in ['skills', 'agents', 'commands', 'hooks']:
        raise BettyError(
            f"Invalid registry: {registry}",
            details={
                "valid_registries": ["skills", "agents", "commands", "hooks"],
                "provided": registry
            }
        )

    # Load registry
    registry_data = load_registry(registry)
    entries = registry_data.get(registry, [])

    # Merge tag and tags parameters
    if tag:
        tags = tags or []
        if tag not in tags:
            tags.append(tag)

    # Filter entries
    results = filter_entries(
        entries,
        registry,
        name=name,
        version=version,
        status=status,
        tags=tags,
        capability=capability,
        domain=domain,
        fuzzy=fuzzy
    )

    # Apply limit
    if limit and limit > 0:
        results = results[:limit]

    # Build response
    return build_response(
        ok=True,
        details={
            "registry": registry,
            "query": {
                "name": name,
                "version": version,
                "status": status,
                "tags": tags,
                "capability": capability,
                "domain": domain,
                "fuzzy": fuzzy,
                "limit": limit
            },
            "total_entries": len(entries),
            "matching_entries": len(results),
            "results": results
        }
    )


def format_table(results: List[Dict[str, Any]], registry_type: str) -> str:
    """
    Format results as an aligned table.

    Args:
        results: List of matching entries
        registry_type: Type of registry

    Returns:
        Formatted table string
    """
    if not results:
        return "No matching entries found."

    # Define columns based on registry type
    if registry_type == "skills":
        columns = ["Name", "Version", "Status", "Tags", "Commands"]
    elif registry_type == "agents":
        columns = ["Name", "Version", "Status", "Tags", "Reasoning", "Skills"]
    elif registry_type == "commands":
        columns = ["Name", "Version", "Status", "Tags", "Execution Type"]
    elif registry_type == "hooks":
        columns = ["Name", "Version", "Status", "Event", "Command", "Enabled"]
    else:
        columns = ["Name", "Version", "Status", "Description"]

    # Extract data for each column
    rows = []
    for entry in results:
        if registry_type == "skills":
            commands = [ep.get('command', '') for ep in entry.get('entrypoints', [])]
            row = [
                entry.get('name', ''),
                entry.get('version', ''),
                entry.get('status', ''),
                ', '.join(entry.get('tags', [])[:3]),  # Limit to 3 tags
                ', '.join(commands[:2])  # Limit to 2 commands
            ]
        elif registry_type == "agents":
            row = [
                entry.get('name', ''),
                entry.get('version', ''),
                entry.get('status', ''),
                ', '.join(entry.get('tags', [])[:3]),
                entry.get('reasoning_mode', ''),
                str(len(entry.get('skills_available', [])))
            ]
        elif registry_type == "commands":
            exec_type = entry.get('execution', {}).get('type', '')
            row = [
                entry.get('name', ''),
                entry.get('version', ''),
                entry.get('status', ''),
                ', '.join(entry.get('tags', [])[:3]),
                exec_type
            ]
        elif registry_type == "hooks":
            row = [
                entry.get('name', ''),
                entry.get('version', ''),
                entry.get('status', ''),
                entry.get('event', ''),
                entry.get('command', '')[:40],  # Truncate long commands
                str(entry.get('enabled', True))
            ]
        else:
            row = [
                entry.get('name', ''),
                entry.get('version', ''),
                entry.get('status', ''),
                entry.get('description', '')[:50]
            ]
        rows.append(row)

    # Calculate column widths
    col_widths = [len(col) for col in columns]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Build table
    lines = []
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    # Header
    lines.append(separator)
    header = "|" + "|".join(f" {col:<{col_widths[i]}} " for i, col in enumerate(columns)) + "|"
    lines.append(header)
    lines.append(separator)

    # Rows
    for row in rows:
        row_str = "|" + "|".join(f" {str(cell):<{col_widths[i]}} " for i, cell in enumerate(row)) + "|"
        lines.append(row_str)

    lines.append(separator)

    return "\n".join(lines)


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Query Betty registries programmatically",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all skills (compact format)
  registry_query.py skills

  # Find skills with 'api' tag in table format
  registry_query.py skills --tag api --format table

  # Find agents with 'design' capability
  registry_query.py agents --capability design

  # Find active skills with name containing 'validate'
  registry_query.py skills --name validate --status active

  # Query hooks registry
  registry_query.py hooks --status active --format table

  # Fuzzy search for commands
  registry_query.py commands --name test --fuzzy

  # Limit results with JSON output
  registry_query.py skills --tag api --limit 5 --format json
        """
    )

    parser.add_argument(
        "registry",
        choices=["skills", "agents", "commands", "hooks"],
        help="Registry to query"
    )
    parser.add_argument(
        "--name",
        help="Filter by name (substring match)"
    )
    parser.add_argument(
        "--version",
        help="Filter by version (exact match)"
    )
    parser.add_argument(
        "--status",
        help="Filter by status (e.g., active, draft, deprecated)"
    )
    parser.add_argument(
        "--tag",
        help="Filter by single tag"
    )
    parser.add_argument(
        "--tags",
        nargs="+",
        help="Filter by multiple tags (any match)"
    )
    parser.add_argument(
        "--capability",
        help="Filter by capability (agents only)"
    )
    parser.add_argument(
        "--domain",
        help="Filter by domain (alias for tag)"
    )
    parser.add_argument(
        "--fuzzy",
        action="store_true",
        help="Use fuzzy matching for name and capability"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of results to return"
    )
    parser.add_argument(
        "--format",
        choices=["json", "table", "compact"],
        default="compact",
        help="Output format (default: compact)"
    )

    args = parser.parse_args()

    try:
        result = query_registry(
            registry=args.registry,
            name=args.name,
            version=args.version,
            status=args.status,
            tag=args.tag,
            tags=args.tags,
            capability=args.capability,
            domain=args.domain,
            fuzzy=args.fuzzy,
            limit=args.limit
        )

        details = result["details"]

        if args.format == "json":
            # Output full JSON
            print(json.dumps(result, indent=2))
        elif args.format == "table":
            # Table format
            print(f"\n{'='*80}")
            print(f"REGISTRY QUERY: {details['registry'].upper()}")
            print(f"{'='*80}")
            print(f"\nTotal entries: {details['total_entries']}")
            print(f"Matching entries: {details['matching_entries']}\n")

            if details['results']:
                print(format_table(details['results'], details['registry']))
            else:
                print("No matching entries found.")

            print(f"\n{'='*80}\n")
        else:
            # Compact format (original pretty print)
            print(f"\n{'='*80}")
            print(f"REGISTRY QUERY: {details['registry'].upper()}")
            print(f"{'='*80}")
            print(f"\nTotal entries: {details['total_entries']}")
            print(f"Matching entries: {details['matching_entries']}")

            if details['results']:
                print(f"\n{'-'*80}")
                print("RESULTS:")
                print(f"{'-'*80}\n")

                for i, entry in enumerate(details['results'], 1):
                    print(f"{i}. {entry['name']} (v{entry['version']})")
                    print(f"   Status: {entry['status']}")
                    print(f"   Description: {entry['description'][:80]}...")
                    if entry.get('tags'):
                        print(f"   Tags: {', '.join(entry['tags'])}")

                    # Registry-specific details
                    if details['registry'] == 'skills':
                        if entry.get('entrypoints'):
                            commands = [ep['command'] for ep in entry['entrypoints']]
                            print(f"   Commands: {', '.join(commands)}")
                    elif details['registry'] == 'agents':
                        if entry.get('capabilities'):
                            print(f"   Capabilities: {len(entry['capabilities'])} capabilities")
                        print(f"   Reasoning: {entry.get('reasoning_mode', 'unknown')}")
                    elif details['registry'] == 'hooks':
                        print(f"   Event: {entry.get('event', 'unknown')}")
                        print(f"   Command: {entry.get('command', 'unknown')}")
                        print(f"   Enabled: {entry.get('enabled', True)}")

                    print()

                print(f"{'-'*80}")
            else:
                print("\nNo matching entries found.")

            print(f"\n{'='*80}\n")

        sys.exit(0 if result['ok'] else 1)

    except BettyError as e:
        logger.error(f"Query failed: {e}")
        result = build_response(
            ok=False,
            errors=[str(e)]
        )
        print(json.dumps(result, indent=2))
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        result = build_response(
            ok=False,
            errors=[f"Unexpected error: {str(e)}"]
        )
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
