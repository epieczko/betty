# Artifact-to-Skill Mapping

**Version**: 1.0.0
**Last Updated**: 2025-11-02
**Purpose**: Document which skills produce/consume which artifacts for autonomous agent composition

---

## Overview

This document maps the relationship between **skills** and **artifacts** in Betty Framework. This mapping enables:

1. **Autonomous Agent Composition**: Agents discover compatible skills based on artifact flow
2. **Workflow Validation**: Ensure skill chains have compatible inputs/outputs
3. **Ecosystem Growth**: New skills can be discovered based on artifact types they handle

---

## Verified Mappings

### threat.model.generate

**Status**: ✅ Fully Verified
**Created**: 2025-11-02
**Verification**: All artifact types match registry

#### Produces

| Artifact Type | File Pattern | Content Type | Schema |
|---------------|--------------|--------------|--------|
| `threat-model` | `*.threat-model.yaml` | `application/yaml` | `schemas/artifacts/threat-model-schema.json` |

#### Consumes (Optional)

| Artifact Type | File Pattern | Content Type | Purpose |
|---------------|--------------|--------------|---------|
| `architecture-overview` | `*.architecture-overview.md` | `text/markdown` | Enriches threat model with system context |
| `data-flow-diagrams` | `*.data-flow-diagrams.*` | `` | Identifies threat vectors in data flows |
| `logical-data-model` | `*.logical-data-model.*` | `` | Identifies sensitive data to protect |

#### Integration with Agents

- **Primary Agent**: `security.architect`
- **Workflow**: Used as first step in security assessment workflows
- **Downstream Skills**: Output threat-model consumed by `compliance.matrix.generate` and `security.gap.analyze`

---

## Universal Skills (Work with All Artifacts)

These skills work with **any of the 409 registered artifact types**:

### artifact.create

**Produces**: Any registered artifact type (dynamic based on input)
**Consumes**: User context/requirements
**Pattern**: Loads template from `templates/{category}/{artifact-type}.{ext}`, uses AI to populate

### artifact.validate

**Produces**: `validation-report`
**Consumes**: Any artifact type
**Pattern**: Validates against schema (if exists) and quality criteria

### artifact.review

**Produces**: `review-report`
**Consumes**: Any artifact type
**Pattern**: AI-powered quality review against best practices

---

## Domain-Specific Skills

### API Skills

| Skill | Produces | Consumes |
|-------|----------|----------|
| `api.define` | `openapi-spec`, `asyncapi-spec` | User requirements |
| `api.validate` | `validation-report` | `openapi-spec`, `asyncapi-spec` |
| `api.generatemodels` | Type-safe models (TypeScript, Python, etc.) | `openapi-spec`, `asyncapi-spec` |
| `api.compatibility` | `api-compatibility-report` | Old spec, New spec |

### Registry Skills

| Skill | Produces | Consumes |
|-------|----------|----------|
| `registry.update` | Updated registry | Skill/Agent manifest |
| `registry.diff` | `diff-report` | Current manifest, Registry entry |
| `registry.query` | Query results | Search criteria |

---

## Planned P1 Specialized Skills

These skills are planned but not yet implemented:

### compliance.matrix.generate

**Produces**: `compliance-matrix`, compliance reports for SOC2/ISO27001/GDPR/HIPAA/PCI-DSS
**Consumes**: `threat-model`, existing controls
**Status**: Pending skill description

### requirements.trace.generate

**Produces**: `requirements-traceability-matrix`
**Consumes**: `product-requirements-document`, design docs, test plans
**Status**: Pending skill description

### data.lineage.generate

**Produces**: `data-lineage-diagram`
**Consumes**: Code, configs, `data-flow-diagrams`
**Status**: Pending skill description

### security.gap.analyze

**Produces**: `security-gap-report`
**Consumes**: `threat-model`, existing controls
**Status**: Pending skill description

### compliance.gap.analyze

**Produces**: `compliance-gap-report`
**Consumes**: `compliance-matrix`, current controls
**Status**: Pending skill description

---

## Artifact Flow Examples

### Security Assessment Workflow

```
User Request
    ↓
security.architect agent
    ↓
threat.model.generate skill
    ↓ produces: threat-model
compliance.matrix.generate skill (future)
    ↓ produces: compliance-matrix
security.gap.analyze skill (future)
    ↓ produces: security-gap-report
artifact.review skill
    ↓ produces: review-report
Complete Security Assessment Package
```

### API Development Workflow

```
User Request
    ↓
api.designer agent
    ↓
api.define skill
    ↓ produces: openapi-spec
api.validate skill
    ↓ consumes: openapi-spec, produces: validation-report
api.generatemodels skill
    ↓ consumes: openapi-spec, produces: TypeScript/Python models
Complete API Package
```

---

## Verification Process

For each skill, verify artifact mapping:

```bash
# 1. Check produces artifacts exist in registry
jq '.artifact_types[] | select(.name == "threat-model")' registry/artifact_types.json

# 2. Verify file_pattern matches
# Skill:    *.threat-model.yaml
# Registry: *.threat-model.yaml ✅

# 3. Verify content_type matches
# Skill:    application/yaml
# Registry: application/yaml ✅

# 4. Verify schema reference (if exists)
# Skill:    schemas/artifacts/threat-model-schema.json
# Registry: schemas/artifacts/threat-model-schema.json ✅
# File:     ls schemas/artifacts/threat-model-schema.json ✅
```

---

## Adding New Artifact-Skill Mappings

When creating a new specialized skill:

1. **Check registry for artifact type**:
   ```bash
   jq '.artifact_types[] | select(.name == "{artifact-type}")' registry/artifact_types.json
   ```

2. **If artifact doesn't exist, choose**:
   - Option A: Use similar existing artifact type
   - Option B: Create new artifact type (update registry + create schema)

3. **Match exactly**:
   - `file_pattern` must match registry
   - `content_type` must match registry
   - `schema` must reference actual schema file (if exists)

4. **Run verification script**:
   ```bash
   # See SPECIALIZED_SKILL_CREATION_PATTERN.md Step 3.5
   ```

5. **Update this document** with the new mapping

---

## Common Pitfalls

### ❌ Singular vs Plural

```yaml
# WRONG
consumes:
  - type: data-flow-diagram  # Doesn't exist!

# CORRECT
consumes:
  - type: data-flow-diagrams  # Exists in registry
```

### ❌ Generic vs Specific Types

```yaml
# WRONG
consumes:
  - type: data-model  # Too generic, doesn't exist!

# CORRECT
consumes:
  - type: logical-data-model  # Specific registered type
```

### ❌ Format Mismatch

```yaml
# Registry says YAML
produces:
  - type: threat-model
    file_pattern: "*.threat-model.md"  # WRONG: Should be .yaml
    content_type: "text/markdown"      # WRONG: Should be application/yaml
```

---

## Future Enhancements

### Automated Discovery

```python
# Planned: artifact.discover skill
def find_skills_for_artifact(artifact_type: str) -> List[str]:
    """Find all skills that can produce this artifact type."""
    # Query skills registry for artifact_metadata.produces

def find_consumers_for_artifact(artifact_type: str) -> List[str]:
    """Find all skills that consume this artifact type."""
    # Query skills registry for artifact_metadata.consumes
```

### Artifact Flow Validation

```python
# Planned: workflow.validate enhancement
def validate_artifact_flow(workflow: Dict) -> bool:
    """Validate that artifact flow is complete (no missing links)."""
    # Check each skill's outputs feed into next skill's inputs
```

### Agent Auto-Composition

```python
# Planned: agent.compose enhancement
def compose_agent_for_artifacts(required_artifacts: List[str]) -> Dict:
    """Auto-compose agent from skills based on artifact requirements."""
    # Build skill chain to produce all required artifacts
```

---

## Maintenance

This document should be updated whenever:

- ✅ New specialized skill is created
- ✅ Artifact type is added/modified in registry
- ✅ Skill artifact_metadata is changed
- ✅ New artifact flow pattern is established

**Last Verified**: 2025-11-02
**Next Review**: When P1 skills are created

---

## See Also

- [SPECIALIZED_SKILL_CREATION_PATTERN.md](SPECIALIZED_SKILL_CREATION_PATTERN.md) - How to create skills
- [ARTIFACT_STANDARDS.md](ARTIFACT_STANDARDS.md) - Artifact type definitions
- [ARTIFACT_PRODUCER_CONSUMER_MAP.md](ARTIFACT_PRODUCER_CONSUMER_MAP.md) - High-level mapping
