# Skill Description: registry.validate

## Overview
Validates Betty Framework registry files (skills.json, agents.json, artifact_types.json) for schema compliance, consistency, and completeness. Provides dry-run mode to test changes before committing.

## Skill Name
`registry.validate`

## Purpose
This skill is critical for maintaining registry integrity as the Betty Framework scales. It validates:
- JSON syntax and structure
- Pydantic model compliance (SkillManifest, AgentManifest)
- Artifact type references (all types exist in artifact_types.json)
- No duplicate names/versions
- Required fields present
- File paths exist (for schemas, entrypoints)
- Circular dependency detection

This skill should be run:
- Before committing registry changes
- In CI/CD pipelines
- By meta.skill before registration
- By developers as dry-run test

## Inputs

### Required
- **registry_files** (array): List of registry files to validate (e.g., ["registry/skills.json", "registry/agents.json"])

### Optional
- **check_file_paths** (boolean): Whether to verify referenced files exist on filesystem. Default: true
- **check_artifacts** (boolean): Whether to validate artifact type references. Default: true
- **check_dependencies** (boolean): Whether to check for circular dependencies. Default: true
- **strict_mode** (boolean): Whether to treat warnings as errors. Default: false
- **output_format** (string): Output format ("json", "summary", "detailed"). Default: "detailed"

## Outputs

- **valid** (boolean): Whether all registry files are valid
- **validation_results** (object): Results for each registry file
- **errors** (array): List of errors found
- **warnings** (array): List of warnings found
- **suggestions** (array): List of suggestions for improvement
- **stats** (object): Statistics about registry (skill count, agent count, etc.)

## Artifact Metadata

### Produces
- **validation-report**: Validation results for registry files
  - File pattern: `*.validation.json`
  - Content type: `application/json`
  - Schema: `schemas/validation-report.json`

### Consumes
- **skills-registry**: skills.json file
- **agents-registry**: agents.json file
- **artifact-types-registry**: artifact_types.json file

## Implementation Requirements

### Core Validations

1. **JSON Syntax Validation**
   ```python
   try:
       with open(registry_file) as f:
           data = json.load(f)
   except json.JSONDecodeError as e:
       errors.append(f"Invalid JSON in {registry_file}: {e}")
   ```

2. **Pydantic Model Validation**
   ```python
   # For skills.json
   for skill in registry['skills']:
       try:
           SkillManifest(**skill)
       except ValidationError as e:
           errors.append(f"Skill {skill['name']}: {e}")

   # For agents.json
   for agent in registry['agents']:
       try:
           AgentManifest(**agent)
       except ValidationError as e:
           errors.append(f"Agent {agent['name']}: {e}")
   ```

3. **Artifact Type Reference Validation**
   ```python
   # Load artifact types registry
   artifact_types = load_artifact_types()

   # For each skill with artifact_metadata
   for skill in skills:
       if 'artifact_metadata' in skill:
           for artifact in skill['artifact_metadata'].get('produces', []):
               if artifact['type'] not in artifact_types:
                   errors.append(f"Skill {skill['name']} produces unknown type: {artifact['type']}")
   ```

4. **Duplicate Detection**
   ```python
   seen_names = {}
   for skill in skills:
       key = f"{skill['name']}:{skill['version']}"
       if key in seen_names:
           errors.append(f"Duplicate skill: {key}")
       seen_names[key] = True
   ```

5. **File Path Validation**
   ```python
   # Check schema files exist
   for artifact_type in artifact_types:
       if 'schema' in artifact_type:
           if not os.path.exists(artifact_type['schema']):
               warnings.append(f"Schema file missing: {artifact_type['schema']}")

   # Check entrypoint handlers exist
   for skill in skills:
       for entrypoint in skill.get('entrypoints', []):
           handler_path = f"skills/{skill['name']}/{entrypoint['handler']}"
           if not os.path.exists(handler_path):
               errors.append(f"Handler missing: {handler_path}")
   ```

6. **Circular Dependency Detection**
   ```python
   def detect_circular_deps(skills):
       graph = build_dependency_graph(skills)
       cycles = find_cycles(graph)
       if cycles:
           errors.append(f"Circular dependencies detected: {cycles}")
   ```

### Validation Result Structure

```json
{
  "valid": false,
  "validation_results": {
    "registry/skills.json": {
      "valid": true,
      "errors": [],
      "warnings": ["Schema file missing: schemas/foo.json"],
      "skill_count": 54,
      "validated_at": "2025-11-02T14:00:00Z"
    },
    "registry/agents.json": {
      "valid": false,
      "errors": ["Agent meta.skill: Missing required field 'description'"],
      "warnings": [],
      "agent_count": 21,
      "validated_at": "2025-11-02T14:00:00Z"
    }
  },
  "errors": [
    {
      "file": "registry/agents.json",
      "item": "meta.skill",
      "field": "description",
      "message": "Missing required field",
      "severity": "error"
    }
  ],
  "warnings": [
    {
      "file": "registry/skills.json",
      "item": "threat.model.generate",
      "field": "schema",
      "message": "Schema file missing: schemas/foo.json",
      "severity": "warning"
    }
  ],
  "suggestions": [
    "Consider adding version constraints for dependencies",
    "10 skills missing comprehensive documentation"
  ],
  "stats": {
    "total_skills": 54,
    "total_agents": 21,
    "total_artifact_types": 409,
    "skills_with_tests": 12,
    "skills_with_artifacts": 35,
    "validation_time_ms": 245
  }
}
```

## Output Formats

### 1. Summary Format
```
✅ registry/skills.json - Valid (54 skills, 2 warnings)
❌ registry/agents.json - Invalid (21 agents, 1 error)
✅ registry/artifact_types.json - Valid (409 types)

Overall: FAILED (1 error, 2 warnings)
```

### 2. Detailed Format
```
=== Registry Validation Report ===

registry/skills.json:
  Status: ✅ Valid
  Skills: 54
  Errors: 0
  Warnings: 2
    ⚠️  threat.model.generate: Schema file missing
    ⚠️  api.validate: Missing test coverage

registry/agents.json:
  Status: ❌ Invalid
  Agents: 21
  Errors: 1
    ❌ meta.skill: Missing required field 'description'

Suggestions:
  - Add version constraints for Python dependencies
  - Document artifact flow for 15 skills
  - Add integration tests for 8 agents

Overall: FAILED
```

### 3. JSON Format
(Full JSON structure as shown above)

## Permissions
- `filesystem:read` - Read registry files and check referenced files

## Tags
- registry
- validation
- quality
- ci-cd
- testing

## Dependencies
- pydantic
- jsonschema
- pyyaml

## Status
active

## Usage Examples

### Example 1: Validate All Registries
```bash
betty skill registry.validate \
  --registry_files '["registry/skills.json", "registry/agents.json", "registry/artifact_types.json"]' \
  --output_format summary
```

**Output:**
```
✅ registry/skills.json - Valid (54 skills, 2 warnings)
✅ registry/agents.json - Valid (21 agents)
✅ registry/artifact_types.json - Valid (409 types)

Overall: PASSED (0 errors, 2 warnings)
```

### Example 2: Strict Validation Before Commit
```bash
betty skill registry.validate \
  --registry_files '["registry/skills.json"]' \
  --strict_mode true \
  --check_file_paths true \
  --check_artifacts true
```

**Output:**
```json
{
  "valid": false,
  "errors": [
    {
      "file": "registry/skills.json",
      "item": "new.skill.name",
      "field": "artifact_metadata.produces[0].type",
      "message": "Unknown artifact type: 'invalid-type'",
      "severity": "error"
    }
  ]
}
```

### Example 3: Dry-Run Before Registration
```bash
# Test what would happen if we added this skill
betty skill registry.validate \
  --registry_files '["registry/skills.json"]' \
  --check_dependencies true
```

### Example 4: CI/CD Integration
```bash
# In GitHub Actions workflow
- name: Validate Registries
  run: |
    betty skill registry.validate \
      --registry_files '["registry/skills.json", "registry/agents.json"]' \
      --strict_mode true \
      --output_format json > validation-report.json

    if [ $(jq '.valid' validation-report.json) == "false" ]; then
      echo "Registry validation failed!"
      jq '.errors' validation-report.json
      exit 1
    fi
```

## Integration with meta.skill

This skill should be called by meta.skill in Step 9 (Register Skill) BEFORE calling registry.update:

```yaml
# meta.skill workflow Step 9
9. **Register Skill** - Update registry with dry-run validation
   - Call registry.validate as dry-run test:
     python3 skills/registry.validate/registry_validate.py \
       --registry_files '["registry/skills.json"]' \
       --strict_mode true
   - If validation fails:
     → Display errors and warnings
     → Ask user if they want to proceed anyway
     → HALT if user declines
   - If validation passes:
     → Call registry.update to add skill
     → Verify skill appears in registry
```

## CI/CD Integration

Add to `.github/workflows/validate-registries.yml`:

```yaml
name: Validate Registries

on:
  pull_request:
    paths:
      - 'registry/**'
  push:
    branches:
      - main

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install pydantic jsonschema pyyaml

      - name: Validate Registries
        run: |
          python3 skills/registry.validate/registry_validate.py \
            --registry_files '["registry/skills.json", "registry/agents.json", "registry/artifact_types.json"]' \
            --strict_mode true \
            --output_format detailed
```

## Success Criteria

- ✅ Validates all 3 registry files correctly
- ✅ Catches Pydantic validation errors
- ✅ Detects invalid artifact type references
- ✅ Finds duplicate skills/agents
- ✅ Verifies file paths exist
- ✅ Detects circular dependencies
- ✅ Completes validation in <1 second for all registries
- ✅ Provides actionable error messages
- ✅ Supports dry-run mode

## Quality Standards

- Accuracy: 100% for schema validation
- Performance: <1s for all 3 registries (<500ms typical)
- Error messages: Clear, actionable, with line numbers where possible
- Exit codes: 0 for valid, 1 for invalid
- Output: Structured JSON or human-readable summary

## References

- [Pydantic Validation](https://docs.pydantic.dev/) - Schema validation
- [JSON Schema](https://json-schema.org/) - Artifact schema validation
- [SkillManifest](../betty/models.py) - Skill schema definition
- [Betty Registries](../registry/) - Registry files to validate
