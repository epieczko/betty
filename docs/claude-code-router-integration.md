# Integrating Claude Code Router with Betty

## Executive Summary

**Claude Code Router** (by musistudio) is an **open-source proxy** that sits between Claude Code and LLM providers, enabling Betty agents to use **any LLM** without any code changes to Betty itself.

**Repository**: https://github.com/musistudio/claude-code-router (20k+ stars)

This is the **simplest and most elegant** solution for multi-LLM support in Betty - it's essentially "Path 3" from our analysis, but **already implemented and production-ready**.

---

## How Claude Code Router Works

### Architecture Overview

```
Claude Code CLI
    ↓ (API requests)
Claude Code Router Proxy ← You configure this!
    ↓ (routes to)
┌─────────────┬──────────────┬────────────┬─────────┐
│  OpenRouter │  DeepSeek    │  Ollama    │  Gemini │
└─────────────┴──────────────┴────────────┴─────────┘
    ↓ (models run Betty's agent reasoning)
Betty Framework
    ↓ (executes)
Skills (unchanged)
```

**Key Insight**: The router is **transparent** to both Claude Code and Betty. It intercepts HTTP requests to Anthropic's API and routes them to configured providers.

### What Gets Routed

When Betty agents run in Claude Code:
1. Claude Code makes API calls to `api.anthropic.com`
2. Router **intercepts** these calls
3. Router **transforms** request format for target provider (OpenAI, DeepSeek, etc.)
4. Target LLM processes the request (agent reasoning, skill orchestration)
5. Router **transforms** response back to Claude Code format
6. Claude Code receives response and continues normally

**Betty is completely unaware** that a different LLM is being used!

---

## Installation & Setup

### Step 1: Install Claude Code Router

```bash
# Install globally via npm
npm install -g @musistudio/claude-code-router

# Verify installation
ccr --version
```

### Step 2: Interactive Configuration

```bash
# Run interactive setup
ccr code

# This creates: ~/.claude-code-router/config.json
```

The interactive setup will ask:
- Which providers you want to use (OpenRouter, DeepSeek, Ollama, etc.)
- API keys for each provider
- Default routing rules
- Model preferences

### Step 3: Configure Providers

Edit `~/.claude-code-router/config.json`:

```json
{
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": [
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4",
        "google/gemini-2.5-pro-preview",
        "meta-llama/llama-3.3-70b-instruct"
      ]
    },
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": [
        "deepseek-chat",
        "deepseek-reasoner"
      ]
    },
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": [
        "llama3.3:70b",
        "mistral-large"
      ]
    }
  ],
  "Router": {
    "default": "openrouter,anthropic/claude-3.5-sonnet",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

### Step 4: Launch Claude Code via Router

```bash
# Instead of running 'claude' directly, run:
ccr code

# Or set up an alias
alias claude='ccr code'
```

---

## Routing Strategies for Betty Agents

### Context-Based Routing

Claude Code Router supports **four routing contexts** that map perfectly to Betty's use cases:

#### 1. **Default** (General Agent Reasoning)
```json
"Router": {
  "default": "openrouter,openai/gpt-4"
}
```

**Used for**: Standard agent orchestration, skill selection, decision-making

**Betty agents**: `api.designer`, `api.analyzer`, most general-purpose agents

**Recommended models**:
- `openai/gpt-4` - Best for complex reasoning
- `anthropic/claude-3.5-sonnet` - Balanced performance
- `deepseek-chat` - Cost-effective alternative

#### 2. **Background** (Async/Long-Running Tasks)
```json
"Router": {
  "background": "deepseek,deepseek-chat"
}
```

**Used for**: Background skill execution, batch processing, low-priority tasks

**Betty use cases**:
- Bulk API validation across multiple specs
- Registry updates
- Documentation generation

**Recommended models**:
- `deepseek-chat` - Fast and cheap
- `openai/gpt-3.5-turbo` - Cost-effective
- Local models via Ollama - No API costs

#### 3. **Think** (Complex Reasoning)
```json
"Router": {
  "think": "deepseek,deepseek-reasoner"
}
```

**Used for**: Deep analysis, complex problem-solving, iterative refinement

**Betty agents with `reasoning_mode: iterative`**:
- `api.designer` - Iteratively refining API specs
- Complex validation and error analysis
- Breaking change impact assessment

**Recommended models**:
- `deepseek-reasoner` - Specialized reasoning model
- `openai/o1` - Advanced reasoning
- `anthropic/claude-opus-4` - Deep thinking

#### 4. **Long Context** (Large Codebases/Docs)
```json
"Router": {
  "longContext": "openrouter,google/gemini-2.5-pro-preview"
}
```

**Used for**: Processing large API specs, analyzing multiple files, comprehensive reviews

**Betty use cases**:
- Analyzing entire API portfolios
- Cross-spec compatibility checks
- Large-scale refactoring analysis

**Recommended models**:
- `google/gemini-2.5-pro-preview` - 2M+ token context
- `anthropic/claude-3.5-sonnet` - 200k context
- `cohere/command-r-plus` - 128k context

---

## Betty-Specific Configuration Examples

### Example 1: Cost-Optimized Setup

**Goal**: Minimize costs while maintaining quality for Betty agents

```json
{
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": ["anthropic/claude-3.5-sonnet", "openai/gpt-4"]
    },
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": ["llama3.3:70b"]
    }
  ],
  "Router": {
    "default": "ollama,llama3.3:70b",           // Local model for most work
    "background": "ollama,llama3.3:70b",        // Local for background tasks
    "think": "openrouter,anthropic/claude-3.5-sonnet",  // Claude for complex reasoning
    "longContext": "openrouter,anthropic/claude-3.5-sonnet"
  }
}
```

**Cost profile**:
- 90% of operations: Free (local model)
- 10% of operations: Paid (Claude for complex tasks)
- Estimated savings: 85-95%

### Example 2: Quality-First Setup

**Goal**: Best possible results for Betty agents

```json
{
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": [
        "openai/gpt-4",
        "openai/o1",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-pro-preview"
      ]
    }
  ],
  "Router": {
    "default": "openrouter,openai/gpt-4",
    "background": "openrouter,openai/gpt-4",
    "think": "openrouter,openai/o1",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**Quality profile**:
- Best-in-class models for each task type
- Optimal for production/enterprise use
- Higher cost but best results

### Example 3: Hybrid Setup (Recommended)

**Goal**: Balance cost and quality for Betty workflows

```json
{
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": [
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4",
        "google/gemini-2.5-pro-preview"
      ]
    },
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",                        // Fast & cheap for standard work
    "background": "deepseek,deepseek-chat",                     // Cheap for background
    "think": "deepseek,deepseek-reasoner",                      // Specialized reasoning
    "longContext": "openrouter,google/gemini-2.5-pro-preview"  // Best for large context
  }
}
```

**Profile**:
- Most operations: DeepSeek (very cost-effective)
- Complex reasoning: DeepSeek Reasoner
- Large specs: Gemini (2M token context)
- Best balance of cost/quality

---

## Dynamic Model Switching

### Using `/model` Command

While Betty is running, you can **dynamically switch models** using Claude Code's `/model` command:

```bash
# In Claude Code session
/model openrouter anthropic/claude-3.5-sonnet

# Run Betty agent
/api-design user-service

# Switch to DeepSeek for cost savings
/model deepseek deepseek-chat

# Run another agent
/api-validate user-service-spec
```

### Model Selection Strategy

| Betty Task | Recommended Model | Context | Reasoning |
|------------|------------------|---------|-----------|
| API Design (`api.designer`) | GPT-4, Claude Sonnet | `think` | Complex reasoning, iterative refinement |
| API Validation (`api.validate`) | DeepSeek Chat, Claude Haiku | `default` | Simple validation, pattern matching |
| Model Generation (`api.generate-models`) | DeepSeek Chat, GPT-3.5 | `background` | Deterministic transformation |
| Compatibility Analysis (`api.compatibility`) | Claude Sonnet, GPT-4 | `think` | Complex diff analysis |
| Bulk Operations | Local Ollama, DeepSeek | `background` | Cost optimization |
| Large API Portfolios | Gemini 2.5 Pro, Claude Opus | `longContext` | Handle massive specs |

---

## Configuring Betty Agents for Router

### Option A: No Changes Required (Recommended)

Betty agents work **as-is** with the router. The router handles everything transparently:

```yaml
# agents/api.designer/agent.yaml
# No changes needed!
name: api.designer
version: 0.1.0
reasoning_mode: iterative

skills_available:
  - api.define
  - api.validate
```

The router's `default` and `think` contexts will automatically be used based on task complexity.

### Option B: Add Router Hints (Future Enhancement)

If you want explicit control, you could extend agent manifests with routing hints:

```yaml
# agents/api.designer/agent.yaml
name: api.designer
version: 0.2.0
reasoning_mode: iterative

# NEW: Router configuration hints
router_preferences:
  preferred_context: think          # Prefer 'think' context
  min_context_window: 100000        # Require 100k+ context
  preferred_providers:
    - anthropic
    - openai
  fallback_strategy: use_default    # Fall back to 'default' if preferred unavailable

skills_available:
  - api.define
  - api.validate
```

**Note**: This requires Betty to pass these hints to Claude Code (future work).

---

## Integration Steps for Betty

### Current State: Immediate Use (No Code Changes)

1. **Install Claude Code Router**:
   ```bash
   npm install -g @musistudio/claude-code-router
   ```

2. **Configure providers** (`~/.claude-code-router/config.json`):
   - Add OpenRouter, DeepSeek, Ollama, or other providers
   - Set routing rules for `default`, `background`, `think`, `longContext`

3. **Launch Claude Code via router**:
   ```bash
   ccr code
   ```

4. **Use Betty normally**:
   ```bash
   # Betty commands work exactly as before
   /api-design user-service
   /api-validate user-service-spec
   ```

5. **Betty agents now use configured LLMs** - no code changes needed!

### Future Enhancements: Betty-Aware Routing

#### 1. Add Router Configuration to Betty

Create `betty/router_config.py`:

```python
"""Router configuration for Betty agents."""

from typing import Dict, Any

# Map Betty reasoning modes to router contexts
REASONING_MODE_TO_CONTEXT = {
    "iterative": "think",     # Iterative agents need deep reasoning
    "oneshot": "default"      # Oneshot agents use standard context
}

# Map agent capabilities to preferred models
CAPABILITY_TO_MODEL = {
    "Design RESTful APIs": "think",           # Complex design work
    "Validate API specs": "default",          # Standard validation
    "Generate code models": "background",     # Simple transformation
    "Analyze compatibility": "think",         # Complex analysis
    "Process large portfolios": "longContext" # Large context needed
}

def get_recommended_context(agent_manifest: Dict[str, Any]) -> str:
    """Get recommended router context for agent."""

    # Check reasoning mode
    mode = agent_manifest.get("reasoning_mode", "oneshot")
    base_context = REASONING_MODE_TO_CONTEXT.get(mode, "default")

    # Check capabilities
    capabilities = agent_manifest.get("capabilities", [])
    for capability in capabilities:
        if "large" in capability.lower() or "portfolio" in capability.lower():
            return "longContext"
        if "complex" in capability.lower() or "design" in capability.lower():
            return "think"

    return base_context
```

#### 2. Add Routing Metadata to Agent Manifests

Extend agent schema to include router hints:

```yaml
# agents/api.designer/agent.yaml
name: api.designer
version: 0.3.0

# Standard fields
reasoning_mode: iterative
skills_available: [api.define, api.validate]

# NEW: Router metadata
metadata:
  router:
    preferred_context: think
    min_tokens: 100000
    preferred_providers: [anthropic, openai]
    cost_tier: standard  # budget|standard|premium

  complexity:
    reasoning_intensity: high
    context_window_needs: medium
    iteration_likelihood: high
```

#### 3. Create Router Configuration Skill

Create `skills/router.configure/` to generate optimal router configs:

```bash
# Generate router config optimized for Betty
betty run router.configure --profile hybrid
# Creates ~/.claude-code-router/config.json

# Generate cost-optimized config
betty run router.configure --profile cost-optimized

# Generate quality-first config
betty run router.configure --profile quality-first
```

---

## Advanced Features

### 1. Provider-Specific Transformers

Claude Code Router supports **custom transformers** to modify requests/responses:

```json
{
  "Providers": [
    {
      "name": "custom-provider",
      "api_base_url": "https://api.example.com/chat",
      "transformer": {
        "request": {
          "headers": {
            "X-Betty-Agent": "{agent_name}"
          },
          "body": {
            "custom_field": "value"
          }
        },
        "response": {
          "map": {
            "content": "choices[0].message.content"
          }
        }
      }
    }
  ]
}
```

**Betty use case**: Add Betty-specific metadata to LLM requests for tracking/analytics.

### 2. Fallback Chains

Configure automatic fallback if primary provider fails:

```json
{
  "Router": {
    "default": "openrouter,openai/gpt-4",
    "fallback": [
      "openrouter,anthropic/claude-3.5-sonnet",
      "deepseek,deepseek-chat",
      "ollama,llama3.3:70b"
    ]
  }
}
```

### 3. Cost Tracking

Router can log all requests for cost analysis:

```json
{
  "Logging": {
    "enabled": true,
    "log_file": "~/.claude-code-router/usage.log",
    "include_costs": true
  }
}
```

**Betty enhancement**: Aggregate costs per agent/skill for budget tracking.

---

## Benefits for Betty

### 1. Zero Code Changes
- Betty works **exactly as before**
- No modifications to agent manifests
- No changes to skill implementations
- Drop-in replacement for Claude

### 2. Cost Optimization
- Route simple tasks to cheap models (DeepSeek, local Ollama)
- Route complex reasoning to premium models (GPT-4, Claude Opus)
- Estimated savings: 70-90% vs. all-Claude workflow

### 3. Model Diversity
- Use best model for each task type
- Test agents with multiple models
- Avoid vendor lock-in
- Access latest models instantly

### 4. Local Development
- Use Ollama for offline development
- No API costs during testing
- Faster iteration cycles
- Full privacy (data never leaves your machine)

### 5. Enterprise Features
- Custom model deployment support
- On-premises LLM routing
- Compliance with data residency requirements
- Audit trails via router logging

---

## Testing Strategy

### Phase 1: Validation (Week 1)

```bash
# 1. Install router
npm install -g @musistudio/claude-code-router

# 2. Configure with DeepSeek (cheap for testing)
ccr code  # Interactive setup

# 3. Test existing Betty workflows
ccr code
> /api-design test-service
> /api-validate test-service-spec

# 4. Verify outputs match Claude-generated results
```

### Phase 2: Multi-Model Testing (Week 2)

```yaml
# Test matrix
Models to test:
  - anthropic/claude-3.5-sonnet (baseline)
  - openai/gpt-4 (comparison)
  - deepseek-chat (cost optimization)
  - llama3.3:70b via Ollama (local)

Betty agents to test:
  - api.designer (iterative, complex)
  - api.validator (oneshot, simple)
  - api.compatibility (oneshot, analytical)

Metrics:
  - Output quality (subjective evaluation)
  - Cost per operation
  - Latency
  - Success rate
```

### Phase 3: Production Rollout (Week 3-4)

```bash
# 1. Deploy recommended hybrid config
# 2. Monitor usage and costs
# 3. Tune routing rules based on performance
# 4. Document best practices
```

---

## Limitations & Considerations

### 1. Provider Compatibility
- Not all providers support all Claude features (tools, vision, etc.)
- Some transformers may lose fidelity
- Test thoroughly with each provider

### 2. Context Window Differences
- GPT-4: 128k tokens
- Claude Sonnet: 200k tokens
- Gemini 2.5: 2M+ tokens
- Ensure provider can handle your spec sizes

### 3. Prompt Engineering Differences
- Models may interpret agent instructions differently
- Some tuning may be needed for optimal results
- Claude-specific prompts may not translate perfectly

### 4. Cost Variability
- Pricing changes frequently across providers
- Monitor costs and adjust routing as needed
- Set up billing alerts

### 5. Rate Limits
- Each provider has different rate limits
- Configure appropriate retry logic
- Consider multiple providers for high-volume use

---

## Recommended Next Steps

### Immediate (This Week)
1. ✅ Install Claude Code Router: `npm install -g @musistudio/claude-code-router`
2. ✅ Test with DeepSeek (cheap, fast): Configure and validate
3. ✅ Run existing Betty workflows: Verify compatibility

### Short-term (Next 2 Weeks)
4. Configure hybrid setup (DeepSeek + OpenRouter)
5. Test all Betty agents with multiple models
6. Document optimal routing strategies
7. Measure cost savings vs. Claude-only

### Medium-term (Next Month)
8. Add router configuration to Betty docs
9. Create `router.configure` skill for optimal setup
10. Extend agent manifests with router hints
11. Build cost tracking and analytics

### Long-term (Ongoing)
12. Contribute back to claude-code-router project
13. Share Betty-specific routing strategies with community
14. Explore custom provider integrations
15. Build Betty-specific router dashboard

---

## Conclusion

**Claude Code Router is the perfect solution for Betty's multi-LLM needs:**

✅ **Zero code changes** - Works immediately with existing Betty agents
✅ **Production-ready** - 20k+ stars, active development, MIT license
✅ **Cost-effective** - 70-90% savings with smart routing
✅ **Flexible** - 8+ providers, local models, custom transformers
✅ **Enterprise-ready** - On-premises support, audit logging, fallback chains

**This is Path 3 from our analysis, but already implemented and battle-tested.**

---

## Resources

- **Repository**: https://github.com/musistudio/claude-code-router
- **Documentation**: https://claudecoderouter.com/
- **OpenRouter**: https://openrouter.ai/ (unified API for 200+ models)
- **DeepSeek**: https://platform.deepseek.com/ (cost-effective reasoning)
- **Ollama**: https://ollama.ai/ (local model hosting)

---

## Quick Start Commands

```bash
# Install
npm install -g @musistudio/claude-code-router

# Setup
ccr code  # Follow interactive prompts

# Use Betty as normal (now with any LLM!)
/api-design user-service

# Check which model is being used
/model

# Switch models dynamically
/model deepseek deepseek-chat
```

That's it! Betty now supports any LLM with zero code changes.
