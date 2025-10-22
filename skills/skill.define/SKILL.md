---
name: Skill Define
description: Validate and register new Claude Code Skill manifests (.skill.yaml) to ensure structure, inputs/outputs, and dependencies are correct.
---

# Skill Define

## Purpose
Acts as the compiler and registrar for Betty Framework skills.
Ensures each `skill.yaml` conforms to schema and governance rules before registration.

## How to Use
Run the validator directly with Python:
```bash
python skills/skill.define/skill_define.py skills/workflow.compose/skill.yaml
