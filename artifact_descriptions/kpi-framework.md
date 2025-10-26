# Name: kpi-framework

## Executive Summary

The KPI Framework defines the key performance indicators, metrics hierarchy, and measurement systems that track product health, business performance, and progress toward strategic objectives. This artifact establishes the North Star Metric, supporting metrics, AARRR pirate metrics (Acquisition, Activation, Retention, Revenue, Referral), and leading/lagging indicators that drive data-informed decision-making across the product organization.

Built on proven analytics frameworks from companies like Amplitude, Mixpanel, and Product-Led Growth practitioners, this framework creates a metrics tree that cascades from the North Star Metric to input metrics, enabling teams to identify levers for growth and product improvement. Product Managers use this framework with tools like Amplitude, Mixpanel, Heap, Pendo, Looker, or Tableau to build dashboards, track performance, run experiments, and report to stakeholders. The framework distinguishes between vanity metrics and actionable metrics, emphasizing leading indicators that teams can influence.

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

This artifact serves as the comprehensive measurement framework for product performance, business health, and customer behavior. It defines what metrics to track, how to measure them, how they relate to each other (metrics tree), and how to use them for decision-making, experimentation, and reporting.

### Scope

**In Scope**:
- North Star Metric definition and rationale (the single metric that best captures core value delivered)
- Metrics hierarchy and tree (North Star > primary drivers > input metrics)
- AARRR pirate metrics framework (Acquisition, Activation, Retention, Revenue, Referral)
- Leading indicators (predictive) vs. lagging indicators (historical)
- Product metrics (engagement, adoption, feature usage, stickiness)
- Business metrics (ARR, MRR, CAC, LTV, churn rate, NRR, GRR)
- Customer health metrics (NPS, CSAT, CES, product-market fit score)
- Growth metrics (user growth, activation rate, viral coefficient, time-to-value)
- Metric definitions, calculation methods, and data sources
- Dashboard specifications and reporting cadence
- Metric ownership and accountability (DRI for each metric)
- Experimentation metrics and statistical significance criteria

**Out of Scope**:
- Specific OKR targets and quarterly goals (covered in OKR Definitions)
- Detailed analytics implementation and instrumentation (covered in technical documentation)
- Product roadmap and feature prioritization (covered in Portfolio Roadmap)
- Data warehouse architecture and ETL pipelines (covered in data engineering docs)
- Individual user data and privacy considerations (covered in privacy/security policies)
- Competitive benchmarking details (covered in Market Analysis)

### Target Audience

**Primary Audience**:
- Product Managers who track metrics and make data-driven decisions
- Product Leaders (VP Product, CPO) who monitor portfolio health and report to executives
- Data Analysts and Product Analysts who build dashboards and run analyses

**Secondary Audience**:
- Executive Leadership (CEO, CFO, Board) who review business performance
- Engineering teams who instrument analytics and build data pipelines
- Growth teams who optimize acquisition and activation funnels
- Customer Success teams who monitor customer health and churn risk
- Marketing teams who track campaign performance and conversion rates

## Document Information

**Format**: Markdown

**File Pattern**: `*.kpi-framework.md`

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
**North Star Focus**: Define clear North Star Metric that captures core value delivered to customers
**Metrics Tree**: Build hierarchical metrics tree showing how input metrics drive North Star Metric
**Actionable Metrics**: Focus on metrics teams can influence, not vanity metrics
**Leading Indicators**: Prioritize leading indicators (predictive) over lagging indicators (historical)
**Cohort Analysis**: Use cohort-based analysis to understand retention, activation, and behavior trends
**Segmentation**: Segment metrics by customer type, use case, acquisition channel, or persona
**Benchmarking**: Establish internal baselines and external benchmarks where possible
**Dashboard Design**: Create role-specific dashboards (exec, product, growth, CS) with appropriate granularity
**Data Quality**: Ensure metrics have clear definitions, consistent calculation, and reliable instrumentation
**Experimentation Rigor**: Apply proper statistical methods to A/B tests; avoid p-hacking
**AARRR Framework**: Apply AARRR funnel to understand user journey and identify conversion levers
**Business + Product**: Balance product engagement metrics with business outcome metrics
**Real-Time Monitoring**: Set up alerts for critical metric degradations or anomalies
**Regular Reviews**: Review metrics weekly (tactical) and monthly/quarterly (strategic)

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

**Product Metrics Frameworks**:
- North Star Framework (Amplitude, Sean Ellis) - single metric that matters most
- AARRR Pirate Metrics (Dave McClure) - Acquisition, Activation, Retention, Revenue, Referral
- HEART framework (Google) - Happiness, Engagement, Adoption, Retention, Task Success
- Product Metrics Tree (hierarchical metrics decomposition)
- Input Metrics vs. Output Metrics
- Leading Indicators vs. Lagging Indicators
- Actionable Metrics vs. Vanity Metrics (Lean Analytics)

**Growth & Engagement Metrics**:
- DAU/MAU ratio (Daily/Monthly Active Users) - stickiness metric
- L7/L28 engagement (7-day/28-day active)
- Activation rate and time-to-value (TTV)
- Retention curves (Day 1, Day 7, Day 30 retention)
- Cohort analysis and retention cohorts
- Power User Curve (frequency distribution)
- Feature adoption and usage depth metrics

**Business & SaaS Metrics**:
- ARR (Annual Recurring Revenue) and MRR (Monthly Recurring Revenue)
- CAC (Customer Acquisition Cost) and LTV (Lifetime Value)
- LTV:CAC ratio (healthy ratio is 3:1 or higher)
- Churn rate (customer churn vs. revenue churn)
- NRR (Net Revenue Retention) and GRR (Gross Revenue Retention)
- Rule of 40 (growth rate + profit margin ≥ 40%)
- Magic Number (sales efficiency metric)
- Quick Ratio (new + expansion MRR / churned + contraction MRR)

**Customer Experience Metrics**:
- NPS (Net Promoter Score) - customer loyalty and satisfaction
- CSAT (Customer Satisfaction Score) - transactional satisfaction
- CES (Customer Effort Score) - ease of use
- Product-Market Fit Score (Sean Ellis PMF survey: "How disappointed would you be...")
- Customer Health Score (composite metric)
- Support ticket volume and resolution time

**Product-Market Fit & Validation**:
- Sean Ellis PMF Score (40%+ "very disappointed" threshold)
- Retention curve shape (flattening = PMF signal)
- Organic growth rate and viral coefficient
- Word-of-mouth and referral rates
- Customer concentration (% revenue from top customers)

**Analytics & Experimentation**:
- A/B testing and experimentation frameworks
- Statistical significance and p-values
- Minimum Detectable Effect (MDE)
- Sample size calculations
- Bayesian vs. Frequentist approaches
- Multiple testing corrections (Bonferroni)
- Guardrail metrics and counterfactual metrics

**Product Analytics Tools**:
- Product Analytics: Amplitude, Mixpanel, Heap, Pendo, FullStory, Hotjar
- Business Intelligence: Looker, Tableau, Mode, Metabase, Power BI
- Data Warehouses: Snowflake, BigQuery, Redshift, Databricks
- Event Tracking: Segment, RudderStack, mParticle
- Session Replay: FullStory, LogRocket, Hotjar
- Experimentation: Optimizely, LaunchDarkly, VWO, Split.io

**Metric Frameworks & Books**:
- Lean Analytics (Alistair Croll, Benjamin Yoskovitz)
- The Lean Startup (Eric Ries) - validated learning and innovation accounting
- Inspired (Marty Cagan) - product discovery metrics
- Hacking Growth (Sean Ellis) - growth metrics and experimentation
- The Startup Metrics for Pirates (Dave McClure) - AARRR framework

**Data Governance & Quality**:
- Data quality frameworks (accuracy, completeness, consistency, timeliness)
- Metric definitions documentation
- Single source of truth (SSOT) principles
- Data lineage and provenance tracking
- Privacy-compliant analytics (GDPR, CCPA)

**Reference**: Amplitude Playbooks, Mixpanel Benchmark Reports, Reforge Growth Series, Lenny's Newsletter (metrics deep-dives)

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
