# ROI Model (Return on Investment)

**Document Version**: 1.0.0
**Last Updated**: 2025-01-15
**Document Owner**: Finance & FP&A Team
**Classification**: Confidential

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ROI-CLOUD-MIGRATION-2025 |
| **Investment Name** | Cloud Migration & Platform Modernization |
| **Status** | Approved |
| **Created Date** | 2024-12-01 |
| **Analysis Date** | 2025-01-15 |
| **Primary Author** | Senior Financial Analyst |
| **Approvers** | CFO, CTO, CEO |
| **Investment Committee Decision** | Approved - 2025-01-20 |

## Executive Summary

This ROI Model provides comprehensive financial analysis for the Cloud Migration & Platform Modernization initiative using industry-standard metrics including Net Present Value (NPV), Internal Rate of Return (IRR), payback period, and sensitivity analysis. This analysis supports capital allocation decisions and demonstrates expected value creation of $8.2M NPV over 5 years with 42% IRR.

**Investment Request**: $3.5M (CapEx + OpEx over 2 years)
**Expected Return**: $11.7M total value over 5 years
**Net Present Value (NPV)**: $8.2M (@ 10% WACC)
**Internal Rate of Return (IRR)**: 42%
**Payback Period**: 2.3 years
**Recommendation**: Approve - Strong financial returns, strategic alignment, acceptable risk

---

## 1. Investment Overview

### Business Case Summary

**Strategic Objective**: Migrate from on-premise data centers to AWS cloud infrastructure to improve scalability, reliability, and developer velocity while reducing operational costs.

**Current State Pain Points**:
- Data center lease expires in 18 months ($500K/year)
- Infrastructure at capacity; can't scale to support growth
- Deployment cycles averaging 2 weeks (vs. industry best practice of hours/days)
- 99.5% uptime (target: 99.9% for enterprise customers)
- Security compliance gaps (SOC 2 Type II required for enterprise sales)

**Proposed Solution**:
- Migrate all workloads to AWS (EC2, RDS, S3, Lambda)
- Implement Infrastructure-as-Code (Terraform)
- Establish CI/CD pipelines (GitHub Actions, ArgoCD)
- Multi-region active-active architecture
- Achieve SOC 2 Type II certification

**Success Criteria**:
- 100% workload migration by Q4 2025
- 99.9%+ uptime SLA achieved
- Deployment frequency increased to daily
- $1.2M annual OpEx savings realized
- SOC 2 Type II certification obtained

---

## 2. Financial Assumptions

### Key Assumptions

| Category | Assumption | Source | Confidence |
|----------|-----------|--------|-----------|
| **Discount Rate (WACC)** | 10% | CFO-approved hurdle rate | High |
| **Analysis Period** | 5 years (2025-2029) | Standard for infrastructure investments | High |
| **Cloud Cost Growth** | 15% annually | AWS pricing trends + usage growth | Medium |
| **Revenue Growth** | 25% annually | Sales forecast (conservative) | Medium |
| **Inflation** | 3% annually | Federal Reserve projections | High |
| **Tax Rate** | 21% | Corporate tax rate | High |
| **Implementation Timeline** | 18 months (Q1 2025 - Q2 2026) | Engineering estimate | Medium |

### Cost Assumptions

**One-Time Costs** (CapEx Treatment):
- Migration labor (engineering, consulting): $1.2M
- Software licenses (Terraform Enterprise, monitoring tools): $300K
- Training and enablement: $150K
- SOC 2 audit and certification: $200K
- **Total One-Time**: $1.85M

**Recurring Costs** (OpEx):
- AWS infrastructure (compute, storage, networking): $800K/year (Year 1) → $1.2M/year (Year 5)
- Monitoring and observability tools (Datadog): $120K/year
- Support and maintenance: $80K/year
- **Total Annual OpEx** (Year 1): $1.0M

### Benefits Assumptions

**Cost Savings**:
- Data center elimination: $500K/year (lease + utilities)
- Reduced headcount (datacenter ops): $300K/year (2 FTEs)
- Software licensing savings (legacy monitoring): $100K/year
- **Total Annual Savings**: $900K/year

**Revenue Enablers**:
- Enterprise deals unlocked (SOC 2): $2M ARR in Year 2, $5M by Year 5
- Reduced downtime (99.9% vs 99.5%): $200K/year avoided revenue loss
- Faster time-to-market: $500K/year in competitive advantage

**Productivity Gains**:
- Developer velocity (10 hrs/week/engineer x 20 engineers): $520K/year

---

## 3. Financial Projections (5-Year Cashflow)

### Detailed Cashflow Analysis

| Year | 2025 | 2026 | 2027 | 2028 | 2029 |
|------|------|------|------|------|------|
| **REVENUE IMPACT** |  |  |  |  |  |
| Enterprise ARR (SOC 2) | $0 | $2,000K | $3,500K | $4,500K | $5,000K |
| Reduced Downtime Revenue Loss | $100K | $200K | $200K | $200K | $200K |
| Faster Time-to-Market | $250K | $500K | $600K | $700K | $800K |
| **Total Revenue Impact** | **$350K** | **$2,700K** | **$4,300K** | **$5,400K** | **$6,000K** |
|  |  |  |  |  |  |
| **COST SAVINGS** |  |  |  |  |  |
| Data Center Elimination | $250K | $500K | $500K | $500K | $500K |
| Reduced Headcount (Ops) | $150K | $300K | $300K | $300K | $300K |
| Legacy Software Savings | $50K | $100K | $100K | $100K | $100K |
| **Total Cost Savings** | **$450K** | **$900K** | **$900K** | **$900K** | **$900K** |
|  |  |  |  |  |  |
| **GROSS BENEFITS** | **$800K** | **$3,600K** | **$5,200K** | **$6,300K** | **$6,900K** |
|  |  |  |  |  |  |
| **COSTS** |  |  |  |  |  |
| One-Time Costs (CapEx) | ($1,500K) | ($350K) | $0 | $0 | $0 |
| AWS Infrastructure (OpEx) | ($800K) | ($920K) | ($1,058K) | ($1,217K) | ($1,399K) |
| Monitoring Tools | ($120K) | ($124K) | ($128K) | ($131K) | ($135K) |
| Support & Maintenance | ($80K) | ($82K) | ($85K) | ($87K) | ($90K) |
| **Total Costs** | **($2,500K)** | **($1,476K)** | **($1,271K)** | **($1,435K)** | **($1,624K)** |
|  |  |  |  |  |  |
| **NET CASH FLOW** | **($1,700K)** | **$2,124K** | **$3,929K** | **$4,865K** | **$5,276K** |
| **Cumulative Cash Flow** | ($1,700K) | $424K | $4,353K | $9,218K | $14,494K |

**Note**: Costs inflated at 3% annually; cloud costs grow at 15% due to usage scale.

---

## 4. ROI Metrics & Analysis

### Net Present Value (NPV)

**Calculation**:
```
NPV = Σ [CF_t / (1 + WACC)^t] - Initial Investment

Where:
  CF_t = Net cash flow in year t
  WACC = 10% (weighted average cost of capital)
  t = Year (0-5)
```

**NPV Calculation**:

| Year | Net Cash Flow | Discount Factor (10%) | Present Value |
|------|--------------|----------------------|--------------|
| 2025 | ($1,700K) | 1.000 | ($1,700K) |
| 2026 | $2,124K | 0.909 | $1,931K |
| 2027 | $3,929K | 0.826 | $3,245K |
| 2028 | $4,865K | 0.751 | $3,654K |
| 2029 | $5,276K | 0.683 | $3,603K |
| **Total NPV** |  |  | **$8,733K** |

**Result**: **NPV = $8.7M** (positive → project creates value)

---

### Internal Rate of Return (IRR)

**Definition**: Discount rate at which NPV = 0 (break-even discount rate)

**Calculation**:
Using Excel/financial calculator: IRR = 42%

**Interpretation**:
- IRR (42%) > WACC (10%) → Project exceeds hurdle rate
- High IRR indicates strong returns relative to cost of capital
- 42% IRR is well above typical technology infrastructure IRR benchmarks (15-25%)

---

### Payback Period

**Definition**: Time required to recover initial investment

**Calculation**:

| Year | Cumulative Cash Flow |
|------|---------------------|
| 2025 | ($1,700K) |
| 2026 | $424K |
| 2027 | $4,353K |

**Payback occurs between Year 2 and Year 3**:
- Cumulative CF at end of Year 2: $424K
- Year 3 annual CF: $3,929K
- Months into Year 3 to payback: ($1,700K - $424K) / ($3,929K / 12) ≈ 3.9 months

**Payback Period**: **2.3 years** (within typical 3-year requirement for infrastructure investments)

---

### Profitability Index (PI)

**Definition**: Ratio of PV of benefits to initial investment

**Calculation**:
```
PI = NPV + Initial Investment / Initial Investment
PI = $8,733K / $1,850K = 4.72
```

**Result**: **PI = 4.72** (every $1 invested returns $4.72 in present value)

**Interpretation**: PI > 1.0 indicates value creation; PI of 4.72 is excellent

---

## 5. Sensitivity Analysis

### One-Way Sensitivity (± 20%)

**Impact on NPV**:

| Variable | -20% | Base Case | +20% | NPV Range |
|----------|------|-----------|------|-----------|
| **Revenue Impact** | $6,987K | $8,733K | $10,479K | $3,492K |
| **Cost Savings** | $8,013K | $8,733K | $9,453K | $1,440K |
| **Implementation Costs** | $9,103K | $8,733K | $8,363K | $740K |
| **Cloud Costs (OpEx)** | $9,329K | $8,733K | $8,137K | $1,192K |
| **Discount Rate (WACC)** | $10,249K | $8,733K | $7,441K | $2,808K |

**Key Insights**:
- NPV most sensitive to revenue impact (+/- $3.5M swing)
- NPV remains positive even in worst-case scenarios (-20% benefits, +20% costs)
- Discount rate sensitivity moderate (-$1.3M at 12% WACC)

---

### Scenario Analysis

#### Scenario 1: Best Case (P90)

**Assumptions**:
- Enterprise adoption exceeds forecast (+30%)
- Cloud costs lower than expected (-15%)
- Faster implementation (12 months vs. 18)

**Results**:
- NPV: $12.8M (+47% vs. base case)
- IRR: 58%
- Payback: 1.9 years

---

#### Scenario 2: Base Case (P50) - Approved Forecast

**Results** (as calculated above):
- NPV: $8.7M
- IRR: 42%
- Payback: 2.3 years

---

#### Scenario 3: Worst Case (P10)

**Assumptions**:
- Enterprise adoption slow (-30%)
- Cloud costs higher than expected (+25%)
- Implementation delays (24 months)

**Results**:
- NPV: $4.1M (still positive)
- IRR: 24%
- Payback: 3.5 years

**Risk Assessment**: Even in worst case, project delivers positive NPV and IRR > WACC

---

## 6. Risk Analysis & Mitigation

### Key Risks

| Risk | Probability | Impact | Mitigation Strategy | Risk-Adjusted Impact |
|------|-----------|--------|---------------------|---------------------|
| **Implementation delays** (>18 months) | 30% | -$800K NPV | Experienced consulting partner; phased migration | -$240K |
| **Cloud cost overruns** (+30%) | 25% | -$1.2M NPV | Reserved instances; strict cost monitoring | -$300K |
| **Enterprise sales slower than forecast** | 40% | -$2M NPV | Conservative forecast (only SOC 2 impact) | -$800K |
| **Data migration failures** | 15% | -$500K NPV | Pilot migration; comprehensive testing | -$75K |
| **Key personnel attrition** | 20% | -$400K NPV | Knowledge transfer; consulting support | -$80K |

**Total Risk-Adjusted NPV**: $8,733K - $1,495K = **$7,238K**

**Conclusion**: Even with risk adjustment, NPV remains strongly positive.

---

## 7. Break-Even Analysis

### NPV Break-Even Points

**Question**: How much can assumptions change before NPV = 0?

| Variable | Base Case | Break-Even Point | % Change Allowed |
|----------|-----------|-----------------|-----------------|
| **Revenue Impact** | $4.6M (avg/year) | $2.1M/year | -54% |
| **Cost Savings** | $900K/year | $400K/year | -56% |
| **Implementation Costs** | $1.85M | $4.2M | +127% |
| **Cloud OpEx** | $1.0M/year (Year 1) | $2.3M/year | +130% |

**Interpretation**: Project has significant margin of safety. Benefits would need to drop by >50% or costs double before NPV turns negative.

---

## 8. Comparison to Alternatives

### Alternative 1: Do Nothing (Status Quo)

**Costs**:
- Data center renewal: $600K/year (10% increase)
- Continued ops headcount: $300K/year
- Lost enterprise revenue: $5M/year (no SOC 2)
- Competitive disadvantage: $500K/year

**5-Year NPV**: **-$12.5M** (opportunity cost)

---

### Alternative 2: Hybrid Cloud (Partial Migration)

**Investment**: $2.2M
**Benefits**: $8.5M over 5 years
**NPV**: $5.8M (@ 10% WACC)
**IRR**: 31%

**Comparison**: Lower NPV than full migration; doesn't solve data center expiration

---

### Alternative 3: On-Premise Refresh

**Investment**: $4.5M (new hardware, data center renewal)
**Benefits**: $4.2M over 5 years (cost avoidance only)
**NPV**: -$1.2M (@ 10% WACC)
**IRR**: 8% (below WACC)

**Conclusion**: Not financially viable; doesn't enable enterprise growth

---

## 9. Value Realization Tracking

### Quarterly Milestones & KPIs

| Quarter | Milestone | Success Metric | Target | Actual | Status |
|---------|-----------|---------------|--------|--------|--------|
| **Q1 2025** | AWS account setup, architecture design | Design complete | 100% | 100% | ✅ Complete |
| **Q2 2025** | Pilot migration (dev/staging environments) | 25% workloads migrated | 25% | 20% | 🟡 On track |
| **Q3 2025** | Production migration Phase 1 (non-critical) | 50% workloads migrated | 50% | TBD | ⏳ Pending |
| **Q4 2025** | Production migration Phase 2 (critical) | 90% workloads migrated | 90% | TBD | ⏳ Pending |
| **Q1 2026** | Data center decommissioned, SOC 2 audit | 100% migration, SOC 2 Type II | 100% | TBD | ⏳ Pending |

### Benefits Tracking

| Benefit | Q1 2026 Target | Measurement Method | Owner |
|---------|---------------|-------------------|-------|
| **Enterprise ARR** | $2M | Salesforce closed-won deals (SOC 2-contingent) | CRO |
| **Uptime SLA** | 99.9% | Datadog uptime monitoring | VP Engineering |
| **Deployment Frequency** | 5x/week | GitHub Actions deployment logs | Engineering |
| **Data Center Savings** | $500K/year | Finance actuals (lease termination confirmed) | CFO |
| **Cloud OpEx** | <$1.2M/year | AWS Cost Explorer monthly spend | FinOps Team |

---

## 10. Governance & Approvals

### Investment Committee Decision

**Meeting Date**: 2025-01-20
**Decision**: **Approved**
**Vote**: Unanimous (6-0)

**Approvals**:

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| **CFO** | Jane Smith | ___________ | 2025-01-20 | Strong NPV and IRR; approve with quarterly review |
| **CTO** | Bob Johnson | ___________ | 2025-01-20 | Critical for enterprise strategy; engineering ready |
| **CEO** | Alice Williams | ___________ | 2025-01-20 | Approve; strategic priority for 2025 |
| **VP Finance** | Tom Brown | ___________ | 2025-01-20 | Financial analysis validated; conservative assumptions |

**Conditions of Approval**:
1. Quarterly investment committee check-ins on progress and spend
2. Hard cap on total investment at $4.0M (15% buffer)
3. Go/No-Go decision at 50% migration milestone (Q3 2025)
4. CFO sign-off required for any cloud vendor changes

---

## 11. Post-Implementation Review Plan

### 12-Month Post-Launch Review (Q1 2027)

**Review Questions**:
1. Did we achieve target NPV? (compare actual benefits vs. forecast)
2. Were costs within budget? (+/- 10% acceptable variance)
3. Did we achieve target milestones on schedule?
4. What surprised us? (positive and negative)
5. What would we do differently?

**Success Criteria**:
- NPV actual within 20% of forecast: $7M - $10.5M
- IRR actual > 35%
- 90%+ of benefits realized by end of Year 2

---

## 12. Related Artifacts

| Artifact Type | Relationship | Location |
|--------------|--------------|----------|
| **Business Case** | Strategic justification for this investment | `/governance/business-case.md` |
| **Technical Design** | Implementation approach and architecture | `/architecture/cloud-migration-design.md` |
| **Project Charter** | Governance and execution plan | `/governance/initiative-charter.md` |
| **Risk Register** | Detailed risk assessment | `/governance/raid-log.md` |
| **Benefits Realization Plan** | Post-implementation tracking | `/governance/benefits-realization-plan.md` |

---

## 13. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Senior Financial Analyst | Final version for investment committee |
| 0.9.0 | 2025-01-05 | Senior Financial Analyst | Draft with sensitivity analysis |
| 0.8.0 | 2024-12-15 | Senior Financial Analyst | Initial draft with NPV/IRR calculations |

---

## Appendix A: Financial Calculation Details

### DCF Model Formulas

**Net Present Value**:
```
NPV = Σ [CF_t / (1 + r)^t] for t = 0 to n

Where:
  CF_t = Net cash flow in period t
  r = Discount rate (WACC)
  t = Time period
  n = Total number of periods
```

**Internal Rate of Return**:
```
0 = Σ [CF_t / (1 + IRR)^t] for t = 0 to n

Solve for IRR using iterative methods (Excel XIRR function)
```

**Payback Period**:
```
Payback = Year when Cumulative CF turns positive

Precise calculation:
  Payback = Last negative year + |Cumulative CF| / Next year CF
```

---

## Appendix B: Assumptions Validation

| Assumption | Validation Source | Confidence Level | Sensitivity |
|-----------|------------------|------------------|------------|
| WACC 10% | CFO-approved corporate hurdle rate | High | Medium impact |
| AWS costs | AWS pricing calculator + 3 vendor quotes | Medium | Medium impact |
| Enterprise revenue | Sales pipeline analysis (CRM data) | Medium | High impact |
| Implementation timeline | Engineering capacity planning + consulting estimate | Medium | Low impact |
| Productivity gains | Developer survey + time-motion study | Low | Low impact |

---

**Final Recommendation**: **APPROVE** - Project delivers strong financial returns ($8.7M NPV, 42% IRR) with acceptable risk profile and strategic alignment to enterprise growth objectives.

---

*This ROI Model follows FP&A best practices and incorporates discounted cash flow (DCF) analysis, sensitivity testing, and risk-adjusted returns. For questions, contact the Finance team.*
