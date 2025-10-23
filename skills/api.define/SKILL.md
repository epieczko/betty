# api.define

## Overview

**api.define** scaffolds OpenAPI and AsyncAPI specifications from enterprise-compliant templates, generating production-ready API contracts with best practices built-in.

## Purpose

Quickly create API specifications that follow enterprise guidelines:
- Generate Zalando-compliant OpenAPI 3.1 specs
- Generate AsyncAPI 3.0 specs for event-driven APIs
- Include proper error handling (RFC 7807 Problem JSON)
- Use correct naming conventions (snake_case)
- Include required metadata and security schemes

## Usage

### Basic Usage

```bash
python skills/api.define/api_define.py <service_name> [spec_type] [options]
```

### Parameters

| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `service_name` | Yes | Service/API name | - |
| `spec_type` | No | openapi or asyncapi | `openapi` |
| `--template` | No | Template name | `zalando` |
| `--output-dir` | No | Output directory | `specs` |
| `--version` | No | API version | `1.0.0` |

## Examples

### Example 1: Create Zalando-Compliant OpenAPI Spec

```bash
python skills/api.define/api_define.py user-service openapi --template=zalando
```

**Output**: `specs/user-service.openapi.yaml`

Generated spec includes:
- ✅ Required Zalando metadata (`x-api-id`, `x-audience`)
- ✅ CRUD operations for users resource
- ✅ RFC 7807 Problem JSON for errors
- ✅ snake_case property names
- ✅ X-Flow-ID headers for tracing
- ✅ Proper HTTP status codes
- ✅ JWT authentication scheme

### Example 2: Create AsyncAPI Spec

```bash
python skills/api.define/api_define.py user-service asyncapi
```

**Output**: `specs/user-service.asyncapi.yaml`

Generated spec includes:
- ✅ Lifecycle events (created, updated, deleted)
- ✅ Kafka channel definitions
- ✅ Event payload schemas
- ✅ Publish/subscribe operations

### Example 3: Custom Output Directory

```bash
python skills/api.define/api_define.py order-api openapi \
  --output-dir=api-specs \
  --version=2.0.0
```

## Generated OpenAPI Structure

For a service named `user-service`, the generated OpenAPI spec includes:

**Paths**:
- `GET /users` - List users with pagination
- `POST /users` - Create new user
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

**Schemas**:
- `User` - Main resource schema
- `UserCreate` - Creation payload schema
- `UserUpdate` - Update payload schema
- `Pagination` - Pagination metadata
- `Problem` - RFC 7807 error schema

**Responses**:
- `200` - Success (with X-Flow-ID header)
- `201` - Created (with Location and X-Flow-ID headers)
- `204` - No Content (for deletes)
- `400` - Bad Request (application/problem+json)
- `404` - Not Found (application/problem+json)
- `409` - Conflict (application/problem+json)
- `500` - Internal Error (application/problem+json)

**Security**:
- Bearer token authentication (JWT)

**Required Metadata**:
- `x-api-id` - Unique UUID
- `x-audience` - Target audience (company-internal)
- `contact` - Team contact information

## Resource Name Extraction

The skill automatically extracts resource names from service names:

| Service Name | Resource | Plural |
|--------------|----------|--------|
| `user-service` | user | users |
| `order-api` | order | orders |
| `payment-gateway` | payment | payments |

## Naming Conventions

The skill automatically applies proper naming:

| Context | Convention | Example |
|---------|------------|---------|
| Paths | kebab-case | `/user-profiles` |
| Properties | snake_case | `user_id` |
| Schemas | TitleCase | `UserProfile` |
| Operations | camelCase | `getUserById` |

## Integration with api.validate

The generated specs are designed to pass `api.validate` with zero errors:

```bash
# Generate spec
python skills/api.define/api_define.py user-service

# Validate (should pass)
python skills/api.validate/api_validate.py specs/user-service.openapi.yaml zalando
```

## Use in Workflows

```yaml
# workflows/api_first_development.yaml
steps:
  - skill: api.define
    args:
      - "user-service"
      - "openapi"
      - "--template=zalando"
    output: spec_path

  - skill: api.validate
    args:
      - "{spec_path}"
      - "zalando"
    required: true
```

## Customization

After generation, customize the spec:

1. **Add properties** to schemas:
```yaml
User:
  properties:
    user_id: ...
    email:          # Add this
      type: string
      format: email
```

2. **Add operations**:
```yaml
/users/search:      # Add new endpoint
  post:
    summary: Search users
```

3. **Modify metadata**:
```yaml
info:
  contact:
    name: Your Team Name    # Update this
    email: team@company.com
```

## Output

### Success Response

```json
{
  "status": "success",
  "data": {
    "spec_path": "specs/user-service.openapi.yaml",
    "spec_content": {...},
    "api_id": "d0184f38-b98d-11e7-9c56-68f728c1ba70",
    "template_used": "zalando",
    "service_name": "user-service"
  }
}
```

## Dependencies

- **PyYAML**: Required for YAML handling
  ```bash
  pip install pyyaml
  ```

## Templates

| Template | Spec Type | Description |
|----------|-----------|-------------|
| `zalando` | OpenAPI | Zalando-compliant with all required fields |
| `basic` | AsyncAPI | Basic event-driven API structure |

## See Also

- [api.validate](../api.validate/SKILL.md) - Validate generated specs
- [hook.define](../hook.define/SKILL.md) - Set up automatic validation
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [API-Driven Development](../../docs/api-driven-development.md) - Complete guide

## Version

**0.1.0** - Initial implementation with Zalando template support
