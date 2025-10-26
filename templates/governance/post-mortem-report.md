# Post Mortem Report

> **See also**: `artifact_descriptions/post-mortem-report.md` for complete guidance

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

<!-- This artifact documents production incidents through comprehensive, blameless analysis including detailed timelines, root causes, impact metrics, and actionable remediation plans. It transforms failur... -->

## Scope

### In Scope

- Incident overview and severity classification (P0/SEV0 through P3/SEV3)
- Detailed timeline with UTC timestamps (detection, acknowledgment, escalation, mitigation, resolution)
- Impact quantification (MTTR, MTTA, customers affected, revenue loss, error budget burn)
- Root cause analysis using 5 Whys, Fishbone, or Fault Tree Analysis
- Contributing factors across people/process/technology dimensions

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- SRE Teams conducting and learning from post-mortem analysis
- Incident Commanders documenting incident response and coordination
- Engineering Teams implementing remediation actions

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Blameless Culture**: Explicitly state "this is a blameless post-mortem" at the start; focus on systems, not individuals

**Timely Completion**: Publish post-mortem within 48-72 hours while details are fresh; don't wait weeks

**Precise Timeline**: Use UTC timestamps accurate to minutes; include detection, acknowledgment, escalation, mitigation, resolution

**Quantify Impact**: Always include MTTR, customers affected, error budget burn; use data, not vague estimates

**Honest Assessment**: Document both successes and failures; "what went well" is as important as "what went poorly"

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
