# Claude Code Router Configuration Examples

This directory contains example router configurations for different use cases and environments.

## Available Examples

### 1. `local-dev-openrouter-ollama.yaml`
**Use Case**: Local development with cost-effective routing

**Features**:
- OpenRouter for premium models (Claude, Gemini, GPT-4)
- Ollama for free local models (background tasks)
- Optimized for development workflow

**Best For**: Developers working locally who want to minimize costs while maintaining access to premium models when needed.

### 2. `production-multi-cloud.yaml`
**Use Case**: Production deployment with redundancy

**Features**:
- Multiple providers (Anthropic, OpenAI, Google)
- No single point of failure
- Load balancing across providers

**Best For**: Production environments requiring high availability and reliability.

### 3. `cost-optimized.yaml`
**Use Case**: Minimize API costs

**Features**:
- Cheaper models for default tasks (Claude Haiku, Gemini Flash)
- Premium models only for critical tasks (think mode)
- Local models for background work

**Best For**: Budget-conscious deployments or high-volume usage scenarios.

### 4. `air-gapped-offline.yaml`
**Use Case**: Fully offline operation

**Features**:
- All models run locally via Ollama
- No external API calls
- Complete data privacy

**Best For**: Secure environments, air-gapped networks, or offline development.

### 5. `ci-cd-automated.yaml`
**Use Case**: CI/CD pipelines

**Features**:
- Fast models for quick feedback
- Non-interactive mode enabled
- Shorter timeouts for CI speed

**Best For**: Automated testing, code review, and deployment pipelines.

## Usage

### Preview Configuration
```bash
/meta-config-router --routing_config_path=examples/router-configs/local-dev-openrouter-ollama.yaml
```

### Apply Configuration
```bash
/meta-config-router \
  --routing_config_path=examples/router-configs/local-dev-openrouter-ollama.yaml \
  --apply_config
```

### Verify Configuration
```bash
cat ~/.claude-code-router/config.json
```

## Environment Variables

Most examples use environment variables for API keys:

- `$OPENROUTER_API_KEY` - OpenRouter API key
- `$ANTHROPIC_API_KEY` - Anthropic API key
- `$OPENAI_API_KEY` - OpenAI API key
- `$GOOGLE_API_KEY` - Google AI API key

Set these in your shell:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Customization

Feel free to customize these examples for your specific needs:

1. **Add/Remove Providers**: Modify the `llm_backends` section
2. **Change Routing**: Update the `routing_rules` section
3. **Adjust Settings**: Modify `config_options` (LOG, API_TIMEOUT_MS, etc.)
4. **Add Metadata**: Include custom metadata for tracking/auditing

## Routing Contexts

| Context | Purpose | Example Use |
|---------|---------|-------------|
| `default` | General-purpose tasks | Regular coding, documentation |
| `background` | Non-interactive background work | File processing, batch operations |
| `think` | Complex reasoning tasks | Architecture design, debugging |
| `longContext` | Large document handling | Analyzing large codebases |
| `webSearch` | Web-aware responses | Research, documentation lookup |
| `image` (beta) | Image processing | Screenshot analysis, diagrams |

## Validation

All example configs are validated before use. The validator checks:

- Required fields present (name, api_base_url, models)
- Unique provider names
- Non-empty models lists
- Valid API URLs
- Provider/model references in routing rules
- Essential routing contexts defined (default required)

## Support

For issues or questions:
- Check the Claude Code Router docs: https://github.com/musistudio/claude-code-router
- Review the meta.config.router agent: `agents/meta.config.router/README.md`
