# Incident Reports

> **See also**: `artifact_descriptions/incident-reports.md` for complete guidance

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

Incident Reports document the timeline, root cause analysis, impact assessment, and remediation actions for production incidents and outages. These reports are essential for conducting blameless postmortems, improving MTTR, preventing recurrence, and maintaining SRE and ITIL 4 incident management be

## Purpose

This artifact documents incident timeline, impact assessment, root cause analysis, and remediation actions following production incidents to enable blameless learning, prevent recurrence, improve MTTR, and maintain compliance with incident management best practices.

## Scope

### In Scope

- Incident timeline (detection, escalation, mitigation, resolution with timestamps)
- Severity classification (SEV0/P0/Critical through SEV4/P4/Low)
- Impact assessment (users affected, revenue impact, SLO consumption, duration)
- MTTD/MTTA/MTTR metrics (Mean Time To Detect/Acknowledge/Recover)
- Root cause analysis (5 Whys, Ishikawa diagram, contributing factors)

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Blameless Always**: Focus on systems and processes, never blame individuals for incidents

**Timeline First**: Document detailed timeline with timestamps immediately after incident while memory is fresh

**Root Cause Depth**: Use 5 Whys or similar to find true root cause, not superficial symptoms

**Action Items Required**: Every incident must produce actionable improvement items with owners and due dates

**Track to Completion**: Follow up on all action items until completed; remediation prevents recurrence

**Measure MTTR**: Track MTTD, MTTA, MTTR metrics to identify response improvement opportunities

**SLO Impact**: Document error budget consumption and SLI degradation during incidents

**Communicate Early**: Notify stakeholders immediately; transparency builds trust during incidents

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
