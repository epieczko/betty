# Name: security-architecture-diagram

## Executive Summary

The Security Architecture Diagram is a critical artifact that visualizes security controls, trust boundaries, data protection mechanisms, authentication/authorization flows, and threat mitigation strategies across a system's architecture. Using industry standards (NIST Cybersecurity Framework, ISO 27001, CIS Controls) and notations (UML, ArchiMate, threat modeling diagrams), it communicates security design to technical teams, security auditors, and compliance stakeholders.

As a cornerstone of defense-in-depth strategy, this diagram maps security controls to architecture layers (perimeter, network, host, application, data) and shows how mechanisms like encryption (AES-256, TLS 1.3), identity management (OAuth 2.0, SAML, Zero Trust), key management (HSM, KMS), and monitoring (SIEM, IDS/IPS) protect against threats documented in frameworks like MITRE ATT&CK and OWASP Top 10.

### Strategic Importance

- **Security-by-Design**: Embeds security controls at architecture level following NIST Cybersecurity Framework, ISO 27001, and Zero Trust principles
- **Compliance Enablement**: Demonstrates adherence to regulatory requirements (SOC 2, PCI DSS, HIPAA, GDPR) and security standards (CIS Controls, NIST 800-53)
- **Threat Mitigation**: Documents defenses against MITRE ATT&CK techniques, OWASP Top 10 vulnerabilities, and industry-specific threats
- **Audit Readiness**: Provides security auditors and assessors with clear view of controls, boundaries, and data protection mechanisms
- **Incident Response**: Supports security operations by documenting monitoring points, logging infrastructure, and security tool integration

## Purpose & Scope

### Primary Purpose

This artifact documents security architecture using threat modeling diagrams, security zone diagrams, data flow diagrams with trust boundaries, and control mapping visualizations. Created using tools like Microsoft Threat Modeling Tool, OWASP Threat Dragon, Lucidchart, or draw.io, it specifies authentication mechanisms, encryption standards, security zones, and monitoring infrastructure to guide secure implementation and validate compliance.

### Scope

**In Scope**:
- Security zones and trust boundaries: DMZ, internal zones, VPCs, network segmentation, micro-segmentation (Zero Trust Network Access)
- Authentication and authorization: OAuth 2.0, OpenID Connect, SAML 2.0, Multi-Factor Authentication (MFA), passwordless authentication (FIDO2, WebAuthn)
- Identity and access management: Active Directory, Azure AD, Okta, Auth0, AWS IAM, role-based access control (RBAC), attribute-based access control (ABAC)
- Encryption mechanisms: Data-at-rest (AES-256, BitLocker, LUKS), data-in-transit (TLS 1.3, mTLS), end-to-end encryption
- Key management: Hardware Security Modules (HSM), Key Management Services (AWS KMS, Azure Key Vault, GCP KMS), envelope encryption, key rotation
- Security controls: Web Application Firewall (WAF), API Gateway security, DDoS protection (CloudFlare, AWS Shield), intrusion detection/prevention (IDS/IPS)
- Monitoring and logging: SIEM (Splunk, ELK Stack, Azure Sentinel), security event correlation, audit logging, threat intelligence feeds
- Secrets management: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, sealed secrets (Kubernetes)
- Certificate management: PKI infrastructure, certificate authorities, automated certificate management (Let's Encrypt, cert-manager)

**Out of Scope**:
- Detailed implementation code and configuration files (see Security Configuration documentation)
- Penetration testing procedures and results (see Security Testing artifacts)
- Incident response playbooks and procedures (see Incident Response Plan)
- Physical security controls for data centers (see Physical Security documentation)
- Detailed vulnerability management processes (see Vulnerability Management Plan)

### Target Audience

**Primary Audience**:
- Security Architects designing defense-in-depth strategies using NIST CSF, ISO 27001, or Zero Trust frameworks
- Application Security Engineers implementing security controls, encryption, authentication, and secure coding practices
- Cloud Security Engineers configuring cloud-native security services (AWS Security Hub, Azure Security Center, GCP Security Command Center)

**Secondary Audience**:
- Compliance Officers validating controls against SOC 2, PCI DSS, HIPAA, GDPR, ISO 27001, or FedRAMP requirements
- Security Operations Center (SOC) teams understanding monitoring points, logging infrastructure, and SIEM integration
- External auditors and assessors reviewing security architecture for compliance certifications

## Document Information

**Format**: Multiple

**File Pattern**: `*.security-architecture-diagram.*`

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

**Security Frameworks & Standards**:
- NIST Cybersecurity Framework (CSF) - Identify, Protect, Detect, Respond, Recover functions
- ISO/IEC 27001:2022 - Information Security Management System (ISMS) requirements
- ISO/IEC 27002:2022 - Information security controls reference
- CIS Controls v8 - 18 critical security controls for cyber defense
- NIST SP 800-53 Rev. 5 - Security and Privacy Controls for Information Systems
- NIST SP 800-171 - Protecting Controlled Unclassified Information (CUI)
- MITRE ATT&CK Framework - Adversary tactics and techniques knowledge base
- OWASP Top 10 - Top application security risks (injection, broken authentication, XSS, etc.)
- OWASP ASVS (Application Security Verification Standard) - Application security requirements
- SANS Top 25 - Most dangerous software weaknesses
- Zero Trust Architecture - NIST SP 800-207 principles (never trust, always verify)

**Compliance & Regulatory Standards**:
- SOC 2 Type II - Trust Services Criteria (security, availability, confidentiality, privacy)
- PCI DSS 4.0 - Payment Card Industry Data Security Standard
- HIPAA Security Rule - Healthcare data protection requirements
- GDPR - EU General Data Protection Regulation (privacy and data protection)
- FedRAMP - Federal Risk and Authorization Management Program
- FISMA - Federal Information Security Management Act
- CCPA - California Consumer Privacy Act

**Threat Modeling & Risk Assessment**:
- Microsoft Threat Modeling Tool - STRIDE threat modeling (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- OWASP Threat Dragon - Open-source threat modeling tool
- PASTA (Process for Attack Simulation and Threat Analysis) - Risk-centric threat modeling
- DREAD - Risk assessment model (Damage, Reproducibility, Exploitability, Affected Users, Discoverability)
- CVSS (Common Vulnerability Scoring System) - Vulnerability severity scoring
- Common Weakness Enumeration (CWE) - Software weakness classification

**Cryptography & Encryption Standards**:
- AES (Advanced Encryption Standard) - AES-128, AES-256 for symmetric encryption
- RSA - Asymmetric encryption algorithm (2048-bit, 4096-bit)
- TLS 1.3 (Transport Layer Security) - Secure communication protocol for data-in-transit
- mTLS (Mutual TLS) - Certificate-based mutual authentication
- NIST FIPS 140-2/140-3 - Cryptographic module validation standard
- Common Criteria (ISO 15408) - Security evaluation criteria for IT products
- PKCS (Public Key Cryptography Standards) - RSA cryptography standards

**Identity & Access Management**:
- OAuth 2.0 / OAuth 2.1 - Authorization framework for delegated access
- OpenID Connect (OIDC) - Identity layer on top of OAuth 2.0
- SAML 2.0 - Security Assertion Markup Language for SSO
- FIDO2 / WebAuthn - Passwordless authentication standards
- SCIM (System for Cross-domain Identity Management) - Identity provisioning
- JWT (JSON Web Tokens) - Compact token format for claims-based identity

**Security Tools & Platforms**:
- WAF (Web Application Firewall) - ModSecurity, AWS WAF, Azure WAF, Cloudflare WAF
- SIEM (Security Information and Event Management) - Splunk, ELK Stack, Azure Sentinel, QRadar
- IDS/IPS - Snort, Suricata, Zeek (formerly Bro)
- Secrets Management - HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, CyberArk
- HSM (Hardware Security Module) - Thales, Gemalto, AWS CloudHSM, Azure Dedicated HSM
- KMS (Key Management Service) - AWS KMS, Azure Key Vault, GCP Cloud KMS
- Certificate Management - Let's Encrypt, DigiCert, cert-manager (Kubernetes)

**Cloud Security**:
- AWS Security Hub - Centralized security and compliance dashboard
- Azure Security Center / Microsoft Defender for Cloud - Cloud security posture management
- GCP Security Command Center - Security and risk management for GCP
- CSPM (Cloud Security Posture Management) - Prisma Cloud, Wiz, Orca Security
- CASB (Cloud Access Security Broker) - Microsoft Cloud App Security, Netskope

**Architecture Frameworks with Security Integration**:
- TOGAF Security Architecture - Integrated security into enterprise architecture
- SABSA (Sherwood Applied Business Security Architecture) - Risk-driven architecture framework
- O-ESA (Open Enterprise Security Architecture) - Security architecture patterns

**Reference**: Consult organizational security architecture, InfoSec, and compliance teams for detailed guidance on security control implementation, cryptographic standards selection, and regulatory compliance requirements for your specific industry and threat landscape

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
