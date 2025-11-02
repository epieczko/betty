# Lessons Learned: Artifact-Skills Mapping

**Date**: 2025-11-02
**Context**: Creating first specialized skill (threat.model.generate)
**Issue**: Bypassed proper meta.skill workflow, leading to manual artifact validation

---

## What We Did Wrong ❌

### 1. **Bypassed meta.skill Agent**

**What we did:**
```bash
# Used skill.create directly (low-level tool)
PYTHONPATH=/home/user/betty python3 skills/skill.create/skill_create.py \
  threat.model.generate \
  "description" \
  --inputs "..." \
  --outputs "..."
```

**What we should have done:**
```bash
# Use meta.skill agent (high-level orchestrator)
betty agent meta.skill \
  --skill_description "skill_descriptions/threat.model.generate.md"
```

**Why it matters:**
- `skill.create` is a **low-level skill** that just creates directory structure
- `meta.skill` is a **meta-agent** that orchestrates validation and quality checks
- meta.skill has `artifact.define` in its `skills_available` list specifically to validate artifact types!

---

### 2. **Manual Artifact Validation**

**What we did:**
- Manually wrote Python scripts to verify artifact types exist in registry
- Manually checked file_pattern, content_type, schema matches
- Added "Step 3.5: Verify Artifact Mapping" to pattern doc

**What meta.skill should have done automatically:**
- Use `artifact.define` skill to validate artifact types against registry
- Check that all produces/consumes types exist
- Verify file patterns match registry
- Ensure schema references are valid

**From meta.skill system_prompt:**
```
2. **Generate skill.yaml** - Create complete definition with ALL required fields
   - Artifact metadata (produces/consumes)  <-- Should validate this!
```

**Skills available to meta.skill:**
```yaml
skills_available:
  - skill.create      # Low-level: create structure
  - skill.define      # Validate skill manifest
  - artifact.define   # Validate artifact types! <-- THIS IS KEY
```

---

### 3. **Didn't Update Skills Registry with artifact_metadata**

**What we found:**
```bash
# Some skills in registry HAVE artifact_metadata:
jq '.skills[] | select(has("artifact_metadata"))' registry/skills.json

# Results:
- agent.compose        ✅ Has artifact_metadata
- api.test             ✅ Has artifact_metadata
- artifact.define      ✅ Has artifact_metadata
- data.transform       ✅ Has artifact_metadata
- threat.model.generate  ❌ NOT IN REGISTRY YET!
```

**Why it's missing:**
- We created skill but didn't register it
- skill.create validation failed due to missing pydantic
- We manually added skill.yaml but didn't run registry.update

**What should happen:**
```yaml
# registry/skills.json should contain:
{
  "name": "threat.model.generate",
  "version": "0.1.0",
  "description": "...",
  "artifact_metadata": {          # <-- CRITICAL: Must be here!
    "produces": [
      {
        "type": "threat-model",
        "file_pattern": "*.threat-model.yaml",
        "content_type": "application/yaml",
        "schema": "schemas/artifacts/threat-model-schema.json"
      }
    ],
    "consumes": [
      {
        "type": "architecture-overview",
        ...
      }
    ]
  }
}
```

---

## What Betty Was Designed to Do ✅

### The Proper Flow:

```
1. Write comprehensive skill description
   └─> skill_descriptions/threat.model.generate.md

2. Invoke meta.skill agent
   └─> betty agent meta.skill \
         --skill_description skill_descriptions/threat.model.generate.md

3. meta.skill orchestrates:
   a. skill.create           # Create directory structure
   b. artifact.define        # VALIDATE artifact types exist in registry!
   c. skill.define           # Validate skill manifest
   d. registry.update        # Register skill WITH artifact_metadata
   e. docs generation        # Create SKILL.md

4. Result:
   ✅ Skill created
   ✅ Artifact types validated against registry
   ✅ artifact_metadata in skills.json
   ✅ Ready for agent composition
```

---

## Why This Matters

### 1. **Autonomous Agent Composition Requires Registry**

**How agent.compose works:**
```python
# From agent.compose skill:
def find_skills_for_artifacts(required_artifacts: List[str]):
    # Reads registry/skills.json
    # Filters skills where artifact_metadata.produces matches required_artifacts
    # Returns compatible skills
```

**If artifact_metadata not in registry:**
```python
# agent.compose can't find threat.model.generate!
# Because registry doesn't know it produces "threat-model"
```

### 2. **Skills Registry IS the Skill Artifact Registry**

**Correct understanding:**
```
registry/skills.json = {
  "skills": [
    {
      "name": "skill-name",
      "artifact_metadata": {   # <-- THIS is the skill artifact registry
        "produces": [...],
        "consumes": [...]
      }
    }
  ]
}
```

**There's no separate "skill artifact registry"** - it's the `artifact_metadata` field in `registry/skills.json`!

### 3. **meta.skill Enforces Quality**

**meta.skill should be the gatekeeper that:**
- ✅ Validates artifact types exist before allowing skill creation
- ✅ Ensures file_pattern/content_type/schema match registry
- ✅ Registers skill with complete artifact_metadata
- ✅ Enables autonomous discovery and composition

---

## Root Cause Analysis

### Why We Bypassed meta.skill

**Issue 1: meta.skill agent execution failed**
```bash
# Tried to run:
python3 skills/agent.run/agent_run.py agents/meta.skill/agent.yaml ...

# Error:
ModuleNotFoundError: No module named 'betty'
```

**Issue 2: Missing dependencies**
```bash
# skill.create validation failed:
ModuleNotFoundError: No module named 'pydantic'
```

**Our workaround:**
- Used skill.create directly (bypassing meta.skill)
- Manually created artifact_metadata
- Didn't register in skills.json

**Should have done:**
- Fixed Python environment (install dependencies)
- OR created skill description and let meta.skill handle it via Claude conversation
- OR at minimum, manually run registry.update after skill.create

---

## Correct Path Forward

### For Remaining P1 Skills

#### Option A: Fix Environment & Use meta.skill Properly ✅ RECOMMENDED

```bash
# 1. Install dependencies
pip install pydantic jsonschema

# 2. For each P1 skill:
#    - Create comprehensive skill description
#    - Invoke meta.skill agent (via Claude or directly)
#    - Let meta.skill orchestrate validation and registration

# 3. meta.skill will:
#    - Use artifact.define to validate artifact types
#    - Create skill with validated artifact_metadata
#    - Register in skills.json with artifact_metadata
```

#### Option B: Use skill.create + Manual Registry Update

```bash
# 1. Create skill with skill.create
PYTHONPATH=/home/user/betty python3 skills/skill.create/skill_create.py ...

# 2. Manually enhance skill.yaml with artifact_metadata

# 3. CRITICAL: Run artifact validation
cat <<'EOF' | python3
# ... artifact verification script ...
EOF

# 4. CRITICAL: Register skill in registry
PYTHONPATH=/home/user/betty python3 skills/registry.update/registry_update.py \
  skills/threat.model.generate/skill.yaml

# This will add skill to registry/skills.json WITH artifact_metadata!
```

---

## Action Items

### Immediate (Next Session)

1. **Install Dependencies**
   ```bash
   pip install pydantic jsonschema PyYAML
   ```

2. **Fix threat.model.generate Registration**
   ```bash
   # Register our already-created skill
   PYTHONPATH=/home/user/betty python3 skills/registry.update/registry_update.py \
     skills/threat.model.generate/skill.yaml

   # Verify it's in registry with artifact_metadata
   jq '.skills[] | select(.name == "threat.model.generate")' registry/skills.json
   ```

3. **Update SPECIALIZED_SKILL_CREATION_PATTERN.md**
   - Remove manual verification scripts
   - Document proper meta.skill usage
   - Show how meta.skill uses artifact.define for validation
   - Emphasize: meta.skill is the gatekeeper!

### For Future Skills (P1 Skills)

1. **Use meta.skill agent for skill creation**
   - Write skill description
   - Let meta.skill orchestrate validation
   - Trust meta.skill to enforce artifact mapping

2. **If meta.skill not available:**
   - Use skill.create + MANDATORY registry.update
   - registry.update puts artifact_metadata in registry

3. **Verify registration**
   ```bash
   # After creating skill, verify it's in registry:
   jq '.skills[] | select(.name == "{skill-name}") | .artifact_metadata' \
     registry/skills.json
   ```

---

## Key Learnings

### 1. Trust Betty's Meta-Agents ✅
- meta.skill was specifically designed to enforce quality
- It has artifact.define in its skills for validation
- We should have used it, not bypassed it

### 2. Registry IS the Source of Truth ✅
- `registry/skills.json` with `artifact_metadata` = skill artifact registry
- Agents use this for autonomous composition
- Skills not in registry can't be discovered

### 3. Low-Level vs High-Level Tools ✅
- **Low-level**: skill.create (structure only)
- **High-level**: meta.skill (validation + registration + quality)
- **Use high-level tools when possible**

### 4. Manual Processes Don't Scale ❌
- Manual artifact verification scripts won't scale to 50+ skills
- meta.skill automation is the way
- Document the proper flow, not workarounds

---

## Updated Skill Creation Flow

### The Right Way:

```
1. Write skill_descriptions/{skill-name}.md
   └─> Comprehensive specification with artifact types

2. Invoke meta.skill agent:
   betty agent meta.skill --skill_description skill_descriptions/{skill-name}.md

   OR (if agent.run not working):
   Conversation with Claude using meta.skill's system prompt

3. meta.skill orchestrates:
   skill.create → artifact.define → skill.define → registry.update

4. Result:
   ✅ skills/{skill-name}/ created
   ✅ Artifact types validated
   ✅ Skill in registry/skills.json WITH artifact_metadata
   ✅ Ready for agents to discover and use
```

---

## References

- `agents/meta.skill/agent.yaml` - meta.skill definition (HAS artifact.define!)
- `registry/skills.json` - Skills registry with artifact_metadata
- `skills/artifact.define/` - Artifact type validation skill
- `skills/agent.compose/` - Uses artifact_metadata for skill discovery
