# Name: pre-commit-test

# Event: before-tool-call

# Tool Filter: git

# Description: Run test suite before commits to prevent broken code from being committed

# Command: pytest tests/ -v --tb=short

# Timeout: 60000

# Enabled: true
