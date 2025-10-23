# api.analyzer Agent

## Purpose

**api.analyzer** is a specialized agent that analyzes API specifications for backward compatibility and breaking changes between versions.

This agent provides detailed compatibility reports, identifies breaking vs non-breaking changes, and suggests migration paths for consumers when breaking changes are unavoidable.

## Behavior

- **Reasoning Mode**: `oneshot` – The agent executes once without retries, as compatibility analysis is deterministic
- **Capabilities**:
  - Detect breaking changes between API versions
  - Generate detailed compatibility reports
  - Identify removed or modified endpoints
  - Suggest migration paths for breaking changes
  - Validate API evolution best practices

## Skills Used

The agent has access to the following skills:

| Skill | Purpose |
|-------|---------|
| `api.compatibility` | Compares two API spec versions and detects breaking changes |
| `api.validate` | Validates individual specs for well-formedness |

## Workflow Pattern

The agent follows this straightforward pattern:

```
1. Load old and new API specifications
2. Run comprehensive compatibility analysis
3. Categorize changes as breaking or non-breaking
4. Generate detailed report with migration recommendations
5. Return results (no retry needed)
```

## Manifest Fields (Quick Reference)

```yaml
name: api.analyzer
version: 0.1.0
reasoning_mode: oneshot
skills_available:
  - api.compatibility
  - api.validate
status: draft
```

## Usage

This agent is invoked through a command or workflow:

### Via Slash Command

```bash
# Assuming /api-compatibility command is registered to use this agent
/api-compatibility specs/user-service-v1.yaml specs/user-service-v2.yaml
```

### Via Workflow

Include the agent in a workflow YAML:

```yaml
# workflows/check_api_compatibility.yaml
steps:
  - agent: api.analyzer
    input:
      old_spec_path: "specs/user-service-v1.0.0.yaml"
      new_spec_path: "specs/user-service-v2.0.0.yaml"
      fail_on_breaking: true
```

## Context Requirements

The agent expects the following context:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `old_spec_path` | string | Path to the previous/old API specification | `"specs/api-v1.0.0.yaml"` |
| `new_spec_path` | string | Path to the new/updated API specification | `"specs/api-v2.0.0.yaml"` |
| `fail_on_breaking` | boolean | Whether to fail (exit non-zero) if breaking changes detected | `true` or `false` |

## Example Task

**Input**:
```
"Compare user-service v1.0.0 with v2.0.0 for breaking changes"
```

**Agent execution**:

1. **Load both specifications**:
   - Old: `specs/user-service-v1.0.0.openapi.yaml`
   - New: `specs/user-service-v2.0.0.openapi.yaml`

2. **Analyze endpoint changes**:
   - ✅ **Added**: `GET /users/{id}/preferences` (non-breaking)
   - ❌ **Removed**: `DELETE /users/{id}/avatar` (breaking)
   - ⚠️ **Modified**: `POST /users` now requires additional field `email_verified` (breaking)

3. **Check for breaking schema changes**:
   - ❌ Removed property: `User.phoneNumber` (breaking)
   - ✅ Added optional property: `User.preferences` (non-breaking)
   - ❌ Changed property type: `User.age` from `integer` to `string` (breaking)

4. **Identify parameter or response format changes**:
   - ❌ Query parameter `filter` changed from optional to required in `GET /users` (breaking)
   - ✅ Response includes new optional field `User.last_login` (non-breaking)

5. **Generate compatibility report**:
   ```json
   {
     "compatible": false,
     "breaking_changes": [
       {
         "type": "endpoint_removed",
         "endpoint": "DELETE /users/{id}/avatar",
         "severity": "high",
         "migration": "Use PUT /users/{id} with avatar=null instead"
       },
       {
         "type": "required_field_added",
         "location": "POST /users request body",
         "field": "email_verified",
         "severity": "high",
         "migration": "Clients must now provide email_verified field"
       },
       {
         "type": "property_removed",
         "schema": "User",
         "property": "phoneNumber",
         "severity": "medium",
         "migration": "Use new phone_contacts array instead"
       },
       {
         "type": "type_changed",
         "schema": "User",
         "property": "age",
         "old_type": "integer",
         "new_type": "string",
         "severity": "high",
         "migration": "Convert age to string format"
       }
     ],
     "non_breaking_changes": [
       {
         "type": "endpoint_added",
         "endpoint": "GET /users/{id}/preferences"
       },
       {
         "type": "optional_field_added",
         "schema": "User",
         "property": "preferences"
       },
       {
         "type": "response_field_added",
         "endpoint": "GET /users/{id}",
         "field": "last_login"
       }
     ],
     "change_summary": {
       "breaking": 4,
       "additions": 2,
       "modifications": 2,
       "removals": 2
     }
   }
   ```

6. **Provide migration recommendations**:
   ```markdown
   ## Migration Guide: v1.0.0 → v2.0.0

   ### Breaking Changes

   1. **Removed endpoint: DELETE /users/{id}/avatar**
      - **Impact**: High - Clients using this endpoint will fail
      - **Migration**: Use PUT /users/{id} with avatar=null instead
      - **Effort**: Low

   2. **New required field: email_verified in POST /users**
      - **Impact**: High - All user creation requests must include this field
      - **Migration**: Update client code to provide email_verified boolean
      - **Effort**: Medium

   3. **Property removed: User.phoneNumber**
      - **Impact**: Medium - Clients reading this field will get undefined
      - **Migration**: Use User.phone_contacts array instead
      - **Effort**: Medium

   4. **Type changed: User.age (integer → string)**
      - **Impact**: High - Type mismatch will cause deserialization errors
      - **Migration**: Update models to use string type and convert existing data
      - **Effort**: High

   ### Recommended Approach
   1. Implement migration layer for 2 versions
   2. Communicate breaking changes to consumers 30 days in advance
   3. Provide backward-compatible endpoints during transition period
   4. Monitor usage of deprecated endpoints
   ```

## Error Handling

| Scenario | Timeout | Behavior |
|----------|---------|----------|
| Spec load failure | N/A | Return error with file path details |
| Comparison failure | N/A | Return partial analysis with error context |
| Timeout | 120 seconds | Fails after 2 minutes |

### On Success

```json
{
  "status": "success",
  "outputs": {
    "compatibility_report": {
      "compatible": false,
      "breaking_changes": [...],
      "non_breaking_changes": [...],
      "change_summary": {...}
    },
    "migration_recommendations": "...",
    "api_diff_visualization": "..."
  }
}
```

### On Failure

```json
{
  "status": "failed",
  "error_details": {
    "error": "Failed to load old spec",
    "file_path": "specs/user-service-v1.0.0.yaml",
    "details": "File not found"
  },
  "partial_analysis": null,
  "suggested_fixes": [
    "Verify file path exists",
    "Check file permissions"
  ]
}
```

## Use Cases

### 1. Pre-Release Validation

Run before releasing a new API version to ensure backward compatibility:

```yaml
# workflows/validate_release.yaml
steps:
  - agent: api.analyzer
    input:
      old_spec_path: "specs/production/api-v1.yaml"
      new_spec_path: "specs/staging/api-v2.yaml"
      fail_on_breaking: true
```

### 2. Continuous Integration

Integrate into CI/CD to prevent accidental breaking changes:

```yaml
# .github/workflows/api-check.yml
- name: Check API Compatibility
  run: |
    # Agent runs via workflow.compose
    python skills/workflow.compose/workflow_compose.py \
      workflows/check_api_compatibility.yaml
```

### 3. Documentation Generation

Generate migration guides automatically:

```bash
# Use agent output to create migration documentation
/api-compatibility old.yaml new.yaml > migration-guide.md
```

## Status

**Draft** – This agent is under development and not yet marked active in the registry.

## Related Documentation

- [Agents Overview](../../docs/betty-architecture.md#layer-2-agents-reasoning-layer) – Understanding agents in Betty's architecture
- [Agent Schema Reference](../../docs/agent-schema-reference.md) – Agent manifest fields and structure
- [api.compatibility SKILL.md](../../skills/api.compatibility/SKILL.md) – Underlying compatibility check skill
- [API-Driven Development](../../docs/api-driven-development.md) – Full API workflow including compatibility checks

## Version History

- **0.1.0** (Oct 2025) – Initial draft implementation with oneshot analysis pattern
