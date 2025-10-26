# Name: contributing-guide

## Executive Summary

Contributing Guides provide comprehensive documentation for community contributors, external developers, and internal teams to participate in open-source projects, documentation improvements, and collaborative development. Typically stored as CONTRIBUTING.md in repository root following GitHub/GitLab conventions, contributing guides establish clear expectations for code contributions, documentation updates, issue reporting, and community engagement while defining workflows, coding standards, and review processes.

These guides implement inclusive community practices aligned with open-source governance models, incorporating Developer Certificate of Origin (DCO) or Contributor License Agreement (CLA) requirements, pull request templates for consistency, code review guidelines, commit message conventions (Conventional Commits), and community codes of conduct. Written in Markdown following plain language principles and the Google Developer Documentation Style Guide, contributing guides reduce friction for new contributors, standardize contribution quality, and scale community participation through clear, accessible documentation of processes and expectations.

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

Contributing Guides serve as the gateway for community participation by documenting how to contribute code, documentation, bug reports, and feature requests while establishing quality standards, review processes, and community norms. They solve the problem of inconsistent contributions and repeated questions by providing clear, step-by-step guidance that reduces maintainer burden and accelerates contributor onboarding.

### Scope

**In Scope**:
- Contribution process overview (how to get started, finding issues to work on)
- Development environment setup for contributors
- Git workflow and branching strategy (fork-and-pull, feature branches)
- Commit message conventions (Conventional Commits, semantic messages)
- Pull request process (PR templates, description requirements, review expectations)
- Code review guidelines (what reviewers look for, responding to feedback)
- Coding standards and style guides (language-specific conventions, linting, formatting)
- Testing requirements (unit tests, integration tests, coverage thresholds)
- Documentation expectations (API docs, README updates, changelog entries)
- Issue reporting guidelines (bug reports, feature requests, templates)
- Community guidelines and code of conduct
- Legal requirements (CLA, DCO, license compatibility)
- Recognition and attribution practices
- Communication channels (Slack, Discord, forums, mailing lists)
- Maintainer responsibilities and response expectations

**Out of Scope**:
- Product roadmap and feature prioritization (covered in product documentation)
- Detailed technical architecture (covered in architecture docs)
- User-facing documentation (covered in user guides and API docs)
- Internal team processes not relevant to external contributors
- Project governance and decision-making authority (covered in governance docs)

### Target Audience

**Primary Audience**:
- Open-source contributors making their first contribution
- External developers contributing code, documentation, or bug fixes
- Community members reporting issues or suggesting features
- Documentation contributors improving docs and examples

**Secondary Audience**:
- Project maintainers enforcing contribution standards
- Technical Writers ensuring documentation quality
- Community managers fostering healthy participation
- Legal/Compliance teams ensuring proper attribution and licensing
- DevRel teams promoting community contributions

## Document Information

**Format**: Markdown

**File Pattern**: `CONTRIBUTING.md`

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

**Welcoming First-Time Contributors**: Create "good first issue" labels for beginner-friendly tasks, provide detailed mentorship on first PRs, celebrate first-time contributors with bot comments or recognition, offer office hours or pair programming for newcomers, maintain comprehensive setup documentation, and respond promptly and kindly to questions

**Clear Contribution Process**: Document step-by-step contribution workflow with examples, provide flowcharts or diagrams showing PR lifecycle, include troubleshooting for common setup issues, create video walkthroughs of contribution process, link to all required templates (PR, issue), and set clear expectations for response times

**Automated Quality Gates**: Implement pre-commit hooks for code formatting and linting, run automated tests on every PR, validate commit message format automatically, check license headers and attribution, scan for security vulnerabilities, enforce code coverage thresholds, and provide clear feedback when checks fail

**Maintainable PR Standards**: Request small, focused PRs (< 400 lines ideal), encourage draft PRs for early feedback, require linked issue for context, enforce descriptive PR titles and descriptions, mandate testing evidence (screenshots, test results), and provide PR templates with checklist

**Inclusive Community Culture**: Enforce code of conduct consistently, use inclusive language in all communications, provide multiple communication channels for different preferences, accommodate different time zones and languages, recognize diverse contribution types (code, docs, community support), and foster psychological safety for questions

**Legal Compliance**: Clearly state licensing requirements upfront, implement DCO or CLA signing workflow, automate license compliance checking, document acceptable licenses for dependencies, provide guidance on copyright and attribution, and maintain clear intellectual property policies

**Effective Code Review**: Provide constructive, specific feedback with examples, suggest improvements with code snippets, distinguish between required changes and suggestions, respond to contributor questions promptly, approve when requirements met (don't bikeshed), recognize good work in reviews, and maintain review turnaround SLAs

**Documentation Requirements**: Require documentation updates with code changes, mandate changelog entries for user-facing changes, enforce API documentation for new endpoints/functions, include README updates for new features, provide examples and use cases in documentation, and validate documentation builds in CI/CD

**Contribution Diversity**: Accept various contribution types (code, documentation, testing, issue triage, community support), recognize non-code contributions equally, provide contribution pathways for different skill levels, create opportunities for technical writing contributions, and encourage domain expertise contributions

**Maintainer Sustainability**: Set realistic response time expectations, use automation to reduce manual work, empower trusted contributors with triage permissions, rotate maintainer responsibilities to prevent burnout, document maintainer escalation paths, and provide maintainer onboarding and offboarding

**Transparency & Communication**: Publicly document decision-making processes, explain rejection reasons constructively, provide project roadmap and priorities, share metrics on contributor health, communicate breaking changes well in advance, maintain public issue tracker, and hold regular community calls

**Continuous Improvement**: Regularly review contribution guidelines based on feedback, track contribution metrics (velocity, diversity, retention), survey contributors about their experience, identify and remove contribution friction, update guides when processes change, and learn from other successful projects

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

**Open Source Governance**:
- OSI (Open Source Initiative) approved licenses
- Apache Software Foundation contribution guidelines
- Linux Foundation open source best practices
- CNCF (Cloud Native Computing Foundation) contributor guidance
- GitHub Open Source Guides
- GitLab's guide to open source contributions
- TODO Group open source program office resources

**Contribution Legal Frameworks**:
- Developer Certificate of Origin (DCO) with signed-off-by commits
- Contributor License Agreement (CLA) individual and corporate
- License compatibility and inbound=outbound licensing
- Copyright and attribution requirements
- Patent grant considerations
- Third-party dependency license compliance

**Version Control Workflows**:
- Fork-and-pull model for external contributors
- Shared repository model for internal teams
- Git branching strategies (GitFlow, GitHub Flow, trunk-based development)
- Conventional Commits specification for commit messages
- Semantic versioning (SemVer) for releases
- Git commit signing and verification (GPG, SSH)

**Pull Request Standards**:
- PR templates with required sections (description, testing, checklist)
- Commit message format and conventions
- PR size guidelines (optimal lines changed, review complexity)
- Draft PR workflow for early feedback
- PR labels and categorization
- Automated PR checks (CI/CD, linting, tests)
- Review approval requirements

**Code Review Practices**:
- Google Code Review Guidelines
- Thoughtful Code Review practices
- Conventional Comments for review feedback
- Code review etiquette and inclusive language
- Review response time expectations
- Addressing review feedback effectively
- Approving and merging criteria

**Documentation Standards**:
- README.md best practices (shields.io badges, clear structure)
- CHANGELOG.md format (Keep a Changelog specification)
- LICENSE file selection and placement
- CODE_OF_CONDUCT.md (Contributor Covenant, custom codes)
- SECURITY.md for responsible disclosure
- SUPPORT.md for getting help
- Documentation style guides (Google, Microsoft, Write the Docs)

**Coding Standards & Quality**:
- Language-specific style guides (PEP 8, Standard JS, Go fmt, Rustfmt)
- Automated formatting tools (Prettier, Black, gofmt, rustfmt)
- Linting standards (ESLint, Pylint, Clippy, golangci-lint)
- Static analysis tools (SonarQube, CodeClimate, Coverity)
- Code coverage requirements and reporting
- Security scanning (Dependabot, Snyk, Trivy)

**Testing Requirements**:
- Test-driven development (TDD) practices
- Unit testing frameworks and conventions
- Integration testing requirements
- End-to-end testing guidelines
- Test coverage thresholds (line, branch, function coverage)
- Continuous integration testing requirements
- Performance and load testing expectations

**Issue Management**:
- Issue templates for bugs, features, questions
- Issue labeling taxonomy and conventions
- Issue triage process and prioritization
- "Good first issue" identification for newcomers
- Issue assignment and claiming workflow
- Stale issue management and closure policies

**Community Standards**:
- Contributor Covenant Code of Conduct
- Mozilla Community Participation Guidelines
- Inclusive language guidelines
- Diversity and inclusion best practices
- Community health metrics (CHAOSS project)
- Contributor recognition and attribution

**Automation & CI/CD**:
- GitHub Actions workflows for contribution validation
- GitLab CI/CD pipelines for automated testing
- Pre-commit hooks for local validation
- Automated code formatting on commit
- License header checking automation
- Changelog generation from commits
- Release automation with semantic-release

**Communication Channels**:
- GitHub Discussions for community conversations
- Discord/Slack for real-time chat
- Mailing lists for announcements and RFC
- Stack Overflow tags for Q&A
- Reddit communities for broader discussions
- Twitter/Mastodon for project updates

**Contributor Recognition**:
- All Contributors specification
- CONTRIBUTORS.md or AUTHORS file
- GitHub contributor graphs and insights
- Contributor badges and swag programs
- Hall of fame or contributor spotlights
- GitHub Sponsors or Open Collective funding

**Accessibility Standards**:
- WCAG 2.1 for web contributions
- Inclusive language in code and docs
- Clear, plain language for all audiences
- Multiple formats for documentation
- Keyboard navigation requirements
- Screen reader compatibility

**Project Metrics**:
- Contribution velocity metrics
- Time-to-first-response for PRs/issues
- Contributor diversity and growth
- PR acceptance rate
- Code review turnaround time
- Contributor retention rates

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
