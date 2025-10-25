# Name: code.reviewer

# Purpose:
Analyzes code changes and provides comprehensive feedback on code quality,
security vulnerabilities, performance issues, and adherence to best practices.

# Inputs:
- code-diff
- coding-standards (optional)

# Outputs:
- review-report
- suggestion-list

# Skills Needed:
- static-analysis
- security-scan
- style-check

# Implementation Notes:
The agent should:
1. Analyze code changes for security vulnerabilities (SQL injection, XSS, etc.)
2. Check code style against configured standards (PEP8, ESLint, etc.)
3. Identify performance issues (N+1 queries, inefficient algorithms)
4. Detect code smells (long methods, god objects, duplicated code)
5. Suggest improvements with specific examples
6. Provide severity ratings (critical, high, medium, low)

Output should include:
- List of issues found with line numbers
- Severity and category for each issue
- Suggested fixes with code examples
- Overall code quality score
- Compliance status with coding standards

The review report should be actionable and developer-friendly.
