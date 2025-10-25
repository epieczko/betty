# Name: enterprise-risk-register

## Executive Summary

The Enterprise Risk Register is a comprehensive risk management artifact that provides centralized tracking and quantification of organizational risks using industry-standard frameworks such as COSO ERM, ISO 31000, and FAIR (Factor Analysis of Information Risk). This critical deliverable enables risk-based decision making through structured risk identification, assessment, treatment planning, and continuous monitoring within GRC platforms like ServiceNow GRC, RSA Archer, MetricStream, or LogicGate.

As the authoritative source for enterprise risk information, this artifact serves Risk Managers, Compliance Officers, CISOs, Internal Audit, and Board Risk Committees by providing real-time visibility into risk exposure, heat maps, risk trends, and mitigation effectiveness. It integrates with NIST Risk Management Framework (RMF), supports quantitative risk analysis through FAIR methodology, and enables risk appetite alignment through consistent risk scoring and categorization.

### Strategic Importance

- **Risk Quantification**: Enables FAIR-based quantitative risk analysis with Loss Event Frequency (LEF) and Loss Magnitude (LM) calculations, providing monetary risk exposure estimates
- **Heat Map Visualization**: Provides risk heat maps plotting likelihood vs. impact, enabling executive dashboards and risk portfolio views across risk categories
- **Mitigation Tracking**: Tracks risk treatment plans, control effectiveness, and residual risk levels with accountability assignment and target completion dates
- **Regulatory Compliance**: Supports SOC 2 (CC4.1, CC9.1), ISO 27001 (A.5.7 Threat Intelligence), NIST 800-53 (RA family), and SOX risk assessment requirements
- **Board Reporting**: Enables Board Risk Committee reporting with executive summaries, top risks, risk velocity trends, and key risk indicators (KRIs)
- **Risk Appetite Alignment**: Maps individual risks to organizational risk appetite thresholds defined in Risk Appetite Statement, flagging tolerance breaches
- **Continuous Monitoring**: Supports ongoing risk monitoring with trigger-based updates, quarterly reviews, and emerging risk identification processes

## Purpose & Scope

### Primary Purpose

This artifact serves as the centralized enterprise risk register tracking all identified risks across strategic, operational, financial, compliance, cyber security, and third-party risk categories. It supports risk-based decision making through FAIR quantification (Annualized Loss Expectancy calculations), risk heat maps plotting inherent and residual risk, mitigation planning with ownership assignment, and continuous monitoring of risk treatment effectiveness aligned to organizational risk appetite thresholds.

### Scope

**In Scope**:
- Risk identification across all risk domains (strategic, operational, financial, compliance, technology, cyber, third-party, reputational)
- Inherent risk assessment using likelihood x impact scoring (typically 1-5 scales or FAIR quantitative models)
- Risk categorization aligned to COSO ERM framework or ISO 31000 risk taxonomy
- Risk heat maps and portfolio views visualizing risk concentration and exposure trends
- Control identification and effectiveness assessment (design and operating effectiveness)
- Residual risk calculation after control mitigation
- Risk treatment plans including avoid, transfer, mitigate, accept decisions with rationale
- Risk owner and control owner assignment with accountability tracking
- Risk appetite threshold monitoring and tolerance breach escalation
- FAIR quantitative analysis for high-impact risks (Loss Event Frequency, Threat Event Frequency, Vulnerability, Loss Magnitude)
- Key Risk Indicators (KRIs) and trigger thresholds for early warning
- Quarterly risk reviews and risk trend analysis
- Integration with incident register and issue management

**Out of Scope**:
- Detailed vendor risk assessments (see Third-Party Risk Assessments artifact)
- Individual project risks (managed in project RAID logs)
- Operational incident tracking (see Incident Register)
- Policy exception tracking (see Exception Register)
- Detailed audit findings remediation (see Audit Management)
- Insurance policy management and claims

### Target Audience

**Primary Audience**:
- Chief Risk Officer (CRO) and Enterprise Risk Management team for comprehensive risk portfolio oversight and Board reporting
- Risk Managers for day-to-day risk register maintenance, assessment coordination, and mitigation tracking
- Compliance Officers for regulatory risk identification and compliance program alignment
- Chief Information Security Officer (CISO) for cyber risk quantification and security control effectiveness
- Internal Audit for risk-based audit planning and control testing coordination

**Secondary Audience**:
- Board of Directors Risk Committee for risk oversight, appetite setting, and material risk review
- Executive Leadership Team (C-suite) for strategic risk-informed decision making
- Business Unit Leaders as risk owners accountable for risk treatment execution
- Control Owners responsible for implementing and maintaining risk mitigation controls
- External Auditors requiring risk assessment documentation for SOC 2, ISO 27001, or financial audits

## Document Information

**Format**: Markdown

**File Pattern**: `*.enterprise-risk-register.md`

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
**Risk-Specific Best Practices**:
**Consistent Risk Scoring**: Use standardized likelihood and impact scales (e.g., 1-5) with clear definitions to ensure consistency across risk assessors
**Inherent vs Residual Risk**: Always assess both inherent risk (before controls) and residual risk (after controls) to demonstrate control effectiveness
**FAIR Quantification**: Apply FAIR methodology to top 10-20 risks to provide monetary exposure estimates for executive decision making
**Heat Map Visualization**: Maintain risk heat maps plotting likelihood vs. impact to provide portfolio view and identify risk concentrations
**Risk Appetite Mapping**: Map each risk to risk appetite categories and flag when residual risk exceeds tolerance thresholds
**Three Lines of Defense**: Assign risk ownership following 3LOD model (Business owns, Risk oversees, Audit provides assurance)
**Control Linkage**: Link each risk to specific controls and document control design effectiveness and operating effectiveness
**Quarterly Reviews**: Conduct mandatory quarterly risk reviews with risk owners to update status, reassess ratings, and track mitigation progress
**Emerging Risk Scanning**: Establish process for identifying emerging risks through horizon scanning, threat intelligence, and industry analysis
**Key Risk Indicators**: Define measurable KRIs with thresholds that provide early warning before risk materializes
**Board Reporting Cadence**: Provide quarterly Board Risk Committee reports with top risks, risk trends, appetite breaches, and material changes
**Integration with GRC Platform**: Leverage GRC platform workflows for risk assessment, review cycles, and automated reporting
**Risk Treatment Documentation**: Document risk response strategy (avoid/transfer/mitigate/accept) with clear rationale and approval evidence
**Scenario Analysis**: Conduct scenario planning and stress testing for high-impact risks to understand potential cascading effects
**Risk Velocity Tracking**: Track risk velocity (speed of onset) to prioritize risks that could materialize quickly

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
- COSO Enterprise Risk Management (ERM) - Integrated Framework (2017)
- ISO 31000:2018 Risk Management - Guidelines
- FAIR (Factor Analysis of Information Risk) - Quantitative risk analysis framework
- NIST Risk Management Framework (RMF) - NIST SP 800-37 Rev. 2
- OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation)
- CRAMM (CCTA Risk Analysis and Management Method)
- Bowtie methodology for risk visualization
- FMEA (Failure Mode and Effects Analysis)
- ISO 31010:2019 Risk Assessment Techniques

**GRC Platforms & Tools**:
- ServiceNow GRC (Integrated Risk Management module)
- RSA Archer Suite (Enterprise & Operational Risk Management)
- MetricStream Risk Management Solution
- LogicGate Risk Cloud
- OneTrust GRC & Privacy Management
- SAI Global Compliance 360
- Resolver Risk Intelligence Platform
- Riskonnect Integrated Risk Management
- NAVEX Global RiskRate
- Quantivate Risk Management

**Risk Quantification & Analysis**:
- FAIR-U (FAIR Uncertainty Calculator)
- OpenFAIR Risk Analysis Tool
- Monte Carlo simulation for risk modeling
- Value at Risk (VaR) methodologies
- Expected Loss calculations
- Annualized Loss Expectancy (ALE = SLE x ARO)
- PERT (Program Evaluation and Review Technique) for risk estimation
- Decision tree analysis for risk scenarios
- Sensitivity analysis and scenario planning

**Governance & Compliance Standards**:
- COBIT 2019 (EDM03 Ensure Risk Optimization, APO12 Manage Risk)
- ISO 38500:2015 IT Governance framework
- ITIL 4 Service Management (Risk Management Practice)
- TOGAF Enterprise Architecture (Risk Management)
- PMBOK Guide (Project Risk Management - Chapter 11)
- Prince2 Risk Management theme
- SOC 2 Trust Services Criteria (CC4.1, CC9.1 Risk Assessment)
- ISO 27001:2022 (Clause 6.1 Risk Assessment, Annex A.5.7)
- NIST Cybersecurity Framework (Identify function - Risk Assessment)
- PCI DSS v4.0 (Requirement 12.3 Risk Assessment)
- HIPAA Security Rule (§164.308 Risk Analysis)
- GDPR Article 32 (Risk-based security measures)
- SOX Section 404 (Internal Control Risk Assessment)
- NIST SP 800-30 Guide for Conducting Risk Assessments
- NIST SP 800-53 Rev. 5 (RA family - Risk Assessment controls)

**Industry-Specific Risk Standards**:
- Basel III/IV for financial services operational risk
- Solvency II for insurance risk management
- FDA 21 CFR Part 11 for pharmaceutical risk
- NERC CIP for energy sector critical infrastructure
- FedRAMP risk assessment for cloud services

**Reference**: Consult Enterprise Risk Management team and organizational architecture group for detailed guidance on framework selection, risk assessment methodologies, and GRC platform implementation

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
