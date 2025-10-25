# Name: quarterly-access-reviews

## Executive Summary

The Quarterly Access Reviews artifact documents periodic access recertification campaigns where managers attest to the appropriateness of their direct reports' application access, privileged entitlements, and role assignments. These reviews, also called access certifications or attestations, are executed through Identity Governance and Administration (IGA) platforms like SailPoint, Saviynt, or Okta Identity Governance to identify orphaned accounts, detect segregation of duties (SOD) violations, and ensure least privilege access principles are maintained.

Access reviews satisfy SOC 2 CC6.1 controls, ISO 27001 A.9.2.5 requirements, and SOX IT General Controls for user access management. They leverage automated workflows to distribute access lists to managers, track attestation completion rates, and auto-remediate access for non-certified entitlements. The artifact includes segregation of duties analysis detecting toxic combinations (e.g., ability to both create and approve transactions), orphaned account identification for terminated employees or service accounts, and privileged access validation for elevated permissions requiring heightened scrutiny.

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

This artifact serves as the evidence of periodic access validation ensuring user entitlements remain appropriate, comply with least privilege principles, and align with current job responsibilities. It detects access creep, identifies orphaned accounts, validates segregation of duties, and provides audit trails demonstrating continuous access governance.

### Scope

**In Scope**:
- Manager attestation of direct reports' application access
- Privileged access recertification (admin accounts, root access, production access)
- Role-based access control (RBAC) assignment validation
- Segregation of duties (SOD) conflict detection and remediation
- Orphaned account identification (terminated employees, inactive accounts)
- Service account and shared account review
- Application owner attestation of application-specific entitlements
- Third-party contractor and vendor access recertification
- Emergency access and break-glass account validation
- Cloud IAM role and permission reviews (AWS, Azure, GCP)
- Database privileged user access validation
- Network device and infrastructure access review
- Compliance evidence collection for SOC 2, ISO 27001, SOX audits
- Access review completion tracking and escalation
- Auto-remediation of non-certified or expired access

**Out of Scope**:
- Initial access provisioning and onboarding (see onboarding-checklist)
- Immediate access revocation for terminations (see offboarding-checklist)
- Real-time access monitoring and anomaly detection
- Identity lifecycle management automation
- Password policy and authentication strength validation
- User behavior analytics (UBA) and insider threat detection

### Target Audience

**Primary Audience**:
- Hiring managers attesting to team members' access
- IAM Administrators coordinating certification campaigns
- IGA platform administrators (SailPoint, Saviynt, Okta)
- Application owners validating application-specific entitlements
- Security teams monitoring SOD violations and anomalies

**Secondary Audience**:
- Internal Audit teams reviewing access governance
- Compliance teams collecting SOC 2/ISO 27001 evidence
- External auditors validating access controls
- Risk management teams assessing access-related risks
- IT leadership tracking attestation completion metrics

## Document Information

**Format**: Markdown

**File Pattern**: `*.quarterly-access-reviews.md`

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

**Quarterly Cadence Minimum**: Conduct access reviews at minimum quarterly; more frequently (monthly) for privileged and production access
**Manager Accountability**: Assign attestation responsibility to direct managers who understand business need for access, not IT teams
**Automated Campaign Launch**: Trigger review campaigns automatically via IGA platform integration with HRIS for current reporting relationships
**Risk-Based Prioritization**: Prioritize high-risk access first (privileged accounts, SOD violations, orphaned accounts) before standard user access
**Clear Attestation Questions**: Ask "Should this person still have this access?" not technical jargon about entitlements and permissions
**Remediation Deadlines**: Automatically revoke non-certified access 7-14 days after campaign deadline with clear warning notifications
**Delegated Reviews**: Allow managers to delegate attestation to senior team members for large teams, with manager final approval
**SOD Detection First**: Run SOD analysis before campaign launch to highlight conflicts requiring immediate manager attention
**Orphaned Account Flagging**: Pre-identify accounts for terminated employees and flag for immediate review and revocation
**Application Owner Reviews**: Supplement manager reviews with application owner attestation for high-value systems
**Privileged Access Scrutiny**: Require additional justification and approval for admin accounts and production access
**Service Account Governance**: Include service accounts and shared accounts in reviews with designated technical owners
**Completion Tracking Dashboard**: Provide real-time dashboard showing attestation completion rates by organization and manager
**Executive Escalation**: Escalate incomplete attestations to executives for managers missing deadlines after multiple reminders
**Auto-Remediation Caution**: Use auto-revocation carefully; implement grace periods and confirmation workflows to prevent disruption
**Evidence Retention**: Maintain complete audit trail of attestations, decisions, and remediations for minimum 7 years
**Trend Analysis**: Track metrics like access creep rates, SOD violation trends, and average access per user over time
**Feedback Loop**: Incorporate attestation feedback into provisioning workflows to prevent future inappropriate access grants
**Training for Managers**: Provide annual training to managers on attestation responsibilities and security implications
**Exception Management**: Establish formal exception process for SOD violations requiring documented business justification and compensating controls

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

**Identity Governance & Administration (IGA) Platforms**:
- SailPoint IdentityIQ and IdentityNow for access certifications
- Saviynt Enterprise Identity Cloud for attestation campaigns
- Okta Identity Governance for access reviews
- Microsoft Entra Identity Governance (Azure AD)
- Oracle Identity Governance for enterprise IGA
- IBM Security Verify Governance
- One Identity Manager for identity governance
- Broadcom (CA) Identity Governance
- RSA Identity Governance and Lifecycle

**Segregation of Duties (SOD) Analysis**:
- SailPoint SOD detection and remediation
- SAP GRC Access Control for ERP SOD
- Oracle Access Controls Governor
- Pathlock (formerly Greenlight) for ERP compliance
- Appsian Security Platform for SOD monitoring
- SOD matrices for financial systems
- Toxic combination detection and prevention

**Compliance & Regulatory Standards**:
- SOC 2 CC6.1 (Logical and Physical Access Controls)
- ISO 27001 A.9.2.5 (Review of User Access Rights)
- SOX IT General Controls (ITGC) for access management
- NIST SP 800-53 AC-2 (Account Management)
- NIST Cybersecurity Framework PR.AC-4 (Access permissions managed)
- CIS Controls v8 - Control 5.4 (Restrict Administrator Privileges)
- CIS Controls v8 - Control 6.8 (Define and Maintain Role-Based Access)
- PCI DSS Requirement 8.1.4 (Remove/disable inactive accounts)
- HIPAA 164.308(a)(4)(ii)(C) (Access Authorization)
- GDPR Article 32 (Security of Processing)
- COBIT 2019 DSS05.04 (Manage User Identity and Access)
- FFIEC IT Examination Handbook (Access Rights Administration)

**IAM & Access Management**:
- SCIM 2.0 for automated access provisioning
- OAuth 2.0 and OpenID Connect for authorization
- RBAC (Role-Based Access Control) frameworks
- ABAC (Attribute-Based Access Control) models
- PBAC (Policy-Based Access Control) principles
- Least Privilege Access (PoLP) principles
- Zero Trust Architecture access validation

**Automation & Workflow**:
- ServiceNow IGA integration for access reviews
- Workday adaptive security and access certification
- Microsoft Power Automate for attestation workflows
- SailPoint Lifecycle Events for automated remediation
- Okta Workflows for access review automation

**Privileged Access Management (PAM)**:
- CyberArk Privileged Access Manager
- BeyondTrust Privileged Remote Access
- Delinea (Thycotic) Secret Server
- HashiCorp Vault for secrets management
- AWS Secrets Manager and IAM Access Analyzer
- Azure Privileged Identity Management (PIM)
- Google Cloud Identity-Aware Proxy (IAP)
- Just-In-Time (JIT) access principles

**Audit & Reporting**:
- SIEM integration (Splunk, QRadar, Sentinel)
- Access governance dashboards and metrics
- Compliance reporting for SOC 2, ISO audits
- Access review completion KPIs
- Orphaned account trending and analysis
- SOD violation tracking and remediation metrics

**Best Practice Frameworks**:
- NIST Identity and Access Management framework
- ISO/IEC 29146 (Access Management Framework)
- OWASP Access Control Cheat Sheet
- Cloud Security Alliance (CSA) IAM guidance
- SANS Institute access control guidelines

**Cloud IAM Reviews**:
- AWS IAM Access Analyzer
- Azure AD Access Reviews and PIM
- Google Cloud Asset Inventory and IAM Recommender
- AWS Organizations service control policies (SCPs)
- Azure AD entitlement management
- GCP VPC Service Controls

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
