# Name: decision-log

## Executive Summary

The Decision Log is a structured governance artifact that captures critical decisions, their rationale, alternatives considered, decision-makers, and outcomes throughout an initiative. Similar to Architectural Decision Records (ADRs) in software development, this log applies decision frameworks like DACI (Driver, Approver, Contributor, Informed) and RAPID (Recommend, Agree, Perform, Input, Decide) to ensure accountability and traceability.

Modern decision logs are maintained in collaboration platforms (Confluence, Jira, Notion) and leverage decision-making methodologies including decision journals (Annie Duke), pre-mortems (Gary Klein), Cost of Delay (Don Reinertsen), and the Cynefin framework for complexity assessment. The log serves executive leadership, product leaders, and program managers by providing an audit trail for governance, enabling retrospective analysis, and supporting lessons learned. It captures not just what was decided, but why, by whom, and what alternatives were rejected.

### Strategic Importance

- **Governance Excellence**: Demonstrates rigorous program management and adherence to organizational standards
- **Risk Mitigation**: Early identification of patterns and trends enables proactive intervention
- **Audit Readiness**: Provides comprehensive trail for internal and external audits
- **Knowledge Capture**: Preserves institutional knowledge beyond individual personnel tenure
- **Continuous Improvement**: Enables data-driven process improvements through trend analysis

## Purpose & Scope

### Primary Purpose

The Decision Log creates a transparent, searchable record of significant decisions throughout an initiative, capturing the decision context, rationale, alternatives considered, decision-makers (using DACI or RAPID frameworks), and outcomes. It enables accountability, supports audit requirements, facilitates knowledge transfer, and provides input for retrospectives and post-implementation reviews. The log answers: What was decided? Why? By whom? What else was considered? What happened?

### Scope

**In Scope**:
- Strategic decisions (scope, approach, architecture, investment, priority)
- Decision record structure (context, decision, rationale, alternatives, consequences)
- Decision-maker identification using DACI or RAPID frameworks
- Alternatives considered and reasons for rejection
- Decision date, status (proposed, accepted, superseded, deprecated)
- Cost of Delay considerations for prioritization decisions
- Risk-based decision rationale
- Outcomes and retrospective analysis
- Decision dependencies and relationships
- Links to supporting artifacts (business cases, feasibility studies, technical designs)

**Out of Scope**:
- Day-to-day tactical decisions (unless significant impact)
- Meeting minutes (covered in Meeting Minutes, Steering Committee Minutes)
- Detailed technical specifications (covered in Technical Design Documents)
- Change requests (covered in Change Log, Change Request artifacts)
- Risk details (covered in Risk Register)

### Target Audience

**Primary Audience**:
- **Executive Leadership**: Reviews strategic decisions, accountability, and alignment with strategy
- **Program Managers**: Tracks decisions affecting program scope, schedule, and resources
- **Product Leaders**: Documents product strategy and prioritization decisions

**Secondary Audience**:
- **Governance & Audit Teams**: Reviews decision-making process and accountability
- **Portfolio Management**: Assesses decision quality and portfolio alignment
- **Future Teams**: Learns from historical decisions and rationale (onboarding, knowledge transfer)

## Document Information

**Format**: Markdown

**File Pattern**: `*.decision-log.md`

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
**DACI/RAPID Clarity**: Explicitly identify decision-maker roles using DACI or RAPID framework for every decision
**Capture Alternatives**: Document alternatives considered and why they were rejected (avoid hindsight bias)
**Timely Recording**: Log decisions immediately while context is fresh; don't wait for formal documentation
**Decision Context**: Always capture the context that drove the decision (constraints, information available, urgency)
**Status Tracking**: Track decision status (proposed, accepted, superseded, deprecated) and update when changed
**Link to Outcomes**: Circle back to record actual outcomes versus expected (enable retrospective learning)
**Pre-Mortem Practice**: Use pre-mortem analysis for major decisions to identify potential failure modes
**Cost of Delay**: Apply Cost of Delay framework for prioritization decisions to make trade-offs explicit
**Bias Awareness**: Train decision-makers on cognitive biases; use devil's advocate or red team approaches
**Searchable Format**: Maintain in searchable format (Confluence, Notion) with tags and categories
**ADR Format**: Consider using ADR (Architectural Decision Record) format for technical decisions
**Decision Journals**: Encourage leaders to maintain decision journals (Annie Duke methodology) for learning
**Escalation Criteria**: Define clear criteria for when decisions need escalation to higher authority
**Reversibility Assessment**: Note whether decisions are reversible or irreversible (Type 1 vs Type 2 - Jeff Bezos)
**Regular Review**: Review decision log in retrospectives to improve decision-making quality over time

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

**Decision Framework Methodologies**:
- DACI (Driver, Approver, Contributor, Informed) - Intuit decision-making framework
- RAPID (Recommend, Agree, Perform, Input, Decide) - Bain & Company framework
- RACI (Responsible, Accountable, Consulted, Informed) - Traditional responsibility matrix
- Decision Rights Framework - Who decides what
- Delegated Decision-Making - Spotify/Agile models
- Escalation frameworks and criteria

**Decision Record Formats**:
- ADR (Architectural Decision Records) - Michael Nygard format
- MADR (Markdown ADR) - Lightweight decision records
- Y-Statements - "In the context of [use case/user story], facing [concern], we decided for [option] to achieve [quality], accepting [downside]"
- Decision record templates (context, decision, status, consequences)
- RFC (Request for Comments) processes

**Decision-Making Methodologies**:
- Decision Journals - Annie Duke ("Thinking in Bets")
- Pre-mortem Analysis - Gary Klein methodology
- Prospective Hindsight - Imagining future failure
- Cost of Delay (CD3) - Don Reinertsen (weighted shortest job first)
- Cynefin Framework - Dave Snowden (complexity-based decision approach)
- OODA Loop (Observe, Orient, Decide, Act) - John Boyd
- Recognize-Analyze-Decide - Naturalistic decision making

**Prioritization & Trade-off Frameworks**:
- WSJF (Weighted Shortest Job First) - SAFe prioritization
- Cost of Delay Divided by Duration (CD3)
- Value vs. Effort matrices
- RICE Scoring (Reach, Impact, Confidence, Effort) - Intercom
- MoSCoW Prioritization (Must, Should, Could, Won't)
- Kano Model - Feature prioritization
- ICE Scoring (Impact, Confidence, Ease)

**Decision Quality Frameworks**:
- Decision Quality Chain - Strategic Decisions Group
- Six Elements of Decision Quality
- Expected Value calculations
- Probability-weighted outcomes
- Bayesian decision theory
- Multi-criteria decision analysis (MCDA)

**Governance & Accountability**:
- Decision authority matrices
- Governance decision gates
- Stage-Gate decision processes
- Investment decision frameworks
- Portfolio Kanban decision points (SAFe)
- Approval workflows and delegation

**Cognitive Bias Awareness**:
- Confirmation bias mitigation
- Sunk cost fallacy awareness
- Anchoring bias
- Availability heuristic
- Groupthink prevention techniques
- Red team / blue team approaches
- Devil's advocate methodology

**Collaborative Decision Tools**:
- Confluence - Decision documentation and tracking
- Jira - Decision tracking as stories/epics
- Notion - Decision log databases
- Miro/Mural - Decision-making workshops, pre-mortems
- ProductBoard - Product decision tracking
- Aha! - Strategic decision documentation

**Quality & Retrospective Analysis**:
- Decision effectiveness metrics
- Retrospective decision analysis
- Lessons learned from decisions
- Decision velocity tracking
- Decision reversal rates
- Time to decision metrics

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
