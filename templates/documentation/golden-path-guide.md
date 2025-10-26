# Golden Path Guide

> **See also**: `artifact_descriptions/golden-path-guide.md` for complete guidance

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Author** | Author Name |
| **Owner** | Owner Name/Role |
| **Classification** | Internal |

## Executive Summary

The Golden Path Guide, also known as "Paved Roads" or "Blessed Paths," is a platform engineering artifact that defines opinionated, pre-approved technology choices and self-service workflows for common development scenarios. These guides reduce cognitive load on development teams by providing curate

## Purpose

This artifact serves as the definitive reference for approved technology patterns, self-service platform capabilities, and blessed implementation paths that development teams should follow. It eliminates decision paralysis, reduces time-to-first-commit, ensures architectural consistency, and provides pre-integrated observability, security, and operational tooling through opinionated templates and 

## Scope

### In Scope

- Backstage Software Templates for common service archetypes (REST API, web frontend, data pipeline, microservice)
- Approved technology stack recommendations by use case (languages, frameworks, databases)
- Infrastructure-as-Code (IaC) reference implementations using Terraform, Pulumi, or CloudFormation
- Pre-configured CI/CD pipeline templates (GitHub Actions, GitLab CI, Jenkins, CircleCI)
- Containerization standards and base image repositories (Docker, Kaniko, Buildpacks)

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Opinionated but Escapable**: Provide strong defaults and recommendations while allowing justified deviations with architectural review

**One-Click Creation**: Enable complete service creation from template in under 5 minutes with all integrations pre-configured

**Production-Ready from Start**: Include monitoring, logging, error tracking, security scanning, and deployment automation in every template

**Living Examples**: Maintain reference implementations that actually run in production as proof-of-concept and testing grounds

**Developer Feedback Loops**: Survey developers quarterly on template usability and pain points; iterate based on real usage data

**Template Versioning**: Version templates like software with semantic versioning and clear upgrade paths for existing services

**Documentation Embedded**: Include comprehensive README, architecture diagrams, and onboarding guides within generated projects

**Progressive Disclosure**: Start with simplest working example; provide links to advanced patterns for complex requirements

## Related Documents

- [Related Artifact]: Relationship description

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
