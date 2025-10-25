# Name: optimization-report

# Purpose:
Performance and security optimization recommendations for APIs and workflows. Contains actionable suggestions for improving efficiency, security posture, and adherence to best practices.

# Format: JSON

# File Pattern: *.optimization.json

# Content Type: application/json

# Schema Properties:
- optimizations (array): List of optimization recommendations
- severity (string): Overall severity level (low, medium, high, critical)
- categories (array): Categories of optimizations (performance, security, best-practice)
- timestamp (string): When the analysis was performed
- analyzed_artifact (string): Reference to the artifact that was analyzed

# Required Fields:
- optimizations
- severity
- analyzed_artifact

# Producers:
- api.optimize
- workflow.optimize

# Consumers:
- api.implement
- report.generate
- dashboard.display

# Related Types:
- validation-report
- openapi-spec
- workflow-definition

# Validation Rules:
- severity must be one of: low, medium, high, critical
- optimizations array must not be empty
- each optimization must have: description, category, priority, suggested_fix
