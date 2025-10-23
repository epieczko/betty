# Betty Framework Glossary

This glossary defines key terms used throughout the Betty Framework documentation.

## A

### Active
A status indicating that a component is production-ready and available for use in workflows and operations.

### Agent
An intelligent orchestrator with reasoning capabilities that can iteratively execute skills based on context and feedback. Agents operate at Layer 2 of Betty's architecture and can be either **iterative** (retry on failure) or **oneshot** (single execution). Defined by `agent.yaml` manifests.

**Example**: The `api.designer` agent uses `api.define`, `api.validate`, and `api.generate-models` skills iteratively to create compliant API specifications.

### Agent Registry
A JSON file (`/registry/agents.json`) that tracks all registered agents in the Betty ecosystem. Managed by the `agent.define` skill.

### Audit Log
A record of all skill and workflow executions for compliance and debugging. Maintained by the `audit.log` skill (when available) and stored in workflow history.

### AsyncAPI
An industry-standard specification format for event-driven APIs, supported by Betty's API skills alongside OpenAPI.

## B

### Betty
The Build Execution sTructured sYstem - a framework that transforms Claude Code's plugin system into a structured engineering discipline with five architectural layers.

### Blocking Hook
A hook with `blocking: true` that prevents an operation from completing if the hook fails. Used for critical validations like preventing commits with breaking changes.

### Breaking Change
A modification to an API specification that is not backward compatible with previous versions. Detected by the `api.compatibility` skill.

## C

### Command
A user-facing slash command (e.g., `/api-design`) that provides an intuitive entry point to Betty capabilities. Commands operate at Layer 1 and can delegate to agents, workflows, or skills. Defined by command manifests and registered via `command.define`.

### Command Registry
A JSON file (`/registry/commands.json`) that tracks all registered commands. Updated by the `command.define` skill.

### Claude Code
Anthropic's official CLI for Claude - the runtime environment in which Betty operates. Betty extends Claude Code with structured workflows and governance.

## D

### Draft
A status indicating that a component is under development and not yet production-ready. Draft components are excluded from production operations.

### Dependency
A required skill or external resource that another skill needs to function. Listed in skill manifests under the `dependencies` field.

### Draft Status
A status (`draft`) indicating that a skill, agent, command, or hook is under development and not yet production-ready. Contrasts with `active` status.

## E

### Entrypoint
A CLI command definition in a skill manifest that specifies how to invoke the skill, including parameters, permissions, and runtime requirements.

### Event
A trigger point for hooks, such as `on_file_edit`, `on_commit`, or `on_push`. Hooks execute automatically when their associated event occurs.

## F

### Filesystem:Read
Permission to read files and directories from the filesystem.

### Filesystem:Write
Permission to write, modify, or delete files and directories.

### Five-Layer Model
Betty's architectural pattern consisting of: (1) Commands, (2) Agents, (3) Workflows, (4) Skills, and (5) Hooks. Each layer serves a distinct purpose and delegates to the layer below.

## G

### Governance
The policy enforcement and validation layer (Layer 5) implemented through hooks and the `policy.enforce` skill. Ensures organizational standards are automatically applied.

### Guideline Set
A collection of API design rules (e.g., Zalando API Guidelines) that specifications must conform to. Used by `api.validate` and `api.define` skills.

## H

### Hook
An automatic validation or action triggered by events like file edits, commits, or pushes. Hooks operate at Layer 5 and enforce governance policies. Created via `hook.define` or `hook.register`.

### Hook Registry
A JSON file (`/registry/hooks.json`) that tracks formalized hook manifests for version control and review. Different from `.claude/hooks.yaml` which is the live configuration.

## I

### Iterative
A reasoning mode where an agent can retry operations based on feedback, useful for tasks requiring refinement.

### Inputs
Parameters that a skill accepts. Defined in skill manifests with name, type, required status, and description.

### Iterative Agent
An agent with `reasoning_mode: iterative` that can retry operations based on feedback. Useful for tasks requiring refinement, like API design with validation loops.

## L

### Layer
One of the five architectural tiers in Betty: Commands, Agents, Workflows, Skills, or Hooks. Each layer has specific responsibilities and interfaces.

## M

### Manifest
A YAML configuration file that defines a skill, agent, command, or hook. Contains metadata, parameters, dependencies, and other specifications.

### Modelina
An AsyncAPI code generator used by the `api.generate-models` skill to create type-safe models from API specifications in multiple languages.

## O

### On_Compilation_Failure
Error handling strategy that defines actions to take when compilation fails.

### On_Generation_Failure
Error handling strategy that defines actions to take when generation fails.

### On_Validation_Failure
Error handling strategy that defines actions to take when validation fails.

### Oneshot
A reasoning mode where an agent executes once without retries, suitable for deterministic tasks.

### Oneshot Agent
An agent with `reasoning_mode: oneshot` that executes once without retries. Suitable for simple, deterministic tasks.

### OpenAPI
An industry-standard specification format for REST APIs (formerly Swagger). Supported by all Betty API skills.

### Outputs
Artifacts produced by a skill execution. Defined in skill manifests with name, type, and description.

## P

### Process:Execute
Permission to execute process resources.

### Python
A runtime environment for executing Python-based skills and operations.

### Policy Enforcement
The process of validating operations against organizational rules before execution. Implemented by the `policy.enforce` skill and run automatically by `registry.update`.

### Plugin
In Claude Code terms, an extension that adds functionality. Betty itself can be packaged as a Claude Code plugin, and Betty skills are analogous to Claude Code plugins.

## R

### Registry
A JSON file tracking registered components (skills, agents, commands, or hooks). Provides a single source of truth for the Betty ecosystem.

### Registry Update
The process of adding or modifying entries in a registry. Centralized through the `registry.update` skill to ensure consistency and policy compliance.

### Reasoning Mode
The execution strategy for an agent: either `iterative` (with retries and feedback loops) or `oneshot` (single execution). Defined in agent manifests.

## S

### Skill
An atomic unit of functionality - a testable, composable operation like validating an API spec or generating models. Skills operate at Layer 4 and are the building blocks of workflows and agents. Defined by `skill.yaml` manifests.

### Skill Registry
A JSON file (`/registry/skills.json`) containing all registered skills with their metadata, inputs, outputs, and dependencies.

### Status
The lifecycle state of a component: `draft` (under development) or `active` (production-ready). Controls whether components are used in production workflows.

## T

### Tags
Categorization labels applied to skills, agents, commands, or hooks. Enable filtering and organization (e.g., `["api", "validation", "openapi"]`).

### Thread-Safe
A property of operations that can be safely executed concurrently without data corruption. `registry.update` uses file locking to ensure thread-safe registry updates.

## V

### Validation
The process of checking that a manifest, API specification, or workflow conforms to required schemas and rules. Core to Betty's quality assurance.

## W

### Workflow
A declarative YAML definition of multi-step processes that chain skills sequentially. Workflows operate at Layer 3 and enable complex operations to be defined once and reused. Executed by `workflow.compose`.

### Workflow History
A record of workflow executions stored in `/registry/workflow_history.json`. Tracks which workflows ran, when, and their outcomes.

## Y

### YAML
YAML Ain't Markup Language - the human-readable format used for all Betty manifests (skills, agents, workflows, commands, hooks).

## Z

### Zalando API Guidelines
An enterprise-standard set of REST API design rules. Betty's API skills default to validating against these guidelines, though others (Google, Microsoft) are also supported.

---

## Related Documentation

- [Betty Architecture](betty-architecture.md) - Understanding the Five-Layer Model
- [Contributing](contributing.md) - How to contribute to Betty
- [Developer Guide](developer-guide.md) - Building and extending Betty
- [Main README](../README.md) - Project overview and quickstart

## Terminology Conventions

Throughout Betty documentation:
- **Skill** = lowercase with dot notation (e.g., `api.validate`)
- **Agent** = lowercase with dot notation (e.g., `api.designer`)
- **Command** = slash prefix (e.g., `/api-design`)
- **Hook** = kebab-case descriptive name (e.g., `validate-openapi-specs`)
- **Registry** = capitalized when referring to the concept, lowercase for file paths

