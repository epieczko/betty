# Agent Manifest Schema Reference

This document provides the formal specification for Betty Framework agent manifests.

## Overview

Agents are intelligent orchestrators that compose skills with reasoning, context awareness, and error recovery. Unlike workflows (which follow fixed sequential steps) or skills (which execute atomic operations), agents can:

- **Reason** about requirements and choose appropriate strategies
- **Iterate** based on feedback and validation results
- **Recover** from errors with intelligent retry logic
- **Adapt** their approach based on context

## File Structure

```
agents/
├── <agent-name>/
│   ├── agent.yaml              # Agent manifest (required)
│   ├── README.md               # Documentation (auto-generated)
│   ├── tests/                  # Agent behavior tests (optional)
│   │   └── test_agent.py
│   └── examples/               # Example invocations (optional)
│       └── example_usage.md
```

## Manifest Format

### Complete Example

```yaml
# agents/api.designer/agent.yaml

# === REQUIRED FIELDS ===

name: api.designer
version: 0.1.0
description: "Design RESTful APIs following enterprise guidelines with iterative refinement"

capabilities:
  - Design RESTful APIs from natural language requirements
  - Apply Zalando guidelines automatically
  - Generate OpenAPI 3.1 specs with best practices
  - Iteratively refine based on validation feedback
  - Handle AsyncAPI for event-driven architectures

skills_available:
  - api.define
  - api.validate
  - api.generate-models
  - api.compatibility

reasoning_mode: iterative

# === OPTIONAL FIELDS ===

status: draft

context_requirements:
  guidelines: string
  domain: string
  existing_apis: list
  strict_mode: boolean

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
  6. Verify generated models compile

example_task: |
  Input: "Create API for user management with CRUD operations"

  Agent will:
  1. Draft OpenAPI spec with resource paths
  2. Apply Zalando guidelines
  3. Validate spec against Zally rules
  4. Fix issues iteratively
  5. Generate models
  6. Verify compilation

error_handling:
  max_retries: 3
  on_validation_failure: "Analyze errors, refine spec, retry"
  on_generation_failure: "Try alternative configurations"
  timeout_seconds: 300

output:
  success:
    - OpenAPI spec (validated)
    - Generated models (compiled)
    - Validation report
  failure:
    - Error analysis
    - Partial spec
    - Suggested fixes

tags:
  - api
  - design
  - openapi

dependencies:
  - context.schema
```

---

## Field Reference

### Required Fields

#### `name`
- **Type**: `string`
- **Format**: `^[a-z][a-z0-9._-]*$`
- **Pattern**: `<domain>.<action>`
- **Examples**: `api.designer`, `compliance.checker`, `data.migrator`
- **Description**: Unique identifier for the agent. Must be lowercase, start with a letter, and use dots, hyphens, or underscores as separators.

**Validation Rules**:
- Must match regex pattern
- Must be unique within agent registry
- Cannot be empty
- Recommended max length: 50 characters

---

#### `version`
- **Type**: `string`
- **Format**: `^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$`
- **Examples**: `0.1.0`, `1.0.0`, `2.3.1-beta`, `1.0.0-rc.1`
- **Description**: Semantic version following [semver](https://semver.org/) specification.

**Versioning Guidelines**:
- **MAJOR**: Breaking changes to agent interface or behavior
- **MINOR**: New capabilities or skills added (backward compatible)
- **PATCH**: Bug fixes, refinements (backward compatible)
- **Prerelease**: `-alpha`, `-beta`, `-rc.1` for pre-release versions

---

#### `description`
- **Type**: `string`
- **Length**: 1-200 characters
- **Example**: `"Design RESTful APIs following enterprise guidelines with iterative refinement"`
- **Description**: Human-readable summary of what the agent does.

**Best Practices**:
- Start with an action verb (Design, Analyze, Validate, Generate)
- Be specific about the domain and purpose
- Mention key features or guidelines if applicable
- Keep it concise but informative

---

#### `capabilities`
- **Type**: `array[string]`
- **Min Length**: 1
- **Example**:
  ```yaml
  capabilities:
    - Design RESTful APIs from natural language requirements
    - Apply Zalando guidelines automatically
    - Generate OpenAPI 3.1 specs with best practices
    - Iteratively refine based on validation feedback
  ```
- **Description**: List of what the agent can accomplish.

**Best Practices**:
- Each capability should be a complete sentence
- Start with action verbs
- Be specific about technologies, standards, or frameworks
- Order by importance or typical execution order
- Include iteration/refinement capabilities if applicable

---

#### `skills_available`
- **Type**: `array[string]`
- **Min Length**: 1
- **Format**: Each element must be a valid skill name
- **Example**:
  ```yaml
  skills_available:
    - api.define
    - api.validate
    - api.generate-models
    - api.compatibility
  ```
- **Description**: List of skills the agent can orchestrate.

**Validation Rules**:
- All skills must exist in the skill registry
- Skill names must match regex: `^[a-z][a-z0-9._-]*$`
- No duplicate skills
- At least one skill required

**Best Practices**:
- List skills in logical execution order
- Add inline comments explaining each skill's role
- Only include skills the agent will actually use
- Consider grouping related skills

---

#### `reasoning_mode`
- **Type**: `enum`
- **Values**: `iterative` | `oneshot`
- **Default**: None (must be specified)
- **Description**: Defines how the agent approaches problem-solving.

**Mode Definitions**:

**`iterative`** - Agent can retry with feedback
- Use for: Validation loops, refinement tasks, error correction
- Behavior: Agent analyzes failures, adjusts strategy, retries
- Example: API design with validation feedback
- Max iterations: Defined in `error_handling.max_retries`

**`oneshot`** - Agent executes once without retry
- Use for: Analysis, reporting, deterministic transformations
- Behavior: Single execution, returns result or error
- Example: API compatibility report, documentation generation
- Failure: Returns immediately with error details

---

### Optional Fields

#### `status`
- **Type**: `enum`
- **Values**: `draft` | `active` | `deprecated` | `archived`
- **Default**: `draft`
- **Description**: Lifecycle stage of the agent.

**Status Lifecycle**:
```
draft → active → deprecated → archived
```

**Status Definitions**:
- **`draft`**: Under development, not ready for production
- **`active`**: Production-ready, can be invoked by commands
- **`deprecated`**: Still functional but not recommended (emits warnings)
- **`archived`**: No longer maintained, cannot be executed

**Validation Rules**:
- Can only progress forward in lifecycle
- Cannot transition from `archived` to any other state
- Only `active` agents can be invoked by commands

---

#### `context_requirements`
- **Type**: `object`
- **Default**: `{}`
- **Example**:
  ```yaml
  context_requirements:
    guidelines: string
    domain: string
    existing_apis: list
    strict_mode: boolean
    target_languages: list
  ```
- **Description**: Structured context the agent needs to make decisions.

**Best Practices**:
- Define type for each context field (string, boolean, number, list, object)
- Document expected values or formats
- Mark required vs optional context
- Provide sensible defaults where possible

**Common Context Patterns**:
```yaml
# API Design Context
context_requirements:
  guidelines: string        # zalando, google, microsoft
  domain: string           # user-management, payments
  existing_apis: list      # Related APIs for consistency

# Compliance Context
context_requirements:
  policy_set: string       # Which policies to enforce
  severity_threshold: string  # error, warning, info

# Code Generation Context
context_requirements:
  target_languages: list   # typescript, python, java
  framework: string        # react, django, spring
  style_guide: string      # airbnb, google
```

---

#### `workflow_pattern`
- **Type**: `string` (multi-line)
- **Default**: `null`
- **Example**:
  ```yaml
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
  ```
- **Description**: Narrative description of the agent's reasoning process.

**Best Practices**:
- Use numbered steps for sequential actions
- Use bullet points for decision branches
- Reference specific skills in parentheses
- Describe iteration/retry logic clearly
- Keep it high-level (not implementation details)

---

#### `example_task`
- **Type**: `string` (multi-line)
- **Default**: `null`
- **Example**:
  ```yaml
  example_task: |
    Input: "Create API for user management with CRUD operations"

    Agent will:
    1. Draft OpenAPI spec with resource paths
    2. Apply Zalando guidelines
    3. Validate spec against Zally rules
    4. Fix issues iteratively
    5. Generate TypeScript and Python models
  ```
- **Description**: Concrete example demonstrating agent behavior.

**Best Practices**:
- Show realistic input
- Describe step-by-step what the agent does
- Mention specific technologies or standards
- Include expected outputs
- Show iteration/refinement if applicable

---

#### `error_handling`
- **Type**: `object`
- **Default**: `{}`
- **Example**:
  ```yaml
  error_handling:
    max_retries: 3
    on_validation_failure: "Analyze errors, refine spec, retry"
    on_generation_failure: "Try alternative configurations"
    on_compilation_failure: "Adjust spec to fix type issues"
    timeout_seconds: 300
  ```
- **Description**: Retry strategies and failure handling.

**Common Fields**:
- `max_retries`: Maximum iteration attempts (for `iterative` mode)
- `timeout_seconds`: Maximum execution time
- `on_<error_type>_failure`: Strategy for specific error types
- `backoff_strategy`: `exponential`, `linear`, `constant`
- `retry_delay_seconds`: Base delay between retries

---

#### `output`
- **Type**: `object`
- **Default**: `{}`
- **Example**:
  ```yaml
  output:
    success:
      - OpenAPI spec (validated)
      - Generated models (compiled)
      - Validation report
      - Dependency graph
    failure:
      - Error analysis
      - Partial spec
      - Suggested fixes
      - Validation errors
  ```
- **Description**: Expected artifacts and reports for success and failure cases.

**Best Practices**:
- List artifacts in order of importance
- Specify format or state in parentheses
- Include both success and failure outputs
- Mention partial results in failure case
- Reference specific file types or formats

---

#### `tags`
- **Type**: `array[string]`
- **Default**: `[]`
- **Example**: `["api", "design", "openapi", "zalando"]`
- **Description**: Categorization tags for discovery and organization.

**Common Tags**:
- **Domain**: `api`, `data`, `compliance`, `security`
- **Action**: `design`, `validate`, `generate`, `analyze`, `migrate`
- **Technology**: `openapi`, `asyncapi`, `graphql`, `grpc`
- **Standard**: `zalando`, `google`, `restful`, `jsonapi`

---

#### `dependencies`
- **Type**: `array[string]`
- **Default**: `[]`
- **Example**: `["context.schema", "api.guidelines.zalando"]`
- **Description**: Other agents, schemas, or resources this agent depends on.

**Validation Rules**:
- No circular dependencies
- Dependencies must exist in registry
- Agent cannot depend on itself

---

## Validation Rules

### 1. Name Validation
```python
import re

def validate_agent_name(name: str) -> bool:
    """Agent name must match pattern."""
    pattern = r'^[a-z][a-z0-9._-]*$'
    return bool(re.match(pattern, name))

# Valid: api.designer, compliance.checker, data-migrator
# Invalid: ApiDesigner, 1agent, agent_name, AGENT
```

### 2. Version Validation
```python
import re

def validate_version(version: str) -> bool:
    """Version must follow semantic versioning."""
    pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$'
    return bool(re.match(pattern, version))

# Valid: 0.1.0, 1.0.0, 2.3.1-beta, 1.0.0-rc.1
# Invalid: 1.0, v1.0.0, 1.0.0.0
```

### 3. Skills Validation
```python
def validate_skills(skills: list, skill_registry: dict) -> tuple[bool, str]:
    """All skills must exist in registry."""
    if not skills:
        return False, "At least one skill required"

    for skill in skills:
        if skill not in skill_registry:
            return False, f"Skill '{skill}' not found in registry"

    return True, "All skills valid"
```

### 4. Required Fields Check
```python
REQUIRED_FIELDS = [
    "name",
    "version",
    "description",
    "capabilities",
    "skills_available",
    "reasoning_mode"
]

def validate_required_fields(manifest: dict) -> tuple[bool, list]:
    """Check all required fields are present."""
    missing = [field for field in REQUIRED_FIELDS if field not in manifest]
    return len(missing) == 0, missing
```

---

## Agent Registry

Agents are registered in `/registry/agents.json` (similar to skills registry):

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
      "skills_available": [
        "api.define",
        "api.validate",
        "api.generate-models"
      ],
      "status": "draft",
      "dependencies": ["context.schema"],
      "tags": ["api", "design", "openapi"]
    }
  ]
}
```

---

## Best Practices

### 1. Agent Naming
- Use dot notation: `<domain>.<action>`
- Keep names concise and descriptive
- Examples: `api.designer`, `compliance.auditor`, `code.refactor`

### 2. Reasoning Mode Selection
- **Use `iterative`** for:
  - Validation and refinement loops
  - Tasks that benefit from error feedback
  - Complex multi-step processes with uncertain outcomes

- **Use `oneshot`** for:
  - Deterministic transformations
  - Analysis and reporting
  - Tasks where retry doesn't help

### 3. Capabilities vs Skills
- **Capabilities**: What the agent can accomplish (user-facing)
- **Skills**: How the agent accomplishes it (implementation)

Example:
```yaml
capabilities:
  - "Design RESTful APIs following Zalando guidelines"  # What

skills_available:
  - api.define       # How
  - api.validate     # How
```

### 4. Error Handling
- Always define `max_retries` for `iterative` agents
- Set reasonable timeouts (consider skill execution times)
- Provide specific strategies for known error types
- Include fallback behaviors

### 5. Documentation
- Use `workflow_pattern` to explain reasoning process
- Use `example_task` to show realistic usage
- Keep `description` concise but informative
- Add tags for discoverability

---

## Examples

### Example 1: Iterative Refinement Agent

```yaml
name: api.designer
version: 0.1.0
description: "Design and refine OpenAPI specs until they pass validation"
reasoning_mode: iterative

capabilities:
  - Design RESTful APIs from requirements
  - Apply enterprise API guidelines
  - Iteratively refine based on validation feedback

skills_available:
  - api.define
  - api.validate

error_handling:
  max_retries: 3
  on_validation_failure: "Analyze errors and refine spec"
  timeout_seconds: 180

status: active
```

### Example 2: One-Shot Analysis Agent

```yaml
name: api.compatibility
version: 1.0.0
description: "Analyze API changes for backward compatibility"
reasoning_mode: oneshot

capabilities:
  - Detect breaking changes between API versions
  - Generate compatibility reports
  - Suggest migration paths

skills_available:
  - api.diff
  - api.compatibility

output:
  success:
    - Compatibility report
    - Breaking changes list
    - Migration recommendations
  failure:
    - Error analysis
    - Partial comparison results

status: active
```

### Example 3: Multi-Domain Agent

```yaml
name: compliance.auditor
version: 0.2.0
description: "Audit code, APIs, and infrastructure for compliance"
reasoning_mode: iterative

capabilities:
  - Audit API specs for compliance violations
  - Check code for security vulnerabilities
  - Validate infrastructure configurations
  - Generate compliance reports

skills_available:
  - api.validate
  - code.scan
  - policy.validate
  - audit.report

context_requirements:
  policy_set: string       # gdpr, hipaa, sox, pci-dss
  severity_threshold: string  # critical, high, medium, low

error_handling:
  max_retries: 2
  timeout_seconds: 600
  on_policy_violation: "Document and continue audit"

tags:
  - compliance
  - security
  - audit
  - governance

status: active
```

---

## See Also

- [Betty Architecture](./betty-architecture.md) - Five-layer architecture overview
- [Skills Framework](./skills-framework.md) - Complete skill taxonomy
- [API-Driven Development](./api-driven-development.md) - API-first workflow example
