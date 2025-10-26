# Name: software-bill-of-materials

## Executive Summary

The Software Bill of Materials (SBOM) is a machine-readable inventory documenting all software components, dependencies, licenses, and metadata within an application or system. Mandated by Executive Order 14028 for federal software procurement, SBOMs have become the foundation of supply chain security, vulnerability management, and software transparency. Organizations must generate SBOMs in industry-standard formats (SPDX 2.3, CycloneDX 1.4+, SWID tags) that meet NTIA minimum elements requirements.

Modern software composition includes hundreds of open-source dependencies, transitive dependencies, and third-party libraries—creating blind spots for vulnerability response and license compliance. Automated SBOM generation tools like Syft, CycloneDX generators, SPDX Tools, and Tern integrate into CI/CD pipelines to maintain continuous inventory accuracy. When paired with Vulnerability Exploitability eXchange (VEX) documents, SBOMs enable rapid triage of disclosed vulnerabilities like Log4Shell by instantly identifying affected products and versions across portfolios.

### Strategic Importance

- **Executive Order 14028 Compliance**: Federal agencies require SBOM delivery for all software purchases per May 2021 cybersecurity executive order
- **Vulnerability Response**: Enables 4-hour response to disclosed CVEs by instantly identifying affected products containing vulnerable components
- **Supply Chain Security**: Provides transparency into software composition, preventing adversarial code injection and malicious dependencies
- **License Compliance**: Integrates with license BOM for comprehensive open-source governance and GPL obligation management
- **M&A Due Diligence**: Accelerates technical due diligence with complete software composition inventory and dependency analysis
- **NIST SSDF Alignment**: Satisfies NIST SP 800-218 Secure Software Development Framework requirement for software transparency
- **Customer Requirements**: Meets growing enterprise and government procurement demands for SBOM attestation and software supply chain visibility

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative, machine-readable inventory of all software components (libraries, frameworks, dependencies, packages) comprising a software product. It enables rapid vulnerability identification, license compliance verification, and supply chain risk assessment by documenting component names, versions, suppliers, dependency relationships, and cryptographic hashes in standardized formats (SPDX 2.3, CycloneDX 1.4+) meeting NTIA minimum elements.

### Scope

**In Scope**:
- Component inventory with Package URLs (PURLs) and Common Platform Enumeration (CPE) identifiers
- Dependency graph mapping (direct dependencies, transitive dependencies, dependency depth)
- NTIA minimum elements: supplier name, component name, version, unique identifiers, dependency relationships, SBOM author, timestamp
- SPDX 2.3 format generation (RDF, JSON, YAML, tag-value) with SPDX license expressions
- CycloneDX 1.4+ format generation (JSON, XML) with component type classifications (library, framework, application, container)
- SWID tags for installed software inventory (ISO/IEC 19770-2:2015 compliance)
- Cryptographic hashes (SHA-256, SHA-512) for component integrity verification
- VEX (Vulnerability Exploitability eXchange) integration for vulnerability status communication
- Container image layer analysis and base image SBOM composition
- Firmware and embedded system component tracking

**Out of Scope**:
- Detailed license legal analysis and GPL compatibility assessment (covered by License BOM)
- Vulnerability remediation guidance and patch prioritization (handled by vulnerability management process)
- Runtime behavior monitoring and dynamic component discovery
- Infrastructure-as-Code (IaC) and cloud service dependencies (covered by separate cloud asset inventory)
- Malware signatures and adversarial code detection (handled by security scanning tools)

### Target Audience

**Primary Audience**:
- Security Engineers: Vulnerability mapping, incident response, CVE-to-product correlation, zero-day triage
- DevOps/Platform Teams: CI/CD SBOM generation, artifact signing, SBOM distribution, automation workflows
- Compliance Officers: Executive Order 14028 attestation, NIST SSDF compliance, customer SBOM delivery requirements
- Open Source Program Office (OSPO): Component tracking, license-to-SBOM correlation, supply chain policy enforcement

**Secondary Audience**:
- Legal Counsel: Component provenance verification, supply chain liability assessment, contractual SBOM obligations
- Procurement: Vendor SBOM requirements, third-party software evaluation, supplier security questionnaires
- Product Security Incident Response Team (PSIRT): Vulnerability disclosure response, customer notification, affected product identification
- Risk Management: Supply chain risk quantification, single points of failure analysis, critical component assessment

## Document Information

**Format**: JSON

**File Pattern**: `*.software-bill-of-materials.json`

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

**Automated Generation**: Generate SBOMs automatically in CI/CD pipelines using Syft, CycloneDX plugins, or SPDX tools on every build
**NTIA Minimum Elements**: Ensure all SBOMs include required fields: supplier, component name, version, unique identifiers, dependency relationships, timestamp, SBOM author
**Multi-Format Support**: Generate both SPDX 2.3 (for government/standards) and CycloneDX 1.4+ (for security tooling) formats
**Cryptographic Signing**: Sign SBOMs with Sigstore/Cosign and publish signatures to Rekor transparency log for attestation
**SBOM-per-Artifact**: Generate separate SBOMs for each release artifact, container image, and firmware build
**Transitive Dependencies**: Include full dependency tree, not just direct dependencies; vulnerabilities hide in transitive deps
**VEX Integration**: Pair SBOMs with VEX documents to communicate vulnerability status (affected, not affected, fixed, under investigation)
**PURL and CPE**: Include Package URLs for component identification and CPE identifiers for NVD vulnerability correlation
**Version Pinning**: Document exact versions with commit hashes/build IDs, not version ranges, for reproducibility
**SBOM Distribution**: Host SBOMs at standardized URIs (e.g., /.well-known/sbom) or embed in container image metadata
**Continuous Monitoring**: Import SBOMs into Dependency-Track or similar platforms for continuous vulnerability monitoring
**Build Provenance**: Link SBOMs to SLSA provenance attestations documenting build environment integrity
**Container Layer Analysis**: For container images, document SBOM for each layer and base image composition
**SBOM Validation**: Validate SBOM syntax and completeness using SPDX validator or CycloneDX schema validation
**Historical SBOMs**: Archive SBOMs for all released versions to enable vulnerability retrospective analysis
**Customer Delivery**: Establish process for delivering SBOMs to customers upon request (automated portal preferred)
**Vulnerability Correlation**: Test SBOM quality by correlating components with NVD/OSV to validate CPE/PURL mapping
**Nested SBOMs**: For multi-repo projects, generate component SBOMs and assemble hierarchical SBOM relationships
**License Integration**: Cross-reference SBOM with license BOM to ensure consistent component identification
**SBOM Diff Analysis**: Compare SBOMs across versions to identify new/removed/updated components for change review
**Tool Diversity**: Use multiple SBOM generation tools and reconcile results to improve component detection accuracy

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

**SBOM Format Standards**:
- SPDX (Software Package Data Exchange) 2.3 (Linux Foundation, ISO/IEC 5962:2021)
- CycloneDX 1.4+ and 1.5 (OWASP, ECMA-424 standard)
- SWID Tags (Software Identification Tags) ISO/IEC 19770-2:2015
- Package URL (PURL) specification for universal component identifiers
- Common Platform Enumeration (CPE) 2.3 for vulnerability correlation

**U.S. Government Requirements**:
- Executive Order 14028 (Improving the Nation's Cybersecurity) May 2021
- NIST SP 800-218 Secure Software Development Framework (SSDF)
- NTIA Minimum Elements for Software Bill of Materials (July 2021)
- CISA Vulnerability Exploitability eXchange (VEX) specification
- OMB M-22-18 Memorandum (Enhancing Software Supply Chain Security)
- NIST SSDF Practice PW.1.3 (Create and maintain SBOM)

**SBOM Generation Tools**:
- Syft (Anchore, popular open-source SBOM generator)
- CycloneDX Maven/Gradle/npm/Python plugins
- SPDX sbom-tool (Microsoft, multi-language support)
- Tern (VMware, container image SBOM generation)
- Scancode Toolkit (AboutCode, deep package analysis)
- Trivy SBOM mode (Aqua Security, container-focused)
- Grype (Anchore, SBOM-based vulnerability scanning)
- OSS Review Toolkit (ORT) SBOM generation
- WhiteSource/Mend SBOM export
- Snyk SBOM export functionality

**VEX (Vulnerability Exploitability eXchange)**:
- CISA VEX specification for vulnerability status communication
- OpenVEX (open-source VEX implementation)
- CycloneDX VEX BOM format
- CSAF (Common Security Advisory Framework) 2.0 VEX profile
- VEX Status Values: Not Affected, Affected, Fixed, Under Investigation

**Vulnerability Databases**:
- National Vulnerability Database (NVD) with CPE/CVE correlation
- OSV (Open Source Vulnerabilities) database schema
- GitHub Advisory Database
- Snyk Vulnerability Database
- CISA Known Exploited Vulnerabilities (KEV) catalog

**Supply Chain Security Frameworks**:
- NIST Cybersecurity Supply Chain Risk Management (C-SCRM)
- SLSA (Supply-chain Levels for Software Artifacts) Framework Levels 1-4
- in-toto Framework for supply chain integrity attestation
- Sigstore for artifact signing (Cosign, Rekor, Fulcio)
- The Update Framework (TUF) for secure software updates
- SCVS (Software Component Verification Standard) by OWASP

**Industry Standards & Initiatives**:
- OpenSSF (Open Source Security Foundation) SBOM Everywhere initiative
- Linux Foundation SPDX project and SPDX Lite profile
- OWASP CycloneDX community and tools ecosystem
- CISA SBOM-a-rama events and SBOM sharing initiatives
- NTIA Framing Working Group (Software Transparency)
- SPDX Security Team vulnerability profile development

**Compliance & Attestation**:
- SLSA Provenance for build attestation
- in-toto Layout and Link metadata for supply chain verification
- Sigstore Rekor transparency log for artifact signatures
- NIST SP 800-161 Cybersecurity Supply Chain Risk Management
- ISO/IEC 27036 Cybersecurity for Supplier Relationships

**Dependency Management**:
- Dependency-Track (OWASP, SBOM ingestion and vulnerability monitoring)
- DependencyCheck (OWASP, identify known vulnerable components)
- Renovate/Dependabot for automated dependency updates
- NPM audit, Maven dependency:tree, pip-audit for package analysis
- Software Heritage Archive for source code archival

**Container & Cloud Native**:
- OCI (Open Container Initiative) image specification
- Docker SBOM generation (docker sbom command)
- Kubernetes SBOM generation for clusters
- Cloud Native Security Whitepaper (CNCF)
- SPIFFE/SPIRE for workload identity attestation

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
