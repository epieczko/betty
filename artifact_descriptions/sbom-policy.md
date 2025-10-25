# Name: sbom-policy

# Purpose:
SBOM policy for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables.

# Format: JSON

# File Pattern: *.sbom-policy.json

# Schema Properties:
- metadata (object): Metadata about this artifact including version, author, timestamp
- content (object): Main content of the artifact
- scope (string): Scope of the policy/charter
- rules (array): Rules and guidelines

# Required Fields:
- metadata
- content

# Producers:
- TBD

# Consumers:
- TBD

# Related Types:
- TBD
