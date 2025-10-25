# Name: skill-definition

# Purpose:
Complete skill configuration in YAML format. Defines skill metadata, inputs, outputs, artifact metadata, permissions, and entrypoints.

# Format: YAML

# File Pattern: skills/*/skill.yaml

# Content Type: application/yaml

# Schema Properties:
- name (string): Skill name
- version (string): Semantic version
- description (string): Skill purpose
- inputs (array): Input parameters
- outputs (array): Output files/artifacts
- artifact_metadata (object): Produces/consumes declarations
- permissions (array): Required permissions
- entrypoints (array): Command entrypoints with handlers

# Required Fields:
- name
- description
- permissions
- entrypoints

# Producers:
- meta.skill

# Consumers:
- plugin.sync (converts to plugin.yaml commands)
- meta.agent (selects skills for agents)
- Betty runtime

# Related Types:
- skill-implementation
- agent-definition
