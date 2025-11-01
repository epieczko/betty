# meta.policy.profile

Generate and register reusable policy profiles from Markdown descriptions.

## Purpose

The `meta.policy.profile` agent transforms human-readable policy specifications into structured YAML profiles that can be enforced by `policy.enforce` and referenced by compliance hooks. This enables declarative policy management and automated compliance checking.

## Capabilities

- Parse Markdown policy specifications into structured rules
- Convert policy rules to YAML format compatible with `policy.enforce`
- Validate policy profiles for completeness and correctness
- Register policy profiles in the registry (`registry/policies/`)
- Generate audit trails for policy profile creation

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `profile_name` | string | Yes | Name of the policy profile (e.g., "default", "prod", "strict") |
| `policy_spec` | string | Yes | Markdown document with policy rules and descriptions |
| `target_scope` | array | No | Scopes where this policy applies (default: ["artifact", "agent", "skill"]) |
| `severity_mapping` | object | No | Optional mapping of rules to severity levels |
| `output_mode` | enum | No | "preview", "register", or "both" (default: "both") |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| `policy_profile_file` | string | Path to generated policy profile |
| `rule_count` | integer | Number of rules in the profile |
| `validation_result` | string | "pass" or "fail" |
| `trace_id` | string | Audit event identifier |

## Usage Example

```bash
/agent/run meta.policy.profile --input '
profile_name: "strict"
policy_spec: |
  # Policy Profile: strict

  ## Rule 1: No hardcoded secrets
  pattern: (password|api_key|secret)\\s*=\\s*["\'][^"\']+["\']
  action: block

  ## Rule 2: Require version field
  check: version exists
  action: warn

  Metadata:
  version: 0.1.0
  environments: [prod]
  tags: ["security", "strict"]
output_mode: "both"
'
```

## Policy Spec Format

Policy specifications are written in Markdown with the following structure:

```markdown
# Policy Profile: <name>

## Rule 1: <description>
pattern: <regex_pattern>  # or check: <field> exists
action: <block|warn|info>

## Rule 2: <description>
check: <field_check>
action: <block|warn|info>

Metadata:
version: <semantic_version>
environments: [<env1>, <env2>]
status: <active|draft>
tags: [<tag1>, <tag2>]
```

## Generated Policy Format

The agent generates YAML files in the following format:

```yaml
policy:
  name: <profile_name>
  version: <version>
  description: <description>
  type: <validation|security|compliance>
  scope: [<scopes>]
  rules:
    - field: <field_name>
      pattern: <regex>  # optional
      message: <user_message>
      severity: <error|warning|info>
      action: <block|warn|info>
  enforcement: <blocking|warning|info>
  environments: [<environments>]
  tags: [<tags>]
```

## Skills Used

- `policy.define` - Parse and structure policy rules
- `policy.validate` - Validate policy definitions
- `fs.write` - Write policy files to registry
- `audit.log` - Create audit trail

## Integration

Policy profiles created by this agent are automatically:
- Registered in `registry/policies/<profile_name>.yaml`
- Available for use by `policy.enforce` skill
- Referenced by compliance hooks (e.g., `artifact.policy.validate`)
- Tracked in the audit log for governance

## Related Components

- **Hook**: `artifact.policy.validate` - Automatically validates artifacts using policy profiles
- **Skill**: `policy.enforce` - Enforces policy rules against artifacts
- **Skill**: `policy.define` - Converts policy specs to structured YAML
- **Skill**: `policy.validate` - Validates policy profile definitions

## Tags

meta, policy, compliance, governance, validation, security
