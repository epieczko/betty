# Name: export-control-screening

## Executive Summary

The Export Control Screening artifact documents compliance verification procedures for software, cryptography, and technology exports under U.S. Export Administration Regulations (EAR), International Traffic in Arms Regulations (ITAR), and international export control regimes. This artifact provides systematic screening of products, technologies, customers, and destinations against denied parties lists, ECCN classification requirements, and license exception eligibility ensuring legal distribution of controlled items and technologies.

As a critical compliance control for software distribution and technology transfer, export control screening records serve compliance officers verifying export authorization, legal teams assessing regulatory requirements, release managers implementing geographic restrictions, and executives managing regulatory risk. Integration with Bureau of Industry and Security (BIS) denied parties screening, ECCN self-classification tools, encryption registration (ENC) procedures, and automated compliance platforms ensures systematic verification before international software distribution while maintaining comprehensive audit trails for regulatory examinations.

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

This artifact serves as comprehensive documentation of export compliance verification including ECCN (Export Control Classification Number) self-classification for software and cryptography, denied party screening against BIS Denied Persons List and OFAC SDN List, license exception determination (TSU, ENC), encryption registration with BIS, and geographic distribution restrictions. It provides evidence of export compliance due diligence, supports regulatory audits, enables incident response for export violations, and demonstrates adherence to EAR, ITAR, Wassenaar Arrangement, and international export control requirements.

### Scope

**In Scope**:
- ECCN classification for software (5D002 - cryptographic software, 5D992 - mass market cryptography)
- Encryption strength assessment (key length, algorithms, cryptographic functions)
- BIS encryption registration and classification requests
- License exception determination (TSU Technology and Software Unrestricted, ENC encryption)
- Denied party screening (BIS Denied Persons, Entity List, Unverified List)
- OFAC sanctions screening (Specially Designated Nationals SDN List)
- Wassenaar Arrangement dual-use controls
- EU Dual-Use Regulation (EU 2021/821)
- Country-based restrictions (embargoed countries, E:1 E:2 classification)
- Cryptography export notifications and self-classifications
- Open-source software exception eligibility (publicly available encryption)
- Mass market encryption eligibility (≤64-bit symmetric, consumer products)
- Technology transfer controls (foreign person access, deemed exports)

**Out of Scope**:
- ITAR-controlled defense articles (separate DDTC registration and licensing)
- Physical product export logistics (covered by shipping/customs artifacts)
- Tariff classification and customs duties (covered by trade compliance)
- International privacy regulations (GDPR, covered by privacy compliance)
- Product safety certifications (CE, FCC, covered by product compliance)

### Target Audience

**Primary Audience**:
- Export Compliance Officers performing ECCN classification and screening
- Legal Counsel assessing export control requirements and violations
- Trade Compliance Specialists managing denied party screening

**Secondary Audience**:
- Release Engineers implementing geographic distribution controls
- Product Managers determining market availability and restrictions
- Engineering Leaders managing technology transfer and foreign person access

## Document Information

**Format**: Markdown

**File Pattern**: `*.export-control-screening.md`

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

**ECCN Self-Classification**: Determine ECCN for all software products before distribution; document classification rationale; retain classification memos 5+ years
**Encryption Registration**: File one-time BIS encryption registration within 30 days of first export; update annually if product changes significantly
**Mass Market Eligibility**: Verify mass market encryption criteria (≤64-bit symmetric, consumer products, retail availability) for 5D992 classification
**TSU/ENC Exceptions**: Leverage License Exception TSU for publicly available software; use ENC exception for encryption products meeting criteria
**Denied Party Screening**: Screen all international customers, distributors, end-users against consolidated screening lists before each transaction
**Automated Screening**: Implement automated denied party screening in order management systems; screen at order entry and fulfillment
**Geographic Controls**: Implement IP geolocation and download restrictions for embargoed countries (Cuba, Iran, North Korea, Syria, Russia regions)
**Open Source Notifications**: For publicly available encryption software on GitHub/GitLab, provide BIS notification URL and ECCN classification
**Deemed Export Controls**: Screen foreign person employees for access to controlled technology; implement technology transfer agreements
**Documentation Retention**: Retain export classification records, screening results, licenses, exception claims for 5+ years per EAR recordkeeping requirements
**Sanctions Compliance**: Monitor OFAC sanctions updates; implement sectoral sanctions (Russia, Venezuela); screen beneficial owners
**License Requirements**: If license required, file application with BIS; track license conditions, expiration, reporting requirements
**Red Flags**: Train staff on export control red flags (evasive answers, unusual shipping, sanctioned destinations); escalate suspicious inquiries
**Voluntary Disclosure**: If export violation discovered, consult counsel immediately; prepare VSD to BIS Office of Export Enforcement within 30 days
**Annual Reviews**: Review ECCN classifications annually or when product changes; update encryption registrations; refresh denied party screening procedures
**Compliance Training**: Train sales, engineering, shipping staff on export controls; conduct annual refresher training; document training completion
**Audit Preparedness**: Maintain comprehensive audit trail of classifications, screenings, licenses, exceptions; prepare for potential BIS audit
**Legal Counsel**: Engage export control counsel for ECCN determinations, license applications, VSD filings, and regulatory interpretation

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

**U.S. Export Control Regulations**:
- Export Administration Regulations (EAR) 15 CFR Parts 730-774
- International Traffic in Arms Regulations (ITAR) 22 CFR Parts 120-130
- EAR Part 740 (License Exceptions: TSU, ENC, TMP, BAG)
- EAR Part 742.15 (Encryption Items)
- EAR Part 734 (Scope of EAR - software, technology)
- EAR Part 774 Supplement No. 1 (Commerce Control List)
- ECCN 5D002 (Information Security Software)
- ECCN 5D992 (Software not controlled by 5D002)

**ECCN Classification Resources**:
- BIS ECCN Classification Tool
- Commerce Control List (CCL) Category 5 Part 2
- Encryption Registration and Classification Requests
- Self-Classification Report Procedures
- BIS Advisory Opinions (formal ECCN determinations)
- Commodity Jurisdiction (CJ) determinations (EAR vs. ITAR)

**Denied Party Screening Lists**:
- BIS Denied Persons List (DPL)
- BIS Entity List (restricted end-users)
- BIS Unverified List (UVL)
- BIS Military End User (MEU) List
- OFAC Specially Designated Nationals (SDN) List
- OFAC Consolidated Sanctions List
- Debarred Parties List (State Department)
- FBI Most Wanted Terrorists
- Nonproliferation Sanctions Lists

**License Exceptions**:
- TSU (Technology and Software Unrestricted)
- ENC (Encryption Commodities, Software, and Technology)
- TMP (Temporary Imports, Exports, Re-exports)
- BAG (Baggage)
- APR (Additional Permissive Re-exports)
- RPL (Servicing and Replacement of Parts and Equipment)

**Encryption Controls**:
- BIS Encryption Registration (one-time annual reporting)
- Self-Classification Reports for ENC license exception
- Mass Market Encryption (5A992, 5D992 - ≤64-bit symmetric)
- Publicly Available Encryption Software exception
- Open-source software and encryption exemptions
- Wassenaar Arrangement Category 5 Part 2 (cryptography)

**International Export Control Regimes**:
- Wassenaar Arrangement on Export Controls (dual-use goods)
- EU Dual-Use Regulation (EU 2021/821)
- Australia Group (chemical, biological controls)
- Missile Technology Control Regime (MTCR)
- Nuclear Suppliers Group (NSG)

**Country & Sanctions Controls**:
- Office of Foreign Assets Control (OFAC) Sanctions Programs
- Comprehensive Embargoes (Cuba, Iran, North Korea, Syria, Russia regions)
- Country Groups (E:1 terrorist supporting, E:2 regional stability)
- Sectoral sanctions (Russia, Venezuela)
- Entity-specific sanctions (Huawei, ZTE)

**Technology Transfer**:
- Deemed Export Rules (foreign person access to controlled technology)
- Fundamental Research Exclusion (university research exemption)
- Public Domain (publicly available information exemption)
- Educational Information exemption
- Know Your Customer (KYC) procedures for technology transfer

**Compliance Programs**:
- Export Management and Compliance Program (EMCP) Guidelines
- BIS Export Compliance Guidelines (Supplement No. 3 to Part 732)
- Voluntary Self-Disclosure (VSD) procedures for violations
- Recordkeeping requirements (5 years minimum)

**Automated Screening Tools**:
- Visual Compliance (OFAC/BIS screening)
- Descartes Denied Party Screening
- C4 (Customs4Trade) Compliance
- Oracle Global Trade Management
- SAP Global Trade Services
- Amber Road (now E2open)
- Integration with CRM/ERP for customer screening

**Cryptography Standards**:
- FIPS 140-2/140-3 (cryptographic modules)
- NIST SP 800-57 (key management recommendations)
- Suite B Cryptography (NSA cryptographic algorithms)
- Commercial National Security Algorithm Suite (CNSA)
- AES-256, RSA-2048/3072/4096, ECDSA P-256/384/521

**Open Source & Public Availability**:
- Publicly Available Encryption Software (PAES) exemption criteria
- Open-source license requirements (OSI-approved licenses)
- GitHub/GitLab public repository notifications to BIS
- Unrestricted publication and availability requirements

**Industry-Specific Controls**:
- Aerospace and Defense (ITAR controls, DDTC registration)
- Telecommunications (encryption, lawful intercept requirements)
- Financial Services (encryption for payments, trading systems)
- Healthcare (encryption for HIPAA, patient data)

**Compliance & Audit**:
- Voluntary Self-Disclosure (VSD) to BIS Office of Export Enforcement
- Administrative Enforcement Actions (warning letters, civil penalties)
- Criminal Enforcement (willful violations, jail time, corporate fines)
- Recordkeeping and audit trail requirements (5+ years)

**Reference**: Consult export compliance counsel, BIS classification specialists, and trade compliance team for ECCN determinations, screening procedures, and regulatory interpretation

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
