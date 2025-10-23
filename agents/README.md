# Betty Framework Agents

This directory contains agent manifests for the Betty Framework.

## What are Agents?

Agents are intelligent orchestrators that compose skills with reasoning, context awareness, and error recovery. Unlike workflows (which follow fixed sequential steps) or skills (which execute atomic operations), agents can:

- **Reason** about requirements and choose appropriate strategies
- **Iterate** based on feedback and validation results
- **Recover** from errors with intelligent retry logic
- **Adapt** their approach based on context

## Directory Structure

Each agent has its own directory containing:
```
agents/
├── <agent-name>/
│   ├── agent.yaml              # Agent manifest (required)
│   ├── README.md               # Documentation (auto-generated)
│   └── tests/                  # Agent behavior tests (optional)
│       └── test_agent.py
```

## Creating an Agent

### Manual Creation

1. Create agent directory:
   ```bash
   mkdir -p agents/my.agent
   ```

2. Create agent manifest (`agents/my.agent/agent.yaml`):
   ```yaml
   name: my.agent
   version: 0.1.0
   description: "What your agent does"

   capabilities:
     - First capability
     - Second capability

   skills_available:
     - skill.one
     - skill.two

   reasoning_mode: iterative  # or oneshot

   status: draft
   ```

3. Validate and register:
   ```bash
   python skills/agent.define/agent_define.py agents/my.agent/agent.yaml
   ```

### Using agent.define Skill

```bash
# Validate an agent manifest
python skills/agent.define/agent_define.py agents/<agent-name>/agent.yaml
```

## Agent Manifest Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique identifier (e.g., `api.designer`) |
| `version` | string | Semantic version (e.g., `0.1.0`) |
| `description` | string | Human-readable purpose statement |
| `capabilities` | array[string] | List of what the agent can do |
| `skills_available` | array[string] | Skills the agent can orchestrate |
| `reasoning_mode` | enum | `iterative` or `oneshot` |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | enum | `draft`, `active`, `deprecated`, `archived` |
| `context_requirements` | object | Structured context the agent needs |
| `workflow_pattern` | string | Narrative description of reasoning process |
| `example_task` | string | Concrete usage example |
| `error_handling` | object | Retry strategies and failure handling |
| `output` | object | Expected success/failure outputs |
| `tags` | array[string] | Categorization tags |
| `dependencies` | array[string] | Other agents or schemas |

## Reasoning Modes

### Iterative
Agent can retry with feedback, refine based on errors, and improve incrementally.

**Use for:**
- Validation loops (API design with validation feedback)
- Refinement tasks (code optimization)
- Error correction (fixing compilation errors)

**Example:**
```yaml
reasoning_mode: iterative

error_handling:
  max_retries: 3
  on_validation_failure: "Analyze errors, refine spec, retry"
```

### Oneshot
Agent executes once without retry.

**Use for:**
- Analysis and reporting (compatibility checks)
- Deterministic transformations (code generation)
- Tasks where retry doesn't help (documentation)

**Example:**
```yaml
reasoning_mode: oneshot

output:
  success:
    - Analysis report
  failure:
    - Error details
```

## Example Agents

See the documentation for example agent manifests:
- [API Designer](../docs/agent-schema-reference.md#example-iterative-refinement-agent) - Iterative API design
- [Compliance Checker](../docs/agent-schema-reference.md#example-multi-domain-agent) - Multi-domain compliance

## Validation

All agent manifests are automatically validated for:
- Required fields presence
- Name format (`^[a-z][a-z0-9._-]*$`)
- Version format (semantic versioning)
- Reasoning mode enum (`iterative` or `oneshot`)
- Skill references (all skills must exist in skill registry)

## Registry

Validated agents are registered in `/registry/agents.json`:
```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T00:00:00Z",
  "agents": [
    {
      "name": "api.designer",
      "version": "0.1.0",
      "description": "Design RESTful APIs...",
      "reasoning_mode": "iterative",
      "skills_available": ["api.define", "api.validate"],
      "status": "draft"
    }
  ]
}
```

## See Also

- [Agent Schema Reference](../docs/agent-schema-reference.md) - Complete field reference
- [Betty Architecture](../docs/betty-architecture.md) - Five-layer architecture
- [Agent Implementation Plan](../docs/agent-define-implementation-plan.md) - Implementation details
