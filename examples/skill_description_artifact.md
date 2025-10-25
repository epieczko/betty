# Name: skill-description

# Purpose:
Natural language description of a skill's requirements, inputs, outputs, and implementation details. Used by meta.skill to generate complete skill implementations.

# Format: Markdown

# File Pattern: **/skill_description.md

# Content Type: text/markdown

# Schema Properties:
- name (string): Skill name in domain.action format
- purpose (string): What the skill does
- inputs (array): Input parameters or artifact types
- outputs (array): Output artifact types
- permissions (array): Required permissions
- implementation_notes (string): Implementation guidance

# Required Fields:
- name
- purpose

# Producers:
- Developers (manual creation)

# Consumers:
- meta.skill

# Related Types:
- skill-definition
- agent-description
