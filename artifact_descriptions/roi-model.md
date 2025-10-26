# Name: roi-model

## Executive Summary

The ROI Model is a critical financial analysis deliverable within the Inception / Strategy phase, supporting investment decision-making across the initiative lifecycle. This artifact provides rigorous financial evaluation using industry-standard metrics including Net Present Value (NPV), Internal Rate of Return (IRR), payback period, and sensitivity analysis to justify capital allocation and technology investments.

As a cornerstone of financial planning and analysis (FP&A), this artifact enables CFOs, finance teams, and executive leadership to evaluate investment opportunities using discounted cash flow (DCF) analysis, scenario modeling (best case, worst case, expected case), and risk-adjusted returns. Built using tools like Excel, Google Sheets, Anaplan, or Adaptive Insights, the ROI model translates technical initiatives into quantifiable business value with specific emphasis on CapEx vs OpEx trade-offs, total cost of ownership (TCO), and long-term value creation.

### Strategic Importance

- **Investment Justification**: Provides data-driven financial rationale for capital allocation decisions using NPV, IRR, and payback analysis
- **Financial Planning**: Supports FP&A processes with multi-year cash flow projections, operating budget impacts, and capital budgeting
- **Risk Quantification**: Quantifies financial risks through sensitivity analysis, Monte Carlo simulation, and scenario modeling
- **Value Realization**: Establishes baseline metrics and KPIs to track actual vs projected returns and economic value added (EVA)
- **Stakeholder Alignment**: Communicates financial impact to Board, CFO, and executive leadership using standardized financial metrics
- **Resource Optimization**: Enables portfolio-level comparison across competing investment opportunities using consistent financial framework
- **Compliance & Governance**: Supports SOX compliance, capital approval processes, and financial governance requirements

## Purpose & Scope

### Primary Purpose

This artifact provides comprehensive financial analysis to support investment decision-making through:
- **NPV Calculation**: Discounted cash flow analysis using weighted average cost of capital (WACC) to determine net present value
- **IRR Analysis**: Internal rate of return calculation to evaluate investment yield relative to hurdle rate
- **Payback Period**: Time-to-recovery analysis showing when cumulative cash flows turn positive
- **Sensitivity Analysis**: Impact assessment of key variables (revenue growth, cost assumptions, discount rate, implementation timeline)
- **Scenario Modeling**: Best case, worst case, and expected case financial projections with probability weighting
- **Risk-Adjusted Returns**: Incorporation of implementation risk, technology risk, and market risk into financial projections

### Scope

**In Scope**:
- Multi-year financial projections (typically 3-5 years) with annual and quarterly breakdown
- Revenue impact analysis including new revenue, revenue acceleration, and revenue protection
- Cost analysis covering one-time costs (CapEx) and recurring costs (OpEx)
- Cash flow modeling with detailed timing of inflows and outflows
- NPV, IRR, payback period, and profitability index calculations
- Sensitivity analysis on key drivers (±10%, ±20%, ±30% variance scenarios)
- Monte Carlo simulation for probabilistic outcomes (when applicable)
- Comparison to alternative investment options or "do nothing" baseline
- Assumptions documentation and validation approach

**Out of Scope**:
- Total Cost of Ownership (TCO) detailed breakdown (covered in ROI-TCO Calculators artifact)
- Detailed project implementation plan (covered in Project Charter)
- Capitalization accounting treatment (covered in Capitalization Policy)
- Operational metrics beyond financial impact (covered in separate KPI frameworks)

### Target Audience

**Primary Audience**:
- CFO and Finance Leadership: Investment approval and capital allocation decisions
- FP&A Analysts: Financial modeling, analysis, and business case development
- Executive Leadership/Board: Strategic investment evaluation and portfolio prioritization

**Secondary Audience**:
- Program/Project Managers: Understanding financial targets and value realization requirements
- Business Unit Leaders: Evaluating business case for technology or process investments
- Corporate Development: M&A evaluation and strategic initiative assessment

## Document Information

**Format**: Markdown

**File Pattern**: `*.roi-model.md`

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

### Specification Overview

**Specification Purpose**:
- `specificationGoal`: What this specification is defining
- `userStories`: User needs being addressed
- `requirements`: High-level requirements this spec satisfies
- `designPrinciples`: Guiding principles for this specification
- `constraints`: Technical, business, or regulatory constraints

### Technical Specification

**System Components**:
- `componentName`: Name of each system component
- `componentType`: Service | Library | Integration | Data Store | UI Component
- `purpose`: Why this component exists
- `responsibilities`: What this component is responsible for
- `interfaces`: How other components interact with it
- `dependencies`: What this component depends on
- `dataModel`: Data structures used or managed
- `apiEndpoints`: API endpoints exposed (if applicable)

**Functional Requirements**:
- `requirementId`: Unique identifier (e.g., FR-001)
- `requirement`: Detailed requirement statement
- `acceptance Criteria`: How requirement is verified
- `priority`: Must Have | Should Have | Could Have | Won't Have
- `complexity`: Estimation of implementation complexity
- `risks`: Risks associated with this requirement

**Non-Functional Requirements**:
- `performance`: Response time, throughput, capacity targets
- `scalability`: How system scales with load or data volume
- `availability`: Uptime requirements and SLAs
- `reliability`: Error rates, MTBF, MTTR targets
- `security`: Authentication, authorization, encryption requirements
- `compliance`: Regulatory or policy requirements
- `usability`: User experience and accessibility requirements
- `maintainability`: Code quality, documentation, testing standards
- `portability`: Platform independence or migration requirements

### Design Details

**Architecture**:
- `architecturePattern`: Microservices | Monolith | Serverless | Event-Driven
- `componentDiagram`: Visual representation of components and relationships
- `dataFlow`: How data moves through the system
- `integrationPoints`: External system integrations
- `deploymentModel`: How components are deployed and distributed

**Data Model**:
- `entities`: Core data entities
- `relationships`: How entities relate to each other
- `constraints`: Data validation and business rules
- `indexes`: Performance optimization through indexing
- `archival`: Data retention and archival strategy

**Security Design**:
- `authenticationMechanism`: How users/services authenticate
- `authorizationModel`: RBAC | ABAC | ACL approach
- `dataProtection`: Encryption at rest and in transit
- `auditLogging`: What is logged for security audit
- `threatModel`: Key threats and mitigations

### Implementation Guidance

**Development Standards**:
- `codingStandards`: Language-specific coding standards to follow
- `testingRequirements`: Unit test coverage, integration tests required
- `documentationRequirements`: Code comments, API docs, README
- `versionControl`: Branching strategy and commit conventions
- `codeReview`: Review process and criteria

**Quality Gates**:
- `buildRequirements`: Must compile without errors/warnings
- `testRequirements`: All tests must pass, minimum coverage %
- `securityRequirements`: No high/critical vulnerabilities
- `performanceRequirements`: Must meet performance SLAs
- `accessibilityRequirements`: WCAG 2.1 AA compliance (if applicable)


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

**Financial Modeling Best Practices**:
**DCF Methodology**: Use discounted cash flow with organization's standard WACC; document discount rate assumptions and source
**Conservative Assumptions**: Apply conservative revenue growth and aggressive cost estimates to avoid optimism bias
**Sensitivity Analysis**: Test ±20% variance on all key assumptions; identify breakeven points and critical success factors
**Scenario Modeling**: Model best case (P90), expected case (P50), worst case (P10) with probability-weighted expected value
**Cash Flow Timing**: Use realistic implementation timelines; model cash outflows before inflows; account for working capital
**Incremental Analysis**: Measure incremental cash flows only; exclude sunk costs; include opportunity costs
**Tax Treatment**: Account for tax shields on interest, depreciation (if CapEx), and tax impact on operational savings
**Terminal Value**: For long-term investments, calculate terminal value using perpetuity growth or exit multiple approach
**Hurdle Rates**: Compare IRR to organization's hurdle rate (typically WACC + risk premium); NPV must be positive
**Assumption Documentation**: Document all assumptions with sources; distinguish facts from estimates; note confidence levels
**Market Validation**: Validate revenue assumptions with market research, customer interviews, and pilot data
**Competitive Benchmarking**: Compare assumptions to industry benchmarks and competitive intelligence
**Risk Quantification**: Quantify implementation risk, technology risk, and market risk; incorporate into probability-weighted scenarios
**Audit Trail**: Maintain clear links between inputs, calculations, and outputs; enable formula auditing
**FP&A Alignment**: Align with annual operating plan, long-range plan, and capital allocation framework

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

**Financial Metrics & Analysis**:
- Net Present Value (NPV) - Discounted cash flow valuation
- Internal Rate of Return (IRR) - Investment yield metric
- Modified Internal Rate of Return (MIRR) - Addresses IRR limitations
- Payback Period - Time to recover initial investment
- Discounted Payback Period - Time to recover using discounted cash flows
- Profitability Index (PI) - Ratio of NPV to initial investment
- Return on Investment (ROI) - Simple return calculation
- Return on Assets (ROA) - Asset efficiency metric
- Return on Equity (ROE) - Shareholder return metric
- Economic Value Added (EVA) - Value creation above cost of capital
- Total Shareholder Return (TSR) - Combined stock price appreciation and dividends
- Weighted Average Cost of Capital (WACC) - Discount rate calculation
- Free Cash Flow (FCF) - Cash available after capital expenditures
- Discounted Cash Flow (DCF) Analysis - Core valuation methodology

**Financial Planning Standards**:
- GAAP (Generally Accepted Accounting Principles)
- IFRS (International Financial Reporting Standards)
- CFA Institute Standards - Investment analysis best practices
- PMI Standard for Business Analysis
- IIBA BABOK (Business Analysis Body of Knowledge)
- Capital Budgeting Best Practices
- Investment Committee Governance Standards

**SaaS & Technology Metrics**:
- Total Cost of Ownership (TCO)
- CapEx vs OpEx Analysis
- Rule of 40 (Growth Rate + Profit Margin)
- Magic Number (ARR Growth / Sales & Marketing Spend)
- CAC Payback Period (Customer Acquisition Cost recovery)
- LTV:CAC Ratio (Lifetime Value to Customer Acquisition Cost)
- Cloud Migration ROI Models
- Digital Transformation Value Frameworks

**Risk Analysis Frameworks**:
- Monte Carlo Simulation
- Sensitivity Analysis (Tornado Diagrams)
- Scenario Analysis (Best/Base/Worst Case)
- Decision Tree Analysis
- Real Options Valuation
- Risk-Adjusted Net Present Value (rNPV)
- Value at Risk (VaR)
- Expected Monetary Value (EMV)

**Tools & Platforms**:
- Microsoft Excel with Financial Modeling Add-ins
- Google Sheets with Finance Functions
- Anaplan (Enterprise Planning Platform)
- Adaptive Insights (Workday Adaptive Planning)
- Oracle Hyperion Planning
- SAP BPC (Business Planning and Consolidation)
- Prophix (CPM Software)
- Board International
- @RISK (Monte Carlo Simulation Add-in)
- Crystal Ball (Oracle Risk Analysis)

**Governance & Compliance**:
- SOX (Sarbanes-Oxley) Section 404 - Internal Controls
- Capital Allocation Framework
- Investment Committee Charter
- Financial Authorization Matrix
- Project Portfolio Management (PPM) Standards
- IT Investment Governance (ITIL Financial Management)

**Reference**: Consult CFO, FP&A leadership, and corporate finance team for detailed guidance on framework application and organization-specific hurdle rates, discount rates, and approval thresholds

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
