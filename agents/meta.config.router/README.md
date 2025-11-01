# Agent: meta.config.router

## Purpose

Configure Claude Code Router for Betty to support multi-model LLM routing across environments. This agent creates or previews a `config.json` file at `~/.claude-code-router/config.json` with model providers, routing profiles, and audit metadata.

## Version

0.1.0

## Status

active

## Reasoning Mode

oneshot

## Capabilities

- Generate multi-model LLM router configurations
- Validate router configuration inputs for correctness
- Apply configurations to filesystem with audit trails
- Support multiple output modes (preview, file, both)
- Work across local, cloud, and CI environments
- Ensure deterministic and portable configurations

## Skills Available

- `config.validate.router` - Validates router configuration inputs
- `config.generate.router` - Generates router configuration JSON
- `audit.log` - Records audit events for configuration changes

## Inputs

### llm_backends (required)
- **Type**: List of objects
- **Description**: Backend provider configurations
- **Schema**:
  ```json
  [
    {
      "name": "string (e.g., openrouter, ollama, claude)",
      "api_base_url": "string (API endpoint URL)",
      "api_key": "string (optional for local providers)",
      "models": ["string (model identifiers)"]
    }
  ]
  ```

### routing_rules (required)
- **Type**: Dictionary
- **Description**: Mapping of Claude routing contexts to provider/model pairs
- **Contexts**: default, think, background, longContext
- **Schema**:
  ```json
  {
    "default": { "provider": "string", "model": "string" },
    "think": { "provider": "string", "model": "string" },
    "background": { "provider": "string", "model": "string" },
    "longContext": { "provider": "string", "model": "string" }
  }
  ```

### output_mode (optional)
- **Type**: enum
- **Values**: "preview" | "file" | "both"
- **Default**: "preview"
- **Description**: Output mode for configuration

### apply_config (optional)
- **Type**: boolean
- **Default**: false
- **Description**: Write config to disk if true

### metadata (optional)
- **Type**: object
- **Description**: Optional audit metadata (initiator, environment, etc.)

## Outputs

### routing_config
- **Type**: object
- **Description**: Rendered router config as JSON

### write_status
- **Type**: string
- **Values**: "success" | "skipped" | "error"
- **Description**: Status of file write operation

### audit_id
- **Type**: string
- **Description**: Unique trace ID for configuration event

## Behavior

1. Validates inputs via `config.validate.router`
2. Constructs valid router config using `config.generate.router`
3. If `apply_config=true` and `output_mode≠preview`, writes config to: `~/.claude-code-router/config.json`
4. Outputs JSON config regardless of write action
5. Logs audit record via `audit.log` with:
   - timestamp
   - initiator
   - hash of input
   - environment fingerprint

## Usage Example

```bash
# Preview configuration (no file write)
/meta/config.router --routing_config_path=router-config.yaml

# Apply configuration to disk
/meta/config.router --routing_config_path=router-config.yaml --apply_config=true

# Both preview and write
/meta/config.router --routing_config_path=router-config.yaml --apply_config=true --output_mode=both
```

## Example Input (YAML)

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

## Example Output

```json
{
  "version": "1.0.0",
  "generated_at": "2025-11-01T12:34:56Z",
  "backends": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1",
      "api_key": "${OPENROUTER_API_KEY}",
      "models": [
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4"
      ]
    },
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/v1",
      "models": [
        "llama3.1:70b",
        "codellama:34b"
      ]
    }
  ],
  "routing": {
    "default": {
      "provider": "openrouter",
      "model": "anthropic/claude-3.5-sonnet"
    },
    "think": {
      "provider": "openrouter",
      "model": "anthropic/claude-3.5-sonnet"
    },
    "background": {
      "provider": "ollama",
      "model": "llama3.1:70b"
    },
    "longContext": {
      "provider": "openrouter",
      "model": "anthropic/claude-3.5-sonnet"
    }
  },
  "metadata": {
    "generated_by": "meta.config.router",
    "schema_version": "1.0.0",
    "initiator": "user@example.com",
    "environment": "production",
    "purpose": "Multi-model routing for development"
  }
}
```

## Permissions

- `filesystem:read` - Read router config input files
- `filesystem:write` - Write config to ~/.claude-code-router/config.json

## Artifacts

### Consumes
- `router-config-input` - User-provided router configuration inputs

### Produces
- `llm-router-config` - Complete Claude Code Router configuration file
- `audit-log-entry` - Audit trail entry for configuration events

## Tags

llm, router, configuration, meta, infra, openrouter, claude, ollama, multi-model

## Environments

- local
- cloud
- ci

## Requires Human Approval

false

## Notes

- The config is deterministic and portable across environments
- API keys can use environment variable substitution (e.g., ${OPENROUTER_API_KEY})
- Local providers (localhost/127.0.0.1) don't require API keys
- All configuration changes are audited for traceability
- The agent supports preview mode to verify configuration before applying
