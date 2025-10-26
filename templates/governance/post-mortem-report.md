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

The Post-Mortem Report is a comprehensive incident review document that captures what happened, why it happened, how it was resolved, and what actions will prevent recurrence. Following the blameless postmortem culture pioneered by Google SRE and Etsy, this artifact transforms production incidents i

## Purpose

This artifact documents production incidents through comprehensive, blameless analysis including detailed timelines, root causes, impact metrics, and actionable remediation plans. It transforms failure into organizational learning by systematically capturing what went wrong, why it went wrong, and how to prevent recurrence, while fostering a culture of psychological safety and continuous improveme

## Scope

### In Scope

- Incident overview and severity classification (P0/SEV0 through P3/SEV3)
- Detailed timeline with UTC timestamps (detection, acknowledgment, escalation, mitigation, resolution)
- Impact quantification (MTTR, MTTA, customers affected, revenue loss, error budget burn)
- Root cause analysis using 5 Whys, Fishbone, or Fault Tree Analysis
- Contributing factors across people/process/technology dimensions

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Blameless Culture**: Explicitly state "this is a blameless post-mortem" at the start; focus on systems, not individuals

**Timely Completion**: Publish post-mortem within 48-72 hours while details are fresh; don't wait weeks

**Precise Timeline**: Use UTC timestamps accurate to minutes; include detection, acknowledgment, escalation, mitigation, resolution

**Quantify Impact**: Always include MTTR, customers affected, error budget burn; use data, not vague estimates

**Honest Assessment**: Document both successes and failures; "what went well" is as important as "what went poorly"

**Root Cause Focus**: Apply 5 Whys or Fishbone; don't stop at symptoms; identify fundamental causes

**Actionable Items**: Every action item must have owner, deadline, and success criteria (SMART)

**Categorize Actions**: Separate immediate fixes (done), short-term (30 days), long-term (90+ days)

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
