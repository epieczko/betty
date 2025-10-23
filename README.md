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

Betty's self-referential "kernel" of skills bootstraps the rest of the system:

### Foundation Skills

| Skill | Purpose |
|--------|----------|
| **registry.update** | Updates the Betty Framework Skill Registry by adding or modifying entries based on validated skill manifests. |
| **skill.create** | Generates a new Betty Framework Skill directory and manifest. Used to bootstrap new Claude Code-compatible skills inside the Betty Framework. |
| **skill.define** | Validates and registers skill manifests (.skill.yaml) for the Betty Framework. Ensures schema compliance and updates the Skill Registry. |
| **workflow.compose** | Executes multi-step Betty Framework workflows by chaining existing skills. Enables declarative orchestration of skill pipelines. |
| **workflow.validate** | Validates Betty workflow YAML definitions to ensure correct structure and required fields. |

### API Development Skills

| Skill | Purpose |
|--------|----------|
| **api.compatibility** | Detect breaking changes between API specification versions |
| **api.define** | Create OpenAPI and AsyncAPI specifications from templates |
| **api.generate-models** | Generate type-safe models from OpenAPI and AsyncAPI specifications using Modelina |
| **api.validate** | Validate OpenAPI and AsyncAPI specifications against enterprise guidelines |

### Infrastructure Skills

| Skill | Purpose |
|--------|----------|
| **agent.define** | Validates and registers agent manifests for the Betty Framework. Ensures schema compliance, validates skill references, and updates the Agent Registry. |
| **agent.run** | Execute a registered Betty agent by loading its manifest, generating a Claude-friendly prompt, invoking skills based on the agent's workflow, and logging results. Supports both iterative and oneshot reasoning modes with optional Claude API integration. |
| **command.define** | Validate and register command manifests in the Command Registry |
| **docs.sync.readme** | Regenerate the top-level README.md to reflect all current registered skills and agents. Pulls from registry/skills.json and registry/agents.json, groups by category, and updates documentation sections while maintaining repo style and tone. |
| **generate.marketplace** | Generate marketplace catalog files from Betty Framework registries. Filters active and certified skills/agents and outputs marketplace-ready JSON files. |
| **hook.define** | Create and register validation hooks for Claude Code |
| **hook.register** | Validate and register hook manifests in the Hook Registry |
| **plugin.build** | Automatically bundle a plugin directory (or the whole repo) into a deployable Claude Code plugin package. Gathers all declared entrypoints, validates handler files exist, and packages everything into .tar.gz or .zip under /dist. |
| **plugin.sync** | Automatically generates plugin.yaml from Betty Framework registries. Reads skills.json, commands.json, and hooks.json to build a complete plugin configuration. |
| **policy.enforce** | Validates operations against organizational policies before execution |
| **run.agent** | Simulates execution of a Betty agent by loading its manifest, constructing the prompt, and demonstrating which skills would be invoked. Useful for testing agent design and understanding agent behavior. |

These skills form the baseline for an **AI-native SDLC** where creation, validation, registration, and orchestration are themselves skills.
---

## 🧱 Repository Structure

```
betty-framework/
├── betty/                         # Shared Python utilities
│   ├── config.py                  # Configuration constants and paths
│   ├── validation.py              # Validation utility functions
│   ├── logging_utils.py           # Logging infrastructure
│   ├── file_utils.py              # File operations with locking
│   └── errors.py                  # Custom exception classes
│
├── docs/                          # Documentation
│   ├── betty-framework-overview.md    # High-level architecture overview
│   ├── betty-architecture.md          # Five-layer model details
│   ├── CODEBASE_ANALYSIS.md          # Technical codebase analysis
│   ├── COMMAND_HOOK_INFRASTRUCTURE.md # Commands & hooks documentation
│   ├── api-driven-development.md     # API-first workflow guide
│   ├── skills-framework.md           # Skills taxonomy and design
│   ├── multi-llm-integration-paths.md # Multi-LLM integration options
│   ├── references.md                  # External documentation links
│   ├── glossary.md                    # Betty terminology reference
│   └── contributing.md                # Contribution guidelines
│
├── skills/                        # Skills implementation
│   ├── skill.create/              # Scaffold new skills
│   ├── skill.define/              # Validate skill manifests
│   ├── registry.update/           # Update skill registry
│   ├── workflow.compose/          # Execute workflows
│   ├── workflow.validate/         # Validate workflow YAML
│   ├── agent.define/              # Validate & register agents
│   ├── command.define/            # Validate & register commands
│   ├── hook.define/               # Create validation hooks
│   ├── hook.register/             # Register hook manifests
│   ├── api.define/                # Create API specifications
│   ├── api.validate/              # Validate API specs
│   ├── api.generate-models/       # Generate models from specs
│   ├── api.compatibility/         # Check API compatibility
│   ├── policy.enforce/            # Enforce organizational policies
│   └── audit.log/                 # Audit trail logging
│
├── agents/                        # Intelligent orchestrators
│   ├── api.designer/              # Design APIs with iterative refinement
│   │   ├── agent.yaml             # Agent manifest
│   │   └── README.md              # Agent documentation
│   └── api.analyzer/              # Analyze API compatibility
│       ├── agent.yaml
│       └── README.md
│
├── .claude/                       # Claude Code integration
│   ├── commands/                  # Slash command definitions
│   │   ├── README.md              # Commands overview
│   │   ├── api-design.md          # /api-design command
│   │   ├── api-validate.md        # /api-validate command
│   │   ├── api-generate.md        # /api-generate command
│   │   └── api-compatibility.md   # /api-compatibility command
│   └── hooks.yaml                 # Live hooks configuration
│
├── registry/                      # Registries (source of truth)
│   ├── skills.json                # Registered skills
│   ├── agents.json                # Registered agents
│   ├── commands.json              # Registered commands
│   ├── hooks.json                 # Registered hooks
│   └── workflow_history.json      # Workflow execution history
│
├── workflows/                     # Workflow definitions
│   ├── example_create_and_register.yaml
│   └── api_first_development.yaml
│
└── tests/                         # Test suites
    └── integration/               # Integration tests
```

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
```

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

### Architecture & Design

* [Betty Architecture](docs/betty-architecture.md) — Five-layer model explained
* [Betty Framework Overview](docs/betty-framework-overview.md) — Lifecycle and bootstrapping
* [Skills Framework](docs/skills-framework.md) — Skill taxonomy and categories
* [API-Driven Development](docs/api-driven-development.md) — Complete API workflow guide

### Infrastructure

* [Command & Hook Infrastructure](docs/COMMAND_HOOK_INFRASTRUCTURE.md) — Layer 1 and 5 details
* [Multi-LLM Integration](docs/multi-llm-integration-paths.md) — Multi-model strategies

### Reference

* [Glossary](docs/glossary.md) — Betty terminology and concepts
* [Contributing](docs/contributing.md) — How to contribute to Betty
* [References](docs/references.md) — External documentation links
* [Codebase Analysis](docs/CODEBASE_ANALYSIS.md) — Technical implementation details

### Skills Documentation

Each skill has comprehensive documentation in its `SKILL.md` file:
* Foundation: `skill.create`, `skill.define`, `registry.update`, `workflow.compose`, `workflow.validate`
* API: `api.define`, `api.validate`, `api.generate-models`, `api.compatibility`
* Infrastructure: `agent.define`, `command.define`, `hook.define`, `hook.register`

### Agents Documentation

Each agent has a `README.md` in its directory:
* [api.analyzer](agents/api.analyzer/README.md) — Analyze API specifications for backward compatibility and breaking changes
* [api.designer](agents/api.designer/README.md) — Design RESTful APIs following enterprise guidelines with iterative refinement


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

We welcome contributions! Please see our [Contributing Guide](docs/contributing.md) for detailed instructions.

**Quick Guidelines:**

1. Use lowercase, dot-separated names (e.g., `domain.action` for skills).
2. Include `skill.yaml`, `SKILL.md`, and a handler script for each skill.
3. Validate via `skill.create → skill.define → registry.update` before commit.
4. Write comprehensive tests and documentation.
5. Submit PRs with clear workflow examples and registry entries set to `draft` initially.

**Before submitting:**
- [ ] Manifest validated with `skill.define` or `agent.define`
- [ ] Documentation (SKILL.md/README.md) is complete
- [ ] Examples and usage instructions provided
- [ ] Code follows style guidelines
- [ ] Registry updated

See [docs/contributing.md](docs/contributing.md) for full details.


