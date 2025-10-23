# Betty Framework CLI Commands Quick Reference

## Foundation Skills (Framework Management)

### `/skill/create` - Create New Skills
**File**: `skills/skill.create/skill_create.py`
**Purpose**: Scaffold a new skill directory with manifest, handler, and documentation

```bash
python skills/skill.create/skill_create.py <skill_name> "<description>" [--inputs input1,input2] [--outputs output1,output2]
```

**Process**:
1. Validates skill name (lowercase, dots allowed: e.g., "api.monitor")
2. Creates directory: `skills/[skill_name]/`
3. Generates `skill.yaml` manifest
4. Creates handler Python file (`[skill_name].py`)
5. Creates `SKILL.md` documentation
6. Validates via `skill.define`
7. Registers in `registry/skills.json`

**Response**:
```json
{
  "ok": true,
  "status": "success",
  "path": "/home/user/betty/skills/api.monitor",
  "details": {
    "skill_name": "api.monitor",
    "validation": "passed",
    "registry_updated": true,
    "timestamp": "2025-10-23T00:13:56.634600+00:00"
  }
}
```

---

### `/skill/define` - Validate Skill Manifests
**File**: `skills/skill.define/skill_define.py`
**Purpose**: Validate a skill.yaml manifest for schema compliance

```bash
python skills/skill.define/skill_define.py <path/to/skill.yaml>
```

**Validates**:
- Required fields: name, version, description, inputs, outputs, status
- Semantic versioning format
- Valid status values (draft, active, deprecated, archived)
- YAML syntax
- File existence

**Response**:
```json
{
  "ok": true,
  "status": "success",
  "path": "skills/api.monitor/skill.yaml",
  "details": {
    "valid": true,
    "missing": [],
    "manifest": {
      "name": "api.monitor",
      "version": "0.1.0",
      "status": "active",
      ...
    }
  }
}
```

---

### `/registry/update` - Update Skill Registry
**File**: `skills/registry.update/registry_update.py`
**Purpose**: Add or update a skill in the central registry

```bash
python skills/registry.update/registry_update.py <path/to/skill.yaml>
```

**Process**:
1. Loads manifest from YAML
2. Enforces policies via `policy.enforce`
3. Merges into `registry/skills.json`
4. Updates timestamp

**Response**:
```json
{
  "ok": true,
  "status": "success",
  "path": "skills/api.monitor/skill.yaml",
  "details": {
    "status": "success",
    "updated": "api.monitor",
    "registry_path": "/home/user/betty/registry/skills.json",
    "total_skills": 12,
    "timestamp": "2025-10-23T02:30:14.709693+00:00"
  }
}
```

---

### `/workflow/compose` - Execute Multi-Step Workflows
**File**: `skills/workflow.compose/workflow_compose.py`
**Purpose**: Chain multiple skills together in a workflow

```bash
python skills/workflow.compose/workflow_compose.py <path/to/workflow.yaml>
```

**Workflow YAML Format**:
```yaml
steps:
  - skill: skill.define
    args: ["skills/api.monitor/skill.yaml"]
    description: "Validate the manifest"
  
  - skill: registry.update
    args: ["skills/api.monitor/skill.yaml"]
    description: "Register in system"
```

**Process**:
1. Load and parse YAML
2. For each step:
   - Execute skill handler as subprocess
   - Capture stdout/stderr
   - Parse JSON output
   - Log to audit trail
3. Record complete execution in `workflow_history.json`
4. Return aggregated results

**Response**:
```json
{
  "ok": true,
  "status": "success",
  "path": "/home/user/betty/workflows/my_workflow.yaml",
  "details": {
    "steps": [
      {
        "step_number": 1,
        "skill": "skill.define",
        "status": "success",
        "returncode": 0,
        "duration_ms": 237
      },
      {
        "step_number": 2,
        "skill": "registry.update",
        "status": "success",
        "returncode": 0,
        "duration_ms": 180
      }
    ],
    "status": "success",
    "completed_at": "2025-10-23T00:13:56.891522+00:00"
  }
}
```

---

### `/policy/enforce` - Enforce Policy Rules
**File**: `skills/policy.enforce/policy_enforce.py`
**Purpose**: Validate manifests against naming and structure policies

```bash
python skills/policy.enforce/policy_enforce.py <path/to/manifest.yaml>
```

**Rules Enforced**:
- Naming convention: lowercase, dots allowed, no spaces
- Semantic versioning (e.g., 1.0.0)
- Valid permissions: filesystem, network, read, write
- Valid status: draft, active, deprecated, archived
- Required fields present

**Response**:
```json
{
  "ok": true,
  "status": "success",
  "violations": [],
  "details": {
    "name_format": "valid",
    "version_format": "valid",
    "permissions": "valid",
    "status": "valid"
  }
}
```

---

## API Development Skills

### `/api-define` - Create API Specifications
**File**: `skills/api.define/api_define.py`
**Purpose**: Generate OpenAPI/AsyncAPI specs from templates

```bash
python skills/api.define/api_define.py <service_name> [openapi|asyncapi] --template=zalando
```

**Outputs**:
- `specs/[service_name].openapi.yaml` - Generated specification

---

### `/api-validate` - Validate API Specs
**File**: `skills/api.validate/api_validate.py`
**Purpose**: Validate specs against enterprise guidelines

```bash
python skills/api.validate/api_validate.py <spec_path> [zalando|google|microsoft]
```

**Guidelines**:
- Zalando RESTful API Guidelines
- Google API Improvement Proposals
- Microsoft Cloud Guidelines

---

### `/api-generate` - Generate Models
**File**: `skills/api.generate-models/modelina_generate.py`
**Purpose**: Generate type-safe models from API specs

```bash
python skills/api.generate-models/modelina_generate.py <spec_path> [typescript|python|java|go]
```

**Output Languages**:
- TypeScript (interfaces)
- Python (dataclasses)
- Java (classes)
- Go (structs)

---

### `/api-compatibility` - Check for Breaking Changes
**File**: `skills/api.compatibility/check_compatibility.py`
**Purpose**: Compare API versions for compatibility issues

```bash
python skills/api.compatibility/check_compatibility.py <old_spec> <new_spec>
```

**Detection**:
- Removed endpoints
- Removed or changed properties
- Made optional fields required
- Suggestions for migration

---

## File Locations Quick Reference

### Core Framework Files
- **Plugin Definition**: `/home/user/betty/plugin.yaml`
- **Config Constants**: `/home/user/betty/betty/config.py`
- **Validation Rules**: `/home/user/betty/betty/validation.py`
- **Error Classes**: `/home/user/betty/betty/errors.py`

### Registries
- **Skill Registry**: `/home/user/betty/registry/skills.json`
- **Agent Registry**: `/home/user/betty/registry/agents.json`
- **Workflow History**: `/home/user/betty/registry/workflow_history.json`
- **Command Registry**: `/home/user/betty/registry/commands.json`
- **Hook Registry**: `/home/user/betty/registry/hooks.json`
- **Audit Log**: `/home/user/betty/registry/audit_log.json`

### Skill Implementations
- All in `/home/user/betty/skills/[skill.name]/`
- Handler pattern: `[skill_name].py` (dots replaced with underscores)
- Manifest pattern: `skill.yaml`

### Workflows
- All in `/home/user/betty/workflows/`
- Format: YAML files with `.yaml` extension
- Step-based execution with skill references

### Tests
- All in `/home/user/betty/tests/`
- Subprocess-based integration tests
- Tests call skill handlers directly

---

## Standard Response Format

All skills output JSON in this format:

```json
{
  "ok": true|false,
  "status": "success|failed",
  "errors": ["error1", "error2"],
  "path": "/path/to/resource",
  "details": {
    "...": "skill-specific details"
  }
}
```

**Key Values**:
- `ok`: true if successful, false if failed
- `status`: "success" or "failed"
- `errors`: List of error messages (empty if no errors)
- `path`: Relevant file/directory path
- `details`: Skill-specific metadata

---

## Common Integration Patterns

### Complete Lifecycle: Create → Validate → Register
```bash
# 1. Create skill
python skills/skill.create/skill_create.py api.monitor "Monitor API health"

# 2. Skill automatically validates (via skill.create calling skill.define)

# 3. Skill automatically registers (via skill.create calling registry.update)

# 4. (Optional) Manually verify registration
python skills/skill.define/skill_define.py skills/api.monitor/skill.yaml
```

### Execute a Workflow
```bash
python skills/workflow.compose/workflow_compose.py workflows/api_first_development.yaml
```

### Validate All Manifests
```bash
# Validate skill
python skills/skill.define/skill_define.py skills/api.monitor/skill.yaml

# Validate workflow
python skills/workflow.validate/workflow_validate.py workflows/my_workflow.yaml

# Validate agent
python skills/agent.define/agent_define.py agents/api.designer/agent.yaml
```

---

## Configuration

### Environment Variables
- `BETTY_HOME`: Override default Betty directory (default: auto-detected)

### Required Directories
- `skills/` - Skill implementations
- `agents/` - Agent definitions
- `registry/` - Registries and audit logs
- `workflows/` - Workflow definitions
- `.claude/commands/` - Command documentation
- `.claude/hooks/` - Hook definitions

---

## Naming Conventions

### Skill Names
- Lowercase letters, numbers, dots, hyphens, underscores
- Examples: `skill.create`, `api.monitor`, `runtime-execute`
- Handler files use underscores: `skill_create.py`, `api_monitor.py`

### Agent Names
- Same as skill names
- Examples: `api.designer`, `compliance.checker`

### Command Names
- Start with `/`
- Followed by lowercase letters, numbers, hyphens
- Examples: `/api-design`, `/api-validate`, `/workflow-run`

### Skill Status Values
- `draft` - In development
- `active` - Ready for production
- `deprecated` - No longer recommended
- `archived` - No longer maintained

---

## Testing

### Run Integration Tests
```bash
cd /home/user/betty
pytest tests/test_integration_core.py -v
```

### Run All Tests
```bash
pytest tests/ -v
```

### Test Specific Skill
```bash
pytest tests/test_integration_core.py::TestSkillCreateIntegration::test_skill_create_basic -v
```

