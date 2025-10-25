# Name: git.cleanupbranches

# Version: 1.0.0

# Purpose:
Clean up merged and stale git branches both locally and remotely. Analyzes branch status, identifies branches that are safe to delete (merged or stale), and provides interactive cleanup with safety checks.

# Category: git-workflow

# Inputs (Consumes):
- git-repository - Local git repository with branch information
- branch-metadata - Branch merge status and last commit dates

# Outputs (Produces):
- branch-cleanup-report - Report of branches analyzed and deleted
- cleanup-summary - Summary with statistics (branches deleted, kept, errors)

# Parameters:
- dry_run (boolean): Show what would be deleted without deleting (default: true)
- include_remote (boolean): Also clean up remote branches (default: false)
- stale_days (integer): Consider branches stale after N days of no commits (default: 30)
- protected_branches (array): Branches to never delete (default: ["main", "master", "develop", "development"])
- interactive (boolean): Ask for confirmation before deleting (default: true)
- merged_only (boolean): Only delete merged branches, ignore stale (default: false)

# Dependencies:
- git command line tool
- Access to git repository (read for analysis, write for deletion)
- Access to remote repository (if include_remote=true)

# Steps:
1. Validate we're in a git repository
2. Get list of all local branches
3. Identify current branch (never delete)
4. For each branch:
   - Check if in protected list
   - Check if merged into main/master/develop
   - Check last commit date for staleness
   - Calculate deletion recommendation
5. Build list of branches to delete (merged or stale)
6. Display analysis results to user
7. If interactive, ask for confirmation
8. If confirmed (or not interactive):
   - Delete local branches
   - If include_remote, delete from remote
   - Track successes and failures
9. Generate cleanup report with statistics
10. Return structured results

# Safety Features:
- Never deletes current branch
- Never deletes protected branches (main, master, develop)
- Default is dry_run=true (shows what would happen)
- Interactive confirmation by default
- Detailed logging of all operations
- Rollback information provided

# Example Usage:
```python
# Dry run (safe, shows what would be deleted)
python3 skills/git.cleanupbranches/git_cleanupbranches.py --dry-run

# Delete merged branches interactively
python3 skills/git.cleanupbranches/git_cleanupbranches.py --no-dry-run

# Delete branches stale for 60+ days
python3 skills/git.cleanupbranches/git_cleanupbranches.py --no-dry-run --stale-days 60

# Clean up remote branches too
python3 skills/git.cleanupbranches/git_cleanupbranches.py --no-dry-run --include-remote

# Non-interactive (CI/CD use)
python3 skills/git.cleanupbranches/git_cleanupbranches.py --no-dry-run --no-interactive --merged-only
```

# Output Format:
```json
{
  "status": "success",
  "analyzed": 25,
  "deleted": 5,
  "kept": 20,
  "branches_deleted": ["feature/old-feature", "fix/old-bug"],
  "branches_kept": ["feature/active", "main", "develop"],
  "protected": 3,
  "dry_run": false,
  "errors": []
}
```

# Tags:
- git
- cleanup
- maintenance
- branches
- automation

# Status: draft

# Notes:
This skill requires SKILL_AND_COMMAND pattern due to:
- 8-10 steps (exceeds threshold)
- Medium autonomy (analyzes and recommends deletions)
- Reusable for CI/CD and release workflows
- Complex logic with safety checks and interactive confirmation
