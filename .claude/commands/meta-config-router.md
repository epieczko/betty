# /meta-config-router

Configure Claude Code Router for multi-model LLM support across OpenRouter, Ollama, Claude, and other providers.

## Description

The `/meta-config-router` command creates or previews a router configuration file that enables Betty to route LLM requests across multiple model providers based on context (default, think, background, longContext).

This command:
- Validates router configuration inputs for correctness
- Generates a complete `config.json` file with backends and routing rules
- Supports preview mode (no file write) or direct application to `~/.claude-code-router/config.json`
- Logs all configuration changes with audit trails
- Works across local, cloud, and CI environments

## Usage

```bash
/meta-config-router --routing_config_path=<path> [--apply_config] [--output_mode=<mode>]
```

## Parameters

### Required

- `--routing_config_path=<path>` - Path to router configuration input file (YAML or JSON)

### Optional

- `--apply_config` - Write configuration to `~/.claude-code-router/config.json` (default: false)
- `--output_mode=<mode>` - Output mode: `preview`, `file`, or `both` (default: `preview`)

## Examples

### Preview Configuration (No File Write)

```bash
/meta-config-router --routing_config_path=examples/router-config.yaml
```

### Apply Configuration to Disk

```bash
/meta-config-router --routing_config_path=examples/router-config.yaml --apply_config
```

### Both Preview and Write

```bash
/meta-config-router --routing_config_path=examples/router-config.yaml --apply_config --output_mode=both
```

## Input File Format (YAML)

```yaml
llm_backends:
  - name: openrouter
    api_base_url: https://openrouter.ai/api/v1
    api_key: ${OPENROUTER_API_KEY}
    models:
      - anthropic/claude-3.5-sonnet
      - openai/gpt-4

  - name: ollama
    api_base_url: http://localhost:11434/v1
    models:
      - llama3.1:70b
      - codellama:34b

routing_rules:
  default:
    provider: openrouter
    model: anthropic/claude-3.5-sonnet

  think:
    provider: openrouter
    model: anthropic/claude-3.5-sonnet

  background:
    provider: ollama
    model: llama3.1:70b

  longContext:
    provider: openrouter
    model: anthropic/claude-3.5-sonnet

metadata:
  initiator: user@example.com
  environment: production
  purpose: Multi-model routing for development
```

## Output

The command generates a complete router configuration JSON file with:

- Version and generation timestamp
- Backend provider configurations
- Routing context mappings
- Audit metadata

Example output:

```json
{
  "version": "1.0.0",
  "generated_at": "2025-11-01T12:34:56Z",
  "backends": [...],
  "routing": {
    "default": { "provider": "openrouter", "model": "anthropic/claude-3.5-sonnet" },
    "think": { "provider": "openrouter", "model": "anthropic/claude-3.5-sonnet" },
    "background": { "provider": "ollama", "model": "llama3.1:70b" },
    "longContext": { "provider": "openrouter", "model": "anthropic/claude-3.5-sonnet" }
  },
  "metadata": {
    "generated_by": "meta.config.router",
    "schema_version": "1.0.0",
    ...
  }
}
```

## Validation

The command validates:

- Required fields in backend configurations (name, api_base_url, models)
- Unique backend names
- Non-empty models lists
- Valid routing contexts (default, think, background, longContext)
- Provider and model references exist
- Essential routing contexts are defined (default required)

## Audit Trail

All configuration changes are logged to `registry/audit_log.json` with:

- Unique audit ID
- Timestamp
- Input hash
- Environment fingerprint
- Write status
- Initiator metadata

## Permissions

- `filesystem:read` - Read router config input files
- `filesystem:write` - Write config to `~/.claude-code-router/config.json`

## Related Commands

- `/agent/run` - Run agents with custom configurations

## Tags

llm, router, configuration, multi-model, openrouter, claude, ollama
