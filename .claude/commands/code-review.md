# Code Review

Perform intelligent code review with context-aware analysis.

## What to do:

1. **Invoke the code reviewer agent**:
   - The agent will analyze the code with reasoning and context understanding
   - Agent: code.reviewer
   - Note: This is an AGENT pattern example - requires reasoning and judgment

2. **Agent analyzes**:
   - Understands project context and coding standards
   - Identifies bugs, security issues, and code smells
   - Evaluates readability and maintainability
   - Makes judgment calls about design trade-offs

3. **Present results**:
   - Show overall quality score
   - List findings by priority (critical, high, medium, low)
   - Provide specific, actionable recommendations
   - Include code examples where helpful

4. **Discuss recommendations**:
   - Explain the reasoning behind each recommendation
   - Discuss trade-offs and alternatives
   - Prioritize by impact vs. effort

## Arguments:

The user will provide:
- Path to file or directory to review
- Optional: Severity filter (all, critical, high, medium, low)
- Optional: Output format (markdown, json)

## Success Criteria:

- ✅ Code thoroughly analyzed with context understanding
- ✅ Issues identified and prioritized
- ✅ Actionable recommendations provided
- ✅ Reasoning explained for key suggestions

## Pattern Note:

This command uses the **AGENT** execution pattern because:
- Requires reasoning and context understanding
- Makes qualitative judgments about code quality
- Adapts recommendations to project context
- Cannot be fully automated with deterministic rules
