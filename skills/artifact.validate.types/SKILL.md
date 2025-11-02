# artifact.validate.types

## Overview

Validates artifact type names against the Betty Framework registry and returns complete metadata for each type. Provides intelligent fuzzy matching and suggestions for invalid types.

**Version**: 0.1.0
**Status**: active

## Purpose

This skill is critical for ensuring skills reference valid artifact types before creation. It validates artifact type names against `registry/artifact_types.json`, retrieves complete metadata (file_pattern, content_type, schema), and suggests alternatives for invalid types using three fuzzy matching strategies:

1. **Singular/Plural Detection** (high confidence) - Detects "data-flow-diagram" vs "data-flow-diagrams"
2. **Generic vs Specific Variants** (medium confidence) - Suggests "logical-data-model" for "data-model"
3. **Levenshtein Distance** (low confidence) - Catches typos like "thret-model" → "threat-model"

This skill is specifically designed to be called by `meta.skill` during Step 2 (Validate Artifact Types) of the skill creation workflow.

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `artifact_types` | array | Yes | - | List of artifact type names to validate |
| `check_schemas` | boolean | No | `true` | Whether to verify schema files exist on filesystem |
| `suggest_alternatives` | boolean | No | `true` | Whether to suggest similar types for invalid ones |
| `max_suggestions` | number | No | `3` | Maximum number of suggestions per invalid type |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `validation_results` | object | Validation results for each artifact type with complete metadata |
| `all_valid` | boolean | Whether all artifact types are valid |
| `invalid_types` | array | List of artifact types that don't exist in registry |
| `suggestions` | object | Suggested alternatives for each invalid type |
| `warnings` | array | List of warnings (e.g., schema file missing) |

## Artifact Metadata

### Produces
- **validation-report** (`*.validation.json`) - Validation results with metadata and suggestions

### Consumes
None - reads directly from registry files

## Usage

### Example 1: Validate Single Artifact Type

```bash
python artifact_validate_types.py \
  --artifact_types '["threat-model"]' \
  --check_schemas true
```

**Output:**
```json
{
  "validation_results": {
    "threat-model": {
      "valid": true,
      "file_pattern": "*.threat-model.yaml",
      "content_type": "application/yaml",
      "schema": "schemas/artifacts/threat-model-schema.json",
      "description": "Threat model (STRIDE, attack trees)..."
    }
  },
  "all_valid": true,
  "invalid_types": [],
  "suggestions": {},
  "warnings": []
}
```

### Example 2: Invalid Type with Suggestions

```bash
python artifact_validate_types.py \
  --artifact_types '["data-flow-diagram", "threat-model"]' \
  --suggest_alternatives true
```

**Output:**
```json
{
  "validation_results": {
    "data-flow-diagram": {
      "valid": false
    },
    "threat-model": {
      "valid": true,
      "file_pattern": "*.threat-model.yaml",
      "content_type": "application/yaml",
      "schema": "schemas/artifacts/threat-model-schema.json"
    }
  },
  "all_valid": false,
  "invalid_types": ["data-flow-diagram"],
  "suggestions": {
    "data-flow-diagram": [
      {
        "type": "data-flow-diagrams",
        "reason": "Plural form",
        "confidence": "high"
      },
      {
        "type": "dataflow-diagram",
        "reason": "Similar spelling",
        "confidence": "low"
      }
    ]
  },
  "warnings": [],
  "ok": false,
  "status": "validation_failed"
}
```

### Example 3: Multiple Invalid Types with Generic → Specific Suggestions

```bash
python artifact_validate_types.py \
  --artifact_types '["data-model", "api-spec", "test-result"]' \
  --max_suggestions 3
```

**Output:**
```json
{
  "all_valid": false,
  "invalid_types": ["data-model", "api-spec"],
  "suggestions": {
    "data-model": [
      {
        "type": "logical-data-model",
        "reason": "Specific variant of model",
        "confidence": "medium"
      },
      {
        "type": "physical-data-model",
        "reason": "Specific variant of model",
        "confidence": "medium"
      },
      {
        "type": "enterprise-data-model",
        "reason": "Specific variant of model",
        "confidence": "medium"
      }
    ],
    "api-spec": [
      {
        "type": "openapi-spec",
        "reason": "Specific variant of spec",
        "confidence": "medium"
      },
      {
        "type": "asyncapi-spec",
        "reason": "Specific variant of spec",
        "confidence": "medium"
      }
    ]
  },
  "validation_results": {
    "test-result": {
      "valid": true,
      "file_pattern": "*.test-result.json",
      "content_type": "application/json"
    }
  }
}
```

### Example 4: Save Validation Report to File

```bash
python artifact_validate_types.py \
  --artifact_types '["threat-model", "architecture-overview"]' \
  --output validation-results.validation.json
```

Creates `validation-results.validation.json` with complete validation report.

## Integration with meta.skill

The `meta.skill` agent calls this skill in Step 2 of its workflow:

```yaml
# meta.skill workflow Step 2
2. **Validate Artifact Types**
   - Extract artifact types from skill description
   - Call artifact.validate.types with all types
   - If all_valid == false:
     → Display suggestions to user
     → Ask user to confirm correct types
     → HALT until types are validated
   - Store validated metadata for use in skill.yaml generation
```

**Example Integration:**

```python
# meta.skill calls artifact.validate.types
result = subprocess.run([
    'python', 'skills/artifact.validate.types/artifact_validate_types.py',
    '--artifact_types', json.dumps(["threat-model", "data-flow-diagrams"]),
    '--suggest_alternatives', 'true'
], capture_output=True, text=True)

validation = json.loads(result.stdout)

if not validation['all_valid']:
    print(f"❌ Invalid artifact types: {validation['invalid_types']}")
    for invalid_type, suggestions in validation['suggestions'].items():
        print(f"\n  Suggestions for '{invalid_type}':")
        for s in suggestions:
            print(f"    - {s['type']} ({s['confidence']} confidence): {s['reason']}")
    # HALT skill creation
else:
    print("✅ All artifact types validated")
    # Continue with skill.yaml generation using validated metadata
```

## Fuzzy Matching Strategies

### Strategy 1: Singular/Plural Detection (High Confidence)

Detects when a user forgets the "s":

| Invalid Type | Suggested Type | Reason |
|-------------|----------------|--------|
| `data-flow-diagram` | `data-flow-diagrams` | Plural form |
| `threat-models` | `threat-model` | Singular form |

### Strategy 2: Generic vs Specific Variants (Medium Confidence)

Suggests specific variants when a generic term is used:

| Invalid Type | Suggested Types |
|-------------|-----------------|
| `data-model` | `logical-data-model`, `physical-data-model`, `enterprise-data-model` |
| `api-spec` | `openapi-spec`, `asyncapi-spec`, `graphql-spec` |
| `architecture-diagram` | `system-architecture-diagram`, `component-architecture-diagram` |

### Strategy 3: Levenshtein Distance (Low Confidence)

Catches typos and misspellings (60%+ similarity):

| Invalid Type | Suggested Type | Similarity |
|-------------|----------------|------------|
| `thret-model` | `threat-model` | ~90% |
| `architecure-overview` | `architecture-overview` | ~85% |
| `api-specfication` | `api-specification` | ~92% |

## Error Handling

### Missing Registry File

```json
{
  "ok": false,
  "status": "error",
  "error": "Artifact registry not found: registry/artifact_types.json"
}
```

**Resolution**: Ensure you're running from the Betty Framework root directory.

### Invalid JSON in artifact_types Parameter

```json
{
  "ok": false,
  "status": "error",
  "error": "Invalid JSON: Expecting ',' delimiter: line 1 column 15 (char 14)"
}
```

**Resolution**: Ensure artifact_types is a valid JSON array with proper quoting.

### Corrupted Registry File

```json
{
  "ok": false,
  "status": "error",
  "error": "Invalid JSON in registry file: ..."
}
```

**Resolution**: Validate and fix `registry/artifact_types.json` syntax.

## Performance

- **Single type validation**: <100ms
- **20 types validation**: <1 second
- **All 409 types validation**: <5 seconds

Memory usage is minimal as registry is loaded once and indexed by name for O(1) lookups.

## Dependencies

- **Python 3.7+**
- **PyYAML** - For reading registry
- **difflib** - For fuzzy matching (Python stdlib)
- **jsonschema** - For validation (optional)

## Testing

Run the test suite:

```bash
cd skills/artifact.validate.types
python test_artifact_validate_types.py
```

**Test Coverage:**
- ✅ Valid artifact type validation
- ✅ Invalid artifact type detection
- ✅ Singular/plural suggestion
- ✅ Generic → specific suggestion
- ✅ Typo detection with Levenshtein distance
- ✅ Max suggestions limit
- ✅ Schema file existence checking
- ✅ Empty input handling
- ✅ Mixed valid/invalid types

## Quality Standards

- **Accuracy**: 100% for exact matches in registry
- **Suggestion Quality**: >80% relevant for common mistakes
- **Performance**: <1s for 20 types, <100ms for single type
- **Schema Verification**: 100% accurate file existence check
- **Error Handling**: Graceful handling of corrupted registry files

## Success Criteria

- ✅ Validates all 409 artifact types correctly
- ✅ Provides accurate suggestions for common mistakes (singular/plural)
- ✅ Returns exact metadata from registry (file_pattern, content_type, schema)
- ✅ Detects missing schema files and warns appropriately
- ✅ Completes validation in <1 second for up to 20 types
- ✅ Fuzzy matching handles typos within 40% character difference

## Troubleshooting

### Skill returns all_valid=false but I think types are correct

1. Check the exact spelling in `registry/artifact_types.json`
2. Look at suggestions - they often reveal plural/singular issues
3. Use `jq` to search registry:
   ```bash
   jq '.artifact_types[] | select(.name | contains("your-search"))' registry/artifact_types.json
   ```

### Fuzzy matching isn't suggesting the type I expect

1. Check if the type name follows patterns (ending in common suffix like "-model", "-spec")
2. Increase `max_suggestions` to see more options
3. The type might be too dissimilar (< 60% match threshold)

### Schema warnings appearing for valid types

This is normal if schema files haven't been created yet. Schema files are optional for many artifact types. Set `check_schemas=false` to suppress these warnings.

## Related Skills

- **artifact.define** - Define new artifact types
- **artifact.create** - Create artifact files
- **skill.define** - Validate skill manifests
- **registry.update** - Update skill registry

## References

- [Python difflib](https://docs.python.org/3/library/difflib.html) - Fuzzy string matching
- [Betty Artifact Registry](../../registry/artifact_types.json) - Source of truth for artifact types
- [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) - String similarity algorithm
- [meta.skill Agent](../../agents/meta.skill/agent.yaml) - Primary consumer of this skill
