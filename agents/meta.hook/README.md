# meta.hook - Hook Creator Meta-Agent

Generates Claude Code hooks from natural language descriptions.

## Overview

**meta.hook** is a meta-agent that creates Claude Code hooks from simple description files. It generates hook configurations that execute commands in response to events like tool calls, errors, or user interactions.

**What it does:**
- Parses hook descriptions (Markdown or JSON)
- Generates `.claude/hooks.yaml` configurations
- Validates event types and hook structure
- Manages hook lifecycle (create, update, enable/disable)
- Supports tool-specific filtering

## Quick Start

### Create a Hook

```bash
python3 agents/meta.hook/meta_hook.py examples/my_hook.md
```

Output:
```
🪝  meta.hook - Creating hook from examples/my_hook.md

✨ Hook 'pre-commit-lint' created successfully!

📄 Created/updated file:
   - .claude/hooks.yaml

✅ Hook 'pre-commit-lint' is ready to use
   Event: before-tool-call
   Command: npm run lint
```

### Hook Description Format

Create a Markdown file:

```markdown
# Name: pre-commit-lint

# Event: before-tool-call

# Tool Filter: git

# Description: Run linter before git commits

# Command: npm run lint

# Timeout: 30000

# Enabled: true
```

Or use JSON format:

```json
{
  "name": "pre-commit-lint",
  "event": "before-tool-call",
  "tool_filter": "git",
  "description": "Run linter before git commits",
  "command": "npm run lint",
  "timeout": 30000,
  "enabled": true
}
```

## Event Types

Supported Claude Code events:

- **before-tool-call** - Before any tool is executed
- **after-tool-call** - After any tool completes
- **on-error** - When a tool call fails
- **user-prompt-submit** - When user submits a prompt
- **assistant-response** - After assistant responds

## Generated Structure

meta.hook generates or updates `.claude/hooks.yaml`:

```yaml
hooks:
- name: pre-commit-lint
  event: before-tool-call
  command: npm run lint
  description: Run linter before git commits
  enabled: true
  tool_filter: git
  timeout: 30000
```

## Usage Examples

### Example 1: Pre-commit Linting

**Description file** (`lint_hook.md`):

```markdown
# Name: pre-commit-lint

# Event: before-tool-call

# Tool Filter: git

# Description: Run linter before git commits to ensure code quality

# Command: npm run lint

# Timeout: 30000
```

**Create hook:**

```bash
python3 agents/meta.hook/meta_hook.py lint_hook.md
```

### Example 2: Post-deployment Notification

**Description file** (`deploy_notify.json`):

```json
{
  "name": "deploy-notify",
  "event": "after-tool-call",
  "tool_filter": "deploy",
  "description": "Send notification after deployment",
  "command": "./scripts/notify-team.sh",
  "timeout": 10000
}
```

**Create hook:**

```bash
python3 agents/meta.hook/meta_hook.py deploy_notify.json
```

### Example 3: Error Logging

**Description file** (`error_logger.md`):

```markdown
# Name: error-logger

# Event: on-error

# Description: Log errors to monitoring system

# Command: ./scripts/log-error.sh "{error}" "{tool}"

# Timeout: 5000

# Enabled: true
```

**Create hook:**

```bash
python3 agents/meta.hook/meta_hook.py error_logger.md
```

## Hook Parameters

### Required

- **name** - Unique hook identifier
- **event** - Trigger event type
- **command** - Shell command to execute

### Optional

- **description** - What the hook does
- **tool_filter** - Only trigger for specific tools (e.g., "git", "npm", "docker")
- **enabled** - Whether hook is active (default: true)
- **timeout** - Command timeout in milliseconds (default: none)

## Tool Filters

Restrict hooks to specific tools:

```markdown
# Tool Filter: git
```

This hook only triggers for git-related tool calls.

Common tool filters:
- `git` - Git operations
- `npm` - NPM commands
- `docker` - Docker commands
- `python` - Python execution
- `bash` - Shell commands

## Managing Hooks

### Update Existing Hook

Run meta.hook with the same hook name to update:

```bash
python3 agents/meta.hook/meta_hook.py updated_hook.md
```

Output:
```
⚠️  Warning: Hook 'pre-commit-lint' already exists, updating...
✨ Hook 'pre-commit-lint' created successfully!
```

### Disable Hook

Set `Enabled: false` in description:

```markdown
# Name: my-hook
# Event: before-tool-call
# Command: echo "test"
# Enabled: false
```

### Multiple Hooks

Create multiple hook descriptions and run meta.hook for each:

```bash
for hook in hooks/*.md; do
    python3 agents/meta.hook/meta_hook.py "$hook"
done
```

## Integration

### With Claude Code

Hooks are automatically loaded by Claude Code from `.claude/hooks.yaml`.

### With meta.agent

Create agents that use hooks:

```yaml
name: ci.agent
description: Continuous integration agent
# Hooks will trigger during agent execution
```

## Artifact Types

### Consumes

- **hook-description** - Natural language hook requirements
  - Pattern: `**/hook_description.md`
  - Format: Markdown or JSON

### Produces

- **hook-config** - Claude Code hook configuration
  - Pattern: `.claude/hooks.yaml`
  - Schema: `schemas/hook-config.json`

## Common Workflows

### Workflow 1: Create and Test Hook

```bash
# 1. Create hook description
cat > my_hook.md <<EOF
# Name: test-runner
# Event: after-tool-call
# Tool Filter: git
# Description: Run tests after git push
# Command: npm test
EOF

# 2. Generate hook
python3 agents/meta.hook/meta_hook.py my_hook.md

# 3. Test hook (trigger the event)
git add .
git commit -m "test"
```

### Workflow 2: Create Pre-commit Workflow

```bash
# Create linting hook
cat > lint_hook.md <<EOF
# Name: lint
# Event: before-tool-call
# Tool Filter: git
# Command: npm run lint
EOF

python3 agents/meta.hook/meta_hook.py lint_hook.md

# Create test hook
cat > test_hook.md <<EOF
# Name: test
# Event: before-tool-call
# Tool Filter: git
# Command: npm test
EOF

python3 agents/meta.hook/meta_hook.py test_hook.md
```

### Workflow 3: Error Monitoring

```bash
# Create error notification hook
cat > error_notify.md <<EOF
# Name: error-notify
# Event: on-error
# Description: Send error notifications
# Command: ./scripts/notify.sh
# Timeout: 5000
EOF

python3 agents/meta.hook/meta_hook.py error_notify.md
```

## Tips & Best Practices

### Command Design

**Use absolute paths for scripts:**
```markdown
# Good
# Command: ./scripts/lint.sh

# Bad
# Command: lint.sh
```

**Set appropriate timeouts:**
```markdown
# Fast operations: 5-10 seconds
# Timeout: 10000

# Longer operations: 30-60 seconds
# Timeout: 60000
```

**Handle errors gracefully:**
```bash
#!/bin/bash
# In your hook script
set -e  # Exit on error
trap 'echo "Hook failed"' ERR
```

### Tool Filters

Be specific with tool filters to avoid unnecessary executions:

```markdown
# Specific
# Tool Filter: git

# Too broad
# (no tool filter - runs for ALL tools)
```

### Testing Hooks

Test hooks before enabling:

```markdown
# Enabled: false
```

Then manually test the command, and enable once verified.

## Troubleshooting

### Hook not triggering

**Check event type:**
```bash
# Verify event is correct in .claude/hooks.yaml
cat .claude/hooks.yaml
```

**Check tool filter:**
```markdown
# If using tool filter, ensure it matches the tool being called
# Tool Filter: git
```

### Command fails

**Check command path:**
```bash
# Test command manually
npm run lint

# If fails, fix path or installation
```

**Check timeout:**
```markdown
# Increase timeout for slow commands
# Timeout: 60000
```

### Hook already exists warning

This is normal when updating hooks. The old version is replaced with the new one.

## Architecture

```
meta.hook
    ├─ Input: hook-description (Markdown/JSON)
    ├─ Parser: extract name, event, command, filters
    ├─ Generator: create/update hooks.yaml
    ├─ Validator: check event types and structure
    └─ Output: .claude/hooks.yaml configuration
```

## Related Documentation

- [META_AGENTS.md](../../docs/META_AGENTS.md) - Meta-agent ecosystem
- [ARTIFACT_STANDARDS.md](../../docs/ARTIFACT_STANDARDS.md) - Artifact system
- [hook-description schema](../../schemas/hook-description.json)
- [hook-config schema](../../schemas/hook-config.json)

## How Claude Uses This

Claude can:
1. **Create hooks on demand** - "Create a pre-commit linting hook"
2. **Automate workflows** - "Add error logging for all failures"
3. **Build CI/CD pipelines** - "Create hooks for test, lint, and deploy"
4. **Monitor executions** - "Add notification hooks for important events"

meta.hook enables powerful event-driven automation in Claude Code!
