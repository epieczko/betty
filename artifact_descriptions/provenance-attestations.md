# Name: provenance-attestations

## Executive Summary

The Provenance Attestations artifact provides cryptographically-signed build provenance records using SLSA (Supply-chain Levels for Software Artifacts), in-toto, and Sigstore frameworks to establish tamper-evident chains of custody for software artifacts, container images, and AI/ML models. These attestations create verifiable audit trails documenting what was built, when, by whom, from what source code, using what dependencies, enabling detection of supply chain compromises and compliance with emerging software security regulations.

Software supply chain attacks have increased 742% since 2019, with high-profile incidents like SolarWinds and Log4j demonstrating the critical need for build provenance verification. Provenance attestations solve this by generating cryptographically-signed metadata (SLSA provenance, SBOM, VEX) that can be verified at deployment time, ensuring artifacts haven't been tampered with between build and runtime. This artifact documents the standards, tools (Sigstore, in-toto, SLSA), and processes for generating, signing, and verifying provenance attestations across CI/CD pipelines.

### Strategic Importance

- **Supply Chain Security**: Prevents malicious code injection by verifying artifact integrity from source to deployment (SLSA framework)
- **Regulatory Compliance**: Meets emerging software security requirements (Executive Order 14028, EU Cyber Resilience Act, NIST SSDF)
- **Incident Response**: Enables rapid identification of affected systems during vulnerability disclosures (Log4j-style incidents)
- **Dependency Transparency**: Provides SBOM (Software Bill of Materials) for license compliance and vulnerability management
- **Non-Repudiation**: Cryptographic signatures establish legal accountability for software provenance
- **Zero Trust Architecture**: Enables verification of artifact provenance before deployment in zero-trust environments
- **Customer Assurance**: Provides verifiable evidence of secure build practices to security-conscious enterprise customers

## Purpose & Scope

### Primary Purpose

This artifact serves as the implementation guide for generating, signing, and verifying cryptographic provenance attestations using SLSA, in-toto, and Sigstore. It documents how to instrument CI/CD pipelines to automatically generate SLSA provenance, sign artifacts with Sigstore (Cosign), and verify attestations at deployment time to prevent supply chain compromises.

### Scope

**In Scope**:
- SLSA (Supply-chain Levels for Software Artifacts) provenance generation for builds (SLSA Levels 1-4)
- in-toto attestations documenting build steps and artifact transformations
- Sigstore signing (Cosign for container images, Rekor transparency log, Fulcio keyless signing)
- SBOM (Software Bill of Materials) generation using SPDX, CycloneDX, and Syft
- VEX (Vulnerability Exploitability eXchange) for vulnerability disclosure
- Build provenance for container images (Docker, OCI images)
- AI/ML model provenance (training data lineage, model cards, reproducibility metadata)
- Cryptographic signing of release artifacts (binaries, packages, containers)
- Provenance verification in deployment pipelines (admission controllers, policy enforcement)

**Out of Scope**:
- Source code signing and commit verification (handled through Git commit signing)
- Runtime security monitoring and anomaly detection (covered in runtime security tooling)
- Vulnerability scanning and remediation (managed through security scanning tools)
- Dependency management and update automation (handled by Dependabot, Renovate)
- Secrets management and key rotation (covered in secrets management documentation)
- Incident response playbooks (documented in security incident response plans)

### Target Audience

**Primary Audience**:
- DevSecOps Engineers: Implement provenance attestation generation in CI/CD pipelines
- Security Engineers: Configure provenance verification policies and admission controls
- Platform Engineers: Deploy Sigstore infrastructure (Fulcio, Rekor, Cosign) and in-toto tooling

**Secondary Audience**:
- Compliance Teams: Demonstrate software supply chain security controls to auditors and customers
- Release Managers: Understand provenance requirements for production releases
- Customer Security Teams: Verify provenance attestations of vendor-provided software and containers

## Document Information

**Format**: Markdown

**File Pattern**: `*.provenance-attestations.md`

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

**SLSA Level 2 Minimum**: Achieve SLSA Level 2 (hosted build, signed provenance) as baseline for all production artifacts
**Keyless Signing**: Use Sigstore Fulcio keyless signing to avoid long-lived private key management burden
**Automated Provenance**: Generate SLSA provenance automatically in CI/CD; never manually create provenance
**Builder Identity**: Use OIDC identity from GitHub Actions, GitLab CI as signer identity (no service accounts with keys)
**Transparency Logging**: Record all signatures in Rekor transparency log for public accountability
**SBOM Generation**: Generate SBOM (SPDX or CycloneDX) automatically on every build using Syft or Trivy
**Provenance Attachment**: Store provenance as OCI artifact attestations alongside container images
**Hermetic Builds**: Use containerized builds or Bazel for reproducible, hermetic build environments (SLSA Level 4 goal)
**Dependency Pinning**: Pin all dependencies with cryptographic hashes (npm lock files, Go sum files, Python requirements.txt with hashes)
**Build Isolation**: Run builds in ephemeral, isolated environments (GitHub Actions hosted runners, GitLab shared runners)
**Two-Party Review**: Require code review approval before merge (GitHub branch protection, GitLab approval rules)
**Verification at Deploy**: Enforce signature verification in Kubernetes admission controllers (Kyverno, Policy Controller)
**Policy-as-Code**: Define provenance verification policies in OPA Rego or Kyverno YAML
**Git Commit Signing**: Sign Git commits with Sigstore Gitsign for end-to-end source-to-artifact traceability
**VEX Publication**: Publish VEX documents when vulnerabilities are not exploitable in your context
**Attestation Bundles**: Package SLSA provenance, SBOM, and signatures together for verification
**Public Transparency**: Make provenance attestations publicly verifiable when possible (open source projects)
**Incident Readiness**: Practice supply chain incident response (what if Rekor is compromised, how to rotate identities)
**Reproducible Builds**: Invest in reproducible builds for critical software (Debian reproducible builds model)
**Dependency Scanning**: Scan SBOM for known vulnerabilities using Grype, Trivy, or Snyk before deployment

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

**Supply Chain Security Frameworks**:
- SLSA (Supply-chain Levels for Software Artifacts): Framework defining 4 levels of supply chain security maturity
- in-toto: Framework for securing software supply chain integrity through layout and link metadata
- NIST SSDF (Secure Software Development Framework): Secure development practices including provenance
- NIST SP 800-218: Secure Software Development Framework implementation guidance
- SCVS (Software Component Verification Standard): OWASP standard for software supply chain security

**Sigstore Ecosystem**:
- Cosign: Container signing and verification tool (OCI image signatures)
- Rekor: Transparency log for software artifact signatures (certificate transparency for software)
- Fulcio: Keyless signing using OIDC identity (no long-lived private keys)
- Gitsign: Git commit signing using Sigstore (ephemeral certificates)
- Policy Controller: Kubernetes admission controller for signature verification

**SBOM (Software Bill of Materials) Standards**:
- SPDX (Software Package Data Exchange): ISO/IEC 5962:2021 SBOM standard
- CycloneDX: OWASP SBOM standard optimized for security use cases
- SWID (Software Identification Tags): ISO/IEC 19770-2 software identification
- Syft: SBOM generation tool supporting SPDX and CycloneDX
- Trivy: Security scanner with SBOM generation capabilities

**Provenance Generation Tools**:
- GitHub Actions Attestations: Native SLSA provenance generation in GitHub Actions
- GitLab Attestations: Built-in provenance for GitLab CI/CD
- SLSA Generators: Reference implementations for SLSA provenance (slsa-github-generator)
- Tekton Chains: Kubernetes-native provenance for Tekton Pipelines
- witness: in-toto attestation framework for CI/CD pipelines

**SLSA Levels & Requirements**:
- SLSA Level 1: Build provenance exists (documented build process)
- SLSA Level 2: Hosted build platform, signed provenance (GitHub Actions, GitLab CI)
- SLSA Level 3: Hardened build platform, non-falsifiable provenance (isolated build)
- SLSA Level 4: Two-party review, hermetic builds (reproducible, maximum security)

**Regulatory & Compliance**:
- Executive Order 14028 (US): Improving the Nation's Cybersecurity (SBOM requirement for federal software)
- EU Cyber Resilience Act: Software supply chain security and SBOM requirements
- NIST Cybersecurity Framework: Supply chain risk management (SC.GRC, SC.RA)
- FedRAMP Requirements: Software supply chain controls for cloud services
- PCI DSS 4.0: Requirement 6.3 (secure software development lifecycle)

**Vulnerability Disclosure**:
- VEX (Vulnerability Exploitability eXchange): Machine-readable vulnerability impact statements
- CVE (Common Vulnerabilities and Exposures): Vulnerability identification system
- OSV (Open Source Vulnerabilities): Vulnerability database for open source
- CVSS v3.1/v4.0: Common Vulnerability Scoring System
- EPSS (Exploit Prediction Scoring System): Probability of vulnerability exploitation

**Cryptographic Standards**:
- X.509 Certificates: Public key infrastructure for code signing
- PGP/GPG: Traditional artifact signing (less common, being replaced by Sigstore)
- Keyless Signing: Ephemeral certificates via OIDC (Fulcio) eliminating key management
- Certificate Transparency: Public append-only logs for certificate issuance (Rekor model)
- Notary v2: OCI artifact signing and verification specification

**Container Image Security**:
- OCI (Open Container Initiative): Container image and distribution specifications
- Container Image Signing: Cosign signatures for Docker/OCI images
- Container Registry: Harbor, Artifactory, GHCR with signature verification
- Admission Controllers: Kyverno, OPA Gatekeeper, Sigstore Policy Controller for verification
- Image Provenance: SLSA provenance for container builds (source, builder, materials)

**CI/CD Integration**:
- GitHub Actions: Native provenance generation and artifact attestations
- GitLab CI/CD: Integrated provenance and signing workflows
- Jenkins: Provenance plugins (SLSA plugin, in-toto integration)
- Tekton: Chains for automatic SLSA provenance generation
- CircleCI, Travis CI: Third-party provenance generation tools

**Build Reproducibility**:
- Reproducible Builds: Bit-for-bit identical artifacts from source (hermetic builds)
- Build Environment Capture: Record build tool versions, OS, dependencies
- Dependency Pinning: Lock files for exact dependency versions
- Hermetic Build Systems: Bazel, Nix for deterministic builds

**Artifact Types Requiring Provenance**:
- Container Images: Docker, OCI images deployed to Kubernetes
- Binary Executables: CLI tools, services, applications
- Software Packages: npm, PyPI, Maven, NuGet packages
- Release Archives: tar.gz, zip files with application code
- AI/ML Models: Model weights, training data references, model cards
- Infrastructure as Code: Terraform modules, Helm charts, Kubernetes manifests

**Provenance Verification**:
- Policy-as-Code: OPA Rego policies for provenance verification
- Admission Control: Kubernetes admission webhooks rejecting unsigned images
- Supply Chain Policy: Automated policy enforcement (Sigstore Policy Controller, Kyverno)
- Attestation Storage: OCI registries, artifact stores with attestation support

**Reference**: Consult security engineering, DevSecOps, and compliance teams for detailed guidance on provenance attestation implementation and verification requirements

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
