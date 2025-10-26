# Name: attribution-files

## Executive Summary

Attribution Files (NOTICE, LICENSE, THIRD-PARTY-NOTICES) are legal documents bundled with software distributions that acknowledge open-source components, copyright holders, and license obligations. These files satisfy Apache License 2.0 Section 4(d) NOTICE requirements, GPL attribution clauses, and general copyright law obligations to preserve author credit and license text. Attribution files prevent copyright infringement claims by providing evidence of license compliance and proper credit to original authors.

Modern attribution management uses automated tools (FOSSA, Black Duck, license-maven-plugin, CycloneDX) to generate attribution files from SBOM and license scan data, ensuring accuracy across hundreds of dependencies. Organizations must distinguish between LICENSE files (verbatim license text for the project itself), NOTICE files (third-party attributions required by Apache 2.0 and similar licenses), and THIRD-PARTY-NOTICES files (comprehensive attribution for all dependencies). Attribution completeness is increasingly scrutinized in M&A due diligence, enterprise procurement, and open-source license audits.

### Strategic Importance

- **License Compliance**: Satisfies Apache 2.0, MIT, BSD license attribution requirements preventing copyright infringement and license breach
- **Copyright Preservation**: Maintains legal chain of attribution from original authors through derivative works and commercial distributions
- **Audit Defense**: Provides documentary evidence of license compliance for OpenChain certification, customer audits, and litigation discovery
- **Transparency**: Demonstrates respect for open-source authors and adherence to community norms building ecosystem trust
- **REUSE Specification**: Supports REUSE 3.0 compliance for machine-readable copyright and licensing information in source files
- **M&A Due Diligence**: Accelerates IP verification by documenting all third-party code attributions and license obligations
- **Customer Requirements**: Satisfies enterprise buyer policies requiring full third-party component disclosure and attribution documentation

## Purpose & Scope

### Primary Purpose

This artifact documents all copyright notices, license texts, and attribution statements for third-party open-source components included in software distributions. It ensures compliance with license attribution clauses (Apache 2.0 Section 4, MIT/BSD copyright preservation, GPL copyright notices) by providing complete, accurate credit to original authors and copyright holders as required by respective licenses.

### Scope

**In Scope**:
- LICENSE file: Full verbatim license text for the project's own code and licensing terms
- NOTICE file: Apache-style attribution per Section 4(d), trademark disclaimers, patent notices, required attributions
- THIRD-PARTY-NOTICES / CREDITS file: Comprehensive list of dependencies with copyright holders, licenses, and required attribution text
- Copyright headers: SPDX-FileCopyrightText and SPDX-License-Identifier in source files per REUSE specification
- Attribution text format: component name, version, copyright holders, license type, license text or URL
- Automated generation: Integration with FOSSA, Black Duck, license-maven-plugin, npm-license-crawler, pip-licenses
- Binary distribution attribution: Including attribution in "About" dialogs, help screens, or documentation for GUI applications
- Container image attribution: Embedding attribution files in container metadata or /usr/share/doc locations
- Attribution for modified code: Documenting changes per license requirements (GPL Section 5(a), Apache Section 4(b))

**Out of Scope**:
- Detailed legal analysis of license compatibility (covered by License BOM)
- Source code disclosure obligations for GPL/LGPL (separate compliance process)
- Patent grant analysis beyond what's stated in NOTICE files
- Contributor License Agreements (separate CLA artifact)
- Commercial software EULA terms

### Target Audience

**Primary Audience**:
- Legal Counsel: Verifying attribution completeness, license compliance validation, audit defense preparation
- Compliance Officers: OpenChain certification, customer audit responses, policy enforcement
- Open Source Program Office (OSPO): Attribution automation, license compliance workflows, SBOM-to-attribution synchronization
- Release Engineers: Automated attribution file generation in CI/CD, distribution packaging, container image builds

**Secondary Audience**:
- End Users/Customers: Reviewing third-party components and licenses in products they deploy
- Security Teams: Correlating attributions with vulnerability disclosures, verifying component provenance
- Product Management: Understanding third-party dependencies for customer disclosures and competitive analysis
- M&A Due Diligence: Validating IP chain-of-title and attribution accuracy during acquisitions

## Document Information

**Format**: Markdown

**File Pattern**: `*.attribution-files.md`

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

**Automated Generation**: Generate attribution files automatically from SBOM/license scans using FOSSA, Black Duck, or language-specific tools
**CI/CD Integration**: Regenerate attribution files on every build to ensure accuracy as dependencies change
**Root Directory Placement**: Place LICENSE, NOTICE, THIRD-PARTY-NOTICES in repository root for discoverability and compliance
**Verbatim License Text**: Include full license text verbatim; some licenses (Apache 2.0) explicitly require unmodified license text
**Copyright Holder Accuracy**: Extract copyright holders from source file headers, not package metadata (which may be incomplete)
**Attribution Grouping**: Group components by license type for readability (all MIT components, then Apache 2.0, then BSD, etc.)
**SPDX Identifiers**: Use SPDX license identifiers in attribution for machine readability and standardization
**Transitive Dependencies**: Include transitive dependencies in attribution, not just direct dependencies (licenses cascade through dep tree)
**Binary Distribution Inclusion**: Embed attribution files in binary distributions, container images, executables (not just source releases)
**GUI Attribution**: For GUI applications, provide "About" dialog or menu item showing third-party licenses and attributions
**Web Application Display**: For web apps, link to /licenses or /attributions page from footer or settings
**Modification Notices**: When modifying open-source code, add modification notices per GPL Section 5(a) and Apache Section 4(b)
**NOTICE File Specificity**: Apache NOTICE should contain only required attributions, not general credits or advertising (per ASF policy)
**License Text URLs**: Include URLs to license texts for long licenses (GPL, LGPL) to avoid 1000+ line LICENSE files
**Archival Copies**: Maintain local copies of license texts; upstream URLs may change or disappear over time
**Version-Specific Attribution**: Generate separate attribution files for each release version; dependencies change between versions
**Container Layer Attribution**: For container images, document attribution per layer or provide aggregate attribution in final image
**REUSE Compliance**: Adopt REUSE 3.0 with SPDX headers in source files for machine-readable attribution at file level
**Validation Testing**: Run reuse-tool lint or license compliance validators in CI to detect missing attributions before release
**Legal Review Workflow**: Have legal counsel spot-check attribution completeness quarterly or before major releases

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

**License Attribution Requirements**:
- Apache License 2.0 Section 4(d) (NOTICE file requirements, attribution preservation)
- MIT License (copyright notice preservation in distributions)
- BSD Licenses (copyright notice, conditions list, disclaimer preservation)
- GPL v2/v3 Section 5 (copyright notices, license text, modification notices)
- MPL 2.0 Section 3.3 (attribution notice requirements)
- CC-BY licenses (Creative Commons attribution for non-code assets)

**REUSE Specification**:
- REUSE Software 3.0 (machine-readable copyright and licensing in source files)
- SPDX-FileCopyrightText tag for copyright holders
- SPDX-License-Identifier tag for license identification
- DEP5 (Debian copyright format) for bulk file licensing
- reuse-tool for automated REUSE compliance validation

**Copyright Law Frameworks**:
- Berne Convention Article 5 (copyright notice not required but preserving author attribution protects moral rights)
- 17 USC 401 (copyright notice format: © [year] [owner])
- WIPO Copyright Treaty protection of author attribution rights

**Automated Attribution Tools**:
- FOSSA (automated attribution file generation from dependency scanning)
- Black Duck (attribution report generation, NOTICE file creation)
- FOSSology (license and copyright extraction for attribution)
- license-maven-plugin (Maven plugin for THIRD-PARTY.txt generation)
- npm-license-crawler (Node.js dependency license extraction)
- pip-licenses (Python package license listing)
- cargo-about (Rust dependency attribution generation)
- go-licenses (Go module license extraction)
- license-checker (npm package for license audit and attribution)

**Attribution File Formats**:
- Plain text NOTICE/LICENSE files (most common, human-readable)
- Markdown THIRD-PARTY-NOTICES.md for formatted attribution
- HTML attributions.html for web-based software About pages
- JSON/XML structured attribution for programmatic processing
- SPDX Document as comprehensive attribution + license data
- CycloneDX BOM with license and copyright metadata

**Apache Software Foundation Standards**:
- Apache NOTICE file requirements (ASF policy for trademark, patent, attribution notices)
- Apache LICENSE file format (project license with appendix for dependency attributions)
- Apache license headers in source files (SPDX-License-Identifier preferred)

**Industry Best Practices**:
- OpenChain ISO/IEC 5230 Section 3.3.2 (attribution documentation requirements)
- Linux Foundation SPDX Lite profile for minimal attribution data
- TODO Group attribution guidance for open-source programs
- CHAOSS Project metrics for attribution completeness

**GPL Specific Requirements**:
- GPL Section 1 "Appropriate Legal Notices" preservation
- GPL Section 5(a) modification notices in changed files
- GPL Section 7 additional permissions preservation
- LGPL Section 4(d) combined work attribution requirements

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
