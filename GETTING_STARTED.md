# Getting Started with Betty Framework

A quick start guide to building your first agents, skills, and hooks with Betty.

## Table of Contents

- [Overview](#overview)
- [5-Minute Quick Start](#5-minute-quick-start)
- [Core Concepts](#core-concepts)
- [Your First Agent](#your-first-agent)
- [Your First Skill](#your-first-skill)
- [Your First Hook](#your-first-hook)
- [Working with Artifacts](#working-with-artifacts)
- [Multi-Agent Workflows](#multi-agent-workflows)
- [Next Steps](#next-steps)

## Overview

Betty Framework provides **6 meta-agents** that help you create and manage framework components:

| Meta-Agent | Creates | Purpose |
|------------|---------|---------|
| **meta.agent** (atum) | Agents | Build agents from descriptions |
| **meta.skill** | Skills | Generate skills from descriptions |
| **meta.hook** | Hooks | Create event-driven automation |
| **meta.artifact** | Artifact types | Define data standards |
| **meta.compatibility** | Compatibility graphs | Analyze agent relationships |
| **meta.suggest** | Suggestions | Get next-step recommendations |

## 5-Minute Quick Start

```bash
# 1. Create your first artifact type
cat > /tmp/my_artifact.md <<'EOF'
# Name: api-spec
# Purpose: OpenAPI specification documents
# Format: YAML
# File Pattern: *.openapi.yaml
# Producers: api.designer
# Consumers: api.validator
EOF

python3 agents/meta.artifact/meta_artifact.py create /tmp/my_artifact.md

# 2. Create your first agent
cat > /tmp/my_agent.md <<'EOF'
# Name: api.designer
# Purpose: Design REST API specifications
# Outputs:
- api-spec
EOF

python3 agents/atum/atum.py /tmp/my_agent.md

# 3. Verify it works
python3 agents/meta.compatibility/meta_compatibility.py analyze api.designer
```

**Congratulations!** You've created your first Betty components.

## Core Concepts

### 1. Artifacts

**Artifacts** are typed data that flows between agents and skills.

Examples:
- `openapi-spec` - API specifications
- `validation-report` - Validation results
- `agent-definition` - Agent configurations

### 2. Agents

**Agents** are intelligent components that consume and produce artifacts.

Example agent.yaml:
```yaml
name: api.validator
description: Validates OpenAPI specifications
artifact_metadata:
  consumes:
    - type: openapi-spec
  produces:
    - type: validation-report
```

### 3. Skills

**Skills** are reusable functions that agents can use.

Example skill.yaml:
```yaml
name: data.validatejson
description: Validates JSON files
permissions:
  - filesystem:read
artifact_metadata:
  produces:
    - type: validation-report
```

### 4. Hooks

**Hooks** are event-driven automations.

Example hooks.yaml:
```yaml
hooks:
  - name: pre-commit-lint
    event: before-tool-call
    tool_filter: git
    command: npm run lint
```

## Your First Agent

### Step 1: Write Agent Description

```bash
cat > examples/my_first_agent.md <<'EOF'
# Name: code.reviewer

# Purpose:
Reviews code changes and provides feedback on code quality,
security issues, and best practices.

# Inputs:
- code-diff
- coding-standards

# Outputs:
- review-report
- suggestion-list

# Skills Needed:
- static-analysis
- security-scan
- style-check

# Implementation Notes:
Analyze code changes for:
- Security vulnerabilities
- Code style violations
- Performance issues
- Best practice adherence
EOF
```

### Step 2: Generate Agent

```bash
python3 agents/atum/atum.py examples/my_first_agent.md
```

Output:
```
✨ Agent 'code.reviewer' created successfully!

📄 Created files:
   - agents/code.reviewer/agent.yaml
   - agents/code.reviewer/README.md

✅ Agent 'code.reviewer' is ready to use
```

### Step 3: Review Generated Files

```bash
# View agent configuration
cat agents/code.reviewer/agent.yaml

# Read documentation
cat agents/code.reviewer/README.md
```

### Step 4: Analyze Compatibility

```bash
# Find compatible agents
python3 agents/meta.compatibility/meta_compatibility.py find-compatible code.reviewer

# Get next-step suggestions
python3 agents/meta.suggest/meta_suggest.py suggest agents/code.reviewer/agent.yaml
```

## Your First Skill

### Step 1: Write Skill Description

```bash
cat > examples/my_first_skill.md <<'EOF'
# Name: file.compare

# Purpose:
Compare two files and generate a diff report

# Inputs:
- file_path_1
- file_path_2
- output_format (optional)

# Outputs:
- diff_report.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- diff-report

# Implementation Notes:
Use Python's difflib to compare files line by line.
Support multiple output formats (unified, context, HTML).
EOF
```

### Step 2: Generate Skill

```bash
python3 agents/meta.skill/meta_skill.py examples/my_first_skill.md
```

Output:
```
✨ Skill 'file.compare' created successfully!

📄 Created files:
   - skills/file.compare/skill.yaml
   - skills/file.compare/file_compare.py
   - skills/file.compare/test_file_compare.py
   - skills/file.compare/README.md
```

### Step 3: Implement Skill Logic

```bash
# Edit the generated implementation
vim skills/file.compare/file_compare.py
```

Add your logic to the `execute()` method:

```python
def execute(self, file_path_1: Optional[str] = None,
            file_path_2: Optional[str] = None,
            output_format: Optional[str] = None) -> Dict[str, Any]:
    """Execute the skill"""
    try:
        logger.info("Executing file.compare...")

        # Your implementation here
        import difflib

        with open(file_path_1, 'r') as f1:
            lines1 = f1.readlines()

        with open(file_path_2, 'r') as f2:
            lines2 = f2.readlines()

        diff = difflib.unified_diff(lines1, lines2,
                                    fromfile=file_path_1,
                                    tofile=file_path_2)

        diff_text = ''.join(diff)

        result = {
            "ok": True,
            "status": "success",
            "diff": diff_text,
            "files_compared": [file_path_1, file_path_2]
        }

        logger.info("Skill completed successfully")
        return result

    except Exception as e:
        logger.error(f"Error executing skill: {e}")
        return {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
```

### Step 4: Test Skill

```bash
# Run tests
pytest skills/file.compare/test_file_compare.py -v

# Test CLI
python3 skills/file.compare/file_compare.py \
  --file-path-1 file1.txt \
  --file-path-2 file2.txt \
  --output-format json
```

### Step 5: Add to Agent

```yaml
# In agents/code.reviewer/agent.yaml
skills_available:
  - file.compare
```

## Your First Hook

### Step 1: Write Hook Description

```bash
cat > examples/my_first_hook.md <<'EOF'
# Name: auto-test

# Event: before-tool-call

# Tool Filter: git

# Description: Run tests automatically before git commits

# Command: pytest tests/ -v

# Timeout: 60000

# Enabled: true
EOF
```

### Step 2: Generate Hook

```bash
python3 agents/meta.hook/meta_hook.py examples/my_first_hook.md
```

Output:
```
✨ Hook 'auto-test' created successfully!

📄 Created/updated file:
   - .claude/hooks.yaml

✅ Hook 'auto-test' is ready to use
   Event: before-tool-call
   Command: pytest tests/ -v
```

### Step 3: Test Hook

```bash
# View generated hook
cat .claude/hooks.yaml

# Trigger hook (make a git commit)
git add .
git commit -m "test"  # Hook runs pytest before commit
```

### Step 4: Manage Hooks

```bash
# Disable hook temporarily
# Edit .claude/hooks.yaml and set:
# enabled: false

# Update hook
python3 agents/meta.hook/meta_hook.py examples/updated_hook.md
```

## Working with Artifacts

### Define New Artifact Type

```bash
cat > examples/test_result_artifact.md <<'EOF'
# Name: test-result

# Purpose:
Test execution results with pass/fail status and coverage data

# Format: JSON

# File Pattern: *.test-result.json

# Schema Properties:
- total_tests (number): Total number of tests
- passed (number): Tests that passed
- failed (number): Tests that failed
- coverage (number): Code coverage percentage
- duration (number): Execution time in seconds

# Required Fields:
- total_tests
- passed
- failed

# Producers:
- test.runner

# Consumers:
- test.reporter
- ci.dashboard

# Related Types:
- validation-report
- build-result
EOF

python3 agents/meta.artifact/meta_artifact.py create examples/test_result_artifact.md
```

### Use Artifact in Agents

```yaml
# Producer agent
name: test.runner
artifact_metadata:
  produces:
    - type: test-result

# Consumer agent
name: test.reporter
artifact_metadata:
  consumes:
    - type: test-result
  produces:
    - type: html-report
```

### Find Compatible Agents

```bash
# Find agents that can use test-result
python3 agents/meta.compatibility/meta_compatibility.py list-all --format json | \
  jq '.agents[] | select(.consumes[] | contains("test-result"))'
```

## Multi-Agent Workflows

### Example: Code Review Pipeline

```bash
# 1. Define artifacts
python3 agents/meta.artifact/meta_artifact.py create examples/code_diff_artifact.md
python3 agents/meta.artifact/meta_artifact.py create examples/review_report_artifact.md

# 2. Create agents
python3 agents/atum/atum.py examples/code_analyzer.md     # Produces: review-report
python3 agents/atum/atum.py examples/fix_suggester.md     # Consumes: review-report
python3 agents/atum/atum.py examples/code_formatter.md    # Consumes: review-report

# 3. Discover pipeline
python3 agents/meta.compatibility/meta_compatibility.py \
  suggest-pipeline "Analyze code, suggest fixes, and format"
```

Output:
```json
{
  "pipeline": {
    "name": "Code Review and Fix",
    "steps": [
      {
        "agent": "code.analyzer",
        "produces": ["review-report"]
      },
      {
        "agent": "fix.suggester",
        "consumes": ["review-report"],
        "produces": ["fix-suggestions"]
      },
      {
        "agent": "code.formatter",
        "consumes": ["review-report", "fix-suggestions"],
        "produces": ["formatted-code"]
      }
    ]
  }
}
```

### Execution

```bash
# Execute pipeline manually
python3 agents/code.analyzer/run.py input.py > review.json
python3 agents/fix.suggester/run.py review.json > fixes.json
python3 agents/code.formatter/run.py review.json fixes.json > output.py
```

## Common Patterns

### Pattern 1: Create + Validate + Deploy

```bash
# Create API spec
python3 agents/api.designer/run.py requirements.md > api.yaml

# Validate spec
python3 skills/api.validate/api_validate.py api.yaml > validation.json

# Deploy if valid
if jq -e '.ok == true' validation.json; then
    python3 agents/api.deployer/run.py api.yaml
fi
```

### Pattern 2: Test + Report + Notify

```bash
# Run tests
pytest tests/ --json-report --json-report-file=results.json

# Generate report
python3 skills/test.report/test_report.py results.json > report.html

# Send notification
python3 agents/notifier/run.py report.html team@example.com
```

### Pattern 3: Monitor + Analyze + Alert

```bash
# Continuous monitoring loop
while true; do
    # Collect metrics
    python3 skills/metrics.collect/metrics_collect.py > metrics.json

    # Analyze for anomalies
    python3 agents/anomaly.detector/run.py metrics.json > alerts.json

    # Send alerts if needed
    if jq -e '.alerts | length > 0' alerts.json; then
        python3 agents/alerter/run.py alerts.json
    fi

    sleep 60
done
```

## Tips & Best Practices

### 1. Start Small

Begin with simple agents and skills, then build complexity:

```bash
# ✅ Good: Simple, focused agent
meta.agent: "Validate JSON files"

# ❌ Too complex: Multiple responsibilities
meta.agent: "Validate JSON, XML, YAML, and TOML files, convert between formats, and generate schemas"
```

### 2. Use Descriptive Names

Follow naming conventions:

```bash
# ✅ Good
- Agents: domain.action (e.g., api.validate, code.review)
- Skills: domain.action (e.g., file.compare, data.transform)
- Artifacts: descriptive-kebab-case (e.g., api-spec, test-result)

# ❌ Bad
- my_agent, agent1, test
```

### 3. Define Artifacts First

Create artifact types before agents that use them:

```bash
# 1. Define what data flows
python3 agents/meta.artifact/meta_artifact.py create artifact.md

# 2. Then create agents
python3 agents/atum/atum.py agent.md
```

### 4. Leverage Compatibility Analysis

Use meta.compatibility to discover workflows:

```bash
# Find what can work with your agent
python3 agents/meta.compatibility/meta_compatibility.py find-compatible YOUR_AGENT

# Get suggestions
python3 agents/meta.suggest/meta_suggest.py suggest agents/YOUR_AGENT/agent.yaml
```

### 5. Test Everything

Run integration tests regularly:

```bash
# Full test suite
bash tests/integration/test_meta_agents.sh

# Individual component tests
pytest skills/YOUR_SKILL/test_YOUR_SKILL.py -v
```

## Next Steps

### Learn More

1. **Meta-Agents Deep Dive**: [docs/META_AGENTS.md](docs/META_AGENTS.md)
2. **Artifact Standards**: [docs/ARTIFACT_STANDARDS.md](docs/ARTIFACT_STANDARDS.md)
3. **Examples**: Browse [examples/](examples/) directory

### Build Real Projects

Try these project ideas:

1. **CI/CD Pipeline**: Build agents for testing, building, and deploying
2. **API Development**: Create agents for designing, validating, and generating API code
3. **Code Quality**: Build automated code review and refactoring agents
4. **Data Processing**: Create skills for data transformation and validation

### Join the Community

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Share your agents and skills
- **Contributing**: See CONTRIBUTING.md

## Troubleshooting

### Common Issues

**Problem**: Agent creation fails

```bash
# Solution: Check artifact types exist first
python3 agents/meta.artifact/meta_artifact.py check YOUR_ARTIFACT_TYPE
```

**Problem**: Skill import errors

```bash
# Solution: Ensure PYTHONPATH is set
export PYTHONPATH="${PYTHONPATH}:/path/to/betty"
```

**Problem**: Hook doesn't trigger

```bash
# Solution: Check event type and tool filter
cat .claude/hooks.yaml

# Verify hook is enabled
# enabled: true
```

## Quick Reference

```bash
# Meta-Agents
python3 agents/meta.artifact/meta_artifact.py create <file>
python3 agents/atum/atum.py <description>
python3 agents/meta.skill/meta_skill.py <description>
python3 agents/meta.hook/meta_hook.py <description>
python3 agents/meta.compatibility/meta_compatibility.py <command>
python3 agents/meta.suggest/meta_suggest.py <command>

# Testing
bash tests/integration/test_meta_agents.sh
pytest <test_file> -v

# Common Commands
python3 agents/meta.artifact/meta_artifact.py check <type>
python3 agents/meta.compatibility/meta_compatibility.py list-all
python3 agents/meta.compatibility/meta_compatibility.py find-compatible <agent>
python3 agents/meta.suggest/meta_suggest.py suggest <agent_file>
```

---

**Ready to build!** Start creating agents, skills, and hooks with Betty Framework.
