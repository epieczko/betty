# Name: iso-27001-mapping

## Executive Summary

The ISO 27001 Mapping artifact provides a comprehensive traceability matrix linking organizational security controls, policies, procedures, and technical implementations to specific ISO/IEC 27001:2022 Annex A controls (114 controls across 4 themes and 14 control categories). This critical audit artifact enables organizations to demonstrate systematic coverage of all required controls, identify control gaps, and provide auditors with evidence of how organizational practices satisfy certification requirements.

In organizations pursuing ISO 27001 certification or maintaining existing certificates through annual surveillance audits and tri-annual re-certification, this mapping serves as the primary artifact for Stage 1 documentation review and Stage 2 implementation testing. Modern GRC platforms like Vanta, Drata, Secureframe, and dedicated ISO 27001 tools (ISMS.online, Scytale, Tugboat Logic) automate mapping maintenance and evidence collection, reducing certification preparation time from 12-18 months to 6-9 months for initial certification and ongoing audit cycles from 4-6 weeks to 1-2 weeks.

The ISO 27001 mapping enables quantifiable compliance metrics including: 1) Control coverage completeness showing 114/114 controls mapped with evidence, 2) Control effectiveness scores averaging 85%+ across all control categories, 3) Gap remediation velocity tracking closure of control deficiencies within 30-60 days, 4) Evidence collection automation reducing manual evidence gathering by 70%, and 5) Certification maintenance demonstrating year-over-year control maturity improvement of 15-20%.

### Strategic Importance

- **Certification Achievement**: Provides structured roadmap to ISO 27001 certification, with clear mapping reducing certification timeline by 40-50%
- **Audit Readiness**: Enables rapid response to auditor requests with pre-mapped control evidence, reducing audit duration from 4-6 weeks to 1-2 weeks
- **Control Gap Analysis**: Identifies missing or weak controls requiring remediation before surveillance audits, preventing audit findings
- **Customer Assurance**: Demonstrates systematic information security management to enterprise customers requiring ISO 27001 certification
- **Regulatory Alignment**: Provides foundation for meeting GDPR Article 32 (security of processing) and other regulations referencing ISO 27001
- **Risk-Based Approach**: Aligns organizational risk treatment with ISO 27001 Clause 6.1.3 requirements for risk assessment and treatment
- **Continuous Improvement**: Supports ISO 27001 Clause 10 (improvement) requirements through systematic control monitoring and enhancement

## Purpose & Scope

### Primary Purpose

This artifact establishes comprehensive bidirectional traceability between organizational information security management system (ISMS) components and all 114 ISO/IEC 27001:2022 Annex A controls, enabling certification bodies to verify systematic control implementation and providing ongoing evidence for annual surveillance audits and tri-annual re-certification cycles. The mapping demonstrates how organizational policies (security-policy-library), technical controls (security configurations, access controls, encryption), operational procedures (incident response, change management, backup), and monitoring processes (log analysis, vulnerability management, access reviews) collectively satisfy each ISO 27001 control objective. This artifact solves the critical certification challenge of proving control completeness and effectiveness by maintaining real-time linkage between controls and evidence sources (logs, tickets, screenshots, reports) automatically collected from integrated security tools, reducing auditor evidence requests by 70% and enabling same-day audit responses for most control testing scenarios.

### Scope

**In Scope**:
- All 114 ISO/IEC 27001:2022 Annex A controls across 4 organizational themes (5 controls), 4 people themes (8 controls), 14 physical controls, and 91 technological controls
- Mapping from each Annex A control to implemented organizational controls (policies, procedures, technical configurations)
- Evidence collection points showing where audit evidence is generated and stored (SIEM, GRC platform, ticketing system, cloud logs)
- Control ownership assignment identifying responsible parties for each control implementation
- Control applicability statements and justifications for controls marked as "not applicable"
- Gap analysis documentation for controls that are partially implemented or require remediation
- Control testing frequency and last test date for all implemented controls
- Statement of Applicability (SoA) linking risk treatment decisions to control selection
- Integration with risk assessment showing which risks are mitigated by which controls
- Automated evidence collection workflows from security tools (Wiz, Crowdstrike, Okta, Vanta, AWS CloudTrail, Azure Monitor)
- Control effectiveness metrics and maturity scoring (Level 1-5 per control)
- Remediation tracking for control deficiencies identified during audits or internal assessments
- Compliance dashboard showing real-time control implementation status across all 114 controls
- Certification audit history including findings, observations, and continuous improvement actions

**Out of Scope**:
- Detailed risk assessment methodology (documented in risk register and risk assessment artifacts)
- Full policy and procedure text (maintained in security-policy-library)
- Technical implementation details for specific security controls (documented in system security plans)
- Vendor management and third-party risk assessments (covered in vendor risk management artifacts)
- Business continuity and disaster recovery detailed plans (separate BCP/DR documentation)

### Target Audience

**Primary Audience**:
- **ISO 27001 Lead Auditors and Certification Bodies** (BSI, LRQA, A-LIGN, Schellman) requiring evidence during Stage 1 and Stage 2 audits
- **Information Security Managers and ISMS Owners** responsible for ISO 27001 program management and certification maintenance
- **Compliance Officers and GRC Analysts** managing ongoing control monitoring and audit readiness for surveillance audits

**Secondary Audience**:
- **CISOs and Security Leadership** reviewing control coverage and maturity for strategic security planning
- **Internal Audit Teams** conducting pre-certification gap assessments and continuous control testing
- **Enterprise Customers** requiring ISO 27001 certification evidence during security due diligence
- **Control Owners** across IT, security, HR, facilities, and legal responsible for specific control implementation

## Document Information

**Format**: Multiple

**File Pattern**: `*.iso-27001-mapping.*`

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

**Complete Annex A Coverage**: Map all 114 ISO 27001:2022 Annex A controls with explicit applicability decisions (applicable, not applicable with justification, partially applicable with remediation plan)
**Statement of Applicability (SoA) Integration**: Link control selection to risk treatment decisions documented in risk assessment, showing which risks drive which control implementations
**Automated Evidence Collection**: Integrate GRC platforms (Vanta, Drata, Secureframe, ISMS.online) with security tools to auto-collect control evidence reducing manual effort by 70%+
**Control Ownership Assignment**: Designate specific individuals (not just roles) as control owners responsible for implementation, monitoring, and annual attestation
**Evidence Timestamping**: Ensure all control evidence includes collection timestamp to demonstrate recency for auditor testing (most evidence should be <30 days old)
**Maturity Level Scoring**: Rate each control on 5-level maturity scale (1=Ad-hoc, 2=Repeatable, 3=Defined, 4=Managed, 5=Optimizing) to track continuous improvement
**Quarterly Control Testing**: Conduct automated or manual control testing quarterly for critical controls, annually for all others, documenting test results in mapping
**Gap Remediation Tracking**: For controls marked "partially implemented" or with findings, track remediation progress with target dates (Critical: 30 days, High: 60 days, Medium: 90 days)
**Multi-Evidence Approach**: Map multiple evidence sources per control (policy, procedure, technical config, logs, screenshots) to provide defense-in-depth for audit
**Risk-Based Prioritization**: Focus implementation and testing effort on controls that mitigate high-risk threats identified in risk assessment
**Audit Readiness Testing**: Conduct pre-audit gap assessments 60-90 days before surveillance audits to identify and remediate control deficiencies
**Evidence Repository Organization**: Structure evidence folders by Annex A control number (A.5.1, A.6.1, etc.) for rapid auditor access during Stage 2 testing
**Control Testing Automation**: Use automated compliance testing tools (Prowler, ScoutSuite, CloudSploit) to continuously validate technical control effectiveness
**ISMS Context Documentation**: Map controls to organizational context including scope, boundaries, interested parties, and internal/external issues per Clause 4
**Annual SoA Review**: Review and update Statement of Applicability annually or when significant changes occur (new systems, acquisitions, regulatory changes)
**Certification Body Alignment**: Understand specific certification body preferences (BSI, LRQA, Schellman) for evidence format and control interpretation
**Control Integration Documentation**: Show how multiple controls work together (defense-in-depth) rather than treating each control in isolation
**Continuous Monitoring Dashboards**: Maintain real-time compliance dashboards showing control implementation status, evidence freshness, and gap remediation progress
**Audit Finding Correlation**: Link past audit findings to specific controls to show correction and prevent recurrence in future audits
**Cloud Control Mapping**: For cloud-native organizations, map cloud provider responsibility matrix (AWS, Azure, GCP) to show shared responsibility for controls
**Version Control for Controls**: Track changes to control implementations over time to demonstrate continuous improvement and maturity progression
**Pre-Certification Consultant Engagement**: Engage ISO 27001 consultants 6-12 months before certification to review mapping completeness and identify gaps
**Control Compensating Controls**: Where controls can't be fully implemented, document compensating controls with risk acceptance by management
**Evidence Collection SLAs**: Define maximum age for evidence types (logs: 30 days, access reviews: 90 days, training records: 365 days) to maintain audit readiness

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

**ISO/IEC 27001:2022 Standard Structure**:
- Clause 4: Context of the Organization (4.1 Understanding organization and context, 4.2 Understanding needs and expectations, 4.3 Determining scope, 4.4 ISMS)
- Clause 5: Leadership (5.1 Leadership and commitment, 5.2 Policy, 5.3 Organizational roles)
- Clause 6: Planning (6.1 Actions to address risks and opportunities, 6.2 Information security objectives, 6.3 Planning of changes)
- Clause 7: Support (7.1 Resources, 7.2 Competence, 7.3 Awareness, 7.4 Communication, 7.5 Documented information)
- Clause 8: Operation (8.1 Operational planning, 8.2 Information security risk assessment, 8.3 Information security risk treatment)
- Clause 9: Performance Evaluation (9.1 Monitoring and measurement, 9.2 Internal audit, 9.3 Management review)
- Clause 10: Improvement (10.1 Nonconformity and corrective action, 10.2 Continual improvement)

**ISO 27001:2022 Annex A Control Themes**:
- Organizational Controls (5 controls): A.5.1-A.5.37 covering policies, asset management, HR security, supplier relationships
- People Controls (8 controls): A.6.1-A.6.8 covering screening, terms of employment, awareness, disciplinary process
- Physical Controls (14 controls): A.7.1-A.7.14 covering physical security perimeters, entry controls, equipment security
- Technological Controls (87 controls): A.8.1-A.8.34 covering endpoint, network, application, data security, cryptography, incident management

**ISO 27002:2022 Implementation Guidance**:
- Provides detailed implementation guidance for each of the 114 Annex A controls
- Includes control attributes (control type, information security properties, cybersecurity concepts, operational capabilities, security domains)
- References to other ISO standards (ISO 27017 cloud security, ISO 27018 cloud privacy, ISO 27701 privacy)

**Related ISO Standards**:
- ISO/IEC 27017:2015: Cloud services information security controls
- ISO/IEC 27018:2019: Protection of PII in public cloud services
- ISO/IEC 27701:2019: Privacy Information Management System (PIMS) extending ISO 27001 for GDPR
- ISO/IEC 27032:2012: Cybersecurity guidelines
- ISO/IEC 27033 (1-7): Network security standards
- ISO/IEC 27035:2016: Information security incident management
- ISO/IEC 27036 (1-4): Information security for supplier relationships
- ISO 31000:2018: Risk management guidelines (supports ISO 27001 Clause 6 planning)
- ISO 9001:2015: Quality management (compatible management system standard)

**SOC 2 Trust Service Criteria Alignment**:
- Many ISO 27001 Annex A controls directly map to SOC 2 TSC controls
- Organizations often pursue dual ISO 27001 and SOC 2 certification with shared control implementations
- Control mapping between ISO 27001 and SOC 2 reduces audit effort for organizations holding both certifications

**NIST Framework Alignment**:
- NIST CSF 2.0: Maps to ISO 27001 controls through crosswalk documents
- NIST SP 800-53: Federal systems align NIST controls to ISO 27001 Annex A
- NIST Privacy Framework: Aligns with ISO 27701 privacy extension

**GDPR Compliance Alignment**:
- Article 32 Security of Processing explicitly references "state of the art" including ISO 27001
- ISO 27001 certification demonstrates GDPR technical and organizational measures
- ISO 27701 extension provides specific GDPR Article 30 (ROPA) and DPO requirements

**PCI-DSS Alignment**:
- PCI-DSS requirements map to ISO 27001 controls (access control, encryption, monitoring, incident response)
- Organizations often maintain both certifications with shared control evidence

**Cloud Provider Certifications**:
- AWS: ISO 27001, ISO 27017, ISO 27018 certified with shared responsibility model
- Microsoft Azure: ISO 27001, ISO 27017, ISO 27018 certified
- Google Cloud Platform: ISO 27001, ISO 27017, ISO 27018 certified
- Customer responsibility to implement controls for customer-managed components

**Certification Bodies and Accreditation**:
- ANAB (ANSI National Accreditation Board): U.S. accreditation for ISO 27001 certification bodies
- UKAS (United Kingdom Accreditation Service): UK accreditation
- DAkkS (Deutsche Akkreditierungsstelle): German accreditation
- Major certification bodies: BSI, LRQA, A-LIGN, Schellman, TUV, SGS, Bureau Veritas
- IAF (International Accreditation Forum): Ensures mutual recognition of accredited certifications globally

**ISO 27001 Implementation Tools**:
- Vanta: Automated ISO 27001 compliance with continuous monitoring
- Drata: ISO 27001 program automation with evidence collection
- Secureframe: Compliance automation for ISO 27001, SOC 2, HIPAA
- ISMS.online: Dedicated ISO 27001 management platform
- Scytale: Automated compliance for startups and scale-ups
- Tugboat Logic: GRC platform with ISO 27001 support
- StandardFusion: Policy management and ISO 27001 compliance
- Apptega: Cybersecurity and compliance management platform

**Industry-Specific Guidance**:
- Financial Services: ISO 27001 + PCI-DSS + local banking regulations
- Healthcare: ISO 27001 + HIPAA + ISO 27799 (health informatics)
- Government: ISO 27001 + FedRAMP + FISMA + NIST SP 800-53
- Cloud Services: ISO 27001 + ISO 27017 + ISO 27018 + SOC 2
- Telecommunications: ISO 27001 + ETSI specifications
- Critical Infrastructure: ISO 27001 + NERC CIP + IEC 62443

**Reference**: Consult ISO 27001 lead implementer consultants, certification body readiness assessments, and GRC platform implementation teams for detailed guidance on control mapping, evidence collection automation, and audit preparation strategies. Organizations should budget 6-12 months for initial certification with dedicated ISMS owner and 20-40% FTE commitment from control owners across organization.

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
