# Contributing to Betty Framework

Thank you for your interest in contributing to Betty! This document provides guidelines and best practices for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guide](#style-guide)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

Betty Framework is committed to providing a welcoming and inclusive environment for all contributors. Please be respectful, constructive, and professional in all interactions.

## Getting Started

### Prerequisites

- Python 3.11 or newer
- Git
- PyYAML (`pip install pyyaml`)
- Basic understanding of YAML and Python
- Familiarity with Claude Code is helpful but not required

### Setting Up Your Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/betty.git
   cd betty
   ```
3. Install dependencies:
   ```bash
   pip install pyyaml
   ```
4. Verify the installation by running a skill:
   ```bash
   python skills/skill.create/skill_create.py --help
   ```

## Development Workflow

### Creating a New Skill

Follow Betty's self-hosting philosophy by using existing skills to create new ones:

```bash
# 1. Create the skill scaffold
python skills/skill.create/skill_create.py \
  my.skill \
  "Description of what this skill does" \
  --inputs "input1,input2" \
  --outputs "output1"

# 2. Implement the skill logic
# Edit skills/my.skill/my_skill.py with your implementation

# 3. Update the SKILL.md documentation
# Edit skills/my.skill/SKILL.md with usage examples

# 4. Validate the manifest
python skills/skill.define/skill_define.py skills/my.skill/skill.yaml

# 5. Test your skill
python skills/my.skill/my_skill.py <test-args>

# 6. Update the registry
python skills/registry.update/registry_update.py skills/my.skill/skill.yaml
```

### Creating a New Agent

```bash
# 1. Create the agent directory and manifest
mkdir -p agents/my.agent

# 2. Create agent.yaml following the agent schema
# See docs/betty-architecture.md for agent manifest structure

# 3. Validate and register
python skills/agent.define/agent_define.py agents/my.agent/agent.yaml

# 4. Create agent documentation
# Create agents/my.agent/README.md following the agent template
```

### Creating a New Command or Hook

```bash
# For commands:
python skills/command.define/command_define.py commands/my-command.yaml

# For hooks:
python skills/hook.register/hook_register.py hooks/my-hook.yaml
```

## Contribution Guidelines

### General Principles

1. **Structure over improvisation** – Follow Betty's established patterns and conventions
2. **Self-documenting** – Code should be clear, with comprehensive documentation
3. **Test thoroughly** – Test all code paths and edge cases
4. **Audit trail** – All operations should be logged appropriately

### Naming Conventions

- **Skills**: Lowercase with dot notation (e.g., `api.validate`, `skill.create`)
  - Format: `<domain>.<action>`
  - Domain examples: `api`, `skill`, `workflow`, `agent`, `hook`
  - Action examples: `create`, `validate`, `define`, `update`

- **Agents**: Lowercase with dot notation (e.g., `api.designer`, `api.analyzer`)
  - Format: `<domain>.<role>`

- **Commands**: Slash prefix with kebab-case (e.g., `/api-design`, `/validate-spec`)

- **Hooks**: Kebab-case descriptive names (e.g., `validate-openapi-specs`, `prevent-breaking-changes`)

- **Files**: Snake_case for Python files, UPPERCASE for documentation markers
  - Python: `skill_create.py`, `api_validate.py`
  - Docs: `SKILL.md`, `README.md`

### Manifest Requirements

Every skill MUST include:

1. **skill.yaml** – Manifest with:
   - `name`: Unique identifier
   - `version`: Semantic version (e.g., `0.1.0`)
   - `description`: Clear, concise description (20+ characters)
   - `inputs`: Array of input parameters with types and descriptions
   - `outputs`: Array of output artifacts
   - `dependencies`: Array of required skills (use `[]` if none)
   - `status`: `draft` or `active`

2. **SKILL.md** – Documentation with:
   - Purpose and overview
   - Usage instructions with examples
   - Input/output descriptions
   - Integration examples
   - Common errors and troubleshooting

3. **Implementation file** – Python script (or other runtime) that:
   - Accepts arguments via command line
   - Validates inputs properly
   - Provides clear error messages
   - Returns structured output (JSON when possible)
   - Logs operations appropriately

### Required Fields in Manifests

#### Skill Manifest (skill.yaml)

```yaml
name: domain.action
version: 0.1.0
description: "Clear description of what this skill does (minimum 20 characters)"

inputs:
  - name: param_name
    type: string
    required: true
    description: "What this parameter is for"

outputs:
  - name: output_name
    type: object
    description: "What this output contains"

dependencies: []  # or list of required skills

status: draft  # or active

entrypoints:  # optional but recommended
  - command: /skill/domain/action
    handler: domain_action.py
    runtime: python
    permissions: [filesystem:read, filesystem:write]

tags: [category, feature]  # optional but recommended
```

#### Agent Manifest (agent.yaml)

```yaml
name: domain.role
version: 0.1.0
description: "What this agent does"

reasoning_mode: iterative  # or oneshot

capabilities:
  - "Capability 1"
  - "Capability 2"

skills_available:
  - skill.name1
  - skill.name2

status: draft  # or active

tags: [category, feature]
```

## Style Guide

### Python Code Style

- Follow PEP 8 conventions
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Use descriptive variable names
- Keep functions focused and small (single responsibility)

### Code Organization

```python
#!/usr/bin/env python3
"""
skill_name.py – Brief description
Longer description if needed.
"""

import os
import sys
# ... other imports

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import ...
from betty.validation import ...
# ... betty imports

# Constants
CONSTANT_NAME = "value"

# Functions in logical order
def helper_function():
    """Helper function docstring."""
    pass

def main():
    """Main CLI entry point."""
    pass

if __name__ == "__main__":
    main()
```

### Error Handling

- Use Betty's custom exceptions from `betty.errors`
- Provide clear, actionable error messages
- Return structured error responses (JSON)
- Log errors appropriately using `betty.logging_utils`

```python
from betty.errors import SkillValidationError, format_error_response

try:
    # ... operation
except SkillValidationError as e:
    logger.error(str(e))
    error_info = format_error_response(e)
    # ... handle error
```

## Testing

### Manual Testing

Before submitting a pull request:

1. **Test the skill directly**:
   ```bash
   python skills/my.skill/my_skill.py <valid-args>
   python skills/my.skill/my_skill.py <invalid-args>  # Should fail gracefully
   ```

2. **Validate the manifest**:
   ```bash
   python skills/skill.define/skill_define.py skills/my.skill/skill.yaml
   ```

3. **Test in a workflow**:
   ```bash
   # Create a test workflow that uses your skill
   python skills/workflow.compose/workflow_compose.py workflows/test_my_skill.yaml
   ```

4. **Test with hooks** (if applicable):
   ```bash
   # Test hook triggering
   python skills/hook.define/hook_define.py ...
   ```

### Integration Testing

Ensure your changes work with existing skills:

```bash
# Test the complete skill lifecycle
python skills/skill.create/skill_create.py test.integration "Test skill"
python skills/skill.define/skill_define.py skills/test.integration/skill.yaml
python skills/registry.update/registry_update.py skills/test.integration/skill.yaml
```

## Documentation

### SKILL.md Template

Every skill must have a comprehensive SKILL.md. See existing skills for examples:

```markdown
---
name: Skill Name
description: Brief description
---

# skill.name

## Overview
What this skill does and why it exists.

## Purpose
Specific problems this skill solves.

## Usage
```bash
python skills/skill.name/skill_name.py <args>
```

## Inputs
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ... | ... | ... | ... |

## Outputs
Description of what the skill produces.

## Examples
### Example 1: Common Use Case
...

## Integration
How to use with workflows, hooks, etc.

## Common Errors
| Error | Cause | Solution |
|-------|-------|----------|
| ... | ... | ... |

## See Also
- Related skills
- Documentation links
```

### Updating Existing Documentation

- Keep README.md in sync with new features
- Update architecture docs if adding new patterns
- Add entries to glossary for new terminology
- Update example workflows if changing skill interfaces

## Pull Request Process

### Before Submitting

1. ✅ Skill implemented and tested
2. ✅ Manifest (skill.yaml/agent.yaml) validated
3. ✅ SKILL.md or README.md created
4. ✅ Registry updated (skills.json/agents.json)
5. ✅ Code follows style guidelines
6. ✅ No breaking changes to existing skills (unless discussed)
7. ✅ Examples and tests provided

### Submitting a Pull Request

1. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-skill
   ```

2. Make your changes following the guidelines above

3. Commit with clear messages:
   ```bash
   git add .
   git commit -m "Add skill.name for <purpose>

   - Implements <feature>
   - Validates <constraints>
   - Documented in SKILL.md
   - Updated registry with active status"
   ```

4. Push to your fork:
   ```bash
   git push origin feature/my-new-skill
   ```

5. Open a Pull Request on GitHub with:
   - Clear title describing the change
   - Description of what the PR adds/fixes
   - Examples of usage
   - Any breaking changes noted
   - Screenshots/output samples if applicable

### PR Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, your PR will be merged
4. Your contribution will be included in the next release

### Commit Message Format

```
<type>: <short summary>

<detailed description>

- Bullet points for key changes
- Reference issues if applicable (#123)
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

## Status Lifecycle

New contributions should start as `draft`:

```yaml
status: draft
```

After review and testing, maintainers will promote to `active`:

```yaml
status: active
```

## Questions or Need Help?

- Check existing documentation in `docs/`
- Review similar skills for patterns
- See the [Glossary](glossary.md) for terminology
- Open an issue for discussion before large changes

## License

By contributing to Betty Framework, you agree that your contributions will be licensed under the project's license.

---

## Quick Reference Checklist

Before submitting a PR for a new skill:

- [ ] Skill name follows `domain.action` pattern
- [ ] skill.yaml includes all required fields
- [ ] SKILL.md is comprehensive with examples
- [ ] Implementation handles errors gracefully
- [ ] Skill has been tested manually
- [ ] Manifest validated with skill.define
- [ ] Registry updated with registry.update
- [ ] Status set to `draft` initially
- [ ] Documentation is clear and complete
- [ ] Follows Python style guidelines
- [ ] Commit messages are descriptive
- [ ] PR description explains the change

Thank you for contributing to Betty Framework! 🚀
