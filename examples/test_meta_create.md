# Name: test.example

# Type: skill

# Purpose:
A simple test skill for validating the meta.create orchestrator workflow

# Inputs:
- input_data (string) - Test input data

# Outputs:
- output_result (string) - Processed result

# Produces Artifacts:
- test.result

# Consumes Artifacts:
- test.input

# Permissions:
- filesystem:read

# Implementation Notes:
This is a minimal test skill to verify that meta.create can properly
orchestrate the creation of skills, check for duplicates, and validate
compatibility.

# Examples:
- Process test data and produce test results
- Validate meta.create orchestration workflow
