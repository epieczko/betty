# Phase 1 Implementation: Git Workflow Commands

## Overview

Phase 1 implements the two simplest git-workflow commands using the **COMMAND_ONLY** pattern. These commands contain inline instructions and do not require separate skills.

## Commands Implemented

### 1. /create-worktrees

**Location:** `.claude/commands/create-worktrees.md`

**Purpose:** Create and manage git worktrees for parallel development on multiple branches

**Features:**
- ✅ Creates new worktree with new branch
- ✅ Supports custom base branch (default: main)
- ✅ Optional GitHub issue linking
- ✅ Custom directory path support
- ✅ Lists all worktrees after creation

**Usage:**
```bash
# Create worktree for feature branch
/create-worktrees feature/new-feature

# Create worktree from develop branch
/create-worktrees feature/api-update --base-branch develop

# Create worktree linked to issue
/create-worktrees fix/bug-123 --issue 123

# Create worktree with custom directory
/create-worktrees feature/test --directory ../test-workspace
```

**Decision Rationale:**
- **Steps:** 5 (below 10 threshold)
- **Autonomy:** Low (straightforward git commands)
- **Reusability:** Low (user-facing only)
- **Pattern:** COMMAND_ONLY ✓

---

### 2. /update-branch-name

**Location:** `.claude/commands/update-branch-name.md`

**Purpose:** Rename a git branch both locally and on the remote repository

**Features:**
- ✅ Renames branch locally and remotely
- ✅ Validates new name doesn't exist
- ✅ Updates upstream tracking automatically
- ✅ Optional local-only rename (--skip-remote)
- ✅ Works on current branch or specified branch

**Usage:**
```bash
# Rename current branch
/update-branch-name feature/new-name

# Rename specific branch
/update-branch-name feature/better-name --old-name feature/old-name

# Rename only locally (don't update remote)
/update-branch-name feature/local-only --skip-remote
```

**Decision Rationale:**
- **Steps:** 4-5 (below 10 threshold)
- **Autonomy:** Low (straightforward git operations)
- **Reusability:** Low (typically one-off user operation)
- **Pattern:** COMMAND_ONLY ✓

---

## Implementation Details

### File Structure

```
betty/
├── .claude/
│   └── commands/
│       ├── create-worktrees.md      # ← Claude Code command (user-facing)
│       └── update-branch-name.md    # ← Claude Code command (user-facing)
└── examples/
    └── git-workflow/
        ├── create-worktrees-command.md      # ← Example/documentation
        └── update-branch-name-command.md    # ← Example/documentation
```

### Why COMMAND_ONLY Pattern?

According to the decision tree in `/docs/SKILL_COMMAND_DECISION_TREE.md`:

**Pattern 1: Command Only (Inline Instructions)**

✅ **When to use:**
- Simple orchestration (1-3 bash commands) ← **Both commands fit**
- Task doesn't need to be reusable outside the command ← **Both are user-facing only**
- No complex logic or autonomous decision-making ← **Both are straightforward**
- Fast, straightforward execution ← **Both are quick operations**

**Characteristics:**
- ✅ Simple and direct
- ✅ Easy to understand and modify
- ✅ No additional skill creation overhead
- ❌ Logic not reusable elsewhere (acceptable for these use cases)
- ❌ Can become unwieldy if task grows (we'll refactor if needed)

### Comparison with Other Patterns

| Feature | COMMAND_ONLY (Phase 1) | SKILL_AND_COMMAND (Phase 3) |
|---------|------------------------|------------------------------|
| **Example** | create-worktrees | create-pr |
| **Steps** | 4-5 | 10-12 |
| **Complexity** | Low | High |
| **File Count** | 1 (.md) | 5+ (skill.yaml, .py, test, SKILL.md, command.yaml) |
| **Setup Time** | Minutes | Hours |
| **Reusability** | User-only | Agents, workflows, CI/CD |
| **Autonomy** | None | High (auto-generates content) |

For Phase 1, COMMAND_ONLY is the right choice because:
1. **Quick to implement** - Just write markdown instructions
2. **Easy to test** - Use the command directly in Claude Code
3. **Simple to maintain** - Edit one markdown file
4. **No overhead** - No skill creation, no registry updates, no tests

---

## How Claude Code Commands Work

Claude Code commands (`.claude/commands/*.md`) are different from Betty command manifests:

### Claude Code Commands (.claude/commands/*.md)
- **Format:** Markdown with instructions for Claude
- **Execution:** Claude reads and follows instructions inline
- **Registration:** Automatic (Claude scans .claude/commands/)
- **Usage:** `/command-name` in Claude Code
- **Best for:** Simple, user-facing operations

### Betty Command Manifests (commands/*.yaml)
- **Format:** YAML with execution type and target
- **Execution:** Delegates to skill, agent, or workflow
- **Registration:** Must be registered in registry/commands.json
- **Usage:** Via Betty framework or Claude Code
- **Best for:** Complex operations that need reusability

**For Phase 1, we use Claude Code commands** because they're simple and user-facing only.

---

## Testing

### Test /create-worktrees

```bash
# In Claude Code, run:
/create-worktrees test-feature

# Expected output:
# - Fetches from origin
# - Creates ../worktrees/test-feature
# - Creates branch 'test-feature' from main
# - Shows success message with path
# - Lists all worktrees

# Verify:
git worktree list
# Should show the new worktree

# Cleanup:
git worktree remove ../worktrees/test-feature
```

### Test /update-branch-name

```bash
# Create a test branch first:
git checkout -b old-branch-name
git push -u origin old-branch-name

# In Claude Code, run:
/update-branch-name new-branch-name

# Expected output:
# - Renames branch locally
# - Pushes new branch to remote
# - Deletes old branch from remote
# - Updates upstream tracking
# - Shows success summary

# Verify:
git branch
# Should show 'new-branch-name' as current branch

git branch -r
# Should show 'origin/new-branch-name'
# Should NOT show 'origin/old-branch-name'
```

---

## What's Next: Phase 2

After Phase 1, we move to Phase 2 which includes:

### 1. /branch-cleanup (SKILL_AND_COMMAND)
- **Complexity:** Medium (6-8 steps)
- **Pattern:** Skill + Command
- **Requires:**
  - Create `git.cleanup-branches` skill
  - Create `/branch-cleanup` command that delegates

### 2. /commit (HYBRID)
- **Complexity:** Medium (4-6 steps)
- **Pattern:** Hybrid (orchestrates existing skills)
- **Requires:**
  - Create `git.validate-commit-message` skill (optional)
  - Create `/commit` command that orchestrates

**Phase 2 will take 2-3 days** because we need to:
- Use meta.skill to create skill scaffolding
- Implement skill logic
- Create tests
- Use meta.command to create command wrappers
- Register everything in registries

---

## Lessons Learned

### 1. Know Your Patterns

The decision tree helps determine the right pattern:
- **1-3 steps, low complexity** → COMMAND_ONLY ✓ (Phase 1)
- **4-9 steps, medium complexity** → Evaluate case by case (Phase 2)
- **10+ steps, high complexity** → SKILL_AND_COMMAND (Phase 3+)

### 2. Start Simple

Phase 1 is intentionally simple:
- No skill creation overhead
- No registry management
- No tests (Claude follows instructions)
- Fast iteration

This builds momentum for more complex phases.

### 3. Claude Code Commands vs Betty Manifests

- **Claude Code commands** = User-facing, inline instructions
- **Betty command manifests** = Registered, delegates to skills/agents

Both are valuable, but for different purposes.

### 4. The Meta-Agent System

While we didn't use meta.command for Phase 1 (COMMAND_ONLY doesn't need it), we'll use it heavily in Phase 2+:
- **Phase 2:** meta.skill + meta.command
- **Phase 3:** meta.skill + meta.command
- **Phase 4:** meta.skill + meta.command + meta.agent

The meta-agent system shines when creating complex skills and agents.

---

## Summary

✅ **Phase 1 Complete!**

**Implemented:**
- `/create-worktrees` - Create git worktrees for parallel development
- `/update-branch-name` - Rename branches locally and remotely

**Pattern Used:** COMMAND_ONLY (inline instructions)

**Time Taken:** ~1 hour

**Files Created:**
- `.claude/commands/create-worktrees.md`
- `.claude/commands/update-branch-name.md`
- `examples/git-workflow/create-worktrees-command.md` (documentation)
- `examples/git-workflow/update-branch-name-command.md` (documentation)

**Ready for:** Phase 2 implementation (branch-cleanup + commit)

---

## References

- [Git Workflow Analysis](/docs/GIT_WORKFLOW_ANALYSIS.md) - Complete analysis of all 9 commands
- [Implementation Guide](/IMPLEMENTATION_GUIDE.md) - Quick reference
- [Decision Tree](/docs/SKILL_COMMAND_DECISION_TREE.md) - Pattern selection framework
- [Meta Agents](/docs/META_AGENTS.md) - Meta-agent system overview
