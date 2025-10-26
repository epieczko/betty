# Name: joiner-mover-leaver-workflows

## Executive Summary

The Joiner-Mover-Leaver (JML) Workflows artifact documents automated identity lifecycle management processes for employee onboarding (joiners), role changes (movers), and offboarding (leavers). This artifact specifies HR-driven IAM provisioning/deprovisioning workflows using Okta Workflows, Azure AD Lifecycle Workflows, SailPoint IdentityIQ, Saviynt, or custom SCIM-based integrations that automatically provision accounts, assign group memberships, grant application access, and revoke permissions based on HR events.

As organizations mature their identity governance programs, this artifact serves IAM Administrators implementing automated provisioning, Security teams ensuring access control and zero-trust principles, Compliance teams maintaining least-privilege access and audit trails, and IT Service Management teams reducing manual account management overhead. It transforms manual, error-prone identity processes into automated, policy-driven workflows with comprehensive audit logging for compliance, security, and operational efficiency.

### Strategic Importance

- **Identity Automation**: Implements automated user provisioning/deprovisioning using Okta Workflows, Azure AD Lifecycle, SailPoint IdentityIQ, Saviynt, or custom SCIM integrations
- **HR Integration**: Integrates with HRIS systems (Workday, SuccessFactors, BambooHR, ADP) to trigger workflows on hire, transfer, termination events
- **Access Provisioning**: Automatically provisions accounts (Active Directory, Google Workspace, Okta, Azure AD), assigns group memberships, grants application access based on role
- **Role-Based Access**: Implements RBAC with role templates, department-based access, manager-based provisioning, temporary elevated access
- **Offboarding Security**: Ensures timely deprovisioning on termination, disables accounts immediately, revokes VPN/SSO access, retrieves hardware, transfers data ownership
- **Compliance & Audit**: Maintains complete audit trail for SOX, SOC 2, ISO 27001, supports access reviews, attestation campaigns, separation of duties enforcement
- **Zero-Trust Principles**: Implements least-privilege access, just-in-time provisioning, time-bound access, continuous verification

## Purpose & Scope

### Primary Purpose

This artifact documents automated identity lifecycle workflows for joiners (new hires), movers (role changes), and leavers (terminations) using IAM platforms like Okta, Azure AD, SailPoint, or Saviynt. It specifies HR system integration, provisioning logic, access assignment rules, and deprovisioning procedures to ensure secure, compliant, and efficient identity management.

### Scope

**In Scope**:
- Joiner workflows: Pre-boarding (provision accounts before start date), onboarding (first-day access), role-based provisioning, manager approval
- HRIS integration: Workday, SuccessFactors, BambooHR, ADP webhooks/APIs triggering IAM workflows
- Account provisioning: Active Directory, Azure AD, Google Workspace, Okta, AWS IAM, SaaS applications via SCIM 2.0
- Access assignment: RBAC role templates, group memberships (AD groups, Okta groups), application entitlements, license assignment
- Mover workflows: Department transfer, role change, manager change triggering access re-evaluation, temporary access elevation
- Leaver workflows: Immediate account disable, access revocation, VPN/SSO termination, email forwarding, data transfer, hardware return
- Automated provisioning: SCIM 2.0 protocol, API-based provisioning, directory sync, JIT (just-in-time) provisioning
- Approval workflows: Manager approval, IT approval, security review for privileged access, exception requests
- Access reviews: Periodic certification, manager attestation, orphaned account cleanup, dormant account detection
- Audit logging: Complete provisioning/deprovisioning history, approval evidence, access change tracking

**Out of Scope**:
- Application-specific access controls (covered in Application Security artifacts)
- Privileged access management (PAM) for admin accounts (covered in PAM artifacts)
- Identity federation and SSO configuration (covered in SSO/SAML artifacts)
- Password policies and MFA configuration (covered in Authentication artifacts)

### Target Audience

**Primary Audience**:
- IAM Administrators implementing and maintaining JML workflows
- IT Service Management teams handling onboarding/offboarding tickets
- Security teams ensuring access control and zero-trust implementation

**Secondary Audience**:
- Compliance teams auditing access provisioning and reviews
- HR teams understanding IAM integration touchpoints
- Application owners managing application access provisioning

## Document Information

**Format**: Markdown

**File Pattern**: `*.joiner-mover-leaver-workflows.md`

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

**Automated Provisioning**: Automate 90%+ of standard access provisioning, use SCIM 2.0 for SaaS apps, reduce manual ticket handling
**HR as Source of Truth**: Use HRIS (Workday, SuccessFactors) as authoritative source for user attributes, trigger workflows on HR events
**Immediate Deprovisioning**: Disable accounts within 1 hour of termination notification, revoke VPN/SSO access immediately
**Role-Based Access**: Define RBAC role templates by job function, automatically assign based on department/title, minimize custom access
**Least Privilege**: Provision minimum required access, implement time-bound elevated access, require justification for privileged accounts
**Pre-boarding**: Provision accounts 1-2 days before start date, ensure first-day access ready, send welcome email with login instructions
**Mover Efficiency**: Automatically re-evaluate access on role change, remove old access, add new access, notify manager of changes
**Approval Workflows**: Require manager approval for non-standard access, implement four-eyes for privileged access, log all approvals
**Regular Access Reviews**: Quarterly manager attestation, annual comprehensive review, automated orphaned account detection
**Audit Trail**: Log all provisioning/deprovisioning events with timestamp, actor, reason, maintain audit logs for 7 years
**Exception Handling**: Define exception process for urgent access, require justification, set expiration, review regularly
**Testing**: Test workflows in non-production, validate provisioning accuracy, ensure deprovisioning completeness
**Monitoring**: Track provisioning SLAs, deprovisioning compliance, workflow failures, access review completion rates

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

**IAM Platforms**:
- Okta Workflows - Low-code automation for identity workflows
- Azure AD Lifecycle Workflows - Microsoft identity lifecycle management
- SailPoint IdentityIQ - Enterprise identity governance and administration (IGA)
- Saviynt - Cloud-native IGA platform
- CyberArk Identity - Identity security and governance
- ForgeRock Identity Platform - Full-stack identity and access management
- Ping Identity - Intelligent identity solutions
- OneLogin - Cloud-based IAM
- JumpCloud - Directory-as-a-Service with lifecycle management

**HRIS Systems**:
- Workday - Cloud-based HCM system
- SAP SuccessFactors - HR management suite
- BambooHR - HR software for small/medium businesses
- ADP Workforce Now - Payroll and HR management
- UKG (Ultimate Kronos Group) - HR and workforce management
- Oracle HCM Cloud - Human capital management
- Namely - HR platform with HRIS integration

**Provisioning Standards**:
- SCIM 2.0 (System for Cross-domain Identity Management) - Standard protocol for user provisioning
- SAML 2.0 - Identity federation standard
- OAuth 2.0 / OpenID Connect - Authorization and authentication
- LDAP - Directory access protocol
- API-based provisioning - REST APIs for custom integrations
- Just-in-Time (JIT) provisioning - Real-time account creation on first login

**Directory Services**:
- Active Directory (AD) - Microsoft on-premises directory
- Azure Active Directory (Azure AD / Entra ID) - Cloud identity service
- Google Workspace Directory - Google cloud directory
- Okta Universal Directory - Cloud directory service
- AWS IAM Identity Center (formerly SSO) - Centralized AWS access

**Access Governance**:
- Role-Based Access Control (RBAC) - Role assignment framework
- Attribute-Based Access Control (ABAC) - Policy-based access
- Access certification campaigns - Periodic access reviews
- Separation of Duties (SoD) - Conflicting access prevention
- Privileged Access Management (PAM) - Admin account management
- Just-in-Time (JIT) access - Time-bound elevated privileges

**Compliance Frameworks**:
- SOX (Sarbanes-Oxley) - Financial system access controls
- SOC 2 Type II - Access provisioning and deprovisioning controls
- ISO 27001 - Access control requirements (A.9 family)
- NIST 800-53 - Access control baseline (AC family)
- PCI DSS - User access management for payment systems
- GDPR - Right to erasure (deprovisioning user data)
- HIPAA - Workforce security and access management

**Workflow Automation**:
- ServiceNow - IT service management and workflow automation
- Jira Service Management - IT service desk and approvals
- Microsoft Power Automate - Workflow automation
- Zapier - Integration and automation platform
- Workato - Enterprise automation platform

**Access Review Tools**:
- SailPoint IdentityIQ Compliance Manager
- Saviynt Access Governance
- Okta Identity Governance
- Azure AD Access Reviews
- Manager attestation workflows
- Orphaned account detection

**Audit & Logging**:
- SIEM integration (Splunk, Sentinel, Chronicle)
- Audit log retention (7 years for compliance)
- Provisioning event logging
- Approval evidence capture
- Access change tracking

**Reference**: Consult organizational IAM, security, and compliance teams for detailed guidance on framework application

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
