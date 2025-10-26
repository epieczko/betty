# Name: offboarding-checklist

## Executive Summary

The Offboarding Checklist is a critical security and compliance deliverable that orchestrates immediate access revocation, knowledge transfer, and asset recovery when employees separate from the organization. This artifact ensures zero-delay deprovisioning through automated workflows in IAM platforms (Okta, Azure AD, SailPoint), HRIS-triggered termination events (Workday, BambooHR), and systematic account disablement across all enterprise applications.

The checklist covers voluntary resignations, involuntary terminations, and contractor end-of-engagement scenarios, ensuring consistent execution regardless of separation type. It coordinates cross-functional activities including IT access removal (immediate), manager-led knowledge transfer sessions, equipment return tracking, exit interview completion, and alumni network enrollment. The artifact maintains compliance with SOX ITGC controls for timely access revocation, supports forensic preservation requirements, and provides complete audit trails for regulatory examinations and security certifications.

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

This artifact serves as the authoritative framework for employee separation procedures, ensuring immediate access revocation, systematic knowledge transfer, complete asset recovery, and compliant offboarding processes. It protects organizational data, maintains business continuity, and ensures regulatory compliance during all employee departures.

### Scope

**In Scope**:
- Immediate access revocation (within 1 hour of notification for involuntary terminations)
- Automated account disablement via HRIS-triggered workflows
- Application-by-application access removal across SaaS and on-premise systems
- Email forwarding setup and mailbox archival procedures
- Knowledge transfer sessions and documentation handoffs
- Equipment return (laptop, mobile devices, security tokens, badges)
- Physical access revocation (building access, parking, key cards)
- Exit interview scheduling and completion tracking
- Final expense reimbursement and benefits coordination
- Alumni network enrollment and LinkedIn transition support
- Manager-led handoff of responsibilities and work-in-progress
- COBRA and benefits continuation information
- Retrieval of confidential documents and intellectual property
- Personal data removal per GDPR/privacy requirements
- License reclamation and cost optimization

**Out of Scope**:
- Legal proceedings related to termination disputes
- Detailed severance package negotiations
- HRIS payroll and final compensation calculations
- Long-term alumni engagement programs
- Rehire eligibility determinations and processes

### Target Audience

**Primary Audience**:
- HR Business Partners managing separations
- IT Operations teams executing access revocation
- IAM Administrators coordinating deprovisioning
- Hiring Managers facilitating knowledge transfer
- Security teams validating complete access removal

**Secondary Audience**:
- Legal and Compliance teams ensuring regulatory adherence
- Internal Audit reviewing offboarding controls
- Finance teams managing asset recovery and license reclamation
- Facilities teams coordinating physical access removal

## Document Information

**Format**: Markdown

**File Pattern**: `*.offboarding-checklist.md`

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

**Immediate Access Revocation**: Disable all accounts within 1 hour of involuntary termination notification; within 24 hours for voluntary resignations
**HRIS-Driven Automation**: Configure Workday or equivalent to automatically trigger deprovisioning workflows upon termination date
**Separation Type Classification**: Distinguish between voluntary, involuntary, contractor end-of-engagement, and executive departures with appropriate procedures
**Privileged Access Priority**: Immediately revoke privileged accounts, VPN access, and production system credentials before standard application access
**Email Continuity**: Set up email forwarding to manager with auto-reply message; archive mailbox per retention policy
**Knowledge Transfer Requirements**: Mandate documented handoff sessions 2 weeks before departure date for critical roles
**Equipment Recovery Tracking**: Use asset management system to track all issued equipment and verify 100% return
**Exit Interview Completion**: Schedule within final week; capture feedback on experience, reasons for departure, and improvement suggestions
**Alumni Network Enrollment**: Offer enrollment in alumni programs for eligible departures to maintain talent pipeline
**License Reclamation**: Immediately reclaim SaaS licenses to optimize costs; track in license management platform
**Physical Security Coordination**: Notify facilities and security teams same-day to disable badge access and retrieve credentials
**Legal Hold Preservation**: Before any data deletion, verify no active litigation holds or eDiscovery requirements
**Manager Enablement**: Provide managers with offboarding playbooks and 1-week advance notice when possible
**Audit Trail Documentation**: Maintain timestamped records of all deprovisioning actions for compliance verification
**Access Certification Cleanup**: Remove terminated users from quarterly access reviews and certification campaigns
**Shared Account Rotation**: Rotate passwords for any shared accounts the departing employee had access to
**Data Migration Ownership**: Transfer ownership of critical files, folders, and documents to designated successors
**Compliance Validation**: Conduct post-termination access review 7 days after departure to verify complete removal
**Graceful Degradation**: For planned departures, implement phased access removal to maintain productivity through final day
**Metrics and Monitoring**: Track offboarding completion rate, time-to-full-removal, equipment recovery rate, and exit interview participation

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

**Identity & Access Management**:
- Okta Workflows for automated deprovisioning on termination events
- Azure AD Lifecycle Workflows for leaver processes
- SailPoint IdentityIQ termination workflows and certification
- Saviynt IGA for access removal orchestration
- CyberArk for privileged account deprovisioning
- SCIM 2.0 for automated account deactivation
- Active Directory account disablement and OU moves
- Google Workspace offboarding automation
- Microsoft 365 retention and eDiscovery holds
- Conditional Access policies for immediate blocking

**HRIS Integration**:
- Workday termination event triggers for downstream systems
- BambooHR offboarding workflows and integrations
- ADP Workforce Now separation processing
- UKG Pro termination notifications
- SuccessFactors Employee Central offboarding
- PeopleSoft HRMS deprovisioning triggers

**ITSM & Automation**:
- ServiceNow HR Service Delivery offboarding cases
- Jira Service Management termination workflows
- PagerDuty on-call rotation removal
- Slack workspace deactivation
- Microsoft Teams guest access removal
- Zoom account deprovisioning

**Asset Management**:
- Jamf Pro for Mac device lock and wipe
- Microsoft Intune for mobile device management
- Workspace ONE for device decommissioning
- ServiceNow Asset Management for equipment tracking
- Atlassian Asset Discovery for license reclamation
- Snow Software for license optimization

**Data Retention & eDiscovery**:
- Microsoft 365 Litigation Hold procedures
- Google Vault for email preservation
- Mailbox archival and forwarding setup
- SharePoint/OneDrive data migration
- Slack export and archival
- Box and Dropbox folder ownership transfer

**Compliance & Security Standards**:
- SOC 2 CC6.1 (Logical Access Controls - Terminations)
- ISO 27001 A.9.2.6 (Removal of Access Rights)
- SOX ITGC controls for timely access revocation
- NIST SP 800-53 AC-2(3) (Account Disablement)
- CIS Controls v8 - Control 5.5 (Account Deactivation)
- GDPR Article 17 (Right to Erasure) for personal data
- PCI DSS Requirement 8.1.4 (Remove terminated user access)
- HIPAA 164.308(a)(3)(ii)(C) (Termination Procedures)
- COBIT 2019 DSS05.05 (Manage User Accounts)
- Federal Rules of Civil Procedure (FRCP) for legal holds

**Knowledge Management**:
- Confluence knowledge transfer templates
- SharePoint runbook documentation handoffs
- README maintenance for code repositories
- Tribal knowledge capture procedures
- Work-in-progress transition plans

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
