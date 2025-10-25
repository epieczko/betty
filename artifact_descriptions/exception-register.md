# Name: exception-register

## Executive Summary

The Exception Register is a governance and compliance artifact that provides centralized tracking of approved policy exceptions, control deviations, and temporary non-compliance situations with documented compensating controls, risk acceptance, and sunset dates. This critical deliverable supports risk-based exception management aligned to ISO 27001, SOC 2, PCI DSS, and GRC platform workflows (ServiceNow GRC, RSA Archer, MetricStream) enabling controlled policy variance while maintaining oversight, accountability, and audit trail.

As a key component of the governance framework, this artifact serves Compliance Officers, Risk Managers, CISOs, Internal Audit, and Policy Owners by providing visibility into all active exceptions, their business justification, compensating controls effectiveness, residual risk levels, and time-bound remediation plans. It integrates with GRC platforms to enable exception workflow approval, automatic sunset date alerts, quarterly reviews, and SOC 2/ISO 27001 audit evidence.

### Strategic Importance

- **Risk-Based Flexibility**: Enables business agility through controlled policy exceptions when strict compliance would block legitimate business needs, while maintaining risk oversight
- **Compensating Controls**: Documents alternative controls that mitigate risks when standard controls cannot be implemented, satisfying PCI DSS and SOC 2 compensating control requirements
- **Time-Bound Accountability**: Requires sunset dates, business owners, and remediation plans ensuring exceptions are temporary with defined expiration and renewal governance
- **Audit Trail**: Provides complete audit trail of exception approval, renewal, and closure supporting SOC 2 (CC1.4), ISO 27001 (A.5.1), and regulatory examinations
- **Risk Acceptance**: Documents formal risk acceptance by business owners and risk committee for residual risk resulting from policy deviation
- **Compliance Monitoring**: Enables compliance tracking of exception population, aging analysis, and sunset date compliance supporting continuous compliance programs
- **Governance Oversight**: Provides Board and Executive visibility into exception trends, high-risk exceptions, and policy effectiveness requiring exception support

## Purpose & Scope

### Primary Purpose

This artifact serves as the centralized Exception Register tracking all approved deviations from organizational policies, standards, procedures, and regulatory requirements with documented business justification, compensating controls, residual risk assessment, approval authority, and time-bound sunset dates. It supports governance oversight of policy variance, ensures risk-based exception approval, maintains compliance audit trail, and provides automated workflow for exception request, review, approval, renewal, and closure within GRC platforms.

### Scope

**In Scope**:
- Policy exception requests and approvals (security policies, IT policies, HR policies, finance policies, operational policies)
- Control exceptions and alternative compensating controls (PCI DSS compensating controls, SOC 2 control alternatives)
- Regulatory compliance exceptions with regulatory approval documentation
- Technical standard deviations (architecture standards, coding standards, configuration baselines)
- Business justification documenting why exception is necessary and why standard control cannot be implemented
- Risk assessment of exception including inherent risk, compensating controls, and residual risk rating
- Compensating control documentation describing alternative controls mitigating risks
- Approval workflow tracking request, review, risk acceptance, and formal approval by appropriate authority
- Sunset dates defining exception expiration with automatic notification 30/60/90 days prior
- Renewal process requiring rejustification and re-approval before expiration
- Exception owner accountability and contact information
- Quarterly exception reviews validating exception status, compensating controls effectiveness, and continued business need
- Exception closure and remediation tracking when permanent solution implemented
- Exception metrics and reporting (open exceptions, overdue exceptions, exceptions by policy, high-risk exceptions)
- Integration with risk register for exceptions representing accepted risks

**Out of Scope**:
- Incident response and security incident tracking (see Incident Management)
- Audit findings and remediation plans (see Audit Management)
- Change requests and change management (see Change Management)
- Project-specific risks not related to policy exceptions (see RAID Log)
- Vendor contract exceptions (covered in Vendor Management)

### Target Audience

**Primary Audience**:
- Compliance Officers for exception oversight, approval workflow management, and regulatory compliance documentation
- Risk Managers for risk assessment validation, risk acceptance coordination, and residual risk monitoring
- Chief Information Security Officer (CISO) for security policy exception approval and compensating control assessment
- Policy Owners for policy exception review, impact assessment, and approval recommendations
- Internal Audit for exception population testing, compensating control validation, and governance assessment

**Secondary Audience**:
- Exception Requesters (business units, IT teams, project managers) seeking policy variance approval
- Exception Approvers (executives, risk committee, security leadership) providing risk acceptance and formal approval
- GRC Administrators maintaining exception workflows, sunset date alerts, and quarterly review cycles
- External Auditors requiring exception documentation for SOC 2, ISO 27001, PCI DSS, or regulatory audits
- Board Risk Committee for high-risk exception visibility and exception trend reporting

## Document Information

**Format**: Markdown

**File Pattern**: `*.exception-register.md`

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
**Exception Management Best Practices**:
**Mandatory Sunset Dates**: All exceptions must have defined expiration dates (typically 6-12 months maximum) with automatic renewal required
**Risk-Based Approval**: Establish tiered approval authority based on risk level (low-risk to manager, medium to director, high to executive/risk committee)
**Compensating Controls Required**: Document specific compensating controls for each exception with validation they provide equivalent protection
**Business Justification**: Require clear business need explanation and documentation why standard control cannot be implemented
**No Permanent Exceptions**: Establish policy that all exceptions are temporary; if permanent variance needed, update the policy/standard
**Quarterly Reviews**: Conduct quarterly exception reviews validating ongoing business need, compensating controls, and progress toward remediation
**Sunset Alerts**: Configure GRC platform to alert exception owner and approver 30/60/90 days before expiration
**Zero-Tolerance for Expired**: Do not allow exceptions to operate past sunset date without formal renewal approval
**Compensating Control Testing**: Periodically test compensating controls for operating effectiveness, not just design
**Exception Metrics Dashboard**: Track and report metrics: open exceptions, overdue, high-risk, exceptions by policy, average duration
**Linkage to Risk Register**: Create risk register entries for high-risk exceptions documenting accepted residual risk
**Formal Risk Acceptance**: Require documented risk acceptance from business owner and risk committee for medium/high-risk exceptions
**Remediation Plans**: Require documented permanent remediation plan with milestones for all exceptions
**Exception Limits**: Consider establishing limits on number of exceptions per policy (if too many, policy may need revision)
**Audit Trail**: Maintain complete audit trail of all exception requests, approvals, reviews, renewals, and closures for compliance audits

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

**Compliance & Governance Frameworks**:
- SOC 2 Trust Services Criteria (CC1.4 Management oversight, CC5.1 Control deviations)
- ISO 27001:2022 (A.5.1 Policies, 6.1.3 Risk treatment, exception handling)
- PCI DSS v4.0 (Requirement 12.4.1 Compensating controls documentation)
- NIST SP 800-53 Rev. 5 (Control tailoring and compensating controls)
- COBIT 2019 (APO01.06 Define exception process, MEA02 Monitor system of internal control)
- ISO 9001:2015 Quality Management (Clause 10.2 Nonconformity and corrective action)
- ITIL 4 Service Management (Change Enablement - Standard vs. emergency changes)
- NIST Cybersecurity Framework (Governance function - exception handling)
- HIPAA Security Rule (§164.308 Exception documentation for security requirements)
- GDPR Article 5 (Data protection principles with documented exceptions)
- CMMC Level 3 (Exception tracking for defense contractor compliance)

**GRC Platforms with Exception Management**:
- ServiceNow GRC (Policy Exception Management module with workflow)
- RSA Archer (Policy Management with exception tracking)
- MetricStream Policy Management
- LogicGate Risk Cloud (Policy exception workflows)
- OneTrust GRC (Policy & exception management)
- SAI Global Compliance 360
- Resolver GRC Platform
- Riskonnect Policy Management
- NAVEX Global PolicyTech with exception tracking
- Quantivate GRC Suite

**Risk Management Standards**:
- COSO ERM 2017 (Exception handling in risk response)
- ISO 31000:2018 (Risk treatment and acceptance)
- FAIR (Risk quantification for exception decisions)
- NIST Risk Management Framework (Control tailoring and exceptions)
- OCTAVE for risk-based exception assessment

**Policy Management & Governance**:
- ISO 19600:2014 Compliance Management Systems
- ISO 37301:2021 Compliance Management Systems (updated from 19600)
- ANSI/ASIS GRC.1-2009 Risk Assessment for Organizations
- GAPP (Generally Accepted Privacy Principles) exception handling
- COBIT 2019 (APO01 Manage Framework, policy exception governance)

**Compensating Controls Guidance**:
- PCI DSS Compensating Controls Worksheet and methodology
- SOC 2 Compensating Controls guidance from AICPA
- NIST SP 800-53 Appendix E (Assurance and Trustworthiness)
- FFIEC IT Examination Handbook (Compensating controls)
- ISO 27001 Annex A control selection and justification

**Audit & Assurance Standards**:
- AICPA SOC 2 Reporting (Testing exceptions and compensating controls)
- IIA Standards (Testing of control exceptions)
- ISACA COBIT Assurance Guide
- ISO 19011:2018 Guidelines for auditing management systems

**Reference**: Consult Compliance team, Risk Management, CISO, and Internal Audit for detailed guidance on exception management processes, compensating control validation, and regulatory compliance requirements for policy exceptions

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
