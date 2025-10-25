# meta.create - Component Creation Orchestrator

The intelligent orchestrator for creating Betty skills, commands, and agents from natural language descriptions.

## Purpose

`meta.create` is the primary entry point for creating Betty components. It automatically:

- **Detects** what type of component you're describing (skill, command, agent, or combination)
- **Checks** inventory to avoid duplicates
- **Analyzes** complexity to determine the optimal creation pattern
- **Creates** components in dependency order
- **Validates** compatibility and identifies gaps
- **Recommends** next steps for completion

## Why Use meta.create?

Instead of manually running multiple meta-agents (`meta.skill`, `meta.command`, `meta.agent`, `meta.compatibility`), `meta.create` orchestrates everything for you in the right order.

### Before meta.create:
```bash
# Manual workflow - you had to know the order and check everything
python3 agents/meta.command/meta_command.py description.md
# Check if it recommends creating a skill...
python3 agents/meta.skill/meta_skill.py skill_description.md
python3 agents/meta.agent/meta_agent.py agent_description.md
python3 agents/meta.compatibility/meta_compatibility.py analyze my.agent
# Check for gaps, create missing skills...
```

### With meta.create:
```bash
# One command does it all
python3 agents/meta.create/meta_create.py description.md
```

## How It Works

### Step 1: Analysis
Parses your description to determine:
- Is this a skill? command? agent?
- What artifacts are involved?
- What's the complexity level?

### Step 2: Duplicate Check
Queries registries to find existing components:
- Prevents recreating existing skills
- Shows what you can reuse
- Skips unnecessary work

### Step 3: Creation Planning
Uses `meta.command` complexity analysis to determine pattern:
- **COMMAND_ONLY**: Simple inline logic (1-3 steps)
- **SKILL_ONLY**: Reusable utility without command
- **SKILL_AND_COMMAND**: Complex logic in skill + command wrapper
- **AGENT**: Multi-skill orchestration

### Step 4: Component Creation
Creates components in dependency order:
1. **Skills first** (using `meta.skill`)
2. **Commands second** (using `meta.command`)
3. **Agents last** (using `meta.agent` with skill composition)

### Step 5: Compatibility Validation
For agents, runs `meta.compatibility` to:
- Find compatible agent pipelines
- Identify artifact gaps
- Suggest workflows

### Step 6: Recommendations
Provides actionable next steps:
- Missing skills to create
- Compatibility issues to fix
- Integration opportunities

## Usage

### Basic Usage

```bash
python3 agents/meta.create/meta_create.py <description.md>
```

### Create Skill and Command

```bash
python3 agents/meta.create/meta_create.py examples/api_validate.md
```

If `api_validate.md` describes a complex command, meta.create will:
1. Analyze complexity → detects SKILL_AND_COMMAND pattern
2. Create the skill first
3. Create the command that uses the skill
4. Report what was created

### Create Agent with Dependencies

```bash
python3 agents/meta.create/meta_create.py examples/api_agent.md
```

meta.create will:
1. Detect it's an agent description
2. Check for required skills (reuse existing)
3. Create missing skills if needed
4. Create the agent with proper skill composition
5. Validate compatibility with other agents
6. Report gaps and recommendations

### Auto-Fill Gaps

```bash
python3 agents/meta.create/meta_create.py description.md --auto-fill-gaps
```

Automatically creates missing skills to fill compatibility gaps.

### Skip Duplicate Check

```bash
python3 agents/meta.create/meta_create.py description.md --skip-duplicate-check
```

Force creation even if components exist (useful for updates).

### Output Formats

```bash
# Human-readable text (default)
python3 agents/meta.create/meta_create.py description.md

# JSON output for automation
python3 agents/meta.create/meta_create.py description.md --output-format json

# YAML output
python3 agents/meta.create/meta_create.py description.md --output-format yaml
```

### With Traceability

```bash
python3 agents/meta.create/meta_create.py description.md \
  --requirement-id REQ-2025-042 \
  --requirement-description "Create API validation agent" \
  --issue-id JIRA-1234 \
  --requested-by "Product Team"
```

## Description File Format

Your description file can be Markdown or JSON. meta.create detects the type automatically.

### Example: Skill Description

```markdown
# Name: data.validate

# Type: skill

# Purpose:
Validate data against JSON schemas with detailed error reporting

# Inputs:
- data (JSON object to validate)
- schema (JSON schema for validation)

# Outputs:
- validation_result (validation report with errors)

# Produces Artifacts:
- validation.report

# Consumes Artifacts:
- data.json
- schema.json
```

### Example: Command Description

```markdown
# Name: /validate-api

# Type: command

# Description:
Validate API responses against OpenAPI schemas

# Execution Type: skill

# Target: api.validate

# Parameters:
- endpoint: string (required) - API endpoint to validate
- schema: string (required) - Path to OpenAPI schema
```

### Example: Agent Description

```markdown
# Name: api.validator

# Type: agent

# Purpose:
Comprehensive API testing and validation agent

# Inputs:
- api.spec

# Outputs:
- validation.report
- test.results

# Examples:
- Validate all API endpoints against OpenAPI spec
- Generate test cases from schema
```

## What Gets Created

### For Skills
- `skills/{name}/skill.yaml` - Skill configuration
- `skills/{name}/{name}.py` - Python implementation stub
- `skills/{name}/test_{name}.py` - pytest test template
- `skills/{name}/README.md` - Documentation

### For Commands
- `commands/{name}.yaml` - Command manifest
- Recommendations for skill creation if needed

### For Agents
- `agents/{name}/agent.yaml` - Agent configuration
- `agents/{name}/README.md` - Documentation with usage examples
- Compatibility analysis report

## Output Report

meta.create provides a comprehensive report:

```
🎯 meta.create - Orchestrating component creation from description.md

📋 Step 1: Analyzing description...
   Detected types: Skill=True, Command=True, Agent=False

🔍 Step 2: Checking for existing components...
   ✅ No duplicates found

🛠️  Step 3: Creating components...
   📊 Analyzing command complexity...
   Recommended pattern: SKILL_AND_COMMAND
   Should create skill: True

   🔧 Creating skill...
   ✅ Skill 'api.validate' created

   📜 Creating command...
   ✅ Command '/validate-api' created

================================================================================
✨ CREATION SUMMARY
================================================================================

✅ Created 2 component(s):
   • SKILL: api.validate
   • COMMAND: /validate-api

================================================================================
```

## Integration with Other Meta-Agents

meta.create uses:
- **meta.command** - Complexity analysis and command generation
- **meta.skill** - Skill creation with full package
- **meta.agent** - Agent creation with skill composition
- **meta.compatibility** - Compatibility validation and gap detection
- **registry.query** - Duplicate checking
- **agent.compose** - Skill recommendation for agents

## Decision Tree

```
Description Input
       ↓
   Parse Type
       ↓
    ┌──┴──────────────────┐
    ↓                     ↓
  Command?             Agent?
    ↓                     ↓
Analyze              Find Skills
Complexity              ↓
    ↓              Create Missing
SKILL_ONLY            Skills
COMMAND_ONLY            ↓
SKILL_AND_COMMAND   Create Agent
    ↓                     ↓
Create Skill      Validate Compat
    ↓                     ↓
Create Command      Report Gaps
    ↓                     ↓
   Done              Recommend
```

## Examples

### Example 1: Simple Command

```bash
# description.md specifies a simple 2-step command
python3 agents/meta.create/meta_create.py description.md
# Result: Creates COMMAND_ONLY (inline logic is sufficient)
```

### Example 2: Complex Command

```bash
# description.md specifies 10+ step validation logic
python3 agents/meta.create/meta_create.py description.md
# Result: Creates SKILL_AND_COMMAND (skill has logic, command delegates)
```

### Example 3: Multi-Agent System

```bash
# description.md describes an orchestration agent
python3 agents/meta.create/meta_create.py description.md
# Result:
#   - Creates agent with existing skills
#   - Validates compatibility
#   - Reports: "Can receive from api.architect, can feed to report.generator"
#   - Suggests pipeline workflows
```

## Benefits

✅ **Intelligent** - Automatically determines optimal creation pattern
✅ **Safe** - Checks for duplicates, prevents overwrites
✅ **Complete** - Creates all necessary components in order
✅ **Validated** - Runs compatibility checks automatically
✅ **Traceable** - Supports requirement tracking
✅ **Informative** - Provides detailed reports and recommendations

## Next Steps

After using meta.create:

1. **Review** created files
2. **Implement** TODO sections in generated code
3. **Test** with pytest
4. **Register** components (manual or use `skill.register`, etc.)
5. **Use** in your Betty workflows

## Troubleshooting

**Q: meta.create says component already exists**
A: Use `--skip-duplicate-check` to override, or rename your component

**Q: Compatibility gaps reported**
A: Use `--auto-fill-gaps` or manually create the missing skills

**Q: Wrong pattern detected**
A: Add explicit `# Type: skill` or `# Type: command` to your description

## Related Documentation

- [META_AGENTS.md](../../docs/META_AGENTS.md) - Overview of all meta-agents
- [SKILL_COMMAND_DECISION_TREE.md](../../docs/SKILL_COMMAND_DECISION_TREE.md) - Pattern decision logic
- [ARTIFACTS.md](../../docs/ARTIFACTS.md) - Artifact metadata system

---

*Created by the Betty Framework Meta-Agent System*
