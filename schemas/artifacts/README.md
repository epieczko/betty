# Artifact JSON Schemas

JSON Schema definitions for validating Betty Framework artifacts.

## Overview

This directory contains JSON Schema files that define the structure, required fields, and validation rules for artifact types in the Betty Framework.

## Available Schemas

### Core Schemas

#### metadata-schema.json
Common metadata schema inherited by all artifact types. Defines:
- Document control fields (version, dates, status, classification)
- Ownership and approval workflow
- Related documents and dependencies
- Change history tracking

**Required Fields**: `version`, `created`, `author`, `status`

### Artifact Type Schemas

#### business-case-schema.json
Schema for business case artifacts. Validates:
- Executive summary
- Problem statement with stakeholders and impact
- Proposed solution with scope and approach
- Financial analysis (costs, benefits, ROI)
- Risk assessment with mitigation strategies
- Timeline and phases
- Recommendation and next steps

**Key Sections**: `executiveSummary`, `problemStatement`, `proposedSolution`, `financialAnalysis`

#### threat-model-schema.json
Schema for threat model artifacts. Validates:
- System description with components and data flows
- Asset inventory with classification
- Threat catalog using STRIDE methodology
- Security controls mapped to threats
- Residual risk acceptance
- Compliance framework mapping

**Key Sections**: `systemDescription`, `assets`, `threats`, `controls`

**STRIDE Categories**: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege

## Usage

### With artifact.validate Skill

```bash
python3 skills/artifact.validate/artifact_validate.py \
  my-artifact.yaml \
  --schema-path schemas/artifacts/business-case-schema.json
```

### With JSON Schema Validation Libraries

**Python (jsonschema)**:
```python
import json
import yaml
from jsonschema import validate, ValidationError

# Load schema
with open('schemas/artifacts/business-case-schema.json') as f:
    schema = json.load(f)

# Load artifact
with open('my-business-case.yaml') as f:
    artifact = yaml.safe_load(f)

# Validate
try:
    validate(instance=artifact, schema=schema)
    print("✅ Valid")
except ValidationError as e:
    print(f"❌ Invalid: {e.message}")
```

**Node.js (ajv)**:
```javascript
const Ajv = require('ajv');
const YAML = require('yaml');
const fs = require('fs');

const ajv = new Ajv();

// Load schema
const schema = JSON.parse(fs.readFileSync('schemas/artifacts/business-case-schema.json'));

// Load artifact
const artifact = YAML.parse(fs.readFileSync('my-business-case.yaml', 'utf8'));

// Validate
const valid = ajv.validate(schema, artifact);
if (valid) {
  console.log('✅ Valid');
} else {
  console.log('❌ Invalid:', ajv.errors);
}
```

## Schema Structure

All artifact schemas follow this pattern:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://betty-framework.dev/schemas/<artifact-type>.json",
  "title": "Artifact Type Schema",
  "description": "Schema description",
  "type": "object",
  "required": ["metadata", "content"],
  "allOf": [
    {"$ref": "./metadata-schema.json"}
  ],
  "properties": {
    "content": {
      // Artifact-specific content schema
    }
  }
}
```

## Adding New Schemas

To create a schema for a new artifact type:

1. **Create schema file**: `schemas/artifacts/<artifact-type>-schema.json`

2. **Extend metadata schema**:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://betty-framework.dev/schemas/<artifact-type>.json",
  "title": "<Artifact Type> Schema",
  "type": "object",
  "required": ["metadata", "content"],
  "allOf": [
    {"$ref": "./metadata-schema.json"}
  ],
  "properties": {
    "content": {
      // Define artifact-specific fields
    }
  }
}
```

3. **Define required fields** in the `content` section

4. **Add validation rules** (formats, enums, patterns, min/max lengths)

5. **Test the schema** against sample artifacts

6. **Update this README** with the new schema

## Validation Rules

### Common Field Types

- **Dates**: `"format": "date"` (YYYY-MM-DD)
- **Semantic Versions**: `"pattern": "^\\d+\\.\\d+\\.\\d+$"`
- **Enums**: Predefined value lists
- **Min Length**: Ensure fields have substantive content
- **Arrays**: Lists of items with item schemas
- **Objects**: Nested structures with their own required fields

### Best Practices

1. **Use descriptive titles and descriptions** for all fields
2. **Mark truly required fields only** - avoid over-constraining
3. **Provide enum values** for standardized fields (status, classification, etc.)
4. **Set reasonable min/max constraints** based on actual usage
5. **Reference metadata-schema** for consistency
6. **Document rationale** for complex validation rules

## Schema Validation Status

| Schema | Status | Coverage | Last Updated |
|--------|--------|----------|--------------|
| metadata-schema.json | ✅ Complete | Core metadata | 2025-10-25 |
| business-case-schema.json | ✅ Complete | Financial, risk, timeline | 2025-10-25 |
| threat-model-schema.json | ✅ Complete | STRIDE, controls, compliance | 2025-10-25 |

## Future Schemas

Planned schemas for Phase 2 expansion:
- requirements-specification-schema.json
- test-plan-schema.json
- architecture-diagram-schema.json
- data-model-schema.json
- deployment-plan-schema.json

## Resources

- [JSON Schema Documentation](https://json-schema.org/)
- [JSON Schema Validator](https://www.jsonschemavalidator.net/)
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/)
- [Betty Framework Artifact Standards](../docs/ARTIFACT_STANDARDS.md)

## Version

**Version**: 0.1.0
**Last Updated**: 2025-10-25
**Status**: Phase 2 - Active Development
