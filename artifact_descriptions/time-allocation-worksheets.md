# Name: time-allocation-worksheets

## Executive Summary

The Time Allocation Worksheets artifact tracks and analyzes how engineering teams allocate their time across project work, business-as-usual (BAU) operations, toil, technical debt, innovation, and unplanned work. This operational planning tool enables Engineering Managers and Team Leads to measure capacity utilization, identify toil reduction opportunities, and ensure healthy balance between feature delivery, operational sustainability, and innovation investments aligned with Google SRE and industry best practices.

Built on SRE principles that toil should consume less than 50% of time and innovation frameworks like Google's 20% time or the 70-20-10 model (70% core work, 20% adjacent projects, 10% innovation), this artifact makes time allocation visible and actionable. It identifies when teams are overwhelmed by operational toil, under-investing in technical debt reduction, or lacking time for innovation, enabling data-driven conversations about priorities, automation investments, and sustainable workload management.

### Strategic Importance

- **Toil Measurement**: Quantifies operational toil and drives automation to keep it below 50% (Google SRE)
- **Sustainable Pace**: Ensures teams balance feature delivery, operations, and improvement work
- **Innovation Time**: Protects capacity for learning, experimentation, and technical innovation
- **Technical Debt Visibility**: Tracks and justifies time investment in debt reduction and refactoring
- **Capacity Planning**: Provides data for realistic sprint planning and roadmap commitments
- **Burnout Prevention**: Identifies unsustainable workload patterns (excessive on-call, unplanned work)
- **Investment Trade-offs**: Enables informed decisions on project vs. BAU vs. innovation allocation

## Purpose & Scope

### Primary Purpose

This artifact measures and optimizes how engineering teams allocate time across competing demands—feature development, operational support, toil, technical debt, innovation—enabling sustainable workload management, toil reduction, and balanced investment in delivery, reliability, and improvement.

### Scope

**In Scope**:
- Project work: planned feature development, new capabilities, strategic initiatives
- Business-as-usual (BAU): steady-state operations, maintenance, regular releases
- Toil: repetitive, automatable operational work (target: <50% per Google SRE)
- Technical debt: refactoring, modernization, architectural improvements
- Innovation time: 20% time, 70-20-10 model, hackathons, learning, experiments
- Unplanned work: incidents, urgent bugs, escalations, production firefighting
- On-call time: incident response, escalation handling, production support
- Meetings and overhead: ceremonies, planning, reviews, 1-on-1s, administrative
- Training and development: learning, conferences, certification prep
- Context switching: measuring multitasking costs and interrupt-driven work

**Out of Scope**:
- Individual performance evaluation or time tracking for billing (separate HR/finance process)
- Detailed task-level time logs (use project management tools)
- Team organizational structure (see team-topology-map)
- Service ownership definitions (see ownership-charters)
- Skills and competencies (see skills-matrix)
- Initiative governance (see initiative-charter)

### Target Audience

**Primary Audience**:
- Engineering Managers tracking team capacity and workload balance
- Team Leads planning sprints and managing sustainable pace
- SRE and Operations Leaders measuring and reducing toil
- Product Leaders understanding engineering capacity constraints

**Secondary Audience**:
- CTOs and VPs understanding organizational time allocation patterns
- Program Managers adjusting roadmaps based on available capacity
- HR/People Teams identifying burnout risk from excessive on-call or unplanned work
- Finance teams allocating costs by project vs. BAU activities

## Document Information

**Format**: Markdown

**File Pattern**: `*.time-allocation-worksheets.md`

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
**Time Allocation Tracking Best Practices**:
- **Weekly Retrospectives**: Teams reflect on time allocation and identify improvement opportunities
- **Categorization Consistency**: Use standardized categories (project, BAU, toil, debt, innovation, unplanned)
- **Lightweight Tracking**: Don't burden teams with excessive time logging; use estimates or sampling
- **Team-Level Aggregation**: Focus on team patterns, not individual time tracking for surveillance
- **Trend Analysis**: Track allocation over quarters to identify concerning trends
- **Action-Oriented**: Use data to drive automation, process improvement, and workload rebalancing

**Toil Reduction Strategies**:
- **Measure Toil**: Quantify toil hours and percentage of total time
- **50% Budget**: Keep toil below 50% per Google SRE best practices
- **Automation Prioritization**: Calculate ROI for automating highest-frequency toil
- **Platform Capabilities**: Build self-service tools to reduce manual work
- **Eliminate vs. Automate**: First question if work is necessary; then automate if required
- **Continuous Improvement**: Regular toil reduction sprints or 20% time for automation

**Innovation Time Protection**:
- **Explicit Allocation**: Dedicate 10-20% time for learning, experiments, and innovation
- **Scheduled Innovation**: Regular hackathons, innovation sprints, or 20% time
- **Bottom-Up Ideation**: Let teams choose innovation projects aligned with their interests
- **Showcase Results**: Celebrate and share innovation outcomes to reinforce value
- **Fail-Fast Culture**: Encourage experiments and learning from failures
- **Connect to Strategy**: Guide innovation toward strategic priorities without being prescriptive

**Technical Debt Management**:
- **Visible Debt Backlog**: Track technical debt explicitly in project management tools
- **20% Time for Debt**: Allocate roughly 20% of capacity to debt reduction
- **Debt Prioritization**: Focus on high-interest debt (costly to maintain) first
- **Boy Scout Rule**: Continuous small improvements alongside feature work
- **Debt Metrics**: Track debt accumulation vs. paydown over time
- **Strategic Debt Paydown**: Periodic focused sprints to tackle major debt items

**Capacity Planning**:
- **Realistic Commitments**: Account for toil, unplanned work, and overhead in sprint planning
- **Historical Velocity**: Use past throughput to forecast future capacity
- **Buffer for Unplanned**: Reserve 20-30% capacity for incidents, urgent bugs, escalations
- **Meeting Overhead**: Factor in ceremonies, 1-on-1s, and meetings (typically 20-30%)
- **On-Call Impact**: Reduce sprint commitments during on-call rotations
- **Sustainable Pace**: Avoid chronic overcommitment leading to burnout

**Workload Balance**:
- **Project-BAU Mix**: Aim for roughly 60-70% project, 20-30% BAU, 10% innovation (adjust by context)
- **Unplanned Work**: Target <20% unplanned; higher indicates process/reliability issues
- **Context Switching**: Minimize concurrent priorities; focus teams on one major initiative
- **Flow State**: Protect blocks of uninterrupted time for deep work
- **Meeting Discipline**: Reduce unnecessary meetings; shift to asynchronous when possible

**Burnout Prevention**:
- **Monitor On-Call Load**: Track pages, incident resolution time, recovery periods
- **Sustainable Rotations**: Weekly on-call with adequate backup and follow-the-sun for global teams
- **Post-Incident Recovery**: Allow recovery time after major incidents
- **Overtime Tracking**: Flag chronic overtime as burnout risk
- **Team Health Checks**: Regular surveys on workload, stress, satisfaction
- **Workload Rebalancing**: Redistribute work when teams are overloaded

**Automation Investment**:
- **Calculate ROI**: Time saved by automation vs. time to build and maintain
- **High-Frequency First**: Automate tasks done most often for maximum impact
- **Self-Service**: Enable other teams to operate independently, reducing your toil
- **Infrastructure as Code**: Automate environment provisioning and configuration
- **CI/CD**: Automate building, testing, and deployment to reduce manual toil
- **Runbook Automation**: Convert manual procedures to automated scripts

**Tools and Visualization**:
- **Pie Charts**: Visualize time allocation across categories at team level
- **Trend Lines**: Show allocation changes over time (quarters or months)
- **Heatmaps**: Identify teams with unsustainable allocations (>50% toil, <5% innovation)
- **Dashboards**: Real-time visibility into capacity utilization and workload
- **Jira Reports**: Use project management tools to categorize and track work types

**Governance Alignment**: Align time allocation with organizational priorities and OKRs
**Metric-Driven**: Track toil percentage, unplanned work ratio, innovation investment over time
**Transparency**: Share time allocation data to have informed conversations about priorities
**Regular Review**: Monthly or quarterly review of time allocation trends and adjustments
**Continuous Improvement**: Use allocation data to drive automation, process improvements, and policy changes

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

**SRE and Operational Excellence**:
- Google SRE toil budget: keep toil below 50% of time through automation
- Toil definition: manual, repetitive, automatable, tactical, no enduring value
- Error budget: balance reliability work vs. feature velocity
- On-call rotation sustainability: reasonable load, handoff protocols, burnout prevention
- Production readiness: minimizing operational burden through good design
- Automation ROI: calculating value of automating repetitive work

**Innovation Time Models**:
- Google 20% time: one day per week for personal projects and learning
- 70-20-10 model: 70% core work, 20% adjacent projects, 10% new experiments
- 3M 15% time: innovation time leading to Post-it Notes and other products
- Atlassian ShipIt days: quarterly 24-hour hackathons
- Innovation sprints: dedicated time for experimentation and prototyping
- Genius time: self-directed learning and passion projects

**Capacity Planning Frameworks**:
- Team capacity calculation: available hours minus meetings, overhead, on-call
- Sustainable pace: 40-hour weeks, avoiding chronic overtime
- Velocity and throughput: measuring team output over time
- Work-in-progress (WIP) limits: reducing context switching costs
- Load balancing: distributing work evenly across team members
- Buffer capacity: maintaining slack for unplanned work (typically 20-30%)

**Technical Debt Management**:
- Technical debt quadrant: Reckless/Prudent x Deliberate/Inadvertent
- Debt quantification: estimating interest (time cost) and principal (payoff time)
- 20% rule: allocate 20% of capacity to technical debt reduction
- Boy Scout Rule: leave code better than you found it
- Debt backlog: tracking, prioritizing, and scheduling debt work
- Refactoring economics: when to pay down debt vs. living with it

**Agile and Lean Principles**:
- Sprint planning: realistic commitments based on historical capacity
- Yesterday's weather: using past velocity to forecast future capacity
- Kanban: visualizing work and limiting WIP to improve flow
- Theory of Constraints: identifying and addressing bottlenecks
- Value stream mapping: eliminating waste in delivery process
- Continuous improvement: retrospectives and process refinement

**Work Classification Models**:
- Four types of work (Phoenix Project): business projects, IT projects, changes, unplanned work
- Planned vs. unplanned work ratio: target <20% unplanned
- Interrupt-driven work: measuring and minimizing context switching
- Maker's schedule vs. Manager's schedule: protecting focus time
- Deep work vs. shallow work: optimizing for high-value activities

**Time Tracking and Measurement**:
- Activity-based costing: allocating time to projects for financial tracking
- Timeboxing: fixed time allocations for different work types
- Time audits: periodic assessments of actual time allocation
- Pomodoro technique: focused work sessions with breaks
- Calendar analysis: meeting load, focus time, fragmentation
- Tools: Jira time tracking, Harvest, Toggl, RescueTime, Clockify

**Operational Metrics**:
- Toil percentage: operational toil as percentage of available time
- Unplanned work ratio: incidents and escalations vs. planned work
- Context switching cost: time lost to task transitions
- Meeting load: percentage of time in meetings vs. productive work
- On-call burden: pages per week, time to resolution, recovery time
- Innovation investment: time allocated to learning and experiments

**Workload Management**:
- Psychological safety and sustainable pace
- Burnout prevention: monitoring excessive on-call, overtime, context switching
- Work-life balance: tracking hours, vacation usage, recovery time
- Team health metrics: happiness, satisfaction, perceived workload
- Cognitive load management: limiting simultaneous responsibilities
- Flow state protection: minimizing interrupts during focused work

**Project Portfolio Management**:
- Project vs. BAU allocation: balancing new work and maintenance
- Portfolio prioritization: which projects to fund based on capacity
- Resource allocation: distributing team capacity across initiatives
- Demand management: saying no when capacity is constrained
- Investment categories: run-the-business vs. change-the-business
- ROI analysis: value delivered per time invested

**Automation and Efficiency**:
- Automation opportunities: identifying high-frequency, high-toil tasks
- Self-service capabilities: reducing team dependencies and handoffs
- Platform engineering: building capabilities to reduce toil for application teams
- CI/CD automation: reducing manual deployment and testing toil
- Infrastructure as Code: automating environment provisioning
- Runbook automation: automating incident response procedures

**Lean and Waste Reduction**:
- Seven wastes of lean: transport, inventory, motion, waiting, overproduction, overprocessing, defects
- Value-added vs. non-value-added activities
- Process improvement: eliminating unnecessary meetings, approvals, handoffs
- Communication efficiency: asynchronous vs. synchronous collaboration
- Documentation ROI: right-sizing documentation efforts

**Health and Wellbeing**:
- Sustainable pace and avoiding burnout
- Recovery time after incidents and on-call rotations
- Vacation and PTO usage rates
- Mental health and psychological safety
- Work-life integration strategies
- Ergonomics and breaks for remote work

**Related Standards**:
- ISO 9001: Quality management and process efficiency
- ITIL 4: Service management capacity planning
- COBIT: IT governance and resource optimization
- PMI: Project resource management standards
- Agile frameworks: Scrum, Kanban capacity planning practices

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
