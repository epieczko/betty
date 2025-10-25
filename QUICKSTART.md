# Betty in 5 Minutes

Get started with Betty Framework in under 5 minutes! This quickstart guide will help you install Betty and create your first "Hello World" skill.

## What is Betty?

Betty is an AI-native Software Development Life Cycle (SDLC) framework that runs on Claude Code. It provides:

- **Meta-Agents**: AI-powered generators that create skills, agents, and hooks from descriptions
- **Skills**: Reusable, composable building blocks for automation
- **Agents**: Orchestrators that combine skills into workflows
- **Registries**: Source of truth for all framework components
- **Hooks**: Event-driven automation for CI/CD pipelines

## Prerequisites

- Python 3.8 or higher
- Git 2.20 or higher
- Claude Code CLI

## Quick Setup

Run the single-command setup script:

```bash
curl -sSL https://raw.githubusercontent.com/epieczko/betty/main/scripts/quickstart.sh | bash
```

Or manually:

```bash
# Clone the repository
git clone https://github.com/epieczko/betty.git
cd betty

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export BETTY_HOME="$(pwd)"

# Verify installation
python3 -m betty.validation
```

## Create Your First Skill: Hello World

Betty makes it incredibly easy to create new skills using meta-agents. Let's create a simple "Hello World" skill.

### Step 1: Describe Your Skill

Create a skill description file:

```bash
cat > hello_world_description.md <<'EOF'
# Skill: hello.world

## Purpose
Create a friendly greeting skill that says hello to users.

## Inputs
- `name` (required): Name of the person to greet
- `greeting_style` (optional): Style of greeting (casual, formal, enthusiastic). Default: casual

## Outputs
- `greeting.txt`: File containing the personalized greeting
- Console output with the greeting message

## Behavior
1. Accept a name as input
2. Generate a personalized greeting based on the style
3. Save the greeting to a file
4. Print the greeting to console

## Example Usage
```bash
python3 skills/hello.world/hello_world.py --name "Alice" --greeting_style casual
# Output: "Hey Alice! Welcome to Betty Framework!"
```
EOF
```

### Step 2: Generate the Skill

Use the `meta.skill` agent to generate your skill:

```bash
python3 agents/meta.skill/meta_skill.py hello_world_description.md
```

This creates:
```
skills/hello.world/
├── skill.yaml           # Skill manifest
├── hello_world.py       # Python implementation
├── test_hello_world.py  # Test suite
└── README.md            # Documentation
```

### Step 3: Implement the Skill Logic

Edit the generated `skills/hello.world/hello_world.py`:

```python
#!/usr/bin/env python3
"""Hello World Skill - A simple greeting skill."""

import argparse
import json
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class HelloWorld:
    """Generate personalized greetings."""

    GREETING_STYLES = {
        "casual": "Hey {name}! Welcome to Betty Framework!",
        "formal": "Good day, {name}. Welcome to the Betty Framework.",
        "enthusiastic": "🎉 Hello {name}! We're SO excited to have you here! 🚀"
    }

    def __init__(self, base_dir: str = BASE_DIR):
        self.base_dir = Path(base_dir)
        self.output_dir = self.base_dir / "output" / "hello.world"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def execute(self, name: str, greeting_style: str = "casual") -> Dict[str, Any]:
        """
        Generate a personalized greeting.

        Args:
            name: Name of the person to greet
            greeting_style: Style of greeting (casual, formal, enthusiastic)

        Returns:
            Dictionary with execution results
        """
        try:
            # Validate greeting style
            if greeting_style not in self.GREETING_STYLES:
                return {
                    "ok": False,
                    "status": "error",
                    "error": f"Invalid greeting style. Choose from: {list(self.GREETING_STYLES.keys())}"
                }

            # Generate greeting
            greeting = self.GREETING_STYLES[greeting_style].format(name=name)

            # Save to file
            output_file = self.output_dir / "greeting.txt"
            output_file.write_text(greeting)

            # Print to console
            print(greeting)

            return {
                "ok": True,
                "status": "success",
                "greeting": greeting,
                "output_file": str(output_file)
            }

        except Exception as e:
            return {
                "ok": False,
                "status": "error",
                "error": str(e)
            }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Hello World Skill")
    parser.add_argument("--name", required=True, help="Name of person to greet")
    parser.add_argument(
        "--greeting_style",
        default="casual",
        choices=["casual", "formal", "enthusiastic"],
        help="Style of greeting"
    )
    parser.add_argument("--output-format", default="json", choices=["json", "yaml"])

    args = parser.parse_args()

    skill = HelloWorld()
    result = skill.execute(args.name, args.greeting_style)

    if args.output_format == "json":
        print(json.dumps(result, indent=2))

    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    exit(main())
```

### Step 4: Test Your Skill

Run your Hello World skill:

```bash
# Casual greeting
python3 skills/hello.world/hello_world.py --name "Alice"

# Formal greeting
python3 skills/hello.world/hello_world.py --name "Bob" --greeting_style formal

# Enthusiastic greeting
python3 skills/hello.world/hello_world.py --name "Charlie" --greeting_style enthusiastic
```

Run the test suite:

```bash
pytest skills/hello.world/test_hello_world.py -v
```

### Step 5: Use in an Agent

Create an agent that uses your Hello World skill:

```bash
cat > my_first_agent.yaml <<'EOF'
name: greeter
version: 0.1.0
description: A friendly agent that greets users
skills:
  - hello.world
workflow:
  - step: greet_user
    skill: hello.world
    inputs:
      name: ${USER_NAME}
      greeting_style: casual
EOF
```

## What's Next?

Congratulations! You've created your first Betty skill. Here's what to explore next:

### Learn More
- **[Full Documentation](docs/betty-architecture.md)** - Deep dive into Betty's architecture
- **[Skills Framework](docs/skills-framework.md)** - Learn skill design patterns
- **[Meta-Agents Guide](docs/META_AGENTS.md)** - Master AI-powered generators

### Explore Examples
- **[Example Skills](examples/skills/)** - Pre-built skills you can use
- **[Example Agents](examples/agents/)** - Ready-to-use agents
- **[Example Hooks](examples/hooks/)** - Event-driven automation

### Create More
```bash
# Create a new skill
python3 agents/meta.skill/meta_skill.py my_skill_description.md

# Create a new agent
python3 agents/atum/atum.py my_agent_description.md

# Create a new hook
python3 agents/meta.hook/meta_hook.py my_hook_description.md
```

### Join the Community
- **[GitHub Issues](https://github.com/epieczko/betty/issues)** - Report bugs or request features
- **[Discussions](https://github.com/epieczko/betty/discussions)** - Ask questions and share ideas

## Troubleshooting

### Common Issues

**Import errors:**
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Permission denied:**
```bash
chmod +x skills/hello.world/hello_world.py
```

**Skill not found in registry:**
```bash
python3 skills/registry.update/registry_update.py --scan-all
```

## Key Concepts

- **Skills**: Reusable building blocks (like functions in code)
- **Agents**: Orchestrators that combine skills (like programs)
- **Artifacts**: Typed outputs that skills produce (like data structures)
- **Registries**: Source of truth for all components (like package managers)
- **Meta-Agents**: AI generators that create skills/agents from descriptions

## Quick Reference

```bash
# List all skills
cat registry/skills.json | jq '.skills[].name'

# List all agents
cat registry/agents.json | jq '.agents[].name'

# Update registries
python3 skills/registry.update/registry_update.py --scan-all

# Run tests
pytest tests/ -v

# Validate everything
python3 -m betty.validation
```

---

**Ready to build amazing automations?** Start creating your own skills and agents! 🚀
