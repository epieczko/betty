# Betty Meta-Agents

Meta-agents are specialized agents that create and manage other agents, skills, hooks, and framework components. They operate at a higher abstraction level than regular agents.

## Meta-Agent Registry

### meta.agent - Agent Creator
**Current name:** `atum` (Egyptian god who speaks existence into being)
**Aliases:** `atum`, `meta.agent`, `agent.create`

**Purpose:** Creates complete, functional agents from natural language descriptions

**Produces:**
- `agent-definition` (agent.yaml)
- `agent-documentation` (README.md)
- Compatibility metadata

**Skills:**
- `agent.compose` - Find compatible skills
- `artifact.define` - Generate artifact metadata

**Usage:**
```bash
# Using descriptive name
betty meta agent create examples/my_agent_description.md

# Using legacy name (Atum)
python3 agents/atum/atum.py examples/my_agent_description.md
```

---

### meta.skill - Skill Creator
**Status:** Not yet implemented

**Purpose:** Creates skills from natural language descriptions

**Produces:**
- `skill-definition` (skill.yaml)
- `skill-implementation` (Python/script stub)
- `skill-tests` (test template)
- `skill-documentation` (README.md)

**Skills:**
- `meta.artifact` - Define artifact metadata for the skill
- `registry.update` - Register the new skill

**Usage:**
```bash
betty meta skill create examples/my_skill_description.md
```

**Example Description:**
```markdown
# Name: api.optimize

# Purpose:
Analyze OpenAPI specifications and suggest optimizations for
performance, security, and best practices.

# Inputs:
- openapi-spec

# Outputs:
- optimization-report
- openapi-spec (optimized version)

# Implementation Notes:
- Use static analysis
- Check against industry best practices
- Suggest specific improvements
```

---

### meta.artifact - Artifact Standards Authority
**Status:** Not yet implemented

**Purpose:** THE single source of truth for artifact standards. Manages schemas, conventions, and compatibility rules.

**Responsibilities:**
1. Define new artifact types
2. Create/update JSON schemas
3. Maintain ARTIFACT_STANDARDS.md
4. Validate artifact compatibility
5. Register artifact types in system

**Produces:**
- `artifact-schema` (JSON Schema)
- `artifact-documentation` (Standards docs)
- `artifact-registry` (Known types list)

**Usage:**
```bash
# Define new artifact type
betty meta artifact define optimization-report \
  --schema-from examples/optimization-report.json \
  --file-pattern "*.optimization.json" \
  --description "Performance and security optimization recommendations"

# Validate artifact compatibility
betty meta artifact validate-compatibility \
  --producer api.optimize \
  --consumer api.implement

# Check if artifact type exists
betty meta artifact exists workflow-definition
```

**Critical Rule:** All artifact types MUST be registered with `meta.artifact` before use. No ad-hoc artifact definitions.

---

### meta.hook - Hook Creator
**Status:** Not yet implemented

**Purpose:** Creates Claude Code hooks from descriptions

**Produces:**
- `hook-config` (hooks.yaml entry)
- `hook-implementation` (Shell script or command)
- `hook-documentation` (README.md)

**Skills:**
- `hook.validate` - Validate hook syntax
- `meta.artifact` - Define hook-related artifacts if needed

**Usage:**
```bash
betty meta hook create examples/pre_commit_hook_description.md
```

**Example Description:**
```markdown
# Name: pre-commit-lint

# Purpose:
Run linting checks before every commit to ensure code quality

# Trigger: pre-commit

# Commands:
- ruff check .
- mypy .

# On Failure:
Block commit, display errors
```

---

### meta.compatibility - Compatibility Analyzer
**Status:** Not yet implemented

**Purpose:** Analyzes agent/skill compatibility, discovers pipelines, helps Claude orchestrate multi-agent workflows

**Produces:**
- `compatibility-graph` (Agent relationship map)
- `pipeline-suggestions` (Multi-agent workflows)
- `artifact-flow-diagram` (Visual flow charts)

**Skills:**
- `agent.list` - Get all agents
- `artifact.search` - Find artifacts by type
- Graph analysis algorithms

**Usage:**
```bash
# Find compatible agents
betty meta compatibility find-compatible api.architect

# Suggest pipeline for task
betty meta compatibility suggest-pipeline "Design, validate, and implement an API"

# Visualize artifact flow
betty meta compatibility visualize agents/api.architect
```

**Output Example:**
```yaml
compatible_agents:
  produces_artifacts_for:
    - api.validator (consumes: openapi-spec)
    - api.code-generator (consumes: openapi-spec)
    - api.test-generator (consumes: openapi-spec)

  consumes_artifacts_from:
    - api.requirements-analyzer (produces: api-requirements)

suggested_pipelines:
  - name: "Quick Validation"
    steps:
      - agent: api.architect
        produces: openapi-spec
      - agent: api.validator
        consumes: openapi-spec
        produces: validation-report

  - name: "Full Development"
    steps:
      - agent: api.architect
      - agent: api.validator
      - agent: api.code-generator
      - agent: api.test-generator
```

---

### meta.suggest - Next Steps Recommender
**Status:** Not yet implemented

**Purpose:** Context-aware suggestions for what to do next after an agent completes

**Consumes:**
- Current context (what just ran)
- Produced artifacts
- Project state

**Produces:**
- `suggestion-report` (Structured recommendations)

**Usage:**
```bash
# After running an agent
betty meta suggest \
  --context api.architect \
  --artifacts specs/user-api.openapi.yaml

# Generic "what should I do next"
betty meta suggest --analyze-project
```

---

## Meta-Agent Naming Conventions

### Namespace Pattern: `meta.*`

All meta-agents use the `meta.*` namespace to clearly indicate they operate at a meta-level:

- `meta.agent` - Creates agents
- `meta.skill` - Creates skills
- `meta.artifact` - Manages artifact standards
- `meta.hook` - Creates hooks
- `meta.compatibility` - Analyzes compatibility
- `meta.suggest` - Suggests next steps

### Aliases

Some meta-agents may have poetic or legacy aliases:
- `atum` → `meta.agent` (poetic: Egyptian god of creation)
- Future: `thoth` → `meta.artifact` (if we want to keep thematic naming)

### Discovery

List all meta-agents:
```bash
betty meta list
betty agent list --filter meta.*
```

---

## Architecture Layers

```
┌─────────────────────────────────────────────────────────┐
│ Meta-Agent Layer (Creation & Governance)                │
├─────────────────────────────────────────────────────────┤
│ meta.agent          → Creates agents                    │
│ meta.skill          → Creates skills                    │
│ meta.artifact       → Defines artifact standards        │
│ meta.hook           → Creates hooks                     │
│ meta.compatibility  → Analyzes compatibility            │
│ meta.suggest        → Suggests next steps               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ Agent Layer (Composed from Skills)                      │
├─────────────────────────────────────────────────────────┤
│ api.architect, workflow.orchestrator, etc.              │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ Skill Layer (Atomic Operations)                         │
├─────────────────────────────────────────────────────────┤
│ api.define, api.validate, workflow.compose, etc.        │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Order

1. **meta.artifact** (FIRST) - Establish standards governance
2. **meta.compatibility** (SECOND) - Enable discovery
3. **Enhance meta.agent** (THIRD) - Better compatibility info
4. **meta.skill** (FOURTH) - Create skills with proper standards
5. **meta.hook** (FIFTH) - Create hooks
6. **meta.suggest** (SIXTH) - Smart suggestions

---

## Governance Rules

1. **All artifact types MUST be registered with `meta.artifact`**
2. **All meta-agents MUST use the `meta.*` namespace**
3. **All created agents/skills MUST include compatibility metadata**
4. **Artifact standards are the source of truth, not individual implementations**
5. **Meta-agents can suggest but not force workflows**

---

## For Claude Code Integration

When used in Claude Code context, these meta-agents help Claude:

1. **Discover capabilities** - What agents/skills exist
2. **Understand compatibility** - What works together
3. **Suggest workflows** - Multi-agent pipelines
4. **Create new components** - Extend the framework
5. **Maintain standards** - Consistent artifact contracts

Claude reads agent READMEs, compatibility metadata, and can invoke `meta.suggest` to make intelligent orchestration decisions.
