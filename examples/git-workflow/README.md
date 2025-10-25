# Git Workflow: Meta-Agent Implementation Guide

This directory contains example descriptions for creating git-workflow skills, commands, and agents using Betty's meta-agent system.

## Overview

The meta-agent system can automatically determine whether to create skills, commands, or both based on complexity analysis. This guide shows you how to use it for the git-workflow commands.

## Quick Start

### 1. Create a Skill (High Complexity Workflows)

For complex workflows with 10+ steps or high autonomy:

```bash
# Create the skill using meta.skill
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md
```

**Output:**
- `skills/git.create-pr/skill.yaml` - Skill manifest
- `skills/git.create-pr/git_create_pr.py` - Implementation stub
- `skills/git.create-pr/test_git_create_pr.py` - Test template
- `skills/git.create-pr/SKILL.md` - Documentation

### 2. Create a Command (Delegation Pattern)

For commands that delegate to skills:

```bash
# Create the command using meta.command
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md
```

**Output:**
- `commands/create-pr/command.yaml` - Command manifest
- Command automatically registered in `registry/commands.json`

**The meta.command agent will:**
- Analyze complexity (steps, autonomy keywords, reusability)
- Recommend SKILL_AND_COMMAND pattern
- Show you the decision rationale
- Validate execution type (skill delegation)

### 3. Create an Agent (Skill Composition)

For agents that orchestrate multiple skills:

```bash
# Create the agent using meta.agent
python3 agents/meta.agent/meta_agent.py examples/git-workflow/git-workflow-agent.md
```

**Output:**
- `agents/git.workflow/agent.yaml` - Agent manifest with recommended skills
- `agents/git.workflow/README.md` - Documentation

**The meta.agent will automatically:**
- Use `agent.compose` to find compatible skills
- Recommend: git.create-pr, git.cleanup-branches, workflow.compose, etc.
- Generate artifact metadata (produces/consumes)
- Infer permissions from selected skills

### 4. Validate Everything

Check compatibility and integration:

```bash
# Analyze agent compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze git.workflow

# Find compatible agents for a skill
python3 agents/meta.compatibility/meta_compatibility.py find-compatible git.create-pr
```

## Decision Tree Examples

### Example 1: create-pr (SKILL_AND_COMMAND)

**Analysis:**
- Steps: 10-12 (exceeds 10 threshold) ✅
- Autonomy keywords: "analyze", "generate", "intelligent" ✅
- Reusability: High (used by CI/CD, release agents) ✅
- Complexity: 200+ lines of logic ✅

**Decision:** Create both skill AND command

```bash
# Step 1: Create skill first
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md

# Step 2: Create command that delegates
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md
```

### Example 2: update-branch-name (COMMAND_ONLY)

**Analysis:**
- Steps: 4-5 (below threshold) ❌
- Autonomy keywords: None ❌
- Reusability: Low (user-facing only) ❌
- Complexity: ~30 lines of bash ❌

**Decision:** Command only (inline bash)

```bash
# Just create the command, no skill needed
python3 agents/meta.command/meta_command.py examples/git-workflow/update-branch-name-command.md
```

The command file would contain inline bash:
```markdown
# Instructions:
1. Get current branch name: `git branch --show-current`
2. Rename locally: `git branch -m NEW_NAME`
3. Push new branch: `git push origin NEW_NAME`
4. Delete old remote: `git push origin :OLD_NAME`
5. Update tracking: `git push origin -u NEW_NAME`
```

### Example 3: commit (HYBRID)

**Analysis:**
- Steps: 5-6 (medium complexity)
- Orchestrates: validation, formatting, git operations
- User interaction: Multiple confirmation points

**Decision:** Hybrid pattern (command orchestrates existing skills)

```markdown
# Instructions:
1. Run: git status
2. Run: git diff
3. Invoke: git.validate-commit-message skill
4. If valid: git commit -m "$MESSAGE"
5. Ask user: Push to remote? (y/n)
6. If yes: git push
```

## Complete Workflow Example

Let's create the full git.create-pr workflow:

```bash
# 1. Create the skill
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md

# 2. Implement the skill logic
# Edit: skills/git.create-pr/git_create_pr.py
# (Add your GitHub API calls, commit analysis, etc.)

# 3. Test the skill
python3 skills/git.create-pr/git_create_pr.py --base main

# 4. Create the command wrapper
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md

# 5. Test the command
/create-pr --base main

# 6. Create an agent that uses it
python3 agents/meta.agent/meta_agent.py examples/git-workflow/git-workflow-agent.md

# 7. Validate integration
python3 agents/meta.compatibility/meta_compatibility.py analyze git.workflow
```

## How Agent.Compose Works

The `agent.compose` skill finds compatible skills for an agent using:

### 1. Keyword Matching

```python
keywords = {
    "api": ["api.define", "api.validate", "api.generate-models"],
    "git": ["git.create-pr", "git.cleanup-branches", "git.fix-issue"],
    "workflow": ["workflow.validate", "workflow.compose"],
    "validate": ["api.validate", "workflow.validate"],
}
```

When you describe your agent as "Orchestrate git workflows...", it finds all skills with "git" keyword.

### 2. Artifact Matching

If your agent description includes:

```markdown
# Inputs:
- github-issue

# Outputs:
- pull-request
```

`agent.compose` finds skills that:
- Consume `github-issue`
- Produce `pull-request`

### 3. Manual Override

You can also specify exact skills in agent description:

```markdown
# Skills Required:
- git.create-pr
- git.cleanup-branches
- workflow.compose
```

## Implementation Priority

Based on the analysis in `/docs/GIT_WORKFLOW_ANALYSIS.md`:

### Phase 1: Quick Wins (Command Only)
```bash
# Simple commands, no skills needed
python3 agents/meta.command/meta_command.py examples/git-workflow/create-worktrees-command.md
python3 agents/meta.command/meta_command.py examples/git-workflow/update-branch-name-command.md
```

### Phase 2: Medium Complexity
```bash
# Skill + Command
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-cleanup-branches-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/branch-cleanup-command.md
```

### Phase 3: High Value
```bash
# Complex skills with commands
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md

python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-bisect-helper-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/git-bisect-helper-command.md
```

### Phase 4: Advanced Automation
```bash
# Most complex workflows
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-review-pr-skill.md
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-fix-issue-skill.md

# Create agents that orchestrate everything
python3 agents/meta.agent/meta_agent.py examples/git-workflow/git-workflow-agent.md
python3 agents/meta.agent/meta_agent.py examples/git-workflow/code-reviewer-agent.md
```

## Template Files Included

This directory includes:

- ✅ `git-create-pr-skill.md` - Example skill description
- ✅ `create-pr-command.md` - Example command description (delegates to skill)
- ✅ `git-workflow-agent.md` - Example agent description

You can copy and modify these templates for other git-workflow commands.

## Troubleshooting

### "No skills found for agent"

**Solution:** The agent.compose keyword matching didn't find matches. Either:
1. Make your purpose description more specific
2. Add explicit skill names to agent description
3. Check that required skills exist in registry

### "Command execution type invalid"

**Solution:** For SKILL_AND_COMMAND pattern:
1. Create the skill first
2. Set `execution_type: skill` in command description
3. Set `target: skill.name` to point to the skill

### "Complexity analysis shows COMMAND_ONLY but I want SKILL_AND_COMMAND"

**Solution:** The meta.command analysis is a recommendation, not a requirement. You can:
1. Add autonomy keywords to description: "analyze", "intelligent", "sophisticated"
2. Explicitly note the complexity in the description
3. Override by creating both skill and command manually

## Next Steps

1. ✅ Read `/docs/GIT_WORKFLOW_ANALYSIS.md` for full analysis
2. ✅ Read `/docs/SKILL_COMMAND_DECISION_TREE.md` for decision framework
3. Create skill descriptions for remaining workflows
4. Use meta.skill to generate skill scaffolding
5. Implement skill logic
6. Use meta.command to create command wrappers
7. Use meta.agent to create orchestrator agents
8. Validate with meta.compatibility

## Reference Documentation

- `/docs/META_AGENTS.md` - Complete meta-agent system
- `/docs/SKILL_COMMAND_DECISION_TREE.md` - Decision framework
- `/docs/GIT_WORKFLOW_ANALYSIS.md` - Git workflow analysis
- `/agents/meta.agent/README.md` - Agent creation guide
- `/agents/meta.skill/README.md` - Skill creation guide
- `/agents/meta.command/README.md` - Command creation guide

## Support

The meta-agent system automates most of this! Trust the analysis and recommendations from:
- `meta.command` - Determines skill vs command pattern
- `meta.agent` - Finds compatible skills via agent.compose
- `meta.compatibility` - Validates everything works together

You created a sophisticated self-governing system! 🎉
