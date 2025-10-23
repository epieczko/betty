# Betty Framework - Claude Code Plugin

## Overview

Betty Framework is now packaged as a native Claude Code plugin, exposing all core skills and API workflows as easy-to-use slash commands.

> **Claude Code thinks. Betty builds.**

This plugin provides structured, auditable AI-assisted engineering with enterprise-grade governance, transforming Claude Code into a complete development methodology.

---

## Installation

### Prerequisites

Before installing the Betty plugin, ensure you have:

1. **Python 3.11 or newer**
   ```bash
   python --version  # Should show Python 3.11+
   ```

2. **Required Python packages**
   ```bash
   pip install pyyaml
   ```

3. **Optional dependencies** (for full functionality)
   ```bash
   # For advanced API model generation
   pip install datamodel-code-generator
   ```

### Install the Plugin

#### Method 1: Install from Repository Root

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/epieczko/betty.git
cd betty

# Install the plugin
claude plugin add ./plugin.yaml
```

#### Method 2: Install from GitHub URL

```bash
claude plugin add https://raw.githubusercontent.com/epieczko/betty/main/plugin.yaml
```

#### Method 3: Install from Local Path

```bash
# If you already have the repository locally
claude plugin add /path/to/betty/plugin.yaml
```

### Verify Installation

Check that the plugin is installed and all commands are available:

```bash
# List installed plugins
claude plugin list

# Check Betty commands
claude help betty
```

---

## Available Commands

### Foundation Skills

#### `/skill/create` - Create New Skills

Scaffold a new Betty Framework skill with complete directory structure.

**Usage:**
```bash
/skill/create <skill_name> "<description>" [--inputs=...] [--outputs=...]
```

**Examples:**
```bash
# Basic skill creation
/skill/create data.transform "Transform data between formats"

# With inputs and outputs
/skill/create api.monitor "Monitor API health" --inputs=endpoint,interval --outputs=status,metrics

# Complex workflow skill
/skill/create deployment.orchestrate "Orchestrate multi-stage deployments" --inputs=environment,version --outputs=deployment_id,status
```

**What it creates:**
- `skills/<skill_name>/` directory
- `skill.yaml` manifest
- `SKILL.md` documentation
- `<skill_name>.py` handler script
- Registry entry (if validation passes)

---

#### `/skill/define` - Validate Skill Manifests

Validate skill manifests for correctness and completeness.

**Usage:**
```bash
/skill/define <manifest_path>
```

**Examples:**
```bash
/skill/define skills/data.transform/skill.yaml
/skill/define skills/api.monitor/skill.yaml
```

**Validates:**
- Required fields presence
- Field types and formats
- Status values
- Dependencies resolution

---

#### `/agent/define` - Validate Agent Manifests

Validate and register agent manifests in the Agent Registry.

**Usage:**
```bash
/agent/define <manifest_path>
```

**Examples:**
```bash
/agent/define agents/api.designer/agent.yaml
/agent/define agents/deployment.orchestrator/agent.yaml
```

**Validates:**
- Agent metadata completeness
- Reasoning mode validity
- Skills availability
- Capability definitions

---

#### `/registry/update` - Update Skill Registry

Add or update skill entries in the central registry.

**Usage:**
```bash
/registry/update <manifest_path>
```

**Examples:**
```bash
/registry/update skills/data.transform/skill.yaml
/registry/update skills/api.monitor/skill.yaml
```

**Features:**
- Atomic registry updates
- Policy enforcement
- Audit logging
- Version tracking

---

#### `/workflow/compose` - Execute Workflows

Execute multi-step workflows by chaining skills together.

**Usage:**
```bash
/workflow/compose <workflow_file>
```

**Examples:**
```bash
# API-first development workflow
/workflow/compose workflows/api_first_development.yaml

# Create and register skill workflow
/workflow/compose workflows/example_create_and_register.yaml

# Custom deployment workflow
/workflow/compose workflows/production_deployment.yaml
```

**Features:**
- Step-by-step execution
- Error handling and rollback
- Progress tracking
- Audit trail generation

---

### API Development Skills

#### `/api-define` - Create API Specifications

Generate OpenAPI or AsyncAPI specifications from enterprise templates.

**Usage:**
```bash
/api-define <service_name> [spec_type] [--template=...] [--version=...] [--output-dir=...]
```

**Examples:**
```bash
# Create OpenAPI spec with Zalando template (default)
/api-define user-service

# Create OpenAPI with specific version
/api-define order-service openapi --template=zalando --version=2.0.0

# Create AsyncAPI for event-driven service
/api-define notification-service asyncapi

# Custom output directory
/api-define payment-gateway openapi --output-dir=api-specs --template=zalando
```

**Supported Templates:**
- **OpenAPI**: `zalando`, `basic`, `minimal`
- **AsyncAPI**: `basic`, `kafka`, `rabbitmq`

**What it creates:**
- Fully-structured API specification
- Enterprise-compliant metadata
- Sample endpoints and schemas
- Documentation structure

---

#### `/api-validate` - Validate API Specifications

Validate API specs against enterprise guidelines.

**Usage:**
```bash
/api-validate <spec_path> [guideline_set] [--strict] [--format=...]
```

**Examples:**
```bash
# Validate against Zalando guidelines (default)
/api-validate specs/user-service.openapi.yaml

# Strict mode with human-readable output
/api-validate specs/order-api.yaml zalando --strict --format=human

# Validate against Google guidelines
/api-validate specs/payment-api.yaml google

# Validate AsyncAPI spec
/api-validate specs/events.asyncapi.yaml
```

**Supported Guidelines:**
- `zalando` - Zalando RESTful API Guidelines
- `google` - Google API Design Guide
- `microsoft` - Microsoft REST API Guidelines

**Validation Coverage:**
- Schema correctness
- Naming conventions
- Security definitions
- Documentation completeness
- Best practices compliance

---

#### `/api-generate` - Generate Type-Safe Models

Generate models in multiple languages from API specifications.

**Usage:**
```bash
/api-generate <spec_path> <language> [--output-dir=...] [--package-name=...]
```

**Examples:**
```bash
# Generate TypeScript interfaces
/api-generate specs/user-service.openapi.yaml typescript

# Generate Python dataclasses
/api-generate specs/order-api.yaml python --output-dir=backend/models

# Generate Java classes with package
/api-generate specs/payment-api.yaml java --package-name=com.company.payment

# Generate Go structs
/api-generate specs/product-api.yaml go --output-dir=internal/models

# Generate C# classes
/api-generate specs/inventory-api.yaml csharp --output-dir=Models
```

**Supported Languages:**
- `typescript` - TypeScript interfaces
- `python` - Python dataclasses/Pydantic models
- `java` - Java classes
- `go` - Go structs
- `csharp` - C# classes
- `rust` - Rust structs
- `kotlin` - Kotlin data classes
- `dart` - Dart classes

**Generation Features:**
- Type-safe models
- Validation attributes
- Documentation comments
- Proper imports/dependencies

---

#### `/api-compatibility` - Check API Compatibility

Detect breaking changes between API specification versions.

**Usage:**
```bash
/api-compatibility <old_spec_path> <new_spec_path> [--fail-on-breaking] [--format=...]
```

**Examples:**
```bash
# Check compatibility between versions
/api-compatibility specs/user-service.v1.yaml specs/user-service.v2.yaml

# Human-readable report
/api-compatibility specs/api-old.yaml specs/api-new.yaml --format=human

# Don't fail on breaking changes (report only)
/api-compatibility specs/v1.yaml specs/v2.yaml --fail-on-breaking=false
```

**Detects:**
- **Breaking Changes**:
  - Removed endpoints
  - Removed operation methods
  - Removed required fields
  - Type changes
  - Required field additions

- **Non-Breaking Changes**:
  - Added endpoints
  - Added operations
  - Added optional fields
  - Documentation updates

---

## Complete Workflows

### API-First Development Workflow

Create a complete API with validation, models, and compatibility checks:

```bash
# 1. Define the API specification
/api-define user-service openapi --template=zalando

# 2. Validate against guidelines
/api-validate specs/user-service.openapi.yaml zalando --format=human

# 3. Generate TypeScript models
/api-generate specs/user-service.openapi.yaml typescript --output-dir=frontend/models

# 4. Generate Python models
/api-generate specs/user-service.openapi.yaml python --output-dir=backend/models

# 5. Make changes to spec (if needed)
# ... edit specs/user-service.openapi.yaml ...

# 6. Check compatibility
/api-compatibility specs/user-service.openapi.yaml specs/user-service.v2.openapi.yaml
```

### Create and Register Custom Skill

```bash
# 1. Create the skill
/skill/create custom.processor "Process custom data format" --inputs=data,format --outputs=processed_data

# 2. Implement the skill logic
# ... edit skills/custom.processor/custom_processor.py ...

# 3. Validate the manifest
/skill/define skills/custom.processor/skill.yaml

# 4. Register in the skill registry
/registry/update skills/custom.processor/skill.yaml
```

### Execute Orchestrated Workflow

```bash
# Create a workflow definition (YAML)
cat > workflows/my_workflow.yaml << 'EOF'
name: my-workflow
version: 1.0.0
description: Custom orchestrated workflow

steps:
  - name: create_api
    skill: api.define
    inputs:
      service_name: my-service
      spec_type: openapi

  - name: validate_api
    skill: api.validate
    inputs:
      spec_path: specs/my-service.openapi.yaml
      guideline_set: zalando

  - name: generate_models
    skill: api.generate-models
    inputs:
      spec_path: specs/my-service.openapi.yaml
      language: typescript
EOF

# Execute the workflow
/workflow/compose workflows/my_workflow.yaml
```

---

## Configuration

### Environment Variables

```bash
# Set custom Betty home directory
export BETTY_HOME=/path/to/betty

# Python version requirement
export PYTHON_VERSION=3.11
```

### Plugin Configuration

The plugin respects Betty's configuration in `betty/config.py`:

- **Paths**: Skills, agents, registry locations
- **API Defaults**: Templates, guidelines, versions
- **Governance**: Policy enforcement, audit logging

### Registry Management

All skills and agents are tracked in:
- `registry/skills.json` - Skill registry
- `registry/agents.json` - Agent registry
- `registry/commands.json` - Command registry
- `registry/hooks.json` - Hook registry
- `registry/workflow_history.json` - Workflow execution history

---

## Troubleshooting

### Plugin Installation Issues

**Problem**: Plugin not found
```bash
# Solution: Verify path
ls -la plugin.yaml
claude plugin add $(pwd)/plugin.yaml
```

**Problem**: Python version error
```bash
# Solution: Check Python version
python --version  # Must be 3.11+
```

### Skill Execution Issues

**Problem**: Skill handler not found
```bash
# Solution: Verify handler exists
ls -la skills/<skill-name>/<skill-name>.py
```

**Problem**: Import errors
```bash
# Solution: Install dependencies
pip install -r requirements.txt
pip install pyyaml datamodel-code-generator
```

### API Generation Issues

**Problem**: No models generated
```bash
# Solution: Check spec file exists and is valid
cat specs/<service-name>.openapi.yaml
/api-validate specs/<service-name>.openapi.yaml
```

---

## Uninstalling

To remove the Betty Framework plugin:

```bash
# Remove the plugin
claude plugin remove betty-framework

# Verify removal
claude plugin list
```

**Note**: This does not delete the repository or any created skills/workflows.

---

## Support

For issues, questions, or contributions:

- **GitHub Issues**: https://github.com/epieczko/betty/issues
- **Documentation**: https://github.com/epieczko/betty/tree/main/docs
- **Contributing**: See [CONTRIBUTING.md](docs/contributing.md)

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## What's Next?

Explore the full Betty Framework documentation:

- [Betty Architecture](docs/betty-architecture.md) - Five-layer model
- [Skills Framework](docs/skills-framework.md) - Skill taxonomy
- [API-Driven Development](docs/api-driven-development.md) - Complete workflow guide
- [Command & Hook Infrastructure](docs/COMMAND_HOOK_INFRASTRUCTURE.md) - Layer 1 and 5

**Claude Code thinks. Betty builds.**
