# Name: finops-dashboards

## Executive Summary

The FinOps Dashboards are comprehensive visualizations that provide real-time visibility into cloud spending, unit economics, cost per customer, COGS (Cost of Goods Sold), gross margin, and cloud resource utilization across AWS, Azure, and GCP environments. These mission-critical dashboards enable FinOps teams, engineering leaders, and CFOs to monitor cloud spend trends, identify cost anomalies, optimize resource allocation, and track cost efficiency metrics against business growth.

As essential Cloud Financial Management tools, FinOps dashboards integrate data from AWS Cost Explorer, Azure Cost Management, GCP Cost Management, Kubecost, CloudHealth, and Apptio Cloudability to provide unified views of cloud spend by service, team, environment, project, and business unit. They track key metrics including cost per transaction, cost per user, cost per GB stored, infrastructure costs as % of revenue, cloud efficiency ratios, Reserved Instance/Savings Plan coverage, and month-over-month/year-over-year cost trends enabling proactive cost optimization and budget management.

### Strategic Importance

- **Cost Visibility**: Provides real-time visibility into cloud spending by service, team, environment, and cost center to drive accountability
- **Unit Economics**: Tracks cost per customer, cost per transaction, cost per API call enabling optimization of unit cost structure
- **Gross Margin Tracking**: Monitors infrastructure COGS as % of revenue to protect and improve gross margins
- **Budget Management**: Enables proactive budget monitoring with alerts for overruns and anomaly detection
- **Optimization Opportunities**: Identifies rightsizing opportunities, idle resources, unattached volumes, and RI/Savings Plan gaps
- **Chargeback/Showback**: Supports cost allocation and chargeback to business units through detailed cost attribution
- **Predictive Forecasting**: Projects future costs based on historical trends, growth rates, and seasonal patterns

## Purpose & Scope

### Primary Purpose

These dashboards provide comprehensive cloud financial visibility through:
- **Unit Economics Dashboard**: Cost per customer, cost per transaction, cost per user, cost per API call, infrastructure cost per dollar of revenue
- **Cost by Service/Team/Environment**: Breakdown of cloud spend by AWS/Azure/GCP service, engineering team, environment (prod/staging/dev)
- **COGS Dashboard**: Infrastructure costs as % of revenue, gross margin trends, direct cloud costs allocated to COGS
- **Gross Margin Analysis**: Revenue vs infrastructure costs, margin trends, margin by customer segment or product line
- **Budget Tracking**: Actual vs budget spend by month/quarter, forecast vs actuals, variance analysis, burn rate
- **Cost Optimization**: RI/Savings Plan coverage, rightsizing recommendations, idle resource costs, unattached volume costs
- **Anomaly Detection**: Unusual spend spikes, cost outliers, unexpected service usage increases
- **Trend Analysis**: Month-over-month growth, year-over-year trends, seasonal patterns, cost efficiency over time

### Scope

**In Scope**:
- Cloud spend visualization (AWS, Azure, GCP)
- Cost allocation by team, service, environment, project, cost center
- Unit economics metrics (cost per customer, per transaction, per user, per API call)
- COGS tracking (infrastructure costs, third-party services, direct cloud costs)
- Gross margin analysis (revenue vs infrastructure costs)
- Budget vs actual tracking and variance analysis
- RI/Savings Plan utilization and coverage
- Cost optimization opportunities (rightsizing, idle resources, waste)
- Forecasting and predictive cost modeling
- Anomaly detection and alerts
- Multi-cloud consolidated view
- Kubernetes cost visibility (via Kubecost/OpenCost)

**Out of Scope**:
- Detailed TCO modeling (covered in ROI-TCO Calculators)
- Chargeback/showback report generation (covered in Showback & Chargeback Reports)
- Application performance monitoring (APM)
- Infrastructure monitoring and alerting (covered by observability tools)
- Revenue analytics (covered by revenue dashboards)

### Target Audience

**Primary Audience**:
- FinOps Teams: Daily monitoring and cost optimization
- CFO/Finance Leadership: COGS, gross margin, and budget oversight
- VP Engineering/CTO: Engineering cost efficiency and resource allocation

**Secondary Audience**:
- Engineering Teams: Team-specific cost visibility and accountability
- Product Management: Product-level unit economics
- FP&A: Budget planning and forecasting
- Business Unit Leaders: Cost allocation and showback visibility

## Document Information

**Format**: Markdown

**File Pattern**: `*.finops-dashboards.md`

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

**FinOps Dashboard Best Practices**:
**Tagging Strategy**: Enforce comprehensive tagging (cost center, team, environment, project, application); target >95% tag compliance
**Automated Data Pipelines**: Automate data ingestion from AWS CUR, Azure, GCP; refresh dashboards daily (or hourly for real-time)
**Multi-Cloud Normalization**: Normalize cost data across AWS/Azure/GCP for consistent cross-cloud comparison
**Unit Economics Focus**: Prioritize cost per customer, cost per transaction metrics; align infrastructure efficiency with business growth
**Anomaly Alerts**: Configure automated alerts for unusual spend spikes (>20% day-over-day or week-over-week)
**Budget Guardrails**: Set budget alerts at 50%, 75%, 90%, 100% thresholds with escalating notifications
**RI/SP Tracking**: Monitor RI and Savings Plan coverage, utilization, and expiration; target >70% coverage for steady-state workloads
**Rightsizing Recommendations**: Surface rightsizing opportunities weekly; track implementation and realized savings
**Idle Resource Detection**: Identify idle EC2 instances, unattached EBS volumes, orphaned snapshots; automate cleanup where safe
**Environment Segregation**: Separate prod, staging, dev costs; challenge non-prod spending >20% of total
**Team Accountability**: Provide team-level dashboards; make engineering teams responsible for their cloud spend
**Executive Dashboards**: Create CFO/CTO dashboards showing COGS%, gross margin, infrastructure cost as % of revenue
**Historical Trending**: Show 12-month trailing trends to identify seasonal patterns and growth trajectory
**Forecast Accuracy**: Compare forecast vs actuals monthly; refine forecasting models to improve accuracy
**Cost Attribution**: Allocate 100% of costs to business units/teams; break down shared costs (network, security) proportionally
**Optimization Tracking**: Track cost optimization initiatives (RI purchases, rightsizing) and actual savings realized
**Reserved Capacity Planning**: Model RI/SP purchases based on 3-6 month stable usage patterns; avoid overcommitment
**Kubernetes Cost Visibility**: Use Kubecost/OpenCost for pod-level, namespace-level, and deployment-level cost attribution
**Drill-Down Capability**: Enable drill-down from high-level metrics to resource-level detail for root cause analysis

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

**FinOps Framework**:
- FinOps Foundation Principles (Inform, Optimize, Operate)
- FinOps Certified Practitioner Standards
- Cloud Financial Management Maturity Model
- FinOps Domains (Understand Cloud Usage, Performance Tracking, Real-Time Decision Making, Cloud Rate Optimization, Cloud Usage Optimization, Organizational Alignment)
- FOCUS (FinOps Open Cost and Usage Specification)

**Cloud-Native Cost Tools**:
- AWS Cost Explorer
- AWS Cost and Usage Reports (CUR)
- AWS Cost Anomaly Detection
- Azure Cost Management + Billing
- Azure Consumption API
- Azure Cost Analysis
- Google Cloud Cost Management
- GCP Billing Export to BigQuery
- GCP Recommender (cost optimization)

**FinOps Platforms**:
- CloudHealth (VMware)
- Apptio Cloudability
- Flexera One
- CloudCheckr
- Spot.io
- ProsperOps
- Vantage
- Zesty

**Container & Kubernetes Cost**:
- Kubecost (Kubernetes cost visibility)
- OpenCost (CNCF open source)
- AWS Container Insights
- Azure Monitor for Containers
- GCP GKE Cost Allocation

**Visualization & BI Tools**:
- Tableau (cloud cost dashboards)
- Power BI (Azure integration)
- Looker (GCP integration)
- Grafana (with FinOps plugins)
- Datadog (infrastructure cost visibility)
- QuickSight (AWS)

**Unit Economics Metrics**:
- Cost per Customer (total infrastructure cost / active customers)
- Cost per Transaction (cloud cost / transaction volume)
- Cost per API Call
- Cost per GB Stored
- Cost per Compute Hour
- Infrastructure Cost as % of Revenue
- COGS as % of Revenue
- Gross Margin %

**Cloud Cost Metrics**:
- Total Cloud Spend (TCS)
- Month-over-Month (MoM) Growth %
- Year-over-Year (YoY) Growth %
- Cost per Service (EC2, RDS, S3, Lambda, etc.)
- Cost by Environment (prod, staging, dev, test)
- Cost by Team/Cost Center
- Cost by Tag (project, owner, application)

**Optimization Metrics**:
- Reserved Instance (RI) Coverage %
- Savings Plan Coverage %
- RI/SP Utilization Rate
- On-Demand vs RI/SP Mix
- Rightsizing Opportunities ($)
- Idle Resource Cost
- Unattached EBS Volume Cost
- Orphaned Snapshots Cost
- Cost Savings Realized

**Budget & Forecasting**:
- Budget vs Actual Variance
- Forecast Accuracy
- Burn Rate ($/day)
- Run Rate (current spend * 12)
- Trending Forecast (based on historical)
- Commitment-Based Forecast

**Tags & Attribution**:
- Cost Allocation Tags
- Tag Compliance %
- Untagged Resource Cost
- Business Unit Attribution
- Project/Application Attribution
- Environment Attribution

**Data Sources**:
- AWS Cost and Usage Reports (CUR) - S3/Athena/QuickSight
- Azure Consumption API / Billing Export
- GCP Billing Export to BigQuery
- CloudWatch Metrics
- Third-Party SaaS Costs
- Revenue Data (for unit economics)

**Reference**: Consult FinOps team, Cloud Center of Excellence, and Finance for detailed guidance on dashboard design, metric definitions, cost allocation methodologies, and tagging standards

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
