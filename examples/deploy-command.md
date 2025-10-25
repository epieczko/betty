# Name: /deploy
# Version: 0.1.0
# Description: Deploy application to target environment with full pipeline

# Execution Type: workflow
# Target: workflows/deploy-pipeline.yaml

# Parameters:
- environment: enum (required, values=[dev,staging,production]) - Target environment
- version: string (required) - Version tag to deploy
- skip_tests: boolean (optional, default=false) - Skip test execution

# Status: active

# Tags: deployment, workflow, pipeline, workflow-example

## Instructions

This command executes a comprehensive deployment workflow that orchestrates
multiple components in a coordinated sequence:

1. **Validate** the version tag
2. **Run tests** (unless skipped)
3. **Build artifacts** in parallel (backend + frontend)
4. **Deploy** using intelligent orchestration agent
5. **Verify** the deployment
6. **Notify** stakeholders

The workflow coordinates:
- Multiple skills for deterministic tasks
- An agent for intelligent deployment orchestration
- Parallel execution for efficiency
- Error handling and rollback capabilities

This is a perfect workflow example because it:
- Orchestrates multiple distinct components
- Includes both sequential and parallel execution
- Mixes skills (deterministic) and agents (reasoning)
- Has clear phases with dependencies
- Implements error handling and rollback
