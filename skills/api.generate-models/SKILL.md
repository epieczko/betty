# api.generate-models

## Overview

**api.generate-models** generates type-safe models from OpenAPI and AsyncAPI specifications, enabling shared models between frontend and backend using code generation.

## Purpose

Transform API specifications into type-safe code:
- Generate TypeScript interfaces from OpenAPI schemas
- Generate Python dataclasses/Pydantic models
- Generate Java classes, Go structs, C# classes
- Single source of truth: the API specification
- Automatic synchronization when specs change

## Usage

### Basic Usage

```bash
python skills/api.generate-models/modelina_generate.py <spec_path> <language> [options]
```

### Parameters

| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `spec_path` | Yes | Path to API spec file | - |
| `language` | Yes | Target language | - |
| `--output-dir` | No | Output directory | `src/models` |
| `--package-name` | No | Package/module name | - |

### Supported Languages

| Language | Extension | Status |
|----------|-----------|--------|
| `typescript` | `.ts` | ✅ Supported |
| `python` | `.py` | ✅ Supported |
| `java` | `.java` | 🚧 Planned |
| `go` | `.go` | 🚧 Planned |
| `csharp` | `.cs` | 🚧 Planned |
| `rust` | `.rs` | 🚧 Planned |

## Examples

### Example 1: Generate TypeScript Models

```bash
python skills/api.generate-models/modelina_generate.py \
  specs/user-service.openapi.yaml \
  typescript \
  --output-dir=src/models/user-service
```

**Generated files**:
```
src/models/user-service/
├── User.ts
├── UserCreate.ts
├── UserUpdate.ts
├── Pagination.ts
└── Problem.ts
```

**Example TypeScript output**:
```typescript
// src/models/user-service/User.ts
export interface User {
  /** Unique identifier */
  user_id: string;
  /** Creation timestamp */
  created_at: string;
  /** Last update timestamp */
  updated_at?: string;
}

// src/models/user-service/Pagination.ts
export interface Pagination {
  /** Number of items per page */
  limit: number;
  /** Number of items skipped */
  offset: number;
  /** Total number of items available */
  total: number;
}
```

### Example 2: Generate Python Models

```bash
python skills/api.generate-models/modelina_generate.py \
  specs/user-service.openapi.yaml \
  python \
  --output-dir=src/models/user_service
```

**Generated files**:
```
src/models/user_service/
└── models.py
```

**Example Python output**:
```python
# src/models/user_service/models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class User(BaseModel):
    """User model"""
    user_id: UUID = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

class Pagination(BaseModel):
    """Pagination metadata"""
    limit: int = Field(..., description="Number of items per page")
    offset: int = Field(..., description="Number of items skipped")
    total: int = Field(..., description="Total number of items available")
```

### Example 3: Generate for Multiple Languages

```bash
# TypeScript for frontend
python skills/api.generate-models/modelina_generate.py \
  specs/user-service.openapi.yaml \
  typescript \
  --output-dir=frontend/src/models

# Python for backend
python skills/api.generate-models/modelina_generate.py \
  specs/user-service.openapi.yaml \
  python \
  --output-dir=backend/app/models
```

## Code Generators Used

The skill uses multiple code generation approaches:

### 1. datamodel-code-generator (Primary)

**Best for**: OpenAPI specs → Python/TypeScript
**Installation**: `pip install datamodel-code-generator`

Generates:
- Python: Pydantic v2 models with type hints
- TypeScript: Type-safe interfaces
- Validates schema during generation

### 2. Simple Built-in Generator (Fallback)

**Best for**: Basic models when external tools not available
**Installation**: None required

Generates:
- Python: dataclasses
- TypeScript: interfaces
- Basic but reliable

### 3. Modelina (Future)

**Best for**: AsyncAPI specs, multiple languages
**Installation**: `npm install -g @asyncapi/modelina`
**Status**: Planned

## Output

### Success Response

```json
{
  "status": "success",
  "data": {
    "models_path": "src/models/user-service",
    "files_generated": [
      "src/models/user-service/User.ts",
      "src/models/user-service/UserCreate.ts",
      "src/models/user-service/Pagination.ts",
      "src/models/user-service/Problem.ts"
    ],
    "model_count": 4,
    "generator_used": "datamodel-code-generator"
  }
}
```

## Integration with Workflows

```yaml
# workflows/api_first_development.yaml
steps:
  - skill: api.define
    args:
      - "user-service"
      - "openapi"
    output: spec_path

  - skill: api.validate
    args:
      - "{spec_path}"
      - "zalando"
    required: true

  - skill: api.generate-models
    args:
      - "{spec_path}"
      - "typescript"
      - "--output-dir=frontend/src/models"

  - skill: api.generate-models
    args:
      - "{spec_path}"
      - "python"
      - "--output-dir=backend/app/models"
```

## Integration with Hooks

Auto-regenerate models when specs change:

```bash
python skills/hook.define/hook_define.py \
  on_file_save \
  "python betty/skills/api.generate-models/modelina_generate.py {file_path} typescript --output-dir=src/models" \
  --pattern="specs/*.openapi.yaml" \
  --blocking=false \
  --description="Auto-regenerate TypeScript models when OpenAPI specs change"
```

## Benefits

### For Developers
- ✅ **Type safety**: Catch errors at compile time, not runtime
- ✅ **IDE autocomplete**: Full IntelliSense/autocomplete support
- ✅ **No manual typing**: Models generated automatically
- ✅ **Always in sync**: Regenerate when spec changes

### For Teams
- ✅ **Single source of truth**: API spec defines types
- ✅ **Frontend/backend alignment**: Same types everywhere
- ✅ **Reduced errors**: Type mismatches caught early
- ✅ **Faster development**: No manual model creation

### For Organizations
- ✅ **Consistency**: All services use same model generation
- ✅ **Maintainability**: Update spec → regenerate → done
- ✅ **Documentation**: Types are self-documenting
- ✅ **Quality**: Generated code is tested and reliable

## Dependencies

### Required
- **PyYAML**: For YAML parsing (`pip install pyyaml`)

### Optional (Better Output)
- **datamodel-code-generator**: For high-quality Python/TypeScript (`pip install datamodel-code-generator`)
- **Node.js + Modelina**: For AsyncAPI and more languages (`npm install -g @asyncapi/modelina`)

## Examples with Real Specs

Using the user-service spec from Phase 1:

```bash
# Generate TypeScript
python skills/api.generate-models/modelina_generate.py \
  specs/user-service.openapi.yaml \
  typescript

# Output:
{
  "status": "success",
  "data": {
    "models_path": "src/models",
    "files_generated": [
      "src/models/User.ts",
      "src/models/UserCreate.ts",
      "src/models/UserUpdate.ts",
      "src/models/Pagination.ts",
      "src/models/Problem.ts"
    ],
    "model_count": 5
  }
}
```

## See Also

- [api.define](../api.define/SKILL.md) - Create OpenAPI specs
- [api.validate](../api.validate/SKILL.md) - Validate specs
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [API-Driven Development](../../docs/api-driven-development.md) - Complete guide

## Version

**0.1.0** - Initial implementation with TypeScript and Python support
