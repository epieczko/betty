# Betty Framework

[![Run in Smithery](https://smithery.ai/badge/skills/epieczko)](https://smithery.ai/skills?ns=epieczko&utm_source=github&utm_medium=badge)


<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![License](https://img.shields.io/badge/license-MIT-purple.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Skills](https://img.shields.io/badge/skills-35-orange.svg)
![Agents](https://img.shields.io/badge/agents-20-red.svg)
![Templates](https://img.shields.io/badge/templates-406-yellow.svg)

### **Claude Code thinks. Betty builds.**

**Enterprise-grade AI-assisted engineering framework with self-improving meta-agents**

[Quick Start](#-quick-start) • [Documentation Guide](#-documentation-guide) • [Features](#-key-features) • [Meta-Agents](#-meta-agents-self-improving-infrastructure) • [Artifacts](#-artifact-framework) • [Contributing](#-contributing)

</div>

---

## ⚙️ **Integration Note: Betty as a Claude Code Plugin System**

**Betty is designed as a collection of Claude Code plugins.** You do not invoke Betty via a standalone CLI (`betty` command). Instead:

- **Claude Code serves as the execution environment and unified CLI**
- Each skill, agent, and command is registered through its manifest (`skill.yaml`, `agent.yaml`, etc.)
- Components automatically become discoverable and executable inside Claude Code's command palette
- All invocation, routing, and argument parsing is handled by Claude Code

**No separate installation step is needed** beyond plugin registration in your Claude Code environment.

---

## 🎯 What is Betty?

Betty Framework is **RiskExec's AI-native SDLC platform** built on Anthropic's Claude Code. Where Claude Code provides the runtime, **Betty adds methodology, orchestration, and governance**—transforming AI capabilities into a repeatable, auditable engineering discipline.

**Named for Betty Shannon (1922-2017)**, the electrical engineer who translated Claude Shannon's information theory into applied computation, Betty embodies **turning reasoning into engineered systems**.

### At a Glance

- **35 Production Skills** — Composable building blocks for automation
- **20 Intelligent Agents** — Orchestrators combining skills into workflows
- **6 Meta-Agents** — AI-powered generators that create skills, agents, and hooks
- **391 Artifact Types** — Enterprise SDLC standards (TOGAF, SAFe, Big Five)
- **406 Ready Templates** — Consulting-quality artifacts across all phases
- **Full Governance** — Audit trails, policy enforcement, telemetry
- **v1.0.0 Released** — Production-ready, marketplace-certified

---

## 📑 Table of Contents

- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Meta-Agents: Self-Improving Infrastructure](#-meta-agents-self-improving-infrastructure)
- [Artifact Framework](#-artifact-framework)
- [Skills Catalog](#-skills-catalog)
- [Agents Catalog](#-agents-catalog)
- [Enterprise Features](#-enterprise-features)
- [Documentation Guide](#-documentation-guide)
- [Repository Structure](#-repository-structure)
- [Requirements](#%EF%B8%8F-requirements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Key Features

### 🤖 **Meta-Agents: Self-Improving Infrastructure**

Betty includes **6 meta-agents** that create and manage framework components autonomously:

| Meta-Agent | Creates | Use Case |
|------------|---------|----------|
| **meta.agent** | Agents from descriptions | "Create an API designer agent" |
| **meta.skill** | Skills from descriptions | "Generate a validation skill" |
| **meta.hook** | Event-driven hooks | "Add pre-commit API validation" |
| **meta.artifact** | Artifact type definitions | "Define deployment manifests" |
| **meta.compatibility** | Compatibility graphs | "Analyze agent dependencies" |
| **meta.suggest** | Next-step recommendations | "What should I build next?" |

**Breakthrough**: Meta-agents enable **recursive AI infrastructure** where Betty builds Betty.

### 📦 **Artifact Framework: 391 Enterprise Standards**

Complete SDLC artifact library covering:

- **Architecture** (60+ types) — TOGAF, C4, ADRs, system designs
- **Security** (80+ types) — Threat models, pen tests, compliance
- **Governance** (100+ types) — RAID logs, charters, decision logs
- **Data** (40+ types) — Data models, catalogs, lineage
- **Testing** (50+ types) — Test plans, automation, performance
- **Requirements** (30+ types) — User stories, epics, BRDs
- **Deployment** (20+ types) — Runbooks, DR plans, SRE docs
- **Plus**: AI/ML, Operations, Compliance, Documentation

**406 ready-to-use templates** with Big Five consulting-quality content.

### 🛠️ **35 Production Skills**

Composable, auditable building blocks across:

- **Foundation** — skill.create, registry.update, workflow.compose
- **API Development** — api.define, api.validate, api.generate-models
- **Governance** — policy.enforce, audit.log, telemetry.capture
- **Infrastructure** — plugin.build, plugin.sync, agent.run
- **Documentation** — docs.sync.readme, generate.docs

### 🎭 **20 Intelligent Agents**

Including specialized consulting agents:

- **strategy.architect** — Business strategy and ROI models
- **security.architect** — Threat modeling and zero-trust
- **data.architect** — Data governance and MDM
- **governance.manager** — Program governance and RAID logs
- **test.engineer** — Test strategy and automation
- **deployment.engineer** — SRE and operational excellence

### 🏢 **Enterprise-Grade Governance**

- ✅ **Audit Trails** — Every action logged with provenance
- ✅ **Policy Enforcement** — Automatic validation against org policies
- ✅ **Telemetry** — Performance metrics and usage analytics
- ✅ **Version Control** — Semantic versioning with breaking change detection
- ✅ **Compliance** — GDPR, SOC 2, HIPAA, PCI-DSS support

---

## 🚀 Quick Start

**Get Betty running in under 2 minutes:**

### One-Command Installation

**Linux/macOS:**
```bash
curl -sSL https://raw.githubusercontent.com/epieczko/betty/main/scripts/quickstart.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/epieczko/betty/main/scripts/quickstart.ps1 | iex
```

### Manual Installation

The authoritative setup commands live in [INSTALLATION.md](INSTALLATION.md#canonical-setup). Follow that sequence for Linux, macOS, or Windows, then return here to continue with the quick start walkthrough.

### Your First Betty Experience

**Using Claude Code to execute Betty components:**

```
# Ask Claude to create an artifact type using the meta.artifact agent
"Use meta.artifact to create an openapi-spec artifact type for OpenAPI 3.0 specifications
produced by api.designer and consumed by api.validator and code.generator"

# Ask Claude to create an agent using meta.agent
"Use meta.agent to create an api.designer agent that designs REST APIs following
enterprise guidelines and outputs openapi-spec artifacts"

# Ask Claude to verify with compatibility analysis
"Use meta.compatibility to analyze the api.designer agent"
```

**Alternative: Direct Python execution (for development/testing):**

```bash
# When working outside Claude Code, you can invoke scripts directly
python agents/meta.artifact/meta_artifact.py create /tmp/api-spec.md
python agents/meta.agent/meta_agent.py /tmp/designer.md
python agents/meta.compatibility/meta_compatibility.py analyze api.designer
```

**Congratulations!** You've just created artifacts and agents through Claude Code.

📖 **Full Tutorials**:
- [QUICKSTART.md](QUICKSTART.md) — Betty in 5 minutes
- [GETTING_STARTED.md](GETTING_STARTED.md) — Comprehensive guide
- [INSTALLATION.md](INSTALLATION.md) — Detailed installation

---

## 🤖 Meta-Agents: Self-Improving Infrastructure

Meta-agents are **AI-powered generators** that create Betty components from natural language descriptions.

### 1. meta.agent — Create Agents

**Claude Code invocation:**

```
"Use meta.agent to create a code.reviewer agent for automated code review with best practices.
It should accept source-code and review-guidelines as inputs, output review-report and issue-list,
and use code.analyze, pattern.detect, and recommendation.generate skills."
```

**Direct execution (development/testing):**

```bash
# Describe what you want
cat > /tmp/my_agent.md <<'EOF'
# Name: code.reviewer
# Purpose: Automated code review with best practices
# Inputs: source-code, review-guidelines
# Outputs: review-report, issue-list
# Skills: code.analyze, pattern.detect, recommendation.generate
EOF

# Generate the agent
python agents/meta.agent/meta_agent.py /tmp/my_agent.md
```

**Output:** Complete agent with agent.yaml, README.md, and workflow

### 2. meta.skill — Create Skills

**Claude Code invocation:**

```
"Use meta.skill to create a security.scan skill that runs security vulnerability scans.
It should accept codebase-path and scan-config as inputs, output a vulnerability-report,
and depend on python-security-tools."
```

**Direct execution (development/testing):**

```bash
# Describe the skill
cat > /tmp/my_skill.md <<'EOF'
# Name: security.scan
# Purpose: Run security vulnerability scans
# Inputs: codebase-path, scan-config
# Outputs: vulnerability-report
# Dependencies: python-security-tools
EOF

# Generate the skill
python agents/meta.skill/meta_skill.py /tmp/my_skill.md
```

**Output:** skills/security.scan/ with skill.yaml, SKILL.md, handler

### 3. meta.hook — Create Event Automation

**Claude Code invocation:**

```
"Use meta.hook to create a hook that validates OpenAPI specs on file edits.
It should trigger on on_file_edit events for *.openapi.yaml files,
run api.validate, and be blocking."
```

**Direct execution (development/testing):**

```bash
python agents/meta.hook/meta_hook.py create \
  --event on_file_edit \
  --pattern "*.openapi.yaml" \
  --command api.validate \
  --blocking true
```

**Output:** Automatic API validation on file edits

### 4. meta.artifact — Define Data Standards

**Claude Code invocation:**

```
"Use meta.artifact to create a deployment-manifest artifact type for Kubernetes
deployment configurations in YAML format using k8s-deployment-v1 schema,
produced by deployment.engineer and consumed by infrastructure.deploy and security.scan."
```

**Direct execution (development/testing):**

```bash
python agents/meta.artifact/meta_artifact.py create <<'EOF'
# Name: deployment-manifest
# Purpose: Kubernetes deployment configurations
# Format: YAML
# Schema: k8s-deployment-v1
# Producers: deployment.engineer
# Consumers: infrastructure.deploy, security.scan
EOF
```

**Output:** Artifact definition with schema and validation

### 5. meta.compatibility — Analyze Dependencies

**Claude Code invocation:**

```
"Use meta.compatibility to analyze the api.designer agent"
```

**Direct execution (development/testing):**

```bash
python agents/meta.compatibility/meta_compatibility.py analyze api.designer
```

**Example Output:**
```
✓ Produces: openapi-spec, api-documentation
✓ Consumes: requirements-doc
✓ Compatible with: api.validator, code.generator
⚠ Missing consumer for: api-documentation
```

### 6. meta.suggest — Get Recommendations

**Claude Code invocation:**

```
"Use meta.suggest with context 'I have api.designer and api.validator'
and goal 'Complete API workflow' to get next step recommendations"
```

**Direct execution (development/testing):**

```bash
python agents/meta.suggest/meta_suggest.py \
  --context "I have api.designer and api.validator" \
  --goal "Complete API workflow"
```

**Example Output:**
```
Suggested next steps:
1. Create code.generator agent (produces: client-sdk)
2. Add api.publisher skill (deploy to gateway)
3. Create api.monitor agent (track usage)
```

**Why Meta-Agents Matter**: They enable **emergent capabilities**. As you create more artifacts, agents, and skills, the meta-agents understand your domain better and generate increasingly relevant components.

---

## 🔌 How Claude Code Uses Betty

Betty integrates seamlessly with Claude Code through a plugin architecture that eliminates the need for standalone CLI commands.

### Manifest Registration

Each Betty component declares its capabilities through YAML manifests:

- **Skills** (`skill.yaml`) — Define inputs, outputs, dependencies, and execution handlers
- **Agents** (`agent.yaml`) — Specify reasoning modes, capabilities, and skill orchestration
- **Commands** (`.claude/commands/*.md`) — Provide slash commands for common workflows
- **Hooks** (`.claude/hooks.yaml`) — Define event-driven automation triggers

### Automatic Discovery

Claude Code automatically:

1. **Scans** the Betty repository for manifest files
2. **Validates** manifests against schema definitions
3. **Registers** components in the command registry (`registry/skills.json`, `registry/agents.json`)
4. **Exposes** skills and agents through natural language interface

### Execution Through MCP (Model Context Protocol)

When you ask Claude to execute a Betty component:

1. **Claude parses** your natural language request
2. **Identifies** the appropriate skill or agent from the registry
3. **Validates** inputs against the manifest schema
4. **Invokes** the handler script with validated parameters
5. **Returns** structured output back to Claude for interpretation
6. **Logs** execution to audit trail (`registry/audit_log.json`)

### Registry-Driven Architecture

All component registration happens through centralized registries:

```
registry/
├── skills.json          # load_command_manifest() → skill definitions
├── agents.json          # load_command_manifest() → agent definitions
├── commands.json        # Slash command registry
├── hooks.json           # Event hook registry
└── audit_log.json       # Execution provenance
```

Functions like `load_command_manifest()` and `update_command_registry()` ensure:
- Single source of truth for all components
- Version tracking and breaking change detection
- Dependency validation across components
- Automatic plugin.yaml synchronization

### No Separate Installation

Unlike traditional CLI tools, Betty requires **no installation step** beyond:

1. Cloning the repository
2. Ensuring Python 3.11+ and dependencies are installed
3. Running Claude Code in the repository directory

Claude Code automatically discovers and registers all Betty components at startup.

---

## 📦 Artifact Framework

Betty's artifact framework provides **391 enterprise-standard artifact types** with **406 ready-to-use templates**.

### Artifact Categories

#### 🏗️ Architecture (60+ types)
- System architecture diagrams (C4, UML, deployment)
- Architecture Decision Records (ADRs)
- Technology selection matrices
- Integration patterns and diagrams
- Capacity planning models

#### 🔒 Security (80+ types)
- Threat models (STRIDE, attack trees)
- Security architecture diagrams
- Penetration testing reports
- Vulnerability management plans
- Incident response playbooks
- Zero-trust architecture designs
- Compliance matrices (GDPR, SOC 2, HIPAA, PCI-DSS)

#### 📊 Governance (100+ types)
- Project charters
- RAID logs (Risks, Assumptions, Issues, Decisions)
- Decision logs and ADRs
- Governance frameworks
- Stakeholder analyses
- Steering committee reports
- Change control processes
- Benefits realization plans

#### 💾 Data (40+ types)
- Data models (logical, physical, conceptual)
- Data dictionaries and catalogs
- Data flow diagrams
- Data governance policies
- Data quality frameworks
- Master data management plans
- Data lineage diagrams

#### ✅ Testing (50+ types)
- Test plans and strategies
- Test cases and scenarios
- Test automation frameworks
- Performance test plans
- Integration test suites
- Regression test suites
- Quality assurance reports
- Acceptance criteria

#### 📋 Requirements (30+ types)
- Business requirements documents
- Functional specifications
- User stories and epics
- Use case diagrams
- Requirements traceability matrices
- Product roadmaps
- Feature prioritization matrices

#### 🚀 Deployment (20+ types)
- Deployment runbooks
- Disaster recovery plans
- SRE documentation
- Monitoring and alerting configs
- Infrastructure as code
- CI/CD pipeline definitions
- Release notes and changelogs

#### Plus More Categories
- **AI/ML**: Model cards, training plans, experiment logs
- **Operations**: Incident post-mortems, on-call guides, SLO/SLA definitions
- **Compliance**: Audit reports, policy documents, certification evidence
- **Documentation**: API docs, user guides, architecture docs

### Using Artifacts

**Claude Code invocation:**

```
# List available artifact types
"Use meta.artifact to list all artifact types in the security category"

# Create artifact from template
"Use artifact.create to create a threat-model artifact named payment-system-threats
using the stride template"

# Validate artifact
"Use artifact.validate to validate artifacts/threat-model/payment-system-threats.yaml"

# Review artifact quality
"Use artifact.review to review artifacts/threat-model/payment-system-threats.yaml
against big-five-standards criteria"
```

**Direct execution (development/testing):**

```bash
python agents/meta.artifact/meta_artifact.py list --category security
python skills/artifact.create/artifact_create.py \
  --type threat-model \
  --name payment-system-threats \
  --template stride
python skills/artifact.validate/artifact_validate.py \
  artifacts/threat-model/payment-system-threats.yaml
python skills/artifact.review/artifact_review.py \
  artifacts/threat-model/payment-system-threats.yaml \
  --criteria big-five-standards
```

**Phase Documentation**:
- [PHASE1_COMPLETE.md](PHASE1_COMPLETE.md) — Artifact definitions and templates
- [PHASE2_COMPLETE.md](PHASE2_COMPLETE.md) — Validation and review capabilities
- [PHASE3_COMPLETE.md](PHASE3_COMPLETE.md) — Specialized agents and workflows

---

## 🧩 Skills Catalog

**35 active production skills** organized by category:

### Foundation Skills (5 skills)

| Skill | Purpose |
|-------|---------|
| **registry.update** | Add/update entries in skill registry with automatic versioning |
| **skill.create** | Generate new skill directory and manifest |
| **skill.define** | Validate and register skill manifests |
| **workflow.compose** | Execute multi-step workflows by chaining skills |
| **workflow.validate** | Validate workflow YAML definitions |

### API Development Skills (4 skills)

| Skill | Purpose |
|-------|---------|
| **api.compatibility** | Detect breaking changes between API versions |
| **api.define** | Create OpenAPI/AsyncAPI specs from templates |
| **api.generate-models** | Generate type-safe models using Modelina |
| **api.validate** | Validate specs against enterprise guidelines (Zalando, Google, Microsoft) |

### Governance Skills (6 skills)

| Skill | Purpose |
|-------|---------|
| **audit.log** | Record audit events to centralized log |
| **policy.enforce** | Validate operations against organizational policies |
| **telemetry.capture** | Capture usage telemetry with thread-safe logging |
| **registry.diff** | Compare manifest versions and detect breaking changes |
| **registry.query** | Query registry for skills, agents, commands |
| **plugin.publish** | Publish bundled plugins to marketplace |

### Infrastructure Skills (12 skills)

| Skill | Purpose |
|-------|---------|
| **agent.define** | Validate and register agent manifests |
| **agent.run** | Execute agents with iterative/oneshot reasoning |
| **command.define** | Validate and register command manifests |
| **hook.define** | Create validation hooks for Claude Code |
| **hook.register** | Register hook manifests |
| **hook.simulate** | Test hook behavior before deployment |
| **plugin.build** | Bundle plugin into deployable package |
| **plugin.sync** | Auto-generate plugin.yaml from registries |
| **run.agent** | Simulate agent execution for testing |
| **git.commit** | Create conventional commit messages |
| **file.processor** | Process files with transformations |
| **data.validator** | Validate data against schemas |

### Documentation Skills (8 skills)

| Skill | Purpose |
|-------|---------|
| **docs.sync.readme** | Regenerate README from registry state |
| **docs.sync.plugin_manifest** | Reconcile plugin.yaml with registries |
| **docs.expand.glossary** | Expand glossary with new terms |
| **docs.lint.links** | Validate markdown links |
| **docs.validate.skill_docs** | Ensure skill documentation completeness |
| **generate.docs** | Auto-generate SKILL.md from manifests |
| **generate.marketplace** | Generate marketplace catalog files |
| **serve.marketplace** | Run local marketplace server |

**Each skill includes**:
- `skill.yaml` — Manifest with inputs, outputs, dependencies
- `SKILL.md` — Comprehensive documentation
- Handler script — Python implementation
- Tests — Unit and integration tests
- Examples — Usage examples

---

## 🎭 Agents Catalog

**20 intelligent agents** that orchestrate skills into workflows:

### Meta-Agents (6 agents)

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **meta.agent** | Create agents from descriptions | Generates agent.yaml, README, workflow patterns |
| **meta.skill** | Create skills from descriptions | Generates skill.yaml, SKILL.md, handler script |
| **meta.hook** | Create event-driven hooks | Generates hook definitions and registrations |
| **meta.artifact** | Define artifact types | Creates artifact schemas and templates |
| **meta.compatibility** | Analyze dependencies | Builds compatibility graphs and recommendations |
| **meta.suggest** | Next-step recommendations | Suggests agents, skills, workflows to build |

### Specialized Consulting Agents (6 agents)

| Agent | Domain | Produces |
|-------|--------|----------|
| **strategy.architect** | Business strategy | Business cases, ROI models, strategic plans, portfolios |
| **security.architect** | Security | Threat models, pen test reports, zero-trust designs |
| **data.architect** | Data governance | Data models, governance policies, MDM plans, lineage |
| **governance.manager** | Program governance | Charters, RAID logs, decision logs, compliance matrices |
| **test.engineer** | Quality assurance | Test plans, automation strategies, QA reports |
| **deployment.engineer** | Operations | Runbooks, DR plans, SRE docs, monitoring configs |

### API & Development Agents (4 agents)

| Agent | Purpose | Key Features |
|-------|---------|--------------|
| **api.designer** | Design REST APIs | Follows Zalando guidelines, iterative refinement |
| **api.analyzer** | Analyze API compatibility | Breaking change detection, version comparison |
| **api.architect** | API strategy | API governance, standards, lifecycle management |
| **code.reviewer** | Code review automation | Best practices, pattern detection, recommendations |

### Utility Agents (4 agents)

| Agent | Purpose | Use Case |
|-------|---------|----------|
| **file.processor** | File transformations | Batch processing, format conversion |
| **data.validator** | Data validation | Schema validation, quality checks |
| **meta.command** | Command creation | Generate slash commands |
| **meta.hook** | Hook management | Event-driven automation |

**Each agent includes**:
- `agent.yaml` — Manifest with capabilities and skills
- `README.md` — Documentation and examples
- Workflow definitions — Orchestration patterns
- Integration tests — End-to-end validation

---

## 🏢 Enterprise Features

### Audit & Compliance

- **Complete Audit Trails** — Every action logged with timestamp, user, inputs, outputs
- **Policy Enforcement** — Automatic validation against organizational policies
- **Compliance Support** — GDPR, SOC 2, HIPAA, PCI-DSS templates and validation
- **Change Tracking** — Full version history with breaking change detection

### Governance & Control

- **Registry-Driven** — Single source of truth for all components
- **Approval Workflows** — Human-in-the-loop for critical operations
- **Role-Based Access** — Control who can create, modify, execute
- **Certification Levels** — draft, active, deprecated, archived

### Observability

- **Telemetry Capture** — Automatic performance metrics and usage analytics
- **Execution Traces** — Complete workflow execution history
- **Error Tracking** — Structured error logging with context
- **Performance Monitoring** — Duration tracking, bottleneck detection

### Integration & Extensibility

- **Claude Code Native** — Full plugin integration with marketplace support
- **API-First** — All functionality accessible via programmatic interfaces
- **Schema-Driven** — JSON Schema validation for all artifacts
- **Extensible** — Create custom skills, agents, artifacts without modifying core

---

## 🧭 Documentation Guide

Use this hub to jump directly to the resources that match your role.

### New Contributors & Onboarding

- **[Quickstart](QUICKSTART.md)** — Spin up Betty in minutes with a guided walkthrough.
- **[Getting Started Tutorial](GETTING_STARTED.md)** — Step-by-step introduction to the framework.
- **[Installation Guide](INSTALLATION.md)** — Detailed setup across environments.

### System & Enterprise Architects

- **[Framework Overview](docs/betty-framework-overview.md)** — Betty lifecycle, layers, and bootstrapping.
- **[Betty Architecture](docs/betty-architecture.md)** — Deep dive into the five-layer reference model.
- **[Governance Architecture](docs/governance-architecture.md)** — Control planes, audit posture, and decision flows.
- **[Artifact Framework Integration](docs/ARTIFACT_FRAMEWORK_INTEGRATION.md)** — Mapping enterprise standards into Betty artifacts.

### Implementation & Skill Builders

- **[Implementation Guide](IMPLEMENTATION_GUIDE.md)** — Recommended rollout path for Git workflow automation.
- **[Skills Framework](docs/skills-framework.md)** — Taxonomy, lifecycle, and extension patterns for skills.
- **[Implementation Playbooks](docs/PHASE_1_IMPLEMENTATION.md)** — Phased delivery guidance with meta-agent checkpoints (see also [Phase 2](docs/PHASE_2_IMPLEMENTATION.md)).
- **[Agent Implementation Plan](docs/agent-define-implementation-plan.md)** — Blueprint for composing and validating agents.
- **[API-Driven Development](docs/api-driven-development.md)** — End-to-end workflow example from spec to deployment.
- **[Complete Implementation Summary](docs/COMPLETE_IMPLEMENTATION_SUMMARY.md)** — Snapshot of delivered capabilities across phases.

### Governance & Compliance Leaders

- **[Traceability](docs/TRACEABILITY.md)** — Linking requirements, skills, and execution evidence.
- **[Artifact Standards](docs/ARTIFACT_STANDARDS.md)** — Enterprise documentation expectations and templates.
- **[Artifact Status & Usage](docs/ARTIFACT_STATUS.md)** — Certification levels, lifecycle rules, and consumption guidance.
- **[Artifact Usage Guide](docs/ARTIFACT_USAGE_GUIDE.md)** — Producer/consumer best practices for portfolio teams.
- **[Certification Playbook](docs/CERTIFICATION.md)** — Criteria for promoting skills, agents, and artifacts to production.

### Marketplace & Operations Teams

- **[Marketplace Ingestion](docs/MARKETPLACE_INGESTION.md)** — Process for publishing bundles into Claude's marketplace.
- **[Performance Monitoring](docs/PERFORMANCE_MONITORING.md)** — Telemetry, benchmarking, and alerting patterns.
- **[Claude Router Integration](docs/claude-code-router-integration.md)** — Configuration for multi-tenant routing.
- **[Multi-LLM Integration Paths](docs/multi-llm-integration-paths.md)** — Strategies for orchestrating Claude with other models.
- **[Model Recommendations](docs/model-recommendations.md)** — Guidance on model selection by workload.

### Reference & Community

- **[Glossary](docs/glossary.md)** — Common language for teams collaborating in Betty.
- **[Contributing Guide](docs/contributing.md)** — How to propose changes and ship improvements.
- **[External References](docs/references.md)** — Standards, research, and source inspiration.
- **[Phase Completion Reports](PHASE1_COMPLETE.md)** — Progress documentation for stakeholders (see also [Phase 2](PHASE2_COMPLETE.md) and [Phase 3](PHASE3_COMPLETE.md)).

Looking for something else? Browse the full [docs directory](docs/) for deep dives, standards, and integration notes.

---

## 🧱 Repository Structure

```
betty/
├── agents/                        # 20 intelligent agents
│   ├── meta.agent/                # Creates agents from descriptions
│   ├── meta.skill/                # Creates skills from descriptions
│   ├── meta.hook/                 # Creates event-driven hooks
│   ├── meta.artifact/             # Defines artifact types
│   ├── meta.compatibility/        # Analyzes dependencies
│   ├── meta.suggest/              # Recommends next steps
│   ├── strategy.architect/        # Business strategy
│   ├── security.architect/        # Security architecture
│   ├── data.architect/            # Data governance
│   ├── governance.manager/        # Program governance
│   ├── test.engineer/             # Testing & QA
│   ├── deployment.engineer/       # Operations
│   ├── api.designer/              # API design
│   ├── api.analyzer/              # API analysis
│   └── ... (6 more agents)
│
├── skills/                        # 35 production skills
│   ├── skill.create/              # Scaffold new skills
│   ├── skill.define/              # Validate skill manifests
│   ├── registry.update/           # Update registries
│   ├── workflow.compose/          # Execute workflows
│   ├── api.define/                # Create API specs
│   ├── api.validate/              # Validate API specs
│   ├── policy.enforce/            # Enforce policies
│   ├── audit.log/                 # Audit logging
│   └── ... (27 more skills)
│
├── templates/                     # 406 artifact templates
│   ├── architecture/              # System design templates
│   ├── security/                  # Security templates
│   ├── governance/                # 100+ governance templates
│   ├── data/                      # Data templates
│   ├── testing/                   # Testing templates
│   ├── requirements/              # Requirements templates
│   ├── deployment/                # Deployment templates
│   └── ... (6 more categories)
│
├── registry/                      # Source of truth
│   ├── skills.json                # 35 registered skills
│   ├── agents.json                # 20 registered agents
│   ├── commands.json              # Registered commands
│   ├── hooks.json                 # Registered hooks
│   ├── telemetry.json             # Usage metrics
│   ├── audit_log.json             # Audit trail
│   └── workflow_history.json      # Execution history
│
├── betty/                         # Core Python utilities
│   ├── config.py                  # Configuration and paths
│   ├── validation.py              # Validation utilities
│   ├── logging_utils.py           # Logging infrastructure
│   ├── file_utils.py              # Thread-safe file ops
│   ├── errors.py                  # Exception hierarchy
│   └── telemetry_capture.py       # Telemetry system
│
├── docs/                          # Documentation
│   ├── betty-architecture.md      # Architecture details
│   ├── skills-framework.md        # Skill taxonomy
│   ├── api-driven-development.md  # API workflow
│   ├── glossary.md                # Terminology
│   └── contributing.md            # Contribution guide
│
├── .claude/                       # Claude Code integration
│   ├── commands/                  # Slash commands
│   └── hooks.yaml                 # Event hooks
│
├── .claude-plugin/                # Marketplace integration
│   ├── marketplace.json           # v1.0.0 metadata
│   └── README.md                  # Plugin documentation
│
├── workflows/                     # Workflow definitions
├── tests/                         # Test suites
├── scripts/                       # Setup scripts
├── examples/                      # Usage examples
│
├── QUICKSTART.md                  # 5-minute tutorial
├── GETTING_STARTED.md             # Comprehensive guide
├── INSTALLATION.md                # Installation details
├── PHASE1_COMPLETE.md             # Artifact framework
├── PHASE2_COMPLETE.md             # Validation layer
├── PHASE3_COMPLETE.md             # Specialized agents
├── plugin.yaml                    # Claude Code plugin (925 lines)
└── README.md                      # This file
```

---

## ⚙️ Requirements

- **Python 3.11+** — Core runtime
- **PyYAML** — YAML processing (`pip install pyyaml`)
- **Git 2.20+** — Version control
- **Claude Code** — (Optional) For plugin execution

**Optional Dependencies**:
- `datamodel-code-generator` — For API model generation
- `pytest` — For running tests
- `black`, `mypy`, `pylint` — For development

---

## 🤝 Contributing

We welcome contributions! Betty is designed for extensibility.

### Quick Contribution Guide

1. **Create a new skill using meta.skill**:

   **Via Claude Code:**
   ```
   "Use meta.skill to create a custom.processor skill that processes custom data formats,
   accepts raw-data and config as inputs, and outputs processed-data"
   ```

   **Direct execution (development/testing):**
   ```bash
   cat > /tmp/my_skill.md <<'EOF'
   # Name: custom.processor
   # Purpose: Process custom data formats
   # Inputs: raw-data, config
   # Outputs: processed-data
   EOF
   python agents/meta.skill/meta_skill.py /tmp/my_skill.md
   ```

2. **Implement the handler**: Edit `skills/custom.processor/custom_processor.py`

3. **Test your skill**: Write tests in `tests/test_custom_processor.py`

4. **Validate and register**:

   **Via Claude Code:**
   ```
   "Use skill.define to validate skills/custom.processor/skill.yaml, then use registry.update to register it"
   ```

   **Direct execution (development/testing):**
   ```bash
   python skills/skill.define/skill_define.py skills/custom.processor/skill.yaml
   python skills/registry.update/registry_update.py skills/custom.processor/skill.yaml
   ```

5. **Submit PR**: Set status to `draft` initially, include examples

### Contribution Guidelines

- Use lowercase, dot-separated names (`domain.action`)
- Include comprehensive documentation (SKILL.md/README.md)
- Write tests for all new functionality
- Follow existing code patterns and style
- Update registry files appropriately

**Before Submitting**:
- [ ] Manifest validated with `skill.define` or `agent.define`
- [ ] Documentation complete with examples
- [ ] Tests written and passing
- [ ] Code follows style guidelines (`black`, `pylint`)
- [ ] Registry updated with `draft` status

See **[docs/contributing.md](docs/contributing.md)** for detailed guidelines.

---

## 🎯 Design Principles

- **Structure over improvisation** — Every workflow is defined, typed, reproducible
- **Human oversight first** — Developers approve, correct, extend AI outputs
- **Composable by default** — Skills can be rearranged without breaking systems
- **Audit as a feature** — Provenance and traceability built-in, not bolted-on
- **Self-improving** — Meta-agents enable emergent capabilities
- **Enterprise-ready** — Governance, compliance, security from day one

---

## 📊 Project Status

**Version**: 1.0.0 (Released October 2025)
**Status**: Production Ready
**License**: MIT
**Maintainer**: RiskExec Platform Team

### Key Metrics

- ✅ **35 Active Skills** — Production-tested building blocks
- ✅ **20 Intelligent Agents** — Including 6 meta-agents
- ✅ **391 Artifact Types** — Complete SDLC coverage
- ✅ **406 Ready Templates** — Big Five consulting quality
- ✅ **v1.0.0 Released** — Semantic versioning
- ✅ **Marketplace Ready** — Claude Code plugin certified
- ✅ **Test Coverage** — Comprehensive test suite
- ✅ **Documentation** — 20+ docs, phase guides, tutorials

---

## 🔭 Roadmap

### v1.1.0 (Q1 2026)
- [ ] Multi-LLM support (GPT-4, Gemini, Claude)
- [ ] Visual workflow builder (GUI)
- [ ] Enhanced telemetry dashboard
- [ ] REST API for remote execution

### v1.2.0 (Q2 2026)
- [ ] Enterprise SSO integration
- [ ] Role-based access control (RBAC)
- [ ] Advanced compliance reporting
- [ ] Multi-tenant support

### v2.0.0 (Q3 2026)
- [ ] Cloud-hosted Betty (SaaS)
- [ ] Real-time collaboration
- [ ] Marketplace plugins ecosystem
- [ ] IDE integrations (VS Code, PyCharm)

---

## 📄 License

MIT License — see LICENSE file for details

Copyright (c) 2025 RiskExec

---

## 🙏 Acknowledgments

Named for **Betty Shannon (1922-2017)**, whose work translating information theory into practical computing inspired this framework's philosophy: **turning AI reasoning into engineered systems**.

---

## 📞 Support & Community

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/epieczko/betty/issues)
- **Discussions**: [GitHub Discussions](https://github.com/epieczko/betty/discussions)
- **Email**: platform@riskexec.com

---

<div align="center">

**Built with ❤️ by RiskExec**

[![GitHub](https://img.shields.io/badge/GitHub-epieczko/betty-blue.svg)](https://github.com/epieczko/betty)
[![Documentation](https://img.shields.io/badge/docs-latest-green.svg)](https://github.com/epieczko/betty/tree/main/docs)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

**Claude Code thinks. Betty builds.**

</div>
