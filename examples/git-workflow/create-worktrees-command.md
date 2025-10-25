# Name: create-worktrees

# Description:
Create and manage git worktrees for parallel development on multiple branches

# Execution Type: workflow

# Status: draft

# Version: 1.0.0

# Parameters:
- branch_name (string, required): Name for the new branch in the worktree
- base_branch (string, optional): Base branch to create from (default: main)
- issue_number (string, optional): GitHub issue number to link (e.g., "123")
- directory (string, optional): Directory name for worktree (default: branch_name)

# Usage Examples:
```bash
# Create worktree for feature branch
/create-worktrees feature/new-feature

# Create worktree from develop branch
/create-worktrees feature/api-update --base develop

# Create worktree linked to issue
/create-worktrees fix/bug-123 --issue 123

# Create worktree with custom directory
/create-worktrees feature/test --directory ../test-workspace
```

# Instructions:
1. Validate current directory is a git repository
   ```bash
   if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
     echo "Error: Not in a git repository"
     exit 1
   fi
   ```

2. Get base branch (default to main if not specified)
   ```bash
   BASE_BRANCH=${base_branch:-main}
   ```

3. Determine worktree directory path
   ```bash
   WORKTREE_DIR=${directory:-../worktrees/$branch_name}
   ```

4. Fetch latest changes from remote
   ```bash
   git fetch origin
   ```

5. Create the worktree with new branch
   ```bash
   git worktree add -b "$branch_name" "$WORKTREE_DIR" "origin/$BASE_BRANCH"
   ```

6. If issue number provided, create initial commit linking to issue
   ```bash
   if [ -n "$issue_number" ]; then
     cd "$WORKTREE_DIR"
     git commit --allow-empty -m "chore: initialize branch for issue #$issue_number"
   fi
   ```

7. Display success message with worktree location
   ```bash
   echo "✓ Worktree created successfully!"
   echo "  Location: $WORKTREE_DIR"
   echo "  Branch: $branch_name"
   echo "  Base: $BASE_BRANCH"
   [ -n "$issue_number" ] && echo "  Issue: #$issue_number"
   echo ""
   echo "To start working:"
   echo "  cd $WORKTREE_DIR"
   ```

8. List all worktrees for reference
   ```bash
   echo ""
   echo "All worktrees:"
   git worktree list
   ```

# Notes:
- This is a COMMAND_ONLY pattern (3-5 simple steps)
- No skill needed - all logic is inline bash
- Worktrees allow working on multiple branches simultaneously
- Each worktree is a separate working directory
- To remove a worktree: `git worktree remove <path>`
- To list worktrees: `git worktree list`

# Complexity Analysis:
- Steps: 5 (below 10 threshold)
- Autonomy: Low (straightforward git commands)
- Reusability: Low (user-facing only)
- Decision: COMMAND_ONLY ✓
