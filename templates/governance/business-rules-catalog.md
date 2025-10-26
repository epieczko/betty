# Business Rules Catalog

**Document Version**: 1.0.0
**Last Updated**: 2025-01-15
**Document Owner**: Business Analysis & Product Management
**Classification**: Internal

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | BR-CAT-2025-001 |
| **Status** | Active |
| **Created Date** | 2025-01-15 |
| **Next Review** | 2025-04-15 (Quarterly) |
| **Primary Author** | Business Analyst |
| **Approvers** | Product Owner, Compliance Officer |

## Executive Summary

This Business Rules Catalog serves as the centralized repository for all business logic, decision criteria, policies, and constraints that govern organizational operations and system behavior. Using Decision Model and Notation (DMN) standard and structured decision tables, this artifact enables business users to define, test, and modify rules without code changes while maintaining complete audit trails for regulatory compliance (SOX, GDPR, HIPAA, PCI-DSS).

**Purpose**: Single source of truth for all business rules, enabling centralized management, version control, impact analysis, and regulatory compliance.

**Strategic Value**: Separates business logic from application code, reduces time-to-market for policy changes from weeks to hours, provides complete audit trail for compliance.

---

## 1. Business Rule Categories

| Category | Definition | Examples | Ownership |
|----------|------------|----------|-----------|
| **Validation Rules** | Data quality and completeness checks | Email format, required fields, data ranges | Product Team |
| **Calculation Rules** | Mathematical computations and formulas | Pricing, tax, discounts, commissions | Finance Team |
| **Inference Rules** | Logical deductions from facts | Customer segmentation, risk scoring | Data Science Team |
| **Constraints** | Business policies and limits | Credit limits, approval thresholds, SLAs | Compliance Team |
| **Eligibility Rules** | Qualification criteria | Discount eligibility, feature access | Product Team |

---

## 2. Rule Naming Convention

**Format**: `BR-[DOMAIN]-[TYPE]-[SEQUENCE]`

**Examples**:
- `BR-PRICING-CALC-001`: Product pricing calculation
- `BR-CREDIT-VALID-012`: Credit score validation
- `BR-DISCOUNT-ELIG-005`: Discount eligibility criteria
- `BR-SHIPPING-INFER-003`: Shipping method recommendation

---

## 3. Decision Tables (DMN Standard)

### Example 1: Discount Eligibility (E-Commerce)

**Rule ID**: BR-DISCOUNT-ELIG-001
**Rule Name**: Volume Discount Eligibility
**Effective Date**: 2025-01-01
**Owner**: Pricing Team
**Version**: 2.0

| Order Value (USD) | Customer Type | Order Frequency (90d) | Discount % | Priority |
|------------------|---------------|---------------------|-----------|----------|
| >= $10,000 | Enterprise | Any | 15% | 1 |
| >= $5,000 | Enterprise | Any | 10% | 2 |
| >= $2,500 | SMB | >= 3 orders | 8% | 3 |
| >= $1,000 | SMB | >= 5 orders | 5% | 4 |
| >= $500 | Retail | >= 10 orders | 3% | 5 |
| < $500 | Any | Any | 0% | 6 |

**Rule Logic** (Hit Policy: First Match):
```
IF Order_Value >= 10000 AND Customer_Type = "Enterprise"
  THEN Discount = 15%
ELSE IF Order_Value >= 5000 AND Customer_Type = "Enterprise"
  THEN Discount = 10%
ELSE IF Order_Value >= 2500 AND Customer_Type = "SMB" AND Order_Frequency_90d >= 3
  THEN Discount = 8%
...
```

**Test Scenarios**:

| Test Case | Order Value | Customer Type | Order Frequency | Expected Discount | Actual Result | Status |
|-----------|------------|---------------|----------------|------------------|---------------|--------|
| TC-001 | $12,000 | Enterprise | 2 | 15% | 15% | Pass |
| TC-002 | $6,000 | Enterprise | 1 | 10% | 10% | Pass |
| TC-003 | $3,000 | SMB | 5 | 8% | 8% | Pass |
| TC-004 | $800 | Retail | 12 | 3% | 3% | Pass |
| TC-005 | $400 | Retail | 2 | 0% | 0% | Pass |

---

### Example 2: Credit Application Approval (Financial Services)

**Rule ID**: BR-CREDIT-ELIG-001
**Rule Name**: Consumer Credit Approval Decisioning
**Effective Date**: 2025-01-01
**Owner**: Risk Management
**Compliance**: FCRA, Equal Credit Opportunity Act
**Version**: 3.1

| Credit Score | Debt-to-Income Ratio | Employment Status | Bankruptcies (7yr) | Decision | Credit Limit | Interest Rate |
|-------------|---------------------|-------------------|-------------------|----------|-------------|--------------|
| >= 750 | <= 30% | Employed | 0 | Approved | $50,000 | 12.9% |
| >= 700 | <= 35% | Employed | 0 | Approved | $25,000 | 15.9% |
| >= 650 | <= 40% | Employed | 0 | Approved | $10,000 | 19.9% |
| >= 620 | <= 45% | Employed | 0 | Manual Review | TBD | TBD |
| >= 600 | <= 35% | Employed | 0 | Manual Review | TBD | TBD |
| < 600 | Any | Any | Any | Declined | $0 | N/A |
| Any | > 50% | Any | Any | Declined | $0 | N/A |
| Any | Any | Unemployed | Any | Declined | $0 | N/A |
| Any | Any | Any | >= 1 | Declined | $0 | N/A |

**Regulatory Notes**:
- Adverse action notices required for declines (FCRA Section 615)
- Manual review decisions documented within 30 days
- Annual rule review for disparate impact analysis (ECOA)

---

### Example 3: Shipping Method Recommendation

**Rule ID**: BR-SHIPPING-INFER-001
**Rule Name**: Optimal Shipping Method Selection
**Effective Date**: 2025-01-01
**Owner**: Logistics Team
**Version**: 1.2

| Package Weight | Destination Zone | Delivery Urgency | Customer Tier | Recommended Method | Est. Delivery | Cost |
|---------------|-----------------|-----------------|---------------|-------------------|--------------|------|
| <= 1 lb | Zone 1-3 | Standard | Any | USPS First Class | 3-5 days | $4.50 |
| <= 5 lb | Zone 1-3 | Standard | Any | USPS Priority | 2-3 days | $8.90 |
| <= 5 lb | Zone 1-3 | Expedited | Premium | FedEx Overnight | 1 day | $35.00 |
| <= 50 lb | Any | Standard | Any | UPS Ground | 3-7 days | $12.50 |
| > 50 lb | Any | Any | Any | Freight Quote | TBD | TBD |
| Any | International | Any | Any | UPS Worldwide | 5-10 days | Calculated |

---

## 4. Business Rule Specifications

### Template: Structured Natural Language

**Rule ID**: BR-PRICING-CALC-003
**Rule Name**: Dynamic Pricing Adjustment for Peak Demand
**Category**: Calculation Rule
**Status**: Active
**Effective Date**: 2024-12-01
**Expiration Date**: None
**Owner**: Revenue Management Team
**Last Modified**: 2025-01-10 by Sarah Johnson

**Business Context**:
During high-demand periods (holidays, special events), apply surge pricing to optimize revenue while maintaining customer satisfaction. This rule applies to all bookable inventory (hotel rooms, car rentals, event tickets).

**Rule Statement**:
```
WHEN inventory_utilization >= 85%
AND booking_lead_time < 7 days
THEN base_price = base_price * surge_multiplier

WHERE surge_multiplier IS CALCULATED AS:
  - Peak Season (Dec 20-31, July 1-15): 1.5x
  - High Demand (80-89% utilization): 1.25x
  - Very High Demand (90-95% utilization): 1.5x
  - Extreme Demand (>95% utilization): 2.0x
  - Maximum multiplier cap: 2.0x

AND surge_multiplier DOES NOT APPLY IF:
  - Customer has VIP status
  - Booking is part of corporate contract
  - Advance purchase (>30 days) with price lock
```

**Input Variables**:
- `inventory_utilization`: Float (0-100%)
- `booking_lead_time`: Integer (days)
- `base_price`: Currency (USD)
- `season`: Enum (PEAK, STANDARD, OFF_PEAK)
- `customer_tier`: Enum (VIP, STANDARD, NEW)

**Output Variables**:
- `adjusted_price`: Currency (USD)
- `surge_multiplier`: Float
- `surge_reason`: String

**Dependencies**:
- Inventory Management System (real-time utilization data)
- Customer Relationship Management (tier status)
- Pricing Engine API

**Exceptions**:
1. If pricing error occurs, default to base_price (no surge)
2. Log all pricing decisions to audit table
3. Alert Revenue Team if surge > 1.75x for manual review

**Compliance**:
- Must comply with state price gouging laws
- Transparency requirement: Display surge reason to customer
- Price lock honored for confirmed bookings

---

## 5. Rule Versioning & Change Control

### Version History Example

| Version | Effective Date | Changes | Reason | Approver | Compliance Impact |
|---------|---------------|---------|--------|----------|------------------|
| 3.1 | 2025-01-01 | Increased DTI threshold from 35% to 40% for 650+ credit scores | Market competitiveness | Risk Committee | None - within FCRA guidelines |
| 3.0 | 2024-10-01 | Added employment status check | Regulatory requirement | Compliance Officer | ECOA compliance - approved by Legal |
| 2.5 | 2024-07-01 | Reduced min credit score from 640 to 620 for manual review | Expand addressable market | Chief Risk Officer | Increased manual review volume |
| 2.0 | 2024-01-01 | Restructured decision table for clarity | Process improvement | Risk Committee | No business impact |

**Change Request Process**:
1. Submit change request with business justification
2. Impact analysis: affected systems, downstream rules, test scenarios
3. Compliance review (if regulatory impact)
4. Approval by rule owner and stakeholders
5. Update rule catalog and version control
6. Deploy to test environment
7. Execute regression test suite
8. Deploy to production with rollback plan
9. Monitor for 48 hours post-deployment

---

## 6. Rule Conflict Detection

### Conflict Analysis Matrix

| Rule ID | BR-DISCOUNT-ELIG-001 | BR-PRICING-CALC-003 | Conflict Type | Resolution |
|---------|---------------------|-------------------|--------------|-----------|
| **BR-DISCOUNT-ELIG-001** | - | Potential | Both modify price | Apply discount first, then surge pricing |
| **BR-CREDIT-ELIG-001** | None | None | None | - |
| **BR-SHIPPING-INFER-001** | None | None | None | - |

**Conflict Types**:
- **Overlapping Conditions**: Multiple rules match same input
- **Contradictory Actions**: Rules produce conflicting outputs
- **Circular Dependencies**: Rule A depends on Rule B depends on Rule A

**Resolution Strategies**:
1. **Priority-Based**: Execute highest priority rule first
2. **Sequence-Based**: Define explicit execution order
3. **Aggregate**: Combine outputs (e.g., average, min, max)
4. **Override**: Later rule overrides earlier rule

---

## 7. Rule Testing & Validation

### Test Coverage Requirements

| Rule Category | Test Cases per Rule | Coverage Target | Regression Frequency |
|--------------|-------------------|----------------|---------------------|
| Validation Rules | Minimum 5 (happy path + 4 edge cases) | 100% | Every deployment |
| Calculation Rules | Minimum 8 (boundaries, rounding, errors) | 100% | Every deployment |
| Inference Rules | Minimum 10 (all decision paths) | 95% | Weekly |
| Constraints | Minimum 6 (within/exceed limits) | 100% | Every deployment |

### Test Case Template

**Test Case ID**: TC-BR-DISCOUNT-001
**Rule Under Test**: BR-DISCOUNT-ELIG-001
**Test Type**: Boundary Value Analysis
**Test Date**: 2025-01-15
**Tester**: QA Engineer

| Input | Expected Output | Actual Output | Result |
|-------|----------------|---------------|--------|
| Order Value: $9,999, Customer: Enterprise | 10% discount | 10% discount | Pass |
| Order Value: $10,000, Customer: Enterprise | 15% discount | 15% discount | Pass |
| Order Value: $10,001, Customer: Enterprise | 15% discount | 15% discount | Pass |

---

## 8. Rule Impact Analysis

### Impact Tracking

**Rule ID**: BR-DISCOUNT-ELIG-001
**Change**: Increase Enterprise tier 1 threshold from $8,000 to $10,000

**Impacted Systems**:
- E-commerce Web Application (JavaScript)
- Mobile App (iOS, Android)
- Order Management System (Java)
- Reporting Dashboard (SQL queries)

**Impacted Processes**:
- Quote generation workflow
- Invoice calculation process
- Revenue recognition (delayed by discount changes)

**Impacted Stakeholders**:
- Finance Team (revenue forecasting)
- Sales Team (quoting)
- Customer Success (customer communication)

**Estimated Impact**:
- Affected customers: ~500 Enterprise accounts
- Revenue impact: -$120K annually (reduced discounts)
- System changes: 4 code repositories, 12 test cases

---

## 9. Regulatory Compliance Mapping

| Rule ID | Regulation | Requirement | Audit Frequency | Last Audit | Status |
|---------|-----------|-------------|----------------|-----------|--------|
| BR-CREDIT-ELIG-001 | FCRA (Fair Credit Reporting Act) | Adverse action notices for declines | Annual | 2024-11-15 | Compliant |
| BR-CREDIT-ELIG-001 | ECOA (Equal Credit Opportunity Act) | No discrimination on protected classes | Annual | 2024-11-15 | Compliant |
| BR-PRICING-CALC-003 | State Price Gouging Laws (varies) | Surge pricing caps during emergencies | As needed | 2024-08-01 | Compliant |
| BR-DISCOUNT-ELIG-001 | SOX (Sarbanes-Oxley) | Revenue recognition controls | Quarterly | 2025-01-10 | Compliant |

**Audit Trail Requirements**:
- All rule executions logged with timestamp, inputs, outputs, decision rationale
- Retention period: 7 years (SOX, FCRA)
- Access controls: Read-only for auditors, write for rule administrators

---

## 10. Rule Catalog Maintenance

### Governance & Ownership

| Activity | Frequency | Owner | Process |
|----------|-----------|-------|---------|
| **Rule Review** | Quarterly | Rule Owner | Validate rule still aligns with business needs |
| **Compliance Audit** | Annual | Compliance Officer | Verify regulatory adherence |
| **Performance Monitoring** | Monthly | Engineering Team | Track execution time, errors, usage |
| **Conflict Detection** | On change | Business Analyst | Automated conflict checker + manual review |
| **Test Suite Execution** | On change | QA Team | Regression tests for all rules |
| **Documentation Update** | On change | Business Analyst | Keep catalog current |

---

## 11. Related Artifacts

| Artifact Type | Relationship | Location |
|--------------|--------------|----------|
| **Business Process Models** | Shows where rules are applied in workflows | `/governance/business-process-models.md` |
| **System Requirements** | Technical implementation details | `/requirements/system-requirements-specification.yaml` |
| **Data Dictionary** | Defines data elements used in rules | `/data/data-dictionaries.md` |
| **API Documentation** | Rule execution endpoints | `/documentation/openapi-specification.yaml` |
| **Compliance Documentation** | Regulatory requirements | `/compliance/regulatory-mapping.md` |

---

## 12. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Business Analyst | Initial catalog with 15 core business rules |
| 0.9.0 | 2025-01-01 | Business Analyst | Draft for stakeholder review |

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | [Name] | _____________ | ______ |
| Compliance Officer | [Name] | _____________ | ______ |
| Engineering Manager | [Name] | _____________ | ______ |

---

*This Business Rules Catalog follows DMN (Decision Model and Notation) OMG standard. For questions, contact the Business Analysis team.*
