# Name: ownership-charters

## Executive Summary

The Ownership Charters artifact defines clear service and component ownership responsibilities across engineering teams, establishing accountability for system reliability, feature development, and operational excellence. This critical governance document specifies which teams own which services, their operational responsibilities under the "You Build It You Run It" DevOps model, and their commitments to Service Level Objectives (SLOs), incident response, and continuous improvement.

Grounded in DORA DevOps capabilities and SRE principles, ownership charters eliminate ambiguity about who is accountable for each service's health, security, and evolution. They define escalation paths using RACI matrices, establish on-call rotations, and clarify the boundaries between platform teams providing capabilities and stream-aligned teams consuming them, enabling high-performing organizations to achieve elite DORA metrics through clear accountability.

### Strategic Importance

- **Clear Accountability**: Eliminates ambiguity about service ownership and operational responsibilities
- **You Build It You Run It**: Establishes DevOps accountability for teams owning their services end-to-end
- **SLO Ownership**: Defines which teams are accountable for service-level objectives and error budgets
- **Escalation Clarity**: Specifies incident response paths and on-call rotation responsibilities
- **DORA Capabilities**: Supports deployment frequency, lead time, MTTR, and change failure rate improvement
- **Platform Service Boundaries**: Clarifies what platform teams provide vs. what stream-aligned teams own

## Purpose & Scope

### Primary Purpose

This artifact establishes clear ownership for services, components, and systems across the organization, defining accountability for development, operations, reliability, security, and continuous improvement. It enables autonomous teams by clarifying responsibilities and eliminating ownership gaps that cause incidents and delays.

### Scope

**In Scope**:
- Service ownership mapping: which team owns each microservice, application, or component
- Operational accountability: on-call rotations, incident response, SLO ownership
- DORA DevOps capabilities: deployment responsibility, infrastructure ownership
- SRE responsibilities: error budget management, toil reduction, reliability improvements
- Security ownership: vulnerability remediation, compliance, security controls per service
- Platform service catalogs: what capabilities platform teams provide and support
- Escalation paths: primary owner, secondary support, subject matter expert contacts
- Component lifecycle ownership: development, deployment, monitoring, decommissioning
- Documentation responsibilities: runbooks, architecture diagrams, API documentation

**Out of Scope**:
- Team topology and interaction modes (see team-topology-map)
- Cross-functional RACI for initiatives or projects (see raci-per-workstream)
- Individual skill development and competencies (see skills-matrix)
- Time allocation across project/BAU/toil (see time-allocation-worksheets)
- Strategic initiative governance (see initiative-charter)

### Target Audience

**Primary Audience**:
- Engineering Managers defining service ownership and accountability
- Team Leads understanding their team's operational responsibilities
- SRE and Operations teams coordinating incident response and on-call rotations
- Platform Engineering teams publishing service catalogs and support models

**Secondary Audience**:
- Product Leaders understanding which teams can deliver features for specific services
- Security teams identifying security ownership and vulnerability remediation paths
- Compliance teams verifying control ownership for audit purposes
- HR/People Teams supporting on-call compensation and workload management

## Document Information

**Format**: Markdown

**File Pattern**: `*.ownership-charters.md`

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

**Ownership Assignment Principles**:
- **Single Team Accountability**: Each service should have exactly one team as primary owner
- **You Build It You Run It**: Teams that develop services should operate them in production
- **Avoid Gaps**: Every service, component, and infrastructure element must have a clear owner
- **Minimize Shared Ownership**: Shared ownership dilutes accountability; prefer clear boundaries
- **Platform Service Catalog**: Platform teams publish explicit service catalogs with support models
- **Escalation Path Clarity**: Define primary owner, secondary support, and subject matter experts

**SRE and Operational Excellence**:
- **SLO Ownership**: Each service owner defines and monitors SLOs (availability, latency, error rate)
- **Error Budget Management**: Teams balance feature velocity against reliability using error budgets
- **Toil Budget**: Keep toil under 50% per Google SRE; automate repetitive operational work
- **On-Call Rotation**: Implement sustainable on-call (weekly rotations, follow-the-sun for global teams)
- **Production Readiness**: Define ownership criteria before services go to production
- **Runbook Maintenance**: Service owners maintain up-to-date incident response procedures

**DORA Capabilities and Metrics**:
- **Deployment Ownership**: Teams own their CI/CD pipelines and deployment process
- **Lead Time Accountability**: Track and improve lead time for changes per service
- **MTTR Responsibility**: Service owners accountable for mean time to recovery
- **Change Failure Rate**: Teams monitor and reduce deployment failures
- **Continuous Improvement**: Regularly review DORA metrics and improve capabilities

**Incident Management Best Practices**:
- **Clear Escalation**: Document primary on-call, secondary backup, manager escalation
- **Severity Definitions**: Align on P0/P1/P2/P3 severity levels and response times
- **Incident Commander Role**: Designate who leads major incidents per service
- **Blameless Postmortems**: Conduct learning-focused postmortems without blame
- **Follow-up Action Ownership**: Assign owners to postmortem action items

**Platform and Service Boundaries**:
- **Service Catalog**: Publish what platform teams provide and support levels
- **Golden Paths**: Define recommended, well-supported approaches platform teams maintain
- **Self-Service Model**: Enable stream-aligned teams to operate independently
- **Shared Responsibility**: Clarify platform vs. application team accountability
- **Platform SLOs**: Platform teams maintain SLOs for their internal services

**Security and Compliance Ownership**:
- **Vulnerability Remediation**: Assign ownership for patching and remediation SLAs
- **Security Champions**: Embed security ownership within each team
- **Compliance Controls**: Map SOC 2, ISO 27001, PCI controls to owning teams
- **Data Ownership**: Clarify who owns sensitive data and compliance requirements
- **Secrets Management**: Define ownership for rotating keys and managing secrets

**Documentation and Communication**:
- **Service Registry**: Maintain centralized registry of services and owners (ServiceNow, Backstage)
- **Contact Information**: Keep on-call contacts, Slack channels, and escalation paths current
- **Ownership Changes**: Communicate ownership transfers clearly with transition plans
- **Runbook Standards**: Standardize runbook format and maintenance cadence
- **Architecture Diagrams**: Keep system diagrams current showing ownership boundaries

**Version Control**: Store ownership charters in Git alongside service code for versioning
**Regular Review**: Update ownership quarterly or when organizational changes occur
**Metrics Tracking**: Monitor on-call load, incident volume, toil percentage by owner
**Accountability Reviews**: Regularly review service health and ownership effectiveness
**Transition Support**: Provide adequate transition period when changing ownership

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

**DevOps and SRE Principles**:
- DORA DevOps capabilities: deployment frequency, lead time, MTTR, change failure rate
- You Build It You Run It: teams owning full lifecycle of their services
- SRE principles: error budgets, SLOs/SLIs, toil reduction, capacity planning
- Error budget policy: how teams balance reliability and feature velocity
- Service Level Objectives (SLOs): ownership of availability, latency, error rate targets
- Service Level Indicators (SLIs): metrics teams are accountable for
- Toil tracking and automation: keeping toil under 50% per Google SRE

**Ownership and Accountability Models**:
- RACI matrix: Responsible, Accountable, Consulted, Informed for services
- RAPID (Bain): Recommend, Agree, Perform, Input, Decide decision framework
- DACI (Intuit): Driver, Approver, Contributor, Informed model
- Responsibility Assignment Matrix (RAM): mapping work to owners
- Service ownership model: single team accountable for service health
- Shared responsibility model: platform vs. application team boundaries

**Incident Management and On-Call**:
- Incident Command System (ICS): incident commander, ops lead, communications
- PagerDuty escalation policies: primary, secondary, and manager escalation
- Follow-the-sun support models for global teams
- On-call rotation best practices: weekly rotations, backup coverage
- Blameless postmortem culture: learning from incidents without blame
- Severity level definitions: P0/P1/P2/P3 incident classification
- Mean Time to Acknowledge (MTTA) and Mean Time to Resolve (MTTR) ownership

**Platform Engineering Patterns**:
- Internal Developer Platform (IDP): platform team service catalog
- Thinnest Viable Platform: right-sizing platform capabilities
- Platform-as-a-Product: treating platform as product with internal customers
- Self-service infrastructure: empowering stream-aligned teams
- Golden paths: opinionated, well-supported patterns for common tasks
- Platform engineering team models: centralized, federated, hybrid

**DORA State of DevOps Capabilities**:
- Continuous delivery capabilities: version control, deployment automation, trunk-based development
- Architecture capabilities: loosely coupled architecture, teams can choose tools
- Product and process capabilities: customer feedback loops, work visibility
- Lean management: WIP limits, visual management, process improvement
- Monitoring and observability: proactive monitoring, distributed tracing ownership
- Database change management: automated database deployments

**Service Catalog and CMDB**:
- ITIL Service Catalog: catalog of IT services and ownership
- Configuration Management Database (CMDB): tracking service components and owners
- Service portfolio management: investment in services by ownership
- Application Portfolio Management (APM): rationalizing application ownership
- Technology Business Management (TBM): cost allocation by service owner

**Reliability Engineering**:
- Chaos Engineering: ownership of resilience testing
- Disaster Recovery (DR) and Business Continuity (BC) ownership
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) accountability
- Site Reliability Engineering (SRE) team structures
- Reliability budgets and error budgets
- Production Readiness Reviews (PRR): ownership of production criteria

**Security and Compliance Ownership**:
- Secure Software Development Lifecycle (SSDLC): security ownership per phase
- Vulnerability management: remediation SLAs by severity and owner
- Security champions program: embedded security ownership in teams
- Compliance controls ownership: SOC 2, ISO 27001, PCI-DSS control owners
- Data classification and handling: data owner responsibilities
- Secrets management and key rotation ownership

**Documentation and Knowledge Management**:
- Runbook ownership: who maintains operational procedures
- Architecture Decision Records (ADRs): decision documentation accountability
- API documentation standards: OpenAPI/Swagger ownership
- System diagrams and documentation: C4 model, architecture diagrams
- Knowledge base and wiki ownership: team responsibility for documentation
- On-call playbooks: incident response procedure ownership

**Metrics and Performance Management**:
- Service performance metrics: latency, throughput, error rates
- Cost allocation and FinOps: cloud cost ownership by team/service
- Technical debt tracking: ownership of debt reduction
- DORA metrics tracking: deployment frequency, lead time ownership per team
- Team health metrics: on-call load, toil percentage, incident volume

**Related Standards**:
- ISO 9001: Quality management and process ownership
- ISO 27001: Information security management system ownership
- ITIL 4: Service management ownership and accountability
- COBIT: IT governance and control ownership
- SOC 2 Type II: Control ownership and evidence collection

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
