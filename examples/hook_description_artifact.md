# Name: hook-description

# Purpose:
Natural language description of a Claude Code hook's purpose, trigger event, and command to execute. Used by meta.hook to generate hook configurations.

# Format: Markdown

# File Pattern: **/hook_description.md

# Content Type: text/markdown

# Schema Properties:
- name (string): Hook name (descriptive identifier)
- event (string): Trigger event (e.g., before-tool-call, after-tool-call, on-error)
- description (string): What the hook does
- command (string): Shell command to execute
- enabled (boolean): Whether hook is active (default: true)
- tool_filter (string, optional): Only trigger for specific tools

# Required Fields:
- name
- event
- description
- command

# Producers:
- Developers (manual creation)

# Consumers:
- meta.hook

# Related Types:
- hook-config
- agent-definition
