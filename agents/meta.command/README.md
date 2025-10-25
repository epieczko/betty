# meta.command - Command Creator Meta-Agent

Creates complete, production-ready command manifests from natural language descriptions.

## Purpose

The `meta.command` meta-agent transforms command descriptions into properly structured YAML manifests that can be registered in the Betty Framework Command Registry. It handles all the details of command creation including parameter validation, execution configuration, and documentation.

## What It Does

- ✅ Parses natural language command descriptions (Markdown or JSON)
- ✅ Generates complete command manifests in YAML format
- ✅ Validates command structure and execution types
- ✅ Supports all three execution types: agent, skill, workflow
- ✅ Creates proper parameter definitions with type validation
- ✅ Prepares commands for registration via `command.define` skill
- ✅ Supports traceability tracking

## Usage

```bash
python3 agents/meta.command/meta_command.py <description_file>
```

### With Traceability

```bash
python3 agents/meta.command/meta_command.py examples/api_validate_command.md \
  --requirement-id "REQ-2025-042" \
  --requirement-description "Create command for API validation" \
  --rationale "Simplify API validation workflow for developers"
```

## Input Format

### Markdown Format

Create a description file with the following structure:

```markdown
# Name: /api-validate
# Version: 0.1.0
# Description: Validate API specifications against standards

# Execution Type: skill
# Target: api.validate

# Parameters:
- spec_file: string (required) - Path to API specification file
- format: enum (optional, default=openapi, values=[openapi,asyncapi,grpc]) - API specification format
- strict: boolean (optional, default=true) - Enable strict validation mode

# Execution Context:
- format: json
- timeout: 300

# Status: active

# Tags: api, validation, quality
```

### JSON Format

Alternatively, use JSON:

```json
{
  "name": "/api-validate",
  "version": "0.1.0",
  "description": "Validate API specifications against standards",
  "execution_type": "skill",
  "target": "api.validate",
  "parameters": [
    {
      "name": "spec_file",
      "type": "string",
      "required": true,
      "description": "Path to API specification file"
    },
    {
      "name": "format",
      "type": "enum",
      "values": ["openapi", "asyncapi", "grpc"],
      "default": "openapi",
      "description": "API specification format"
    }
  ],
  "execution_context": {
    "format": "json",
    "timeout": 300
  },
  "status": "active",
  "tags": ["api", "validation", "quality"]
}
```

## Command Execution Types

### 1. Agent Execution

Use for complex, context-aware tasks requiring reasoning:

```markdown
# Name: /api-design
# Execution Type: agent
# Target: api.architect
# Description: Design a complete API architecture
```

**When to use:**
- Tasks requiring multi-step reasoning
- Context-aware decision making
- Complex analysis or design work

### 2. Skill Execution

Use for atomic, deterministic operations:

```markdown
# Name: /api-validate
# Execution Type: skill
# Target: api.validate
# Description: Validate API specifications
```

**When to use:**
- Direct, predictable operations
- Fast, single-purpose tasks
- Composable building blocks

### 3. Workflow Execution

Use for orchestrated multi-step processes:

```markdown
# Name: /api-pipeline
# Execution Type: workflow
# Target: workflows/api-pipeline.yaml
# Description: Execute full API development pipeline
```

**When to use:**
- Multi-agent/skill coordination
- Sequential or parallel task execution
- Complex business processes

## Parameter Types

### Supported Types

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text values | `"api-spec.yaml"` |
| `integer` | Whole numbers | `42` |
| `boolean` | true/false | `true` |
| `enum` | Fixed set of values | `["openapi", "asyncapi"]` |
| `array` | Lists of values | `["tag1", "tag2"]` |
| `object` | Structured data | `{"key": "value"}` |

### Parameter Options

- `required: true/false` - Whether parameter is mandatory
- `default: value` - Default value if not provided
- `values: [...]` - Allowed values (for enum type)
- `description: "..."` - What the parameter does

## Examples

### Example 1: Simple Validation Command

**Input:** `examples/api-validate-cmd.md`

```markdown
# Name: /api-validate
# Description: Validate API specification files
# Execution Type: skill
# Target: api.validate

# Parameters:
- spec_file: string (required) - Path to specification file
- format: enum (optional, default=openapi, values=[openapi,asyncapi]) - Spec format

# Status: active
# Tags: api, validation
```

**Output:** `commands/api-validate.yaml`

```yaml
name: /api-validate
version: 0.1.0
description: Validate API specification files
parameters:
  - name: spec_file
    type: string
    required: true
    description: Path to specification file
  - name: format
    type: enum
    values:
      - openapi
      - asyncapi
    default: openapi
    description: Spec format
execution:
  type: skill
  target: api.validate
status: active
tags:
  - api
  - validation
```

### Example 2: Agent-Based Design Command

**Input:** `examples/api-design-cmd.md`

```markdown
# Name: /api-design
# Description: Design a complete API architecture
# Execution Type: agent
# Target: api.architect

# Parameters:
- requirements: string (required) - Path to requirements document
- style: enum (optional, default=rest, values=[rest,graphql,grpc]) - API style

# Execution Context:
- reasoning_mode: iterative
- max_iterations: 10

# Status: active
# Tags: api, design, architecture
```

**Output:** `commands/api-design.yaml`

```yaml
name: /api-design
version: 0.1.0
description: Design a complete API architecture
parameters:
  - name: requirements
    type: string
    required: true
    description: Path to requirements document
  - name: style
    type: enum
    values:
      - rest
      - graphql
      - grpc
    default: rest
    description: API style
execution:
  type: agent
  target: api.architect
  context:
    reasoning_mode: iterative
    max_iterations: 10
status: active
tags:
  - api
  - design
  - architecture
```

### Example 3: Workflow Command

**Input:** `examples/deploy-cmd.md`

```markdown
# Name: /deploy
# Description: Deploy application to specified environment
# Execution Type: workflow
# Target: workflows/deploy-pipeline.yaml

# Parameters:
- environment: enum (required, values=[dev,staging,production]) - Target environment
- version: string (required) - Version to deploy
- skip_tests: boolean (optional, default=false) - Skip test execution

# Status: draft
# Tags: deployment, devops
```

## Output

The meta-agent creates:

1. **Command Manifest** - Complete YAML file in `commands/` directory
2. **Console Output** - Summary of created command
3. **Next Steps** - Instructions for registration

Example console output:

```
🎯  meta.command - Creating command from examples/api-validate-cmd.md

✨ Command '/api-validate' created successfully!

📄 Created file:
   - commands/api-validate.yaml

✅ Command manifest is ready for registration
   Name: /api-validate
   Execution: skill → api.validate
   Status: active

📝 Next steps:
   1. Review the manifest: cat commands/api-validate.yaml
   2. Register command: python3 skills/command.define/command_define.py commands/api-validate.yaml
   3. Verify in registry: cat registry/commands.json
```

## Integration with command.define

After creating a command manifest, register it using the `command.define` skill:

```bash
# Register the command
python3 skills/command.define/command_define.py commands/api-validate.yaml

# Verify registration
cat registry/commands.json
```

The `command.define` skill will:
- Validate the manifest structure
- Check that the execution target exists
- Add the command to the Command Registry
- Make the command available for use

## Artifact Flow

```
┌──────────────────────────┐
│ Command Description      │
│ (Markdown or JSON)       │
└──────────┬───────────────┘
           │ consumes
           ▼
    ┌──────────────┐
    │ meta.command │
    └──────┬───────┘
           │ produces
           ▼
┌──────────────────────────┐
│ Command Manifest (YAML)  │
│ commands/*.yaml          │
└──────────┬───────────────┘
           │
           ▼
    ┌──────────────┐
    │command.define│
    │   (skill)    │
    └──────┬───────┘
           │
           ▼
┌──────────────────────────┐
│ Commands Registry        │
│ registry/commands.json   │
└──────────────────────────┘
```

## Command Naming Conventions

- ✅ Must start with `/` (e.g., `/api-validate`)
- ✅ Use kebab-case for multi-word commands (e.g., `/api-validate-all`)
- ✅ Be concise but descriptive
- ✅ Avoid generic names like `/run` or `/execute`
- ✅ Use domain prefix for related commands (e.g., `/api-*`, `/db-*`)

## Validation

The meta-agent validates:

- ✅ Required fields present (name, description, execution_type, target)
- ✅ Valid execution type (agent, skill, workflow)
- ✅ **Execution target exists** (skill in registry, agent in registry, or workflow file)
- ✅ Command name starts with `/`
- ✅ Parameter types are valid
- ✅ Enum parameters have values defined
- ✅ Version follows semantic versioning
- ✅ Status is valid (draft, active, deprecated, archived)

### Target Validation

The meta-agent performs **mandatory validation** to ensure the execution target exists:

**For skill execution:**
- Checks if the skill exists in `registry/skills.json`
- Fails with error if skill not found
- Lists all available skills for reference

**For agent execution:**
- Checks if the agent exists in `registry/agents.json`
- Fails with error if agent not found
- Lists all available agents for reference

**For workflow execution:**
- Checks if the workflow file exists in `workflows/` directory
- Supports both full paths and workflow names
- Fails with error if workflow file not found

This **fail-fast approach** prevents creating command manifests that will fail during registration.

## Error Handling

Common errors and solutions:

**Missing required fields:**
```
❌ Error: Missing required fields: execution_type, target
```
→ Add all required fields to your description

**Invalid execution type:**
```
❌ Error: Invalid execution type: service. Must be one of: agent, skill, workflow
```
→ Use only valid execution types

**Target not found (skill):**
```
❌ Error: Skill 'nonexistent.skill' not found in skill registry.
Available skills: api.validate, workflow.compose, ...
```
→ Use a skill that exists in the registry, or create the skill first using meta.skill

**Target not found (agent):**
```
❌ Error: Agent 'nonexistent.agent' not found in agent registry.
Available agents: api.designer, api.analyzer
```
→ Use an agent that exists in the registry, or create the agent first using meta.agent

**Target not found (workflow):**
```
❌ Error: Workflow file not found: /home/user/betty/workflows/nonexistent.yaml
Expected workflow file at: /home/user/betty/workflows/nonexistent.yaml
```
→ Create the workflow file first, or check the target path

**Invalid parameter type:**
```
❌ Error: Invalid parameter type: float
```
→ Use supported parameter types

## Best Practices

1. **Clear Descriptions** - Write concise, actionable command descriptions
2. **Proper Parameters** - Define all parameters with types and validation
3. **Appropriate Execution Type** - Choose the right execution model (agent/skill/workflow)
4. **Meaningful Tags** - Add relevant tags for discoverability
5. **Version Management** - Start with 0.1.0, increment appropriately
6. **Status Lifecycle** - Use draft → active → deprecated → archived

## Files Generated

```
commands/
└── {command-name}.yaml    # Command manifest
```

## Integration with Meta-Agents

The `meta.command` agent works alongside:

- **meta.skill** - Create skills that commands can execute
- **meta.agent** - Create agents that commands can delegate to
- **meta.artifact** - Define artifact types for command I/O
- **meta.compatibility** - Find compatible agents for command workflows

## Traceability

Track command creation with requirement metadata:

```bash
python3 agents/meta.command/meta_command.py examples/api-validate-cmd.md \
  --requirement-id "REQ-2025-042" \
  --requirement-description "API validation command" \
  --issue-id "BETTY-123" \
  --requested-by "dev-team" \
  --rationale "Streamline API validation process"
```

View trace:
```bash
python3 betty/trace_cli.py show command.api_validate
```

## See Also

- **command.define skill** - Register command manifests
- **meta.skill** - Create skills for command execution
- **meta.agent** - Create agents for command delegation
- **Command Registry** - `registry/commands.json`
- **Command Infrastructure** - `docs/COMMAND_HOOK_INFRASTRUCTURE.md`
