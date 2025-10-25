# Name: root-cause-analyses

## Executive Summary

Root Cause Analysis (RCA) is a systematic investigation methodology that identifies the underlying technical, process, and human factors contributing to production incidents. This analytical artifact moves beyond surface-level symptoms to uncover fundamental causes through structured techniques including 5 Whys, Fishbone (Ishikawa) diagrams, Fault Tree Analysis, and timeline reconstruction, enabling targeted remediation that prevents incident recurrence.

Following ITIL 4 Problem Management and Google SRE postmortem practices, RCA provides a blameless framework for investigating SEV0/P0 critical incidents and recurring SEV1/P1 issues. The analysis reconstructs incident timelines with precision timestamps, identifies contributing factors across people/process/technology dimensions, applies causal analysis methodologies, and generates actionable recommendations with SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) for preventing similar failures.

### Strategic Importance

- **Recurrence Prevention**: Reduces repeat incidents by 60-80% through systematic identification and remediation of root causes
- **Pattern Recognition**: Identifies systemic issues affecting multiple services or incident categories
- **Architectural Insights**: Reveals design weaknesses, technical debt, and reliability gaps requiring long-term investment
- **Blameless Culture**: Emphasizes system improvement over individual blame, fostering psychological safety
- **Knowledge Transfer**: Documents failure modes and remediation strategies for organizational learning
- **Metric-Driven**: Links RCA to MTTR reduction, incident frequency trends, and error budget consumption
- **Compliance**: Satisfies SOC 2, ISO 27001, and regulatory requirements for incident investigation and corrective action

## Purpose & Scope

### Primary Purpose

This artifact provides systematic analysis of incident root causes using proven methodologies (5 Whys, Fishbone, Fault Tree Analysis) to identify fundamental failures and generate actionable remediation strategies. It solves the problem of recurring incidents by moving beyond surface-level fixes to address underlying system weaknesses, process gaps, and architectural limitations that enable failures.

### Scope

**In Scope**:
- Timeline reconstruction with precise timestamps (detection, escalation, mitigation, resolution)
- 5 Whys analysis to drill down from symptoms to fundamental causes
- Fishbone (Ishikawa) diagram mapping contributing factors (People, Process, Technology, Environment)
- Fault Tree Analysis for complex, multi-factor failures
- Pareto analysis identifying the 20% of causes driving 80% of incidents
- Contributing factor identification across technical, process, and human dimensions
- FMEA (Failure Mode and Effects Analysis) for systematic failure scenarios
- Immediate, short-term, and long-term remediation recommendations
- SMART action items with owners, deadlines, and success metrics
- Related incident correlation and pattern analysis

**Out of Scope**:
- Incident response procedures (covered in playbooks artifact)
- Post-mortem meeting facilitation (covered in post-mortem-report artifact)
- Lessons learned repository management (covered in lessons-learned-document artifact)
- Individual performance reviews or blame attribution
- Legal liability determinations

### Target Audience

**Primary Audience**:
- SRE Teams conducting deep-dive technical analysis of production incidents
- Incident Commanders coordinating RCA investigations
- Engineering Leads identifying architectural improvements based on failure patterns
- Operations Teams implementing preventative measures

**Secondary Audience**:
- Platform Teams addressing systemic reliability issues
- Engineering Managers prioritizing technical debt and reliability investments
- Product Managers understanding customer impact and product reliability trends
- Executive Leadership reviewing high-impact incident causes and remediation strategies

## Document Information

**Format**: Markdown

**File Pattern**: `*.root-cause-analyses.md`

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

**Blameless Approach**: Focus on system failures, not individual blame; create psychological safety for honest analysis
**Ask Why 5 Times**: Drill down from symptom to root cause; don't stop at first answer (5 Whys methodology)
**Precise Timeline**: Reconstruct incident timeline with UTC timestamps accurate to seconds/minutes
**Multiple Causes**: Recognize most incidents have multiple contributing factors; use Fishbone to map all contributors
**Data-Driven**: Support analysis with logs, metrics, traces; avoid speculation without evidence
**Distinguish Root from Contributing**: Identify THE root cause while documenting all contributing factors
**SMART Action Items**: Every action must be Specific, Measurable, Assignable, Realistic, Time-bound
**Owner Assignment**: Assign single DRI (Directly Responsible Individual) to each remediation action
**Categorize Actions**: Separate immediate fixes, short-term improvements (30 days), long-term investments (90+ days)
**Validate Hypotheses**: Test causal theories with additional data; don't assume first hypothesis is correct
**Cross-Reference Incidents**: Search for similar past incidents to identify patterns and recurring root causes
**Involve SMEs**: Include database experts, network engineers, or security specialists as analysis requires
**Quantify Impact**: Document MTTR, customer impact, revenue loss, error budget burn for prioritization
**Preventability Analysis**: Explicitly state whether incident was preventable and what would have prevented it
**Document Near-Misses**: Analyze incidents that could have been worse to prevent future escalation
**Track Action Completion**: Follow up on remediation items; report completion metrics in subsequent reviews
**Knowledge Base**: Add failure modes and solutions to searchable knowledge repository for future reference

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

**RCA Methodologies**:
- 5 Whys (Toyota Production System, Lean methodology)
- Fishbone Diagram / Ishikawa Diagram (cause-and-effect analysis)
- Fault Tree Analysis (FTA) for complex system failures
- Pareto Analysis (80/20 rule for incident causes)
- FMEA (Failure Mode and Effects Analysis)
- Kepner-Tregoe Problem Analysis
- RCFA (Root Cause Failure Analysis)
- Causal Factor Charting

**Incident Management Frameworks**:
- ITIL 4 Problem Management (root cause identification and elimination)
- Google SRE Book (Postmortem Culture, Learning from Failure)
- NIST SP 800-61 Incident Handling Guide
- COBIT (Control Objectives for Information Technology)

**Timeline Reconstruction Tools**:
- Incident timeline visualization tools
- Log aggregation platforms (Splunk, ELK Stack, Datadog)
- Distributed tracing (Jaeger, Zipkin, AWS X-Ray)
- Metrics correlation (Grafana, Datadog, New Relic)
- Change tracking (deployments, config changes, infrastructure modifications)

**Contributing Factor Categories**:
- People: Training gaps, communication failures, assumptions
- Process: Inadequate procedures, missing validation, approval gaps
- Technology: Software bugs, infrastructure failures, design flaws
- Environment: Load conditions, external dependencies, timing issues
- Management: Resource constraints, priority conflicts, technical debt

**RCA Facilitation Techniques**:
- Blameless postmortem culture (Etsy Debriefing Facilitation Guide)
- Socratic questioning techniques
- Just Culture principles (balancing accountability and learning)
- Learning Review facilitation (LR methodology)
- Appreciative Inquiry for positive framing

**Action Item Management**:
- SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
- Action item tracking in Jira, Linear, Asana, GitHub Issues
- Priority frameworks (SEV0 → immediate, SEV1 → 30 days, SEV2 → 90 days)
- Ownership assignment (single DRI - Directly Responsible Individual)
- Progress tracking and follow-up cadence

**Pattern Analysis & Trending**:
- Incident categorization taxonomies
- Common vulnerability patterns (CWE, OWASP)
- Reliability anti-patterns (Google SRE)
- Failure mode libraries and knowledge bases
- Incident frequency trending over time

**Compliance & Audit**:
- SOC 2 Type II (corrective action requirements)
- ISO 27001 (nonconformity and corrective action)
- ISO 9001 (quality management, root cause analysis)
- FDA 21 CFR Part 11 (for healthcare/pharma)
- Sarbanes-Oxley (financial controls)

**Reference**: Consult SRE leadership and quality management teams for RCA methodology standards

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
