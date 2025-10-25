# Name: certificate-policy

## Executive Summary

The Certificate Policy establishes comprehensive governance for Public Key Infrastructure (PKI) and digital certificate management including TLS/SSL certificates, code signing certificates, email encryption certificates (S/MIME), client authentication certificates, and internal certificate authorities. This critical security policy implements industry standards including X.509 v3 certificate specifications (RFC 5280), CA/Browser Forum Baseline Requirements, WebTrust Principles and Criteria for Certification Authorities, and certificate transparency requirements (RFC 6962) to ensure trust, confidentiality, authentication, and non-repudiation across enterprise systems and communications.

Modern certificate management leverages automated certificate lifecycle management platforms such as Venafi Trust Protection Platform, DigiCert CertCentral, Sectigo Certificate Manager, AppViewX CERT+, or open-source solutions (cert-manager for Kubernetes, Certbot for Let's Encrypt ACME protocol) to handle certificate issuance, renewal, revocation, and inventory management. The policy addresses public certificate authorities (DigiCert, Sectigo, GlobalSign, Let's Encrypt, Amazon Certificate Manager, Google Cloud Certificate Authority), private internal CAs (Microsoft Active Directory Certificate Services, OpenSSL-based CAs, HashiCorp Vault PKI), certificate validation (OCSP, CRL), key length requirements (RSA 2048/4096-bit, ECC P-256/P-384), approved cryptographic algorithms (SHA-256/SHA-384 hashing, AES-256 encryption), and certificate lifespan limits (398 days for public TLS certificates per CA/B Forum, 2-5 years for internal certificates).

Certificate use cases include external website TLS/SSL (HTTPS, mutual TLS), internal application encryption (database connections, API authentication), code signing (software deployment, PowerShell scripts, macOS applications, driver signing), email encryption and signing (S/MIME certificates for confidential communications), VPN authentication (IPsec, SSL VPN client certificates), device authentication (IoT, mobile device management, network access control 802.1X), and document signing (PDF digital signatures, electronic signatures). The policy establishes certificate request approval workflows, key pair generation and storage (hardware security modules for high-value keys, software keystores for general use), certificate renewal automation, emergency revocation procedures, and compliance monitoring.

### Strategic Importance

- **Encryption & Confidentiality**: Protects data in transit (TLS 1.2/1.3) and at rest through certificate-based encryption; prevents man-in-the-middle attacks and eavesdropping on sensitive communications
- **Authentication & Identity Assurance**: Establishes cryptographic proof of server, user, and device identities; prevents impersonation attacks and enables zero-trust architecture principals
- **Regulatory Compliance**: Satisfies encryption and authentication requirements for PCI DSS 4.4/4.5, HIPAA 164.312(e)(1), SOC 2 CC6.7, GDPR Article 32, and industry-specific regulations
- **Certificate Outage Prevention**: Automated renewal and expiration monitoring prevents service disruptions from expired certificates (common cause of production outages and customer-facing downtime)
- **Trust & Brand Protection**: Valid certificates from trusted CAs prevent browser security warnings, maintain customer trust, and protect brand reputation; prevents certificate spoofing and phishing attacks
- **Code Signing Integrity**: Ensures software authenticity and prevents malware distribution through compromised binaries; establishes software provenance and publisher identity
- **Audit & Non-Repudiation**: Provides cryptographic proof of actions for compliance, legal proceedings, and forensic investigations; prevents users from denying actions performed with their certificates

## Purpose & Scope

### Primary Purpose

This policy defines mandatory requirements for digital certificate provisioning, key generation, certificate validation, lifecycle management, revocation procedures, cryptographic standards, and PKI governance. It establishes authority, accountability, and technical controls for all certificate operations across the enterprise to ensure trust, security, and regulatory compliance.

### Scope

**In Scope**:
- **TLS/SSL Certificates**: External website HTTPS (publicly trusted CAs), internal application TLS (private CA or public CA), load balancer certificates, API gateway certificates, mutual TLS (mTLS) for service-to-service authentication, wildcard certificates (*.company.com), multi-domain SAN certificates, Extended Validation (EV) certificates
- **Code Signing Certificates**: Windows Authenticode signing (executables, DLLs, drivers), Java code signing (JAR files), macOS code signing (application bundles, kernel extensions), PowerShell script signing, mobile app signing (iOS, Android), container image signing (Docker Content Trust, Sigstore Cosign)
- **Email Certificates**: S/MIME certificates for email encryption and digital signatures, secure email gateways (Proofpoint, Mimecast), end-user certificate distribution and management
- **User & Device Authentication**: Client authentication certificates for VPN access, 802.1X network access control (NAC), smart card certificates for privileged user authentication, mobile device management (MDM) certificates, IoT device certificates
- **Internal Certificate Authorities**: Microsoft Active Directory Certificate Services (AD CS) deployment and management, OpenSSL-based private CA infrastructure, HashiCorp Vault PKI engine, CA hierarchy design (root CA, intermediate CAs, issuing CAs), offline root CA security, certificate templates and auto-enrollment
- **Public Certificate Authorities**: Approved CA vendors (DigiCert, Sectigo, GlobalSign, Let's Encrypt), CA account management and provisioning, certificate request validation (domain validation, organization validation, extended validation), CA/Browser Forum compliance
- **Certificate Lifecycle Management**: Automated certificate discovery and inventory, certificate request and approval workflows, key pair generation (CSR creation), certificate issuance and installation, renewal automation (30-60 days before expiration), expiration monitoring and alerting, certificate revocation (CRL, OCSP), certificate archival and audit trails
- **Cryptographic Requirements**: RSA minimum 2048-bit (prefer 4096-bit for long-lived certificates), ECC P-256/P-384 curves for modern applications, SHA-256/SHA-384 hashing algorithms (SHA-1 deprecated), approved cipher suites (TLS 1.2/1.3 only), key storage (hardware security modules for code signing and root CAs, software keystores for general use)
- **Certificate Transparency**: CT log monitoring for unauthorized certificate issuance, CAA DNS records specifying authorized CAs, certificate pinning for critical applications (HTTP Public Key Pinning successor mechanisms)
- **Automation Platforms**: Venafi Trust Protection Platform (enterprise PKI management), DigiCert CertCentral (certificate lifecycle automation), cert-manager for Kubernetes, Certbot for Let's Encrypt ACME protocol, AWS Certificate Manager (ACM), Azure Key Vault certificates, Google Cloud Certificate Authority Service
- **Monitoring & Compliance**: Certificate inventory dashboards, expiration alerting (90/60/30/7 days), weak algorithm detection (SHA-1, RSA 1024-bit), unauthorized CA usage alerts, certificate revocation checking, compliance reporting for audits

**Out of Scope**:
- **Physical Access Credentials**: Covered in physical-security-policy artifact (badge systems, smart cards for physical access, RFID tokens, visitor badges)
- **Encryption Key Management**: Covered in key-management-policy artifact (symmetric encryption keys, database encryption keys, application secrets, key rotation, key escrow)
- **Application-Specific Cryptography**: Covered in cryptographic-standards artifact (encryption algorithm selection, random number generation, cryptographic libraries, FIPS 140-2 compliance)
- **Code Signing Procedures**: Covered in secure-software-development artifact (build signing processes, CI/CD integration, developer workflows, release management)
- **Identity & Access Management**: Covered in access-control-policy and authentication-policy artifacts (user provisioning, MFA, SSO, password policies)
- **Data Classification & Handling**: Covered in data-classification-policy artifact (data sensitivity levels, encryption requirements by data type, data retention)

### Target Audience

**Primary Audience**:
- **PKI Administrators**: Operates internal certificate authorities, manages certificate templates, processes certificate requests, monitors certificate inventory, handles revocations, performs CA maintenance and backups
- **Security Engineers**: Defines cryptographic requirements, approves certificate policies, validates CA trust relationships, implements certificate pinning, monitors for unauthorized certificates, responds to certificate security incidents
- **IT Operations & Infrastructure Teams**: Installs and renews certificates on servers and network devices, configures web servers and load balancers for TLS, troubleshoots certificate validation errors, monitors certificate expirations
- **Cloud Platform Engineers**: Manages ACM, Azure Key Vault, GCP CA Service, implements certificate automation in cloud environments, configures auto-renewal, integrates with Terraform/CloudFormation
- **DevOps/SRE Teams**: Integrates cert-manager into Kubernetes, automates certificate renewal in CI/CD pipelines, implements Let's Encrypt ACME workflows, monitors certificate health in production

**Secondary Audience**:
- **Chief Information Security Officer (CISO)**: Approves certificate policy, authorizes approved CAs, allocates PKI budget, reviews certificate-related security incidents, presents certificate security posture to board
- **Compliance & Audit Teams**: Validates certificate policy compliance for SOC 2, PCI DSS, HIPAA audits, reviews certificate inventory, tests certificate controls, verifies cryptographic standards
- **Application Development Teams**: Requests certificates for applications, implements certificate-based authentication, handles certificate errors, renews application certificates, integrates with PKI APIs
- **Procurement/Vendor Management**: Manages CA vendor relationships and contracts, processes certificate purchase orders, negotiates volume pricing, evaluates CA vendor security and financial stability
- **Legal/Risk Management**: Reviews certificate policy for legal sufficiency, assesses liability for certificate misuse, manages certificate insurance policies, handles certificate-related legal disputes
- **External Auditors**: Reviews certificate policy during SOC 2, ISO 27001, PCI DSS audits, validates certificate controls, tests key strength and algorithm compliance

## Document Information

**Format**: Markdown

**File Pattern**: `*.certificate-policy.md`

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
**Legal Review**: Have legal counsel review before approval
**Exception Process**: Define clear exception request and approval process
**Communication Plan**: Communicate policy broadly with training as needed
**Enforcement Mechanism**: Define how compliance is monitored and enforced
**Automated Lifecycle Management**: Implement certificate lifecycle platforms (Venafi, DigiCert, cert-manager) to automate discovery, renewal, and expiration monitoring; manual tracking fails at scale
**Certificate Inventory Required**: Maintain complete inventory of all certificates including location, owner, expiration, CA issuer; unknown certificates are major security risk
**Short Certificate Lifespans**: Prefer 90-day certificates (Let's Encrypt model) over 1-year to force automation and reduce exposure from compromised keys; CA/B Forum mandates maximum 398 days
**Expiration Alerting**: Alert 90/60/30/7 days before expiration; escalate to management for certificates <7 days from expiration; expired certificates cause production outages
**Wildcard Certificate Caution**: Limit wildcard certificate (*.domain.com) use due to broad scope of compromise; prefer specific domain certificates where feasible
**Private Key Protection**: Store code signing and root CA private keys in FIPS 140-2 Level 2+ HSMs; general-use keys in encrypted keystores with access controls
**Certificate Revocation Preparedness**: Document and test certificate revocation procedures; establish emergency contacts for CA vendors for urgent revocations
**Let's Encrypt for Non-Production**: Use Let's Encrypt for dev/test environments to avoid CA costs; reserve paid CAs for production and warranty requirements
**Certificate Pinning Carefully**: Implement certificate pinning for mobile apps and critical services to prevent MITM attacks; include backup pins to avoid outage if primary certificate rotated
**Avoid Self-Signed in Production**: Never use self-signed certificates in production; breaks browser trust, prevents security tooling integration, no warranty/insurance coverage
**CAA DNS Records**: Implement Certificate Authority Authorization (CAA) DNS records to specify which CAs are authorized to issue certificates for your domains
**Certificate Transparency Monitoring**: Monitor CT logs using services like crt.sh or Facebook CT Monitor to detect unauthorized certificate issuance
**Separate Code Signing Keys**: Use separate code signing certificates for different software products; compromise of one certificate doesn't affect all products
**Time-Stamping for Code Signing**: Always include trusted timestamp in code signatures so signature remains valid after certificate expires
**Offline Root CA**: Keep root CA offline (air-gapped) for security; only bring online for issuing intermediate certificates every 1-2 years
**Regular CA Security Audits**: Audit internal CA configurations quarterly; validate templates, permissions, key storage, logging, and backup procedures
**Certificate Renewals in Advance**: Renew certificates 30-60 days before expiration to allow time for testing and rollback if issues discovered
**Multi-Domain SAN Certificates**: Use Subject Alternative Name (SAN) certificates to consolidate multiple domains into single certificate; reduces management overhead
**TLS 1.3 Adoption**: Migrate to TLS 1.3 for performance and security improvements; deprecate TLS 1.0/1.1 per PCI DSS and industry standards
**Certificate Cost Optimization**: Use free Let's Encrypt for non-critical services; negotiate volume pricing with commercial CAs for production certificates

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

**PKI & Certificate Standards**:
- RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- RFC 6960: X.509 Internet Public Key Infrastructure Online Certificate Status Protocol (OCSP)
- RFC 6962: Certificate Transparency (CT) requirements and log monitoring
- RFC 7030: Enrollment over Secure Transport (EST) for automated certificate enrollment
- RFC 8555: Automatic Certificate Management Environment (ACME) protocol (Let's Encrypt standard)
- X.509 v3: ITU-T standard for digital certificate format and extensions
- PKCS #10: Certification Request Syntax Standard (CSR format)
- PKCS #12: Personal Information Exchange Syntax (PFX/P12 certificate bundles)

**CA/Browser Forum Requirements**:
- Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates: Maximum 398-day certificate validity, domain validation requirements, key length minimums, revocation timelines
- Extended Validation Guidelines: Identity verification requirements for EV certificates
- Code Signing Baseline Requirements: Private key protection for code signing certificates, timestamp requirements
- S/MIME Baseline Requirements: Email certificate issuance and validation standards

**Audit & Trust Standards**:
- WebTrust for Certification Authorities: Independent audit framework for public CAs; required for browser/OS trust inclusion
- WebTrust for Certification Authorities - SSL Baseline with Network Security: Additional requirements for TLS certificate issuance
- ETSI EN 319 411: Policy and security requirements for Trust Service Providers issuing certificates (European standard)
- ISO/IEC 27006: Requirements for bodies providing audit and certification of information security management systems (includes CA audits)

**Cryptographic Standards**:
- NIST SP 800-52 Rev 2: Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations
- NIST SP 800-57: Recommendation for Key Management (key lengths, algorithm lifetimes)
- NIST SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths
- FIPS 186-4: Digital Signature Standard (DSS) for public key cryptography
- FIPS 140-2/140-3: Security Requirements for Cryptographic Modules (HSM validation)

**Compliance Requirements**:
- PCI DSS v4.0: Requirement 4.2 (Protect cardholder data with strong cryptography during transmission), Requirement 6.2.4 (Certificate validation), Requirement 12.3 (Acceptable use policies for critical technologies)
- HIPAA Security Rule: 164.312(e)(1) (Transmission security - encryption of ePHI), 164.312(a)(2)(iv) (Encryption and decryption)
- SOC 2 Type II: CC6.7 (Restricts transmission of sensitive data), CC6.1 (Logical access controls), additional criteria for encryption key management
- GDPR Article 32: Security of processing including encryption and pseudonymization requirements
- FISMA/FedRAMP: SC-12 (Cryptographic Key Establishment and Management), SC-13 (Cryptographic Protection), SC-17 (Public Key Infrastructure Certificates)

**Browser & OS Trust Programs**:
- Apple Root Certificate Program: Requirements for CA inclusion in macOS/iOS trust stores
- Google Chrome Certificate Transparency Policy: CT log requirements for certificate validity
- Microsoft Trusted Root Program: Requirements for Windows trust store inclusion
- Mozilla CA Certificate Policy: Requirements for Firefox/Thunderbird trust inclusion
- Android Certificate Authority Requirements: Google's requirements for Android trust

**Industry Best Practices**:
- NIST Cybersecurity Framework (CSF): PR.DS-2 (Data-in-transit protected), PR.DS-5 (Protections against data leaks), ID.AM-3 (Organizational communication flows mapped)
- CIS Controls v8: 3.3 (Configure data access control lists), 3.10 (Encrypt sensitive data in transit), 14.4 (Encrypt all sensitive information in transit)
- OWASP Transport Layer Protection Cheat Sheet: TLS configuration best practices for web applications
- Cloud Security Alliance (CSA): Certificate management in cloud environments, secrets management best practices

**Vendor Platform Documentation**:
- Venafi Trust Protection Platform: Enterprise PKI policy enforcement, certificate discovery, lifecycle automation
- DigiCert CertCentral: Certificate lifecycle management, ACME integration, bulk certificate operations
- Microsoft AD CS Best Practices: Certificate templates, auto-enrollment, CA hierarchy design, CA security hardening
- Let's Encrypt Documentation: ACME protocol implementation, rate limits, certificate renewal best practices
- AWS Certificate Manager (ACM): Managed certificate service, automatic renewal, CloudFront/ELB integration
- Azure Key Vault Certificates: Certificate lifecycle management, HSM-backed keys, automatic rotation
- Google Cloud Certificate Authority Service: Private CA management, certificate issuance APIs, integration with GKE

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
