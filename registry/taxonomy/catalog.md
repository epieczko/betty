# Betty Component Catalog

Generated catalog of all components grouped by domain and role.

## AI

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Agent | `meta.agent` | Meta-agent that creates other agents by composing skills based on natural
langua |
| Agent | `meta.artifact` | The artifact standards authority - THE single source of truth for all
artifact t |
| Agent | `meta.command` | Creates complete command manifests from natural language descriptions.

This met |
| Skill | `meta.compatibility` | Automatic artifact dependency graph validation and diagnostics. Builds a depende |
| Agent | `meta.compatibility` | Analyzes agent and skill compatibility to discover multi-agent workflows.

This  |
| Agent | `meta.hook` | Hook creator meta-agent that generates Claude Code hooks from descriptions |
| Agent | `meta.skill` | Creates complete, functional skills from natural language descriptions.

This me |
| Agent | `meta.suggest` | Context-aware next-step recommender that helps Claude decide what to do next
aft |

### Create

| Type | Name | Description |
|------|------|-------------|
| Skill | `agent.compose` | Recommend skills for a Betty agent based on its purpose and responsibilities. An |
| Skill | `agent.define` | Validates and registers agent manifests for the Betty Framework. Ensures schema  |
| Skill | `generate.docs` | Automatically generate or update SKILL.md documentation from skill.yaml manifest |
| Skill | `generate.marketplace` | Generate marketplace catalog files from Betty Framework registries. Filters acti |
| Agent | `meta.create` | Orchestrator meta-agent that intelligently creates skills, commands, and agents. |

### Orchestrate

| Type | Name | Description |
|------|------|-------------|
| Skill | `agent.run` | Execute a registered Betty agent by loading its manifest, generating a Claude-fr |

## API

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Agent | `api.analyzer` | Analyze API specifications for backward compatibility and breaking changes |
| Skill | `api.compatibility` | Detect breaking changes between API specification versions |
| Agent | `api.designer` | Design RESTful APIs following enterprise guidelines with iterative refinement |

### Create

| Type | Name | Description |
|------|------|-------------|
| Agent | `api.architect` | An agent that designs comprehensive REST APIs and validates them against best pr |
| Skill | `api.define` | Create OpenAPI and AsyncAPI specifications from templates |
| Skill | `api.generatemodels` | Generate type-safe models from OpenAPI and AsyncAPI specifications using Modelin |

### Validate

| Type | Name | Description |
|------|------|-------------|
| Skill | `api.test` | Test REST API endpoints by executing HTTP requests and validating responses agai |
| Skill | `api.validate` | Validate OpenAPI and AsyncAPI specifications against enterprise guidelines |

## ARCHITECTURE

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Skill | `hook.register` | Validate and register hook manifests in the Hook Registry |
| Skill | `hook.simulate` | Simulate hook execution to test manifests before registration |

### Create

| Type | Name | Description |
|------|------|-------------|
| Skill | `artifact.create` | Create artifacts from templates with AI-assisted population. Takes an artifact t |
| Skill | `artifact.define` | Define artifact metadata for Betty Framework skills. Helps create artifact_metad |
| Skill | `artifact.scaffold` | Generate new artifact templates automatically from metadata inputs. Creates full |
| Skill | `command.define` | Validate and register command manifests in the Command Registry |
| Skill | `epic.decompose` | Take an Epic (as Markdown) and decompose it into user stories. Analyzes Epic doc |
| Skill | `epic.write` | Generate an Agile Epic from a high-level goal, feature request, or strategic ini |
| Skill | `hook.define` | Create and register validation hooks for Claude Code |
| Skill | `skill.create` | Generates a new Betty Framework Skill directory and manifest. Used to bootstrap  |
| Skill | `skill.define` | Validates and registers skill manifests (.skill.yaml) for the Betty Framework. E |
| Skill | `story.write` | Convert decomposed items from epic.decompose into fully formatted user stories.  |

### Review

| Type | Name | Description |
|------|------|-------------|
| Skill | `artifact.review` | AI-powered artifact content review for quality, completeness, and best practices |

### Validate

| Type | Name | Description |
|------|------|-------------|
| Skill | `artifact.validate` | Validate artifacts against schema, structure, and quality criteria. Checks for c |

## DATA

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Skill | `data.transform` | Transform data between different formats (JSON, YAML, XML, CSV) with validation  |
| Agent | `data.validator` | Validates data files against schemas, business rules, and data quality standards |

### Create

| Type | Name | Description |
|------|------|-------------|
| Agent | `data.architect` | Create comprehensive data architecture and governance artifacts including data m |

## DEPLOYMENT

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Skill | `plugin.build` | Automatically bundle a plugin directory (or the whole repo) into a deployable Cl |
| Skill | `plugin.publish` | Publish a bundled plugin package (.tar.gz) to various targets: local directory,  |
| Skill | `plugin.sync` | Automatically generates plugin.yaml from Betty Framework registries. Reads skill |

## DOCS

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Skill | `docs.expand.glossary` | Extract undocumented terms from manifests and documentation, then enrich glossar |
| Skill | `docs.sync.pluginmanifest` | Reconciles plugin.yaml with Betty Framework registries to ensure consistency. Id |
| Skill | `docs.sync.readme` | Regenerate the top-level README.md to reflect all current registered skills and  |

### Review

| Type | Name | Description |
|------|------|-------------|
| Skill | `docs.lint.links` | Validates Markdown links to detect broken internal or external links, with optio |

### Validate

| Type | Name | Description |
|------|------|-------------|
| Skill | `docs.validate.skilldocs` | Validate SKILL.md documentation files against their skill.yaml manifests to ensu |

## GOVERNANCE

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Skill | `registry.diff` | Compare current and previous versions of skills/agents and report differences. D |
| Skill | `registry.query` | Search Betty registries programmatically by filtering skills, agents, commands,  |
| Skill | `registry.update` | Updates the Betty Framework Skill Registry by adding or modifying entries based  |

### Govern

| Type | Name | Description |
|------|------|-------------|
| Skill | `policy.enforce` | Enforces policy rules for skill and agent manifests including naming conventions |

### Review

| Type | Name | Description |
|------|------|-------------|
| Skill | `audit.log` | Records audit events to a centralized audit log with timestamped JSON entries tr |

## OPERATIONS

### Analyze

| Type | Name | Description |
|------|------|-------------|
| Command | `/api-compatibility` |  |
| Command | `/api-design` |  |
| Command | `/api-generate` |  |
| Command | `/api-validate` |  |
| Command | `/branch-cleanup` |  |
| Command | `/commit` |  |
| Command | `/create-pr` |  |
| Command | `/create-worktrees` |  |
| Command | `/optimize-build` |  |
| Command | `/update-branch-name` |  |
| Hook | `auto-stage-edited-files` | Automatically stage modified files with git add after editing. Helps maintain a  |
| Skill | `build.optimize` | Comprehensive build process optimization and analysis.

Analyzes build systems ( |
| Skill | `code.format` | Format code using Prettier, supporting multiple languages and file types. This s |
| Agent | `deployment.engineer` | Create comprehensive deployment and release artifacts including deployment plans |
| Skill | `file.compare` | Compare two files and generate detailed diff reports showing line-by-line differ |
| Agent | `file.processor` | Processes files through various transformations including format conversion, com |
| Skill | `git.cleanupbranches` | Clean up merged and stale git branches both locally and remotely. Analyzes branc |
| Hook | `performance-monitor-post` | Monitor system performance - track CPU, memory usage at tool end and rotate logs |
| Hook | `performance-monitor-pre` | Monitor system performance - track CPU, memory usage at tool start |

### Create

| Type | Name | Description |
|------|------|-------------|
| Skill | `git.createpr` | Create GitHub pull requests with auto-generated titles and descriptions based on |
| Agent | `strategy.architect` | Create comprehensive business strategy and planning artifacts including business |
| Skill | `workflow.compose` | Executes multi-step Betty Framework workflows by chaining existing skills. Enabl |

### Govern

| Type | Name | Description |
|------|------|-------------|
| Agent | `governance.manager` | Create comprehensive program and project governance artifacts including project  |

### Observe

| Type | Name | Description |
|------|------|-------------|
| Skill | `telemetry.capture` | Captures and logs usage telemetry for Betty Framework components. Provides threa |

### Orchestrate

| Type | Name | Description |
|------|------|-------------|
| Skill | `workflow.orchestrate` | Orchestrate multi-artifact workflows by coordinating specialized agents and arti |

### Review

| Type | Name | Description |
|------|------|-------------|
| Agent | `code.reviewer` | Analyzes code changes and provides comprehensive feedback on code quality, secur |

### Validate

| Type | Name | Description |
|------|------|-------------|
| Skill | `workflow.validate` | Validates Betty workflow YAML definitions to ensure correct structure and requir |

## SECURITY

### Create

| Type | Name | Description |
|------|------|-------------|
| Agent | `security.architect` | Create comprehensive security architecture and assessment artifacts including th |

## TESTING

### Validate

| Type | Name | Description |
|------|------|-------------|
| Agent | `test.engineer` | Create comprehensive testing artifacts including test plans, test cases, test re |
| Skill | `test.example` | A simple test skill for validating the meta.create orchestrator workflow |
