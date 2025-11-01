# Policy Profile Compliance System - Setup Complete

## Overview

This implementation provides a comprehensive policy profile compliance system for the Betty Framework, enabling automated validation of AI-generated artifacts against named policy profiles.

## Components Created

### 1. Hook: artifact.policy.validate

**Location**: `hooks/artifact.policy.validate.yaml`

**Purpose**: Automatically validates every AI-generated artifact against a named policy profile using `policy.enforce`. Ensures compliance scanning is applied post-generation before merge, deployment, or downstream reuse.

**Key Features**:
- Triggers on `artifact.generated` events
- Enforces policy using `policy.enforce` skill
- Logs audit trails with `audit.log`
- Notifies humans on policy violations
- Stops execution on failures (blocking enforcement)

**Outputs**:
- `policy_status` - Overall validation status
- `violation_report` - Detailed violation information
- `audit_trace_id` - Audit trail identifier

### 2. Agent: meta.policy.profile

**Location**: `agents/meta.policy.profile/agent.yaml`

**Purpose**: Generate and register reusable policy profiles from Markdown descriptions. Transforms human-readable policy specifications into structured YAML profiles.

**Capabilities**:
- Parse Markdown policy specifications
- Convert to structured YAML format
- Validate policy profiles
- Register in `registry/policies/`
- Generate audit trails

**Skills Used**:
- `policy.define` - Parse and structure rules
- `policy.validate` - Validate definitions
- `fs.write` - Write to registry
- `audit.log` - Create audit trail

**Reasoning Mode**: Oneshot (fast, single-pass processing)

### 3. Skill: policy.define

**Location**: `skills/policy.define/skill.yaml`

**Purpose**: Define and structure policy rules from natural language or Markdown specifications. Converts human-readable requirements into structured YAML.

**Inputs**:
- `policy_spec` - Markdown specification
- `profile_name` - Profile identifier
- `policy_type` - validation/security/compliance
- `scope` - Where policy applies
- `enforcement` - Enforcement level

**Outputs**:
- `policy_yaml` - Structured definition
- `rule_count` - Number of rules
- `validation_errors` - Any errors found

### 4. Skill: policy.validate

**Location**: `skills/policy.validate/skill.yaml`

**Purpose**: Validate policy profile definitions for correctness and completeness before registration.

**Features**:
- Schema compliance checking
- Pattern validation
- Field completeness verification
- Strict mode support

**Outputs**:
- `valid` - Boolean validation status
- `validation_report` - Detailed results
- `errors` - Validation errors
- `warnings` - Validation warnings

### 5. Policy Profile: default

**Location**: `registry/policies/default.yaml`

**Purpose**: Default policy profile with common security and compliance rules.

**Rules Included**:
1. **No secrets in debug logs** - Blocks `logger.debug(${secret})`
2. **OpenAPI title requirement** - Warns if title missing
3. **Insecure crypto library** - Blocks `import crypto` (requires `cryptography`)
4. **Semantic versioning** - Warns on version format issues
5. **Dangerous permissions** - Warns on risky permissions

**Enforcement**: Blocking (stops on errors)
**Environments**: local, staging, prod

## Registry Updates

### Hooks Registry
- Added `artifact.policy.validate` hook entry
- Event type: `artifact.generated`
- Status: Active

### Agents Registry
- Added `meta.policy.profile` agent entry
- Positioned after `meta.hook` in registry
- Status: Active

### Skills Registry
- Added `policy.define` skill entry
- Added `policy.validate` skill entry
- Both marked as Active

### Audit Log
- Hook creation event logged
- Agent creation event logged
- Both skills creation events logged
- Default policy profile creation logged

## Usage Examples

### Creating a New Policy Profile

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
  version: 1.0.0
  environments: [prod]
  tags: ["security", "strict"]
output_mode: "both"
'
```

### Validating an Artifact Against Policy

The `artifact.policy.validate` hook will automatically trigger when artifacts are generated. You can also manually enforce policies:

```bash
/policy/enforce path/to/artifact.yaml --profile default
```

### Validating a Policy Profile

```bash
/policy/validate registry/policies/default.yaml
/policy/validate registry/policies/strict.yaml --strict
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Artifact Generation                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ artifact.generated    │ ◄── Hook Trigger Event
         │      (event)          │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ artifact.policy.      │
         │    validate (hook)    │
         └───────────┬───────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌─────────────┐ ┌────────┐ ┌───────────┐
│ policy.     │ │ audit. │ │  notify.  │
│ enforce     │ │  log   │ │  human    │
└──────┬──────┘ └────────┘ └───────────┘
       │
       │ References
       ▼
┌─────────────────────┐
│ registry/policies/  │
│  - default.yaml     │
│  - strict.yaml      │
│  - ...              │
└─────────────────────┘
```

## Policy Specification Format

Policies are written in Markdown with this structure:

```markdown
# Policy Profile: <name>

## Rule 1: <description>
pattern: <regex_pattern>
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

Converted to YAML:

```yaml
policy:
  name: <profile_name>
  version: <version>
  description: <description>
  type: <validation|security|compliance>
  scope: [<scopes>]
  rules:
    - field: <field_name>
      pattern: <regex>
      message: <user_message>
      severity: <error|warning|info>
      action: <block|warn|info>
  enforcement: <blocking|warning|info>
  environments: [<environments>]
  tags: [<tags>]
```

## Integration Points

1. **Artifact Generation**: Hook automatically triggers on artifact creation
2. **Policy Enforcement**: `policy.enforce` skill validates against profiles
3. **Audit Trail**: All validations logged via `audit.log`
4. **Human Notification**: Violations notify designated channels
5. **Registry Integration**: Policies stored in `registry/policies/`

## Files Created

```
betty/
├── hooks/
│   ├── artifact.policy.validate.yaml
│   └── README.md
├── agents/
│   └── meta.policy.profile/
│       ├── agent.yaml
│       └── README.md
├── skills/
│   ├── policy.define/
│   │   ├── skill.yaml
│   │   └── README.md
│   └── policy.validate/
│       ├── skill.yaml
│       └── README.md
├── registry/
│   ├── policies/
│   │   └── default.yaml
│   ├── hooks.json (updated)
│   ├── agents.json (updated)
│   ├── skills.json (updated)
│   └── audit_log.json (updated)
└── POLICY_COMPLIANCE_SETUP.md (this file)
```

## Next Steps

1. **Implement Handler Scripts**: Create Python handlers for:
   - `policy_define.py`
   - `policy_validate.py`

2. **Test the System**:
   - Create test artifacts
   - Trigger the hook
   - Verify policy enforcement

3. **Create Additional Profiles**:
   - `strict` - Stricter security rules
   - `prod` - Production-only requirements
   - `dev` - Development-friendly rules

4. **Extend Rules**:
   - Add more security patterns
   - Include compliance checks
   - Add industry-specific rules

5. **Integrate with CI/CD**:
   - Hook into build pipelines
   - Gate deployments on policy compliance
   - Generate compliance reports

## Tags

policy, compliance, governance, security, validation, meta-agent, hooks, automation
