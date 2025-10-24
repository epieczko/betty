# Name: compatibility-graph

# Purpose:
Agent relationship graph showing which agents can work together based on artifact flows. Maps producers to consumers, enabling intelligent multi-agent orchestration.

# Format: JSON

# File Pattern: *.compatibility.json

# Content Type: application/json

# Schema Properties:
- agents (array): List of agents in the graph
- relationships (array): Compatible agent pairs with artifact flows
- pipelines (array): Suggested multi-agent workflows
- gaps (array): Missing artifacts or incompatibilities
- metadata (object): Analysis timestamp and version

# Required Fields:
- agents
- relationships

# Producers:
- meta.compatibility

# Consumers:
- meta.suggest
- dashboard.display
- workflow.orchestrator

# Related Types:
- agent-definition
- pipeline-suggestion
- artifact-definition
