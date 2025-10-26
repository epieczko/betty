# Name: open-source-license-bom

## Executive Summary

The Open Source License Bill of Materials (BOM) is a critical legal compliance artifact that catalogs all open-source software components, their licenses, and usage terms within an application or product. This artifact enables organizations to ensure OSI-approved license compliance, prevent copyleft contamination in proprietary codebases, and meet supply chain transparency requirements mandated by customers and regulators.

In an era where modern applications integrate hundreds of open-source dependencies, automated license detection tools like FOSSA, Black Duck, Snyk, WhiteSource Bolt, and Scancode Toolkit have become essential for continuous compliance monitoring. Organizations must navigate complex license compatibility matrices—understanding the distinctions between permissive licenses (MIT, Apache 2.0, BSD), weak copyleft (LGPL, MPL 2.0), and strong copyleft (GPL v2/v3, AGPL)—to avoid inadvertent IP exposure and legal liability.

### Strategic Importance

- **License Compliance**: Prevents GPL violations, ensures Apache 2.0/MIT compatibility, and manages copyleft obligations across supply chain
- **Legal Risk Mitigation**: Identifies license conflicts before product release, avoiding costly litigation and forced source code disclosure
- **M&A Due Diligence**: Provides clean IP inventory for acquisitions, demonstrating compliance posture to investors and acquirers
- **Customer Requirements**: Satisfies enterprise procurement policies requiring OSS license disclosure and FOSS transparency
- **OpenChain Certification**: Supports ISO/IEC 5230:2020 compliance for organizations seeking open-source program office maturity
- **Supply Chain Security**: Complements SBOM for comprehensive software composition analysis integrating license and vulnerability data
- **Regulatory Alignment**: Demonstrates FOSS governance for industries with strict IP controls (financial services, healthcare, defense)

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative inventory of all OSI-approved open-source licenses detected in software components, enabling legal counsel and compliance teams to assess license compatibility, identify copyleft obligations, and ensure GPL/LGPL compliance. It documents license types (permissive vs. copyleft), license text locations, copyright holders, and usage context to support informed decisions about component integration, derivative work creation, and source code disclosure obligations.

### Scope

**In Scope**:
- Direct and transitive dependency license identification across package managers (npm, Maven, PyPI, RubyGems, NuGet)
- OSI-approved license classification: MIT, Apache 2.0, BSD (2-Clause/3-Clause), GPL v2/v3, LGPL v2.1/v3, MPL 2.0, EPL 2.0
- License compatibility analysis: permissive-to-copyleft mixing, GPL compatibility matrix, dual-licensing scenarios
- Copyleft obligation tracking: strong copyleft (GPL, AGPL) vs. weak copyleft (LGPL, MPL) boundary analysis
- License expression parsing using SPDX license identifiers and compound expressions (AND, OR, WITH operators)
- Custom/proprietary license detection requiring manual legal review
- License conflict identification: GPL-incompatible combinations, commercial license restrictions

**Out of Scope**:
- Vulnerability data and CVE tracking (covered by Software Bill of Materials with VEX)
- Patent grant analysis (handled by separate patent risk assessment)
- Export control classifications (ECCN) for cryptographic libraries
- Commercial software license management and enterprise license agreements
- Contributor provenance and Developer Certificate of Origin tracking (covered by CLA artifact)

### Target Audience

**Primary Audience**:
- Legal Counsel: License compatibility review, IP risk assessment, GPL obligation analysis
- Open Source Program Office (OSPO): Policy enforcement, license approval workflows, OpenChain compliance
- Compliance Officers: Audit readiness, regulatory reporting, customer license disclosure requirements
- Security Engineers: Integration with SCA tools, policy-as-code enforcement, CI/CD license gates

**Secondary Audience**:
- Engineering Leadership: Risk-based component selection, technical debt from license conflicts
- M&A Due Diligence Teams: IP portfolio assessment, clean-room validation, license liability quantification
- Product Management: Customer licensing questions, open-source strategy, competitive licensing analysis
- Procurement: Vendor OSS policies, third-party component evaluation, contract license terms

## Document Information

**Format**: Markdown

**File Pattern**: `*.open-source-license-bom.md`

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

**Automated License Detection**: Integrate FOSSA, Snyk, or Black Duck into CI/CD pipelines for continuous license scanning on every build
**SPDX Identifier Usage**: Use standardized SPDX license identifiers in package metadata and source file headers for machine readability
**Transitive Dependency Analysis**: Scan full dependency trees (not just direct dependencies) as transitive dependencies inherit license obligations
**License Policy Enforcement**: Define approved/denied license lists in tools; fail builds on GPL detection in proprietary codebases
**Manual Review Queue**: Establish legal review workflow for non-standard licenses, dual licenses, and license exceptions
**GPL Isolation Strategy**: Containerize or service-wrap GPL components to maintain license boundary separation from proprietary code
**License Compatibility Matrix**: Maintain organizational matrix documenting approved license combinations and prohibited mixtures
**NOTICE File Generation**: Auto-generate NOTICE/LICENSE files with all third-party attributions for distribution with products
**License Change Monitoring**: Track upstream license changes in dependencies; major version updates may introduce license changes
**OpenChain Process Compliance**: Document license review workflows, maintain training records, and assign OSPO accountability per ISO/IEC 5230
**Dual-License Evaluation**: When components offer dual licensing (e.g., GPL + Commercial), document election and procurement of commercial licenses
**Copyleft Boundary Testing**: Validate that LGPL/MPL weak copyleft boundaries are maintained through dynamic linking or separate processes
**Version Control**: Store license BOMs in Git alongside source code with automated generation on release branches
**Quarterly License Audits**: Schedule regular compliance reviews even without code changes, as tools improve detection over time
**M&A Preparation**: Maintain clean, up-to-date license inventory as standard practice to accelerate due diligence processes
**Customer Disclosure**: Prepare customer-facing license disclosures using SPDX or CycloneDX formats for transparency
**Patent Grant Analysis**: For Apache 2.0 components, document patent grant implications and contributor patent licensing
**Export Control Awareness**: Flag cryptographic libraries requiring export compliance (OpenSSL, BouncyCastle) for ECCN classification
**License Text Preservation**: Maintain copies of actual license texts as URLs may change; use SPDX LicenseRef for custom licenses
**Training & Awareness**: Provide developer training on license implications of package selection and GPL contamination risks

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

**OSI License Standards**:
- Open Source Initiative (OSI) Approved Licenses (100+ licenses)
- SPDX License List 3.21+ (standardized license identifiers)
- SPDX License Expression syntax (compound licenses with AND/OR/WITH operators)
- Creative Commons licenses (CC0, CC-BY, CC-BY-SA for documentation/assets)

**Permissive Licenses**:
- MIT License (most permissive, minimal restrictions)
- Apache License 2.0 (patent grant, trademark restrictions)
- BSD 2-Clause License (FreeBSD license)
- BSD 3-Clause License (includes non-endorsement clause)
- ISC License (functionally equivalent to MIT)
- Unlicense (public domain dedication)

**Weak Copyleft Licenses**:
- GNU Lesser General Public License (LGPL) v2.1 and v3.0 (library linking exception)
- Mozilla Public License (MPL) 2.0 (file-level copyleft)
- Eclipse Public License (EPL) 1.0 and 2.0
- Common Development and Distribution License (CDDL) 1.0
- European Union Public License (EUPL) 1.2

**Strong Copyleft Licenses**:
- GNU General Public License (GPL) v2.0 (no compatibility with v3)
- GNU General Public License (GPL) v3.0 (enhanced patent protection)
- GNU Affero General Public License (AGPL) v3.0 (network copyleft trigger)
- Open Software License (OSL) 3.0
- European Union Public License (EUPL) with copyleft provisions

**License Compatibility Frameworks**:
- GPL Compatibility Matrix (FSF-maintained compatibility guidance)
- Apache Software Foundation License Compatibility Policy
- Copyleft vs. Permissive Mixing Rules
- Dual-Licensing Strategies (GPL + Commercial, MPL + Secondary License)
- License Stacking Analysis (multiple licenses in dependency chain)

**Compliance Standards**:
- OpenChain ISO/IEC 5230:2020 (open-source compliance program specification)
- OpenChain ISO/IEC 18974:2023 (security assurance for open source)
- REUSE Software Specification 3.0 (licensing best practices, copyright/license headers)
- Linux Foundation SPDX Specification 2.3 (machine-readable license data)
- ClearlyDefined Project (community-curated licensing metadata)

**Scanning & Analysis Tools**:
- FOSSA (license compliance automation, policy enforcement)
- Black Duck by Synopsys (enterprise SCA with license risk scoring)
- Snyk Open Source (license policy violations in CI/CD)
- WhiteSource Bolt/Mend (real-time license compliance monitoring)
- Scancode Toolkit (open-source license detection engine)
- FOSSology (license scanning and clearing workflow)
- licensee (GitHub's Ruby-based license detector)
- SPDX Tools (SPDX document creation and validation)
- ORT (OSS Review Toolkit by OSS Review Toolkit contributors)
- Trivy (license scanning alongside vulnerability detection)

**Industry Standards**:
- NTIA SBOM Minimum Elements (license as required field in SBOM)
- Linux Foundation OpenSSF Best Practices Badge (FOSS project licensing clarity)
- TODO Group Open Source Guides (corporate OSPO frameworks)
- CHAOSS Project Metrics (community health analytics including licensing)

**Legal & Regulatory**:
- U.S. Copyright Office Regulations (copyright notice requirements)
- EU Copyright Directive Article 17 (platform liability for user uploads)
- Open Source License Litigation Precedents (Artifex v. Hancom, GPL enforcement cases)
- Export Administration Regulations (EAR) for cryptographic OSS

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
