# Betty Framework

> **Claude Code thinks. Betty builds.**

Betty Framework is **RiskExec’s system for structured, auditable AI-assisted engineering** built on Anthropic’s Claude Code Plugins platform.  
Where Claude Code provides the runtime, plugin model, and marketplace for extending AI development, **Betty adds methodology, orchestration, and governance**—turning raw agent capability into a repeatable, enterprise-grade engineering discipline.

---

## 🌐 Mission and Inspiration

Named for **Betty Shannon (1922 – 2017)**—the electrical engineer and mathematician who helped translate Claude Shannon’s theory of information into applied computation—  
Betty embodies the spirit of **turning reasoning into engineered systems**.

> Claude Code thinks. Betty builds.

---

## 🧭 Purpose and Scope

Betty extends Claude Code Plugins into a structured engineering layer that:

* Defines **standardized workflows** (specify → plan → implement → verify).  
* Establishes **governance and auditability** for every agent action.  
* Integrates with **enterprise orchestrators and compliance systems**.  
* Enables **composable engineering** through curated Claude Code Plugins published in the RiskExec Marketplace.

Betty doesn’t modify the Claude Code runtime—it **configures and disciplines** it, providing conventions for how plugins, agents, and teams interact.

---

## ⚙️ How Betty Builds on Claude Code

| Claude Code Provides | Betty Adds |
|----------------------|------------|
| Plugin runtime & manifest model | Structured engineering lifecycle |
| Agent & tool integration (via MCP) | Governance, context schema, traceability |
| Public & private marketplaces | Curated RiskExec Marketplace with certified plugins |
| Command execution & logging | Multi-phase orchestration and artifact lineage |
| Context & memory APIs | Enterprise analytics, QA, and policy enforcement |

---

## 🧩 Current Core Skills

Betty’s self-referential “kernel” of skills bootstraps the rest of the system:

| Skill | Purpose |
|--------|----------|
| **skill.create** | Scaffolds new skill directories and manifests. |
| **skill.define** | Validates and registers skill manifests. |
| **registry.update** | Adds or modifies entries in `/registry/skills.json`. |
| **workflow.compose** | Executes declarative YAML workflows chaining skills together. |

These four form the baseline for an **AI-native SDLC** where creation, validation, registration, and orchestration are themselves skills.

---

## 🧱 Repository Structure

```

betty-framework/
├── docs/
│   ├── betty-framework-overview.md
│   └── references.md
├── skills/
│   ├── skill.create/
│   ├── skill.define/
│   ├── registry.update/
│   └── workflow.compose/
├── registry/
│   ├── skills.json
│   └── workflow_history.json
└── workflows/
└── example_create_and_register.yaml

````

---

## 🚀 Example Usage

```bash
# 1 · Create a new skill
python skills/skill.create/skill_create.py workflow.validate "Validates workflow YAML definitions"

# 2 · Validate its manifest
python skills/skill.define/skill_define.py skills/workflow.validate/skill.yaml

# 3 · Update the registry
python skills/registry.update/registry_update.py skills/workflow.validate/skill.yaml

# 4 · Run the entire process as a workflow
python skills/workflow.compose/workflow_compose.py workflows/example_create_and_register.yaml
````

Each step logs to `/registry/skills.json` and `/registry/workflow_history.json`.

---

## 🧠 Design Principles

* **Structure over improvisation** — Every workflow step is defined, typed, and reproducible.
* **Human oversight first** — Developers can approve, correct, or extend any agent output.
* **Composable by default** — Skills can be rearranged or replaced without breaking the system.
* **Audit as a feature** — Provenance and traceability are built-in, not bolted-on.
* **Future-ready** — Engineered for multi-agent collaboration and adaptive workflows.

---

## 🔭 Planned Expansion

| Area                         | Skill / Feature     | Description                                                   |
| ---------------------------- | ------------------- | ------------------------------------------------------------- |
| **Workflow Validation**      | `workflow.validate` | Ensures workflow YAML schema correctness before execution.    |
| **Documentation Generation** | `generate.docs`     | Auto-creates `SKILL.md` from each `skill.yaml`.               |
| **Governance Policies**      | `policy.enforce`    | Enforces naming rules, permissions, and compliance policies.  |
| **Observability**            | `telemetry.capture` | Collects runtime metrics and logs for skills and agents.      |
| **Versioning**               | `registry.diff`     | Tracks manifest deltas and release history.                   |
| **Marketplace Integration**  | `plugin.publish`    | Publishes certified Betty skills to Claude Code marketplaces. |

---

## 📚 Documentation

* `docs/betty-framework-overview.md` — Full lifecycle and architecture
* `docs/references.md` — Official Claude Code API and plugin references

---

## ⚙️ Requirements

* Python 3.11 or newer
* PyYAML (`pip install pyyaml`)
* (Optional) Claude Code runtime for plugin execution

---

## 🧭 Roadmap

1. **Core Stabilization** — Improve error handling and atomic writes.
2. **Governance Layer** — Add `policy.enforce` and compliance logging.
3. **Plugin Packaging** — Introduce `plugin.yaml` for native Claude commands.
4. **Marketplace Integration** — Enable publishing and certification of skills.
5. **Agent Collaboration** — Expand from skills → workflows → multi-agent systems.

---

## 🤝 Contributing

1. Use lowercase, dot-separated names (e.g., `domain.action`).
2. Include `skill.yaml`, `SKILL.md`, and a handler script for each skill.
3. Validate via `skill.create → skill.define → registry.update` before commit.
4. Submit PRs with clear workflow examples and registry entries set to `active`.


