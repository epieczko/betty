# Name: uptime-methodology

## Executive Summary

The Uptime Methodology defines standardized approaches for calculating service availability, managing planned maintenance windows, implementing multi-region redundancy, and administering SLA credits for downtime violations. This artifact establishes measurement methodologies aligned with contractual SLAs, handles timezone considerations, excludes legitimate downtime, and ensures transparent reporting of service reliability metrics.

As a critical component of SLA management and customer communication, the Uptime Methodology provides consistent availability calculations (monthly, quarterly, annual), maintenance window scheduling practices, multi-AZ/multi-region deployment patterns, and SLA credit policies. It bridges SRE reliability practices with contractual obligations, ensuring internal SLOs drive external SLA commitments.

### Strategic Importance

- **SLA Compliance**: Ensures accurate availability calculations for contractual SLA commitments and service credit administration
- **Transparency**: Provides customers with clear uptime metrics, maintenance schedules, and downtime explanations
- **Multi-Region Reliability**: Implements active-active, active-passive, and multi-region architectures for high availability
- **Maintenance Planning**: Schedules maintenance windows during low-traffic periods with advance customer notification
- **Financial Impact**: Manages SLA credits, service level penalties, and revenue implications of downtime
- **Trust Building**: Demonstrates commitment to reliability through transparent status pages and incident communication

## Purpose & Scope

### Primary Purpose

This artifact standardizes uptime calculation methodologies, maintenance window management, multi-region deployment strategies, and SLA credit administration. It defines availability formulas (uptime minutes / total minutes), planned maintenance exclusions, multi-AZ/multi-region patterns, status page communication, and financial remediation for SLA violations.

### Scope

**In Scope**:
- Availability calculation: (total_time - downtime) / total_time * 100% for monthly/quarterly/annual periods
- Planned maintenance windows: scheduling, duration limits, advance notice (7-14 days), customer communication
- Multi-region architectures: active-active, active-passive, multi-AZ deployments (AWS, Azure, GCP)
- SLA tiers: 99.9% (three nines = 43m downtime/month), 99.95%, 99.99% (four nines = 4.3m/month)
- SLA credits: percentage refunds based on availability shortfall (10-25-50-100% credit tiers)
- Exclusions: planned maintenance, customer-caused outages, DDoS attacks, force majeure events
- Status pages: Statuspage.io, Atlassian Statuspage, custom status dashboards
- Uptime monitoring: synthetic monitoring, health checks, multi-region probes (Pingdom, UptimeRobot, Datadog Synthetics)
- Regional failover: DNS failover, load balancer failover, database replication and failover
- Incident classification: partial outage vs. full outage, region-specific vs. global incidents

**Out of Scope**:
- Internal SLO definitions and error budgets (covered in service-level-objectives artifact)
- Detailed incident response procedures (covered in incident management runbooks)
- Disaster recovery and business continuity planning (covered in DR/BCP artifacts)
- Infrastructure architecture and capacity planning (covered in architecture artifacts)
- Customer contract terms and legal SLA language (covered in legal/commercial agreements)

### Target Audience

**Primary Audience**:
- SRE Teams: Calculate uptime, track SLA compliance, coordinate maintenance windows, manage status pages
- Platform Engineers: Implement multi-region architectures, configure health checks, automate failover
- Customer Success: Communicate uptime metrics, process SLA credit requests, manage customer expectations
- Finance Teams: Administer SLA credits, track revenue impact of downtime, process refunds

**Secondary Audience**:
- Engineering Leadership: Review availability trends, approve architecture investments for higher uptime
- Legal/Compliance: Ensure uptime calculations match contractual SLA definitions
- DevOps Engineers: Schedule deployments during maintenance windows, minimize customer impact
- Product Management: Set uptime targets aligned with customer requirements and market standards

## Document Information

**Format**: Markdown

**File Pattern**: `*.uptime-methodology.md`

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

**Monthly Calculation**: Calculate uptime monthly (calendar month) for consistency with billing cycles and SLA reporting
**Maintenance Windows**: Schedule during low-traffic hours (2-6 AM local time); limit to 4 hours max; provide 7-14 days notice
**Exclude Planned**: Exclude planned maintenance from uptime calculations if advance notice given and during designated window
**Multi-Region Buffer**: Deploy to 3+ regions/AZs; design for single region failure without service impact
**Health Checks**: Implement deep health checks beyond simple HTTP 200 (database connectivity, dependency health)
**Synthetic Monitoring**: Use multi-region synthetic monitors (Pingdom, Datadog Synthetics) to detect outages before customers
**Status Page Transparency**: Publish real-time status page; update within 5 minutes of incident detection; provide incident timelines
**SLA Credit Automation**: Automate SLA credit calculation and customer notification; proactive outreach for violations
**Grace Period**: Implement 5-minute grace period before declaring incident (avoid false positives from brief hiccups)
**Partial Outage Credits**: Prorate credits for partial outages affecting subset of customers or degraded performance
**Timezone Consistency**: Use UTC for all uptime calculations; convert to customer timezone for reporting
**Downtime Attribution**: Clearly categorize downtime (unplanned outage, planned maintenance, third-party dependency)
**SLO-SLA Alignment**: Maintain buffer (SLO 99.9%, SLA 99.5%) to avoid SLA breaches despite internal SLO violations
**Incident Declaration**: Declare incidents for customer-facing impact; internal degradation tracked separately
**Post-Incident Review**: Calculate actual downtime from logs/metrics; reconcile with monitoring data; communicate to customers
**Credit Tiers**: Standard tiers (99.9-99%: 10% credit, 99-95%: 25% credit, <95%: 50-100% credit)
**Proactive Communication**: Update status page and notify customers proactively during incidents, not reactively

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

**SLA Standards**:
- ITIL v4 - Service level management and availability management practices
- ISO/IEC 20000 - Service availability and continuity requirements
- TM Forum SLA Management (GB917) - Service level agreement best practices

**Cloud Provider SLAs**:
- AWS SLA - EC2 (99.99% multi-AZ), RDS (99.95% multi-AZ), S3 (99.9%), Lambda (99.95%)
- Azure SLA - VMs (99.99% multi-zone), SQL Database (99.99%), Storage (99.9%)
- GCP SLA - Compute Engine (99.99% regional), Cloud SQL (99.95%), Cloud Storage (99.9%)

**Status Page Platforms**:
- Atlassian Statuspage - Industry-standard status page SaaS platform
- Status.io - Status page with incident management integration
- Cachet - Open-source status page system
- Instatus - Modern status page platform

**Uptime Monitoring**:
- Pingdom - Synthetic monitoring and uptime tracking (SolarWinds)
- UptimeRobot - Free/paid uptime monitoring with 5-minute checks
- Datadog Synthetics - Multi-location API and browser tests
- New Relic Synthetics - Scripted browser and API monitors
- Checkly - Programmable synthetic monitoring
- Site24x7 - Website monitoring and uptime tracking

**Multi-Region Architectures**:
- AWS Multi-Region - Route 53 health checks, CloudFront, global accelerator
- Azure Traffic Manager - DNS-based traffic routing for failover
- GCP Cloud Load Balancing - Global anycast load balancing
- Multi-AZ Deployments - AWS availability zones, Azure availability zones, GCP zones

**Failover Patterns**:
- Active-Active - Traffic distributed across multiple regions simultaneously
- Active-Passive - Standby region activated during primary region failure
- DNS Failover - Route 53, Azure Traffic Manager, GCP Cloud DNS health checks
- Database Replication - Read replicas, cross-region replication, automatic failover

**Availability Calculation**:
- Uptime Formula - (total_minutes - downtime_minutes) / total_minutes * 100%
- Downtime Allowances - 99.9% = 43.2min/month, 99.95% = 21.6min/month, 99.99% = 4.32min/month
- Monthly vs Annual - Calculate both; annual smooths out monthly variances

**SLA Credit Administration**:
- Automated Credit Calculation - Calculate based on actual uptime vs SLA target
- Tiered Credit Structure - Increasing credit percentages for worse availability
- Claim Process - Customer-initiated vs proactive credit issuance
- Credit Caps - Maximum credit (e.g., 100% of monthly fee, no consequential damages)

**Health Check Standards**:
- HTTP Health Checks - /health, /healthz, /ping endpoints returning 200 OK
- Deep Health Checks - Database connectivity, cache availability, dependency health
- Kubernetes Liveness/Readiness - Container orchestration health checks
- Load Balancer Health Checks - ALB, NLB, Azure Load Balancer, GCP Load Balancer health probes

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
