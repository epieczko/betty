# hook.define

## Overview

**hook.define** is a Betty skill that creates and registers validation hooks for Claude Code. Hooks enable automatic validation and policy enforcement by triggering skills on events like file edits, commits, and pushes.

## Purpose

Transform manual validation into automatic safety rails:
- **Before**: Developers must remember to run validation
- **After**: Validation happens automatically on every file edit

## Usage

### Basic Usage

```bash
python skills/hook.define/hook_define.py <event> <command> [options]
```

### Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `event` | Yes | Hook event trigger | `on_file_edit` |
| `command` | Yes | Command to execute | `api.validate {file_path} zalando` |
| `--pattern` | No | File pattern to match | `*.openapi.yaml` |
| `--blocking` | No | Block on failure (default: true) | `true` |
| `--timeout` | No | Timeout in ms (default: 30000) | `10000` |
| `--description` | No | Human-readable description | `Validate OpenAPI specs` |

### Valid Events

| Event | Triggers When | Use Case |
|-------|---------------|----------|
| `on_file_edit` | File is edited in editor | Syntax validation |
| `on_file_save` | File is saved | Code generation |
| `on_commit` | Git commit attempted | Breaking change detection |
| `on_push` | Git push attempted | Full validation suite |
| `on_tool_use` | Any tool is used | Audit logging |
| `on_agent_start` | Agent begins execution | Context injection |
| `on_workflow_end` | Workflow completes | Cleanup/notification |

## Examples

### Example 1: Validate OpenAPI Specs on Edit

```bash
python skills/hook.define/hook_define.py \
  on_file_edit \
  "python betty/skills/api.validate/api_validate.py {file_path} zalando" \
  --pattern="*.openapi.yaml" \
  --blocking=true \
  --timeout=10000 \
  --description="Validate OpenAPI specs against Zalando guidelines"
```

**Result**: Every time a `*.openapi.yaml` file is edited, it's automatically validated against Zalando guidelines. If validation fails, the edit is blocked.

### Example 2: Check Breaking Changes on Commit

```bash
python skills/hook.define/hook_define.py \
  on_commit \
  "python betty/skills/api.compatibility/check_breaking_changes.py {file_path}" \
  --pattern="specs/**/*.yaml" \
  --blocking=true \
  --description="Prevent commits with breaking API changes"
```

**Result**: Commits are blocked if they contain breaking API changes.

### Example 3: Regenerate Models on Save

```bash
python skills/hook.define/hook_define.py \
  on_file_save \
  "python betty/skills/api.generate-models/auto_generate.py {file_path}" \
  --pattern="specs/*.openapi.yaml" \
  --blocking=false \
  --description="Auto-regenerate models when specs change"
```

**Result**: When an OpenAPI spec is saved, models are regenerated automatically (non-blocking).

### Example 4: Audit Trail for All Tool Use

```bash
python skills/hook.define/hook_define.py \
  on_tool_use \
  "python betty/skills/audit.log/log_api_change.py {tool_name}" \
  --blocking=false \
  --description="Log all tool usage for compliance"
```

**Result**: All tool usage is logged for audit trails (non-blocking).

## Output

### Success Response

```json
{
  "status": "success",
  "data": {
    "hook_config": {
      "name": "api-validate-all-openapi-yaml",
      "command": "python betty/skills/api.validate/api_validate.py {file_path} zalando",
      "blocking": true,
      "timeout": 10000,
      "when": {
        "pattern": "*.openapi.yaml"
      },
      "description": "Validate OpenAPI specs against Zalando guidelines"
    },
    "hooks_file_path": "/home/user/betty/.claude/hooks.yaml",
    "event": "on_file_edit",
    "total_hooks": 1
  }
}
```

### Generated Hooks File

The skill creates/updates `.claude/hooks.yaml`:

```yaml
hooks:
  on_file_edit:
    - name: api-validate-all-openapi-yaml
      command: python betty/skills/api.validate/api_validate.py {file_path} zalando
      blocking: true
      timeout: 10000
      when:
        pattern: "*.openapi.yaml"
      description: Validate OpenAPI specs against Zalando guidelines
```

## How It Works

1. **Load Existing Hooks**: Reads `.claude/hooks.yaml` if it exists
2. **Create Hook Config**: Builds configuration from parameters
3. **Add or Update**: Adds new hook or updates existing one with same name
4. **Save**: Writes updated configuration back to `.claude/hooks.yaml`

## Benefits

### For Developers
- ✅ **Instant feedback**: Errors caught immediately, not at commit time
- ✅ **No discipline required**: Validation happens automatically
- ✅ **Consistent quality**: Standards enforced, not suggested

### For Teams
- ✅ **Enforced standards**: Can't save non-compliant code
- ✅ **Reduced review time**: Automated checks before human review
- ✅ **Onboarding**: New developers can't accidentally break standards

### For Organizations
- ✅ **Compliance**: Policies enforced at tool level
- ✅ **Audit trail**: Every validation is logged
- ✅ **Risk reduction**: Catch issues early, not in production

## Integration with Betty

### Use in Workflows

```yaml
# workflows/setup_api_validation.yaml
steps:
  - skill: hook.define
    args:
      - "on_file_edit"
      - "api.validate {file_path} zalando"
      - "--pattern=*.openapi.yaml"
      - "--blocking=true"
```

### Use in Agents

Agents can dynamically create hooks based on project needs:

```python
# Agent detects OpenAPI specs in project
# Automatically sets up validation hooks
```

## File Pattern Examples

| Pattern | Matches |
|---------|---------|
| `*.openapi.yaml` | All OpenAPI files in current directory |
| `*.asyncapi.yaml` | All AsyncAPI files in current directory |
| `specs/**/*.yaml` | All YAML files in specs/ and subdirectories |
| `src/**/*.ts` | All TypeScript files in src/ and subdirectories |
| `**/*.py` | All Python files anywhere |

## Blocking vs Non-Blocking

### Blocking Hooks (blocking: true)
- Operation is **paused** until hook completes
- If hook **fails**, operation is **aborted**
- Use for: Validation, compliance checks, breaking change detection

### Non-Blocking Hooks (blocking: false)
- Hook runs **asynchronously**
- Operation **continues** regardless of hook result
- Use for: Logging, notifications, background tasks

## Timeout Considerations

| Operation | Suggested Timeout | Reasoning |
|-----------|-------------------|-----------|
| Syntax validation | 5,000 - 10,000 ms | Fast, local checks |
| Zally API call | 10,000 - 30,000 ms | Network latency |
| Model generation | 30,000 - 60,000 ms | Compilation time |
| Full test suite | 300,000 ms (5 min) | Comprehensive testing |

## Error Handling

### Hook Execution Failed

If a blocking hook fails:
```
❌ Hook 'validate-openapi' failed:
   - Missing required field: info.x-api-id
   - Property 'userId' should use snake_case

Operation blocked. Fix errors and try again.
```

### Hook Timeout

If a hook exceeds timeout:
```
⚠️ Hook 'validate-openapi' timed out after 10000ms
Operation blocked for safety.
```

## Dependencies

- **PyYAML**: Required for YAML file handling
  ```bash
  pip install pyyaml
  ```

- **context.schema**: For validation rule definitions

## Files Created

- `.claude/hooks.yaml` - Hook configurations for Claude Code

## See Also

- [api.validate](../api.validate/SKILL.md) - API validation skill
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [API-Driven Development](../../docs/api-driven-development.md) - Complete guide
- [Claude Code Hooks Documentation](https://docs.claude.com/en/docs/claude-code/hooks)

## Version

**0.1.0** - Initial implementation with basic hook definition support
