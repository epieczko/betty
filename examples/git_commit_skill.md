# Name: git.commit

# Purpose:
Generate descriptive commit messages by analyzing git diffs. Helps developers write clear, consistent commit messages following conventional commits format with proper types (feat, fix, docs, etc.) and scopes.

# Inputs:
- git_diff (optional - auto-detected from staged changes if not provided)
- scope (optional - e.g., api, ui, database)

# Outputs:
- commit_message (conventional commits format)
- commit_type (detected type: feat, fix, docs, refactor, test, chore, style)

# Permissions:
- filesystem:read

# Produces Artifacts:
- commit-message

# Implementation Notes:
Analyze staged git changes to determine the type of commit (feature, fix, refactor, etc.). Generate commit messages following conventional commits format: `<type>(<scope>): <description>`. Include guidelines for:
- Using imperative mood
- Keeping summary under 50 characters
- Explaining WHY not just WHAT
- Marking breaking changes
- Following atomic commit principles

Provide comprehensive documentation with examples, templates, and best practices checklist.

# Examples:
- Generate commit message for staged API changes
- Suggest commit type based on file modifications
- Help write multi-file commit message with proper scope
- Guide user through conventional commits format

# Tags:
- git
- commit
- conventional-commits
- documentation
- developer-tools
- best-practices
