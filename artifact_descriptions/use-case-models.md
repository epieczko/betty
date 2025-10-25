# Name: use-case-models

## Executive Summary

Use Case Models provide detailed textual specifications for each use case identified in use case diagrams, documenting preconditions, postconditions, main success scenarios (happy paths), alternative flows, exception flows, business rules, and validation criteria following Alistair Cockburn and Ivar Jacobson methodologies. These comprehensive specifications transform visual use case diagrams into actionable requirements documentation that developers can implement and QA engineers can test, using structured templates (brief, casual, fully-dressed formats) managed in tools like Jira, Confluence, Azure DevOps, or dedicated requirements platforms.

Each use case specification documents actor interactions with the system through numbered steps showing request-response sequences, decision points, alternative paths, error handling, and success criteria. Following IEEE 29148 and BABOK standards, use case models bridge the gap between high-level use case diagrams and detailed functional requirements, providing scenario-based specifications that capture business workflows, user goals, system responses, and validation rules in structured, testable formats accessible to both business stakeholders and technical teams.

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

This artifact serves as the detailed textual specification for each use case, documenting step-by-step interactions between actors and the system including preconditions, main success scenario, alternative flows, exception handling, postconditions, business rules, and non-functional requirements. These specifications provide sufficient detail for development, testing, and validation activities.

### Scope

**In Scope**:
- Use case name and unique identifier
- Primary and secondary actors
- Stakeholders and interests
- Preconditions (what must be true before use case starts)
- Postconditions (guaranteed outcomes after successful completion)
- Main success scenario (happy path, numbered steps)
- Alternative flows (variations, optional paths, branches)
- Exception flows (error conditions, failure handling)
- Business rules and validation logic
- Frequency of occurrence and performance requirements
- Open issues and assumptions
- Use case priority and complexity estimation
- Related use cases (includes, extends, generalizes)
- Trigger events (what initiates the use case)
- Special requirements (NFRs specific to use case)

**Out of Scope**:
- Implementation details and technology choices
- User interface designs and wireframes (reference UI specs)
- Detailed class diagrams and object models
- Sequence diagrams (create separately if needed)
- Test procedures and test cases (derive from use cases)
- Project management information (effort, assignments, dates)

### Target Audience

**Primary Audience**:
- Business Analysts who author and maintain use case specifications
- Requirements Engineers who validate completeness and quality
- Development Teams who implement use case functionality
- QA Engineers who derive test scenarios from use cases
- Product Managers who validate use cases meet business needs

**Secondary Audience**:
- Business stakeholders who review and approve use case specifications
- System Architects who design system to support use case flows
- UX Designers who design interfaces for use case interactions
- Technical Writers who create user documentation
- Training Teams who develop training materials

## Document Information

**Format**: Markdown

**File Pattern**: `*.use-case-models.md`

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

### Specification Overview

**Specification Purpose**:
- `specificationGoal`: What this specification is defining
- `userStories`: User needs being addressed
- `requirements`: High-level requirements this spec satisfies
- `designPrinciples`: Guiding principles for this specification
- `constraints`: Technical, business, or regulatory constraints

### Technical Specification

**System Components**:
- `componentName`: Name of each system component
- `componentType`: Service | Library | Integration | Data Store | UI Component
- `purpose`: Why this component exists
- `responsibilities`: What this component is responsible for
- `interfaces`: How other components interact with it
- `dependencies`: What this component depends on
- `dataModel`: Data structures used or managed
- `apiEndpoints`: API endpoints exposed (if applicable)

**Functional Requirements**:
- `requirementId`: Unique identifier (e.g., FR-001)
- `requirement`: Detailed requirement statement
- `acceptance Criteria`: How requirement is verified
- `priority`: Must Have | Should Have | Could Have | Won't Have
- `complexity`: Estimation of implementation complexity
- `risks`: Risks associated with this requirement

**Non-Functional Requirements**:
- `performance`: Response time, throughput, capacity targets
- `scalability`: How system scales with load or data volume
- `availability`: Uptime requirements and SLAs
- `reliability`: Error rates, MTBF, MTTR targets
- `security`: Authentication, authorization, encryption requirements
- `compliance`: Regulatory or policy requirements
- `usability`: User experience and accessibility requirements
- `maintainability`: Code quality, documentation, testing standards
- `portability`: Platform independence or migration requirements

### Design Details

**Architecture**:
- `architecturePattern`: Microservices | Monolith | Serverless | Event-Driven
- `componentDiagram`: Visual representation of components and relationships
- `dataFlow`: How data moves through the system
- `integrationPoints`: External system integrations
- `deploymentModel`: How components are deployed and distributed

**Data Model**:
- `entities`: Core data entities
- `relationships`: How entities relate to each other
- `constraints`: Data validation and business rules
- `indexes`: Performance optimization through indexing
- `archival`: Data retention and archival strategy

**Security Design**:
- `authenticationMechanism`: How users/services authenticate
- `authorizationModel`: RBAC | ABAC | ACL approach
- `dataProtection`: Encryption at rest and in transit
- `auditLogging`: What is logged for security audit
- `threatModel`: Key threats and mitigations

### Implementation Guidance

**Development Standards**:
- `codingStandards`: Language-specific coding standards to follow
- `testingRequirements`: Unit test coverage, integration tests required
- `documentationRequirements`: Code comments, API docs, README
- `versionControl`: Branching strategy and commit conventions
- `codeReview`: Review process and criteria

**Quality Gates**:
- `buildRequirements`: Must compile without errors/warnings
- `testRequirements`: All tests must pass, minimum coverage %
- `securityRequirements`: No high/critical vulnerabilities
- `performanceRequirements`: Must meet performance SLAs
- `accessibilityRequirements`: WCAG 2.1 AA compliance (if applicable)


## Best Practices

**Structured Templates**: Use standard templates (brief, casual, fully-dressed) appropriate to use case complexity and project phase
**Numbered Steps**: Number each step in main and alternative flows for precise referencing (e.g., 3a, 3b for alternatives to step 3)
**Actor-System Dialogue**: Write steps as interaction pairs (Actor action → System response)
**Goal-Level Consistency**: Match detail level to goal level (user-goal level most common for functional requirements)
**Preconditions**: Specify clear, testable preconditions; avoid vague statements like "user is logged in" (specify authentication state)
**Postconditions**: Define guaranteed outcomes (minimal and success guarantees); distinguish from side effects
**Alternative Flows**: Document all significant variations from main success scenario with branch points clearly identified
**Exception Handling**: Specify system behavior for all error conditions and how system recovers or fails gracefully
**Business Rules**: Separate business rules from procedural steps; reference business rule identifiers
**Technology Neutrality**: Keep use cases technology-independent at requirements level; describe intent not implementation
**Testability**: Write use cases so each step can be validated through testing
**Active Voice**: Use active voice (System validates credentials, not Credentials are validated)
**Consistent Abstraction**: Maintain same level of detail throughout use case; avoid mixing high-level and low-level steps
**Stakeholder Walkthrough**: Walk through use cases with stakeholders to validate accuracy and completeness
**Unique Identifiers**: Assign unique IDs to use cases for traceability (UC-001, UC-PAYMENT-01)
**Related Use Case Links**: Document includes, extends, and generalization relationships
**Frequency and Volume**: Specify expected frequency and data volumes for capacity planning

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

**Use Case Writing Standards**:
- "Writing Effective Use Cases" by Alistair Cockburn: Standard reference for use case templates and best practices
- Cockburn Use Case Template: Brief, Casual, Fully-Dressed formats
- Goal Levels: Summary, User-Goal, Subfunction (cloud, sea-level, fish levels)
- Ivar Jacobson Use Case Methodology: Original use case specification approach
- Use Case 2.0: Modern use case practices with use case slices and incremental development

**Requirements Engineering Standards**:
- IEEE 29148-2018: Use cases as requirements specification technique
- BABOK v3 (IIBA): Use case modeling in business analysis
- IREB/CPRE: Use case analysis in requirements engineering certification
- ISO/IEC/IEEE 29148: Requirements engineering processes including use case modeling

**Use Case Template Components**:
- Cockburn Fully-Dressed Template: Scope, level, primary actor, stakeholders, preconditions, postconditions, main scenario, extensions
- Essential Use Cases: Technology-free, implementation-independent specifications
- System Use Cases vs. Business Use Cases: Distinguish system-level from business process level
- Use Case Briefs: One-paragraph summaries for high-level scoping
- Casual Use Cases: Multi-paragraph informal descriptions
- Fully-Dressed Use Cases: Comprehensive specifications with all sections

**Use Case Analysis Techniques**:
- Use Case Points (UCP): Effort estimation based on use case complexity
- Robustness Analysis: Identifying boundary, control, and entity objects from use cases
- ICONIX Process: Use case-driven development with robustness diagrams
- Rational Unified Process (RUP): Use case-driven iterative development
- Use Case Realization: Tracing use cases to design (sequence diagrams, class diagrams)

**Documentation and Collaboration Tools**:
- Confluence: Wiki-based use case documentation and collaboration
- Jira: Use case management with issues and epics
- Azure DevOps: Work items for use case specifications
- Google Docs/Microsoft Word: Traditional documentation with templates
- Notion: Collaborative documentation platform
- GitLab/GitHub Wiki: Version-controlled use case documentation

**Related Modeling Approaches**:
- User Stories: Agile lightweight alternative (As a... I want... So that...)
- BDD/Gherkin: Given-When-Then scenarios (executable specifications)
- Scenario-Based Design: Rosson and Carroll scenario methodology
- Task Analysis: HCI task modeling techniques
- BPMN: Business process flows for detailed workflow modeling
- Activity Diagrams: UML workflow and decision flow visualization

**Use Case Testing**:
- Use Case-Based Testing: Deriving test cases from use case flows
- Scenario Testing: Testing each use case scenario (main + alternatives + exceptions)
- Acceptance Test-Driven Development (ATDD): Using use cases for acceptance criteria
- Specification by Example: Gojko Adzic's approach to executable specifications

**Quality Frameworks**:
- Use Case Quality Checklist: Completeness, correctness, clarity, consistency
- Ambiguity Analysis: Identifying vague or ambiguous language in use cases
- Peer Review Techniques: Structured walkthroughs and inspections
- Traceability: Linking use cases to requirements, design, tests

**Industry and Domain Practices**:
- Financial Services: Use cases for transaction processing, account management
- Healthcare: Use cases for patient workflows, clinical processes (HL7, FHIR integration)
- E-commerce: Use cases for shopping cart, checkout, order management
- SaaS Applications: Use cases for subscription, billing, user management

**Academic References**:
- "Use Case Modeling" by Kurt Bittner and Ian Spence
- "Applying Use Cases: A Practical Guide" by Geri Schneider and Jason Winters
- "UML Distilled" by Martin Fowler (use case chapter)
- "Object-Oriented Software Engineering" by Ivar Jacobson

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
