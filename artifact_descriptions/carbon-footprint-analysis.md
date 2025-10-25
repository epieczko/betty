# Name: carbon-footprint-analysis

## Executive Summary

The Carbon Footprint Analysis artifact quantifies greenhouse gas (GHG) emissions across Scope 1 (direct), Scope 2 (purchased energy), and Scope 3 (value chain) categories following GHG Protocol Corporate Standard, ISO 14064-1:2018, and Science Based Targets initiative (SBTi) methodologies. For technology companies, this analysis focuses on data center energy consumption, cloud infrastructure emissions, employee commuting, business travel, purchased goods, and end-of-life product disposal.

Modern carbon accounting leverages cloud provider emissions APIs (AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint, Azure Emissions Impact Dashboard), infrastructure monitoring (Prometheus, Datadog), and carbon intelligence platforms (Watershed, Persefoni, Greenly, Sweep) to track emissions in near-real-time. Organizations measure Power Usage Effectiveness (PUE 1.1-1.2 for efficient data centers), carbon intensity (gCO2e/kWh), and renewable energy percentage (targeting 100% per Google, Microsoft, Apple commitments).

Companies with comprehensive carbon programs achieve 25-40% emissions reductions through renewable energy procurement, data center optimization, and supply chain engagement. Carbon footprint analysis enables TCFD (Task Force on Climate-related Financial Disclosures) reporting, CDP (Carbon Disclosure Project) questionnaire responses, and SBTi validation for 1.5°C-aligned targets, reducing climate risk exposure and meeting stakeholder ESG expectations.

### Strategic Importance

- **Climate Risk Management**: Quantifies enterprise carbon exposure, supporting TCFD scenario analysis and climate risk disclosures per SEC proposed rules
- **SBTi Target Setting**: Provides baseline for Science Based Targets (1.5°C, Well-Below 2°C pathways), requiring Scope 1+2 reductions and Scope 3 engagement
- **CDP & ESG Reporting**: Enables CDP Climate Change questionnaire responses, DJSI (Dow Jones Sustainability Index), and MSCI ESG ratings improvement
- **Regulatory Compliance**: Satisfies EU Corporate Sustainability Reporting Directive (CSRD), California SB 253/261, UK Streamlined Energy & Carbon Reporting (SECR)
- **Carbon Pricing Exposure**: Assesses financial impact of carbon taxes (EU ETS €80-100/tonne), internal carbon pricing, and border adjustment mechanisms
- **Renewable Energy Strategy**: Informs PPA (Power Purchase Agreement) negotiations, REC (Renewable Energy Certificate) purchases, and 100% renewable commitments
- **Stakeholder Transparency**: Demonstrates climate leadership to investors (BlackRock, Vanguard ESG criteria), customers (Salesforce Net Zero Cloud), and employees

## Purpose & Scope

### Primary Purpose

Quantifies organizational GHG emissions across Scope 1 (direct operations), Scope 2 (purchased electricity), and Scope 3 (value chain) following GHG Protocol Corporate Standard and ISO 14064-1:2018, enabling SBTi target setting, TCFD disclosures, CDP reporting, and data-driven decarbonization strategies for technology infrastructure, cloud services, and employee operations.

### Scope

**In Scope**:
- Scope 1 emissions from company-owned data centers (natural gas, diesel generators, refrigerants)
- Scope 2 emissions from purchased electricity (location-based and market-based methods per Scope 2 Guidance)
- Scope 3 Category 1: Purchased goods and services (servers, networking equipment, software licenses)
- Scope 3 Category 3: Fuel and energy-related activities not in Scope 1/2
- Scope 3 Category 5: Waste generated in operations (e-waste recycling, data center waste)
- Scope 3 Category 6: Business travel (flights, rental cars, hotels)
- Scope 3 Category 7: Employee commuting and remote work energy consumption
- Scope 3 Category 11: Use of sold products (cloud services customer consumption, software energy usage)
- Scope 3 Category 13: Downstream leased assets (colocation facilities)
- Cloud provider emissions data (AWS, Google Cloud, Azure APIs for customer carbon footprint)
- Data center efficiency metrics (PUE, WUE, CUE) and renewable energy percentage
- Renewable energy procurement (PPAs, RECs, on-site solar/wind)
- SBTi target alignment (1.5°C pathway, net-zero by 2050)
- TCFD scenario analysis (1.5°C, 2°C, 4°C pathways)
- CDP Climate Change questionnaire responses

**Out of Scope**:
- Scope 3 Categories not material to technology businesses (Category 10: Processing of sold products, Category 14: Franchises)
- Product carbon footprints (LCA) for individual software products (covered in separate Product Carbon Footprint artifact)
- Supply chain emissions beyond Tier 1 suppliers (requires separate Scope 3 deep-dive analysis)
- Biodiversity impacts and nature-related disclosures (covered in TNFD reporting)
- Social sustainability metrics (DEI, labor practices covered in ESG Sustainability Report)
- Detailed offset project verification (covered in Carbon Offset Portfolio Management)

### Target Audience

**Primary Audience**:
- **Sustainability/ESG Teams**: Use carbon footprint data to set SBTi targets, prepare CDP/TCFD reports, and track progress toward net-zero commitments
- **Data Center Operations**: Utilize PUE, WUE metrics to optimize cooling, power distribution, and renewable energy procurement for owned facilities
- **Cloud FinOps Teams**: Analyze AWS/Google Cloud/Azure emissions data to optimize workload placement, rightsizing, and carbon-aware scheduling
- **Corporate Finance**: Assess carbon pricing exposure, internal carbon fee allocations, and ROI for renewable energy investments and efficiency projects

**Secondary Audience**:
- **Executive Leadership & Board**: Review annual emissions trends, SBTi progress, and TCFD climate risk assessments for strategic decision-making
- **Investor Relations**: Communicate emissions performance to ESG-focused investors (BlackRock, Vanguard) and respond to shareholder climate proposals
- **Procurement Teams**: Evaluate supplier emissions data, prioritize low-carbon vendors, and incorporate emissions criteria in RFPs per Scope 3 engagement strategy
- **External Auditors**: Verify emissions calculations and data quality for limited assurance engagements under ISAE 3000, AA1000 standards

## Document Information

**Format**: Markdown

**File Pattern**: `*.carbon-footprint-analysis.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal (emissions data), Public (annual sustainability report summary)

**Retention**: 7 years minimum (regulatory requirements), permanent for annual baseline and SBTi submissions

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

### Report Overview

**Reporting Period**:
- `reportingPeriod`: Time period covered (e.g., Q2 2024, Jan 2024, etc.)
- `reportDate`: Date report was generated
- `reportType`: Regular | Ad-hoc | Special Investigation | Executive Briefing
- `frequency`: How often this report is generated
- `distribution`: Intended recipients and distribution method

### Executive Summary

**Key Highlights**:
- `criticalFindings`: Top 3-5 most important findings for executive attention
- `trendAnalysis`: Key trends compared to previous periods
- `recommendations`: Priority recommendations requiring executive decision
- `impactAssessment`: Business impact of findings or metrics

### Detailed Analysis

**Metrics & KPIs**:
- `metricName`: Name of each metric or KPI
- `currentValue`: Value for this reporting period
- `targetValue`: Target or goal
- `previousValue`: Value from previous period for trending
- `variance`: Difference from target and trend direction
- `variances`: Explanation of significant variances
- `dataSource`: Where data comes from
- `collectionMethod`: How data is collected and validated

**Analysis by Category**:
- `category`: Grouping for related metrics or findings
- `observations`: What was observed or measured
- `analysis`: Interpretation and meaning
- `rootCauses`: Underlying causes for significant findings
- `impact`: Business or operational impact
- `trends`: Patterns over time
- `comparatives`: Benchmarking against industry or peer data

### Recommendations & Actions

**Priority Actions**:
- `actionId`: Unique identifier
- `actionDescription`: What needs to be done
- `rationale`: Why this action is needed
- `priority`: P0 | P1 | P2 | P3
- `owner`: Who is responsible
- `dueDate`: Target completion date
- `estimatedEffort`: Resource requirement
- `dependencies`: Prerequisites or dependencies
- `successMetrics`: How success will be measured

**Follow-up Items**:
- `openItems`: Items from previous reports still in progress
- `closedItems`: Items completed since last report
- `escalations`: Items requiring escalation to higher authority


## Best Practices

**Organizational Boundaries**: Apply operational control approach (GHG Protocol) consistently; document organizational boundary methodology annually per ISO 14064-1:2018 Section 5
**Data Quality Tiers**: Prioritize primary data (utility bills, fuel receipts) over secondary (industry averages); achieve 80%+ primary data coverage for Scope 1+2 per GHG Protocol quality standards
**Market-Based Scope 2**: Calculate both location-based (grid average) and market-based (contractual instruments like RECs, PPAs) methods per Scope 2 Guidance dual reporting requirement
**Scope 3 Materiality Screening**: Conduct annual materiality assessment across all 15 categories; focus detailed tracking on categories >5% total emissions per Corporate Value Chain Standard
**Emission Factors**: Use region-specific factors (IEA, EPA eGRID, DEFRA) updated annually; document factor sources and vintages for audit trail and year-over-year comparability
**Cloud Provider APIs**: Integrate AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint, Azure Emissions Impact Dashboard for automated Scope 3 Category 11 tracking
**PUE Measurement**: Calculate Power Usage Effectiveness monthly per The Green Grid methodology; target PUE <1.2 for hyperscale data centers, <1.5 for enterprise facilities
**SBTi Alignment**: Set near-term (5-10 year) and net-zero (2050) targets following SBTi Corporate Net-Zero Standard v1.1; validate targets through SBTi submission process
**Carbon Intensity Metrics**: Track emissions per revenue (tCO2e/$M), per employee (tCO2e/FTE), per data transferred (gCO2e/GB) for operational KPIs and benchmarking
**Renewable Energy Matching**: Achieve 24/7 hourly matching (Google, Microsoft approach) beyond annual RECs; prioritize PPAs with additionality over unbundled RECs
**Scenario Analysis**: Conduct TCFD-aligned climate scenario modeling (1.5°C, 2°C, 4°C pathways) annually; assess physical and transition risks per TCFD recommendations
**Data Center Optimization**: Implement AI/ML-driven cooling optimization (DeepMind approach); achieve 30-40% cooling energy reduction through machine learning controls
**Employee Engagement**: Track remote work emissions (home office electricity, heating); provide carbon budgets for business travel with low-carbon alternatives (rail vs. air)
**Supplier Engagement**: Request CDP Supply Chain disclosures from top 80% spend suppliers; incorporate emissions reduction clauses in procurement contracts
**Third-Party Assurance**: Obtain limited assurance (ISAE 3000, AA1000) for Scope 1+2 emissions; pursue reasonable assurance for mature programs
**Automation & Tools**: Implement carbon accounting platforms (Watershed, Persefoni, Sweep) for continuous monitoring; reduce manual data collection by 70%+
**Offset Quality**: Prioritize removal-based offsets (direct air capture, reforestation) over avoidance; ensure additionality, permanence per VCS, Gold Standard
**Internal Carbon Pricing**: Set shadow carbon price ($40-100/tonne) for investment decisions; implement internal carbon fee to fund decarbonization projects
**Disclosure Transparency**: Publish full GHG inventory in annual sustainability report; achieve CDP A/A- rating through comprehensive disclosure
**Continuous Improvement**: Conduct quarterly emissions reviews with operations teams; set annual reduction targets (5-10% YoY) aligned with SBTi pathways
**Regulatory Monitoring**: Track evolving mandatory disclosure (EU CSRD, SEC Climate Rule, California laws); prepare for Scope 3 reporting expansion
**Data Governance**: Establish clear data ownership, validation workflows, and audit trails; maintain 7+ years historical data for trend analysis and regulatory compliance
**Cross-Functional Collaboration**: Convene monthly carbon steering committee (Finance, Operations, Procurement, IT); assign carbon accountability to business units
**Technology Innovation**: Pilot carbon-aware computing (shift workloads to low-carbon hours/regions); evaluate emerging tech (liquid cooling, hydrogen fuel cells)
**Benchmarking**: Compare PUE, carbon intensity against industry peers (Uptime Institute, The Green Grid); participate in industry consortiums for best practice sharing

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

**GHG Accounting Standards**: GHG Protocol Corporate Accounting and Reporting Standard, GHG Protocol Scope 2 Guidance (market-based, location-based), GHG Protocol Corporate Value Chain (Scope 3) Standard, ISO 14064-1:2018 GHG Emissions and Removals, ISO 14064-3:2019 Validation and Verification, WRI/WBCSD GHG Protocol Amendments

**Science-Based Targets**: SBTi Corporate Net-Zero Standard v1.1, SBTi Criteria and Recommendations v5.2, 1.5°C Business Ambition Pledge, SBTi FLAG (Forest, Land, and Agriculture) Guidance, SBTi Sectoral Decarbonization Approach (SDA), SBTi Beyond Value Chain Mitigation (BVCM)

**Climate Disclosure Frameworks**: TCFD (Task Force on Climate-related Financial Disclosures) Recommendations v1.0, CDP Climate Change Questionnaire 2024, ISSB IFRS S2 Climate-related Disclosures, SEC Climate Disclosure Proposed Rule (33-11042), CDSB (Climate Disclosure Standards Board) Framework

**ESG Reporting Standards**: GRI (Global Reporting Initiative) Standards 305 (Emissions), SASB (Sustainability Accounting Standards Board) Standards for Technology & Communications, EU Corporate Sustainability Reporting Directive (CSRD), EU Taxonomy for Sustainable Activities Regulation, ESRS E1 (Climate Change)

**Carbon Measurement Tools**: AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint Dashboard, Azure Emissions Impact Dashboard, Watershed Carbon Intelligence Platform, Persefoni Climate Management & Accounting Platform, Greenly Carbon Accounting Software, Sweep ESG Data Management Platform

**Data Center Efficiency**: PUE (Power Usage Effectiveness) - The Green Grid Standard v3.0, WUE (Water Usage Effectiveness), CUE (Carbon Usage Effectiveness), ASHRAE TC 9.9 Mission Critical Facilities Standards, EU Code of Conduct for Data Centres Energy Efficiency v12.0, Uptime Institute Tier Standards

**Renewable Energy**: RE100 100% Renewable Electricity Initiative, EAC (Energy Attribute Certificates) International REC Standard, RECs (Renewable Energy Certificates) - Green-e Certification, PPAs (Power Purchase Agreements) - VPPA Structures, IEA Renewable Energy Taxonomy, 24/7 Carbon-Free Energy Compact

**Carbon Pricing & Offsets**: Internal Carbon Pricing Guidance - CDP/WRI, EU ETS (Emissions Trading System) Phase 4 Regulations, California Cap-and-Trade Program, VCS (Verified Carbon Standard) v4.4, Gold Standard for Global Goals Impact Registry, CDM (Clean Development Mechanism), ACR (American Carbon Registry), Puro.earth CO2 Removal Certificates

**Cloud & IT Emissions**: Software Carbon Intensity (SCI) Specification - Green Software Foundation, SDIA (Sustainable Digital Infrastructure Alliance) Metrics, Energy Star for Data Centers, TCO Certified for IT Products, IEEE 1680.1 EPEAT for Computers and Displays, ASHRAE 90.4 Energy Standard for Data Centers

**Aviation & Travel**: CORSIA (Carbon Offsetting and Reduction Scheme for International Aviation), DEFRA GHG Conversion Factors for Business Travel, GHG Protocol Transport Tool v2.8, Atmosfair Flight Emissions Calculator, myclimate Carbon Footprint Calculator for Business Travel

**Supply Chain Emissions**: CDP Supply Chain Program Questionnaire, Science Based Targets for Value Chains, Scope 3 Evaluator Tool - Quantis/WRI, Product Attribute to Impact Algorithm (PAIA) - Walmart, Partnership for Carbon Transparency (PACT) Pathfinder Framework, ISO 14067:2018 Carbon Footprint of Products

**Regulatory & Compliance**: California SB 253 Climate Corporate Data Accountability Act, California SB 261 Greenhouse Gases: Climate-Related Financial Risk, UK Streamlined Energy and Carbon Reporting (SECR), Australia NGER (National Greenhouse and Energy Reporting) Scheme, Japan Act on Promotion of Global Warming Countermeasures

**Assurance Standards**: ISAE 3000 Assurance on Non-Financial Information, ISAE 3410 Assurance on GHG Statements, AA1000 Assurance Standard v3, Limited Assurance vs. Reasonable Assurance Guidance, DNV GL GHG Verification Protocol, SGS Carbon Footprint Verification Services

**Data Quality**: GHG Protocol Data Uncertainty Guidance, ISO/IEC Guide 98-3 Uncertainty of Measurement, Primary vs. Secondary Data Hierarchy, Data Quality Scoring (1-5 scale per GHG Protocol), Activity Data Collection Best Practices, Emission Factor Selection Criteria

**Sector-Specific**: SASB Technology & Communications Sector Standards TC-SI (Software & IT Services), GRESB Infrastructure Asset Assessment for Data Centers, Uptime Institute PUE Reporting Protocol, The Green Grid Data Center Maturity Model, Energy Star Portfolio Manager for Data Centers

**Emerging Standards**: TNFD (Taskforce on Nature-related Financial Disclosures) Beta Framework, CSRD ESRS 2 (General Disclosures), IFRS S1 General Requirements for Sustainability Disclosures, GHG Protocol Land Sector and Removals Guidance (under development), Scope 4 Avoided Emissions Guidance (emerging)

**Reference**: Consult GHG Protocol Technical Guidance Library, SBTi Criteria Document v5.2, CDP Technical Guidance for Climate Change, TCFD Knowledge Hub Resources, and organizational sustainability accounting standards for detailed methodological guidance and sector-specific calculation approaches

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Energy consumption data (electricity, natural gas, diesel) from utility bills and facility management systems
- Cloud provider carbon footprint data (AWS, Google Cloud, Azure) via APIs or dashboards
- Travel and expense system data (business travel flights, hotels, rental cars) from Concur, SAP, Expensify
- Procurement data (purchased goods, capital equipment) from ERP systems with spend categorization
- Employee commute surveys and remote work assessments for Scope 3 Category 7
- Data center operations metrics (PUE, cooling loads, IT equipment power) from DCIM systems
- Renewable energy contracts (PPAs, RECs) from procurement and finance teams
- Organizational structure and operational boundary documentation defining consolidation approach
- Prior year GHG inventory for baseline establishment and year-over-year trending

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Annual Sustainability Report for public disclosure and stakeholder communication
- CDP Climate Change Questionnaire responses (C6-C10 emissions sections)
- TCFD Climate Risk Assessment for scenario analysis and transition risk quantification
- SBTi Target Submission for near-term and net-zero target validation
- Board ESG Committee quarterly reviews and climate strategy discussions
- Investor Relations materials for ESG-focused investors and shareholder engagement
- Internal carbon pricing models for project evaluation and budget allocation
- Procurement scorecards incorporating supplier emissions performance
- Data center operations dashboards for PUE tracking and efficiency optimization
- Cloud FinOps optimization recommendations for carbon-aware workload scheduling

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Sustainability Report (comprehensive ESG performance including carbon alongside DEI, governance metrics)
- TCFD Climate Risk Assessment (uses carbon data for transition risk scenario analysis)
- Science Based Targets Submission (defines reduction pathways informed by baseline emissions)
- Renewable Energy Procurement Strategy (PPAs, RECs aligned with Scope 2 reduction goals)
- Data Center Efficiency Roadmap (PUE improvement initiatives tied to Scope 1+2 targets)
- Cloud Cost Optimization Plan (FinOps initiatives including carbon-aware scheduling)
- Sustainable Procurement Policy (supplier engagement requirements for Scope 3 reduction)
- Business Continuity Plan (climate scenario risks inform resilience planning)

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
- Primary Approver: VP Sustainability / Chief Sustainability Officer
- Secondary Approver: CFO (for carbon pricing exposure and financial risk assessment)
- Governance Approval: Board ESG Committee (annual baseline and SBTi commitments)

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly (interim tracking), Annually (full inventory and external reporting)

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur (M&A, divestiture, new data centers)
- Regulatory requirements change (new mandatory disclosure rules)
- Major incidents reveal deficiencies (data quality issues, calculation errors)
- Stakeholder requests identify needed updates (investor queries, CDP feedback)
- Related artifacts are substantially updated (renewable energy contracts, SBTi targets)

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Methodology changes (operational control to equity share, emission factor updates)
- **MINOR**: New Scope 3 categories added, expanded data coverage
- **PATCH**: Corrections, clarifications, minor updates to formatting

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: 7 years minimum (regulatory requirements), permanent for annual baselines and SBTi submissions

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Sustainability Manager / ESG Analyst

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates quarterly and annually
- Manage review and approval process for annual inventory
- Respond to stakeholder questions from investors, auditors, regulators
- Archive superseded versions per retention policy

## Templates & Examples

### Template Access

**Primary Template**: `templates/carbon-footprint-analysis-template.md`

**Alternative Formats**: Excel (GHG calculations), PDF (executive summary)

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/carbon-footprint-analysis-example-2024.md`

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

- SOC 2: Environmental sustainability controls for Type II reporting
- ISO 27001: Environmental management integration with ISMS
- GDPR/Privacy: Employee commute data privacy considerations
- Industry-Specific: SEC Climate Disclosure Rule (pending), EU CSRD mandatory reporting

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team (annual GHG inventory review)
- External audits by third-party auditors (ISAE 3000 limited assurance)
- Regulatory examinations (SEC climate risk disclosure if finalized)
- Customer security assessments (Scope 3 Category 11 customer data requests)

**Audit Preparation**:
- Maintain complete version history
- Document all approvals with evidence
- Keep change log current
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- Corporate Sustainability Policy (climate commitments, SBTi alignment)
- Procurement Policy (supplier emissions disclosure requirements)
- Travel Policy (carbon budgets, low-carbon alternatives)
- Data Center Operations Policy (PUE targets, renewable energy procurement)

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: 100% of required data fields populated for Scope 1+2, 80%+ for material Scope 3 categories
- **Data Quality Score**: 80%+ primary data for Scope 1+2 per GHG Protocol quality tiers
- **Review Cycle Time**: Annual inventory completed within 90 days of fiscal year end
- **Stakeholder Satisfaction**: Survey rating from sustainability committee and ESG investors

### Usage Metrics

- **Access Frequency**: Monthly by sustainability team, quarterly by exec leadership
- **Update Frequency**: Quarterly interim tracking, annual full inventory
- **Downstream Impact**: Feeds 5+ artifacts (Sustainability Report, CDP, TCFD, SBTi, Board reporting)

### Continuous Improvement

- Gather feedback from users and reviewers (auditors, CDP scoring feedback)
- Track common questions or confusion points (methodology changes, data gaps)
- Identify recurring issues or challenges (Scope 3 data availability, cloud provider APIs)
- Update template and guidance based on lessons learned (automation opportunities)
- Share best practices across organization (procurement engagement tactics)

## Metadata Tags

**Phase**: Portfolio, Governance, and Delivery Ops

**Category**: Sustainability, ESG, Climate Risk

**Typical Producers**: Sustainability Manager, ESG Analyst, Environmental Specialist

**Typical Consumers**: Chief Sustainability Officer, CFO, Board ESG Committee, Investor Relations, External Auditors

**Effort Estimate**: 120-200 hours annually (data collection, calculations, verification, reporting)

**Complexity Level**: High (multi-category emissions, complex calculations, regulatory requirements)

**Business Criticality**: High (investor expectations, regulatory compliance, reputational risk)

**Change Frequency**: Regular (quarterly tracking, annual comprehensive update)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Portfolio, Governance, and Delivery Ops - Version 2.0*
