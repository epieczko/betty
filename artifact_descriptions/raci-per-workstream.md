# Name: raci-per-workstream

## Executive Summary

The RACI per Workstream artifact is a responsibility assignment matrix that clearly defines who is Responsible, Accountable, Consulted, and Informed for each major activity, decision, or deliverable within initiatives and projects. This critical governance tool eliminates role confusion, prevents ownership gaps, and ensures cross-functional alignment by making decision rights and accountability explicit across Engineering, Product, Design, Security, and other teams.

Building on the RACI framework (Responsible-Accountable-Consulted-Informed) and related models like RAPID (Bain) and DACI (Intuit), this artifact maps organizational roles to workstreams, clarifying who does the work (Responsible), who has final approval authority (Accountable), who provides input (Consulted), and who needs to be kept informed. It supports efficient decision-making, reduces bottlenecks, and enables autonomous teams by establishing clear accountability boundaries for complex, cross-functional initiatives.

### Strategic Importance

- **Decision Rights Clarity**: Eliminates confusion about who makes decisions and who executes
- **Accountability Definition**: Ensures every workstream activity has exactly one Accountable owner
- **Cross-Functional Alignment**: Coordinates responsibilities across Engineering, Product, Design, Security teams
- **Approval Path Optimization**: Streamlines approval workflows by clarifying Consulted vs. Informed roles
- **Bottleneck Reduction**: Identifies decision-making choke points and over-consulted stakeholders
- **Organizational Efficiency**: Enables faster execution by making responsibility boundaries explicit
- **Governance Transparency**: Provides clear audit trail of decision authority and accountability

## Purpose & Scope

### Primary Purpose

This artifact establishes clear decision rights and execution accountability across cross-functional workstreams using RACI (Responsible-Accountable-Consulted-Informed) framework. It eliminates ambiguity about who owns what, who approves decisions, who must be consulted, and who simply needs to be informed, enabling efficient execution and reducing organizational friction.

### Scope

**In Scope**:
- RACI assignments: Responsible, Accountable, Consulted, Informed per major activity
- Workstream decomposition: key activities, deliverables, and decision points
- Cross-functional coordination: Engineering, Product, Design, Security, Legal, Compliance roles
- Decision rights matrix: who has authority to approve, recommend, or provide input
- Approval workflows: routing for architecture decisions, security reviews, compliance sign-offs
- Escalation paths: when consensus fails, who has decision authority
- Stakeholder engagement model: which roles must be consulted vs. simply informed
- Dependency management: identifying cross-workstream coordination needs
- Alternative frameworks: RAPID (Recommend-Agree-Perform-Input-Decide), DACI (Driver-Approver-Contributor-Informed)

**Out of Scope**:
- Service ownership and operational accountability (see ownership-charters)
- Team organizational structure and topologies (see team-topology-map)
- Individual skills and competency assessments (see skills-matrix)
- Time allocation and capacity planning (see time-allocation-worksheets)
- Overall initiative governance (see initiative-charter)

### Target Audience

**Primary Audience**:
- Engineering Managers coordinating cross-functional delivery
- Product Leaders clarifying decision authority and stakeholder involvement
- Team Leads understanding their workstream responsibilities and decision rights
- Program Managers orchestrating complex, multi-team initiatives

**Secondary Audience**:
- Individual Contributors understanding approval paths and stakeholder consultation requirements
- Architecture teams clarifying review and approval roles
- Security and Compliance teams defining their consultation and approval authority
- Organizational Designers optimizing decision-making efficiency

## Document Information

**Format**: Markdown

**File Pattern**: `*.raci-per-workstream.md`

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
**RACI Assignment Best Practices**:
- **One Accountable**: Each activity must have exactly one Accountable person (never zero, never multiple)
- **Clear Responsible**: Define who does the work; can be multiple people but needs coordination
- **Minimize Consulted**: Over-consultation slows decisions; consult only when input truly needed
- **Right-Size Informed**: Inform those who need to know; avoid over-communicating to reduce noise
- **Combine R and A**: When possible, same person/team should be Responsible and Accountable
- **Avoid RACI Gaps**: Every workstream activity must have assigned roles; no blank cells
- **Resolve Conflicts**: Address disagreements about assignments before finalizing matrix

**Decision Authority Clarity**:
- **Accountable Owns Outcome**: Accountable person has final decision authority and accountability
- **Consulted Provides Input**: Consultation is two-way dialogue; Accountable must seek their input
- **Informed Receives Updates**: One-way communication; no input required or expected
- **Escalation Path**: Define who breaks ties when Accountable and Consulted disagree
- **Delegation Clarity**: Document when Accountable delegates decision-making to Responsible
- **Time Boundaries**: Specify consultation and approval SLAs to prevent bottlenecks

**Cross-Functional Coordination**:
- **Engineering-Product Alignment**: Clarify Product's decision authority on what/why, Engineering on how
- **Security Gates**: Define when Security is Consulted (design review) vs. Accountable (approval)
- **Architecture Review**: Specify ARB as Consulted for guidance vs. Approver for standards compliance
- **Design Involvement**: Clarify when Design is Responsible vs. Consulted
- **Legal/Compliance**: Define approval authority for contracts, privacy, regulatory requirements
- **Platform Teams**: Specify platform team consultation for infrastructure and standards

**Process Efficiency**:
- **Parallel Consultation**: Consult multiple stakeholders in parallel, not sequentially
- **Asynchronous Reviews**: Use RFCs, design docs, pull requests for asynchronous input
- **Decision Logs**: Document decisions and rationale in ADRs, reducing re-consultation
- **Informed Automation**: Use Slack, email, dashboards for automatic status updates
- **Pre-Approval Patterns**: Pre-approve common scenarios to reduce approval overhead
- **Lightweight Reviews**: Risk-based review depth (quick review for low risk, thorough for high)

**Organizational Patterns**:
- **DRI Model**: Assign Directly Responsible Individuals for clear accountability
- **Product Trio**: Product Manager (Accountable for what), Designer (Responsible for UX), Tech Lead (Responsible for how)
- **Agile Roles**: Product Owner (Accountable for backlog), Scrum Master (Responsible for process), Team (Responsible for delivery)
- **Platform Service Model**: Platform Accountable for capabilities, stream-aligned teams Responsible for consumption
- **Security Champions**: Embedded security role for consultation, CISO org Accountable for approval

**Tools and Visualization**:
- **Visual RACI Matrix**: Use color coding (R=blue, A=red, C=yellow, I=green) for clarity
- **RACI Templates**: Start with Miro, Mural, or Excel templates for consistency
- **Integration with Tools**: Link RACI to Jira workflows, approval routing in tools
- **Regular Review**: Update RACI quarterly or when organizational changes occur
- **Complexity Analysis**: Flag activities with too many Consulted roles for simplification

**Executive Sponsorship**: Ensure visible executive sponsorship and regular executive review
**Governance Alignment**: Align with organizational governance framework and decision-making bodies
**Metric-Driven**: Track decision cycle time, approval SLA adherence, bottleneck identification
**Dependency Management**: Explicitly identify and track dependencies on other initiatives or resources
**Risk Integration**: Integrate with risk management processes; escalate risks appropriately
**Audit Trail**: Maintain comprehensive audit trail for governance and compliance purposes

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

**Responsibility Assignment Frameworks**:
- RACI Matrix: Responsible (does the work), Accountable (final authority), Consulted (input), Informed (notified)
- RAPID (Bain): Recommend, Agree, Perform, Input, Decide - emphasizes decision authority
- DACI (Intuit): Driver, Approver, Contributor, Informed - focuses on driver ownership
- RASCI: Adds "Support" role for those providing resources
- RACI-VS: Adds "Verify" (quality check) and "Sign-off" (formal approval)
- Responsibility Assignment Matrix (RAM): Generic term for role-to-task mapping
- Linear Responsibility Chart (LRC): Visual representation of RACI assignments

**Decision-Making Frameworks**:
- Decision Rights Framework: clarity on who makes which decisions
- Delegation of Authority (DOA): formal delegation levels and limits
- Consensus Decision-Making: when and how to seek group alignment
- Consultative Decision-Making: seeking input while retaining authority
- Command Decision Model: hierarchical authority in time-critical situations
- Advice Process (Reinventing Organizations): seek advice but decide autonomously

**Accountability and Governance Models**:
- Single Wringable Neck (SWN): exactly one person accountable per outcome
- Directly Responsible Individual (DRI) - Apple's accountability model
- Owner-Approver-Contributor model used in OKR frameworks
- Governance boards and steering committees: decision authority structures
- Program governance: roles in program boards and oversight committees

**Agile and Product Development Models**:
- Scrum roles: Product Owner, Scrum Master, Development Team responsibilities
- SAFe roles: Release Train Engineer, Product Management, System Architect
- Product Trio: Product Manager, Designer, Tech Lead collaboration model
- Spotify Model: Squad autonomy with aligned decision-making
- Shape Up (Basecamp): Shaper, Designer, Programmers role clarity

**Cross-Functional Collaboration Patterns**:
- Design-Development-Product triangle of accountability
- Security champions: embedded security consultation model
- Architecture Review Board (ARB): review and approval authority
- Technical Design Review (TDR): consultation and approval process
- Change Advisory Board (CAB): ITIL change approval authority
- Compliance review gates: legal, privacy, security approval checkpoints

**Approval and Review Processes**:
- Multi-stage approval workflows: peer review, manager approval, architecture sign-off
- Lightweight vs. heavyweight review processes by risk level
- Asynchronous review and approval (RFC process, pull request reviews)
- Architecture Decision Records (ADRs): documenting who decided what and why
- Request for Comments (RFC): structured consultation and decision process
- Design review checkpoints: concept, detailed design, implementation review

**Organizational Design Patterns**:
- Centralized vs. Decentralized decision-making structures
- Federated model: domain-specific decision authority
- Matrix organization accountability: functional vs. project reporting
- Committee-based governance: steering committees, review boards
- Empowerment and delegation: push decisions to edges
- Escalation paths: when to escalate unresolved decisions

**Lean and Efficiency Principles**:
- Eliminate unnecessary approvals: reduce "Consulted" and "Informed" roles
- Push decisions to information: those closest to work should decide
- Reduce handoffs: combine Responsible and Accountable when possible
- Just-in-time consultation: consult when needed, not by default
- Information radiators: make status visible, reduce need for "Informed" meetings
- Decision velocity: measure and improve decision cycle time

**Stakeholder Management**:
- Power-Interest Grid: mapping stakeholder influence and engagement level
- Stakeholder engagement plans: when to consult vs. inform
- Communication plans: RACI-informed notification strategies
- Influence mapping: understanding formal vs. informal decision influence
- RACI-based communication matrix: who communicates what to whom

**Tools and Visualization**:
- RACI matrix templates (Excel, Google Sheets, Miro, Mural)
- Project management tools: Asana, Jira, Monday.com RACI features
- Organizational charting tools: LucidChart, OrgChart
- Decision log tools: ADR repositories, Confluence decision pages
- Workflow automation: approval routing in Jira, ServiceNow
- RACI audit and analysis: identifying gaps, overlaps, bottlenecks

**Process Improvement Methodologies**:
- Lean Six Sigma: SIPOC (Suppliers-Inputs-Process-Outputs-Customers) and RACI alignment
- Business Process Reengineering: redesigning processes with clear accountability
- Value Stream Mapping: identifying decision points and ownership
- Process mining: analyzing actual vs. intended decision flows
- Continuous improvement: regularly review and optimize RACI assignments

**Quality and Compliance**:
- ISO 9001: Quality management system roles and responsibilities
- ISO 27001: Information Security Management System (ISMS) accountability
- SOC 2: Control ownership and accountability documentation
- GDPR: Data Protection Officer and data controller/processor roles
- ITIL 4: Service management roles and accountability
- COBIT: IT governance roles and decision authority

**Program and Portfolio Management**:
- PMI PMBOK: Project roles and responsibility assignment
- Portfolio governance: investment decision authority
- Program-level vs. project-level decision authority
- Multi-project coordination: resolving cross-project dependencies
- Resource allocation authority: who approves staffing decisions

**Conflict Resolution and Escalation**:
- Escalation triggers: when to escalate unresolved RACI conflicts
- Tie-breaking authority: who decides when Accountable parties disagree
- Consensus vs. consultative thresholds: when to seek agreement vs. input
- Escalation paths: team lead → manager → director → VP
- Mediation and arbitration: neutral third-party decision support

**Related Standards**:
- PMI Project Management Body of Knowledge (PMBOK): Responsibility Assignment Matrix
- PRINCE2: Project roles and responsibility definitions
- ITIL 4: Service management accountability framework
- TOGAF: Enterprise Architecture governance roles
- Agile frameworks: Scrum, SAFe, LeSS role definitions

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
