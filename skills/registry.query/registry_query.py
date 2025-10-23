#!/usr/bin/env python3
"""
Registry Query Skill - Search Betty registries programmatically

This skill allows users and workflows to look up skills, agents, commands, and hooks
dynamically based on various criteria.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add betty module to path
BETTY_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BETTY_ROOT))

from betty.config import (
    REGISTRY_FILE,
    AGENTS_REGISTRY_FILE,
    COMMANDS_REGISTRY_FILE,
    HOOKS_REGISTRY_FILE,
)
from betty.file_utils import safe_read_json


class RegistryQuery:
    """Query engine for Betty registries."""

    REGISTRY_MAP = {
        "skills": REGISTRY_FILE,
        "agents": AGENTS_REGISTRY_FILE,
        "commands": COMMANDS_REGISTRY_FILE,
        "hooks": HOOKS_REGISTRY_FILE,
    }

    REGISTRY_KEY_MAP = {
        "skills": "skills",
        "agents": "agents",
        "commands": "commands",
        "hooks": "hooks",
    }

    def __init__(self, registry_type: str):
        """Initialize query engine for specified registry type.

        Args:
            registry_type: One of "skills", "agents", "commands", "hooks"
        """
        if registry_type not in self.REGISTRY_MAP:
            raise ValueError(
                f"Invalid registry type: {registry_type}. "
                f"Must be one of: {', '.join(self.REGISTRY_MAP.keys())}"
            )

        self.registry_type = registry_type
        self.registry_path = self.REGISTRY_MAP[registry_type]
        self.registry_key = self.REGISTRY_KEY_MAP[registry_type]

    def load_registry(self) -> List[Dict[str, Any]]:
        """Load registry data from JSON file.

        Returns:
            List of registry entries
        """
        data = safe_read_json(self.registry_path, {})
        return data.get(self.registry_key, [])

    def query(
        self,
        name: Optional[str] = None,
        version: Optional[str] = None,
        tag: Optional[str] = None,
        tags: Optional[List[str]] = None,
        status: Optional[str] = None,
        capability: Optional[str] = None,
        domain: Optional[str] = None,
        partial_name: bool = False,
    ) -> List[Dict[str, Any]]:
        """Query registry with filtering criteria.

        Args:
            name: Exact or partial name match (based on partial_name flag)
            version: Exact version match
            tag: Single tag to match (deprecated, use tags)
            tags: List of tags - entry must have at least one
            status: Exact status match (draft, active, deprecated, archived)
            capability: Capability substring match (agents only)
            domain: Domain prefix match (e.g., "api" matches "api.define", "api.validate")
            partial_name: If True, name is matched as substring

        Returns:
            List of matching registry entries
        """
        entries = self.load_registry()
        results = []

        # Combine tag and tags parameters
        all_tags = []
        if tag:
            all_tags.append(tag)
        if tags:
            all_tags.extend(tags)

        for entry in entries:
            # Name filter
            if name:
                entry_name = entry.get("name", "")
                if partial_name:
                    if name.lower() not in entry_name.lower():
                        continue
                else:
                    if entry_name != name:
                        continue

            # Version filter
            if version and entry.get("version") != version:
                continue

            # Tag filter - entry must have at least one matching tag
            if all_tags:
                entry_tags = entry.get("tags", [])
                if not any(t in entry_tags for t in all_tags):
                    continue

            # Status filter
            if status and entry.get("status") != status:
                continue

            # Capability filter (agents only)
            if capability:
                entry_capabilities = entry.get("capabilities", [])
                if not any(capability.lower() in str(cap).lower() for cap in entry_capabilities):
                    continue

            # Domain filter - match name prefix before first dot
            if domain:
                entry_name = entry.get("name", "")
                entry_domain = entry_name.split(".")[0] if "." in entry_name else entry_name
                if entry_domain != domain:
                    continue

            results.append(entry)

        return results

    def format_results(
        self,
        results: List[Dict[str, Any]],
        output_format: str = "summary",
        fields: Optional[List[str]] = None,
    ) -> str:
        """Format query results for output.

        Args:
            results: List of matching entries
            output_format: "summary", "detailed", "json", "names"
            fields: List of specific fields to include (for custom output)

        Returns:
            Formatted output string
        """
        if not results:
            return json.dumps({"count": 0, "results": []}, indent=2)

        if output_format == "json":
            return json.dumps({"count": len(results), "results": results}, indent=2)

        if output_format == "names":
            names = [entry.get("name", "unknown") for entry in results]
            return "\n".join(names)

        if output_format == "summary":
            output_lines = [f"Found {len(results)} matching {self.registry_type}:\n"]
            for entry in results:
                name = entry.get("name", "unknown")
                version = entry.get("version", "unknown")
                status = entry.get("status", "unknown")
                description = entry.get("description", "No description")

                # Truncate long descriptions
                if len(description) > 80:
                    description = description[:77] + "..."

                output_lines.append(f"  • {name} (v{version}) [{status}]")
                output_lines.append(f"    {description}")

                # Add tags if present
                if "tags" in entry and entry["tags"]:
                    tags_str = ", ".join(entry["tags"][:5])
                    if len(entry["tags"]) > 5:
                        tags_str += f" (+{len(entry['tags']) - 5} more)"
                    output_lines.append(f"    Tags: {tags_str}")

                output_lines.append("")

            return "\n".join(output_lines)

        if output_format == "detailed":
            output_lines = [f"Found {len(results)} matching {self.registry_type}:\n"]
            for i, entry in enumerate(results, 1):
                output_lines.append(f"--- Entry {i} ---")

                # Display all fields or custom fields
                display_fields = fields if fields else entry.keys()
                for field in display_fields:
                    if field in entry:
                        value = entry[field]
                        # Format lists and dicts nicely
                        if isinstance(value, (list, dict)):
                            value_str = json.dumps(value, indent=2)
                            output_lines.append(f"{field}:")
                            for line in value_str.split("\n"):
                                output_lines.append(f"  {line}")
                        else:
                            output_lines.append(f"{field}: {value}")

                output_lines.append("")

            return "\n".join(output_lines)

        return json.dumps({"count": len(results), "results": results}, indent=2)


def main():
    """Command-line interface for registry queries."""
    parser = argparse.ArgumentParser(
        description="Query Betty registries for skills, agents, commands, and hooks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Find all API-related skills
  python registry_query.py skills --domain api

  # Find active skills with 'validation' tag
  python registry_query.py skills --tag validation --status active

  # Find agents with specific capability
  python registry_query.py agents --capability "API design"

  # Search for skills by partial name
  python registry_query.py skills --name compatibility --partial

  # Get all hook names
  python registry_query.py hooks --format names

  # Detailed view of all draft agents
  python registry_query.py agents --status draft --format detailed
        """,
    )

    parser.add_argument(
        "registry",
        choices=["skills", "agents", "commands", "hooks"],
        help="Registry to query",
    )

    # Filter arguments
    parser.add_argument(
        "--name",
        help="Filter by name (exact match unless --partial is used)",
    )
    parser.add_argument(
        "--partial",
        action="store_true",
        help="Enable partial/substring name matching",
    )
    parser.add_argument(
        "--version",
        help="Filter by exact version",
    )
    parser.add_argument(
        "--tag",
        help="Filter by tag (entries must have this tag)",
    )
    parser.add_argument(
        "--tags",
        nargs="+",
        help="Filter by multiple tags (entries must have at least one)",
    )
    parser.add_argument(
        "--status",
        choices=["draft", "active", "deprecated", "archived"],
        help="Filter by status",
    )
    parser.add_argument(
        "--capability",
        help="Filter by capability (substring match, agents only)",
    )
    parser.add_argument(
        "--domain",
        help="Filter by domain (name prefix before first dot, e.g., 'api')",
    )

    # Output format arguments
    parser.add_argument(
        "--format",
        choices=["summary", "detailed", "json", "names"],
        default="summary",
        help="Output format (default: summary)",
    )
    parser.add_argument(
        "--fields",
        nargs="+",
        help="Specific fields to include in output (for detailed format)",
    )

    args = parser.parse_args()

    try:
        # Create query engine
        query_engine = RegistryQuery(args.registry)

        # Execute query
        results = query_engine.query(
            name=args.name,
            version=args.version,
            tag=args.tag,
            tags=args.tags,
            status=args.status,
            capability=args.capability,
            domain=args.domain,
            partial_name=args.partial,
        )

        # Format and print results
        output = query_engine.format_results(
            results,
            output_format=args.format,
            fields=args.fields,
        )
        print(output)

        # Exit with appropriate code
        sys.exit(0 if results else 1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
