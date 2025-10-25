# Name: workflow.orchestrate

# Purpose:
Orchestrate multi-artifact workflows by coordinating specialized agents and artifact creation skills. Creates complete artifact sets for complex initiatives by managing dependencies, sequencing work, and ensuring artifact consistency. Supports common SDLC workflows like project initiation, security reviews, data design, test planning, deployment planning, and full SDLC cycles.

# Inputs:
- workflow_type (string, required): Type of workflow to execute (project-initiation, security-review, data-design, test-planning, deployment-planning, full-sdlc)
- description (string, required): Initiative or project description for context
- output_directory (string, required): Directory where all workflow artifacts will be created
- author (string, optional): Author name for generated artifacts (default: "Workflow Orchestrator")
- classification (string, optional): Classification level (Public, Internal, Confidential, Restricted, default: Internal)

# Outputs:
- workflow-execution-report: Complete workflow execution report with all generated artifacts
- artifact-manifest: Manifest of all created artifacts with paths and validation status
- All artifacts specified by the workflow type (e.g., business-case, project-charter, etc.)

# Artifacts Consumed:
- None (initiates workflows from user context)

# Artifacts Produced:
- workflow-execution-report
- artifact-manifest
- Plus all artifacts specified by the chosen workflow type

# Permissions Required:
- filesystem:read
- filesystem:write

# Dependencies:
- artifact.create skill (to create individual artifacts)
- artifact.validate skill (to validate created artifacts)
- Template files in templates/ directory

# Implementation Requirements:

## Workflow Definitions
Support these pre-defined workflows:

1. **project-initiation**: business-case, project-charter, raid-log, stakeholder-analysis
2. **security-review**: threat-model, security-architecture-diagram, security-assessment, vulnerability-management-plan
3. **data-design**: data-model, schema-definition, data-flow-diagram, data-governance-policy
4. **test-planning**: test-plan, test-automation-strategy, test-cases, acceptance-criteria
5. **deployment-planning**: deployment-plan, cicd-pipeline-definition, runbooks, rollback-plan
6. **full-sdlc**: business-case, project-charter, threat-model, data-model, test-plan, deployment-plan

## Orchestration Logic
1. Create output directory
2. For each artifact in workflow (sorted by priority/dependencies):
   - Call artifact.create with appropriate type and context
   - Call artifact.validate to check quality
   - Track created artifacts and validation results
3. Generate workflow execution report with summary
4. Generate artifact manifest listing all created artifacts
5. Return success if at least one artifact created

## Error Handling
- Handle missing dependencies gracefully
- Continue workflow even if individual artifacts fail
- Report all failures in execution report
- Return overall success based on whether any artifacts were created

# Examples:

## Example 1: Project Initiation Workflow
```bash
python3 skills/workflow.orchestrate/workflow_orchestrate.py \
  project-initiation \
  "New customer self-service portal to reduce support costs" \
  ./artifacts/customer-portal \
  --author "Product Team"
```

Generates:
- business-case.yaml
- project-charter.yaml
- raid-log.yaml
- stakeholder-analysis.yaml
- project-initiation-workflow-report.yaml

## Example 2: Security Review Workflow
```bash
python3 skills/workflow.orchestrate/workflow_orchestrate.py \
  security-review \
  "Payment API with PCI-DSS compliance" \
  ./artifacts/payment-api-security \
  --classification Confidential
```

Generates:
- threat-model.yaml
- security-architecture-diagram.yaml
- security-assessment.yaml
- vulnerability-management-plan.yaml
- security-review-workflow-report.yaml

## Example 3: Full SDLC Workflow
```bash
python3 skills/workflow.orchestrate/workflow_orchestrate.py \
  full-sdlc \
  "Cloud migration program - migrate 50 applications to AWS" \
  ./artifacts/cloud-migration \
  --author "Enterprise Architecture"
```

Generates complete artifact set covering strategy through deployment.

# CLI Interface:
```
workflow_orchestrate.py <workflow_type> <description> <output_directory> [--author NAME] [--classification LEVEL]
```

Positional arguments:
- workflow_type: One of the supported workflow types
- description: Project/initiative description
- output_directory: Where to save all artifacts

Optional arguments:
- --author: Author name for artifacts
- --classification: Classification level (Public|Internal|Confidential|Restricted)

Exit code: 0 if successful (at least one artifact created), 1 if failed

# Output Format:
Prints progress to stdout, returns JSON-formatted workflow execution report
