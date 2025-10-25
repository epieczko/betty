# Name: price-books

## Executive Summary

The Price Books are comprehensive product and service catalogs that define official list prices, SKU structures, volume discounts, channel partner pricing, and regional pricing variations across all offerings. These master pricing references serve as the single source of truth for sales, finance, and operations teams, ensuring pricing consistency, enabling accurate quoting, and supporting revenue recognition compliance.

As critical revenue management tools, price books integrate with CRM systems (Salesforce, HubSpot), CPQ (Configure Price Quote) platforms, ERP systems, and billing platforms to automate quote generation, enforce discount guardrails, and maintain pricing integrity. They capture complex pricing models including tiered pricing, volume discounts, good/better/best packaging, channel partner pricing, educational/non-profit pricing, and geographic price variations, while maintaining audit trails for pricing changes and approvals.

### Strategic Importance

- **Revenue Consistency**: Ensures standardized pricing across all sales channels, preventing revenue leakage and margin erosion
- **Sales Enablement**: Provides clear, accessible pricing for sales teams to quote accurately and close deals efficiently
- **Margin Protection**: Establishes list prices that support target margins and profitability goals before discounting
- **Channel Management**: Defines partner pricing, distributor pricing, and reseller discounts to support indirect sales
- **Competitive Positioning**: Reflects market positioning (premium, competitive, value) through pricing structure and levels
- **Compliance & Audit**: Supports revenue recognition (ASC 606), tax compliance, and financial audit requirements
- **Analytics Foundation**: Enables pricing analytics, discount analysis, and realization rate tracking (actual vs list price)

## Purpose & Scope

### Primary Purpose

This artifact provides authoritative pricing information including:
- **SKU Catalog**: Complete product and service SKU list with descriptions, product codes, and categorization
- **List Prices**: Official standard pricing before any discounts (MSRP, list price, rack rate)
- **Volume Discounts**: Tiered pricing based on quantity breakpoints (1-10 units, 11-50, 51-100, etc.)
- **Channel Partner Pricing**: Distributor pricing, reseller discounts, VAR pricing, SI partner pricing
- **Regional Pricing**: Geographic price variations (US, EMEA, APAC) accounting for currency, taxes, market conditions
- **Pricing Tiers**: Good/better/best packaging, bronze/silver/gold/platinum tiers, freemium vs paid
- **Contract Pricing**: Multi-year agreement pricing, enterprise license agreements (ELA), volume commitment discounts
- **Special Pricing Programs**: Educational pricing, non-profit pricing, government pricing, startup programs

### Scope

**In Scope**:
- Product catalog with SKU numbers, descriptions, and product hierarchy
- Standard list prices and effective dates for all products and services
- Volume discount schedules and quantity breakpoints
- Partner/channel pricing tiers and discount percentages
- Regional pricing variations and currency conversions
- Promotional pricing and limited-time offers
- Pricing approval workflows and authorization levels
- Price change management and version control
- Integration with CPQ, CRM, ERP, and billing systems
- Pricing terms and conditions (annual, monthly, one-time, usage-based)

**Out of Scope**:
- Discounting policies and approval limits (covered in Discount Guardrails)
- Pricing strategy and positioning (covered in Pricing & Packaging Strategy)
- Deal-specific custom pricing and exceptions
- Revenue recognition accounting treatment
- Detailed product specifications (covered in product documentation)

### Target Audience

**Primary Audience**:
- Sales Teams: Accessing pricing for quotes and proposals
- Pricing Teams: Maintaining price books and managing price changes
- Finance Teams: Revenue planning, margin analysis, and financial reporting

**Secondary Audience**:
- Channel Partners: Understanding partner pricing and discounts
- Product Management: Aligning pricing with product strategy
- Revenue Operations: CPQ configuration and pricing automation
- Deal Desk: Pricing approvals and exception management

## Document Information

**Format**: Markdown

**File Pattern**: `*.price-books.md`

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

**Price Book Management Best Practices**:
**Single Source of Truth**: Maintain one master price book; avoid duplicate or conflicting price lists across systems
**Effective Dating**: Use clear effective dates for all price changes; support future-dated pricing for planned increases
**Version Control**: Track all price changes with version history, change rationale, and approval evidence
**SKU Standardization**: Establish consistent SKU naming conventions; use product codes that scale and organize logically
**Margin Discipline**: Set list prices to support target gross margins (e.g., 70-80% for SaaS) before discounting
**Competitive Benchmarking**: Review competitive pricing quarterly; ensure positioning supports value proposition
**Volume Bands**: Structure volume discounts at meaningful breakpoints that incentivize larger purchases
**Channel Consistency**: Ensure channel partner pricing protects direct sales and prevents channel conflict
**Regional Parity**: Balance local market pricing with global consistency; account for purchasing power and competition
**Currency Management**: Update exchange rates regularly; consider currency hedging for multi-year contracts
**Price Testing**: Test price changes with small customer segments before broad rollout
**Grandfathering Policy**: Define clear policy for existing customers when prices increase (honor old pricing for how long?)
**Promotional Discipline**: Limit promotional pricing duration; require approval and sunset dates to prevent permanent discounts
**CPQ Integration**: Ensure price books sync seamlessly with CPQ; test quote calculations thoroughly
**Sales Training**: Train sales teams on new pricing; provide pricing rationale and competitive positioning
**Price Change Communication**: Communicate price increases to customers 60-90 days in advance with clear justification
**Discount Waterfall**: Track discount progression from list price to net price; identify margin leakage
**ASC 606 Alignment**: Ensure price books support standalone selling price (SSP) determination for revenue recognition

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

**Pricing Management Platforms**:
- Salesforce CPQ (Configure Price Quote)
- Oracle CPQ Cloud
- SAP CPQ (formerly CallidusCloud)
- Apttus (Conga) CPQ
- PandaDoc CPQ & Pricing
- DealHub CPQ
- Zuora (subscription billing and pricing)
- Chargebee (subscription pricing management)

**CRM & Sales Systems**:
- Salesforce Sales Cloud (Price Books feature)
- Microsoft Dynamics 365 Sales
- HubSpot CRM
- Pipedrive
- Oracle CRM
- SAP CRM

**ERP & Billing Systems**:
- NetSuite (Price Books and Item Pricing)
- SAP S/4HANA (Pricing Conditions)
- Oracle ERP Cloud
- Microsoft Dynamics 365 Finance & Operations
- Sage Intacct
- QuickBooks Enterprise

**Revenue Management Standards**:
- ASC 606 / IFRS 15: Revenue from Contracts with Customers
- Standalone Selling Price (SSP) determination
- Variable Consideration and Price Concessions
- Contract Modifications and Pricing Changes
- Performance Obligations and Pricing Allocation

**Pricing Strategy Frameworks**:
- Value-Based Pricing methodology
- Cost-Plus Pricing approach
- Competitive Pricing analysis
- Penetration Pricing for market entry
- Price Skimming for innovation
- Psychological Pricing (charm pricing, prestige pricing)
- Dynamic Pricing and algorithmic pricing
- Freemium Pricing models

**SaaS & Subscription Pricing**:
- Per-User (Per-Seat) Pricing
- Per-Feature/Tier Pricing (good/better/best)
- Usage-Based Pricing (consumption, metered)
- Freemium with paid upgrades
- Land-and-Expand pricing strategies
- Annual vs Monthly pricing (ACV vs MRR)

**Channel & Partner Pricing**:
- Distributor Pricing and Margins
- Value-Added Reseller (VAR) Discounts
- System Integrator (SI) Partner Pricing
- Referral Partner Commissions
- Managed Service Provider (MSP) Pricing
- OEM and White-Label Pricing

**Pricing Analytics & Optimization**:
- Price Elasticity Analysis
- Willingness to Pay (WTP) Research
- Van Westendorp Price Sensitivity Meter
- Conjoint Analysis for pricing features
- Price Realization Rate (List vs Actual)
- Price Waterfall Analysis
- Margin Bridge Analysis

**Compliance & Governance**:
- Robinson-Patman Act (price discrimination)
- Export Control Regulations (ITAR, EAR)
- Transfer Pricing for multinational operations
- Tax Compliance (VAT, Sales Tax, GST)
- Government Pricing Regulations (GSA, DoD)
- Antitrust and Competition Law

**Pricing Change Management**:
- Price Increase Communication Strategies
- Grandfathering vs Universal Price Changes
- Contract Price Escalation Clauses
- Promotional Pricing Sunsets
- Price Protection Periods

**Tools & Platforms**:
- Microsoft Excel (Price List Management)
- Google Sheets
- Pricefx (pricing software)
- PROS Pricing (AI-driven pricing)
- Vendavo (B2B pricing optimization)
- Zilliant (pricing intelligence)

**Reference**: Consult Chief Revenue Officer (CRO), VP Pricing, Revenue Operations, and Finance teams for detailed guidance on pricing framework application, competitive positioning, and margin requirements

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
