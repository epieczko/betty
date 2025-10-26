# On Call Handbook

> **See also**: `artifact_descriptions/on-call-handbook.md` for complete guidance

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

<!-- This artifact serves as the authoritative reference for all on-call operations, defining rotation schedules, escalation policies, SLA response times, handoff procedures, and support expectations. It s... -->

## Scope

### In Scope

- On-call rotation schedules (primary, secondary, tertiary) across teams and time zones
- Escalation policies and paths (L1 → L2 → L3 → management → executive)
- SLA response time requirements by severity level (P0/SEV0
- Shift handoff procedures, handoff checklists, and knowledge transfer protocols
- Integration with alerting platforms (PagerDuty, Opsgenie, VictorOps, xMatters)

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- On-Call Engineers actively participating in rotation schedules
- SRE Teams responsible for production system reliability
- Incident Commanders coordinating major incident response

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Rotation Fairness**: Distribute on-call burden equitably across team members; use metrics to track rotation balance and alert fatigue

**Clear Escalation Paths**: Define explicit L1 → L2 → L3 → management escalation chains with specific trigger criteria for each level

**SLA-Based Response Times**: Enforce response time commitments based on incident severity (P0: 15min, P1: 1hr, P2: 4hrs, P3: next business day)

**Shift Handoff Rituals**: Conduct structured handoffs with written summaries of ongoing incidents, pending alerts, and system status

**Runbook Integration**: Link common alert types to specific troubleshooting runbooks and automated remediation playbooks

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
