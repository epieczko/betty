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

    def create_hook(self, description_path: str) -> Dict[str, Any]:
        """
        Create hook from description file

        Args:
            description_path: Path to description file

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

            return {
                "ok": True,
                "status": "success",
                "hook_name": hook_desc["name"],
                "hooks_file": str(hooks_file)
            }

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
    if len(sys.argv) < 2:
        print("Usage: python3 meta_hook.py <hook_description_file>")
        print("\nExamples:")
        print("  python3 meta_hook.py examples/lint_hook.md")
        print("  python3 meta_hook.py examples/notify_hook.json")
        sys.exit(1)

    description_path = sys.argv[1]

    creator = HookCreator()
    result = creator.create_hook(description_path)

    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
