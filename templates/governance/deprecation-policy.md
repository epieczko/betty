# Deprecation Policy

> **See also**: `artifact_descriptions/deprecation-policy.md` for complete guidance

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

<!-- This policy establishes mandatory procedures for deprecating software components (APIs, features, libraries, services, infrastructure), defining timeline requirements, communication protocols, migrati... -->

## Scope

### In Scope

- Public API deprecation
- SDK/library deprecation
- Feature deprecation
- Service deprecation
- Protocol/standard deprecation

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- Engineering Leadership: Deprecation roadmap planning, resource allocation for migration support, technical debt prioritization
- Platform/API Teams: Deprecation timeline enforcement, versioning strategy, backward compatibility maintenance
- Product Management: Customer communication planning, feature sunset decisions, migration effort estimation

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Tiered Timeline Model**: Use 6-month minimum for internal APIs, 12-month for public APIs, 24+ months for critical infrastructure/protocols

**SemVer Compliance**: Increment MAJOR version for breaking changes; use MINOR for deprecation warnings with continued support

**Sunset HTTP Header**: Implement RFC 8594 Sunset header returning deprecation date in HTTP responses for automated detection

**Multi-Phase Rollout**: (1) Deprecation announcement, (2) Warning phase with logs, (3) Error phase, (4) Removal phase

**Usage Telemetry**: Instrument deprecated endpoints/features to track adoption of replacements before final sunset

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
