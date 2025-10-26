# Requirements Traceability Matrix (RTM)
<!-- See also: artifact_descriptions/requirements-traceability-matrix.md for complete guidance -->
<!-- YAML version available at: requirements-traceability-matrix.yaml -->

## Document Information

**Project**: [Project Name]
**Version**: 1.0.0
**Created**: YYYY-MM-DD
**Last Modified**: YYYY-MM-DD
**Status**: Draft | Review | Approved
**Author**: [Author Name - Requirements Lead]
**Document Owner**: [Product Management]
**Classification**: Internal - Confidential

### Approvers

| Name | Role | Date | Status |
|------|------|------|--------|
| [Product Director] | Product Director | YYYY-MM-DD | Pending |

---

## Purpose

The Requirements Traceability Matrix (RTM) provides **bidirectional traceability** following IEEE 29148 standards, linking business needs through user stories, requirements, design elements, implementation (code), and test cases. This ensures:

- **Complete coverage**: Every business need has corresponding requirements and tests
- **Impact analysis**: Identify all artifacts affected by requirement changes
- **Compliance**: Demonstrate requirement satisfaction for regulatory audits
- **Orphan detection**: Identify requirements without tests or tests without requirements
- **Change management**: Track suspect links when requirements or designs change

**YAML Version**: For structured data and automated queries, use `requirements-traceability-matrix.yaml`.

---

## Traceability Coverage Metrics

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Business Needs | 12 | - |
| Total User Stories | 48 | - |
| Total Requirements | 127 | - |
| Total Design Elements | 89 | - |
| Total Test Cases | 342 | - |
| **Coverage Metrics** | | |
| Requirements with Tests | 124/127 | 97.6% |
| Tests with Requirements | 338/342 | 98.8% |
| Orphaned Requirements | 3 | - |
| Orphaned Tests | 4 | - |
| Suspect Links | 7 | - |

### Test Coverage by MoSCoW Priority

| Priority | Requirements | With Tests | Coverage |
|----------|--------------|------------|----------|
| Must Have (Critical) | 94 | 94 | 100% |
| Should Have (High) | 23 | 22 | 95.7% |
| Could Have (Medium) | 7 | 5 | 71.4% |
| Won't Have | 3 | 3 | 100% |

---

## Traceability Chain Example

### Business Need → User Story → Requirement → Design → Code → Test

**BN-001**: Enable instant person-to-person payments to improve customer engagement
- **Measurable Goal**: Increase app DAU by 25%, achieve 1M P2P transactions/month
- **Stakeholder**: Product Management, Marketing

└── **US-010**: As a mobile banking user, I want to send money to friends instantly
    - **Epic**: EP-003: Peer-to-Peer Payments

    └── **REQ-P2P-001**: System shall allow users to send money via mobile number or email
        - **Type**: Functional
        - **Priority**: Must Have

        └── **DESIGN-P2P-01**: P2P Payment Service API
            - **Artifact**: `architecture/p2p-payment-service.md`
            - **Type**: Component Design

            └── **CODE-P2P-01**: PaymentService Implementation
                - **Module**: `com.bank.p2p.PaymentService`
                - **Files**: PaymentService.java, PaymentRepository.java, PaymentController.java
                - **PR**: #1247 (Merged)

                └── **TC-P2P-001**: Verify user can send $50 to recipient via mobile number
                    - **Type**: Integration Test
                    - **Automation**: Automated (Postman/Newman)
                    - **Status**: Passed
                    - **Last Run**: 2024-10-22

                └── **TC-P2P-002**: Verify user can send $100 to recipient via email
                    - **Type**: Integration Test
                    - **Automation**: Automated
                    - **Status**: Passed

                └── **TC-P2P-003**: Verify payment fails when daily limit ($1000) exceeded
                    - **Type**: Integration Test
                    - **Automation**: Automated
                    - **Status**: Passed

---

## Orphaned Requirements (No Test Coverage)

Items requiring attention - these represent gaps in test coverage:

| Requirement ID | Requirement | Type | Priority | Reason | Owner | Target Sprint |
|----------------|-------------|------|----------|--------|-------|---------------|
| REQ-P2P-015 | System shall support scheduled P2P payments | Functional | Could Have | Feature deprioritized to Sprint 10; tests not yet written | QA Team | Sprint 10 |
| REQ-MCD-010 | System shall detect and prevent duplicate check deposits | Functional | Must Have | Implementation delayed; integration with fraud detection pending | Dev + QA | Sprint 9 |
| REQ-NOTIF-005 | System shall support in-app messaging for marketing campaigns | Functional | Nice to Have | Low priority; deferred to Phase 2 | - | Phase 2 |

**Risk Assessment**:
- **HIGH RISK**: REQ-MCD-010 (duplicate deposits = financial loss)
- **MEDIUM RISK**: REQ-P2P-015 (user-requested feature)
- **LOW RISK**: REQ-NOTIF-005 (nice-to-have feature)

---

## Orphaned Tests (No Requirement Link)

Tests not linked to documented requirements - these may indicate missing requirements:

| Test ID | Test Case | Type | Reason | Recommendation |
|---------|-----------|------|--------|----------------|
| TC-MISC-001 | Verify app displays correctly in landscape mode on iPad | UI Test | No formal requirement documented; implied from UX design | Create requirement REQ-UI-020 for tablet support |
| TC-PERF-050 | App cold start time < 3 seconds | Performance Test | Performance requirement not formally documented in SyRS | Add to NFR matrix |
| TC-SEC-025 | Verify app obfuscates account balance when app backgrounded | Security Test | Security best practice; should be documented as requirement | Add REQ-SEC-015 for screen privacy |
| TC-ACC-010 | VoiceOver screen reader navigation test | Accessibility Test | Accessibility requirement exists but not linked | Link to REQ-ACC-001 |

---

## Suspect Links (Requiring Revalidation)

Recent requirement or design changes that may have broken traceability:

| Requirement/Design | Linked Item | Reason | Recommendation | Owner | Status |
|--------------------|-------------|--------|----------------|-------|--------|
| REQ-P2P-001 | TC-P2P-001 | Requirement modified 2024-10-15 to add email-based payments; test only validates mobile number | Update TC-P2P-001 to cover both mobile and email, or create TC-P2P-001b | QA Team | In Progress |
| REQ-AUTH-001 | DESIGN-AUTH-01 | Design updated 2024-10-18 to add Android fingerprint support; design review pending | Requirements analyst review design change for requirement impact | Amanda Rodriguez | Pending Review |

---

## Impact Analysis Example

When a change request is submitted, the RTM enables complete impact analysis:

**Change Request CR-345**: Add support for international P2P payments

**Impacted Artifacts**:

1. **Requirements**:
   - REQ-P2P-001 (modify to add currency selection)
   - REQ-P2P-002 (performance impact due to FX rate lookup)
   - REQ-P2P-005 (new: compliance with international AML regulations)

2. **Design**:
   - DESIGN-P2P-01 (add FX rate service integration)
   - DESIGN-P2P-03 (new: international payment routing)

3. **Code**:
   - PaymentService.java (add currency parameter)
   - FxRateService.java (new service)

4. **Tests**:
   - TC-P2P-001 (modify to test USD and EUR transactions)
   - TC-P2P-050 through TC-P2P-070 (new: international payment test suite)

**Estimated Effort**: 8 story points (1 sprint)
**Priority**: High
**Target Release**: Release 3.0

---

## Regulatory Traceability

For compliance audits, RTM demonstrates how regulations map to requirements and evidence:

### PCI DSS 4.0 Compliance

| Regulation | Applicable Requirements | Compliance Evidence | Audit Date | Result |
|------------|-------------------------|---------------------|------------|--------|
| PCI DSS 4.0 | REQ-SEC-010: Encrypt payment card data at rest (AES-256)<br>REQ-SEC-011: Mask PAN when displayed (last 4 digits only)<br>REQ-SEC-012: Tokenize card numbers (never store PAN) | TC-SEC-010: PCI data encryption test (Passed)<br>TC-SEC-011: PAN masking validation (Passed)<br>TC-SEC-012: Tokenization verification (Passed) | 2024-09-15 | Compliant - No exceptions |

### WCAG 2.1 Level AA Compliance

| Regulation | Applicable Requirements | Compliance Evidence | Audit Date | Result |
|------------|-------------------------|---------------------|------------|--------|
| WCAG 2.1 AA | REQ-ACC-001: Support VoiceOver and TalkBack screen readers<br>REQ-ACC-002: Minimum touch target size 44x44 pixels<br>REQ-ACC-003: Color contrast ratio ≥ 4.5:1 for text | TC-ACC-001: Screen reader navigation (Passed)<br>TC-ACC-002: Touch target size validation (Passed)<br>TC-ACC-003: Color contrast audit with axe DevTools (Passed) | 2024-10-01 | Compliant - 2 minor issues identified and fixed |

---

## Test Results Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Tests | 342 | - |
| Passed | 331 | 96.8% |
| Failed | 4 | 1.2% |
| Blocked | 3 | 0.9% |
| Not Run | 4 | 1.2% |

### Failed Tests (Requiring Attention)

| Test ID | Test Case | Status | Reason | Bug ID | Owner |
|---------|-----------|--------|--------|--------|-------|
| TC-P2P-035 | Verify payment request expiration after 7 days | Failed | Expiration job not running | BUG-892 | Dev Team |
| TC-MCD-025 | Verify deposit holds based on customer risk profile | Failed | Incorrect hold period calculation | BUG-901 | Dev Team |
| TC-AUTH-015 | Verify account lockout after 5 failed password attempts | Failed | Lockout threshold not enforced | BUG-905 | Security Team |
| TC-PERF-020 | API response time p95 < 500ms under 1000 TPS load | Failed | Performance regression: p95 = 720ms | - | Performance Team |

---

## Traceability Tool Configuration

**Requirements Management Tool**: Jira (with Zephyr Scale for test management)

**Traceability Automation**:
- GitHub PR links to Jira requirements via commit messages
- Zephyr Scale test execution linked to Jira requirements
- Confluence for design documentation with requirement links

**Reporting Frequency**: Weekly RTM coverage report to Product & QA leadership

---

## Best Practices Applied

- ✓ Unique IDs for all traceable items (BN-xxx, US-xxx, REQ-xxx, TC-xxx, DESIGN-xxx)
- ✓ Bidirectional traceability: forward (BN → US → REQ → Design → Code → Tests) and backward
- ✓ Automated traceability where possible (GitHub PR → Jira, Test execution → Requirements)
- ✓ Regular orphan detection (weekly RTM review meetings)
- ✓ Suspect link tracking when requirements or designs change
- ✓ Impact analysis documented for all change requests
- ✓ Regulatory traceability for compliance verification

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Author] | Initial RTM baseline following IEEE 29148 standards |

---

## Related Artifacts

- **YAML Version**: `requirements-traceability-matrix.yaml` (structured data for queries)
- **Functional Requirements**: `functional-requirements-specification.yaml`
- **User Stories**: Jira Epics and Stories
- **Test Cases**: Zephyr Scale test repository
- **Design Documents**: Confluence architecture pages

---

**Note**: This RTM should be updated continuously throughout the project lifecycle. Orphaned items and suspect links should be reviewed and resolved weekly. The YAML version enables automated traceability queries and reporting.
