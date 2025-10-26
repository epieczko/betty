# Name: architecture-waivers

## Executive Summary

The Architecture Waivers artifact documents formal exception requests when projects or systems cannot comply with established architectural standards, patterns, or technology choices. This risk management artifact follows TOGAF 9.2 Architecture Governance principles and ISO 31000 Risk Management frameworks to ensure that architectural deviations are properly evaluated, approved with appropriate authority, and mitigated through compensating controls.

Each waiver captures the standard being waived, business justification for the exception, risk assessment using FAIR methodology, compensating controls to mitigate increased risk, sunset date for time-limited exceptions, and remediation plan for eventual compliance. The artifact integrates with the Architecture Review Board (ARB) approval process, risk register for ongoing risk tracking, and compliance frameworks (SOC 2, ISO 27001, GDPR) to demonstrate that exceptions are managed responsibly. Waivers require executive-level risk acceptance for high-risk deviations and include automated sunset date monitoring to prevent indefinite exceptions.

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

This artifact provides transparent mechanism for managing architectural exceptions when strict compliance is not feasible due to business constraints, technical limitations, legacy system constraints, or time-to-market pressures. It enables informed risk acceptance while maintaining architectural governance, ensures compensating controls reduce risk to acceptable levels, and prevents exceptions from becoming permanent technical debt.

### Scope

**In Scope**:
- Exception requests: standard/pattern/technology being waived, specific deviation requested, scope of waiver
- Business justification: why compliance is not feasible, business impact of compliance vs. waiver, alternatives considered
- Risk assessment: qualitative and quantitative risk analysis using FAIR (Factor Analysis of Information Risk) or ISO 31000
- Threat analysis: security implications, data protection concerns, compliance violations, operational risks
- Compensating controls: specific mitigations to reduce risk (additional monitoring, manual procedures, restricted access)
- Risk acceptance: formal acceptance by appropriate authority level (ARB for medium, CTO/CIO for high, CISO for security)
- Sunset dates: time-limited exceptions with defined expiration (typically 6-12 months, maximum 24 months)
- Remediation plans: roadmap for achieving compliance, resources required, dependencies, timeline
- Impact analysis: affected systems, data flows, integrations, security boundaries
- Compliance mapping: impact on SOC 2, ISO 27001, GDPR, HIPAA, PCI DSS controls
- Monitoring requirements: how exception will be tracked, metrics for risk indicators, escalation triggers
- Renewal process: criteria for extending waivers, re-evaluation requirements, maximum renewal periods
- Waiver dependencies: related waivers, cascading exceptions, cumulative risk

**Out of Scope**:
- Permanent architectural decisions (handled through Architecture Decision Records)
- Minor deviations that don't require governance approval (handled through architecture review)
- Implementation details of compensating controls (documented in security/operations artifacts)
- Business requirements driving the exception (referenced from requirements documentation)
- Detailed technical designs (referenced from architecture overview)

### Target Audience

**Primary Audience**:
- Architecture Review Board (ARB) Members: evaluate and approve waiver requests based on risk and compensating controls
- Enterprise Architects: assess impact on enterprise architecture standards and reference architectures
- Solution Architects: submit waiver requests when project constraints prevent standard compliance
- Technical Architects: design compensating controls and remediation approaches

**Secondary Audience**:
- Risk Management: track architectural risk, aggregate waiver risk exposure, report to executive leadership
- Security Architects: evaluate security implications, validate compensating controls, assess threat landscape
- Compliance Officers: ensure waivers don't violate regulatory requirements, document audit trail
- Executive Leadership (CTO, CIO, CISO): risk acceptance for high-risk waivers

## Document Information

**Format**: Markdown

**File Pattern**: `*.architecture-waivers.md`

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

**Exhaustive Alternatives Analysis**: Require documentation of all alternatives considered before granting waiver; demonstrate due diligence in seeking compliant approaches
**Quantitative Risk Assessment**: Use FAIR methodology to quantify risk in monetary terms (annual loss expectancy); avoid purely qualitative assessments for high-risk waivers
**Specific Compensating Controls**: Define measurable, verifiable compensating controls with clear implementation criteria; avoid vague mitigations like "increased monitoring"
**Risk Acceptance Authority**: Match approval authority to risk level - ARB for low/medium, CTO/CIO for high, Board for critical; never allow self-approval
**Mandatory Sunset Dates**: Require expiration date on all waivers (no permanent exceptions); maximum 12 months for first approval, 24 months lifetime
**Remediation Roadmap**: Mandate detailed plan for achieving compliance including timeline, resources, dependencies, success criteria
**Security Architect Review**: Require security architecture review for all waivers affecting security posture; CISO approval for high-risk security exceptions
**Compliance Impact Assessment**: Document impact on SOC 2, ISO 27001, GDPR, PCI DSS controls; involve compliance officer in review
**Automated Monitoring**: Implement automated tracking of compensating controls effectiveness; alert when controls fail or risk indicators spike
**Sunset Alerts**: Configure automated reminders at 90, 60, 30 days before expiration; require renewal request or remediation completion
**Limited Renewals**: Allow maximum of 2 renewals (3 total approvals); require escalation to higher authority for renewals; eventually force remediation
**Cumulative Risk Tracking**: Monitor aggregate risk from all active waivers; set organizational risk threshold; pause new waivers when threshold exceeded
**Waiver Dependencies**: Identify cascading waivers where one exception requires others; evaluate cumulative risk holistically
**Template Standardization**: Use standard waiver request template ensuring all required fields completed; reject incomplete submissions
**Immutable Audit Trail**: Maintain complete, tamper-proof record of request, reviews, approvals, monitoring, renewals, closure
**Risk Register Integration**: Link each waiver to risk register; update risk status as waivers are created, renewed, remediated
**Regular Review Cadence**: Quarterly review of all active waivers; verify compensating controls still effective; assess if remediation progressing
**Escalation for Overdue Remediation**: Escalate to project sponsor and executive leadership when remediation plans are behind schedule
**Metrics & Reporting**: Track waiver volume, renewal rate, remediation success rate, average time to remediation; report trends to ARB and leadership
**Compensating Control Validation**: Require proof of implementation for all compensating controls; conduct periodic audits of control effectiveness
**No Blanket Waivers**: Deny requests for organization-wide or multi-system waivers; require specific, scoped exceptions per system/component

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

**Risk Management Frameworks**:
- ISO 31000 Risk Management - principles and guidelines for managing architectural risk
- FAIR (Factor Analysis of Information Risk) - quantitative risk analysis with loss event frequency and magnitude
- NIST Risk Management Framework (RMF) - categorize, select, implement, assess, authorize, monitor
- OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) - risk-based strategic assessment
- COSO ERM Framework - enterprise risk management integrated framework

**Architecture Governance**:
- TOGAF 9.2 Architecture Governance - managing exceptions through architecture contracts and waivers
- TOGAF Architecture Compliance Review - formal assessment against standards with exception handling
- Architecture Exception Process - request, review, approve, monitor, remediate workflow
- COBIT 2019 Risk Management (EDM03) - ensuring risk optimization
- ISO/IEC 38500 - IT governance with evaluate, direct, monitor including exception management

**Security Risk Assessment**:
- NIST SP 800-30 - Guide for Conducting Risk Assessments with threat, vulnerability, impact analysis
- OWASP Risk Rating Methodology - likelihood and impact scoring for security exceptions
- Threat Modeling - STRIDE, PASTA, LINDDUN for identifying security risks
- Attack Surface Analysis - quantifying exposure introduced by architectural deviations
- Defense in Depth - evaluating how waivers affect layered security controls

**Compensating Controls**:
- PCI DSS Compensating Controls - requirements for alternative security measures
- SOC 2 Complementary User Entity Controls (CUEC) - additional controls when standard controls unavailable
- ISO 27001 Statement of Applicability (SoA) - documenting controls not implemented with justification
- NIST 800-53 Control Tailoring - selecting alternative controls when baseline controls don't apply
- Defense in Depth Strategies - layered controls to compensate for single control gaps

**Compliance Frameworks**:
- SOC 2 Trust Service Criteria - security, availability, processing integrity, confidentiality, privacy controls
- ISO 27001 Annex A Controls - 114 security controls with justification for non-implementation
- GDPR Article 32 - security of processing with appropriate technical and organizational measures
- HIPAA Security Rule - administrative, physical, technical safeguards with exception documentation
- PCI DSS - payment card data security with compensating controls for standard deviations
- FedRAMP - federal cloud security with formal deviation request process

**Risk Acceptance**:
- Risk Acceptance Matrix - defining authority levels based on risk severity (low/medium/high/critical)
- Residual Risk Calculation - risk after compensating controls applied
- Risk Appetite Framework - organizational tolerance for different risk types
- Risk Transfer Options - insurance, contractual liability, third-party assumption
- Risk Treatment Strategies - accept, avoid, transfer, mitigate

**Sunset Date Management**:
- Time-Limited Exceptions - maximum waiver duration policies (6, 12, 18, 24 months)
- Automatic Expiration - system-enforced sunset dates requiring renewal or remediation
- Escalation Ladders - increasing scrutiny for waiver renewals (ARB → CTO → Board)
- Technical Debt Tracking - linking waivers to technical debt register with remediation priority
- Remediation Roadmaps - planned path to compliance with milestones and resource allocation

**Monitoring & Reporting**:
- Key Risk Indicators (KRI) - metrics that signal increasing risk (incidents, performance degradation)
- Waiver Dashboard - real-time visibility into active waivers, expiration dates, risk levels
- Aggregated Risk Exposure - cumulative risk from all active waivers across organization
- Trend Analysis - increasing/decreasing waiver volume, renewal rates, remediation success
- Executive Reporting - quarterly risk reports to leadership on architectural exceptions

**Architecture Standards**:
- Architecture Principles - foundational principles that waivers deviate from
- Reference Architectures - standard patterns that exceptions bypass
- Technology Standards - approved technology stack that waivers allow alternatives to
- Security Architecture Standards - baseline security controls that waivers reduce
- Integration Standards - standard integration patterns that exceptions violate

**Audit & Compliance**:
- Audit Trail Requirements - immutable record of waiver request, approval, monitoring, closure
- Compliance Documentation - demonstrating to auditors that exceptions are managed responsibly
- Control Effectiveness Testing - validating that compensating controls provide equivalent protection
- Audit Finding Remediation - waivers resulting from audit findings with corrective action plans
- Regulatory Reporting - disclosing architectural exceptions to regulators when required

**Quality Frameworks**:
- ISO 25010 Quality Attributes - documenting impact on performance, security, reliability, maintainability
- Non-Functional Requirements - quality attribute targets that waivers may compromise
- Service Level Objectives (SLO) - documenting SLO impact and compensating SLAs
- Architectural Fitness Functions - automated tests to monitor exception impacts

**Tools & Platforms**:
- GRC Platforms - ServiceNow GRC, Archer, MetricStream for waiver workflow and tracking
- Risk Registers - centralized tracking of architectural risks and waivers
- Jira/ServiceNow - workflow automation for waiver request, approval, monitoring
- Confluence/SharePoint - waiver documentation repository with access controls
- Automated Alerting - sunset date reminders, KRI threshold alerts, renewal notifications

**Reference**: Consult organizational risk management, architecture governance, and compliance teams for waiver policies, approval authorities, and compensating control requirements

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
