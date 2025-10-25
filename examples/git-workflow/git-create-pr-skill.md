# Name: git.create-pr

# Version: 1.0.0

# Purpose:
Create GitHub pull requests with auto-generated titles and descriptions based on commit analysis. Analyzes commit history, identifies related issues, and creates well-formatted PRs with proper linking.

# Category: git-workflow

# Inputs (Consumes):
- git-commits - List of commits between base and feature branch
- github-token - Authentication for GitHub API

# Outputs (Produces):
- pull-request - Created GitHub pull request with metadata
- pr-report - Summary of PR creation including URL and status

# Parameters:
- base_branch (string): Base branch for PR (default: main)
- draft (boolean): Create as draft PR (default: false)
- auto_merge (boolean): Enable auto-merge if checks pass (default: false)
- reviewers (array): List of GitHub usernames to request reviews from

# Dependencies:
- git command line tool
- GitHub CLI (gh) or GitHub API access
- Access to git repository

# Steps:
1. Get current branch name
2. Fetch latest changes from remote
3. Analyze commit history between base and current branch
4. Extract commit messages and identify patterns
5. Generate PR title from commits
6. Generate PR description with:
   - Summary of changes
   - List of commits
   - Related issues (detected from commit messages)
7. Identify related GitHub issues from commit messages
8. Create PR via GitHub API
9. Apply labels based on commit analysis
10. Request reviewers if specified
11. Link to project board if configured
12. Return PR URL and metadata

# Examples:
- Create PR from feature branch to main
- Create draft PR for work-in-progress
- Create PR with auto-generated description and issue linking

# Tags:
- git
- github
- pull-request
- automation
- workflow

# Status: draft

# Notes:
This skill requires SKILL_AND_COMMAND pattern due to:
- 10+ steps (exceeds complexity threshold)
- High autonomy (auto-generates PR content)
- Highly reusable for release automation and CI/CD
- Complex GitHub API interaction
