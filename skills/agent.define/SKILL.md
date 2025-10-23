# agent.define Skill

Validates and registers agent manifests for the Betty Framework.

## Purpose

The `agent.define` skill is the Layer 2 (Reasoning Layer) equivalent of `skill.define`. It validates agent manifests (`agent.yaml`) for schema compliance, verifies skill references, and updates the central Agent Registry.

## Capabilities

- Validate agent manifest structure and required fields
- Verify agent name and version formats
- Validate reasoning mode enum values
- Check that all referenced skills exist in skill registry
- Ensure capabilities and skills lists are non-empty
- Validate status lifecycle values
- Register valid agents in `/registry/agents.json`
- Update existing agent entries with new versions

## Usage

### Command Line

```bash
python skills/agent.define/agent_define.py <path_to_agent.yaml>
```

### Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `manifest_path` | string | Yes | Path to the agent.yaml file to validate |

### Exit Codes

- `0`: Validation succeeded and agent was registered
- `1`: Validation failed or registration error

## Validation Rules

### Required Fields

All agent manifests must include:

| Field | Type | Validation |
|-------|------|------------|
| `name` | string | Must match `^[a-z][a-z0-9._-]*$` |
| `version` | string | Must follow semantic versioning |
| `description` | string | Non-empty string (1-200 chars recommended) |
| `capabilities` | array[string] | Must contain at least one item |
| `skills_available` | array[string] | Must contain at least one item, all skills must exist in registry |
| `reasoning_mode` | enum | Must be `iterative` or `oneshot` |

### Optional Fields

| Field | Type | Default | Validation |
|-------|------|---------|------------|
| `status` | enum | `draft` | Must be `draft`, `active`, `deprecated`, or `archived` |
| `context_requirements` | object | `{}` | Any valid object |
| `workflow_pattern` | string | `null` | Any string |
| `example_task` | string | `null` | Any string |
| `error_handling` | object | `{}` | Any valid object |
| `output` | object | `{}` | Any valid object |
| `tags` | array[string] | `[]` | Array of strings |
| `dependencies` | array[string] | `[]` | Array of strings |

### Name Format

Agent names must:
- Start with a lowercase letter
- Contain only lowercase letters, numbers, dots, hyphens, underscores
- Follow pattern: `<domain>.<action>`

**Valid**: `api.designer`, `compliance.checker`, `data-migrator`
**Invalid**: `ApiDesigner`, `1agent`, `agent_name`

### Version Format

Versions must follow semantic versioning: `MAJOR.MINOR.PATCH[-prerelease]`

**Valid**: `0.1.0`, `1.0.0`, `2.3.1-beta`, `1.0.0-rc.1`
**Invalid**: `1.0`, `v1.0.0`, `1.0.0.0`

### Reasoning Mode

Must be one of:
- `iterative`: Agent can retry with feedback and refine based on errors
- `oneshot`: Agent executes once without retry

### Skills Validation

All skills in `skills_available` must exist in the skill registry (`/registry/skills.json`).

## Response Format

### Success Response

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "agents/api.designer/agent.yaml",
  "details": {
    "valid": true,
    "errors": [],
    "path": "agents/api.designer/agent.yaml",
    "manifest": {
      "name": "api.designer",
      "version": "0.1.0",
      "description": "Design RESTful APIs...",
      "capabilities": [...],
      "skills_available": [...],
      "reasoning_mode": "iterative"
    },
    "status": "registered",
    "registry_updated": true
  }
}
```

### Failure Response

```json
{
  "ok": false,
  "status": "failed",
  "errors": [
    "Missing required fields: capabilities, skills_available",
    "Invalid reasoning_mode: 'hybrid'. Must be one of: iterative, oneshot"
  ],
  "path": "agents/bad.agent/agent.yaml",
  "details": {
    "valid": false,
    "errors": [
      "Missing required fields: capabilities, skills_available",
      "Invalid reasoning_mode: 'hybrid'. Must be one of: iterative, oneshot"
    ],
    "path": "agents/bad.agent/agent.yaml"
  }
}
```

## Examples

### Example 1: Validate Iterative Agent

**Agent Manifest** (`agents/api.designer/agent.yaml`):
```yaml
name: api.designer
version: 0.1.0
description: "Design RESTful APIs following enterprise guidelines"

capabilities:
  - Design RESTful APIs from requirements
  - Apply Zalando guidelines automatically
  - Generate OpenAPI 3.1 specs
  - Iteratively refine based on validation feedback

skills_available:
  - api.define
  - api.validate
  - api.generate-models

reasoning_mode: iterative

status: draft

tags:
  - api
  - design
  - openapi
```

**Command**:
```bash
python skills/agent.define/agent_define.py agents/api.designer/agent.yaml
```

**Output**:
```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "agents/api.designer/agent.yaml",
  "details": {
    "valid": true,
    "status": "registered",
    "registry_updated": true
  }
}
```

### Example 2: Validation Errors

**Agent Manifest** (`agents/bad.agent/agent.yaml`):
```yaml
name: BadAgent  # Invalid: must be lowercase
version: 1.0   # Invalid: must be semver
description: "Test agent"
capabilities: []  # Invalid: must have at least one
skills_available:
  - nonexistent.skill  # Invalid: skill doesn't exist
reasoning_mode: hybrid  # Invalid: must be iterative or oneshot
```

**Command**:
```bash
python skills/agent.define/agent_define.py agents/bad.agent/agent.yaml
```

**Output**:
```json
{
  "ok": false,
  "status": "failed",
  "errors": [
    "Invalid name: Invalid agent name: 'BadAgent'. Must start with lowercase letter...",
    "Invalid version: Invalid version: '1.0'. Must follow semantic versioning...",
    "Invalid reasoning_mode: Invalid reasoning_mode: 'hybrid'. Must be one of: iterative, oneshot",
    "capabilities must contain at least one item",
    "Skills not found in registry: nonexistent.skill"
  ],
  "path": "agents/bad.agent/agent.yaml"
}
```

### Example 3: Oneshot Agent

**Agent Manifest** (`agents/api.analyzer/agent.yaml`):
```yaml
name: api.analyzer
version: 0.1.0
description: "Analyze API specifications for compatibility"

capabilities:
  - Detect breaking changes between API versions
  - Generate compatibility reports
  - Suggest migration paths

skills_available:
  - api.compatibility

reasoning_mode: oneshot

output:
  success:
    - Compatibility report
    - Breaking changes list
  failure:
    - Error analysis

status: active

tags:
  - api
  - analysis
  - compatibility
```

**Command**:
```bash
python skills/agent.define/agent_define.py agents/api.analyzer/agent.yaml
```

**Result**: Agent validated and registered successfully.

## Integration

### With Registry

The skill automatically updates `/registry/agents.json`:

```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T10:30:00Z",
  "agents": [
    {
      "name": "api.designer",
      "version": "0.1.0",
      "description": "Design RESTful APIs following enterprise guidelines",
      "reasoning_mode": "iterative",
      "skills_available": ["api.define", "api.validate", "api.generate-models"],
      "capabilities": ["Design RESTful APIs from requirements", ...],
      "status": "draft",
      "tags": ["api", "design", "openapi"],
      "dependencies": []
    }
  ]
}
```

### With Other Skills

- **Depends on**: `skill.define` (for skill registry validation)
- **Used by**: Future `command.define` skill (to register commands that invoke agents)
- **Complements**: `workflow.compose` (agents orchestrate skills; workflows execute fixed sequences)

## Common Errors

### Missing Skills in Registry

**Error**:
```
Skills not found in registry: api.nonexistent, data.missing
```

**Solution**: Ensure all skills in `skills_available` are registered in `/registry/skills.json`. Check skill names for typos.

### Invalid Reasoning Mode

**Error**:
```
Invalid reasoning_mode: 'hybrid'. Must be one of: iterative, oneshot
```

**Solution**: Use `iterative` for agents that retry with feedback, or `oneshot` for deterministic execution.

### Empty Capabilities

**Error**:
```
capabilities must contain at least one item
```

**Solution**: Add at least one capability string describing what the agent can do.

### Invalid Name Format

**Error**:
```
Invalid agent name: 'API-Designer'. Must start with lowercase letter...
```

**Solution**: Use lowercase names following pattern `<domain>.<action>` (e.g., `api.designer`).

## Development

### Testing

Create test agent manifests in `/agents/test/`:

```bash
# Create test directory
mkdir -p agents/test.agent

# Create minimal test manifest
cat > agents/test.agent/agent.yaml << EOF
name: test.agent
version: 0.1.0
description: "Test agent"
capabilities:
  - Test capability
skills_available:
  - skill.define
reasoning_mode: oneshot
status: draft
EOF

# Validate
python skills/agent.define/agent_define.py agents/test.agent/agent.yaml
```

### Registry Location

- Skill registry: `/registry/skills.json` (read for validation)
- Agent registry: `/registry/agents.json` (updated by this skill)

## See Also

- [Agent Schema Reference](../../docs/agent-schema-reference.md) - Complete field specifications
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer architecture overview
- [Agent Implementation Plan](../../docs/agent-define-implementation-plan.md) - Implementation details
- `/agents/README.md` - Agent directory documentation
