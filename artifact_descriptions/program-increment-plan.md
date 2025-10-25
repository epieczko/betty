# Name: program-increment-plan

## Executive Summary

The Program Increment Plan is the cornerstone SAFe planning artifact that defines the 8-12 week Program Increment (PI) objectives, feature commitments, team assignments, and dependencies for an Agile Release Train (ART). This plan emerges from the PI Planning event where 50-125 team members collaborate face-to-face (or virtually) to align on business goals, define PI objectives, identify dependencies, and commit to deliverables for the upcoming increment.

As the authoritative SAFe planning deliverable, it captures PI objectives with business value scoring, program board visualizations showing feature delivery timelines and cross-team dependencies, team breakout planning results with sprint-by-sprint capacity allocation, identified risks and impediments requiring management attention, and confidence votes from teams. The plan drives ART execution through the PI, guiding daily work, informing ART Sync meetings, tracking progress through iteration reviews, and enabling course correction at mid-PI checkpoints until the PI System Demo and Inspect & Adapt workshop conclude the increment.

### Strategic Importance

- **Strategic Alignment**: Ensures activities directly support organizational objectives and expected outcomes
- **Resource Optimization**: Enables efficient allocation of personnel, budget, and technology resources
- **Risk Management**: Identifies potential obstacles and defines proactive mitigation strategies
- **Stakeholder Alignment**: Creates shared understanding of approach, timeline, and expectations
- **Success Measurement**: Establishes clear metrics and criteria for evaluating outcomes

## Purpose & Scope

### Primary Purpose

This artifact documents the outcome of SAFe PI Planning, serving as the committed plan for an Agile Release Train's work over the next 8-12 weeks. It solves the problem of aligning multiple Agile teams toward common objectives, managing cross-team dependencies, and creating predictable delivery cadence at scale while maintaining team autonomy and enabling continuous value delivery.

### Scope

**In Scope**:
- PI objectives for each team with business value scoring (1-10 scale)
- Program objectives rolled up from team objectives with stretch objectives identified
- Program Board showing features, iterations, milestones, and cross-team dependencies
- Team breakout planning results (sprint-by-sprint capacity and feature assignments)
- Cross-team dependencies identified and managed (including supplier/consumer relationships)
- Risks and impediments identified during PI Planning (ROAM'd - Resolved, Owned, Accepted, Mitigated)
- Team confidence votes on PI objective achievability (fist-of-five voting)
- PI capacity allocation (planned vs. available capacity factoring in PTO and support work)
- PI milestones and key dates (innovation sprint, IP iteration, PI System Demo)
- ART planning metrics (planned velocity, predictability, load factor)
- PI Planning event agenda and outcomes (management briefing, team breakouts, draft plans)

**Out of Scope**:
- Detailed story-level sprint planning (occurs during iteration planning)
- Individual task assignments and hour-level estimates
- Long-term product roadmap beyond the PI (covered in product vision/roadmap)
- Architectural runway and technical enablers details (covered in architecture artifacts)
- Individual team retrospectives and improvement actions

### Target Audience

**Primary Audience**:
- Release Train Engineer (RTE) who facilitates PI Planning and ART execution
- Business Owners who define business objectives and validate PI plans
- Product Management who presents vision and prioritizes features for the PI
- System Architect/Engineering who defines technical direction and enablers
- Scrum Masters who facilitate team planning and dependency management

**Secondary Audience**:
- Development teams who execute against the PI plan
- Product Owners who refine backlogs and manage team-level priorities
- Stakeholders and customers who benefit from PI deliverables
- Portfolio Management who track ART-level progress and value delivery
- Other ARTs and Solution Trains with dependencies

## Document Information

**Format**: Markdown

**File Pattern**: `*.program-increment-plan.md`

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
**Executive Sponsorship**: Ensure visible executive sponsorship and regular executive review
**Governance Alignment**: Align with organizational governance framework and decision-making bodies
**Metric-Driven**: Include measurable metrics and KPIs to track progress and outcomes
**Dependency Management**: Explicitly identify and track dependencies on other initiatives or resources
**Risk Integration**: Integrate with risk management processes; escalate risks appropriately
**Change Control**: Submit significant changes through formal change control process
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

**SAFe Framework (Core)**:
- SAFe Program Increment (PI) Planning (2-day planning event, quarterly cadence)
- SAFe Agile Release Train (ART) structure (50-125 people, 5-12 Agile teams)
- SAFe PI Objectives (SMART goals with business value, team and program level)
- SAFe Program Board (visual planning board, dependencies, milestones)
- SAFe Confidence Vote (fist-of-five voting on plan achievability)
- ROAM risk management (Resolved, Owned, Accepted, Mitigated)

**SAFe Events & Ceremonies**:
- PI Planning event (management briefing, team breakouts, draft plan review, final plan)
- ART Sync (weekly coordination meeting across teams during PI execution)
- Iteration Review and System Demo (sprint reviews and integrated solution demos)
- Inspect & Adapt (I&A) workshop (PI retrospective with problem-solving)
- Pre-PI Planning and Post-PI Planning (preparation and finalization)
- Scrum of Scrums (daily cross-team coordination)

**SAFe Roles**:
- Release Train Engineer (RTE - servant leader for ART, facilitates PI Planning)
- Product Management (defines features, manages program backlog, business value)
- System Architect/Engineering (technical leadership, architecture runway)
- Business Owners (define business objectives, participate in PI Planning)
- Product Owner (team-level backlog management)
- Scrum Master (team facilitation, impediment removal)

**SAFe Planning Artifacts**:
- Program Backlog (features prioritized by WSJF - Weighted Shortest Job First)
- Team Backlog (user stories derived from features)
- Program Board (physical or digital board showing PI plan)
- PI Objectives document (team and program objectives with business value)
- Feature breakdown and story mapping

**PI Planning Tools**:
- Jira Align (SAFe-specific planning and tracking platform)
- Mural / Miro (digital program board, virtual PI Planning)
- Azure DevOps (PI planning features, dependency tracking)
- Rally (CA Agile Central - SAFe planning tool)
- VersionOne / Digital.ai Agile (SAFe portfolio and PI planning)
- Physical program boards (string, sticky notes, poster boards)

**SAFe Metrics & Measurements**:
- Predictability Measure (actual vs. planned business value delivered)
- Program Predictability Measure (rolled up across teams)
- Team PI Performance (objectives achieved vs. planned)
- Feature completion rate and cycle time
- ART velocity and throughput metrics
- Dependency resolution rate

**Agile Planning Techniques**:
- Story mapping and feature decomposition
- WSJF prioritization (Cost of Delay / Job Size)
- Capacity planning with load factor
- Dependency mapping and critical path analysis
- Risk identification and mitigation planning
- Business value scoring and prioritization

**Scaling Agile Frameworks (Related)**:
- SAFe Large Solution level (multiple ARTs coordinated via Solution Train)
- Scrum@Scale (Scrum of Scrums coordination)
- LeSS (Large-Scale Scrum) planning events
- Disciplined Agile Delivery (DAD) inception phase

**Dependency Management**:
- Dependency visualization on program board
- Cross-team dependency tracking and resolution
- Supplier-consumer agreements between teams
- Integration points and milestone coordination

**Reference**: Consult organizational SAFe Program Consultants (SPCs), Release Train Engineers, and Agile Center of Excellence for detailed guidance on PI Planning execution and SAFe practices

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
