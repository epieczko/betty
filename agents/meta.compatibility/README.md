# meta.compatibility - Agent Compatibility Analyzer

Analyzes agent compatibility and discovers multi-agent workflows based on artifact flows.

## Overview

**meta.compatibility** helps Claude discover which agents can work together by analyzing what artifacts they produce and consume. It enables intelligent multi-agent orchestration by suggesting compatible combinations and detecting pipeline gaps.

**What it does:**
- Scans all agents and extracts artifact metadata
- Builds compatibility maps (who produces/consumes what)
- Finds compatible agents based on artifact flows
- Suggests multi-agent pipelines for goals
- Generates complete compatibility graphs
- Detects gaps (consumed but not produced artifacts)

## Quick Start

### Find Compatible Agents

```bash
python3 agents/meta.compatibility/meta_compatibility.py find-compatible atum
```

Output:
```
Agent: atum
Produces: agent-definition, agent-documentation
Consumes: agent-description

✅ Can feed outputs to (1 agents):
   • meta.compatibility (via agent-definition)

⚠️  Gaps (1):
   • agent-description: No agents produce 'agent-description' (required by atum)
```

### Suggest Pipeline

```bash
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Create and analyze an agent"
```

Output:
```
📋 Pipeline 1: Atum Pipeline
   Pipeline starting with atum
   Steps:
      1. atum - Meta-agent that creates other agents...
      2. meta.compatibility - Analyzes agent and skill compatibility...
```

### Analyze Agent

```bash
python3 agents/meta.compatibility/meta_compatibility.py analyze atum
```

### List All Compatibility

```bash
python3 agents/meta.compatibility/meta_compatibility.py list-all
```

Output:
```
Total Agents: 7
Total Artifact Types: 16
Total Relationships: 3

⚠️  Global Gaps (5):
   • agent-description: Consumed by 1 agents but no producers
   ...
```

## Commands

### find-compatible

Find agents compatible with a specific agent.

```bash
python3 agents/meta.compatibility/meta_compatibility.py find-compatible AGENT_NAME [--format json|yaml|text]
```

**Shows:**
- What the agent produces
- What the agent consumes
- Agents that can consume its outputs
- Agents that can provide its inputs
- Gaps (missing producers)

### suggest-pipeline

Suggest multi-agent pipeline for a goal.

```bash
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "GOAL" [--artifacts TYPE1 TYPE2...] [--format json|yaml|text]
```

**Examples:**
```bash
# Suggest pipeline for goal
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Design and validate APIs"

# With required artifacts
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Process data" --artifacts openapi-spec validation-report
```

**Shows:**
- Suggested pipelines (ranked)
- Steps in each pipeline
- Artifact flows between agents
- Whether pipeline is complete (no gaps)

### analyze

Complete compatibility analysis for one agent.

```bash
python3 agents/meta.compatibility/meta_compatibility.py analyze AGENT_NAME [--format json|yaml|text]
```

**Shows:**
- Full compatibility report
- Compatible agents (upstream/downstream)
- Suggested workflows
- Gaps and warnings

### list-all

Generate complete compatibility graph for all agents.

```bash
python3 agents/meta.compatibility/meta_compatibility.py list-all [--format json|yaml|text]
```

**Shows:**
- All agents in the system
- All relationships
- All artifact types
- Global gaps
- Statistics

## Output Formats

### Text (default)

Human-readable output with emojis and formatting.

### JSON

Machine-readable JSON for programmatic use.

```bash
python3 agents/meta.compatibility/meta_compatibility.py find-compatible atum --format json > atum_compatibility.json
```

### YAML

YAML format for configuration or documentation.

```bash
python3 agents/meta.compatibility/meta_compatibility.py list-all --format yaml > compatibility_graph.yaml
```

## How It Works

### 1. Agent Scanning

Scans `agents/` directory for all `agent.yaml` files:

```python
for agent_dir in agents_dir.iterdir():
    agent_yaml = agent_dir / "agent.yaml"
    # Load and parse agent definition
```

### 2. Artifact Extraction

Extracts artifact_metadata from each agent:

```yaml
artifact_metadata:
  produces:
    - type: openapi-spec
  consumes:
    - type: api-requirements
```

### 3. Compatibility Mapping

Builds map of artifact types to producers/consumers:

```
openapi-spec:
  producers: [api.define, api.architect]
  consumers: [api.validate, api.code-generator]
```

### 4. Relationship Discovery

For each agent:
- Find agents that can consume its outputs
- Find agents that can provide its inputs
- Detect gaps (missing producers)

### 5. Pipeline Suggestion

Uses keyword matching and artifact analysis:
- Match goal keywords to agent names/descriptions
- Build pipeline from artifact flows
- Rank by completeness and length
- Return top suggestions

## Integration

### With meta.agent (Atum)

After creating an agent, analyze its compatibility:

```bash
# Create agent
python3 agents/atum/atum.py description.md

# Analyze compatibility
python3 agents/meta.compatibility/meta_compatibility.py analyze new-agent

# Find who can work with it
python3 agents/meta.compatibility/meta_compatibility.py find-compatible new-agent
```

### With meta.suggest

meta.suggest uses meta.compatibility to make recommendations:

```bash
python3 agents/meta.suggest/meta_suggest.py --context atum
```

Internally calls meta.compatibility to find next steps.

## Common Workflows

### Workflow 1: Understand Agent Ecosystem

```bash
# See all compatibility
python3 agents/meta.compatibility/meta_compatibility.py list-all

# Analyze each agent
for agent in atum meta.artifact meta.compatibility meta.suggest; do
    echo "=== $agent ==="
    python3 agents/meta.compatibility/meta_compatibility.py analyze $agent
done
```

### Workflow 2: Build Multi-Agent Pipeline

```bash
# Suggest pipeline
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Create and test an agent"

# Get JSON for workflow automation
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "My goal" --format json > pipeline.json
```

### Workflow 3: Find Gaps

```bash
# Find global gaps
python3 agents/meta.compatibility/meta_compatibility.py list-all | grep "Gaps:"

# Analyze specific agent gaps
python3 agents/meta.compatibility/meta_compatibility.py find-compatible api.architect
```

## Artifact Types

### Consumes

- **agent-definition** - Agent configurations
  - Pattern: `agents/*/agent.yaml`

- **registry-data** - Skills and agents registry
  - Pattern: `registry/*.json`

### Produces

- **compatibility-graph** - Agent relationship maps
  - Pattern: `*.compatibility.json`
  - Schema: `schemas/compatibility-graph.json`

- **pipeline-suggestion** - Multi-agent workflows
  - Pattern: `*.pipeline.json`
  - Schema: `schemas/pipeline-suggestion.json`

## Understanding Output

### Can Feed To

Agents that can consume this agent's outputs.

```
✅ Can feed outputs to (2 agents):
   • api.validator (via openapi-spec)
   • api.code-generator (via openapi-spec)
```

Means:
- api.architect produces openapi-spec
- Both api.validator and api.code-generator consume openapi-spec
- You can run: api.architect → api.validator
- Or: api.architect → api.code-generator

### Can Receive From

Agents that can provide this agent's inputs.

```
⬅️  Can receive inputs from (1 agents):
   • api.requirements-analyzer (via api-requirements)
```

Means:
- api.architect needs api-requirements
- api.requirements-analyzer produces api-requirements
- You can run: api.requirements-analyzer → api.architect

### Gaps

Missing artifacts in the ecosystem.

```
⚠️  Gaps (1):
   • agent-description: No agents produce 'agent-description'
```

Means:
- atum needs agent-description input
- No agent produces it (it's user-provided)
- This is expected for user inputs

### Complete vs Incomplete Pipelines

**Complete Pipeline:**
```
Complete: ✅ Yes
```
All consumed artifacts are produced by pipeline steps.

**Incomplete Pipeline:**
```
Complete: ❌ No
Gaps: agent-description, registry-data
```
Some consumed artifacts aren't produced. Requires user input or additional agents.

## Tips & Best Practices

### Finding Compatible Agents

Use specific artifact types:
```bash
# Instead of generic goal
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Process stuff"

# Use specific artifacts
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Validate API" --artifacts openapi-spec
```

### Understanding Gaps

Not all gaps are problems:
- **User inputs** (agent-description, api-requirements) - Expected
- **Missing producers** for internal artifacts - Need new agents/skills

### Building Pipelines

Start with compatibility analysis:
1. Understand what each agent needs/produces
2. Find compatible combinations
3. Build pipeline step-by-step
4. Validate no gaps exist (or gaps are user inputs)

## Troubleshooting

### Agent not found

```
Error: Agent 'my-agent' not found
```

**Solutions:**
- Check agent exists in `agents/` directory
- Ensure `agent.yaml` exists
- Verify agent name in agent.yaml matches

### No compatible agents found

```
Can feed outputs to (0 agents)
Can receive inputs from (0 agents)
```

**Causes:**
- Agent is isolated (no shared artifact types)
- Agent uses custom artifact types
- No other agents exist yet

**Solutions:**
- Create agents with compatible artifact types
- Use standard artifact types
- Check artifact_metadata is properly defined

### Empty pipeline suggestions

```
Error: Could not determine relevant agents for goal
```

**Solutions:**
- Be more specific in goal description
- Mention artifact types explicitly
- Use `--artifacts` flag

## Architecture

```
meta.compatibility
    ├─ Scans: agents/ directory
    ├─ Analyzes: artifact_metadata
    ├─ Builds: compatibility maps
    ├─ Produces: compatibility graphs
    └─ Used by: meta.suggest, Claude
```

## Examples

See test runs:
```bash
# Example 1: Find compatible agents
python3 agents/meta.compatibility/meta_compatibility.py find-compatible atum

# Example 2: Suggest pipeline
python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Create agent and check compatibility"

# Example 3: Full analysis
python3 agents/meta.compatibility/meta_compatibility.py analyze api.architect

# Example 4: Export to JSON
python3 agents/meta.compatibility/meta_compatibility.py list-all --format json > graph.json
```

## Related Documentation

- [META_AGENTS.md](../../docs/META_AGENTS.md) - Meta-agent ecosystem
- [ARTIFACT_STANDARDS.md](../../docs/ARTIFACT_STANDARDS.md) - Artifact system
- [compatibility-graph schema](../../schemas/compatibility-graph.json)
- [pipeline-suggestion schema](../../schemas/pipeline-suggestion.json)

## How Claude Uses This

Claude can:
1. **Discover capabilities** - "What agents can work with openapi-spec?"
2. **Build workflows** - "How do I design and validate an API?"
3. **Make decisions** - "What should I run next?"
4. **Detect gaps** - "What's missing from the ecosystem?"

meta.compatibility enables autonomous multi-agent orchestration!
