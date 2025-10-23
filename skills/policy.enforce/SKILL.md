# policy.enforce

## Overview

The `policy.enforce` skill validates skill manifests against policy rules to ensure compliance with naming conventions, status values, and permissions.

## Purpose

Enforce governance and security policies for skill definitions before they are registered in the Betty Framework registry.

## Policy Rules

### 1. Skill Naming Convention

- **Must be lowercase**: Only lowercase letters allowed
- **Must use dot notation**: Format should be `category.name`
- **Pattern**: `^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*$`
- **Examples**:
  - ✅ `workflow.validate`
  - ✅ `api.define`
  - ✅ `policy.enforce`
  - ❌ `WorkflowValidate` (uppercase)
  - ❌ `workflow_validate` (underscore)
  - ❌ `workflow-validate` (hyphen)

### 2. Status Values

Must be one of the following:

- `draft` - Skill is in development
- `active` - Skill is production-ready
- `deprecated` - Skill is being phased out
- `archived` - Skill is no longer maintained

### 3. Permissions

Only the following permissions are allowed:

- `filesystem` - Access to file system
- `read` - Read operations
- `write` - Write operations
- `network` - Network access
- `execute` - Execute external commands

**Warnings are issued for:**

- Risky combinations (network + write + filesystem)
- Unusual patterns (write without filesystem)

## Usage

### Command Line

```bash
python policy_enforce.py <path/to/skill.yaml>
```

### Example

```bash
python policy_enforce.py /home/user/betty/skills/workflow.validate/skill.yaml
```

### Success Response

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "/path/to/skill.yaml",
  "details": {
    "compliant": true,
    "errors": [],
    "warnings": [],
    "status": "compliant",
    "path": "/path/to/skill.yaml",
    "manifest": {
      "name": "workflow.validate",
      "status": "active",
      "version": "0.1.0"
    }
  }
}
```

### Failure Response

```json
{
  "ok": false,
  "status": "failed",
  "errors": [
    "Skill name 'Workflow_Validate' violates naming policy. Must be lowercase with dot notation (e.g., 'skill.name'). Only letters, numbers, and dots allowed. Must start with a letter.",
    "Invalid status 'production'. Must be one of: active, archived, deprecated, draft"
  ],
  "path": "/path/to/skill.yaml",
  "details": {
    "compliant": false,
    "errors": [...],
    "warnings": [],
    "status": "violation",
    "path": "/path/to/skill.yaml",
    "manifest": {
      "name": "Workflow_Validate",
      "status": "production",
      "version": "0.1.0"
    }
  }
}
```

## Integration Points

### Registry Updates

The `policy.enforce` skill should be called before updating the skill registry:

```python
# In registry.update skill
policy_result = run_skill("policy.enforce", [manifest_path])
if not policy_result.get("ok"):
    raise RegistryError("Policy violations detected")
```

### CI/CD Pipeline

Can be used in continuous integration to validate skills before deployment:

```yaml
# In CI workflow
steps:
  - name: Validate skill policy
    run: python skills/policy.enforce/policy_enforce.py skills/new.skill/skill.yaml
```

## Error Handling

- Returns non-zero exit code on policy violations
- Logs warnings for potentially risky configurations
- Provides detailed error messages with policy requirements

## Dependencies

- `betty.validation` - Path validation
- `betty.errors` - Error handling
- `betty.logging_utils` - Logging

## Permissions

- `filesystem` - Read skill manifests
- `read` - Read file contents
