# Name: epic-charter

## Executive Summary

The Epic Charter is a strategic hypothesis-driven document that defines the business context, vision, success metrics, and investment boundaries for large-scale initiatives (epics) within Agile frameworks like SAFe (Scaled Agile Framework), LeSS (Large-Scale Scrum), or enterprise Agile programs. Following SAFe epic structure and Lean Portfolio Management practices, this artifact articulates the business problem, proposed solution hypothesis, expected outcomes, success criteria, dependencies, risks, and go/no-go decision criteria, managed in tools like Jira Align, Azure DevOps, Rally, or VersionOne.

This lean business case documents epic vision, hypothesis statement (we believe that [building this solution] will result in [this outcome] as measured by [these metrics]), MVP scope, cost estimates (typically using t-shirt sizing or story points), expected ROI/business value, implementation timeline, key assumptions, risks, and dependencies. Following Lean-Agile principles and portfolio Kanban practices, the epic charter enables portfolio leadership, Product Management, Enterprise Architects, and Agile Release Trains (ARTs) to make informed investment decisions, approve epic funding, prioritize portfolio backlogs, and align teams around common strategic objectives.

### Strategic Importance

- **Formal Authorization**: Provides legitimate mandate from executive sponsors and stakeholders
- **Scope Clarity**: Defines clear boundaries for what is included and excluded
- **Authority Definition**: Establishes decision-making rights and escalation paths
- **Resource Commitment**: Secures commitment of necessary resources and support
- **Stakeholder Alignment**: Creates shared understanding of objectives and approach

## Purpose & Scope

### Primary Purpose

This artifact serves as the lightweight business case and authorization document for large initiatives (epics), defining the business problem, solution hypothesis, expected outcomes, success metrics, MVP scope, investment estimate, and go/no-go criteria. It enables portfolio-level decision-making on epic approval, funding, and prioritization within Lean Portfolio Management processes.

### Scope

**In Scope**:
- Epic vision and strategic alignment with portfolio themes
- Business problem statement and current pain points
- Solution hypothesis (we believe... will result in... as measured by...)
- Target customers/users and their needs (Jobs-to-be-Done)
- Proposed solution approach and architecture runway
- MVP scope and key capabilities/features
- Expected business outcomes and success metrics (leading and lagging indicators)
- Cost estimate (t-shirt size, story points, or range)
- Expected ROI and business value (revenue impact, cost savings, risk reduction)
- Implementation timeline and release strategy
- Key assumptions, risks, and dependencies
- Epic ownership and stakeholder identification
- Go/no-go decision criteria for epic approval
- Portfolio Kanban workflow states (funnel, reviewing, analyzing, portfolio backlog, implementing)
- Enabler epics vs. business epics distinction

**Out of Scope**:
- Detailed feature specifications (decomposed from epic after approval)
- Detailed user stories and acceptance criteria
- Technical implementation details and architecture designs
- Detailed project plans and sprint schedules
- Comprehensive risk management plans (high-level risks only)
- Detailed resource allocation and team assignments

### Target Audience

**Primary Audience**:
- Portfolio Management who approve epic funding and prioritization
- Product Management who define epic vision and business value
- Epic Owners who author and champion epic proposals
- Business Owners who validate business outcomes and ROI
- Enterprise Architects who assess technical feasibility and runway

**Secondary Audience**:
- Lean Portfolio Management teams who manage portfolio Kanban
- Release Train Engineers who plan epic implementation across ARTs
- Agile Teams who will implement epic features
- Program Managers who coordinate epic delivery
- Finance teams who validate investment and ROI calculations
- Executive stakeholders who provide strategic direction

## Document Information

**Format**: Markdown

**File Pattern**: `*.epic-charter.md`

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

**Hypothesis-Driven**: Frame epic as testable hypothesis (we believe X will result in Y as measured by Z)
**Lean Business Case**: Keep lightweight; avoid traditional heavy business case documentation
**Outcome-Focused**: Define success by business outcomes and metrics, not outputs or features
**MVP Definition**: Clearly define minimum viable product scope for initial validation
**Leading/Lagging Indicators**: Specify both leading (predictive) and lagging (outcome) success metrics
**Jobs-to-be-Done**: Frame epic around customer jobs and desired outcomes, not solutions
**T-Shirt Sizing**: Use relative sizing (XS, S, M, L, XL) for initial cost estimates
**WSJF Prioritization**: Use Weighted Shortest Job First (cost of delay / duration) for epic prioritization
**Portfolio Kanban**: Move epic through portfolio Kanban states (funnel, reviewing, analyzing, backlog, implementing)
**Epic Owner**: Assign dedicated epic owner responsible for championing and coordinating epic
**Dependency Mapping**: Identify dependencies on other epics, ARTs, suppliers, or external systems
**Architecture Runway**: Ensure sufficient architecture runway exists or create enabler epics
**Incremental Funding**: Use incremental funding with go/no-go gates rather than full upfront commitment
**Business Epic vs. Enabler Epic**: Distinguish customer-facing business epics from technical enabler epics
**Strategic Themes Alignment**: Align epic with portfolio strategic themes and enterprise strategy
**Stakeholder Identification**: Identify all key stakeholders including customers, users, business owners
**Risk Assessment**: Identify top 3-5 risks with mitigation strategies
**Feature Decomposition**: Decompose epic into features only after epic approval
**Regular Review**: Review epic status and metrics during portfolio sync meetings
**Pivot or Persevere**: Use metrics to make data-driven decisions to pivot, persevere, or stop epic
**Epic Hypothesis Canvas**: Use visual canvas format (SAFe epic hypothesis canvas) for lightweight documentation

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

**Scaled Agile Frameworks**:
- SAFe (Scaled Agile Framework): Epic definition, portfolio Kanban, lean business case
- SAFe Epic Hypothesis Statement: Structured format for epic hypotheses
- SAFe Lean Portfolio Management: Portfolio-level epic approval and funding
- SAFe Portfolio Kanban: Epic workflow states (funnel, reviewing, analyzing, backlog, implementing)
- LeSS (Large-Scale Scrum): Large product development coordination
- Disciplined Agile (DA): Enterprise agile framework
- Nexus: Scaled Scrum framework for multiple teams
- Scrum@Scale: Scalable Scrum framework

**Agile Portfolio Management**:
- Lean Portfolio Management: Portfolio strategy, investment funding, Agile governance
- Portfolio Kanban System: Visualizing and managing portfolio epic flow
- Epic Approval Process: Lean business case review and funding decision
- WSJF (Weighted Shortest Job First): Economic prioritization framework
- Cost of Delay: Economic impact of delaying features
- Participatory Budgeting: Collaborative funding allocation
- Beyond Budgeting: Adaptive management approach

**Epic Management Tools**:
- Jira Align (formerly AgileCraft): Enterprise agile planning and portfolio management
- Azure DevOps: Epic, feature, and user story hierarchy
- Rally (Broadcom): Agile portfolio and program management
- VersionOne (Digital.ai): Enterprise agile planning platform
- Targetprocess: Visual agile management platform
- Planview AgilePlace: Lean portfolio management
- CA Agile Central: Enterprise agile management
- ServiceNow Strategic Portfolio Management: IT portfolio management

**Lean and Business Case Frameworks**:
- Lean Startup: Build-Measure-Learn, hypothesis-driven development
- Lean Canvas: One-page business model (Ash Maurya)
- Business Model Canvas: Value proposition and business model (Osterwalder)
- Value Proposition Canvas: Customer jobs, pains, gains alignment
- Hypothesis-Driven Development: Testable assumptions and validation
- Minimum Viable Product (MVP): Smallest product to test hypotheses
- Pivot or Persevere: Data-driven epic continuation decisions

**Epic Sizing and Estimation**:
- T-Shirt Sizing: Relative sizing (XS, S, M, L, XL, XXL)
- Story Points: Relative effort estimation using Fibonacci sequence
- Epic Splitting: Breaking large epics into smaller testable increments
- Story Mapping: User story mapping to define epic scope (Jeff Patton)
- Three Amigos: Collaborative estimation (business, development, testing)

**Strategic Alignment**:
- Portfolio Strategic Themes: Long-term strategic differentiation areas
- OKRs (Objectives and Key Results): Goal-setting framework
- Hoshin Kanri: Strategic policy deployment (X-Matrix)
- Balanced Scorecard: Strategic performance measurement
- V2MOM (Salesforce): Vision, Values, Methods, Obstacles, Measures

**Jobs-to-be-Done Framework**:
- Clayton Christensen JTBD: Understanding customer motivations
- Outcome-Driven Innovation: Tony Ulwick's systematic innovation
- Job Stories: Alternative to user stories focused on situations and motivations
- Progress-Making Forces: Push, pull, anxiety, habit forces

**Metrics and Measurement**:
- Leading Indicators: Predictive metrics (engagement, adoption, NPS)
- Lagging Indicators: Outcome metrics (revenue, cost savings, customer retention)
- Pirate Metrics (AARRR): Acquisition, Activation, Retention, Revenue, Referral
- North Star Metric: Single metric that best captures core value
- OKR Measurement: Objective and measurable key results
- Innovation Accounting (Lean Startup): Validated learning metrics

**Risk and Dependency Management**:
- Risk-Adjusted Backlog: Prioritizing based on risk and value
- Dependency Matrix: Mapping epic dependencies across ARTs
- Program Increment (PI) Planning: Coordinating dependencies across teams
- ART Coordination: Aligning Agile Release Trains for epic delivery
- Supplier/Vendor Dependencies: External dependency management

**SAFe Epic Components**:
- Business Epic: Customer-facing value delivery
- Enabler Epic: Architecture, infrastructure, or compliance work
- Epic Owner: Responsible for epic definition and coordination
- Epic Hypothesis Statement: For [customers], who [statement of need], the [solution] is a [product category] that [key benefit]. Unlike [primary competitive alternative], our solution [statement of primary differentiation]
- Lean Business Case: Lightweight epic justification
- MVP Definition: Minimum Marketable Feature set

**Agile Governance**:
- Portfolio Sync: Regular portfolio leadership review
- Epic Review and Approval: Governance gate for epic funding
- Participatory Budget Allocation: Team-based funding decisions
- Guardrails: Investment and spending boundaries
- Epic Progress Reviews: Regular status and metrics review

**Enterprise Agile Practices**:
- Agile Release Train (ART): Long-lived team of Agile teams
- Solution Train: Coordination of multiple ARTs for large solutions
- Program Increment (PI): Fixed timebox for planning and delivery
- Inspect and Adapt: PI-level retrospective and adaptation
- Architecture Runway: Technical enablement for upcoming features

**Related Methodologies**:
- Design Thinking: Human-centered problem solving
- Lean UX: Iterative user experience design
- DevOps: Development and operations collaboration
- Continuous Delivery: Frequent, reliable releases
- Feature Toggles: Incremental feature rollout

**Academic and Industry References**:
- "SAFe 6.0 Distilled" by Richard Knaster and Dean Leffingwell
- "The Lean Startup" by Eric Ries
- "Competing Against Luck" by Clayton Christensen (JTBD)
- "Escaping the Build Trap" by Melissa Perri
- Scaled Agile Framework official guidance (scaledagileframework.com)

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
