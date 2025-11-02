# Skill Description: artifact.validate.types

## Overview
Validate that artifact types exist in the Betty Framework registry and return complete metadata for each type. Provides fuzzy matching and suggestions for invalid types.

## Skill Name
`artifact.validate.types`

## Purpose
This skill is critical for ensuring skills reference valid artifact types before creation. It validates artifact type names against `registry/artifact_types.json`, retrieves complete metadata (file_pattern, content_type, schema), and suggests alternatives for invalid types using fuzzy matching (singular/plural, typos, similar names).

This skill is specifically designed to be called by meta.skill during Step 2 (Validate Artifact Types) of the skill creation workflow.

## Inputs

### Required
- **artifact_types** (array): List of artifact type names to validate (e.g., ["threat-model", "architecture-overview"])

### Optional
- **check_schemas** (boolean): Whether to verify schema files exist on filesystem. Default: true
- **suggest_alternatives** (boolean): Whether to suggest similar types for invalid ones. Default: true
- **max_suggestions** (number): Maximum number of suggestions per invalid type. Default: 3

## Outputs

- **validation_results** (object): Validation results for each artifact type with complete metadata
- **all_valid** (boolean): Whether all artifact types are valid
- **invalid_types** (array): List of artifact types that don't exist in registry
- **suggestions** (object): Suggested alternatives for each invalid type
- **warnings** (array): List of warnings (e.g., schema file missing)

## Artifact Metadata

### Produces
- **artifact-validation-report**: Validation results with metadata and suggestions
  - File pattern: `*.artifact-validation-report.json`
  - Content type: `application/json`

### Consumes
None - reads directly from registry files

## Implementation Requirements

### Core Logic

1. **Load Registry**
   ```python
   registry = load_json('registry/artifact_types.json')
   artifact_types_dict = {a['name']: a for a in registry['artifact_types']}
   ```

2. **Validate Each Type**
   ```python
   for artifact_type in artifact_types:
       if artifact_type in artifact_types_dict:
           # Valid - get metadata
           metadata = artifact_types_dict[artifact_type]

           # Check schema file exists (if check_schemas=true)
           if metadata.get('schema'):
               schema_exists = os.path.exists(metadata['schema'])
               if not schema_exists:
                   warnings.append(f"Schema file missing: {metadata['schema']}")

           results[artifact_type] = {
               'valid': True,
               'file_pattern': metadata['file_pattern'],
               'content_type': metadata['content_type'],
               'schema': metadata.get('schema'),
               'description': metadata.get('description')
           }
       else:
           # Invalid - find suggestions
           results[artifact_type] = {'valid': False}
           invalid_types.append(artifact_type)
   ```

3. **Generate Suggestions** (if suggest_alternatives=true)
   ```python
   def find_similar_types(invalid_type, all_types, max_suggestions=3):
       suggestions = []

       # Strategy 1: Singular/Plural variants
       if invalid_type.endswith('s'):
           singular = invalid_type[:-1]
           if singular in all_types:
               suggestions.append({
                   'type': singular,
                   'reason': 'Singular form',
                   'confidence': 'high'
               })
       else:
           plural = invalid_type + 's'
           if plural in all_types:
               suggestions.append({
                   'type': plural,
                   'reason': 'Plural form',
                   'confidence': 'high'
               })

       # Strategy 2: Generic vs Specific variants
       # e.g., "data-model" → ["logical-data-model", "physical-data-model"]
       if '-' in invalid_type:
           parts = invalid_type.split('-')
           base_term = parts[-1]  # e.g., "model"
           matches = [t for t in all_types if t.endswith('-' + base_term)]
           for match in matches[:max_suggestions]:
               suggestions.append({
                   'type': match,
                   'reason': f'Specific variant of {base_term}',
                   'confidence': 'medium'
               })

       # Strategy 3: Levenshtein distance for typos
       from difflib import get_close_matches
       close_matches = get_close_matches(invalid_type, all_types, n=max_suggestions, cutoff=0.6)
       for match in close_matches:
           if match not in [s['type'] for s in suggestions]:
               suggestions.append({
                   'type': match,
                   'reason': 'Similar spelling',
                   'confidence': 'low'
               })

       return suggestions[:max_suggestions]
   ```

4. **Return Results**
   ```python
   return {
       'validation_results': results,
       'all_valid': len(invalid_types) == 0,
       'invalid_types': invalid_types,
       'suggestions': suggestions_dict,
       'warnings': warnings
   }
   ```

### Data Structures

#### Validation Result Object
```json
{
  "validation_results": {
    "threat-model": {
      "valid": true,
      "file_pattern": "*.threat-model.yaml",
      "content_type": "application/yaml",
      "schema": "schemas/artifacts/threat-model-schema.json",
      "description": "Threat model (STRIDE, attack trees)..."
    },
    "data-flow-diagram": {
      "valid": false
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
  "warnings": [
    "Schema file missing: schemas/artifacts/some-schema.json"
  ]
}
```

## Permissions
- `filesystem:read` - Read registry and check schema files exist

## Tags
- artifacts
- validation
- registry
- metadata
- quality

## Dependencies
- PyYAML (for reading registry)
- difflib (for fuzzy matching - Python stdlib)

## Status
active

## Usage Examples

### Example 1: Validate Single Type
```bash
betty skill artifact.validate.types \
  --artifact_types '["threat-model"]' \
  --check_schemas true
```

**Expected Output:**
```json
{
  "validation_results": {
    "threat-model": {
      "valid": true,
      "file_pattern": "*.threat-model.yaml",
      "content_type": "application/yaml",
      "schema": "schemas/artifacts/threat-model-schema.json"
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
betty skill artifact.validate.types \
  --artifact_types '["data-flow-diagram", "threat-model"]' \
  --suggest_alternatives true
```

**Expected Output:**
```json
{
  "validation_results": {
    "data-flow-diagram": {
      "valid": false
    },
    "threat-model": {
      "valid": true,
      "file_pattern": "*.threat-model.yaml",
      ...
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
      }
    ]
  },
  "warnings": []
}
```

### Example 3: Multiple Invalid Types
```bash
betty skill artifact.validate.types \
  --artifact_types '["data-model", "api-spec", "test-result"]' \
  --max_suggestions 3
```

**Expected Output:**
```json
{
  "all_valid": false,
  "invalid_types": ["data-model", "api-spec"],
  "suggestions": {
    "data-model": [
      {"type": "logical-data-model", "reason": "Specific variant", "confidence": "medium"},
      {"type": "physical-data-model", "reason": "Specific variant", "confidence": "medium"},
      {"type": "enterprise-data-model", "reason": "Specific variant", "confidence": "medium"}
    ],
    "api-spec": [
      {"type": "openapi-spec", "reason": "Specific variant", "confidence": "medium"},
      {"type": "asyncapi-spec", "reason": "Specific variant", "confidence": "medium"}
    ]
  }
}
```

## Integration with meta.skill

This skill is called by meta.skill in Step 2:

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

## Success Criteria

- ✅ Validates all 409 artifact types correctly
- ✅ Provides accurate suggestions for common mistakes (singular/plural)
- ✅ Returns exact metadata from registry (file_pattern, content_type, schema)
- ✅ Detects missing schema files and warns appropriately
- ✅ Completes validation in <1 second for up to 20 types
- ✅ Fuzzy matching handles typos within 40% character difference

## Quality Standards

- Accuracy: 100% for exact matches in registry
- Suggestion quality: >80% relevant for common mistakes
- Performance: <1s for 20 types, <100ms for single type
- Schema verification: 100% accurate (file exists check)
- Error handling: Graceful handling of corrupted registry files

## References

- [Python difflib](https://docs.python.org/3/library/difflib.html) - Fuzzy string matching
- [Betty Artifact Registry](../registry/artifact_types.json) - Source of truth for artifact types
- [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) - String similarity algorithm
