---
name: Workflow Compose
description: Executes multi-step workflows by chaining Betty Framework skills.
---

# Workflow Compose

## Purpose
Allows declarative execution of Betty Framework workflows by reading a YAML definition and chaining skills like `skill.create`, `skill.define`, and `registry.update`.

## Example Workflow File
```yaml
# workflows/create_and_register.yaml
steps:
  - skill: skill.create
    args: ["workflow.validate", "Validates workflow definitions"]
  - skill: skill.define
    args: ["skills/workflow.validate/skill.yaml"]
  - skill: registry.update
    args: ["skills/workflow.validate/skill.yaml"]
