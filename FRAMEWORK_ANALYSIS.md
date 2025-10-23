# Betty Framework Codebase Analysis

## 1. OVERALL STRUCTURE & ORGANIZATION

### Directory Layout
```
/home/user/betty/
├── .claude/                    # Claude Code Plugin configuration
│   ├── commands/              # Slash command definitions (.md files)
│   ├── hooks.yaml             # Git hook definitions
│   └── README.md
├── .github/                   # GitHub Actions workflows
├── agents/                    # AI Agent definitions
│   ├── api.analyzer/
│   ├── api.designer/
│   └── README.md
├── betty/                     # Core framework library
│   ├── __init__.py
│   ├── config.py              # Configuration & constants
│   ├── validation.py          # Input validation utilities
│   ├── errors.py              # Custom exception classes
│   ├── file_utils.py          # File I/O utilities
│   └── logging_utils.py       # Logging setup
├── skills/                    # Skill implementations (the main CLI commands)
│   ├── skill.create/          # Create new skills
│   ├── skill.define/          # Validate skill manifests
│   ├── registry.update/       # Update skill registry
│   ├── workflow.compose/      # Execute multi-step workflows
│   ├── workflow.validate/     # Validate workflow definitions
│   ├── policy.enforce/        # Enforce policy rules
│   ├── api.define/            # Create API specs
│   ├── api.validate/          # Validate API specs
│   ├── api.compatibility/     # Check API breaking changes
│   ├── api.generate-models/   # Generate models from specs
│   ├── agent.define/          # Validate & register agents
│   ├── command.define/        # Define CLI commands
│   ├── hook.define/           # Define Git hooks
│   ├── hook.register/         # Register hooks
│   ├── audit.log/             # Log audit events
│   └── generate.docs/         # Generate documentation
├── registry/                  # Persistent storage for framework state
│   ├── skills.json            # Skill registry
│   ├── agents.json            # Agent registry
│   ├── commands.json          # Command registry
│   ├── hooks.json             # Hook registry
│   ├── audit_log.json         # Audit log
│   ├── workflow_history.json  # Execution history
│   └── policies/              # Policy definitions
├── workflows/                 # Workflow definitions (.yaml)
│   ├── create_workflow_validate.yaml
│   ├── api_first_development.yaml
│   └── api_full_lifecycle.yaml
├── tests/                     # Integration & unit tests
├── docs/                      # Documentation
├── examples/                  # Example files
├── plugin.yaml                # Main plugin manifest
├── README.md                  # Framework documentation
└── requirements.txt           # Python dependencies
```

---

## 2. CLI COMMANDS STRUCTURE

### Command Definition Location
- **Primary Definition**: `/home/user/betty/plugin.yaml` (lines 48-273)
- **Alternative Docs**: `/home/user/betty/.claude/commands/` (human-readable markdown)

### Core CLI Commands (as defined in plugin.yaml)

#### FOUNDATION SKILLS

**1. `/skill/create`** - Create new Betty skills
```yaml
Script: skills/skill.create/skill_create.py
Parameters:
  - skill_name (string, required): Name like "runtime.execute"
  - description (string, required): What the skill does
  - inputs (string, optional): Comma-separated list
  - outputs (string, optional): Comma-separated list
Outputs: skill_directory, skill_manifest.yaml, registration_record.json
```

**2. `/skill/define`** - Validate skill manifests
```yaml
Script: skills/skill.define/skill_define.py
Parameters:
  - manifest_path (string, required): Path to skill.yaml
Outputs: validation_result.json, updated_registry.json
```

**3. `/agent/define`** - Validate & register agents
```yaml
Script: skills/agent.define/agent_define.py
Parameters:
  - manifest_path (string, required): Path to agent.yaml
```

**4. `/registry/update`** - Add/update registry entries
```yaml
Script: skills/registry.update/registry_update.py
Parameters:
  - manifest_path (string, required): Path to skill manifest
```

**5. `/workflow/compose`** - Execute multi-step workflows
```yaml
Script: skills/workflow.compose/workflow_compose.py
Parameters:
  - workflow_file (string, required): Path to workflow YAML
```

#### API DEVELOPMENT SKILLS

**6. `/api-define`** - Create OpenAPI/AsyncAPI specs
**7. `/api-validate`** - Validate against enterprise guidelines
**8. `/api-generate`** - Generate models (TypeScript, Python, Java, etc.)
**9. `/api-compatibility`** - Detect breaking changes

---

## 3. SKILL IMPLEMENTATION PATTERNS

### Skill Directory Structure
Each skill is organized as:
```
skills/[skill.name]/
├── skill.yaml                 # Manifest (metadata, inputs, outputs, entrypoints)
├── [handler].py              # Implementation script (e.g., skill_create.py)
├── SKILL.md                  # Documentation
└── [optional files]          # Templates, dependencies, etc.
```

### Manifest Format (skill.yaml)
```yaml
name: skill.create                    # Must be lowercase with dots
version: 0.1.0                       # Semantic versioning
description: Description of skill    # What it does
inputs:
  - skill_name                       # Input parameter names
  - description
outputs:
  - skill_directory                  # Output parameter names
dependencies:
  - skill.define                     # Other required skills
  - context.schema
status: active                       # draft, active, deprecated, archived
entrypoints:
  - command: /skill/create           # CLI command trigger
    handler: skill_create.py         # Implementation file
    runtime: python
    parameters:
      - name: skill_name
        type: string
        required: true
        description: Name of the new skill
    permissions:
      - filesystem
      - read
      - write
```

### Handler Script Pattern
All skill handlers follow this pattern:

```python
#!/usr/bin/env python3
import sys
import os
import json
import argparse

# Add Betty to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, get_skill_path, ensure_directories
from betty.validation import validate_skill_name, ValidationError
from betty.logging_utils import setup_logger
from betty.errors import ManifestError, format_error_response

logger = setup_logger(__name__)

def build_response(ok: bool, path, errors=None, details=None):
    """Standardized response format"""
    return {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "path": path,
        "details": details
    }

def main_logic(*args, **kwargs):
    """Core implementation"""
    # Implementation here
    return result_dict

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("param1", help="Description")
    parser.add_argument("--optional", help="Optional parameter")
    args = parser.parse_args()
    
    try:
        result = main_logic(args.param1, args.optional)
        print(json.dumps(result, indent=2))
        sys.exit(0)
    except (ValidationError, ManifestError) as e:
        logger.error(str(e))
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(json.dumps(format_error_response(e, include_traceback=True), indent=2))
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Key Skill Implementations

#### skill.create (skill_create.py)
- **Location**: `/home/user/betty/skills/skill.create/skill_create.py`
- **Function**: Scaffolds new skill directories with manifest, handler, and docs
- **Process**:
  1. Validates skill name (lowercase, dots allowed)
  2. Creates skill directory
  3. Generates skill.yaml manifest
  4. Creates SKILL.md documentation
  5. Creates handler Python template
  6. Runs skill.define for validation
  7. Updates registry via registry.update

#### skill.define (skill_define.py)
- **Location**: `/home/user/betty/skills/skill.define/skill_define.py`
- **Function**: Validates skill manifests against schema
- **Checks**:
  - Required fields present (name, version, description, inputs, outputs, status)
  - Semantic version format
  - Valid status (draft, active, deprecated, archived)
  - File exists and is valid YAML

#### registry.update (registry_update.py)
- **Location**: `/home/user/betty/skills/registry.update/registry_update.py`
- **Function**: Updates `/home/user/betty/registry/skills.json`
- **Process**:
  1. Loads manifest from skill.yaml
  2. Runs policy.enforce validation
  3. Merges into existing registry
  4. Writes updated JSON

#### workflow.compose (workflow_compose.py)
- **Location**: `/home/user/betty/skills/workflow.compose/workflow_compose.py`
- **Function**: Orchestrates multi-step workflows
- **Features**:
  - Sequential skill execution
  - Fail-fast mode (stops on first error)
  - Audit logging of each step
  - Workflow history recording

#### policy.enforce (policy_enforce.py)
- **Location**: `/home/user/betty/skills/policy.enforce/policy_enforce.py`
- **Rules Enforced**:
  - Naming conventions (lowercase, dots, no spaces)
  - Semantic versioning
  - Valid permissions (filesystem, network, read, write)
  - Valid status values
  - Required fields presence

---

## 4. WORKFLOW EXECUTION STRUCTURE

### Workflow Definition Format (YAML)
```yaml
# workflows/api_first_development.yaml
name: api_first_development
version: 1.0.0
description: Complete API-first development workflow

steps:
  - skill: api.define                    # Skill to execute
    args:                                # Arguments to pass
      - "${service_name}"
      - "${spec_type}"
      - "--template=zalando"
    description: "Create Zalando-compliant API spec"
    
  - skill: api.validate
    args:
      - "specs/${service_name}.${spec_type}.yaml"
      - "zalando"
    description: "Validate against Zalando guidelines"

tags:
  - api-first
  - zalando
```

### Workflow Execution Flow
1. Load workflow YAML via `load_workflow()`
2. For each step:
   - Get skill handler path via `get_skill_handler_path()`
   - Execute as subprocess: `python [handler] [args]`
   - Capture stdout (JSON output), stderr, returncode
   - Parse JSON response
   - Record execution in history
3. If fail_fast=true and step fails, stop immediately
4. Aggregate results and return

### Workflow History Storage
- **Location**: `/home/user/betty/registry/workflow_history.json`
- **Format**: JSON array of workflow execution records
- **Record Structure**:
```json
{
  "workflow": "api_first_development.yaml",
  "workflow_path": "/home/user/betty/workflows/api_first_development.yaml",
  "started_at": "2025-10-23T00:13:56.319229+00:00",
  "fail_fast": true,
  "steps": [
    {
      "step_number": 1,
      "skill": "skill.create",
      "args": ["test.example", "Example skill"],
      "status": "success",
      "returncode": 0,
      "stdout": "... output ...",
      "stderr": "",
      "parsed": { "ok": true, "status": "success", ... },
      "duration_ms": 850
    }
  ],
  "status": "success",
  "completed_at": "2025-10-23T00:13:56.891522+00:00"
}
```

### Example Execution Output (from workflow_history.json)
```json
{
  "workflow": "test_lifecycle.yaml",
  "timestamp": "2025-10-23T00:13:56.319229+00:00",
  "steps": [
    {
      "step_number": 1,
      "skill": "skill.create",
      "args": ["test.example", "Example skill for testing workflow orchestration"],
      "output": "2025-10-23 00:13:56 - __main__ - INFO - Created skill directory: ...",
      "returncode": 0,
      "status": "success"
    }
  ],
  "status": "success",
  "completed_at": "2025-10-23T00:13:56.891522+00:00"
}
```

---

## 5. REGISTRY FILES & FORMATS

### skills.json Registry
**Location**: `/home/user/betty/registry/skills.json`
**Purpose**: Central registry of all installed skills
**Structure**:
```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T02:30:14.709693+00:00",
  "skills": [
    {
      "name": "skill.create",
      "version": "0.1.0",
      "description": "Generates a new Betty Framework Skill...",
      "inputs": ["skill_name", "description", "inputs", "outputs"],
      "outputs": ["skill_directory", "manifest_path", "registration_record.json"],
      "dependencies": ["skill.define", "context.schema"],
      "status": "active",
      "entrypoints": [...]
    }
  ]
}
```

### workflow_history.json
**Location**: `/home/user/betty/registry/workflow_history.json`
**Purpose**: Complete audit trail of workflow executions
**Contents**: Array of workflow execution records (see above)

### agents.json
**Location**: `/home/user/betty/registry/agents.json`
**Purpose**: Registry of AI agents
**Format**: Similar to skills.json

### Configuration Constants
**Location**: `/home/user/betty/betty/config.py`
**Key Paths**:
```python
BASE_DIR = BETTY_HOME
SKILLS_DIR = "skills"
AGENTS_DIR = "agents"
REGISTRY_DIR = "registry"
WORKFLOWS_DIR = "workflows"
REGISTRY_FILE = "registry/skills.json"
AGENTS_REGISTRY_FILE = "registry/agents.json"
WORKFLOW_HISTORY_FILE = "registry/workflow_history.json"
REGISTRY_VERSION = "1.0.0"
```

---

## 6. TESTING STRUCTURE & PATTERNS

### Test File Locations
```
tests/
├── test_integration_core.py    # Full lifecycle integration tests
├── test_commands.py             # Command validation tests
├── test_validation.py           # Input validation unit tests
├── test_config.py               # Configuration tests
├── test_errors.py               # Error handling tests
├── test_skill_yaml_validation.py # YAML schema validation
├── test_agent_yaml_validation.py # Agent manifest validation
├── test_workflow_validate.py     # Workflow validation tests
├── test_api_skills.py           # API skill tests
├── test_hooks.py                # Hook functionality tests
├── test_command_define_skill.py  # Command definition tests
└── __init__.py
```

### Integration Test Pattern (test_integration_core.py)
```python
import pytest
import subprocess
from pathlib import Path

class TestSkillCreateIntegration:
    """Integration tests for skill.create"""
    
    @pytest.fixture
    def temp_skill_name(self):
        """Generate temp skill name"""
        return "test.integration.temp"
    
    @pytest.fixture(autouse=True)
    def cleanup_skill(self, temp_skill_name):
        """Cleanup after each test"""
        yield
        skill_path = BASE_PATH / "skills" / temp_skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)
    
    def test_skill_create_basic(self, temp_skill_name):
        """Test basic skill creation"""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Integration test skill"
            ],
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["ok"] is True
        assert output["status"] == "success"
```

### Key Testing Patterns

1. **JSON Output Parsing**
   - Skills output JSON to stdout
   - Tests use `parse_json_output()` helper
   - Handles logging mixed with JSON output

2. **Subprocess Execution**
   - Skills invoked via subprocess.run()
   - 5-minute timeout for workflow execution
   - Capture stdout, stderr, returncode

3. **Cleanup Fixtures**
   - Use pytest fixtures with autouse=True
   - Clean up created test artifacts
   - Isolated test runs

4. **Full Lifecycle Tests**
   - Create → Validate → Register flow
   - Verify files created
   - Verify registry updated

---

## 7. VALIDATION & ERROR HANDLING

### Validation Module (/home/user/betty/betty/validation.py)
**Key Functions**:
- `validate_skill_name()` - Lowercase, dots/hyphens allowed
- `validate_path()` - Path traversal, null byte checks
- `validate_manifest_fields()` - Required fields present
- `validate_version()` - Semantic versioning
- `validate_agent_name()` - Agent naming rules
- `validate_command_name()` - Command naming (slash prefix)
- `validate_hook_name()` - Hook naming rules
- `validate_command_execution_type()` - agent/skill/workflow
- `validate_hook_event()` - Valid event types
- `validate_skills_exist()` - Skills in registry

### Error Classes (/home/user/betty/betty/errors.py)
```python
class BettyError(Exception):          # Base class
class SkillNotFoundError(BettyError)
class SkillValidationError(BettyError)
class RegistryError(BettyError)
class WorkflowError(BettyError)
class ManifestError(BettyError)
class AgentValidationError(BettyError)
class AgentRegistryError(BettyError)
```

### Response Format (Standardized across all skills)
```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "/path/to/resource",
  "details": {
    "skill_name": "test.example",
    "validation": "passed",
    "registry_updated": true,
    "timestamp": "2025-10-23T00:13:56.634600+00:00"
  }
}
```

---

## 8. CONFIGURATION & CONSTANTS

### Key Configuration Files

**plugin.yaml** (Main plugin manifest)
- Defines all commands, agents, permissions
- Specifies runtime requirements
- Configuration defaults
- Health checks

**config.py** (Framework constants)
```python
BETTY_HOME = os.environ.get('BETTY_HOME', '...')  # Configurable
BASE_DIR = BETTY_HOME
SKILLS_DIR = BASE_DIR + "/skills"
REGISTRY_FILE = BASE_DIR + "/registry/skills.json"
WORKFLOW_HISTORY_FILE = BASE_DIR + "/registry/workflow_history.json"

# Enums
class SkillStatus: DRAFT, ACTIVE, DEPRECATED, ARCHIVED
class CommandExecutionType: AGENT, SKILL, WORKFLOW
class HookEvent: ON_FILE_EDIT, ON_FILE_SAVE, ON_COMMIT, ON_PUSH, ...
```

---

## 9. AGENT DEFINITIONS

### Agent Manifest Structure (agent.yaml)
```yaml
name: api.designer
version: 0.1.0
description: Design APIs with iterative refinement

capabilities:
  - Design RESTful APIs from natural language
  - Apply Zalando guidelines automatically
  - Generate OpenAPI 3.1 specs
  - Iteratively refine based on validation

skills_available:
  - api.define
  - api.validate
  - api.generate-models
  - api.compatibility

reasoning_mode: iterative           # or oneshot

context_requirements:
  guidelines: string
  domain: string
  existing_apis: list

workflow_pattern: |
  1. Analyze requirements and domain context
  2. Draft OpenAPI spec following guidelines
  3. Run validation (api.validate)
  4. If validation fails:
     - Analyze errors
     - Refine spec
     - Re-validate
     - Repeat until passing
  5. Generate models for target languages

error_handling:
  max_retries: 3
  timeout_seconds: 300

status: draft
tags: [api, design, openapi, zalando]
```

---

## 10. FRAMEWORK DEPENDENCIES

### Python Requirements
```
pyyaml>=5.4
datamodel-code-generator>=2.0 (optional, for model generation)
```

### Core Betty Modules
- `betty.config` - Paths, constants, enums
- `betty.validation` - Input validation
- `betty.errors` - Exception classes
- `betty.file_utils` - File I/O helpers
- `betty.logging_utils` - Logging setup

---

## 11. EXECUTION FLOW DIAGRAM

```
CLI Command (/skill/create)
         ↓
    plugin.yaml
    (Find handler)
         ↓
skills/skill.create/skill_create.py
         ↓
   Main Function
    (Parse args)
         ↓
   Validation
(validate_skill_name, validate_path)
         ↓
   Core Logic
 (create_skill())
         ↓
Directory & File Creation
(skill.yaml, SKILL.md, handler.py)
         ↓
Subprocess: skill.define
         ↓
Subprocess: registry.update
         ↓
JSON Response
         ↓
   CLI Exit
```

---

## 12. WORKFLOW EXECUTION DIAGRAM

```
/workflow/compose workflows/api_first_development.yaml
         ↓
Load & Parse YAML
         ↓
For each step:
  ├─ Get handler path (get_skill_handler_path)
  ├─ Run subprocess: python handler args
  ├─ Capture stdout/stderr
  ├─ Parse JSON output
  ├─ Record in step result
  └─ Continue or fail-fast
         ↓
Aggregate Results
         ↓
Record in workflow_history.json
         ↓
Return Combined Response
```

---

## SUMMARY

The Betty Framework is a sophisticated plugin system for Claude Code that:

1. **CLI Commands** are defined in `plugin.yaml` and implemented as Python scripts in `skills/*/`
2. **Core Commands** are: skill.create, skill.define, registry.update, workflow.compose, policy.enforce, and API tools
3. **Skills** are self-contained units with manifest (YAML) + handler (Python)
4. **Workflows** chain skills together via simple YAML definition
5. **Registry** tracks all skills, agents, commands in JSON files in `registry/`
6. **Workflow History** provides complete audit trail of executions
7. **Testing** uses pytest with subprocess-based integration tests
8. **Validation** is enforced at multiple levels (naming, schema, policies)
9. **Error Handling** is standardized with JSON responses
10. **Configuration** is centralized in `config.py` with `BETTY_HOME` override capability

