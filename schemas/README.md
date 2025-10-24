# Betty Framework - Artifact Schemas

This directory contains JSON schemas for artifact types used in the Betty Framework.

## Schemas

| Schema | Artifact Type | Description |
|--------|---------------|-------------|
| `openapi-spec.json` | `openapi-spec` | OpenAPI 3.0+ specification artifacts |
| `validation-report.json` | `validation-report` | Validation reports from any validation skill |
| `workflow-definition.json` | `workflow-definition` | Betty workflow definitions |
| `hook-config.json` | `hook-config` | Claude Code hook configurations |

## Usage

### In Skills

Skills reference schemas in their `artifact_metadata`:

```yaml
# skills/api.define/skill.yaml
artifact_metadata:
  produces:
    - type: openapi-spec
      schema: schemas/openapi-spec.json
      file_pattern: "*.openapi.yaml"
```

### Validation

Skills can validate artifacts against schemas:

```python
import json
import jsonschema

def validate_artifact(artifact_path, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)

    with open(artifact_path) as f:
        artifact = json.load(f) if artifact_path.endswith('.json') else yaml.safe_load(f)

    jsonschema.validate(artifact, schema)
```

### Adding New Schemas

1. Create `schemas/my-artifact-type.json`
2. Document in `docs/ARTIFACT_STANDARDS.md`
3. Add to skills' `artifact_metadata`
4. Update registry validation to recognize the type

## Schema Standards

All schemas follow:
- JSON Schema Draft 07 specification
- Include `$schema` and `$id` fields
- Provide `title` and `description`
- Use descriptive property names
- Include examples where helpful

## Validation Tools

Betty provides utilities for schema validation:

```python
from betty.artifact_validation import validate_artifact

# Validate an artifact
result = validate_artifact(
    artifact_path='specs/user-api.openapi.yaml',
    artifact_type='openapi-spec'
)

if not result.valid:
    print(f"Validation errors: {result.errors}")
```

## References

- **Artifact Standards**: `/docs/ARTIFACT_STANDARDS.md`
- **Skills Documentation**: `/skills/*/SKILL.md`
- **JSON Schema Specification**: https://json-schema.org/
