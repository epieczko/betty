# api.validate

## Overview

**api.validate** validates OpenAPI and AsyncAPI specifications against enterprise guidelines, with built-in support for Zalando RESTful API Guidelines.

## Purpose

Ensure API specifications meet enterprise standards:
- Validate OpenAPI 3.x specifications
- Validate AsyncAPI 3.x specifications
- Check compliance with Zalando guidelines
- Detect common API design mistakes
- Provide actionable suggestions for fixes

## Usage

### Basic Usage

```bash
python skills/api.validate/api_validate.py <spec_path> [guideline_set] [options]
```

### Parameters

| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `spec_path` | Yes | Path to API spec file | - |
| `guideline_set` | No | Guidelines to validate against | `zalando` |
| `--strict` | No | Warnings become errors | `false` |
| `--format` | No | Output format (json, human) | `json` |

### Guideline Sets

| Guideline | Status | Description |
|-----------|--------|-------------|
| `zalando` | ✅ Supported | Zalando RESTful API Guidelines |
| `google` | 🚧 Planned | Google API Design Guide |
| `microsoft` | 🚧 Planned | Microsoft REST API Guidelines |

## Examples

### Example 1: Validate OpenAPI Spec

```bash
python skills/api.validate/api_validate.py specs/user-service.openapi.yaml zalando
```

**Output** (JSON format):
```json
{
  "status": "success",
  "data": {
    "valid": false,
    "errors": [
      {
        "rule_id": "MUST_001",
        "message": "Missing required field 'info.x-api-id'",
        "severity": "error",
        "path": "info.x-api-id",
        "suggestion": "Add a UUID to uniquely identify this API"
      }
    ],
    "warnings": [
      {
        "rule_id": "SHOULD_001",
        "message": "Missing 'info.contact'",
        "severity": "warning",
        "path": "info.contact"
      }
    ],
    "spec_path": "specs/user-service.openapi.yaml",
    "spec_type": "openapi",
    "guideline_set": "zalando"
  }
}
```

### Example 2: Human-Readable Output

```bash
python skills/api.validate/api_validate.py \
  specs/user-service.openapi.yaml \
  zalando \
  --format=human
```

**Output**:
```
============================================================
API Validation Report
============================================================
Spec: specs/user-service.openapi.yaml
Type: OPENAPI
Guidelines: zalando
============================================================

❌ ERRORS (1):
  [MUST_001] Missing required field 'info.x-api-id'
    Path: info.x-api-id
    💡 Add a UUID to uniquely identify this API

⚠️  WARNINGS (1):
  [SHOULD_001] Missing 'info.contact'
    Path: info.contact
    💡 Add contact information

============================================================
❌ Validation FAILED
============================================================
```

### Example 3: Strict Mode

```bash
python skills/api.validate/api_validate.py \
  specs/user-service.openapi.yaml \
  zalando \
  --strict
```

In strict mode, warnings are treated as errors. Use for CI/CD pipelines where you want zero tolerance for issues.

### Example 4: Validate AsyncAPI Spec

```bash
python skills/api.validate/api_validate.py specs/user-events.asyncapi.yaml
```

## Validation Rules

### Zalando Guidelines (OpenAPI)

#### MUST Rules (Errors)

| Rule | Description | Example Fix |
|------|-------------|-------------|
| **MUST_001** | Required `x-api-id` metadata | `x-api-id: 'd0184f38-b98d-11e7-9c56-68f728c1ba70'` |
| **MUST_002** | Required `x-audience` metadata | `x-audience: 'company-internal'` |
| **MUST_003** | Path naming conventions | Use lowercase kebab-case or snake_case |
| **MUST_004** | Property naming (snake_case) | `userId` → `user_id` |
| **MUST_005** | HTTP method usage | GET should not have requestBody |

#### SHOULD Rules (Warnings)

| Rule | Description | Example Fix |
|------|-------------|-------------|
| **SHOULD_001** | Contact information | Add `info.contact` with team details |
| **SHOULD_002** | POST returns 201 | Add 201 response to POST operations |
| **SHOULD_003** | Document 400 errors | Add 400 Bad Request response |
| **SHOULD_004** | Document 500 errors | Add 500 Internal Error response |
| **SHOULD_005** | 201 includes Location header | Add Location header to 201 responses |
| **SHOULD_006** | Problem schema for errors | Define RFC 7807 Problem schema |
| **SHOULD_007** | Error responses use application/problem+json | Use correct content type |
| **SHOULD_008** | X-Flow-ID header | Add request tracing header |
| **SHOULD_009** | Security schemes defined | Add authentication schemes |

### AsyncAPI Guidelines

| Rule | Description |
|------|-------------|
| **ASYNCAPI_001** | Required `info` field |
| **ASYNCAPI_002** | Required `channels` field |
| **ASYNCAPI_003** | Version check (recommend 3.x) |

## Integration with Hooks

### Automatic Validation on File Edit

```bash
# Create hook using hook.define
python skills/hook.define/hook_define.py \
  on_file_edit \
  "python betty/skills/api.validate/api_validate.py {file_path} zalando" \
  --pattern="*.openapi.yaml" \
  --blocking=true \
  --timeout=10000 \
  --description="Validate OpenAPI specs on edit"
```

**Result**: Every time you edit a `*.openapi.yaml` file, it's automatically validated. If validation fails, the edit is blocked.

### Validation on Commit

```bash
python skills/hook.define/hook_define.py \
  on_commit \
  "python betty/skills/api.validate/api_validate.py {file_path} zalando --strict" \
  --pattern="specs/**/*.yaml" \
  --blocking=true \
  --description="Prevent commits with invalid specs"
```

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Validation passed (no errors) |
| `1` | Validation failed (has errors) or execution error |

## Common Validation Errors

### Missing x-api-id

**Error**:
```
Missing required field 'info.x-api-id'
```

**Fix**:
```yaml
info:
  title: My API
  version: 1.0.0
  x-api-id: d0184f38-b98d-11e7-9c56-68f728c1ba70  # Add this
```

### Wrong Property Naming

**Error**:
```
Property 'userId' should use snake_case
```

**Fix**:
```yaml
# Before
properties:
  userId:
    type: string

# After
properties:
  user_id:
    type: string
```

### Missing Error Responses

**Error**:
```
GET operation should document 400 (Bad Request) response
```

**Fix**:
```yaml
responses:
  '200':
    description: Success
  '400':  # Add this
    $ref: '#/components/responses/BadRequest'
  '500':  # Add this
    $ref: '#/components/responses/InternalError'
```

### Wrong Content Type for Errors

**Error**:
```
Error response 400 should use 'application/problem+json'
```

**Fix**:
```yaml
'400':
  description: Bad request
  content:
    application/problem+json:  # Not application/json
      schema:
        $ref: '#/components/schemas/Problem'
```

## Use in Workflows

```yaml
# workflows/api_validation_suite.yaml
steps:
  - skill: api.validate
    args:
      - "specs/user-service.openapi.yaml"
      - "zalando"
      - "--strict"
    required: true
```

## Dependencies

- **PyYAML**: Required for YAML parsing
  ```bash
  pip install pyyaml
  ```

## Files

### Input
- `*.openapi.yaml` - OpenAPI 3.x specifications
- `*.asyncapi.yaml` - AsyncAPI 3.x specifications
- `*.json` - JSON format specifications

### Output
- JSON validation report (stdout)
- Human-readable report (with `--format=human`)

## See Also

- [hook.define](../hook.define/SKILL.md) - Create validation hooks
- [api.define](../api.define/SKILL.md) - Create OpenAPI specs
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [API-Driven Development](../../docs/api-driven-development.md) - Complete guide
- [Zalando API Guidelines](https://opensource.zalando.com/restful-api-guidelines/)
- [RFC 7807 Problem Details](https://datatracker.ietf.org/doc/html/rfc7807)

## Version

**0.1.0** - Initial implementation with Zalando guidelines support
