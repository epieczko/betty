# Name: physical-architecture-diagram

## Executive Summary

The Physical Architecture Diagram is a critical technical artifact that documents the actual deployment topology, infrastructure components, network configuration, and physical/virtual resource allocation for a system. Using industry-standard notations (UML Deployment Diagrams, ArchiMate Technology Layer, C4 Deployment diagrams), it shows how logical components map to physical infrastructure across data centers, cloud platforms, and edge locations.

As an essential element of infrastructure planning and operations, this diagram bridges architecture design and implementation by specifying server instances, containers, network zones, storage systems, and hardware dependencies. It supports capacity planning, disaster recovery design, security zone definition, and infrastructure-as-code (IaC) implementation using tools like Terraform, CloudFormation, or Bicep.

### Strategic Importance

- **Infrastructure Planning**: Enables capacity planning, cost estimation, and resource allocation across on-premises, cloud (AWS, Azure, GCP), and hybrid environments
- **Deployment Automation**: Provides blueprint for infrastructure-as-code implementation using Terraform, Pulumi, CloudFormation, ARM Templates, or Ansible
- **Operations Readiness**: Supports SRE teams, platform engineers, and operations staff in understanding physical topology, dependencies, and failover scenarios
- **Compliance & Security**: Documents security zones, network segmentation, DMZs, and compliance boundary definitions for audit and regulatory requirements
- **Cost Optimization**: Facilitates right-sizing analysis, reserved instance planning, and multi-region deployment strategies

## Purpose & Scope

### Primary Purpose

This artifact documents the physical deployment architecture using UML Deployment Diagrams, C4 Deployment diagrams, or cloud-specific architecture diagrams (AWS Architecture Diagrams, Azure Architecture Icons, GCP Architecture Diagramming Tool). Created using Lucidchart, draw.io, CloudCraft, or diagrams-as-code tools (Diagrams.py, CloudFormation Designer), it specifies servers, containers, networks, storage, and infrastructure services to guide deployment and operations.

### Scope

**In Scope**:
- Physical and virtual server topology: EC2 instances, Azure VMs, GCE instances, on-premises servers, container hosts (ECS, AKS, GKE, Kubernetes)
- Network architecture: VPCs, subnets, availability zones, regions, network security groups, load balancers (ALB, NLB, Azure Load Balancer, Cloud Load Balancing)
- Storage infrastructure: Block storage (EBS, Azure Disks), object storage (S3, Azure Blob, GCS), file systems (EFS, Azure Files), databases (RDS, Cosmos DB, Cloud SQL)
- Container orchestration: Kubernetes clusters, Docker Swarm, ECS/Fargate, AKS, GKE, OpenShift topology
- Infrastructure services: API Gateways, message queues (SQS, Service Bus, Pub/Sub), caching (ElastiCache, Redis Cache), CDN (CloudFront, Azure CDN)
- Deployment zones: Production, staging, development, DR sites, multi-region configurations
- Infrastructure-as-Code mappings: Terraform modules, CloudFormation stacks, ARM templates, Bicep, Pulumi projects

**Out of Scope**:
- Logical component design and service boundaries (see Logical Architecture Diagram)
- Application code structure and internal component details (see Component Diagrams)
- Detailed security controls and encryption mechanisms (see Security Architecture Diagram)
- Network packet flows and protocol details (see Network Architecture Diagram)
- CI/CD pipeline configuration (see Deployment Pipeline documentation)

### Target Audience

**Primary Audience**:
- Platform Engineers and SREs managing infrastructure provisioning, scaling, and reliability
- Cloud Architects designing multi-cloud, hybrid, or cloud-native infrastructure on AWS, Azure, GCP
- Infrastructure Engineers implementing infrastructure-as-code using Terraform, Pulumi, CloudFormation, or Ansible

**Secondary Audience**:
- DevOps Engineers configuring deployment automation and container orchestration
- Security Architects validating network segmentation, security zones, and compliance boundaries
- FinOps teams analyzing cloud costs, reserved capacity, and resource optimization opportunities

## Document Information

**Format**: Multiple

**File Pattern**: `*.physical-architecture-diagram.*`

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

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use approved templates to ensure completeness and consistency across teams
**Peer Review**: Have at least one qualified peer review before submitting for approval
**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management
**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in
**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon
**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively
**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation
**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes
**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats
**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates
**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy

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

**Architecture Frameworks & Standards**:
- TOGAF 10 ADM Phase D: Technology Architecture - Physical infrastructure and deployment architecture
- ArchiMate 3.1 Technology Layer - Infrastructure modeling including devices, networks, system software
- C4 Model Level 4: Deployment Diagrams - System landscape and deployment topology
- ISO/IEC/IEEE 42010 - Architecture description standards for deployment views
- AWS Well-Architected Framework - Reliability, Performance Efficiency, Cost Optimization pillars
- Microsoft Azure Architecture Framework - Operational excellence and infrastructure design
- Google Cloud Architecture Framework - Infrastructure and deployment best practices

**Diagramming Notations & Tools**:
- UML 2.5 Deployment Diagrams - Nodes, artifacts, and deployment specifications
- ArchiMate 3.1 Notation - Technology layer elements (device, node, network, path)
- C4 Deployment Diagrams - Deployment nodes and containerization topology
- AWS Architecture Icons - Official AWS service icons for architecture diagrams
- Azure Architecture Icons - Microsoft Azure service symbols and patterns
- GCP Architecture Diagramming Tool - Google Cloud architecture visualization icons
- Lucidchart - Cloud architecture templates for AWS, Azure, GCP with official icon sets
- draw.io / diagrams.net - Cloud architecture shape libraries and templates
- CloudCraft - 3D cloud architecture designer for AWS with cost estimation
- Diagrams (diagrams.py) - Python-based diagrams-as-code for cloud architectures

**Cloud Platforms & Services**:
- Amazon Web Services (AWS) - EC2, ECS, EKS, Lambda, RDS, S3, VPC, CloudFormation, AWS CDK
- Microsoft Azure - Virtual Machines, AKS, Azure Functions, Cosmos DB, Azure Resource Manager, Bicep
- Google Cloud Platform (GCP) - Compute Engine, GKE, Cloud Functions, Cloud SQL, Deployment Manager
- Kubernetes - Container orchestration platform for cloud-native deployments (CNCF)
- OpenShift - Enterprise Kubernetes platform (Red Hat)
- VMware vSphere - Virtualization platform for on-premises infrastructure

**Infrastructure-as-Code (IaC) Tools**:
- Terraform / OpenTofu - Multi-cloud infrastructure provisioning with HCL declarative language
- AWS CloudFormation - AWS-native infrastructure templates in JSON/YAML
- Azure Resource Manager (ARM) Templates - Azure infrastructure deployment templates
- Bicep - Domain-specific language for Azure resource deployment
- Pulumi - Multi-cloud IaC with general-purpose programming languages (TypeScript, Python, Go, C#)
- Ansible - Configuration management and infrastructure automation with YAML playbooks
- Chef / Puppet - Infrastructure configuration management and automation

**Container & Orchestration Platforms**:
- Docker - Container runtime and image management
- Kubernetes - Container orchestration (deployment, scaling, networking, storage)
- Amazon ECS / Fargate - AWS container orchestration services
- Azure Kubernetes Service (AKS) - Managed Kubernetes on Azure
- Google Kubernetes Engine (GKE) - Managed Kubernetes on GCP
- Docker Swarm - Native Docker clustering and orchestration
- HashiCorp Nomad - Workload orchestrator for containers and non-containerized applications

**Monitoring & Observability**:
- Prometheus - Time-series metrics collection and monitoring
- Grafana - Metrics visualization and dashboards
- Datadog - Cloud-scale monitoring and observability platform
- New Relic - Application performance monitoring (APM) and infrastructure monitoring
- AWS CloudWatch - AWS-native monitoring and logging
- Azure Monitor - Azure monitoring, metrics, and log analytics
- Google Cloud Operations (formerly Stackdriver) - GCP monitoring and logging

**Reference**: Consult organizational architecture, cloud platform, and infrastructure teams for detailed guidance on cloud provider selection, infrastructure-as-code standards, and deployment architecture patterns for your specific environment

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
