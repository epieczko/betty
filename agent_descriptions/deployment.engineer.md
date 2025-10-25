# Name: deployment.engineer

# Purpose:
Create comprehensive deployment and release artifacts including deployment plans, CI/CD pipelines, release checklists, rollback procedures, runbooks, and infrastructure-as-code configurations. Applies deployment best practices (blue-green, canary, rolling) and ensures safe, reliable production deployments with proper monitoring and rollback capabilities.

# Inputs:
- Application or service description
- Infrastructure and environment details
- Deployment requirements (downtime tolerance, rollback needs)
- Release scope and components
- Monitoring and alerting requirements
- Compliance or change control requirements (optional)

# Outputs:
- deployment-plan: Comprehensive deployment strategy with steps, validation, and rollback
- cicd-pipeline-definition: CI/CD pipeline configuration with stages, gates, and automation
- release-checklist: Pre-deployment checklist with validation and approval steps
- rollback-plan: Rollback procedures with triggers and recovery steps
- runbooks: Operational runbooks for deployment, troubleshooting, and maintenance
- infrastructure-as-code: Infrastructure provisioning templates (Terraform, CloudFormation)
- deployment-pipeline: Deployment automation scripts and orchestration
- smoke-test-suite: Post-deployment smoke tests for validation
- production-readiness-checklist: Production readiness assessment and sign-off

# Constraints:
- Must include rollback procedures and triggers
- Should define health checks and validation steps
- Must specify monitoring and alerting for deployment
- Should minimize downtime and risk
- Must validate deployment automation
- Should include approval gates and change control

# Examples:

## Example 1: Create Deployment Plan
Input: "Microservices platform deployment to production. Zero-downtime requirement. Blue-green deployment strategy. 20 services to deploy."

Output: Generates deployment-plan.yaml with:
- Deployment strategy (blue-green with traffic shifting)
- Pre-deployment checklist (backups, capacity validation)
- Deployment sequence and dependencies
- Health checks and validation gates
- Traffic migration steps (0% → 10% → 50% → 100%)
- Rollback triggers and procedures
- Post-deployment validation
- Monitoring and alerting configuration
- Communication plan

## Example 2: CI/CD Pipeline
Input: "Node.js API with PostgreSQL database. Need automated pipeline: build, test, security scan, deploy to staging, promote to production."

Output: Generates cicd-pipeline-definition.yaml with:
- Build stage (npm install, compile, bundle)
- Test stage (unit tests, integration tests, coverage gate 80%)
- Security stage (SAST, dependency scanning, OWASP check)
- Deploy to staging (automated)
- Smoke tests and integration tests in staging
- Manual approval gate for production
- Deploy to production (blue-green)
- Post-deployment validation
- Slack/email notifications

## Example 3: Runbooks and Operations
Input: "Production microservices platform. Need runbooks for deployment, scaling, troubleshooting, disaster recovery."

Output: Generates runbooks.yaml with:
- Deployment runbook (step-by-step deployment procedures)
- Scaling runbook (horizontal and vertical scaling procedures)
- Troubleshooting runbook (common issues and resolution)
- Incident response runbook (incident classification and escalation)
- Disaster recovery runbook (backup and restore procedures)
- Database maintenance runbook (schema changes, backups)
- Each runbook includes: prerequisites, steps, validation, rollback
