# Carbon Footprint Analysis

> **See also**: `artifact_descriptions/carbon-footprint-analysis.md` for complete guidance

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Author** | Author Name |
| **Owner** | Owner Name/Role |
| **Classification** | Internal |

## Executive Summary

The Carbon Footprint Analysis artifact quantifies greenhouse gas (GHG) emissions across Scope 1 (direct), Scope 2 (purchased energy), and Scope 3 (value chain) categories following GHG Protocol Corporate Standard, ISO 14064-1:2018, and Science Based Targets initiative (SBTi) methodologies. For techn

## Purpose

Quantifies organizational GHG emissions across Scope 1 (direct operations), Scope 2 (purchased electricity), and Scope 3 (value chain) following GHG Protocol Corporate Standard and ISO 14064-1:2018, enabling SBTi target setting, TCFD disclosures, CDP reporting, and data-driven decarbonization strategies for technology infrastructure, cloud services, and employee operations.

## Scope

### In Scope

- Scope 1 emissions from company-owned data centers (natural gas, diesel generators, refrigerants)
- Scope 2 emissions from purchased electricity (location-based and market-based methods per Scope 2 Guidance)
- Scope 3 Category 1
- Scope 3 Category 3
- Scope 3 Category 5

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Organizational Boundaries**: Apply operational control approach (GHG Protocol) consistently; document organizational boundary methodology annually per ISO 14064-1:2018 Section 5

**Data Quality Tiers**: Prioritize primary data (utility bills, fuel receipts) over secondary (industry averages); achieve 80%+ primary data coverage for Scope 1+2 per GHG Protocol quality standards

**Market-Based Scope 2**: Calculate both location-based (grid average) and market-based (contractual instruments like RECs, PPAs) methods per Scope 2 Guidance dual reporting requirement

**Scope 3 Materiality Screening**: Conduct annual materiality assessment across all 15 categories; focus detailed tracking on categories >5% total emissions per Corporate Value Chain Standard

**Emission Factors**: Use region-specific factors (IEA, EPA eGRID, DEFRA) updated annually; document factor sources and vintages for audit trail and year-over-year comparability

**Cloud Provider APIs**: Integrate AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint, Azure Emissions Impact Dashboard for automated Scope 3 Category 11 tracking

**PUE Measurement**: Calculate Power Usage Effectiveness monthly per The Green Grid methodology; target PUE <1.2 for hyperscale data centers, <1.5 for enterprise facilities

**SBTi Alignment**: Set near-term (5-10 year) and net-zero (2050) targets following SBTi Corporate Net-Zero Standard v1.1; validate targets through SBTi submission process

## Related Documents

- [Related Artifact]: Relationship description

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
