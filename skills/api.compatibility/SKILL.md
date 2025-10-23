# api.compatibility

## Overview

Detect breaking changes between API specification versions to maintain backward compatibility.

## Usage

```bash
python skills/api.compatibility/check_compatibility.py <old_spec> <new_spec> [options]
```

## Examples

```bash
# Check compatibility
python skills/api.compatibility/check_compatibility.py \
  specs/user-service-v1.openapi.yaml \
  specs/user-service-v2.openapi.yaml

# Human-readable output
python skills/api.compatibility/check_compatibility.py \
  specs/user-service-v1.openapi.yaml \
  specs/user-service-v2.openapi.yaml \
  --format=human
```

## Breaking Changes Detected

- **path_removed**: Endpoint removed
- **operation_removed**: HTTP method removed
- **schema_removed**: Model schema removed
- **property_removed**: Schema property removed
- **property_made_required**: Optional property now required
- **property_type_changed**: Property type changed

## Non-Breaking Changes

- **path_added**: New endpoint
- **operation_added**: New HTTP method
- **schema_added**: New model schema
- **property_added**: New optional property

## Version

**0.1.0** - Initial implementation
