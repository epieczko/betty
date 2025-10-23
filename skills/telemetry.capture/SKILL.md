# telemetry.capture

## Overview

The `telemetry.capture` skill provides comprehensive runtime telemetry tracking for the Betty Framework. It captures detailed metrics about skill usage across workflows, agents, and CLI executions, enabling performance monitoring, usage analytics, and operational insights.

## Purpose

Track skill execution metrics with full context to enable:
- Performance monitoring and optimization
- Usage analytics across workflows and agents
- Runtime behavior analysis
- Future integration with observability platforms (Grafana, Prometheus)

## Telemetry Entry Format

Each telemetry entry contains:

```json
{
  "timestamp": "2025-10-23T12:34:56.789Z",
  "skill": "workflow.compose",
  "inputs": {
    "workflow_path": "example.yaml",
    "strict_mode": true
  },
  "status": "success",
  "duration_ms": 1234,
  "agent": "workflow-orchestrator",
  "workflow": "deployment-pipeline",
  "caller": "cli"
}
```

### Fields

- **timestamp** (required): ISO 8601 UTC timestamp of when the skill was executed
- **skill** (required): Name of the skill that was executed
- **inputs** (required): JSON object containing input parameters passed to the skill
- **status** (required): Execution status (success, failed, timeout, etc.)
- **duration_ms** (required): Execution duration in milliseconds
- **agent** (optional): Name of the agent that invoked the skill
- **workflow** (optional): Name of the workflow in which the skill was executed
- **caller** (optional): Caller identifier (CLI, API, workflow, agent, etc.)

## Usage

### Command Line

```bash
python telemetry_capture.py <skill_name> <inputs_json> <status> <duration_ms> [agent] [workflow] [caller]
```

### Examples

#### Basic Telemetry Capture

```bash
python telemetry_capture.py "workflow.validate" '{"path": "test.yaml"}' "success" 150
```

#### Capture with Agent Context

```bash
python telemetry_capture.py "skill.create" '{"name": "new.skill"}' "success" 2500 "skill-generator" "" "cli"
```

#### Capture from Workflow Execution

```bash
python telemetry_capture.py "policy.enforce" '{"policy": "naming"}' "failed" 450 "" "validation-pipeline" "workflow"
```

#### Complete Context

```bash
python telemetry_capture.py \
  "agent.define" \
  '{"name": "test-agent", "mode": "iterative"}' \
  "success" \
  3200 \
  "meta-orchestrator" \
  "agent-creation-workflow" \
  "api"
```

### From Python Code

#### Direct Function Call

```python
from skills.telemetry.capture.telemetry_capture import create_telemetry_entry, capture_telemetry

# Create and capture telemetry
entry = create_telemetry_entry(
    skill_name="my.skill",
    inputs={"param1": "value1", "param2": 42},
    status="success",
    duration_ms=1234,
    agent="my-agent",
    workflow="my-workflow",
    caller="cli"
)

result = capture_telemetry(entry)
print(f"Captured to: {result['telemetry_path']}")
```

#### Using the Decorator

The skill provides a `@telemetry_decorator` for automatic telemetry capture:

```python
from skills.telemetry.capture.telemetry_capture import telemetry_decorator

@telemetry_decorator(skill_name="my.custom.skill", caller="cli")
def my_skill_function(arg1, arg2):
    # Your skill logic here
    return result

# Telemetry is automatically captured on each call
result = my_skill_function("test", 42)
```

The decorator:
- Automatically captures execution time
- Records success/failure status
- Sanitizes inputs (captures arg count and kwarg keys, not actual values)
- Non-blocking (errors in telemetry don't affect the main function)

### CLI Integration Example

```python
import subprocess
import json
import time

# Track CLI command execution
start_time = time.time()
result = subprocess.run(["betty", "skill", "validate", "test.yaml"], capture_output=True)
duration_ms = int((time.time() - start_time) * 1000)

# Capture telemetry
subprocess.run([
    sys.executable,
    "skills/telemetry.capture/telemetry_capture.py",
    "skill.validate",
    json.dumps({"path": "test.yaml"}),
    "success" if result.returncode == 0 else "failed",
    str(duration_ms),
    "",  # no agent
    "",  # no workflow
    "cli"
])
```

## Telemetry Data File

### Location

`/home/user/betty/registry/telemetry.json`

### Structure

The telemetry file is a JSON array of entries ordered by timestamp:

```json
[
  {
    "timestamp": "2025-10-23T12:30:00.000Z",
    "skill": "workflow.validate",
    "inputs": {"path": "test.yaml"},
    "status": "success",
    "duration_ms": 150,
    "caller": "cli"
  },
  {
    "timestamp": "2025-10-23T12:31:00.000Z",
    "skill": "agent.define",
    "inputs": {"name": "new-agent", "mode": "iterative"},
    "status": "success",
    "duration_ms": 2500,
    "agent": "orchestrator",
    "workflow": "setup-pipeline",
    "caller": "workflow"
  }
]
```

### Retention Policy

The telemetry log automatically retains only the last **100,000 entries** to prevent unbounded growth. Older entries are automatically removed when the limit is exceeded.

## Integration Points

### Workflow Execution Tracking

```python
# In workflow executor
start_time = time.time()
result = execute_step(step_name, step_config)
duration_ms = int((time.time() - start_time) * 1000)

# Capture telemetry
from skills.telemetry.capture.telemetry_capture import create_telemetry_entry, capture_telemetry

entry = create_telemetry_entry(
    skill_name=step_config.get('skill'),
    inputs=step_config.get('inputs', {}),
    status="success" if result.get('ok') else "failed",
    duration_ms=duration_ms,
    workflow=workflow_name,
    caller="workflow"
)
capture_telemetry(entry)
```

### Agent Skill Invocation

```python
# In agent skill runner
@telemetry_decorator(skill_name=skill_name, caller="agent")
def run_agent_skill(skill_name: str, **kwargs):
    # Execute skill
    return execute_skill(skill_name, **kwargs)
```

### CLI Commands

Apply the decorator to CLI entrypoints:

```python
from skills.telemetry.capture.telemetry_capture import telemetry_decorator

@telemetry_decorator(skill_name="skill.register", caller="cli")
def register_skill_cli(skill_path: str):
    # CLI logic
    return register_skill(skill_path)
```

## Thread Safety

The `telemetry.capture` skill uses thread-safe file operations with locking via `betty.file_utils.safe_update_json`. Multiple concurrent telemetry writes are handled safely without data corruption.

## Error Handling

- Returns non-zero exit code on failures
- Logs errors to stderr via `betty.logging_utils`
- Provides detailed error messages in JSON response
- Decorator mode: telemetry failures are logged but don't interrupt the main function

## Response Format

### Success

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "/home/user/betty/registry/telemetry.json",
  "details": {
    "status": "success",
    "telemetry_entry": {
      "timestamp": "2025-10-23T12:34:56.789Z",
      "skill": "workflow.validate",
      "inputs": {"path": "test.yaml"},
      "status": "success",
      "duration_ms": 150,
      "caller": "cli"
    },
    "telemetry_path": "/home/user/betty/registry/telemetry.json",
    "total_entries": 1523
  }
}
```

### Failure

```json
{
  "ok": false,
  "status": "failed",
  "errors": ["Invalid inputs JSON: not a valid json"],
  "path": "",
  "details": {
    "error": {
      "error": "ValueError",
      "message": "Invalid inputs JSON: not a valid json"
    }
  }
}
```

## Analytics and Querying

The telemetry data can be analyzed using standard JSON tools:

```bash
# Count total telemetry entries
jq 'length' registry/telemetry.json

# Find all failed executions
jq '.[] | select(.status == "failed")' registry/telemetry.json

# Get average duration for a specific skill
jq '[.[] | select(.skill == "workflow.compose") | .duration_ms] | add / length' registry/telemetry.json

# Top 10 slowest skill executions
jq 'sort_by(.duration_ms) | reverse | .[0:10]' registry/telemetry.json

# Count executions by caller
jq 'group_by(.caller) | map({caller: .[0].caller, count: length})' registry/telemetry.json

# Entries from specific workflow
jq '.[] | select(.workflow == "deployment-pipeline")' registry/telemetry.json

# Skills executed by specific agent
jq '.[] | select(.agent == "orchestrator")' registry/telemetry.json

# Get entries from last hour
jq --arg cutoff "$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S)" \
   '.[] | select(.timestamp > $cutoff)' registry/telemetry.json
```

## Future Enhancements

### Prometheus Export

The telemetry data can be exported to Prometheus format:

```python
# Future implementation
from skills.telemetry.capture.exporters import PrometheusExporter

exporter = PrometheusExporter()
metrics = exporter.export_metrics()
# Expose on /metrics endpoint
```

### Grafana Dashboard

Create dashboards to visualize:
- Skill execution rates over time
- Average execution durations by skill
- Success/failure rates
- Workflow performance metrics
- Agent activity patterns

### Real-time Streaming

Future support for streaming telemetry to external systems:
- OpenTelemetry integration
- CloudWatch/Datadog export
- Custom webhook notifications

## Dependencies

- `betty.config` - Registry directory configuration
- `betty.file_utils` - Thread-safe JSON updates
- `betty.logging_utils` - Logging infrastructure
- `betty.errors` - Error handling

## Permissions

- `filesystem:read` - Access to registry directory
- `filesystem:write` - Write telemetry entries to log file

## Best Practices

1. **Sanitize Sensitive Inputs**: Don't capture passwords, tokens, or PII in the inputs field
2. **Use Meaningful Status Values**: Stick to standard values like "success", "failed", "timeout"
3. **Always Include Duration**: Performance tracking requires accurate timing
4. **Provide Context**: Use agent/workflow/caller fields when available
5. **Non-blocking Capture**: Use the decorator or handle exceptions to prevent telemetry from breaking main logic

## Comparison with audit.log

| Feature | telemetry.capture | audit.log |
|---------|------------------|-----------|
| Purpose | Performance & usage metrics | Compliance & audit trail |
| Required Fields | skill, inputs, status, duration | skill, status |
| Context Tracking | agent, workflow, caller | metadata (generic) |
| Retention | 100,000 entries | 10,000 entries |
| Focus | Runtime analytics | Governance & debugging |
| Decorator Support | Yes | No |

Both skills complement each other and can be used together for comprehensive observability.
