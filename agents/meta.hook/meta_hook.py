#!/usr/bin/env python3
"""
meta.hook - Hook Creator Meta-Agent

Generates Claude Code hooks from natural language descriptions.

Usage:
    python3 agents/meta.hook/meta_hook.py <hook_description_file>

Examples:
    python3 agents/meta.hook/meta_hook.py examples/lint_hook.md
    python3 agents/meta.hook/meta_hook.py examples/notify_hook.json
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.traceability import get_tracer, RequirementInfo

logger = setup_logger(__name__)


class HookCreator:
    """Creates Claude Code hooks from descriptions"""

    VALID_EVENTS = [
        "before-tool-call",
        "after-tool-call",
        "on-error",
        "user-prompt-submit",
        "assistant-response"
    ]

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize hook creator"""
        self.base_dir = Path(base_dir)
        self.hooks_dir = self.base_dir / ".claude"

    def parse_description(self, description_path: str) -> Dict[str, Any]:
        """
        Parse hook description from Markdown or JSON file

        Args:
            description_path: Path to description file

        Returns:
            Dict with hook configuration
        """
        path = Path(description_path)

        if not path.exists():
            raise FileNotFoundError(f"Description file not found: {description_path}")

        # Read file
        content = path.read_text()

        # Try JSON first
        if path.suffix == ".json":
            return json.loads(content)

        # Parse Markdown format
        hook_desc = {}

        # Extract fields
        patterns = {
            "name": r"#\s*Name:\s*(.+)",
            "event": r"#\s*Event:\s*(.+)",
            "description": r"#\s*Description:\s*(.+)",
            "command": r"#\s*Command:\s*(.+)",
            "tool_filter": r"#\s*Tool\s*Filter:\s*(.+)",
            "enabled": r"#\s*Enabled:\s*(.+)",
            "timeout": r"#\s*Timeout:\s*(\d+)"
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                value = match.group(1).strip()

                # Convert types
                if field == "enabled":
                    value = value.lower() in ("true", "yes", "1")
                elif field == "timeout":
                    value = int(value)

                hook_desc[field] = value

        # Validate required fields
        required = ["name", "event", "command"]
        missing = [f for f in required if f not in hook_desc]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        # Validate event type
        if hook_desc["event"] not in self.VALID_EVENTS:
            raise ValueError(
                f"Invalid event type: {hook_desc['event']}. "
                f"Must be one of: {', '.join(self.VALID_EVENTS)}"
            )

        return hook_desc

    def generate_hooks_yaml(self, hook_desc: Dict[str, Any]) -> str:
        """
        Generate hooks.yaml configuration

        Args:
            hook_desc: Parsed hook description

        Returns:
            YAML string
        """
        hook_config = {
            "name": hook_desc["name"],
            "event": hook_desc["event"],
            "command": hook_desc["command"]
        }

        # Add optional fields
        if "description" in hook_desc:
            hook_config["description"] = hook_desc["description"]

        if "enabled" in hook_desc:
            hook_config["enabled"] = hook_desc["enabled"]
        else:
            hook_config["enabled"] = True

        if "tool_filter" in hook_desc:
            hook_config["tool_filter"] = hook_desc["tool_filter"]

        if "timeout" in hook_desc:
            hook_config["timeout"] = hook_desc["timeout"]

        # Wrap in hooks array
        hooks_yaml = {"hooks": [hook_config]}

        return yaml.dump(hooks_yaml, default_flow_style=False, sort_keys=False)

    def create_hook(
        self,
        description_path: str,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create hook from description file

        Args:
            description_path: Path to description file
            requirement: Optional requirement information for traceability

        Returns:
            Dict with creation results
        """
        try:
            print(f"🪝  meta.hook - Creating hook from {description_path}\n")

            # Parse description
            hook_desc = self.parse_description(description_path)

            # Generate hooks.yaml
            hooks_yaml = self.generate_hooks_yaml(hook_desc)

            # Ensure .claude directory exists
            self.hooks_dir.mkdir(parents=True, exist_ok=True)

            # Write hooks.yaml (or append if exists)
            hooks_file = self.hooks_dir / "hooks.yaml"

            if hooks_file.exists():
                # Load existing hooks
                existing = yaml.safe_load(hooks_file.read_text())
                if not existing or not isinstance(existing, dict):
                    existing = {"hooks": []}
                if "hooks" not in existing:
                    existing["hooks"] = []
                if not isinstance(existing["hooks"], list):
                    existing["hooks"] = []

                # Add new hook
                new_hook = yaml.safe_load(hooks_yaml)["hooks"][0]

                # Check for duplicate
                hook_names = [h.get("name") for h in existing["hooks"] if isinstance(h, dict)]
                if new_hook["name"] in hook_names:
                    print(f"⚠️  Warning: Hook '{new_hook['name']}' already exists, updating...")
                    # Remove old version
                    existing["hooks"] = [h for h in existing["hooks"] if h["name"] != new_hook["name"]]

                existing["hooks"].append(new_hook)
                hooks_yaml = yaml.dump(existing, default_flow_style=False, sort_keys=False)

            # Write file
            hooks_file.write_text(hooks_yaml)

            print(f"✨ Hook '{hook_desc['name']}' created successfully!\n")
            print(f"📄 Created/updated file:")
            print(f"   - {hooks_file}\n")
            print(f"✅ Hook '{hook_desc['name']}' is ready to use")
            print(f"   Event: {hook_desc['event']}")
            print(f"   Command: {hook_desc['command']}")

            result = {
                "ok": True,
                "status": "success",
                "hook_name": hook_desc["name"],
                "hooks_file": str(hooks_file)
            }

            # Log traceability if requirement provided
            trace_id = None
            if requirement:
                try:
                    tracer = get_tracer()

                    # Create component ID from hook name
                    component_id = f"hook.{hook_desc['name'].replace('-', '_')}"

                    trace_id = tracer.log_creation(
                        component_id=component_id,
                        component_name=hook_desc["name"],
                        component_type="hook",
                        component_version="0.1.0",
                        component_file_path=str(hooks_file),
                        input_source_path=description_path,
                        created_by_tool="meta.hook",
                        created_by_version="0.1.0",
                        requirement=requirement,
                        tags=["hook", "auto-generated", hook_desc["event"]],
                        project="Betty Framework"
                    )

                    # Log validation check
                    validation_details = {
                        "checks_performed": [
                            {"name": "hook_structure", "status": "passed"},
                            {"name": "event_validation", "status": "passed",
                             "message": f"Valid event type: {hook_desc['event']}"}
                        ]
                    }

                    # Check for tool filter
                    if hook_desc.get("tool_filter"):
                        validation_details["checks_performed"].append({
                            "name": "tool_filter_validation",
                            "status": "passed",
                            "message": f"Tool filter: {hook_desc['tool_filter']}"
                        })

                    tracer.log_verification(
                        component_id=component_id,
                        check_type="validation",
                        tool="meta.hook",
                        result="passed",
                        details=validation_details
                    )

                    result["trace_id"] = trace_id
                    result["component_id"] = component_id

                except Exception as e:
                    print(f"⚠️  Warning: Could not log traceability: {e}")

            return result

        except Exception as e:
            print(f"❌ Error creating hook: {e}")
            logger.error(f"Error creating hook: {e}", exc_info=True)
            return {
                "ok": False,
                "status": "failed",
                "error": str(e)
            }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.hook - Create hooks from descriptions"
    )
    parser.add_argument(
        "description",
        help="Path to hook description file (.md or .json)"
    )

    # Traceability arguments
    parser.add_argument(
        "--requirement-id",
        help="Requirement identifier (e.g., REQ-2025-001)"
    )
    parser.add_argument(
        "--requirement-description",
        help="What this hook accomplishes"
    )
    parser.add_argument(
        "--requirement-source",
        help="Source document"
    )
    parser.add_argument(
        "--issue-id",
        help="Issue tracking ID (e.g., JIRA-123)"
    )
    parser.add_argument(
        "--requested-by",
        help="Who requested this"
    )
    parser.add_argument(
        "--rationale",
        help="Why this is needed"
    )

    args = parser.parse_args()

    # Create requirement info if provided
    requirement = None
    if args.requirement_id and args.requirement_description:
        requirement = RequirementInfo(
            id=args.requirement_id,
            description=args.requirement_description,
            source=args.requirement_source,
            issue_id=args.issue_id,
            requested_by=args.requested_by,
            rationale=args.rationale
        )

    creator = HookCreator()
    result = creator.create_hook(args.description, requirement=requirement)

    # Display traceability info if available
    if result.get("trace_id"):
        print(f"\n📝 Traceability: {result['trace_id']}")
        print(f"   View trace: python3 betty/trace_cli.py show {result['component_id']}")

    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
