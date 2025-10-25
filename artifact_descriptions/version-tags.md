# Name: version-tags

## Executive Summary

The Version Tags artifact defines version identification standards for software artifacts, container images, git releases, and deployed services using Semantic Versioning 2.0.0 (SemVer) conventions. Version tags enable precise artifact tracking, reproducible builds, deployment traceability, and rollback operations across CI/CD pipelines, container registries (Docker Hub, ECR, GCR, ACR), and artifact repositories (npm, Maven, PyPI, NuGet).

Version tags integrate with git tagging (annotated tags like v1.2.3), OCI image specifications for container versioning, GitVersion for automated SemVer calculation, and semantic-release for automated tag creation. They support deployment tracking in Kubernetes (image tags), infrastructure as code (Terraform module versions), and observability platforms (Datadog deployment markers, New Relic change tracking). Version tags provide audit trails for compliance (SOC 2, ISO 27001), enable precise rollback to known-good versions, and support canary deployments with specific version targeting.

### Strategic Importance

- **Artifact Traceability**: Enables precise tracking of code versions through git tags, container images, and deployed services
- **Semantic Versioning**: Enforces SemVer 2.0.0 (MAJOR.MINOR.PATCH) for clear breaking change communication
- **Reproducible Builds**: Ensures identical artifacts can be rebuilt from specific git tags and commit SHAs
- **Deployment Precision**: Enables targeting specific versions for blue-green, canary, and rollback deployments
- **Container Image Management**: Supports immutable container tags in OCI registries (never reuse tags like latest)
- **Automated Version Calculation**: Integrates GitVersion, semantic-release for CI/CD automation
- **Compliance Audit Trail**: Provides version tracking evidence for SOC 2, ISO 27001, regulatory requirements

## Purpose & Scope

### Primary Purpose

Version tags define naming conventions and versioning strategies for git tags, container images, artifacts, and deployed services following Semantic Versioning 2.0.0. They enable artifact identification, deployment targeting, rollback operations, and compliance audit trails across development, CI/CD, and production environments.

### Scope

**In Scope**:
- Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH) for all version identifiers
- Git annotated tags (v1.2.3) with release metadata and GPG signatures
- Container image tags (myapp:1.2.3, myapp:1.2.3-alpine, myapp:sha-abc123f)
- Pre-release version suffixes (1.0.0-alpha.1, 1.0.0-beta.2, 1.0.0-rc.1)
- Build metadata suffixes (1.0.0+20240315.build.123, 1.0.0+sha.abc123f)
- Immutable tag policies (never reuse version tags, avoid mutable tags like latest)
- OCI Image Specification compliance for container registries
- Package manager version conventions (npm, Maven, PyPI, NuGet, RubyGems, Cargo)
- Calendar versioning (CalVer) alternatives for time-based releases (YYYY.MM.DD)
- GitVersion configuration for automated SemVer calculation from git history
- semantic-release automated tag creation and version bumping
- Kubernetes image tag references (deployment manifests, Helm values)
- Infrastructure as Code version tags (Terraform modules, Ansible roles, CloudFormation)
- Artifact repository versioning (Docker Hub, Amazon ECR, Google GCR, Azure ACR, Artifactory, Nexus)
- Deployment marker integration (Datadog, New Relic, Sentry release tracking)

**Out of Scope**:
- Detailed release note content for each version (handled by release-notes.md)
- Change history documentation (handled by changelogs.md)
- Version release risk assessment (handled by release-risk-assessment.md)
- Release certification criteria (handled by release-certification.md)

### Target Audience

**Primary Audience**:
- DevOps Engineers managing CI/CD pipelines and artifact versioning automation
- Release Managers coordinating version releases and deployment tracking
- SRE Teams deploying specific versions and performing rollback operations
- Build Engineers configuring automated versioning in CI/CD systems
- Container Platform Engineers managing image registries and tag policies

**Secondary Audience**:
- Software Engineers understanding version tagging for local development
- Security Teams tracking deployed versions for vulnerability management
- Compliance Officers auditing version history for regulatory requirements
- Infrastructure Engineers versioning IaC modules and configurations
- QA Teams identifying tested versions and release candidate tracking

## Document Information

**Format**: Markdown

**File Pattern**: `*.version-tags.md`

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

**Semantic Versioning Compliance**: Strictly follow SemVer 2.0.0 - MAJOR.MINOR.PATCH with clear breaking change communication
**Immutable Tags**: Never reuse or overwrite version tags - each version is immutable forever
**Annotated Git Tags**: Use git annotated tags (git tag -a v1.2.3) with release descriptions, not lightweight tags
**v-Prefix Convention**: Prefix git tags with 'v' (v1.2.3) to distinguish from other tag types
**Automated Tagging**: Use GitVersion or semantic-release for consistent, automated version calculation
**Multi-Tag Strategy**: Tag container images with version, SHA, and conditional latest (myapp:1.2.3, myapp:sha-abc123, myapp:latest)
**Avoid Latest Tag**: Minimize use of 'latest' tag in production deployments - always use specific versions
**Image Digest Pinning**: Reference container images by SHA256 digest in production for absolute immutability
**Pre-Release Suffixes**: Use standard suffixes (alpha, beta, rc) for pre-production versions (1.0.0-beta.2)
**Build Metadata**: Include commit SHA and build info in metadata suffix (1.0.0+sha.abc123f.build.456)
**Git Tag Protection**: Enable tag protection in GitHub/GitLab to prevent unauthorized tag modification
**GPG Sign Tags**: Sign release tags with GPG for cryptographic verification (git tag -s v1.2.3)
**Tag Synchronization**: Ensure git tags, container tags, and artifact versions match exactly
**Deployment Markers**: Send version tags to observability platforms (Datadog, New Relic, Sentry) for deployment tracking
**Tag Retention Policy**: Define lifecycle policies for old container image tags to reduce storage costs
**Version Documentation**: Document version in git tag annotation with release notes summary and links
**Rollback Version Access**: Maintain all historical versions in registries for potential rollback needs
**Environment-Specific Suffixes**: Use suffixes for environment variants (1.2.3-staging, 1.2.3-production) sparingly
**Monorepo Versioning**: Consider independent versioning per package vs unified version in monorepos
**Version Validation**: Implement CI checks to validate version format and SemVer compliance

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

**Semantic Versioning**:
- Semantic Versioning 2.0.0 (SemVer) - MAJOR.MINOR.PATCH version standard
- SemVer Pre-Release Versions - Alpha, beta, rc (release candidate) suffixes
- SemVer Build Metadata - Build number, commit SHA, date suffixes
- Calendar Versioning (CalVer) - YYYY.MM.DD time-based versioning alternative
- ZeroVer - 0.x.y versioning for pre-1.0 software
- Romantic Versioning - Alternative versioning philosophies

**Git Tagging**:
- Git Annotated Tags - Metadata-rich tags (git tag -a v1.2.3 -m "Release 1.2.3")
- Git Lightweight Tags - Simple commit pointers (git tag v1.2.3)
- GPG Signed Tags - Cryptographically signed release tags (git tag -s)
- Tag Naming Conventions - v-prefix (v1.2.3) vs no prefix (1.2.3)
- Git Tag Push - Remote tag synchronization (git push --tags, git push origin v1.2.3)
- Tag Protection - GitHub/GitLab tag protection rules
- GitHub Releases - Tag-based release documentation

**Automated Version Calculation**:
- GitVersion - Automatic SemVer from git history (mainline, GitFlow, GitHubFlow modes)
- semantic-release - Fully automated versioning and releases
- standard-version - Manual trigger automated versioning
- release-please - Automated release PRs with version bumping
- bump2version / bumpversion - Python version bumping tool
- cargo-release - Rust crate release automation
- npm version - npm built-in version bumping (major, minor, patch)

**Container Image Tagging**:
- OCI Image Specification - Open Container Initiative standards
- Docker Image Tags - Immutable versioning best practices
- Container Registry Standards - Docker Hub, Amazon ECR, Google GCR, Azure ACR
- Image Digest (SHA256) - Immutable image identification
- Multi-Tag Strategy - Version tag + latest + SHA tags
- Immutable Tags - Never reuse version tags policy
- Tag Retention Policies - Automatic old tag cleanup
- Vulnerability Scanning Tags - Integration with Trivy, Clair, Snyk

**Package Manager Versioning**:
- npm Semantic Versioning - package.json version field and version ranges
- Maven Versioning - POM version conventions (SNAPSHOT, release versions)
- PyPI Versioning - PEP 440 version identification and ordering
- NuGet Semantic Versioning - .NET package versioning
- RubyGems Versioning - Gem specification versioning
- Cargo (Rust) Versioning - Semantic versioning for crates
- Go Module Versioning - go.mod major version in import path (v2, v3)
- Gradle Version Catalogs - Centralized dependency version management

**Kubernetes & Container Orchestration**:
- Kubernetes Image Tags - Pod spec container image references
- Helm Chart Versioning - Chart.yaml version and appVersion fields
- Kustomize Image Tags - Image transformer version management
- ArgoCD Image Updater - Automated image version updates
- Flux CD Image Automation - GitOps-based image version updates
- Deployment Rollback - kubectl rollout undo using image tags

**Infrastructure as Code Versioning**:
- Terraform Module Versioning - Git tags for module source references
- Terraform Registry - Module versioning standards
- Ansible Role Versioning - Galaxy role version tags
- CloudFormation Template Versions - Stack template versioning
- Pulumi Stack Tags - Infrastructure state versioning
- CDK Version Management - Cloud Development Kit versioning

**Artifact Repository Management**:
- Docker Hub - Public and private container registry
- Amazon ECR - Elastic Container Registry versioning and lifecycle
- Google Artifact Registry (GCR) - Container and artifact storage
- Azure Container Registry (ACR) - Container image versioning
- JFrog Artifactory - Universal artifact repository
- Sonatype Nexus - Artifact repository manager
- GitHub Packages - Native GitHub artifact hosting
- GitLab Container Registry - Integrated container storage

**Deployment Tracking & Observability**:
- Datadog Deployment Tracking - Version deployment markers
- New Relic Change Tracking - Release version monitoring
- Sentry Release Tracking - Error tracking with version context
- PagerDuty Change Events - Version deployment notifications
- Prometheus Deployment Annotations - Metric annotation with versions
- Grafana Deployment Annotations - Dashboard version markers
- Honeycomb Deployment Markers - Observability context with versions

**CI/CD Integration**:
- GitHub Actions - Automated tagging workflows
- GitLab CI/CD - Version tag-based pipelines
- Jenkins Versioning - Build number and version management
- CircleCI - Tag-based deployment workflows
- Azure DevOps Pipelines - Semantic versioning integration
- AWS CodePipeline - Version-based deployment stages
- Argo Workflows - Version-aware workflow execution

**Compliance & Audit**:
- SOC 2 Type 2 - Version control and change tracking evidence
- ISO 27001 - Configuration management and version control
- NIST Cybersecurity Framework - Asset management and versioning
- Software Bill of Materials (SBOM) - Version inventory tracking
- Provenance Attestation - SLSA framework version verification

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
