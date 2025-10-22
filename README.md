# Betty Framework

A self-bootstrapping skill system built on top of Claude Code for creating, managing, and orchestrating reusable AI-powered skills.

## Overview

Betty Framework enables you to:
- **Create** new skills with standardized manifests and handlers
- **Validate** skill definitions against schema requirements
- **Register** skills in a centralized registry
- **Compose** multi-step workflows by chaining skills together
- **Bootstrap** itself by using its own skills to create new skills

## Features

- **Self-Bootstrapping**: Betty can generate new skills using existing skills
- **Declarative Workflows**: Define multi-step processes in YAML
- **Type-Safe**: Full type hints and validation throughout
- **Production-Ready**: File locking, error handling, logging, and tests
- **Extensible**: Easy to add new skills and integrate with existing tools

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd betty

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m pytest
```

### Creating Your First Skill

```bash
# Create a new skill
python skills/skill.create/skill_create.py \
    "hello.world" \
    "A simple hello world skill" \
    --inputs "name" \
    --outputs "greeting"

# This creates:
# - skills/hello.world/skill.yaml (manifest)
# - skills/hello.world/SKILL.md (documentation)
# - skills/hello.world/hello_world.py (handler)
```

### Running a Workflow

```bash
# Create a workflow YAML file
cat > my_workflow.yaml << EOF
steps:
  - skill: skill.create
    args: ["test.skill", "A test skill"]
  - skill: skill.define
    args: ["skills/test.skill/skill.yaml"]
  - skill: registry.update
    args: ["skills/test.skill/skill.yaml"]
EOF

# Execute the workflow
python skills/workflow.compose/workflow_compose.py my_workflow.yaml
```

## Architecture

### Core Components

| Component | Description | Location |
|-----------|-------------|----------|
| **skill.create** | Scaffolds new skill directories and manifests | `skills/skill.create/` |
| **skill.define** | Validates skill manifests against schema | `skills/skill.define/` |
| **registry.update** | Updates the central skill registry | `skills/registry.update/` |
| **workflow.compose** | Executes multi-step skill workflows | `skills/workflow.compose/` |

### Directory Structure

```
betty/
├── betty/                  # Core framework modules
│   ├── config.py          # Configuration and constants
│   ├── validation.py      # Input validation utilities
│   ├── errors.py          # Custom exception classes
│   ├── logging_utils.py   # Logging setup
│   └── file_utils.py      # Safe file I/O with locking
├── skills/                # Individual skills
│   ├── skill.create/
│   ├── skill.define/
│   ├── registry.update/
│   └── workflow.compose/
├── registry/              # Skill registry and history
│   ├── skills.json
│   └── workflow_history.json
├── workflows/             # Workflow definitions
├── docs/                  # Documentation
└── tests/                 # Unit tests
```

## Skill Manifest Format

Skills are defined using YAML manifests (`skill.yaml`):

```yaml
name: skill.name
version: 0.1.0
description: >
  What this skill does
inputs:
  - input_parameter_1
  - input_parameter_2
outputs:
  - output_parameter_1
dependencies:
  - required.skill.1
  - required.skill.2
status: active  # draft, active, deprecated, archived

entrypoints:
  - command: /skill/name
    handler: skill_name.py
    runtime: python
    description: >
      Detailed description of what this entrypoint does
    parameters:
      - name: param1
        type: string
        required: true
        description: Parameter description
    permissions:
      - filesystem
      - read
      - write
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=betty --cov-report=html

# Run specific test file
pytest tests/test_validation.py

# Run specific test
pytest tests/test_validation.py::TestValidateSkillName::test_valid_skill_names
```

### Code Quality

```bash
# Type checking
mypy betty/ skills/

# Code formatting
black betty/ skills/ tests/

# Linting
pylint betty/ skills/
```

### Adding a New Skill

1. **Create the skill**:
   ```bash
   python skills/skill.create/skill_create.py \
       "my.skill" \
       "Description of my skill" \
       --inputs "input1,input2" \
       --outputs "output1"
   ```

2. **Implement the handler**: Edit `skills/my.skill/my_skill.py`

3. **Update documentation**: Edit `skills/my.skill/SKILL.md`

4. **Test the skill**: Create tests in `tests/test_my_skill.py`

5. **Validate and register**:
   ```bash
   python skills/skill.define/skill_define.py skills/my.skill/skill.yaml
   ```

## API Reference

### Betty Core Modules

#### `betty.config`
- `BASE_DIR`: Root directory of Betty framework
- `SKILLS_DIR`: Directory containing all skills
- `REGISTRY_FILE`: Path to skills registry JSON
- `get_skill_path(skill_name)`: Get path to a skill directory
- `ensure_directories()`: Ensure all required directories exist

#### `betty.validation`
- `validate_skill_name(name)`: Validate skill naming convention
- `validate_path(path, must_exist=False)`: Validate file paths
- `validate_manifest_fields(manifest, required_fields)`: Validate manifest
- `validate_version(version)`: Validate semantic version

#### `betty.errors`
- `BettyError`: Base exception for all Betty errors
- `SkillNotFoundError`: Raised when a skill cannot be found
- `SkillValidationError`: Raised when validation fails
- `RegistryError`: Raised for registry operation failures
- `WorkflowError`: Raised for workflow execution failures
- `ManifestError`: Raised for manifest parsing errors

#### `betty.file_utils`
- `locked_file(path, mode)`: Context manager for file locking
- `safe_read_json(path, default=None)`: Thread-safe JSON read
- `safe_write_json(path, data)`: Thread-safe JSON write
- `safe_update_json(path, update_fn, default=None)`: Atomic JSON update

## Configuration

Betty can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `BETTY_HOME` | Root directory for Betty | Current directory |

## Workflow Features

Workflows support:
- **Sequential execution**: Steps run in order
- **Error handling**: Configure fail-fast or continue-on-error
- **History tracking**: All workflow runs are logged
- **Timeouts**: Automatic timeout for long-running skills (5 minutes)
- **Rich logging**: Detailed execution logs with timestamps

### Workflow YAML Format

```yaml
fail_fast: true  # Stop on first error (default: true)

steps:
  - skill: skill.name
    args:
      - argument1
      - argument2

  - skill: another.skill
    args: ["single-arg"]
```

## Best Practices

1. **Skill Naming**: Use dot notation (`category.action`)
2. **Versioning**: Follow semantic versioning (MAJOR.MINOR.PATCH)
3. **Error Handling**: Always use Betty error classes
4. **Logging**: Use `setup_logger(__name__)` in all modules
5. **Type Hints**: Add type annotations to all functions
6. **Documentation**: Keep SKILL.md files up to date
7. **Testing**: Write unit tests for all new functionality

## Troubleshooting

### Common Issues

**Skill not found**
```
SkillNotFoundError: Skill 'my.skill' not found
```
- Ensure the skill directory exists in `skills/`
- Check that the skill is registered in `registry/skills.json`

**Validation failed**
```
SkillValidationError: Missing required fields: ['version']
```
- Check your skill.yaml has all required fields
- Run `skill.define` to see detailed validation errors

**Permission denied**
```
PermissionError: Cannot write to registry/skills.json
```
- Check file permissions
- Ensure parent directory exists
- Try running with appropriate permissions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/my-feature`)
8. Create a Pull Request

## Roadmap

### Current Features (v0.1.0)
- ✅ Skill creation and scaffolding
- ✅ Skill validation and registration
- ✅ Workflow composition and execution
- ✅ File locking for concurrent access
- ✅ Comprehensive error handling
- ✅ Unit test coverage

### Planned Features (v0.2.0)
- 🔄 Claude Code plugin integration
- 🔄 Skill dependency resolution
- 🔄 Parallel workflow execution
- 🔄 Skill versioning and migrations
- 🔄 Web UI for skill management
- 🔄 Marketplace integration

### Future (v1.0.0)
- 🎯 Remote skill execution
- 🎯 Skill sandboxing
- 🎯 Performance monitoring
- 🎯 Auto-documentation generation
- 🎯 Skill composition (meta-skills)

## License

[Add your license here]

## Support

- **Documentation**: See `docs/` directory
- **Issues**: [GitHub Issues](https://github.com/yourusername/betty/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/betty/discussions)

## Acknowledgments

Built for use with [Claude Code](https://claude.com/claude-code) by Anthropic.

---

**Version**: 0.1.0
**Last Updated**: 2025-10-22
