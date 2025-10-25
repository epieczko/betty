# Name: exception-log

## Executive Summary

The Exception Log captures deviations from planned baselines, approved variances, risk acceptances, and corrective actions taken when program constraints (scope, schedule, budget, quality) cannot be met as planned. Aligned with governance frameworks (SAFe Lean Portfolio Management, PMI standards, stage-gate processes) and change control practices, this log documents when and why the program diverged from original commitments and what approvals and mitigations were put in place.

Modern exception management leverages tracking tools (Jira, Azure DevOps, ServiceNow) and collaboration platforms (Confluence) to document variance requests, approval workflows, risk acceptance decisions, and corrective action plans. The log serves program managers, executive leadership, and portfolio management by providing transparency on program health, enabling trend analysis of deviations, supporting audit requirements, and informing future estimation and planning. It applies variance thresholds, escalation criteria, and approval authorities to ensure appropriate governance of exceptions.

### Strategic Importance

- **Governance Excellence**: Demonstrates rigorous program management and adherence to organizational standards
- **Risk Mitigation**: Early identification of patterns and trends enables proactive intervention
- **Audit Readiness**: Provides comprehensive trail for internal and external audits
- **Knowledge Capture**: Preserves institutional knowledge beyond individual personnel tenure
- **Continuous Improvement**: Enables data-driven process improvements through trend analysis

## Purpose & Scope

### Primary Purpose

The Exception Log documents deviations from approved baselines (scope, schedule, budget, quality), variance approvals, risk acceptances, and corrective actions when program constraints cannot be met. It answers: What deviated from plan? Why? Who approved the exception? What corrective actions were taken? What was the impact? The log ensures accountability, transparency, and appropriate governance oversight of program exceptions.

### Scope

**In Scope**:
- Scope baseline deviations (scope creep, descope decisions, requirements changes)
- Schedule baseline variances (delays, milestone slips, critical path impacts)
- Budget baseline exceptions (cost overruns, unforeseen expenses, budget reallocation)
- Quality standard variances (technical debt acceptance, quality gate exceptions)
- Risk acceptances (risks accepted outside normal risk tolerance)
- Variance request documentation (justification, impact analysis, alternatives)
- Approval workflows and authorities (DACI/RAPID, delegation of authority)
- Corrective action plans and mitigation strategies
- Exception status tracking (requested, approved, rejected, implemented, resolved)
- Variance thresholds and escalation criteria
- Impact analysis (cost, schedule, quality, scope, stakeholder)
- Root cause analysis for recurring exceptions
- Trend analysis and pattern identification

**Out of Scope**:
- Normal change requests within tolerance (covered in Change Log)
- Day-to-day issue tracking (covered in Issue Log)
- Risk identification and assessment (covered in Risk Register)
- Detailed corrective action execution (covered in Action Item logs, Project Plans)
- Technical defects and bugs (covered in Defect Tracking systems)

### Target Audience

**Primary Audience**:
- **Program Managers**: Documents exceptions, requests approvals, implements corrective actions
- **Executive Leadership**: Reviews and approves significant exceptions based on authority thresholds
- **Governance & PMO**: Monitors exception trends, identifies process improvements

**Secondary Audience**:
- **Portfolio Management**: Assesses program health and forecasting accuracy
- **Audit & Compliance**: Reviews exception handling and approval processes
- **Steering Committee**: Makes governance decisions on major exceptions

## Document Information

**Format**: Markdown

**File Pattern**: `*.exception-log.md`

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
**Threshold Definition**: Define clear variance thresholds requiring exception approval (e.g., >10% budget, >2 weeks schedule)
**DACI/RAPID Clarity**: Document approval authority using DACI or RAPID; respect delegation of authority limits
**Timely Logging**: Log exceptions immediately when variance identified; don't wait for formal approvals
**Impact Analysis**: Conduct thorough impact analysis (cost, schedule, scope, quality, risk) before approval
**Root Cause Analysis**: Apply Five Whys or Fishbone to understand root causes, not just symptoms
**Corrective Action Focus**: Every approved exception must have corrective action plan with owner and dates
**Trend Analysis**: Regularly analyze exception patterns; address systemic issues causing repeated exceptions
**EVM Integration**: Use Earned Value Management (EVM) metrics to identify variances early
**Risk Register Link**: Link exceptions to Risk Register; track risk acceptances and risk response effectiveness
**Approval Evidence**: Maintain documented approvals with approver name, date, and any conditions
**Escalation Speed**: Escalate exceptions quickly based on magnitude and impact; don't delay bad news
**Baseline Integrity**: Protect baseline integrity; only re-baseline with formal approval and documentation
**Jira Workflow**: Use Jira or similar tool to track exception workflow from request through resolution
**Lessons Learned**: Capture lessons from exceptions for future planning and estimation improvements
**No Finger-Pointing**: Focus on process improvement, not blame; create psychological safety for transparency
**Forecasting Updates**: Update forecasts (EAC, ETC) based on approved exceptions and trends
**Steering Committee**: Report significant exceptions to Steering Committee for oversight and guidance
**Audit Readiness**: Maintain complete audit trail for compliance, financial audits, and governance reviews
**Recovery Planning**: Develop get-well plans for programs with significant exception trends

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

**Variance & Exception Management**:
- Earned Value Management (EVM) - Variance analysis (CV, SV, CPI, SPI)
- Variance thresholds and tolerance limits
- Exception handling procedures
- Baseline change control
- Variance trend analysis
- Control limits and statistical process control

**Change Control Frameworks**:
- Integrated Change Control - PMI/PMBOK
- Change Control Board (CCB) processes
- Configuration Management
- Baseline management (scope, schedule, cost, quality)
- Change request workflows
- Impact assessment methodologies

**Governance & Approval Frameworks**:
- DACI (Driver, Approver, Contributor, Informed) - Exception approval
- RAPID (Recommend, Agree, Perform, Input, Decide) - Decision rights
- Delegation of Authority (DoA) frameworks
- Approval thresholds by exception type and magnitude
- Escalation paths and criteria
- Stage-gate exception review

**Risk Management Integration**:
- Risk acceptance decisions and criteria
- Risk tolerance and appetite frameworks
- Risk response strategies (accept, mitigate, transfer, avoid)
- Residual risk tracking
- Risk-based variance analysis
- Contingency and management reserve usage

**Corrective Action Planning**:
- Root cause analysis (Five Whys, Fishbone, Pareto)
- Corrective Action / Preventive Action (CAPA) systems
- Get-well plans and recovery strategies
- Re-baselining procedures
- Turnaround planning
- Remediation tracking

**Project Management Standards**:
- PMI PMBOK - Integrated Change Control
- PRINCE2 - Exception management and tolerance
- Agile governance - Iteration and PI exception handling (SAFe)
- Stage-Gate exception reviews
- Critical Chain buffer management

**Portfolio & Program Governance**:
- SAFe Lean Portfolio Management - Program health tracking
- Portfolio exception escalation
- Program health metrics and dashboards
- Portfolio Kanban exception handling
- Investment review and revalidation

**Variance Analysis Techniques**:
- Earned Value Analysis (EVA)
- Variance at Completion (VAC)
- To-Complete Performance Index (TCPI)
- Trend analysis and forecasting
- Monte Carlo simulation for variance impact
- Sensitivity analysis

**Tracking & Workflow Tools**:
- Jira - Exception tracking, workflow, and approvals
- Azure DevOps - Work item tracking for exceptions
- ServiceNow - IT exception and change management
- Confluence - Exception documentation and knowledge base
- Monday.com - Exception workflow and tracking
- Asana - Exception action item management

**Audit & Compliance**:
- Audit trail requirements
- SOC 2 change control compliance
- ISO 9001 nonconformance handling
- Regulatory exception reporting
- Financial controls and variance reporting
- Sarbanes-Oxley (SOX) compliance for budget exceptions

**Metrics & Reporting**:
- Exception frequency and trends
- Exception approval cycle time
- Exception resolution effectiveness
- Variance metrics (cost variance, schedule variance)
- Exception category analysis
- Repeat exception patterns
- Mean Time to Resolution (MTTR) for exceptions

**Communication & Stakeholder Management**:
- Exception reporting formats
- Stakeholder notification protocols
- Executive dashboards for exceptions
- Red/Yellow/Green (RAG) status reporting
- Exception communication templates

**Continuous Improvement**:
- Lessons learned from exceptions
- Process improvement based on exception trends
- Estimating and planning improvements
- Risk identification improvements
- Proactive variance prevention

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
