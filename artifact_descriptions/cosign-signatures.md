# Name: cosign-signatures

## Executive Summary

The Cosign Signatures artifact documents cryptographic signatures for container images and software artifacts using Sigstore's Cosign tool, a critical component of software supply chain security. This artifact provides verifiable proof of artifact authenticity, enabling organizations to establish trust in their software supply chain through keyless signing with OIDC identity, transparency logs via Rekor, and integration with policy enforcement tools like Open Policy Agent (OPA) and Kyverno.

As software supply chain attacks have increased 650% year-over-year (Sonatype 2024), Cosign signatures serve as a foundational control for zero-trust software distribution. This artifact enables verification of artifact provenance, detection of tampering, and compliance with SLSA (Supply Chain Levels for Software Artifacts) requirements for build integrity. Organizations leveraging Cosign can achieve SLSA Level 3+ compliance through cryptographic verification combined with in-toto attestation and SBOM correlation.

### Strategic Importance

- **Supply Chain Security**: Mitigates software supply chain risks through cryptographic verification (SLSA Level 2+ requirement)
- **Zero-Trust Distribution**: Enables policy-based admission control in Kubernetes with signature verification
- **Regulatory Compliance**: Supports Executive Order 14028 requirements for SBOM and software provenance
- **Incident Response**: Provides forensic trail for software artifact integrity verification with 90-day SLA for critical vulnerabilities
- **CI/CD Integration**: Automates signing in GitHub Actions, GitLab CI, CircleCI with keyless OIDC authentication
- **Transparency & Auditability**: Leverages Rekor transparency log for immutable signature records
- **Policy Enforcement**: Integrates with Kyverno, OPA Gatekeeper, and Ratify for admission control

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative record of cryptographic signatures applied to container images, binary artifacts, and software packages using Sigstore Cosign. It documents signature metadata including public keys, OIDC identity claims, Rekor transparency log entries, and verification results to enable trustworthy software distribution and policy-based admission control in cloud-native environments.

### Scope

**In Scope**:
- Cosign signature generation with keyless signing (OIDC-based Fulcio certificates)
- Container image signatures for Docker, OCI, and Kubernetes artifacts
- Key-based signing with traditional PKI and hardware security modules (HSMs)
- Rekor transparency log entries and inclusion proofs
- Signature verification workflows with Cosign verify and policy engines
- Integration with SLSA provenance attestations and in-toto layouts
- Admission controller policies (Kyverno, OPA Gatekeeper, Ratify)
- SBOM attestation signing with SPDX and CycloneDX formats
- Multi-arch image signatures for ARM64, AMD64, and other platforms
- Air-gapped environment signing workflows with private Sigstore instances
- Signature key rotation and revocation procedures
- CI/CD pipeline integration (GitHub Actions, GitLab CI, Jenkins, Tekton)
- Policy-as-code for signature verification requirements
- Vulnerability Exploitability eXchange (VEX) statement signing

**Out of Scope**:
- General PKI certificate management (see certificate-management-policy.md)
- Code signing for non-container artifacts (see code-signing-policy.md)
- SBOM generation tooling (see sbom-generation-playbook.md)
- Vulnerability scanning results (see vulnerability-scan-reports.md)
- Container registry access controls (see registry-access-policy.md)

### Target Audience

**Primary Audience**:
- Security Engineers implementing supply chain security controls and signature verification
- DevOps Engineers integrating Cosign signing into CI/CD pipelines
- Platform Engineers deploying admission controllers with signature policy enforcement
- Compliance Officers verifying adherence to Executive Order 14028 and SLSA requirements

**Secondary Audience**:
- Security Architects designing zero-trust software distribution architectures
- Incident Response Teams investigating software supply chain compromises
- Auditors reviewing software provenance and cryptographic verification controls
- Open Source Security Foundation (OpenSSF) contributors implementing best practices

## Document Information

**Format**: Markdown

**File Pattern**: `*.cosign-signatures.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal (signature metadata public, private keys Confidential)

**Retention**: 7 years per software supply chain audit requirements


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

**Keyless Signing Default**: Use OIDC-based keyless signing with Fulcio for ephemeral certificates to eliminate key management burden
**Rekor Transparency**: Always publish signatures to Rekor transparency log for auditability and non-repudiation
**SLSA Provenance**: Combine Cosign signatures with SLSA provenance attestations for comprehensive build integrity
**Multi-Arch Signing**: Sign all platform-specific images individually and create signed image index for multi-arch manifests
**Policy-as-Code**: Define signature verification policies in Kyverno or OPA for automated admission control
**CI/CD Integration**: Automate signing in pipeline with dedicated service accounts and least-privilege OIDC claims
**Signature Verification**: Verify signatures before deployment using cosign verify with public key or OIDC issuer
**Private Sigstore Instances**: Deploy private Fulcio/Rekor for air-gapped or highly regulated environments
**SBOM Attestation**: Attach SBOM as signed attestation using cosign attest for software bill of materials
**VEX Statements**: Sign vulnerability exploitability statements to document false positives and mitigations
**Key Rotation**: Rotate signing keys every 90 days for key-based signing; keyless automatically rotates via Fulcio
**Admission Control**: Require signature verification in production clusters with ClusterPolicy or ValidatingWebhook
**Timestamp Authority**: Use RFC 3161 timestamp authority for long-term signature validity beyond certificate expiry
**Offline Verification**: Cache Rekor bundle and public keys for environments with limited internet connectivity
**Sigstore Conformance**: Verify Cosign implementation against Sigstore conformance test suite
**Monitoring & Alerting**: Alert on signature verification failures, expired certificates, and Rekor unavailability
**Disaster Recovery**: Maintain offline backups of signing keys and Rekor transparency log entries
**Documentation**: Document OIDC identity mapping, key storage locations, and signature verification procedures
**Testing**: Test signature verification in staging before enforcing in production environments
**Compliance Mapping**: Map signature requirements to SLSA levels, NIST SSDF, and Executive Order 14028
**Supply Chain Metadata**: Include git commit SHA, build timestamp, and builder identity in signature claims
**Vulnerability Window**: Resign images when critical vulnerabilities are patched to update SBOM attestations
**Forensics**: Preserve signature artifacts for incident response and post-incident analysis (minimum 1 year)

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

**Supply Chain Security Standards**:
- SLSA (Supply Chain Levels for Software Artifacts) v1.0 - Levels 1-4 for build integrity
- NIST SP 800-218 SSDF (Secure Software Development Framework) practices
- Executive Order 14028 on Improving the Nation's Cybersecurity (Section 4)
- CISA Secure Software Development Attestation Form requirements
- ISO/IEC 27001:2022 Annex A.8.31 (Separation of development, test and production environments)
- ISO/IEC 27034 Application Security for supply chain controls
- CIS Software Supply Chain Security Guide v1.0
- NIST SP 800-161 Rev 1 Cybersecurity Supply Chain Risk Management
- OpenSSF Scorecards for repository health and security posture
- OWASP Software Component Verification Standard (SCVS)
- IEEE 2675-2021 DevOps Standard for Build, Test, and Release processes

**Sigstore & Cosign Standards**:
- Sigstore Cosign specification and keyless signing protocol
- Fulcio Certificate Authority for short-lived code signing certificates
- Rekor transparency log API specification and inclusion proofs
- in-toto Attestation Framework for provenance and policy
- SLSA Provenance specification v0.2 and v1.0 formats
- The Update Framework (TUF) for secure software update systems
- Notary v2 specification for OCI artifact signing (alternate to Cosign)
- OCI Image Manifest Specification v1.0 for artifact references
- RFC 3161 Time-Stamp Protocol for trusted timestamps
- PKCS#11 for hardware security module (HSM) integration

**Container & Kubernetes Security**:
- NIST SP 800-190 Application Container Security Guide
- CIS Kubernetes Benchmark v1.8 for admission controller configuration
- Kubernetes Pod Security Standards (Restricted, Baseline, Privileged)
- OPA (Open Policy Agent) Rego policy language for admission control
- Kyverno policy engine for Kubernetes admission control
- Ratify for supply chain artifact verification in Kubernetes
- Azure Container Registry (ACR), Amazon ECR, Google GCR signature storage
- Harbor registry with content trust and Cosign integration
- Trivy, Grype, and Snyk for vulnerability scanning integration

**SBOM & Vulnerability Management**:
- SPDX (Software Package Data Exchange) 2.3 and 3.0 for SBOM formats
- CycloneDX 1.4+ specification for SBOM and VEX
- NTIA Minimum Elements for Software Bill of Materials
- VEX (Vulnerability Exploitability eXchange) for vulnerability status
- CVSS v3.1 and v4.0 Common Vulnerability Scoring System
- CVE (Common Vulnerabilities and Exposures) identifiers
- CISA Known Exploited Vulnerabilities (KEV) catalog
- NVD (National Vulnerability Database) integration
- OSV (Open Source Vulnerabilities) schema for vulnerability disclosure

**Cryptography & PKI**:
- FIPS 140-2/140-3 cryptographic module validation
- NIST SP 800-57 Recommendation for Key Management
- RFC 5280 X.509 Certificate and CRL Profile
- RFC 6960 Online Certificate Status Protocol (OCSP)
- RFC 8446 TLS 1.3 for secure communication
- NIST SP 800-208 Recommendation for Stateful Hash-Based Signature Schemes
- WebAuthn and FIDO2 for hardware-backed authentication
- OAuth 2.0 and OpenID Connect (OIDC) for keyless signing identity

**Compliance & Audit Frameworks**:
- SOC 2 Type II Trust Service Criteria (CC6.6 for logical access)
- ISO/IEC 27001:2022 Information Security Management
- PCI DSS 4.0 Requirement 6 (Secure Software Development)
- FedRAMP Rev 5 controls for federal systems
- NIST Cybersecurity Framework 2.0 (Supply Chain Risk Management)
- CIS Controls v8 (Control 16.14 - Establish and Maintain a Secure Application Development Process)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Container images and OCI artifacts requiring signature
- CI/CD pipeline configuration (GitHub Actions, GitLab CI, Jenkins)
- Identity provider (IdP) configuration for OIDC keyless signing
- Public key infrastructure (PKI) for key-based signing
- SBOM generation outputs from Syft, Trivy, or dependency scanning tools
- SLSA provenance attestations from build systems

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Kubernetes admission controllers (Kyverno, OPA Gatekeeper, Ratify)
- Container registry policies for signature enforcement
- Security Information and Event Management (SIEM) systems
- Compliance reporting and audit artifacts
- Incident response procedures for supply chain compromises
- Vulnerability management workflows requiring signed VEX statements

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- SBOM generation and verification documentation
- Container security scanning policies
- Software supply chain risk management plans
- Cryptographic key management procedures
- Incident response playbooks for supply chain attacks

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
- Primary Approver: CISO or Chief Security Architect
- Secondary Approver: DevOps/Platform Engineering Lead
- Governance Approval: Security Architecture Review Board (SARB)

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review for tooling updates and policy changes

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

**Retention Period**: 7 years per software supply chain audit requirements

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Security Engineering Team Lead

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/cosign-signatures-template.md`

**Alternative Formats**: JSON schema for automated signature verification

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/cosign-signatures-example-*.md`

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

- SOC 2: CC6.6 Logical and Physical Access Controls
- ISO 27001: A.8.31 Separation of development, testing and production environments
- GDPR/Privacy: Not typically applicable to signatures
- Industry-Specific: Executive Order 14028 for federal suppliers

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

- Software supply chain security policy
- Cryptographic key management policy
- Container security standards
- SLSA compliance requirements

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

**Phase**: Security & Operations

**Category**: Supply Chain Security

**Typical Producers**: Security Engineers, DevOps Engineers, Platform Engineers

**Typical Consumers**: Security Architects, Compliance Officers, Incident Response Teams

**Effort Estimate**: 2-4 hours for initial setup, 30 minutes per artifact signed

**Complexity Level**: High

**Business Criticality**: Mission Critical

**Change Frequency**: Regular (weekly for new artifacts)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Security & Operations - Version 2.0*
