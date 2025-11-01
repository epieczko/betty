# policy.validate

Validate policy profile definitions for correctness and completeness.

## Purpose

Ensures policy rules are well-formed before registration in the policy registry. Validates schema compliance, pattern correctness, and policy best practices.

## Inputs

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `policy_path` | string | No | - | Path to policy YAML file |
| `policy_content` | object | No | - | Policy definition as object |
| `strict` | boolean | No | false | Enable strict validation |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| `valid` | boolean | Whether policy is valid |
| `validation_report` | object | Detailed results |
| `errors` | array | Validation errors |
| `warnings` | array | Validation warnings |

## Usage

```bash
/policy/validate registry/policies/default.yaml
/policy/validate registry/policies/strict.yaml --strict
```

## Validation Checks

- Schema compliance
- Required fields present
- Valid regex patterns
- Severity levels valid
- Enforcement modes valid
- Scope values valid

## Tags

policy, validation, schema, governance, quality
