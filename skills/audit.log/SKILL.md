# audit.log

## Overview

The `audit.log` skill provides centralized audit logging for the Betty Framework. It records timestamped JSON entries tracking skill execution, status, duration, and errors.

## Purpose

Maintain a comprehensive audit trail of all skill executions for compliance, debugging, and operational visibility.

## Audit Entry Format

Each audit entry contains:

```json
{
  "timestamp": "2025-10-23T12:34:56.789Z",
  "skill": "workflow.compose",
  "status": "success",
  "duration_ms": 1234,
  "errors": [],
  "metadata": {
    "workflow": "example.yaml",
    "steps_completed": 5
  }
}
```

### Fields

- **timestamp** (required): ISO 8601 UTC timestamp
- **skill** (required): Name of the skill that was executed
- **status** (required): Execution status (success, failed, timeout, etc.)
- **duration_ms** (optional): Execution duration in milliseconds
- **errors** (optional): Array of error messages
- **metadata** (optional): Additional context about the execution

## Usage

### Command Line

```bash
python audit_log.py <skill_name> <status> [duration_ms] [errors_json] [metadata_json]
```

### Examples

#### Log Successful Execution

```bash
python audit_log.py "workflow.validate" "success" 150
```

#### Log Failed Execution with Errors

```bash
python audit_log.py "workflow.compose" "failed" 5000 '["Step 3 failed", "Timeout occurred"]'
```

#### Log with Metadata

```bash
python audit_log.py "api.validate" "success" 250 "[]" '{"api": "users.yaml", "endpoints": 12}'
```

### From Python Code

```python
import subprocess
import json

# Log audit entry
result = subprocess.run(
    [
        sys.executable,
        "/path/to/audit_log.py",
        "my.skill",
        "success",
        "1234",
        json.dumps([]),
        json.dumps({"key": "value"})
    ],
    capture_output=True,
    text=True
)
```

## Audit Log File

### Location

`/home/user/betty/registry/audit_log.json`

### Structure

The audit log is a JSON array of entries:

```json
[
  {
    "timestamp": "2025-10-23T12:30:00.000Z",
    "skill": "workflow.validate",
    "status": "success",
    "duration_ms": 150
  },
  {
    "timestamp": "2025-10-23T12:31:00.000Z",
    "skill": "workflow.compose",
    "status": "failed",
    "duration_ms": 5000,
    "errors": ["Step 3 failed", "Timeout occurred"]
  }
]
```

### Rotation Policy

The audit log automatically retains only the last **10,000 entries** to prevent unbounded growth. Older entries are automatically removed when the limit is exceeded.

## Integration Points

### Workflow Execution

Audit logging should be integrated after each skill completes in workflow execution:

```python
# In workflow.compose
start_time = datetime.now()
result = run_skill(skill_name, args)
duration_ms = int((datetime.now() - start_time).total_seconds() * 1000)

# Log audit entry
audit_handler = get_skill_handler_path("audit.log")
subprocess.run([
    sys.executable,
    audit_handler,
    skill_name,
    "success" if result["returncode"] == 0 else "failed",
    str(duration_ms),
    json.dumps(result.get("errors", []))
])
```

### Registry Updates

Log registry changes:

```python
# After successful registry update
subprocess.run([
    sys.executable,
    audit_handler,
    "registry.update",
    "success",
    "",
    "[]",
    json.dumps({"skill": skill_name, "action": "update"})
])
```

## Thread Safety

The `audit.log` skill uses thread-safe file operations with locking via `betty.file_utils.safe_update_json`. Multiple concurrent audit log writes are handled safely without data corruption.

## Error Handling

- Returns non-zero exit code on failures
- Logs errors to stderr via `betty.logging_utils`
- Provides detailed error messages in JSON response

## Response Format

### Success

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "/home/user/betty/registry/audit_log.json",
  "details": {
    "status": "success",
    "audit_entry": {
      "timestamp": "2025-10-23T12:34:56.789Z",
      "skill": "workflow.validate",
      "status": "success",
      "duration_ms": 150
    },
    "audit_log_path": "/home/user/betty/registry/audit_log.json",
    "total_entries": 42
  }
}
```

### Failure

```json
{
  "ok": false,
  "status": "failed",
  "errors": ["Failed to append audit entry: Permission denied"],
  "path": "/home/user/betty/registry/audit_log.json",
  "details": {
    "error": {
      "error": "SkillValidationError",
      "message": "Failed to append audit entry: Permission denied",
      "details": {}
    }
  }
}
```

## Dependencies

- `betty.config` - Registry directory configuration
- `betty.file_utils` - Thread-safe JSON updates
- `betty.logging_utils` - Logging infrastructure
- `betty.errors` - Error handling

## Permissions

- `filesystem` - Access to registry directory
- `write` - Write audit entries to log file

## Query and Analysis

The audit log can be queried using standard JSON tools:

```bash
# Count total entries
jq 'length' /home/user/betty/registry/audit_log.json

# Find failed executions
jq '.[] | select(.status == "failed")' /home/user/betty/registry/audit_log.json

# Get average duration for a skill
jq '[.[] | select(.skill == "workflow.compose") | .duration_ms] | add / length' /home/user/betty/registry/audit_log.json

# Get entries from last hour
jq --arg cutoff "$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S)" \
   '.[] | select(.timestamp > $cutoff)' /home/user/betty/registry/audit_log.json
```
