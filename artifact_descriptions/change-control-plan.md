# Name: change-control-plan

## Executive Summary

The Change Control Plan establishes a comprehensive IT change management framework aligned with ITIL 4 Change Enablement practices, ISO/IEC 20000-1 change management requirements, and COBIT 2019 governance principles to ensure controlled, risk-assessed, and properly authorized modifications to IT infrastructure, applications, databases, network devices, cloud services, and security configurations. This critical operational plan implements structured change workflows, Change Advisory Board (CAB) governance, emergency change procedures, and continuous improvement mechanisms to maximize successful change implementation while minimizing service disruptions, security incidents, and compliance violations.

Modern change management leverages IT Service Management (ITSM) platforms including ServiceNow Change Management, Jira Service Management, BMC Remedy, Cherwell, or Ivanti Service Manager to automate change request submission, approval routing, impact analysis, risk assessment, scheduling coordination, implementation tracking, and post-implementation review. The plan categorizes changes into Standard Changes (pre-approved, low-risk, well-documented procedures like password resets, certificate renewals, routine patching), Normal Changes (requiring CAB assessment and formal approval for moderate-risk modifications like application upgrades, configuration changes, infrastructure modifications), and Emergency Changes (expedited approval for urgent fixes addressing critical incidents, security vulnerabilities, or regulatory compliance failures).

Change workflows integrate with Configuration Management Database (CMDB) for impact analysis across configuration items (CIs), release management for coordinated deployments, incident management for emergency change triggers, problem management for root cause remediation changes, and capacity management for infrastructure changes. Risk assessment evaluates change complexity, blast radius, rollback capability, security implications, and timing constraints to classify changes as Low/Medium/High/Very High risk, determine appropriate approval authority (automated approval vs. CAB vs. Emergency CAB vs. executive approval), and establish testing and backout requirements. Change scheduling coordinates with maintenance windows, blackout periods (end-of-quarter financial close, holiday shopping season, tax filing deadlines), and deployment freeze periods while balancing business agility needs with stability requirements.

### Strategic Importance

- **Service Stability & Availability**: Reduces unplanned outages and service degradation caused by poorly planned changes; improves Mean Time Between Failures (MTBF) through controlled change implementation
- **Compliance & Audit Readiness**: Satisfies SOC 2 CC8.1, ISO 27001 A.8.32, PCI DSS 6.5.1, HIPAA 164.308(a)(8), and SOX ITGC change management control requirements with documented approvals, testing evidence, and audit trails
- **Security Risk Management**: Prevents security control bypasses, configuration drift, and unauthorized access through structured change authorization, segregation of duties enforcement, and security review for high-risk changes
- **Change Success Rate Optimization**: Increases successful change implementation rate (target >95%) and reduces failed changes, emergency rollbacks, and post-implementation defects through proper planning, testing, and risk assessment
- **Business Agility Enablement**: Balances governance rigor with deployment speed through standard change pre-approvals, automated change workflows, and DevOps-friendly continuous deployment integration
- **Incident Prevention**: Proactively identifies conflicting changes, configuration dependencies, and timing risks before implementation to prevent change-induced incidents and service disruptions
- **Transparency & Communication**: Provides stakeholders with visibility into planned changes, impact assessment, and maintenance schedules; enables coordinated business planning around IT changes

## Purpose & Scope

### Primary Purpose

This plan defines end-to-end change management processes, governance structures, approval authorities, risk assessment criteria, implementation procedures, rollback protocols, and metrics/reporting to ensure all IT changes are properly evaluated, authorized, tested, implemented, and reviewed. It establishes the operational framework for managing technical changes across the enterprise while balancing risk management with business agility.

### Scope

**In Scope**:
- **Change Categories**: Standard Changes (pre-approved low-risk procedures), Normal Changes (CAB-reviewed moderate-risk changes), Emergency Changes (urgent high-risk changes), Major Changes (high-impact transformational initiatives requiring executive approval)
- **Change Types**: Infrastructure changes (servers, storage, network devices, virtualization), application changes (code deployments, configuration updates, database schema), cloud platform changes (AWS/Azure/GCP configurations, IaaS/PaaS modifications), security changes (firewall rules, access controls, security patches), network changes (routing, switching, load balancing, DNS), database changes (schema modifications, stored procedures, data migrations)
- **Change Advisory Board (CAB)**: CAB membership (IT leadership, application owners, security, compliance, business stakeholders), meeting cadence (weekly CAB for normal changes, ad-hoc Emergency CAB for urgent changes), quorum requirements, voting procedures, escalation to executive steering committee
- **Approval Workflows**: Standard change auto-approval based on documented procedures, normal change multi-level approval (requester → technical lead → CAB → change manager), emergency change expedited approval (on-call change manager → emergency CAB), major change executive approval (CIO, CTO, CISO)
- **Risk Assessment**: Change complexity scoring (simple/moderate/complex), blast radius analysis (number of affected systems/users), rollback capability evaluation (automated rollback, manual rollback, no rollback), security impact review, compliance implications, timing risk (blackout periods, maintenance windows)
- **Change Scheduling**: Maintenance window management (scheduled maintenance windows by environment), blackout period enforcement (no changes during critical business periods), change calendar coordination, conflict detection (overlapping changes to same CI), resource allocation (implementation teams, subject matter experts)
- **Implementation Requirements**: Pre-implementation testing (dev/test/staging validation), implementation plan documentation, rollback/backout procedures, success criteria definition, smoke testing procedures, communication plans (stakeholder notifications, service desk alerts)
- **Integration with ITIL Processes**: CMDB integration for CI dependency analysis, incident management integration for emergency change triggers, problem management integration for permanent fixes, release management coordination for bundled changes, service catalog integration for standard change requests
- **ITSM Platform Implementation**: ServiceNow Change Management module configuration, Jira Service Management workflows, BMC Remedy Change Management, approval automation, notification automation, change calendar visualization, reporting dashboards
- **Metrics & KPIs**: Change success rate (target >95%), emergency change percentage (target <5%), mean time to implement (MTTI), CAB approval cycle time, change-related incidents, unauthorized changes detected, change backlog aging, standard change utilization rate

**Out of Scope**:
- **Incident Management**: Covered in incident-response-plan artifact (incident detection, triage, escalation, resolution, post-incident review)
- **Problem Management**: Covered in problem-management-process artifact (root cause analysis, known error database, permanent solution implementation, proactive problem identification)
- **Release & Deployment Management**: Covered in release-management-plan artifact (release planning, build management, deployment automation, release validation)
- **Configuration Management**: Covered in configuration-management-plan artifact (CMDB design, CI discovery, relationship mapping, configuration baseline management)
- **Patch Management**: Covered in patch-management-policy artifact (patch testing, vulnerability prioritization, patch deployment schedules, compliance tracking)
- **Software Development Lifecycle (SDLC)**: Covered in secure-sdlc-policy artifact (code review, security testing, CI/CD pipelines, DevOps practices)
- **Business Continuity & Disaster Recovery**: Covered in bcdr-plan artifact (disaster declaration, failover procedures, recovery time objectives)

### Target Audience

**Primary Audience**:
- **Change Manager**: Chairs CAB meetings, reviews change requests for completeness, coordinates change scheduling, enforces change policy, tracks metrics, facilitates post-implementation reviews
- **Change Advisory Board (CAB) Members**: Reviews and approves/rejects normal changes, assesses risk and impact, provides technical expertise, represents business stakeholder interests, validates implementation plans
- **IT Operations Teams**: Submits change requests for infrastructure modifications, implements approved changes, executes rollback procedures if needed, provides post-implementation status updates
- **Application Development Teams**: Submits change requests for application deployments, provides technical details and testing evidence, coordinates with operations for implementation, monitors post-deployment application health
- **IT Service Desk**: Logs change requests on behalf of users, communicates scheduled maintenance to end users, monitors change-related incidents, escalates failed changes

**Secondary Audience**:
- **Chief Information Officer (CIO)**: Approves major changes and change policy, reviews change metrics and success rates, allocates budget for change management tooling, escalation point for disputed change decisions
- **Chief Technology Officer (CTO)**: Provides technical direction for change processes, approves architectural changes, champions DevOps and automation initiatives, balances innovation with stability
- **Chief Information Security Officer (CISO)**: Reviews security-impacting changes, approves security control modifications, ensures segregation of duties in change approval, investigates unauthorized changes
- **Compliance & Audit Teams**: Validates change management controls for SOC 2, ISO 20000, PCI DSS audits, reviews approval evidence, tests segregation of duties, samples change documentation completeness
- **Business Unit Leaders**: Provides input on blackout periods and business-critical timing, approves changes affecting their applications/services, participates in CAB for major changes, communicates change impacts to business stakeholders
- **External Auditors**: Reviews change management process during SOC 2, ISO 27001, PCI DSS assessments, validates change controls, tests approval workflows, confirms emergency change justifications

## Document Information

**Format**: Markdown

**File Pattern**: `*.change-control-plan.md`

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
**Market Validation**: Validate assumptions with market research and customer feedback
**Financial Rigor**: Use discounted cash flow, NPV, and scenario analysis for financial projections
**Competitive Intelligence**: Incorporate competitive analysis and market positioning
**Standard Changes are Key to Agility**: Document and pre-approve frequent low-risk changes (password resets, certificate renewals, routine patches) to avoid CAB bottlenecks; target 60-70% standard change utilization
**CAB Meetings Keep Moving**: Time-box CAB meetings to 60-90 minutes; defer complex discussions to working groups; focus on risk/go-no-go decisions
**Risk Assessment Framework**: Implement consistent risk scoring (complexity + blast radius + rollback capability) to objectively classify changes and determine approval level
**Emergency Change Criteria**: Clearly define what constitutes an emergency (production outage, critical security vulnerability, regulatory deadline); prevent routine work from being classified as emergency to bypass governance
**Segregation of Duties**: Enforce separation between change requesters, approvers, and implementers for SOX/PCI compliance; developers cannot approve or deploy their own changes to production
**Automated Change Windows**: Implement automated change windows in ITSM tool; system automatically approves/rejects changes based on blackout periods and maintenance schedules
**Change-Related Incident Tracking**: Tag incidents caused by changes; calculate change failure rate and root cause categories to drive continuous improvement
**CMDB Integration Essential**: Accurate CMDB enables automated impact analysis; changes to web server auto-identify dependent databases, load balancers, and downstream services
**Rollback Plans Mandatory**: Require documented rollback procedures for all normal/emergency changes; test rollback capability in non-production before implementation
**Progressive Rollout for High-Risk Changes**: Implement canary deployments, blue-green deployments, or phased rollouts for high-risk changes to limit blast radius
**Blackout Period Enforcement**: Define and enforce blackout periods (end-of-quarter financial close, peak shopping seasons, tax deadlines); reject non-emergency changes during blackouts
**Post-Implementation Review (PIR)**: Conduct PIR for failed changes and high-impact changes; capture lessons learned and update standard change procedures
**DevOps Integration**: Integrate CI/CD pipeline deployments with change management; auto-create change records for automated deployments while maintaining audit trail
**Metrics Dashboard**: Track change success rate, emergency change percentage, CAB approval cycle time, change volume trends; target >95% success rate and <5% emergency changes
**Change Freeze Periods**: Establish change freeze periods around major events (Black Friday, tax season, annual conferences) to maximize stability
**Virtual CAB for Remote Teams**: Leverage video conferencing and ITSM collaboration features for distributed CAB members; record meetings for audit evidence
**Service Owner Accountability**: Assign service owners for critical applications/infrastructure; service owners must approve changes affecting their services
**Change Conflict Detection**: Implement automated detection of conflicting changes (multiple teams modifying same CI, overlapping maintenance windows)
**Expedited CAB for Time-Sensitive Changes**: Establish expedited CAB review process for business-critical changes that can't wait for weekly CAB but don't meet emergency criteria
**Continuous Improvement Culture**: Celebrate successful complex changes; conduct blameless post-mortems on failures; update procedures based on lessons learned

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

**ITIL & Service Management Standards**:
- ITIL 4 (2019): Change Enablement practice, Service Value System (SVS), Service Value Chain, Guiding Principles (focus on value, start where you are, progress iteratively, collaborate)
- ITIL v3 (2011): Change Management process, Change Advisory Board, Standard/Normal/Emergency change types
- ISO/IEC 20000-1:2018: IT Service Management - Part 1: Service management system requirements (Clause 8.5.2 Change Management)
- ISO/IEC 20000-2:2019: IT Service Management - Part 2: Guidance on the application of service management systems
- VeriSM: Value-driven, Evolving, Responsive, Integrated Service Management model

**Governance & Compliance Frameworks**:
- COBIT 2019 (Control Objectives for Information Technologies): BAI06 (Manage Changes), BAI10 (Manage Configuration), DSS05 (Manage Security Services)
- NIST SP 800-53 Rev 5: CM-3 (Configuration Change Control), CM-4 (Impact Analysis), CM-9 (Configuration Management Plan), SA-10 (Developer Configuration Management)
- NIST Cybersecurity Framework (CSF): PR.IP-3 (Configuration change control processes established), PR.IP-4 (Backups of information conducted), DE.CM-7 (Monitoring for unauthorized activity)
- CIS Controls v8: 4.1 (Establish and Maintain Secure Configuration Process), 12.1 (Ensure Network Infrastructure is Up-to-Date)

**Compliance Requirements**:
- SOC 2 Trust Services: CC8.1 (Change management process controls changes), additional criteria for change authorization, testing, and approval evidence
- ISO/IEC 27001:2022: A.8.9 (Configuration management), A.8.19 (Installation of software on operational systems), A.8.32 (Change management)
- PCI DSS v4.0: Requirement 6.5.1 (Changes to system components managed via change control procedures), Requirement 12.5.3 (Unauthorized changes detected)
- HIPAA Security Rule: 164.308(a)(8) (Evaluation - testing and revision procedures for security), 164.308(a)(5)(ii)(B) (Protection from malicious software)
- SOX (Sarbanes-Oxley): IT General Controls (ITGC) for change management in financial systems, segregation of duties for developers and production deployers
- FedRAMP: CM-3 (Configuration Change Control) and SA-10 (Developer Configuration Management) requirements

**DevOps & Continuous Delivery**:
- DORA State of DevOps Report: Deployment frequency, lead time for changes, mean time to recovery (MTTR), change failure rate as key metrics
- The Phoenix Project / DevOps Handbook: Three Ways principles (flow, feedback, continuous learning), breaking down IT/Dev silos
- Site Reliability Engineering (SRE) - Google: Error budgets, toil reduction, blameless post-mortems, progressive delivery practices
- Continuous Delivery: Automated deployment pipelines, deployment automation, feature flags, canary deployments, blue-green deployments

**Change Management Platforms**:
- ServiceNow Change Management: Change request workflows, CAB automation, approval policies, integration with CMDB and incident management
- Jira Service Management: Change workflows, approvals, calendar views, integration with Jira Software for developer changes
- BMC Remedy Change Management: Change lifecycle automation, risk assessment, conflict detection, compliance reporting
- Cherwell Service Management: Change request automation, approval routing, change calendar, CMDB integration
- Ivanti Service Manager: ITIL-based change workflows, CAB management, change impact analysis

**Additional Best Practice Frameworks**:
- CMMI (Capability Maturity Model Integration): Configuration management and change management process areas
- MOF (Microsoft Operations Framework): Change and Configuration Management Service Management Function
- PRINCE2 (Projects IN Controlled Environments): Change control in project management context
- Agile/Scrum: Sprint planning, backlog management, iterative development integrated with change control
- Lean IT: Value stream mapping, waste elimination (reducing change approval bureaucracy without sacrificing control)

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
