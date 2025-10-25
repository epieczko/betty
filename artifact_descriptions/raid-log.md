# Name: raid-log

## Executive Summary

The RAID Log (Risks, Assumptions, Issues, Decisions) is a critical PMO governance artifact providing centralized tracking of project/program risks, assumptions, issues, and decisions aligned to PMBOK Guide, PRINCE2 methodology, and PMI standards. This real-time management tool integrates with project management platforms (Jira, ServiceNow PPM, Microsoft Project, SmartSheet) enabling transparency, accountability, status reporting, and audit trail throughout project lifecycle phases from initiation through closure.

As a cornerstone of project governance, this artifact serves Program/Project Managers, PMO Directors, Executive Sponsors, Steering Committees, and Delivery Teams by providing immediate visibility into project risks requiring mitigation, assumptions requiring validation, issues blocking progress, and decisions made with rationale. It supports PMO governance, steering committee reporting, risk-informed decision making, and lessons learned capture.

### Strategic Importance

- **Comprehensive Tracking**: Provides single source of truth for RAID items (Risks, Assumptions, Issues, Decisions) with unique IDs, ownership, status, and resolution tracking
- **Risk Management Integration**: Links to Enterprise Risk Register for high-impact risks while managing project-specific tactical risks
- **Issue Resolution**: Tracks issues blocking project progress with priority, owner, target resolution date, and escalation path
- **Decision Trail**: Documents all project decisions with date, decision-maker, options considered, rationale, and approval evidence
- **Assumption Validation**: Tracks critical assumptions requiring validation ensuring assumptions don't become risks or issues
- **PMO Governance**: Enables PMO oversight, steering committee reporting, and project health dashboards with RAID item metrics
- **Lessons Learned**: Provides audit trail for post-project reviews, retrospectives, and continuous improvement

## Purpose & Scope

### Primary Purpose

This artifact serves as the project/program RAID Log tracking Risks (potential future events impacting objectives), Assumptions (factors believed true requiring validation), Issues (current problems requiring resolution), and Decisions (choices made with rationale). It provides centralized governance tool for project management, steering committee reporting, risk mitigation tracking, issue resolution, assumption validation, and decision audit trail aligned to PMBOK, PRINCE2, and PMO best practices.

### Scope

**In Scope**:
- **Risks**: Project-specific risks with likelihood/impact assessment, mitigation plans, risk owner, target dates, and risk response strategy (avoid/transfer/mitigate/accept)
- **Assumptions**: Critical assumptions underlying project plan with validation approach, assumption owner, validation status, and contingency if invalid
- **Issues**: Current problems blocking progress with priority (P1 Critical/P2 High/P3 Medium/P4 Low), issue owner, root cause, resolution plan, target date, escalation path
- **Decisions**: Project decisions documenting date, decision-maker, options considered, decision rationale, approval evidence, and impact on project
- Unique ID assignment for each RAID item with traceability
- Status tracking (Open, In Progress, Resolved, Closed) with status dates
- Priority/severity scoring for risks and issues
- Owner assignment with accountability for each RAID item
- Target resolution dates and actual resolution dates
- Escalation tracking for overdue or high-priority items
- RAID item metrics and dashboard (open risks, overdue issues, decision count, assumption validation rate)
- Integration with project status reports and steering committee reports
- Linkage to project schedule and work breakdown structure
- Weekly RAID review cadence with project team
- Escalation to Enterprise Risk Register for high-impact project risks
- Lessons learned extraction from closed RAID items

**Out of Scope**:
- Enterprise-wide strategic and operational risks (see Enterprise Risk Register)
- Policy exceptions and control deviations (see Exception Register)
- Security incidents and operational incidents (see Incident Management)
- Vendor risks and third-party assessments (see Third-Party Risk Assessments)
- Audit findings and remediation plans (see Audit Management)
- Change requests and change management (see Change Control)

### Target Audience

**Primary Audience**:
- Program/Project Managers for day-to-day RAID log maintenance, risk mitigation, issue resolution, and decision documentation
- PMO Directors for portfolio oversight, RAID metrics reporting, and PMO governance
- Executive Sponsors for high-level project health visibility and key decision approval
- Project Steering Committee for RAID review, risk acceptance, issue escalation, and strategic decisions

**Secondary Audience**:
- Project Team Members as risk/issue owners responsible for mitigation and resolution
- Functional Managers providing resources for issue resolution and risk mitigation
- Enterprise Risk Management for high-impact project risk escalation and integration with Enterprise Risk Register
- Internal Audit for project governance assessment and decision trail audit
- Lessons Learned teams for post-project review and continuous improvement

## Document Information

**Format**: Markdown

**File Pattern**: `*.raid-log.md`

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
**RAID Log Best Practices**:
**Weekly RAID Review**: Conduct weekly RAID log review with project team to add new items, update status, and close resolved items
**Unique ID System**: Assign unique IDs to each RAID item (e.g., R-001, A-001, I-001, D-001) for traceability and reference
**Owner Assignment**: Every RAID item must have a named owner accountable for resolution or mitigation
**Priority Scoring**: Use consistent priority/severity scoring (P1/Critical, P2/High, P3/Medium, P4/Low) for risks and issues
**Target Dates**: Establish and track target resolution dates for all risks and issues with aging alerts for overdue items
**Escalation Path**: Define clear escalation path for overdue or high-priority items (e.g., P1 issues unresolved in 48 hours escalate to steering committee)
**RAI Conversion**: Monitor assumptions and risks that convert to issues, validating assumption failure or risk materialization
**Decision Documentation**: Document all major project decisions with date, decision-maker, options considered, rationale, and approval
**Status Reporting Integration**: Include RAID summary in weekly status reports and steering committee presentations
**Dashboard Metrics**: Track metrics including open risks, overdue issues, decisions made this period, assumption validation rate
**Risk vs Enterprise Risk**: Escalate high-impact project risks (potential loss >$500K or strategic impact) to Enterprise Risk Register
**Root Cause Analysis**: Conduct root cause analysis for recurring issues using 5 Whys or Fishbone diagram
**Lessons Learned**: Extract lessons learned from closed RAID items for project retrospectives and knowledge sharing
**PM Tool Integration**: Maintain RAID log in project management tool (Jira, ServiceNow PPM) not just spreadsheets
**No Duplicate Tracking**: Avoid duplicate tracking - if escalated to Enterprise Risk Register, close in RAID log with reference

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

**Project Management Standards**:
- PMBOK Guide 7th Edition (PMI) - Project Risk Management (Chapter 11)
- PRINCE2 (Projects IN Controlled Environments) - Risk, Issue, Decision management
- PMI Practice Standard for Project Risk Management
- ISO 21500:2021 Project, programme and portfolio management - Context and concepts
- APM Body of Knowledge (Association for Project Management)
- IPMA Competence Baseline (International Project Management Association)
- Agile Practice Guide (PMI/Agile Alliance) - Risk and issue management in agile
- SAFe (Scaled Agile Framework) - Program Risk Management
- PMI-ACP (Agile Certified Practitioner) risk management practices

**PMO & Governance Frameworks**:
- PMI Pulse of the Profession - PMO frameworks and best practices
- Gartner PMO Maturity Model
- COBIT 2019 (BAI01 Manage Programmes and Projects)
- ITIL 4 Service Management (Project Management practice)
- Portfolio, Programme and Project Offices (P3O) framework
- MoP (Management of Portfolios) framework
- MSP (Managing Successful Programmes) framework

**Risk Management Integration**:
- ISO 31000:2018 Risk Management Guidelines
- COSO Enterprise Risk Management Framework
- FAIR (Factor Analysis of Information Risk) for risk quantification
- NIST Risk Management Framework
- Three Lines Model for risk governance

**Project Management Tools & Platforms**:
- Jira (Atlassian) - Issue and risk tracking
- ServiceNow PPM (Project Portfolio Management)
- Microsoft Project / Project Online
- SmartSheet project management
- Monday.com project tracking
- Asana project management
- Wrike project collaboration
- Planview Enterprise One PPM
- Clarity PPM (Broadcom)
- Oracle Primavera P6

**Issue & Decision Management**:
- PMI Practice Guide on Decision Making
- DACI (Driver, Approver, Contributor, Informed) decision framework
- RACI (Responsible, Accountable, Consulted, Informed) for issue ownership
- ITIL Problem Management for root cause analysis
- Six Sigma DMAIC for issue resolution
- 8D (Eight Disciplines) Problem Solving

**Agile & Scrum Integration**:
- Scrum Guide - Sprint risks and impediments
- SAFe Program Risk Management
- Kanban board for issue tracking
- Retrospective practices for lessons learned
- Sprint Review for decision documentation

**Compliance & Audit**:
- SOC 2 (CC5.2 Risk assessment in project delivery)
- ISO 27001 (Project risk management for ISMS projects)
- COBIT 2019 project governance
- PMI Code of Ethics and Professional Conduct
- Sarbanes-Oxley project governance for IT implementations

**Reference**: Consult PMO, Program/Project Managers, and Enterprise Risk Management team for detailed guidance on RAID log templates, risk assessment methodologies, issue escalation procedures, and integration with portfolio management tools

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
