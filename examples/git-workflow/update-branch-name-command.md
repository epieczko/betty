# Name: update-branch-name

# Description:
Rename a git branch both locally and on the remote repository

# Execution Type: workflow

# Status: draft

# Version: 1.0.0

# Parameters:
- new_name (string, required): New name for the branch
- old_name (string, optional): Old branch name (default: current branch)
- skip_remote (boolean, optional): Skip updating remote (default: false)

# Usage Examples:
```bash
# Rename current branch
/update-branch-name feature/new-name

# Rename specific branch
/update-branch-name feature/better-name --old-name feature/old-name

# Rename only locally (don't update remote)
/update-branch-name feature/local-only --skip-remote
```

# Instructions:
1. Get the old branch name (current branch if not specified)
   ```bash
   if [ -n "$old_name" ]; then
     OLD_BRANCH="$old_name"
   else
     OLD_BRANCH=$(git branch --show-current)
   fi

   if [ -z "$OLD_BRANCH" ]; then
     echo "Error: Could not determine branch name"
     exit 1
   fi
   ```

2. Validate new branch name
   ```bash
   if [ -z "$new_name" ]; then
     echo "Error: New branch name is required"
     exit 1
   fi

   if [ "$OLD_BRANCH" = "$new_name" ]; then
     echo "Error: New name is the same as old name"
     exit 1
   fi
   ```

3. Check if new branch name already exists
   ```bash
   if git show-ref --verify --quiet "refs/heads/$new_name"; then
     echo "Error: Branch '$new_name' already exists"
     exit 1
   fi
   ```

4. Rename the branch locally
   ```bash
   echo "Renaming branch '$OLD_BRANCH' to '$new_name'..."
   git branch -m "$OLD_BRANCH" "$new_name"
   echo "✓ Local branch renamed"
   ```

5. If not skipping remote, update remote repository
   ```bash
   if [ "$skip_remote" != "true" ]; then
     # Check if old branch exists on remote
     if git ls-remote --heads origin "$OLD_BRANCH" | grep -q "$OLD_BRANCH"; then
       echo "Updating remote repository..."

       # Push new branch to remote
       git push origin "$new_name"
       echo "✓ New branch pushed to remote"

       # Delete old branch from remote
       git push origin --delete "$OLD_BRANCH"
       echo "✓ Old branch deleted from remote"

       # Update upstream tracking
       git branch --set-upstream-to="origin/$new_name" "$new_name"
       echo "✓ Upstream tracking updated"
     else
       echo "Note: Old branch does not exist on remote, pushing new branch..."
       git push -u origin "$new_name"
       echo "✓ New branch pushed to remote"
     fi
   else
     echo "⊘ Skipping remote update (--skip-remote flag)"
   fi
   ```

6. Display summary
   ```bash
   echo ""
   echo "✓ Branch rename complete!"
   echo "  Old name: $OLD_BRANCH"
   echo "  New name: $new_name"
   [ "$skip_remote" != "true" ] && echo "  Remote: Updated"
   echo ""
   echo "Current branch: $(git branch --show-current)"
   ```

# Notes:
- This is a COMMAND_ONLY pattern (4-5 simple steps)
- No skill needed - all logic is inline bash
- Safe: Checks if new name already exists before renaming
- Updates tracking information automatically
- Can be used for local-only renames with --skip-remote flag

# Complexity Analysis:
- Steps: 4-5 (below 10 threshold)
- Autonomy: Low (straightforward git operations)
- Reusability: Low (typically one-off user operation)
- Decision: COMMAND_ONLY ✓
