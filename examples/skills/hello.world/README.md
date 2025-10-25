# Hello World Skill

A simple greeting skill that demonstrates the fundamental concepts of the Betty Framework.

## Overview

The Hello World skill is a beginner-friendly example that showcases:

- **Input Handling**: Accept and validate user inputs
- **Processing Logic**: Generate personalized greetings
- **Output Management**: Save results to files and console
- **Error Handling**: Gracefully handle invalid inputs
- **Testing**: Comprehensive test coverage

This skill is perfect for learning Betty Framework basics and serves as a template for creating your own skills.

## Features

- Three greeting styles: casual, formal, and enthusiastic
- Input validation and error handling
- File output generation
- JSON/YAML result formatting
- Comprehensive test suite
- CLI with helpful argument parsing

## Usage

### Basic Usage

```bash
# Casual greeting (default)
python3 hello_world.py --name "Alice"
# Output: Hey Alice! Welcome to Betty Framework!

# Formal greeting
python3 hello_world.py --name "Bob" --greeting_style formal
# Output: Good day, Bob. Welcome to the Betty Framework.

# Enthusiastic greeting
python3 hello_world.py --name "Charlie" --greeting_style enthusiastic
# Output: 🎉 Hello Charlie! We're SO excited to have you here! 🚀
```

### Output Formats

```bash
# JSON output (default)
python3 hello_world.py --name "Alice" --output-format json

# YAML output (requires PyYAML)
python3 hello_world.py --name "Alice" --output-format yaml
```

### Help

```bash
python3 hello_world.py --help
```

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | string | Yes | - | Name of the person to greet |
| `greeting_style` | string | No | `casual` | Style of greeting (`casual`, `formal`, `enthusiastic`) |
| `output_format` | string | No | `json` | Output format (`json`, `yaml`) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `greeting.txt` | text file | File containing the personalized greeting |
| Console output | text | Greeting message printed to stdout |
| Result JSON/YAML | structured data | Execution results with metadata |

### Result Structure

```json
{
  "ok": true,
  "status": "success",
  "greeting": "Hey Alice! Welcome to Betty Framework!",
  "output_file": "/path/to/output/hello.world/greeting.txt",
  "greeting_style": "casual",
  "name": "Alice"
}
```

## Greeting Styles

### Casual
Friendly, informal greeting perfect for everyday interactions.
```
Hey Alice! Welcome to Betty Framework!
```

### Formal
Professional, polite greeting suitable for business contexts.
```
Good day, Bob. Welcome to the Betty Framework.
```

### Enthusiastic
Excited, emoji-filled greeting for celebratory moments.
```
🎉 Hello Charlie! We're SO excited to have you here! 🚀
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest test_hello_world.py -v

# Run specific test
pytest test_hello_world.py::TestHelloWorld::test_casual_greeting -v

# Run with coverage
pytest test_hello_world.py --cov=hello_world --cov-report=html
```

### Test Coverage

The test suite includes:
- ✓ All greeting styles
- ✓ Default parameter handling
- ✓ Output file creation and content
- ✓ Input validation
- ✓ Error handling
- ✓ Special characters in names
- ✓ Whitespace handling
- ✓ Multiple executions
- ✓ Result structure validation

## Integration with Agents

Use this skill in an agent workflow:

```yaml
name: greeter.agent
version: 0.1.0
description: Agent that greets multiple users
skills:
  - hello.world

workflow:
  - step: greet_alice
    skill: hello.world
    inputs:
      name: Alice
      greeting_style: casual

  - step: greet_bob
    skill: hello.world
    inputs:
      name: Bob
      greeting_style: formal
```

## Code Structure

```python
class HelloWorld:
    """Main skill class."""

    GREETING_STYLES = {
        "casual": "...",
        "formal": "...",
        "enthusiastic": "..."
    }

    def __init__(self, base_dir: Optional[Path] = None):
        """Initialize the skill."""
        pass

    def execute(self, name: str, greeting_style: str = "casual") -> Dict[str, Any]:
        """Execute the skill logic."""
        pass

def main():
    """CLI entry point."""
    pass
```

## Key Concepts Demonstrated

1. **Skill Structure**: Standard Betty Framework skill layout
2. **Input Validation**: Check and validate user inputs
3. **Error Handling**: Return structured error messages
4. **Output Management**: Save results to files and return metadata
5. **CLI Interface**: argparse-based command-line interface
6. **Testing**: pytest-based test suite
7. **Documentation**: Comprehensive README and docstrings

## Extending This Skill

Ideas for extending the Hello World skill:

1. **Add More Greeting Styles**: Add new styles like "pirate", "shakespearean", etc.
2. **Internationalization**: Support greetings in multiple languages
3. **Time-Based Greetings**: "Good morning", "Good afternoon", etc.
4. **Custom Templates**: Allow users to provide custom greeting templates
5. **Email Output**: Send greeting via email
6. **API Integration**: Post greeting to Slack, Discord, etc.

### Example: Adding a Pirate Style

```python
GREETING_STYLES = {
    "casual": "Hey {name}! Welcome to Betty Framework!",
    "formal": "Good day, {name}. Welcome to the Betty Framework.",
    "enthusiastic": "🎉 Hello {name}! We're SO excited to have you here! 🚀",
    "pirate": "Ahoy {name}! Welcome aboard the Betty ship, matey! 🏴‍☠️"
}
```

## Troubleshooting

### Common Issues

**Import Error: ModuleNotFoundError**
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/betty"
```

**Permission Denied**
```bash
chmod +x hello_world.py
```

**Output Directory Not Found**
The skill automatically creates the output directory if it doesn't exist.

**YAML Output Not Working**
```bash
pip install pyyaml
```

## Related Documentation

- [Quickstart Tutorial](../../../QUICKSTART.md) - Betty in 5 minutes guide
- [Skills Framework](../../../docs/skills-framework.md) - Comprehensive skill design guide
- [Getting Started](../../../GETTING_STARTED.md) - Full getting started guide
- [Example Skills](../) - More example skills to learn from

## License

MIT License - See [LICENSE](../../../LICENSE) for details

## Contributing

Found a bug or want to improve this example? Please open an issue or submit a pull request!

## Author

Betty Framework Team

---

**Ready to create your own skill?** Use this as a template and start building! 🚀
