# Release Risk Assessment

> **See also**: `artifact_descriptions/release-risk-assessment.md` for complete guidance

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

<!-- Provide a 2-3 paragraph overview for executive audience -->
<!-- What is this document about and why does it matter? -->

## Purpose

<!-- Release risk assessment systematically evaluates potential failure modes, estimates impact severity, calculates likelihood, defines mitigation strategies, and establishes rollback criteria for product... -->

## Scope

### In Scope

- FMEA risk scoring (Severity x Likelihood x Detection) for technical, operational, security, business risks
- Pre-mortem analysis identifying potential failure scenarios before deployment
- Blast radius estimation (percentage of users affected, services impacted, revenue at risk)
- Rollback criteria definition (automated triggers, manual decision thresholds, success metrics)
- Mean Time to Recovery (MTTR) estimation for various failure scenarios

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- Release Managers evaluating risk vs. business value tradeoffs and deployment timing
- SRE Teams assessing operational risks, recovery procedures, and monitoring adequacy
- Change Advisory Board (CAB) members making approval decisions based on risk profile

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**FMEA Scoring Consistency**: Use standardized scoring scales (1-10) for Severity, Likelihood, Detection to enable risk comparison

**Pre-Mortem Facilitation**: Conduct collaborative pre-mortem sessions with engineering, SRE, security, and product teams

**Quantify Blast Radius**: Estimate specific percentages (e.g., "affects 15% of users", "impacts $50K/hour revenue") not vague terms

**Define Measurable Rollback Triggers**: Specify objective thresholds (error rate > 5%, p95 latency > 500ms, 10 customer complaints)

**Risk Mitigation Accountability**: Assign owners and completion dates for each mitigation action

## Quality Checklist

Before finalizing this artifact, verify:

- [ ] **Completeness**: All required sections present and adequately detailed
- [ ] **Accuracy**: Information verified and validated by appropriate subject matter experts
- [ ] **Clarity**: Written in clear, unambiguous language appropriate for intended audience
- [ ] **Consistency**: Aligns with organizational standards, templates, and related artifacts
- [ ] **Currency**: Based on current information; outdated content removed or updated

## Related Documents

- [Related Artifact]: Description and relationship

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | Name | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
