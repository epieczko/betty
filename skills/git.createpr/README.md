# git.createpr

Create GitHub pull requests with auto-generated titles and descriptions based on commit analysis. Analyzes commit history, identifies related issues, and creates well-formatted PRs with proper linking and metadata. - git-commits - Commit history between base and feature branch - git-repository - Local git repository with commit information - github-credentials - GitHub token for API access (from gh CLI or environment) - pull-request - Created GitHub pull request with metadata - pr-report - Summary of PR creation including URL, number, and status - base_branch (string): Base branch for PR (default: main) - title (string): PR title (optional, auto-generated from commits if not provided) - draft (boolean): Create as draft PR (default: false) - auto_merge (boolean): Enable auto-merge if checks pass (default: false) - reviewers (array): List of GitHub usernames to request reviews from - labels (array): Labels to apply to PR (optional, auto-detected from commits) - body (string): PR description (optional, auto-generated if not provided) - git command line tool - GitHub CLI (gh) or GitHub API access with token - Access to git repository - GitHub repository with permissions to create PRs 1. Validate we're in a git repository 2. Get current branch name 3. Validate base branch exists 4. Fetch latest changes from remote 5. Get commit history between base and current branch 6. Analyze commits to extract: - Commit messages - Conventional commit types (feat, fix, docs, etc.) - Issue references (#123) - Breaking changes 7. Generate PR title (if not provided): - Use most recent commit message - Or summarize multiple commits - Format: "type(scope): description" 8. Generate PR description (if not provided): - Summary of changes - List of commits with links - Related issues section - Breaking changes warning (if any) 9. Detect labels from commit types: - feat → enhancement - fix → bug - docs → documentation - etc. 10. Create PR using GitHub CLI (gh pr create): - Set title and body - Set base and head branches - Apply labels - Request reviewers - Set draft status 11. Parse PR URL and number from output 12. Return structured result with PR metadata ```bash python3 skills/git.createpr/git_createpr.py python3 skills/git.createpr/git_createpr.py --draft python3 skills/git.createpr/git_createpr.py --reviewers alice bob python3 skills/git.createpr/git_createpr.py --base develop python3 skills/git.createpr/git_createpr.py --title "feat: add user authentication" python3 skills/git.createpr/git_createpr.py --labels enhancement breaking-change ``` ```json { "ok": true, "status": "success", "pr_number": 123, "pr_url": "https://github.com/owner/repo/pull/123", "title": "feat: add user authentication", "base_branch": "main", "head_branch": "feature/auth", "commits_analyzed": 5, "issues_linked": ["#45", "#67"], "labels_applied": ["enhancement", "feature"], "reviewers_requested": ["alice", "bob"], "is_draft": false } ``` - git - github - pull-request - automation - workflow - pr This skill requires SKILL_AND_COMMAND pattern due to: - 12 steps (exceeds threshold) - High autonomy (auto-generates PR content intelligently) - Highly reusable for release automation and CI/CD - Complex GitHub API interaction - Commit analysis and pattern detection - Multiple execution contexts (CLI, agents, workflows) This implementation uses GitHub CLI (gh) for simplicity and authentication: - Leverages existing gh authentication - Simpler than managing GitHub API tokens - Better error messages - Handles pagination automatically If gh CLI is not available, falls back to REST API with token from: - GITHUB_TOKEN environment variable - GH_TOKEN environment variable

## Overview

**Purpose:** Create GitHub pull requests with auto-generated titles and descriptions based on commit analysis. Analyzes commit history, identifies related issues, and creates well-formatted PRs with proper linking and metadata. - git-commits - Commit history between base and feature branch - git-repository - Local git repository with commit information - github-credentials - GitHub token for API access (from gh CLI or environment) - pull-request - Created GitHub pull request with metadata - pr-report - Summary of PR creation including URL, number, and status - base_branch (string): Base branch for PR (default: main) - title (string): PR title (optional, auto-generated from commits if not provided) - draft (boolean): Create as draft PR (default: false) - auto_merge (boolean): Enable auto-merge if checks pass (default: false) - reviewers (array): List of GitHub usernames to request reviews from - labels (array): Labels to apply to PR (optional, auto-detected from commits) - body (string): PR description (optional, auto-generated if not provided) - git command line tool - GitHub CLI (gh) or GitHub API access with token - Access to git repository - GitHub repository with permissions to create PRs 1. Validate we're in a git repository 2. Get current branch name 3. Validate base branch exists 4. Fetch latest changes from remote 5. Get commit history between base and current branch 6. Analyze commits to extract: - Commit messages - Conventional commit types (feat, fix, docs, etc.) - Issue references (#123) - Breaking changes 7. Generate PR title (if not provided): - Use most recent commit message - Or summarize multiple commits - Format: "type(scope): description" 8. Generate PR description (if not provided): - Summary of changes - List of commits with links - Related issues section - Breaking changes warning (if any) 9. Detect labels from commit types: - feat → enhancement - fix → bug - docs → documentation - etc. 10. Create PR using GitHub CLI (gh pr create): - Set title and body - Set base and head branches - Apply labels - Request reviewers - Set draft status 11. Parse PR URL and number from output 12. Return structured result with PR metadata ```bash python3 skills/git.createpr/git_createpr.py python3 skills/git.createpr/git_createpr.py --draft python3 skills/git.createpr/git_createpr.py --reviewers alice bob python3 skills/git.createpr/git_createpr.py --base develop python3 skills/git.createpr/git_createpr.py --title "feat: add user authentication" python3 skills/git.createpr/git_createpr.py --labels enhancement breaking-change ``` ```json { "ok": true, "status": "success", "pr_number": 123, "pr_url": "https://github.com/owner/repo/pull/123", "title": "feat: add user authentication", "base_branch": "main", "head_branch": "feature/auth", "commits_analyzed": 5, "issues_linked": ["#45", "#67"], "labels_applied": ["enhancement", "feature"], "reviewers_requested": ["alice", "bob"], "is_draft": false } ``` - git - github - pull-request - automation - workflow - pr This skill requires SKILL_AND_COMMAND pattern due to: - 12 steps (exceeds threshold) - High autonomy (auto-generates PR content intelligently) - Highly reusable for release automation and CI/CD - Complex GitHub API interaction - Commit analysis and pattern detection - Multiple execution contexts (CLI, agents, workflows) This implementation uses GitHub CLI (gh) for simplicity and authentication: - Leverages existing gh authentication - Simpler than managing GitHub API tokens - Better error messages - Handles pagination automatically If gh CLI is not available, falls back to REST API with token from: - GITHUB_TOKEN environment variable - GH_TOKEN environment variable

**Command:** `/git/createpr`

## Usage

### Basic Usage

```bash
python3 skills/git/createpr/git_createpr.py
```

### With Arguments

```bash
python3 skills/git/createpr/git_createpr.py \
  --output-format json
```

## Integration

This skill can be used in agents by including it in `skills_available`:

```yaml
name: my.agent
skills_available:
  - git.createpr
```

## Testing

Run tests with:

```bash
pytest skills/git/createpr/test_git_createpr.py -v
```

## Created By

This skill was generated by **meta.skill**, the skill creator meta-agent.

---

*Part of the Betty Framework*
