# Name: sbom-verification-reports

# Purpose:
SBOM verification reports for Deployment and Release. Part of Release Management documentation and deliverables.

# Format: JSON

# File Pattern: *.sbom-verification-reports.json

# Schema Properties:
- metadata (object): Metadata about this artifact including version, author, timestamp
- content (object): Main content of the artifact
- findings (array): List of findings or results
- summary (string): Executive summary

# Required Fields:
- metadata
- content

# Producers:
- TBD

# Consumers:
- TBD

# Related Types:
- TBD
