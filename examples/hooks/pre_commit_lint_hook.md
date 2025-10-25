# Name: pre-commit-lint

# Event: before-tool-call

# Tool Filter: git

# Description: Run linter before git commits to ensure code quality and catch style issues early

# Command: ruff check . && mypy .

# Timeout: 30000

# Enabled: true
