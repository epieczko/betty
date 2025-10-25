# artifact.validate

Automated artifact validation against structure, schema, and quality criteria.

## Purpose

The `artifact.validate` skill provides comprehensive validation of artifacts to ensure:
- Correct syntax (YAML/Markdown)
- Complete metadata
- Required sections present
- No placeholder content
- Schema compliance (when applicable)
- Quality standards met

## Features

✅ **Syntax Validation**: YAML and Markdown format checking
✅ **Metadata Validation**: Document control completeness
✅ **Section Validation**: Required sections verification
✅ **TODO Detection**: Placeholder and incomplete content identification
✅ **Schema Validation**: JSON schema compliance (when provided)
✅ **Quality Scoring**: 0-100 quality score with breakdown
✅ **Strict Mode**: Enforce all recommendations
✅ **Detailed Reporting**: Actionable validation reports

## Usage

### Basic Validation

```bash
python3 skills/artifact.validate/artifact_validate.py <artifact-path>
```

### With Artifact Type

```bash
python3 skills/artifact.validate/artifact_validate.py \
  my-artifact.yaml \
  --artifact-type business-case
```

### Strict Mode

```bash
python3 skills/artifact.validate/artifact_validate.py \
  my-artifact.yaml \
  --strict
```

Strict mode treats warnings as errors. Useful for:
- CI/CD pipeline gates
- Approval workflow requirements
- Production release criteria

### With JSON Schema

```bash
python3 skills/artifact.validate/artifact_validate.py \
  my-business-case.yaml \
  --schema-path schemas/artifacts/business-case-schema.json
```

### Save Validation Report

```bash
python3 skills/artifact.validate/artifact_validate.py \
  my-artifact.yaml \
  --output validation-report.yaml
```

## Validation Checks

### 1. Syntax Validation (30% weight)

**YAML Artifacts**:
- Valid YAML syntax
- Proper indentation
- No duplicate keys
- Valid data types

**Markdown Artifacts**:
- At least one heading
- Document control section
- Proper markdown structure

**Score**:
- ✅ Valid: 100 points
- ❌ Invalid: 0 points

### 2. Metadata Completeness (25% weight)

**Required Fields**:
- `version` - Semantic version (e.g., 1.0.0)
- `created` - Creation date (YYYY-MM-DD)
- `author` - Author name or team
- `status` - Draft | Review | Approved | Published

**Recommended Fields**:
- `lastModified` - Last modification date
- `classification` - Public | Internal | Confidential | Restricted
- `documentOwner` - Owning role or person
- `approvers` - Approval workflow
- `relatedDocuments` - Dependencies and references

**Scoring**:
- Missing required field: -25 points each
- Missing recommended field: -10 points each
- TODO placeholder in field: -10 points

### 3. Required Sections (25% weight)

**YAML Artifacts**:
- `metadata` section required
- `content` section expected (unless schema-only artifact)
- Empty content fields detected

**Scoring**:
- Missing required section: -30 points each
- Empty content warning: -15 points each

### 4. TODO Markers (20% weight)

Detects placeholder content:
- `TODO` markers
- `TODO:` comments
- Empty required fields
- Template placeholders

**Scoring**:
- Each TODO marker: -5 points
- Score floor: 0 (cannot go negative)

## Quality Score Interpretation

| Score | Rating | Meaning | Recommendation |
|-------|--------|---------|----------------|
| 90-100 | Excellent | Ready for approval | Minimal polish |
| 70-89 | Good | Minor improvements | Review recommendations |
| 50-69 | Fair | Needs refinement | Address key issues |
| < 50 | Poor | Significant work needed | Major revision required |

## Validation Report Structure

```yaml
success: true
validation_results:
  artifact_path: /path/to/artifact.yaml
  artifact_type: business-case
  file_format: yaml
  file_size: 2351
  validated_at: 2025-10-25T19:30:00

  syntax:
    valid: true
    error: null

  metadata:
    complete: false
    score: 90
    issues: []
    warnings:
      - "Field 'documentOwner' contains TODO marker"

  sections:
    valid: true
    score: 100
    issues: []
    warnings: []

  todos:
    - "Line 10: author: TODO"
    - "Line 15: documentOwner: TODO"
    # ... more TODOs

  quality_score: 84
  recommendations:
    - "🟡 Complete 1 recommended metadata field(s)"
    - "🔴 Replace 13 TODO markers with actual content"
    - "🟢 Artifact is good - minor improvements recommended"

is_valid: true
quality_score: 84
```

## Command-Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `artifact_path` | string | required | Path to artifact file |
| `--artifact-type` | string | auto-detect | Artifact type override |
| `--strict` | flag | false | Treat warnings as errors |
| `--schema-path` | string | none | Path to JSON schema |
| `--output` | string | none | Save report to file |

## Exit Codes

- `0`: Validation passed (artifact is valid)
- `1`: Validation failed (artifact has critical issues)

In strict mode, warnings also cause exit code `1`.

## Integration Examples

### CI/CD Pipeline (GitHub Actions)

```yaml
name: Validate Artifacts

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Validate artifacts
        run: |
          python3 skills/artifact.validate/artifact_validate.py \
            artifacts/*.yaml \
            --strict
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Validate all modified YAML artifacts
git diff --cached --name-only | grep '\.yaml$' | while read file; do
  python3 skills/artifact.validate/artifact_validate.py "$file" --strict
  if [ $? -ne 0 ]; then
    echo "❌ Validation failed for $file"
    exit 1
  fi
done
```

### Makefile Target

```makefile
.PHONY: validate
validate:
	@echo "Validating artifacts..."
	@find artifacts -name "*.yaml" -exec \
	  python3 skills/artifact.validate/artifact_validate.py {} \;
```

## Artifact Type Detection

The skill automatically detects artifact type using:

1. **Filename match**: Direct match with registry (e.g., `business-case.yaml`)
2. **Partial match**: Artifact type found in filename (e.g., `portal-business-case.yaml` → `business-case`)
3. **Metadata**: `artifactType` field in YAML metadata
4. **Manual override**: `--artifact-type` parameter

## Error Handling

### File Not Found
```
Error: Artifact file not found: /path/to/artifact.yaml
```

### Unsupported Format
```
Error: Unsupported file format: .txt. Expected yaml, yml, or md
```

### YAML Syntax Error
```
Syntax Validation:
  ❌ YAML syntax error: while parsing a block mapping
     in "<unicode string>", line 3, column 1
     expected <block end>, but found '<block mapping start>'
```

## Performance

- **Validation time**: < 100ms per artifact
- **Memory usage**: < 10MB
- **Scalability**: Can validate 1000+ artifacts in batch

## Dependencies

- Python 3.7+
- `yaml` (PyYAML) - YAML parsing
- `artifact.define` skill - Artifact registry

## Status

**Active** - Phase 2 implementation complete

## Tags

artifacts, validation, quality, schema, tier2, phase2

## Version History

- **0.1.0** (2025-10-25): Initial implementation
  - Syntax validation (YAML/Markdown)
  - Metadata completeness checking
  - Required section verification
  - TODO marker detection
  - Quality scoring
  - Strict mode
  - JSON schema support (framework)

## See Also

- `artifact.review` - AI-powered content quality review
- `artifact.create` - Generate artifacts from templates
- `schemas/artifacts/` - JSON schema library
- `docs/ARTIFACT_USAGE_GUIDE.md` - Complete usage guide
