# docs.validate.skill_docs

## Overview

The `docs.validate.skill_docs` skill validates SKILL.md documentation files against their corresponding skill.yaml manifests to ensure completeness, consistency, and quality. This skill helps maintain high documentation standards across all Betty Framework skills by automatically checking for required sections and verifying that documented fields match the manifest.

## Purpose

Documentation quality is critical for skill discoverability and usability. This skill addresses the common problem of documentation drift, where SKILL.md files become outdated or incomplete as skills evolve. By automatically validating documentation, this skill ensures that:

- All required documentation sections are present
- Documented inputs and outputs match the manifest
- Skill metadata is consistent between files
- Documentation follows Betty Framework standards

This enables developers to maintain high-quality, trustworthy documentation with minimal manual effort.

## Usage

### Basic Usage

```bash
python skills/docs.validate.skill_docs/skill_docs_validate.py <skill_path> [options]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `skill_path` | string | Yes | - | Path to skill directory containing skill.yaml and SKILL.md |
| `--summary` | boolean | No | false | Print a short summary table instead of full JSON output |
| `--no-headers` | boolean | No | false | Skip validation of required headers |
| `--no-manifest-parity` | Skip validation of manifest field parity |

### Options

- `--summary`: Displays a concise table showing validation status for each skill
- `--no-headers`: Skips checking for required section headers
- `--no-manifest-parity`: Skips checking that SKILL.md matches skill.yaml fields

## Inputs

The skill accepts the following inputs:

- **skill_path** (required): Path to the skill directory to validate. Can be a single skill directory or a parent directory containing multiple skills for batch validation.

- **summary** (optional, default: false): When enabled, outputs a formatted table summary instead of detailed JSON output. Useful for quick validation checks.

- **check_headers** (optional, default: true): Validates that SKILL.md contains all required section headers: Overview, Purpose, Usage, Inputs, Outputs, Examples, Integration, and Errors.

- **check_manifest_parity** (optional, default: true): Validates that documented inputs, outputs, and metadata match the skill.yaml manifest.

## Outputs

The skill produces a JSON validation report with the following fields:

- **ok** (boolean): Overall validation status (true if valid, false if errors found)
- **status** (string): "valid" or "invalid"
- **skill_path** (string): Path to the validated skill
- **skill_name** (string): Name of the skill from manifest
- **valid** (boolean): Whether the skill documentation is valid
- **errors** (array): List of validation errors
- **warnings** (array): List of validation warnings
- **validation_report** (object): Detailed validation results

Each error/warning includes:
- `type`: Error type (e.g., "missing_header", "undocumented_input")
- `message`: Human-readable description
- `severity`: "error" or "warning"
- `file`: Affected file (if applicable)
- `suggestion`: Recommended fix (if applicable)

## Examples

### Example 1: Validate a Single Skill

```bash
python skills/docs.validate.skill_docs/skill_docs_validate.py skills/api.validate
```

**Output**:
```json
{
  "ok": true,
  "status": "valid",
  "skill_path": "skills/api.validate",
  "errors": [],
  "warnings": [],
  "details": {
    "valid": true,
    "skill_name": "api.validate",
    "skill_path": "skills/api.validate",
    "errors": [],
    "warnings": [],
    "checks_run": {
      "headers": true,
      "manifest_parity": true
    }
  }
}
```

### Example 2: Batch Validate All Skills with Summary

```bash
python skills/docs.validate.skill_docs/skill_docs_validate.py skills --summary
```

**Output**:
```
================================================================================
SKILL DOCUMENTATION VALIDATION SUMMARY
================================================================================
Skill Name                      Status    Errors    Warnings
--------------------------------------------------------------------------------
api.validate                    VALID     0         0
docs.validate.skill_docs        VALID     0         0
generate.docs                   VALID     0         1
workflow.validate               INVALID   2         0
--------------------------------------------------------------------------------
Total: 4 skills | Valid: 3 | Total Errors: 2 | Total Warnings: 1
================================================================================
```

### Example 3: Validate with Detailed Error Report

```bash
python skills/docs.validate.skill_docs/skill_docs_validate.py skills/workflow.validate
```

**Output**:
```json
{
  "ok": false,
  "status": "invalid",
  "skill_path": "skills/workflow.validate",
  "errors": [
    {
      "type": "missing_header",
      "message": "Required header 'Integration' not found in SKILL.md",
      "severity": "error",
      "file": "SKILL.md",
      "suggestion": "Add a '## Integration' section to SKILL.md"
    },
    {
      "type": "undocumented_input",
      "message": "Input 'strict_mode' from manifest not documented in SKILL.md",
      "severity": "error",
      "file": "SKILL.md",
      "suggestion": "Document the 'strict_mode' input in the Inputs section"
    }
  ],
  "warnings": [],
  "details": {
    "valid": false,
    "skill_name": "workflow.validate",
    "checks_run": {
      "headers": true,
      "manifest_parity": true
    }
  }
}
```

### Example 4: Skip Header Validation

```bash
python skills/docs.validate.skill_docs/skill_docs_validate.py skills/api.validate --no-headers
```

This validates only manifest field parity, skipping header checks.

## Validation Rules

### Required Headers

The following headers must be present in SKILL.md:

1. **Overview**: Brief description of the skill
2. **Purpose**: Detailed explanation of the problem it solves
3. **Usage**: How to use the skill with command examples
4. **Inputs**: Documentation of all input parameters
5. **Outputs**: Documentation of all output fields
6. **Examples**: Practical usage examples
7. **Integration**: How to integrate with workflows or hooks
8. **Errors**: Common errors and exit codes

Alternative header variations are accepted (e.g., "How to Use" for "Usage", "Parameters" for "Inputs").

### Manifest Parity Checks

The skill validates that:

- **Skill name** from manifest appears in the documentation
- **All inputs** defined in skill.yaml are documented in SKILL.md
- **All outputs** defined in skill.yaml are documented in SKILL.md
- **Status** field uses standard values (active, deprecated, experimental)
- **Tags** are defined for skill discoverability

### Error Types

| Error Type | Severity | Description |
|------------|----------|-------------|
| `missing_file` | error | SKILL.md file not found |
| `missing_header` | error | Required section header missing |
| `undocumented_input` | error | Manifest input not documented |
| `undocumented_output` | warning | Manifest output not documented |
| `missing_skill_name` | warning | Skill name not mentioned in docs |
| `invalid_status` | warning | Non-standard status value |
| `missing_tags` | warning | No tags defined in manifest |

## Integration

### Integration with Hooks

You can integrate this skill with Betty's hook system to automatically validate documentation before commits:

```yaml
# .betty/hooks/pre-commit.yaml
name: validate-docs-pre-commit
event: pre-commit
skill: docs.validate.skill_docs
inputs:
  skill_path: ${CHANGED_SKILL_DIR}
  summary: true
on_failure: block
```

### Use in Workflows

Example workflow for continuous documentation validation:

```yaml
name: validate-all-skill-docs
description: Validate all skill documentation files

steps:
  - name: validate-docs
    skill: docs.validate.skill_docs
    inputs:
      skill_path: skills
      summary: true
      check_headers: true
      check_manifest_parity: true

  - name: report-results
    condition: ${{ steps.validate-docs.outputs.valid == false }}
    action: fail
    message: "Documentation validation failed. See errors above."
```

### CI/CD Integration

Add to your CI/CD pipeline:

```bash
# Validate all skills and fail on errors
python skills/docs.validate.skill_docs/skill_docs_validate.py skills --summary || exit 1
```

## Errors

### Exit Codes

| Code | Description |
|------|-------------|
| 0 | All validations passed successfully |
| 1 | Validation failed (errors found) or usage error |

### Common Validation Errors

#### Missing Header Error

**Error**:
```json
{
  "type": "missing_header",
  "message": "Required header 'Integration' not found in SKILL.md"
}
```

**Fix**: Add the missing section to SKILL.md:
```markdown
## Integration

Describe how to integrate this skill with workflows and hooks.
```

#### Undocumented Input Error

**Error**:
```json
{
  "type": "undocumented_input",
  "message": "Input 'api_key' from manifest not documented in SKILL.md"
}
```

**Fix**: Document the input in the Inputs section:
```markdown
## Inputs

- **api_key** (optional): API authentication key for external service
```

#### Invalid Status Warning

**Error**:
```json
{
  "type": "invalid_status",
  "message": "Manifest status 'beta' is not a standard value"
}
```

**Fix**: Update skill.yaml to use a standard status:
```yaml
status: experimental  # Use: active, deprecated, or experimental
```

## Dependencies

- **Python**: 3.8+
- **PyYAML**: For parsing skill.yaml manifests
- **Betty Framework**: context.schema dependency

## See Also

- [generate.docs](../generate.docs/SKILL.md) - Generate SKILL.md from manifests
- [workflow.validate](../workflow.validate/SKILL.md) - Validate workflow definitions
- [api.validate](../api.validate/SKILL.md) - Validate API specifications

## Version

v0.1.0
