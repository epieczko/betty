# Name: data-retention-plan

## Executive Summary

The Data Retention Plan is a comprehensive governance framework that defines retention periods, deletion schedules, archival procedures, and legal hold processes for personal data and regulated information to satisfy GDPR Article 5(1)(e) storage limitation principle, CCPA/CPRA deletion requirements, and industry-specific retention mandates. This critical privacy artifact establishes data lifecycle management policies from collection through secure deletion, ensuring compliance with "right to erasure" obligations under GDPR Article 17 while preserving data for legitimate business and legal requirements.

Modern data retention strategies leverage privacy automation platforms like OneTrust Data Retention, BigID Retention Automation, and Collibra Data Retention to implement policy-driven deletion workflows, automate GDPR Article 17 erasure requests, and maintain audit trails for regulatory compliance. Organizations deploy data lifecycle management across databases (automated TTL policies), cloud storage (S3 Lifecycle, Azure Blob Storage lifecycle), backup systems (Veeam, Commvault retention policies), and enterprise applications (Salesforce, Workday data archival) to operationalize retention schedules while supporting legal discovery and regulatory examination requirements.

### Strategic Importance

- **GDPR Storage Limitation**: Satisfies Article 5(1)(e) requirement to retain personal data no longer than necessary for processing purposes with documented retention justification
- **Right to Erasure Compliance**: Implements GDPR Article 17 "right to be forgotten" deletion obligations within required timelines (typically 30 days of verified request)
- **CCPA/CPRA Deletion Rights**: Addresses California Consumer Privacy Act requirements for consumer deletion requests and 12-month business purpose retention disclosures
- **Legal Discovery Readiness**: Balances deletion obligations with litigation hold requirements, e-discovery preservation duties, and regulatory examination data availability
- **Regulatory Penalties Avoidance**: Mitigates GDPR fines for excessive retention (up to 4% global revenue), CCPA violations ($2,500-$7,500 per violation), and sector-specific sanctions
- **Data Minimization**: Reduces security breach exposure, storage costs, and privacy risks by systematically deleting unnecessary personal information
- **Operational Efficiency**: Automates retention workflows using policy engines in OneTrust, BigID, or Collibra reducing manual deletion effort and ensuring consistent application

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative policy defining data retention periods by category, automated deletion triggers, legal hold procedures, archival workflows, and secure disposal methods to ensure GDPR Article 5(1)(e) storage limitation compliance, support GDPR Article 17 erasure rights, satisfy industry-specific retention mandates, and balance privacy obligations with legitimate business and legal preservation requirements.

### Scope

**In Scope**:
- Retention schedules by data category (customer data, employee records, financial data, marketing data, system logs, metadata)
- GDPR Article 5(1)(e) storage limitation principle implementation with documented retention justification
- GDPR Article 17 right to erasure deletion workflows and 30-day response timeline procedures
- CCPA/CPRA consumer deletion request processes and verification methods
- Legal hold procedures for litigation, regulatory examinations, and investigation preservation requirements
- Backup retention policies for disaster recovery systems (Veeam, Commvault, AWS Backup, Azure Backup)
- Archival workflows for long-term storage using compliant formats (WORM storage, AWS Glacier, Azure Archive)
- Secure deletion methods aligned with NIST 800-88 Guidelines for Media Sanitization
- Automated deletion triggers using database TTL (Time-to-Live), S3 Lifecycle policies, and retention automation tools
- Industry-specific retention requirements (HIPAA 6 years, SOX 7 years, FINRA 6 years, GDPR varies by purpose)
- Records management for GDPR Article 30 ROPA, audit logs, and privacy assessment documentation
- Data subject request tracking with retention of request evidence per GDPR accountability principle

**Out of Scope**:
- Data classification and sensitivity labeling (covered by Data Classification Policy)
- Privacy policy public disclosures of retention periods (addressed in Privacy Policy artifact)
- Data Processing Agreement vendor retention obligations (managed through DPA artifact)
- Specific backup and disaster recovery technology implementation (handled by BCP/DR documentation)
- Information security controls for data protection (documented in Security Architecture)
- E-discovery and litigation support procedures (separate Legal Hold and E-Discovery playbooks)

### Target Audience

**Primary Audience**:
- Data Protection Officers (DPOs) establishing retention schedules compliant with GDPR Article 5(1)(e) and Article 17
- Privacy and Compliance Teams operationalizing retention policies and managing deletion request workflows
- Records Management Officers maintaining retention schedules and coordinating legal hold procedures
- Legal Counsel defining litigation hold requirements and balancing privacy with preservation duties

**Secondary Audience**:
- Engineering Teams implementing automated retention in databases (TTL), cloud storage (lifecycle), and applications
- Information Security Teams configuring secure deletion methods and data sanitization procedures
- IT Operations managing backup retention policies in Veeam, Commvault, AWS Backup, Azure Site Recovery
- Business Unit Leaders understanding retention constraints for customer data, marketing databases, and analytics

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-retention-plan.md`

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

**Purpose-Based Retention**: Define retention periods based on documented processing purpose per GDPR Article 5(1)(e) with clear business or legal justification for each data category
**Retention Schedule Matrix**: Create comprehensive retention matrix specifying data categories, retention periods, deletion triggers, legal basis, and responsible owners
**Automated Deletion Workflows**: Implement automated retention using database TTL (Time-to-Live), S3 Lifecycle policies, Azure Blob lifecycle, and privacy platform automation (OneTrust, BigID, Collibra)
**GDPR Article 17 Compliance**: Establish 30-day deletion timeline for verified erasure requests with audit trail of deletion confirmation and exception justification
**Legal Hold Integration**: Implement legal hold flag mechanisms preventing automated deletion when litigation, regulatory examination, or investigation preservation duties exist
**Backup Retention Alignment**: Ensure backup systems (Veeam, Commvault, AWS Backup) honor retention policies with automated backup expiration aligned to retention schedules
**Secure Deletion Methods**: Apply NIST SP 800-88 sanitization standards with cryptographic erasure (key destruction), overwriting (multiple passes), or physical destruction for media
**Archival for Long-Term Retention**: Use compliant archival storage (AWS Glacier, Azure Archive, WORM storage) for records requiring extended retention (SOX 7 years, HIPAA 6 years)
**Differential Retention by Jurisdiction**: Implement geography-specific retention to accommodate varying requirements (EU GDPR vs. California CCPA vs. Brazil LGPD retention obligations)
**Active vs. Inactive Data Policies**: Define different retention for active customer relationships vs. inactive/churned customers balancing business needs with minimization principle
**Metadata Retention**: Retain minimal metadata for accountability even after deletion (e.g., "deletion performed on [date]" without retaining actual personal data)
**Cross-System Deletion Coordination**: Ensure deletion propagates across all systems including primary databases, data warehouses, analytics platforms, CRM, marketing automation, and backups
**Regular Retention Audits**: Conduct quarterly reviews of data stores validating deletion execution, identifying retention policy violations, and remediating over-retained data
**ROPA Documentation**: Document retention periods in GDPR Article 30 Records of Processing Activities for transparency and supervisory authority examination
**Privacy Policy Disclosure**: Disclose retention periods (or criteria for determination) in privacy notices per GDPR Articles 13-14 transparency requirements
**Vendor Retention Requirements**: Include retention and deletion obligations in Data Processing Agreements (DPAs) with processors ensuring downstream compliance
**Anonymization Alternative**: For analytics and research, consider anonymization as alternative to deletion when data no longer reasonably identifies individuals
**Employee Training**: Train data stewards, engineers, and business users on retention policies, legal hold procedures, and deletion request handling
**Exception Management**: Establish formal exception process for retention extensions with DPO approval, documented justification, and periodic review
**Deletion Verification**: Implement confirmation mechanisms (deletion certificates, audit logs, checksums) proving data removal per controller accountability obligations
**Cloud Storage Lifecycle**: Configure AWS S3 Lifecycle, Azure Blob lifecycle, GCP Object lifecycle for automated tiering to archival storage and eventual expiration
**Immutable Storage for Compliance**: Use S3 Object Lock compliance mode, Azure immutable storage, or WORM storage preventing premature deletion during mandatory retention
**Regular Policy Updates**: Review retention schedules annually or when regulations change (e.g., new CCPA amendments, GDPR guidance, industry standards updates)

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

**Privacy Regulations - Retention and Deletion**:
- GDPR Article 5(1)(e) - Storage limitation principle requiring data retention only as long as necessary
- GDPR Article 17 - Right to erasure ("right to be forgotten") with deletion within one month of verified request
- GDPR Article 30 - Records of Processing Activities (ROPA) including retention period documentation
- CCPA/CPRA - Consumer deletion rights and business purpose retention disclosures (12-month periods)
- LGPD Article 16 - Brazilian data retention and deletion requirements
- PIPEDA - Canadian reasonable retention periods and disposal requirements
- APPI (Japan) - Retention period specifications and secure disposal obligations
- POPIA (South Africa) - Retention limitation and destruction requirements
- UK GDPR and Data Protection Act 2018 - Post-Brexit UK retention and erasure requirements
- China PIPL - Personal information retention minimization and deletion procedures

**Industry-Specific Retention Requirements**:
- HIPAA - Protected Health Information (PHI) 6-year retention minimum under 45 CFR 164.530
- SOX (Sarbanes-Oxley) - Financial records 7-year retention requirement
- FINRA Rule 4511 - Securities broker-dealer 6-year record retention
- SEC Rule 17a-4 - Investment adviser records retention (5 years minimum)
- DOL (Department of Labor) - Employment records 3-7 years depending on record type
- IRS - Tax records 7-year retention for audit purposes
- FDA 21 CFR Part 11 - Electronic records in clinical trials and pharmaceutical manufacturing
- PCI DSS Requirement 10.7 - Payment card audit log retention minimum one year, three months online
- FERPA - Student education records retention varies by institution policy
- GLBA - Financial institution customer records retention requirements

**Data Retention Frameworks and Standards**:
- ISO 15489:2016 - Records management standard for retention and disposition
- NIST SP 1800-11 - Data integrity and lifecycle management
- ARMA International GARP - Generally Accepted Recordkeeping Principles
- ISO 27001:2022 Annex A.5.33 - Records retention and disposal controls
- ISO 27701:2019 - PIMS extension covering retention period specification
- NIST Privacy Framework PR.DM-P3 - Data disposal practices aligned with retention policies
- MoReq (Model Requirements for Electronic Records Management) - EU retention framework
- DoD 5015.2 - US Department of Defense records management standard

**Retention Automation and Privacy Platforms**:
- OneTrust Data Retention - Policy-driven retention schedules, automated deletion workflows
- BigID Retention Automation - Data lifecycle management and erasure automation across data stores
- Collibra Data Retention - Retention policy enforcement and compliance tracking
- Securiti.ai Sentra - Data retention and automated deletion for cloud and SaaS
- DataGrail Retention Management - Consumer deletion requests and retention automation
- WireWheel Retention Policies - Automated data aging and disposal workflows
- Transcend Data Lifecycle - Engineering-first retention and deletion automation
- TrustArc Data Retention Manager - Retention schedule management and policy enforcement
- Osano Data Lifecycle - Website and SaaS data retention automation
- Privacy Dynamics Retention Controls - Synthetic data generation for aged data replacement

**Backup and Archival Solutions**:
- Veeam Backup & Replication - Retention policies and automated backup deletion
- Commvault - Information lifecycle governance and retention enforcement
- AWS Backup - Backup retention policies and S3 Lifecycle management
- Azure Backup - Azure Site Recovery retention and archive tier policies
- Google Cloud Backup and DR - Retention policy configuration and lifecycle management
- Veritas NetBackup - Enterprise backup retention and archival management
- Rubrik - Cloud data management with retention policy automation
- Cohesity - Data lifecycle management and retention enforcement
- IBM Spectrum Protect - Backup retention and archival tier management
- Dell EMC Data Domain - Deduplication storage with retention policies

**Secure Deletion and Data Sanitization**:
- NIST SP 800-88 Rev. 1 - Guidelines for Media Sanitization (clear, purge, destroy methods)
- DoD 5220.22-M - Department of Defense disk sanitization standard (superseded by NIST 800-88)
- ISO/IEC 27040:2015 - Storage security including secure deletion guidance
- BSI IT-Grundschutz - German Federal Office for Information Security deletion standards
- CSEC ITSG-06 - Canadian secure deletion guidance for protected information
- HMG Infosec Standard 5 - UK government secure sanitization standard
- Blancco - Certified data erasure software compliant with international standards
- DBAN (Darik's Boot and Nuke) - Free open-source data deletion tool
- AWS S3 Object Lock - WORM (Write Once Read Many) immutable storage for compliance
- Azure Immutable Blob Storage - Legal hold and time-based retention policies

**Legal Hold and E-Discovery**:
- Federal Rules of Civil Procedure (FRCP) - US litigation hold and preservation duties
- eDiscovery Reference Model (EDRM) - Framework for e-discovery lifecycle
- ISO 27050 - Electronic discovery standard series (parts 1-4)
- Relativity - E-discovery platform for legal hold management
- Exterro - Legal GRC platform for legal hold and retention
- Onna - Unified legal hold across cloud applications (Slack, Teams, Google Workspace)
- Zapproved - Legal hold automation and data preservation tracking

**Cloud Storage Lifecycle Management**:
- AWS S3 Lifecycle Policies - Automated transition to Glacier and expiration deletion
- Azure Blob Storage Lifecycle Management - Automated tiering and deletion policies
- Google Cloud Storage Lifecycle - Object lifecycle actions and automatic deletion
- AWS S3 Object Lock - Compliance mode preventing deletion during retention period
- Azure Blob Immutable Storage - Time-based retention and legal hold policies
- GCP Bucket Lock - Retention policy enforcement preventing premature deletion

**Reference**: Consult Data Protection Officer (DPO), Records Management, Legal Counsel, and Privacy Teams for detailed guidance on retention framework application and regulatory compliance validation

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
