# Crash Reporting Taxonomy

> **See also**: `artifact_descriptions/crash-reporting-taxonomy.md` for complete guidance

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

<!-- Establishes a unified taxonomy for classifying application crashes, errors, and exceptions across all platforms to enable consistent reporting, prioritization, and remediation tracking using crash mon... -->

## Scope

### In Scope

- Mobile crash classification (iOS, Android native crashes, ANR, OOM errors)
- Web application errors (JavaScript exceptions, unhandled promise rejections, network failures)
- Backend service crashes (uncaught exceptions, segmentation faults, OOM kills, panic conditions)
- Crash severity levels with clear user impact definitions (P0
- Error fingerprinting rules for deduplication and grouping

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- Mobile developers (iOS, Android) classifying and triaging crashes
- Web frontend developers handling JavaScript errors and exceptions
- Backend engineers investigating service crashes and panics

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Severity Standardization**: Define P0 (launch blocker), P1 (core feature failure), P2 (degraded experience), P3 (minor issue) with explicit user impact criteria

**Crash-Free Rate Targets**: Maintain >99.5% crash-free sessions for production; >98% for beta releases

**Fingerprinting Consistency**: Use stable error fingerprints combining exception type, file path, and function name (avoid line numbers)

**Symbolication Requirements**: Upload symbols within 1 hour of release to enable readable stack traces

**Grouping Intelligence**: Configure smart grouping to cluster similar crashes while avoiding over-aggregation

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
