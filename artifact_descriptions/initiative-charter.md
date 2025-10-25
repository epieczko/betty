# Name: initiative-charter

## Executive Summary

The Initiative Charter is a formal authorization and strategic planning document that establishes the business case, objectives, scope, success metrics, governance, and resource commitments for strategic initiatives. This foundational artifact aligns executive sponsors, cross-functional teams, and stakeholders on the initiative's hypothesis, expected outcomes measured through OKRs, RACI accountability, dependencies, and investment thesis, providing the legitimate mandate and strategic direction for execution.

Grounded in OKR frameworks (Objectives and Key Results), hypothesis-driven development, and investment governance practices, this charter transforms strategic intent into actionable plans with measurable success criteria. It defines RACI for initiative governance, identifies dependencies and risks, establishes investment amounts and ROI expectations, and connects initiative goals to organizational North Star metrics and strategic pillars, ensuring alignment, accountability, and evidence-based decision-making throughout the initiative lifecycle.

### Strategic Importance

- **OKR Alignment**: Links initiative goals to organizational OKRs and North Star metrics
- **Hypothesis and Validation**: Frames initiative as testable hypothesis with measurable outcomes
- **Success Metrics**: Defines specific, measurable Key Results for tracking progress and impact
- **RACI Governance**: Establishes clear accountability (Driver, Approver, Contributors, Informed)
- **Dependency Mapping**: Identifies cross-team dependencies and sequencing constraints
- **Investment Thesis**: Articulates expected ROI, strategic value, and resource requirements
- **Risk Management**: Documents key risks, assumptions, and mitigation strategies

## Purpose & Scope

### Primary Purpose

This artifact provides formal authorization and strategic direction for initiatives by defining objectives, measurable success criteria, governance accountability, dependencies, and investment thesis, enabling aligned execution and evidence-based decision-making.

### Scope

**In Scope**:
- Business case and problem statement: what problem are we solving and why it matters
- Hypothesis: testable assumption about how solution will achieve desired outcomes
- OKR alignment: how initiative connects to organizational Objectives and Key Results
- Success metrics: specific Key Results, North Star metric, DORA metrics, customer outcomes
- RACI for governance: Driver, Approver, Contributor, Informed roles
- Scope definition: what's included, what's explicitly excluded
- Dependencies: cross-team dependencies, infrastructure needs, external dependencies
- Resource requirements: team allocation, budget, timeline
- Investment thesis: expected ROI, strategic value, opportunity cost
- Risk and assumptions: key risks, mitigation strategies, critical assumptions
- Governance cadence: steering committee, check-ins, decision-making forums
- Exit criteria: when to declare success, when to pivot or kill

**Out of Scope**:
- Detailed project plans and sprint-level tasks (use project management tools)
- Team organizational structure (see team-topology-map)
- Service ownership definitions (see ownership-charters)
- Detailed workstream RACI (see raci-per-workstream)
- Individual skills and capacity (see skills-matrix, time-allocation-worksheets)
- Stakeholder engagement details (see stakeholder-map)

### Target Audience

**Primary Audience**:
- Engineering Managers and Product Leaders defining and executing strategic initiatives
- Program Managers coordinating cross-functional initiatives
- Executive sponsors approving and overseeing strategic investments
- Portfolio Leaders prioritizing initiatives and allocating resources

**Secondary Audience**:
- Team Leads understanding how their work contributes to strategic goals
- Finance teams tracking investment and ROI
- Stakeholders understanding initiative direction and success criteria
- Governance boards reviewing and approving strategic initiatives

## Document Information

**Format**: Markdown

**File Pattern**: `*.initiative-charter.md`

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

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use approved templates to ensure completeness and consistency across teams
**Peer Review**: Have at least one qualified peer review before submitting for approval
**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management
**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in
**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon
**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively
**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation
**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes
**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats
**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates
**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy
**Charter Development Best Practices**:
- **Problem-First**: Start with clear problem statement and business case, not solution
- **Hypothesis-Driven**: Frame as testable hypothesis with validation criteria
- **SMART Objectives**: Specific, Measurable, Achievable, Relevant, Time-bound OKRs
- **One-Page Summary**: Create executive summary that fits on one page for busy stakeholders
- **Explicit Trade-offs**: Document what you're NOT doing and why (scope, resources, timing)
- **Stakeholder Co-Creation**: Develop charter collaboratively with key stakeholders
- **Evidence-Based**: Ground business case in data, customer research, market analysis

**OKR Definition**:
- **Compelling Objective**: Qualitative, inspirational, time-bound goal (e.g., "Delight customers with instant search")
- **Measurable Key Results**: 3-5 quantitative outcomes that prove Objective achieved
- **Outcome-Focused**: Measure outcomes (customer value, business impact), not outputs (features shipped)
- **Ambitious but Achievable**: Stretch goals (target 70% achievement) vs. committed goals (100% expected)
- **Aligned Upward**: Connect to organizational OKRs and North Star metric
- **Quarterly Cadence**: Set Key Results for quarter; review and adjust each cycle

**Success Metrics Selection**:
- **North Star Metric**: Single metric capturing customer value (e.g., weekly active users, orders completed)
- **Input Metrics**: Leading indicators driving North Star (activation rate, feature adoption)
- **DORA Metrics**: Deployment frequency, lead time, MTTR, change failure rate for engineering health
- **Business Metrics**: Revenue, cost savings, conversion rate, market share
- **Customer Metrics**: NPS, CSAT, retention, lifetime value
- **Lagging vs. Leading**: Balance outcome metrics with predictive indicators

**RACI and Accountability**:
- **Driver/Owner**: Single person accountable for initiative success (DRI/Accountable)
- **Approver**: Who has authority to approve major decisions and scope changes
- **Contributors**: Teams and individuals doing the work (Responsible)
- **Informed**: Stakeholders who need updates but don't contribute (see stakeholder-map)
- **Escalation Path**: Clear chain for resolving blockers and disagreements
- **Decision Rights**: Document who can make what decisions (RAPID framework)

**Dependency and Risk Management**:
- **Dependency Mapping**: Identify all cross-team dependencies with owners and timing
- **Critical Path**: Highlight dependencies on critical path that could delay initiative
- **Risk Register**: Top 5-10 risks with probability, impact, mitigation strategy
- **Assumptions**: Document critical assumptions requiring validation
- **Pre-Mortem**: Imagine failure scenarios to identify risks proactively
- **Mitigation Plans**: Specific actions to reduce risk probability or impact

**Investment Thesis**:
- **Resource Requirements**: FTE allocation, budget, infrastructure, vendor costs
- **Expected ROI**: Quantified return on investment (revenue, cost savings, strategic value)
- **Payback Period**: Time to recoup investment
- **Opportunity Cost**: What we're NOT doing to invest in this initiative
- **Strategic Value**: Non-financial benefits (competitive advantage, platform capabilities, market position)
- **Investment Horizons**: Horizon 1 (current business), Horizon 2 (emerging), Horizon 3 (future)

**Scope Management**:
- **MVP Scope**: Minimum to validate hypothesis and deliver value
- **Explicit Exclusions**: Document what's out of scope to prevent scope creep
- **Phase Planning**: Break large initiatives into phased releases
- **Change Control**: Process for approving scope changes with impact assessment
- **Done Criteria**: Clear definition of when initiative is complete

**Governance and Oversight**:
- **Steering Committee**: Executive oversight, decision authority, meeting cadence
- **Check-In Cadence**: Weekly standups, monthly reviews, quarterly planning
- **Status Reporting**: Red/yellow/green health on scope, schedule, resources, quality
- **Decision-Making**: How decisions are made and escalated
- **Exit Criteria**: Conditions to declare success, pivot, or kill initiative

**Stakeholder Alignment**:
- **Executive Sponsorship**: Secure visible, active sponsor with authority
- **Stakeholder Map**: Reference stakeholder-map artifact for engagement strategy
- **Communication Plan**: How and when stakeholders are updated
- **Change Management**: Address organizational change and adoption
- **Resistance Planning**: Anticipate and address resistance from affected parties

**Executive Sponsorship**: Ensure visible executive sponsorship and regular executive review
**Governance Alignment**: Align with organizational OKRs, strategic pillars, portfolio priorities
**Metric-Driven**: Track OKRs, Key Results, North Star metric, DORA metrics quarterly
**Dependency Management**: Explicitly identify and track dependencies; resolve blockers
**Risk Integration**: Maintain risk register; escalate risks to steering committee
**Change Control**: Formal process for scope changes with impact assessment and approval
**Audit Trail**: Document decisions, changes, and rationale for governance and learning

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

**OKR (Objectives and Key Results) Frameworks**:
- OKR fundamentals: Objectives (qualitative goals), Key Results (measurable outcomes)
- Measure What Matters (John Doerr): OKR best practices from Google and Intel
- Committed vs. aspirational OKRs: must-achieve vs. stretch goals
- OKR cadence: quarterly Key Results, annual Objectives
- Scoring OKRs: 0-1.0 scale, target 0.7 for aspirational OKRs
- CFRs (Conversations, Feedback, Recognition): continuous performance management with OKRs

**North Star Framework**:
- North Star metric: single metric that best captures customer value delivered
- Input metrics: leading indicators that drive North Star metric
- Customer outcome focus: value to customers vs. vanity metrics
- Product-market fit indicators: retention, engagement, activation
- Growth accounting: new, retained, churned, resurrected users

**Strategic Alignment Models**:
- V2MOM (Salesforce): Vision, Values, Methods, Obstacles, Measures
- Hoshin Kanri (Strategy Deployment): cascading strategic goals
- Balanced Scorecard: financial, customer, internal process, learning perspectives
- Strategy maps: cause-and-effect relationships between strategic objectives
- Jobs-to-be-Done: customer jobs and desired outcomes

**Hypothesis-Driven Development**:
- Lean Startup: Build-Measure-Learn cycle
- Hypothesis statement: If [action], then [outcome], because [rationale]
- Validation criteria: measurable thresholds for hypothesis validation
- Pivot or persevere: data-driven decision to continue, pivot, or kill
- Minimum Viable Product (MVP): smallest thing to test hypothesis
- A/B testing and experimentation: measuring impact

**Accountability and Governance**:
- RACI for initiatives: Responsible, Accountable, Consulted, Informed
- DACI (Intuit): Driver, Approver, Contributor, Informed - emphasizes driver
- RAPID (Bain): Recommend, Agree, Perform, Input, Decide - decision authority
- DRI (Directly Responsible Individual): single owner for initiatives
- Steering committees: executive oversight and decision-making forums
- Governance cadence: weekly standups, monthly reviews, quarterly planning

**Dependency Management**:
- Critical path analysis: identifying sequencing constraints
- Dependency mapping: visualizing cross-team dependencies
- Parallel vs. sequential work: maximizing parallelization
- External dependencies: third-party vendors, partnerships, regulatory approvals
- Platform dependencies: infrastructure, capabilities, shared services needed
- Dependency resolution: strategies to mitigate or eliminate dependencies

**Investment and Portfolio Management**:
- Investment thesis: expected return, strategic value, opportunity cost
- ROI calculation: return on investment for initiatives
- Payback period: time to recoup investment
- Portfolio optimization: balancing initiatives across risk, return, strategic alignment
- Three horizons model: current business, emerging opportunities, future options
- Resource allocation: FTE allocation, budget, time commitment

**Success Metrics and Measurement**:
- SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound
- Leading vs. lagging indicators: predictive metrics vs. outcome metrics
- DORA metrics: deployment frequency, lead time, MTTR, change failure rate
- AARRR (Pirate Metrics): Acquisition, Activation, Retention, Revenue, Referral
- Customer metrics: NPS, CSAT, retention, lifetime value
- Business metrics: revenue, cost reduction, time savings, market share

**Risk Management**:
- Risk register: identifying, assessing, and mitigating risks
- Risk probability and impact: high/medium/low classification
- Assumption documentation: critical assumptions requiring validation
- Pre-mortem analysis: imagining failure to identify risks
- Mitigation strategies: avoid, transfer, mitigate, accept
- Risk monitoring: tracking risk indicators and triggers

**Scope Management**:
- Scope definition: clear boundaries of what's included and excluded
- Scope creep prevention: change control and scope management practices
- MVP scope: minimum features to validate hypothesis
- Phased delivery: breaking large initiatives into incremental releases
- Out-of-scope documentation: explicitly stating what won't be delivered

**Agile and Lean Principles**:
- Agile manifesto values: individuals, working software, collaboration, responding to change
- Lean principles: eliminate waste, amplify learning, decide late, deliver fast
- Incremental delivery: delivering value in small increments
- Continuous improvement: inspect and adapt based on feedback
- Fail fast: rapid experimentation and learning from failures

**Product Management Frameworks**:
- Product vision: long-term direction and purpose
- Product strategy: how to achieve vision
- Product roadmap: sequenced initiatives aligned to strategy
- Feature prioritization: RICE (Reach, Impact, Confidence, Effort), MoSCoW
- Product discovery: continuous learning about customer needs
- Product-market fit: evidence that product solves real problem

**Change Management**:
- Kotter's 8 steps: urgency, coalition, vision, communication, obstacles, wins, anchoring
- ADKAR: Awareness, Desire, Knowledge, Ability, Reinforcement
- Change impact assessment: understanding who and what is affected
- Adoption metrics: measuring change adoption and resistance
- Communication planning: targeted messaging for change

**Governance and Oversight**:
- Stage gates: go/no-go decision points
- Investment review boards: portfolio governance and prioritization
- Quarterly business reviews (QBRs): stakeholder updates and strategic alignment
- Health checks: red/yellow/green status on scope, schedule, resources, quality
- Escalation paths: when and how to escalate issues

**Tools and Templates**:
- OKR tracking tools: Lattice, 15Five, Weekdone, spreadsheets
- Project management: Jira, Asana, Monday.com for initiative tracking
- Roadmap tools: ProductBoard, Aha!, Roadmunk
- Business case templates: financial models, cost-benefit analysis
- Charter templates: standardized initiative charter formats

**Related Standards**:
- PMI PMBOK: Project charter and project management standards
- PRINCE2: Project initiation documentation
- SAFe: Program Increment (PI) planning and objectives
- ISO 21500: Project management guidance
- Agile frameworks: Scrum, Kanban, SAFe initiative planning

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
