# Multi-LLM Integration Paths for Betty

## Executive Summary

Betty currently has **zero direct LLM integration**. All reasoning happens through Claude Code's runtime, which provides Claude as the underlying LLM. To enable Betty agents to use any LLM (OpenAI, Anthropic, local models, etc.), we need to introduce an abstraction layer.

This document outlines three architectural approaches, from simplest to most comprehensive.

---

## Current Architecture Limitations

### What Betty Does Today:
- **Orchestrates skills** (deterministic Python functions)
- **Defines agent patterns** (YAML manifests describing what skills agents can use)
- **Validates and registers** components (skills, agents, workflows)
- **Runs inside Claude Code** as a framework

### What Betty Does NOT Do:
- ❌ Call LLM APIs directly (no Anthropic SDK, no OpenAI client)
- ❌ Manage model selection or routing
- ❌ Handle LLM authentication or rate limiting
- ❌ Provide reasoning capabilities (delegates to Claude Code)

### The Dependency:
```
Betty Framework
    ↓ (runs inside)
Claude Code IDE
    ↓ (provides)
Claude LLM (for agent reasoning)
```

**Problem**: Betty agents can only reason via Claude because Claude Code only supports Claude.

---

## Three Paths Forward

### **Path 1: LLM-Powered Skills** ⭐ Recommended Starting Point

**Concept**: Create skills that can call any LLM, while keeping agent orchestration via Claude Code.

**Architecture**:
```
Claude Code Agent (reasoning/planning)
    ↓ orchestrates
Betty Skills
    ├── api.define (deterministic)
    ├── api.validate (deterministic)
    └── llm.query (NEW - calls any LLM)
```

**Implementation**:

```yaml
# skills/llm.query/skill.yaml
name: llm.query
version: 0.1.0
description: Query any LLM with a prompt and return structured results

inputs:
  - name: prompt
    type: string
    required: true
  - name: model
    type: string
    required: false
    default: gpt-4
    options: [gpt-4, gpt-3.5-turbo, claude-opus-4, claude-sonnet-4, llama-3-70b]
  - name: temperature
    type: float
    required: false
    default: 0.7
  - name: system_prompt
    type: string
    required: false

outputs:
  - name: response
    type: string
  - name: model_used
    type: string
  - name: tokens_used
    type: object
```

```python
# skills/llm.query/llm_query.py
import os
import sys
import json
from typing import Dict, Any

# Multi-LLM client (litellm, langchain, or custom)
from litellm import completion

def query_llm(
    prompt: str,
    model: str = "gpt-4",
    temperature: float = 0.7,
    system_prompt: str | None = None
) -> Dict[str, Any]:
    """Query any LLM via unified interface."""

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        response = completion(
            model=model,
            messages=messages,
            temperature=temperature
        )

        return {
            "ok": True,
            "response": response.choices[0].message.content,
            "model_used": response.model,
            "tokens_used": {
                "prompt": response.usage.prompt_tokens,
                "completion": response.usage.completion_tokens,
                "total": response.usage.total_tokens
            }
        }
    except Exception as e:
        return {
            "ok": False,
            "error": str(e),
            "model": model
        }

def main():
    if len(sys.argv) < 3:
        print(json.dumps({
            "ok": False,
            "error": "Usage: llm.query <prompt> <model>"
        }, indent=2))
        sys.exit(1)

    prompt = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "gpt-4"

    result = query_llm(prompt, model)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["ok"] else 1)

if __name__ == "__main__":
    main()
```

**Usage in Agents**:

```yaml
# agents/api.analyzer/agent.yaml
name: api.analyzer
version: 0.1.0
reasoning_mode: oneshot

skills_available:
  - api.validate
  - llm.query  # Can now query any LLM!

capabilities:
  - Analyze OpenAPI specs using multiple LLMs
  - Compare responses from different models
  - Generate insights using best model for task
```

**Pros**:
- ✅ Easy to implement (single new skill)
- ✅ Works with existing Betty architecture
- ✅ Agents still orchestrated by Claude (no breaking changes)
- ✅ Can use any LLM via skills (OpenAI, local models, etc.)

**Cons**:
- ⚠️ Agent reasoning still happens via Claude
- ⚠️ Not suitable for replacing agent orchestration layer

**Best For**:
- Hybrid workflows (Claude orchestrates, but delegates specific tasks to other LLMs)
- Testing/comparing different models for specific tasks
- Cost optimization (use cheaper models for simple queries)

---

### **Path 2: Betty Agent Runtime** 🔧 Medium Complexity

**Concept**: Build Betty's own agent execution engine that can use any LLM for reasoning.

**Architecture**:
```
Betty CLI (new)
    ↓
Betty Agent Runtime (new - selects LLM)
    ↓ reasons with
Any LLM (OpenAI, Anthropic, Local)
    ↓ orchestrates
Betty Skills (existing)
```

**Components to Build**:

1. **LLM Router** (`betty/router.py`):
```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class LLMProvider(ABC):
    @abstractmethod
    def complete(self, messages: List[Dict], **kwargs) -> str:
        pass

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key: str):
        from anthropic import Anthropic
        self.client = Anthropic(api_key=api_key)

    def complete(self, messages: List[Dict], **kwargs) -> str:
        response = self.client.messages.create(
            model=kwargs.get("model", "claude-opus-4"),
            messages=messages,
            max_tokens=kwargs.get("max_tokens", 4096)
        )
        return response.content[0].text

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str):
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)

    def complete(self, messages: List[Dict], **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=kwargs.get("model", "gpt-4"),
            messages=messages
        )
        return response.choices[0].message.content

class LLMRouter:
    """Route agent tasks to appropriate LLM."""

    def __init__(self):
        self.providers = {
            "anthropic": AnthropicProvider(os.getenv("ANTHROPIC_API_KEY")),
            "openai": OpenAIProvider(os.getenv("OPENAI_API_KEY")),
        }

    def select_provider(self, agent_config: Dict) -> LLMProvider:
        """Select LLM based on agent configuration."""
        preferred = agent_config.get("llm_preference", "anthropic")
        return self.providers.get(preferred, self.providers["anthropic"])
```

2. **Agent Executor** (`betty/executor.py`):
```python
class AgentExecutor:
    """Execute agents with any LLM."""

    def __init__(self, router: LLMRouter):
        self.router = router
        self.skill_runner = SkillRunner()

    def run_agent(self, agent_name: str, task: str) -> Dict[str, Any]:
        """Execute agent with configured LLM."""

        # Load agent manifest
        manifest = load_agent_manifest(agent_name)

        # Select LLM
        provider = self.router.select_provider(manifest)

        # Build agent prompt
        prompt = self.build_agent_prompt(manifest, task)

        # Execute with iterative loop
        max_retries = manifest.get("error_handling", {}).get("max_retries", 3)
        for attempt in range(max_retries + 1):
            # LLM plans next steps
            plan = provider.complete([
                {"role": "system", "content": prompt},
                {"role": "user", "content": task}
            ])

            # Execute planned skills
            results = self.execute_skills(plan)

            # Check if successful
            if all(r["ok"] for r in results):
                return {"ok": True, "results": results}

            # Iterative refinement
            if manifest["reasoning_mode"] == "iterative":
                task = self.refine_task(task, results)
            else:
                break

        return {"ok": False, "error": "Max retries exceeded"}
```

3. **Agent Configuration** (extend manifests):
```yaml
# agents/api.designer/agent.yaml
name: api.designer
version: 0.2.0

llm_config:
  primary_provider: openai
  primary_model: gpt-4
  fallback_provider: anthropic
  fallback_model: claude-sonnet-4
  reasoning_budget: high  # or low/medium

reasoning_mode: iterative
skills_available:
  - api.define
  - api.validate
```

4. **CLI Entry Point** (`betty/cli.py`):
```python
import click
from betty.executor import AgentExecutor
from betty.router import LLMRouter

@click.group()
def cli():
    """Betty Framework CLI"""
    pass

@cli.command()
@click.argument("agent_name")
@click.argument("task")
def run(agent_name: str, task: str):
    """Run an agent with any LLM."""
    router = LLMRouter()
    executor = AgentExecutor(router)
    result = executor.run_agent(agent_name, task)

    if result["ok"]:
        click.echo("Success!")
        click.echo(json.dumps(result["results"], indent=2))
    else:
        click.echo("Failed:", err=True)
        click.echo(result["error"], err=True)
        sys.exit(1)

if __name__ == "__main__":
    cli()
```

**Usage**:
```bash
# Run agent with OpenAI
export OPENAI_API_KEY=sk-...
betty run api.designer "Design a user service API"

# Run agent with Anthropic
export ANTHROPIC_API_KEY=sk-ant-...
betty run api.analyzer "Analyze the user service spec"
```

**Pros**:
- ✅ Full control over LLM selection
- ✅ Can run Betty standalone (not dependent on Claude Code)
- ✅ Enables cost optimization and model comparison
- ✅ Works with local models (Ollama, etc.)

**Cons**:
- ⚠️ Requires building agent execution engine
- ⚠️ Need to replicate Claude Code's agent orchestration logic
- ⚠️ More complex to maintain

**Best For**:
- Running Betty outside Claude Code
- Production deployments with custom LLM requirements
- Enterprise environments with specific model governance

---

### **Path 3: Claude Code Router Plugin** 🚀 Most Integrated

**Concept**: Extend Claude Code itself to support multiple LLMs via a router plugin.

**Architecture**:
```
Claude Code (extended)
    ↓
Claude Code Router Plugin (NEW)
    ├── Route to Claude (Anthropic)
    ├── Route to OpenAI
    ├── Route to Local Models
    └── Route based on task complexity
    ↓
Betty Framework (unchanged)
```

**This requires**:
1. **Understanding Claude Code's plugin architecture** (if it exists)
2. **Building a router that Claude Code can use** before delegating to agents
3. **Configuring Betty agents with model preferences** that Claude Code respects

**Hypothetical Implementation**:

```yaml
# .claude/config.yaml (new configuration)
llm_router:
  enabled: true
  default_provider: anthropic

  providers:
    anthropic:
      models: [claude-opus-4, claude-sonnet-4, claude-haiku-4-5]
      api_key_env: ANTHROPIC_API_KEY

    openai:
      models: [gpt-4, gpt-3.5-turbo]
      api_key_env: OPENAI_API_KEY

    local:
      models: [llama-3-70b, mistral-large]
      endpoint: http://localhost:11434

  routing_rules:
    - agent_pattern: "api.*"
      preferred_provider: openai
      preferred_model: gpt-4

    - agent_pattern: "*.analyzer"
      preferred_provider: anthropic
      preferred_model: claude-sonnet-4

    - task_complexity: simple
      preferred_provider: local
      preferred_model: llama-3-70b
```

**Pros**:
- ✅ Seamless integration with Claude Code
- ✅ Betty remains unchanged (just configuration)
- ✅ All tools/features of Claude Code still work
- ✅ Centralized model governance

**Cons**:
- ❌ Requires Claude Code to support this (may not be possible)
- ❌ Dependent on Anthropic's roadmap
- ❌ May not be feasible if Claude Code is closed-source

**Best For**:
- If Anthropic adds multi-LLM support to Claude Code
- Contributing to Claude Code's open-source development
- Long-term vision where Claude Code becomes LLM-agnostic

---

## Recommendation

### **Start with Path 1, Plan for Path 2**

**Phase 1 (Immediate)**: Implement `llm.query` skill
- Add LiteLLM-based skill for querying any LLM
- Keep Claude Code for agent orchestration
- Enable hybrid workflows

**Phase 2 (Medium-term)**: Build Betty Agent Runtime
- Implement `betty/router.py` and `betty/executor.py`
- Add CLI for running agents standalone
- Enable production deployments outside Claude Code

**Phase 3 (Long-term)**: Explore Claude Code Plugin
- Monitor Claude Code's plugin ecosystem
- Contribute to open-source efforts if applicable
- Advocate for multi-LLM support in Claude Code

---

## Next Steps

1. **Prototype `llm.query` skill**:
   ```bash
   betty create skill llm.query
   # Implement using LiteLLM
   ```

2. **Test with existing agents**:
   ```yaml
   # Update api.designer to use llm.query for specific tasks
   ```

3. **Design Betty Agent Runtime**:
   - Sketch out `router.py` and `executor.py`
   - Define agent manifest extensions
   - Plan migration path

4. **Investigate Claude Code extensibility**:
   - Research if Claude Code supports plugins
   - Reach out to Anthropic developer relations
   - Explore open-source contributions

---

## References

- **Betty Architecture**: `/home/user/betty/docs/betty-architecture.md`
- **Agent Schema**: `/home/user/betty/docs/agent-schema-reference.md`
- **Skill Creation**: `/home/user/betty/skills/skill.create/`
- **LiteLLM**: https://github.com/BerriAI/litellm (unified LLM interface)
