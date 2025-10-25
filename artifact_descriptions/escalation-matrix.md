# Name: escalation-matrix

## Executive Summary

The Escalation Matrix is a structured reference document that defines support tier responsibilities (L1/L2/L3), escalation paths, contact information, and SLA response times for incident management. This critical operational artifact ensures rapid, appropriate escalation of production incidents by mapping incident types and severity levels to responsible teams, specialists, and subject matter experts with defined escalation criteria and communication protocols.

Aligned with ITIL 4 service desk practices and Google SRE on-call models, this matrix integrates with incident management platforms (PagerDuty, Opsgenie, Incident.io) to automate escalation workflows, enforce SLA compliance, and provide 24/7 contact directories. It defines clear L1 (first responder) → L2 (specialist) → L3 (expert/architect) → management escalation chains with time-based triggers, complexity thresholds, and cross-team coordination procedures.

### Strategic Importance

- **Rapid Escalation**: Reduces time to engage appropriate expertise by 50-70% through predefined escalation paths
- **SLA Compliance**: Ensures incidents escalate within defined timeframes (P0: 15min, P1: 1hr, P2: 4hrs)
- **Clear Accountability**: Eliminates confusion about who to contact for specific incident types or system components
- **24/7 Coverage**: Maintains current contact information across time zones for follow-the-sun support
- **Multi-Tier Support**: Optimizes resource utilization by routing incidents to appropriate skill levels
- **Cross-Team Coordination**: Facilitates handoffs between platform, application, database, and security teams
- **Audit Trail**: Documents escalation procedures for SOC 2, ISO 27001, and compliance requirements

## Purpose & Scope

### Primary Purpose

This artifact provides the authoritative reference for incident escalation paths, support tier responsibilities, and contact information across the organization. It solves the problem of delayed incident resolution by clearly defining when and to whom incidents should be escalated based on severity, complexity, and time elapsed, ensuring the right expertise engages at the right time.

### Scope

**In Scope**:
- L1/L2/L3 support tier definitions and responsibilities (L1: triage, L2: specialized troubleshooting, L3: architecture/expert)
- Escalation paths by incident type (application, infrastructure, database, network, security)
- Escalation paths by severity level (P0/SEV0, P1/SEV1, P2/SEV2, P3/SEV3)
- Time-based escalation triggers (e.g., escalate to L2 if unresolved after 30 minutes)
- Contact directory with phone numbers, Slack handles, email addresses, and time zones
- On-call rotation references for each support tier
- Management escalation chains (Director → VP → CTO → CEO)
- Cross-functional escalation (Engineering → Product → Customer Success → Legal)
- SLA response time targets by severity and support tier
- Follow-the-sun handoff procedures between geographic regions

**Out of Scope**:
- Detailed troubleshooting procedures (covered in playbooks artifact)
- On-call rotation schedules (covered in on-call-handbook artifact)
- Root cause analysis procedures (covered in root-cause-analyses artifact)
- Post-incident review processes (covered in post-mortem-report artifact)
- Individual employee performance management

### Target Audience

**Primary Audience**:
- On-Call Engineers making real-time escalation decisions during incidents
- Incident Commanders coordinating cross-team response efforts
- Support Engineers triaging customer-reported issues
- SRE Teams managing production system incidents

**Secondary Audience**:
- Engineering Managers understanding team escalation responsibilities
- Operations Managers maintaining contact directories and rotation coverage
- Customer Success Teams escalating customer-impacting incidents
- Executive Leadership receiving escalations for critical business-impacting incidents

## Document Information

**Format**: Markdown

**File Pattern**: `*.escalation-matrix.md`

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

**Clear Tier Definitions**: Define L1/L2/L3 responsibilities explicitly (L1: triage and basic troubleshooting, L2: specialized diagnosis, L3: architectural expertise)
**Time-Based Triggers**: Specify exact escalation timelines (e.g., "Escalate to L2 if unresolved after 30 minutes on P0 incident")
**Multiple Contact Methods**: Provide phone, email, Slack handle, and PagerDuty/Opsgenie identifier for each contact
**Timezone Awareness**: Always include timezone for each contact (e.g., "John Doe (UTC-8)") to support follow-the-sun
**Automated Enforcement**: Configure PagerDuty/Opsgenie escalation policies to match matrix for automatic escalation
**Visual Matrix Format**: Use table format mapping incident types × severity levels to responsible teams
**Current Contacts**: Review and update contact information monthly; mark any outdated entries immediately
**Escalation Criteria**: Define specific conditions triggering escalation (time elapsed, complexity, impact, SLA risk)
**Manager Escalation Path**: Define clear Director → VP → C-level chain for business-critical escalations
**Cross-Functional Paths**: Document when to engage Product, Legal, PR, Customer Success teams
**No Ambiguity**: Avoid "may escalate" language; use "must escalate when..." with specific conditions
**Backup Contacts**: Always list secondary and tertiary contacts in case primary is unavailable
**Platform Integration**: Sync matrix with incident management platform configurations bi-weekly
**Regular Testing**: Test escalation paths quarterly with simulated incidents (gamedays)
**Compliance Evidence**: Maintain audit trail of escalation path reviews for SOC 2 and ISO 27001
**Quick Reference**: Provide one-page quick-reference guide for most common escalation scenarios
**Self-Service Access**: Publish matrix in centralized wiki accessible 24/7 to all on-call engineers

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

**Support Tier Models**:
- ITIL 4 Service Desk and Incident Management (L1/L2/L3 tier definitions)
- Multi-Level Support Model (Gartner framework)
- Google SRE escalation ladder concept
- Three-Tier Support Architecture (First Line, Second Line, Third Line)

**Incident Severity Classification**:
- SEV0/P0 (Critical): Complete outage, revenue impact, all customers affected
- SEV1/P1 (High): Major degradation, significant customer impact
- SEV2/P2 (Medium): Limited impact, workaround available
- SEV3/P3 (Low): Minor issues, no immediate impact
- SLA Response Times: P0: 15min, P1: 1hr, P2: 4hrs, P3: next business day

**Escalation Management Platforms**:
- PagerDuty Escalation Policies (automated time-based and manual escalation)
- Opsgenie Escalation Rules (conditional escalation workflows)
- VictorOps (Splunk On-Call) Escalation Chains
- Incident.io (Slack-native escalation workflows)
- ServiceNow Incident Management (ITSM escalation)
- Jira Service Management (Atlassian)

**Contact Directory Standards**:
- RFC 2142 (Mailbox Names for Common Services)
- E.164 international phone number format
- ISO 8601 time zone representation
- Organizational contact schema (name, role, phone, email, Slack, timezone)

**Escalation Triggers**:
- Time-based escalation (no response in X minutes)
- SLA breach imminent (approaching deadline)
- Complexity-based escalation (L1 unable to diagnose)
- Impact-based escalation (increasing customer/revenue impact)
- Severity escalation (incident upgraded from P2 to P1)
- Cross-team dependency (requires specialized expertise)

**Communication Channels**:
- Slack incident channels (#incidents, #sev0, #sev1)
- Microsoft Teams incident rooms
- Conference bridges (Zoom, Google Meet, dedicated dial-in)
- SMS/text notifications for critical escalations
- Email distribution lists by tier and specialty

**Follow-the-Sun Support**:
- APAC → EMEA → Americas handoff model
- 24/7 coverage with regional on-call rotations
- Handoff documentation and communication protocols
- Timezone coordination (UTC standardization)

**Compliance Standards**:
- SOC 2 Type II (defined escalation procedures)
- ISO 27001 (incident escalation controls)
- ITIL Service Management
- PCI-DSS (security incident escalation)

**Reference**: Consult SRE leadership and operations team for escalation policy standards

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
