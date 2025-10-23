# Ollama Setup Guide for Betty with Claude Code Router

## Why Ollama?

**Ollama** enables you to run LLMs **locally** on your machine:
- ✅ **Free**: No API costs (just hardware)
- ✅ **Private**: Data never leaves your machine
- ✅ **Offline**: Works without internet
- ✅ **Fast**: No network latency
- ✅ **95%+ cost savings** vs cloud APIs

Perfect for Betty development and testing!

---

## Installation (Local Environment)

### macOS

```bash
# Download and install from website
open https://ollama.com/download

# Or use Homebrew
brew install ollama
```

### Linux

```bash
# Install script
curl -fsSL https://ollama.ai/install.sh | sh

# Or download binary directly
curl -L https://ollama.com/download/ollama-linux-amd64 \
  -o /usr/local/bin/ollama
chmod +x /usr/local/bin/ollama
```

### Windows

Download installer from: https://ollama.com/download

---

## Starting Ollama

```bash
# Start Ollama server
ollama serve

# This runs on http://localhost:11434
# Keep this running in a terminal
```

---

## Downloading Models for Betty

### Recommended Models for Betty Agents

#### 1. **Llama 3.3 70B** (Best all-around)
```bash
ollama pull llama3.3:70b
```

**Specs**:
- Size: ~40GB
- RAM needed: 48GB+
- Performance: Excellent for code, reasoning
- Best for: Default agent operations

#### 2. **Qwen 2.5 72B** (Best for code)
```bash
ollama pull qwen2.5:72b
```

**Specs**:
- Size: ~41GB
- RAM needed: 48GB+
- Performance: Outstanding code generation
- Best for: API design, model generation

#### 3. **Llama 3.3 8B** (Lightweight)
```bash
ollama pull llama3.3:8b
```

**Specs**:
- Size: ~4.7GB
- RAM needed: 8GB+
- Performance: Good for simple tasks
- Best for: Background operations, validation

#### 4. **DeepSeek-R1** (Reasoning)
```bash
ollama pull deepseek-r1:70b
```

**Specs**:
- Size: ~40GB
- RAM needed: 48GB+
- Performance: Specialized reasoning
- Best for: Complex problem-solving

#### 5. **Mistral Large** (Balanced)
```bash
ollama pull mistral-large
```

**Specs**:
- Size: ~39GB
- RAM needed: 48GB+
- Performance: Well-rounded
- Best for: General-purpose tasks

### Hardware Requirements

| Model Size | Minimum RAM | Recommended RAM | GPU VRAM | CPU |
|------------|-------------|-----------------|----------|-----|
| 7-8B | 8GB | 16GB | 6GB+ | 4+ cores |
| 13B | 16GB | 32GB | 8GB+ | 8+ cores |
| 34B | 32GB | 64GB | 24GB+ | 16+ cores |
| 70B | 48GB | 128GB | 48GB+ | 24+ cores |

**Tip**: If you have limited RAM, use quantized versions (8-bit, 4-bit).

---

## Configuring Claude Code Router for Ollama

### Configuration 1: All Local (Development)

**Best for**: Development, testing, offline work

```json
{
  "PORT": 3456,
  "Providers": [
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": [
        "llama3.3:70b",
        "qwen2.5:72b",
        "llama3.3:8b"
      ]
    }
  ],
  "Router": {
    "default": "ollama,llama3.3:70b",
    "background": "ollama,llama3.3:8b",
    "think": "ollama,qwen2.5:72b",
    "longContext": "ollama,llama3.3:70b"
  }
}
```

**Setup**:
```bash
# 1. Copy config
cp /home/user/betty/config/router-examples/local-dev.json \
   ~/.claude-code-router/config.json

# 2. Edit for all-local
nano ~/.claude-code-router/config.json

# 3. Start Ollama
ollama serve &

# 4. Start router
ccr start

# 5. Use Betty
ccr code
/api-design user-service
```

### Configuration 2: Hybrid Local + Cloud (Recommended)

**Best for**: Development with cloud fallback

```json
{
  "PORT": 3456,
  "Providers": [
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": [
        "llama3.3:70b",
        "llama3.3:8b"
      ]
    },
    {
      "name": "anthropic",
      "api_base_url": "https://api.anthropic.com/v1/messages",
      "api_key": "${ANTHROPIC_API_KEY}",
      "models": [
        "claude-3-5-sonnet-20241022",
        "claude-opus-4-20250514"
      ]
    }
  ],
  "Router": {
    "default": "ollama,llama3.3:70b",
    "background": "ollama,llama3.3:8b",
    "think": "anthropic,claude-opus-4-20250514",
    "longContext": "anthropic,claude-3-5-sonnet-20241022"
  }
}
```

**Strategy**: Use local for most work, cloud for complex reasoning and large context.

### Configuration 3: Production with Local Development

**Best for**: Cost optimization with cloud backup

```json
{
  "PORT": 3456,
  "Providers": [
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": ["llama3.3:70b"]
    },
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "${DEEPSEEK_API_KEY}",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    }
  ],
  "Router": {
    "default": "ollama,llama3.3:70b",
    "background": "ollama,llama3.3:70b",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "deepseek,deepseek-chat"
  }
}
```

**Cost Profile**: 95%+ savings (only DeepSeek for complex reasoning)

---

## Testing Ollama with Betty

### Step 1: Verify Ollama is Running

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Should return list of available models
```

### Step 2: Test Model Directly

```bash
# Test Llama 3.3 directly
ollama run llama3.3:70b "Write a simple REST API design for a user service"

# Test code generation
ollama run qwen2.5:72b "Generate TypeScript interfaces for a user API"
```

### Step 3: Test with Router

```bash
# Start router
ccr start

# Launch Claude Code through router
ccr code

# Test Betty agent
/api-design test-service

# Check which model was used
ccr model
```

### Step 4: Verify Model Routing

```bash
# In Claude Code session, check current model
/model

# Should show: ollama | llama3.3:70b

# Switch to background model
/model ollama llama3.3:8b

# Run simple task
/api-validate test-spec.yaml
```

---

## Betty Agent Recommendations with Ollama

### Agent-to-Model Mapping

| Betty Agent | Best Ollama Model | Context | Why |
|-------------|------------------|---------|-----|
| `api.designer` | qwen2.5:72b | think | Best code generation |
| `api.validate` | llama3.3:8b | background | Fast, simple validation |
| `api.compatibility` | llama3.3:70b | think | Good analysis |
| `api.generate-models` | qwen2.5:72b | default | Excellent code gen |
| Large portfolios | llama3.3:70b | longContext | Good context handling |

### Workflow Examples

#### Development Workflow (All Local)

```bash
# Design API (Qwen 2.5 72B)
/model ollama qwen2.5:72b
/api-design user-service

# Validate (Llama 3.3 8B - fast)
/model ollama llama3.3:8b
/api-validate user-service-spec.yaml

# Generate models (Qwen 2.5 72B)
/model ollama qwen2.5:72b
/api-generate-models user-service-spec.yaml
```

#### Production Workflow (Hybrid)

```bash
# Quick validation (local)
/model ollama llama3.3:8b
/api-validate spec.yaml

# Complex design (cloud)
/model anthropic claude-opus-4-20250514
/api-design complex-payment-service

# Large analysis (cloud long context)
/model anthropic claude-3-5-sonnet-20241022
/api-compatibility old-spec.yaml new-spec.yaml
```

---

## Performance Optimization

### Ollama Configuration

Edit `~/.ollama/config.json`:

```json
{
  "num_parallel": 4,
  "num_gpu": 1,
  "num_thread": 16,
  "num_ctx": 8192,
  "keep_alive": "5m"
}
```

**Parameters**:
- `num_parallel`: Concurrent requests (4-8)
- `num_gpu`: GPUs to use (1 for single GPU)
- `num_thread`: CPU threads (match your cores)
- `num_ctx`: Context window (2048-32768)
- `keep_alive`: Model cache time

### Model Loading

```bash
# Pre-load models (faster first request)
ollama run llama3.3:70b ""
ollama run qwen2.5:72b ""
ollama run llama3.3:8b ""

# Now they're cached in memory
```

### GPU Acceleration

Ollama automatically uses GPU if available:

```bash
# Check GPU usage
nvidia-smi

# Or for Apple Silicon
system_profiler SPDisplaysDataType | grep Metal

# Ollama will show GPU usage when running
ollama run llama3.3:70b --verbose
```

---

## Troubleshooting

### Ollama won't start

```bash
# Check if already running
ps aux | grep ollama

# Kill existing process
killall ollama

# Start fresh
ollama serve
```

### Model not found

```bash
# List available models
ollama list

# Pull missing model
ollama pull llama3.3:70b

# Verify
ollama list
```

### Out of memory

```bash
# Use smaller model
ollama pull llama3.3:8b

# Or use quantized version
ollama pull llama3.3:70b-q4

# Update router config to use smaller model
```

### Slow performance

```bash
# Check if using GPU
nvidia-smi  # Should show ollama process

# If not using GPU, check drivers
ollama --version

# Increase threads
export OLLAMA_NUM_THREADS=16
ollama serve
```

### Router can't connect

```bash
# Verify Ollama is running
curl http://localhost:11434/api/tags

# Check router config has correct URL
cat ~/.claude-code-router/config.json | grep api_base_url

# Should be: http://localhost:11434/api/chat
```

---

## Cost Comparison

### Monthly Cost Estimate (100M tokens)

| Configuration | Hardware | API Costs | Total | Savings |
|---------------|----------|-----------|-------|---------|
| All Claude | - | $1,800 | $1,800 | 0% |
| Hybrid (Ollama + Claude) | $20 | $180 | $200 | 89% |
| Hybrid (Ollama + DeepSeek) | $20 | $14 | $34 | 98% |
| All Ollama | $20 | $0 | $20 | 99% |

**Hardware costs**: Electricity (~$20/month for 24/7 operation)

### Per-Request Comparison

| Task | Model | Time | Cost |
|------|-------|------|------|
| API Design | Claude Opus | 3s | $0.15 |
| API Design | Qwen 2.5 72B | 2s | $0.00 |
| Validation | Claude Haiku | 1s | $0.02 |
| Validation | Llama 3.3 8B | 0.5s | $0.00 |

---

## Advanced: Multiple Ollama Instances

### Run Multiple Models Simultaneously

```bash
# Terminal 1: Start Ollama on default port
ollama serve

# Terminal 2: Start second instance on different port
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

**Router config**:
```json
{
  "Providers": [
    {
      "name": "ollama-default",
      "api_base_url": "http://localhost:11434/api/chat",
      "models": ["llama3.3:70b"]
    },
    {
      "name": "ollama-fast",
      "api_base_url": "http://localhost:11435/api/chat",
      "models": ["llama3.3:8b"]
    }
  ],
  "Router": {
    "default": "ollama-default,llama3.3:70b",
    "background": "ollama-fast,llama3.3:8b"
  }
}
```

---

## Production Deployment

### Docker Compose Setup

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  claude-code-router:
    image: musistudio/claude-code-router:latest
    ports:
      - "3456:3456"
    volumes:
      - ./config.json:/root/.claude-code-router/config.json
    depends_on:
      - ollama

volumes:
  ollama-data:
```

**Usage**:
```bash
docker-compose up -d
docker exec -it ollama ollama pull llama3.3:70b
ccr code
```

---

## Next Steps

1. **Install Ollama** on your local machine
2. **Pull recommended models** (llama3.3:70b, qwen2.5:72b)
3. **Copy local-dev.json** to router config
4. **Test with Betty** agents
5. **Monitor performance** and tune

---

## Resources

- **Ollama**: https://ollama.ai/
- **Ollama Models**: https://ollama.ai/library
- **Claude Code Router**: https://github.com/musistudio/claude-code-router
- **Betty Docs**: `/docs/betty-architecture.md`
- **Router Integration**: `/docs/claude-code-router-integration.md`

---

## Summary

✅ **Ollama enables 95%+ cost savings** for Betty development
✅ **Complete privacy** - data never leaves your machine
✅ **Works offline** - no internet required
✅ **Fast** - no network latency
✅ **Easy setup** - download, pull models, configure router
✅ **Hybrid approach** - use cloud for complex tasks only

**Recommended**: Start with hybrid (Ollama + DeepSeek) for best balance of cost/quality.
