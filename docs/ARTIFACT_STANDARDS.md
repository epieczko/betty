# Betty Framework - Artifact Standards

## Overview

Betty Framework uses **artifact metadata** to enable certified skills and agents to interoperate autonomously. While Claude Code doesn't support hard-coded workflows (skills are invoked autonomously), artifact standards ensure that skills can discover and consume each other's outputs reliably.

## Philosophy: Hybrid Approach

Betty uses a **3-tier artifact system**:

### Tier 1: Conventions (Required)
- Documented file patterns and naming standards
- All certified skills MUST document what they produce/consume
- Lightweight and always present

### Tier 2: Metadata (Optional but Encouraged)
- Skills MAY declare `artifact_metadata` in skill.yaml
- Enables runtime validation and better Claude understanding
- Recommended for all certified skills

### Tier 3: Guidance (Agent System Prompts)
- Agents reference artifact standards in system prompts
- Guides Claude's autonomous skill selection
- Not mandatory but improves reliability

---

## Artifact Metadata Reusability

**Key Principle: Artifact metadata is defined once at the skill level and automatically inherited by all agents that use those skills.**

### Skills Define, Agents Inherit

Artifact metadata lives in **skills** (the source of truth), not in agents:

```yaml
# skills/api.define/skill.yaml
name: api.define
artifact_metadata:
  produces:
    - type: openapi-spec
      schema: schemas/openapi-spec.json
      file_pattern: "*.openapi.yaml"

# skills/api.validate/skill.yaml
name: api.validate
artifact_metadata:
  consumes:
    - type: openapi-spec
  produces:
    - type: validation-report
```

**Agents automatically inherit artifact capabilities from their skills:**

```yaml
# agents/api.designer/agent.yaml
name: api.designer
skills_available:
  - api.define        # Inherits: produces openapi-spec
  - api.validate      # Inherits: consumes openapi-spec, produces validation-report

# Agent can now work with:
# - openapi-spec (from api.define and api.validate)
# - validation-report (from api.validate)
# WITHOUT duplicating any artifact_metadata!
```

### Benefits of Reusability

✅ **DRY (Don't Repeat Yourself)**
- Artifact metadata defined **once** at skill level
- Multiple agents can use the same skill
- No duplication across agent definitions

✅ **Automatic Capability Discovery**
```python
# Betty can derive agent capabilities automatically
agent_artifacts = get_artifacts_from_skills(agent['skills_available'])
# Returns all artifacts the agent can produce/consume
```

✅ **Consistency Enforcement**
- All agents using `api.define` produce the **same** openapi-spec format
- Schema is enforced at the skill level
- No divergence across agents

✅ **Composability**
```yaml
# Create new agent by composing existing skills
agents/api.migrator/agent.yaml:
  skills_available:
    - api.validate      # Inherits artifact metadata
    - api.compatibility # Inherits artifact metadata

# This agent automatically works with the artifacts those skills define!
```

### Multi-Agent Collaboration

Different agents can communicate through shared artifact types:

```
Agent 1 (api.designer) uses api.define
  → Produces: specs/user-api.openapi.yaml (openapi-spec)
  → Saves to standard location (convention)

Agent 2 (api.validator) uses api.validate
  → Finds: specs/user-api.openapi.yaml
  → Consumes: openapi-spec artifact
  → Validates and produces: validation-report

Both agents work with the same artifact type (defined at skill level)
No artifact metadata duplication needed!
```

### What Goes Where

**In Skills (Required):**
- `artifact_metadata` with produces/consumes
- Defines the contract

**In Agents (Optional):**
- `skills_available` list (this is how they inherit)
- `system_prompt` can reference artifact conventions for guidance
- NO duplication of artifact_metadata

---

## Meta-Skills for Artifact Management

Betty provides skills to help create and manage the artifact system itself:

### artifact.define - Define Artifact Metadata

Helps create `artifact_metadata` blocks for skills.

**Usage:**
```bash
/skill/artifact/define api.validate \
  --produces validation-report \
  --consumes openapi-spec
```

**Output:**
```yaml
artifact_metadata:
  produces:
    - type: validation-report
      schema: schemas/validation-report.json
      file_pattern: "*.validation.json"
      content_type: application/json
  consumes:
    - type: openapi-spec
      required: true
```

### agent.compose - Recommend Skills for Agents

Suggests compatible skills based on agent purpose.

**Usage:**
```bash
/agent/compose "Design and validate APIs" \
  --required-artifacts openapi-spec validation-report
```

**Output:**
```yaml
skills_available:
  - api.define       # Produces: openapi-spec
  - api.validate     # Consumes: openapi-spec, produces: validation-report
  - api.generate-models  # Consumes: openapi-spec

# Rationale:
# - api.define: Produces required openapi-spec artifacts
# - api.validate: Validates openapi-spec, produces validation-report
# - api.generate-models: Can generate code from openapi-spec
```

The agent.compose skill analyzes:
- Artifact compatibility (ensures skills can work together)
- Artifact flow (no gaps in produce/consume chain)
- Purpose matching (keywords in agent description)

### atum - Meta-Agent That Creates Agents

**Atum** is a meta-agent that creates other agents by speaking them into existence. Named after the Egyptian deity of creation, Atum transforms natural language descriptions into complete, functional agents with proper skill composition, artifact metadata, and documentation.

**Artifacts:**
- **Consumes:** `agent-description` (Markdown or JSON)
- **Produces:** `agent-definition` (agent.yaml), `agent-documentation` (README.md)

**Skills Used:**
- `agent.compose` - Recommend compatible skills
- `artifact.define` - Generate artifact metadata

**Usage:**
```bash
# Create agent from description
python3 agents/atum/atum.py examples/api_architect_description.md

# Or as a Betty command (future)
betty agent create examples/api_architect_description.md
```

**Example Agent Description:**
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
```

**What Atum Creates:**

1. **agent.yaml** - Complete agent definition with:
   - Recommended skills based on purpose
   - Artifact metadata (consumes/produces)
   - Inferred permissions from skills
   - Professional description

2. **README.md** - Comprehensive documentation with:
   - Agent purpose and use cases
   - Skills list with rationale
   - Artifact flow diagram
   - Usage examples
   - Link back to Atum

**Atum's Workflow:**
1. Parse natural language description
2. Use `agent.compose` to find compatible skills
3. Use `artifact.define` to generate artifact metadata
4. Infer permissions from selected skills
5. Generate agent.yaml and README.md
6. Validate artifact flow (no gaps)

This enables **agent-driven agent creation** - describe what you want an agent to do, and Atum creates it with the right skills and artifact contracts.

---

## Artifact Types

Betty defines standard artifact types that certified skills produce and consume:

### 1. OpenAPI Specification (`openapi-spec`)

**Description:** OpenAPI 3.0+ API specifications

**Convention:**
- File pattern: `specs/*.openapi.yaml` or `specs/*.openapi.json`
- Format: YAML or JSON
- Version: OpenAPI 3.0+

**Schema:** `schemas/openapi-spec.json`

**Produced by:**
- `api.define` - Create new OpenAPI specs from templates
- `api.designer` (agent) - Design APIs interactively

**Consumed by:**
- `api.validate` - Validate specs against guidelines
- `api.generate-models` - Generate data models from specs
- `api.compatibility` - Check breaking changes

**Example:**
```yaml
# specs/user-service.openapi.yaml
openapi: 3.0.0
info:
  title: User Service API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      # ...
```

---

### 2. Validation Report (`validation-report`)

**Description:** Structured validation results from any validation skill

**Convention:**
- File pattern: `validation/*.validation.json`
- Format: JSON
- Schema: `schemas/validation-report.json`

**Schema:** `schemas/validation-report.json`

**Produced by:**
- `api.validate` - API specification validation
- `workflow.validate` - Workflow definition validation
- `hook.validate` - Hook configuration validation

**Consumed by:**
- Any skill/agent that needs validation results
- CI/CD pipelines
- Reporting tools

**Example:**
```json
{
  "artifact": "specs/user-service.openapi.yaml",
  "artifact_type": "openapi-spec",
  "valid": true,
  "errors": [],
  "warnings": [
    {
      "rule": "zalando-must-use-problem-json",
      "severity": "warning",
      "message": "Consider using problem+json for error responses"
    }
  ],
  "guideline": "zalando",
  "guideline_version": "1.0.0",
  "validated_at": "2025-10-24T23:00:00Z"
}
```

---

### 3. Workflow Definition (`workflow-definition`)

**Description:** Betty workflow YAML definitions

**Convention:**
- File pattern: `workflows/*.workflow.yaml`
- Format: YAML
- Schema: `schemas/workflow-definition.json`

**Produced by:**
- `workflow.compose` - Create workflow definitions
- `workflow.designer` (future agent)

**Consumed by:**
- `workflow.validate` - Validate workflow structure
- `workflow.execute` (future) - Execute workflows

---

### 4. Hook Configuration (`hook-config`)

**Description:** Claude Code hook definitions

**Convention:**
- File pattern: `.claude/hooks.yaml`
- Format: YAML
- Schema: `schemas/hook-config.json`

**Produced by:**
- `hook.define` - Create hook definitions

**Consumed by:**
- Claude Code runtime
- `hook.validate` (future)

---

### 5. API Data Models (`api-models`)

**Description:** Generated data models from API specifications

**Convention:**
- File pattern: `models/*.py`, `models/*.ts`, `models/*.go`
- Format: Depends on language
- Generated from: `openapi-spec`

**Produced by:**
- `api.generate-models` - Generate Pydantic/TypeScript/Go models

**Consumed by:**
- Application code
- Testing frameworks

---

### 6. Agent Description (`agent-description`)

**Description:** Natural language description of agent purpose and requirements

**Convention:**
- File pattern: `**/agent_description.md` or `agent_description.json`
- Format: Markdown or JSON
- Sections: Name, Purpose, Inputs, Outputs, Constraints, Examples

**Schema:** `schemas/agent-description.json`

**Produced by:**
- Developers (manual creation)
- Agent design tools

**Consumed by:**
- `atum` agent - Meta-agent that creates agents from descriptions

**Example Structure (Markdown):**
```markdown
# Name: api.architect

# Purpose:
Design and validate REST APIs...

# Inputs:
- API requirements

# Outputs:
- openapi-spec
- validation-report

# Examples:
- Design a RESTful API for e-commerce
```

---

### 7. Agent Definition (`agent-definition`)

**Description:** Complete agent configuration with skills and metadata

**Convention:**
- File pattern: `agents/*/agent.yaml`
- Format: YAML
- Required fields: name, description, skills_available, permissions

**Schema:** `schemas/agent-definition.json`

**Produced by:**
- `atum` agent - Creates agents from descriptions
- Developers (manual creation)

**Consumed by:**
- Betty Framework runtime
- Agent registry and certification systems

**Example Structure:**
```yaml
name: api.architect
description: Designs and validates REST APIs
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
    - type: validation-report
```

---

### 8. Agent Documentation (`agent-documentation`)

**Description:** Human-readable agent documentation

**Convention:**
- File pattern: `agents/*/README.md`
- Format: Markdown
- Sections: Purpose, Skills, Artifact Flow, Examples, Usage

**Produced by:**
- `atum` agent - Auto-generates documentation for created agents
- Developers (manual creation)

**Consumed by:**
- Users browsing agent marketplace
- Documentation generation tools

**Example Structure:**
```markdown
# API Architect Agent

## Purpose
Designs comprehensive REST APIs...

## Skills
- api.define
- api.validate

## Artifact Flow
### Consumes
- api-requirements

### Produces
- openapi-spec
- validation-report

## Usage
```bash
/agent api.architect
```
```

---

### 9. Optimization Report (`optimization-report`)

**Description:** Performance and security optimization recommendations for APIs and workflows. Contains actionable suggestions for improving efficiency, security posture, and adherence to best practices.

**Convention:**
- File pattern: `*.optimization.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/optimization-report.json`

**Produced by:**
- `api.optimize`
- `workflow.optimize`

**Consumed by:**
- `api.implement`
- `report.generate`
- `dashboard.display`

**Related types:**
- `validation-report`
- `openapi-spec`
- `workflow-definition`

---

### 10. Compatibility Graph (`compatibility-graph`)

**Description:** Agent relationship graph showing which agents can work together based on artifact flows. Maps producers to consumers, enabling intelligent multi-agent orchestration.

**Convention:**
- File pattern: `*.compatibility.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/compatibility-graph.json`

**Produced by:**
- `meta.compatibility`

**Consumed by:**
- `meta.suggest`
- `dashboard.display`
- `workflow.orchestrator`

**Related types:**
- `agent-definition`
- `pipeline-suggestion`
- `artifact-definition`

---

### 11. Pipeline Suggestion (`pipeline-suggestion`)

**Description:** Suggested multi-agent workflow with step-by-step execution plan. Ensures artifact compatibility and provides rationale for agent selection.

**Convention:**
- File pattern: `*.pipeline.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/pipeline-suggestion.json`

**Produced by:**
- `meta.compatibility`
- `meta.suggest`

**Consumed by:**
- `workflow.orchestrator`
- `Claude (for decision making)`

**Related types:**
- `compatibility-graph`
- `workflow-definition`
- `agent-definition`

---

## Artifact Metadata Schema

Skills declare artifact metadata in `skill.yaml`:

```yaml
name: api.define
version: 0.1.0
description: Create OpenAPI specifications from templates

# Standard skill fields...
inputs: [...]
outputs: [...]

# Artifact metadata (optional but recommended)
artifact_metadata:
  produces:
    - type: openapi-spec              # Artifact type identifier
      version: "3.0"                  # Version/variant
      schema: schemas/openapi-spec.json  # JSON schema for validation
      file_pattern: "*.openapi.yaml"  # Expected file naming
      content_type: application/yaml  # MIME type
      description: OpenAPI 3.0 specification in YAML format

  consumes: []  # This skill doesn't consume artifacts (creates from scratch)
```

**For skills that consume artifacts:**

```yaml
name: api.validate
version: 0.1.0
description: Validate OpenAPI specifications

artifact_metadata:
  consumes:
    - type: openapi-spec
      version: "3.0"
      required: true
      description: OpenAPI specification to validate

  produces:
    - type: validation-report
      schema: schemas/validation-report.json
      file_pattern: "*.validation.json"
      content_type: application/json
```

---

## How Claude Uses Artifact Metadata

While Claude Code autonomously selects skills, artifact metadata helps in several ways:

### 1. **Capability Discovery**

Claude can see what artifacts a skill produces:
```
User: "Create an API specification"
Claude sees: api.define produces openapi-spec artifacts
Claude invokes: api.define skill
```

### 2. **Input Matching**

Claude can find skills that consume existing artifacts:
```
Claude produced: specs/user-api.openapi.yaml (openapi-spec)
User: "Validate this API"
Claude sees: api.validate consumes openapi-spec artifacts
Claude invokes: api.validate with the spec file
```

### 3. **Runtime Validation**

Skills can validate inputs/outputs against schemas:
```python
# In skill implementation
def validate_output(output_file, artifact_type):
    schema = load_artifact_schema(artifact_type)
    validate_json_schema(output_file, schema)
```

### 4. **Better Descriptions**

Enriched skill descriptions help Claude understand capabilities:
```
"This skill validates OpenAPI 3.0 specifications (openapi-spec artifacts)
and produces validation-report artifacts"
```

---

## Agent System Prompts

Agents reference artifact standards to guide Claude's decisions:

```yaml
# agents/api.designer/agent.yaml
system_prompt: |
  You are an API designer specializing in enterprise-grade APIs.

  **Artifacts You Work With:**
  - openapi-spec: OpenAPI 3.0 specifications in specs/*.openapi.yaml
  - validation-report: Validation results in validation/*.validation.json

  **Standard Workflow:**
  1. Use api.define to create OpenAPI specs (produces openapi-spec)
  2. Save to specs/<service-name>.openapi.yaml
  3. Use api.validate to verify (consumes openapi-spec, produces validation-report)
  4. Iterate based on validation results

  **Available Skills:**
  - api.define: Creates openapi-spec artifacts
  - api.validate: Validates openapi-spec, produces validation-report
  - api.generate-models: Generates code from openapi-spec
```

---

## Certification Requirements

For a skill to be certified in the Betty registry:

### Required:
1. ✅ **Document artifact inputs/outputs** in skill description
2. ✅ **Follow file naming conventions** for artifact types
3. ✅ **Include usage examples** showing artifact flow

### Recommended:
1. 📝 **Add `artifact_metadata`** to skill.yaml
2. 📝 **Validate inputs** against artifact schemas
3. 📝 **Produce outputs** matching declared schemas

### Optional:
1. 💡 Include integration tests showing artifact compatibility
2. 💡 Add runtime schema validation

---

## Validation

### At Certification Time

Registry validates artifact metadata when certifying skills:

```python
def validate_skill_artifacts(skill):
    """Validate artifact metadata in skill definition."""
    if 'artifact_metadata' not in skill:
        # Warn but allow (metadata is optional)
        warn("No artifact_metadata - consider adding for better interoperability")
        return True

    # Validate produces
    for artifact in skill['artifact_metadata'].get('produces', []):
        # Check schema exists
        if 'schema' in artifact:
            schema_path = artifact['schema']
            if not schema_exists(schema_path):
                return False, f"Schema not found: {schema_path}"

        # Validate type is known
        if artifact['type'] not in KNOWN_ARTIFACT_TYPES:
            warn(f"Unknown artifact type: {artifact['type']}")

    # Validate consumes
    for artifact in skill['artifact_metadata'].get('consumes', []):
        # Check if any certified skill produces this type
        producers = find_artifact_producers(artifact['type'])
        if not producers:
            warn(f"No certified producers found for: {artifact['type']}")

    return True
```

### At Runtime

Skills can validate artifacts:

```python
# In api.validate skill
def validate_spec(spec_path):
    # Check file follows convention
    if not spec_path.endswith('.openapi.yaml'):
        logger.warning("File doesn't follow *.openapi.yaml convention")

    # Validate against schema if available
    schema = load_artifact_schema('openapi-spec')
    if schema:
        try:
            validate_json_schema(spec_path, schema)
        except ValidationError as e:
            return {"valid": False, "error": str(e)}

    # Run domain-specific validation...
```

---

## Integration Testing

Test artifact compatibility between skills:

```yaml
# registry/integration-tests/api-workflow.test.yaml
name: API Design Workflow
description: Test that api.define → api.validate → api.generate-models works

agents:
  - api.designer

steps:
  - name: Create API specification
    skill: api.define
    inputs:
      service_name: test-service
      template: zalando
    expect_artifact:
      type: openapi-spec
      path_pattern: specs/test-service.openapi.yaml
      schema: schemas/openapi-spec.json

  - name: Validate specification
    skill: api.validate
    inputs:
      spec_path: specs/test-service.openapi.yaml  # From previous step
    expect_artifact:
      type: validation-report
      schema: schemas/validation-report.json
      assert:
        valid: true

  - name: Generate models
    skill: api.generate-models
    inputs:
      spec_path: specs/test-service.openapi.yaml
      language: python
    expect_artifact:
      type: api-models
      path_pattern: models/*.py
```

---

## Adding New Artifact Types

To define a new artifact type:

### 1. Create Schema

```bash
# schemas/my-artifact.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "My Artifact Type",
  "type": "object",
  "properties": {
    "version": {"type": "string"},
    "content": {"type": "object"}
  },
  "required": ["version", "content"]
}
```

### 2. Document Convention

Add to this file:
- Artifact type name and description
- File naming convention
- Schema location
- Which skills produce/consume it
- Example artifact

### 3. Update Skills

Add artifact_metadata to relevant skills:
```yaml
artifact_metadata:
  produces:
    - type: my-artifact
      schema: schemas/my-artifact.json
      file_pattern: "*.my-artifact.json"
```

### 4. Add to Registry Validation

Update `KNOWN_ARTIFACT_TYPES` in registry validation.

---

## Examples

### Example 1: API Design Flow

```
User → Claude: "Design a user management API"

Claude invokes: api.designer agent
  ↓
Agent uses: api.define skill
  Produces: specs/user-service.openapi.yaml (openapi-spec)
  ↓
Agent uses: api.validate skill
  Consumes: specs/user-service.openapi.yaml
  Produces: validation/user-service.validation.json (validation-report)
  ↓
Agent uses: api.generate-models skill
  Consumes: specs/user-service.openapi.yaml
  Produces: models/user_service.py (api-models)
  ↓
Returns to user: Complete API with validation and models
```

### Example 2: Workflow Orchestration

```
User → Claude: "Create a workflow for API validation"

Claude uses: workflow.compose skill
  Produces: workflows/api-validation.workflow.yaml (workflow-definition)
  ↓
Claude uses: workflow.validate skill
  Consumes: workflows/api-validation.workflow.yaml
  Produces: validation/api-validation.validation.json (validation-report)
  ↓
If valid → Register workflow
```

---

## Benefits

### For Skills
- ✅ Clear contracts for inputs/outputs
- ✅ Runtime validation ensures correctness
- ✅ Better discoverability by Claude

### For Agents
- ✅ System prompts guide toward compatible skills
- ✅ Autonomous yet reliable skill selection
- ✅ Predictable artifact flow

### For Users
- ✅ Certified skills work together reliably
- ✅ Predictable file locations and formats
- ✅ Integration tests prove compatibility

### For Registry
- ✅ Validate interoperability at certification
- ✅ Ensure artifact schemas exist
- ✅ Warn about orphaned artifact types

---

## Future Enhancements

1. **Artifact Versioning**: Support multiple versions of artifact types
2. **Transformation Skills**: Skills that convert between artifact types
3. **Artifact Registry**: Centralized registry of available artifacts
4. **Dependency Resolution**: Automatically find skills to produce needed artifacts
5. **Artifact Lineage**: Track which artifacts were produced from which inputs

---

## References

- **Schema Definitions**: `/schemas/`
- **Skill Examples**: `/skills/api.define/`, `/skills/api.validate/`
- **Agent Examples**: `/agents/api.designer/`
- **Integration Tests**: `/registry/integration-tests/`

---

## Quick Reference

| Artifact Type | File Pattern | Schema | Producers | Consumers |
|---------------|--------------|--------|-----------|-----------|
| openapi-spec | specs/*.openapi.yaml | schemas/openapi-spec.json | api.define | api.validate, api.generate-models |
| validation-report | validation/*.validation.json | schemas/validation-report.json | api.validate, workflow.validate | Any |
| workflow-definition | workflows/*.workflow.yaml | schemas/workflow-definition.json | workflow.compose | workflow.validate |
| hook-config | .claude/hooks.yaml | schemas/hook-config.json | hook.define | Claude Code |
| api-models | models/*.{py,ts,go} | - | api.generate-models | Application code |
| agent-description | **/agent_description.md | schemas/agent-description.json | Developers | atum agent |
| agent-definition | agents/*/agent.yaml | schemas/agent-definition.json | atum agent | Betty runtime |
| agent-documentation | agents/*/README.md | - | atum agent | Users, docs tools |
| optimization-report | *.optimization.json | schemas/optimization-report.json | api.optimize, workflow.optimize | api.implement, report.generate, dashboard.display |
| compatibility-graph | *.compatibility.json | schemas/compatibility-graph.json | meta.compatibility | meta.suggest, dashboard.display, workflow.orchestrator |
| pipeline-suggestion | *.pipeline.json | schemas/pipeline-suggestion.json | meta.compatibility, meta.suggest | workflow.orchestrator, Claude (for decision making) |
