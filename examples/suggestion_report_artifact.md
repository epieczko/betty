# Name: suggestion-report

# Purpose:
Context-aware recommendations for what to do next after an agent completes. Includes ranked suggestions with rationale, required artifacts, and expected outcomes.

# Format: JSON

# File Pattern: *.suggestions.json

# Content Type: application/json

# Schema Properties:
- context (object): Current context (agent that ran, artifacts produced)
- suggestions (array): Ranked list of recommended next steps
- primary_suggestion (object): Best recommendation with detailed rationale
- alternatives (array): Alternative options
- warnings (array): Things to be aware of

# Required Fields:
- context
- suggestions
- primary_suggestion

# Producers:
- meta.suggest

# Consumers:
- Claude (for decision making)
- dashboard.display
- workflow.orchestrator

# Related Types:
- compatibility-graph
- pipeline-suggestion
- agent-definition
