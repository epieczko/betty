# Name: data.transform

# Purpose:
Transform data between different formats (JSON, YAML, XML, CSV) with validation and error handling

# Inputs:
- input_file_path
- source_format
- target_format
- schema_path (optional)

# Outputs:
- transformed_file
- transformation_report.json

# Permissions:
- filesystem:read
- filesystem:write

# Produces Artifacts:
- transformed-data
- transformation-report

# Implementation Notes:
Support transformations between:
- JSON ↔ YAML
- JSON ↔ XML
- JSON ↔ CSV
- YAML ↔ XML
- XML ↔ CSV

Features:
- Validate input against schema before transformation
- Preserve data types during conversion
- Handle nested structures appropriately
- Report data loss warnings (e.g., CSV can't represent nesting)
- Support custom transformation rules
- Provide detailed error messages

Output report should include:
- Transformation success status
- Source and target formats
- Data validation results
- Warnings about potential data loss
- Transformation time and file sizes
