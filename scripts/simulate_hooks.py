#!/usr/bin/env python3
"""
Hook Simulation Script
Simulates hook execution to verify triggers and dependencies
"""

import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

BASE_DIR = Path("/home/user/betty")
HOOKS_FILE = BASE_DIR / ".claude" / "hooks.yaml"
OUTPUT_DIR = BASE_DIR / "registry" / "taxonomy"

# Simulated events for testing
SIMULATION_EVENTS = [
    {
        "event": "before-tool-call",
        "context": {
            "tool": "Edit",
            "file_path": "/home/user/betty/test.py",
            "timestamp": "2025-10-26T23:00:00Z"
        }
    },
    {
        "event": "after-tool-call",
        "context": {
            "tool": "Edit",
            "file_path": "/home/user/betty/test.py",
            "timestamp": "2025-10-26T23:00:01Z"
        }
    },
    {
        "event": "before-tool-call",
        "context": {
            "tool": "Write",
            "file_path": "/home/user/betty/new_file.py",
            "timestamp": "2025-10-26T23:00:02Z"
        }
    },
    {
        "event": "after-tool-call",
        "context": {
            "tool": "Write",
            "file_path": "/home/user/betty/new_file.py",
            "timestamp": "2025-10-26T23:00:03Z"
        }
    }
]


def load_hooks() -> List[Dict[str, Any]]:
    """Load hooks from hooks.yaml"""
    try:
        with open(HOOKS_FILE, 'r') as f:
            data = yaml.safe_load(f)
            return data.get("hooks", [])
    except Exception as e:
        print(f"Error loading hooks: {e}")
        return []


def simulate_hook(hook: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    """Simulate a single hook execution"""
    result = {
        "hook_name": hook.get("name", "unknown"),
        "event_type": event["event"],
        "triggered": False,
        "would_execute": False,
        "command": hook.get("command", ""),
        "reason": "",
        "dependencies": [],
        "potential_issues": []
    }

    # Check if hook is enabled
    if not hook.get("enabled", True):
        result["reason"] = "Hook is disabled"
        return result

    # Check if event matches
    hook_event = hook.get("event", "")
    if hook_event != event["event"]:
        result["reason"] = f"Event mismatch: expected '{hook_event}', got '{event['event']}'"
        return result

    result["triggered"] = True

    # Check tool filter
    tool_filter = hook.get("tool_filter", "")
    if tool_filter:
        tool = event["context"].get("tool", "")
        # Simple regex match
        if not re.search(tool_filter, tool):
            result["reason"] = f"Tool filter '{tool_filter}' does not match '{tool}'"
            return result

    # Check condition (if any)
    condition = hook.get("condition", "")
    if condition:
        result["dependencies"].append(f"Condition check: {condition}")

    result["would_execute"] = True

    # Analyze command for dependencies
    command = hook.get("command", "")

    # Check for environment variables
    env_vars = re.findall(r'\$\{?(\w+)\}?', command)
    if env_vars:
        result["dependencies"].extend([f"Env var: ${var}" for var in env_vars])

    # Check for file operations
    if "git add" in command:
        result["dependencies"].append("Git repository")
    if ">>" in command or ">" in command:
        file_match = re.search(r'>>?\s*([^\s;]+)', command)
        if file_match:
            result["dependencies"].append(f"File write: {file_match.group(1)}")

    # Check for potential issues
    if "rm " in command or "mv " in command:
        result["potential_issues"].append("Destructive file operation")

    if not command.strip():
        result["potential_issues"].append("Empty command")

    timeout = hook.get("timeout", 0)
    if timeout > 10000:
        result["potential_issues"].append(f"Long timeout: {timeout}ms")

    result["reason"] = "Would execute successfully"
    return result


def run_simulation() -> Dict[str, Any]:
    """Run complete hook simulation"""
    print("🪝 Running Hook Simulation")
    print("=" * 60)

    hooks = load_hooks()
    print(f"Loaded {len(hooks)} hooks\n")

    simulation_results = {
        "simulation_time": datetime.now().isoformat(),
        "total_hooks": len(hooks),
        "total_events": len(SIMULATION_EVENTS),
        "results": [],
        "summary": {
            "total_triggers": 0,
            "successful_executions": 0,
            "failed_conditions": 0,
            "disabled_hooks": 0,
            "total_dependencies": 0,
            "potential_issues": 0
        },
        "hooks_overview": []
    }

    # Simulate each event
    for event in SIMULATION_EVENTS:
        print(f"📍 Simulating event: {event['event']}")

        for hook in hooks:
            result = simulate_hook(hook, event)

            if result["triggered"] or result["would_execute"]:
                print(f"  → Hook '{result['hook_name']}': {result['reason']}")
                simulation_results["results"].append(result)

                if result["triggered"]:
                    simulation_results["summary"]["total_triggers"] += 1

                if result["would_execute"]:
                    simulation_results["summary"]["successful_executions"] += 1
                else:
                    simulation_results["summary"]["failed_conditions"] += 1

                simulation_results["summary"]["total_dependencies"] += len(result["dependencies"])
                simulation_results["summary"]["potential_issues"] += len(result["potential_issues"])

        print()

    # Count disabled hooks
    disabled = sum(1 for h in hooks if not h.get("enabled", True))
    simulation_results["summary"]["disabled_hooks"] = disabled

    # Create hooks overview
    for hook in hooks:
        overview = {
            "name": hook.get("name", ""),
            "event": hook.get("event", ""),
            "enabled": hook.get("enabled", True),
            "has_condition": bool(hook.get("condition", "")),
            "has_tool_filter": bool(hook.get("tool_filter", "")),
            "timeout": hook.get("timeout", 0),
            "command_length": len(hook.get("command", ""))
        }
        simulation_results["hooks_overview"].append(overview)

    return simulation_results


def generate_report(results: Dict[str, Any]):
    """Generate simulation report"""
    print("📊 Simulation Summary")
    print("=" * 60)
    print(f"Total Hooks: {results['total_hooks']}")
    print(f"Total Events Simulated: {results['total_events']}")
    print(f"Total Triggers: {results['summary']['total_triggers']}")
    print(f"Successful Executions: {results['summary']['successful_executions']}")
    print(f"Failed Conditions: {results['summary']['failed_conditions']}")
    print(f"Disabled Hooks: {results['summary']['disabled_hooks']}")
    print(f"Total Dependencies: {results['summary']['total_dependencies']}")
    print(f"Potential Issues: {results['summary']['potential_issues']}")

    # Save JSON report
    report_file = OUTPUT_DIR / "hook_simulation_report.json"
    with open(report_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Report saved to {report_file}")

    # Generate markdown report
    md_lines = ["# Hook Simulation Report", "", f"Generated: {results['simulation_time']}", ""]

    md_lines.extend([
        "## Summary",
        "",
        f"- **Total Hooks**: {results['total_hooks']}",
        f"- **Events Simulated**: {results['total_events']}",
        f"- **Total Triggers**: {results['summary']['total_triggers']}",
        f"- **Successful Executions**: {results['summary']['successful_executions']}",
        f"- **Failed Conditions**: {results['summary']['failed_conditions']}",
        f"- **Disabled Hooks**: {results['summary']['disabled_hooks']}",
        f"- **Dependencies Found**: {results['summary']['total_dependencies']}",
        f"- **Potential Issues**: {results['summary']['potential_issues']}",
        "",
        "## Hooks Overview",
        "",
        "| Hook | Event | Enabled | Has Condition | Has Filter | Timeout |",
        "|------|-------|---------|---------------|------------|---------|"
    ])

    for hook in results['hooks_overview']:
        enabled = "✓" if hook['enabled'] else "✗"
        condition = "✓" if hook['has_condition'] else "✗"
        filter_col = "✓" if hook['has_tool_filter'] else "✗"
        md_lines.append(
            f"| `{hook['name']}` | {hook['event']} | {enabled} | {condition} | {filter_col} | {hook['timeout']}ms |"
        )

    md_lines.extend(["", "## Simulation Results", ""])

    # Group results by hook
    hook_results = {}
    for result in results['results']:
        hook_name = result['hook_name']
        if hook_name not in hook_results:
            hook_results[hook_name] = []
        hook_results[hook_name].append(result)

    for hook_name, hook_res in hook_results.items():
        md_lines.append(f"### {hook_name}")
        md_lines.append("")

        for res in hook_res:
            status = "✅ Would Execute" if res['would_execute'] else "⚠️ Would Not Execute"
            md_lines.append(f"**Event**: `{res['event_type']}` - {status}")
            md_lines.append(f"- Reason: {res['reason']}")

            if res['dependencies']:
                md_lines.append("- Dependencies:")
                for dep in res['dependencies']:
                    md_lines.append(f"  - {dep}")

            if res['potential_issues']:
                md_lines.append("- ⚠️ Potential Issues:")
                for issue in res['potential_issues']:
                    md_lines.append(f"  - {issue}")

            md_lines.append("")

    md_file = OUTPUT_DIR / "hook_simulation_report.md"
    with open(md_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"📄 Markdown report saved to {md_file}")


if __name__ == "__main__":
    results = run_simulation()
    generate_report(results)
