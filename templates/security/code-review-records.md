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

The Code Review Records artifact documents systematic peer review activities for source code changes, capturing review comments, security findings, quality metrics, and approval decisions aligned with Google Code Review Guidelines, Conventional Comments taxonomy, and pull request best practices. Thi

## Purpose

This artifact serves as comprehensive documentation of code review activities, capturing reviewer comments, defect identification, security findings, code quality assessments, and approval workflows. It provides auditable evidence of peer review compliance, supports knowledge sharing, enables defect trend analysis, and demonstrates adherence to LGTM (Looks Good To Me) criteria including functional

## Scope

### In Scope

- Pull request/merge request review documentation (GitHub, GitLab, Bitbucket)
- Review comments taxonomy (Conventional Comments
- Security findings (OWASP Top 10, CWE vulnerabilities identified during review)
- Code quality metrics (complexity, duplication, maintainability, technical debt)
- LGTM approval criteria (functionality, security, tests, performance, documentation)

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**PR Templates**: Implement standardized PR templates requiring description, testing approach, screenshots, breaking changes, and linked issues

**Conventional Comments**: Adopt Conventional Comments taxonomy (praise, suggestion, issue, question, thought, chore) for clear feedback categorization

**LGTM Criteria**: Define explicit approval criteria: functionality verified, security reviewed, tests added/passing, documentation updated, no performance regressions

**Review Size Limits**: Keep PRs under 400 lines of code for effective review; split larger changes into incremental PRs

**Review SLA**: Establish service-level expectations (first review within 24 hours, approval within 48 hours for non-blocking changes)

**Security-Focused Review**: Require dedicated security review for authentication, authorization, cryptography, input validation, and sensitive data handling code

**CODEOWNERS**: Implement CODEOWNERS file for automatic reviewer assignment based on file paths (security team for auth/* files)

**Required Reviewers**: Mandate minimum 2 reviewers for production code; 1 must be senior engineer or security engineer for security-sensitive changes

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
