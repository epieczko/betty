# Name: onboarding-checklist

## Executive Summary

The Onboarding Checklist is a critical deliverable for automating and standardizing employee onboarding through Identity and Access Management (IAM) platforms. This artifact orchestrates Day 1 access provisioning using SCIM 2.0 automation, integrates with HR systems like Workday and BambooHR for Joiner/Mover/Leaver (JML) workflows, and leverages platforms such as Okta Workflows, Azure AD Lifecycle Management, and SailPoint IdentityIQ to ensure zero-touch provisioning.

The checklist spans pre-boarding through 90-day milestones, covering account creation, application access, hardware provisioning, security training completion, and manager-led onboarding activities. It integrates with ITSM platforms (ServiceNow, Jira Service Management) for ticket automation, establishes buddy system assignments, and tracks completion of mandatory compliance training. The artifact supports SOX ITGC controls for segregation of duties validation and provides audit trails for access certification compliance.

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

This artifact serves as the comprehensive framework for employee onboarding automation and manual activities, ensuring Day 1 access provisioning, systematic application access grants, hardware setup, training curriculum completion, and 30-60-90 day milestone tracking. It standardizes the onboarding experience while enabling role-based customization and automated workflow orchestration.

### Scope

**In Scope**:
- Pre-boarding activities (offer acceptance to Day 1)
- SCIM-based account provisioning to directory services (Active Directory, Azure AD, Okta)
- Application access requests via IGA platforms (SailPoint, Saviynt, CyberArk)
- Hardware procurement and configuration (laptop, mobile device, peripherals)
- Physical access provisioning (building badges, parking, key cards)
- Security awareness training and compliance certifications
- Manager-led orientation and buddy system assignments
- 30-60-90 day check-ins and milestone reviews
- Integration with HRIS (Workday, BambooHR, ADP) for automated triggers
- ServiceNow/Jira ticket creation and tracking
- Role-based access templates and provisioning profiles

**Out of Scope**:
- Offboarding and termination procedures (see offboarding-checklist)
- Detailed application-specific training curricula
- Performance management and goal setting processes
- Compensation and benefits administration
- Organizational change management for restructures

### Target Audience

**Primary Audience**:
- IT Operations teams responsible for access provisioning
- HR Business Partners and People Operations teams
- IAM Administrators managing identity lifecycle
- Hiring Managers coordinating team onboarding
- Help Desk teams handling access requests

**Secondary Audience**:
- Security teams validating access controls
- Compliance teams auditing onboarding processes
- Internal Audit for SOX ITGC reviews
- New employees as self-service checklist reference

## Document Information

**Format**: Markdown

**File Pattern**: `*.onboarding-checklist.md`

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

**Automation-First Approach**: Leverage SCIM 2.0 and automated workflows to eliminate manual provisioning; aim for 90%+ zero-touch onboarding
**HRIS as Source of Truth**: Configure Workday, BambooHR, or equivalent as authoritative source triggering all downstream provisioning
**Pre-Boarding Excellence**: Initiate account creation and hardware procurement 5-7 days before start date to ensure Day 1 readiness
**Role-Based Templates**: Create provisioning profiles by role/department to standardize access patterns and reduce manual decision-making
**Manager Self-Service**: Empower hiring managers with self-service portals for non-standard access requests and onboarding customization
**Buddy System Integration**: Systematically assign onboarding buddies through automated matching based on role, location, and experience
**30-60-90 Day Milestones**: Structure check-ins at 30, 60, and 90 days with automated reminders and completion tracking
**Compliance-First Training**: Require security awareness, data privacy, and code of conduct training completion before application access grants
**Hardware Pre-Configuration**: Deploy standardized SOE (Standard Operating Environment) images with pre-installed applications
**Mobile Device Management**: Enroll mobile devices in MDM (Intune, Jamf, Workspace ONE) during Day 1 setup
**Access Validation**: Implement manager attestation within first 30 days to validate access appropriateness
**Feedback Loops**: Collect new hire feedback at 30 and 90 days to continuously improve onboarding experience
**Audit Trail Retention**: Maintain complete audit logs of all provisioning actions for compliance and troubleshooting
**Segregation of Duties**: Validate SOD conflicts during provisioning using IGA platform rules
**Version Control**: Store checklist templates in Git with versioning for rollback capability
**Metrics Tracking**: Monitor time-to-productivity, Day 1 readiness rate, provisioning SLA compliance, and new hire satisfaction
**Integration Testing**: Validate all HRIS-to-IAM integrations in staging before production deployment
**Exception Handling**: Define escalation paths for non-standard access requests requiring approval workflow
**Documentation Currency**: Update onboarding procedures within 30 days of system or process changes
**Stakeholder Alignment**: Quarterly reviews with HR, IT, Security, and Compliance to ensure continued alignment

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
- SCIM 2.0 (System for Cross-domain Identity Management) for automated provisioning
- Okta Workflows for JML (Joiner/Mover/Leaver) automation
- Azure AD Lifecycle Workflows and Entitlement Management
- SailPoint IdentityIQ and IdentityNow for IGA
- Saviynt Enterprise Identity Cloud
- CyberArk Identity for privileged access onboarding
- Workday HCM integration for HRIS-driven provisioning
- BambooHR API for employee data synchronization
- OneLogin lifecycle management
- Auth0 B2E (Business to Employee) identity
- JumpCloud directory-as-a-service onboarding
- SAML 2.0 and OAuth 2.0 for SSO enablement
- RBAC (Role-Based Access Control) frameworks
- ABAC (Attribute-Based Access Control) models
- Least Privilege Access principles

**ITSM & Workflow Automation**:
- ServiceNow Employee Center and HRSD modules
- Jira Service Management for onboarding workflows
- Workato and Tray.io for integration automation
- Microsoft Power Automate for provisioning orchestration
- Zapier for SaaS application integrations
- PagerDuty for escalation workflows

**HR Systems & Platforms**:
- Workday HCM as authoritative source
- BambooHR for SMB onboarding
- ADP Workforce Now integration
- UltiPro/UKG Pro for enterprise HR
- SuccessFactors Employee Central
- Greenhouse and Lever ATS integration
- 30-60-90 day plan frameworks
- New hire orientation best practices

**Training & Compliance**:
- KnowBe4 for security awareness training
- SANS Security Awareness for technical roles
- Compliance training platforms (Ethena, Navex)
- LMS integration (Cornerstone, Docebo, TalentLMS)
- SOC 2 CC6.1 (Logical Access Controls)
- GDPR Article 32 (Security of Processing)
- NIST SP 800-53 AC-2 (Account Management)

**Access Control Standards**:
- ISO 27001 A.9.2.1 (User Registration and De-registration)
- ISO 27001 A.9.2.2 (User Access Provisioning)
- SOX ITGC controls for access management
- NIST Cybersecurity Framework PR.AC (Identity Management)
- CIS Controls v8 - Control 5 (Account Management)
- COBIT 2019 DSS05.04 (Manage User Identity and Access)

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
