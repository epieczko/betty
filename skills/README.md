# Betty Framework Skills

## ⚙️ **Integration Note: Claude Code Plugin System**

**Betty skills are Claude Code plugins.** You do not invoke skills via standalone CLI commands (`betty` or direct Python scripts). Instead:

- **Claude Code serves as the execution environment** for all skill execution
- Each skill is registered through its `skill.yaml` manifest
- Skills become automatically discoverable and executable through Claude Code's natural language interface
- All routing, validation, and execution is handled by Claude Code via MCP (Model Context Protocol)

**No separate installation step is needed** beyond plugin registration in your Claude Code environment.

---

This directory contains skill manifests and implementations for the Betty Framework.

## What are Skills?

Skills are **atomic, composable building blocks** that execute specific operations. Unlike agents (which orchestrate multiple skills with reasoning) or workflows (which follow fixed sequential steps), skills are:

- **Atomic** — Each skill does one thing well
- **Composable** — Skills can be combined into complex workflows
- **Auditable** — Every execution is logged with inputs, outputs, and provenance
- **Type-safe** — Inputs and outputs are validated against schemas

## Directory Structure

Each skill has its own directory containing:
```
skills/
├── <skill-name>/
│   ├── skill.yaml              # Skill manifest (required)
│   ├── SKILL.md                # Documentation (auto-generated)
│   ├── <skill_name>.py         # Implementation handler (required)
│   ├── requirements.txt        # Python dependencies (optional)
│   └── tests/                  # Skill tests (optional)
│       └── test_skill.py
```

## Creating a Skill

### Using meta.skill (Recommended)

**Via Claude Code:**
```
"Use meta.skill to create a custom.processor skill that processes custom data formats,
accepts raw-data and config as inputs, and outputs processed-data"
```

**Direct execution (development/testing):**
```bash
cat > /tmp/my_skill.md <<'EOF'
# Name: custom.processor
# Purpose: Process custom data formats
# Inputs: raw-data, config
# Outputs: processed-data
# Dependencies: python-processing-tools
EOF
python agents/meta.skill/meta_skill.py /tmp/my_skill.md
```

### Manual Creation

1. Create skill directory:
   ```bash
   mkdir -p skills/custom.processor
   ```

2. Create skill manifest (`skills/custom.processor/skill.yaml`):
   ```yaml
   name: custom.processor
   version: 0.1.0
   description: "Process custom data formats"

   inputs:
     - name: raw-data
       type: file
       description: "Input data file"
       required: true
     - name: config
       type: object
       description: "Processing configuration"
       required: false

   outputs:
     - name: processed-data
       type: file
       description: "Processed output file"

   dependencies:
     - python-processing-tools

   status: draft
   ```

3. Implement the handler (`skills/custom.processor/custom_processor.py`):
   ```python
   #!/usr/bin/env python3
   """Custom data processor skill implementation."""

   import sys
   from pathlib import Path

   def main():
       if len(sys.argv) < 2:
           print("Usage: custom_processor.py <raw-data> [config]")
           sys.exit(1)

       raw_data = Path(sys.argv[1])
       config = sys.argv[2] if len(sys.argv) > 2 else None

       # Your processing logic here
       print(f"Processing {raw_data} with config {config}")

   if __name__ == "__main__":
       main()
   ```

4. Validate and register:

   **Via Claude Code:**
   ```
   "Use skill.define to validate skills/custom.processor/skill.yaml,
   then use registry.update to register it"
   ```

   **Direct execution (development/testing):**
   ```bash
   python skills/skill.define/skill_define.py skills/custom.processor/skill.yaml
   python skills/registry.update/registry_update.py skills/custom.processor/skill.yaml
   ```

## Skill Manifest Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique identifier (e.g., `api.validate`) |
| `version` | string | Semantic version (e.g., `0.1.0`) |
| `description` | string | Human-readable purpose statement |
| `inputs` | array[object] | Input parameters and their types |
| `outputs` | array[object] | Output artifacts and their types |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | enum | `draft`, `active`, `deprecated`, `archived` |
| `dependencies` | array[string] | External tools or libraries required |
| `tags` | array[string] | Categorization tags |
| `examples` | array[object] | Usage examples |
| `error_handling` | object | Error handling strategies |

## Skill Categories

### Foundation Skills
- **skill.create** — Generate new skill scaffolding
- **skill.define** — Validate skill manifests
- **registry.update** — Update component registries
- **workflow.compose** — Chain skills into workflows

### API Development Skills
- **api.define** — Create API specifications
- **api.validate** — Validate specs against guidelines
- **api.generate-models** — Generate type-safe models
- **api.compatibility** — Detect breaking changes

### Governance Skills
- **audit.log** — Record audit events
- **policy.enforce** — Validate against policies
- **telemetry.capture** — Capture usage metrics
- **registry.query** — Query component registry

### Infrastructure Skills
- **agent.define** — Validate agent manifests
- **agent.run** — Execute agents
- **plugin.build** — Bundle plugins
- **plugin.sync** — Sync plugin manifests

### Documentation Skills
- **docs.sync.readme** — Regenerate README files
- **generate.docs** — Auto-generate documentation
- **docs.validate.skill_docs** — Validate documentation completeness

## Using Skills

### Via Claude Code (Recommended)

Simply ask Claude to execute the skill by name:

```
"Use api.validate to check specs/user-service.openapi.yaml against Zalando guidelines"

"Use artifact.create to create a threat-model artifact named payment-system-threats"

"Use registry.query to find all skills in the api category"
```

### Direct Execution (Development/Testing)

For development and testing, you can invoke skill handlers directly:

```bash
python skills/api.validate/api_validate.py specs/user-service.openapi.yaml

python skills/artifact.create/artifact_create.py \
  threat-model \
  "Payment processing system" \
  ./artifacts/threat-model.yaml

python skills/registry.query/registry_query.py --category api
```

## Validation

All skill manifests are automatically validated for:
- Required fields presence
- Name format (`^[a-z][a-z0-9._-]*$`)
- Version format (semantic versioning)
- Input/output schema correctness
- Dependency declarations

## Registry

Validated skills are registered in `/registry/skills.json`:
```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-26T00:00:00Z",
  "skills": [
    {
      "name": "api.validate",
      "version": "0.1.0",
      "description": "Validate API specs against guidelines",
      "inputs": [...],
      "outputs": [...],
      "status": "active"
    }
  ]
}
```

## Composing Skills into Workflows

Skills can be chained together using the `workflow.compose` skill:

**Via Claude Code:**
```
"Use workflow.compose to create a workflow that:
1. Uses api.define to create a spec
2. Uses api.validate to check it
3. Uses api.generate-models to create TypeScript models"
```

**Workflow YAML definition:**
```yaml
name: api-development-workflow
version: 0.1.0

steps:
  - skill: api.define
    inputs:
      service_name: "user-service"
    outputs:
      spec_path: "${OUTPUT_DIR}/user-service.openapi.yaml"

  - skill: api.validate
    inputs:
      spec_path: "${steps[0].outputs.spec_path}"
    outputs:
      validation_report: "${OUTPUT_DIR}/validation-report.json"

  - skill: api.generate-models
    inputs:
      spec_path: "${steps[0].outputs.spec_path}"
      language: "typescript"
    outputs:
      models_dir: "${OUTPUT_DIR}/models/"
```

## Testing Skills

Skills should include comprehensive tests:

```python
# tests/test_custom_processor.py
import pytest
from skills.custom_processor import custom_processor

def test_processor_with_valid_input():
    result = custom_processor.process("test-data.json", {"format": "json"})
    assert result.success
    assert result.output_path.exists()

def test_processor_with_invalid_input():
    with pytest.raises(ValueError):
        custom_processor.process("nonexistent.json")
```

Run tests:
```bash
pytest tests/test_custom_processor.py
```

## See Also

- [Main README](../README.md) — Framework overview
- [Agents README](../agents/README.md) — Skill orchestration
- [Skills Framework](../docs/skills-framework.md) — Complete skill taxonomy
- [Betty Architecture](../docs/betty-architecture.md) — Five-layer architecture
