# Name: privacy-impact-assessment

## Executive Summary

The Privacy Impact Assessment (PIA), also known as Data Protection Impact Assessment (DPIA) under GDPR Article 35, is a systematic privacy risk assessment process that identifies, evaluates, and mitigates privacy risks associated with new projects, systems, technologies, or data processing operations that are likely to result in high risk to individuals' rights and freedoms. This mandatory privacy artifact evaluates necessity and proportionality of processing, assesses privacy risks, and documents risk mitigation measures.

Modern PIAs leverage privacy assessment platforms like OneTrust Privacy Impact Assessment, TrustArc Assessment Manager, and Securiti.ai DPIA Automation to streamline assessment workflows, maintain assessment libraries, and track remediation progress. Organizations conduct PIAs for GDPR Article 35 mandatory scenarios (systematic monitoring, large-scale sensitive data processing, automated decision-making), apply NIST Privacy Framework risk management principles, and follow ISO 27701 privacy controls to demonstrate accountability under privacy regulations worldwide including GDPR, CCPA/CPRA, PIPEDA, and LGPD.

### Strategic Importance

- **GDPR Article 35 Compliance**: Satisfies mandatory DPIA requirements for high-risk processing including systematic monitoring, Article 9 special categories at scale, automated decision-making with legal effects
- **Privacy Risk Identification**: Systematically identifies risks to individual rights and freedoms including discrimination, identity theft, financial loss, reputational damage, and loss of confidentiality
- **Necessity and Proportionality**: Evaluates whether processing is necessary for stated purpose and proportionate to privacy risks through data minimization analysis
- **Privacy by Design Implementation**: Operationalizes GDPR Article 25 Privacy by Design and by Default principles through proactive risk mitigation
- **Regulatory Penalty Avoidance**: Mitigates GDPR Article 83 fines for failure to conduct mandatory DPIAs (up to €10 million or 2% of global revenue)
- **Stakeholder Transparency**: Demonstrates accountability to supervisory authorities, executives, and data subjects through documented privacy risk assessment
- **Decision Support**: Provides privacy risk intelligence to product teams, engineering, and leadership for go/no-go decisions on high-risk initiatives

## Purpose & Scope

### Primary Purpose

This artifact serves as a systematic risk assessment evaluating privacy risks to individuals from new or changed data processing operations, determining GDPR Article 35 necessity and proportionality compliance, identifying risk mitigation measures aligned with Privacy by Design principles, and supporting informed decision-making on whether to proceed with high-risk processing activities.

### Scope

**In Scope**:
- GDPR Article 35 mandatory DPIA triggers (systematic monitoring, Article 9 special categories at scale, automated decision-making per Article 22)
- Processing operation description including data categories, purposes, recipients, retention periods, and data flows
- Necessity and proportionality assessment evaluating whether processing is essential for stated purpose with minimal privacy intrusion
- Privacy risk identification covering risks to individual rights (discrimination, identity theft, unauthorized disclosure, profiling harm)
- Risk likelihood and impact assessment using privacy risk matrices (e.g., catastrophic/likely to negligible/rare scale)
- Privacy by Design and by Default controls per GDPR Article 25 (pseudonymization, encryption, access controls, data minimization)
- Data subject consultation documenting engagement with individuals or representative organizations per Article 35(9)
- DPO consultation and review per GDPR Article 35(2) requirement for DPO advice on DPIA execution
- Transfer Impact Assessments (TIAs) when processing involves international data transfers per Schrems II requirements
- Vendor privacy risk assessment for third-party processors and subprocessors handling personal data
- Residual risk evaluation after mitigation measures with recommendations for supervisory authority consultation if high risk remains

**Out of Scope**:
- Cybersecurity threat assessments focused on technical vulnerabilities (handled by Security Risk Assessment)
- Business impact analysis for system availability or disaster recovery (covered by BCP/DR assessment)
- Vendor security assessments focused on information security controls (managed through Vendor Risk Management)
- General data inventory or data mapping exercises (addressed by Data Discovery and ROPA artifacts)
- Privacy policy public disclosures (documented in Privacy Policy artifact)
- Specific implementation details of technical controls (covered in Security Architecture)

### Target Audience

**Primary Audience**:
- Data Protection Officers (DPOs) reviewing DPIAs per GDPR Article 35(2) and providing privacy risk guidance
- Privacy Teams conducting systematic privacy risk assessments for new projects and processing operations
- Product Managers and Business Owners understanding privacy constraints and risk mitigation requirements
- Privacy Counsel evaluating legal risks, necessity/proportionality compliance, and supervisory authority consultation needs

**Secondary Audience**:
- Engineering and Development Teams implementing Privacy by Design controls identified in DPIA recommendations
- Information Security Teams contributing to technical risk mitigation measures (encryption, access controls)
- Compliance Teams tracking DPIA completion for audit and regulatory examination readiness
- Executive Leadership making informed decisions on high-risk initiatives with privacy risk transparency

## Document Information

**Format**: Markdown

**File Pattern**: `*.privacy-impact-assessment.md`

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

### Assessment Methodology

**Approach**:
- `assessmentFramework`: Framework or standard used (e.g., NIST, ISO, proprietary)
- `assessmentScope`: Systems, processes, or areas assessed
- `evaluationCriteria`: Specific criteria used for evaluation
- `maturityModel`: Maturity levels if applicable (Initial, Managed, Defined, etc.)
- `scoringMethodology`: How scores or ratings are assigned

**Assessment Execution**:
- `assessmentPeriod`: Time period covered by the assessment
- `dataCollectionMethods`: Interviews, documentation review, testing, observation
- `participantsInterviewed`: Roles and number of people interviewed
- `evidenceReviewed`: Types and volume of evidence examined
- `limitations`: Any limitations or constraints on the assessment

### Findings & Results

**Summary Results**:
- `overallRating`: Aggregate assessment result
- `maturityLevel`: Current maturity level if using maturity model
- `complianceScore`: Percentage compliance if applicable
- `trendAnalysis`: Comparison to previous assessments

**Detailed Findings**:
- `findingId`: Unique identifier for each finding
- `findingCategory`: Category or control area
- `findingTitle`: Concise title
- `description`: Detailed description of finding
- `severity`: Critical | High | Medium | Low
- `evidence`: Supporting evidence for finding
- `impact`: Business or technical impact
- `likelihood`: Probability of occurrence if risk-related
- `currentState`: Current state or practice observed
- `desiredState`: Target state or required practice
- `gap`: Specific gap between current and desired
- `recommendations`: Specific remediation recommendations
- `priority`: Prioritization for remediation
- `estimatedEffort`: Effort required to remediate

### Remediation Plan

**Recommendations Summary**:
- `totalRecommendations`: Count by severity
- `quickWins`: High-value, low-effort improvements
- `strategicInitiatives`: Long-term, high-effort improvements
- `costBenefitAnalysis`: Estimated cost vs. benefit for major recommendations

**Remediation Roadmap**:
- `phase1Immediate`: 0-3 months, critical items
- `phase2NearTerm`: 3-6 months, high priority items
- `phase3MidTerm`: 6-12 months, medium priority items
- `phase4LongTerm`: 12+ months, strategic initiatives

**Implementation Tracking**:
- `recommendationOwner`: Who is responsible for each item
- `targetCompletionDate`: When remediation should be complete
- `statusTracking`: Mechanism for tracking progress
- `successCriteria`: How completion will be verified


## Best Practices

**Early Assessment Timing**: Conduct DPIAs at project inception before system design decisions are finalized, enabling Privacy by Design integration and cost-effective risk mitigation
**GDPR Article 35 Trigger Check**: Systematically evaluate whether processing meets mandatory DPIA triggers (systematic monitoring, Article 9 special categories at scale, Article 22 automated decisions, EDPB criteria list)
**DPO Consultation**: Seek DPO advice per GDPR Article 35(2) throughout DPIA process including assessment scoping, risk evaluation, and mitigation recommendations
**Necessity and Proportionality Analysis**: Rigorously assess whether processing is necessary for stated purpose and proportionate to privacy intrusion using data minimization principles
**Privacy Risk Matrix**: Apply consistent risk scoring methodology (e.g., likelihood × impact matrix) with clear definitions of catastrophic/high/medium/low/negligible risk levels
**Data Subject Consultation**: Document engagement with affected individuals or representative organizations per GDPR Article 35(9) to understand privacy concerns and perspectives
**Privacy by Design Measures**: Identify technical and organizational measures aligned with GDPR Article 25 including pseudonymization, encryption, access controls, data minimization, and privacy-enhancing technologies
**Automated DPIA Triggers**: Configure privacy platforms (OneTrust, TrustArc, Securiti.ai) to automatically flag new processing requiring DPIAs based on data discovery, system changes, or assessment criteria
**Transfer Impact Assessment Integration**: For international transfers, incorporate TIA evaluating destination country laws, government access risks, and supplementary measures per EDPB Recommendations 01/2020
**Vendor Privacy Assessment**: Assess processor and subprocessor privacy risks including data localization, security measures, breach notification capabilities, and audit rights
**Residual Risk Evaluation**: After mitigation measures, evaluate remaining privacy risks and determine whether Article 36 prior consultation with supervisory authority is required
**DPIA Repository**: Maintain centralized DPIA library in OneTrust, SharePoint, or GRC platform for audit trail, knowledge sharing, and regulatory examination readiness
**Regular Reviews**: Re-assess DPIAs when processing changes materially, new risks emerge, or supervisory authority guidance updates (typically annual review minimum)
**Plain Language Documentation**: Write DPIAs in accessible language for non-technical stakeholders including executives, supervisory authorities, and potentially data subjects
**Supervisory Authority Consultation**: When high residual risks remain despite mitigation, consult supervisory authority per GDPR Article 36 before commencing processing
**DPIA Template Standardization**: Use ICO, CNIL, or organizational DPIA templates ensuring consistency, completeness, and alignment with supervisory authority expectations
**Cross-Functional Collaboration**: Engage product, engineering, security, legal, and business stakeholders to capture complete risk picture and feasible mitigations
**Remediation Tracking**: Document DPIA recommendations with assigned owners, target completion dates, and status tracking in OneTrust, Jira, or GRC platforms
**Accountability Evidence**: Retain completed DPIAs as accountability documentation per GDPR Article 5(2) demonstrating compliance with privacy obligations
**Training and Awareness**: Train product managers, engineers, and business teams to identify DPIA triggers and initiate assessments early in project lifecycle
**Version Control**: Store DPIAs in centralized version control (Git, SharePoint with versioning) maintaining complete assessment history and update audit trail
**Approval Authority**: Define clear approval authority (DPO, Privacy Counsel, Executive depending on risk level) before proceeding with high-risk processing

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

**Privacy Regulations - DPIA/PIA Requirements**:
- GDPR Article 35 - Data Protection Impact Assessment mandatory requirements and triggers
- GDPR Article 36 - Prior consultation with supervisory authority when high residual risk remains
- UK GDPR Article 35 - UK-specific DPIA requirements post-Brexit
- CCPA/CPRA - California privacy risk assessments for high-risk processing
- PIPEDA - Canadian Privacy Impact Assessment guidance from Privacy Commissioner
- APPI (Japan) - Privacy impact assessment requirements for high-risk processing
- LGPD (Brazil) - Data protection impact assessment for high-risk operations
- POPIA (South Africa) - Processing operations impact assessment requirements
- China PIPL - Personal information protection impact assessment for high-risk processing

**DPIA Frameworks and Standards**:
- ISO 27701:2019 - Privacy Information Management System DPIA requirements (Annex A/B controls)
- ISO 29134:2017 - Privacy impact assessment standard with methodology and guidelines
- NIST Privacy Framework - Core function ID.RA-P for privacy risk assessment
- AICPA/CICA Privacy Management Framework - Privacy risk assessment and mitigation principles
- Privacy by Design Framework - 7 foundational principles by Ann Cavoukian
- CNIL DPIA Methodology - French DPA official DPIA guidance and templates
- ICO DPIA Guidance - UK Information Commissioner's Office comprehensive DPIA framework
- EDPB Guidelines 09/2020 - Relevant and reasoned objections for lead supervisory authority decisions

**Privacy Risk Assessment Platforms**:
- OneTrust Privacy Impact Assessment - DPIA workflow automation, assessment library, remediation tracking
- TrustArc Assessment Manager - Privacy risk assessment questionnaires and DPIA templates
- Securiti.ai DPIA Automation - Automated privacy impact assessment for cloud and SaaS applications
- WireWheel DPIA Management - Privacy assessment workflows and risk scoring
- Collibra Privacy - DPIA process management integrated with data governance
- BigID Privacy Assessment - Automated DPIA triggers based on data discovery findings
- DataGrail Privacy Assessment - Risk assessment automation for data processing activities
- Osano DPIA Templates - Standardized privacy impact assessment questionnaires
- Ethyca Fides - Open-source privacy engineering with DPIA integration
- TrustArc Nymity - Privacy assessments and DPIA collaboration workflows

**GDPR Supervisory Authority DPIA Guidance**:
- CNIL (France) DPIA Template and Methodology - Official French DPA comprehensive guidance
- ICO (UK) DPIA Guidance - Detailed UK Information Commissioner's Office framework
- Irish DPC DPIA Guidance - Irish Data Protection Commission DPIA recommendations
- Spanish AEPD DPIA Guide - Spanish Data Protection Agency assessment methodology
- German State DPAs DPIA Guidance - Coordinated German supervisory authority recommendations
- EDPB DPIA List - Supervisory authority lists of processing requiring mandatory DPIAs
- WP29 Guidelines on DPIA (wp248rev.01) - Article 29 Working Party foundational guidance

**Privacy by Design Frameworks**:
- GDPR Article 25 - Data protection by design and by default requirements
- Privacy by Design 7 Foundational Principles - Proactive, privacy as default, embedded into design
- ISO 31000:2018 - Risk management principles applied to privacy risk assessment
- NIST Risk Management Framework - Adapted for privacy risk assessment and mitigation
- FAIR (Factor Analysis of Information Risk) - Quantitative privacy risk analysis methodology
- OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) - Privacy risk assessment

**AI and Automated Decision-Making Assessment**:
- GDPR Article 22 - Automated individual decision-making including profiling
- EDPB Guidelines 3/2019 - Processing of personal data through video devices
- EDPB Guidelines 4/2019 - Article 25 Data Protection by Design and by Default
- ICO AI Auditing Framework - UK guidance on AI system fairness and privacy assessment
- NIST AI Risk Management Framework - Privacy considerations in AI systems
- IEEE P7000 Series - Ethical considerations in AI and autonomous systems
- ISO/IEC TR 24028:2020 - AI trustworthiness assessment
- EU AI Act - High-risk AI system conformity assessment and DPIA integration

**Industry-Specific Privacy Assessment**:
- HIPAA Privacy Rule - Healthcare privacy impact assessment for PHI processing
- PCI DSS - Payment card data privacy and security assessment requirements
- COPPA - Children's privacy impact assessment for online services targeting minors
- FERPA - Educational records privacy assessment for student information systems
- GLBA - Financial privacy assessment for customer information processing

**Transfer Impact Assessment (TIA)**:
- EDPB Recommendations 01/2020 - Supplementary measures for international transfers post-Schrems II
- ICO International Transfers Guidance - UK TIA requirements and methodology
- CNIL Transfer Impact Assessment Tools - French DPA TIA templates and guidance
- Schrems II (CJEU C-311/18) - Privacy Shield invalidation and TIA obligations
- EDPB Recommendations 02/2020 - European Essential Guarantees for surveillance measures

**Reference**: Consult Data Protection Officer (DPO), Privacy Teams, and Privacy Counsel for detailed guidance on DPIA framework application and supervisory authority compliance

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
