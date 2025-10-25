# Commit

Interactive git commit helper with best practices validation.

## What to do:

1. **Show current repository status**:
   - Run: `git status`
   - Show what files have changed
   - Show what's staged vs unstaged

2. **Show the diff**:
   - Run: `git diff` for unstaged changes
   - Run: `git diff --staged` for staged changes
   - Help user understand what will be committed

3. **If nothing is staged, ask what to stage**:
   - Show list of changed files
   - Ask user which files to stage
   - Run: `git add <files>` for selected files
   - Or suggest: `git add .` to add everything

4. **Get commit message from user**:
   - Ask for commit message
   - Validate the commit message format:
     - Check if it follows conventional commits (optional but suggested)
     - Should be clear and descriptive
     - Suggest format: `type(scope): description`
     - Types: feat, fix, docs, style, refactor, test, chore

5. **Validate commit message best practices**:
   - ✅ Not too short (minimum 10 characters)
   - ✅ Not too long (maximum 72 characters for summary)
   - ✅ Starts with lowercase (after type prefix)
   - ✅ No period at end of summary line
   - ✅ Descriptive and meaningful

   If message doesn't follow best practices, suggest improvements

6. **Create the commit**:
   - Run: `git commit -m "message"`
   - If multi-line message, use appropriate format
   - Show commit hash and summary

7. **Ask about pushing**:
   - Show current branch
   - Ask: "Would you like to push to remote?"
   - If yes:
     - Check if branch has upstream: `git rev-parse --abbrev-ref @{upstream}`
     - If no upstream: `git push -u origin <branch>`
     - If has upstream: `git push`
   - Show push results

## Arguments:

The user may provide:
- **message** (string): Commit message (optional, will prompt if not provided)
- **add-all** (boolean): Add all changes before committing (default: false)
- **push** (boolean): Automatically push after commit (default: false)
- **no-verify** (boolean): Skip pre-commit hooks (NOT recommended)

## Usage Examples:

```bash
# Interactive commit
/commit

# Commit with message
/commit --message "feat: add user authentication"

# Add all and commit
/commit --add-all --message "fix: resolve login bug"

# Commit and push
/commit --push --message "docs: update README"

# Multi-line commit (interactive)
/commit
# You'll be prompted for message and can provide:
# feat: add new feature
#
# This adds support for X, Y, and Z
# - Detail 1
# - Detail 2
```

## Commit Message Format (Conventional Commits):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

**Examples:**
- `feat: add user registration`
- `fix(auth): resolve token expiration issue`
- `docs: update installation guide`
- `refactor(api): simplify error handling`
- `test: add unit tests for user service`

## Success Criteria:

- ✅ User sees current git status
- ✅ User understands what will be committed
- ✅ Commit message follows best practices
- ✅ Commit is created successfully
- ✅ User knows commit hash
- ✅ Optional: Changes pushed to remote

## Notes:

- This is a HYBRID command (orchestrates multiple git operations)
- Provides interactive guidance through the commit process
- Validates commit messages against best practices
- Safe: shows diffs before committing
- Optional: integrates with existing hooks if configured
