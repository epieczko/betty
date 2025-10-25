# Name: budget-forecast

## Executive Summary

The Budget Forecast is a comprehensive financial planning document that projects multi-year operating and capital expenditures (OpEx/CapEx), incorporating activity-based costing, zero-based budgeting principles, and driver-based forecasting models. This artifact leverages financial planning tools including cloud cost management platforms (AWS Cost Explorer, Azure Cost Management, Google Cloud Billing), ERP budgeting modules (SAP, Oracle Financials, Workday), and FP&A (Financial Planning & Analysis) software to provide rolling forecasts with variance analysis and scenario planning capabilities.

As a foundational component of financial governance and portfolio planning, this artifact supports CFOs, Finance Teams, Program Management Offices, and Business Unit Leaders in resource allocation, cost optimization, and financial performance management. The forecast integrates T-shirt sizing for project estimates, consumption-based pricing models for cloud services, full-time equivalent (FTE) planning, vendor contract commitments, and contingency reserves. It enables proactive financial management through budget-vs-actual tracking, burn rate analysis, and early warning indicators for budget overruns.

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

This artifact serves as the financial blueprint for planned expenditures across fiscal periods, enabling budget allocation, cost control, variance tracking, and financial forecasting. It separates CapEx (capital expenditures for long-term assets) from OpEx (operational expenses for ongoing operations), supports zero-based budgeting reviews, and provides rolling 12-18 month forecasts with monthly/quarterly granularity.

### Scope

**In Scope**:
- CapEx budget: Infrastructure, software licenses, hardware, facility investments
- OpEx budget: Personnel costs (FTE, contractors), SaaS subscriptions, cloud consumption
- Multi-year budget projections (typically 3-5 year planning horizon)
- Cloud cost forecasting using AWS Cost Explorer, Azure Cost Management, GCP Billing
- T-shirt sizing estimates (Small/Medium/Large) for project budgeting
- Headcount planning: FTEs, contractors, offshore resources, blended rates
- Vendor contracts and committed spend (reserved instances, enterprise agreements)
- Contingency reserves and management reserve (typically 10-20% of total budget)
- Budget-vs-actual variance analysis and explanations
- Cost allocation by department, project, product, or cost center
- Depreciation and amortization schedules
- Currency exchange rate assumptions for global operations
- Inflation assumptions and cost escalation factors

**Out of Scope**:
- Detailed project schedules and resource assignments (covered in Project Plan)
- Vendor pricing negotiations and procurement strategy
- Revenue forecasting and P&L projections (covered in Financial Model)
- Tax planning and accounting policy decisions

### Target Audience

**Primary Audience**:
- CFO and Finance Teams: Budget approval, financial planning, variance management
- Finance Business Partners: Cost center budget management and forecasting
- Program Management Office (PMO): Portfolio budgeting and resource allocation
- Business Unit Leaders: Department budget planning and cost control

**Secondary Audience**:
- Executive Leadership: Strategic investment decisions and cost optimization
- Procurement: Vendor spend forecasting and contract planning
- IT Operations: Cloud cost optimization and infrastructure planning
- Finance Planning & Analysis (FP&A): Rolling forecasts and scenario modeling

## Document Information

**Format**: Markdown

**File Pattern**: `*.budget-forecast.md`

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
**Executive Sponsorship**: Ensure visible executive sponsorship and regular executive review
**Governance Alignment**: Align with organizational governance framework and decision-making bodies
**Metric-Driven**: Include measurable metrics and KPIs to track progress and outcomes
**Dependency Management**: Explicitly identify and track dependencies on other initiatives or resources
**Risk Integration**: Integrate with risk management processes; escalate risks appropriately
**Change Control**: Submit significant changes through formal change control process
**Audit Trail**: Maintain comprehensive audit trail for governance and compliance purposes
**CapEx/OpEx Clarity**: Clearly separate CapEx and OpEx per accounting policies and capitalization rules
**Rolling Forecasts**: Implement rolling 12-18 month forecasts, updated monthly or quarterly
**Variance Tracking**: Establish variance thresholds (e.g., 5-10%) requiring explanation and action
**Cloud Cost Tagging**: Enforce consistent tagging strategies for cloud resource cost allocation
**Reserved Capacity**: Model reserved instances, savings plans, and committed use discounts
**Contingency Planning**: Include management reserve (5-10%) and contingency reserve (10-20%)
**Zero-Based Review**: Conduct periodic zero-based budgeting reviews to eliminate waste
**Driver-Based Models**: Link budgets to business drivers (users, transactions, revenue growth)
**Scenario Planning**: Develop 3-5 scenarios (optimistic, pessimistic, most likely) with triggers
**Monthly Tracking**: Monitor budget-vs-actual monthly with formal variance reviews
**T-Shirt Sizing**: Use standardized T-shirt sizes (S/M/L/XL) for early-stage project estimates

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

**Budgeting Methodologies**:
- Zero-Based Budgeting (ZBB) - justify all expenses from zero baseline
- Activity-Based Budgeting (ABB) - cost allocation by activities
- Driver-Based Budgeting - forecasting based on business drivers (users, transactions, revenue)
- Incremental Budgeting - prior period baseline with adjustments
- Rolling Forecasts - continuous 12-18 month forward-looking projections
- Beyond Budgeting principles - adaptive, decentralized planning
- Flexible budgeting for variable cost management

**Financial Planning & Analysis (FP&A)**:
- Variance analysis (budget vs. actual, forecast vs. actual)
- Scenario planning (best case, worst case, most likely)
- Sensitivity analysis for key assumptions
- What-if modeling and simulation
- Waterfall charts for variance visualization
- Burn rate and runway calculations
- Budget reforecasting and course corrections

**Cost Accounting & Allocation**:
- CapEx vs OpEx classification standards
- Cost center and profit center accounting
- Allocation methodologies (direct, indirect, overhead)
- Full absorption costing vs. variable costing
- Activity-Based Costing (ABC)
- Chargeback and showback models for IT costs
- Transfer pricing for shared services

**Cloud Cost Management**:
- AWS Cost Explorer and AWS Budgets
- Azure Cost Management + Billing
- Google Cloud Billing and Cost Management
- FinOps Framework (Cloud Financial Management)
- Reserved Instances (RI) and Savings Plans optimization
- Spot instances and committed use discounts
- Rightsizing and waste elimination (idle resources, overprovisioning)
- Tagging strategies for cost allocation
- Cloud cost optimization tools (CloudHealth, Apptio Cloudability, Flexera)

**Technology & Infrastructure Budgeting**:
- Total Cost of Ownership (TCO) modeling
- Cloud migration cost estimation (6R framework: Rehost, Replatform, Refactor, etc.)
- SaaS subscription management and license optimization
- Infrastructure as Code (IaC) cost estimation
- Container and Kubernetes cost allocation
- Network egress and data transfer cost forecasting

**Headcount & Labor Planning**:
- Full-Time Equivalent (FTE) planning and forecasting
- Blended rates (onshore, offshore, nearshore)
- Contractor vs. employee cost comparisons
- Salary increases and merit budgets
- Benefits and burden rates (typically 25-40% of base salary)
- Recruitment and onboarding costs
- Attrition assumptions and backfill planning

**Project & Portfolio Budgeting**:
- T-shirt sizing (S/M/L/XL) for ROM estimates
- Project cost estimation (PERT, analogous, parametric, bottom-up)
- Agile budgeting and funding incremental delivery
- Portfolio optimization and prioritization
- Management reserve (typically 5-10% of project budget)
- Contingency reserve for known risks (typically 10-20%)

**Financial Standards & Compliance**:
- Generally Accepted Accounting Principles (GAAP)
- International Financial Reporting Standards (IFRS)
- CapEx capitalization rules and depreciation schedules
- Software capitalization (FASB ASC 350-40)
- Budget governance and approval workflows
- SOX compliance for financial controls

**FP&A Tools & Platforms**:
- Anaplan, Adaptive Insights (Workday), Planful
- Oracle Hyperion, IBM Planning Analytics (TM1)
- SAP BPC (Business Planning and Consolidation)
- Microsoft Excel with Power BI for visualization
- Tableau, Qlik for budget dashboards

**Performance Management**:
- KPIs and financial metrics tracking
- Balanced Scorecard methodology
- Management by Objectives (MBO)
- OKRs (Objectives and Key Results) integration

**Reference**: Consult organizational finance, FP&A, and cloud FinOps teams for detailed guidance on budgeting methodologies, cost allocation rules, and financial planning tools

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
