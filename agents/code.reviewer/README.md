# Code.Reviewer Agent

## Purpose

Analyzes code changes and provides comprehensive feedback on code quality, security vulnerabilities, performance issues, and adherence to best practices.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `code-diff`
- `coding-standards`

### Produces

- `review-report`
- `suggestion-list`
- `static-analysis`
- `security-scan`
- `style-check`
- `List of issues found with line numbers`
- `Severity and category for each issue`
- `Suggested fixes with code examples`
- `Overall code quality score`
- `Compliance status with coding standards`

## Usage

```bash
# Activate the agent
/agent code.reviewer

# Or invoke directly
betty agent run code.reviewer --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
