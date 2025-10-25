# Betty Meta-Agents

Meta-agents are specialized agents that create and manage other agents, skills, hooks, and framework components. They operate at a higher abstraction level than regular agents.

## Meta-Agent Registry

### meta.create - Component Creation Orchestrator
**Status:** ✅ Implemented

**Purpose:** Intelligent orchestrator that automatically creates skills, commands, and agents from descriptions. This is the primary entry point for creating Betty components.

**Capabilities:**
- Detects component type from description (skill/command/agent)
- Checks registries for duplicates
- Analyzes complexity using meta.command decision tree
- Creates components in dependency order (skills → commands → agents)
- Validates compatibility using meta.compatibility
- Identifies gaps and provides recommendations
- Supports auto-filling missing dependencies

**Consumes:**
- `component.description` (Natural language description in Markdown or JSON)

**Produces:**
- `skill.definition` (Complete skill package with YAML, implementation, tests)
- `command.manifest` (Command manifest in YAML format)
- `agent.definition` (Agent configuration with skill composition)
- `compatibility.report` (Compatibility analysis showing relationships and gaps)

**Uses:**
- `meta.command` - Complexity analysis and command creation
- `meta.skill` - Skill creation
- `meta.agent` - Agent creation with skill composition
- `meta.compatibility` - Compatibility validation and gap detection
- `registry.query` - Duplicate checking
- `agent.compose` - Skill recommendation

**Usage:**
```bash
# Create from any description (auto-detects type)
python3 agents/meta.create/meta_create.py examples/my_component.md

# With auto-fill gaps
python3 agents/meta.create/meta_create.py description.md --auto-fill-gaps

# Skip duplicate check
python3 agents/meta.create/meta_create.py description.md --skip-duplicate-check

# JSON output for automation
python3 agents/meta.create/meta_create.py description.md --output-format json
```

**Why use meta.create instead of individual meta-agents?**
- **Automatic**: Determines what to create without you specifying
- **Comprehensive**: Handles complex SKILL_AND_COMMAND patterns
- **Safe**: Checks for duplicates before creating
- **Validated**: Runs compatibility checks automatically
- **Complete**: Creates all dependencies in the right order

**See:** [meta.create README](../agents/meta.create/README.md) for detailed documentation

---

### meta.agent - Agent Creator
**Current name:** `meta.agent`

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
# Using the agent directly
python3 agents/meta.agent/meta_agent.py examples/my_agent_description.md

# Or via betty CLI (if available)
betty meta agent create examples/my_agent_description.md
```

---

### meta.skill - Skill Creator
**Status:** ✅ Implemented

**Purpose:** Creates complete, functional skills from natural language descriptions

**Consumes:**
- `skill-description` (Markdown or JSON)

**Produces:**
- `skill-definition` (skill.yaml)
- `skill-implementation` (Python stub with proper structure)
- `skill-tests` (pytest test template)
- `skill-documentation` (README.md)

**Features:**
- Validates skill naming convention (domain.action format)
- Sanitizes parameter names automatically
- Registers artifact metadata for interoperability
- Generates CLI with argparse
- Includes error handling and logging
- Creates comprehensive test scaffolding

**Usage:**
```bash
python3 agents/meta.skill/meta_skill.py examples/my_skill_description.md
```

**Example Description:**
```markdown
# Name: data.validatejson

# Purpose:
Validates JSON files against JSON Schema definitions

# Inputs:
- json_file_path
- schema_file_path (optional)

# Outputs:
- validation_result.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- validation-report

# Implementation Notes:
Use Python's jsonschema library for validation. Support both inline
schemas and external schema files. Provide detailed error messages.
```

**Generated Structure:**
```
skills/data.validatejson/
├── skill.yaml              # Complete skill configuration
├── data_validatejson.py    # Python implementation stub
├── test_data_validatejson.py  # pytest test suite
└── README.md               # Full documentation
```

**See:** [meta.skill README](../agents/meta.skill/README.md) for detailed documentation

---

### meta.command - Command Creator
**Status:** ✅ Implemented

**Purpose:** Creates command manifests from natural language descriptions with intelligent complexity analysis

**Consumes:**
- `command-description` (Markdown or JSON)

**Produces:**
- `command.manifest` (YAML command definition)
- `complexity-analysis` (Pattern recommendation: COMMAND_ONLY, SKILL_ONLY, SKILL_AND_COMMAND)

**Features:**
- **Intelligent Complexity Analysis**: Automatically determines optimal pattern
  - Counts steps in description
  - Analyzes autonomy keywords (analyze, optimize, decide, evaluate, etc.)
  - Assesses reusability markers (composable, building block, utility, etc.)
  - Recommends creation pattern based on decision tree
- **Pattern Recommendations:**
  - `COMMAND_ONLY`: Simple 1-3 steps, inline logic sufficient
  - `SKILL_ONLY`: Reusable utility, low complexity but high reuse
  - `SKILL_AND_COMMAND`: Complex (10+ steps) or high autonomy needs
  - `HYBRID`: Medium complexity with some autonomy requirements
- **Parameter Parsing**: Extracts and validates command parameters
- **Execution Type Validation**: Supports agent, skill, and workflow targets
- **Tag Management**: Automatic categorization and filtering

**Decision Tree:**
```
Description → Count Steps → Analyze Keywords
                    ↓
    ┌───────────────┴────────────────┐
    ↓                                 ↓
1-3 steps                        10+ steps
low autonomy                     OR high complexity
    ↓                                 ↓
COMMAND_ONLY                    SKILL_AND_COMMAND
    ↓                                 ↓
inline logic                   skill has logic,
                              command delegates
```

**Usage:**
```bash
# Create command from description
python3 agents/meta.command/meta_command.py examples/api_validate_command.md

# With traceability
python3 agents/meta.command/meta_command.py description.md \
  --requirement-id REQ-2025-001 \
  --requirement-description "API validation command"
```

**Example Description:**
```markdown
# Name: /validate-api

# Description:
Validate API responses against OpenAPI schemas with detailed reporting

# Execution Type: skill

# Target: api.validate

# Parameters:
- endpoint: string (required) - API endpoint to validate
- schema: string (required) - Path to OpenAPI schema file
- strict: boolean (optional, default=false) - Enable strict validation

# Tags:
- api
- validation
- testing
```

**Generated Output:**
```yaml
name: /validate-api
version: 0.1.0
description: Validate API responses against OpenAPI schemas
parameters:
  - name: endpoint
    type: string
    required: true
    description: API endpoint to validate
  - name: schema
    type: string
    required: true
    description: Path to OpenAPI schema file
  - name: strict
    type: boolean
    required: false
    default: false
    description: Enable strict validation
execution:
  type: skill
  target: api.validate
status: draft
tags:
  - api
  - validation
  - testing
```

**Complexity Analysis Output:**
```
📊 Complexity Analysis:
   Steps detected: 12
   Complexity: high
   Autonomy level: medium
   Reusability: high

💡 Recommended Pattern: SKILL_AND_COMMAND
   • High complexity: 12 steps detected
   • High reusability with 12 steps: create both

⚠️  RECOMMENDATION: Create the skill first!
   Pattern: SKILL_AND_COMMAND

   This command delegates to a skill (api.validate),
   but that skill may not exist yet.

   Suggested workflow:
   1. Create skill: python3 agents/meta.skill/meta_skill.py <skill-description.md>
   2. Test skill: python3 skills/api.validate/api_validate.py
   3. Review this command manifest: cat commands/validate-api.yaml
   4. Register command: python3 skills/command.define/command_define.py commands/validate-api.yaml
```

**See:** [SKILL_COMMAND_DECISION_TREE.md](SKILL_COMMAND_DECISION_TREE.md) for complete decision logic

---

### meta.artifact - Artifact Standards Authority
**Status:** ✅ Implemented

**Purpose:** THE single source of truth for artifact standards. Manages schemas, conventions, and compatibility rules.

**Responsibilities:**
1. Define new artifact types
2. Create/update JSON schemas
3. Maintain ARTIFACT_STANDARDS.md
4. Validate artifact compatibility
5. Register artifact types in system

**Produces:**
- `artifact-schema` (JSON Schema)
- `artifact-documentation` (Standards docs in ARTIFACT_STANDARDS.md)
- `artifact-registry` (artifact_define.py registry)

**Commands:**
- `create` - Define new artifact type from description
- `check` - Verify if artifact type exists

**Usage:**
```bash
# Define new artifact type from description
python3 agents/meta.artifact/meta_artifact.py create examples/optimization_report_artifact.md

# Check if artifact type exists
python3 agents/meta.artifact/meta_artifact.py check optimization-report
```

**Critical Rule:** All artifact types MUST be registered with `meta.artifact` before use. No ad-hoc artifact definitions.

**See:** [meta.artifact README](../agents/meta.artifact/README.md) for detailed documentation

---

### meta.hook - Hook Creator
**Status:** ✅ Implemented

**Purpose:** Creates Claude Code hooks from natural language descriptions

**Consumes:**
- `hook-description` (Markdown or JSON)

**Produces:**
- `hook-config` (.claude/hooks.yaml)

**Features:**
- Validates event types (before-tool-call, after-tool-call, on-error, etc.)
- Supports tool-specific filtering (git, npm, docker, etc.)
- Manages hook lifecycle (create, update, enable/disable)
- Configurable timeouts
- Handles duplicate detection and updates

**Event Types:**
- `before-tool-call` - Before any tool executes
- `after-tool-call` - After tool completes
- `on-error` - When tool call fails
- `user-prompt-submit` - When user submits prompt
- `assistant-response` - After assistant responds

**Usage:**
```bash
python3 agents/meta.hook/meta_hook.py examples/pre_commit_hook.md
```

**Example Description:**
```markdown
# Name: pre-commit-lint

# Event: before-tool-call

# Tool Filter: git

# Description: Run linter before git commits to ensure code quality

# Command: npm run lint

# Timeout: 30000

# Enabled: true
```

**Generated Configuration:**
```yaml
hooks:
- name: pre-commit-lint
  event: before-tool-call
  command: npm run lint
  description: Run linter before git commits to ensure code quality
  enabled: true
  tool_filter: git
  timeout: 30000
```

**See:** [meta.hook README](../agents/meta.hook/README.md) for detailed documentation

---

### meta.compatibility - Compatibility Analyzer
**Status:** ✅ Implemented

**Purpose:** Analyzes agent/skill compatibility, discovers pipelines, helps Claude orchestrate multi-agent workflows

**Produces:**
- `compatibility-graph` (Agent relationship map)
- `pipeline-suggestion` (Multi-agent workflows)

**Commands:**
- `find-compatible` - Find agents compatible with a specific agent
- `suggest-pipeline` - Suggest multi-agent workflows for a task
- `analyze` - Analyze a specific agent's compatibility
- `list-all` - List all agents with their artifact metadata

**Usage:**
```bash
# Find compatible agents
python3 agents/meta.compatibility/meta_compatibility.py find-compatible meta.agent

# Suggest pipeline for task
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Validate and optimize API specs"

# Analyze specific agent
python3 agents/meta.compatibility/meta_compatibility.py analyze agents/meta.agent/agent.yaml

# List all agents (JSON or YAML output)
python3 agents/meta.compatibility/meta_compatibility.py --format json list-all
```

**Output Example:**
```json
{
  "agent": "meta.agent",
  "compatible_agents": {
    "produces_for": [
      {
        "agent": "meta.compatibility",
        "shared_artifacts": ["agent-definition"]
      }
    ],
    "consumes_from": [
      {
        "agent": "meta.artifact",
        "shared_artifacts": ["artifact-definition"]
      }
    ]
  },
  "total_compatible": 2
}
```

**See:** [meta.compatibility README](../agents/meta.compatibility/README.md) for detailed documentation

---

### meta.suggest - Next Steps Recommender
**Status:** ✅ Implemented

**Purpose:** Context-aware suggestions for what to do next after an agent completes

**Consumes:**
- `agent-definition` (Current agent context)
- `compatibility-graph` (Agent relationships)
- Project state

**Produces:**
- `suggestion-report` (Structured recommendations with priorities)

**Commands:**
- `suggest` - Get next-step recommendations for an agent
- `analyze-project` - Analyze entire project and suggest workflows

**Usage:**
```bash
# Get suggestions after running an agent
python3 agents/meta.suggest/meta_suggest.py suggest agents/meta.agent/agent.yaml

# Analyze entire project
python3 agents/meta.suggest/meta_suggest.py analyze-project

# Output in JSON format
python3 agents/meta.suggest/meta_suggest.py --format json suggest agents/meta.agent/agent.yaml
```

**Output Example:**
```json
{
  "agent": "meta.agent",
  "suggestions": [
    {
      "priority": "high",
      "type": "next_agent",
      "description": "Use meta.compatibility to find agents that can consume agent-definition",
      "command": "python3 agents/meta.compatibility/meta_compatibility.py find-compatible meta.agent"
    }
  ]
}
```

**See:** [meta.suggest README](../agents/meta.suggest/README.md) for detailed documentation

---

## Meta-Agent Naming Conventions

### Namespace Pattern: `meta.*`

All meta-agents use the `meta.*` namespace to clearly indicate they operate at a meta-level:

- `meta.create` - **Orchestrator** - Main entry point for component creation
- `meta.command` - Creates commands with complexity analysis
- `meta.skill` - Creates skills
- `meta.agent` - Creates agents
- `meta.artifact` - Manages artifact standards
- `meta.hook` - Creates hooks
- `meta.compatibility` - Analyzes compatibility
- `meta.suggest` - Suggests next steps

### Aliases

Some meta-agents may have poetic or legacy aliases:
- `meta.agent` - Agent creation through skill composition
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
│ meta.create         → ORCHESTRATOR - Main entry point   │
│   ├─ meta.command   → Creates commands + analyzes       │
│   ├─ meta.skill     → Creates skills                    │
│   ├─ meta.agent     → Creates agents                    │
│   └─ meta.compatibility → Validates compatibility       │
│ meta.artifact       → Defines artifact standards        │
│ meta.hook           → Creates hooks                     │
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
python3 agents/meta.agent/meta_agent.py examples/api_designer.md
```

3. **Analyze compatibility**:
```bash
python3 agents/meta.compatibility/meta_compatibility.py find-compatible api.designer
```

4. **Get suggestions for next steps**:
```bash
python3 agents/meta.suggest/meta_suggest.py \
  --context meta.agent \
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
python3 agents/meta.agent/meta_agent.py examples/requirements_analyzer.md

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
python3 agents/meta.agent/meta_agent.py examples/security_auditor.md
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
python3 agents/meta.agent/meta_agent.py examples/security_fixer.md
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

### Tutorial 6: Creating Skills with meta.skill

**Goal:** Generate a complete skill from a natural language description

**Steps:**

1. **Write skill description**:
```bash
cat > examples/json_validator_skill.md <<'EOF'
# Name: data.validatejson

# Purpose:
Validates JSON files against JSON Schema definitions

# Inputs:
- json_file_path
- schema_file_path (optional)

# Outputs:
- validation_result.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- validation-report

# Implementation Notes:
Use Python's jsonschema library for validation. Support both inline
schemas and external schema files. Provide detailed error messages.
EOF
```

2. **Generate skill**:
```bash
python3 agents/meta.skill/meta_skill.py examples/json_validator_skill.md
```

Output:
```
✨ Skill 'data.validatejson' created successfully!

📄 Created files:
   - skills/data.validatejson/skill.yaml
   - skills/data.validatejson/data_validatejson.py
   - skills/data.validatejson/test_data_validatejson.py
   - skills/data.validatejson/README.md
```

3. **Review generated files**:
```bash
# View skill configuration
cat skills/data.validatejson/skill.yaml

# Check Python implementation
cat skills/data.validatejson/data_validatejson.py

# Test CLI
python3 skills/data.validatejson/data_validatejson.py --help
```

4. **Implement skill logic**:
```bash
# Edit the execute() method in data_validatejson.py
vim skills/data.validatejson/data_validatejson.py

# Add jsonschema validation logic
# Update tests
```

5. **Test the skill**:
```bash
# Run tests
pytest skills/data.validatejson/test_data_validatejson.py -v

# Test CLI execution
python3 skills/data.validatejson/data_validatejson.py \
  --json-file-path test.json \
  --schema-file-path schema.json
```

6. **Add to agent**:
```yaml
# In agent.yaml
skills_available:
  - data.validatejson
```

**Result:** Fully functional skill with configuration, implementation, tests, and documentation!

---

### Tutorial 7: Creating Hooks with meta.hook

**Goal:** Create Claude Code hooks for event-driven automation

**Steps:**

1. **Create pre-commit linting hook**:
```bash
cat > examples/lint_hook.md <<'EOF'
# Name: pre-commit-lint

# Event: before-tool-call

# Tool Filter: git

# Description: Run linter before git commits to ensure code quality

# Command: npm run lint

# Timeout: 30000

# Enabled: true
EOF
```

2. **Generate hook**:
```bash
python3 agents/meta.hook/meta_hook.py examples/lint_hook.md
```

Output:
```
✨ Hook 'pre-commit-lint' created successfully!

📄 Created/updated file:
   - .claude/hooks.yaml

✅ Hook 'pre-commit-lint' is ready to use
   Event: before-tool-call
   Command: npm run lint
```

3. **Create error notification hook**:
```bash
cat > examples/error_notify_hook.md <<'EOF'
# Name: error-notify

# Event: on-error

# Description: Send notification when tools fail

# Command: ./scripts/notify-team.sh "{error}" "{tool}"

# Timeout: 5000

# Enabled: true
EOF

python3 agents/meta.hook/meta_hook.py examples/error_notify_hook.md
```

4. **View generated hooks**:
```bash
cat .claude/hooks.yaml
```

Output:
```yaml
hooks:
- name: pre-commit-lint
  event: before-tool-call
  command: npm run lint
  description: Run linter before git commits
  enabled: true
  tool_filter: git
  timeout: 30000
- name: error-notify
  event: on-error
  command: ./scripts/notify-team.sh "{error}" "{tool}"
  description: Send notification when tools fail
  enabled: true
  timeout: 5000
```

5. **Test hooks**:
```bash
# Trigger before-tool-call hook
git add .
git commit -m "test"  # Hook runs npm lint before commit

# Disable hook for testing
# Edit .claude/hooks.yaml and set enabled: false
```

6. **Create CI/CD pipeline with hooks**:
```bash
# Create test hook
python3 agents/meta.hook/meta_hook.py test_hook.md

# Create deploy hook
python3 agents/meta.hook/meta_hook.py deploy_hook.md

# Create notification hook
python3 agents/meta.hook/meta_hook.py notify_hook.md
```

**Result:** Event-driven automation with pre-commit checks, error handling, and notifications!

---

### Common Patterns

#### Pattern 1: Create → Analyze → Enhance

```bash
# Create component
python3 agents/meta.agent/meta_agent.py description.md

# Analyze compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze NEW_AGENT

# Get enhancement suggestions
python3 agents/meta.suggest/meta_suggest.py --context meta.agent
```

#### Pattern 2: Define → Register → Use

```bash
# Define artifact type
python3 agents/meta.artifact/meta_artifact.py create artifact.md

# Register in agent
# (meta.agent will automatically use registered types)

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
