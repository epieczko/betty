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

## Usage Examples & Tutorials

### Tutorial 1: Creating Your First Agent

**Goal:** Create an API design agent from scratch

**Steps:**

1. **Write agent description** (`examples/api_designer.md`):
```markdown
# Name: api.designer

# Purpose:
Interactive agent that helps design RESTful APIs by creating OpenAPI
specifications and validating them against best practices.

# Inputs:
- API requirements (natural language)

# Outputs:
- openapi-spec
- validation-report

# Examples:
- Design a RESTful API for a blogging platform
- Create an API for a task management system
```

2. **Create the agent**:
```bash
python3 agents/atum/atum.py examples/api_designer.md
```

3. **Analyze compatibility**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py find-compatible api.designer
```

4. **Get suggestions for next steps**:
```bash
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --artifacts agents/api.designer/agent.yaml
```

**Result:** Complete agent with proper skills, artifact metadata, and documentation!

---

### Tutorial 2: Creating a New Artifact Type

**Goal:** Define a custom artifact type for API performance reports

**Steps:**

1. **Write artifact description** (`examples/performance_report_artifact.md`):
```markdown
# Name: performance-report

# Purpose:
API performance analysis results including response times, throughput,
and optimization recommendations.

# Format: JSON

# File Pattern: *.performance.json

# Schema Properties:
- endpoint (string): API endpoint tested
- avg_response_time (number): Average response time in ms
- throughput (number): Requests per second
- recommendations (array): Performance optimization suggestions

# Required Fields:
- endpoint
- avg_response_time
- throughput

# Producers:
- api.performance-analyzer

# Consumers:
- api.optimizer
- report.generator
```

2. **Register the artifact type**:
```bash
python3 agents/meta.artifact/meta_artifact.py create examples/performance_report_artifact.md
```

3. **Verify registration**:
```bash
python3 agents/meta.artifact/meta_artifact.py check performance-report
```

**Result:** New artifact type available system-wide with schema, documentation, and registry entry!

---

### Tutorial 3: Building a Multi-Agent Workflow

**Goal:** Create a workflow that designs, validates, and documents an API

**Steps:**

1. **Discover available agents**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py list-all
```

2. **Suggest pipeline for goal**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py \
  suggest-pipeline "Design, validate, and document an API"
```

3. **Analyze compatibility between agents**:
```bash
# Check what api.designer produces
python3 agents/meta.compatibility/meta_compatibility.py analyze api.designer

# Find who can consume those outputs
python3 agents/meta.compatibility/meta_compatibility.py find-compatible api.designer
```

4. **Build the workflow**:
```bash
# Step 1: Design API
# (Manual: provide requirements)

# Step 2: Create OpenAPI spec
# (Agent: api.designer)

# Step 3: Validate the spec
# (Agent: api.validator - consumes openapi-spec)

# Step 4: Generate documentation
# (Agent: api.documenter - consumes openapi-spec)
```

5. **Get suggestions after each step**:
```bash
# After api.designer completes
python3 agents/meta.suggest/meta_suggest.py --context api.designer

# After api.validator completes
python3 agents/meta.suggest/meta_suggest.py --context api.validator
```

**Result:** Complete multi-agent workflow with intelligent next-step suggestions!

---

### Tutorial 4: Analyzing Your Agent Ecosystem

**Goal:** Understand your current agents and identify gaps

**Steps:**

1. **Generate compatibility graph**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py list-all --format json > ecosystem.json
```

2. **Analyze project health**:
```bash
python3 agents/meta.suggest/meta_suggest.py --analyze-project
```

3. **Review gaps**:
```text
⚠️  Global Gaps (5):
   • api-requirements: Consumed by 2 agents but no producers
   • user-stories: Consumed by 1 agents but no producers
```

4. **Create agents to fill gaps**:
```bash
# Create agent that produces api-requirements
python3 agents/atum/atum.py examples/requirements_analyzer.md

# Verify gap is filled
python3 agents/meta.compatibility/meta_compatibility.py list-all
```

**Result:** Comprehensive understanding of ecosystem health and actionable improvements!

---

### Tutorial 5: End-to-End: Artifact → Agent → Workflow

**Goal:** Complete workflow from defining an artifact to using it in a multi-agent pipeline

**Steps:**

1. **Define artifact type**:
```bash
# Create security-audit artifact type
python3 agents/meta.artifact/meta_artifact.py create examples/security_audit_artifact.md
```

2. **Create agent that produces it**:
```markdown
# examples/security_auditor.md
# Name: security.auditor
# Purpose: Analyze APIs for security vulnerabilities
# Outputs:
- security-audit
- validation-report
```

```bash
python3 agents/atum/atum.py examples/security_auditor.md
```

3. **Create agent that consumes it**:
```markdown
# examples/security_fixer.md
# Name: security.fixer
# Purpose: Fix security issues based on audit results
# Inputs:
- security-audit
# Outputs:
- openapi-spec (fixed version)
```

```bash
python3 agents/atum/atum.py examples/security_fixer.md
```

4. **Verify compatibility**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py analyze security.auditor
```

Output:
```
✅ Can feed outputs to (1 agents):
   • security.fixer (via security-audit)
```

5. **Build pipeline**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py \
  suggest-pipeline "Audit and fix API security issues"
```

**Result:** Complete artifact-driven workflow from type definition to agent pipeline!

---

### Common Patterns

#### Pattern 1: Create → Analyze → Enhance

```bash
# Create component
python3 agents/atum/atum.py description.md

# Analyze compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze NEW_AGENT

# Get enhancement suggestions
python3 agents/meta.suggest/meta_suggest.py --context atum
```

#### Pattern 2: Define → Register → Use

```bash
# Define artifact type
python3 agents/meta.artifact/meta_artifact.py create artifact.md

# Register in agent
# (atum will automatically use registered types)

# Verify usage
python3 agents/meta.compatibility/meta_compatibility.py list-all
```

#### Pattern 3: Discover → Build → Validate

```bash
# Discover available agents
python3 agents/meta.compatibility/meta_compatibility.py list-all

# Build workflow
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "GOAL"

# Validate no gaps
# (Check if pipeline is complete)
```

---

### Best Practices

1. **Always register artifact types first** with `meta.artifact` before creating agents that use them

2. **Use meta.compatibility** to verify agents work together before building workflows

3. **Run meta.suggest** after each agent completes to get context-aware next steps

4. **Analyze project health regularly** with `meta.suggest --analyze-project`

5. **Follow naming conventions**:
   - Agents: `domain.purpose` (e.g., `api.designer`)
   - Artifacts: `noun-type` (e.g., `validation-report`)
   - Use kebab-case for all names

6. **Document everything** - READMEs are auto-generated but can be enhanced

7. **Test compatibility** before committing to multi-agent workflows

---

### Troubleshooting Common Issues

#### Issue: Agent has no compatible partners

**Symptom:**
```
Can feed outputs to (0 agents)
Can receive inputs from (0 agents)
```

**Solutions:**
- Create more agents that work with the same artifact types
- Use standard artifact types
- Ensure artifact_metadata is properly defined in agent.yaml

#### Issue: Artifact type not found

**Symptom:**
```
Warning: Artifact type 'my-type' not in known registry
```

**Solution:**
```bash
python3 agents/meta.artifact/meta_artifact.py create my_type_artifact.md
```

#### Issue: No pipeline suggestions

**Symptom:**
```
Error: Could not determine relevant agents for goal
```

**Solutions:**
- Be more specific in goal description
- Mention specific artifact types with `--artifacts` flag
- Create more agents to expand ecosystem

---

## For Claude Code Integration

When used in Claude Code context, these meta-agents help Claude:

1. **Discover capabilities** - What agents/skills exist
2. **Understand compatibility** - What works together
3. **Suggest workflows** - Multi-agent pipelines
4. **Create new components** - Extend the framework
5. **Maintain standards** - Consistent artifact contracts

Claude reads agent READMEs, compatibility metadata, and can invoke `meta.suggest` to make intelligent orchestration decisions.
