# Name: /deploy
# Version: 0.1.0
# Description: Deploy application to specified environment

# Execution Type: workflow
# Target: workflows/deploy-pipeline.yaml

# Parameters:
- environment: enum (required, values=[dev,staging,production]) - Target deployment environment
- version: string (required) - Application version to deploy
- skip_tests: boolean (optional, default=false) - Skip test execution before deployment
- rollback_on_failure: boolean (optional, default=true) - Automatically rollback on deployment failure

# Execution Context:
- timeout: 1800
- notification_channel: slack

# Status: draft

# Tags: deployment, devops, workflow
