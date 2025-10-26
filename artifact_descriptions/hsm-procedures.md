# Name: hsm-procedures

## Executive Summary

The HSM Procedures artifact documents operational procedures for Hardware Security Modules (HSMs) including FIPS 140-2 Level 3 initialization, crypto officer role management, key generation and backup, firmware updates, and disaster recovery operations. This artifact provides comprehensive operational guidance for managing SafeNet Luna, Thales nShield, AWS CloudHSM, Azure Dedicated HSM, and YubiHSM platforms ensuring cryptographic key protection, tamper resistance, and regulatory compliance.

As a critical operational control for cryptographic infrastructure, HSM procedures serve crypto officers performing daily HSM operations, security engineers implementing key management workflows, PKI administrators managing certificate authority infrastructure, and compliance teams demonstrating FIPS 140-2/3, PCI-DSS, and Common Criteria adherence. Integration with key management systems, certificate authorities, code signing infrastructure, and encryption services ensures HSM-protected cryptographic operations across the enterprise while maintaining detailed audit logs and access controls.

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

This artifact serves as authoritative operational documentation for HSM lifecycle management including initialization, partitioning, crypto officer credential management, key generation and storage, backup and recovery, firmware updates, security monitoring, and decommissioning. It provides step-by-step procedures for FIPS 140-2 Level 3 operations, emergency response for HSM failures, and compliance validation ensuring cryptographic operations meet regulatory and security requirements.

### Scope

**In Scope**:
- HSM initialization and FIPS mode activation (FIPS 140-2 Level 2/3)
- Crypto Officer (CO) and Security Officer (SO) role management
- HSM partitioning and client application access controls
- Key generation within HSM (RSA, ECDSA, AES, HMAC keys)
- Key backup and cloning (HSM-to-HSM secure transfer)
- PKCS#11, JCE, CNG, and KSP integration
- Firmware update and vulnerability patching procedures
- HSM health monitoring and performance metrics
- Audit log management and SIEM integration
- Disaster recovery and failover procedures
- HSM decommissioning and secure key destruction
- Cloud HSM operations (AWS CloudHSM, Azure Dedicated HSM, Google Cloud HSM)
- USB HSM operations (YubiHSM 2, Nitrokey HSM)
- Network HSM clustering and high availability
- Entropy pool monitoring and RNG validation

**Out of Scope**:
- Key ceremony procedures for root CA operations (covered by key ceremony records)
- Certificate issuance workflows (covered by CA operational procedures)
- Application-specific cryptographic implementations (covered by application artifacts)
- HSM procurement and vendor selection (covered by procurement artifacts)
- Physical data center security (covered by facilities security)

### Target Audience

**Primary Audience**:
- Crypto Officers performing daily HSM operations and key management
- HSM Administrators configuring partitions, policies, and access controls
- Security Engineers integrating applications with HSM services

**Secondary Audience**:
- PKI Administrators using HSMs for CA operations
- DevOps Engineers managing cloud HSM infrastructure (CloudHSM, Azure)
- Compliance Officers demonstrating FIPS 140-2, PCI-DSS, HIPAA compliance

## Document Information

**Format**: Markdown

**File Pattern**: `*.hsm-procedures.md`

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

**FIPS Mode Always**: Initialize HSMs in FIPS 140-2 mode; never operate in non-FIPS mode for production; verify FIPS validation certificate
**Dual Control**: Implement dual control for all critical operations; require minimum 2 crypto officers for key generation, backup, restore
**M-of-N Authentication**: Use M-of-N quorum authentication (e.g., 3-of-5 COs required) for high-security operations
**Partition Isolation**: Create separate HSM partitions per application/environment; isolate development, staging, production keys
**Role Separation**: Maintain strict separation between Security Officer (SO) and Crypto Officer (CO) roles; never combine roles
**Credential Security**: Store CO/SO credentials in password manager or physical safe; enforce password complexity; rotate quarterly
**Backup HSMs**: Maintain backup HSM in geographically separate facility; regularly test backup/restore procedures
**Firmware Updates**: Apply firmware updates promptly; follow vendor security advisories; test updates in non-production HSM first
**Audit Logging**: Enable comprehensive audit logging; forward logs to SIEM in real-time; retain logs 7+ years per compliance requirements
**Tamper Monitoring**: Monitor tamper sensors continuously; implement immediate alerting for tamper events; investigate all tamper alerts
**Network Segmentation**: Isolate HSMs on dedicated network segment; implement strict firewall rules; use VPN/TLS for remote access
**Physical Security**: Secure HSMs in locked data center with access controls; implement video surveillance; use tamper-evident seals
**Key Lifecycle**: Document key generation dates, expiration, usage policies; implement automated key rotation; track key usage metrics
**Entropy Monitoring**: Monitor HSM random number generator health; alert on entropy pool exhaustion; validate RNG quality periodically
**Capacity Planning**: Monitor HSM capacity (keys, sessions, throughput); plan for growth; implement clustering for scalability
**Disaster Recovery**: Document and test DR procedures annually; maintain runbooks for HSM failover; validate backup restoration
**Cloud HSM Security**: For CloudHSM/Azure HSM, use VPC/VNet isolation; implement least privilege IAM policies; enable CloudTrail/Azure Monitor
**Decommissioning**: Zeroize HSMs before decommissioning; verify complete key destruction; document destruction certificate
**Vendor Support**: Maintain active support contracts; establish direct vendor escalation path; participate in vendor security bulletins

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

**HSM Platforms & Vendors**:
- SafeNet Luna HSM (Thales Luna Network HSM, Luna PCIe, Luna USB)
- Thales nShield HSM (nShield Connect, nShield Solo, nShield Edge, nShield as a Service)
- AWS CloudHSM (FIPS 140-2 Level 3 validated)
- Azure Dedicated HSM (Thales Luna Network HSM in Azure)
- Google Cloud HSM (FIPS 140-2 Level 3 validated)
- IBM Cloud HSM (based on Thales Luna)
- Utimaco CryptoServer (HSM for payment and PKI)
- YubiHSM 2 (USB HSM for small-scale PKI and code signing)
- Nitrokey HSM (open-source USB HSM)
- Marvell LiquidSecurity HSM (formerly Cavium)

**FIPS & Security Standards**:
- FIPS 140-2 (Security Requirements for Cryptographic Modules) Levels 1-4
- FIPS 140-3 (updated standard with enhanced requirements)
- Common Criteria for Information Technology Security Evaluation (CC EAL4+)
- Protection Profile for Cryptographic Modules (PP-CM)
- NIST SP 800-131A (Transitioning the Use of Cryptographic Algorithms and Key Lengths)
- NIST SP 800-133 (Recommendation for Cryptographic Key Generation)
- NIST SP 800-57 (Recommendation for Key Management)
- NIST SP 800-90A/B/C (Random Number Generation)

**HSM APIs & Interfaces**:
- PKCS#11 (Cryptographic Token Interface Standard)
- Microsoft CNG (Cryptography API: Next Generation)
- Microsoft CAPI (CryptoAPI - legacy)
- Java JCA/JCE (Java Cryptography Architecture/Extension)
- OpenSSL Engine interface
- KMIP (Key Management Interoperability Protocol)
- REST APIs (cloud HSM management)

**Key Management Standards**:
- NIST SP 800-57 Parts 1-3 (Key Management)
- NIST SP 800-130 (Framework for Designing Cryptographic Key Management Systems)
- ANSI X9.24 (Retail Financial Services Symmetric Key Management)
- PCI-DSS Appendix A1 (Additional PCI DSS Requirements for HSM usage)
- PKCS#1 (RSA Cryptography Standard)
- PKCS#12 (Personal Information Exchange Syntax)

**Cloud HSM Management**:
- AWS CloudHSM CLI and SDK
- Azure Key Vault with Dedicated HSM
- Google Cloud KMS and Cloud HSM
- HashiCorp Vault Transit Engine with HSM
- Kubernetes External Secrets with HSM backend

**HSM Clustering & HA**:
- SafeNet Luna HSM HA (high availability clustering)
- Thales nShield CodeSafe (custom firmware for HSM)
- Load balancing across HSM partitions
- Disaster recovery HSM synchronization
- Multi-region HSM deployment (active-active, active-passive)

**Regulatory Compliance**:
- PCI-DSS Requirement 3.5/3.6 (HSM for encryption key management)
- HIPAA Security Rule 164.312(a)(2)(iv) (Encryption and Decryption)
- GDPR Article 32 (Security of Processing - encryption)
- SOC 2 Type II (CC6.1, CC6.6 - Logical and Physical Access Controls)
- ISO 27001 A.10.1.2 (Key Management)
- Federal PKI (FPKI) requirements for HSM usage
- Payment Card Industry PIN Transaction Security (PCI PTS) HSM requirements
- eIDAS Regulation (EU electronic identification and trust services)

**HSM Operations**:
- Crypto Officer (CO) procedures (key generation, backup, restore)
- Security Officer (SO) procedures (partition management, CO credential management)
- Dual control and split knowledge implementation
- M-of-N authentication schemes (quorum authentication)
- HSM firmware update procedures
- Backup and disaster recovery procedures
- Key destruction and zeroization procedures

**Monitoring & Logging**:
- HSM audit log formats (syslog, CEF, LEEF)
- SIEM integration (Splunk, QRadar, ArcSight, Sentinel)
- HSM health monitoring (performance, capacity, temperature)
- Tamper detection and alerting
- Key usage analytics and anomaly detection

**Use Cases**:
- Certificate Authority (CA) key protection
- Code signing certificate key storage
- Database encryption (Transparent Data Encryption - TDE)
- SSL/TLS private key protection for web servers
- Payment processing (PIN encryption, key derivation)
- Document signing and digital signatures
- Blockchain and cryptocurrency key management
- Key management for tokenization systems

**Reference**: Consult HSM vendor documentation, FIPS 140-2 validation certificates, and crypto team for platform-specific procedures and compliance validation

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
