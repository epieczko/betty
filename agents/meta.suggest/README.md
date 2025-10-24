# meta.suggest - Context-Aware Next-Step Recommender

Helps Claude decide what to do next after an agent completes by analyzing context and suggesting compatible next steps.

## Overview

**meta.suggest** provides intelligent "what's next" recommendations by analyzing what just happened, what artifacts were produced, and what agents are compatible. It works with meta.compatibility to enable smart multi-agent orchestration.

**What it does:**
- Analyzes context (what agent ran, what artifacts produced)
- Uses meta.compatibility to find compatible next steps
- Provides ranked suggestions with clear rationale
- Considers project state and user goals
- Detects warnings (gaps, isolated agents)
- Suggests project-wide improvements

## Quick Start

### Suggest Next Steps

```bash
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --artifacts agents/api.architect/agent.yaml
```

Output:
```
Context: atum
Produced: agent-definition

🌟 Primary Suggestion:
   Process with meta.compatibility
   Rationale: atum produces 'agent-definition' which meta.compatibility consumes
   Priority: high

🔄 Alternatives:
   1. Test the created artifact
      Verify the artifact works as expected

   2. Analyze compatibility
      Understand what agents can work with atum's outputs
```

### Analyze Project

```bash
python3 agents/meta.suggest/meta_suggest.py --analyze-project
```

Output:
```
📊 Project Analysis:
   Total Agents: 7
   Total Artifacts: 16
   Relationships: 3
   Gaps: 5

💡 Suggestions (6):
   1. Create agent/skill to produce 'agent-description'
      Consumed by 1 agents but no producers
      Priority: medium
   ...
```

## Commands

### Suggest After Agent Runs

```bash
python3 agents/meta.suggest/meta_suggest.py \
  --context AGENT_NAME \
  [--artifacts FILE1 FILE2...] \
  [--goal "USER_GOAL"] \
  [--format json|text]
```

**Parameters:**
- `--context` - Agent that just ran
- `--artifacts` - Artifact files that were produced (optional)
- `--goal` - User's goal for better suggestions (optional)
- `--format` - Output format (text or json)

**Examples:**
```bash
# After atum creates agent
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --artifacts agents/my-agent/agent.yaml

# After meta.artifact creates artifact type
python3 agents/meta.suggest/meta_suggest.py \
  --context meta.artifact \
  --artifacts schemas/my-artifact.json

# With user goal
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --goal "Create and validate API design agent"
```

### Analyze Project

```bash
python3 agents/meta.suggest/meta_suggest.py --analyze-project [--format json|text]
```

Analyzes the entire agent ecosystem and suggests improvements:
- Agents to create
- Gaps to fill
- Documentation needs
- Ecosystem health

## How It Works

### 1. Context Analysis

Determines what just happened:
- Which agent ran
- What artifacts were produced
- What artifact types are involved

### 2. Compatibility Check

Uses meta.compatibility to find:
- Agents that can consume the produced artifacts
- Agents that are compatible downstream
- Potential pipeline steps

### 3. Suggestion Generation

Creates suggestions based on:
- Compatible agents (high priority)
- Validation/testing options (medium priority)
- Gap-filling needs (low priority if applicable)

### 4. Ranking

Ranks suggestions by:
- Priority level (high > medium > low)
- Automation (automated > manual)
- Relevance to user goal

### 5. Warning Generation

Detects potential issues:
- Gaps in required artifacts
- Isolated agents (no compatible partners)
- Failed validations

## Suggestion Types

### 1. Process with Compatible Agent

```
🌟 Primary Suggestion:
   Process with api.validator
   Rationale: api.architect produces 'openapi-spec' which api.validator consumes
```

Automatically suggests running compatible agents.

### 2. Validate/Test Artifact

```
   Test the created artifact
   Rationale: Verify the artifact works as expected
```

Suggests testing when creation-type agents run.

### 3. Analyze Compatibility

```
   Analyze compatibility
   Rationale: Understand what agents can work with atum's outputs
   Command: python3 agents/meta.compatibility/meta_compatibility.py analyze atum
```

Suggests understanding the ecosystem.

### 4. Fill Gaps

```
   Create producer for 'agent-description'
   Rationale: No agents produce 'agent-description' (required by atum)
```

Suggests creating missing components.

## Output Structure

### Text Format

```
Context: AGENT_NAME
Produced: artifact-type-1, artifact-type-2

🌟 Primary Suggestion:
   ACTION
   Rationale: WHY
   [Command: HOW (if automated)]
   Priority: LEVEL

🔄 Alternatives:
   1. ACTION
      Rationale: WHY

⚠️  Warnings:
   • WARNING_MESSAGE
```

### JSON Format

```json
{
  "context": {
    "agent": "atum",
    "artifacts_produced": ["agents/my-agent/agent.yaml"],
    "artifact_types": ["agent-definition"],
    "timestamp": "2025-10-24T..."
  },
  "suggestions": [
    {
      "action": "Process with meta.compatibility",
      "agent": "meta.compatibility",
      "rationale": "...",
      "priority": "high",
      "command": "..."
    }
  ],
  "primary_suggestion": {...},
  "alternatives": [...],
  "warnings": [...]
}
```

## Integration

### With meta.compatibility

meta.suggest uses meta.compatibility for discovery:

```python
# Internal call
compatibility = meta.compatibility.find_compatible(agent_name)

# Use compatible agents for suggestions
for compatible in compatibility.get("can_feed_to", []):
    suggest(f"Process with {compatible['agent']}")
```

### With Claude

Claude can call meta.suggest after any agent:

```
User: Create an API design agent
Claude: *runs atum*
Claude: *calls meta.suggest --context atum*
Claude: I've created the agent. Would you like me to:
  1. Analyze its compatibility
  2. Test it
  3. Add documentation
```

### In Workflows

Use in shell scripts:

```bash
#!/bin/bash
# Create and analyze agent

# Step 1: Create agent
python3 agents/atum/atum.py description.md

# Step 2: Get suggestions
SUGGESTIONS=$(python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --format json)

# Step 3: Extract primary suggestion
PRIMARY=$(echo "$SUGGESTIONS" | jq -r '.primary_suggestion.command')

# Step 4: Run it
eval "$PRIMARY"
```

## Common Workflows

### Workflow 1: Agent Creation Pipeline

```bash
# Create agent
python3 agents/atum/atum.py my_agent.md

# Get suggestions
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --artifacts agents/my-agent/agent.yaml

# Follow primary suggestion
python3 agents/meta.compatibility/meta_compatibility.py analyze my-agent
```

### Workflow 2: Continuous Improvement

```bash
# Analyze project
python3 agents/meta.suggest/meta_suggest.py --analyze-project > improvements.txt

# Review suggestions
cat improvements.txt

# Implement top suggestions
# (create missing agents, fill gaps, etc.)
```

### Workflow 3: Goal-Oriented Orchestration

```bash
# Define goal
GOAL="Design, validate, and implement an API"

# Get suggestions for goal
python3 agents/meta.suggest/meta_suggest.py \
  --goal "$GOAL" \
  --format json > pipeline.json

# Execute suggested pipeline
# (extract steps from pipeline.json and run)
```

## Artifact Types

### Consumes

- **compatibility-graph** - Agent compatibility information
  - From: meta.compatibility

- **agent-definition** - Agent that just ran
  - Pattern: `agents/*/agent.yaml`

### Produces

- **suggestion-report** - Next-step recommendations
  - Pattern: `*.suggestions.json`
  - Schema: `schemas/suggestion-report.json`

## Understanding Suggestions

### Priority Levels

**High** - Should probably do this
- Compatible agent waiting
- Validation needed
- Next logical step

**Medium** - Good to do
- Analyze compatibility
- Understand ecosystem
- Non-critical validation

**Low** - Nice to have
- Fill gaps
- Documentation
- Future improvements

### Automated vs Manual

**Automated** - Has command to run
```
Command: python3 agents/meta.compatibility/...
```

**Manual** - Requires user action
```
(No command - manual action required)
```

### Rationale

Always includes "why" for each suggestion:
```
Rationale: atum produces 'agent-definition' which meta.compatibility consumes
```

Helps Claude and users understand the reasoning.

## Tips & Best Practices

### Providing Context

More context = better suggestions:

✅ **Good:**
```bash
--context atum \
--artifacts agents/my-agent/agent.yaml \
--goal "Create and validate agent"
```

❌ **Minimal:**
```bash
--context atum
```

### Interpreting Warnings

**Gaps warning:**
```
⚠️  atum requires artifacts that aren't produced by any agent
```
This is often expected for user inputs. Not always a problem.

**Isolated warning:**
```
⚠️  my-agent has no compatible agents
```
This suggests the agent uses non-standard artifact types or no other agents exist yet.

### Using Suggestions

1. **Review primary suggestion first** - Usually the best option
2. **Consider alternatives** - May be better for your specific case
3. **Check warnings** - Understand potential issues
4. **Verify commands** - Review before running automated suggestions

## Troubleshooting

### No suggestions returned

```
Error: Could not determine relevant agents for goal
```

**Causes:**
- Agent has no compatible downstream agents
- Artifact types are all user-provided inputs
- No other agents in ecosystem

**Solutions:**
- Create more agents
- Use standard artifact types
- Check agent artifact_metadata

### Incorrect suggestions

If suggestions don't make sense:
- Verify agent artifact_metadata is correct
- Check meta.compatibility output directly
- Ensure artifact types are registered

### Empty project analysis

```
Total Agents: 0
```

**Cause:** No agents found in `agents/` directory

**Solution:** Create agents using atum or manually

## Architecture

```
meta.suggest
    ├─ Uses: meta.compatibility (discovery)
    ├─ Analyzes: context and artifacts
    ├─ Produces: ranked suggestions
    └─ Helps: Claude make decisions
```

## Examples

```bash
# Example 1: After creating agent
python3 agents/atum/atum.py examples/api_architect_description.md
python3 agents/meta.suggest/meta_suggest.py --context atum

# Example 2: After creating artifact type
python3 agents/meta.artifact/meta_artifact.py create artifact.md
python3 agents/meta.suggest/meta_suggest.py --context meta.artifact

# Example 3: Project health check
python3 agents/meta.suggest/meta_suggest.py --analyze-project

# Example 4: Export to JSON
python3 agents/meta.suggest/meta_suggest.py \
  --context atum \
  --format json > suggestions.json
```

## Related Documentation

- [META_AGENTS.md](../../docs/META_AGENTS.md) - Meta-agent ecosystem
- [meta.compatibility README](../meta.compatibility/README.md) - Compatibility analyzer
- [ARTIFACT_STANDARDS.md](../../docs/ARTIFACT_STANDARDS.md) - Artifact system
- [suggestion-report schema](../../schemas/suggestion-report.json)

## How Claude Uses This

After any agent completes:
1. Claude calls meta.suggest with context
2. Reviews suggestions and rationale
3. Presents options to user or auto-executes
4. Makes intelligent orchestration decisions

meta.suggest is Claude's assistant for "what's next" decisions!
