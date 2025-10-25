# Create Pull Request

Create GitHub pull request with auto-generated title and description from commits.

## What to do:

1. **Run the git.createpr skill**:
   ```bash
   export BETTY_CERT_MODE=dev
   python3 skills/git.createpr/git_createpr.py --output-format human
   ```

   This will:
   - Analyze commits between current branch and base (default: main)
   - Auto-generate PR title from most recent commit
   - Auto-generate PR description with commit list
   - Extract issue references (#123)
   - Detect labels from commit types (feat → enhancement, fix → bug, etc.)
   - Create PR using GitHub CLI (gh)

2. **Show analysis results**:
   - Display the generated PR title
   - Show PR description preview
   - List detected labels
   - Show linked issues

3. **Create the PR**:
   - The skill handles GitHub authentication via `gh` CLI
   - Returns PR URL and number
   - Displays all metadata

## Arguments:

The user may provide:
- **base** (string): Base branch for PR (default: main)
- **title** (string): Custom PR title (auto-generated if not provided)
- **draft** (boolean): Create as draft PR (default: false)
- **reviewers** (array): GitHub usernames to request reviews from
- **labels** (array): Custom labels (auto-detected if not provided)
- **body** (string): Custom PR description (auto-generated if not provided)

## Usage Examples:

```bash
# Create PR from current branch to main
/create-pr

# Create draft PR
/create-pr --draft

# Create PR with reviewers
/create-pr --reviewers alice bob

# Create PR to develop branch
/create-pr --base develop

# Create PR with custom title
/create-pr --title "feat: add user authentication"
```

## Auto-Generated Content:

### PR Title
- Uses most recent commit message
- Preserves conventional commit format (feat:, fix:, etc.)
- Falls back to first commit if not conventional

### PR Description
Includes:
- **Summary**: Overview of changes
- **Related Issues**: Auto-detected from #123 references
- **Commits**: Full list with hashes
- **Breaking Changes**: Warning if detected (BREAKING CHANGE or type!)

### Labels
Auto-detected from commit types:
- `feat:` → `enhancement`
- `fix:` → `bug`
- `docs:` → `documentation`
- `test:` → `testing`
- `chore:` → `maintenance`
- `perf:` → `performance`

## Requirements:

- ✅ GitHub CLI (`gh`) installed and authenticated
- ✅ In a git repository
- ✅ On a feature branch (not main/master)
- ✅ Commits exist between base and current branch
- ✅ Write access to repository

## Success Criteria:

- ✅ PR created successfully
- ✅ PR URL displayed
- ✅ Title auto-generated from commits
- ✅ Description includes all commits
- ✅ Issues linked automatically
- ✅ Labels applied based on commit types

## Notes:

- This is a SKILL_AND_COMMAND pattern (delegates to git.createpr skill)
- All complex logic is in the skill (500+ lines of Python)
- Command provides simple user interface
- Skill is reusable by agents and workflows
