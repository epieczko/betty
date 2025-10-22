---
name: Registry Update
description: Updates the Betty Framework Skill Registry when new skills are created or validated.
---

# Registry Update

## Purpose
The `registry.update` skill centralizes all changes to `/registry/skills.json`.  
Instead of each skill writing to the registry directly, they call this skill to ensure consistency.

## How to Use
Run locally:
```bash
python skills/registry.update/registry_update.py skills/skill.create/skill.yaml
