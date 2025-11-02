# meta.skill Agent - Detailed Analysis & Shortcomings

**Date**: 2025-11-02
**Agent**: `agents/meta.skill/agent.yaml`
**Purpose**: Creates complete, functional skills from natural language descriptions
**Status**: draft (untested end-to-end)

---

## What meta.skill SHOULD Do

From the agent definition:

```yaml
description: |
  Creates complete, functional skills from natural language descriptions.

  This meta-agent transforms skill descriptions into production-ready skills with:
  - Complete skill.yaml definition
  - Python implementation stub with proper structure
  - Test template with example tests
  - README documentation
  - Registry registration

  Ensures skills follow Betty Framework conventions and are ready for use in agents.
```

**Available Skills:**
```yaml
skills_available:
  - skill.create      # Scaffolds directory and files
  - skill.define      # Validates skill manifest
  - artifact.define   # Generate artifact metadata (KEY FOR VALIDATION!)
```

---

## Identified Shortcomings

### 1. **No Explicit Artifact Validation Step** ⚠️

**Current System Prompt (Step 2):**
```
2. **Generate skill.yaml** - Create complete definition with ALL required fields
   - Artifact metadata (produces/consumes)
```

**Problem:**
- Says to include artifact metadata but doesn't say HOW to validate it
- Doesn't specify to call `artifact.define` skill
- No guidance on checking artifact types exist in registry
- No error handling if artifact type is invalid

**Should Be:**
```
2. **Validate Artifact Types** - Before generating skill.yaml
   - Extract all artifact types from skill description
   - For EACH type in produces/consumes:
     a. Call artifact.define to verify type exists in registry
     b. Retrieve file_pattern, content_type, schema from registry
     c. Verify schema file exists (if specified)
   - If type doesn't exist:
     → Search for similar types (handle singular/plural, typos)
     → ERROR: "Artifact type 'data-flow-diagram' not found. Did you mean 'data-flow-diagrams'?"
     → HALT skill creation until resolved
```

**Evidence:**
```yaml
# System prompt mentions artifact.define but never says when to call it:
skills_available:
  - artifact.define    # Generate artifact metadata
```

But the workflow never explicitly calls it!

---

### 2. **Relies on Broken registry.update** ❌

**Current System Prompt (Step 6):**
```
6. **Register Skill** - Update registry
   - Add to registry/skills.json
   - Include all metadata
   - Validate registration
```

**Problem:**
- `registry.update` uses `SkillManifest` Pydantic model
- `SkillManifest` expects `inputs: List[str]`
- Actual skills use `inputs: List[Object]`
- **Registration will ALWAYS fail with validation error!**

**What Happens:**
```
meta.skill → skill.create → skill.define → registry.update
                                                ↓
                                         ❌ Pydantic ValidationError:
                                            "Input should be a valid string"
```

**This means meta.skill CANNOT complete step 6 successfully!**

---

### 3. **Vague Error Handling** 🤷

**Current System Prompt:**
```
  ## Quality Standards

  - ✅ Follows Betty conventions
  - ✅ All required fields in skill.yaml: name, version, description, inputs, outputs, status
  - ✅ Proper artifact metadata
  - ✅ Clean, documented code
  - ✅ Test template included
  - ✅ SKILL.md with markdown header and examples
  - ✅ Registered in registry
  - ✅ Passes validation tests
```

**Problem:**
- Says "passes validation tests" but what if it doesn't?
- No guidance on what to do when:
  - Artifact type not found
  - Registry update fails
  - Duplicate skill name detected
  - Schema file missing
  - Permission conflicts

**Should Have:**
```
  ## Error Handling & Recovery

  - **Artifact Type Not Found:**
    → Call artifact.define to search for similar types
    → Suggest: "Artifact 'data-model' not found. Did you mean: 'logical-data-model', 'physical-data-model', 'enterprise-data-model'?"
    → Ask user to confirm or provide correct type
    → Do NOT proceed with invalid artifact types

  - **Registry Update Fails:**
    → Report specific Pydantic error
    → Provide manual registration workaround
    → Log issue for framework team

  - **Duplicate Skill Name:**
    → Check existing version in registry
    → Offer to: (a) version bump, (b) rename, (c) cancel
    → Ensure user intent before overwriting

  - **Schema File Missing:**
    → Warn: "Schema file schemas/artifacts/threat-model-schema.json not found"
    → Ask if schema should be: (a) created, (b) removed from reference, (c) ignored
    → Continue with warning, don't block
```

---

### 4. **Untested End-to-End** 🧪

**We've Never Actually Run meta.skill!**

Attempted:
```bash
python3 skills/agent.run/agent_run.py agents/meta.skill/agent.yaml ...
```

Failed:
```
ModuleNotFoundError: No module named 'betty'
```

**Questions:**
- Does meta.skill work at all?
- Can it complete all 6 steps?
- Does it handle errors gracefully?
- Can it recover from validation failures?

**We don't know because we bypassed it!**

---

### 5. **Missing Validation Hooks** 🪝

**Current Workflow:**
```
skill.create → skill.define → registry.update
```

**Problem:**
- No validation between steps
- Can't catch errors early
- All-or-nothing approach

**Better Workflow:**
```
1. Validate artifact types (NEW STEP)
   ↓ (artifact.validate.types)
2. Generate skill.yaml with validated metadata
   ↓ (skill.create)
3. Validate manifest schema
   ↓ (skill.define)
4. Pre-validate registry entry (dry-run)
   ↓ (registry.validate - NEW SKILL)
5. Register skill
   ↓ (registry.update)
6. Post-validate discoverability
   ↓ (agent.compose dry-run to confirm skill findable)
```

Each step has validation gates!

---

### 6. **No Artifact Flow Analysis** 📊

**meta.skill should answer:**
- What artifacts does this skill produce?
- What skills consume those artifacts?
- What artifacts does this skill need?
- What skills produce those artifacts?
- Is there a complete artifact flow?

**Example:**
```
Creating skill: threat.model.generate

Artifact Flow Analysis:
✅ Produces: threat-model
   → Consumed by: (none yet - this is the first!)
   → Recommendation: Consider creating compliance.matrix.generate
                     to consume threat-model

✅ Consumes: architecture-overview
   → Produced by: (need to create architecture.designer agent)
   → Warning: No producer exists yet

⚠️  Consumes: data-flow-diagrams
   → Produced by: (none found)
   → Action Required: Create data.flow.diagram.generate skill
                      OR remove from consumes if not critical
```

**This would prevent orphaned skills!**

---

### 7. **Doesn't Verify Skill Discoverability** 🔍

After registration, meta.skill should verify:

```python
# Step 7: Verify Discoverability
def verify_skill_registered():
    """Confirm skill can be discovered by agents."""

    # Check 1: Skill in registry
    registry = load_registry()
    skill = find_skill_by_name(registry, "threat.model.generate")
    assert skill is not None, "Skill not found in registry!"

    # Check 2: Has artifact_metadata
    assert "artifact_metadata" in skill, "Missing artifact_metadata!"

    # Check 3: Discoverable by artifact type
    for artifact in skill["artifact_metadata"]["produces"]:
        discovered = find_skills_by_artifact_type(artifact["type"])
        assert "threat.model.generate" in discovered, \
            f"Skill not discoverable by artifact type {artifact['type']}!"

    # Check 4: agent.compose can find it
    result = agent.compose(required_artifacts=["threat-model"])
    assert "threat.model.generate" in result["recommended_skills"], \
        "agent.compose cannot discover skill!"

    print("✅ Skill successfully registered and discoverable!")
```

**Currently:** meta.skill just hopes registration worked

---

### 8. **No Dependency Resolution** 🔗

**skill.yaml allows dependencies:**
```yaml
dependencies:
  - PyYAML
  - jsonschema
  - custom-library
```

**meta.skill should:**
- Check if dependencies are available
- Suggest installation commands
- Warn about version conflicts
- Validate Python package names

**Currently:** Accepts any string, no validation

---

### 9. **Template Quality Issues** 📝

**Generated Files Quality:**

**Python Stub:**
```python
# Currently generates:
def main():
    parser = argparse.ArgumentParser(description="threat.model.generate")
    # TODO: Add arguments
    args = parser.parse_args()

    try:
        logger.info("Executing threat.model.generate...")
        # TODO: Implement skill logic
        result = {"status": "success", "message": "Not yet implemented"}
        print(json.dumps(result, indent=2))
```

**Problem:**
- `# TODO` everywhere
- No actual argument definitions
- No docstrings with types
- No example implementation patterns

**Should Generate:**
```python
def main():
    """
    Generate STRIDE-based threat models.

    Inputs:
        system_description (str): System architecture description
        data_flows (dict): Data flows between components
        ...

    Outputs:
        threat_model (dict): Complete threat model
        threat_model_file (str): Path to YAML file
        ...
    """
    parser = argparse.ArgumentParser(
        description="Generate STRIDE-based threat models"
    )
    parser.add_argument(
        "--system_description",
        type=str,
        required=True,
        help="System architecture description"
    )
    # ... all arguments from skill.yaml inputs
    args = parser.parse_args()

    try:
        logger.info("Generating STRIDE threat model...")

        # TODO: Implement STRIDE methodology
        # See skill_descriptions/threat.model.generate.md for requirements

        result = {
            "ok": True,
            "threat_model": {},
            "threat_model_file": args.output_path,
            "threat_count": 0,
            "high_risk_count": 0
        }
        print(json.dumps(result, indent=2))
```

Actually parse inputs from skill.yaml and generate proper CLI!

---

### 10. **No Feedback Loop** 🔁

**meta.skill is oneshot per the definition:**
```yaml
reasoning_mode: iterative
```

**But system prompt doesn't leverage this!**

**Should have feedback loop:**
```
User: "Create threat modeling skill"
  ↓
meta.skill: "I found these artifact types in description:
             - threat-model ✅ exists
             - data-flow-diagram ❌ not found
             Did you mean 'data-flow-diagrams' (plural)?"
  ↓
User: "Yes, use data-flow-diagrams"
  ↓
meta.skill: "Updated. Generating skill with validated artifacts..."
```

**Currently:** No user interaction, just fails silently or succeeds partially

---

## Summary of Shortcomings

### Critical (Blocks Functionality) 🔴

1. **No artifact type validation** - Can create skills with invalid artifact types
2. **Broken registry.update dependency** - Cannot register skills with detailed inputs
3. **Untested end-to-end** - Don't know if it works at all

### High Priority (Quality Issues) 🟡

4. **Vague error handling** - Fails without helpful guidance
5. **No validation hooks** - Can't catch errors early
6. **No discoverability verification** - Doesn't confirm skill is usable

### Medium Priority (Enhancements) 🟢

7. **No artifact flow analysis** - Misses orphaned skills
8. **No dependency resolution** - Accepts invalid dependencies
9. **Poor template quality** - Generated code has too many TODOs
10. **No feedback loop** - Can't interact with user to fix issues

---

## Recommended Improvements

### Phase 1: Make It Work (Week 1)

1. **Add explicit artifact validation step**
   - Update system prompt with Step 1.5: "Validate Artifact Types"
   - Specify calling artifact.define for each type
   - Add error handling for missing types

2. **Work around registry.update bug**
   - Until SkillManifest is fixed, document manual registration
   - OR create registry.add.skill that bypasses validation
   - OR fix SkillManifest to accept Union[List[str], List[Object]]

3. **Test end-to-end**
   - Fix PYTHONPATH issues
   - Run meta.skill with test skill description
   - Document what works and what doesn't

### Phase 2: Make It Robust (Week 2)

4. **Add comprehensive error handling**
   - Specific recovery for each error type
   - Clear user guidance
   - Graceful degradation

5. **Add validation gates**
   - Pre-validate artifacts
   - Pre-validate registry entry (dry-run)
   - Post-validate discoverability

6. **Verify discoverability**
   - Test agent.compose can find skill
   - Confirm artifact_metadata in registry
   - Check artifact flow completeness

### Phase 3: Make It Smart (Week 3)

7. **Add artifact flow analysis**
   - Show what consumes skill's outputs
   - Show what produces skill's inputs
   - Warn about gaps

8. **Validate dependencies**
   - Check Python package names
   - Suggest installation commands
   - Warn about conflicts

9. **Improve templates**
   - Parse skill.yaml to generate proper CLI
   - Add type hints and docstrings
   - Include implementation patterns

10. **Enable feedback loop**
    - Use iterative reasoning mode
    - Ask user to confirm/fix issues
    - Iterate until skill is correct

---

## Success Criteria

After improvements, meta.skill should:

✅ Validate all artifact types before creating skill.yaml
✅ Successfully register skill with complete artifact_metadata
✅ Verify skill is discoverable via agent.compose
✅ Provide helpful error messages with recovery suggestions
✅ Generate production-quality code stubs
✅ Work end-to-end without manual intervention
✅ Scale to creating 50+ specialized skills

---

## Testing Plan

### Unit Tests
- Test artifact type validation
- Test error handling for missing types
- Test template generation quality

### Integration Tests
- Test full skill creation workflow
- Test registry registration succeeds
- Test skill discoverability

### End-to-End Test
```bash
# Create skill from description
betty agent meta.skill \
  --skill_description skill_descriptions/compliance.matrix.generate.md

# Expected result:
# ✅ Artifact types validated
# ✅ skill.yaml created with correct metadata
# ✅ Python stub generated with proper CLI
# ✅ Registered in registry/skills.json
# ✅ Discoverable via agent.compose
# ✅ No manual intervention needed
```

---

## Open Questions

1. **Should meta.skill fix registry.update or work around it?**
   - Fix: More effort, benefits all skills
   - Workaround: Faster, but technical debt

2. **How much user interaction is appropriate?**
   - None: Fully autonomous (current)
   - Some: Confirm fixes for errors (proposed)
   - Lots: Review every step (too slow)

3. **Should meta.skill create artifact types if missing?**
   - Pro: Enables new domains quickly
   - Con: Could lead to artifact sprawl
   - Recommendation: Suggest to user, don't auto-create

4. **What to do about the 409 existing artifact types without skills?**
   - Create skills for all? (massive effort)
   - Rely on generic artifact.create? (current)
   - Prioritize based on usage? (pragmatic)

---

## Next Actions

1. **File GitHub issue**: "meta.skill cannot complete registration due to SkillManifest validation"
2. **Fix SkillManifest** in betty/models.py (blocks everything)
3. **Update meta.skill system prompt** with artifact validation step
4. **Create artifact.validate.types** skill for validation
5. **Test meta.skill end-to-end** with fixed dependencies
6. **Document workarounds** until fixes are complete

**Bottom Line:** meta.skill is a good design but has critical gaps that prevent it from being the quality gatekeeper it was meant to be.
