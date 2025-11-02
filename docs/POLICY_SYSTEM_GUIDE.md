# Betty Policy System - User Guide

Complete guide to creating, managing, and enforcing policy profiles in the Betty Framework.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Policy Profiles](#policy-profiles)
4. [Claude Code Commands](#claude-code-commands)
5. [Creating Custom Policies](#creating-custom-policies)
6. [Examples](#examples)
7. [Troubleshooting](#troubleshooting)

---

## Overview

The Betty Policy System validates skill and agent manifests against configurable rules. It ensures manifests meet quality, security, and compliance standards before deployment.

**Key Features:**
- ✅ Configurable validation rules (YAML-based)
- ✅ Multiple policy profiles (development, staging, production)
- ✅ Automatic enforcement via Claude Code hooks
- ✅ Custom policy creation from Markdown specifications
- ✅ Batch validation across all manifests

**Architecture:**
```
Markdown Spec → policy.define → YAML Profile → policy.validate → registry/policies/
                                                                          ↓
Manifests (skill.yaml) → policy.enforce → Validation Results
```

---

## Quick Start

### List Available Policies

```bash
# In Claude Code
/policy-list
```

This shows all policy profiles in `registry/policies/` with their type, rules count, and enforcement level.

### Test a Manifest

```bash
# In Claude Code
/policy-test betty-core skills/my.skill/skill.yaml
```

This validates your manifest against the `betty-core` policy profile.

### Enforce on All Manifests

```bash
# In Claude Code
/policy-enforce --all
```

This checks ALL skill and agent manifests against betty-core validation rules.

---

## Policy Profiles

### Built-in Profiles

#### `betty-core` (Validation)
Core Betty Framework validation rules:
- Naming conventions (lowercase, dot-separated)
- Semantic versioning
- Required fields (name, version, status)
- Allowed status values (draft, active, deprecated, archived)
- Valid permissions (filesystem, network, read, write)

**Use when:** Developing skills/agents

#### `default` (Security)
Security-focused rules:
- No secrets in debug logs
- No insecure crypto libraries
- No dangerous permissions
- Semantic versioning enforcement

**Use when:** Preparing for deployment

#### `production-ready-v2` (Validation)
Production deployment requirements:
- Status must be "active"
- Strict semantic versioning
- Description required
- Production naming format

**Use when:** Deploying to production

### Profile Structure

```yaml
policy:
  name: my-policy
  version: 0.1.0
  description: What this policy validates
  type: validation | security | compliance
  scope:
    - artifact  # or skill, agent
  enforcement: blocking | warning | info

  rules:
    - field: name
      pattern: ^[a-z][a-z0-9.]*$
      message: Name must be lowercase with dots
      severity: error
      action: block

    - field: status
      allowed_values: [active, deprecated]
      message: Only active or deprecated allowed
      severity: warning
      action: warn
```

---

## Claude Code Commands

### `/policy-list`
**Lists all available policy profiles**

**Output:**
```
Policy Profiles
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
betty-core       validation    Core validation (9 rules)
default          security      Security checks (5 rules)
production-ready validation    Production requirements (4 rules)
```

**Next steps:** Use `/policy-show <name>` to view details

---

### `/policy-show <profile>`
**Show detailed profile information**

**Example:**
```bash
/policy-show betty-core
```

**Output:**
- Profile metadata (name, type, version)
- Complete list of rules with patterns/checks
- Enforcement level
- Applicable scopes

**Next steps:** Test profile with `/policy-test`

---

### `/policy-create <name> <spec-file>`
**Create new policy profile from Markdown**

**Example:**
```bash
/policy-create no-todos ./policies/no-todos-spec.md --type validation
```

**Spec file format** (`no-todos-spec.md`):
```markdown
# No TODOs Policy

Prevents TODO comments in production code.

## Rule 1: No TODO Comments
pattern: TODO:|FIXME:|HACK:
message: Remove TODO/FIXME/HACK comments before production
severity: warning
action: warn
```

**Output:**
- Creates `registry/policies/no-todos.yaml`
- Validates the generated profile
- Shows rule count and any errors

**Next steps:** Test with `/policy-test no-todos <manifest>`

---

### `/policy-validate <policy-file>`
**Validate a policy YAML file**

**Example:**
```bash
/policy-validate registry/policies/custom.yaml --strict
```

**Checks:**
- Required fields (name, version, rules)
- Valid rule structure
- Pattern syntax
- Field references

**Output:**
- ✅ Valid or ❌ Invalid
- List of errors/warnings
- Suggestions for fixes

---

### `/policy-test <profile> <manifest>`
**Test profile against a single manifest**

**Example:**
```bash
/policy-test production-ready-v2 skills/api.validate/skill.yaml
```

**Output:**
```
✓ Policy 'production-ready-v2' validation passed
  Manifest: skills/api.validate/skill.yaml
  Rules checked: 4
```

Or if violations:
```
✗ Policy 'production-ready-v2' validation failed
  Manifest: skills/api.validate/skill.yaml
  Violations: 2

  🔴 status: Status must be 'active' for production
  ⚠️  description: Description field is required
```

**Next steps:**
- Fix violations
- Re-test
- Commit when passing

---

### `/policy-enforce [--all] [--profile <name>]`
**Enforce policies on manifests**

**Single manifest:**
```bash
/policy-enforce skills/my.skill/skill.yaml --profile strict
```

**All manifests (batch mode):**
```bash
/policy-enforce --all
```

**Output:**
```
Policy Enforcement Results
━━━━━━━━━━━━━━━━━━━━━━━━
Total: 25 manifests
✓ Passed: 23
✗ Failed: 2

Failed manifests:
  skills/broken.skill/skill.yaml (2 violations)
  agents/test.agent/agent.yaml (1 violation)
```

---

## Creating Custom Policies

### Step 1: Write Markdown Specification

Create a `.md` file describing your policy rules:

```markdown
# My Custom Policy

Description of what this policy validates.

## Rule 1: Rule Name
pattern: regex-pattern-here
message: What this rule checks
severity: error | warning | info
action: block | warn | log

## Rule 2: Field Validation
field: field_name
allowed_values: [value1, value2]
message: What this rule checks
severity: error
action: block
```

### Step 2: Generate Policy Profile

```bash
/policy-create my-custom policy-spec.md --type security --enforcement blocking
```

### Step 3: Test Your Policy

```bash
/policy-test my-custom skills/test.skill/skill.yaml
```

### Step 4: Use in Enforcement

```bash
/policy-enforce --all --profile my-custom
```

---

## Examples

### Example 1: No Hardcoded Ports Policy

**Spec** (`no-hardcoded-ports.md`):
```markdown
# No Hardcoded Ports

Prevents hardcoded port numbers in configuration.

## Rule 1: Port Numbers
pattern: :\d{4,5}(?![0-9])
message: Use environment variables for port configuration
severity: warning
action: warn
```

**Create:**
```bash
/policy-create no-ports no-hardcoded-ports.md --type security
```

### Example 2: Required Documentation Policy

**Spec** (`docs-required.md`):
```markdown
# Documentation Required

Ensures all skills have proper documentation.

## Rule 1: Description Required
field: description
required: true
message: Description field must be present
severity: error
action: block

## Rule 2: Minimum Length
field: description
pattern: .{20,}
message: Description must be at least 20 characters
severity: warning
action: warn
```

**Create:**
```bash
/policy-create docs-required docs-required.md --type validation
```

### Example 3: Versioning Policy

**Spec** (`strict-versioning.md`):
```markdown
# Strict Versioning

Enforces strict semantic versioning.

## Rule 1: Semantic Version
field: version
pattern: ^\d+\.\d+\.\d+$
message: Version must be X.Y.Z format (no pre-release tags)
severity: error
action: block
```

**Create:**
```bash
/policy-create strict-version strict-versioning.md --type validation
```

---

## Troubleshooting

### Policy Not Found

**Error:** `Policy profile not found: my-policy`

**Solution:**
1. Check profile exists: `ls registry/policies/my-policy.yaml`
2. If missing, create it: `/policy-create my-policy spec.md`
3. Verify name matches exactly (case-sensitive)

### Validation Failures

**Error:** `Policy validation failed with 3 error(s)`

**Solution:**
1. View full errors: `/policy-validate registry/policies/my-policy.yaml`
2. Common issues:
   - Missing required fields (name, version, rules)
   - Invalid regex patterns (escape special chars)
   - Empty rules array
3. Fix and re-validate

### Hook Not Triggering

**Issue:** Hook doesn't run after editing manifests

**Solution:**
1. Check hook is enabled: View `.claude/hooks.yaml`
2. Look for `validate-skill-manifests` with `enabled: true`
3. Hook only triggers on `skill.yaml` and `agent.yaml` files
4. Check file path matches regex: `skill\.yaml$` or `agent\.yaml$`

### Rules Not Matching

**Issue:** Policy rules don't catch expected violations

**Solution:**
1. Test pattern separately: Use regex tester
2. Check field path: Use dot notation for nested fields
3. Verify manifest type: Rules may be scoped to skill/agent
4. Review rule in profile: `/policy-show <profile>`

---

## Advanced Topics

### Custom Rule Types

**Pattern Rules:**
```yaml
- pattern: regex-here
  message: What to check
```

**Field Rules:**
```yaml
- field: field.path
  allowed_values: [val1, val2]
  message: What's allowed
```

**Required Fields:**
```yaml
- field: field.path
  required: true
  message: Field is required
```

### Enforcement Levels

- **blocking**: Prevents deployment (errors)
- **warning**: Allows deployment with warnings
- **info**: Informational only

### Scopes

- **artifact**: General artifacts
- **skill**: Skill manifests only
- **agent**: Agent manifests only

---

## API Reference

### policy.define
```bash
python skills/policy.define/policy_define.py <spec-file> <name> [--type TYPE] [--scope SCOPE] [--enforcement LEVEL]
```

### policy.validate
```bash
python skills/policy.validate/policy_validate.py <policy-file> [--strict]
```

### policy.enforce
```bash
python skills/policy.enforce/policy_enforce.py <manifest> [--profile NAME] [--batch]
```

### meta.policy.profile
```bash
python agents/meta.policy.profile/meta_policy_profile.py <name> <spec-file> [--type TYPE]
```

---

## Best Practices

1. **Start with betty-core** for basic validation
2. **Create environment-specific profiles** (dev, staging, prod)
3. **Test policies on sample manifests** before enforcing
4. **Use descriptive rule messages** to help developers fix issues
5. **Version your policies** (increment policy.version)
6. **Document custom policies** in the spec file
7. **Run enforcement in CI/CD** to catch issues early

---

## Next Steps

- View all profiles: `/policy-list`
- Create your first custom policy
- Enable the validation hook for auto-checking
- Set up CI/CD policy enforcement

For more help, see the Betty Framework documentation.
