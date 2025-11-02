# Framework Improvements Needed

**Date**: 2025-11-02
**Context**: Issues discovered during threat.model.generate skill creation
**Priority**: High - Blocks proper skill registration workflow

---

## Issue 1: registry.update - Critical Pydantic Validation Mismatch ⚠️

### The Problem

**SkillManifest Pydantic Model** (`betty/models.py`):
```python
class SkillManifest(BaseModel):
    name: str
    version: str
    description: str
    inputs: List[str]        # ❌ Expects list of strings
    outputs: List[str]       # ❌ Expects list of strings
    status: str
```

**Actual Registry Format** (`registry/skills.json`):
```json
{
  "name": "agent.compose",
  "inputs": [
    {
      "name": "agent_purpose",
      "type": "string",
      "required": true,
      "description": "Description of what the agent should do"
    }
  ],
  "outputs": [
    {
      "name": "recommended_skills",
      "type": "array",
      "description": "List of recommended skill names"
    }
  ]
}
```

**Impact:**
- ❌ Cannot register skills with detailed input/output specs through registry.update
- ❌ Must bypass validation and manually add to registry
- ❌ Inconsistent with actual registry data format
- ❌ Makes meta.skill agent unable to properly register skills

### Error Message

```
Schema validation error at 'inputs.0': Input should be a valid string (type: string_type)
Schema validation error at 'outputs.0': Input should be a valid string (type: string_type)
```

### Current Workaround

Manual registration bypassing validation:
```python
import json, yaml
with open('skills/threat.model.generate/skill.yaml') as f:
    skill = yaml.safe_load(f)
with open('registry/skills.json') as f:
    registry = json.load(f)
registry['skills'].append(skill)
with open('registry/skills.json', 'w') as f:
    json.dump(registry, f, indent=2)
```

### Root Cause

The Pydantic model was designed for a simpler format but the framework evolved to use rich input/output specifications. The validator wasn't updated to match.

---

## Issue 2: meta.skill Agent - Gaps in Artifact Validation 🔍

### What meta.skill SHOULD Do

From `agents/meta.skill/agent.yaml`:

```yaml
skills_available:
  - skill.create      # Create directory structure
  - skill.define      # Validate skill manifest
  - artifact.define   # Validate artifact types ← KEY SKILL

system_prompt: |
  6. **Register Skill** - Update registry
     - Add to registry/skills.json
     - Include all metadata
     - Validate registration

  **Artifact Metadata:**
  - Always define what the skill produces/consumes
  - Use registered artifact types from meta.artifact
  - Include schemas when applicable
```

### Gaps Identified

#### Gap 1: No Explicit Workflow for artifact.define

The system prompt says "Use registered artifact types" but doesn't specify:
- ❌ WHEN to call artifact.define
- ❌ HOW to validate artifact types exist in registry
- ❌ WHAT to do if artifact type doesn't exist

**What it should say:**
```yaml
system_prompt: |
  2. **Validate Artifact Types** - Before generating skill.yaml
     - Extract all artifact types from skill description
     - For each type in produces/consumes:
       a. Call artifact.define to verify type exists in registry
       b. Check file_pattern matches registry
       c. Verify content_type matches registry
       d. Confirm schema reference is valid
     - If type doesn't exist: ERROR with suggestion to use similar type
     - If pattern/type mismatch: ERROR with correct values from registry
```

#### Gap 2: Dependency on Broken registry.update

If meta.skill calls registry.update (step 6), it will hit the Pydantic validation error!

**Current flow:**
```
meta.skill → skill.create → skill.define → registry.update
                                                ↓
                                         ❌ Pydantic validation fails!
```

#### Gap 3: No Error Recovery Guidance

System prompt doesn't say what to do when:
- Artifact type doesn't exist
- Registry validation fails
- Schema file missing
- Duplicate skill name

#### Gap 4: Untested Workflow

We never actually RAN meta.skill because:
```bash
python3 skills/agent.run/agent_run.py agents/meta.skill/agent.yaml ...
# Error: ModuleNotFoundError: No module named 'betty'
```

**Question:** Does meta.skill even work end-to-end?

---

## Recommended Fixes

### Fix 1: Update SkillManifest Pydantic Model

**File**: `betty/models.py`

**Current:**
```python
class SkillManifest(BaseModel):
    inputs: List[str] = Field(..., description="List of required inputs")
    outputs: List[str] = Field(..., description="List of outputs produced")
```

**Fixed:**
```python
from typing import Union

class SkillInput(BaseModel):
    """Schema for skill input parameter."""
    name: str = Field(..., description="Parameter name")
    type: str = Field(..., description="Parameter type (string, array, object, etc.)")
    required: bool = Field(default=False, description="Whether parameter is required")
    description: str = Field(..., description="Parameter description")
    default: Optional[Any] = Field(None, description="Default value if not required")

    model_config = {"extra": "allow"}


class SkillOutput(BaseModel):
    """Schema for skill output."""
    name: str = Field(..., description="Output name")
    type: str = Field(..., description="Output type")
    description: str = Field(..., description="Output description")

    model_config = {"extra": "allow"}


class SkillManifest(BaseModel):
    name: str = Field(..., description="Skill name in namespace.action format")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    description: str = Field(..., description="Brief description of the skill")

    # Support both simple strings (legacy) and detailed objects (current)
    inputs: Union[List[str], List[SkillInput]] = Field(
        ...,
        description="List of input parameters (simple names or detailed specs)"
    )
    outputs: Union[List[str], List[SkillOutput]] = Field(
        ...,
        description="List of outputs (simple names or detailed specs)"
    )

    status: str = Field(default="draft", description="Skill status")

    # ... rest of fields
```

**Benefits:**
- ✅ Supports both legacy simple format and new detailed format
- ✅ Matches actual registry data
- ✅ Enables proper validation without breaking existing skills
- ✅ Unblocks registry.update for new skills

---

### Fix 2: Enhance meta.skill System Prompt

**File**: `agents/meta.skill/agent.yaml`

Add explicit artifact validation workflow:

```yaml
system_prompt: |
  ## Your Workflow

  1. **Parse Description** - Understand skill requirements
     - Extract name, purpose, inputs, outputs
     - Identify artifact types in produces/consumes
     - Understand implementation requirements

  2. **Validate Artifact Types** - CRITICAL STEP
     - For each artifact type mentioned in description:
       a. Call artifact.define to check if type exists in registry
       b. Get file_pattern, content_type, schema from registry
       c. Verify schema file exists if referenced
     - If artifact type doesn't exist:
       → Search registry for similar types
       → Suggest: "Did you mean 'data-flow-diagrams' (plural)?"
       → ERROR: Cannot proceed with unregistered artifact type
     - Record validated artifact metadata for use in skill.yaml

  3. **Generate skill.yaml** - Use VALIDATED artifact metadata
     - artifact_metadata.produces: Use exact file_pattern from registry
     - artifact_metadata.consumes: Use exact content_type from registry
     - Ensure artifact types match what artifact.define confirmed

  4. **Generate Implementation** - Create Python stub
     [existing content]

  5. **Generate Tests** - Create test template
     [existing content]

  6. **Generate Documentation** - Create SKILL.md
     [existing content]

  7. **Register Skill** - Update registry
     - Call registry.update with manifest path
     - If validation fails: Report specific errors
     - Verify skill appears in registry with artifact_metadata
     - Confirm skill is discoverable via artifact types

  ## Error Handling

  - Artifact type not found: Suggest similar types, halt creation
  - File pattern mismatch: Use registry value, warn user
  - Schema missing: Warn but continue (schema optional)
  - Registry update fails: Report Pydantic errors, suggest manual registration
  - Duplicate skill name: Offer to version bump or rename
```

---

### Fix 3: Create artifact.validate.types Skill

New skill specifically for validating artifact type lists:

**File**: `skills/artifact.validate.types/skill.yaml`

```yaml
name: artifact.validate.types
version: 0.1.0
description: >
  Validate that artifact types exist in registry and return correct
  file_pattern, content_type, and schema references.

inputs:
  - name: artifact_types
    type: array
    required: true
    description: List of artifact types to validate

  - name: check_schemas
    type: boolean
    required: false
    default: true
    description: Whether to verify schema files exist

outputs:
  - name: validation_result
    type: object
    description: Validation results with registry data for each type

  - name: errors
    type: array
    description: List of validation errors

  - name: suggestions
    type: object
    description: Suggested alternatives for invalid types

entrypoints:
  - command: /artifact/validate/types
    handler: artifact_validate_types.py
    runtime: python
    permissions:
      - filesystem:read

status: active
tags:
  - artifacts
  - validation
  - registry
  - quality
```

**Usage by meta.skill:**
```python
# meta.skill calls this before creating skill.yaml
result = artifact.validate.types(
    artifact_types=["threat-model", "data-flow-diagram", "architecture-overview"]
)

# Returns:
{
  "validation_result": {
    "threat-model": {
      "exists": true,
      "file_pattern": "*.threat-model.yaml",
      "content_type": "application/yaml",
      "schema": "schemas/artifacts/threat-model-schema.json"
    },
    "data-flow-diagram": {
      "exists": false,
      "suggestion": "data-flow-diagrams (plural form)"
    },
    "architecture-overview": {
      "exists": true,
      "file_pattern": "*.architecture-overview.md",
      "content_type": "text/markdown",
      "schema": null
    }
  },
  "errors": [
    "Artifact type 'data-flow-diagram' not found in registry"
  ],
  "suggestions": {
    "data-flow-diagram": ["data-flow-diagrams", "dataflow-diagram"]
  }
}
```

---

### Fix 4: Add Validation Tests

**File**: `tests/test_skill_registration.py`

```python
"""Test that skills can be properly registered."""

def test_registry_update_with_detailed_inputs():
    """Test that registry.update accepts detailed input/output specs."""
    manifest = {
        "name": "test.skill",
        "version": "0.1.0",
        "description": "Test skill",
        "inputs": [
            {
                "name": "test_input",
                "type": "string",
                "required": true,
                "description": "Test parameter"
            }
        ],
        "outputs": [
            {
                "name": "test_output",
                "type": "object",
                "description": "Test result"
            }
        ],
        "status": "draft"
    }

    # Should not raise validation error
    SkillManifest.model_validate(manifest)


def test_artifact_metadata_validation():
    """Test that artifact metadata validates against registry."""
    artifact_types = ["threat-model", "architecture-overview"]

    result = validate_artifact_types(artifact_types)

    assert result["threat-model"]["exists"] == True
    assert result["threat-model"]["file_pattern"] == "*.threat-model.yaml"
```

---

## Implementation Priority

### Phase 1: Unblock Skill Registration (Week 1) 🔥

1. **Fix SkillManifest Pydantic Model**
   - Update betty/models.py with Union types
   - Add SkillInput and SkillOutput models
   - Test with existing registry data

2. **Test registry.update**
   - Verify it accepts threat.model.generate
   - Ensure no regressions for existing skills

### Phase 2: Enhance meta.skill (Week 2) 🎯

3. **Create artifact.validate.types Skill**
   - Implement validation logic
   - Add fuzzy matching for suggestions
   - Test with known good/bad artifact types

4. **Update meta.skill System Prompt**
   - Add explicit artifact validation step
   - Specify error handling procedures
   - Add validation call to workflow

5. **Test meta.skill End-to-End**
   - Create a test skill from description
   - Verify artifact types are validated
   - Confirm registration succeeds
   - Check skill is discoverable

### Phase 3: Quality & Documentation (Week 3) 📚

6. **Add Validation Tests**
   - Unit tests for SkillManifest
   - Integration tests for meta.skill
   - Regression tests for registry.update

7. **Update Documentation**
   - Fix SPECIALIZED_SKILL_CREATION_PATTERN.md
   - Document new validation workflow
   - Add troubleshooting guide

---

## Success Criteria

### For registry.update Fix:
- ✅ Can register skills with detailed input/output specs
- ✅ Validates artifact_metadata properly
- ✅ No regressions for existing skills
- ✅ Clear error messages on validation failure

### For meta.skill Enhancement:
- ✅ Automatically validates artifact types before skill creation
- ✅ Suggests corrections for typos (singular/plural, etc.)
- ✅ Prevents creation with invalid artifact types
- ✅ Successfully registers skill with complete artifact_metadata
- ✅ Works end-to-end without manual intervention

### For Overall Framework:
- ✅ Can create P1 skills using meta.skill without workarounds
- ✅ All artifact types validated automatically
- ✅ Skills discoverable via agent.compose
- ✅ Scalable to 50+ specialized skills

---

## Open Questions

1. **Should we support both simple and detailed input formats?**
   - Pro: Backward compatible
   - Con: More complexity
   - Recommendation: Yes, use Union types

2. **What to do about existing skills with wrong format?**
   - Some skills might have simple List[str] inputs
   - Migration needed?
   - Recommendation: Union type handles both automatically

3. **Should artifact.validate.types be separate or part of artifact.define?**
   - Separate: More modular, specific purpose
   - Combined: Fewer skills to maintain
   - Recommendation: Separate for clarity

4. **How to handle version conflicts during registration?**
   - Current behavior unclear
   - Recommendation: Document and test version conflict scenarios

---

## References

- Issue discovered: threat.model.generate registration failure
- Affected files:
  - `betty/models.py` - SkillManifest validation
  - `agents/meta.skill/agent.yaml` - Workflow needs artifact validation
  - `skills/registry.update/registry_update.py` - Uses broken SkillManifest
  - `registry/skills.json` - Actual data format (detailed objects)

---

## Next Steps

1. **Immediate**: File GitHub issues for both problems
2. **This Week**: Fix SkillManifest Pydantic model
3. **Next Week**: Enhance meta.skill with artifact.validate.types
4. **Validation**: Create P1 skills using fixed workflow

**Without these fixes, we cannot properly scale to 50+ specialized skills.**
