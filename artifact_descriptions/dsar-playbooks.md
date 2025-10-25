# Name: dsar-playbooks

## Executive Summary

The DSAR (Data Subject Access Request) Playbooks artifact documents standardized procedures for processing privacy requests under GDPR, CCPA, and other data protection regulations. This artifact specifies workflows for handling data subject rights including right to access (GDPR Article 15), right to erasure/deletion (GDPR Article 17, CCPA deletion), right to portability (GDPR Article 20), right to rectification (GDPR Article 16), and right to restrict processing using privacy automation platforms like OneTrust, TrustArc, Osano, BigID, or custom request management systems.

As privacy regulations expand globally and enforcement intensifies, this artifact serves Privacy/DPO teams managing DSAR intake and response, Engineering teams implementing data discovery and deletion workflows, Legal teams ensuring regulatory compliance, and Customer Support teams handling consumer requests. It transforms manual, spreadsheet-based DSAR management into automated, auditable workflows with integrated data discovery, systematic deletion, and comprehensive compliance reporting for regulatory obligations.

### Strategic Importance

- **Privacy Compliance**: Implements GDPR Articles 15-22 (data subject rights), CCPA consumer rights, LGPD, PIPEDA, and other global privacy regulations
- **Request Types**: Handles right to access, right to erasure/deletion, right to portability, right to rectification, right to restrict processing, right to object
- **Automated Workflows**: Uses OneTrust Privacy Rights Automation, TrustArc Privacy Portal, Osano Consent Manager, BigID Subject Rights Hub, or custom systems
- **Data Discovery**: Automated personal data discovery across databases, cloud storage, SaaS applications, backups, logs using data mapping tools
- **Deletion Workflows**: Systematic deletion from production databases, backups, data warehouses, analytics systems, third-party processors with verification
- **Timeline Compliance**: Ensures 30-day response deadline (GDPR), 45-day response (CCPA), tracks SLA compliance, manages deadline extensions
- **Audit Trail**: Complete request lifecycle logging (intake, verification, discovery, fulfillment, delivery) for regulatory examination and privacy audits

## Purpose & Scope

### Primary Purpose

This artifact documents step-by-step procedures (playbooks) for processing data subject access requests (DSARs) under GDPR, CCPA, and other privacy regulations. It specifies request intake, identity verification, data discovery, request fulfillment, delivery, and documentation workflows to ensure compliant, timely responses.

### Scope

**In Scope**:
- GDPR rights: Right to access (Art. 15), erasure (Art. 17), portability (Art. 20), rectification (Art. 16), restriction (Art. 18), objection (Art. 21)
- CCPA rights: Right to know, right to delete, right to opt-out of sale, right to non-discrimination
- Request intake: Web forms, email, phone, postal mail, third-party platforms (OneTrust, TrustArc)
- Identity verification: Multi-factor verification, ID document validation, knowledge-based authentication, fraud prevention
- Data discovery: Database queries, data warehouse searches, SaaS application exports, backup searches, log mining
- Access requests: Data compilation, PII redaction (third-party data), format conversion (CSV, JSON, PDF), secure delivery
- Deletion requests: Production database deletion, backup purging, data warehouse removal, third-party processor deletion, verification
- Portability requests: Machine-readable format (JSON, CSV), complete data export, schema documentation
- Timeline management: 30-day GDPR deadline, 45-day CCPA deadline, deadline extension process, escalation procedures
- Third-party coordination: Subprocessor deletion requests, vendor data discovery, joint controller coordination
- Audit documentation: Request logs, fulfillment evidence, delivery confirmation, regulatory reporting

**Out of Scope**:
- General privacy program governance (covered in Privacy Program artifacts)
- Consent management and cookie compliance (covered in Consent Management artifacts)
- Privacy impact assessments (covered in DPIA artifacts)
- Incident response for data breaches (covered in Incident Response artifacts)

### Target Audience

**Primary Audience**:
- Privacy/DPO teams managing DSAR intake and fulfillment
- Customer Support teams handling consumer privacy requests
- Engineering teams implementing data discovery and deletion

**Secondary Audience**:
- Legal teams ensuring regulatory compliance
- Security teams coordinating data access and deletion
- Compliance auditors reviewing DSAR processes

## Document Information

**Format**: Markdown

**File Pattern**: `*.dsar-playbooks.md`

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

**Automated Workflows**: Use privacy automation platforms (OneTrust, TrustArc, BigID) to streamline intake, tracking, and fulfillment
**Identity Verification**: Implement strong identity verification (MFA, ID validation) to prevent fraudulent requests and unauthorized data access
**Centralized Tracking**: Maintain single source of truth for all DSARs with status tracking, deadline monitoring, escalation alerts
**Data Discovery Automation**: Implement automated personal data discovery across systems, reduce manual searches, update data inventory regularly
**Template Responses**: Use standardized response templates for common scenarios, ensure legal review of templates, maintain consistent messaging
**Timeline Compliance**: Set internal deadlines 5-7 days before regulatory deadline, escalate at-risk requests, track extension reasons
**Complete Deletion**: Delete from all systems (production, backups, data warehouses, analytics, logs), verify deletion, document completion
**Secure Delivery**: Use encrypted portals or secure email for data delivery, require authentication, expire download links after 30 days
**Third-Party Coordination**: Maintain subprocessor list, automate deletion requests to vendors, track vendor completion, document evidence
**Audit Documentation**: Log all steps (intake, verification, discovery, fulfillment, delivery), retain evidence for 3+ years, prepare for regulatory examination
**Training**: Train support teams on DSAR intake, educate engineering on data discovery, provide playbook access to all stakeholders
**Metrics Tracking**: Monitor response time, on-time completion rate, request volume trends, discover bottlenecks, continuous improvement
**Privacy by Design**: Architect systems for efficient data discovery and deletion, minimize data retention, implement data minimization

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

**Privacy Regulations**:
- GDPR (EU General Data Protection Regulation) - Articles 15-22 covering data subject rights
- CCPA (California Consumer Privacy Act) - Consumer rights to know, delete, opt-out
- CPRA (California Privacy Rights Act) - Enhanced CCPA with correction and limitation rights
- LGPD (Brazil Lei Geral de Proteção de Dados) - Brazilian data protection law
- PIPEDA (Canada Personal Information Protection) - Canadian privacy law
- UK GDPR - Post-Brexit UK data protection regulation
- PDPA (Singapore Personal Data Protection Act)
- Privacy Act 1988 (Australia) - Australian privacy principles

**GDPR Data Subject Rights**:
- Article 15: Right to access personal data
- Article 16: Right to rectification (correction)
- Article 17: Right to erasure ("right to be forgotten")
- Article 18: Right to restriction of processing
- Article 19: Notification obligation regarding rectification or erasure
- Article 20: Right to data portability
- Article 21: Right to object to processing
- Article 22: Rights related to automated decision-making

**Privacy Automation Platforms**:
- OneTrust Privacy Rights Automation - Enterprise privacy management platform
- TrustArc Privacy Portal - DSAR intake and fulfillment automation
- Osano Consent Manager - Privacy request management
- BigID Subject Rights Hub - Automated DSAR orchestration
- Transcend Data Privacy Platform - Privacy request automation
- DataGrail Privacy Request Manager - Automated DSAR workflows
- Securiti PrivacyOps - Privacy automation and orchestration
- WireWheel Privacy Hub - Privacy request management

**Data Discovery Tools**:
- BigID - Automated personal data discovery and classification
- OneTrust Data Discovery - PII discovery across systems
- Spirion (formerly Identity Finder) - Sensitive data discovery
- Varonis - Data security and classification
- Microsoft Purview - Data governance and discovery
- Ground Labs Enterprise Recon - Data discovery platform

**Identity Verification**:
- Multi-factor authentication (MFA, 2FA)
- ID document verification (Jumio, Onfido, Persona)
- Knowledge-based authentication (KBA)
- Biometric verification
- Email/phone verification
- Risk-based authentication

**Timeline Requirements**:
- GDPR: 30 days (1 month) response deadline, extendable to 90 days in complex cases
- CCPA: 45 days response deadline, extendable to 90 days with notice
- CPRA: 45 days (same as CCPA)
- LGPD: 15 days response deadline
- Internal SLA: Recommend 5-7 day buffer before regulatory deadline

**Data Deletion Standards**:
- NIST 800-88: Guidelines for Media Sanitization
- DoD 5220.22-M: Data wiping standard
- Secure deletion from databases (logical deletion, tombstoning)
- Backup purging strategies
- Third-party processor deletion
- Verification and certification of deletion

**Compliance Frameworks**:
- ISO 27701: Privacy Information Management System (PIMS)
- ISO 27001: Information security management
- SOC 2 Type II: Privacy controls and practices
- NIST Privacy Framework: Privacy risk management
- AICPA Privacy Management Framework
- IAPP (International Association of Privacy Professionals) standards

**Audit & Documentation**:
- Complete DSAR lifecycle logs
- Identity verification evidence
- Data discovery documentation
- Fulfillment records
- Delivery confirmation
- 3-7 year retention for audit evidence
- Regulatory examination preparedness

**Request Exemptions (GDPR)**:
- Manifestly unfounded or excessive requests
- Legal obligations requiring data retention
- Public interest in processing
- Exercise or defense of legal claims
- Freedom of expression and information

**Reference**: Consult organizational privacy, legal, and compliance teams for detailed guidance on framework application and regulatory interpretation

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
