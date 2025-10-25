# Name: create-pr

# Description:
Create a GitHub pull request from the current branch with auto-generated title and description.

# Execution Type: skill

# Target: git.create-pr

# Status: draft

# Version: 1.0.0

# Parameters:
- base (string): Base branch for PR (default: main)
- draft (boolean): Create as draft PR (default: false)
- reviewers (array): GitHub usernames to request reviews from

# Usage Examples:
```bash
# Create PR to main branch
/create-pr

# Create draft PR
/create-pr --draft

# Create PR with reviewers
/create-pr --reviewers alice,bob

# Create PR to develop branch
/create-pr --base develop
```

# Instructions:
1. Invoke the git.create-pr skill with provided parameters
2. Display the PR URL to the user
3. Show PR summary including:
   - PR number
   - Title
   - Base and head branches
   - Reviewers requested
   - Link to view PR on GitHub

# Notes:
This is a simple delegation command. All complex logic lives in git.create-pr skill.
This allows the skill to be reused by agents and workflows while users get a simple /create-pr interface.
