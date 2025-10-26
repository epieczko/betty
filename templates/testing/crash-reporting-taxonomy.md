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

The Crash Reporting Taxonomy is a structured classification system that standardizes crash categorization, severity assignment, and metadata capture across mobile, web, and backend applications. This taxonomy ensures consistent crash analysis using platforms like Sentry, Bugsnag, Crashlytics, or Rol

## Purpose

Establishes a unified taxonomy for classifying application crashes, errors, and exceptions across all platforms to enable consistent reporting, prioritization, and remediation tracking using crash monitoring tools.

## Scope

### In Scope

- Mobile crash classification (iOS, Android native crashes, ANR, OOM errors)
- Web application errors (JavaScript exceptions, unhandled promise rejections, network failures)
- Backend service crashes (uncaught exceptions, segmentation faults, OOM kills, panic conditions)
- Crash severity levels with clear user impact definitions (P0
- Error fingerprinting rules for deduplication and grouping

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Severity Standardization**: Define P0 (launch blocker), P1 (core feature failure), P2 (degraded experience), P3 (minor issue) with explicit user impact criteria

**Crash-Free Rate Targets**: Maintain >99.5% crash-free sessions for production; >98% for beta releases

**Fingerprinting Consistency**: Use stable error fingerprints combining exception type, file path, and function name (avoid line numbers)

**Symbolication Requirements**: Upload symbols within 1 hour of release to enable readable stack traces

**Grouping Intelligence**: Configure smart grouping to cluster similar crashes while avoiding over-aggregation

**Platform-Specific Classification**: Separate iOS signal crashes (SIGSEGV, SIGABRT) from Android JNI crashes and JavaScript exceptions

**Breadcrumb Taxonomy**: Standardize breadcrumb categories (navigation, network, user input, state changes) for context

**User Impact Metrics**: Track affected users, not just crash count (10 users with 100 crashes > 100 users with 10 crashes)

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
