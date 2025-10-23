# Command and Hook Infrastructure

This document describes the command and hook infrastructure added to the Betty Framework in Layer 1 (Commands) and Layer 5 (Hooks).

## Overview

The Betty Framework now has complete infrastructure for:

1. **Commands** (Layer 1) - User-facing entry points
2. **Hooks** (Layer 5) - Automatic validation and policy enforcement

Both support manifest-based definition, validation, and registry management, consistent with Skills (Layer 4) and Agents (Layer 2).

## Architecture

```
┌─────────────────────────────────────────────┐
│  COMMANDS (User Interface Layer)            │
│  Slash commands: /api-design, /validate     │
│  ✅ command.define skill validates          │
│  ✅ commands.json registry tracks all       │
└──────────────────┬──────────────────────────┘
                   │ triggers
┌──────────────────▼──────────────────────────┐
│  AGENTS (Reasoning Layer)                   │
│  Intelligent orchestration with feedback    │
└──────────────────┬──────────────────────────┘
                   │ orchestrates
┌──────────────────▼──────────────────────────┐
│  WORKFLOWS (Orchestration Layer)            │
│  Declarative YAML multi-step processes      │
└──────────────────┬──────────────────────────┘
                   │ executes
┌──────────────────▼──────────────────────────┐
│  SKILLS (Execution Layer)                   │
│  Atomic, testable operations                │
└──────────────────┬──────────────────────────┘
                   │ protected by
┌──────────────────▼──────────────────────────┐
│  HOOKS (Validation/Policy Layer)            │
│  Automatic validation and governance        │
│  ✅ hook.define skill creates hooks         │
│  ✅ hook.register validates manifests       │
│  ✅ hooks.json registry tracks all          │
└─────────────────────────────────────────────┘
```

## Layer 1: Commands

### Command Manifest Schema

Commands are defined using YAML manifests that specify:

- **name**: Command name (must start with `/`)
- **version**: Semantic version
- **description**: Human-readable purpose
- **parameters**: Optional list of parameters
- **execution**: How the command executes (agent/skill/workflow)
- **status**: Lifecycle status (draft/active/deprecated/archived)
- **tags**: Categorization tags

### Example Command Manifest

```yaml
# examples/test-command.yaml

name: /api-design
version: 0.1.0
description: "Design a new API following enterprise guidelines"

parameters:
  - name: service_name
    type: string
    required: true
    description: "Name of the service/API"

  - name: spec_type
    type: enum
    values: [openapi, asyncapi]
    default: openapi
    description: "Type of API specification"

execution:
  type: agent              # Delegates to an agent
  target: api.designer     # Which agent to invoke
  context:
    guidelines: zalando    # Context passed to agent
    generate_models: true

status: active

tags: [api, design, user-facing]
```

### Command Execution Types

Commands can execute in three modes:

1. **agent**: Delegates to an intelligent agent
   - Example: `/api-design` → `api.designer` agent
   - Best for: Complex tasks requiring reasoning

2. **skill**: Calls a skill directly
   - Example: `/api-validate` → `api.validate` skill
   - Best for: Simple, deterministic operations

3. **workflow**: Executes a workflow
   - Example: `/api-pipeline` → `api_first_development.yaml`
   - Best for: Multi-step processes

### command.define Skill

The `command.define` skill validates and registers command manifests.

**Usage:**

```bash
python skills/command.define/command_define.py <path-to-command.yaml>
```

**Validation checks:**

1. Required fields present (name, version, description, execution)
2. Name format valid (starts with `/`, lowercase, hyphens only)
3. Version follows semantic versioning
4. Execution type is valid (agent/skill/workflow)
5. Execution target exists in appropriate registry
6. Parameters are properly formatted

**Output:**

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "examples/test-command.yaml",
  "details": {
    "valid": true,
    "status": "registered",
    "registry_updated": true
  }
}
```

### Command Registry

Commands are tracked in `/registry/commands.json`:

```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T01:53:41.669518+00:00",
  "commands": [
    {
      "name": "/api-design",
      "version": "0.1.0",
      "description": "Design API following enterprise guidelines",
      "execution": {
        "type": "agent",
        "target": "api.designer"
      },
      "parameters": [...],
      "status": "active",
      "tags": ["api", "design"]
    }
  ]
}
```

## Layer 5: Hooks

### Hook Manifest Schema

Hooks are defined using YAML manifests that specify:

- **name**: Hook identifier (lowercase, hyphens, underscores)
- **version**: Semantic version
- **description**: Human-readable purpose
- **event**: When the hook triggers (on_file_edit, on_commit, etc.)
- **command**: Command to execute
- **when**: Optional conditions (file pattern)
- **blocking**: Whether hook blocks on failure
- **timeout**: Timeout in milliseconds
- **status**: Lifecycle status (draft/active/disabled/archived)
- **tags**: Categorization tags

### Example Hook Manifest

```yaml
# examples/test-hook.yaml

name: validate-openapi-spec
version: 0.1.0
description: "Validate OpenAPI specs against Zalando guidelines on every edit"

event: on_file_edit

command: "python betty/skills/api.validate/api_validate.py {file_path} zalando"

when:
  pattern: "*.openapi.yaml"

blocking: true

timeout: 30000

on_failure: show_errors

status: active

tags: [validation, openapi, zalando]
```

### Hook Events

Hooks can trigger on these events:

| Event | Description | Use Case |
|-------|-------------|----------|
| `on_file_edit` | File is edited | Validate syntax on every edit |
| `on_file_save` | File is saved | Trigger code generation |
| `on_commit` | Git commit | Prevent breaking changes |
| `on_push` | Git push | Run full validation suite |
| `on_tool_use` | Tool is used | Audit trail logging |
| `on_agent_start` | Agent starts | Context injection |
| `on_workflow_end` | Workflow completes | Cleanup/notification |

### hook.define Skill

The `hook.define` skill creates hooks programmatically via CLI.

**Usage:**

```bash
python skills/hook.define/hook_define.py \
  on_file_edit \
  "python betty/skills/api.validate/api_validate.py {file_path} zalando" \
  --pattern="*.openapi.yaml" \
  --blocking=true \
  --timeout=30000 \
  --description="Validate OpenAPI specs on edit"
```

This creates entries in `.claude/hooks.yaml` for Claude Code to execute.

### hook.register Skill

The `hook.register` skill validates and registers hook manifests (similar to `command.define`).

**Usage:**

```bash
python skills/hook.register/hook_register.py <path-to-hook.yaml>
```

**Validation checks:**

1. Required fields present (name, version, description, event, command)
2. Name format valid (lowercase, hyphens, underscores)
3. Version follows semantic versioning
4. Event type is valid
5. Command is not empty
6. Blocking is boolean (if present)
7. Timeout is positive number (if present)
8. when.pattern is valid (if present)

**Output:**

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "examples/test-hook.yaml",
  "details": {
    "valid": true,
    "status": "registered",
    "registry_updated": true
  }
}
```

### Hook Registry

Hooks are tracked in `/registry/hooks.json`:

```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T01:55:03.830469+00:00",
  "hooks": [
    {
      "name": "validate-openapi-spec",
      "version": "0.1.0",
      "description": "Validate OpenAPI specs against Zalando guidelines",
      "event": "on_file_edit",
      "command": "python betty/skills/api.validate/api_validate.py {file_path} zalando",
      "when": {
        "pattern": "*.openapi.yaml"
      },
      "blocking": true,
      "timeout": 30000,
      "on_failure": "show_errors",
      "status": "active",
      "tags": ["validation", "openapi"]
    }
  ]
}
```

## Configuration

### config.py

New configuration constants:

```python
# File paths
COMMANDS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "commands.json")
HOOKS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "hooks.json")

# Required fields
REQUIRED_COMMAND_FIELDS = ["name", "version", "description", "execution"]
REQUIRED_HOOK_FIELDS = ["name", "version", "description", "event", "command"]

# Enums
class CommandExecutionType(Enum):
    AGENT = "agent"
    SKILL = "skill"
    WORKFLOW = "workflow"

class HookEvent(Enum):
    ON_FILE_EDIT = "on_file_edit"
    ON_FILE_SAVE = "on_file_save"
    ON_COMMIT = "on_commit"
    ON_PUSH = "on_push"
    ON_TOOL_USE = "on_tool_use"
    ON_AGENT_START = "on_agent_start"
    ON_WORKFLOW_END = "on_workflow_end"

class CommandStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"

class HookStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    DISABLED = "disabled"
    ARCHIVED = "archived"
```

### validation.py

New validation functions:

```python
def validate_command_name(name: str) -> None:
    """Validate command name (must start with '/', lowercase, hyphens)."""

def validate_hook_name(name: str) -> None:
    """Validate hook name (lowercase, hyphens, underscores)."""

def validate_command_execution_type(execution_type: str) -> None:
    """Validate execution type (agent/skill/workflow)."""

def validate_hook_event(event: str) -> None:
    """Validate hook event type."""
```

## Skills Summary

| Skill | Purpose | Registry | Status |
|-------|---------|----------|--------|
| `command.define` | Validate and register command manifests | `commands.json` | ✅ Active |
| `hook.define` | Create hooks programmatically | `.claude/hooks.yaml` | ✅ Active |
| `hook.register` | Validate and register hook manifests | `hooks.json` | ✅ Active |

## Example Workflows

### Creating a New Command

1. **Define manifest:**

```yaml
# commands/my-command.yaml
name: /my-command
version: 0.1.0
description: "My custom command"
execution:
  type: skill
  target: my.skill
status: active
```

2. **Validate and register:**

```bash
python skills/command.define/command_define.py commands/my-command.yaml
```

3. **Verify registration:**

```bash
cat registry/commands.json
```

### Creating a New Hook

1. **Define manifest:**

```yaml
# hooks/my-hook.yaml
name: my-validation-hook
version: 0.1.0
description: "Validate my files"
event: on_file_edit
command: "python skills/my.validate/validate.py {file_path}"
when:
  pattern: "*.myfile"
blocking: true
status: active
```

2. **Validate and register:**

```bash
python skills/hook.register/hook_register.py hooks/my-hook.yaml
```

3. **Verify registration:**

```bash
cat registry/hooks.json
```

## Integration with Betty Layers

### Commands → Agents

```yaml
execution:
  type: agent
  target: api.designer
```

Command `/api-design` delegates to `api.designer` agent.

### Commands → Skills

```yaml
execution:
  type: skill
  target: api.validate
```

Command `/api-validate` calls `api.validate` skill directly.

### Commands → Workflows

```yaml
execution:
  type: workflow
  target: api_first_development
```

Command `/api-pipeline` executes `api_first_development.yaml` workflow.

### Hooks → Skills

```yaml
command: "python skills/api.validate/api_validate.py {file_path} zalando"
```

Hook calls `api.validate` skill on file edit.

## Benefits

### Commands

✅ **User-friendly**: Simple slash commands for complex operations
✅ **Type-safe**: Parameter validation before execution
✅ **Traceable**: Registry tracks all available commands
✅ **Flexible**: Can delegate to agents, skills, or workflows
✅ **Versioned**: Semantic versioning for compatibility

### Hooks

✅ **Automatic**: Validation happens without user action
✅ **Immediate**: Fast feedback on errors
✅ **Enforced**: Blocking hooks prevent invalid states
✅ **Auditable**: Registry tracks all hooks
✅ **Configurable**: Pattern matching, timeouts, blocking mode

## Future Enhancements

### Commands

- [ ] Command aliases (`/api` → `/api-design`)
- [ ] Command composition (combine multiple commands)
- [ ] Command history and analytics
- [ ] Interactive parameter prompts

### Hooks

- [ ] Hook chains (multiple hooks on same event)
- [ ] Hook priorities (execution order)
- [ ] Hook analytics (execution times, failure rates)
- [ ] Conditional hooks (complex when clauses)

## See Also

- [Betty Architecture](./betty-architecture.md) - Five-layer design
- [Agent Define Implementation](./agent-define-implementation-plan.md) - Layer 2
- [Skills Framework](./skills-framework.md) - Layer 4
- [Claude Code Hooks Documentation](https://docs.claude.com/en/docs/claude-code/hooks)
