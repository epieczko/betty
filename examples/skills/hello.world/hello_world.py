#!/usr/bin/env python3
"""
Hello World Skill - A simple greeting skill.

This skill demonstrates the basic structure of a Betty Framework skill:
- Accept inputs (name, greeting_style)
- Process data (generate greeting)
- Produce outputs (greeting file, console output)
- Return structured results (JSON)

Usage:
    python3 hello_world.py --name "Alice"
    python3 hello_world.py --name "Bob" --greeting_style formal
    python3 hello_world.py --name "Charlie" --greeting_style enthusiastic
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Determine base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class HelloWorld:
    """
    Hello World Skill - Generate personalized greetings.

    This skill showcases the fundamental patterns of Betty Framework skills:
    - Type-safe input validation
    - Error handling
    - Output file management
    - Structured return values
    """

    # Greeting templates for different styles
    GREETING_STYLES = {
        "casual": "Hey {name}! Welcome to Betty Framework!",
        "formal": "Good day, {name}. Welcome to the Betty Framework.",
        "enthusiastic": "🎉 Hello {name}! We're SO excited to have you here! 🚀"
    }

    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize the Hello World skill.

        Args:
            base_dir: Base directory for the Betty Framework (defaults to project root)
        """
        self.base_dir = base_dir or BASE_DIR
        self.output_dir = self.base_dir / "output" / "hello.world"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def execute(
        self,
        name: str,
        greeting_style: str = "casual"
    ) -> Dict[str, Any]:
        """
        Generate a personalized greeting.

        Args:
            name: Name of the person to greet
            greeting_style: Style of greeting (casual, formal, enthusiastic)

        Returns:
            Dictionary with execution results:
                - ok (bool): Success status
                - status (str): Execution status
                - greeting (str): Generated greeting message
                - output_file (str): Path to output file
                - error (str, optional): Error message if failed
        """
        try:
            # Validate inputs
            if not name or not name.strip():
                return {
                    "ok": False,
                    "status": "error",
                    "error": "Name cannot be empty"
                }

            if greeting_style not in self.GREETING_STYLES:
                return {
                    "ok": False,
                    "status": "error",
                    "error": (
                        f"Invalid greeting style: '{greeting_style}'. "
                        f"Choose from: {list(self.GREETING_STYLES.keys())}"
                    )
                }

            # Generate greeting
            greeting = self.GREETING_STYLES[greeting_style].format(name=name.strip())

            # Save to file
            output_file = self.output_dir / "greeting.txt"
            output_file.write_text(greeting, encoding="utf-8")

            # Return success result
            return {
                "ok": True,
                "status": "success",
                "greeting": greeting,
                "output_file": str(output_file),
                "greeting_style": greeting_style,
                "name": name.strip()
            }

        except Exception as e:
            return {
                "ok": False,
                "status": "error",
                "error": f"Unexpected error: {str(e)}"
            }


def main():
    """CLI entry point for the Hello World skill."""
    parser = argparse.ArgumentParser(
        description="Hello World Skill - Generate personalized greetings",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --name "Alice"
  %(prog)s --name "Bob" --greeting_style formal
  %(prog)s --name "Charlie" --greeting_style enthusiastic --output-format yaml

Greeting Styles:
  casual       - Friendly, informal greeting (default)
  formal       - Professional, formal greeting
  enthusiastic - Excited, emoji-filled greeting
        """
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Name of the person to greet"
    )

    parser.add_argument(
        "--greeting_style",
        default="casual",
        choices=["casual", "formal", "enthusiastic"],
        help="Style of greeting (default: casual)"
    )

    parser.add_argument(
        "--output-format",
        default="json",
        choices=["json", "yaml"],
        help="Output format for results (default: json)"
    )

    args = parser.parse_args()

    # Execute skill
    skill = HelloWorld()
    result = skill.execute(args.name, args.greeting_style)

    # Print greeting to console if successful
    if result.get("ok"):
        print(result["greeting"])
        print()

    # Output structured results
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
    elif args.output_format == "yaml":
        try:
            import yaml
            print(yaml.dump(result, default_flow_style=False))
        except ImportError:
            print(json.dumps(result, indent=2))
            print("\nNote: Install PyYAML for YAML output: pip install pyyaml", file=sys.stderr)

    # Return exit code
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
