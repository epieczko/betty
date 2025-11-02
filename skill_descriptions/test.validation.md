# Skill Description: test.validation

## Overview
A simple test skill to validate that meta.skill workflow works end-to-end.

## Skill Name
`test.validation`

## Purpose
Validate input data and return validation results. Simple skill for testing meta.skill agent.

## Inputs

### Required
- **data** (string): Data to validate

### Optional
- **rules** (array): Validation rules to apply. Default: ["required", "non-empty"]

## Outputs

- **is_valid** (boolean): Whether validation passed
- **errors** (array): List of validation errors if any
- **validation_report** (object): Detailed validation report

## Artifact Metadata

### Produces
- **validation-report**: Validation results and error details
  - File pattern: `*.validation-report.json`
  - Content type: `application/json`

### Consumes (Optional)
None - this is a simple input validation skill

## Implementation Requirements

### Core Logic
1. Parse input data
2. Apply validation rules
3. Generate validation report
4. Return results

## Permissions
- None required (pure validation logic)

## Tags
- validation
- testing
- data-quality

## Status
draft

## Usage Examples

### Example 1: Basic Validation
```bash
betty skill test.validation --data "test string" --rules '["required", "non-empty"]'
```

### Example 2: With Custom Rules
```bash
betty skill test.validation \
  --data "user@example.com" \
  --rules '["required", "email"]'
```

## Success Criteria

- ✅ Validates input according to rules
- ✅ Returns clear error messages
- ✅ Generates validation report artifact
