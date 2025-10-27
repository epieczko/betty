# Git Workflow Commands: Skill vs Command Analysis

## Executive Summary

This document analyzes the proposed git-workflow commands to determine the appropriate implementation pattern (Command Only, Skill Only, Skill + Command, or Hybrid) and identifies which agents should use these capabilities.

**Decision Framework Used:** `/docs/SKILL_COMMAND_DECISION_TREE.md`

**Analysis Tool:** meta.command decision logic (lines 222-337 in `agents/meta.command/meta_command.py`)

---

## Commands Analysis

### 1. branch-cleanup.md

**Purpose:** Clean up merged/stale git branches locally and remotely

**Estimated Complexity:**
- **Steps:** 6-8 steps
  1. List local branches
  2. Identify merged branches
  3. Compare with remote
  4. Check for stale branches (no commits in X days)
  5. Present list to user for approval
  6. Delete selected branches locally
  7. Delete selected branches remotely
  8. Prune remote references

**Autonomy Level:** Medium (requires decision-making about which branches are safe to delete)

**Reusability:** Medium (could be used by release management agents)

**Complexity Keywords:** "analyze", "identify", "evaluate"

**DECISION:** ✅ **SKILL_AND_COMMAND**

**Rationale:**
- 6-8 steps with autonomous decision-making
- Requires analysis of git history and branch status
- Logic should be reusable for CI/CD workflows
- Users need simple `/branch-cleanup` entry point

**Implementation:**
- **Skill:** `git.cleanup-branches` - Contains analysis and deletion logic
- **Command:** `/branch-cleanup` - Simple wrapper that delegates to skill

---

### 2. commit.md

**Purpose:** Interactive git commit helper with best practices validation

**Estimated Complexity:**
- **Steps:** 4-6 steps
  1. Show git status
  2. Show git diff
  3. Validate commit message format
  4. Check for conventional commit standards
  5. Create commit
  6. Optionally push

**Autonomy Level:** Low-Medium (validates format, user provides message)

**Reusability:** High (commit logic useful for CI/CD, release agents)

**Complexity Keywords:** "validate", "interactive"

**DECISION:** ✅ **HYBRID** (Command orchestrates validation skills)

**Rationale:**
- Medium complexity (4-6 steps)
- Orchestrates existing validation logic
- User interaction at multiple points
- Can leverage existing `hook.define` for validation

**Implementation:**
- **Command:** `/commit` - Orchestrates git operations
- **Uses existing skills:** Could use policy.enforce for commit message validation
- **May need new skill:** `git.validate-commit-message`

---

### 3. create-pr.md & create-pull-request.md

**Note:** These appear to be duplicates. Recommend using `/create-pr` (shorter).

**Purpose:** Create GitHub pull request with description from commits

**Estimated Complexity:**
- **Steps:** 8-12 steps
  1. Get current branch
  2. Get base branch
  3. Fetch latest changes
  4. Analyze commit history
  5. Generate PR title from commits
  6. Generate PR description from commits
  7. Identify related issues
  8. Create PR via GitHub API
  9. Apply labels
  10. Request reviewers
  11. Link to project board
  12. Display PR URL

**Autonomy Level:** High (auto-generates PR content, analyzes commits)

**Reusability:** High (essential for automated workflows)

**Complexity Keywords:** "analyze", "generate", "autonomous", "intelligent"

**DECISION:** ✅ **SKILL_AND_COMMAND**

**Rationale:**
- 10+ steps (exceeds threshold)
- High autonomy (generates PR content intelligently)
- Highly reusable for release automation
- Complex GitHub API interaction
- Users need simple interface

**Implementation:**
- **Skill:** `git.create-pr` - Contains PR generation logic and GitHub API calls
- **Command:** `/create-pr` - Simple wrapper
- **Remove duplicate:** Delete `/create-pull-request` or make it an alias

---

### 4. create-worktrees.md

**Purpose:** Create and manage git worktrees for parallel development

**Estimated Complexity:**
- **Steps:** 3-5 steps
  1. Choose base branch
  2. Create worktree directory
  3. Create new branch in worktree
  4. Optional: Link to issue/ticket
  5. Display worktree location

**Autonomy Level:** Low (straightforward git operations)

**Reusability:** Low (typically user-facing only)

**Complexity Keywords:** None

**DECISION:** ✅ **COMMAND_ONLY**

**Rationale:**
- Simple 3-5 step process
- Low complexity (direct git commands)
- Not needed by other workflows
- Easy to modify as plain command

**Implementation:**
- **Command:** `/create-worktrees` - Inline bash orchestration
- **No skill needed**

---

### 5. fix-github-issue.md

**Purpose:** Automated workflow to create branch, make changes, commit, and create PR for a GitHub issue

**Estimated Complexity:**
- **Steps:** 12-15 steps
  1. Fetch issue details from GitHub
  2. Parse issue requirements
  3. Create feature branch with issue number
  4. Analyze codebase for relevant files
  5. Make suggested changes
  6. Run tests
  7. Fix any test failures
  8. Stage changes
  9. Create commit with issue reference
  10. Push branch
  11. Create PR linking to issue
  12. Update issue with PR link
  13. Move issue to "In Progress" status
  14. Optional: Request reviews

**Autonomy Level:** Very High (end-to-end autonomous workflow)

**Reusability:** Very High (core automation workflow)

**Complexity Keywords:** "analyze", "autonomous", "intelligent", "complex", "multi-step", "end-to-end"

**DECISION:** ✅ **SKILL_AND_COMMAND**

**Rationale:**
- 12-15 steps (well exceeds threshold)
- Very high autonomy (makes code changes!)
- Highly complex orchestration
- Extremely reusable for automation
- Users need simple `/fix-github-issue 123` interface

**Implementation:**
- **Skill:** `git.fix-issue` - Contains all autonomous logic
- **Command:** `/fix-github-issue` - Simple wrapper
- **Integrates with:** Existing skills like `git.create-pr`, test runners

**IMPORTANT NOTE:** This is the most complex workflow. Consider breaking into smaller skills:
- `github.fetch-issue`
- `git.create-issue-branch`
- `code.analyze-for-issue`
- `git.fix-issue` (orchestrator skill)

---

### 6. git-bisect-helper.md

**Purpose:** Interactive helper for git bisect to find bug-introducing commits

**Estimated Complexity:**
- **Steps:** 8-10 steps
  1. Initialize git bisect
  2. Get good/bad commits from user
  3. Checkout bisect commit
  4. Run test command
  5. Parse test results
  6. Mark commit as good/bad
  7. Repeat until found
  8. Display culprit commit
  9. Show commit details
  10. Reset bisect state

**Autonomy Level:** High (automates bisect process)

**Reusability:** Medium (useful for debugging workflows)

**Complexity Keywords:** "analyze", "automate", "intelligent", "iterative"

**DECISION:** ✅ **SKILL_AND_COMMAND**

**Rationale:**
- 8-10 steps with iteration
- High autonomy (automates bisect iteration)
- Reusable for CI/CD debugging
- Complex state management
- Users need simple interface

**Implementation:**
- **Skill:** `git.bisect-helper` - Contains bisect automation logic
- **Command:** `/git-bisect-helper` - Simple wrapper

---

### 7. pr-review.md

**Purpose:** Review pull request with automated analysis and suggestions

**Estimated Complexity:**
- **Steps:** 10-15 steps
  1. Fetch PR details from GitHub
  2. Get changed files
  3. Analyze code changes
  4. Run static analysis
  5. Check test coverage
  6. Identify security issues
  7. Check for breaking changes
  8. Evaluate code quality
  9. Generate review comments
  10. Post comments to PR
  11. Request changes or approve
  12. Generate review summary
  13. Check for conflicts
  14. Verify CI status

**Autonomy Level:** Very High (sophisticated code analysis and review)

**Reusability:** Very High (critical for automated review workflows)

**Complexity Keywords:** "analyze", "evaluate", "sophisticated", "intelligent", "comprehensive"

**DECISION:** ✅ **SKILL_AND_COMMAND**

**Rationale:**
- 10-15 steps (exceeds threshold)
- Very high complexity (code analysis, AI review)
- Extremely reusable for CI/CD
- Sophisticated decision-making
- Users need simple `/pr-review 123` interface

**Implementation:**
- **Skill:** `git.review-pr` - Contains review logic and analysis
- **Command:** `/pr-review` - Simple wrapper
- **May integrate with:** `api.compatibility`, static analysis tools

---

### 8. update-branch-name.md

**Purpose:** Rename git branch locally and remotely

**Estimated Complexity:**
- **Steps:** 4-5 steps
  1. Get current branch name
  2. Rename branch locally
  3. Push new branch to remote
  4. Delete old branch on remote
  5. Update upstream tracking

**Autonomy Level:** Low (straightforward git operations)

**Reusability:** Low (typically one-off user operation)

**Complexity Keywords:** None

**DECISION:** ✅ **COMMAND_ONLY**

**Rationale:**
- Simple 4-5 step process
- Low complexity (standard git commands)
- Not needed by automated workflows
- Easy to maintain as inline command

**Implementation:**
- **Command:** `/update-branch-name` - Inline bash orchestration
- **No skill needed**

---

## Summary Table

| Command | Pattern | Skill Name | Complexity | Autonomy | Reusability |
|---------|---------|------------|------------|----------|-------------|
| branch-cleanup | SKILL_AND_COMMAND | `git.cleanup-branches` | Medium | Medium | Medium |
| commit | HYBRID | Uses `git.validate-commit-message` | Medium | Low-Med | High |
| create-pr | SKILL_AND_COMMAND | `git.create-pr` | High | High | High |
| create-worktrees | COMMAND_ONLY | - | Low | Low | Low |
| fix-github-issue | SKILL_AND_COMMAND | `git.fix-issue` | Very High | Very High | Very High |
| git-bisect-helper | SKILL_AND_COMMAND | `git.bisect-helper` | High | High | Medium |
| pr-review | SKILL_AND_COMMAND | `git.review-pr` | Very High | Very High | Very High |
| update-branch-name | COMMAND_ONLY | - | Low | Low | Low |

---

## Recommended Implementation Order

### Phase 1: Simple Commands (Quick Wins)
1. `/create-worktrees` - COMMAND_ONLY
2. `/update-branch-name` - COMMAND_ONLY

### Phase 2: Medium Complexity
3. `/branch-cleanup` - SKILL_AND_COMMAND
4. `/commit` - HYBRID (may need `git.validate-commit-message` skill)

### Phase 3: High Value Automation
5. `/create-pr` - SKILL_AND_COMMAND
6. `/git-bisect-helper` - SKILL_AND_COMMAND

### Phase 4: Advanced Automation
7. `/pr-review` - SKILL_AND_COMMAND
8. `/fix-github-issue` - SKILL_AND_COMMAND (most complex, save for last)

---

## Agent Assignment Analysis

### Which agents should use these skills?

#### 1. **git.workflow** agent (NEW - should be created)

**Purpose:** Orchestrate git workflows from branch creation to PR merging

**Skills needed:**
- `git.cleanup-branches`
- `git.create-pr`
- `git.fix-issue`
- `git.review-pr`
- `git.bisect-helper`

**Use cases:**
- End-to-end feature development workflow
- Bug fix workflow
- Release preparation workflow

**Create with:**
```bash
python3 agents/meta.agent/meta_agent.py examples/git-workflow-agent.md
```

---

#### 2. **release.manager** agent (NEW - should be created)

**Purpose:** Automate release processes including branch management, changelogs, and PRs

**Skills needed:**
- `git.cleanup-branches` - Clean up old release branches
- `git.create-pr` - Create release PRs
- `workflow.compose` - Orchestrate release steps

**Use cases:**
- Prepare release branches
- Generate release PRs
- Clean up after releases

---

#### 3. **code.reviewer** agent (NEW - should be created)

**Purpose:** Automated code review with quality checks

**Skills needed:**
- `git.review-pr` - Main review logic
- `api.compatibility` - Check for breaking changes
- `policy.enforce` - Validate compliance

**Use cases:**
- Automated PR reviews
- Pre-merge quality gates
- Security scanning

---

#### 4. **issue.resolver** agent (NEW - should be created)

**Purpose:** Automatically fix simple GitHub issues

**Skills needed:**
- `git.fix-issue` - End-to-end issue resolution
- `git.create-pr` - Create fix PRs
- Test execution skills (TBD)

**Use cases:**
- Fix simple bugs automatically
- Apply automated refactorings
- Update documentation

---

#### 5. Existing agents that may benefit:

**api.designer** - Could use:
- `git.create-pr` - Create PRs for API changes

**workflow.orchestrator** - Could use:
- `git.create-pr` - Create PRs for workflow updates
- `git.cleanup-branches` - Clean up workflow branches

---

## How to Determine Agent Assignments

### Method 1: Use agent.compose skill

The `agent.compose` skill can recommend skills for an agent based on purpose:

```bash
python3 skills/agent.compose/agent_compose.py \
  --purpose "Orchestrate git workflows from branch creation to PR merging" \
  --artifacts "git-branch,pull-request,github-issue"
```

### Method 2: Use meta.agent

Create an agent description and let meta.agent find compatible skills:

```markdown
# Name: git.workflow

# Purpose:
Orchestrate git workflows from branch creation to PR merging,
including automated PR creation, branch cleanup, and issue resolution.

# Inputs:
- github-issue
- git-branch

# Outputs:
- pull-request
- branch-cleanup-report

# Examples:
- Create feature branch and PR from GitHub issue
- Clean up merged branches after release
- Automate PR creation with commit analysis
```

Then run:
```bash
python3 agents/meta.agent/meta_agent.py examples/git-workflow-agent.md
```

meta.agent will use agent.compose to automatically find compatible skills!

---

## Next Steps

### Step 1: Create Skills First

For SKILL_AND_COMMAND patterns, create skills first:

```bash
# Create skill descriptions
examples/git-cleanup-branches-skill.md
examples/git-create-pr-skill.md
examples/git-fix-issue-skill.md
examples/git-review-pr-skill.md
examples/git-bisect-helper-skill.md

# Create skills using meta.skill
python3 agents/meta.skill/meta_skill.py examples/git-cleanup-branches-skill.md
python3 agents/meta.skill/meta_skill.py examples/git-create-pr-skill.md
# etc...
```

### Step 2: Create Commands

Then create commands that delegate to skills:

```bash
# Create command descriptions
examples/branch-cleanup-command.md
examples/create-pr-command.md
# etc...

# Create commands using meta.command
python3 agents/meta.command/meta_command.py examples/branch-cleanup-command.md
python3 agents/meta.command/meta_command.py examples/create-pr-command.md
# etc...
```

### Step 3: Create Agents

Create agents that compose these skills:

```bash
# Create agent descriptions
examples/git-workflow-agent.md
examples/release-manager-agent.md
examples/code-reviewer-agent.md
examples/issue-resolver-agent.md

# Create agents using meta.agent
python3 agents/meta.agent/meta_agent.py examples/git-workflow-agent.md
python3 agents/meta.agent/meta_agent.py examples/release-manager-agent.md
# etc...
```

### Step 4: Validate with meta.compatibility

Check that everything works together:

```bash
python3 agents/meta.compatibility/meta_compatibility.py analyze git.workflow
```

---

## Conclusion

**Summary of Decisions:**
- ✅ **2 COMMAND_ONLY:** create-worktrees, update-branch-name
- ✅ **1 HYBRID:** commit
- ✅ **5 SKILL_AND_COMMAND:** branch-cleanup, create-pr, fix-github-issue, git-bisect-helper, pr-review

**Recommended New Agents:**
- `git.workflow` - Main git workflow orchestrator
- `release.manager` - Release automation
- `code.reviewer` - Automated PR reviews
- `issue.resolver` - Automated issue resolution

**Tools to Use:**
- `meta.skill` - Create skills
- `meta.command` - Create commands with automatic pattern detection
- `meta.agent` - Create agents with automatic skill composition via agent.compose
- `meta.compatibility` - Validate everything works together

The meta-agent system is sophisticated enough to handle all of this automatically!
