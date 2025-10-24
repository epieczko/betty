# Betty Framework - Utilities Module

This module contains utility functions and decorators for the Betty Framework.

## Telemetry Utils

### Auto-Injection Telemetry Decorator

The `capture_telemetry` decorator automatically instruments skill execution without requiring manual telemetry calls.

#### Features

- **Automatic timing**: Captures execution duration in milliseconds
- **Status detection**: Automatically determines success/failure from return values or exceptions
- **Caller detection**: Auto-detects execution context (CLI, workflow, agent, runtime)
- **Input capture**: Captures CLI arguments and function parameters
- **Sensitive data sanitization**: Automatically redacts passwords, tokens, API keys, etc.
- **Non-blocking**: Telemetry failures don't interrupt skill execution
- **Zero configuration**: Works out-of-the-box with sensible defaults

#### Usage

```python
from utils.telemetry_utils import capture_telemetry

# Basic usage - auto-detects skill name
@capture_telemetry()
def main():
    print("Running skill...")
    return 0

# Explicit skill name and caller
@capture_telemetry(skill_name="plugin.build", caller="cli")
def main():
    result = build_plugin()
    return result

# Workflow execution with auto-detection
@capture_telemetry(skill_name="workflow.step", detect_caller=True)
def execute_step():
    # BETTY_CALLER env var will be auto-detected
    return {"ok": True}
```

#### Captured Data

Each telemetry entry includes:

- `timestamp`: ISO 8601 timestamp with timezone
- `execution_id`: Unique UUID for tracing
- `skill`: Skill name
- `inputs`: Captured CLI arguments and function parameters
- `status`: Execution status (success, failed, error)
- `duration_ms`: Execution duration in milliseconds
- `caller`: Execution context (cli, workflow, agent, runtime)
- `exit_code`: Process exit code
- `error`: Error message (if applicable)
- `workflow`: Workflow name (if in workflow context)
- `agent`: Agent name (if in agent context)

#### Status Detection

The decorator intelligently determines execution status:

- **Integer return values**: 0 = success, non-zero = failed
- **Dict with 'ok' key**: `{'ok': True}` = success, `{'ok': False}` = failed
- **Dict with 'status' key**: `{'status': 'success'}` = success, `{'status': 'failed'}` = failed
- **sys.exit() calls**: exit(0) = success, exit(N) = failed
- **Exceptions**: Any exception = failed (error message captured)
- **Other return values**: Default to success

#### Environment Variables

The decorator respects these environment variables:

- `BETTY_CALLER`: Override caller detection (e.g., "workflow", "agent")
- `BETTY_WORKFLOW`: Name of the executing workflow
- `BETTY_AGENT`: Name of the executing agent
- `BETTY_EXECUTION_ID`: Parent execution ID for hierarchical tracing

#### Applied Skills

The decorator is currently applied to:

1. **agent.run** - Agent execution telemetry
2. **workflow.compose** - Workflow orchestration telemetry
3. **plugin.build** - Plugin build telemetry
4. **plugin.publish** - Plugin publication telemetry

#### Telemetry Storage

All telemetry entries are stored in:
```
/home/user/betty/registry/telemetry.json
```

The file maintains the last 100,000 entries and uses file locking for thread-safe concurrent writes.

#### Testing

Run the built-in tests:

```bash
python3 utils/telemetry_utils.py
```

This will create test telemetry entries and display the results.

#### Integration with Existing Telemetry

The decorator integrates seamlessly with Betty's existing telemetry infrastructure:

- Uses `betty.telemetry_capture.create_telemetry_entry()` for consistent schema
- Uses `betty.telemetry_capture._append_telemetry_entry()` for atomic writes
- Compatible with existing manual telemetry calls
- Can be combined with context managers for fine-grained tracking

#### Example Output

```json
{
  "timestamp": "2025-10-24T21:25:27.374353+00:00",
  "execution_id": "3393d60d-2473-41ea-b4e7-5cc3ad8dae66",
  "skill": "plugin.build",
  "inputs": {
    "cli_args": ["--help"]
  },
  "status": "success",
  "duration_ms": 4,
  "caller": "cli",
  "exit_code": 0
}
```

## Future Enhancements

Planned improvements:

- Automatic decorator injection via metaclasses or import hooks
- Performance profiling integration
- Distributed tracing support
- Telemetry aggregation and analytics
- Real-time telemetry streaming
