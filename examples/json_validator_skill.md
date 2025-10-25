# Name: data.validatejson

# Purpose:
Validates JSON files against JSON Schema definitions. Checks syntax, structure, and conformance to schema specifications.

# Inputs:
- json_file_path
- schema_file_path (optional)

# Outputs:
- validation_result.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- validation-report

# Implementation Notes:
Use Python's jsonschema library for validation. Support both inline schemas and external schema files. Provide detailed error messages for validation failures.

# Examples:
- Validate API response against OpenAPI schema
- Validate configuration file against JSON Schema
- Check JSON syntax and structure
