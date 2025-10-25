# Name: incident-reports

## Executive Summary

Incident Reports document the timeline, root cause analysis, impact assessment, and remediation actions for production incidents and outages. These reports are essential for conducting blameless postmortems, improving MTTR, preventing recurrence, and maintaining SRE and ITIL 4 incident management best practices.

Effective incident reports follow Google SRE principles of blameless postmortems—focusing on systems and processes, not individuals—and employ structured root cause analysis methodologies (5 Whys, Ishikawa diagrams, Pareto analysis). They integrate with incident management platforms (PagerDuty, Opsgenie, ServiceNow), capture detailed timelines with MTTD/MTTR metrics, and drive continuous improvement through actionable remediation items tracked to completion.

### Strategic Importance

- **Learning Organization**: Enables organizational learning from failures through blameless, structured analysis
- **MTTR Reduction**: Improves Mean Time To Recovery by documenting effective response patterns and gaps
- **Recurrence Prevention**: Prevents repeat incidents through root cause elimination and systemic improvements
- **SLO/Error Budget**: Tracks error budget consumption and informs SLO/SLI refinement based on real incidents
- **Compliance**: Meets SOC 2, ISO 27001, and regulatory incident documentation requirements
- **Knowledge Sharing**: Disseminates incident response knowledge across teams and organizations
- **Reliability Engineering**: Drives reliability improvements through data-driven analysis of failure modes

## Purpose & Scope

### Primary Purpose

This artifact documents incident timeline, impact assessment, root cause analysis, and remediation actions following production incidents to enable blameless learning, prevent recurrence, improve MTTR, and maintain compliance with incident management best practices.

### Scope

**In Scope**:
- Incident timeline (detection, escalation, mitigation, resolution with timestamps)
- Severity classification (SEV0/P0/Critical through SEV4/P4/Low)
- Impact assessment (users affected, revenue impact, SLO consumption, duration)
- MTTD/MTTA/MTTR metrics (Mean Time To Detect/Acknowledge/Recover)
- Root cause analysis (5 Whys, Ishikawa diagram, contributing factors)
- Contributing factors (technical issues, process gaps, human errors, external dependencies)
- Mitigation actions taken (immediate fixes, workarounds during incident)
- Remediation action items (long-term fixes, priority, owner, due date, status)
- Communication log (internal/external notifications, status page updates)
- SLO/Error budget impact (error budget consumption, SLI degradation)
- Lessons learned (what went well, what didn't, improvements needed)
- Blameless postmortem findings (system/process improvements, no individual blame)

**Out of Scope**:
- Planned maintenance (covered by change management)
- Security incidents (covered by security incident response)
- Non-production environment issues (covered by development processes)
- Disaster recovery tests (covered by DR test reports)
- Feature requests (covered by product management)

### Target Audience

**Primary Audience**:
- SRE Teams conducting postmortems and implementing reliability improvements
- Incident Commanders reviewing incident response effectiveness
- Engineering Teams responsible for remediation action completion
- On-Call Engineers learning from past incidents to improve response

**Secondary Audience**:
- Engineering Managers tracking MTTR trends and reliability investments
- Product Managers understanding customer impact and prioritizing fixes
- Executive Leadership reviewing high-severity incident trends
- Compliance Officers maintaining incident audit trail for regulatory requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.incident-reports.md`

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

**Blameless Always**: Focus on systems and processes, never blame individuals for incidents
**Timeline First**: Document detailed timeline with timestamps immediately after incident while memory is fresh
**Root Cause Depth**: Use 5 Whys or similar to find true root cause, not superficial symptoms
**Action Items Required**: Every incident must produce actionable improvement items with owners and due dates
**Track to Completion**: Follow up on all action items until completed; remediation prevents recurrence
**Measure MTTR**: Track MTTD, MTTA, MTTR metrics to identify response improvement opportunities
**SLO Impact**: Document error budget consumption and SLI degradation during incidents
**Communicate Early**: Notify stakeholders immediately; transparency builds trust during incidents
**Status Page Updates**: Keep status page current during incidents; customers appreciate transparency
**Postmortem Within 48hrs**: Conduct blameless postmortem within 48 hours while details are fresh
**Facilitate Neutrally**: Use neutral facilitator for postmortems to ensure psychological safety
**Document Contributing Factors**: Identify all contributing factors, not just single "root cause"
**Share Learnings**: Share postmortems widely across organization; everyone learns from incidents
**Template Consistency**: Use standard template for all incident reports to enable analysis and comparison
**Avoid Counterfactuals**: Focus on what happened and improvements, not "should have" statements
**Severity Criteria**: Use clear, objective criteria for severity classification
**On-Call Rotation Health**: Monitor on-call load; too many pages indicates systemic reliability issues
**Trend Analysis**: Regularly review incident trends to identify systemic issues requiring architecture changes
**Runbook Updates**: Update runbooks immediately after incidents based on lessons learned
**Celebrate Learning**: Recognize incidents as learning opportunities, not failures

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

**SRE & Blameless Postmortem Principles**:
- Google SRE Book (blameless postmortems, error budgets, toil reduction)
- Site Reliability Engineering Workbook (postmortem culture and templates)
- Blameless culture (focus on systems/processes, not individuals)
- Just culture (learning from failures, psychological safety)
- No blame, no shame postmortems (constructive, improvement-focused)
- Error budgets (SLO-based reliability management)
- SLI/SLO framework (Service Level Indicators and Objectives)

**Incident Management Frameworks**:
- ITIL 4 Incident Management (incident lifecycle, classification, escalation)
- PagerDuty Incident Response (modern incident management practices)
- Atlassian Incident Management Handbook
- Google's Incident Management at Scale
- Major Incident Management (MIM) best practices
- Incident Command System (ICS, structured incident response)

**Incident Severity Classifications**:
- SEV0/P0/Critical (complete outage, all users affected, immediate response)
- SEV1/P1/High (major functionality degraded, significant user impact)
- SEV2/P2/Medium (partial degradation, limited user impact)
- SEV3/P3/Low (minor issues, minimal impact)
- SEV4/P4/Informational (no customer impact)
- Severity escalation criteria (when to escalate severity level)

**Incident Management Platforms**:
- PagerDuty (alerting, on-call scheduling, incident tracking)
- Opsgenie (incident management, on-call management)
- ServiceNow (ITSM, incident tracking, change management)
- Jira Service Management (incident and problem management)
- VictorOps/Splunk On-Call (incident response platform)
- Incident.io (incident management and postmortems)
- FireHydrant (incident response and retrospectives)

**Root Cause Analysis Methodologies**:
- 5 Whys (iterative questioning to find root cause)
- Ishikawa diagram/Fishbone diagram (categorizing contributing factors)
- Fault Tree Analysis (FTA, systematic failure analysis)
- Failure Mode and Effects Analysis (FMEA)
- Pareto analysis (80/20 rule, identifying most impactful causes)
- Timeline analysis (detailed chronological event reconstruction)
- Contributing factors analysis (multiple causes, not single root cause)

**MTTR/MTTD/MTTA Metrics**:
- MTTD (Mean Time To Detect, time from failure to detection)
- MTTA (Mean Time To Acknowledge, time from detection to acknowledgment)
- MTTR (Mean Time To Recovery/Repair, time from detection to resolution)
- MTTF (Mean Time To Failure, time between incidents)
- MTBF (Mean Time Between Failures)
- Incident frequency (incidents per month/quarter)
- Repeat incident rate (percentage of recurring incidents)

**SLO/Error Budget Management**:
- SLI/SLO definition (latency, availability, error rate, throughput)
- Error budget calculation (1 - SLO = error budget)
- Error budget consumption (tracking budget burn during incidents)
- Error budget policies (response when budget is exhausted)
- SLO-based alerting (alert on SLO violations, not symptoms)
- Burn rate analysis (how fast error budget is consumed)

**Communication & Notification**:
- Status pages (StatusPage.io, Atlassian Statuspage, custom)
- Incident communication templates (initial, update, resolution, postmortem)
- Stakeholder notification procedures (internal, external, regulatory)
- War room/bridge protocols (Slack channels, Zoom bridges, communication norms)
- Customer communication (transparency, apology, resolution timeline)
- Regulatory notification (GDPR breach notification, industry-specific requirements)

**Remediation Action Tracking**:
- Action item management (Jira, GitHub Issues, ServiceNow)
- Priority classification (P0/P1/P2/P3)
- Owner assignment (responsible individual or team)
- Due date tracking (target completion dates)
- Status tracking (not started, in progress, completed, blocked)
- Verification (how to confirm fix prevents recurrence)

**Observability & Monitoring**:
- Prometheus, Grafana (metrics and dashboards)
- Datadog, New Relic (APM and infrastructure monitoring)
- ELK Stack, Splunk (log aggregation and analysis)
- Honeycomb, Lightstep (distributed tracing, observability)
- Sentry (error tracking and alerting)
- Incident response dashboards (real-time incident visibility)

**Compliance & Regulatory**:
- SOC 2 (incident response and documentation requirements)
- ISO 27001 (information security incident management)
- GDPR Article 33 (data breach notification within 72 hours)
- PCI-DSS Requirement 12.10 (incident response plan)
- HIPAA Security Rule (incident reporting for covered entities)
- Regulatory breach notification timelines

**Postmortem Documentation**:
- Incident summary (what happened, impact, resolution)
- Timeline (detailed chronological events with timestamps)
- Root cause (what caused the incident)
- Contributing factors (all factors that contributed)
- What went well (effective response actions)
- What went poorly (gaps, failures, areas for improvement)
- Action items (remediation with owners and due dates)
- Lessons learned (knowledge captured for organization)

**On-Call & Escalation**:
- On-call rotation (PagerDuty, Opsgenie schedules)
- Escalation policies (tier 1/2/3, management escalation)
- On-call runbooks (incident response procedures)
- War room procedures (bridge setup, communication norms)
- Incident commander role (single point of coordination)
- Subject matter expert (SME) identification and engagement

**Learning & Knowledge Management**:
- Postmortem review meetings (facilitated, blameless discussions)
- Incident knowledge base (searchable repository of past incidents)
- Pattern recognition (identifying recurring failure modes)
- Trend analysis (incident frequency, MTTR trends over time)
- Training (using incidents as learning opportunities)
- Best practice sharing (cross-team knowledge dissemination)

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
