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

### meta.agent - Meta-Agent That Creates Agents

**meta.agent** is a meta-agent that creates other agents through skill composition. It transforms natural language descriptions into complete, functional agents with proper skill composition, artifact metadata, and documentation.

**Artifacts:**
- **Consumes:** `agent-description` (Markdown or JSON)
- **Produces:** `agent-definition` (agent.yaml), `agent-documentation` (README.md)

**Skills Used:**
- `agent.compose` - Recommend compatible skills
- `artifact.define` - Generate artifact metadata

**Usage:**
```bash
# Create agent from description
python3 agents/meta.agent/meta_agent.py examples/api_architect_description.md

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

**What meta.agent Creates:**

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
   - Link back to meta.agent

**meta.agent's Workflow:**
1. Parse natural language description
2. Use `agent.compose` to find compatible skills
3. Use `artifact.define` to generate artifact metadata
4. Infer permissions from selected skills
5. Generate agent.yaml and README.md
6. Validate artifact flow (no gaps)

This enables **agent-driven agent creation** - describe what you want an agent to do, and meta.agent creates it with the right skills and artifact contracts.

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
- `meta.agent` agent - Meta-agent that creates agents from descriptions

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
- `meta.agent` agent - Creates agents from descriptions
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
- `meta.agent` agent - Auto-generates documentation for created agents
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

### 12. Suggestion Report (`suggestion-report`)

**Description:** Context-aware recommendations for what to do next after an agent completes. Includes ranked suggestions with rationale, required artifacts, and expected outcomes.

**Convention:**
- File pattern: `*.suggestions.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/suggestion-report.json`

**Produced by:**
- `meta.suggest`

**Consumed by:**
- `Claude (for decision making)`
- `dashboard.display`
- `workflow.orchestrator`

**Related types:**
- `compatibility-graph`
- `pipeline-suggestion`
- `agent-definition`

---

### 13. Skill Description (`skill-description`)

**Description:** Natural language description of a skill's requirements, inputs, outputs, and implementation details. Used by meta.skill to generate complete skill implementations.

**Convention:**
- File pattern: `**/skill_description.md`
- Format: Markdown
- Content type: text/markdown

**Schema:** `schemas/skill-description.json`

**Produced by:**
- `Developers (manual creation)`

**Consumed by:**
- `meta.skill`

**Related types:**
- `skill-definition`
- `agent-description`

---

### 14. Skill Definition (`skill-definition`)

**Description:** Complete skill configuration in YAML format. Defines skill metadata, inputs, outputs, artifact metadata, permissions, and entrypoints.

**Convention:**
- File pattern: `skills/*/skill.yaml`
- Format: YAML
- Content type: application/yaml

**Schema:** `schemas/skill-definition.json`

**Produced by:**
- `meta.skill`

**Consumed by:**
- `plugin.sync (converts to plugin.yaml commands)`
- `meta.agent (selects skills for agents)`
- `Betty runtime`

**Related types:**
- `skill-implementation`
- `agent-definition`

---

### 15. Hook Description (`hook-description`)

**Description:** Natural language description of a Claude Code hook's purpose, trigger event, and command to execute. Used by meta.hook to generate hook configurations.

**Convention:**
- File pattern: `**/hook_description.md`
- Format: Markdown
- Content type: text/markdown

**Schema:** `schemas/hook-description.json`

**Produced by:**
- `Developers (manual creation)`

**Consumed by:**
- `meta.hook`

**Related types:**
- `hook-definition`
- `agent-definition`

---

### 16. Acceptable Use Policy (`acceptable-use-policy`)

**Description:** Acceptable Use Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.acceptable-use-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 17. Acceptance Criteria (`acceptance-criteria`)

**Description:** Acceptance criteria for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.acceptance-criteria.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 18. Access Recertification Plan (`access-recertification-plan`)

**Description:** Access recertification plan for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.access-recertification-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 19. Access Review Logs (`access-review-logs`)

**Description:** Access review logs for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.access-review-logs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 20. Accessibility Audits (`accessibility-audits`)

**Description:** Accessibility audits for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.accessibility-audits.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 21. Accessibility Requirements (`accessibility-requirements`)

**Description:** Accessibility requirements for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.accessibility-requirements.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 22. Admin Guides (`admin-guides`)

**Description:** Admin guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.admin-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 23. Adr Index (`adr-index`)

**Description:** ADR index for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.adr-index.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 24. Adversary Emulation Documents (`adversary-emulation-documents`)

**Description:** Adversary emulation documents for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.adversary-emulation-documents.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 25. Ai Ethics And Bias Assessment (`ai-ethics-and-bias-assessment`)

**Description:** AI ethics and bias assessment for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.ai-ethics-and-bias-assessment.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 26. Ai Use Case Inventory (`ai-use-case-inventory`)

**Description:** AI use-case inventory for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.ai-use-case-inventory.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 27. Alert Catalogs (`alert-catalogs`)

**Description:** Alert catalogs for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.alert-catalogs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 28. Analytics Model Documentation (`analytics-model-documentation`)

**Description:** Analytics model documentation for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.analytics-model-documentation.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 29. Api Catalogs (`api-catalogs`)

**Description:** API catalogs for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.api-catalogs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 30. Api Versioning Policy (`api-versioning-policy`)

**Description:** API versioning policy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.api-versioning-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 31. App Store Metadata (`app-store-metadata`)

**Description:** App store metadata for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.app-store-metadata.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 32. Approval Evidence (`approval-evidence`)

**Description:** Approval evidence for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.approval-evidence.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 33. Architecture Approvals (`architecture-approvals`)

**Description:** Architecture approvals for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.architecture-approvals.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 34. Architecture Overview (`architecture-overview`)

**Description:** Architecture overview for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.architecture-overview.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 35. Architecture Review Board Minutes (`architecture-review-board-minutes`)

**Description:** Architecture review board minutes for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.architecture-review-board-minutes.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 36. Architecture Vision (`architecture-vision`)

**Description:** Architecture vision for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.architecture-vision.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 37. Architecture Waivers (`architecture-waivers`)

**Description:** Architecture waivers for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.architecture-waivers.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 38. Archival Plan (`archival-plan`)

**Description:** Archival plan for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.archival-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 39. Artifact Registry Policies (`artifact-registry-policies`)

**Description:** Artifact registry policies for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.artifact-registry-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 40. Artifact Store Policies (`artifact-store-policies`)

**Description:** Artifact store policies for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.artifact-store-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 41. Asyncapi Specification (`asyncapi-specification`)

**Description:** AsyncAPI specification for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.asyncapi-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 42. Attribution Files (`attribution-files`)

**Description:** Attribution files for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.attribution-files.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 43. Audit Readiness Workbook (`audit-readiness-workbook`)

**Description:** Audit readiness workbook for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.audit-readiness-workbook.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 44. Auto Update Policies (`auto-update-policies`)

**Description:** Auto-update policies for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.auto-update-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 45. Automated Quality Gates (`automated-quality-gates`)

**Description:** Automated quality gates for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.automated-quality-gates.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 46. Automated Test Scripts (`automated-test-scripts`)

**Description:** Automated test scripts for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.automated-test-scripts.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 47. Backup And Recovery Plan (`backup-and-recovery-plan`)

**Description:** Backup and recovery plan for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.backup-and-recovery-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 48. Backup Verification Logs (`backup-verification-logs`)

**Description:** Backup verification logs for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.backup-verification-logs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 49. Baseline Hardening Guides (`baseline-hardening-guides`)

**Description:** Baseline hardening guides for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.baseline-hardening-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 50. Battlecards (`battlecards`)

**Description:** Battlecards for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.battlecards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 51. Benefits Realization Plan (`benefits-realization-plan`)

**Description:** Benefits realization plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.benefits-realization-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 52. Benefits Realization Report (`benefits-realization-report`)

**Description:** Benefits realization report for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.benefits-realization-report.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 53. Bias And Fairness Reports (`bias-and-fairness-reports`)

**Description:** Bias and fairness reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.bias-and-fairness-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 54. Bounded Context Map (`bounded-context-map`)

**Description:** Bounded context map for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.bounded-context-map.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 55. Budget Forecast (`budget-forecast`)

**Description:** Budget forecast for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.budget-forecast.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 56. Bug Bounty Brief (`bug-bounty-brief`)

**Description:** Bug bounty brief for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.bug-bounty-brief.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 57. Build Reproducibility Notes (`build-reproducibility-notes`)

**Description:** Build reproducibility notes for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.build-reproducibility-notes.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 58. Build Scripts (`build-scripts`)

**Description:** Build scripts for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.build-scripts.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 59. Business Associate Agreement (`business-associate-agreement`)

**Description:** Business Associate Agreement (BAA) for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.business-associate-agreement.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 60. Business Case (`business-case`)

**Description:** Business case for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.business-case.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 61. Business Process Models (`business-process-models`)

**Description:** Business process models (BPMN, flowcharts) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.business-process-models.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 62. Business Rules Catalog (`business-rules-catalog`)

**Description:** Business rules catalog for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.business-rules-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 63. Cab Approvals (`cab-approvals`)

**Description:** CAB approvals for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.cab-approvals.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 64. Caching Strategy (`caching-strategy`)

**Description:** Caching strategy for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.caching-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 65. Caching Tiers (`caching-tiers`)

**Description:** Caching tiers for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.caching-tiers.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 66. Capability Model (`capability-model`)

**Description:** Capability model for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.capability-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 67. Capacity Models (`capacity-models`)

**Description:** Capacity models for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.capacity-models.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 68. Capacity Plan (`capacity-plan`)

**Description:** Capacity plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.capacity-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 69. Capitalization Policy (`capitalization-policy`)

**Description:** Capitalization policy for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.capitalization-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 70. Carbon Footprint Analysis (`carbon-footprint-analysis`)

**Description:** Carbon footprint analysis for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.carbon-footprint-analysis.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 71. Cdn And Waf Configs (`cdn-and-waf-configs`)

**Description:** CDN and WAF configs for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.cdn-and-waf-configs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 72. Certificate Policy (`certificate-policy`)

**Description:** Certificate policy for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.certificate-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 73. Certification Exams (`certification-exams`)

**Description:** Certification exams for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.certification-exams.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 74. Change Control Plan (`change-control-plan`)

**Description:** Change control plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.change-control-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 75. Change Log (`change-log`)

**Description:** Change log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.change-log.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 76. Changelogs (`changelogs`)

**Description:** Changelogs for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.changelogs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 77. Chaos Engineering Experiments (`chaos-engineering-experiments`)

**Description:** Chaos engineering experiments for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.chaos-engineering-experiments.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 78. Ci Cd Pipeline Definitions (`ci-cd-pipeline-definitions`)

**Description:** CI/CD pipeline definitions for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.ci-cd-pipeline-definitions.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 79. Circuit Breaker Configurations (`circuit-breaker-configurations`)

**Description:** Circuit breaker configurations for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.circuit-breaker-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 80. Class Diagrams (`class-diagrams`)

**Description:** Class diagrams for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.class-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 81. Cloud Cost Optimization Reports (`cloud-cost-optimization-reports`)

**Description:** Cloud cost optimization reports for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.cloud-cost-optimization-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 82. Cloud Landing Zone Design (`cloud-landing-zone-design`)

**Description:** Cloud landing zone design for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.cloud-landing-zone-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 83. Cmp Configurations (`cmp-configurations`)

**Description:** CMP configurations for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.cmp-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 84. Code Coverage Reports (`code-coverage-reports`)

**Description:** Code coverage reports for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.code-coverage-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 85. Code Review Records (`code-review-records`)

**Description:** Code review records for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.code-review-records.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 86. Code Signing Records (`code-signing-records`)

**Description:** Code signing records for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.code-signing-records.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 87. Coding Standards And Style Guides (`coding-standards-and-style-guides`)

**Description:** Coding standards and style guides for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.coding-standards-and-style-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 88. Commit Logs (`commit-logs`)

**Description:** Commit logs for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.commit-logs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 89. Communication Plan (`communication-plan`)

**Description:** Communication plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.communication-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 90. Competitive Analysis (`competitive-analysis`)

**Description:** Competitive analysis for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.competitive-analysis.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 91. Component Diagrams (`component-diagrams`)

**Description:** Component diagrams for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.component-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 92. Component Model (`component-model`)

**Description:** Component model for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.component-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 93. Configuration Design (`configuration-design`)

**Description:** Configuration design for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.configuration-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 94. Configuration Drift Reports (`configuration-drift-reports`)

**Description:** Configuration drift reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.configuration-drift-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 95. Consent Models (`consent-models`)

**Description:** Consent models for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.consent-models.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 96. Consent Receipts (`consent-receipts`)

**Description:** Consent receipts for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.consent-receipts.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 97. Content Strategy (`content-strategy`)

**Description:** Content strategy for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.content-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 98. Context Diagrams (`context-diagrams`)

**Description:** Context diagrams for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.context-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 99. Continuous Improvement Plan (`continuous-improvement-plan`)

**Description:** Continuous improvement plan for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.continuous-improvement-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 100. Contributing Guide (`contributing-guide`)

**Description:** CONTRIBUTING guide for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `CONTRIBUTING.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 101. Contributor License Agreements (`contributor-license-agreements`)

**Description:** Contributor License Agreements (CLAs) for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.contributor-license-agreements.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 102. Control Test Evidence Packs (`control-test-evidence-packs`)

**Description:** Control test evidence packs for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.control-test-evidence-packs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 103. Cookie Policy Inventory (`cookie-policy-inventory`)

**Description:** Cookie policy inventory for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.cookie-policy-inventory.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 104. Cookie Policy (`cookie-policy`)

**Description:** Cookie Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.cookie-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 105. Cosign Signatures (`cosign-signatures`)

**Description:** Cosign signatures for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.cosign-signatures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 106. Cost Anomaly Alerts (`cost-anomaly-alerts`)

**Description:** Cost anomaly alerts for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.cost-anomaly-alerts.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 107. Cost Tagging Policy (`cost-tagging-policy`)

**Description:** Cost tagging policy for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.cost-tagging-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 108. Crash Reporting Taxonomy (`crash-reporting-taxonomy`)

**Description:** Crash reporting taxonomy for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.crash-reporting-taxonomy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 109. Crash Triage Playbooks (`crash-triage-playbooks`)

**Description:** Crash triage playbooks for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.crash-triage-playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 110. Customer Communication Templates (`customer-communication-templates`)

**Description:** Customer communication templates for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.customer-communication-templates.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 111. Customer Data Return Procedures (`customer-data-return-procedures`)

**Description:** Customer data return procedures for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.customer-data-return-procedures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 112. Customer Onboarding Plan (`customer-onboarding-plan`)

**Description:** Customer onboarding plan for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.customer-onboarding-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 113. Cutover Checklist (`cutover-checklist`)

**Description:** Cutover checklist for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.cutover-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 114. Dag Definitions (`dag-definitions`)

**Description:** DAG definitions for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.dag-definitions.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 115. Data Contracts (`data-contracts`)

**Description:** Data contracts for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.data-contracts.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 116. Data Dictionaries (`data-dictionaries`)

**Description:** Data dictionaries for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-dictionaries.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 117. Data Export Procedures (`data-export-procedures`)

**Description:** Data export procedures for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.data-export-procedures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 118. Data Flow Diagrams (`data-flow-diagrams`)

**Description:** Data flow diagrams (DFDs) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.data-flow-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 119. Data Freshness Slas (`data-freshness-slas`)

**Description:** Data freshness SLAs for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-freshness-slas.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 120. Data Lineage Maps (`data-lineage-maps`)

**Description:** Data lineage maps for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-lineage-maps.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 121. Data Lineage Tracking (`data-lineage-tracking`)

**Description:** Data lineage tracking for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.data-lineage-tracking.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 122. Data Map (`data-map`)

**Description:** Data map for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.data-map.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 123. Data Processing Addendum (`data-processing-addendum`)

**Description:** Data Processing Addendum (DPA) for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.data-processing-addendum.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 124. Data Product Specification (`data-product-specification`)

**Description:** Data product specification for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.data-product-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 125. Data Protection Impact Assessment (`data-protection-impact-assessment`)

**Description:** Data Protection Impact Assessment (DPIA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.data-protection-impact-assessment.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 126. Data Quality Rules (`data-quality-rules`)

**Description:** Data quality rules for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-quality-rules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 127. Data Residency Plan (`data-residency-plan`)

**Description:** Data residency plan for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-residency-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 128. Data Retention Plan (`data-retention-plan`)

**Description:** Data retention plan for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.data-retention-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 129. Database Schema Ddl (`database-schema-ddl`)

**Description:** Database schema DDL for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.database-schema-ddl.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 130. Dataset Documentation (`dataset-documentation`)

**Description:** Dataset documentation for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.dataset-documentation.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 131. Ddos Posture Assessments (`ddos-posture-assessments`)

**Description:** DDoS posture assessments for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.ddos-posture-assessments.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 132. Decision Log (`decision-log`)

**Description:** Decision log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.decision-log.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 133. Decommissioning Plan (`decommissioning-plan`)

**Description:** Decommissioning plan for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.decommissioning-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 134. Defect Log (`defect-log`)

**Description:** Defect log for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.defect-log.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 135. Demo Scripts (`demo-scripts`)

**Description:** Demo scripts for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.demo-scripts.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 136. Dependency Graph (`dependency-graph`)

**Description:** Dependency graph for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.dependency-graph.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 137. Deployment Diagram (`deployment-diagram`)

**Description:** Deployment diagram for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.deployment-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 138. Deployment Plan (`deployment-plan`)

**Description:** Deployment plan (blue-green, canary, rolling) for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.deployment-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 139. Deployment Topology Diagram (`deployment-topology-diagram`)

**Description:** Deployment topology diagram for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.deployment-topology-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 140. Deprecation Policy (`deprecation-policy`)

**Description:** Deprecation policy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.deprecation-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 141. Developer Handbook (`developer-handbook`)

**Description:** Developer handbook for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.developer-handbook.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 142. Disaster Recovery Runbooks (`disaster-recovery-runbooks`)

**Description:** Disaster recovery runbooks for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.disaster-recovery-runbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 143. Discount Guardrails (`discount-guardrails`)

**Description:** Discount guardrails for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.discount-guardrails.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 144. Dns Configurations (`dns-configurations`)

**Description:** DNS configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.dns-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 145. Docker Compose Manifests (`docker-compose-manifests`)

**Description:** Docker Compose manifests for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.docker-compose-manifests.yaml`
- Format: YAML
- Content type: application/yaml

**Schema:** `schemas/docker-compose-manifests.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 146. Dockerfiles (`dockerfiles`)

**Description:** Dockerfiles for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.dockerfiles.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 147. Domain Model (`domain-model`)

**Description:** Domain model for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.domain-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 148. Dr Test Reports (`dr-test-reports`)

**Description:** DR test reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.dr-test-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 149. Drift Detection Reports (`drift-detection-reports`)

**Description:** Drift detection reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.drift-detection-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 150. Dsar Playbooks (`dsar-playbooks`)

**Description:** DSAR playbooks for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.dsar-playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 151. Eccn Classification (`eccn-classification`)

**Description:** ECCN classification for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.eccn-classification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 152. Encryption And Key Management Design (`encryption-and-key-management-design`)

**Description:** Encryption and key management design for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.encryption-and-key-management-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 153. Engagement Plan (`engagement-plan`)

**Description:** Engagement plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.engagement-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 154. Enterprise Data Model (`enterprise-data-model`)

**Description:** Enterprise data model for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.enterprise-data-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 155. Enterprise Risk Register (`enterprise-risk-register`)

**Description:** Enterprise risk register for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.enterprise-risk-register.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 156. Environment Matrix (`environment-matrix`)

**Description:** Environment matrix for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.environment-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 157. Environment Promotion Rules (`environment-promotion-rules`)

**Description:** Environment promotion rules for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.environment-promotion-rules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 158. Epic Charter (`epic-charter`)

**Description:** Epic charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.epic-charter.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 159. Er Diagrams (`er-diagrams`)

**Description:** ER diagrams for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.er-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 160. Error Budget Policy (`error-budget-policy`)

**Description:** Error budget policy for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.error-budget-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 161. Error Taxonomy (`error-taxonomy`)

**Description:** Error taxonomy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.error-taxonomy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 162. Escalation Matrix (`escalation-matrix`)

**Description:** Escalation matrix for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.escalation-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 163. Etl Elt Specifications (`etl-elt-specifications`)

**Description:** ETL/ELT specifications for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.etl-elt-specifications.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 164. Evaluation Protocols (`evaluation-protocols`)

**Description:** Evaluation protocols for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.evaluation-protocols.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 165. Event Schemas (`event-schemas`)

**Description:** Event schemas (Avro, JSON, Protobuf) for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.event-schemas.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/event-schemas.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 166. Eviction Policies (`eviction-policies`)

**Description:** Eviction policies for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.eviction-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 167. Exception Log (`exception-log`)

**Description:** Exception log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.exception-log.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 168. Exception Register (`exception-register`)

**Description:** Exception register for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.exception-register.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 169. Experiment Tracking Logs (`experiment-tracking-logs`)

**Description:** Experiment tracking logs for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.experiment-tracking-logs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 170. Explainability Reports (`explainability-reports`)

**Description:** Explainability reports (SHAP, LIME) for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.explainability-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 171. Export Control Screening (`export-control-screening`)

**Description:** Export control screening for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.export-control-screening.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 172. Faq (`faq`)

**Description:** FAQ for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.faq.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 173. Feasibility Study (`feasibility-study`)

**Description:** Feasibility study for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.feasibility-study.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 174. Feature Flag Registry (`feature-flag-registry`)

**Description:** Feature flag registry for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.feature-flag-registry.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 175. Feature Rollback Playbooks (`feature-rollback-playbooks`)

**Description:** Feature rollback playbooks for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.feature-rollback-playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 176. Feature Store Contracts (`feature-store-contracts`)

**Description:** Feature store contracts for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.feature-store-contracts.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 177. Finops Dashboards (`finops-dashboards`)

**Description:** FinOps dashboards for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.finops-dashboards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 178. Firewall Rules (`firewall-rules`)

**Description:** Firewall rules for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.firewall-rules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 179. Functional Requirements Specification (`functional-requirements-specification`)

**Description:** Functional Requirements Specification (FRS) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.functional-requirements-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 180. Genai Safety Evaluations (`genai-safety-evaluations`)

**Description:** GenAI safety evaluations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.genai-safety-evaluations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 181. Glossary And Taxonomy Index (`glossary-and-taxonomy-index`)

**Description:** Glossary and taxonomy index for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.glossary-and-taxonomy-index.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 182. Go No Go Minutes (`go-no-go-minutes`)

**Description:** Go/no-go minutes for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.go-no-go-minutes.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 183. Golden Path Guide (`golden-path-guide`)

**Description:** Golden path guide for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.golden-path-guide.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 184. Governance Charter (`governance-charter`)

**Description:** Governance charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.governance-charter.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 185. Graphql Schema (`graphql-schema`)

**Description:** GraphQL schema for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.graphql-schema.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 186. Great Expectations Suites (`great-expectations-suites`)

**Description:** Great Expectations suites for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.great-expectations-suites.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 187. Grpc Proto Files (`grpc-proto-files`)

**Description:** gRPC proto files for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.grpc-proto-files.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 188. Gtm Checklist (`gtm-checklist`)

**Description:** GTM checklist for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.gtm-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 189. Helm Charts (`helm-charts`)

**Description:** Helm charts for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*/Chart.yaml`
- Format: YAML
- Content type: application/yaml

**Schema:** `schemas/helm-charts.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 190. High Fidelity Mockups (`high-fidelity-mockups`)

**Description:** High-fidelity mockups for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.high-fidelity-mockups.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 191. Hsm Procedures (`hsm-procedures`)

**Description:** HSM procedures for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.hsm-procedures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 192. Hyperparameter Configurations (`hyperparameter-configurations`)

**Description:** Hyperparameter configurations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.hyperparameter-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 193. Iac Module Registry (`iac-module-registry`)

**Description:** IaC module registry for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.iac-module-registry.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 194. Iam Design (`iam-design`)

**Description:** IAM design for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.iam-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 195. Idempotency And Replay Protection Policy (`idempotency-and-replay-protection-policy`)

**Description:** Idempotency and replay protection policy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.idempotency-and-replay-protection-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 196. Incident Management Plan (`incident-management-plan`)

**Description:** Incident management plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.incident-management-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 197. Incident Reports (`incident-reports`)

**Description:** Incident reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.incident-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 198. Information Architecture (`information-architecture`)

**Description:** Information architecture for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.information-architecture.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 199. Initiative Charter (`initiative-charter`)

**Description:** Initiative charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.initiative-charter.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 200. Installation Guides (`installation-guides`)

**Description:** Installation guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.installation-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 201. Installer Manifests (`installer-manifests`)

**Description:** Installer manifests for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.installer-manifests.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 202. Interactive Prototypes (`interactive-prototypes`)

**Description:** Interactive prototypes for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.interactive-prototypes.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 203. Interface Control Document (`interface-control-document`)

**Description:** Interface Control Document (ICD) for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.interface-control-document.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 204. Ip Register (`ip-register`)

**Description:** IP register for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.ip-register.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 205. Iso 27001 Mapping (`iso-27001-mapping`)

**Description:** ISO 27001 mapping for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.iso-27001-mapping.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 206. Joiner Mover Leaver Workflows (`joiner-mover-leaver-workflows`)

**Description:** Joiner-Mover-Leaver workflows for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.joiner-mover-leaver-workflows.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 207. Key Ceremony Records (`key-ceremony-records`)

**Description:** Key ceremony records for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.key-ceremony-records.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 208. Kill Switch Designs (`kill-switch-designs`)

**Description:** Kill-switch designs for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.kill-switch-designs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 209. Knowledge Base Articles (`knowledge-base-articles`)

**Description:** Knowledge base articles for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.knowledge-base-articles.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 210. Kpi Framework (`kpi-framework`)

**Description:** KPI framework for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.kpi-framework.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 211. Kustomize Manifests (`kustomize-manifests`)

**Description:** Kustomize manifests for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.kustomize-manifests.yaml`
- Format: YAML
- Content type: application/yaml

**Schema:** `schemas/kustomize-manifests.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 212. Labs And Workshops (`labs-and-workshops`)

**Description:** Labs and workshops for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.labs-and-workshops.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 213. Legal Hold Procedures (`legal-hold-procedures`)

**Description:** Legal hold procedures for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.legal-hold-procedures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 214. Lessons Learned Document (`lessons-learned-document`)

**Description:** Lessons learned document for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.lessons-learned-document.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 215. Load Balancer Configurations (`load-balancer-configurations`)

**Description:** Load balancer configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.load-balancer-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 216. Load Profiles (`load-profiles`)

**Description:** Load profiles for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.load-profiles.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 217. Load Test Report (`load-test-report`)

**Description:** Load test report for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.load-test-report.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 218. Locale Files (`locale-files`)

**Description:** Locale files for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.locale-files.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 219. Localization Plan (`localization-plan`)

**Description:** Localization plan for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.localization-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 220. Logging Taxonomy (`logging-taxonomy`)

**Description:** Logging taxonomy for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.logging-taxonomy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 221. Logical Architecture Diagram (`logical-architecture-diagram`)

**Description:** Logical architecture diagram for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.logical-architecture-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 222. Logical Data Model (`logical-data-model`)

**Description:** Logical data model for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.logical-data-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 223. Market Analysis (`market-analysis`)

**Description:** Market analysis for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.market-analysis.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 224. Messaging Frameworks (`messaging-frameworks`)

**Description:** Messaging frameworks for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.messaging-frameworks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 225. Metadata Catalogs (`metadata-catalogs`)

**Description:** Metadata catalogs for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.metadata-catalogs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 226. Metric Catalog (`metric-catalog`)

**Description:** Metric catalog for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.metric-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 227. Microcopy Guides (`microcopy-guides`)

**Description:** Microcopy guides for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.microcopy-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 228. Migration Scripts (`migration-scripts`)

**Description:** Migration scripts (Liquibase/Flyway) for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.migration-scripts.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 229. Mission Statement (`mission-statement`)

**Description:** Mission statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.mission-statement.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 230. Model Cards (`model-cards`)

**Description:** Model cards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.model-cards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 231. Model Governance Policy (`model-governance-policy`)

**Description:** Model governance policy for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.model-governance-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 232. Model Registry Entries (`model-registry-entries`)

**Description:** Model registry entries for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.model-registry-entries.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 233. Model Risk Assessments (`model-risk-assessments`)

**Description:** Model risk assessments for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.model-risk-assessments.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 234. Monitoring And Observability Design (`monitoring-and-observability-design`)

**Description:** Monitoring and observability design for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.monitoring-and-observability-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 235. Monitoring Dashboards (`monitoring-dashboards`)

**Description:** Monitoring dashboards for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.monitoring-dashboards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 236. Multi Region Active Active Plan (`multi-region-active-active-plan`)

**Description:** Multi-region active-active plan for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.multi-region-active-active-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 237. Network Policies (`network-policies`)

**Description:** Network policies for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.network-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 238. Network Topology Diagram (`network-topology-diagram`)

**Description:** Network topology diagram for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.network-topology-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 239. Non Functional Requirements Matrix (`non-functional-requirements-matrix`)

**Description:** Non-Functional Requirements (NFR) matrix for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.non-functional-requirements-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 240. Notarization Records (`notarization-records`)

**Description:** Notarization records for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.notarization-records.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 241. Offboarding Checklist (`offboarding-checklist`)

**Description:** Offboarding checklist for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.offboarding-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 242. Okr Definitions (`okr-definitions`)

**Description:** OKR definitions for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.okr-definitions.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 243. On Call Handbook (`on-call-handbook`)

**Description:** On-call handbook for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.on-call-handbook.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 244. Onboarding Checklist (`onboarding-checklist`)

**Description:** Onboarding checklist for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.onboarding-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 245. Onboarding Guide (`onboarding-guide`)

**Description:** Onboarding guide for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.onboarding-guide.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 246. Open Source License Bom (`open-source-license-bom`)

**Description:** Open source license BoM for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.open-source-license-bom.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 247. Openapi Specification (`openapi-specification`)

**Description:** OpenAPI specification for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.openapi-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 248. Operational Acceptance Certificate (`operational-acceptance-certificate`)

**Description:** Operational acceptance certificate for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.operational-acceptance-certificate.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 249. Operations Manual (`operations-manual`)

**Description:** Operations manual for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.operations-manual.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 250. Ownership Charters (`ownership-charters`)

**Description:** Ownership charters for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.ownership-charters.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 251. Patterns And Anti Patterns Library (`patterns-and-anti-patterns-library`)

**Description:** Patterns and anti-patterns library for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.patterns-and-anti-patterns-library.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 252. Penetration Testing Report (`penetration-testing-report`)

**Description:** Penetration testing report for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.penetration-testing-report.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 253. Performance Strategy (`performance-strategy`)

**Description:** Performance strategy for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.performance-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 254. Performance Test Plan (`performance-test-plan`)

**Description:** Performance test plan for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.performance-test-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 255. Performance Test Results (`performance-test-results`)

**Description:** Performance test results for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.performance-test-results.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 256. Physical Architecture Diagram (`physical-architecture-diagram`)

**Description:** Physical architecture diagram for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.physical-architecture-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 257. Physical Data Model (`physical-data-model`)

**Description:** Physical data model for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.physical-data-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 258. Pipeline Architecture Diagram (`pipeline-architecture-diagram`)

**Description:** Pipeline architecture diagram for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.pipeline-architecture-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 259. Pipeline Definitions (`pipeline-definitions`)

**Description:** Pipeline definitions for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.pipeline-definitions.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 260. Platform Services Catalog (`platform-services-catalog`)

**Description:** Platform services catalog for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.platform-services-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 261. Playbooks (`playbooks`)

**Description:** Playbooks for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 262. Portfolio Roadmap (`portfolio-roadmap`)

**Description:** Portfolio roadmap for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.portfolio-roadmap.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 263. Positioning Documents (`positioning-documents`)

**Description:** Positioning documents for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.positioning-documents.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 264. Post Implementation Review (`post-implementation-review`)

**Description:** Post-implementation review for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.post-implementation-review.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 265. Post Mortem Report (`post-mortem-report`)

**Description:** Post-mortem report for Closure and Archival. Part of Project Closure documentation and deliverables.

**Convention:**
- File pattern: `*.post-mortem-report.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 266. Price Books (`price-books`)

**Description:** Price books for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.price-books.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 267. Pricing And Packaging Strategy (`pricing-and-packaging-strategy`)

**Description:** Pricing and packaging strategy for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.pricing-and-packaging-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 268. Privacy Impact Assessment (`privacy-impact-assessment`)

**Description:** Privacy Impact Assessment (PIA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.privacy-impact-assessment.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 269. Privacy Labels (`privacy-labels`)

**Description:** Privacy labels for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables.

**Convention:**
- File pattern: `*.privacy-labels.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 270. Privacy Policy (`privacy-policy`)

**Description:** Privacy Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.privacy-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 271. Product Launch Plan (`product-launch-plan`)

**Description:** Product launch plan for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.product-launch-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 272. Product Requirements Document (`product-requirements-document`)

**Description:** Product Requirements Document (PRD) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.product-requirements-document.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 273. Product Strategy (`product-strategy`)

**Description:** Product strategy for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.product-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 274. Production Hygiene Checklist (`production-hygiene-checklist`)

**Description:** Production hygiene checklist for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.production-hygiene-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 275. Program Increment Plan (`program-increment-plan`)

**Description:** Program increment plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.program-increment-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 276. Promotion Rules (`promotion-rules`)

**Description:** Promotion rules for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.promotion-rules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 277. Promotion Workflows (`promotion-workflows`)

**Description:** Promotion workflows for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.promotion-workflows.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 278. Prompt Engineering Policy (`prompt-engineering-policy`)

**Description:** Prompt engineering policy for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.prompt-engineering-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 279. Provenance Attestations (`provenance-attestations`)

**Description:** Provenance attestations (in-toto) for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.provenance-attestations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 280. Provenance Chain Documentation (`provenance-chain-documentation`)

**Description:** Provenance chain documentation (SLSA) for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.provenance-chain-documentation.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 281. Pseudo Localization Reports (`pseudo-localization-reports`)

**Description:** Pseudo-localization reports for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.pseudo-localization-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 282. Pull Request Summaries (`pull-request-summaries`)

**Description:** Pull request summaries for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.pull-request-summaries.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 283. Purple Team Reports (`purple-team-reports`)

**Description:** Purple team reports for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.purple-team-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 284. Qbr Templates (`qbr-templates`)

**Description:** QBR templates for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.qbr-templates.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 285. Quarterly Access Reviews (`quarterly-access-reviews`)

**Description:** Quarterly access reviews for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.quarterly-access-reviews.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 286. Raci Per Workstream (`raci-per-workstream`)

**Description:** RACI per workstream for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.raci-per-workstream.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 287. Raid Log (`raid-log`)

**Description:** RAID log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.raid-log.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 288. Rate Limiting Policy (`rate-limiting-policy`)

**Description:** Rate limiting policy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.rate-limiting-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 289. Rbac Abac Matrix (`rbac-abac-matrix`)

**Description:** RBAC/ABAC matrix for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.rbac-abac-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 290. Rbac Abac Policy (`rbac-abac-policy`)

**Description:** RBAC/ABAC policy for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.rbac-abac-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 291. Readme (`readme`)

**Description:** README for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `README.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 292. Records Of Processing Activities (`records-of-processing-activities`)

**Description:** Records of Processing Activities (RoPA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.records-of-processing-activities.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 293. Red Team Reports (`red-team-reports`)

**Description:** Red team reports for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.red-team-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 294. Red Teaming Reports (`red-teaming-reports`)

**Description:** Red-teaming reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.red-teaming-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 295. Reference Architectures (`reference-architectures`)

**Description:** Reference architectures for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.reference-architectures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 296. Regression Test Suite (`regression-test-suite`)

**Description:** Regression test suite for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.regression-test-suite.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 297. Regulatory Mapping (`regulatory-mapping`)

**Description:** Regulatory mapping (SOC2, ISO, NIST, HIPAA, PCI, FedRAMP) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.regulatory-mapping.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 298. Release Certification (`release-certification`)

**Description:** Release certification for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.release-certification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 299. Release Notes (`release-notes`)

**Description:** Release notes for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.release-notes.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 300. Release Plan (`release-plan`)

**Description:** Release plan for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.release-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 301. Release Risk Assessment (`release-risk-assessment`)

**Description:** Release risk assessment for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.release-risk-assessment.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 302. Remediation Tracker (`remediation-tracker`)

**Description:** Remediation tracker for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.remediation-tracker.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 303. Renewal Playbooks (`renewal-playbooks`)

**Description:** Renewal playbooks for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.renewal-playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 304. Reproducibility Checklists (`reproducibility-checklists`)

**Description:** Reproducibility checklists for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.reproducibility-checklists.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 305. Requirements Traceability Matrix (`requirements-traceability-matrix`)

**Description:** Requirements traceability matrix for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.requirements-traceability-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 306. Resource Plan (`resource-plan`)

**Description:** Resource plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.resource-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 307. Retention Schedule (`retention-schedule`)

**Description:** Retention schedule for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.retention-schedule.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 308. Reverse Etl Playbooks (`reverse-etl-playbooks`)

**Description:** Reverse ETL playbooks for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.reverse-etl-playbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 309. Risk Appetite Statement (`risk-appetite-statement`)

**Description:** Risk appetite statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.risk-appetite-statement.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 310. Roi Model (`roi-model`)

**Description:** ROI model for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.roi-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 311. Roi Tco Calculators (`roi-tco-calculators`)

**Description:** ROI/TCO calculators for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.roi-tco-calculators.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 312. Role Catalog (`role-catalog`)

**Description:** Role catalog for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables.

**Convention:**
- File pattern: `*.role-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 313. Rollback Plan (`rollback-plan`)

**Description:** Rollback plan for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.rollback-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 314. Root Cause Analyses (`root-cause-analyses`)

**Description:** Root cause analyses (RCA) for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.root-cause-analyses.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 315. Runbooks (`runbooks`)

**Description:** Runbooks for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.runbooks.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 316. Safety Filter Configurations (`safety-filter-configurations`)

**Description:** Safety filter configurations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.safety-filter-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 317. Sales Enablement Kits (`sales-enablement-kits`)

**Description:** Sales enablement kits for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.sales-enablement-kits.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 318. Sbom Policy (`sbom-policy`)

**Description:** SBOM policy for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

**Convention:**
- File pattern: `*.sbom-policy.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/sbom-policy.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 319. Sbom Verification Reports (`sbom-verification-reports`)

**Description:** SBOM verification reports for Deployment and Release. Part of Release Management documentation and deliverables.

**Convention:**
- File pattern: `*.sbom-verification-reports.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/sbom-verification-reports.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 320. Scaling Policies (`scaling-policies`)

**Description:** Scaling policies for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.scaling-policies.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 321. Scheduling Slas (`scheduling-slas`)

**Description:** Scheduling SLAs for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.scheduling-slas.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 322. Schema Evolution Policy (`schema-evolution-policy`)

**Description:** Schema evolution policy for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.schema-evolution-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 323. Secret Rotation Schedule (`secret-rotation-schedule`)

**Description:** Secret rotation schedule for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.secret-rotation-schedule.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 324. Secrets Management Policy (`secrets-management-policy`)

**Description:** Secrets management policy for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.secrets-management-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 325. Secure Coding Checklist (`secure-coding-checklist`)

**Description:** Secure coding checklist for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.secure-coding-checklist.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 326. Secure Coding Policy (`secure-coding-policy`)

**Description:** Secure coding policy for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.secure-coding-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 327. Security Architecture Diagram (`security-architecture-diagram`)

**Description:** Security architecture diagram for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.security-architecture-diagram.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 328. Security Detections Catalog (`security-detections-catalog`)

**Description:** Security detections catalog (MITRE ATT&CK) for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.security-detections-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 329. Security Policy Library (`security-policy-library`)

**Description:** Security policy library for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.security-policy-library.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 330. Security Test Results (`security-test-results`)

**Description:** Security test results (SAST, DAST, IAST) for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.security-test-results.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 331. Semantic Layer Definitions (`semantic-layer-definitions`)

**Description:** Semantic layer definitions (dbt, LookML) for Architecture. Part of Data and Information documentation and deliverables.

**Convention:**
- File pattern: `*.semantic-layer-definitions.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 332. Sequence Diagrams (`sequence-diagrams`)

**Description:** Sequence diagrams for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.sequence-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 333. Service Configuration Files (`service-configuration-files`)

**Description:** Service configuration files for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.service-configuration-files.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 334. Service Decomposition (`service-decomposition`)

**Description:** Service decomposition for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.service-decomposition.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 335. Service Dependency Graph (`service-dependency-graph`)

**Description:** Service dependency graph for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.service-dependency-graph.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 336. Service Level Objectives (`service-level-objectives`)

**Description:** Service-level objectives (SLOs) for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.service-level-objectives.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 337. Service Mesh Configurations (`service-mesh-configurations`)

**Description:** Service mesh configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.service-mesh-configurations.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 338. Shadow Canary Deployment Scorecards (`shadow-canary-deployment-scorecards`)

**Description:** Shadow/canary deployment scorecards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.shadow-canary-deployment-scorecards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 339. Showback And Chargeback Reports (`showback-and-chargeback-reports`)

**Description:** Showback and chargeback reports for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables.

**Convention:**
- File pattern: `*.showback-and-chargeback-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 340. Sig Questionnaires (`sig-questionnaires`)

**Description:** SIG questionnaires for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.sig-questionnaires.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 341. Skills Matrix (`skills-matrix`)

**Description:** Skills matrix for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.skills-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 342. Sla Slo Schedules (`sla-slo-schedules`)

**Description:** SLA/SLO schedules for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.sla-slo-schedules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 343. Soc 2 Control Implementation Matrix (`soc-2-control-implementation-matrix`)

**Description:** SOC 2 control implementation matrix for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.soc-2-control-implementation-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 344. Sod Conflict Matrices (`sod-conflict-matrices`)

**Description:** SoD conflict matrices for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.sod-conflict-matrices.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 345. Sod Matrix (`sod-matrix`)

**Description:** SoD matrix for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.sod-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 346. Software Bill Of Materials (`software-bill-of-materials`)

**Description:** Software Bill of Materials (SBOM) for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.software-bill-of-materials.json`
- Format: JSON
- Content type: application/json

**Schema:** `schemas/software-bill-of-materials.json`

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 347. Solution Briefs (`solution-briefs`)

**Description:** Solution briefs for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.solution-briefs.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 348. Source Code Repositories (`source-code-repositories`)

**Description:** Source code repositories for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.source-code-repositories.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 349. Sprint Goals (`sprint-goals`)

**Description:** Sprint goals for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.sprint-goals.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 350. Staffing Plan (`staffing-plan`)

**Description:** Staffing plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.staffing-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 351. Stakeholder Map (`stakeholder-map`)

**Description:** Stakeholder map for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.stakeholder-map.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 352. Standard Contractual Clauses (`standard-contractual-clauses`)

**Description:** Standard Contractual Clauses (SCCs) for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.standard-contractual-clauses.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 353. Standard Operating Procedures (`standard-operating-procedures`)

**Description:** Standard operating procedures (SOPs) for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.standard-operating-procedures.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 354. State Diagrams (`state-diagrams`)

**Description:** State diagrams for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.state-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 355. Static Analysis Reports (`static-analysis-reports`)

**Description:** Static analysis reports for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.static-analysis-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 356. Status Page Communication Templates (`status-page-communication-templates`)

**Description:** Status page communication templates for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.status-page-communication-templates.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 357. Steering Committee Minutes (`steering-committee-minutes`)

**Description:** Steering committee minutes for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.steering-committee-minutes.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 358. Storyboards (`storyboards`)

**Description:** Storyboards for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.storyboards.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 359. Subprocessor Notifications (`subprocessor-notifications`)

**Description:** Subprocessor notifications for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.subprocessor-notifications.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 360. Success Plan Templates (`success-plan-templates`)

**Description:** Success plan templates for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.success-plan-templates.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 361. Sustainability Reports (`sustainability-reports`)

**Description:** Sustainability reports for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables.

**Convention:**
- File pattern: `*.sustainability-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 362. Sync Contracts (`sync-contracts`)

**Description:** Sync contracts for Data Engineering and Analytics. Part of Data Platform documentation and deliverables.

**Convention:**
- File pattern: `*.sync-contracts.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 363. Synthetic Data Generation Plan (`synthetic-data-generation-plan`)

**Description:** Synthetic data generation plan for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.synthetic-data-generation-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 364. System Requirements Specification (`system-requirements-specification`)

**Description:** System Requirements Specification (SRS) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.system-requirements-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 365. Target State Evolution Map (`target-state-evolution-map`)

**Description:** Target-state evolution map for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.target-state-evolution-map.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 366. Team Topology Map (`team-topology-map`)

**Description:** Team topology map for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.team-topology-map.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 367. Technology Standards Catalog (`technology-standards-catalog`)

**Description:** Technology standards catalog for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.technology-standards-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 368. Telemetry Schema (`telemetry-schema`)

**Description:** Telemetry schema for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.telemetry-schema.txt`
- Format: Text
- Content type: text/plain

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 369. Tenancy And Isolation Model (`tenancy-and-isolation-model`)

**Description:** Tenancy and isolation model for Architecture. Part of High-Level and Platform documentation and deliverables.

**Convention:**
- File pattern: `*.tenancy-and-isolation-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 370. Terms Of Service (`terms-of-service`)

**Description:** Terms of Service for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.terms-of-service.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 371. Test Case Specifications (`test-case-specifications`)

**Description:** Test case specifications for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.test-case-specifications.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 372. Test Data Specification (`test-data-specification`)

**Description:** Test data specification for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.test-data-specification.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 373. Test Plan (`test-plan`)

**Description:** Test plan for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.test-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 374. Test Strategy (`test-strategy`)

**Description:** Test strategy for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.test-strategy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 375. Third Party Risk Assessments (`third-party-risk-assessments`)

**Description:** Third-party risk assessments for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.third-party-risk-assessments.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 376. Threat Model (`threat-model`)

**Description:** Threat model (STRIDE, attack trees) for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.threat-model.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 377. Time Allocation Worksheets (`time-allocation-worksheets`)

**Description:** Time allocation worksheets for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.time-allocation-worksheets.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 378. Toil Reduction Plan (`toil-reduction-plan`)

**Description:** Toil reduction plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.toil-reduction-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 379. Topic And Queue Catalog (`topic-and-queue-catalog`)

**Description:** Topic and queue catalog for Architecture. Part of Application and Integration documentation and deliverables.

**Convention:**
- File pattern: `*.topic-and-queue-catalog.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 380. Traceability Matrix (`traceability-matrix`)

**Description:** Traceability matrix for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.traceability-matrix.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 381. Trademark Guidance (`trademark-guidance`)

**Description:** Trademark guidance for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.trademark-guidance.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 382. Training Curriculum (`training-curriculum`)

**Description:** Training curriculum for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.training-curriculum.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 383. Training Data Cards (`training-data-cards`)

**Description:** Training data cards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables.

**Convention:**
- File pattern: `*.training-data-cards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 384. Triage Rules (`triage-rules`)

**Description:** Triage rules for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.triage-rules.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 385. Troubleshooting Trees (`troubleshooting-trees`)

**Description:** Troubleshooting trees for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.troubleshooting-trees.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 386. Trust Center Content Plan (`trust-center-content-plan`)

**Description:** Trust center content plan for Product Management and GTM. Part of Product & Market documentation and deliverables.

**Convention:**
- File pattern: `*.trust-center-content-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 387. Trust Center Evidence Summaries (`trust-center-evidence-summaries`)

**Description:** Trust center evidence summaries for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.trust-center-evidence-summaries.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 388. Uat Plan (`uat-plan`)

**Description:** UAT plan for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.uat-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 389. Uat Sign Off Document (`uat-sign-off-document`)

**Description:** UAT sign-off document for Testing. Part of Quality Assurance documentation and deliverables.

**Convention:**
- File pattern: `*.uat-sign-off-document.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 390. Upgrade Guides (`upgrade-guides`)

**Description:** Upgrade guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.upgrade-guides.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 391. Uptime Methodology (`uptime-methodology`)

**Description:** Uptime methodology for Public-Facing and Legal. Part of Legal & External documentation and deliverables.

**Convention:**
- File pattern: `*.uptime-methodology.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 392. Use Case Diagrams (`use-case-diagrams`)

**Description:** Use-case diagrams for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.use-case-diagrams.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 393. Use Case Models (`use-case-models`)

**Description:** Use-case models for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.use-case-models.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 394. User Journeys (`user-journeys`)

**Description:** User journeys for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.user-journeys.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 395. User Manuals (`user-manuals`)

**Description:** User manuals for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables.

**Convention:**
- File pattern: `*.user-manuals.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 396. User Stories (`user-stories`)

**Description:** User stories for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.user-stories.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 397. Velocity And Burndown Reports (`velocity-and-burndown-reports`)

**Description:** Velocity and burndown reports for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.velocity-and-burndown-reports.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 398. Vendor Management Pack (`vendor-management-pack`)

**Description:** Vendor management pack for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.vendor-management-pack.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 399. Vendor Scorecards (`vendor-scorecards`)

**Description:** Vendor scorecards for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables.

**Convention:**
- File pattern: `*.vendor-scorecards.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 400. Version Tags (`version-tags`)

**Description:** Version tags for Implementation. Part of Development documentation and deliverables.

**Convention:**
- File pattern: `*.version-tags.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 401. Vision Statement (`vision-statement`)

**Description:** Vision statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables.

**Convention:**
- File pattern: `*.vision-statement.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 402. Vpat Acr Results (`vpat-acr-results`)

**Description:** VPAT/ACR results for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables.

**Convention:**
- File pattern: `*.vpat-acr-results.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 403. Vulnerability Disclosure Policy (`vulnerability-disclosure-policy`)

**Description:** Vulnerability disclosure policy for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables.

**Convention:**
- File pattern: `*.vulnerability-disclosure-policy.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 404. Vulnerability Management Plan (`vulnerability-management-plan`)

**Description:** Vulnerability management plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables.

**Convention:**
- File pattern: `*.vulnerability-management-plan.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 405. Wireframes (`wireframes`)

**Description:** Wireframes for Design. Part of Design & UX documentation and deliverables.

**Convention:**
- File pattern: `*.wireframes.*`
- Format: Multiple

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

---

### 406. Zero Trust Design (`zero-trust-design`)

**Description:** Zero trust design for Architecture. Part of Security Architecture documentation and deliverables.

**Convention:**
- File pattern: `*.zero-trust-design.md`
- Format: Markdown
- Content type: text/markdown

**Produced by:**
- `TBD`

**Consumed by:**
- `TBD`

**Related types:**
- `TBD`

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
| agent-description | **/agent_description.md | schemas/agent-description.json | Developers | meta.agent agent |
| agent-definition | agents/*/agent.yaml | schemas/agent-definition.json | meta.agent agent | Betty runtime |
| agent-documentation | agents/*/README.md | - | meta.agent agent | Users, docs tools |
| optimization-report | *.optimization.json | schemas/optimization-report.json | api.optimize, workflow.optimize | api.implement, report.generate, dashboard.display |
| compatibility-graph | *.compatibility.json | schemas/compatibility-graph.json | meta.compatibility | meta.suggest, dashboard.display, workflow.orchestrator |
| pipeline-suggestion | *.pipeline.json | schemas/pipeline-suggestion.json | meta.compatibility, meta.suggest | workflow.orchestrator, Claude (for decision making) |
| suggestion-report | *.suggestions.json | schemas/suggestion-report.json | meta.suggest | Claude (for decision making), dashboard.display, workflow.orchestrator |
| skill-description | **/skill_description.md | schemas/skill-description.json | Developers (manual creation) | meta.skill |
| skill-definition | skills/*/skill.yaml | schemas/skill-definition.json | meta.skill | plugin.sync (converts to plugin.yaml commands), meta.agent (selects skills for agents), Betty runtime |
| hook-description | **/hook_description.md | schemas/hook-description.json | Developers (manual creation) | meta.hook |
| acceptable-use-policy | *.acceptable-use-policy.md | - | TBD | TBD |
| acceptance-criteria | *.acceptance-criteria.md | - | TBD | TBD |
| access-recertification-plan | *.access-recertification-plan.md | - | TBD | TBD |
| access-review-logs | *.access-review-logs.md | - | TBD | TBD |
| accessibility-audits | *.accessibility-audits.md | - | TBD | TBD |
| accessibility-requirements | *.accessibility-requirements.md | - | TBD | TBD |
| admin-guides | *.admin-guides.md | - | TBD | TBD |
| adr-index | *.adr-index.md | - | TBD | TBD |
| adversary-emulation-documents | *.adversary-emulation-documents.md | - | TBD | TBD |
| ai-ethics-and-bias-assessment | *.ai-ethics-and-bias-assessment.md | - | TBD | TBD |
| ai-use-case-inventory | *.ai-use-case-inventory.md | - | TBD | TBD |
| alert-catalogs | *.alert-catalogs.md | - | TBD | TBD |
| analytics-model-documentation | *.analytics-model-documentation.md | - | TBD | TBD |
| api-catalogs | *.api-catalogs.md | - | TBD | TBD |
| api-versioning-policy | *.api-versioning-policy.md | - | TBD | TBD |
| app-store-metadata | *.app-store-metadata.md | - | TBD | TBD |
| approval-evidence | *.approval-evidence.md | - | TBD | TBD |
| architecture-approvals | *.architecture-approvals.md | - | TBD | TBD |
| architecture-overview | *.architecture-overview.md | - | TBD | TBD |
| architecture-review-board-minutes | *.architecture-review-board-minutes.md | - | TBD | TBD |
| architecture-vision | *.architecture-vision.md | - | TBD | TBD |
| architecture-waivers | *.architecture-waivers.md | - | TBD | TBD |
| archival-plan | *.archival-plan.md | - | TBD | TBD |
| artifact-registry-policies | *.artifact-registry-policies.md | - | TBD | TBD |
| artifact-store-policies | *.artifact-store-policies.md | - | TBD | TBD |
| asyncapi-specification | *.asyncapi-specification.md | - | TBD | TBD |
| attribution-files | *.attribution-files.md | - | TBD | TBD |
| audit-readiness-workbook | *.audit-readiness-workbook.md | - | TBD | TBD |
| auto-update-policies | *.auto-update-policies.md | - | TBD | TBD |
| automated-quality-gates | *.automated-quality-gates.md | - | TBD | TBD |
| automated-test-scripts | *.automated-test-scripts.txt | - | TBD | TBD |
| backup-and-recovery-plan | *.backup-and-recovery-plan.md | - | TBD | TBD |
| backup-verification-logs | *.backup-verification-logs.md | - | TBD | TBD |
| baseline-hardening-guides | *.baseline-hardening-guides.md | - | TBD | TBD |
| battlecards | *.battlecards.md | - | TBD | TBD |
| benefits-realization-plan | *.benefits-realization-plan.md | - | TBD | TBD |
| benefits-realization-report | *.benefits-realization-report.md | - | TBD | TBD |
| bias-and-fairness-reports | *.bias-and-fairness-reports.md | - | TBD | TBD |
| bounded-context-map | *.bounded-context-map.* | - | TBD | TBD |
| budget-forecast | *.budget-forecast.md | - | TBD | TBD |
| bug-bounty-brief | *.bug-bounty-brief.md | - | TBD | TBD |
| build-reproducibility-notes | *.build-reproducibility-notes.md | - | TBD | TBD |
| build-scripts | *.build-scripts.txt | - | TBD | TBD |
| business-associate-agreement | *.business-associate-agreement.md | - | TBD | TBD |
| business-case | *.business-case.md | - | TBD | TBD |
| business-process-models | *.business-process-models.* | - | TBD | TBD |
| business-rules-catalog | *.business-rules-catalog.md | - | TBD | TBD |
| cab-approvals | *.cab-approvals.md | - | TBD | TBD |
| caching-strategy | *.caching-strategy.md | - | TBD | TBD |
| caching-tiers | *.caching-tiers.md | - | TBD | TBD |
| capability-model | *.capability-model.md | - | TBD | TBD |
| capacity-models | *.capacity-models.md | - | TBD | TBD |
| capacity-plan | *.capacity-plan.md | - | TBD | TBD |
| capitalization-policy | *.capitalization-policy.md | - | TBD | TBD |
| carbon-footprint-analysis | *.carbon-footprint-analysis.md | - | TBD | TBD |
| cdn-and-waf-configs | *.cdn-and-waf-configs.md | - | TBD | TBD |
| certificate-policy | *.certificate-policy.md | - | TBD | TBD |
| certification-exams | *.certification-exams.md | - | TBD | TBD |
| change-control-plan | *.change-control-plan.md | - | TBD | TBD |
| change-log | *.change-log.md | - | TBD | TBD |
| changelogs | *.changelogs.md | - | TBD | TBD |
| chaos-engineering-experiments | *.chaos-engineering-experiments.md | - | TBD | TBD |
| ci-cd-pipeline-definitions | *.ci-cd-pipeline-definitions.md | - | TBD | TBD |
| circuit-breaker-configurations | *.circuit-breaker-configurations.md | - | TBD | TBD |
| class-diagrams | *.class-diagrams.* | - | TBD | TBD |
| cloud-cost-optimization-reports | *.cloud-cost-optimization-reports.md | - | TBD | TBD |
| cloud-landing-zone-design | *.cloud-landing-zone-design.md | - | TBD | TBD |
| cmp-configurations | *.cmp-configurations.md | - | TBD | TBD |
| code-coverage-reports | *.code-coverage-reports.md | - | TBD | TBD |
| code-review-records | *.code-review-records.md | - | TBD | TBD |
| code-signing-records | *.code-signing-records.md | - | TBD | TBD |
| coding-standards-and-style-guides | *.coding-standards-and-style-guides.md | - | TBD | TBD |
| commit-logs | *.commit-logs.md | - | TBD | TBD |
| communication-plan | *.communication-plan.md | - | TBD | TBD |
| competitive-analysis | *.competitive-analysis.md | - | TBD | TBD |
| component-diagrams | *.component-diagrams.* | - | TBD | TBD |
| component-model | *.component-model.md | - | TBD | TBD |
| configuration-design | *.configuration-design.md | - | TBD | TBD |
| configuration-drift-reports | *.configuration-drift-reports.md | - | TBD | TBD |
| consent-models | *.consent-models.md | - | TBD | TBD |
| consent-receipts | *.consent-receipts.md | - | TBD | TBD |
| content-strategy | *.content-strategy.md | - | TBD | TBD |
| context-diagrams | *.context-diagrams.* | - | TBD | TBD |
| continuous-improvement-plan | *.continuous-improvement-plan.md | - | TBD | TBD |
| contributing-guide | CONTRIBUTING.md | - | TBD | TBD |
| contributor-license-agreements | *.contributor-license-agreements.md | - | TBD | TBD |
| control-test-evidence-packs | *.control-test-evidence-packs.md | - | TBD | TBD |
| cookie-policy-inventory | *.cookie-policy-inventory.md | - | TBD | TBD |
| cookie-policy | *.cookie-policy.md | - | TBD | TBD |
| cosign-signatures | *.cosign-signatures.md | - | TBD | TBD |
| cost-anomaly-alerts | *.cost-anomaly-alerts.md | - | TBD | TBD |
| cost-tagging-policy | *.cost-tagging-policy.md | - | TBD | TBD |
| crash-reporting-taxonomy | *.crash-reporting-taxonomy.md | - | TBD | TBD |
| crash-triage-playbooks | *.crash-triage-playbooks.md | - | TBD | TBD |
| customer-communication-templates | *.customer-communication-templates.md | - | TBD | TBD |
| customer-data-return-procedures | *.customer-data-return-procedures.md | - | TBD | TBD |
| customer-onboarding-plan | *.customer-onboarding-plan.md | - | TBD | TBD |
| cutover-checklist | *.cutover-checklist.md | - | TBD | TBD |
| dag-definitions | *.dag-definitions.md | - | TBD | TBD |
| data-contracts | *.data-contracts.md | - | TBD | TBD |
| data-dictionaries | *.data-dictionaries.md | - | TBD | TBD |
| data-export-procedures | *.data-export-procedures.md | - | TBD | TBD |
| data-flow-diagrams | *.data-flow-diagrams.* | - | TBD | TBD |
| data-freshness-slas | *.data-freshness-slas.md | - | TBD | TBD |
| data-lineage-maps | *.data-lineage-maps.* | - | TBD | TBD |
| data-lineage-tracking | *.data-lineage-tracking.md | - | TBD | TBD |
| data-map | *.data-map.* | - | TBD | TBD |
| data-processing-addendum | *.data-processing-addendum.md | - | TBD | TBD |
| data-product-specification | *.data-product-specification.md | - | TBD | TBD |
| data-protection-impact-assessment | *.data-protection-impact-assessment.md | - | TBD | TBD |
| data-quality-rules | *.data-quality-rules.md | - | TBD | TBD |
| data-residency-plan | *.data-residency-plan.md | - | TBD | TBD |
| data-retention-plan | *.data-retention-plan.md | - | TBD | TBD |
| database-schema-ddl | *.database-schema-ddl.txt | - | TBD | TBD |
| dataset-documentation | *.dataset-documentation.md | - | TBD | TBD |
| ddos-posture-assessments | *.ddos-posture-assessments.md | - | TBD | TBD |
| decision-log | *.decision-log.md | - | TBD | TBD |
| decommissioning-plan | *.decommissioning-plan.md | - | TBD | TBD |
| defect-log | *.defect-log.md | - | TBD | TBD |
| demo-scripts | *.demo-scripts.txt | - | TBD | TBD |
| dependency-graph | *.dependency-graph.* | - | TBD | TBD |
| deployment-diagram | *.deployment-diagram.* | - | TBD | TBD |
| deployment-plan | *.deployment-plan.md | - | TBD | TBD |
| deployment-topology-diagram | *.deployment-topology-diagram.* | - | TBD | TBD |
| deprecation-policy | *.deprecation-policy.md | - | TBD | TBD |
| developer-handbook | *.developer-handbook.md | - | TBD | TBD |
| disaster-recovery-runbooks | *.disaster-recovery-runbooks.md | - | TBD | TBD |
| discount-guardrails | *.discount-guardrails.md | - | TBD | TBD |
| dns-configurations | *.dns-configurations.md | - | TBD | TBD |
| docker-compose-manifests | *.docker-compose-manifests.yaml | schemas/docker-compose-manifests.json | TBD | TBD |
| dockerfiles | *.dockerfiles.txt | - | TBD | TBD |
| domain-model | *.domain-model.md | - | TBD | TBD |
| dr-test-reports | *.dr-test-reports.md | - | TBD | TBD |
| drift-detection-reports | *.drift-detection-reports.md | - | TBD | TBD |
| dsar-playbooks | *.dsar-playbooks.md | - | TBD | TBD |
| eccn-classification | *.eccn-classification.md | - | TBD | TBD |
| encryption-and-key-management-design | *.encryption-and-key-management-design.md | - | TBD | TBD |
| engagement-plan | *.engagement-plan.md | - | TBD | TBD |
| enterprise-data-model | *.enterprise-data-model.md | - | TBD | TBD |
| enterprise-risk-register | *.enterprise-risk-register.md | - | TBD | TBD |
| environment-matrix | *.environment-matrix.md | - | TBD | TBD |
| environment-promotion-rules | *.environment-promotion-rules.md | - | TBD | TBD |
| epic-charter | *.epic-charter.md | - | TBD | TBD |
| er-diagrams | *.er-diagrams.* | - | TBD | TBD |
| error-budget-policy | *.error-budget-policy.md | - | TBD | TBD |
| error-taxonomy | *.error-taxonomy.md | - | TBD | TBD |
| escalation-matrix | *.escalation-matrix.md | - | TBD | TBD |
| etl-elt-specifications | *.etl-elt-specifications.md | - | TBD | TBD |
| evaluation-protocols | *.evaluation-protocols.txt | - | TBD | TBD |
| event-schemas | *.event-schemas.json | schemas/event-schemas.json | TBD | TBD |
| eviction-policies | *.eviction-policies.md | - | TBD | TBD |
| exception-log | *.exception-log.md | - | TBD | TBD |
| exception-register | *.exception-register.md | - | TBD | TBD |
| experiment-tracking-logs | *.experiment-tracking-logs.md | - | TBD | TBD |
| explainability-reports | *.explainability-reports.md | - | TBD | TBD |
| export-control-screening | *.export-control-screening.md | - | TBD | TBD |
| faq | *.faq.md | - | TBD | TBD |
| feasibility-study | *.feasibility-study.md | - | TBD | TBD |
| feature-flag-registry | *.feature-flag-registry.md | - | TBD | TBD |
| feature-rollback-playbooks | *.feature-rollback-playbooks.md | - | TBD | TBD |
| feature-store-contracts | *.feature-store-contracts.md | - | TBD | TBD |
| finops-dashboards | *.finops-dashboards.md | - | TBD | TBD |
| firewall-rules | *.firewall-rules.md | - | TBD | TBD |
| functional-requirements-specification | *.functional-requirements-specification.md | - | TBD | TBD |
| genai-safety-evaluations | *.genai-safety-evaluations.md | - | TBD | TBD |
| glossary-and-taxonomy-index | *.glossary-and-taxonomy-index.md | - | TBD | TBD |
| go-no-go-minutes | *.go-no-go-minutes.md | - | TBD | TBD |
| golden-path-guide | *.golden-path-guide.md | - | TBD | TBD |
| governance-charter | *.governance-charter.md | - | TBD | TBD |
| graphql-schema | *.graphql-schema.* | - | TBD | TBD |
| great-expectations-suites | *.great-expectations-suites.md | - | TBD | TBD |
| grpc-proto-files | *.grpc-proto-files.txt | - | TBD | TBD |
| gtm-checklist | *.gtm-checklist.md | - | TBD | TBD |
| helm-charts | */Chart.yaml | schemas/helm-charts.json | TBD | TBD |
| high-fidelity-mockups | *.high-fidelity-mockups.* | - | TBD | TBD |
| hsm-procedures | *.hsm-procedures.md | - | TBD | TBD |
| hyperparameter-configurations | *.hyperparameter-configurations.md | - | TBD | TBD |
| iac-module-registry | *.iac-module-registry.md | - | TBD | TBD |
| iam-design | *.iam-design.md | - | TBD | TBD |
| idempotency-and-replay-protection-policy | *.idempotency-and-replay-protection-policy.md | - | TBD | TBD |
| incident-management-plan | *.incident-management-plan.md | - | TBD | TBD |
| incident-reports | *.incident-reports.md | - | TBD | TBD |
| information-architecture | *.information-architecture.md | - | TBD | TBD |
| initiative-charter | *.initiative-charter.md | - | TBD | TBD |
| installation-guides | *.installation-guides.md | - | TBD | TBD |
| installer-manifests | *.installer-manifests.md | - | TBD | TBD |
| interactive-prototypes | *.interactive-prototypes.* | - | TBD | TBD |
| interface-control-document | *.interface-control-document.md | - | TBD | TBD |
| ip-register | *.ip-register.md | - | TBD | TBD |
| iso-27001-mapping | *.iso-27001-mapping.* | - | TBD | TBD |
| joiner-mover-leaver-workflows | *.joiner-mover-leaver-workflows.md | - | TBD | TBD |
| key-ceremony-records | *.key-ceremony-records.md | - | TBD | TBD |
| kill-switch-designs | *.kill-switch-designs.md | - | TBD | TBD |
| knowledge-base-articles | *.knowledge-base-articles.md | - | TBD | TBD |
| kpi-framework | *.kpi-framework.md | - | TBD | TBD |
| kustomize-manifests | *.kustomize-manifests.yaml | schemas/kustomize-manifests.json | TBD | TBD |
| labs-and-workshops | *.labs-and-workshops.md | - | TBD | TBD |
| legal-hold-procedures | *.legal-hold-procedures.md | - | TBD | TBD |
| lessons-learned-document | *.lessons-learned-document.md | - | TBD | TBD |
| load-balancer-configurations | *.load-balancer-configurations.md | - | TBD | TBD |
| load-profiles | *.load-profiles.md | - | TBD | TBD |
| load-test-report | *.load-test-report.md | - | TBD | TBD |
| locale-files | *.locale-files.md | - | TBD | TBD |
| localization-plan | *.localization-plan.md | - | TBD | TBD |
| logging-taxonomy | *.logging-taxonomy.md | - | TBD | TBD |
| logical-architecture-diagram | *.logical-architecture-diagram.* | - | TBD | TBD |
| logical-data-model | *.logical-data-model.md | - | TBD | TBD |
| market-analysis | *.market-analysis.md | - | TBD | TBD |
| messaging-frameworks | *.messaging-frameworks.md | - | TBD | TBD |
| metadata-catalogs | *.metadata-catalogs.md | - | TBD | TBD |
| metric-catalog | *.metric-catalog.md | - | TBD | TBD |
| microcopy-guides | *.microcopy-guides.md | - | TBD | TBD |
| migration-scripts | *.migration-scripts.txt | - | TBD | TBD |
| mission-statement | *.mission-statement.md | - | TBD | TBD |
| model-cards | *.model-cards.md | - | TBD | TBD |
| model-governance-policy | *.model-governance-policy.md | - | TBD | TBD |
| model-registry-entries | *.model-registry-entries.md | - | TBD | TBD |
| model-risk-assessments | *.model-risk-assessments.md | - | TBD | TBD |
| monitoring-and-observability-design | *.monitoring-and-observability-design.md | - | TBD | TBD |
| monitoring-dashboards | *.monitoring-dashboards.md | - | TBD | TBD |
| multi-region-active-active-plan | *.multi-region-active-active-plan.md | - | TBD | TBD |
| network-policies | *.network-policies.md | - | TBD | TBD |
| network-topology-diagram | *.network-topology-diagram.* | - | TBD | TBD |
| non-functional-requirements-matrix | *.non-functional-requirements-matrix.md | - | TBD | TBD |
| notarization-records | *.notarization-records.md | - | TBD | TBD |
| offboarding-checklist | *.offboarding-checklist.md | - | TBD | TBD |
| okr-definitions | *.okr-definitions.md | - | TBD | TBD |
| on-call-handbook | *.on-call-handbook.md | - | TBD | TBD |
| onboarding-checklist | *.onboarding-checklist.md | - | TBD | TBD |
| onboarding-guide | *.onboarding-guide.md | - | TBD | TBD |
| open-source-license-bom | *.open-source-license-bom.md | - | TBD | TBD |
| openapi-specification | *.openapi-specification.md | - | TBD | TBD |
| operational-acceptance-certificate | *.operational-acceptance-certificate.md | - | TBD | TBD |
| operations-manual | *.operations-manual.md | - | TBD | TBD |
| ownership-charters | *.ownership-charters.md | - | TBD | TBD |
| patterns-and-anti-patterns-library | *.patterns-and-anti-patterns-library.md | - | TBD | TBD |
| penetration-testing-report | *.penetration-testing-report.md | - | TBD | TBD |
| performance-strategy | *.performance-strategy.md | - | TBD | TBD |
| performance-test-plan | *.performance-test-plan.md | - | TBD | TBD |
| performance-test-results | *.performance-test-results.md | - | TBD | TBD |
| physical-architecture-diagram | *.physical-architecture-diagram.* | - | TBD | TBD |
| physical-data-model | *.physical-data-model.md | - | TBD | TBD |
| pipeline-architecture-diagram | *.pipeline-architecture-diagram.* | - | TBD | TBD |
| pipeline-definitions | *.pipeline-definitions.md | - | TBD | TBD |
| platform-services-catalog | *.platform-services-catalog.md | - | TBD | TBD |
| playbooks | *.playbooks.md | - | TBD | TBD |
| portfolio-roadmap | *.portfolio-roadmap.* | - | TBD | TBD |
| positioning-documents | *.positioning-documents.md | - | TBD | TBD |
| post-implementation-review | *.post-implementation-review.md | - | TBD | TBD |
| post-mortem-report | *.post-mortem-report.md | - | TBD | TBD |
| price-books | *.price-books.md | - | TBD | TBD |
| pricing-and-packaging-strategy | *.pricing-and-packaging-strategy.md | - | TBD | TBD |
| privacy-impact-assessment | *.privacy-impact-assessment.md | - | TBD | TBD |
| privacy-labels | *.privacy-labels.md | - | TBD | TBD |
| privacy-policy | *.privacy-policy.md | - | TBD | TBD |
| product-launch-plan | *.product-launch-plan.md | - | TBD | TBD |
| product-requirements-document | *.product-requirements-document.md | - | TBD | TBD |
| product-strategy | *.product-strategy.md | - | TBD | TBD |
| production-hygiene-checklist | *.production-hygiene-checklist.md | - | TBD | TBD |
| program-increment-plan | *.program-increment-plan.md | - | TBD | TBD |
| promotion-rules | *.promotion-rules.md | - | TBD | TBD |
| promotion-workflows | *.promotion-workflows.md | - | TBD | TBD |
| prompt-engineering-policy | *.prompt-engineering-policy.md | - | TBD | TBD |
| provenance-attestations | *.provenance-attestations.md | - | TBD | TBD |
| provenance-chain-documentation | *.provenance-chain-documentation.md | - | TBD | TBD |
| pseudo-localization-reports | *.pseudo-localization-reports.md | - | TBD | TBD |
| pull-request-summaries | *.pull-request-summaries.md | - | TBD | TBD |
| purple-team-reports | *.purple-team-reports.md | - | TBD | TBD |
| qbr-templates | *.qbr-templates.md | - | TBD | TBD |
| quarterly-access-reviews | *.quarterly-access-reviews.md | - | TBD | TBD |
| raci-per-workstream | *.raci-per-workstream.md | - | TBD | TBD |
| raid-log | *.raid-log.md | - | TBD | TBD |
| rate-limiting-policy | *.rate-limiting-policy.md | - | TBD | TBD |
| rbac-abac-matrix | *.rbac-abac-matrix.md | - | TBD | TBD |
| rbac-abac-policy | *.rbac-abac-policy.md | - | TBD | TBD |
| readme | README.md | - | TBD | TBD |
| records-of-processing-activities | *.records-of-processing-activities.md | - | TBD | TBD |
| red-team-reports | *.red-team-reports.md | - | TBD | TBD |
| red-teaming-reports | *.red-teaming-reports.md | - | TBD | TBD |
| reference-architectures | *.reference-architectures.md | - | TBD | TBD |
| regression-test-suite | *.regression-test-suite.md | - | TBD | TBD |
| regulatory-mapping | *.regulatory-mapping.* | - | TBD | TBD |
| release-certification | *.release-certification.md | - | TBD | TBD |
| release-notes | *.release-notes.md | - | TBD | TBD |
| release-plan | *.release-plan.md | - | TBD | TBD |
| release-risk-assessment | *.release-risk-assessment.md | - | TBD | TBD |
| remediation-tracker | *.remediation-tracker.md | - | TBD | TBD |
| renewal-playbooks | *.renewal-playbooks.md | - | TBD | TBD |
| reproducibility-checklists | *.reproducibility-checklists.md | - | TBD | TBD |
| requirements-traceability-matrix | *.requirements-traceability-matrix.md | - | TBD | TBD |
| resource-plan | *.resource-plan.md | - | TBD | TBD |
| retention-schedule | *.retention-schedule.md | - | TBD | TBD |
| reverse-etl-playbooks | *.reverse-etl-playbooks.md | - | TBD | TBD |
| risk-appetite-statement | *.risk-appetite-statement.md | - | TBD | TBD |
| roi-model | *.roi-model.md | - | TBD | TBD |
| roi-tco-calculators | *.roi-tco-calculators.md | - | TBD | TBD |
| role-catalog | *.role-catalog.md | - | TBD | TBD |
| rollback-plan | *.rollback-plan.md | - | TBD | TBD |
| root-cause-analyses | *.root-cause-analyses.md | - | TBD | TBD |
| runbooks | *.runbooks.md | - | TBD | TBD |
| safety-filter-configurations | *.safety-filter-configurations.md | - | TBD | TBD |
| sales-enablement-kits | *.sales-enablement-kits.md | - | TBD | TBD |
| sbom-policy | *.sbom-policy.json | schemas/sbom-policy.json | TBD | TBD |
| sbom-verification-reports | *.sbom-verification-reports.json | schemas/sbom-verification-reports.json | TBD | TBD |
| scaling-policies | *.scaling-policies.md | - | TBD | TBD |
| scheduling-slas | *.scheduling-slas.md | - | TBD | TBD |
| schema-evolution-policy | *.schema-evolution-policy.md | - | TBD | TBD |
| secret-rotation-schedule | *.secret-rotation-schedule.md | - | TBD | TBD |
| secrets-management-policy | *.secrets-management-policy.md | - | TBD | TBD |
| secure-coding-checklist | *.secure-coding-checklist.md | - | TBD | TBD |
| secure-coding-policy | *.secure-coding-policy.md | - | TBD | TBD |
| security-architecture-diagram | *.security-architecture-diagram.* | - | TBD | TBD |
| security-detections-catalog | *.security-detections-catalog.md | - | TBD | TBD |
| security-policy-library | *.security-policy-library.md | - | TBD | TBD |
| security-test-results | *.security-test-results.md | - | TBD | TBD |
| semantic-layer-definitions | *.semantic-layer-definitions.md | - | TBD | TBD |
| sequence-diagrams | *.sequence-diagrams.* | - | TBD | TBD |
| service-configuration-files | *.service-configuration-files.md | - | TBD | TBD |
| service-decomposition | *.service-decomposition.md | - | TBD | TBD |
| service-dependency-graph | *.service-dependency-graph.* | - | TBD | TBD |
| service-level-objectives | *.service-level-objectives.md | - | TBD | TBD |
| service-mesh-configurations | *.service-mesh-configurations.md | - | TBD | TBD |
| shadow-canary-deployment-scorecards | *.shadow-canary-deployment-scorecards.md | - | TBD | TBD |
| showback-and-chargeback-reports | *.showback-and-chargeback-reports.md | - | TBD | TBD |
| sig-questionnaires | *.sig-questionnaires.md | - | TBD | TBD |
| skills-matrix | *.skills-matrix.md | - | TBD | TBD |
| sla-slo-schedules | *.sla-slo-schedules.md | - | TBD | TBD |
| soc-2-control-implementation-matrix | *.soc-2-control-implementation-matrix.md | - | TBD | TBD |
| sod-conflict-matrices | *.sod-conflict-matrices.md | - | TBD | TBD |
| sod-matrix | *.sod-matrix.md | - | TBD | TBD |
| software-bill-of-materials | *.software-bill-of-materials.json | schemas/software-bill-of-materials.json | TBD | TBD |
| solution-briefs | *.solution-briefs.md | - | TBD | TBD |
| source-code-repositories | *.source-code-repositories.md | - | TBD | TBD |
| sprint-goals | *.sprint-goals.md | - | TBD | TBD |
| staffing-plan | *.staffing-plan.md | - | TBD | TBD |
| stakeholder-map | *.stakeholder-map.* | - | TBD | TBD |
| standard-contractual-clauses | *.standard-contractual-clauses.md | - | TBD | TBD |
| standard-operating-procedures | *.standard-operating-procedures.md | - | TBD | TBD |
| state-diagrams | *.state-diagrams.* | - | TBD | TBD |
| static-analysis-reports | *.static-analysis-reports.md | - | TBD | TBD |
| status-page-communication-templates | *.status-page-communication-templates.md | - | TBD | TBD |
| steering-committee-minutes | *.steering-committee-minutes.md | - | TBD | TBD |
| storyboards | *.storyboards.* | - | TBD | TBD |
| subprocessor-notifications | *.subprocessor-notifications.md | - | TBD | TBD |
| success-plan-templates | *.success-plan-templates.md | - | TBD | TBD |
| sustainability-reports | *.sustainability-reports.md | - | TBD | TBD |
| sync-contracts | *.sync-contracts.md | - | TBD | TBD |
| synthetic-data-generation-plan | *.synthetic-data-generation-plan.md | - | TBD | TBD |
| system-requirements-specification | *.system-requirements-specification.md | - | TBD | TBD |
| target-state-evolution-map | *.target-state-evolution-map.* | - | TBD | TBD |
| team-topology-map | *.team-topology-map.* | - | TBD | TBD |
| technology-standards-catalog | *.technology-standards-catalog.md | - | TBD | TBD |
| telemetry-schema | *.telemetry-schema.txt | - | TBD | TBD |
| tenancy-and-isolation-model | *.tenancy-and-isolation-model.md | - | TBD | TBD |
| terms-of-service | *.terms-of-service.md | - | TBD | TBD |
| test-case-specifications | *.test-case-specifications.md | - | TBD | TBD |
| test-data-specification | *.test-data-specification.md | - | TBD | TBD |
| test-plan | *.test-plan.md | - | TBD | TBD |
| test-strategy | *.test-strategy.md | - | TBD | TBD |
| third-party-risk-assessments | *.third-party-risk-assessments.md | - | TBD | TBD |
| threat-model | *.threat-model.md | - | TBD | TBD |
| time-allocation-worksheets | *.time-allocation-worksheets.md | - | TBD | TBD |
| toil-reduction-plan | *.toil-reduction-plan.md | - | TBD | TBD |
| topic-and-queue-catalog | *.topic-and-queue-catalog.md | - | TBD | TBD |
| traceability-matrix | *.traceability-matrix.md | - | TBD | TBD |
| trademark-guidance | *.trademark-guidance.md | - | TBD | TBD |
| training-curriculum | *.training-curriculum.md | - | TBD | TBD |
| training-data-cards | *.training-data-cards.md | - | TBD | TBD |
| triage-rules | *.triage-rules.md | - | TBD | TBD |
| troubleshooting-trees | *.troubleshooting-trees.md | - | TBD | TBD |
| trust-center-content-plan | *.trust-center-content-plan.md | - | TBD | TBD |
| trust-center-evidence-summaries | *.trust-center-evidence-summaries.md | - | TBD | TBD |
| uat-plan | *.uat-plan.md | - | TBD | TBD |
| uat-sign-off-document | *.uat-sign-off-document.md | - | TBD | TBD |
| upgrade-guides | *.upgrade-guides.md | - | TBD | TBD |
| uptime-methodology | *.uptime-methodology.md | - | TBD | TBD |
| use-case-diagrams | *.use-case-diagrams.* | - | TBD | TBD |
| use-case-models | *.use-case-models.md | - | TBD | TBD |
| user-journeys | *.user-journeys.md | - | TBD | TBD |
| user-manuals | *.user-manuals.md | - | TBD | TBD |
| user-stories | *.user-stories.md | - | TBD | TBD |
| velocity-and-burndown-reports | *.velocity-and-burndown-reports.md | - | TBD | TBD |
| vendor-management-pack | *.vendor-management-pack.md | - | TBD | TBD |
| vendor-scorecards | *.vendor-scorecards.md | - | TBD | TBD |
| version-tags | *.version-tags.md | - | TBD | TBD |
| vision-statement | *.vision-statement.md | - | TBD | TBD |
| vpat-acr-results | *.vpat-acr-results.md | - | TBD | TBD |
| vulnerability-disclosure-policy | *.vulnerability-disclosure-policy.md | - | TBD | TBD |
| vulnerability-management-plan | *.vulnerability-management-plan.md | - | TBD | TBD |
| wireframes | *.wireframes.* | - | TBD | TBD |
| zero-trust-design | *.zero-trust-design.md | - | TBD | TBD |
