# Name: git.workflow

# Purpose:
Orchestrate end-to-end git workflows from branch creation to PR merging. Automates common git operations including branch management, PR creation, code review, and issue resolution. Provides intelligent workflow recommendations based on repository state and team practices.

# Inputs:
- github-issue - GitHub issue to work on
- git-branch - Branch to work with
- workflow-config - Team's git workflow configuration

# Outputs:
- pull-request - Created or updated GitHub PR
- branch-cleanup-report - Summary of branch cleanup operations
- workflow-report - Overall workflow execution summary
- review-report - Code review results and recommendations

# Capabilities:
- Create feature branches from GitHub issues
- Analyze commits and generate PR descriptions
- Automate branch cleanup for merged/stale branches
- Coordinate PR creation with proper linking and labeling
- Suggest workflow improvements based on repository patterns

# Workflow Patterns:
- Feature Development: issue → branch → commits → PR → review → merge
- Bug Fix: issue → branch → fix → tests → PR → merge
- Release: version bump → changelog → branch cleanup → release PR

# Skills Needed:
The meta.agent will automatically compose these based on purpose:
- git.create-pr - Create pull requests with auto-generated content
- git.cleanup-branches - Clean up merged and stale branches
- git.fix-issue - Automated issue resolution workflow
- git.review-pr - Automated PR review and analysis
- workflow.compose - Orchestrate multi-step workflows

# Permissions:
- filesystem:read - Read git repository state
- filesystem:write - Create branches, commits
- network:github - GitHub API access for PRs and issues
- exec:git - Execute git commands

# Examples:
- "Create a feature branch for issue #123 and set up PR draft"
- "Clean up all merged branches from the last release"
- "Create PR for current branch with reviewers from CODEOWNERS"
- "Orchestrate bug fix workflow for issue #456"
- "Prepare release branch with changelog and cleanup"

# Status: draft

# Tags:
- git
- github
- workflow
- automation
- orchestration

# Notes:
This agent will be created using meta.agent, which will automatically:
1. Use agent.compose to find compatible skills
2. Generate proper artifact metadata
3. Infer required permissions from skills
4. Create complete agent.yaml and README.md

After creation, validate with:
```bash
python3 agents/meta.compatibility/meta_compatibility.py analyze git.workflow
```
