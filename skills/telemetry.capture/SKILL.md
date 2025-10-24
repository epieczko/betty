# telemetry.capture

**Version:** 0.1.0
**Status:** Active
**Tags:** telemetry, logging, observability, audit

## Overview

The `telemetry.capture` skill provides comprehensive execution logging for Betty Framework components. It captures usage metrics, execution status, timing data, and contextual metadata in a structured, thread-safe manner.

All telemetry data is written to `/registry/telemetry.json` with ISO timestamps and validated JSON schema.

## Features

- Thread-safe JSON logging using file locking (fcntl)
- ISO 8601 timestamp formatting with timezone support
- Structured telemetry entries with validation
- Query interface for telemetry analysis
- Decorator pattern for automatic capture (`@capture_telemetry`)
- Context manager pattern for manual capture
- CLI and programmatic interfaces
- Input sanitization (exclude secrets)

## Purpose

This skill enables:
- **Observability**: Track execution patterns across Betty components
- **Performance Monitoring**: Measure duration of skill executions
- **Error Tracking**: Capture failures with detailed error messages
- **Usage Analytics**: Understand which skills are used most frequently
- **Audit Trail**: Maintain compliance and debugging history
- **Workflow Analysis**: Trace caller chains and dependencies

## Usage

### Basic CLI Usage

```bash
# Capture a successful execution
python skills/telemetry.capture/telemetry_capture.py plugin.build success 320 CLI

# Capture with inputs
python skills/telemetry.capture/telemetry_capture.py \
  agent.run success 1500 API '{"agent": "api.designer", "task": "design_api"}'

# Capture a failure
python skills/telemetry.capture/telemetry_capture.py \
  workflow.compose failure 2800 CLI '{"workflow": "api_first"}' "Validation failed at step 3"
```

### As a Decorator (Recommended)

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "../telemetry.capture"))

from telemetry_utils import capture_telemetry

@capture_telemetry(skill_name="agent.run", caller="CLI", capture_inputs=True)
def run_agent(agent_path: str, task_context: str = None):
    """Execute a Betty agent."""
    # ... implementation
    return {"status": "success", "result": execution_result}

# Usage
result = run_agent("/agents/api.designer", "Design user authentication API")
# Telemetry is automatically captured
```

### As a Context Manager

```python
from telemetry_utils import TelemetryContext

def build_plugin(plugin_path: str):
    with TelemetryContext(skill="plugin.build", caller="CLI") as ctx:
        ctx.set_inputs({"plugin_path": plugin_path})
        
        try:
            # Perform build operations
            result = create_plugin_archive(plugin_path)
            ctx.set_status("success")
            return result
        except Exception as e:
            ctx.set_error(str(e))
            raise
```

### Programmatic API

```python
from telemetry_capture import TelemetryCapture

telemetry = TelemetryCapture()

# Capture an event
entry = telemetry.capture(
    skill="plugin.build",
    status="success",
    duration_ms=320.5,
    caller="CLI",
    inputs={"plugin_path": "./plugin.yaml", "output_format": "tar.gz"},
    metadata={"user": "developer@example.com", "environment": "production"}
)

print(f"Captured: {entry['timestamp']}")
```

### Query Telemetry Data

```python
from telemetry_capture import TelemetryCapture

telemetry = TelemetryCapture()

# Query recent failures
failures = telemetry.query(status="failure", limit=10)

# Query specific skill usage
agent_runs = telemetry.query(skill="agent.run", limit=50)

# Query by caller
cli_executions = telemetry.query(caller="CLI", limit=100)

for entry in failures:
    print(f"{entry['timestamp']}: {entry['skill']} - {entry['error_message']}")
```

## Parameters

### Capture Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `skill` | string | Yes | Name of the skill/component (e.g., 'plugin.build') |
| `status` | string | Yes | Execution status: success, failure, timeout, error, pending |
| `duration_ms` | number | Yes | Execution duration in milliseconds |
| `caller` | string | Yes | Source of the call (CLI, API, workflow.compose) |
| `inputs` | object | No | Sanitized input parameters (default: {}) |
| `error_message` | string | No | Error message if status is failure/error |
| `metadata` | object | No | Additional context (user, session_id, environment) |

### Decorator Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `skill_name` | string | function name | Override skill name |
| `caller` | string | "runtime" | Caller identifier |
| `capture_inputs` | boolean | False | Whether to capture function arguments |
| `sanitize_keys` | list | None | Parameter names to redact (e.g., ['password']) |

## Output Format

### Telemetry Entry Structure

```json
{
  "timestamp": "2025-10-24T14:30:45.123456+00:00",
  "skill": "plugin.build",
  "status": "success",
  "duration_ms": 320.5,
  "caller": "CLI",
  "inputs": {
    "plugin_path": "./plugin.yaml",
    "output_format": "tar.gz"
  },
  "error_message": null,
  "metadata": {
    "user": "developer@example.com",
    "environment": "production"
  }
}
```

### Telemetry File Structure

```json
[
  {
    "timestamp": "2025-10-24T14:30:45.123456+00:00",
    "skill": "plugin.build",
    "status": "success",
    "duration_ms": 320.5,
    "caller": "CLI",
    "inputs": {
      "plugin_path": "./plugin.yaml",
      "output_format": "tar.gz"
    },
    "error_message": null,
    "metadata": {}
  },
  {
    "timestamp": "2025-10-24T14:32:10.789012+00:00",
    "skill": "agent.run",
    "status": "success",
    "duration_ms": 1500.0,
    "caller": "API",
    "inputs": {
      "agent": "api.designer"
    },
    "error_message": null,
    "metadata": {}
  }
]
```

Note: The telemetry file is a simple JSON array for efficient querying and compatibility with existing Betty Framework tools.

## Examples

### Example 1: Capture Plugin Build

```bash
python skills/telemetry.capture/telemetry_capture.py \
  plugin.build success 320 CLI '{"plugin_path": "./plugin.yaml", "output_format": "tar.gz"}'
```

**Output:**
```json
{
  "timestamp": "2025-10-24T14:30:45.123456+00:00",
  "skill": "plugin.build",
  "status": "success",
  "duration_ms": 320.0,
  "caller": "CLI",
  "inputs": {
    "plugin_path": "./plugin.yaml",
    "output_format": "tar.gz"
  },
  "error_message": null,
  "metadata": {}
}

✓ Telemetry captured to /home/user/betty/registry/telemetry.json
```

### Example 2: Capture Agent Execution with Decorator

```python
# In skills/agent.run/agent_run.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "../telemetry.capture"))

from telemetry_utils import capture_telemetry

@capture_telemetry(
    skill_name="agent.run",
    caller="CLI",
    capture_inputs=True,
    sanitize_keys=["api_key", "password"]
)
def main():
    """Execute agent with automatic telemetry capture."""
    # ... existing implementation
    return {"status": "success", "result": result}

if __name__ == "__main__":
    main()
```

### Example 3: Query Recent Failures

```python
from telemetry_capture import TelemetryCapture

telemetry = TelemetryCapture()
failures = telemetry.query(status="failure", limit=10)

print("Recent Failures:")
for entry in failures:
    print(f"  [{entry['timestamp']}] {entry['skill']}")
    print(f"    Error: {entry['error_message']}")
    print(f"    Duration: {entry['duration_ms']}ms")
    print()
```

## Error Handling

### Invalid Status Value

```python
# Raises ValueError
telemetry.capture(
    skill="test.skill",
    status="invalid_status",  # Must be: success, failure, timeout, error, pending
    duration_ms=100,
    caller="CLI"
)
```

**Error:** `ValueError: Invalid status: invalid_status. Must be one of: success, failure, timeout, error, pending`

### Malformed Input JSON (CLI)

```bash
python skills/telemetry.capture/telemetry_capture.py \
  plugin.build success 320 CLI '{invalid json}'
```

**Error:** `Error: Invalid JSON for inputs: Expecting property name enclosed in double quotes`

### File Locking Contention

The implementation uses `fcntl.flock` for thread-safe writes. If multiple processes write simultaneously:
- Writes are serialized automatically
- No data loss occurs
- Performance may degrade under heavy contention

## Dependencies

This skill has no external dependencies beyond Python standard library:
- `json` - JSON parsing and serialization
- `fcntl` - File locking for thread safety
- `datetime` - ISO 8601 timestamp generation
- `pathlib` - Path handling
- `typing` - Type annotations

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `BETTY_TELEMETRY_FILE` | `/home/user/betty/registry/telemetry.json` | Path to telemetry file |

### Custom Telemetry File

```python
from telemetry_capture import TelemetryCapture

# Use custom location
telemetry = TelemetryCapture(telemetry_file="/custom/path/telemetry.json")
```

## Troubleshooting

### Q: Telemetry file doesn't exist

**A:** The skill automatically creates the telemetry file on first use. Ensure:
- The parent directory exists or can be created
- Write permissions are granted
- Path is absolute or correctly relative

### Q: Decorator not capturing telemetry

**A:** Ensure you:
1. Import the decorator correctly
2. Add the parent path to sys.path if needed
3. Check that the decorated function completes (doesn't hang)
4. Verify file permissions on `/registry/telemetry.json`

### Q: How to exclude sensitive data?

**A:** Use `sanitize_keys` parameter:

```python
@capture_telemetry(
    skill_name="auth.login",
    capture_inputs=True,
    sanitize_keys=["password", "api_key", "secret_token"]
)
def login(username: str, password: str):
    # password will be redacted as "***REDACTED***"
    pass
```

### Q: Performance impact of telemetry?

**A:** Minimal impact:
- Decorator adds <1ms overhead per call
- File I/O is buffered and atomic
- No network calls
- Consider async writes for high-throughput scenarios

## Integration with Betty Framework

The `telemetry.capture` skill integrates with:

- **agent.run**: Logs agent executions with task context
- **workflow.compose**: Traces multi-step workflow chains
- **plugin.build**: Monitors build performance
- **api.define**: Tracks API creation events
- **skill.define**: Captures skill registration
- **audit.log**: Complements audit trail with performance metrics

All core Betty components should use the `@capture_telemetry` decorator for consistent observability.

## License

Part of the Betty Framework. See repository LICENSE.
