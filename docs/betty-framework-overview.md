---

## 📘 `docs/betty-framework-overview.md`

### 1. Overview

Explain the goal:

> Betty Framework is a self-bootstrapping skill system built on top of Claude Code.
> It can generate, validate, and register new Claude Code-compatible skills using its own skill chain.

### 2. Core Concepts

| Component     | Description                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Skill**     | Atomic unit of functionality. Each lives under `/skills/<name>/` with its own manifest, SKILL.md, and handler script. |
| **Agent**     | Higher-level process combining multiple skills into workflows.                                                        |
| **Registry**  | JSON catalog at `/registry/skills.json` tracking every skill’s metadata and status.                                   |
| **Lifecycle** | `skill.create → skill.define → registry.update → (future) workflow.compose`.                                          |

### 3. Current Implemented Skills

| Skill                 | Purpose                                                    | Key Files                                                             |
| --------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------- |
| **`skill.create`**    | Scaffolds new skill folders and manifests.                 | `skills/skill.create/skill_create.py`, `skill.yaml`, `SKILL.md`       |
| **`skill.define`**    | Validates and registers skill manifests.                   | `skills/skill.define/skill_define.py`, `skill.yaml`, `SKILL.md`       |
| **`registry.update`** | Updates `/registry/skills.json` for new or changed skills. | `skills/registry.update/registry_update.py`, `skill.yaml`, `SKILL.md` |

### 4. How the Bootstrapping Loop Works

```
[skill.create] → generates new skill folder + manifest
       ↓
[skill.define] → validates the manifest
       ↓
[registry.update] → adds it to registry/skills.json
```

Each skill calls the next as a subprocess so Betty can self-maintain.

### 5. Directory Layout

```
betty-framework/
├── docs/
│   └── betty-framework-overview.md
├── registry/
│   └── skills.json
├── skills/
│   ├── skill.create/
│   ├── skill.define/
│   └── registry.update/
└── tools/        (optional utilities)
```

### 6. Running Locally

```bash
# Create a new skill
python skills/skill.create/skill_create.py workflow.compose "Compose and orchestrate workflows"

# Validate a skill
python skills/skill.define/skill_define.py skills/workflow.compose/skill.yaml

# Update registry explicitly
python skills/registry.update/registry_update.py skills/workflow.compose/skill.yaml
```

### 7. Next Milestones

* Add **`workflow.compose`** to orchestrate multi-step operations.
* Package everything into a Claude Code plugin (`plugin.yaml`) so `/skill/create` etc. run natively inside Claude.
* Add documentation generation (`generate.docs` skill) to automate SKILL.md creation.

---
