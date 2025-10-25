# Name: service-level-objectives

## Executive Summary

The Service Level Objectives (SLOs) artifact defines measurable reliability targets for services using Service Level Indicators (SLIs) including availability (99.9%, 99.95%, 99.99%), latency percentiles (P95, P99), error rates, and throughput. This artifact implements Google SRE methodology for error budgets, burn rate alerts, and data-driven reliability decisions that balance feature velocity with system stability.

As the foundation of Site Reliability Engineering practices, SLOs provide objective criteria for making trade-offs between releasing new features and improving reliability. They enable error budget policies (remaining downtime allowance), multi-window multi-burn-rate alerting, and inform decisions about deployment freezes, incident severity, and engineering priorities based on actual user impact rather than subjective opinions.

### Strategic Importance

- **Reliability Targets**: Establishes concrete availability and performance goals (99.9% uptime, P99 latency <500ms) aligned with business requirements
- **Error Budget Framework**: Implements Google SRE error budget methodology enabling data-driven reliability vs. velocity trade-offs
- **Burn Rate Alerting**: Detects SLO violations early through multi-window (1h, 6h, 3d, 30d) burn rate alerts before exhausting error budget
- **Incident Prioritization**: Objectively determines incident severity based on error budget impact and SLO violation magnitude
- **Release Decision Making**: Provides quantitative criteria for deployment freezes, rollbacks, and feature launch approvals
- **Team Accountability**: Creates shared ownership between SRE and development teams for reliability outcomes through error budget policies

## Purpose & Scope

### Primary Purpose

This artifact defines Service Level Objectives (SLOs) and Service Level Indicators (SLIs) for all critical services, establishing measurable reliability targets, error budget calculations, burn rate alert thresholds, and error budget policies. It documents SLI selection criteria, SLO target percentages (99%, 99.9%, 99.95%, 99.99%), measurement windows (28d, 30d, 90d), and exclusions (planned maintenance, dependency failures).

### Scope

**In Scope**:
- SLI selection: availability, latency (P50/P95/P99), error rate, throughput, data freshness
- SLO targets: 90%, 95%, 99%, 99.9% (three nines), 99.95%, 99.99% (four nines)
- Error budget calculations: allowed downtime (43m/month for 99.9%, 4.3m/month for 99.99%)
- Burn rate alerting: multi-window multi-burn-rate alerts (1h/5m, 6h/30m, 3d/6h windows)
- Error budget policies: deployment freezes, postmortem requirements, engineering allocation
- SLI measurement: request-based (success rate) vs. time-based (uptime percentage)
- Service dependencies: user-facing vs. backend services, dependency SLO inheritance
- SLA alignment: SLOs stricter than SLAs (SLO 99.9%, SLA 99.5%) with buffer
- Exclusions: planned maintenance windows, upstream dependency failures, load shedding
- Tooling: Datadog SLO tracking, Grafana SLO plugins, custom SLO dashboards, Sloth/OpenSLO

**Out of Scope**:
- Contractual SLAs and customer credits (covered in legal/commercial agreements)
- Detailed incident response procedures (covered in incident management runbooks)
- Infrastructure capacity planning (covered in capacity management artifact)
- Cost optimization and FinOps (covered in cost management artifacts)
- Specific metric instrumentation details (covered in metric-catalog artifact)
- Dashboard implementations (covered in monitoring-dashboards artifact)

### Target Audience

**Primary Audience**:
- SRE Teams: Define SLOs/SLIs, implement error budgets, configure burn rate alerts, enforce error budget policies
- Engineering Leadership: Set reliability priorities, approve SLO targets, make deployment freeze decisions
- Platform Engineers: Measure SLIs, implement SLO tracking dashboards, integrate with observability platforms
- Product Managers: Understand reliability commitments, prioritize reliability work vs. features

**Secondary Audience**:
- Application Developers: Optimize code for SLO compliance, understand error budget impact of changes
- DevOps Engineers: Monitor SLO burn rate during deployments, implement automated rollbacks
- Customer Success: Communicate reliability metrics to customers, manage expectations
- Legal/Compliance: Ensure SLOs meet contractual SLA requirements with appropriate buffer

## Document Information

**Format**: Markdown

**File Pattern**: `*.service-level-objectives.md`

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

**User-Centric SLIs**: Define SLIs based on actual user experience (request success, page load latency) not system metrics
**Request-Based SLI**: Prefer request-based SLIs (successful requests / total requests) over time-based for accuracy
**Achievable Targets**: Start with 99% or 99.9%; avoid 100% SLOs (no error budget); four nines (99.99%) rarely justified
**Error Budget Buffer**: Set SLOs stricter than SLAs (SLO 99.9%, SLA 99.5%) to avoid SLA breaches
**Multi-Window Alerts**: Implement burn rate alerts with multiple time windows (1h fast, 6h medium, 3d slow burn)
**Exclude Maintenance**: Exclude planned maintenance windows from SLO calculations with advance notification
**4xx vs 5xx**: Only count 5xx errors against SLOs; 4xx are client errors and don't indicate system failures
**Latency Percentiles**: Use P95 or P99 latency, never average (mean); P99 <500ms is common target
**28-Day Window**: Use 28-day or 30-day rolling windows for error budget calculations (aligned with month)
**Error Budget Policy**: Define consequences when error budget exhausted (deployment freeze, reduced velocity, focus on reliability)
**SLO Review Cadence**: Review SLOs quarterly; adjust based on user feedback, business needs, actual performance
**Dependency Tracking**: Account for dependency failures; don't penalize service for upstream outages
**Data Completeness**: Require >95% data completeness for SLO measurement validity
**Gradual Rollout**: Start with lenient SLOs (95%) and tighten over time based on actual performance
**Document Exclusions**: Clearly document what's excluded (DDoS attacks, force majeure, client errors)
**Automate Reporting**: Generate SLO reports automatically; dashboard showing error budget remaining and burn rate
**Postmortem Triggers**: Require postmortems when error budget consumed >10% in single incident

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

**SRE Principles**:
- Google SRE Book - Chapter 4 (Service Level Objectives), foundational SLO/SLI/SLA definitions
- Site Reliability Workbook - Implementing SLOs (Chapter 2), practical guidance and examples
- Building Secure and Reliable Systems - Google's reliability engineering practices
- The Art of SLOs - Practical guide to implementing SLOs (Alex Hidalgo)

**Error Budget Framework**:
- Error Budget Policy - Google SRE error budget methodology
- Burn Rate Alerts - Multi-window multi-burn-rate alerting strategy
- Error Budget Calculation - Allowed downtime based on SLO targets
- SLO vs SLA Alignment - Maintaining buffer between internal SLOs and external SLAs

**SLO Measurement**:
- Request-Based SLIs - Success rate = good requests / total requests
- Time-Based SLIs - Uptime percentage over measurement window
- Latency SLIs - P50, P95, P99 percentile latency targets
- Availability SLIs - Percentage of successful requests (excluding 4xx)

**SLO Tooling**:
- Datadog SLO Tracking - SaaS SLO monitoring with error budget dashboards
- Grafana SLO Plugin - Open-source SLO tracking and visualization
- New Relic Service Levels - APM-integrated SLO management
- Sloth - OpenSLO-based SLO generator for Prometheus
- OpenSLO - Open standard for defining SLOs in YAML
- Nobl9 - SLO platform for multi-cloud environments
- Blameless SRE Platform - SLO tracking with incident integration

**Burn Rate Alerting**:
- Multi-Window Alerts - Fast (1h), medium (6h), slow (3d) burn rate detection
- Alert Severity - Page for fast burn (exhausts budget in hours), ticket for slow burn
- Alert Thresholds - 14.4x burn rate (1h), 6x (6h), 1x (3d) for 99.9% SLO

**SLI Types**:
- Availability - Request success rate, uptime percentage
- Latency - Response time percentiles (P50, P90, P95, P99)
- Throughput - Requests per second, messages processed
- Quality - Data freshness, correctness, completeness
- Durability - Data loss prevention (for storage systems)

**SLO Calculation Tools**:
- SLO Calculator - Error budget and allowed downtime calculators
- Burn Rate Calculator - Determine alert thresholds for burn rates
- Availability Calculator - Convert SLO percentage to allowed downtime

**Industry Standards**:
- ITIL v4 - Service level management best practices
- ISO/IEC 20000 - Service management system requirements
- COBIT - IT governance framework with service delivery focus

**SLA Standards**:
- AWS SLA - 99.99% for multi-AZ services, credits for violations
- Azure SLA - 99.95% for multi-region, 99.9% single region
- GCP SLA - 99.95% for regional services, 99.99% multi-region
- Industry Standards - Three nines (99.9%) common for SaaS, four nines (99.99%) for critical systems

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
