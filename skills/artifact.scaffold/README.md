# artifact.scaffold

Generate new artifact templates automatically from metadata inputs.

## Overview

The `artifact.scaffold` skill creates fully compliant artifact descriptors in one call. It generates valid `.artifact.yaml` files, assigns auto-incremented versions starting at 0.1.0, and registers artifacts in the artifacts registry.

## Features

- **Automatic Generation**: Creates artifact YAML files from metadata inputs
- **Schema Definition**: Supports field definitions with types, descriptions, and required flags
- **Inheritance**: Supports extending from base artifacts
- **Registry Management**: Automatically registers artifacts in `registry/artifacts.json`
- **Validation**: Optional `--validate` flag to validate generated artifacts
- **Version Management**: Auto-assigns version 0.1.0 to new artifacts

## Usage

### Basic Example

```bash
python3 skills/artifact.scaffold/artifact_scaffold.py \
  --id "new.artifact" \
  --category "report"
```

### With Field Definitions

```bash
python3 skills/artifact.scaffold/artifact_scaffold.py \
  --id "new.artifact" \
  --category "report" \
  --fields '[{"name":"summary","type":"string","description":"Summary field","required":true}]'
```

### With Inheritance and Validation

```bash
python3 skills/artifact.scaffold/artifact_scaffold.py \
  --id "new.artifact" \
  --category "report" \
  --extends "base.artifact" \
  --fields '[{"name":"summary","type":"string"}]' \
  --validate
```

### Custom Output Path

```bash
python3 skills/artifact.scaffold/artifact_scaffold.py \
  --id "new.artifact" \
  --category "report" \
  --output "custom/path/artifact.yaml"
```

## Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `--id` | string | Yes | Unique identifier for the artifact (e.g., "new.artifact") |
| `--category` | string | Yes | Category/type of artifact (e.g., "report", "specification") |
| `--extends` | string | No | Base artifact to extend from |
| `--fields` | JSON array | No | Field definitions with name, type, description, and required properties |
| `--output` | string | No | Custom output path for the artifact file |
| `--validate` | flag | No | Validate the artifact after generation |

## Field Definition Format

Fields are provided as a JSON array with the following structure:

```json
[
  {
    "name": "field_name",
    "type": "string|number|boolean|object|array",
    "description": "Field description",
    "required": true|false
  }
]
```

## Output

The skill outputs a JSON response with the following structure:

```json
{
  "ok": true,
  "status": "success",
  "artifact_id": "new.artifact",
  "file_path": "/path/to/artifact.yaml",
  "version": "0.1.0",
  "category": "report",
  "registry_path": "/path/to/registry/artifacts.json",
  "artifacts_registered": 1,
  "validation": {
    "valid": true,
    "errors": [],
    "warnings": []
  }
}
```

## Generated Artifact Structure

The skill generates artifact YAML files with the following structure:

```yaml
id: new.artifact
version: 0.1.0
category: report
created_at: '2025-10-26T00:00:00.000000Z'
metadata:
  description: new.artifact artifact
  tags:
  - report
extends: base.artifact  # Optional
schema:
  type: object
  properties:
    summary:
      type: string
      description: Summary field
  required:
  - summary
```

## Registry Management

Artifacts are automatically registered in `registry/artifacts.json`:

```json
{
  "registry_version": "1.0.0",
  "generated_at": "2025-10-26T00:00:00.000000Z",
  "artifacts": [
    {
      "id": "new.artifact",
      "version": "0.1.0",
      "category": "report",
      "created_at": "2025-10-26T00:00:00.000000Z",
      "description": "new.artifact artifact",
      "tags": ["report"],
      "extends": "base.artifact",
      "schema": { ... }
    }
  ]
}
```

## Dependencies

- `artifact.define`: For artifact type definitions and validation

## Status

**Active** - Ready for production use

## Tags

- artifacts
- scaffolding
- generation
- templates
- metadata
