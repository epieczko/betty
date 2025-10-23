# Claude Code Router Configuration Examples for Betty

This directory contains ready-to-use configuration files for Claude Code Router, optimized for Betty agents.

## Quick Start

1. **Install Claude Code Router**:
   ```bash
   npm install -g @musistudio/claude-code-router
   ```

2. **Choose a configuration** from the examples below

3. **Copy to router config location**:
   ```bash
   cp <example-file> ~/.claude-code-router/config.json
   ```

4. **Set required API keys** (see each config's requirements)

5. **Start the router**:
   ```bash
   ccr start
   ```

6. **Use Claude Code through router**:
   ```bash
   ccr code
   ```

## Available Configurations

### 1. `hybrid-balanced.json` ⭐ RECOMMENDED

**Best for**: Most users, production use, balanced cost/quality

**Providers**: DeepSeek + OpenRouter (Gemini)

**Routing Strategy**:
- Default & Background: DeepSeek Chat (fast, cheap)
- Think: DeepSeek Reasoner (specialized reasoning)
- Long Context: Gemini 2.5 Pro (2M+ tokens)

**Cost Profile**: 20-30% of Claude-only costs

**Required API Keys**:
```bash
export DEEPSEEK_API_KEY=sk-...
export OPENROUTER_API_KEY=sk-or-v1-...
```

**Setup**:
```bash
cp hybrid-balanced.json ~/.claude-code-router/config.json
ccr start
```

---

### 2. `cost-optimized.json`

**Best for**: Cost-conscious users, high-volume usage

**Providers**: DeepSeek + Anthropic (fallback only)

**Routing Strategy**:
- Default & Background: DeepSeek Chat
- Think: DeepSeek Reasoner
- Long Context: Claude Sonnet (only when needed)

**Cost Profile**: 10-20% of Claude-only costs

**Required API Keys**:
```bash
export DEEPSEEK_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...  # Optional fallback
```

**Setup**:
```bash
cp cost-optimized.json ~/.claude-code-router/config.json
ccr start
```

---

### 3. `quality-first.json`

**Best for**: Enterprise use, critical projects, maximum quality

**Providers**: OpenRouter (GPT-4, O1, Gemini, Claude)

**Routing Strategy**:
- Default: GPT-4
- Background: Claude Sonnet
- Think: OpenAI O1 (advanced reasoning)
- Long Context: Gemini 2.5 Pro

**Cost Profile**: 120-150% of Claude-only (premium models)

**Required API Keys**:
```bash
export OPENROUTER_API_KEY=sk-or-v1-...
```

**Setup**:
```bash
cp quality-first.json ~/.claude-code-router/config.json
ccr start
```

---

### 4. `local-dev.json`

**Best for**: Local development, offline work, privacy-sensitive projects

**Providers**: Ollama (local) + Anthropic (complex tasks only)

**Routing Strategy**:
- Default & Background: Llama 3.3 70B (local)
- Think: Claude Opus (online when needed)
- Long Context: Claude Sonnet

**Cost Profile**: <5% (mostly hardware costs)

**Prerequisites**:
1. Install Ollama: https://ollama.ai/
2. Pull models:
   ```bash
   ollama pull llama3.3:70b
   ollama pull mistral-large
   ```

**Required API Keys**:
```bash
export ANTHROPIC_API_KEY=sk-ant-...  # For think/longContext fallback
```

**Setup**:
```bash
cp local-dev.json ~/.claude-code-router/config.json
ccr start
```

---

## Betty Agent Mapping

Different Betty agents benefit from different routing contexts:

| Betty Agent | Reasoning Mode | Recommended Context | Example Configuration |
|-------------|----------------|---------------------|----------------------|
| `api.designer` | iterative | think | DeepSeek Reasoner / O1 / Claude Opus |
| `api.validate` | oneshot | default | DeepSeek Chat / GPT-3.5 / Claude Haiku |
| `api.compatibility` | oneshot | think | DeepSeek Reasoner / Claude Sonnet |
| `api.generate-models` | oneshot | background | Local Ollama / DeepSeek Chat |
| Large portfolio analysis | oneshot | longContext | Gemini 2.5 Pro / Claude Sonnet |

## Configuration Customization

### Changing Default Models

Edit the `Router` section in your config:

```json
"Router": {
  "default": "provider-name,model-name",
  "background": "provider-name,model-name",
  "think": "provider-name,model-name",
  "longContext": "provider-name,model-name"
}
```

### Adding New Providers

Add to the `Providers` array:

```json
{
  "name": "my-provider",
  "api_base_url": "https://api.example.com/v1/chat/completions",
  "api_key": "${MY_PROVIDER_API_KEY}",
  "models": ["model-1", "model-2"]
}
```

### Fallback Configuration

Add fallback chains for reliability:

```json
"Router": {
  "default": "primary-provider,model",
  "fallback": [
    "secondary-provider,model",
    "tertiary-provider,model"
  ]
}
```

## Testing Your Configuration

1. **Validate JSON**:
   ```bash
   cat ~/.claude-code-router/config.json | python -m json.tool
   ```

2. **Check router status**:
   ```bash
   ccr status
   ```

3. **View model configuration**:
   ```bash
   ccr model
   ```

4. **Test with Betty**:
   ```bash
   ccr code
   # Then run Betty commands
   /api-design test-service
   ```

## Cost Comparison

Estimated costs per 1M tokens (input/output average):

| Provider/Model | Cost/1M Tokens | Relative to Claude Sonnet |
|----------------|----------------|---------------------------|
| Claude Opus 4 | $15 / $75 | 5x |
| Claude Sonnet 3.5 | $3 / $15 | 1x (baseline) |
| Claude Haiku 3.5 | $0.80 / $4 | 0.27x |
| GPT-4 | $10 / $30 | 2.2x |
| DeepSeek Chat | $0.14 / $0.28 | 0.05x |
| DeepSeek Reasoner | $0.55 / $2.19 | 0.15x |
| Gemini 2.5 Pro | $1.25 / $10 | 0.62x |
| Ollama (local) | $0 | 0x (free) |

**Example Monthly Costs** (assuming 100M tokens/month):

| Configuration | Estimated Monthly Cost |
|---------------|----------------------|
| All Claude Sonnet | $1,800 |
| Hybrid Balanced | $360-540 (70-80% savings) |
| Cost Optimized | $180-270 (85-90% savings) |
| Local Dev | $50-100 (95%+ savings, hardware only) |
| Quality First | $2,400-3,000 (premium models) |

## API Key Setup

### DeepSeek
1. Sign up: https://platform.deepseek.com/
2. Generate API key
3. Export: `export DEEPSEEK_API_KEY=sk-...`

### OpenRouter
1. Sign up: https://openrouter.ai/
2. Generate API key
3. Export: `export OPENROUTER_API_KEY=sk-or-v1-...`

### Anthropic
1. Sign up: https://console.anthropic.com/
2. Generate API key
3. Export: `export ANTHROPIC_API_KEY=sk-ant-...`

### Ollama (Local)
1. Install: https://ollama.ai/
2. Pull models: `ollama pull llama3.3:70b`
3. No API key needed (runs locally)

## Troubleshooting

### Router won't start
```bash
ccr stop
ccr start
```

### Invalid configuration
```bash
# Validate JSON
cat ~/.claude-code-router/config.json | python -m json.tool

# Check logs
tail -f ~/.claude-code-router/logs/*.log
```

### Model not found
```bash
# Check available models
ccr model

# Verify provider configuration
cat ~/.claude-code-router/config.json
```

### API key issues
```bash
# Verify keys are set
env | grep -i "API_KEY"

# Test individual provider
curl -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  https://api.deepseek.com/chat/completions
```

## Resources

- **Claude Code Router**: https://github.com/musistudio/claude-code-router
- **Betty Integration Guide**: `/docs/claude-code-router-integration.md`
- **Betty Architecture**: `/docs/betty-architecture.md`
- **Setup Test Results**: `/docs/claude-code-router-setup-test.md`

## Support

For issues specific to:
- **Router**: Open issue at https://github.com/musistudio/claude-code-router/issues
- **Betty**: Open issue at Betty's repository
- **Configuration**: Check Betty docs in `/docs/`
