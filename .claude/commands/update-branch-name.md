# Update Branch Name

Rename a git branch both locally and on the remote repository.

## What to do:

1. **Get the current branch name** (if old name not specified):
   - Run: `git branch --show-current`
   - This will be the branch to rename
   - If not in a git repository or can't determine branch, explain the error

2. **Get parameters from the user**:
   - **new_name** (required): New name for the branch
   - **old_name** (optional): Old branch name (default: current branch)
   - **skip_remote** (optional): Skip updating remote (default: false)

3. **Validate the parameters**:
   - Check that new_name is provided and not empty
   - Check that old_name != new_name
   - Check that new_name doesn't already exist: `git show-ref --verify --quiet "refs/heads/{new_name}"`
   - If validation fails, explain the issue to the user

4. **Rename the branch locally**:
   - Run: `git branch -m "{old_name}" "{new_name}"`
   - Confirm success: "✓ Local branch renamed"

5. **Update the remote** (unless --skip-remote is specified):
   - Check if old branch exists on remote: `git ls-remote --heads origin "{old_name}"`
   - If it exists on remote:
     - Push new branch: `git push origin "{new_name}"`
     - Delete old branch from remote: `git push origin --delete "{old_name}"`
     - Update upstream tracking: `git branch --set-upstream-to="origin/{new_name}" "{new_name}"`
     - Confirm each step with checkmarks
   - If it doesn't exist on remote:
     - Push new branch: `git push -u origin "{new_name}"`
   - If skip_remote is true:
     - Show: "⊘ Skipping remote update (--skip-remote flag)"

6. **Show summary**:
   ```
   ✓ Branch rename complete!
     Old name: {old_name}
     New name: {new_name}
     Remote: Updated (or "Skipped" if --skip-remote)

   Current branch: {current_branch}
   ```

## Arguments:

The user will provide:
- **new_name**: New name for the branch (required)
- **old_name**: Old branch name (default: current branch)
- **skip_remote**: Skip updating remote (default: false)

## Usage Examples:

```bash
# Rename current branch
/update-branch-name feature/new-name

# Rename specific branch
/update-branch-name feature/better-name --old-name feature/old-name

# Rename only locally (don't update remote)
/update-branch-name feature/local-only --skip-remote
```

## Success Criteria:

- ✅ Branch is renamed locally
- ✅ Remote is updated (unless skipped)
- ✅ Upstream tracking is configured
- ✅ User sees clear confirmation
- ✅ Current branch status is shown

## Notes:

- This is safe: checks if new name already exists before renaming
- Updates tracking information automatically
- Can be used for local-only renames with --skip-remote
- If you're on the branch being renamed, you'll stay on it (with new name)
- Other local worktrees/clones need to update their remotes separately
