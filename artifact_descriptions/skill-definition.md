# Name: skill-definition

# Purpose:
Complete skill configuration in YAML format. Defines skill metadata, inputs, outputs, artifact metadata, permissions, and entrypoints.

# Format: YAML

# File Pattern: skills/*/skill.yaml

# Content Type: application/yaml

# Schema Properties:

# Required Fields:

# Producers:
- meta.skill

# Consumers:
- plugin.sync (converts to plugin.yaml commands)
- meta.agent (selects skills for agents)
- Betty runtime

# Examples:

# Validation Rules:

# Related Types:
