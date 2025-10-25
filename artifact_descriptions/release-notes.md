# Name: release-notes

## Executive Summary

The Release Notes artifact is a critical communication deliverable that documents changes, improvements, and breaking modifications introduced in each software release version. Following Semantic Versioning 2.0.0 principles and Keep a Changelog format standards, release notes serve as the primary interface between engineering teams and stakeholders, enabling informed adoption decisions and smooth upgrade paths.

In modern DevOps and continuous delivery environments, release notes bridge technical implementation details with business value communication. They support SemVer-compliant versioning strategies (MAJOR.MINOR.PATCH), document Conventional Commits-aligned changes, and provide migration guidance for breaking changes. Release notes enable customer success teams, internal operations, and end users to understand what changed, why it matters, and what actions they need to take.

### Strategic Importance

- **Version Transparency**: Provides clear communication of changes aligned with Semantic Versioning 2.0.0 (MAJOR for breaking changes, MINOR for features, PATCH for fixes)
- **Adoption Enablement**: Facilitates safe upgrades by documenting breaking changes, deprecations, and migration paths
- **Compliance Documentation**: Supports audit trails for SOC 2, ISO 27001, and regulatory change tracking requirements
- **Customer Communication**: Enables product marketing, customer success, and support teams to communicate value to users
- **Change Traceability**: Links releases to feature requests, bug fixes, security patches, and technical debt reduction
- **Risk Mitigation**: Identifies breaking changes, known issues, rollback procedures, and compatibility requirements
- **Automation Integration**: Supports automated release note generation via conventional-changelog, semantic-release, and GitVersion tools

## Purpose & Scope

### Primary Purpose

Release notes communicate what changed in each software version using Keep a Changelog format, enabling stakeholders to understand new features, bug fixes, breaking changes, deprecations, security patches, and required migration actions. They follow Semantic Versioning 2.0.0 conventions and support Conventional Commits standards (feat:, fix:, BREAKING CHANGE:, chore:, docs:, refactor:, perf:, test:).

### Scope

**In Scope**:
- Version identification following SemVer 2.0.0 (MAJOR.MINOR.PATCH, e.g., 2.3.1)
- Release date and Git tag/commit references
- Added features (MINOR version bumps), bug fixes (PATCH bumps), breaking changes (MAJOR bumps)
- Deprecated functionality with sunset timelines and migration guidance
- Security patches with CVE references, severity ratings (Critical/High/Medium/Low)
- Known issues, limitations, and workarounds
- Migration instructions for breaking changes with code examples
- Dependency updates, API changes, configuration modifications
- Performance improvements with benchmark data
- Backward compatibility statements and supported upgrade paths
- Links to detailed documentation, GitHub issues, pull requests

**Out of Scope**:
- Internal development process details (handled by changelogs.md)
- Complete change history across all versions (use CHANGELOG.md)
- Technical architecture decisions (handled by ADRs)
- Deployment procedures and runbooks (handled by deployment documentation)
- Release certification and readiness criteria (handled by release-certification.md)

### Target Audience

**Primary Audience**:
- Release Managers evaluating release readiness and coordinating deployments
- DevOps Engineers planning deployment windows and rollback strategies
- Software Engineers consuming libraries/services and planning integrations
- Product Managers communicating value to customers and internal stakeholders
- Customer Success Teams advising clients on upgrade timing and migration

**Secondary Audience**:
- SRE Teams assessing operational impact and monitoring requirements
- Security Teams tracking vulnerability remediation and compliance requirements
- QA Teams developing test plans for new features and regression testing
- Technical Writers updating documentation for new features
- End Users understanding new capabilities and required actions

## Document Information

**Format**: Markdown

**File Pattern**: `*.release-notes.md`

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

**Semantic Versioning Compliance**: Strictly follow SemVer 2.0.0 - MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for backward-compatible fixes
**Keep a Changelog Format**: Use standardized sections (Added, Changed, Deprecated, Removed, Fixed, Security) for consistency
**Breaking Change Prominence**: Clearly highlight breaking changes at the top with BREAKING CHANGE: prefix and migration guides
**Conventional Commits Alignment**: Generate release notes from Conventional Commits (feat:, fix:, chore:, docs:, refactor:, perf:, test:)
**Automation**: Use semantic-release, conventional-changelog, or release-please for automated generation from git history
**Migration Guidance**: Provide step-by-step migration instructions with code examples for breaking changes
**Security Transparency**: Document security fixes with CVE numbers, severity ratings, and affected versions
**Deprecation Warnings**: Announce deprecations at least 1-2 MINOR versions before removal with sunset dates
**Link to Details**: Reference GitHub issues, pull requests, commit SHAs, and detailed documentation
**Customer-Focused Language**: Write for end users, not just developers - explain business value and user impact
**Upgrade Path Testing**: Validate upgrade paths from previous versions before publishing release notes
**Pre-Release Communication**: Use alpha, beta, rc (release candidate) suffixes for pre-production releases
**Git Tag Consistency**: Ensure release notes match git tags (v1.2.3) and container image tags
**Distribution Channels**: Publish to GitHub Releases, GitLab Releases, documentation site, and email notifications
**Rollback Documentation**: Include rollback procedures and known rollback limitations
**Performance Impact**: Document performance improvements or regressions with benchmark data
**Dependency Changes**: List major dependency updates that may affect consumers
**API Change Documentation**: Use OpenAPI/Swagger diff tools to detect and document API changes
**Compatibility Matrix**: Provide version compatibility information for dependencies and platforms
**Release Cadence Consistency**: Maintain predictable release schedules (weekly, biweekly, monthly) for stakeholder planning

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

**Version Control & Semantic Versioning**:
- Semantic Versioning 2.0.0 (SemVer) - MAJOR.MINOR.PATCH versioning standard
- Keep a Changelog - Standardized changelog format (Added, Changed, Deprecated, Removed, Fixed, Security)
- Calendar Versioning (CalVer) - Alternative versioning for time-based releases
- Git Tags - Annotated tags for version tracking (v1.2.3, v2.0.0-rc.1)
- Pre-release versioning - Alpha, beta, release candidate conventions

**Commit Standards & Automation**:
- Conventional Commits - Structured commit messages (feat:, fix:, BREAKING CHANGE:, chore:)
- conventional-changelog - Automated changelog generation from git commits
- semantic-release - Automated versioning and release note generation
- GitVersion - Automatic SemVer version calculation from git history
- standard-version - Automated versioning and CHANGELOG generation
- auto - Generate releases based on semantic version labels
- release-please - Automated release PRs with generated changelogs

**Release Management Frameworks**:
- ITIL 4 Service Transition - Release and deployment management practices
- ITIL 4 Release Management - Guidance for release planning and execution
- SAFe Release Management - Agile release trains and PI planning
- GitFlow - Git branching model for release management
- GitHub Flow - Simplified release workflow via main branch deployments
- Trunk-Based Development - Continuous integration and release from main

**Change Documentation Standards**:
- ISO/IEC/IEEE 29148 - Requirements engineering and change documentation
- RFC 2119 - Key words for requirement levels (MUST, SHOULD, MAY)
- OpenAPI Specification - API change documentation standards
- JSON Schema - Data structure change documentation
- GraphQL Schema - API evolution and deprecation patterns

**Security & Compliance**:
- CVE (Common Vulnerabilities and Exposures) - Security issue tracking
- CVSS (Common Vulnerability Scoring System) - Severity ratings
- CWE (Common Weakness Enumeration) - Vulnerability categorization
- NIST Cybersecurity Framework - Security patch documentation
- OWASP Dependency-Check - Vulnerability scanning and reporting
- Snyk Vulnerability DB - Security advisory integration
- GitHub Security Advisories - CVE tracking and disclosure

**Release Communication & Distribution**:
- GitHub Releases - Native release note hosting and distribution
- GitLab Release Notes - Integrated release documentation
- Docker Hub Release Notes - Container image version documentation
- npm package.json - Package versioning and release metadata
- RubyGems Changelog - Gem version documentation
- PyPI Release History - Python package versioning
- Maven Central - Java artifact versioning
- NuGet Package Versioning - .NET package releases

**API & Interface Versioning**:
- API Versioning Strategies - URL path, header, parameter-based versioning
- OpenAPI/Swagger - API change documentation and breaking change detection
- GraphQL Schema Versioning - Field deprecation and evolution patterns
- gRPC Versioning - Protocol buffer compatibility rules
- REST API Deprecation - Sunset header (RFC 8594) for API lifecycle

**Backward Compatibility & Migration**:
- Semantic Import Versioning (Go) - Import path versioning for breaking changes
- Feature Flags - Gradual rollout documentation (LaunchDarkly, Split.io)
- Blue-Green Deployment - Zero-downtime release strategies
- Canary Releases - Gradual rollout documentation and metrics
- Database Migration Tools - Flyway, Liquibase version tracking

**Quality & Testing**:
- Release Qualification Criteria - Acceptance criteria documentation
- Regression Testing Requirements - Test coverage for changes
- Performance Benchmarking - Performance impact documentation
- Load Testing Results - Capacity and scalability validation
- Smoke Test Checklists - Post-deployment verification

**Dependency Management**:
- npm Semantic Versioning - Package.json version ranges
- Maven Dependency Management - POM version specifications
- Go Module Versioning - go.mod version requirements
- Cargo (Rust) Versioning - Semantic version requirements
- Bundler (Ruby) Version Constraints - Gemfile.lock tracking
- Poetry (Python) Dependency Resolution - pyproject.toml versioning
- Dependabot - Automated dependency update notifications
- Renovate - Dependency update automation with release notes

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

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
