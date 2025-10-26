# Name: suggestion-report

# Purpose:
Context-aware recommendations for what to do next after an agent completes. Includes ranked suggestions with rationale, required artifacts, and expected outcomes.

# Format: JSON

# File Pattern: *.suggestions.json

# Content Type: application/json

# Schema Properties:

# Required Fields:

# Producers:
- meta.suggest

# Consumers:
- Claude (for decision making)
- dashboard.display
- workflow.orchestrator

# Examples:

# Validation Rules:

# Related Types:
