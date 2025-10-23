# Telemetry Integration Examples

This document provides practical examples of integrating telemetry tracking into Betty Framework CLI entrypoints, workflows, and agents.

## Quick Start

The Betty Framework provides two main approaches for telemetry integration:

1. **Decorator Pattern** - For CLI entrypoints with standard main() functions
2. **Manual Capture** - For workflows, agents, and custom integrations

## 1. Decorator Pattern (Recommended for CLI)

### Standard CLI with Return Code

For CLI entrypoints that return an exit code:

```python
#!/usr/bin/env python3
import sys
import os
from typing import Optional, List

# Ensure project root on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.logging_utils import setup_logger
from betty.telemetry_integration import telemetry_tracked

logger = setup_logger(__name__)

@telemetry_tracked(skill_name="my.skill", caller="cli")
def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    # Your skill logic here
    if not argv:
        logger.error("Missing required arguments")
        return 1

    # Process and return success
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

**What the decorator does:**
- Automatically measures execution time
- Captures success/failure based on return code (0 = success, non-zero = failed)
- Logs telemetry with sanitized inputs
- Non-blocking - telemetry failures don't affect the main function

### Example: workflow.validate Integration

The `workflow.validate` skill has been updated with telemetry tracking:

```python
# skills/workflow.validate/workflow_validate.py
from betty.telemetry_integration import telemetry_tracked

@telemetry_tracked(skill_name="workflow.validate", caller="cli")
def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    # ... existing validation logic ...
    return 0 if response["ok"] else 1
```

**Test it:**
```bash
python3 skills/workflow.validate/workflow_validate.py example.yaml
cat registry/telemetry.json
```

## 2. Manual Capture Pattern

### Direct Function Call

For programmatic telemetry capture:

```python
from skills.telemetry.capture.telemetry_capture import create_telemetry_entry, capture_telemetry
import time

# Track execution manually
start_time = time.time()
try:
    # Your logic here
    result = execute_my_skill(param1, param2)
    status = "success"
except Exception as e:
    status = "failed"
    raise
finally:
    duration_ms = int((time.time() - start_time) * 1000)

    entry = create_telemetry_entry(
        skill_name="my.skill",
        inputs={"param1": param1, "param2": param2},
        status=status,
        duration_ms=duration_ms,
        caller="api"
    )
    capture_telemetry(entry)
```

### Workflow Execution Tracking

For capturing telemetry within workflow execution:

```python
# In workflow.compose or similar workflow executor
from betty.telemetry_integration import track_skill_execution

def execute_workflow_step(step_config: dict, workflow_name: str):
    """Execute a workflow step with telemetry tracking."""

    skill_name = step_config["skill"]
    skill_args = step_config["args"]

    result = track_skill_execution(
        skill_name=skill_name,
        func=lambda: run_skill(skill_name, skill_args),
        inputs={"args": skill_args},
        workflow=workflow_name,
        caller="workflow"
    )

    return result
```

### Agent Skill Invocation

For tracking skills invoked by agents:

```python
# In agent skill runner
from betty.telemetry_integration import track_skill_execution

def run_agent_skill(agent_name: str, skill_name: str, **kwargs):
    """Run a skill on behalf of an agent with telemetry."""

    result = track_skill_execution(
        skill_name=skill_name,
        func=lambda: execute_skill(skill_name, **kwargs),
        inputs=kwargs,
        agent=agent_name,
        caller="agent"
    )

    return result
```

## 3. CLI Helper Function

For simple CLI telemetry without decorators:

```python
from betty.telemetry_integration import capture_cli_telemetry
import time

def main():
    start_time = time.time()
    status = "failed"

    try:
        # Your CLI logic
        process_command()
        status = "success"
        return 0
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1
    finally:
        duration_ms = int((time.time() - start_time) * 1000)
        capture_cli_telemetry(
            skill_name="my.skill",
            inputs={"cli_args": sys.argv[1:]},
            status=status,
            duration_ms=duration_ms,
            caller="cli"
        )
```

## 4. Context-Rich Telemetry

### Full Context Example

Capture comprehensive context for deep analytics:

```python
entry = create_telemetry_entry(
    skill_name="agent.define",
    inputs={
        "name": "my-agent",
        "mode": "iterative",
        "capabilities": ["code-gen", "testing"]
    },
    status="success",
    duration_ms=2500,
    agent="meta-orchestrator",           # Which agent invoked this
    workflow="agent-creation-pipeline",  # Which workflow this is part of
    caller="api",                        # How it was invoked

    # Custom fields for advanced analytics
    user_id="dev-123",
    environment="staging",
    version="1.0.0"
)

capture_telemetry(entry)
```

## 5. Batch Operations

For tracking multiple skill executions in batch:

```python
from skills.telemetry.capture.telemetry_capture import create_telemetry_entry, capture_telemetry
import time

def process_batch(items: list):
    """Process items in batch with per-item telemetry."""

    for item in items:
        start_time = time.time()

        try:
            process_item(item)
            status = "success"
        except Exception as e:
            status = "failed"

        duration_ms = int((time.time() - start_time) * 1000)

        # Capture telemetry for each item
        entry = create_telemetry_entry(
            skill_name="batch.processor",
            inputs={"item_id": item.id},
            status=status,
            duration_ms=duration_ms,
            caller="batch"
        )
        capture_telemetry(entry)
```

## 6. Error Handling Best Practices

### Graceful Telemetry Failures

Always wrap telemetry in try-except to prevent failures from affecting main logic:

```python
def my_critical_function():
    """Critical function that must not fail due to telemetry issues."""

    start_time = time.time()
    result = None

    try:
        # Critical business logic
        result = perform_critical_operation()
        status = "success"
    except Exception as e:
        status = "failed"
        raise  # Re-raise the original error
    finally:
        # Capture telemetry (failures are logged but don't interrupt)
        try:
            duration_ms = int((time.time() - start_time) * 1000)
            capture_cli_telemetry(
                skill_name="critical.operation",
                inputs={},
                status=status,
                duration_ms=duration_ms
            )
        except Exception as telemetry_error:
            logger.warning(f"Telemetry capture failed: {telemetry_error}")
            # Don't raise - telemetry is not critical

    return result
```

## 7. Sensitive Data Protection

### Sanitize Inputs

Never capture sensitive data like passwords, tokens, or PII:

```python
def sanitize_inputs(inputs: dict) -> dict:
    """Remove sensitive fields from inputs before logging."""

    sensitive_keys = ["password", "token", "api_key", "secret", "ssn", "credit_card"]

    sanitized = {}
    for key, value in inputs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            sanitized[key] = "***REDACTED***"
        else:
            sanitized[key] = value

    return sanitized

# Use it
entry = create_telemetry_entry(
    skill_name="auth.login",
    inputs=sanitize_inputs({"username": "john", "password": "secret123"}),
    status="success",
    duration_ms=150
)
```

## 8. Testing with Telemetry

### Unit Test Example

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMySkillWithTelemetry(unittest.TestCase):

    @patch('betty.telemetry_integration.capture_cli_telemetry')
    def test_skill_execution_captures_telemetry(self, mock_capture):
        """Test that telemetry is captured on skill execution."""

        # Execute the skill
        from skills.my.skill.my_skill import main
        result = main(["arg1", "arg2"])

        # Verify telemetry was captured
        self.assertEqual(result, 0)
        mock_capture.assert_called_once()

        # Verify telemetry parameters
        call_args = mock_capture.call_args
        self.assertEqual(call_args.kwargs['skill_name'], "my.skill")
        self.assertEqual(call_args.kwargs['status'], "success")
        self.assertGreater(call_args.kwargs['duration_ms'], 0)
```

## 9. Migration Checklist

To add telemetry to an existing skill:

1. **Import the telemetry integration:**
   ```python
   from betty.telemetry_integration import telemetry_tracked
   ```

2. **Apply the decorator to main():**
   ```python
   @telemetry_tracked(skill_name="your.skill", caller="cli")
   def main(argv: Optional[List[str]] = None) -> int:
   ```

3. **Ensure main() returns an int:**
   - Return 0 for success
   - Return non-zero for failure

4. **Test the integration:**
   ```bash
   python3 skills/your.skill/your_skill.py test-args
   cat registry/telemetry.json | jq '.[-1]'  # View latest entry
   ```

## 10. Querying Telemetry Data

### Basic Queries

```bash
# Count total telemetry entries
jq 'length' registry/telemetry.json

# Find all failed executions
jq '.[] | select(.status == "failed")' registry/telemetry.json

# Get average duration for a skill
jq '[.[] | select(.skill == "workflow.validate") | .duration_ms] | add / length' registry/telemetry.json

# Top 10 slowest executions
jq 'sort_by(.duration_ms) | reverse | .[0:10]' registry/telemetry.json

# Executions by caller
jq 'group_by(.caller) | map({caller: .[0].caller, count: length})' registry/telemetry.json
```

### Advanced Analytics

```bash
# Skills executed in last hour
jq --arg cutoff "$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S)" \
   '.[] | select(.timestamp > $cutoff)' registry/telemetry.json

# Success rate by skill
jq 'group_by(.skill) | map({
    skill: .[0].skill,
    total: length,
    successful: ([.[] | select(.status == "success")] | length),
    success_rate: (([.[] | select(.status == "success")] | length) / length * 100)
})' registry/telemetry.json
```

## 11. Future: Prometheus Export

Example of how telemetry data could be exported to Prometheus (future implementation):

```python
# Future: skills/telemetry.capture/exporters/prometheus.py
from prometheus_client import Counter, Histogram, Gauge

skill_executions = Counter(
    'betty_skill_executions_total',
    'Total skill executions',
    ['skill', 'status', 'caller']
)

skill_duration = Histogram(
    'betty_skill_duration_seconds',
    'Skill execution duration',
    ['skill', 'caller']
)

def export_to_prometheus(telemetry_entry: dict):
    """Export telemetry entry to Prometheus metrics."""
    skill_executions.labels(
        skill=telemetry_entry['skill'],
        status=telemetry_entry['status'],
        caller=telemetry_entry.get('caller', 'unknown')
    ).inc()

    skill_duration.labels(
        skill=telemetry_entry['skill'],
        caller=telemetry_entry.get('caller', 'unknown')
    ).observe(telemetry_entry['duration_ms'] / 1000.0)
```

## Summary

- **CLI Skills**: Use `@telemetry_tracked` decorator
- **Workflows**: Use `track_skill_execution()` helper
- **Custom Code**: Use `create_telemetry_entry()` + `capture_telemetry()`
- **Always**: Handle telemetry failures gracefully
- **Never**: Capture sensitive data in inputs

For more details, see the [SKILL.md](SKILL.md) documentation.
