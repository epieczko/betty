# Branch Cleanup

Clean up merged and stale git branches both locally and optionally on the remote.

## What to do:

1. **Run the git.cleanupbranches skill**:
   - By default, run in **dry-run mode** (safe, shows what would be deleted):
     ```bash
     python3 skills/git.cleanupbranches/git_cleanupbranches.py --dry-run
     ```
   - This analyzes all branches and shows which would be deleted

2. **Show the analysis results**:
   - Display the list of branches that would be deleted
   - Show the reason for each (merged or stale)
   - Show branches that will be kept (current, protected, active)

3. **If user wants to actually delete branches**:
   - Ask for confirmation
   - Run with `--no-dry-run`:
     ```bash
     python3 skills/git.cleanupbranches/git_cleanupbranches.py --no-dry-run
     ```
   - The skill will ask for interactive confirmation before deleting

4. **Options to offer**:
   - `--stale-days N`: Consider branches stale after N days (default: 30)
   - `--merged-only`: Only delete merged branches, ignore stale ones
   - `--include-remote`: Also delete branches from remote repository
   - `--no-interactive`: Skip confirmation (for automation)
   - `--protected-branches`: Specify additional branches to protect

5. **Safety features to mention**:
   - ✅ Default is dry-run (safe)
   - ✅ Never deletes current branch
   - ✅ Never deletes protected branches (main, master, develop, development)
   - ✅ Interactive confirmation by default
   - ✅ Detailed analysis before deletion

## Arguments:

The user may provide:
- **dry-run** (boolean): Show what would be deleted without deleting (default: true)
- **stale-days** (integer): Consider branches stale after N days (default: 30)
- **merged-only** (boolean): Only delete merged branches (default: false)
- **include-remote** (boolean): Also clean up remote branches (default: false)
- **interactive** (boolean): Ask for confirmation (default: true)

## Usage Examples:

```bash
# Safe dry run (default) - shows what would be deleted
/branch-cleanup

# Delete merged branches interactively
/branch-cleanup --no-dry-run --merged-only

# Delete branches stale for 60+ days
/branch-cleanup --no-dry-run --stale-days 60

# Clean up remote branches too (be careful!)
/branch-cleanup --no-dry-run --include-remote

# Non-interactive for automation
/branch-cleanup --no-dry-run --no-interactive --merged-only
```

## Success Criteria:

- ✅ Branch analysis completed
- ✅ User understands which branches would be/were deleted
- ✅ User knows the reason for each deletion (merged or stale)
- ✅ Protected branches are never touched
- ✅ User is prompted for confirmation (unless --no-interactive)

## Important Safety Notes:

Always start with dry-run mode to see what would happen:
1. First run: `/branch-cleanup` (dry-run)
2. Review the list
3. If OK, run: `/branch-cleanup --no-dry-run`

**Warning:** Use `--include-remote` carefully - deleting remote branches affects the entire team!
