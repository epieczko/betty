# Name: eccn-classification

## Executive Summary

The Export Control Classification Number (ECCN) Classification artifact documents the export control classification of products, software, and technology under the U.S. Export Administration Regulations (EAR), determining licensing requirements for international sales, transfers, and shipments to 180+ countries and restricted end-users. ECCN classification is mandatory for U.S.-origin commercial products and technology, with classifications ranging from EAR99 (low-risk, generally no license required) to controlled categories (0-9) requiring export licenses for specific countries, end-users, or end-uses.

Software and technology classifications cover encryption products (ECCN 5A002, 5D002), telecommunications equipment (ECCN 5A001), cybersecurity tools (ECCN 5A004), artificial intelligence/machine learning systems (ECCN 3E001, 4E001), cloud computing services, and dual-use technologies with both commercial and military applications. Encryption classifications particularly impact SaaS providers, with most commercial encryption qualifying for License Exception ENC after one-time BIS classification review and self-classification reporting.

Organizations with rigorous ECCN classification processes reduce export violation risks (penalties $300K-$1M+ per violation, criminal liability), prevent shipment delays, enable faster international revenue recognition, and maintain compliance with BIS, OFAC sanctions, and denied party screening requirements. Accurate classification supports screening against Entity List, Denied Persons List, Specially Designated Nationals (SDN) List, and embargo countries preventing transactions with prohibited parties.

### Strategic Importance

- **Regulatory Compliance**: Ensures adherence to EAR 15 CFR Parts 730-774, ITAR 22 CFR Parts 120-130, and OFAC sanctions preventing $300K-$1M+ penalties and criminal liability
- **Revenue Enablement**: Enables international sales and SaaS expansion to 180+ countries by determining license requirements and authorized destinations
- **Risk Mitigation**: Prevents export violations, denied party transactions, and sanctions breaches through proper classification and screening
- **Competitive Advantage**: Accelerates international sales cycles by pre-classifying products and establishing License Exception eligibility (ENC, TSU, NLR)
- **M&A Due Diligence**: Provides classification documentation required for acquisition due diligence, CFIUS reviews, and foreign investment approvals
- **Customer Trust**: Demonstrates export compliance rigor to government customers, enterprise buyers, and international distributors requiring classification documentation
- **Operational Efficiency**: Streamlines export licensing workflows, reduces BIS submission delays, and enables automated denied party screening integration

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative export control classification record for products, software, and technology, determining applicable ECCN codes, export licensing requirements, and authorized destinations under U.S. Export Administration Regulations (EAR). It solves the compliance challenge of determining whether specific products require export licenses, which countries can receive them, and which end-users are prohibited, enabling international sales teams to confidently execute transactions while satisfying BIS and OFAC requirements. The classification supports decision-making around product development (avoiding controlled features), sales strategies (identifying no-license markets vs restricted destinations), and operational workflows (configuring automated denied party screening and license application processes).

### Scope

**In Scope**:
- ECCN classification determination for commercial software, technology, hardware, and services under EAR Categories 0-9
- Encryption classification under ECCN 5A002 (encryption items), 5D002 (encryption software), and 5E002 (encryption technology)
- License Exception eligibility assessment including ENC (encryption), TSU (technology and software unrestricted), NLR (no license required)
- Commerce Control List (CCL) review and classification methodology using EAR Part 774 Supplement 1
- Country group classification under EAR Part 740 Supplement 1 (Country Groups A-E, D:1-5, E:1-2)
- Denied party screening requirements against Entity List, Denied Persons List, Unverified List, SDN List
- License application requirements for controlled ECCNs to restricted destinations or end-users
- Self-classification reporting requirements for encryption products under License Exception ENC
- Deemed export analysis for foreign national access to controlled technology in the U.S.
- Product feature analysis determining if encryption strength, parameters, or capabilities trigger classification
- Cloud services classification including SaaS, PaaS, IaaS offerings with encryption or data processing capabilities
- Technical specifications documentation supporting ECCN classification including encryption algorithms, key lengths, authentication methods
- Annual classification review and update requirements when products, features, or regulations change
- ITAR vs EAR jurisdiction determination for dual-use technologies

**Out of Scope**:
- Customs and import regulations, HS tariff codes, and duty calculation (covered by Customs Compliance)
- ITAR (International Traffic in Arms Regulations) defense article classification (covered by ITAR Compliance Program)
- Sanctions compliance beyond export control context (broader OFAC compliance covered in Sanctions Compliance Policy)
- Specific export license applications and BIS correspondence (operational records, not classification documentation)
- Individual transaction screening logs and denied party check results (operational logs, not classification)
- Foreign investment reviews and CFIUS determinations (covered in M&A Due Diligence)
- Product development roadmaps and feature planning (covered in Product Management)

### Target Audience

**Primary Audience**:
- Export Compliance Officers and Trade Compliance teams responsible for ECCN classification, license applications, and BIS reporting
- Legal and Regulatory Affairs teams ensuring compliance with EAR, ITAR, and OFAC sanctions regulations
- International Sales teams requiring classification documentation to determine license requirements for customer transactions
- Product Management and Engineering teams understanding how product features affect export classification and restrictions

**Secondary Audience**:
- Executive Leadership evaluating international expansion strategies, geopolitical risks, and export compliance program maturity
- Finance and Revenue Recognition teams requiring export classification for international revenue recognition and audit support
- M&A and Corporate Development teams providing export compliance documentation for due diligence and CFIUS reviews
- Government Affairs teams engaging with BIS, DDTC, and OFAC on export control policy and classification guidance

## Document Information

**Format**: Markdown

**File Pattern**: `*.eccn-classification.md`

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

**Technical Specification Documentation**: Document detailed technical specifications including encryption algorithms (AES, RSA, ECC), key lengths (128-bit, 256-bit), authentication methods, and cryptographic parameters supporting classification rationale
**Commerce Control List Review**: Systematically review all CCL categories (0-9) using elimination methodology ensuring no applicable ECCNs are overlooked during classification
**Encryption Classification Rigor**: For encryption products, determine classification under ECCN 5A002/5D002/5E002 and License Exception ENC eligibility through BIS self-classification or classification request
**Legal Counsel Review**: Engage export control attorneys or outside counsel for complex classifications, novel technologies, or products with potential dual-use concerns
**BIS Classification Requests**: Submit formal classification requests (Commodity Classification Requests) to BIS for ambiguous or high-risk products obtaining official determination
**Annual Classification Review**: Review and update classifications annually or when products, features, regulations, or geopolitical landscape changes (new sanctions, Entity List additions)
**Documentation Retention**: Maintain classification rationale, technical specifications, BIS correspondence, and self-classification reports for 5+ years satisfying audit requirements
**Cross-Functional Review**: Include Product Engineering, Legal, Compliance, and Sales teams in classification review ensuring comprehensive technical and commercial perspective
**Country Group Analysis**: Map product restrictions to EAR Country Groups (A-E, D:1-5, E:1-2) and embargo destinations identifying no-license vs restricted markets
**License Exception Assessment**: Determine eligibility for License Exceptions (ENC, TSU, NLR, GOV, GBS) before defaulting to license requirement reducing unnecessary BIS applications
**Denied Party Integration**: Integrate denied party screening (Entity List, DPL, SDN) into CRM, order management, and sales workflows preventing prohibited transactions
**Deemed Export Controls**: Implement access controls and technology release procedures for foreign nationals in U.S. facilities preventing unauthorized deemed exports
**ITAR Jurisdiction Review**: Evaluate ITAR vs EAR jurisdiction for dual-use technologies consulting with DDTC and BIS for jurisdictional determination requests
**Self-Classification Reporting**: Submit required self-classification reports for encryption products under License Exception ENC including product details and technical parameters
**Product Feature Controls**: Design products with export compliance in mind, avoiding controlled features or implementing feature-gating for restricted destinations
**Customer Communication**: Develop customer-facing export classification documentation, declarations, and license exception claims enabling customer import processes
**Training Programs**: Train Sales, Product, Engineering, and Compliance teams on export classification, license requirements, and denied party screening obligations
**Audit Readiness**: Maintain audit-ready classification files with supporting documentation, decision rationale, and regulatory references for BIS inspections and third-party audits
**Geopolitical Monitoring**: Monitor BIS rule changes, Entity List additions, sanctions developments, and geopolitical events requiring classification or policy updates
**Version Control**: Maintain version history of classification decisions tracking changes in product features, regulations, or BIS guidance affecting classification
**License Application Procedures**: Document license application procedures for controlled ECCNs including BIS SNAP-R system usage, application timelines (60-90 days), and approval tracking
**Expert Consultation**: Engage export control consultants or firms (Sandler Travis, Steptoe, Akin Gump) for complex classifications or compliance program assessments
**Technology Control Plans (TCP)**: Implement TCPs for controlled technology defining access controls, foreign national screening, and technology release procedures
**Compliance Management Systems**: Leverage export compliance platforms (Amber Road, Descartes, OCR Services) automating screening, license management, and classification workflows
**Restricted Party Due Diligence**: Conduct enhanced due diligence on customers in sensitive industries (aerospace, defense, technology) or jurisdictions (China, Russia, Iran)

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

**Export Administration Regulations (EAR)**: 15 CFR Parts 730-774 (Commerce Control List, License Exceptions, Country Groups, General Prohibitions, Deemed Exports)

**ITAR Regulations**: 22 CFR Parts 120-130 (U.S. Munitions List, Defense Articles, Technical Data, Defense Services, DDTC Registration)

**OFAC Sanctions**: 31 CFR Chapter V (Sanctions Programs, SDN List, Embargo Countries, Blocked Persons, General Licenses)

**Commerce Control List (CCL)**: EAR Part 774 Supplement 1 Categories 0-9 (Nuclear, Materials, Electronics, Computers, Telecom, Information Security, Sensors, Navigation, Marine, Aerospace, Propulsion)

**ECCN Categories**: Category 5 Part 2 Information Security (5A002 Encryption Items, 5D002 Encryption Software, 5E002 Encryption Technology, 5A004 Network Penetration Tools)

**License Exceptions**: ENC (Encryption), TSU (Technology and Software Unrestricted), NLR (No License Required), GOV (Government End Users), GBS (Group B Shipments), TMP (Temporary Imports/Exports)

**Country Groups**: EAR Part 740 Supplement 1 (Country Group A:1-6, B, D:1-5, E:1-2), Embargo Destinations (Cuba, Iran, North Korea, Syria, Russia, Belarus)

**Denied Party Lists**: BIS Entity List, Denied Persons List (DPL), Unverified List (UVL), OFAC SDN List, Sectoral Sanctions Identifications List, Foreign Sanctions Evaders List

**BIS Systems**: SNAP-R (Simplified Network Application Process Redesign), ECASS (Export Control Classification Automated Support System), ECCNs Knowledge Base

**Encryption Classification**: CCATS (Commodity Classification Automated Tracking System) Encryption Registration, Annual Self-Classification Reports, Technical Review Board Submissions

**Cryptography Standards**: FIPS 140-2/140-3 (Cryptographic Module Validation), AES (Advanced Encryption Standard), RSA Public Key Cryptography, ECC (Elliptic Curve Cryptography), Suite B Algorithms

**Technical Parameters**: Encryption Key Management, Symmetric Key Length (56-bit, 128-bit, 256-bit), Asymmetric Key Length (1024-bit, 2048-bit, 4096-bit), Hash Functions (SHA-256, SHA-384, SHA-512)

**Deemed Export Regulations**: EAR Part 734.13-734.20 (Foreign National Access, Technology Release, Visual Inspection, Know-How Transfer)

**Wassenaar Arrangement**: Multilateral Export Control Regime covering Dual-Use Goods and Technologies, Munitions List coordination with 42 participating states

**Export Compliance Programs**: BIS Compliance Guidelines, OFAC Framework for Compliance Commitments, ISO 37301 Compliance Management Systems

**Trade Compliance Software**: Amber Road (Descartes), Livingston Trade Compliance, Expeditors Trade Compliance, OCR Services Export Compliance, SAP GTS (Global Trade Services)

**Denied Party Screening**: Visual Compliance (Descartes), Dow Jones Compliance Catalyst, LexisNexis Bridger Insight XG, Accuity Firco Global Watchlist Screening

**Professional Certifications**: Certified Export Compliance Professional (CECP), Certified U.S. Export Compliance Officer (CUSECO), Certified Trade Compliance Professional (CTCP)

**Industry Associations**: Bureau of Industry and Security (BIS), Aerospace Industries Association (AIA), National Defense Industrial Association (NDIA), TechAmerica, U.S. Council for International Business

**Legal Resources**: Export Control and Sanctions Lawyers (Steptoe & Johnson, Akin Gump, Miller & Chevalier, Berliner Corcoran & Rowe)

**Compliance Consultants**: Sandler, Travis & Rosenberg (ST&R), Export Compliance Training Institute (ECTI), Amber Road Consulting, Husch Blackwell Trade & Supply Chain

**CFIUS Regulations**: 31 CFR Part 800 (Foreign Investment Risk Review, Critical Technology Exports, National Security Reviews)

**Anti-Boycott Regulations**: EAR Part 760 (Prohibited Boycott Activities, Reporting Requirements, Commerce Anti-Boycott Compliance)

**CMMC Compliance**: Cybersecurity Maturity Model Certification for defense contractors requiring export control (DFARS 252.204-7012)

**Audit Standards**: Export Management and Compliance Program (EMCP) Best Practices, BIS Export Enforcement Penalty Guidelines, Voluntary Self-Disclosure Procedures

**International Frameworks**: EU Dual-Use Regulation (EU 2021/821), UK Export Control Order 2008, Australia Defense Trade Controls Act, Canada Export and Import Permits Act

**Reference**: Consult Export Compliance Officers, BIS Industry and Analysis staff, trade compliance attorneys, and export control consultants for detailed classification guidance, license applications, and compliance program development

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
