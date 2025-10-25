# Name: deprecation-policy

## Executive Summary

A Deprecation Policy defines the structured process for phasing out software features, APIs, libraries, and services while minimizing disruption to users and downstream systems. This policy establishes deprecation timelines, sunset schedules, migration paths, and communication strategies aligned with Semantic Versioning (SemVer) conventions and API versioning best practices. Organizations must balance technical debt reduction with user stability, providing sufficient notice periods (typically 6-24 months for public APIs) and backward compatibility windows to enable graceful transitions.

Modern deprecation management follows industry patterns: feature flags for gradual rollout, API versioning (v1, v2, v3) for parallel support, and deprecation headers (Sunset HTTP header, API warnings) for programmatic discovery. Cloud providers (AWS, Azure, GCP) have established reference models with 12-36 month deprecation cycles, automated migration tooling, and phased cutover strategies. Organizations must document deprecation rationale, replacement paths, and support commitments to maintain developer trust and meet contractual SLA obligations.

### Strategic Importance

- **Technical Debt Management**: Enables removal of legacy code, outdated dependencies, and unmaintained features reducing maintenance burden
- **Security Posture**: Retires insecure APIs, deprecated cryptographic algorithms, and vulnerable components preventing exploitation
- **Cost Optimization**: Reduces infrastructure costs by sunsetting underutilized services and consolidating duplicate functionality
- **Developer Experience**: Clear deprecation timelines and migration guides maintain ecosystem trust and prevent breaking changes
- **Compliance**: Satisfies GDPR data minimization (Article 5) by retiring unused data collection, and industry deprecation standards
- **Contractual Obligations**: Manages SLA commitments for API availability, backward compatibility windows, and enterprise support terms
- **Innovation Velocity**: Accelerates feature development by removing constraints imposed by legacy architecture and compatibility layers

## Purpose & Scope

### Primary Purpose

This policy establishes mandatory procedures for deprecating software components (APIs, features, libraries, services, infrastructure), defining timeline requirements, communication protocols, migration support obligations, and sunset execution criteria. It ensures deprecated items follow Semantic Versioning conventions (MAJOR version increments for breaking changes), provide sufficient advance notice (6-36 months based on user impact), and include documented migration paths to replacement functionality.

### Scope

**In Scope**:
- Public API deprecation: REST endpoints, GraphQL fields, gRPC services with versioning strategies (v1, v2, v3)
- SDK/library deprecation: npm packages, Maven artifacts, Python packages, Ruby gems with version sunset
- Feature deprecation: UI features, product capabilities, configuration options with user migration guides
- Service deprecation: microservices, infrastructure components, cloud services with cutover planning
- Protocol/standard deprecation: TLS 1.0/1.1 sunset, deprecated cipher suites, outdated authentication methods
- Dependency deprecation: third-party library upgrades, EOL runtime versions (Python 2.7, Node.js 10)
- Data format deprecation: file formats, serialization protocols, schema versions with conversion tooling
- Deprecation timelines: notice periods, warning phases, sunset dates, support cutoff, infrastructure removal
- Communication requirements: changelog entries, API documentation updates, email notifications, blog posts, deprecation headers
- Migration support: code examples, automated migration tools, backward compatibility shims, polyfills

**Out of Scope**:
- Emergency security patches requiring immediate removal without standard deprecation timeline
- Internal-only tools and scripts not exposed to external users or dependent teams
- Alpha/beta features explicitly marked as experimental without stability guarantees
- Data retention and deletion policies (covered by separate data lifecycle policy)
- Product end-of-life (EOL) for entire products (covered by product lifecycle policy)

### Target Audience

**Primary Audience**:
- Engineering Leadership: Deprecation roadmap planning, resource allocation for migration support, technical debt prioritization
- Platform/API Teams: Deprecation timeline enforcement, versioning strategy, backward compatibility maintenance
- Product Management: Customer communication planning, feature sunset decisions, migration effort estimation
- Developer Relations: Migration guide creation, community support, documentation updates, developer outreach

**Secondary Audience**:
- External Developers: API consumers requiring migration timelines and replacement guidance
- Technical Support: Fielding deprecation inquiries, assisting with migration issues, escalation procedures
- Legal/Contracts: SLA impact assessment, contractual notice requirements, customer agreement modifications
- Security Teams: Vulnerability-driven deprecation, EOL software retirement, cryptographic algorithm sunsets

## Document Information

**Format**: Markdown

**File Pattern**: `*.deprecation-policy.md`

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

**Tiered Timeline Model**: Use 6-month minimum for internal APIs, 12-month for public APIs, 24+ months for critical infrastructure/protocols
**SemVer Compliance**: Increment MAJOR version for breaking changes; use MINOR for deprecation warnings with continued support
**Sunset HTTP Header**: Implement RFC 8594 Sunset header returning deprecation date in HTTP responses for automated detection
**Multi-Phase Rollout**: (1) Deprecation announcement, (2) Warning phase with logs, (3) Error phase, (4) Removal phase
**Usage Telemetry**: Instrument deprecated endpoints/features to track adoption of replacements before final sunset
**Migration Guide Template**: Standardize migration docs with: deprecation reason, timeline, replacement API, code examples, breaking changes
**Automated Warnings**: Emit runtime warnings, compile-time deprecation notices, API response headers alerting to upcoming sunset
**Backward Compatibility Window**: Maintain parallel support for old and new versions during migration period (typically 2-3 releases)
**Customer Segmentation**: Enterprise customers may require longer deprecation windows per SLA; tier timelines accordingly
**Feature Flag Gradual Rollout**: Use feature flags to incrementally sunset features, enabling quick rollback if migration issues arise
**Deprecation Log**: Maintain public log of all deprecations with dates, rationale, and migration paths for transparency
**Early Adopter Program**: Offer beta access to replacements before deprecating old features to smooth transition
**Breaking Change Batching**: Batch multiple deprecations into single major version release to minimize disruption frequency
**Metrics-Driven Decisions**: Only deprecate after usage drops below threshold (e.g., <5% of API calls) or replacement adoption >80%
**Security Exception Process**: Define accelerated deprecation for security vulnerabilities (e.g., 30-day emergency sunset)
**Dependency Impact Analysis**: Before deprecating, assess impact on downstream dependencies and notify maintainers
**Automated Migration Tools**: Provide codemods, scripts, or IDE refactoring tools to automate migration where feasible
**Changelog Documentation**: Document deprecations prominently in CHANGELOG.md with BREAKING CHANGE and DEPRECATED sections
**Email Notification Cadence**: Send deprecation notices at: announcement, 6-month, 3-month, 1-month, 1-week before sunset
**OpenAPI/GraphQL Annotations**: Mark deprecated endpoints/fields in schema definitions for automatic documentation generation

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

**Versioning Standards**:
- Semantic Versioning (SemVer) 2.0.0 (MAJOR.MINOR.PATCH for breaking changes)
- Calendar Versioning (CalVer) for time-based releases (Ubuntu YY.MM model)
- API Versioning strategies: URI versioning (/v1/, /v2/), header versioning (Accept: application/vnd.api+json;version=2)
- GraphQL versioning patterns (field deprecation directives, schema evolution)
- gRPC versioning best practices (package versioning, backward compatibility)

**HTTP Standards for Deprecation**:
- RFC 8594 Sunset HTTP Header (deprecation date communication)
- HTTP Warning header (299 Miscellaneous Persistent Warning for deprecated endpoints)
- Link header with rel="deprecation" for migration guidance URLs
- Custom headers: X-API-Deprecation-Date, X-API-Sunset-Date

**Cloud Provider Deprecation Models**:
- AWS Service Deprecation Policy (12-month minimum notice for service termination)
- Google Cloud Platform End of Life Policy (12+ months notice, migration guides)
- Microsoft Azure deprecation lifecycle (retirement notifications 12+ months in advance)
- Kubernetes API deprecation policy (3 minor version or 9-month minimum support)
- OpenStack deprecation policy (cycle-based deprecation with warnings)

**Language/Runtime EOL**:
- Python EOL Schedule (PEP 387 Backwards Compatibility Policy)
- Node.js Release Schedule (LTS, Active, Maintenance, EOL phases)
- Java SE Support Roadmap (Oracle LTS versions and EOL timelines)
- .NET Support Policy (LTS vs. Current release support windows)
- Ruby EOL Schedule (branch maintenance timelines)
- PHP Supported Versions timeline

**API Design Standards**:
- OpenAPI Specification 3.1 (deprecated flag for operations, parameters, schemas)
- REST API Design Guidelines (Microsoft, Google, Zalando) deprecation sections
- GraphQL Schema directives: @deprecated(reason: "Use newField instead")
- JSON:API specification versioning and deprecation guidance
- gRPC API design guide deprecation best practices

**Industry Deprecation Frameworks**:
- NIST SP 800-57 (cryptographic algorithm lifecycle, algorithm transitions)
- PCI DSS TLS/SSL deprecation requirements (TLS 1.2+ mandates)
- FIPS 140-2/140-3 deprecated cryptographic modules
- CA/Browser Forum Baseline Requirements (certificate algorithm deprecations)
- W3C Process for obsoleting web standards

**Developer Communication Standards**:
- Changelog format: Keep a Changelog (keepachangelog.com) with DEPRECATED section
- RFC 8288 Web Linking (rel="deprecation" link relations)
- Conventional Commits with BREAKING CHANGE footer for SemVer
- API Blueprint and RAML deprecation annotations
- Swagger/OpenAPI deprecation markers

**Monitoring and Analytics**:
- API usage analytics (identify deprecated endpoint calls)
- Feature flag platforms: LaunchDarkly, Split, Unleash (gradual rollout/rollback)
- APM tools: New Relic, Datadog (deprecated API usage tracking)
- API gateway deprecation headers: Kong, Apigee, AWS API Gateway
- Telemetry for deprecated feature usage (OpenTelemetry instrumentation)

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
