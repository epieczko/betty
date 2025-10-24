# Name: pipeline-suggestion

# Purpose:
Suggested multi-agent workflow with step-by-step execution plan. Ensures artifact compatibility and provides rationale for agent selection.

# Format: JSON

# File Pattern: *.pipeline.json

# Content Type: application/json

# Schema Properties:
- name (string): Pipeline name
- description (string): What this pipeline accomplishes
- steps (array): Ordered list of agents to execute
- artifact_flow (array): How artifacts flow between steps
- rationale (string): Why this pipeline works
- confidence (string): Confidence level (high, medium, low)
- estimated_duration (string): Expected execution time

# Required Fields:
- name
- steps
- artifact_flow

# Producers:
- meta.compatibility
- meta.suggest

# Consumers:
- workflow.orchestrator
- Claude (for decision making)

# Related Types:
- compatibility-graph
- workflow-definition
- agent-definition
