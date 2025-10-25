# Betty Model Recommendations Guide

**Last Updated**: October 2025
**Target Audience**: Betty developers, DevOps engineers, API architects

## Table of Contents

1. [Overview](#overview)
2. [How Claude Code Router Works in Betty](#how-claude-code-router-works-in-betty)
3. [Available Models](#available-models)
4. [Router Contexts](#router-contexts)
5. [Model Recommendations by Agent Type](#model-recommendations-by-agent-type)
6. [Model Recommendations by Task Type](#model-recommendations-by-task-type)
7. [Cost Optimization Strategies](#cost-optimization-strategies)
8. [Configuration Examples](#configuration-examples)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Overview

Betty is designed as an **LLM-agnostic framework** that delegates reasoning to Claude Code. By integrating **Claude Code Router**, you can route different types of work to different AI models based on task complexity, context requirements, and cost considerations.

### Key Benefits

- **Cost Optimization**: Save 70-95% by routing simple tasks to cheaper models
- **Performance Optimization**: Use specialized models for specific tasks (reasoning, large context, etc.)
- **Vendor Flexibility**: Avoid lock-in by using multiple providers
- **Transparent Integration**: Zero Betty code changes required

### Architecture

```
Betty Framework (LLM-agnostic)
    ↓
Claude Code CLI (executes skills)
    ↓
Claude Code Router (intercepts API calls)
    ↓
Multiple LLM Providers (routes based on context)
    ↓
Optimal Model for Each Task
```

---

## How Claude Code Router Works in Betty

### Integration Points

The router operates **outside of Betty** as a transparent proxy:

1. **Betty Agent Execution**: Betty constructs prompts and calls Claude Code
2. **Router Interception**: Router intercepts API calls to `api.anthropic.com`
3. **Context-Based Routing**: Router determines optimal model based on context
4. **Response Transformation**: Router transforms responses back to Claude-compatible format
5. **Transparent Execution**: Betty and Claude Code remain unaware of routing

### Reasoning Modes in Betty

Betty agents define their reasoning complexity in their manifest:

```yaml
# agent.yaml
reasoning_mode: iterative  # or "oneshot"
```

**Reasoning Mode Mapping**:
- `iterative` → Router `think` context (complex reasoning)
- `oneshot` → Router `default` context (standard processing)

---

## Available Models

### Claude Models (Anthropic)

| Model | Context Window | Best For | Pricing (Input/Output per 1M tokens) | Speed |
|-------|----------------|----------|--------------------------------------|-------|
| **Claude Opus 4** | 200K | Maximum intelligence, complex reasoning, research | $15.00 / $75.00 | Slow |
| **Claude Sonnet 4.5** | 200K | Balanced performance, coding, general tasks | $3.00 / $15.00 | Medium |
| **Claude Haiku 3.5** | 200K | Fast responses, simple tasks, cost-efficiency | $0.80 / $4.00 | Fast |

**Key Characteristics**:
- **Opus**: 65% accuracy on GPQA Diamond benchmark, near-human comprehension
- **Sonnet**: 93.7% on HumanEval coding benchmark, excellent code generation
- **Haiku**: 0.36s TTFT (time to first token), outperforms older Opus on some tasks

**Deprecation Notes** (as of October 2025):
- Claude 3 Sonnet: Retired July 21, 2025
- Claude 3 Opus: Deprecated June 30, 2025 (scheduled retirement January 5, 2026)

### DeepSeek Models (DeepSeek)

| Model | Context Window | Best For | Pricing (Input/Output per 1M tokens) | Speed |
|-------|----------------|----------|--------------------------------------|-------|
| **DeepSeek Chat (V3)** | 64K | General conversation, classification, content generation | $0.56 / $1.68 | Fast |
| **DeepSeek Reasoner (R1)** | 128K | Deep reasoning, mathematics, coding, complex analysis | $0.56 / $1.68 | Medium |

**Key Characteristics**:
- **Chat**: Multilingual support, excellent for everyday tasks
- **Reasoner**: Generates extensive reasoning traces before final answer
- **Cost**: Uniform pricing as of September 2025 (previously Chat was cheaper)
- **Free Tier**: Web-based version completely free with no message caps

**Cache Optimization**:
- Cache hit: $0.07 per 1M tokens (92% discount)
- Cache miss: $0.56 per 1M tokens

### OpenAI Models (GPT)

| Model | Context Window | Best For | Pricing (Input/Output per 1M tokens) | Speed |
|-------|----------------|----------|--------------------------------------|-------|
| **GPT-4 Turbo** | 128K | Complex reasoning, coding, multimodal tasks | $10.00 / $30.00 | Medium |
| **GPT-3.5 Turbo** | 16K | Quick queries, basic chatbots, simple content | $0.50 / $1.50 | Fast |

**Key Characteristics**:
- **GPT-4**: Multimodal (text + images), Bar Exam performance, 300 pages/prompt
- **GPT-3.5**: 20x cheaper than GPT-4, faster speeds, text-only
- **Best For**: Organizations already using OpenAI ecosystem

### Google Gemini Models

| Model | Context Window | Best For | Pricing (Input/Output per 1M tokens) | Speed |
|-------|----------------|----------|--------------------------------------|-------|
| **Gemini 2.5 Pro** | 1M (2M coming) | Massive codebases, long documents, video analysis | Varies by provider | Medium |
| **Gemini 2.5 Flash** | 1M | Fast processing with large context | Varies by provider | Fast |

**Key Characteristics**:
- **Largest Context**: 1M tokens (vs Claude 200K, GPT-4 128K, DeepSeek 128K)
- **Recall Performance**: 100% recall up to 530K tokens, 99.7% at 1M tokens
- **Output Capacity**: Pro can output 64K tokens (8x Flash's 8K limit)
- **Multimodal**: Text, audio, images, video, code repositories
- **Best For**: Entire codebase analysis, large API portfolios, video processing

### Local Models (Ollama)

| Model | Context Window | Best For | Pricing | Speed |
|-------|----------------|----------|---------|-------|
| **Llama 3.1 (70B)** | 128K | Local deployment, privacy, cost-free operations | Free | Medium-Slow |
| **Mistral (7B)** | 8K | Fast local inference, simple tasks | Free | Fast |
| **CodeLlama** | 16K | Code generation, local development | Free | Medium |

**Key Characteristics**:
- **Zero Cost**: Run locally without API charges
- **Privacy**: Data never leaves your infrastructure
- **Trade-offs**: Lower quality than commercial models, requires GPU resources

---

## Router Contexts

The Claude Code Router uses **four contexts** to route requests to appropriate models:

### 1. Default Context

**Purpose**: Standard agent orchestration and reasoning
**Betty Use Cases**: General agent execution, skill selection, decision-making
**Betty Agents**: `api.analyzer`, `code.reviewer`, most agents with `reasoning_mode: oneshot`

**Recommended Models**:
- **Cost-Optimized**: DeepSeek Chat ($0.56/$1.68 per 1M tokens)
- **Balanced**: Claude Sonnet 4.5 ($3.00/$15.00 per 1M tokens)
- **Quality-First**: GPT-4 Turbo ($10/$30 per 1M tokens)

**Configuration Example**:
```json
"Router": {
  "default": "deepseek,deepseek-chat"
}
```

### 2. Background Context

**Purpose**: Asynchronous, low-priority, long-running tasks
**Betty Use Cases**: Bulk API validation, registry updates, documentation generation, data transformations
**Betty Agents**: Batch operations, marketplace updates, artifact generation

**Recommended Models**:
- **Ultra Cost-Optimized**: Local Ollama models (free)
- **Cost-Optimized**: DeepSeek Chat with caching ($0.07 cache hit)
- **Fast & Cheap**: GPT-3.5 Turbo ($0.50/$1.50 per 1M tokens)
- **Balanced**: Claude Haiku 3.5 ($0.80/$4.00 per 1M tokens)

**Configuration Example**:
```json
"Router": {
  "background": "ollama,llama3.1:70b"
}
```

### 3. Think Context

**Purpose**: Complex reasoning, iterative refinement, deep analysis
**Betty Use Cases**: API design, architecture decisions, security analysis
**Betty Agents**: `api.designer`, `api.architect`, `security.architect`, `data.architect`, agents with `reasoning_mode: iterative`

**Recommended Models**:
- **Best Reasoning**: DeepSeek Reasoner ($0.56/$1.68 per 1M tokens)
- **Code Excellence**: Claude Sonnet 4.5 ($3.00/$15.00 per 1M tokens)
- **Maximum Intelligence**: Claude Opus 4 ($15/$75 per 1M tokens)
- **Extended Thinking**: GPT-4 Turbo ($10/$30 per 1M tokens)

**Configuration Example**:
```json
"Router": {
  "think": "deepseek,deepseek-reasoner"
}
```

### 4. LongContext Context

**Purpose**: Processing large codebases, extensive documentation, massive API specs
**Betty Use Cases**: Large API portfolios, cross-spec compatibility, codebase-wide refactoring
**Betty Agents**: Multi-file analysis, comprehensive reviews, large-scale validation

**Recommended Models**:
- **Massive Context**: Gemini 2.5 Pro (1M tokens, 2M coming)
- **Balanced Context**: GPT-4 Turbo (128K tokens)
- **Cost-Effective Context**: DeepSeek Reasoner (128K tokens)

**Configuration Example**:
```json
"Router": {
  "longContext": "openrouter,google/gemini-2.5-pro-preview"
}
```

### Context Selection Matrix

| Task Characteristic | Context to Use |
|---------------------|----------------|
| Simple validation, one-pass analysis | `default` |
| Bulk operations, documentation gen | `background` |
| Iterative design, complex reasoning | `think` |
| Multiple files, large specs (>50K tokens) | `longContext` |
| Real-time user interaction | `default` |
| Cost is primary concern | `background` |
| Quality is primary concern | `think` |
| Processing entire codebase | `longContext` |

---

## Model Recommendations by Agent Type

### API-Focused Agents

#### `api.designer` (Iterative)

**Reasoning Mode**: `iterative`
**Complexity**: High
**Context Requirements**: Medium (10-50K tokens)

**Recommended Setup**:
1. **Primary**: DeepSeek Reasoner (best cost/quality balance)
2. **Alternative**: Claude Sonnet 4.5 (best for complex API design)
3. **Budget**: DeepSeek Chat (acceptable quality at low cost)

**Router Context**: `think`

**Rationale**: Iterative API design requires multiple refinement cycles. DeepSeek Reasoner excels at generating reasoning traces for design decisions while remaining cost-effective.

#### `api.analyzer` (Oneshot)

**Reasoning Mode**: `oneshot`
**Complexity**: Medium
**Context Requirements**: Medium (10-50K tokens)

**Recommended Setup**:
1. **Primary**: DeepSeek Chat (fast and cost-effective)
2. **Alternative**: Claude Haiku 3.5 (fastest TTFT)
3. **Quality-First**: Claude Sonnet 4.5 (best accuracy)

**Router Context**: `default`

**Rationale**: Compatibility analysis is pattern-matching with some reasoning. Fast, cost-effective models handle this well.

#### `api.architect`

**Reasoning Mode**: Not explicitly set (defaults to oneshot)
**Complexity**: High
**Context Requirements**: Medium-High (20-100K tokens)

**Recommended Setup**:
1. **Primary**: Claude Sonnet 4.5 (best for architecture design)
2. **Alternative**: DeepSeek Reasoner (cost-effective reasoning)
3. **Budget**: DeepSeek Chat

**Router Context**: `think` (override default due to high complexity)

**Rationale**: Comprehensive API architecture requires deep reasoning about system design, scalability, and best practices.

### Meta/Framework Agents

#### `meta.agent`, `meta.skill`, `meta.command`

**Reasoning Mode**: Varies
**Complexity**: High (code generation)
**Context Requirements**: Medium (10-50K tokens)

**Recommended Setup**:
1. **Primary**: Claude Sonnet 4.5 (best code generation)
2. **Alternative**: DeepSeek Reasoner (good at structured output)
3. **Budget**: DeepSeek Chat

**Router Context**: `think` (requires understanding of Betty framework)

**Rationale**: Meta-agents generate Betty artifacts (agents, skills, commands) which requires deep understanding of framework conventions and code generation expertise.

### Domain-Specific Architects

#### `security.architect`

**Reasoning Mode**: Not explicitly set
**Complexity**: Very High
**Context Requirements**: High (50-200K tokens with security frameworks)

**Recommended Setup**:
1. **Primary**: Claude Opus 4 (best for security reasoning)
2. **Alternative**: Claude Sonnet 4.5 (strong security understanding)
3. **Budget**: DeepSeek Reasoner

**Router Context**: `think`

**Rationale**: Security architecture requires expert-level understanding of STRIDE, NIST, ISO 27001, OWASP. Claude models excel at security domain knowledge.

#### `data.architect`

**Reasoning Mode**: Not explicitly set
**Complexity**: High
**Context Requirements**: Medium-High (20-100K tokens)

**Recommended Setup**:
1. **Primary**: Claude Sonnet 4.5 (strong data modeling)
2. **Alternative**: DeepSeek Reasoner
3. **Context-Heavy**: Gemini 2.5 Pro (if analyzing existing large schemas)

**Router Context**: `think` (or `longContext` for large schema analysis)

**Rationale**: Data modeling requires understanding relationships, normalization, and governance principles.

#### `code.reviewer`

**Reasoning Mode**: Not explicitly set
**Complexity**: Medium
**Context Requirements**: Variable (1K-200K tokens depending on code size)

**Recommended Setup**:
- **Small PRs (<10K tokens)**: DeepSeek Chat or Claude Haiku 3.5
- **Medium PRs (10-50K tokens)**: Claude Sonnet 4.5
- **Large PRs (50-200K tokens)**: Gemini 2.5 Pro
- **Entire Codebase**: Gemini 2.5 Pro

**Router Context**: `default` for small, `longContext` for large

**Rationale**: Code review quality scales with model capability, but context window is crucial for large changes.

### Batch Processing Agents

#### `deployment.engineer`, `file.processor`, `governance.manager`

**Reasoning Mode**: Typically oneshot
**Complexity**: Low-Medium
**Context Requirements**: Low (1-10K tokens)

**Recommended Setup**:
1. **Primary**: Local Ollama (zero cost for batch jobs)
2. **Alternative**: DeepSeek Chat (extremely cheap)
3. **Fast**: Claude Haiku 3.5

**Router Context**: `background`

**Rationale**: Batch operations prioritize cost over quality. Run overnight with free/cheap models.

---

## Model Recommendations by Task Type

### Task: OpenAPI Spec Generation

**Complexity**: Medium
**Input Size**: Small (1-5K tokens)
**Output Size**: Large (5-50K tokens)

**Recommended Models**:
1. **DeepSeek Chat** (cost-effective, good at structured output)
2. **Claude Sonnet 4.5** (best quality OpenAPI specs)
3. **GPT-4 Turbo** (good at YAML/JSON generation)

**Router Context**: `default`

### Task: Breaking Change Analysis

**Complexity**: High
**Input Size**: Large (20-200K tokens - comparing two versions)
**Output Size**: Medium (1-10K tokens)

**Recommended Models**:
1. **Gemini 2.5 Pro** (can hold both full specs in context)
2. **Claude Sonnet 4.5** (excellent at API comparison)
3. **DeepSeek Reasoner** (good reasoning about compatibility)

**Router Context**: `longContext` (for large specs) or `think` (for medium specs)

### Task: Security Threat Modeling

**Complexity**: Very High
**Input Size**: Medium (10-50K tokens)
**Output Size**: Large (10-100K tokens)

**Recommended Models**:
1. **Claude Opus 4** (best security reasoning)
2. **Claude Sonnet 4.5** (strong security, better cost)
3. **DeepSeek Reasoner** (budget option)

**Router Context**: `think`

### Task: Bulk API Validation

**Complexity**: Low
**Input Size**: Large (many small specs, 1-10K each)
**Output Size**: Small (pass/fail results)

**Recommended Models**:
1. **Local Ollama** (zero cost, good for validation rules)
2. **DeepSeek Chat** (fast and cheap)
3. **Claude Haiku 3.5** (fastest, low cost)

**Router Context**: `background`

### Task: Data Model Generation from ER Diagrams

**Complexity**: Medium
**Input Size**: Medium (10-50K tokens with diagrams)
**Output Size**: Large (20-100K tokens of schemas)

**Recommended Models**:
1. **Claude Sonnet 4.5** (best at structured data modeling)
2. **GPT-4 Turbo** (multimodal, can analyze diagram images)
3. **DeepSeek Chat** (cost-effective)

**Router Context**: `default` or `think`

### Task: Large API Portfolio Migration

**Complexity**: High
**Input Size**: Very Large (500K-2M tokens - entire portfolio)
**Output Size**: Large (50-500K tokens)

**Recommended Models**:
1. **Gemini 2.5 Pro** (only model that can hold entire portfolio)
2. **Process in chunks with Claude Sonnet** (if portfolio can be split)

**Router Context**: `longContext`

### Task: Agile Story Generation from Epic

**Complexity**: Medium
**Input Size**: Small-Medium (1-20K tokens)
**Output Size**: Medium (5-50K tokens)

**Recommended Models**:
1. **Claude Sonnet 4.5** (best at structured decomposition)
2. **DeepSeek Chat** (cost-effective)
3. **GPT-4 Turbo** (good at task breakdown)

**Router Context**: `default`

---

## Cost Optimization Strategies

### Strategy 1: Hybrid Routing (Recommended)

Route different tasks to different cost tiers:

```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "ollama,llama3.1:70b",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**Estimated Cost Breakdown** (per 1M tokens processed):
- 50% background tasks: $0 (Ollama) = $0
- 30% default tasks: $0.56 (DeepSeek Chat) = $0.17
- 15% think tasks: $0.56 (DeepSeek Reasoner) = $0.08
- 5% longContext tasks: ~$2.00 (Gemini) = $0.10
- **Total: ~$0.35 per 1M input tokens**

**Compared to All Claude Sonnet**: $3.00 per 1M tokens
**Savings**: 88%

### Strategy 2: DeepSeek-First

Use DeepSeek for everything except extreme cases:

```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "deepseek,deepseek-reasoner"
  }
}
```

**Cost**: $0.56 per 1M input tokens (uniform)
**Compared to All Claude Sonnet**: $3.00 per 1M tokens
**Savings**: 81%

**Benefits**: Simplest configuration, consistent behavior, very cheap
**Trade-offs**: Lower quality than Claude for complex tasks, limited context (128K max)

### Strategy 3: Free-First (Maximum Savings)

Use local models for everything, fallback to paid only when necessary:

```json
{
  "Router": {
    "default": "ollama,llama3.1:70b",
    "background": "ollama,mistral:7b",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "ollama,llama3.1:70b"
  }
}
```

**Cost**: ~$0.08 per 1M tokens (only think context paid)
**Savings**: 97% vs all Claude

**Benefits**: Minimal API costs, privacy (all local)
**Trade-offs**: Requires GPU infrastructure, lower quality, slower

### Strategy 4: Quality-First

Use best models for everything:

```json
{
  "Router": {
    "default": "anthropic,claude-sonnet-4.5",
    "background": "anthropic,claude-haiku-3.5",
    "think": "anthropic,claude-opus-4",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**Cost**: ~$8 per 1M input tokens (weighted average)
**Compared to All Claude Opus**: $15 per 1M tokens
**Savings**: 47% (by using cheaper models for simple tasks)

**Benefits**: Best possible quality
**Trade-offs**: 23x more expensive than DeepSeek strategy

### Strategy 5: Task-Specific Optimization

Optimize router based on your specific Betty usage:

**If you primarily use API design agents**:
```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "think": "anthropic,claude-sonnet-4.5",  // Splurge on API design
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**If you process large API portfolios**:
```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"  // Critical for large specs
  }
}
```

**If you run many batch jobs**:
```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "ollama,llama3.1:70b",  // Free for batch
    "think": "anthropic,claude-sonnet-4.5"
  }
}
```

### Cost Tracking Best Practices

1. **Enable Router Logging**: Track which models are used for which tasks
2. **Monitor Token Usage**: Use provider dashboards to see actual consumption
3. **Calculate Cost per Agent**: Determine which agents are most expensive
4. **A/B Test Models**: Compare quality vs cost for specific use cases
5. **Review Monthly**: Adjust router configuration based on usage patterns

---

## Configuration Examples

### Minimal Setup (Single Provider)

```json
{
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat"
  }
}
```

### Recommended Production Setup

```json
{
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    },
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": [
        "anthropic/claude-sonnet-4.5",
        "google/gemini-2.5-pro-preview"
      ]
    },
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/v1/chat/completions",
      "models": ["llama3.1:70b", "mistral:7b"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "ollama,llama3.1:70b",
    "think": "openrouter,anthropic/claude-sonnet-4.5",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**Cost Profile**: ~$1.50 per 1M input tokens (75% savings vs all Claude)

### Enterprise Setup with Fallbacks

```json
{
  "Providers": [
    {
      "name": "primary-deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    },
    {
      "name": "fallback-openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": [
        "anthropic/claude-sonnet-4.5",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-pro-preview",
        "openai/gpt-4-turbo"
      ]
    }
  ],
  "Router": {
    "default": "primary-deepseek,deepseek-chat",
    "background": "primary-deepseek,deepseek-chat",
    "think": "fallback-openrouter,anthropic/claude-sonnet-4.5",
    "longContext": "fallback-openrouter,google/gemini-2.5-pro-preview"
  },
  "Fallback": {
    "strategy": "cascade",
    "order": ["primary-deepseek", "fallback-openrouter"]
  }
}
```

### Quality-Optimized Setup

```json
{
  "Providers": [
    {
      "name": "anthropic",
      "api_base_url": "https://api.anthropic.com/v1/chat/completions",
      "api_key": "sk-ant-xxx",
      "models": ["claude-opus-4", "claude-sonnet-4.5", "claude-haiku-3.5"]
    },
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-or-v1-xxx",
      "models": ["google/gemini-2.5-pro-preview"]
    }
  ],
  "Router": {
    "default": "anthropic,claude-sonnet-4.5",
    "background": "anthropic,claude-haiku-3.5",
    "think": "anthropic,claude-opus-4",
    "longContext": "openrouter,google/gemini-2.5-pro-preview"
  }
}
```

**Cost Profile**: ~$8 per 1M input tokens (highest quality)

---

## Best Practices

### 1. Start Simple, Optimize Later

**Phase 1: Single Provider** (Week 1)
```json
"Router": {
  "default": "deepseek,deepseek-chat"
}
```
- Establish baseline functionality
- Measure quality and cost
- Identify pain points

**Phase 2: Add Reasoning** (Week 2)
```json
"Router": {
  "default": "deepseek,deepseek-chat",
  "think": "deepseek,deepseek-reasoner"
}
```
- Improve complex task quality
- Measure improvement vs cost

**Phase 3: Add Context** (Week 3-4)
```json
"Router": {
  "default": "deepseek,deepseek-chat",
  "think": "deepseek,deepseek-reasoner",
  "longContext": "openrouter,google/gemini-2.5-pro-preview"
}
```
- Enable large spec processing
- Optimize for your specific workload

### 2. Match Models to Agent Reasoning Modes

**Explicitly Set Reasoning Modes** in agent manifests:

```yaml
# agents/my-agent/agent.yaml
name: my.agent
reasoning_mode: iterative  # or "oneshot"
```

**Review Current Agents**:
```bash
# Find agents without explicit reasoning modes
grep -L "reasoning_mode" agents/*/agent.yaml
```

**Guidelines**:
- `iterative` → Use for multi-step design, complex analysis, architecture
- `oneshot` → Use for validation, simple transformations, quick analysis

### 3. Monitor and Adjust

**Enable Router Logging**:
```bash
export CCR_LOG_LEVEL=debug
ccr code
```

**Track Metrics**:
- Cost per agent
- Token usage per context
- Model error rates
- Response quality (human review)

**Monthly Review**:
- Identify most expensive agents
- Test cheaper models for high-volume tasks
- Adjust router configuration

### 4. Use Context Windows Efficiently

**Context Window Sizes**:
- Gemini 2.5 Pro: 1M tokens (~4M characters)
- GPT-4 Turbo: 128K tokens (~512K characters)
- DeepSeek Reasoner: 128K tokens (~512K characters)
- Claude Sonnet: 200K tokens (~800K characters)

**Optimization Strategies**:
- **Split large tasks**: Break 500K token task into 5x 100K tasks (use cheaper model)
- **Summarize incrementally**: Process large specs in chunks, summarize each
- **Cache aggressively**: DeepSeek offers 92% discount on cache hits

### 5. Leverage Free Models for Development

**Development Setup**:
```json
{
  "Router": {
    "default": "ollama,llama3.1:70b",
    "think": "ollama,llama3.1:70b",
    "longContext": "ollama,llama3.1:70b"
  }
}
```

**Benefits**:
- Zero cost for development/testing
- Fast iteration
- Privacy (no data leaves local machine)

**Switch to Paid for Production**:
```bash
# Use environment-based config
cp .claude-code-router/config.dev.json .claude-code-router/config.json  # Dev
cp .claude-code-router/config.prod.json .claude-code-router/config.json  # Prod
```

### 6. Test Agent Quality Across Models

**Create Test Suite**:
```bash
# Test api.designer with different models
betty test agents/api.designer --model deepseek-chat
betty test agents/api.designer --model claude-sonnet-4.5
betty test agents/api.designer --model gpt-4-turbo
```

**Compare Results**:
- OpenAPI spec validity
- Guideline compliance
- Response time
- Cost per run

**Document Findings**:
```markdown
# agents/api.designer/MODEL_TESTS.md

## Test Results (2025-10-25)

| Model | Quality Score | Avg Time | Cost per Run |
|-------|---------------|----------|--------------|
| DeepSeek Chat | 8.5/10 | 12s | $0.02 |
| Claude Sonnet | 9.5/10 | 18s | $0.08 |
| GPT-4 Turbo | 9.0/10 | 15s | $0.15 |

**Recommendation**: Use DeepSeek Chat for most API designs, Claude Sonnet for critical/complex APIs
```

### 7. Plan for Model Deprecations

**Models Currently Deprecated** (October 2025):
- Claude 3 Opus (retirement: January 5, 2026)
- Claude 3 Sonnet (retired: July 21, 2025)

**Migration Strategy**:
1. **Monitor announcements**: Subscribe to provider newsletters
2. **Version your config**: Keep dated configs for rollback
3. **Test new models early**: Evaluate replacements before forced migration
4. **Use version pinning**: Specify exact model versions in config

### 8. Security Considerations

**API Key Management**:
```bash
# Never commit keys to git
echo ".claude-code-router/config.json" >> .gitignore

# Use environment variables
export DEEPSEEK_API_KEY="sk-xxx"
export OPENROUTER_API_KEY="sk-or-v1-xxx"

# Reference in config
{
  "api_key": "${DEEPSEEK_API_KEY}"
}
```

**Data Privacy**:
- **Local models**: Data never leaves infrastructure
- **Cloud models**: Review provider privacy policies
- **Sensitive data**: Use local models or vetted providers (SOC 2, GDPR compliant)

**Audit Logging**:
```bash
# Enable request/response logging
export CCR_LOG_REQUESTS=true
export CCR_LOG_RESPONSES=true
export CCR_LOG_DIR=/var/log/betty-router
```

---

## Troubleshooting

### Issue: Router not routing to expected model

**Symptoms**: All requests use same model despite router configuration

**Debug Steps**:
```bash
# 1. Verify router is running
ps aux | grep ccr

# 2. Check router logs
export CCR_LOG_LEVEL=debug
ccr code

# 3. Verify context detection
# Look for log lines like: "Detected context: think"
```

**Common Causes**:
- Router not properly initialized
- Context detection not working (update Claude Code Router)
- Config file syntax error

### Issue: Model returns errors or poor quality

**Symptoms**: Agent executions fail or produce incorrect results

**Debug Steps**:
```bash
# 1. Test model directly
curl https://api.deepseek.com/chat/completions \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Hello"}]}'

# 2. Check model compatibility
# Ensure model supports Claude-style API format

# 3. Try different model
# Edit router config, change to known-good model
```

**Common Causes**:
- Model doesn't support required features (function calling, system prompts)
- Model context window too small for task
- Model not trained for task type (e.g., coding)

### Issue: High costs despite cheap model selection

**Symptoms**: Bill higher than expected given router configuration

**Debug Steps**:
```bash
# 1. Enable detailed logging
export CCR_LOG_REQUESTS=true

# 2. Analyze token usage
grep "tokens_used" /var/log/betty-router/*.log | awk '{sum+=$NF} END {print sum}'

# 3. Check which models are actually being used
grep "model=" /var/log/betty-router/*.log | sort | uniq -c
```

**Common Causes**:
- Fallback to expensive model due to errors
- Incorrect context routing (think context used for simple tasks)
- Large output tokens (cost often dominated by output)

### Issue: Gemini "context window exceeded" errors

**Symptoms**: Large specs fail with context errors

**Debug Steps**:
```bash
# 1. Check actual token count
betty estimate-tokens --file large-spec.yaml
# If > 1M, Gemini 2.5 Pro current limit exceeded

# 2. Wait for 2M context window
# Gemini 2.5 Pro expanding from 1M to 2M tokens "coming soon"

# 3. Split task
# Process in chunks or summarize incrementally
```

### Issue: Local Ollama models too slow

**Symptoms**: Background tasks take hours with Ollama

**Debug Steps**:
```bash
# 1. Check GPU usage
nvidia-smi

# 2. Check model size
ollama list
# If using 70B model, consider 7B or 13B for speed

# 3. Monitor system resources
htop
```

**Solutions**:
- Use smaller models (mistral:7b instead of llama3.1:70b)
- Upgrade GPU hardware
- Use cloud models for time-sensitive tasks

### Issue: DeepSeek cache not working

**Symptoms**: Not seeing 92% cost reduction from cache hits

**Debug Steps**:
```bash
# 1. Check if requests are identical
# Cache requires exact prefix match

# 2. Enable cache in requests
# Ensure router is sending cache-compatible requests

# 3. Check billing dashboard
# Verify cache hit rate
```

**Common Causes**:
- Request prompts vary (timestamps, UUIDs in prompts)
- Cache TTL expired (unclear what DeepSeek's TTL is)
- Cache not enabled for model tier

---

## Appendix: Quick Reference

### Model Cheat Sheet

| Need | Use Model | Cost | Context |
|------|-----------|------|---------|
| Cheapest | DeepSeek Chat | $0.56/1M | 64K |
| Free | Ollama Llama 3.1 | $0 | 128K |
| Best Quality | Claude Opus 4 | $15/1M | 200K |
| Best Balance | Claude Sonnet 4.5 | $3/1M | 200K |
| Best Coding | Claude Sonnet 4.5 | $3/1M | 200K |
| Best Reasoning | DeepSeek Reasoner | $0.56/1M | 128K |
| Largest Context | Gemini 2.5 Pro | Varies | 1M (2M soon) |
| Fastest | Claude Haiku 3.5 | $0.80/1M | 200K |
| Best Multimodal | GPT-4 Turbo | $10/1M | 128K |

### Context Routing Cheat Sheet

| Agent | Reasoning Mode | Recommended Context | Recommended Model |
|-------|----------------|---------------------|-------------------|
| api.designer | iterative | think | Claude Sonnet 4.5 |
| api.analyzer | oneshot | default | DeepSeek Chat |
| api.architect | (default) | think | Claude Sonnet 4.5 |
| meta.agent | (default) | think | Claude Sonnet 4.5 |
| meta.skill | (default) | think | Claude Sonnet 4.5 |
| security.architect | (default) | think | Claude Opus 4 |
| data.architect | (default) | think | Claude Sonnet 4.5 |
| code.reviewer | (default) | default/longContext | Gemini 2.5 Pro (large PRs) |
| deployment.engineer | (default) | background | Ollama/DeepSeek Chat |
| file.processor | (default) | background | Ollama/DeepSeek Chat |

### Cost Comparison (per 1M input tokens)

| Strategy | Cost | Savings vs Claude Sonnet |
|----------|------|--------------------------|
| Free-First (mostly Ollama) | $0.08 | 97% |
| DeepSeek-First | $0.56 | 81% |
| Hybrid (recommended) | $1.50 | 50% |
| Claude Sonnet (baseline) | $3.00 | 0% |
| Quality-First (Claude Opus heavy) | $8.00 | -167% |

---

## Additional Resources

- **Claude Code Router Documentation**: https://github.com/musistudio/claude-code-router
- **Betty Integration Guide**: [claude-code-router-integration.md](./claude-code-router-integration.md)
- **Multi-LLM Integration Paths**: [multi-llm-integration-paths.md](./multi-llm-integration-paths.md)
- **DeepSeek API Docs**: https://api-docs.deepseek.com/
- **OpenRouter Documentation**: https://openrouter.ai/docs
- **Anthropic Model Comparison**: https://docs.anthropic.com/claude/docs/models-overview
- **OpenAI Model Docs**: https://platform.openai.com/docs/models
- **Google Gemini Docs**: https://ai.google.dev/gemini-api/docs
- **Ollama Models**: https://ollama.ai/library

---

**Document Version**: 1.0
**Last Updated**: October 25, 2025
**Maintainer**: Betty Core Team

**Feedback**: If you discover effective model configurations or routing strategies, please contribute to this document via pull request.
