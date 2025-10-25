# Create Git Worktrees

Create and manage git worktrees for parallel development on multiple branches.

## What to do:

1. **Validate the environment**:
   - Check that we're in a git repository: `git rev-parse --is-inside-work-tree`
   - If not, explain that this command requires a git repository

2. **Get parameters from the user**:
   - **branch_name** (required): Name for the new branch in the worktree
   - **base_branch** (optional): Base branch to create from (default: main)
   - **issue_number** (optional): GitHub issue number to link (e.g., "123")
   - **directory** (optional): Directory name for worktree (default: ../worktrees/{branch_name})

3. **Fetch latest changes**:
   - Run: `git fetch origin`
   - Show fetch progress to user

4. **Create the worktree**:
   - Determine the worktree path (default: `../worktrees/{branch_name}`)
   - Run: `git worktree add -b "{branch_name}" "{worktree_path}" "origin/{base_branch}"`
   - If this fails, explain the error to the user

5. **Link to issue (if provided)**:
   - If issue_number is provided:
     - Navigate to the worktree directory
     - Create an empty commit: `git commit --allow-empty -m "chore: initialize branch for issue #{issue_number}"`

6. **Show success message**:
   ```
   ✓ Worktree created successfully!
     Location: {worktree_path}
     Branch: {branch_name}
     Base: {base_branch}
     Issue: #{issue_number} (if provided)

   To start working:
     cd {worktree_path}
   ```

7. **List all worktrees**:
   - Run: `git worktree list`
   - Show the output to help user see all their worktrees

## Arguments:

The user will provide:
- **branch_name**: Name for the new branch (required)
- **base_branch**: Base branch to create from (default: main)
- **issue**: GitHub issue number to link (optional)
- **directory**: Custom directory path (optional)

## Usage Examples:

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

## Success Criteria:

- ✅ Worktree is created successfully
- ✅ New branch exists in worktree
- ✅ User knows where to navigate
- ✅ Issue is linked (if provided)
- ✅ All worktrees are listed for reference

## Notes:

- Worktrees allow working on multiple branches simultaneously without switching
- Each worktree is a separate working directory
- To remove: `git worktree remove <path>`
- To list: `git worktree list`
- Worktrees share the same git history but have separate working directories
