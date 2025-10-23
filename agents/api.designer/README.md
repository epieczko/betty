# api.designer Agent

## Purpose

**api.designer** is an intelligent agent that orchestrates the API design process from natural language requirements to validated, production-ready OpenAPI specifications with generated models.

This agent uses iterative refinement to create APIs that comply with enterprise guidelines (Zalando by default), automatically fixing validation errors and ensuring best practices.

## Behavior

- **Reasoning Mode**: `iterative` – The agent retries on validation failures, refining the spec until it passes all checks
- **Capabilities**:
  - Design RESTful APIs from natural language requirements
  - Apply Zalando guidelines automatically (or other guideline sets)
  - Generate OpenAPI 3.1 specs with best practices
  - Iteratively refine based on validation feedback
  - Handle AsyncAPI for event-driven architectures

## Skills Used

The agent has access to the following skills and uses them in sequence:

| Skill | Purpose |
|-------|---------|
| `api.define` | Scaffolds initial OpenAPI spec from service name and requirements |
| `api.validate` | Validates spec against enterprise guidelines (Zalando, Google, Microsoft) |
| `api.generate-models` | Generates type-safe models in target languages (TypeScript, Python, etc.) |
| `api.compatibility` | Checks for breaking changes when updating existing APIs |

## Workflow Pattern

The agent follows this iterative pattern:

```
1. Analyze requirements and domain context
2. Draft OpenAPI spec following guidelines
3. Run validation (api.validate)
4. If validation fails:
   - Analyze errors
   - Refine spec
   - Re-validate
   - Repeat until passing (max 3 retries)
5. Generate models for target languages
6. Verify generated models compile
```

## Manifest Fields (Quick Reference)

```yaml
name: api.designer
version: 0.1.0
reasoning_mode: iterative
skills_available:
  - api.define
  - api.validate
  - api.generate-models
  - api.compatibility
status: draft
```

## Usage

This agent is invoked through a command or workflow:

### Via Slash Command

```bash
# Assuming /api-design command is registered to use this agent
/api-design user-service
```

The command passes the service name to the agent, which then:
1. Uses `api.define` to create initial spec
2. Validates with `api.validate`
3. Fixes any validation errors iteratively
4. Generates models with `api.generate-models`

### Via Workflow

Include the agent in a workflow YAML:

```yaml
# workflows/design_api.yaml
steps:
  - agent: api.designer
    input:
      service_name: "user-service"
      guidelines: "zalando"
      languages: ["typescript", "python"]
```

## Context Requirements

The agent expects the following context:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `guidelines` | string | Which API guidelines to follow | `"zalando"`, `"google"`, `"microsoft"` |
| `domain` | string | Business domain for API design | `"user-management"`, `"e-commerce"` |
| `existing_apis` | list | Related APIs to maintain consistency with | `["auth-service", "notification-service"]` |
| `strict_mode` | boolean | Whether to treat warnings as errors | `true` or `false` |

## Example Task

**Input**:
```
"Create API for user management with CRUD operations,
 authentication via JWT, and email verification workflow"
```

**Agent execution**:

1. **Draft OpenAPI spec** with proper resource paths:
   - `POST /users` - Create user
   - `GET /users/{id}` - Get user
   - `PUT /users/{id}` - Update user
   - `DELETE /users/{id}` - Delete user
   - `POST /users/{id}/verify-email` - Email verification

2. **Apply Zalando guidelines**:
   - Use snake_case for property names
   - Include problem JSON error responses
   - Add required headers (X-Request-ID, etc.)
   - Define proper HTTP status codes

3. **Validate spec** using `api.validate`:
   ```bash
   python skills/api.validate/api_validate.py specs/user-service.yaml zalando
   ```

4. **Fix validation issues** (if any):
   - Missing required headers → Add to spec
   - Incorrect naming → Convert to snake_case
   - Missing error schemas → Add problem JSON schemas

5. **Generate models** using Modelina:
   ```bash
   python skills/api.generate-models/modelina_generate.py \
     specs/user-service.yaml typescript src/models/typescript
   python skills/api.generate-models/modelina_generate.py \
     specs/user-service.yaml python src/models/python
   ```

6. **Verify models compile**:
   - TypeScript: `tsc --noEmit`
   - Python: `mypy --strict`

## Error Handling

| Scenario | Max Retries | Behavior |
|----------|-------------|----------|
| Validation failure | 3 | Analyze errors, refine spec, retry |
| Model generation failure | 3 | Try alternative Modelina configurations |
| Compilation failure | 3 | Adjust spec to fix type issues |
| Timeout | N/A | Fails after 300 seconds (5 minutes) |

### On Success

```json
{
  "status": "success",
  "outputs": {
    "spec_path": "specs/user-service.openapi.yaml",
    "validation_report": {
      "valid": true,
      "errors": [],
      "warnings": []
    },
    "generated_models": {
      "typescript": ["src/models/typescript/User.ts", "src/models/typescript/UserResponse.ts"],
      "python": ["src/models/python/user.py", "src/models/python/user_response.py"]
    },
    "dependency_graph": "..."
  }
}
```

### On Failure

```json
{
  "status": "failed",
  "error_analysis": {
    "step": "validation",
    "attempts": 3,
    "last_error": "Missing required header: X-Request-ID in all endpoints"
  },
  "partial_spec": "specs/user-service.openapi.yaml",
  "suggested_fixes": [
    "Add X-Request-ID header to all operations",
    "See Zalando guidelines: https://..."
  ]
}
```

## Status

**Draft** – This agent is under development and not yet marked active in the registry. Current goals for next version:

- [ ] Improve prompt engineering for better initial API designs
- [ ] Add more robust error handling for iterative loops
- [ ] Support for more guideline sets (Google, Microsoft)
- [ ] Better context injection from existing APIs
- [ ] Automatic testing of generated models

## Related Documentation

- [Agents Overview](../../docs/betty-architecture.md#layer-2-agents-reasoning-layer) – Understanding agents in Betty's architecture
- [Agent Schema Reference](../../docs/agent-schema-reference.md) – Agent manifest fields and structure
- [API-Driven Development](../../docs/api-driven-development.md) – Full API design workflow using Betty
- [api.define SKILL.md](../../skills/api.define/SKILL.md) – Skill for creating API specs
- [api.validate SKILL.md](../../skills/api.validate/SKILL.md) – Skill for validating specs
- [api.generate-models SKILL.md](../../skills/api.generate-models/SKILL.md) – Skill for generating models

## Version History

- **0.1.0** (Oct 2025) – Initial draft implementation with iterative refinement pattern
