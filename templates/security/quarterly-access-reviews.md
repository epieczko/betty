# Quarterly Access Reviews

> **See also**: `artifact_descriptions/quarterly-access-reviews.md` for complete guidance

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

The Quarterly Access Reviews artifact documents periodic access recertification campaigns where managers attest to the appropriateness of their direct reports' application access, privileged entitlements, and role assignments. These reviews, also called access certifications or attestations, are exe

## Purpose

This artifact serves as the evidence of periodic access validation ensuring user entitlements remain appropriate, comply with least privilege principles, and align with current job responsibilities. It detects access creep, identifies orphaned accounts, validates segregation of duties, and provides audit trails demonstrating continuous access governance.

## Scope

### In Scope

- Manager attestation of direct reports' application access
- Privileged access recertification (admin accounts, root access, production access)
- Role-based access control (RBAC) assignment validation
- Segregation of duties (SOD) conflict detection and remediation
- Orphaned account identification (terminated employees, inactive accounts)

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Quarterly Cadence Minimum**: Conduct access reviews at minimum quarterly; more frequently (monthly) for privileged and production access

**Manager Accountability**: Assign attestation responsibility to direct managers who understand business need for access, not IT teams

**Automated Campaign Launch**: Trigger review campaigns automatically via IGA platform integration with HRIS for current reporting relationships

**Risk-Based Prioritization**: Prioritize high-risk access first (privileged accounts, SOD violations, orphaned accounts) before standard user access

**Clear Attestation Questions**: Ask "Should this person still have this access?" not technical jargon about entitlements and permissions

**Remediation Deadlines**: Automatically revoke non-certified access 7-14 days after campaign deadline with clear warning notifications

**Delegated Reviews**: Allow managers to delegate attestation to senior team members for large teams, with manager final approval

**SOD Detection First**: Run SOD analysis before campaign launch to highlight conflicts requiring immediate manager attention

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
