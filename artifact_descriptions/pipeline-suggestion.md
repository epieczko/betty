# Name: pipeline-suggestion

# Purpose:
Suggested multi-agent workflow with step-by-step execution plan. Ensures artifact compatibility and provides rationale for agent selection.

# Format: JSON

# File Pattern: *.pipeline.json

# Content Type: application/json

# Schema Properties:

# Required Fields:

# Producers:
- meta.compatibility
- meta.suggest

# Consumers:
- workflow.orchestrator
- Claude (for decision making)

# Examples:

# Validation Rules:

# Related Types:
