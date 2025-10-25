# Git Workflow Commands: Implementation Guide

## Quick Summary

✅ **Analysis Complete!** All 9 git-workflow commands have been analyzed using the meta-agent decision framework.

## Decision Results

| Command | Pattern | Skill Name | Priority |
|---------|---------|------------|----------|
| create-worktrees | COMMAND_ONLY | - | Phase 1 |
| update-branch-name | COMMAND_ONLY | - | Phase 1 |
| branch-cleanup | SKILL_AND_COMMAND | `git.cleanup-branches` | Phase 2 |
| commit | HYBRID | Uses existing skills | Phase 2 |
| create-pr | SKILL_AND_COMMAND | `git.create-pr` | Phase 3 |
| git-bisect-helper | SKILL_AND_COMMAND | `git.bisect-helper` | Phase 3 |
| pr-review | SKILL_AND_COMMAND | `git.review-pr` | Phase 4 |
| fix-github-issue | SKILL_AND_COMMAND | `git.fix-issue` | Phase 4 |

## Recommended New Agents

Four new agents should be created to use these skills:

1. **git.workflow** - Main git workflow orchestrator
2. **release.manager** - Release automation
3. **code.reviewer** - Automated PR reviews
4. **issue.resolver** - Automated issue resolution

## How the Meta-Agent System Determines This

### 1. meta.command - Decides Skill vs Command

Located in `agents/meta.command/meta_command.py` (lines 222-337)

**Analyzes:**
- Step count (1-3 = command, 10+ = skill+command)
- Autonomy keywords: "analyze", "optimize", "decide", "intelligent", etc. (48 keywords)
- Reusability keywords: "reusable", "composable", "shared", etc. (9 keywords)
- Complexity estimation from instruction lines

**Decision Logic:**
```python
if step_count >= 10 OR complexity == "high":
    → SKILL_AND_COMMAND
elif autonomy_level == "high":
    → SKILL_AND_COMMAND
elif reusability == "high":
    → SKILL_AND_COMMAND (if complex) or SKILL_ONLY (if simple)
elif step_count <= 3:
    → COMMAND_ONLY
else:
    → Evaluate case by case
```

### 2. agent.compose - Finds Skills for Agents

Located in `skills/agent.compose/agent_compose.py`

**How it works:**
1. **Keyword Matching** - Scans agent purpose for domain keywords:
   - "api" → finds api.define, api.validate, api.generate-models
   - "git" → finds git.create-pr, git.cleanup-branches
   - "workflow" → finds workflow.validate, workflow.compose

2. **Artifact Matching** - Matches produces/consumes:
   - Agent needs "pull-request" output
   - Finds skills that produce "pull-request" artifact
   - Recommends git.create-pr skill

3. **Manual Override** - Agent description can specify exact skills

**Used by:**
- `meta.agent` - Automatically composes agents from skills
- `meta.compatibility` - Analyzes skill compatibility

## Implementation Workflow

### Quick Start (Create PR workflow as example)

```bash
# 1. Create the skill
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md

# Output:
# ✅ skills/git.create-pr/skill.yaml
# ✅ skills/git.create-pr/git_create_pr.py (implementation stub)
# ✅ skills/git.create-pr/test_git_create_pr.py (test template)
# ✅ skills/git.create-pr/SKILL.md (documentation)

# 2. Implement the skill logic
# Edit: skills/git.create-pr/git_create_pr.py
# (Add GitHub API calls, commit analysis, etc.)

# 3. Create the command wrapper
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md

# Output:
# ✅ commands/create-pr/command.yaml
# ✅ Registered in registry/commands.json
# ℹ️  meta.command will show you its analysis:
#    - Step count: 10-12 steps
#    - Complexity: HIGH
#    - Autonomy: HIGH
#    - Recommendation: SKILL_AND_COMMAND ✅

# 4. Create agent that uses it
python3 agents/meta.agent/meta_agent.py examples/git-workflow/git-workflow-agent.md

# Output:
# ✅ agents/git.workflow/agent.yaml (with recommended skills)
# ✅ agents/git.workflow/README.md
# ℹ️  meta.agent will use agent.compose to find:
#    - git.create-pr
#    - git.cleanup-branches
#    - workflow.compose
#    - Any other compatible skills

# 5. Validate everything works
python3 agents/meta.compatibility/meta_compatibility.py analyze git.workflow
```

### Phase-by-Phase Implementation

#### Phase 1: Simple Commands (1-2 days)

```bash
# These need COMMAND_ONLY pattern - just create the commands
python3 agents/meta.command/meta_command.py examples/git-workflow/create-worktrees-command.md
python3 agents/meta.command/meta_command.py examples/git-workflow/update-branch-name-command.md
```

**No skills needed!** Commands contain inline bash.

#### Phase 2: Medium Complexity (2-3 days)

```bash
# Create skill first, then command
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-cleanup-branches-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/branch-cleanup-command.md

# Hybrid pattern - orchestrates existing skills
python3 agents/meta.command/meta_command.py examples/git-workflow/commit-command.md
```

#### Phase 3: High Value Automation (1 week)

```bash
# Complex skills - most valuable
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-create-pr-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/create-pr-command.md

python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-bisect-helper-skill.md
python3 agents/meta.command/meta_command.py examples/git-workflow/git-bisect-helper-command.md
```

#### Phase 4: Advanced Automation (1-2 weeks)

```bash
# Most complex workflows
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-review-pr-skill.md
python3 agents/meta.skill/meta_skill.py examples/git-workflow/git-fix-issue-skill.md

# Create orchestrator agents
python3 agents/meta.agent/meta_agent.py examples/git-workflow/git-workflow-agent.md
python3 agents/meta.agent/meta_agent.py examples/git-workflow/code-reviewer-agent.md
python3 agents/meta.agent/meta_agent.py examples/git-workflow/release-manager-agent.md
python3 agents/meta.agent/meta_agent.py examples/git-workflow/issue-resolver-agent.md
```

## Key Files Created

### Documentation
- ✅ `/docs/GIT_WORKFLOW_ANALYSIS.md` - Complete analysis of all 9 commands
- ✅ `/examples/git-workflow/README.md` - Implementation guide with examples
- ✅ `/IMPLEMENTATION_GUIDE.md` - This file (quick reference)

### Example Templates
- ✅ `/examples/git-workflow/git-create-pr-skill.md` - Skill description template
- ✅ `/examples/git-workflow/create-pr-command.md` - Command description template
- ✅ `/examples/git-workflow/git-workflow-agent.md` - Agent description template

### Reference Documentation (Already exists)
- `/docs/SKILL_COMMAND_DECISION_TREE.md` - Decision framework
- `/docs/META_AGENTS.md` - Meta-agent system overview
- `/agents/meta.agent/README.md` - Agent creation guide
- `/agents/meta.command/README.md` - Command creation guide

## How to Determine Agent Skill Assignments

### Method 1: Automatic (Recommended)

Let `meta.agent` use `agent.compose` automatically:

```bash
# Just create an agent description with clear purpose
cat > examples/my-agent.md << 'EOF'
# Name: git.workflow

# Purpose:
Orchestrate git workflows including PR creation, branch cleanup,
and issue resolution. Automate common git operations.

# Inputs:
- github-issue
- git-branch

# Outputs:
- pull-request
- branch-cleanup-report
EOF

# meta.agent will automatically find compatible skills!
python3 agents/meta.agent/meta_agent.py examples/my-agent.md
```

### Method 2: Manual Inspection

Check what skills agent.compose would recommend:

```bash
# Test what skills would be recommended
python3 skills/agent.compose/agent_compose.py \
  --purpose "Orchestrate git workflows" \
  --artifacts "pull-request,github-issue"
```

### Method 3: Explicit Assignment

Specify exact skills in agent description:

```markdown
# Skills Required:
- git.create-pr
- git.cleanup-branches
- workflow.compose
```

## Trust the Meta-Agent System!

The beauty of the Betty framework is that **the meta-agents do the analysis for you**:

1. ✅ **meta.command** tells you if something should be a skill or command
2. ✅ **agent.compose** finds compatible skills for your agent
3. ✅ **meta.agent** creates complete agents with proper skill composition
4. ✅ **meta.compatibility** validates everything works together

**You don't have to guess!** The system analyzes:
- Step count
- Complexity keywords
- Autonomy requirements
- Reusability needs
- Artifact compatibility

## Next Steps

### Immediate Actions

1. ✅ Review `/docs/GIT_WORKFLOW_ANALYSIS.md` for detailed analysis
2. ✅ Review example templates in `/examples/git-workflow/`
3. Start with Phase 1 (simple commands)
4. Use meta.skill and meta.command to create remaining workflows

### Testing the System

```bash
# Test the decision logic with a new command
cat > examples/test-command.md << 'EOF'
# Name: my-test

# Description:
This command analyzes code, optimizes performance, and generates reports.
It requires 15 steps of sophisticated analysis.
EOF

# meta.command will analyze and recommend pattern
python3 agents/meta.command/meta_command.py examples/test-command.md

# You'll see output like:
# ✅ Complexity Analysis:
#    - Steps: 15 (HIGH)
#    - Autonomy keywords found: analyze, optimizes, sophisticated
#    - Recommendation: SKILL_AND_COMMAND
#    - Rationale: High complexity (15 steps) and autonomy keywords detected
```

### Validation Workflow

After creating skills/commands/agents:

```bash
# Check agent compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze AGENT_NAME

# Find all agents that can use a skill
python3 agents/meta.compatibility/meta_compatibility.py find-compatible SKILL_NAME

# List all meta-agents
python3 agents/meta.agent/meta_agent.py --list
```

## Summary

**The System Works Like This:**

```
You write a description
         ↓
meta.command analyzes it
         ↓
Recommends: COMMAND_ONLY / SKILL_ONLY / SKILL_AND_COMMAND / HYBRID
         ↓
You create skill (if needed) with meta.skill
         ↓
You create command with meta.command
         ↓
You create agent with meta.agent
         ↓
meta.agent uses agent.compose to find compatible skills
         ↓
agent.compose matches by keywords + artifacts
         ↓
Complete agent.yaml created with proper skills
         ↓
Validate with meta.compatibility
         ↓
Done! 🎉
```

## Questions?

- Decision framework: `/docs/SKILL_COMMAND_DECISION_TREE.md`
- Meta-agent system: `/docs/META_AGENTS.md`
- Git workflow analysis: `/docs/GIT_WORKFLOW_ANALYSIS.md`
- Examples: `/examples/git-workflow/`

The meta-agent system is **self-documenting** and **self-governing**. Trust the analysis! 🚀
