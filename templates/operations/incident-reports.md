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

<!-- Provide a 2-3 paragraph overview for executive audience -->
<!-- What is this document about and why does it matter? -->

## Purpose

<!-- This artifact documents incident timeline, impact assessment, root cause analysis, and remediation actions following production incidents to enable blameless learning, prevent recurrence, improve MTTR... -->

## Scope

### In Scope

- Incident timeline (detection, escalation, mitigation, resolution with timestamps)
- Severity classification (SEV0/P0/Critical through SEV4/P4/Low)
- Impact assessment (users affected, revenue impact, SLO consumption, duration)
- MTTD/MTTA/MTTR metrics (Mean Time To Detect/Acknowledge/Recover)
- Root cause analysis (5 Whys, Ishikawa diagram, contributing factors)

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- SRE Teams conducting postmortems and implementing reliability improvements
- Incident Commanders reviewing incident response effectiveness
- Engineering Teams responsible for remediation action completion

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Blameless Always**: Focus on systems and processes, never blame individuals for incidents

**Timeline First**: Document detailed timeline with timestamps immediately after incident while memory is fresh

**Root Cause Depth**: Use 5 Whys or similar to find true root cause, not superficial symptoms

**Action Items Required**: Every incident must produce actionable improvement items with owners and due dates

**Track to Completion**: Follow up on all action items until completed; remediation prevents recurrence

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
