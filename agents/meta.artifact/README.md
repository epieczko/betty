# meta.artifact - The Artifact Standards Authority

THE single source of truth for all artifact type definitions in Betty Framework.

## Overview

**meta.artifact** manages the complete lifecycle of artifact types - from definition to documentation to registration. All artifact types MUST be created through meta.artifact. No ad-hoc definitions are permitted.

**What it does:**
- Defines new artifact types from descriptions
- Generates JSON schemas with validation rules
- Updates ARTIFACT_STANDARDS.md automatically
- Registers types in KNOWN_ARTIFACT_TYPES
- Validates uniqueness and prevents conflicts

## Quick Start

### 1. Create Artifact Description

```markdown
# Name: optimization-report

# Purpose:
Performance and security optimization recommendations for APIs

# Format: JSON

# File Pattern: *.optimization.json

# Schema Properties:
- optimizations (array): List of optimization recommendations
- severity (string): Severity level
- analyzed_artifact (string): Reference to analyzed artifact

# Required Fields:
- optimizations
- severity
- analyzed_artifact

# Producers:
- api.optimize

# Consumers:
- api.implement
- report.generate
```

### 2. Create Artifact Type

```bash
python3 agents/meta.artifact/meta_artifact.py create examples/optimization_report_artifact.md
```

### 3. Output

```
✨ Artifact type 'optimization-report' created successfully!

📄 Created files:
   - schemas/optimization-report.json

📝 Updated files:
   - docs/ARTIFACT_STANDARDS.md
   - skills/artifact.define/artifact_define.py

✅ Artifact type 'optimization-report' is now registered
```

## Usage

### Create New Artifact Type

```bash
# From Markdown description
python3 agents/meta.artifact/meta_artifact.py create artifact_description.md

# From JSON description
python3 agents/meta.artifact/meta_artifact.py create artifact_description.json

# Force overwrite if exists
python3 agents/meta.artifact/meta_artifact.py create artifact_description.md --force
```

### Check if Artifact Exists

```bash
python3 agents/meta.artifact/meta_artifact.py check optimization-report
```

Output:
```
✅ Artifact type 'optimization-report' exists
   Location: docs/ARTIFACT_STANDARDS.md
```

## What meta.artifact Creates

### 1. JSON Schema (schemas/*.json)

Complete JSON Schema Draft 07 schema with:
- Properties from description
- Required fields
- Type validation
- Descriptions

Example:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Optimization Report",
  "description": "Performance and security recommendations...",
  "type": "object",
  "required": ["optimizations", "severity", "analyzed_artifact"],
  "properties": {
    "optimizations": {
      "type": "array",
      "description": "List of optimization recommendations"
    },
    ...
  }
}
```

### 2. Documentation Section (docs/ARTIFACT_STANDARDS.md)

Adds complete section with:
- Artifact number and title
- Description
- Convention (file pattern, format, content type)
- Schema reference
- Producers and consumers
- Related types

### 3. Registry Entry (skills/artifact.define/artifact_define.py)

Adds to KNOWN_ARTIFACT_TYPES:
```python
"optimization-report": {
    "schema": "schemas/optimization-report.json",
    "file_pattern": "*.optimization.json",
    "content_type": "application/json",
    "description": "Performance and security optimization recommendations..."
}
```

## Description Format

### Markdown Format

```markdown
# Name: artifact-type-name

# Purpose:
Detailed description of what this artifact represents...

# Format: JSON | YAML | Markdown | Python | etc.

# File Pattern: *.artifact-type.ext

# Content Type: application/json (optional, inferred from format)

# Schema Properties:
- property_name (type): Description
- another_property (array): Description

# Required Fields:
- property_name
- another_property

# Producers:
- skill.that.produces
- agent.that.produces

# Consumers:
- skill.that.consumes
- agent.that.consumes

# Related Types:
- related-artifact-1
- related-artifact-2

# Validation Rules:
- Custom rule 1
- Custom rule 2
```

### JSON Format

```json
{
  "name": "artifact-type-name",
  "purpose": "Description...",
  "format": "JSON",
  "file_pattern": "*.artifact-type.json",
  "schema_properties": {
    "field1": {"type": "string", "description": "..."},
    "field2": {"type": "array", "description": "..."}
  },
  "required_fields": ["field1"],
  "producers": ["producer.skill"],
  "consumers": ["consumer.skill"]
}
```

## Governance Rules

meta.artifact enforces these rules:

1. **Uniqueness** - Each artifact type must have a unique name
2. **Clarity** - Names must be descriptive (e.g., "openapi-spec" not "spec")
3. **Consistency** - Must use kebab-case (lowercase with hyphens)
4. **Documentation** - Every type must be fully documented
5. **Schemas** - Every type should have a JSON schema (if applicable)
6. **No Conflicts** - Checks for naming conflicts before creating

## Workflow

```
Developer creates artifact_description.md
    ↓
meta.artifact validates name and format
    ↓
Checks if type already exists
    ↓
Generates JSON Schema
    ↓
Updates ARTIFACT_STANDARDS.md
    ↓
Adds to KNOWN_ARTIFACT_TYPES
    ↓
Validates all files
    ↓
Type is now registered and usable
```

## Integration

### With meta.agent (Atum)

When Atum needs a new artifact type:

```bash
# 1. Define the artifact type
python3 agents/meta.artifact/meta_artifact.py create my_artifact.md

# 2. Create agent that uses it
python3 agents/atum/atum.py agent_description.md
```

### With meta.suggest

meta.suggest will recommend creating artifact types for gaps:

```bash
python3 agents/meta.suggest/meta_suggest.py --analyze-project
```

Output includes:
```
💡 Suggestions:
   1. Create agent/skill to produce 'missing-artifact'
```

## Existing Artifact Types

Check `docs/ARTIFACT_STANDARDS.md` for all registered types:

- `openapi-spec` - OpenAPI specifications
- `validation-report` - Validation results
- `workflow-definition` - Betty workflows
- `hook-config` - Claude Code hooks
- `api-models` - Generated data models
- `agent-description` - Agent requirements
- `agent-definition` - Agent configurations
- `agent-documentation` - Agent READMEs
- `optimization-report` - Optimization recommendations
- `compatibility-graph` - Agent relationships
- `pipeline-suggestion` - Multi-agent workflows
- `suggestion-report` - Next-step recommendations

## Tips & Best Practices

### Naming Artifact Types

✅ **Good:**
- `validation-report` (clear, descriptive)
- `openapi-spec` (standard term)
- `optimization-report` (action + result)

❌ **Avoid:**
- `report` (too generic)
- `validationReport` (should be kebab-case)
- `val-rep` (abbreviations)

### Writing Descriptions

Be comprehensive:
- Explain what the artifact represents
- Include all important properties
- Document producers and consumers
- Add related types for discoverability

### Schema Properties

Be specific about types:
- Use JSON Schema types: string, number, integer, boolean, array, object
- Add descriptions for every property
- Mark required fields
- Consider validation rules

## Troubleshooting

### Name already exists

```
Error: Artifact type 'my-artifact' already exists at: docs/ARTIFACT_STANDARDS.md
```

**Solutions:**
1. Use `--force` to overwrite (careful!)
2. Choose a different name
3. Use the existing type if appropriate

### Invalid name format

```
Error: Artifact name must be kebab-case (lowercase with hyphens): MyArtifact
```

**Solution:** Use lowercase with hyphens: `my-artifact`

### Missing schema properties

If your artifact is JSON/YAML but has no schema properties, meta.artifact will still create a basic schema. Add properties for better validation.

## Architecture

meta.artifact is THE authority in the meta-agent ecosystem:

```
meta.artifact (Authority)
    ├─ Manages: All artifact type definitions
    ├─ Updates: ARTIFACT_STANDARDS.md
    ├─ Registers: KNOWN_ARTIFACT_TYPES
    ├─ Used by: meta.agent, meta.skill, all agents
    └─ Governance: Single source of truth
```

## Examples

See `examples/` for artifact descriptions:
- `optimization_report_artifact.md`
- `compatibility_graph_artifact.md`
- `pipeline_suggestion_artifact.md`
- `suggestion_report_artifact.md`

## Related Documentation

- [ARTIFACT_STANDARDS.md](../../docs/ARTIFACT_STANDARDS.md) - Complete artifact documentation
- [artifact-type-description schema](../../schemas/artifact-type-description.json)
- [META_AGENTS.md](../../docs/META_AGENTS.md) - Meta-agent ecosystem

## Philosophy

**Single Source of Truth** - All artifact definitions flow through meta.artifact. This ensures:
- Consistency across the framework
- Proper documentation
- Schema validation
- No conflicts
- Discoverability

When in doubt, ask meta.artifact.
