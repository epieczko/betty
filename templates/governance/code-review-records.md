# Code Review Records

> **See also**: `artifact_descriptions/code-review-records.md` for complete guidance

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

<!-- This artifact serves as comprehensive documentation of code review activities, capturing reviewer comments, defect identification, security findings, code quality assessments, and approval workflows. ... -->

## Scope

### In Scope

- Pull request/merge request review documentation (GitHub, GitLab, Bitbucket)
- Review comments taxonomy (Conventional Comments
- Security findings (OWASP Top 10, CWE vulnerabilities identified during review)
- Code quality metrics (complexity, duplication, maintainability, technical debt)
- LGTM approval criteria (functionality, security, tests, performance, documentation)

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- Software Engineers performing peer code reviews
- Engineering Managers tracking code quality metrics and review velocity
- Security Engineers reviewing security-sensitive code changes

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**PR Templates**: Implement standardized PR templates requiring description, testing approach, screenshots, breaking changes, and linked issues

**Conventional Comments**: Adopt Conventional Comments taxonomy (praise, suggestion, issue, question, thought, chore) for clear feedback categorization

**LGTM Criteria**: Define explicit approval criteria: functionality verified, security reviewed, tests added/passing, documentation updated, no performance regressions

**Review Size Limits**: Keep PRs under 400 lines of code for effective review; split larger changes into incremental PRs

**Review SLA**: Establish service-level expectations (first review within 24 hours, approval within 48 hours for non-blocking changes)

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
