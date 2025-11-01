# policy.define

Define and structure policy rules from natural language descriptions or Markdown specifications.

## Purpose

Converts human-readable policy requirements into structured YAML format compatible with `policy.enforce`. This skill is used by the `meta.policy.profile` agent to transform policy specifications into enforceable rules.

## Inputs

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `policy_spec` | string | Yes | - | Markdown or natural language policy specification |
| `profile_name` | string | Yes | - | Name of the policy profile to create |
| `policy_type` | enum | No | "validation" | Type: validation, security, or compliance |
| `scope` | array | No | ["artifact"] | Where policy applies |
| `enforcement` | enum | No | "blocking" | Default enforcement level |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| `policy_yaml` | object | Structured policy definition |
| `rule_count` | integer | Number of extracted rules |
| `validation_errors` | array | Parsing/validation errors |

## Usage

```bash
/policy/define "
# Policy Profile: strict
## Rule 1: No secrets
pattern: password\\s*=
action: block
" strict --type security
```

## Tags

policy, governance, validation, parsing, yaml
