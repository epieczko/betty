# Name: standard-operating-procedures

## Executive Summary

Standard Operating Procedures (SOPs) are comprehensive, step-by-step operational runbooks that document routine tasks, system maintenance activities, deployment procedures, and operational workflows for SRE and operations teams. These foundational documents ensure consistency, reduce errors, and accelerate onboarding by codifying best practices for recurring operational activities including system health checks, log rotation, certificate renewal, backup verification, capacity planning, and service provisioning.

Aligned with ITIL 4 Service Operation and Google SRE operational excellence principles, SOPs provide executable procedures for both manual and automated execution, identifying automation opportunities through repetitive task analysis. Each SOP follows a standardized format with clear prerequisites, step-by-step instructions, expected outcomes, error handling procedures, rollback steps, and success validation criteria, enabling any team member to execute operational tasks consistently and reliably.

### Strategic Importance

- **Operational Consistency**: Ensures tasks are performed identically regardless of which engineer executes them
- **Error Reduction**: Reduces human error by 60-80% through documented checklists and validation steps
- **Faster Onboarding**: Accelerates new engineer ramp-up from months to weeks with self-service runbooks
- **Automation Identification**: Highlights repetitive tasks as candidates for automation investment
- **Compliance**: Satisfies SOC 2, ISO 27001, and audit requirements for documented operational procedures
- **Knowledge Preservation**: Captures tribal knowledge from senior engineers in searchable, executable format
- **24/7 Operations**: Enables any on-call engineer to execute critical tasks without expert escalation

## Purpose & Scope

### Primary Purpose

This artifact provides standardized, step-by-step procedures for routine operational tasks, system maintenance, and administrative activities. It solves the problem of operational inconsistency by documenting repeatable processes in executable runbook format, enabling any qualified team member to perform critical tasks reliably without expert guidance or tribal knowledge.

### Scope

**In Scope**:
- System health checks and monitoring validation procedures
- Log rotation, cleanup, and archival procedures
- SSL/TLS certificate renewal and rotation
- Backup execution, verification, and restoration testing
- Database maintenance (vacuuming, index optimization, statistics updates)
- Capacity planning and resource provisioning
- Service provisioning and deprovisioning workflows
- User account management (creation, deletion, permission changes)
- Configuration management and change control procedures
- Scheduled maintenance window procedures
- System patching and update procedures
- Disaster recovery testing and validation
- On-call handoff checklists and procedures
- Monthly/quarterly operational review processes
- Automation opportunities and toil reduction identification

**Out of Scope**:
- Emergency incident response procedures (covered in playbooks artifact)
- Deployment and rollback procedures (covered in feature-rollback-playbooks)
- Post-incident analysis (covered in post-mortem-report artifact)
- Strategic planning and architecture decisions
- Custom application-specific procedures (maintained by dev teams)

### Target Audience

**Primary Audience**:
- Operations Engineers executing routine maintenance tasks
- SRE Teams performing system administration activities
- On-Call Engineers conducting regular health checks and operational tasks
- Junior Engineers learning operational procedures through self-service documentation

**Secondary Audience**:
- DevOps Engineers identifying automation opportunities from manual SOPs
- Engineering Managers understanding team operational workload and toil
- Compliance/Audit Teams validating documented operational procedures
- Platform Teams standardizing operational procedures across services

## Document Information

**Format**: Markdown

**File Pattern**: `*.standard-operating-procedures.md`

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

**Executable Format**: Write imperative, copy-paste ready commands; include exact syntax with expected output
**Prerequisites Clear**: List all prerequisites upfront (permissions, tools, access, dependencies)
**Step Numbering**: Use numbered steps for sequential procedures; makes progress tracking easy
**Validation Steps**: Include verification commands after each step to confirm success before proceeding
**Error Handling**: Document common errors, their causes, and resolution steps
**Time Estimates**: Provide expected execution time for procedure to set expectations
**Rollback Procedures**: Document how to undo changes if procedure fails or needs reversal
**Automation Flags**: Tag manual toil-heavy SOPs as automation candidates; track automation ROI
**Regular Testing**: Execute SOPs quarterly in non-prod to verify accuracy and identify drift
**Ownership Assignment**: Assign owner (DRI) to each SOP responsible for accuracy and updates
**Frequency Tagging**: Label SOPs by execution frequency (daily, weekly, monthly, quarterly, annual)
**Searchable Keywords**: Tag SOPs with relevant keywords for easy discovery (database, backup, certificate, etc.)
**Screenshots/Diagrams**: Include visual aids for UI-based procedures or complex architectures
**Assume Beginner**: Write for junior engineers; don't assume tribal knowledge or expert context
**Single Purpose**: One SOP per task; avoid combining multiple unrelated procedures
**Review Cadence**: Review SOPs semi-annually or when underlying systems change significantly
**Deprecation Process**: Archive outdated SOPs immediately when automated or no longer needed; don't leave stale docs

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

**Operational Excellence Frameworks**:
- ITIL 4 Service Operation (operational procedures and service desk)
- Google SRE Book (Chapter on Eliminating Toil, Automation)
- COBIT (Control Objectives for IT Operations)
- ISO/IEC 20000 Service Management System
- DevOps Handbook (operational excellence practices)

**Runbook & Documentation Formats**:
- Executable runbook format (step-by-step procedures)
- Checklists and validation steps
- Decision trees for conditional logic
- Flowcharts for complex workflows
- Copy-paste ready commands with syntax highlighting
- Expected output examples for validation

**Automation & Toil Reduction**:
- Google SRE Toil Definition (manual, repetitive, automatable, tactical, no enduring value)
- Toil budget targets (SRE should spend <50% time on toil)
- Automation ROI calculation (time saved × frequency)
- Runbook Automation platforms (PagerDuty, Rundeck, AWS Systems Manager)
- Infrastructure-as-Code (Terraform, Ansible, Puppet, Chef)
- Configuration Management (Ansible, SaltStack, Chef, Puppet)

**System Administration Categories**:
- Linux/Unix system administration procedures
- Windows Server administration procedures
- Database administration (PostgreSQL, MySQL, MongoDB, Redis)
- Kubernetes operations (pod management, node maintenance, cluster upgrades)
- Cloud platform operations (AWS, Azure, GCP)
- Network operations (DNS, load balancer, firewall configuration)
- Security operations (certificate management, access control, vulnerability patching)

**Maintenance & Housekeeping**:
- Log rotation and archival (logrotate, centralized logging)
- Disk space cleanup and monitoring
- Certificate renewal (Let's Encrypt, cert-manager, manual renewal)
- Backup verification and restoration testing
- Database vacuuming and optimization
- Cache invalidation and cleanup
- Deprecated resource cleanup

**Change Management**:
- ITIL Change Management (CAB approval, change windows)
- Change Advisory Board (CAB) procedures
- Maintenance window scheduling and communication
- Rollback procedures for operational changes
- Change success validation criteria

**Compliance & Audit**:
- SOC 2 Type II (documented operational procedures)
- ISO 27001 (operational controls documentation)
- PCI-DSS (system administration procedures)
- HIPAA (access control and administrative procedures)
- Segregation of duties (SoD) requirements

**Knowledge Management**:
- Runbook repositories (Confluence, Notion, GitHub Wiki)
- Searchable documentation platforms
- Procedure versioning and change tracking
- Regular review and update cycles
- Deprecated procedure archival

**SOP Content Categories**:
- Daily operational tasks (health checks, monitoring validation)
- Weekly tasks (log review, capacity planning)
- Monthly tasks (certificate checks, backup testing, security patching)
- Quarterly tasks (DR testing, access review, operational reviews)
- Annual tasks (architecture review, vendor assessment)

**Reference**: Consult SRE and operations leadership for SOP documentation standards

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
