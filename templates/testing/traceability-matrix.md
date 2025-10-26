# Requirements Traceability Matrix

<!-- See also: artifact_descriptions/traceability-matrix.md -->

## Document Control

| Field | Value |
|-------|-------|
| **Project/Product** | [Project Name] |
| **Version** | 1.0.0 |
| **Document ID** | RTM-[YYYY-MM-DD] |
| **Created Date** | YYYY-MM-DD |
| **Last Modified** | YYYY-MM-DD |
| **Document Owner** | [QA Manager Name] |
| **Next Review Date** | YYYY-MM-DD |
| **Classification** | Internal |

## Executive Summary

This Requirements Traceability Matrix (RTM) establishes bidirectional traceability between business requirements, functional specifications, design documents, test cases, and defects. It ensures complete test coverage, validates that all requirements are verified, and enables impact analysis when requirements change.

**Coverage Summary**:
- Total Requirements: [X]
- Requirements with Test Cases: [Y]
- Coverage Percentage: [Y/X * 100]%
- Requirements without Tests: [X-Y]
- Test Coverage Goal: 100% for critical/high priority requirements

## Purpose & Scope

### Purpose
Map relationships between requirements, design elements, test cases, and defects to ensure:
- Complete test coverage of all requirements
- Verification that implemented features meet specifications
- Impact analysis for requirement changes
- Compliance with testing and validation standards
- Clear accountability for requirement validation

### Scope
**In Scope**:
- Business requirements from PRD/BRD
- Functional requirements specifications
- Non-functional requirements (performance, security, usability)
- System test cases and automated tests
- Integration and E2E test cases
- Defects mapped to requirements

**Out of Scope**:
- Unit test coverage (tracked in code coverage tools)
- Infrastructure and deployment requirements
- Third-party system requirements

## Traceability Matrix

### Format Legend
- **Req ID**: Requirement identifier (e.g., REQ-001, FR-001, NFR-001)
- **Requirement**: Brief requirement description
- **Priority**: Critical | High | Medium | Low
- **Status**: Draft | Approved | In Development | In Testing | Completed
- **Test Cases**: Test case IDs that verify this requirement
- **Coverage**: Pass | Fail | Blocked | Not Tested
- **Defects**: Associated defect IDs

### Example 1: E-commerce Checkout System

| Req ID | Requirement | Priority | Status | Design Doc | Test Cases | Coverage | Defects | Notes |
|--------|-------------|----------|--------|------------|------------|----------|---------|-------|
| **FR-001** | User can add items to shopping cart | Critical | Completed | DD-CART-001 | TC-001, TC-002, TC-003, AUTO-CART-01 | Pass | - | Automated E2E test |
| **FR-002** | User can update item quantity in cart | High | Completed | DD-CART-002 | TC-004, TC-005, AUTO-CART-02 | Pass | - | |
| **FR-003** | User can remove items from cart | High | Completed | DD-CART-003 | TC-006, AUTO-CART-03 | Pass | - | |
| **FR-004** | Cart persists across sessions (logged in) | Medium | Completed | DD-CART-004 | TC-007, TC-008 | Pass | - | |
| **FR-005** | Guest cart persists for 24 hours | Medium | Completed | DD-CART-005 | TC-009 | Pass | - | |
| **FR-006** | Apply discount/promo code | High | Completed | DD-PROMO-001 | TC-010, TC-011, TC-012 | Fail | DEF-123 | Promo validation issue |
| **FR-007** | Calculate tax based on shipping address | Critical | Completed | DD-TAX-001 | TC-013, TC-014, TC-015 | Pass | - | Multi-state tax rules |
| **FR-008** | Calculate shipping cost | Critical | Completed | DD-SHIP-001 | TC-016, TC-017 | Pass | - | |
| **FR-009** | Process payment (Credit Card) | Critical | In Testing | DD-PAY-001 | TC-018, TC-019, TC-020 | Blocked | DEF-124 | Payment gateway integration |
| **FR-010** | Process payment (PayPal) | High | In Testing | DD-PAY-002 | TC-021, TC-022 | Not Tested | - | Pending test env access |
| **FR-011** | Send order confirmation email | High | Completed | DD-EMAIL-001 | TC-023, TC-024 | Pass | - | |
| **FR-012** | Display order summary before payment | Critical | Completed | DD-SUMM-001 | TC-025, AUTO-E2E-01 | Pass | - | |
| **NFR-001** | Checkout completes within 3 seconds (p95) | Critical | In Testing | DD-PERF-001 | PERF-TC-001 | Not Tested | - | Performance testing in progress |
| **NFR-002** | Support 1000 concurrent checkouts | High | In Testing | DD-PERF-002 | PERF-TC-002 | Not Tested | - | Load testing scheduled |
| **NFR-003** | PCI-DSS compliance for payment data | Critical | Completed | DD-SEC-001 | SEC-TC-001, SEC-TC-002 | Pass | - | Security audit passed |
| **NFR-004** | WCAG 2.1 AA accessibility compliance | High | In Development | DD-A11Y-001 | A11Y-TC-001, A11Y-TC-002 | Fail | DEF-125 | Screen reader issues |

**Coverage Metrics**:
- Total Requirements: 16
- Requirements with Test Cases: 16 (100%)
- Passing Tests: 12 (75%)
- Failing Tests: 2 (12.5%)
- Blocked Tests: 1 (6.25%)
- Not Tested: 3 (18.75%)

### Example 2: User Authentication System

| Req ID | Requirement | Priority | Status | Design Doc | Test Cases | Coverage | Defects | Notes |
|--------|-------------|----------|--------|------------|------------|----------|---------|-------|
| **REQ-AUTH-001** | Users can register with email and password | Critical | Completed | ARCH-AUTH-001 | TC-AUTH-001 to TC-AUTH-005 | Pass | - | Password policy enforced |
| **REQ-AUTH-002** | Email verification required before login | Critical | Completed | ARCH-AUTH-002 | TC-AUTH-006, TC-AUTH-007 | Pass | - | |
| **REQ-AUTH-003** | Users can log in with email/password | Critical | Completed | ARCH-AUTH-003 | TC-AUTH-008 to TC-AUTH-012 | Pass | - | |
| **REQ-AUTH-004** | Support OAuth 2.0 (Google, GitHub) | High | Completed | ARCH-AUTH-004 | TC-AUTH-013, TC-AUTH-014 | Pass | - | |
| **REQ-AUTH-005** | Support SAML 2.0 for enterprise SSO | Medium | In Testing | ARCH-AUTH-005 | TC-AUTH-015, TC-AUTH-016 | Not Tested | - | Pending customer test |
| **REQ-AUTH-006** | Implement MFA (TOTP) | High | Completed | ARCH-AUTH-006 | TC-AUTH-017 to TC-AUTH-020 | Pass | - | |
| **REQ-AUTH-007** | Password reset via email | Critical | Completed | ARCH-AUTH-007 | TC-AUTH-021, TC-AUTH-022 | Pass | - | |
| **REQ-AUTH-008** | Account lockout after 5 failed attempts | High | Completed | ARCH-AUTH-008 | TC-AUTH-023, TC-AUTH-024 | Pass | - | 15-minute lockout |
| **REQ-AUTH-009** | Session timeout after 30 min inactivity | Medium | Completed | ARCH-AUTH-009 | TC-AUTH-025 | Pass | - | |
| **REQ-AUTH-010** | Remember me (30-day session) | Low | Completed | ARCH-AUTH-010 | TC-AUTH-026 | Pass | - | |
| **REQ-AUTH-011** | Audit log all authentication events | High | Completed | ARCH-AUTH-011 | TC-AUTH-027 | Pass | - | SIEM integration |
| **NFR-AUTH-001** | Password hashed with bcrypt (cost factor 12) | Critical | Completed | ARCH-AUTH-012 | SEC-TC-AUTH-001 | Pass | - | Security review approved |
| **NFR-AUTH-002** | Session tokens use JWT with 1-hour expiry | Critical | Completed | ARCH-AUTH-013 | SEC-TC-AUTH-002 | Pass | - | |
| **NFR-AUTH-003** | Support 10,000 concurrent logins | High | In Testing | ARCH-AUTH-014 | PERF-TC-AUTH-001 | Not Tested | - | Performance test scheduled |

**Coverage Metrics**:
- Total Requirements: 14
- Requirements with Test Cases: 14 (100%)
- Passing Tests: 12 (85.7%)
- Not Tested: 2 (14.3%)

### Example 3: API Requirements Traceability

| Req ID | Requirement | Priority | Status | API Spec | Integration Tests | Contract Tests | E2E Tests | Coverage | Defects |
|--------|-------------|----------|--------|----------|-------------------|----------------|-----------|----------|---------|
| **API-001** | GET /api/v1/users - List users with pagination | High | Completed | OAS-USERS-001 | INT-001, INT-002 | CT-001 | E2E-001 | Pass | - |
| **API-002** | GET /api/v1/users/{id} - Get user by ID | Critical | Completed | OAS-USERS-002 | INT-003 | CT-002 | E2E-002 | Pass | - |
| **API-003** | POST /api/v1/users - Create new user | Critical | Completed | OAS-USERS-003 | INT-004, INT-005 | CT-003 | E2E-003 | Pass | - |
| **API-004** | PUT /api/v1/users/{id} - Update user | High | Completed | OAS-USERS-004 | INT-006 | CT-004 | E2E-004 | Pass | - |
| **API-005** | DELETE /api/v1/users/{id} - Delete user | High | Completed | OAS-USERS-005 | INT-007 | CT-005 | E2E-005 | Pass | - |
| **API-006** | GET /api/v1/users/{id}/orders - Get user orders | Medium | Completed | OAS-USERS-006 | INT-008 | CT-006 | - | Pass | - |
| **API-007** | POST /api/v1/auth/login - Authenticate user | Critical | Completed | OAS-AUTH-001 | INT-009, INT-010 | CT-007 | E2E-006 | Pass | - |
| **API-008** | POST /api/v1/auth/refresh - Refresh token | Critical | Completed | OAS-AUTH-002 | INT-011 | CT-008 | E2E-007 | Pass | - |
| **API-NFR-001** | All endpoints return in <200ms (p95) | Critical | In Testing | - | PERF-INT-001 | - | - | Not Tested | - |
| **API-NFR-002** | Rate limit: 1000 req/min per user | High | Completed | - | INT-012 | - | - | Pass | - |
| **API-NFR-003** | All endpoints require JWT authentication | Critical | Completed | - | INT-013, INT-014 | CT-009 | - | Pass | - |
| **API-NFR-004** | OpenAPI 3.0 spec published | High | Completed | OAS-ROOT | - | - | - | Pass | - |

## Bidirectional Traceability Views

### Requirements → Test Cases (Forward Traceability)
Ensures all requirements have test coverage

```
REQ-001 → TC-001, TC-002, TC-003, AUTO-CART-01
REQ-002 → TC-004, TC-005, AUTO-CART-02
REQ-003 → TC-006, AUTO-CART-03
[Continue for all requirements]
```

### Test Cases → Requirements (Backward Traceability)
Ensures all tests map to requirements (no orphaned tests)

```
TC-001 → REQ-001 (Verify add to cart - single item)
TC-002 → REQ-001 (Verify add to cart - multiple items)
TC-003 → REQ-001 (Verify add to cart - out of stock)
[Continue for all test cases]
```

### Defects → Requirements
Track which requirements have issues

```
DEF-123 → FR-006 (Promo code validation failure)
DEF-124 → FR-009 (Payment gateway timeout)
DEF-125 → NFR-004 (Screen reader navigation broken)
```

## Coverage Analysis

### Requirements Coverage by Priority

| Priority | Total Requirements | Tested | Pass | Fail | Blocked | Not Tested | Coverage % |
|----------|-------------------|--------|------|------|---------|------------|------------|
| Critical | 8 | 8 | 6 | 0 | 1 | 1 | 100% |
| High | 6 | 6 | 4 | 2 | 0 | 0 | 100% |
| Medium | 4 | 4 | 3 | 0 | 0 | 1 | 100% |
| Low | 1 | 1 | 1 | 0 | 0 | 0 | 100% |
| **Total** | **19** | **19** | **14** | **2** | **1** | **2** | **100%** |

### Requirements Coverage by Type

| Type | Total | With Tests | Coverage % | Pass Rate |
|------|-------|------------|------------|-----------|
| Functional Requirements | 12 | 12 | 100% | 83% |
| Non-Functional Requirements | 7 | 7 | 100% | 57% |
| API Requirements | 12 | 12 | 100% | 92% |

### Test Type Coverage

| Test Type | Requirements Covered | Percentage |
|-----------|---------------------|------------|
| Unit Tests | 15 | 79% |
| Integration Tests | 19 | 100% |
| E2E Tests | 8 | 42% |
| Performance Tests | 4 | 21% |
| Security Tests | 3 | 16% |
| Accessibility Tests | 2 | 11% |

## Gap Analysis

### Requirements without Complete Test Coverage
*None - 100% coverage achieved*

### Failed or Blocked Requirements

1. **FR-006**: Apply discount/promo code
   - Status: Fail
   - Defect: DEF-123
   - Impact: High priority requirement blocking release
   - Action: Fix promo validation logic by 2024-12-15

2. **FR-009**: Process payment (Credit Card)
   - Status: Blocked
   - Defect: DEF-124
   - Impact: Critical requirement blocking release
   - Action: Resolve payment gateway timeout issue

3. **NFR-004**: WCAG 2.1 AA compliance
   - Status: Fail
   - Defect: DEF-125
   - Impact: High priority for accessibility compliance
   - Action: Fix screen reader navigation

### Untested Requirements

1. **FR-010**: Process payment (PayPal) - Waiting for PayPal sandbox access
2. **NFR-001**: Checkout p95 latency <3s - Performance test scheduled for next sprint
3. **NFR-002**: Support 1000 concurrent checkouts - Load test scheduled
4. **REQ-AUTH-005**: SAML SSO - Waiting for enterprise customer test environment

## Test Case Mapping

### Automated Test Coverage

| Test Suite | Requirements Covered | Test Count | Pass | Fail | Pass Rate |
|------------|---------------------|------------|------|------|-----------|
| Unit Tests | FR-001 to FR-012 | 45 | 43 | 2 | 95.6% |
| Integration Tests | All API requirements | 28 | 27 | 1 | 96.4% |
| E2E Tests | Critical user journeys | 12 | 11 | 1 | 91.7% |
| Performance Tests | NFR-001, NFR-002 | 5 | 0 | 0 | 0% (scheduled) |
| Security Tests | NFR-003, all auth | 8 | 8 | 0 | 100% |
| Accessibility Tests | NFR-004 | 3 | 2 | 1 | 66.7% |

## Requirement Change Impact Analysis

### Change History

| Date | Req ID | Change Type | Impact | Tests Updated | Status |
|------|--------|-------------|--------|---------------|--------|
| 2024-11-15 | FR-006 | Modified | Added multi-code support | TC-010, TC-011, TC-012 | Completed |
| 2024-11-20 | NFR-001 | Modified | Changed p95 target 5s→3s | PERF-TC-001 | In Progress |
| 2024-12-01 | FR-013 | Added | New requirement: Gift cards | New tests needed | Draft |

### Pending Changes Impact

**FR-013** (NEW): Support gift card payment
- Estimated Test Cases: 8 new test cases
- Affected Components: Payment module, Cart module
- Related Requirements: FR-009, FR-010
- Testing Effort: 2 days
- Target Completion: Sprint 24

## Sign-off

### Test Coverage Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Manager | [Name] | _________ | YYYY-MM-DD |
| Dev Manager | [Name] | _________ | YYYY-MM-DD |
| Product Owner | [Name] | _________ | YYYY-MM-DD |
| Test Architect | [Name] | _________ | YYYY-MM-DD |

### Release Readiness Assessment

**Overall Assessment**: ⚠️ NOT READY

**Blocking Issues**:
- [ ] DEF-123: Promo code validation (FR-006) - Target: 2024-12-15
- [ ] DEF-124: Payment gateway timeout (FR-009) - Target: 2024-12-18
- [ ] DEF-125: Accessibility issues (NFR-004) - Target: 2024-12-20

**Pending Tests**:
- [ ] FR-010: PayPal payment testing
- [ ] NFR-001, NFR-002: Performance and load testing

**Release Criteria**: All Critical and High priority requirements must Pass

## Related Artifacts

- **Requirements Documentation**: `/docs/requirements/PRD-v2.0.md`
- **Test Plan**: `/docs/testing/test-plan-v1.5.md`
- **Test Cases**: `/tests/testcases/`
- **Automated Tests**: `/tests/automation/`
- **Defect Tracking**: Jira Project: ECOM
- **Test Execution Results**: `/reports/test-results/`

## Maintenance

- **Review Frequency**: Weekly during active development, Monthly in maintenance
- **Update Triggers**: New requirements, requirement changes, new test cases, defects
- **Owner**: QA Manager
- **Last Updated**: YYYY-MM-DD
- **Next Review**: YYYY-MM-DD
