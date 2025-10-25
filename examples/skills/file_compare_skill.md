# Name: file.compare

# Purpose:
Compare two files and generate detailed diff reports showing line-by-line differences

# Inputs:
- file_path_1
- file_path_2
- output_format (optional)

# Outputs:
- diff_report.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- diff-report

# Implementation Notes:
Use Python's difflib to compare files line by line.
Support multiple output formats:
- unified: Standard unified diff format
- context: Context diff format
- html: HTML diff with color coding
- json: Structured JSON with line-by-line changes

Include statistics:
- Total lines added
- Total lines removed
- Total lines modified
- Percentage similarity

Handle binary files by detecting and reporting as non-text.
