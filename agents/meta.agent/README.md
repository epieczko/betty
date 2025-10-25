# meta.agent - Agent Creator

The meta-agent that creates other agents through skill composition.

## Overview

**meta.agent** transforms natural language descriptions into complete, functional agents with proper skill composition, artifact metadata, and documentation.

**What it produces:**
- Complete `agent.yaml` with recommended skills
- Auto-generated `README.md` documentation
- Proper artifact metadata (produces/consumes)
- Inferred permissions from skills

## Quick Start

### 1. Create an Agent Description

Create a Markdown file describing your agent:

```markdown
# Name: api.architect

# Purpose:
An agent that designs comprehensive REST APIs and validates them
against best practices.

# Inputs:
- API requirements

# Outputs:
- openapi-spec
- validation-report
- api-models

# Examples:
- Design a RESTful API for an e-commerce platform
- Create an API for a task management system
```

### 2. Run meta.agent

```bash
python3 agents/meta.agent/meta_agent.py examples/api_architect_description.md
```

### 3. Output

```
✨ Agent 'api.architect' created successfully!

📄 Agent definition: agents/api.architect/agent.yaml
📖 Documentation: agents/api.architect/README.md

🔧 Skills: api.define, api.validate, workflow.validate
```

## Usage

### Basic Creation

```bash
# Create agent from Markdown description
python3 agents/meta.agent/meta_agent.py path/to/agent_description.md

# Create agent from JSON description
python3 agents/meta.agent/meta_agent.py path/to/agent_description.json

# Specify output directory
python3 agents/meta.agent/meta_agent.py description.md -o agents/my-agent

# Skip validation
python3 agents/meta.agent/meta_agent.py description.md --no-validate
```

### Description Format

**Markdown Format:**

```markdown
# Name: agent-name

# Purpose:
Detailed description of what the agent does...

# Inputs:
- artifact-type-1
- artifact-type-2

# Outputs:
- artifact-type-3
- artifact-type-4

# Constraints:
(Optional) Any constraints or requirements...

# Examples:
- Example use case 1
- Example use case 2
```

**JSON Format:**

```json
{
  "name": "agent-name",
  "purpose": "Detailed description...",
  "inputs": ["artifact-type-1", "artifact-type-2"],
  "outputs": ["artifact-type-3", "artifact-type-4"],
  "examples": ["Example 1", "Example 2"]
}
```

## What meta.agent Creates

### 1. agent.yaml

Complete agent definition with:
- **Recommended skills** - Uses `agent.compose` to find compatible skills
- **Artifact metadata** - Proper produces/consumes declarations
- **Permissions** - Inferred from selected skills
- **Description** - Professional formatting

Example output:
```yaml
name: api.architect
description: Designs and validates REST APIs against best practices
skills_available:
  - api.define
  - api.validate
permissions:
  - filesystem:read
  - filesystem:write
artifact_metadata:
  consumes:
    - type: api-requirements
  produces:
    - type: openapi-spec
      schema: schemas/openapi-spec.json
    - type: validation-report
      schema: schemas/validation-report.json
```

### 2. README.md

Auto-generated documentation with:
- Agent purpose and capabilities
- Skills used with rationale
- Artifact flow (inputs/outputs)
- Example use cases
- Usage instructions
- "Created by meta.agent" attribution

## How It Works

1. **Parse Description** - Reads Markdown or JSON
2. **Find Skills** - Uses `agent.compose` to recommend compatible skills
3. **Generate Metadata** - Uses `artifact.define` for artifact contracts
4. **Infer Permissions** - Analyzes required skills
5. **Create Files** - Generates agent.yaml and README.md
6. **Validate** - Ensures proper structure and compatibility

## Integration with Other Meta-Agents

### With meta.compatibility

After creating an agent, use `meta.compatibility` to analyze it:

```bash
# Create agent
python3 agents/meta.agent/meta_agent.py description.md

# Analyze compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze api.architect
```

### With meta.suggest

Get suggestions after creating an agent:

```bash
python3 agents/meta.suggest/meta_suggest.py \
  --context meta.agent \
  --artifacts agents/api.architect/agent.yaml
```

## Common Workflows

### Workflow 1: Create and Analyze

```bash
# Step 1: Create agent
python3 agents/meta.agent/meta_agent.py examples/my_agent.md

# Step 2: Analyze compatibility
python3 agents/meta.compatibility/meta_compatibility.py find-compatible my-agent

# Step 3: Test the agent
# (Manual testing or agent.run)
```

### Workflow 2: Create Multiple Agents

```bash
# Create several agents
for desc in examples/*_agent_description.md; do
    python3 agents/meta.agent/meta_agent.py "$desc"
done

# Analyze the ecosystem
python3 agents/meta.compatibility/meta_compatibility.py list-all
```

## Artifact Types

### Consumes

- **agent-description** - Natural language agent requirements
  - Format: Markdown or JSON
  - Pattern: `**/agent_description.md`

### Produces

- **agent-definition** - Complete agent.yaml
  - Format: YAML
  - Pattern: `agents/*/agent.yaml`
  - Schema: `schemas/agent-definition.json`

- **agent-documentation** - Auto-generated README
  - Format: Markdown
  - Pattern: `agents/*/README.md`

## Tips & Best Practices

### Writing Good Descriptions

✅ **Good:**
- Clear, specific purpose
- Well-defined inputs and outputs
- Concrete examples
- Specific artifact types

❌ **Avoid:**
- Vague purpose ("does stuff")
- Generic inputs ("data")
- No examples
- Unclear artifact types

### Choosing Artifact Types

Use existing artifact types when possible:
- `openapi-spec` for API specifications
- `validation-report` for validation results
- `workflow-definition` for workflows

If you need a new type, create it with `meta.artifact` first.

### Skill Selection

meta.agent uses keyword matching to find skills:
- "api" → finds api.define, api.validate
- "validate" → finds validation skills
- "agent" → finds agent.compose, meta.agent

Be descriptive in your purpose statement to get better skill recommendations.

## Troubleshooting

### Agent name conflicts

```
Error: Agent 'api.architect' already exists
```

**Solution:** Choose a different name or remove the existing agent directory.

### No skills recommended

```
Warning: No skills found for agent purpose
```

**Solutions:**
- Make purpose more specific
- Mention artifact types explicitly
- Check if relevant skills exist in registry

### Missing artifact types

```
Warning: Artifact type 'my-artifact' not in known registry
```

**Solution:** Create the artifact type with `meta.artifact` first:
```bash
python3 agents/meta.artifact/meta_artifact.py create artifact_description.md
```

## Examples

See `examples/` directory for sample agent descriptions:
- `api_architect_description.md` - API design and validation agent
- (Add more as you create them)

## Architecture

meta.agent is part of the meta-agent ecosystem:

```
meta.agent
    ├─ Uses: agent.compose (find skills)
    ├─ Uses: artifact.define (generate metadata)
    ├─ Produces: agent.yaml + README.md
    └─ Works with: meta.compatibility, meta.suggest
```

## Related Documentation

- [META_AGENTS.md](../../docs/META_AGENTS.md) - Complete meta-agent architecture
- [ARTIFACT_STANDARDS.md](../../docs/ARTIFACT_STANDARDS.md) - Artifact system
- [agent-description schema](../../schemas/agent-description.json) - JSON schema

## Created By

Part of the Betty Framework meta-agent ecosystem.
