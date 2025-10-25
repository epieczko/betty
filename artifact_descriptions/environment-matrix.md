# Name: environment-matrix

## Executive Summary

The Environment Matrix is a comprehensive configuration framework that defines infrastructure, application, and operational parameters across all deployment environments (development, staging, production) and deployment targets (regions, clouds, clusters). This structured artifact ensures environment parity, enables progressive delivery through controlled promotion pipelines, and maintains visibility into configuration differences that exist between environments.

In cloud-native architectures supporting multi-region, multi-cloud, and hybrid deployments, the environment matrix serves as the authoritative source for environment-specific configurations, resource sizing, security policies, compliance requirements, and operational characteristics. It enables organizations to maintain consistency while accommodating necessary environment-specific variations for performance, cost optimization, and regulatory compliance.

### Strategic Importance

- **Environment Parity**: Maintains consistent configuration structure across dev, staging, and production environments
- **Progressive Delivery**: Enables controlled promotion of changes through environment pipelines with validation gates
- **Multi-Region Strategy**: Defines region-specific configurations for disaster recovery and geographic distribution
- **Multi-Cloud Support**: Manages configurations across AWS, Azure, GCP, and on-premises infrastructure
- **Cost Optimization**: Adjusts resource allocations per environment (smaller in dev, production-sized in prod)
- **Compliance Mapping**: Documents environment-specific regulatory and security requirements
- **Configuration Drift Prevention**: Provides baseline for detecting unauthorized configuration changes

## Purpose & Scope

### Primary Purpose

This artifact defines the complete configuration matrix for all deployment environments, regions, clouds, and clusters, specifying infrastructure sizing, security policies, networking configurations, operational parameters, and compliance requirements. It serves as the single source of truth for understanding environmental differences and driving environment-specific Kustomize overlays, Helm values, and Terraform variables.

### Scope

**In Scope**:
- Environment definitions (dev, staging, UAT, pre-prod, production)
- Region/availability zone configurations (us-east-1, eu-west-1, ap-southeast-1)
- Cloud provider-specific settings (AWS, Azure, GCP, on-premises)
- Cluster configurations (EKS, AKS, GKE, self-managed Kubernetes)
- Resource sizing per environment (CPU, memory, storage, node counts)
- Networking configurations (VPCs, subnets, CIDR ranges, DNS zones)
- Security policies per environment (network policies, Pod Security Standards, RBAC)
- Observability configurations (logging levels, metrics retention, tracing sampling)
- Backup and disaster recovery settings per environment
- Compliance and regulatory requirements (PCI-DSS, HIPAA, SOC 2, GDPR)
- Promotion gates and approval requirements between environments
- Environment-specific feature flags and configuration toggles
- Cost allocation tags and budget constraints
- SLOs and SLAs per environment tier

**Out of Scope**:
- Application-specific business logic (handled by application code)
- Detailed Kubernetes manifests (covered by kustomize-manifests and installer-manifests)
- Infrastructure-as-code implementations (Terraform, Pulumi modules)
- CI/CD pipeline definitions (managed in pipeline repositories)
- Secrets and credentials (managed through secret stores)

### Target Audience

**Primary Audience**:
- Platform Engineers defining environment architecture and configurations
- DevOps Engineers managing environment-specific deployments and promotions
- Cloud Architects designing multi-region and multi-cloud strategies

**Secondary Audience**:
- Application Developers understanding environment constraints and capabilities
- Security Engineers auditing environment-specific security controls
- Compliance Officers verifying regulatory requirements per environment
- SRE Teams managing environment reliability and incident response

## Document Information

**Format**: Markdown

**File Pattern**: `*.environment-matrix.md`

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

**Environment Parity**: Maintain structural consistency across environments while varying only size and scale
**Production-Like Staging**: Size staging environment close to production for accurate performance testing
**Immutable Environments**: Treat environments as immutable; recreate rather than patch for configuration changes
**Progressive Promotion**: Always promote changes through dev -> staging -> prod pipeline, never skip stages
**Configuration as Code**: Store all environment configurations in Git with version control and audit trails
**Explicit Differences**: Document and justify every difference between environments with business rationale
**Minimize Dev/Prod Gap**: Keep development environment architecturally identical to production when possible
**Automated Validation**: Run automated tests at each promotion gate to validate environment-specific configurations
**Cost Right-Sizing**: Scale down non-production environments appropriately to optimize cloud spending
**Ephemeral Dev Environments**: Use short-lived development environments to reduce costs and ensure freshness
**Multi-Region Production**: Deploy production to multiple regions for high availability and disaster recovery
**Security Consistency**: Apply consistent security policies across environments with appropriate strength
**Monitoring Everywhere**: Implement observability in all environments, not just production
**Backup All Environments**: Back up configuration and data in all environments to enable quick recovery
**Clear Ownership**: Assign clear ownership for each environment with documented escalation paths
**Change Windows**: Define maintenance windows per environment for planned changes
**Blast Radius Limitation**: Isolate environments to prevent failures from cascading across environments
**Resource Tagging**: Tag all cloud resources with environment, owner, cost-center, and purpose
**Drift Detection**: Implement automated drift detection between desired (Git) and actual (cloud) state
**Documentation**: Maintain up-to-date runbooks for environment-specific operations and troubleshooting

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

**Environment Types**:
- Development environments (ephemeral, long-lived, per-developer)
- Integration/CI environments
- QA/Testing environments
- Staging/pre-production environments
- UAT (User Acceptance Testing) environments
- Production environments (blue/green, canary)
- Disaster recovery environments

**Multi-Cloud Architecture**:
- AWS (EKS, EC2, RDS, S3, Route 53, CloudFront)
- Azure (AKS, VMs, Azure SQL, Blob Storage, Azure DNS, Front Door)
- Google Cloud (GKE, Compute Engine, Cloud SQL, Cloud Storage, Cloud DNS, Cloud CDN)
- Hybrid cloud configurations
- Multi-cloud federation and failover

**Kubernetes Flavors**:
- Amazon EKS (Elastic Kubernetes Service)
- Azure AKS (Azure Kubernetes Service)
- Google GKE (Google Kubernetes Engine)
- Self-managed Kubernetes (kubeadm, kops, Rancher)
- OpenShift (Red Hat)
- K3s for edge deployments
- Kind/Minikube for local development

**Configuration Management**:
- Kustomize overlays per environment
- Helm values files per environment
- Terraform workspaces and variable files
- Pulumi stacks
- Environment-specific ConfigMaps and Secrets
- Feature flags per environment

**Infrastructure Sizing**:
- Node instance types and sizes
- Autoscaling configurations (HPA, VPA, Cluster Autoscaler)
- Resource requests and limits per environment
- Storage classes and capacity
- Database sizing and replica configurations
- Cache sizing (Redis, Memcached)

**Networking Configurations**:
- VPC/VNet CIDR ranges per environment
- Subnet allocation (public, private, data)
- NAT gateway and egress configurations
- Load balancer types and settings
- Ingress controller configurations
- DNS zones and record management
- CDN configurations (CloudFront, Akamai, Cloudflare)

**Security Policies**:
- Pod Security Standards per environment (Privileged, Baseline, Restricted)
- Network policies and segmentation
- RBAC policies per environment
- IAM roles and service accounts
- Certificate management (cert-manager, ACM, Let's Encrypt)
- Secret encryption (KMS, Key Vault, Cloud KMS)
- Security scanning thresholds

**Observability Configurations**:
- Logging levels per environment (DEBUG, INFO, WARN, ERROR)
- Log retention policies
- Metrics collection and retention
- Distributed tracing sampling rates
- APM (Application Performance Monitoring) integration
- Alerting thresholds per environment
- Dashboard configurations

**Disaster Recovery**:
- RTO (Recovery Time Objective) per environment
- RPO (Recovery Point Objective) per environment
- Backup schedules and retention
- Cross-region replication
- Failover procedures and testing
- Data archival policies

**Compliance & Regulatory**:
- PCI-DSS requirements for payment processing environments
- HIPAA for healthcare data environments
- SOC 2 Type II controls per environment
- GDPR data residency requirements
- ISO 27001 information security controls
- FedRAMP for government clouds

**Cost Management**:
- Cost allocation tags per environment
- Budget alerts and limits
- Reserved instances and savings plans allocation
- Spot instance usage per environment
- Auto-shutdown policies for non-production
- Cost optimization recommendations

**Promotion Pipelines**:
- Environment promotion flow (dev -> staging -> prod)
- Approval gates and reviewers
- Automated testing requirements per stage
- Canary analysis thresholds
- Rollback procedures
- Change management integration

**Service Level Objectives**:
- Availability SLOs per environment (99.9%, 99.95%, 99.99%)
- Latency SLOs per environment
- Error rate budgets
- Uptime windows and maintenance schedules
- Support tiers per environment

**GitOps Patterns**:
- Environment-specific Git branches or repositories
- ArgoCD Application per environment
- Flux Kustomization per environment
- Promotion automation with pull requests
- Environment drift detection

**Testing & Validation**:
- Smoke tests per environment
- Integration test suites
- Performance testing configurations
- Chaos engineering per environment
- Synthetic monitoring

**Reference**: Consult organizational platform engineering, cloud architecture, and compliance teams for detailed guidance on environment strategy and configuration standards

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
