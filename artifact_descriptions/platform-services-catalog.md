# Name: platform-services-catalog

## Executive Summary

The Platform Services Catalog is the authoritative registry of all platform capabilities, self-service APIs, and developer-facing services within an Internal Developer Platform (IDP). Built on frameworks like Backstage, Port, or Kratix, this artifact enables platform teams to expose golden paths, service templates, and standardized workflows that accelerate software delivery while maintaining governance and operational excellence.

As the central hub for platform engineering, this catalog provides a unified interface where developers discover, provision, and manage infrastructure resources without requiring deep platform expertise. It embodies the "you build it, you run it" philosophy by offering curated, production-ready building blocks that abstract complexity while preserving flexibility.

### Strategic Importance

- **Developer Velocity**: Reduces time-to-production by providing self-service golden paths and pre-approved templates
- **Cognitive Load Reduction**: Abstracts infrastructure complexity through well-designed abstractions aligned with Team Topologies principles
- **Platform as Product**: Treats internal platform capabilities as products with clear ownership, documentation, and SLOs
- **Standardization at Scale**: Enforces organizational best practices through curated service templates and Software Templates
- **Observability & Governance**: Maintains complete visibility into platform usage, service dependencies, and compliance requirements

## Purpose & Scope

### Primary Purpose

This artifact serves as the comprehensive catalog of all platform services, APIs, and capabilities offered by the platform engineering team. It enables developers to discover and consume infrastructure resources through self-service interfaces, golden paths, and Software Templates while maintaining governance, security, and cost controls.

### Scope

**In Scope**:
- Service catalog entries in Backstage, Port, Kratix, or similar IDP frameworks
- Software Templates for common patterns (microservices, databases, message queues, CDN configurations)
- Self-service APIs and platform capabilities (namespace provisioning, DNS management, certificate issuance)
- Golden paths and recommended technology stacks
- Service metadata including ownership (Team Topologies), SLOs, dependencies, and documentation
- Integration with infrastructure provisioning tools (Terraform, Crossplane, Pulumi, CloudFormation)
- Catalog entity definitions (Components, APIs, Resources, Systems, Domains)
- TechDocs integration for service documentation

**Out of Scope**:
- Application-specific business logic (handled by application teams)
- Individual Kubernetes manifests (covered by kustomize-manifests and installer-manifests)
- Detailed infrastructure-as-code implementations (managed in separate IaC repositories)
- Service mesh traffic management rules (covered by service-mesh-configurations)
- Environment-specific configurations (handled by environment-matrix)

### Target Audience

**Primary Audience**:
- Application Developers consuming platform services through self-service interfaces
- Platform Engineers maintaining and evolving the service catalog
- Product Owners planning application architectures using available platform capabilities

**Secondary Audience**:
- SRE Teams monitoring platform service usage and performance
- Security Teams ensuring compliance and governance through catalog policies
- Engineering Leadership tracking platform adoption and developer productivity metrics

## Document Information

**Format**: Markdown

**File Pattern**: `*.platform-services-catalog.md`

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

**GitOps Workflow**: Store catalog definitions in version control (Git) with pull request reviews and automated validation pipelines
**Semantic Versioning**: Version catalog entities and templates using semantic versioning (MAJOR.MINOR.PATCH) to manage breaking changes
**Self-Service by Default**: Design catalog entries for full self-service provisioning without requiring platform team intervention
**Golden Path Curation**: Maintain opinionated, production-ready templates that encode organizational best practices and security requirements
**Comprehensive Documentation**: Include TechDocs, runbooks, architecture diagrams, and getting-started guides for each catalog entry
**Clear Ownership**: Assign platform team ownership (following Team Topologies) to each catalog entry with clear escalation paths
**SLO Definition**: Define and publish Service Level Objectives (SLOs) for platform services to set clear reliability expectations
**Dependency Mapping**: Explicitly document service dependencies and relationships in catalog metadata
**Cost Transparency**: Include cost estimates and resource quotas in service templates to promote cost awareness
**Security by Default**: Embed security best practices (least privilege, secrets management, network policies) into all templates
**Progressive Disclosure**: Layer complexity - provide simple defaults while allowing advanced customization when needed
**Validation & Testing**: Implement automated validation of catalog schemas and test template execution in sandbox environments
**Usage Analytics**: Track catalog adoption metrics, popular services, and developer friction points to guide platform evolution
**Feedback Loops**: Establish mechanisms for developers to request new services or improvements to existing catalog entries
**Deprecation Strategy**: Define clear processes for deprecating and sunsetting platform services with adequate migration windows
**Multi-Tenancy Support**: Design catalog services with namespace isolation, RBAC, and resource quotas for safe multi-tenant operation

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

**Platform Engineering**:
- Backstage (Spotify's developer portal framework)
- Port (Internal Developer Portal platform)
- Kratix (Promise-based platform framework)
- Team Topologies (platform team patterns, cognitive load management)
- Golden Paths and Paved Roads patterns
- Internal Developer Platforms (IDP) best practices
- Platform as a Product principles

**Service Catalog Standards**:
- Backstage Software Catalog data model
- Backstage Software Templates (cookiecutter, Yeoman scaffolding)
- Open Application Model (OAM)
- Kubernetes Custom Resource Definitions (CRDs)
- OpenAPI / Swagger specifications for platform APIs
- YAML/JSON schema validation

**Infrastructure Automation**:
- Terraform modules and registries
- Crossplane Composite Resource Definitions (XRDs)
- Pulumi component resources
- AWS CloudFormation StackSets
- Azure Blueprints
- Google Cloud Deployment Manager templates

**Kubernetes & Cloud Native**:
- CNCF Landscape technologies
- Kubernetes Operators (Operator SDK, Kubebuilder)
- Operator Lifecycle Manager (OLM)
- Helm charts and registries
- Kustomize bases and overlays
- Cloud Native Computing Foundation (CNCF) graduated projects

**Service Mesh Integration**:
- Istio service entries and configuration
- Linkerd service profiles
- Consul Connect intentions
- AWS App Mesh virtual services

**Configuration Management**:
- ConfigMaps and Secrets management patterns
- External Secrets Operator
- HashiCorp Vault integration
- SOPS (Secrets OPerationS)
- sealed-secrets by Bitnami

**Observability & Service Management**:
- OpenTelemetry for distributed tracing
- Prometheus service discovery
- Grafana dashboards for platform metrics
- Service Level Objectives (SLOs) and Service Level Indicators (SLIs)
- Error budgets and reliability engineering

**GitOps & Continuous Delivery**:
- ArgoCD ApplicationSets
- Flux Kustomizations and HelmReleases
- Tekton Pipelines and Tasks
- GitHub Actions workflows
- GitLab CI/CD pipelines

**Security & Compliance**:
- Pod Security Standards (Restricted, Baseline, Privileged)
- RBAC (Role-Based Access Control) patterns
- Network Policies for zero-trust networking
- SPIFFE/SPIRE for workload identity
- OPA (Open Policy Agent) / Gatekeeper policies
- Falco runtime security rules

**Reference**: Consult organizational platform engineering and architecture teams for detailed guidance on framework application and IDP strategy

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
