# Implementation Plan: agent.define Skill

This document outlines the implementation plan for the `agent.define` skill, which validates and registers agent manifests in the Betty Framework.

## Status: Ready for Implementation

**Created**: 2025-10-23
**Target**: Phase 4 of Betty Framework (Intelligence Layer)
**Priority**: High (blocking agent development)

---

## Overview

The `agent.define` skill will:
1. Validate agent manifests (`agent.yaml`) for schema compliance
2. Verify all referenced skills exist in the skill registry
3. Check for circular dependencies
4. Register valid agents in the agent registry (`/registry/agents.json`)
5. Generate documentation scaffolding

---

## Architecture Decisions

### 1. Directory Structure

```
betty-framework/
├── agents/                      # New directory for agent manifests
│   ├── api.designer/
│   │   ├── agent.yaml          # Agent manifest
│   │   ├── README.md           # Auto-generated documentation
│   │   └── tests/              # Agent behavior tests (optional)
│   └── compliance.checker/
│       └── agent.yaml
│
├── skills/
│   └── agent.define/           # New skill
│       ├── skill.yaml          # Skill manifest
│       ├── agent_define.py     # Handler implementation
│       ├── SKILL.md           # Skill documentation
│       └── tests/
│           └── test_agent_define.py
│
├── registry/
│   ├── skills.json            # Existing skill registry
│   └── agents.json            # New agent registry
│
└── betty/
    └── config.py              # Update with agent-related constants
```

### 2. Agent Registry Format

`/registry/agents.json`:
```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-23T10:00:00Z",
  "agents": [
    {
      "name": "api.designer",
      "version": "0.1.0",
      "description": "Design RESTful APIs following enterprise guidelines",
      "reasoning_mode": "iterative",
      "skills_available": ["api.define", "api.validate", "api.generate-models"],
      "status": "draft",
      "capabilities": [...],
      "dependencies": [],
      "tags": ["api", "design", "openapi"]
    }
  ]
}
```

### 3. Validation Strategy

Follow the same pattern as `skill.define`:
- Load and parse YAML
- Validate required fields
- Validate field formats (name, version)
- Validate skill references against skill registry
- Check for circular dependencies
- Delegate to registry updater (new `registry.update-agent` or extend existing)

---

## Implementation Checklist

### Phase 1: Configuration Updates

- [ ] **Update `/betty/config.py`**:
  ```python
  # Add agent-related paths
  AGENTS_DIR = os.path.join(BASE_DIR, "agents")
  AGENTS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "agents.json")

  # Agent manifest required fields
  REQUIRED_AGENT_FIELDS = [
      "name",
      "version",
      "description",
      "capabilities",
      "skills_available",
      "reasoning_mode"
  ]

  # Agent status enum
  class AgentStatus(Enum):
      DRAFT = "draft"
      ACTIVE = "active"
      DEPRECATED = "deprecated"
      ARCHIVED = "archived"

  # Agent reasoning modes
  class ReasoningMode(Enum):
      ITERATIVE = "iterative"
      ONESHOT = "oneshot"

  # Helper functions
  def get_agent_path(agent_name: str) -> str:
      """Get the directory path for an agent."""
      return os.path.join(AGENTS_DIR, agent_name)

  def get_agent_manifest_path(agent_name: str) -> str:
      """Get the manifest path for an agent."""
      return os.path.join(AGENTS_DIR, agent_name, "agent.yaml")
  ```

- [ ] **Update `/betty/validation.py`**:
  ```python
  def validate_agent_name(name: str) -> bool:
      """Validate agent name format."""
      import re
      pattern = r'^[a-z][a-z0-9._-]*$'
      return bool(re.match(pattern, name))

  def validate_reasoning_mode(mode: str) -> bool:
      """Validate reasoning mode."""
      valid_modes = ["iterative", "oneshot"]
      return mode in valid_modes

  def validate_skills_exist(skills: list, skill_registry: dict) -> tuple[bool, list]:
      """
      Validate that all skills exist in the skill registry.

      Returns:
          (valid, missing_skills)
      """
      skill_names = {skill["name"] for skill in skill_registry.get("skills", [])}
      missing = [skill for skill in skills if skill not in skill_names]
      return len(missing) == 0, missing
  ```

- [ ] **Update `/betty/errors.py`**:
  ```python
  class AgentValidationError(BettyError):
      """Raised when agent manifest validation fails."""
      pass

  class AgentRegistryError(BettyError):
      """Raised when agent registry operations fail."""
      pass
  ```

### Phase 2: Create Agent Registry Infrastructure

- [ ] **Create `/registry/agents.json`**:
  ```json
  {
    "registry_version": "1.0.0",
    "generated_at": "2025-10-23T00:00:00Z",
    "agents": []
  }
  ```

- [ ] **Create `/agents/` directory**:
  ```bash
  mkdir -p /home/user/betty/agents
  ```

- [ ] **Create `/agents/README.md`**:
  ```markdown
  # Betty Framework Agents

  This directory contains agent manifests for the Betty Framework.

  ## What are Agents?

  Agents are intelligent orchestrators that compose skills with reasoning,
  context awareness, and error recovery.

  ## Structure

  Each agent has its own directory containing:
  - `agent.yaml` - Agent manifest (required)
  - `README.md` - Documentation (auto-generated)
  - `tests/` - Agent behavior tests (optional)

  ## Creating an Agent

  Use the `agent.define` skill:
  ```bash
  python skills/agent.define/agent_define.py agents/my.agent/agent.yaml
  ```

  ## See Also

  - [Agent Schema Reference](../docs/agent-schema-reference.md)
  - [Betty Architecture](../docs/betty-architecture.md)
  ```

### Phase 3: Implement agent.define Skill

- [ ] **Create `/skills/agent.define/` directory**

- [ ] **Create `/skills/agent.define/skill.yaml`**:
  ```yaml
  name: agent.define
  version: 0.1.0
  description: >
    Validates and registers agent manifests for the Betty Framework.
    Ensures schema compliance and updates the Agent Registry.

  inputs:
    - name: manifest_path
      type: string
      required: true
      description: Path to the agent.yaml file to validate

  outputs:
    - name: validation_result
      type: object
      description: Validation results including errors and warnings
    - name: registry_updated
      type: boolean
      description: Whether agent was successfully registered

  dependencies:
    - skill.define

  status: active

  entrypoints:
    - command: /agent/define
      handler: agent_define.py
      runtime: python
      description: >
        Validate an agent manifest and register it in the Agent Registry.
      parameters:
        - name: manifest_path
          type: string
          required: true
          description: Path to the agent.yaml file
      permissions:
        - filesystem:read
        - filesystem:write

  tags:
    - agents
    - validation
    - registry
  ```

- [ ] **Create `/skills/agent.define/agent_define.py`**:

  Key functions:
  ```python
  def load_agent_manifest(path: str) -> Dict[str, Any]:
      """Load and parse agent manifest from YAML."""
      pass

  def validate_manifest(path: str, skill_registry: dict) -> Dict[str, Any]:
      """
      Validate agent manifest:
      1. Check required fields
      2. Validate name format
      3. Validate version format
      4. Validate reasoning_mode enum
      5. Verify all skills exist in skill registry
      6. Check for circular dependencies
      """
      pass

  def load_skill_registry() -> dict:
      """Load skill registry for validation."""
      pass

  def load_agent_registry() -> dict:
      """Load existing agent registry."""
      pass

  def update_agent_registry(manifest: dict) -> bool:
      """
      Add or update agent in registry:
      1. Load existing registry
      2. Check if agent exists (update vs create)
      3. Add/update agent entry
      4. Update generated_at timestamp
      5. Write registry back to disk
      """
      pass

  def main():
      """
      CLI entry point:
      1. Parse arguments
      2. Validate manifest
      3. Update registry if valid
      4. Return JSON response
      """
      pass
  ```

  Implementation pattern (similar to skill.define):
  ```python
  #!/usr/bin/env python3
  """
  agent_define.py – Implementation of the agent.define Skill
  Validates agent manifests (agent.yaml) and registers them in the Agent Registry.
  """

  import os
  import sys
  import json
  import yaml
  from typing import Dict, Any, List, Optional
  from datetime import datetime, timezone

  sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

  from betty.config import (
      BASE_DIR,
      REQUIRED_AGENT_FIELDS,
      AGENTS_REGISTRY_FILE,
      REGISTRY_FILE,
      ReasoningMode
  )
  from betty.validation import (
      validate_path,
      validate_manifest_fields,
      validate_agent_name,
      validate_version,
      validate_reasoning_mode,
      validate_skills_exist
  )
  from betty.logging_utils import setup_logger
  from betty.errors import AgentValidationError, format_error_response

  logger = setup_logger(__name__)

  # Implementation here...
  ```

- [ ] **Create `/skills/agent.define/SKILL.md`**:
  - Purpose and usage
  - Examples
  - Validation rules
  - Error handling

- [ ] **Create `/skills/agent.define/tests/test_agent_define.py`**:
  ```python
  """Tests for agent.define skill."""
  import pytest
  import os
  import yaml
  from agent_define import (
      load_agent_manifest,
      validate_manifest,
      update_agent_registry
  )

  def test_validate_valid_manifest():
      """Test validation of a valid agent manifest."""
      pass

  def test_validate_missing_required_fields():
      """Test validation fails with missing required fields."""
      pass

  def test_validate_invalid_name_format():
      """Test validation fails with invalid name format."""
      pass

  def test_validate_invalid_version():
      """Test validation fails with invalid version."""
      pass

  def test_validate_invalid_reasoning_mode():
      """Test validation fails with invalid reasoning mode."""
      pass

  def test_validate_missing_skills():
      """Test validation fails when skills don't exist."""
      pass

  def test_registry_update():
      """Test agent registry update."""
      pass
  ```

### Phase 4: Documentation

- [ ] **Create example agent manifests** in `/agents/`:
  - `api.designer/agent.yaml` - Example iterative agent
  - `api.analyzer/agent.yaml` - Example oneshot agent

- [ ] **Update `/docs/references.md`** to include agent schema reference

- [ ] **Create `/agents/.gitkeep`** or example `.gitignore`

### Phase 5: Integration

- [ ] **Update skill registry** to activate `agent.define`:
  ```bash
  python skills/registry.update/registry_update.py skills/agent.define/skill.yaml
  ```

- [ ] **Test end-to-end**:
  ```bash
  # Create test agent manifest
  mkdir -p agents/test.agent
  cat > agents/test.agent/agent.yaml << EOF
  name: test.agent
  version: 0.1.0
  description: "Test agent for validation"
  capabilities:
    - Test capability
  skills_available:
    - skill.define
  reasoning_mode: oneshot
  status: draft
  EOF

  # Validate and register
  python skills/agent.define/agent_define.py agents/test.agent/agent.yaml

  # Verify registry updated
  cat registry/agents.json
  ```

---

## Success Criteria

1. ✅ `agent.define` skill validates all required fields
2. ✅ `agent.define` skill validates name and version formats
3. ✅ `agent.define` skill verifies skill references
4. ✅ `agent.define` skill detects circular dependencies
5. ✅ `agent.define` skill updates agent registry correctly
6. ✅ All tests pass
7. ✅ Documentation is complete and accurate
8. ✅ Can create and validate example agents

---

## Error Handling

### Validation Errors

1. **Missing Required Fields**:
   ```json
   {
     "ok": false,
     "status": "failed",
     "errors": ["Missing required fields: capabilities, skills_available"],
     "path": "agents/api.designer/agent.yaml"
   }
   ```

2. **Invalid Name Format**:
   ```json
   {
     "ok": false,
     "status": "failed",
     "errors": ["Invalid agent name format: 'ApiDesigner' (must match ^[a-z][a-z0-9._-]*$)"],
     "path": "agents/ApiDesigner/agent.yaml"
   }
   ```

3. **Missing Skills**:
   ```json
   {
     "ok": false,
     "status": "failed",
     "errors": ["Skills not found in registry: api.nonexistent, api.missing"],
     "path": "agents/api.designer/agent.yaml"
   }
   ```

4. **Invalid Reasoning Mode**:
   ```json
   {
     "ok": false,
     "status": "failed",
     "errors": ["Invalid reasoning_mode: 'hybrid' (must be 'iterative' or 'oneshot')"],
     "path": "agents/api.designer/agent.yaml"
   }
   ```

### Registry Errors

1. **Registry Not Found**: Create new registry
2. **Registry Parse Error**: Return error, suggest manual fix
3. **Write Permission Error**: Return error with file path

---

## Testing Strategy

### Unit Tests
- Test each validation function independently
- Test manifest loading and parsing
- Test registry update logic
- Test error handling

### Integration Tests
- End-to-end validation and registration
- Multi-agent registry updates
- Concurrent updates (if applicable)

### Validation Test Cases
- ✅ Valid minimal agent
- ✅ Valid complete agent (all fields)
- ❌ Missing required fields
- ❌ Invalid name format
- ❌ Invalid version format
- ❌ Invalid reasoning mode
- ❌ Non-existent skills
- ❌ Empty capabilities
- ❌ Empty skills_available
- ✅ Optional fields present
- ✅ Update existing agent (version change)

---

## Dependencies

### Required Before Implementation
- ✅ Agent frontmatter specification (completed)
- ✅ Agent schema reference documentation (completed)
- ✅ `skill.define` skill (exists)
- ✅ `registry.update` skill (exists)

### Created During Implementation
- `/betty/config.py` updates
- `/betty/validation.py` agent validation functions
- `/betty/errors.py` agent-specific errors
- `/registry/agents.json` agent registry
- `/agents/` directory structure
- `agent.define` skill implementation

---

## Timeline Estimate

| Phase | Estimated Time | Notes |
|-------|----------------|-------|
| Phase 1: Configuration | 1 hour | Config updates, validation functions |
| Phase 2: Registry Infrastructure | 30 minutes | Create directories and initial files |
| Phase 3: agent.define Implementation | 3-4 hours | Core logic, following skill.define pattern |
| Phase 4: Documentation | 1 hour | Examples, SKILL.md |
| Phase 5: Testing | 2-3 hours | Unit tests, integration tests |
| **Total** | **7-9 hours** | Could be split across multiple sessions |

---

## Open Questions

1. **Agent Execution**: Should we implement agent execution logic now, or just focus on definition/validation?
   - **Decision**: Focus on definition/validation first. Execution can be a separate skill (`agent.run`)

2. **Registry Merging**: How to handle registry updates from multiple sources?
   - **Decision**: Single source of truth in `/registry/agents.json`, updated atomically

3. **Version Conflicts**: What happens if an agent with the same name but different version is registered?
   - **Decision**: Update existing entry, maintain single version (similar to skills)

4. **Circular Dependencies**: Should we detect agent-to-agent dependencies?
   - **Decision**: Yes, add to validation logic

5. **Auto-generation**: Should we auto-generate README.md for agents?
   - **Decision**: Yes, generate basic README with manifest info (Phase 4+)

---

## Next Steps

1. Review this plan with team
2. Prioritize phases
3. Begin implementation with Phase 1
4. Create git branch: `feature/agent-define-implementation`
5. Implement incrementally with tests
6. Submit PR when complete

---

## References

- [Agent Schema Reference](./agent-schema-reference.md)
- [Betty Architecture](./betty-architecture.md)
- [Skills Framework](./skills-framework.md)
- Existing implementation: `/skills/skill.define/`
