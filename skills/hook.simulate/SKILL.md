# hook.simulate

**Version:** 0.1.0
**Status:** Active
**Tags:** hook, simulation, testing, validation, development

## Overview

The `hook.simulate` skill allows developers to test a hook manifest before registering it in the Betty Framework. It validates the manifest structure, simulates hook triggers based on event types, and optionally executes the hook commands in a controlled environment.

This skill is essential for:
- **Testing hooks before deployment** - Catch errors early in development
- **Understanding hook behavior** - See which files match patterns and how commands execute
- **Debugging hook issues** - Validate patterns, commands, and execution flow
- **Safe experimentation** - Test hooks without affecting the live system

## Features

- ✅ **Manifest Validation** - Validates all required and optional fields
- ✅ **Pattern Matching** - Shows which files match the hook's pattern
- ✅ **Event Simulation** - Simulates different hook events (on_file_edit, on_commit, etc.)
- ✅ **Command Execution** - Runs hook commands with dry-run or actual execution
- ✅ **Timeout Testing** - Validates timeout behavior
- ✅ **Blocking Simulation** - Shows how blocking hooks would behave
- ✅ **JSON Output** - Structured results for automation and analysis

## Usage

### Command Line

```bash
# Basic validation and simulation
python skills/hook.simulate/hook_simulate.py examples/test-hook.yaml

# Simulate with dry-run command execution
python skills/hook.simulate/hook_simulate.py examples/test-hook.yaml --execute --dry-run

# Actually execute the command
python skills/hook.simulate/hook_simulate.py examples/test-hook.yaml --execute --no-dry-run

# Get JSON output for scripting
python skills/hook.simulate/hook_simulate.py examples/test-hook.yaml --output json
```

### As a Skill

```python
from skills.hook.simulate.hook_simulate import simulate_hook

# Simulate a hook
results = simulate_hook(
    manifest_path="examples/test-hook.yaml",
    dry_run=True,
    execute=True
)

# Check validation
if results["valid"]:
    print("✅ Hook is valid")
else:
    print("❌ Validation errors:", results["validation_errors"])

# Check if hook would trigger
if results["trigger_simulation"]["would_trigger"]:
    print("Hook would trigger!")
    print("Matching files:", results["trigger_simulation"]["matching_files"])
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `manifest_path` | string | Yes | - | Path to the hook.yaml manifest file |
| `execute` | boolean | No | false | Whether to execute the hook command |
| `dry_run` | boolean | No | true | If true, simulate without actually running commands |

## Output Schema

```json
{
  "manifest_path": "path/to/hook.yaml",
  "timestamp": "2025-10-23 12:34:56",
  "valid": true,
  "validation_errors": [],
  "manifest": {
    "name": "hook-name",
    "version": "0.1.0",
    "description": "Hook description",
    "event": "on_file_edit",
    "command": "python script.py {file_path}",
    "when": {
      "pattern": "*.yaml"
    },
    "blocking": true,
    "timeout": 30000
  },
  "trigger_simulation": {
    "would_trigger": true,
    "reason": "Found 5 file(s) matching pattern: *.yaml",
    "matching_files": ["file1.yaml", "file2.yaml"],
    "pattern": "*.yaml"
  },
  "command_executions": [
    {
      "command": "python script.py file1.yaml",
      "executed": true,
      "dry_run": false,
      "stdout": "Validation passed",
      "stderr": "",
      "return_code": 0,
      "execution_time_ms": 123.45,
      "success": true,
      "file": "file1.yaml"
    }
  ],
  "blocking": true,
  "timeout_ms": 30000
}
```

## Examples

### Example 1: Validate OpenAPI Hook

Create a hook manifest `openapi-validator.yaml`:

```yaml
name: validate-openapi
version: 0.1.0
description: "Validate OpenAPI specifications on edit"

event: on_file_edit

command: "python betty/skills/api.validate/api_validate.py {file_path} zalando"

when:
  pattern: "**/*.openapi.yaml"

blocking: true
timeout: 30000
on_failure: show_errors

status: draft
tags: [api, validation, openapi]
```

Simulate it:

```bash
python skills/hook.simulate/hook_simulate.py openapi-validator.yaml
```

Output:
```
=== Hook Simulation Results ===
Manifest: openapi-validator.yaml
Timestamp: 2025-10-23 12:34:56

✅ VALIDATION PASSED

Hook: validate-openapi v0.1.0
Event: on_file_edit
Command: python betty/skills/api.validate/api_validate.py {file_path} zalando
Blocking: True
Timeout: 30000ms

✅ WOULD TRIGGER
Reason: Found 3 file(s) matching pattern: **/*.openapi.yaml

Matching files (3):
  - specs/petstore.openapi.yaml
  - specs/users.openapi.yaml
  - api/products.openapi.yaml
```

### Example 2: Test Commit Hook

Create `pre-commit.yaml`:

```yaml
name: pre-commit-linter
version: 1.0.0
description: "Run linter before commits"

event: on_commit

command: "pylint src/"

blocking: true
timeout: 60000

status: active
tags: [lint, quality]
```

Simulate with execution:

```bash
python skills/hook.simulate/hook_simulate.py pre-commit.yaml --execute --dry-run
```

Output:
```
=== Hook Simulation Results ===
Manifest: pre-commit.yaml
Timestamp: 2025-10-23 12:35:00

✅ VALIDATION PASSED

Hook: pre-commit-linter v1.0.0
Event: on_commit
Command: pylint src/
Blocking: True
Timeout: 60000ms

✅ WOULD TRIGGER
Reason: on_commit hook would trigger with 5 changed file(s)

Changed files (5):
  - src/main.py
  - src/utils.py
  - tests/test_main.py
  - README.md
  - setup.py

=== Command Execution Results (1) ===

[1] N/A
Command: pylint src/
Mode: DRY RUN (not executed)
```

### Example 3: Test with Actual Execution

```bash
python skills/hook.simulate/hook_simulate.py openapi-validator.yaml --execute --no-dry-run
```

Output:
```
=== Hook Simulation Results ===
...

=== Command Execution Results (3) ===

[1] specs/petstore.openapi.yaml
Command: python betty/skills/api.validate/api_validate.py specs/petstore.openapi.yaml zalando
Executed: Yes
Return code: 0
Execution time: 234.56ms
Status: ✅ SUCCESS

Stdout:
✅ OpenAPI spec is valid

[2] specs/users.openapi.yaml
Command: python betty/skills/api.validate/api_validate.py specs/users.openapi.yaml zalando
Executed: Yes
Return code: 1
Execution time: 189.23ms
Status: ❌ FAILED

Stderr:
Error: Missing required field 'info.contact'

[3] api/products.openapi.yaml
Command: python betty/skills/api.validate/api_validate.py api/products.openapi.yaml zalando
Executed: Yes
Return code: 0
Execution time: 201.45ms
Status: ✅ SUCCESS
```

### Example 4: JSON Output for Automation

```bash
python skills/hook.simulate/hook_simulate.py my-hook.yaml --output json > results.json
```

Then process with scripts:

```python
import json

with open("results.json") as f:
    results = json.load(f)

if not results["valid"]:
    print("Validation failed:")
    for error in results["validation_errors"]:
        print(f"  - {error}")
    exit(1)

if results["trigger_simulation"]["would_trigger"]:
    files = results["trigger_simulation"]["matching_files"]
    print(f"Hook would run on {len(files)} files")

for execution in results["command_executions"]:
    if not execution["success"]:
        print(f"Failed on {execution['file']}")
        print(f"Error: {execution['stderr']}")
```

## Event Type Support

| Event | Simulation Support | Description |
|-------|-------------------|-------------|
| `on_file_edit` | ✅ Full | Matches files by pattern, simulates editing |
| `on_file_save` | ✅ Full | Similar to on_file_edit |
| `on_commit` | ✅ Full | Checks git status, shows changed files |
| `on_push` | ⚠️ Partial | Notes hook would trigger, no git simulation |
| `on_tool_use` | ⚠️ Partial | Notes hook would trigger, no tool simulation |
| `on_agent_start` | ⚠️ Partial | Notes hook would trigger, no agent simulation |
| `on_workflow_end` | ⚠️ Partial | Notes hook would trigger, no workflow simulation |

## Validation Rules

The skill validates all Betty Framework hook requirements:

1. **Required Fields**: name, version, description, event, command
2. **Name Format**: Lowercase, starts with letter, allows hyphens/underscores
3. **Version Format**: Semantic versioning (e.g., 1.0.0, 0.1.0-alpha)
4. **Event**: Must be a valid hook event
5. **Command**: Non-empty string
6. **Blocking**: Must be boolean if specified
7. **Timeout**: Must be positive number in milliseconds if specified
8. **Status**: Must be draft, active, disabled, or archived if specified
9. **Pattern**: Must be non-empty string if specified in when.pattern

## Pattern Matching

The skill supports glob patterns for file matching:

| Pattern | Description | Example Matches |
|---------|-------------|-----------------|
| `*.yaml` | Files in current directory | `config.yaml`, `spec.yaml` |
| `**/*.yaml` | YAML files anywhere | `src/config.yaml`, `specs/api/v1.yaml` |
| `src/**/*.py` | Python files in src/ | `src/main.py`, `src/utils/helper.py` |
| `*.openapi.yaml` | OpenAPI files only | `petstore.openapi.yaml` |
| `tests/**/*.test.js` | Test files | `tests/unit/api.test.js` |

## Dry-Run vs Execution Modes

### Dry-Run Mode (Default)

```bash
python skills/hook.simulate/hook_simulate.py hook.yaml --execute --dry-run
```

- ✅ Validates manifest
- ✅ Shows matching files
- ✅ Shows command that would run
- ❌ Does NOT execute command
- ⚡ Safe for testing

### Execution Mode

```bash
python skills/hook.simulate/hook_simulate.py hook.yaml --execute --no-dry-run
```

- ✅ Validates manifest
- ✅ Shows matching files
- ✅ Actually executes command
- ✅ Captures stdout/stderr
- ✅ Reports execution time
- ⚠️ Use with caution

### Validation Only (No Execution)

```bash
python skills/hook.simulate/hook_simulate.py hook.yaml
```

- ✅ Validates manifest
- ✅ Shows if hook would trigger
- ✅ Shows matching files
- ❌ Does NOT execute command
- ⚡ Fastest mode

## Integration with Hook Workflow

### Development Workflow

```bash
# 1. Create hook manifest
cat > my-hook.yaml <<EOF
name: my-custom-hook
version: 0.1.0
description: "My hook description"
event: on_file_edit
command: "echo 'Hook triggered on {file_path}'"
when:
  pattern: "*.md"
EOF

# 2. Simulate and validate
python skills/hook.simulate/hook_simulate.py my-hook.yaml

# 3. Test with execution
python skills/hook.simulate/hook_simulate.py my-hook.yaml --execute --dry-run

# 4. Test actual execution
python skills/hook.simulate/hook_simulate.py my-hook.yaml --execute --no-dry-run

# 5. Register if tests pass
python skills/hook.register/hook_register.py my-hook.yaml
```

### CI/CD Integration

```yaml
# .github/workflows/test-hooks.yml
name: Test Hooks
on: [push, pull_request]

jobs:
  test-hooks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Validate all hook manifests
        run: |
          for hook in hooks/*.yaml; do
            echo "Testing $hook"
            python skills/hook.simulate/hook_simulate.py "$hook" --output json || exit 1
          done

      - name: Test hook execution
        run: |
          python skills/hook.simulate/hook_simulate.py hooks/validator.yaml --execute --no-dry-run
```

## Error Handling

### Validation Errors

```bash
$ python skills/hook.simulate/hook_simulate.py invalid-hook.yaml

=== Hook Simulation Results ===
❌ VALIDATION FAILED

Errors:
  - Missing required field: 'version'
  - Invalid event: 'on_invalid_event'. Must be one of: on_file_edit, on_file_save, on_commit, on_push, on_tool_use, on_agent_start, on_workflow_end
  - timeout must be a positive number (in milliseconds)
```

### Execution Failures

```bash
$ python skills/hook.simulate/hook_simulate.py hook.yaml --execute --no-dry-run

...

=== Command Execution Results (1) ===

[1] test.yaml
Command: python nonexistent.py test.yaml
Executed: Yes
Return code: -1
Execution time: 45.23ms
Status: ❌ FAILED

Stderr:
Error executing command: [Errno 2] No such file or directory: 'python nonexistent.py test.yaml'
```

### Timeout Handling

```bash
$ python skills/hook.simulate/hook_simulate.py slow-hook.yaml --execute --no-dry-run

...

[1] test.yaml
Command: sleep 100
Executed: Yes
Return code: -1
Execution time: 5000.12ms
Status: ❌ FAILED

Stderr:
Command timed out after 5000ms
```

## Troubleshooting

### Hook Doesn't Trigger

**Problem:** `would_trigger: false`

**Solutions:**
1. Check pattern matches files: `ls -la **/*.yaml`
2. Verify event type is appropriate
3. Ensure files exist in the manifest's directory
4. Check git status for on_commit events

### Command Fails

**Problem:** Command returns non-zero exit code

**Solutions:**
1. Test command manually: `python script.py file.yaml`
2. Check file paths and placeholders
3. Verify dependencies are installed
4. Check timeout is sufficient

### Pattern Not Matching

**Problem:** Expected files not showing in matching_files

**Solutions:**
1. Use `**/*.ext` for recursive matching
2. Check you're in the right directory
3. Test pattern with: `ls **/*.yaml`
4. Ensure pattern is in `when.pattern` field

## Best Practices

1. **Always simulate before registering** - Catch issues early
2. **Test with dry-run first** - Understand what will execute
3. **Verify pattern matching** - Ensure correct files are targeted
4. **Test timeout values** - Make sure commands complete in time
5. **Use JSON output for automation** - Integrate with CI/CD
6. **Test blocking behavior** - Understand impact on workflow
7. **Validate on representative data** - Test with real files

## Related Skills

- **hook.define** - Create hooks dynamically and add to `.claude/hooks.yaml`
- **hook.register** - Register validated hooks in the registry
- **api.validate** - Example validation skill often used in hooks

## Version History

- **0.1.0** (2025-10-23) - Initial release
  - Manifest validation
  - Event simulation (on_file_edit, on_commit)
  - Pattern matching
  - Command execution (dry-run and actual)
  - JSON and summary output formats

## License

MIT License - Part of the Betty Framework

## Contributing

To improve this skill:
1. Add support for more event types
2. Enhance simulation accuracy
3. Add more validation rules
4. Improve error messages
5. Add performance benchmarks
