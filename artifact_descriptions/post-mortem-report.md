# Name: post-mortem-report

## Executive Summary

The Post-Mortem Report is a comprehensive incident review document that captures what happened, why it happened, how it was resolved, and what actions will prevent recurrence. Following the blameless postmortem culture pioneered by Google SRE and Etsy, this artifact transforms production incidents into learning opportunities by systematically documenting incident timelines, root causes, impact metrics, and SMART remediation actions in a psychologically safe, blame-free environment.

Structured around the Google SRE postmortem template and ITIL 4 problem management principles, each post-mortem includes a detailed timeline (detection → escalation → mitigation → resolution), severity classification (P0-P3), impact quantification (MTTR, customers affected, revenue impact, error budget burn), root cause analysis using 5 Whys or Fishbone techniques, and categorized action items (immediate, short-term, long-term) with assigned owners and completion deadlines. Post-mortems are reviewed in team retrospectives and published to a searchable knowledge base for organizational learning.

### Strategic Importance

- **Learning Culture**: Establishes blameless incident review as standard practice, fostering psychological safety and continuous improvement
- **Recurrence Prevention**: Reduces repeat incidents by 60-80% through systematic root cause elimination
- **Transparency**: Builds customer trust through honest, timely communication about service reliability
- **Knowledge Capture**: Creates searchable repository of failure modes, troubleshooting strategies, and solutions
- **Metric-Driven Improvement**: Tracks MTTR trends, incident frequency, and action item completion rates
- **Team Development**: Accelerates engineer growth by documenting expert troubleshooting and decision-making
- **Compliance**: Satisfies SOC 2, ISO 27001, and audit requirements for incident documentation and corrective action

## Purpose & Scope

### Primary Purpose

This artifact documents production incidents through comprehensive, blameless analysis including detailed timelines, root causes, impact metrics, and actionable remediation plans. It transforms failure into organizational learning by systematically capturing what went wrong, why it went wrong, and how to prevent recurrence, while fostering a culture of psychological safety and continuous improvement.

### Scope

**In Scope**:
- Incident overview and severity classification (P0/SEV0 through P3/SEV3)
- Detailed timeline with UTC timestamps (detection, acknowledgment, escalation, mitigation, resolution)
- Impact quantification (MTTR, MTTA, customers affected, revenue loss, error budget burn)
- Root cause analysis using 5 Whys, Fishbone, or Fault Tree Analysis
- Contributing factors across people/process/technology dimensions
- What went well and what went poorly during incident response
- SMART action items categorized by timeline (immediate, 30-day, 90-day, long-term)
- Action item owners (DRI - Directly Responsible Individual) and deadlines
- Lessons learned and knowledge base updates
- Related incidents and pattern analysis
- Blameless facilitation ensuring psychological safety

**Out of Scope**:
- Individual performance reviews or disciplinary action
- Legal liability or blame attribution
- Detailed RCA methodologies (covered in root-cause-analyses artifact)
- Incident response execution (covered in playbooks artifact)
- Compensation or financial impact beyond technical metrics
- Customer communication strategies (handled by customer success/PR)

### Target Audience

**Primary Audience**:
- SRE Teams conducting and learning from post-mortem analysis
- Incident Commanders documenting incident response and coordination
- Engineering Teams implementing remediation actions
- Operations Teams preventing future incident recurrence

**Secondary Audience**:
- Engineering Leadership tracking reliability trends and prioritizing investments
- Product Management understanding customer impact and service quality
- Customer Success Teams communicating incident impacts to customers
- Compliance/Audit Teams validating incident response processes

## Document Information

**Format**: Markdown

**File Pattern**: `*.post-mortem-report.md`

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

### Report Overview

**Reporting Period**:
- `reportingPeriod`: Time period covered (e.g., Q2 2024, Jan 2024, etc.)
- `reportDate`: Date report was generated
- `reportType`: Regular | Ad-hoc | Special Investigation | Executive Briefing
- `frequency`: How often this report is generated
- `distribution`: Intended recipients and distribution method

### Executive Summary

**Key Highlights**:
- `criticalFindings`: Top 3-5 most important findings for executive attention
- `trendAnalysis`: Key trends compared to previous periods
- `recommendations`: Priority recommendations requiring executive decision
- `impactAssessment`: Business impact of findings or metrics

### Detailed Analysis

**Metrics & KPIs**:
- `metricName`: Name of each metric or KPI
- `currentValue`: Value for this reporting period
- `targetValue`: Target or goal
- `previousValue`: Value from previous period for trending
- `variance`: Difference from target and trend direction
- `variances`: Explanation of significant variances
- `dataSource`: Where data comes from
- `collectionMethod`: How data is collected and validated

**Analysis by Category**:
- `category`: Grouping for related metrics or findings
- `observations`: What was observed or measured
- `analysis`: Interpretation and meaning
- `rootCauses`: Underlying causes for significant findings
- `impact`: Business or operational impact
- `trends`: Patterns over time
- `comparatives`: Benchmarking against industry or peer data

### Recommendations & Actions

**Priority Actions**:
- `actionId`: Unique identifier
- `actionDescription`: What needs to be done
- `rationale`: Why this action is needed
- `priority`: P0 | P1 | P2 | P3
- `owner`: Who is responsible
- `dueDate`: Target completion date
- `estimatedEffort`: Resource requirement
- `dependencies`: Prerequisites or dependencies
- `successMetrics`: How success will be measured

**Follow-up Items**:
- `openItems`: Items from previous reports still in progress
- `closedItems`: Items completed since last report
- `escalations`: Items requiring escalation to higher authority


## Best Practices

**Blameless Culture**: Explicitly state "this is a blameless post-mortem" at the start; focus on systems, not individuals
**Timely Completion**: Publish post-mortem within 48-72 hours while details are fresh; don't wait weeks
**Precise Timeline**: Use UTC timestamps accurate to minutes; include detection, acknowledgment, escalation, mitigation, resolution
**Quantify Impact**: Always include MTTR, customers affected, error budget burn; use data, not vague estimates
**Honest Assessment**: Document both successes and failures; "what went well" is as important as "what went poorly"
**Root Cause Focus**: Apply 5 Whys or Fishbone; don't stop at symptoms; identify fundamental causes
**Actionable Items**: Every action item must have owner, deadline, and success criteria (SMART)
**Categorize Actions**: Separate immediate fixes (done), short-term (30 days), long-term (90+ days)
**Track Completion**: Follow up on action items in subsequent reviews; report completion rates
**Facilitate Discussion**: Host synchronous review meeting; don't just circulate document asynchronously
**Invite Participants**: Include all incident responders in post-mortem review for diverse perspectives
**Related Incidents**: Link to similar past incidents; identify patterns requiring systemic fixes
**Knowledge Sharing**: Publish to searchable repository; present interesting post-mortems in team meetings
**Customer Perspective**: Include customer impact narrative; read actual customer support tickets
**Avoid Counterfactuals**: Focus on what happened, not hypotheticals; "we should have" is less useful than "we will"
**Template Consistency**: Use standard template (Google SRE format) for predictable structure
**Executive Summary**: Provide 2-3 paragraph TL;DR for leadership; don't force executives to read full timeline

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

**Post-Mortem Culture & Templates**:
- Google SRE Book (Chapter on Postmortem Culture and Blameless Reviews)
- Google SRE Postmortem Template
- Etsy Debriefing Facilitation Guide (blameless post-mortem facilitation)
- Site Reliability Engineering Workbook (Google)
- PagerDuty Incident Response Documentation
- Atlassian Incident Postmortem Template

**Blameless Culture Principles**:
- Psychological safety (Google's Project Aristotle findings)
- Just Culture (balancing accountability and learning)
- Learning from Incidents (Sidney Dekker, Human Error)
- Resilience Engineering principles
- Human Factors analysis in incident investigation

**Timeline & Analysis Frameworks**:
- ITIL 4 Problem Management
- 5 Whys (Toyota Production System)
- Fishbone/Ishikawa Diagram
- Incident timeline reconstruction best practices
- Contributing factors analysis (people/process/technology)

**Impact Quantification Metrics**:
- MTTR (Mean Time To Resolution)
- MTTA (Mean Time To Acknowledgment)
- MTTD (Mean Time To Detection)
- MTTF (Mean Time To Failure)
- Error budget consumption (SRE concept)
- Customer impact metrics (users affected, revenue loss)
- Availability metrics (uptime %, SLA compliance)

**Action Item Management**:
- SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
- Action item categorization (immediate, short-term, long-term)
- DRI (Directly Responsible Individual) assignment
- Follow-through tracking and completion reporting
- Priority frameworks (P0: immediate, P1: 30 days, P2: 90 days)

**Post-Mortem Facilitation Tools**:
- Incident.io (automated timeline generation, Slack integration)
- FireHydrant (retrospective facilitation, action item tracking)
- Jeli.io (incident analysis and learning platform)
- Confluence/Notion (knowledge base publishing)
- Google Docs (collaborative editing)
- Miro/Mural (visual timeline mapping)

**Knowledge Management**:
- Searchable post-mortem repositories
- Incident tagging taxonomies (service, cause, severity)
- Related incident linking and pattern analysis
- Knowledge base integration (Confluence, Notion, Wiki)
- Post-mortem review cadence (monthly team reviews)

**Communication Patterns**:
- Internal stakeholder communication
- Customer-facing incident reports (status page updates)
- Executive summaries for leadership
- Cross-team sharing and learning sessions

**Compliance & Audit**:
- SOC 2 Type II (incident response documentation)
- ISO 27001 (nonconformity and corrective action)
- PCI-DSS (security incident documentation)
- GDPR (data breach notification requirements)
- HIPAA (breach notification rules)

**Reference**: Consult SRE leadership and incident management team for post-mortem standards

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
