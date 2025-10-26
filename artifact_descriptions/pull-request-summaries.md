# Name: pull-request-summaries

## Executive Summary

The Pull Request Summaries artifact provides concise, structured documentation of code changes proposed for integration into the main codebase, following industry best practices for PR descriptions, Conventional Commits, linked issue tracking, and automated changelog generation. This artifact ensures reviewers can quickly understand the what, why, and how of changes while maintaining traceability to product requirements, bug reports, and feature requests.

As a cornerstone of collaborative software development, PR summaries serve development teams communicating change intent, reviewers assessing risk and impact, release managers generating changelogs, and product managers tracking feature delivery. Integration with platforms like GitHub, GitLab, Bitbucket, and Jira enables automated workflows including PR templates, commit message linting (commitlint), semantic versioning, changelog generation (standard-version, semantic-release), and deployment tracking across environments.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact serves as clear, contextual documentation for each code change, explaining the motivation (why), implementation approach (how), testing strategy (validation), and impact (what changes). It enables reviewers to perform effective code reviews, facilitates changelog generation for release notes, provides traceability to user stories/bugs, and supports deployment decisions by clearly communicating breaking changes, feature flags, and rollback procedures.

### Scope

**In Scope**:
- PR title and description following Conventional Commits (feat, fix, docs, style, refactor, perf, test, chore)
- Motivation and context (problem statement, user story, business value)
- Implementation approach and technical decisions
- Testing performed (unit, integration, E2E, manual testing scenarios)
- Screenshots/recordings for UI changes
- Breaking changes documentation (API changes, migration guides)
- Linked issues and user stories (Jira, GitHub Issues, Linear)
- Reviewer checklist (security, performance, accessibility, documentation)
- Deployment notes (feature flags, database migrations, configuration changes)
- Test coverage metrics (coverage delta, new/modified tests)
- Rollback procedures for high-risk changes
- Changelog entry preview (semantic-release format)

**Out of Scope**:
- Detailed code review comments (covered by code review records)
- Build/CI logs and test results (covered by CI/CD artifacts)
- Production deployment records (covered by deployment artifacts)
- Incident response for failed deployments (covered by incident management)
- Detailed test plans (covered by QA test plan artifacts)

### Target Audience

**Primary Audience**:
- Software Engineers authoring PRs with clear context for reviewers
- Code Reviewers assessing change impact, risk, and quality
- Engineering Managers tracking feature delivery and change velocity

**Secondary Audience**:
- QA Engineers understanding test coverage and validation approach
- Product Managers tracking feature completion and release scope
- DevOps/SRE Engineers assessing deployment risk and rollback requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.pull-request-summaries.md`

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

**Conventional Commits**: Use Conventional Commits format (feat:, fix:, docs:, refactor:) for PR titles; automate changelog generation with semantic-release
**Clear Title**: Write concise, imperative PR titles (max 72 chars) describing the change outcome, not implementation
**Comprehensive Description**: Include WHY (motivation), WHAT (changes), HOW (approach), TESTING (validation), IMPACT (breaking changes, rollout)
**Link Issues**: Always link related issues/tickets (Closes #123, Fixes #456); enables automated issue closure and traceability
**Screenshots for UI**: Include before/after screenshots/GIFs for all UI changes; use tools like Loom for interactive demos
**Breaking Changes**: Explicitly document breaking changes in BREAKING CHANGE section; provide migration guide with code examples
**Test Coverage**: Report test coverage delta; add tests for bug fixes to prevent regressions; document manual test scenarios
**Small PRs**: Keep PRs focused and under 400 lines; split large features into incremental PRs with feature flags
**Draft PRs**: Use draft/WIP PRs for early feedback; convert to ready-for-review when CI passes and self-review complete
**Self-Review**: Review your own PR first; add inline comments explaining complex logic; ensure CI passes before requesting review
**Reviewer Guidance**: Tag specific reviewers for different aspects (security team for auth changes, DBA for schema changes)
**Deployment Notes**: Document required migrations, configuration changes, feature flag states, and rollback procedures
**Changelog Preview**: Include changelog entry in PR description; preview what users/operators will see in release notes
**Review Checklist**: Provide reviewer checklist (security, performance, tests, docs, breaking changes, rollback plan)
**Semantic Labels**: Apply semantic labels (major, minor, patch, breaking-change) to automate version bumps
**Update Frequently**: Rebase/merge main branch frequently to minimize merge conflicts and catch integration issues early
**Respond Timely**: Address review comments within 24 hours; resolve or explain each comment; request re-review explicitly
**Template Enforcement**: Enforce PR templates via CI checks (e.g., danger.js, semantic-pull-requests GitHub App)

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

**Conventional Commits & Semantic Versioning**:
- Conventional Commits v1.0.0 (feat, fix, docs, style, refactor, perf, test, chore, build, ci)
- Semantic Versioning (SemVer) 2.0.0 (MAJOR.MINOR.PATCH)
- Angular Commit Message Conventions
- Commitizen (interactive commit message builder)
- commitlint (enforce commit message conventions)
- Husky (Git hooks for commit message validation)

**PR Templates & Guidelines**:
- GitHub Pull Request Templates (.github/pull_request_template.md)
- GitLab Merge Request Templates (.gitlab/merge_request_templates/)
- Bitbucket Pull Request Templates
- PR Template Best Practices (Atlassian, GitHub, GitLab docs)
- Pull Request Size Guidelines (Google: <400 LOC ideal)
- Stacked PR/Diff Practices (Phabricator-style workflows)

**Changelog Generation**:
- Keep a Changelog (keepachangelog.com)
- standard-version (automated versioning and CHANGELOG generation)
- semantic-release (fully automated version management and package publishing)
- auto (generate releases based on semantic version labels)
- Release Drafter (GitHub Action for draft releases)
- Conventional Changelog (generate changelog from git metadata)

**Issue Tracking Integration**:
- Jira Smart Commits (issue keys in commit messages)
- GitHub Issues (closes #123, fixes #456, resolves #789)
- GitLab Issues (closes, fixes, resolves keywords)
- Linear Integration (automatic status updates from PR states)
- Azure DevOps Work Items (AB#123 syntax)
- Shortcut (formerly Clubhouse) integration

**PR Metadata & Labels**:
- GitHub Labels (bug, enhancement, documentation, breaking-change, needs-review)
- Semantic Pull Requests (GitHub App enforcing conventional PR titles)
- PR size labels (XS, S, M, L, XL based on lines changed)
- Release labels (major, minor, patch for SemVer)
- Status labels (WIP, ready-for-review, changes-requested, approved)
- Type labels (feature, bugfix, hotfix, refactor, docs)

**Code Coverage & Testing**:
- Codecov (PR comments with coverage delta)
- Coveralls (coverage tracking and PR badges)
- SonarCloud (quality gate results in PR)
- Test coverage thresholds (e.g., minimum 80% for new code)
- Mutation testing results (Stryker, PIT)

**Breaking Changes & Migration**:
- BREAKING CHANGE footer in commit body (triggers major version bump)
- Migration guide templates
- Deprecation notices (version when deprecated, version when removed)
- API versioning strategies (URL versioning, header versioning)
- Backward compatibility checklist

**Documentation Requirements**:
- README updates for new features
- API documentation (Swagger/OpenAPI, JSDoc, Javadoc)
- Architecture Decision Records (ADR) for significant changes
- Runbook updates for operational changes
- Configuration documentation for new settings

**Deployment & Rollback**:
- Feature flags/toggles (LaunchDarkly, Split.io, Unleash)
- Database migration scripts (Flyway, Liquibase, Alembic)
- Blue-green deployment considerations
- Canary deployment criteria
- Rollback procedures and safe revert commits

**Compliance & Audit**:
- SOC 2 Type II (CC6.7 - Change Management)
- ISO 27001 (A.14.2.2 - System Change Control Procedures)
- PCI-DSS Requirement 6.4.5 (Change Control Processes)
- 21 CFR Part 11 (Electronic Records; Electronic Signatures)
- NIST SP 800-53 CM-3 (Configuration Change Control)

**Reference**: Consult engineering team for PR template standards, commit message conventions, and changelog automation tooling

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
