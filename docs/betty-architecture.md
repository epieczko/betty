# Betty Architecture: The Five-Layer Model

## Overview

Betty Framework implements a five-layer architecture that transforms Claude Code's plugin system into a structured, auditable engineering discipline. Each layer serves a distinct purpose, from user interaction down to policy enforcement.

```
┌─────────────────────────────────────────────┐
│  COMMANDS (User Interface Layer)            │
│  Slash commands: /api-design, /validate     │
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
└─────────────────────────────────────────────┘
```

---

## Layer 1: Commands (User Interface)

**Purpose**: Provide intuitive, user-facing entry points for Betty capabilities.

**Implementation**: Slash commands registered via Claude Code's command system.

**Created by**: `command.define` skill

### Structure

```yaml
# .claude/commands/api-design.md
# or commands/api-design.yaml (created by command.define)

name: /api-design
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

output:
  - OpenAPI spec in specs/{service_name}.yaml
  - Generated models in src/models/{service_name}/
  - Validation report in .betty/reports/{service_name}-validation.json
```

### Command Examples

| Command | Purpose | Delegates To |
|---------|---------|--------------|
| `/api-design <service>` | Design new API from scratch | `api.designer` agent |
| `/api-validate <spec>` | Validate existing spec | `api.validate` skill directly |
| `/api-migrate <v1> <v2>` | Handle API versioning | `api.migrator` agent |
| `/api-review <spec>` | Review for compliance | `api.reviewer` agent |
| `/api-generate <spec> --lang=ts` | Generate client models | `api.generate-models` skill |

### When to Use Commands

- ✅ User-facing operations that need simple invocation
- ✅ Common workflows that should be easy to remember
- ✅ Operations that benefit from parameter validation
- ❌ Internal skill-to-skill communication (use direct skill calls)
- ❌ Hook triggers (hooks call skills directly)

---

## Layer 2: Agents (Reasoning Layer)

**Purpose**: Provide intelligent, iterative orchestration with reasoning and error recovery.

**Implementation**: Agents as defined in Claude Code's agent system, with manifest files.

**Created by**: `agent.define` skill

### Agent Manifest Schema

Agent manifests define intelligent orchestrators that compose skills with reasoning and context awareness.

#### Required Fields

| Field | Type | Format | Description |
|-------|------|--------|-------------|
| `name` | string | `^[a-z][a-z0-9._-]*$` | Unique identifier (e.g., `api.designer`, `compliance.checker`) |
| `version` | string | `^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$` | Semantic version (e.g., `0.1.0`, `1.0.0-beta`) |
| `description` | string | 1-200 chars | Human-readable purpose statement |
| `capabilities` | array[string] | Non-empty | List of what the agent can do |
| `skills_available` | array[string] | Valid skill names | Skills the agent can orchestrate |
| `reasoning_mode` | enum | `iterative` \| `oneshot` | How the agent approaches tasks |

#### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `context_requirements` | object | `{}` | Structured context the agent needs |
| `workflow_pattern` | string | `null` | Narrative description of agent's reasoning process |
| `example_task` | string | `null` | Concrete example demonstrating agent behavior |
| `error_handling` | object | `{}` | Retry strategies and failure handling |
| `output` | object | `{}` | Expected outputs for success and failure cases |
| `tags` | array[string] | `[]` | Categorization tags (e.g., `api`, `validation`) |
| `dependencies` | array[string] | `[]` | Other agents or schemas this depends on |
| `status` | enum | `draft` | Lifecycle status: `draft` \| `active` \| `deprecated` \| `archived` |

#### Field Specifications

**`reasoning_mode`** - How the agent approaches problems:
- `iterative`: Agent can retry with feedback, refine based on errors, and improve incrementally (for validation loops, refinement tasks)
- `oneshot`: Agent executes once without retry (for analysis, reporting, deterministic tasks)

**`context_requirements`** - Structured context for decision-making:
```yaml
context_requirements:
  guidelines: string           # Type definition
  domain: string
  existing_apis: list
  strict_mode: boolean
  target_languages: list
```

**`error_handling`** - Defines retry and failure strategies:
```yaml
error_handling:
  max_retries: 3
  on_validation_failure: "analyze_and_refine"
  on_generation_failure: "try_alternative_config"
  timeout_seconds: 300
```

**`output`** - Expected artifacts and reports:
```yaml
output:
  success:
    - OpenAPI spec (validated)
    - Generated models (compiled)
    - Validation report
  failure:
    - Error analysis
    - Partial spec
    - Suggested fixes
```

#### Validation Rules

1. **Name Validation**:
   - Must match regex: `^[a-z][a-z0-9._-]*$`
   - Should follow pattern: `<domain>.<action>` (e.g., `api.designer`, `compliance.checker`)
   - Must be unique within agent registry

2. **Version Validation**:
   - Must follow semantic versioning: `MAJOR.MINOR.PATCH[-prerelease]`
   - Examples: `0.1.0`, `1.0.0`, `2.3.1-beta`

3. **Skills Validation**:
   - All skills in `skills_available` must exist in skill registry
   - Must have at least one skill
   - Agent should not list itself as a dependency (no circular references)

4. **Status Lifecycle**:
   - `draft` → `active` → `deprecated` → `archived` (one-way progression)
   - Only `active` agents can be invoked by commands
   - `deprecated` agents emit warnings
   - `archived` agents cannot be executed

### Example: API Designer Agent

```yaml
# agents/api.designer/agent.yaml

name: api.designer
version: 0.1.0
description: "Design RESTful APIs following enterprise guidelines with iterative refinement"

capabilities:
  - Design RESTful APIs from natural language requirements
  - Apply Zalando guidelines automatically
  - Generate OpenAPI 3.1 specs with best practices
  - Iteratively refine based on validation feedback
  - Handle AsyncAPI for event-driven architectures

skills_available:
  - api.define              # Core spec creation
  - api.validate            # Zalando compliance checking
  - api.generate-models     # Modelina integration
  - api.compatibility       # Breaking change detection
  - api.publish             # Registry publication (future)

reasoning_mode: iterative   # Agent can retry with feedback

context_requirements:
  guidelines: string        # Which guidelines to follow (zalando, google, etc.)
  domain: string           # Business domain context
  existing_apis: list      # Related APIs for consistency

workflow_pattern: |
  1. Analyze requirements and domain context
  2. Draft OpenAPI spec following guidelines
  3. Run validation (api.validate)
  4. If validation fails:
     - Analyze errors
     - Refine spec
     - Re-validate
     - Repeat until passing
  5. Generate models for target languages
  6. Verify generated models compile
  7. Publish to registry with metadata

example_task: |
  Input: "Create API for user management with CRUD operations,
          authentication via JWT, and email verification workflow"

  Agent will:
  1. Draft OpenAPI spec with proper resource paths (/users, /users/{id})
  2. Apply Zalando guidelines (snake_case, problem JSON, etc.)
  3. Validate spec against Zally rules
  4. Fix issues (e.g., add required headers, fix naming)
  5. Generate TypeScript and Python models via Modelina
  6. Verify models compile in sample projects
  7. Publish spec and models to registry

error_handling:
  max_retries: 3
  on_validation_failure: "Analyze errors, refine spec, retry"
  on_generation_failure: "Try alternative Modelina configurations"
  on_compilation_failure: "Adjust spec to fix type issues"
  timeout_seconds: 300

output:
  success:
    - OpenAPI spec (validated)
    - Generated models (compiled)
    - Validation report
    - Dependency graph
  failure:
    - Error analysis
    - Partial spec
    - Suggested fixes

status: draft

tags:
  - api
  - design
  - openapi
  - zalando
```

### Agent Examples

| Agent | Purpose | Skills Used | Reasoning Pattern |
|-------|---------|-------------|-------------------|
| `api.designer` | Design APIs from requirements | api.define, api.validate, api.generate-models | Iterative refinement |
| `api.reviewer` | Review specs for compliance | api.validate, api.compatibility, audit.log | Analysis and reporting |
| `api.migrator` | Handle API versioning | api.compatibility, api.define, api.publish | Multi-step migration |
| `compliance.checker` | Ensure enterprise standards | api.validate, policy.validate, audit.log | Policy enforcement |

### When to Use Agents

- ✅ Complex tasks requiring reasoning and decision-making
- ✅ Iterative processes with validation and refinement
- ✅ Operations that may need error recovery and retry logic
- ✅ Tasks that benefit from contextual understanding
- ❌ Simple, deterministic operations (use skills directly)
- ❌ Operations requiring millisecond response times (too slow)

### Agents vs Skills vs Workflows

| Feature | Skills | Workflows | Agents |
|---------|--------|-----------|--------|
| **Reasoning** | None | None | Yes |
| **Iteration** | No | No | Yes |
| **Error Recovery** | Basic | Sequential | Intelligent |
| **Speed** | Fast | Medium | Slower |
| **Use Case** | Atomic operations | Fixed processes | Complex goals |

---

## Layer 3: Workflows (Orchestration Layer)

**Purpose**: Define repeatable, auditable multi-step processes.

**Implementation**: Declarative YAML files executed by `workflow.compose` skill.

**Created by**: Manual authoring or `workflow.define` skill

### Structure

```yaml
# workflows/api_first_development.yaml

name: api_first_development
version: 1.0.0
description: "Complete API-first development workflow following Zalando guidelines"

inputs:
  service_name: string
  spec_type: openapi|asyncapi
  target_languages: list[string]

steps:
  # Step 1: Create the specification
  - skill: api.define
    args:
      - "{service_name}"
      - "{spec_type}"
    output: spec_path
    description: "Create initial API specification"

  # Step 2: Validate against Zalando guidelines
  - skill: api.validate
    args:
      - "{spec_path}"
      - "zalando"
    output: validation_report
    description: "Validate spec against Zalando guidelines"
    required: true  # Workflow fails if validation fails

  # Step 3: Generate models for each target language
  - skill: api.generate-models
    args:
      - "{spec_path}"
      - "typescript"
    output: ts_models_path
    description: "Generate TypeScript models via Modelina"
    when: "'typescript' in target_languages"

  - skill: api.generate-models
    args:
      - "{spec_path}"
      - "python"
    output: py_models_path
    description: "Generate Python models via Modelina"
    when: "'python' in target_languages"

  # Step 4: Verify models compile
  - skill: code.verify
    args:
      - "{ts_models_path}"
      - "typescript"
    description: "Verify TypeScript models compile"
    when: "'typescript' in target_languages"

  # Step 5: Check for breaking changes (if updating existing API)
  - skill: api.compatibility
    args:
      - "specs/{service_name}.yaml"  # old version
      - "{spec_path}"                # new version
    output: compatibility_report
    description: "Check for breaking changes"
    when: "file_exists('specs/{service_name}.yaml')"

  # Step 6: Publish to registry
  - skill: api.publish
    args:
      - "{spec_path}"
      - "{service_name}"
    output: registry_entry
    description: "Publish spec and models to Betty registry"

audit:
  log_to: /registry/workflow_history.json
  include:
    - All input parameters
    - Output of each step
    - Execution time per step
    - Validation results
    - Compatibility reports

on_failure:
  cleanup:
    - Remove partial artifacts
    - Log failure details
  notify:
    - Log to audit.log skill
```

### Workflow Patterns

**Sequential Execution** (current implementation):
```yaml
steps:
  - skill: api.define
    args: [...]
  - skill: api.validate
    args: [...]
  - skill: api.generate-models
    args: [...]
```

**Conditional Execution** (future):
```yaml
steps:
  - skill: api.compatibility
    args: [...]
    when: "file_exists('specs/{service_name}.yaml')"
```

**Parallel Execution** (future):
```yaml
steps:
  - parallel:
      - skill: api.generate-models
        args: ["{spec}", "typescript"]
      - skill: api.generate-models
        args: ["{spec}", "python"]
      - skill: api.generate-models
        args: ["{spec}", "go"]
```

### When to Use Workflows

- ✅ Multi-step processes that should be reproducible
- ✅ Operations requiring audit trails
- ✅ Standard procedures that multiple teams will use
- ✅ Processes that need to be version-controlled
- ❌ One-off operations (just call skills directly)
- ❌ Processes requiring complex branching logic (use agents)

---

## Layer 4: Skills (Execution Layer)

**Purpose**: Provide atomic, testable, reusable operations.

**Implementation**: Python scripts with manifests, registered in Betty registry.

**Created by**: `skill.create` skill

### Structure

```
skills/api.validate/
├── skill.yaml              # Manifest
├── api_validate.py         # Handler implementation
├── SKILL.md               # Documentation
└── tests/
    └── test_api_validate.py
```

**Manifest (`skill.yaml`)**:
```yaml
name: api.validate
version: 0.1.0
description: "Validate OpenAPI/AsyncAPI specs against enterprise guidelines"

inputs:
  - name: spec_path
    type: string
    required: true
    description: "Path to the API specification file"

  - name: guideline_set
    type: string
    required: false
    default: "zalando"
    enum: [zalando, google, microsoft]
    description: "Which API guidelines to validate against"

outputs:
  - name: validation_report
    type: object
    description: "Detailed validation results"
    schema:
      properties:
        valid: boolean
        errors: array
        warnings: array
        guideline_version: string

dependencies:
  - context.schema    # For validation rule definitions

entrypoints:
  - command: /skill/api/validate
    handler: api_validate.py
    runtime: python
    permissions:
      - filesystem:read
      - network:http  # For Zally API calls

status: active

tags: [api, validation, openapi, asyncapi, zalando]
```

**Handler (`api_validate.py`)**:
```python
#!/usr/bin/env python3
"""
Validate API specifications against enterprise guidelines.
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, SkillExecutionError
from betty.validation import validate_path

logger = setup_logger(__name__)


def validate_openapi_spec(spec_path: str, guideline_set: str) -> dict:
    """
    Validate OpenAPI spec against specified guidelines.

    Args:
        spec_path: Path to OpenAPI YAML/JSON file
        guideline_set: Guidelines to validate against (zalando, google, etc.)

    Returns:
        Validation report with errors, warnings, and compliance info
    """
    # Implementation here
    # - Load spec
    # - Call Zally API or local validator
    # - Parse validation results
    # - Return structured report

    return {
        "valid": True,
        "errors": [],
        "warnings": [],
        "guideline_version": "zalando-1.0",
        "spec_version": "3.1.0"
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate API specifications against enterprise guidelines"
    )
    parser.add_argument(
        "spec_path",
        type=str,
        help="Path to the API specification file"
    )
    parser.add_argument(
        "guideline_set",
        type=str,
        nargs="?",
        default="zalando",
        choices=["zalando", "google", "microsoft"],
        help="Guidelines to validate against (default: zalando)"
    )

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_path(args.spec_path)

        # Execute validation
        logger.info(f"Validating {args.spec_path} against {args.guideline_set} guidelines")
        result = validate_openapi_spec(args.spec_path, args.guideline_set)

        # Return structured result
        output = {
            "status": "success",
            "data": result
        }
        print(json.dumps(output, indent=2))

        # Exit with error code if validation failed
        if not result["valid"]:
            sys.exit(1)

    except Exception as e:
        logger.error(f"Validation failed: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
```

### Skill Categories for API-Driven Development

| Category | Skills | Purpose |
|----------|--------|---------|
| **Definition** | api.define, asyncapi.define | Create specifications |
| **Validation** | api.validate, api.lint | Check compliance |
| **Generation** | api.generate-models, api.generate-docs | Code/doc generation |
| **Compatibility** | api.compatibility, api.diff | Version management |
| **Publishing** | api.publish, api.register | Registry management |

### When to Use Skills

- ✅ Always - skills are the fundamental execution unit
- ✅ Atomic operations that can be tested independently
- ✅ Reusable logic needed by multiple workflows/agents
- ✅ Operations that need clear input/output contracts

---

## Layer 5: Hooks (Validation/Policy Layer)

**Purpose**: Provide automatic validation, policy enforcement, and safety rails.

**Implementation**: Event-triggered scripts registered in Claude Code's hooks system.

**Created by**: `hook.define` skill

### Structure

```yaml
# .claude/hooks.yaml (generated by hook.define skill)

hooks:
  # Validate OpenAPI specs on file edit
  on_file_edit:
    - name: validate-openapi-spec
      description: "Validate OpenAPI specs against Zalando guidelines on every edit"
      when:
        pattern: "*.openapi.yaml"
        # or: "specs/**/*.yaml"
      command: "python betty/skills/api.validate/api_validate.py {file_path} zalando"
      blocking: true        # Must pass before edit completes
      timeout: 30000        # 30 seconds
      on_failure: "show_errors"

    - name: validate-asyncapi-spec
      description: "Validate AsyncAPI specs on edit"
      when:
        pattern: "*.asyncapi.yaml"
      command: "python betty/skills/asyncapi.validate/asyncapi_validate.py {file_path}"
      blocking: true

  # Check for breaking changes on commit
  on_commit:
    - name: check-api-compatibility
      description: "Prevent commits with breaking API changes"
      when:
        pattern: "specs/**/*.yaml"
      command: "python betty/skills/api.compatibility/check_breaking_changes.py {file_path}"
      blocking: true
      on_failure: "abort_commit"

    - name: verify-api-versioning
      description: "Ensure proper API versioning on spec changes"
      when:
        pattern: "specs/**/*.yaml"
      command: "python betty/skills/api.version/check_version.py {file_path}"
      blocking: true

  # Audit trail on any tool use
  on_tool_use:
    - name: audit-api-changes
      description: "Log all API-related tool usage for compliance"
      command: "python betty/skills/audit.log/log_api_change.py {tool_name} {file_path}"
      blocking: false       # Just log, don't block

  # Re-generate models when specs change
  on_file_save:
    - name: regenerate-models
      description: "Auto-regenerate client models when specs change"
      when:
        pattern: "specs/*.openapi.yaml"
      command: "python betty/skills/api.generate-models/auto_generate.py {file_path}"
      blocking: false       # Run async, don't block save
      async: true

  # Validate before push
  on_push:
    - name: full-api-validation
      description: "Run complete validation suite before pushing"
      when:
        changed_files: "specs/**"
      command: "python betty/skills/workflow.compose/workflow_compose.py workflows/api_validation_suite.yaml"
      blocking: true
      timeout: 300000       # 5 minutes
```

### Hook Definition Skill

```bash
# Creating a hook via hook.define skill
python betty/skills/hook.define/hook_define.py \
  --event=on_file_edit \
  --pattern="*.openapi.yaml" \
  --command="api.validate {file_path} zalando" \
  --blocking=true \
  --description="Validate OpenAPI specs on edit"
```

This would:
1. Add entry to `.claude/hooks.yaml`
2. Register hook in Betty registry
3. Document in `.betty/hooks/README.md`
4. Create audit entry

### Hook Events for API-Driven Development

| Event | Use Case | Example |
|-------|----------|---------|
| `on_file_edit` | Validate syntax on every edit | OpenAPI schema validation |
| `on_file_save` | Trigger code generation | Regenerate models from spec |
| `on_commit` | Prevent breaking changes | API compatibility check |
| `on_push` | Full validation suite | Run all API tests |
| `on_tool_use` | Audit trail | Log all spec modifications |
| `on_agent_start` | Context injection | Load API guidelines |
| `on_workflow_end` | Cleanup/notification | Publish new API version |

### Why Hooks for Validation?

**Traditional Approach** (manual):
```bash
# Developer has to remember to run:
python api_validate.py specs/user.yaml
# ...and they often forget
```

**Betty Approach** (automatic):
```yaml
# Hook runs automatically on file edit
on_file_edit:
  - pattern: "*.openapi.yaml"
    command: api.validate {file_path}
    blocking: true
```

**Benefits**:
- ✅ Validation happens automatically, not by memory
- ✅ Catches errors immediately, not at commit time
- ✅ Provides fast feedback loop (< 1 second)
- ✅ Prevents invalid specs from ever being saved
- ✅ Enforces guidelines as guardrails, not afterthoughts
- ✅ No discipline required - it's just how the system works

### When to Use Hooks

- ✅ Validation that should happen automatically
- ✅ Policy enforcement that can't be bypassed
- ✅ Audit logging for compliance
- ✅ Code generation that should stay in sync
- ❌ Long-running operations (use async workflows)
- ❌ Operations requiring human decision (use agents)

---

## Integration Example: API-Driven Development

Let's see how all five layers work together for API-driven development:

### User Action
```bash
/api-design user-service
```

### Layer 1: Command Receives Request
```yaml
# commands/api-design.yaml
name: /api-design
execution:
  type: agent
  target: api.designer
```
The command delegates to the `api.designer` agent.

### Layer 2: Agent Reasons and Plans
```yaml
# agents/api.designer/agent.yaml
The agent:
1. Analyzes requirements: "user-service"
2. Decides to use workflow: api_first_development.yaml
3. Adds context: guidelines=zalando, domain=user-management
```

### Layer 3: Workflow Orchestrates Steps
```yaml
# workflows/api_first_development.yaml
steps:
  - skill: api.define
  - skill: api.validate
  - skill: api.generate-models
  - skill: api.publish
```

### Layer 4: Skills Execute
Each skill runs:
1. `api.define` → Creates `specs/user-service.openapi.yaml`
2. Triggers hook immediately...

### Layer 5: Hook Validates
```yaml
# .claude/hooks.yaml
on_file_edit:
  - pattern: "*.openapi.yaml"
    command: api.validate {file_path} zalando
    blocking: true
```

If validation passes:
- Workflow continues
- `api.generate-models` runs
- Models generated in `src/models/user-service/`
- `api.publish` adds to registry

If validation fails:
- Hook blocks the edit
- Agent receives error feedback
- Agent refines the spec
- Process repeats

### Complete Flow

```
User: /api-design user-service
  ↓
Command: Delegates to api.designer agent
  ↓
Agent: Analyzes, plans, selects workflow
  ↓
Workflow: Executes api.define skill
  ↓
Skill: Creates specs/user-service.openapi.yaml
  ↓
Hook: Validates against Zalando (BLOCKS if invalid)
  ↓
(if valid) Workflow continues...
  ↓
Skill: api.generate-models (TypeScript)
  ↓
Hook: Verifies models compile (BLOCKS if broken)
  ↓
(if valid) Workflow continues...
  ↓
Skill: api.publish
  ↓
Agent: Reports success to user
  ↓
User: Receives validated spec + compiled models
```

---

## Design Principles

### 1. Separation of Concerns

| Layer | Responsibility | Should NOT |
|-------|---------------|-----------|
| Commands | User interface | Contain business logic |
| Agents | Reasoning & planning | Execute code directly |
| Workflows | Orchestration | Make decisions |
| Skills | Execution | Reason about context |
| Hooks | Validation | Block for long periods |

### 2. Composability

Every layer should be composable:
- Commands can invoke agents OR skills OR workflows
- Agents can use skills OR workflows
- Workflows chain skills
- Skills are atomic and independent
- Hooks can trigger any of the above

### 3. Auditability

Every layer produces audit trails:
```json
{
  "command": "/api-design",
  "agent": "api.designer",
  "workflow": "api_first_development.yaml",
  "skills_executed": [
    {"skill": "api.define", "status": "success", "duration_ms": 234},
    {"skill": "api.validate", "status": "success", "duration_ms": 456}
  ],
  "hooks_triggered": [
    {"hook": "validate-openapi-spec", "status": "pass"}
  ],
  "artifacts": [
    "specs/user-service.openapi.yaml",
    "src/models/user-service/User.ts"
  ]
}
```

### 4. Fail-Fast with Hooks

Hooks provide immediate feedback:
- Invalid OpenAPI? Blocked at edit time, not commit time
- Breaking change? Blocked at commit time, not production time
- Invalid models? Blocked at generation time, not compile time

### 5. Progressive Enhancement

Start simple, add layers as needed:

**Minimum** (just skills):
```bash
python skills/api.validate/api_validate.py specs/user.yaml
```

**Better** (add hooks):
```yaml
on_file_edit:
  - command: api.validate {file_path}
```

**Good** (add workflows):
```yaml
steps:
  - skill: api.define
  - skill: api.validate
  - skill: api.generate-models
```

**Better** (add agents):
```bash
/api-design user-service  # Agent handles everything
```

**Best** (add commands):
```bash
/api-design user-service  # One command, full automation
```

---

## Implementation Roadmap

### Phase 1: Foundation (Hooks + Skills)
**Goal**: Automatic validation as safety rails

1. Create `hook.define` skill
2. Create `api.validate` skill (Zalando guidelines)
3. Create `api.define` skill (OpenAPI scaffolding)
4. Generate hooks for automatic validation

**Deliverable**: Editing `*.openapi.yaml` files automatically validates against Zalando guidelines.

### Phase 2: Orchestration (Workflows)
**Goal**: Repeatable processes with audit trails

1. Create `api.generate-models` skill (Modelina integration)
2. Create `api.compatibility` skill (breaking change detection)
3. Create `api_first_development.yaml` workflow
4. Create `api_validation_suite.yaml` workflow

**Deliverable**: Single workflow creates spec → validates → generates models → publishes.

### Phase 3: Interface (Commands)
**Goal**: User-friendly entry points

1. Create `command.define` skill
2. Register `/api-design` command
3. Register `/api-validate` command
4. Register `/api-migrate` command

**Deliverable**: Users can type `/api-design service-name` and get complete API scaffolding.

### Phase 4: Intelligence (Agents)
**Goal**: Reasoning and iterative refinement

1. Create `agent.define` skill
2. Create `api.designer` agent
3. Create `api.reviewer` agent
4. Integrate agents with commands

**Deliverable**: Agent iteratively refines API specs based on validation feedback until they pass all guidelines.

---

## Key Insights

1. **Hooks are the game-changer**: They transform validation from a manual checklist item to an automatic guardrail.

2. **Skills are the foundation**: Everything builds on skills. Get skills right, and the rest follows.

3. **Workflows provide repeatability**: They're the difference between ad-hoc processes and engineering discipline.

4. **Agents add intelligence**: They handle the "figure it out" tasks that workflows can't.

5. **Commands improve UX**: They make complex operations feel simple.

6. **Layers enable progressive complexity**: Start with skills, add layers as needed.

---

## See Also

- [Betty Skills Framework](./skills-framework.md) - Complete skill taxonomy
- [API-Driven Development Guide](./api-driven-development.md) - Detailed implementation guide
- [Hooks Reference](https://docs.claude.com/en/docs/claude-code/hooks) - Claude Code hooks documentation
- [Agent Skills Overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) - Claude Code agent documentation
