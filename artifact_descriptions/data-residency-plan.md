# Name: data-residency-plan

## Executive Summary

The Data Residency Plan is a strategic compliance framework that defines where personal data and regulated information must be physically stored and processed to satisfy data localization laws, cross-border transfer restrictions, and data sovereignty requirements under GDPR, China PIPL, Russia Federal Law 242-FZ, and other territorial privacy regulations. This critical planning artifact maps organizational data flows to compliant geographic infrastructure using cloud provider regions (AWS, Azure, GCP), content delivery networks, and data center locations.

Modern data residency planning leverages cloud infrastructure across AWS Regions (33+ worldwide), Azure Geographies (60+ regions), and Google Cloud locations to architect compliant data architectures. Organizations deploy privacy engineering tools like OneTrust Data Discovery, BigID Data Inventory, and Collibra Data Intelligence to map data locations, implement geo-fencing controls, and maintain GDPR Article 30 Records of Processing Activities (ROPA) documenting cross-border data transfers. Data residency strategies incorporate Transfer Impact Assessments (TIAs) for Schrems II compliance, Standard Contractual Clauses (SCCs) implementation, and technical measures including encryption, access controls, and data minimization.

### Strategic Importance

- **Regulatory Compliance**: Satisfies data localization requirements under China PIPL, Russia Data Localization Law, Indonesia PP 71/2019, Vietnam Cybersecurity Law, and Saudi Arabia Cloud Computing Framework
- **GDPR Transfer Mechanisms**: Implements lawful international transfer safeguards through EU adequacy decisions, Standard Contractual Clauses, Binding Corporate Rules, and derogations per GDPR Article 49
- **Data Sovereignty**: Addresses government access concerns, national security laws (US CLOUD Act, China National Intelligence Law), and territorial jurisdiction over data
- **Infrastructure Architecture**: Defines cloud region selection (AWS eu-central-1, Azure Germany, GCP europe-west3), database replication strategies, and CDN content restrictions
- **Risk Mitigation**: Reduces exposure to cross-border data transfer violations with GDPR fines up to 4% of global revenue or €20 million, and PIPL penalties up to ¥50 million
- **Operational Efficiency**: Optimizes data latency, disaster recovery planning, and business continuity through strategic geographic data placement
- **Vendor Management**: Establishes subprocessor location requirements, cloud service provider compliance validation, and third-party data storage restrictions

## Purpose & Scope

### Primary Purpose

This artifact serves as a strategic roadmap defining data storage locations, cross-border transfer mechanisms, cloud infrastructure regions, and technical controls necessary to comply with data localization laws, GDPR Chapter V transfer requirements, and data sovereignty mandates while optimizing system performance and disaster recovery capabilities.

### Scope

**In Scope**:
- Data localization law requirements (China PIPL, Russia Federal Law 242-FZ, Indonesia PP 71/2019, Vietnam Decree 13/2023, India Draft Data Protection Bill)
- GDPR Chapter V international transfer mechanisms (Articles 44-50) including adequacy decisions, SCCs, BCRs, and derogations
- Cloud provider region selection and configuration (AWS Regions, Azure Geographies, Google Cloud locations, Oracle Cloud regions)
- Database residency controls (primary database location, read replicas, backup storage, archival data, disaster recovery sites)
- Application data flow mapping (user data collection points, processing locations, third-party integrations, CDN content delivery)
- Cross-border data transfer inventory documenting sender/receiver countries, data categories, volumes, and legal basis
- Transfer Impact Assessments (TIAs) evaluating destination country laws per Schrems II CJEU C-311/18 requirements
- Technical safeguards including geo-fencing, encryption in transit/at rest, access controls, data minimization, and pseudonymization
- Vendor and subprocessor location tracking for third-party data storage and processing services
- Data center certifications (ISO 27001, SOC 2, TISAX for automotive, CSA STAR for cloud)

**Out of Scope**:
- Detailed network architecture and infrastructure design (handled by Infrastructure Architecture artifact)
- Specific security control implementation details (documented in Security Architecture and SOC 2 reports)
- Data retention schedules and deletion timelines (covered by Data Retention Plan artifact)
- Privacy policy consumer disclosures (addressed in Privacy Policy artifact)
- Data Processing Agreements with specific vendors (managed through DPA artifact)
- Business continuity and disaster recovery procedures (separate BCP/DR plan)

### Target Audience

**Primary Audience**:
- Data Protection Officers (DPOs) ensuring GDPR Chapter V transfer compliance and data localization adherence
- Privacy Counsel evaluating cross-border transfer legal basis and Transfer Impact Assessment requirements
- Cloud Architecture Teams designing multi-region infrastructure with data residency controls
- Infrastructure and Platform Engineering Teams configuring AWS regions, Azure geographies, and database replication

**Secondary Audience**:
- Compliance Teams maintaining regulatory mapping for data localization laws across jurisdictions
- Information Security Teams implementing geo-fencing, encryption, and access controls
- Product and Engineering Leaders understanding data residency constraints for feature development
- Vendor Management Teams validating subprocessor data storage locations and compliance certifications

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-residency-plan.md`

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

**Data Flow Mapping**: Document complete data flows from collection through storage, processing, transfer, and deletion using tools like OneTrust Data Discovery, BigID, or Collibra to identify all cross-border transfers
**Transfer Impact Assessments (TIAs)**: Conduct Schrems II-compliant TIAs for transfers to countries without adequacy decisions, evaluating destination laws, government access risks, and supplementary measures per EDPB Recommendations 01/2020
**Cloud Region Strategy**: Select cloud provider regions based on regulatory requirements (e.g., AWS eu-central-1 for GDPR, Alibaba Cloud China regions for PIPL) and configure region constraints in infrastructure-as-code
**Geo-Fencing Controls**: Implement technical geo-blocking using AWS Organizations SCPs, Azure Policy, GCP Organization Policies to prevent data from leaving authorized regions
**Encryption Everywhere**: Deploy encryption in transit (TLS 1.3) and at rest (AES-256) with customer-managed keys (AWS KMS, Azure Key Vault, GCP Cloud KMS) to maintain control over encryption keys
**Data Minimization**: Limit cross-border transfers to minimum necessary data categories and implement pseudonymization or anonymization for non-essential transfers
**Adequacy Decision Mapping**: Leverage EU adequacy decisions for transfers to approved countries (UK, Switzerland, Japan, Canada under PIPEDA, Israel, Andorra, Argentina, Faroe Islands, Guernsey, Isle of Man, Jersey, New Zealand, Uruguay, South Korea)
**Standard Contractual Clauses**: Implement 2021 EU SCCs for controller-to-processor (Module 2) and processor-to-processor (Module 3) transfers to non-adequate countries
**Binding Corporate Rules**: For multinational organizations, establish BCRs approved by lead supervisory authority for intra-group transfers across multiple entities
**Data Localization Compliance**: For China PIPL, Russia 242-FZ, and Indonesia PP 71/2019, deploy in-country infrastructure or local data centers with certified local hosting providers
**Vendor Location Verification**: Maintain subprocessor registry documenting data storage locations, processing countries, and data center certifications (ISO 27001, SOC 2) using OneTrust Vendorpedia or TrustArc
**Database Replication Strategy**: Configure primary databases in compliant regions with read replicas restricted to authorized geographies; avoid automatic failover to non-compliant regions
**Backup and DR Planning**: Ensure backups and disaster recovery sites comply with residency requirements; document backup storage regions in AWS S3, Azure Blob Storage, or GCP Cloud Storage
**CDN Content Restrictions**: Configure content delivery networks (CloudFront, Azure CDN, Cloudflare) to restrict caching of personal data or implement edge encryption for sensitive content
**Access Control Geography**: Restrict administrative access to production data based on employee location using conditional access policies (Azure AD, Okta) and IP geolocation
**Monitoring and Alerting**: Deploy cloud monitoring (AWS CloudTrail, Azure Monitor, GCP Cloud Logging) with alerts for unauthorized region access or data transfer anomalies
**Documentation in ROPA**: Maintain GDPR Article 30 Records of Processing Activities documenting processing locations, transfer mechanisms, and recipient countries
**Privacy by Design**: Integrate data residency requirements into system design reviews, architecture decision records (ADRs), and infrastructure change management processes
**Regular Compliance Audits**: Conduct quarterly reviews of cloud resource locations, subprocessor changes, and regulatory updates affecting data localization requirements
**Legal Review Requirements**: Obtain Privacy Counsel and DPO approval for new cross-border transfers, particularly to countries requiring TIAs or without adequate protection
**Version Control**: Store data residency architecture diagrams and configuration in Git with infrastructure-as-code (Terraform, CloudFormation, ARM templates) for audit trail
**Regulatory Monitoring**: Subscribe to privacy law updates (IAPP, OneTrust Regulatory Tracker, TrustArc) to identify new data localization requirements and adjust infrastructure accordingly

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

**Data Localization and Sovereignty Laws**:
- China PIPL (Personal Information Protection Law) - Article 40 data localization and Article 38 cross-border transfer security assessment
- Russia Federal Law No. 242-FZ - Personal data localization requirement for Russian citizens
- Indonesia Government Regulation No. 71/2019 - Electronic systems and transaction data localization
- Vietnam Decree No. 13/2023 - Personal data protection and local storage requirements
- India Digital Personal Data Protection Act 2023 - Cross-border transfer restrictions and localization provisions
- Saudi Arabia Cloud Computing Regulatory Framework - Cloud data residency requirements
- Nigeria Data Protection Act 2023 - Cross-border transfer restrictions
- Turkey Personal Data Protection Law - Data localization and transfer authorization requirements
- South Korea Personal Information Protection Act (PIPA) - Cross-border transfer restrictions
- Brazil LGPD Article 33 - International data transfer requirements

**GDPR International Transfer Requirements**:
- GDPR Chapter V (Articles 44-50) - Transfers of personal data to third countries or international organizations
- GDPR Article 45 - Adequacy decisions (EU Commission determinations of adequate protection)
- GDPR Article 46 - Appropriate safeguards (SCCs, BCRs, codes of conduct, certifications)
- GDPR Article 49 - Derogations for specific situations (explicit consent, contract necessity, public interest)
- Schrems II (CJEU C-311/18) - Invalidation of Privacy Shield and Transfer Impact Assessment requirements
- EDPB Recommendations 01/2020 - Measures supplementing transfer tools to ensure GDPR compliance
- EDPB Recommendations 02/2020 - European Essential Guarantees for surveillance measures
- EU Standard Contractual Clauses (2021) - Commission Implementing Decision (EU) 2021/914
- UK International Data Transfer Addendum (IDTA) - Post-Brexit UK transfer mechanism
- Swiss Federal Data Protection Act (FADP) - Swiss-specific cross-border transfer requirements

**Cloud Provider Infrastructure**:
- AWS Global Infrastructure - 33 geographic regions with 105 availability zones
- Microsoft Azure Geographies - 60+ regions worldwide with data residency guarantees
- Google Cloud Platform Locations - 40+ regions with regional data residency
- Oracle Cloud Infrastructure - OCI regions with data sovereignty controls
- IBM Cloud Regions - Multi-zone regions with local data processing
- Alibaba Cloud - China-specific regions compliant with PIPL requirements
- Tencent Cloud - China localization and regulatory compliance infrastructure

**Data Residency and Privacy Frameworks**:
- ISO 27001:2022 - Information security controls for data center operations and cloud infrastructure
- ISO 27017:2015 - Cloud-specific information security controls
- ISO 27018:2019 - Protection of personally identifiable information (PII) in public clouds
- ISO 27701:2019 - Privacy Information Management System extension with transfer controls
- NIST Privacy Framework - Core Function PR.PO-P2 addressing data processing location
- CSA (Cloud Security Alliance) STAR Certification - Cloud provider security assessment
- MTCS (Multi-Tier Cloud Security) Singapore Standard - SS 584 cloud data residency tiers
- SOC 2 Type II - Data center controls including location, physical security, and access management

**Privacy and Data Discovery Tools**:
- OneTrust Data Discovery - Automated data mapping, data flow visualization, transfer documentation
- BigID Data Inventory - Cloud data discovery across AWS, Azure, GCP with residency tagging
- Collibra Data Intelligence - Data catalog with geographic location metadata and lineage
- Securiti.ai Data Command Center - Multi-cloud data discovery and residency compliance automation
- WireWheel Data Inventory - Privacy-centric data mapping and transfer impact assessment
- DataGrail Privacy Platform - Data discovery with subprocessor location tracking
- Transcend Data Mapping - Engineering-first data inventory with regional classification
- Osano Data Discovery - Website data flow mapping and third-party transfer identification
- TrustArc Data Flow Manager - Visual data mapping and cross-border transfer documentation
- Privacy Dynamics - Data residency controls and synthetic data generation for non-production environments

**Cloud Data Residency Controls**:
- AWS Data Residency Features - Region selection, S3 bucket location constraints, RDS instance regions
- Azure Data Residency - Geography-based data residency commitments and customer-managed keys
- GCP Data Residency - Regional resource location, organization policy constraints
- AWS Nitro Enclaves - Isolated compute environments for sensitive data processing
- Azure Confidential Computing - Hardware-based trusted execution environments
- Google Confidential VMs - Encrypted in-use memory for sensitive workloads
- Oracle Cloud Guard - Automated security and residency compliance monitoring
- HashiCorp Sentinel - Policy-as-code for infrastructure residency controls
- Terraform Cloud Governance - Multi-cloud infrastructure compliance and region constraints

**Industry Standards and Certifications**:
- PCI DSS v4.0 - Payment card data geographic processing restrictions
- HIPAA - Protected Health Information (PHI) cross-border transfer limitations
- FedRAMP - US federal data residency requirements for cloud service providers
- TISAX (Trusted Information Security Assessment Exchange) - Automotive industry data residency
- SWIFT Customer Security Programme - Financial messaging data localization
- FINMA (Swiss Financial Market Supervisory Authority) - Financial data residency requirements
- MAS (Monetary Authority of Singapore) Technology Risk Management Guidelines - Financial data outsourcing
- APRA CPS 231 (Australia) - Outsourcing and third-party data storage requirements
- OSFI B-13 (Canada) - Technology and cyber risk management for financial institutions

**Government Access and Surveillance Frameworks**:
- US CLOUD Act (Clarifying Lawful Overseas Use of Data Act) - US law enforcement access to data
- China National Intelligence Law Article 7 - Obligation to support intelligence work
- UK Investigatory Powers Act 2016 - Government surveillance and data access powers
- Five Eyes Intelligence Alliance - Information sharing between US, UK, Canada, Australia, New Zealand
- European Essential Guarantees - EDPB criteria for evaluating third-country surveillance laws
- FISA Section 702 (US) - Foreign intelligence surveillance of non-US persons
- Executive Order 12333 (US) - Signals intelligence collection authorities

**Transfer Impact Assessment (TIA) Frameworks**:
- EDPB Recommendations 01/2020 - Six-step roadmap for Transfer Impact Assessments
- ICO International Data Transfer Agreement and Guidance - UK TIA requirements
- CNIL Transfer Impact Assessment Template - French DPA guidance and tools
- IAPP Transfer Impact Assessment Practice Guide - Practitioner implementation framework
- Future of Privacy Forum TIA Templates - Standardized assessment questionnaires

**Reference**: Consult Data Protection Officer (DPO), Privacy Counsel, Cloud Architecture teams, and Infrastructure Engineering for detailed guidance on data residency framework implementation and regulatory compliance validation

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
