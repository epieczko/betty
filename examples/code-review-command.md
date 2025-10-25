# Name: /code-review
# Version: 0.1.0
# Description: Perform intelligent code review with context-aware analysis

# Execution Type: agent
# Target: code.reviewer

# Parameters:
- file_path: string (required) - Path to file or directory to review
- severity: enum (optional, default=all, values=[all,critical,high,medium,low]) - Minimum severity to report
- format: enum (optional, default=markdown, values=[markdown,json]) - Output format

# Status: active

# Tags: code-review, quality, agent-example

## Instructions

This command delegates to the code.reviewer agent which performs intelligent,
context-aware code analysis.

The agent will:
1. Understand the project context and coding standards
2. Analyze code logic, design, and quality
3. Identify bugs, security issues, and code smells
4. Evaluate readability and maintainability
5. Generate prioritized, actionable recommendations

The agent uses reasoning to:
- Consider trade-offs between different approaches
- Adapt recommendations to project context
- Assess qualitative aspects like code clarity
- Make judgment calls about design decisions
