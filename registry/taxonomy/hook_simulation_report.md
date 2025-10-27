# Hook Simulation Report

Generated: 2025-10-27T02:12:23.909560

## Summary

- **Total Hooks**: 3
- **Events Simulated**: 4
- **Total Triggers**: 6
- **Successful Executions**: 6
- **Failed Conditions**: 0
- **Disabled Hooks**: 0
- **Dependencies Found**: 16
- **Potential Issues**: 2

## Hooks Overview

| Hook | Event | Enabled | Has Condition | Has Filter | Timeout |
|------|-------|---------|---------------|------------|---------|
| `performance-monitor-pre` | before-tool-call | ✓ | ✗ | ✗ | 5000ms |
| `performance-monitor-post` | after-tool-call | ✓ | ✗ | ✗ | 0ms |
| `auto-stage-edited-files` | after-tool-call | ✓ | ✗ | ✓ | 5000ms |

## Simulation Results

### performance-monitor-pre

**Event**: `before-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_NAME
  - File write: ~/.claude/performance.csv

**Event**: `before-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_NAME
  - File write: ~/.claude/performance.csv

### performance-monitor-post

**Event**: `after-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_NAME
  - File write: ~/.claude/performance.csv
- ⚠️ Potential Issues:
  - Destructive file operation

**Event**: `after-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_NAME
  - File write: ~/.claude/performance.csv
- ⚠️ Potential Issues:
  - Destructive file operation

### auto-stage-edited-files

**Event**: `after-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_FILE_PATH
  - Env var: $CLAUDE_TOOL_FILE_PATH
  - Git repository
  - File write: /dev/null

**Event**: `after-tool-call` - ✅ Would Execute
- Reason: Would execute successfully
- Dependencies:
  - Env var: $CLAUDE_TOOL_FILE_PATH
  - Env var: $CLAUDE_TOOL_FILE_PATH
  - Git repository
  - File write: /dev/null
