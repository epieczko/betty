# Name: troubleshooting-trees

## Executive Summary

The Troubleshooting Trees artifact provides structured decision tree diagrams and flowcharts that guide IT operations teams, SRE engineers, and support personnel through systematic problem isolation and resolution. These visual diagnostic tools use binary decision logic (yes/no branches) to narrow root causes, identify appropriate remediation actions, and determine escalation paths when automated or first-level resolution fails.

Troubleshooting trees integrate with runbook automation platforms (PagerDuty Runbook Automation, Rundeck), incident management systems (ServiceNow, Jira), and observability tools (Datadog, Splunk, Grafana) to provide context-aware guidance. They support ITIL problem management practices, reduce Mean Time to Resolution (MTTR), standardize diagnostic approaches across teams, and enable junior engineers to resolve complex incidents with expert-level decision-making frameworks. The trees are typically created using diagramming tools like Lucidchart, Miro, draw.io, or embedded in knowledge bases like Confluence and Notion.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact serves as a visual decision support tool that systematically guides troubleshooting through branching logic, root cause isolation, and resolution action identification. It reduces MTTR, standardizes diagnostic procedures, enables knowledge transfer from senior to junior staff, and provides clear escalation criteria when issues cannot be resolved at current support tier.

### Scope

**In Scope**:
- Binary decision tree diagrams (yes/no, true/false branching)
- Multi-level troubleshooting flows from symptom to root cause
- Integration points to runbooks and remediation procedures
- Escalation criteria and handoff points to L2/L3/vendor support
- Common failure scenarios for applications, infrastructure, and networks
- Diagnostic command sequences and validation checks
- Links to monitoring dashboards and log query examples
- Known issue references and workaround procedures
- Automated remediation triggers and self-healing integration
- Visual representations using flowchart notation (start/end, decision diamonds, process rectangles)
- System-specific trees (database, network, application, platform)
- Service-level trees organized by customer-impacting services

**Out of Scope**:
- Detailed step-by-step runbooks (separate artifacts)
- Root cause analysis deep-dives and postmortems
- Change management and deployment procedures
- Monitoring alert configuration and tuning
- Long-term architectural remediation plans
- Training curricula for complex system administration

### Target Audience

**Primary Audience**:
- IT Operations teams responding to incidents
- Help Desk and L1 support personnel
- Site Reliability Engineers (SRE) on-call rotation
- DevOps engineers troubleshooting deployments
- NOC (Network Operations Center) analysts

**Secondary Audience**:
- Platform engineering teams designing self-service diagnostics
- Technical trainers creating troubleshooting curriculum
- Incident commanders coordinating major incident response
- Knowledge management teams curating diagnostic content

## Document Information

**Format**: Markdown

**File Pattern**: `*.troubleshooting-trees.md`

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

**Start with Symptoms, Not Solutions**: Begin decision trees with observable symptoms (customer impact, error messages, alerts) rather than assumed root causes
**Binary Decision Logic**: Use clear yes/no questions at each decision node to minimize ambiguity and enable rapid navigation
**Maximum 3-5 Levels Deep**: Keep trees shallow to prevent cognitive overload; deeper diagnostics should branch to separate detailed trees
**Link to Runbooks**: Each terminal node should reference specific runbooks or remediation procedures rather than embedding all steps
**Include Diagnostic Commands**: Provide exact CLI commands, API calls, or dashboard queries needed at each decision point
**Escalation Thresholds**: Clearly define when to escalate (time thresholds, skill requirements, customer impact levels)
**Visual Consistency**: Use standardized flowchart symbols (ISO 5807) with consistent color coding for action types
**Embed Dashboard Links**: Include direct links to relevant Grafana/Datadog/Splunk dashboards for real-time validation
**Reference Known Errors**: Link to KEDB entries and previous incident tickets with similar symptom patterns
**Update from Incidents**: Systematically update trees after major incidents to incorporate new failure modes
**Collaborative Creation**: Involve on-call engineers in tree development to capture actual troubleshooting mental models
**Mobile Accessibility**: Ensure trees are readable on mobile devices for on-call engineers accessing remotely
**Search Optimization**: Tag trees with keywords for easy discovery in knowledge base searches
**Version in Git**: Store diagram source files (Mermaid, PlantUML) in Git alongside infrastructure-as-code for change tracking
**Automation Hooks**: Design trees with automation trigger points where self-healing can execute without human intervention
**Feedback Loops**: Collect usage metrics and user feedback to identify confusing branches or missing scenarios
**Living Documentation**: Schedule quarterly reviews to prune outdated branches and add new failure patterns
**Scenario Testing**: Walk through trees during game days and disaster recovery exercises to validate accuracy
**Progressive Disclosure**: Provide summary trees for quick triage with links to detailed sub-trees for complex scenarios
**Context Preservation**: Include relevant environment info (prod vs. staging, region, version) in decision criteria

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

**Diagramming & Visualization Tools**:
- Lucidchart for cloud-based collaborative flowcharts
- Miro for interactive troubleshooting boards
- draw.io (diagrams.net) for open-source diagramming
- Microsoft Visio for enterprise flowchart creation
- Mermaid.js for markdown-based diagram-as-code
- PlantUML for text-based UML and flowcharts
- Excalidraw for hand-drawn style diagrams
- Whimsical for rapid visual documentation

**Runbook Automation & Orchestration**:
- PagerDuty Runbook Automation for incident response
- Rundeck for self-service operations and diagnostics
- StackStorm for event-driven automation
- Ansible Playbooks for remediation automation
- AWS Systems Manager Automation for cloud remediation
- Azure Automation Runbooks
- Google Cloud Workflows
- Shoreline.io for automated incident remediation

**Incident Management Systems**:
- ServiceNow Incident Management and Knowledge Base
- Jira Service Management with integrated runbooks
- PagerDuty for on-call incident routing
- Opsgenie for alert aggregation and escalation
- VictorOps/Splunk On-Call for collaborative response
- Atlassian Statuspage for customer communication

**Observability & Monitoring**:
- Datadog for infrastructure and APM troubleshooting
- Splunk for log analysis and correlation
- Grafana dashboards for visual diagnostics
- Prometheus with AlertManager for metric-based troubleshooting
- New Relic for application performance diagnostics
- Dynatrace for AI-powered root cause analysis
- Elastic Stack (ELK) for centralized logging
- Honeycomb.io for observability-driven debugging

**ITIL & Service Management**:
- ITIL 4 Problem Management practices
- ITIL Service Operation processes
- Known Error Database (KEDB) integration
- Major Incident Management procedures
- Service Desk and escalation models

**SRE & DevOps Practices**:
- Google SRE troubleshooting frameworks
- SRE on-call runbooks and playbooks
- Incident response team structures
- Blameless postmortem methodologies
- Chaos engineering for failure scenario testing

**Knowledge Management**:
- Confluence for centralized troubleshooting wikis
- Notion for collaborative diagnostic documentation
- Stack Overflow for Teams for internal Q&A
- Document360 for customer-facing knowledge bases
- Guru for distributed knowledge capture

**Flowchart Standards**:
- ISO 5807 (Information Processing - Documentation Symbols)
- ANSI/ISO flowchart notation standards
- BPMN (Business Process Model and Notation) for process flows
- UML Activity Diagrams for complex troubleshooting logic

**Incident Response Frameworks**:
- NIST SP 800-61 (Incident Handling Guide)
- SANS Incident Handler's Handbook
- FIRST (Forum of Incident Response and Security Teams) guidelines
- PCI DSS Incident Response requirements

**Automation & Self-Healing**:
- AIOps platforms for intelligent troubleshooting
- ServiceNow Event Management for automated correlation
- BigPanda for alert correlation and suppression
- Moogsoft for AI-driven incident detection

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
