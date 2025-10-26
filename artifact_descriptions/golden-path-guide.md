# Name: golden-path-guide

## Executive Summary

The Golden Path Guide, also known as "Paved Roads" or "Blessed Paths," is a platform engineering artifact that defines opinionated, pre-approved technology choices and self-service workflows for common development scenarios. These guides reduce cognitive load on development teams by providing curated, production-ready templates through Internal Developer Platforms (IDPs) like Backstage, Port, or Kratix, enabling developers to provision infrastructure, deploy applications, and configure CI/CD pipelines without deep platform expertise.

Golden paths embody organizational best practices for technology selection, security compliance, observability integration, and operational excellence. They leverage Software Templates in Backstage, cookiecutter scaffolding, Terraform modules, and pre-configured CI/CD pipelines to enable "one-click" creation of new services that automatically include monitoring, logging, testing, and deployment automation. This artifact accelerates developer velocity, ensures compliance with security and architecture standards, and reduces operational burden by standardizing platform patterns across engineering teams.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact serves as the definitive reference for approved technology patterns, self-service platform capabilities, and blessed implementation paths that development teams should follow. It eliminates decision paralysis, reduces time-to-first-commit, ensures architectural consistency, and provides pre-integrated observability, security, and operational tooling through opinionated templates and automation.

### Scope

**In Scope**:
- Backstage Software Templates for common service archetypes (REST API, web frontend, data pipeline, microservice)
- Approved technology stack recommendations by use case (languages, frameworks, databases)
- Infrastructure-as-Code (IaC) reference implementations using Terraform, Pulumi, or CloudFormation
- Pre-configured CI/CD pipeline templates (GitHub Actions, GitLab CI, Jenkins, CircleCI)
- Containerization standards and base image repositories (Docker, Kaniko, Buildpacks)
- Kubernetes deployment manifests and Helm chart patterns
- Observability integration (Datadog, New Relic, Prometheus, Grafana)
- Security scanning automation (Snyk, SonarQube, Trivy, Checkov)
- API design standards and OpenAPI template generation
- Database provisioning patterns (RDS, Cloud SQL, managed databases)
- Secrets management integration (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
- Service mesh configuration (Istio, Linkerd, Consul)
- Developer environment setup (devcontainers, Gitpod, local development)
- Reference implementations and example repositories

**Out of Scope**:
- Legacy system integration patterns (unless actively maintained)
- Unapproved experimental technologies
- Custom one-off solutions requiring platform team support
- Application-specific business logic implementations
- Detailed programming language tutorials
- Platform team internal operational procedures

### Target Audience

**Primary Audience**:
- Software Engineers creating new services and applications
- Platform Engineering teams maintaining golden path templates
- Developer Experience (DevEx) teams improving self-service capabilities
- Engineering Team Leads selecting technology stacks
- New engineers onboarding to the platform

**Secondary Audience**:
- Architecture teams governing technology choices
- Security teams embedding compliance controls
- SRE teams defining operational standards
- Product managers understanding platform capabilities

## Document Information

**Format**: Markdown

**File Pattern**: `*.golden-path-guide.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: [Define typical classification level - Public | Internal | Confidential | Restricted]

**Retention**: [Define retention period per organizational records management policy]


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Scheduled date for next formal review
- `documentOwner`: Role/person responsible for maintenance
- `classification`: Information classification level
- `retentionPeriod`: How long document must be retained

**Authorship & Review**:
- `primaryAuthor`: Lead author name and role
- `contributors`: Additional contributors and their roles
- `reviewers`: Designated reviewers (technical, security, compliance, etc.)
- `approvers`: Formal approvers with sign-off authority
- `reviewStatus`: Current review status
- `approvalDate`: Date of formal approval

**Document Purpose**:
- `executiveSummary`: 2-3 paragraph overview for executive audience
- `businessContext`: Why this document exists and its business value
- `scope`: What is covered and what is explicitly out of scope
- `applicability`: Who this applies to and under what circumstances
- `relatedDocuments`: References to related artifacts and dependencies

### Main Content Sections

(Content structure will vary based on specific artifact type. Include all relevant sections needed to fully document the subject matter.)

**Core Information**:
- Document the primary information this artifact is meant to capture
- Organize in logical sections appropriate to the content type
- Use consistent formatting and structure
- Include sufficient detail for intended audience
- Provide examples where helpful

**Supporting Information**:
- Background context necessary for understanding
- Assumptions and constraints
- Dependencies on other artifacts or systems
- Related information and cross-references


## Best Practices

**Opinionated but Escapable**: Provide strong defaults and recommendations while allowing justified deviations with architectural review
**One-Click Creation**: Enable complete service creation from template in under 5 minutes with all integrations pre-configured
**Production-Ready from Start**: Include monitoring, logging, error tracking, security scanning, and deployment automation in every template
**Living Examples**: Maintain reference implementations that actually run in production as proof-of-concept and testing grounds
**Developer Feedback Loops**: Survey developers quarterly on template usability and pain points; iterate based on real usage data
**Template Versioning**: Version templates like software with semantic versioning and clear upgrade paths for existing services
**Documentation Embedded**: Include comprehensive README, architecture diagrams, and onboarding guides within generated projects
**Progressive Disclosure**: Start with simplest working example; provide links to advanced patterns for complex requirements
**Measure Adoption**: Track template usage, time-to-first-deployment, and developer satisfaction via platform analytics
**Default to Open Source**: Prefer battle-tested open source tools over proprietary solutions to reduce vendor lock-in
**Security by Default**: Embed secrets scanning, dependency updates (Renovate, Dependabot), and vulnerability scanning in every template
**Observability Integration**: Auto-instrument applications with OpenTelemetry or vendor SDKs at creation time
**Cost Awareness**: Include cost estimation and resource right-sizing recommendations in infrastructure templates
**Migration Guides**: Provide step-by-step guides for teams moving from legacy patterns to golden paths
**Platform Team Dogfooding**: Platform teams should use their own golden paths for internal tools to validate usability
**Technology Radar Updates**: Quarterly reviews of technology choices aligned with ThoughtWorks Tech Radar or internal radar
**Multi-Cloud Consistency**: Where possible, provide equivalent patterns across AWS, Azure, and GCP to support multi-cloud strategies
**Local Development Parity**: Ensure golden paths work identically in local development (Docker Compose, Tilt, Skaffold) and production
**Escape Hatch Documentation**: Clearly document when to deviate from golden paths and the approval process required
**Template Ownership**: Assign dedicated owners to each template for maintenance, updates, and developer support

## Quality Criteria

Before considering this artifact complete and ready for approval, verify:

✓ **Completeness**: All required sections present and adequately detailed
✓ **Accuracy**: Information verified and validated by appropriate subject matter experts
✓ **Clarity**: Written in clear, unambiguous language appropriate for intended audience
✓ **Consistency**: Aligns with organizational standards, templates, and related artifacts
✓ **Currency**: Based on current information; outdated content removed or updated
✓ **Traceability**: Includes references to source materials and related documents
✓ **Stakeholder Review**: Reviewed by all key stakeholders with feedback incorporated
✓ **Technical Review**: Technical accuracy verified by qualified technical reviewers
✓ **Compliance**: Meets all applicable regulatory, policy, and contractual requirements
✓ **Approval**: All required approvals obtained and documented
✓ **Accessibility**: Stored in accessible location with appropriate permissions
✓ **Metadata**: Complete metadata enables search, categorization, and lifecycle management

## Common Pitfalls & How to Avoid

❌ **Incomplete Information**: Rushing to complete without gathering all necessary inputs
   ✓ *Solution*: Create comprehensive checklist of required information; allocate sufficient time

❌ **Lack of Stakeholder Input**: Creating in isolation without engaging affected parties
   ✓ *Solution*: Identify all stakeholders early; schedule working sessions for collaborative development

❌ **Outdated Content**: Using old information or not updating when conditions change
   ✓ *Solution*: Establish refresh schedule; define triggers requiring immediate update

❌ **Inconsistent Format**: Not following organizational templates and standards
   ✓ *Solution*: Always start from approved template; verify against style guide before submission

❌ **Missing Approvals**: Publishing without proper authorization
   ✓ *Solution*: Understand approval chain; route through all required approvers with evidence

❌ **Poor Version Control**: Making changes without maintaining history
   ✓ *Solution*: Use proper version control system; never directly edit published version

❌ **Inadequate Distribution**: Completing artifact but stakeholders unaware it exists
   ✓ *Solution*: Define distribution list; actively communicate availability and location

❌ **No Maintenance Plan**: Creating artifact as one-time activity with no ongoing ownership
   ✓ *Solution*: Assign owner; schedule regular reviews; define update triggers

## Related Standards & Frameworks

**Internal Developer Platforms (IDP)**:
- Backstage (Spotify) for software catalog and templates
- Port for developer self-service portal
- Kratix for platform-as-a-product frameworks
- Humanitec for dynamic configuration orchestration
- OpsLevel for service maturity tracking
- Cortex for internal developer portal
- Configure8 for platform orchestration

**Software Templates & Scaffolding**:
- Backstage Software Templates with Cookiecutter
- Yeoman generators for project scaffolding
- Cookiecutter for project templating
- Copier for template-based project creation
- Nix flakes for reproducible development environments
- Projen for project configuration synthesis

**Infrastructure-as-Code Patterns**:
- Terraform modules and module registries
- Pulumi templates and component libraries
- AWS CDK constructs and patterns
- Azure Bicep modules
- CloudFormation templates
- Crossplane compositions for cloud resources
- Terragrunt for DRY Terraform configurations

**CI/CD Pipeline Templates**:
- GitHub Actions reusable workflows
- GitLab CI templates and includes
- Jenkins shared libraries
- CircleCI orbs
- Tekton pipeline templates
- Argo Workflows templates
- Drone CI pipeline libraries

**Container & Kubernetes Standards**:
- Cloud Native Buildpacks for container builds
- Kustomize for Kubernetes configuration management
- Helm charts and chart repositories
- Kubernetes Operators for application lifecycle
- OCI (Open Container Initiative) image specs
- CNCF graduated project recommendations

**Observability Integration**:
- OpenTelemetry instrumentation standards
- Prometheus metric naming conventions
- Grafana dashboard templates
- Datadog APM auto-instrumentation
- New Relic quickstarts
- Elastic Common Schema for logging
- Jaeger for distributed tracing

**Security & Compliance**:
- OWASP Top 10 security controls
- CIS Benchmarks for container hardening
- NIST Cybersecurity Framework alignment
- SOC 2 evidence collection automation
- PCI DSS compliance for payment services
- HIPAA technical safeguards for healthcare
- GDPR privacy-by-design principles

**API & Service Standards**:
- OpenAPI 3.x specification standards
- gRPC proto file conventions
- GraphQL schema design patterns
- REST API maturity models
- AsyncAPI for event-driven architectures
- JSON Schema for data validation

**Platform Engineering Practices**:
- Team Topologies platform team patterns
- DORA metrics for platform effectiveness
- SPACE framework for developer productivity
- ThoughtWorks Tech Radar for technology adoption
- Gartner Platform Engineering guidance
- CNCF Technology Landscape navigation

**Developer Experience (DevEx)**:
- Inner Loop vs Outer Loop optimization
- Cognitive Load Theory application
- Flow State enablement practices
- Developer Self-Service maturity models
- Platform-as-a-Product principles

**Documentation Standards**:
- README templates with quick-start guides
- ADR (Architecture Decision Record) formats
- Docs-as-Code with MkDocs, Docusaurus
- API documentation with Swagger UI, Redocly
- Service catalog metadata standards

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- [List artifacts that provide input to this one]
- [Data sources that feed this artifact]
- [Prerequisites that must be satisfied]

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- [Artifacts that consume information from this one]
- [Processes that use this artifact]
- [Teams or roles that rely on this information]

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- [Complementary artifacts in same phase]
- [Artifacts in adjacent phases]
- [Cross-cutting artifacts (e.g., risk register)]

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: [If applicable] Architecture board review for standards compliance
5. **Security Review**: [If applicable] Security team review for security requirements
6. **Compliance Review**: [If applicable] Compliance review for regulatory requirements
7. **Legal Review**: [If applicable] Legal counsel review
8. **Final Approval**: Designated approver(s) provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: [Define role - e.g., Program Manager, Architecture Lead, CISO]
- Secondary Approver: [For high-risk or cross-functional artifacts]
- Governance Approval: [If requires board or committee approval]

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: [Define cadence - e.g., Quarterly, Annually]

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur
- Regulatory requirements change
- Major incidents reveal deficiencies
- Stakeholder requests identify needed updates
- Related artifacts are substantially updated

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring, scope changes, or approach changes
- **MINOR**: New sections, substantial additions, or enhancements
- **PATCH**: Corrections, clarifications, minor updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: [Define based on regulatory and business requirements]

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: [Define role responsible for maintenance]

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/{artifact_name}-template.{format_type.lower()}`

**Alternative Formats**: [If multiple formats supported]

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/{artifact_name}-example-*.{format_type.lower()}`

**Annotated Guidance**: See annotated examples showing best practices and common approaches

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified and engaged all required stakeholders
- [ ] Gathered prerequisite information and inputs
- [ ] Obtained access to necessary systems and data
- [ ] Allocated sufficient time for quality completion
- [ ] Identified reviewers and approvers
- [ ] Understood applicable standards and requirements

While creating this artifact:

- [ ] Following approved template structure
- [ ] Documenting sources and references
- [ ] Writing clearly for intended audience
- [ ] Including visual aids where helpful
- [ ] Self-reviewing against quality criteria
- [ ] Seeking input from stakeholders

Before submitting for approval:

- [ ] Completed all required sections
- [ ] Verified accuracy of all information
- [ ] Obtained peer review feedback
- [ ] Addressed all review comments
- [ ] Spell-checked and proofread
- [ ] Completed all metadata fields
- [ ] Verified compliance with standards
- [ ] Ready for formal approval process

## Governance & Compliance

### Regulatory Considerations

[Define any regulatory requirements applicable to this artifact type, such as:]

- SOC 2: [If artifact supports SOC 2 controls]
- ISO 27001: [If part of ISMS documentation]
- GDPR/Privacy: [If contains or references personal data]
- Industry-Specific: [Healthcare, Financial Services, etc.]

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team
- External audits by third-party auditors
- Regulatory examinations
- Customer security assessments

**Audit Preparation**:
- Maintain complete version history
- Document all approvals with evidence
- Keep change log current
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- [Relevant organizational policies]
- [Industry regulations and standards]
- [Contractual obligations]
- [Governance framework requirements]

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Access Frequency**: How often artifact is accessed/referenced
- **Update Frequency**: How often artifact requires updates
- **Downstream Impact**: How many artifacts/processes depend on this

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: {phase}

**Category**: {category}

**Typical Producers**: [Roles/teams that typically create this artifact]

**Typical Consumers**: [Roles/teams that typically use this artifact]

**Effort Estimate**: [Typical hours/days required to complete]

**Complexity Level**: [Low | Medium | High | Very High]

**Business Criticality**: [Low | Medium | High | Mission Critical]

**Change Frequency**: [Static | Infrequent | Regular | Frequent]

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: {phase} - Version 2.0*
