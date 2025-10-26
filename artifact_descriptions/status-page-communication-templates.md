# Name: status-page-communication-templates

## Executive Summary

The Status Page Communication Templates provide pre-approved, standardized message templates for communicating service incidents, maintenance windows, degradations, and resolutions through status page platforms like Statuspage.io (Atlassian), Sorry, Incident.io, and StatusGator. These templates ensure consistent, transparent, and timely communication during service disruptions, maintaining customer trust while meeting SLA notification requirements and regulatory transparency obligations.

Status pages have become the primary channel for service availability communication, with 89% of enterprise SaaS customers checking status pages during perceived outages. Poorly communicated incidents damage customer trust more than the incidents themselves. These templates establish tone, timing, and technical detail standards for incident communication across severity levels (SEV-0 through SEV-4), ensuring teams communicate with appropriate urgency while avoiding premature commitments during active investigations.

### Strategic Importance

- **Incident Transparency**: Provides real-time service status updates to customers during outages, reducing support ticket volume by 40-60%
- **SLA Compliance**: Meets contractual notification requirements for availability incidents and planned maintenance windows
- **Customer Trust**: Maintains transparency during service disruptions with clear, jargon-free incident communication
- **Support Deflection**: Reduces inbound customer inquiries during incidents by proactively communicating status and ETAs
- **Postmortem Communication**: Standardizes incident postmortem publication with root cause, timeline, and prevention measures
- **Regulatory Reporting**: Supports incident notification requirements under SOC 2 (availability criteria) and GDPR (breach notification timelines)
- **Brand Protection**: Ensures professional, empathetic communication tone during high-stress incident situations

## Purpose & Scope

### Primary Purpose

This artifact serves as the template library for all customer-facing service status communications, ensuring consistent messaging during incidents, maintenance windows, and service degradations. Templates define what to communicate, when, and with what level of technical detail across incident severity levels and communication phases (investigating, identified, monitoring, resolved).

### Scope

**In Scope**:
- Incident communication templates (investigating, identified, monitoring, resolved, postmortem phases)
- Severity-based templates (SEV-0 complete outage, SEV-1 major degradation, SEV-2 minor impact, SEV-3 cosmetic)
- Maintenance window notifications (scheduled maintenance, emergency maintenance, maintenance completed)
- Service degradation alerts (partial outage, performance degradation, intermittent issues)
- SLA incident reporting (SLA breach notifications, uptime reporting, availability metrics)
- Postmortem publication templates (root cause, timeline, impact summary, prevention measures)
- Status page platform integration (Statuspage.io, Sorry, Incident.io, StatusGator, Instatus)
- Multi-channel notification (status page, email subscribers, SMS alerts, Slack/Teams webhooks, RSS feeds)

**Out of Scope**:
- Security incident communications (covered in breach notification templates under GDPR requirements)
- Individual customer support ticket responses (handled by support team templates)
- Internal incident response procedures (documented in incident runbooks)
- Social media crisis communication (managed by PR and communications team)
- Press releases for major outages (coordinated through corporate communications)
- API status and rate limit notifications (handled through developer documentation)

### Target Audience

**Primary Audience**:
- Incident Commanders: Lead incident response and own customer communication during active incidents
- On-Call Engineers: Post initial status updates and ongoing investigation progress
- Customer Support Teams: Reference status page to deflect tickets and understand incident scope

**Secondary Audience**:
- Product Management: Understand incident communication standards and customer impact messaging
- Engineering Leadership: Review postmortem communication for accuracy and completeness
- Legal & Compliance: Ensure incident notifications meet SLA and regulatory requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.status-page-communication-templates.md`

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

**15-Minute Rule**: Post initial "Investigating" status update within 15 minutes of SEV-0/SEV-1 incident detection, even with minimal details
**No Premature ETAs**: Avoid estimating resolution time during "Investigating" phase; only provide ETAs once root cause is identified
**Plain Language**: Communicate in customer-friendly language, avoiding internal jargon (bad: "RDS failover timeout," good: "database connection issues")
**Impact-First Communication**: Lead with customer impact ("Some customers may experience errors") before technical details
**Update Frequency**: SEV-0 updates every 30 min, SEV-1 every 60 min, SEV-2 every 2 hours minimum
**Component-Based Status**: Update specific affected components (API, Dashboard, Email Delivery) rather than blanket "Service Disruption"
**Monitoring Phase Transparency**: After mitigation, keep incident in "Monitoring" status for 30-60 min to confirm stability
**72-Hour Postmortem**: Publish postmortem within 72 hours of SEV-0/SEV-1 resolution (Stripe, GitHub, Cloudflare standard)
**Blameless Language**: Never name individuals or teams in public postmortems; focus on systems and processes
**Quantify Impact**: Include specific impact metrics (e.g., "Affected 3% of API requests from 14:23-14:47 UTC")
**UTC Timestamps**: Always use UTC time in status updates to avoid timezone confusion for global customers
**SMS for Critical**: Enable SMS alerts for SEV-0/SEV-1 incidents affecting availability SLAs
**Status Page Testing**: Test status page notification systems monthly to ensure subscriber alerts function properly
**Maintenance Window Notice**: Provide 7 days advance notice for scheduled maintenance affecting availability
**Resolved vs Monitoring**: Move to "Resolved" only after 30+ minutes of stable service post-mitigation
**Root Cause Honesty**: If root cause is unknown in postmortem, state "investigation ongoing" rather than speculating
**Action Items Public**: Publish specific prevention measures in postmortems with completion targets
**Subscriber Segmentation**: Allow customers to subscribe to specific components/services rather than all incidents
**Template Approval**: Require incident commander approval before deviating from standard templates
**Historical Context**: Reference previous similar incidents in postmortems if pattern exists

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

**Status Page Platforms**:
- Statuspage.io (Atlassian) - Industry-leading status page with incident templates and subscriber management
- Sorry - Modern status page with component-based architecture and beautiful design
- Incident.io - Incident management with integrated status page and Slack workflows
- StatusGator - Multi-vendor status page aggregation and monitoring
- Instatus - Fast, customizable status page with real-time updates
- Cachet - Open-source status page system
- StatusKit - Simple status page for small teams
- UptimeRobot Status Pages - Monitoring-integrated status communication

**Incident Severity Classifications**:
- SEV-0/P0: Complete service outage affecting all customers (communicate within 15 minutes)
- SEV-1/P1: Major degradation affecting core functionality (communicate within 30 minutes)
- SEV-2/P2: Partial outage or minor degradation (communicate within 60 minutes)
- SEV-3/P3: Cosmetic issues or limited impact (communicate within 4 hours)
- SEV-4/P4: No customer impact, internal-only tracking

**SLA & Availability Standards**:
- SLA tiers: 99.9% (43.8 min/month downtime), 99.95% (21.9 min/month), 99.99% (4.4 min/month)
- Uptime reporting: Monthly uptime percentage, incident count, MTTR (Mean Time To Resolution)
- Availability zones: Multi-region redundancy and failover communication
- Maintenance windows: Standard windows (low-traffic periods), emergency maintenance protocols

**Incident Communication Frameworks**:
- Incident Communication Lifecycle: Investigating → Identified → Monitoring → Resolved → Postmortem
- Update Frequency Standards: SEV-0 every 30 min, SEV-1 every 60 min, SEV-2 every 2 hours
- Postmortem Timeline: Publish within 72 hours of incident resolution (Stripe standard)
- Five Whys Root Cause Analysis: Structured root cause investigation and communication

**Regulatory & Compliance**:
- SOC 2 Type II Availability Criteria: Incident notification and availability reporting requirements
- GDPR Article 33: 72-hour breach notification (if security incident affects personal data)
- ISO 27001 Annex A.16: Incident management and communication procedures
- PCI DSS Requirement 12.10: Incident response plan and communication protocols
- ITIL v4 Incident Management: Incident classification, communication, and escalation

**Notification Channels**:
- Email notifications: Subscriber-based alerts with severity filtering
- SMS/Text alerts: High-severity incident notifications (SEV-0/SEV-1)
- Slack/Teams webhooks: Real-time incident updates to customer workspaces
- RSS/Atom feeds: Machine-readable incident feed for automation
- Twitter/Status accounts: Public incident communication and updates
- Mobile push notifications: In-app status alerts (Statuspage mobile app)

**Monitoring & Alerting Integration**:
- Datadog: Service monitoring with automatic status page updates
- PagerDuty: Incident management with status page integration
- New Relic: Application monitoring with availability tracking
- Pingdom: Uptime monitoring with public status display
- UptimeRobot: Automated status page updates from monitoring checks

**Postmortem Standards**:
- Blameless Postmortems: Focus on systems and processes, not individuals
- Timeline Format: UTC timestamps, customer-visible impact windows
- Root Cause Analysis: What happened, why, how detected, how resolved
- Prevention Measures: Concrete action items with owners and due dates
- Five Nines Availability: Publish all SEV-0/SEV-1 incidents affecting availability SLAs

**Reference**: Consult incident management and customer success teams for detailed guidance on status communication standards and escalation procedures

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
