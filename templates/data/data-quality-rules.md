# Data Quality Rules
# See also: artifact_descriptions/data-quality-rules.md for complete guidance

**Version:** 1.0.0
**Last Updated:** 2025-10-26
**Owner:** Data Engineering Team
**Status:** Active

## Document Control

| Field | Value |
|-------|-------|
| Dataset | customer_events |
| Data Product | Customer Analytics Data Product |
| Owner | Data Product Owner |
| Steward | Analytics Engineering Team |
| Quality Framework | Great Expectations + dbt tests |
| Review Frequency | Quarterly |
| Classification | Internal |

## Overview

This document defines executable data quality rules for the `customer_events` dataset using Great Expectations, dbt tests, and Soda Core. Rules are organized by DAMA data quality dimensions: accuracy, completeness, consistency, validity, timeliness, and uniqueness.

## Quality Dimensions

### 1. Completeness Rules

**Rule ID:** DQ-COMP-001
**Name:** Event ID Completeness
**Dimension:** Completeness
**Description:** Event ID must be present in all records
**Severity:** Critical
**Threshold:** 100% non-null
**Action:** Block pipeline if failed

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_not_be_null:
  column: event_id

# dbt test
models:
  - name: customer_events
    columns:
      - name: event_id
        tests:
          - not_null
```

---

**Rule ID:** DQ-COMP-002
**Name:** Customer ID Completeness
**Dimension:** Completeness
**Description:** Customer ID should be present for 99% of events
**Severity:** High
**Threshold:** >= 99% non-null
**Action:** Alert if below threshold

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_not_be_null:
  column: customer_id
  mostly: 0.99

# Soda Core
checks for customer_events:
  - missing_count(customer_id) < 1%:
      name: Customer ID completeness
```

---

**Rule ID:** DQ-COMP-003
**Name:** Required Fields Completeness
**Dimension:** Completeness
**Description:** Core fields must be present
**Severity:** Critical
**Required Fields:** event_id, event_type, event_timestamp, created_at

**Implementation:**
```python
# Great Expectations Suite
suite.add_expectation(
    ExpectationConfiguration(
        expectation_type="expect_table_columns_to_match_set",
        kwargs={
            "column_set": [
                "event_id", "customer_id", "event_type", "event_timestamp",
                "event_properties", "session_id", "user_agent", "ip_address",
                "device_type", "country_code", "created_at", "updated_at", "_partition_date"
            ],
            "exact_match": True
        }
    )
)
```

---

### 2. Uniqueness Rules

**Rule ID:** DQ-UNIQ-001
**Name:** Event ID Uniqueness
**Dimension:** Uniqueness
**Description:** Event IDs must be globally unique (no duplicates)
**Severity:** Critical
**Threshold:** 100% unique
**Action:** Block pipeline if failed

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_be_unique:
  column: event_id

# dbt test
models:
  - name: customer_events
    columns:
      - name: event_id
        tests:
          - unique
```

---

**Rule ID:** DQ-UNIQ-002
**Name:** Duplicate Detection
**Dimension:** Uniqueness
**Description:** Detect duplicate events (same customer_id + timestamp + event_type)
**Severity:** Medium
**Threshold:** < 0.1% duplicates
**Action:** Alert and quarantine duplicates

**Implementation:**
```sql
-- dbt singular test (tests/duplicate_events.sql)
WITH duplicates AS (
  SELECT
    customer_id,
    event_type,
    event_timestamp,
    COUNT(*) as cnt
  FROM {{ ref('customer_events') }}
  GROUP BY customer_id, event_type, event_timestamp
  HAVING COUNT(*) > 1
)
SELECT * FROM duplicates
```

---

### 3. Validity Rules

**Rule ID:** DQ-VALID-001
**Name:** Event Type Validity
**Dimension:** Validity
**Description:** Event type must be one of allowed values
**Severity:** High
**Allowed Values:** page_view, button_click, form_submit, purchase, signup, login, logout, add_to_cart, remove_from_cart
**Threshold:** 100% valid
**Action:** Quarantine invalid records

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_be_in_set:
  column: event_type
  value_set:
    - page_view
    - button_click
    - form_submit
    - purchase
    - signup
    - login
    - logout
    - add_to_cart
    - remove_from_cart

# dbt test
models:
  - name: customer_events
    columns:
      - name: event_type
        tests:
          - accepted_values:
              values: ['page_view', 'button_click', 'form_submit', 'purchase',
                       'signup', 'login', 'logout', 'add_to_cart', 'remove_from_cart']
```

---

**Rule ID:** DQ-VALID-002
**Name:** Event ID Format Validation
**Dimension:** Validity
**Description:** Event ID must be valid UUID v4 format
**Severity:** High
**Threshold:** 100% valid format
**Action:** Block invalid records

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_match_regex:
  column: event_id
  regex: "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
  mostly: 1.0

# Soda Core
checks for customer_events:
  - invalid_count(event_id) = 0:
      valid format: uuid
```

---

**Rule ID:** DQ-VALID-003
**Name:** IP Address Format
**Dimension:** Validity
**Description:** IP address must match IPv4 format (when present)
**Severity:** Low
**Threshold:** 100% valid (excluding nulls)
**Action:** Log invalid values

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_match_regex:
  column: ip_address
  regex: "^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$"
  mostly: 1.0
```

---

**Rule ID:** DQ-VALID-004
**Name:** Country Code Format
**Dimension:** Validity
**Description:** Country code must be ISO 3166-1 alpha-2 (two uppercase letters)
**Severity:** Medium
**Threshold:** 100% valid (excluding nulls)

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_match_regex:
  column: country_code
  regex: "^[A-Z]{2}$"
```

---

### 4. Consistency Rules

**Rule ID:** DQ-CONS-001
**Name:** Timestamp Ordering
**Dimension:** Consistency
**Description:** created_at must be >= event_timestamp
**Severity:** Medium
**Threshold:** 100% consistent
**Action:** Alert on violations

**Implementation:**
```sql
-- dbt singular test (tests/timestamp_consistency.sql)
SELECT *
FROM {{ ref('customer_events') }}
WHERE created_at < event_timestamp
```

---

**Rule ID:** DQ-CONS-002
**Name:** Referential Integrity - Customers
**Dimension:** Consistency
**Description:** Customer IDs should exist in customers table
**Severity:** Medium
**Threshold:** >= 95% valid references
**Action:** Alert if below threshold

**Implementation:**
```yaml
# dbt test
models:
  - name: customer_events
    columns:
      - name: customer_id
        tests:
          - relationships:
              to: ref('customers')
              field: customer_id
              config:
                severity: warn
                warn_if: ">5%"  # warn if >5% invalid
```

---

**Rule ID:** DQ-CONS-003
**Name:** Device Type Derivation Consistency
**Dimension:** Consistency
**Description:** device_type should be derivable from user_agent
**Severity:** Low
**Threshold:** >= 90% derivable
**Action:** Log inconsistencies

---

### 5. Accuracy Rules

**Rule ID:** DQ-ACC-001
**Name:** Timestamp Not Future
**Dimension:** Accuracy
**Description:** Event timestamp must not be in the future
**Severity:** High
**Threshold:** 100% not future
**Action:** Quarantine future-dated events

**Implementation:**
```yaml
# Great Expectations
expect_column_values_to_be_between:
  column: event_timestamp
  min_value: null
  max_value: now
  parse_strings_as_datetimes: true
```

---

**Rule ID:** DQ-ACC-002
**Name:** Timestamp Recency
**Dimension:** Accuracy
**Description:** Event timestamps should not be older than 90 days
**Severity:** Medium
**Threshold:** >= 99% within 90 days
**Action:** Alert on old events

**Implementation:**
```sql
-- dbt singular test
SELECT *
FROM {{ ref('customer_events') }}
WHERE event_timestamp < CURRENT_TIMESTAMP - INTERVAL '90 days'
HAVING COUNT(*) > (SELECT COUNT(*) * 0.01 FROM {{ ref('customer_events') }})
```

---

### 6. Timeliness (Freshness) Rules

**Rule ID:** DQ-TIME-001
**Name:** Data Freshness
**Dimension:** Timeliness
**Description:** Most recent event should be less than 15 minutes old
**Severity:** Critical
**Threshold:** MAX(CURRENT_TIMESTAMP - event_timestamp) < 15 minutes
**Action:** Alert if stale

**Implementation:**
```yaml
# dbt freshness test
sources:
  - name: analytics
    tables:
      - name: customer_events
        freshness:
          warn_after: {count: 15, period: minute}
          error_after: {count: 30, period: minute}
        loaded_at_field: event_timestamp

# Great Expectations
expect_column_max_to_be_between:
  column: event_timestamp
  min_value: now - 15 minutes
  max_value: now
```

---

**Rule ID:** DQ-TIME-002
**Name:** Partition Freshness
**Dimension:** Timeliness
**Description:** Today's partition should exist and have data
**Severity:** Critical
**Threshold:** Row count for today's partition > 0
**Action:** Block downstream if no data

**Implementation:**
```sql
-- dbt singular test
SELECT COUNT(*) as row_count
FROM {{ ref('customer_events') }}
WHERE _partition_date = CURRENT_DATE
HAVING COUNT(*) = 0  -- Fails if no rows for today
```

---

### 7. Volume / Completeness Rules

**Rule ID:** DQ-VOL-001
**Name:** Daily Row Count Range
**Dimension:** Volume
**Description:** Daily row count should be between 950K and 1.05M
**Severity:** High
**Threshold:** 950,000 <= daily_rows <= 1,050,000
**Action:** Alert if outside range

**Implementation:**
```yaml
# Great Expectations
expect_table_row_count_to_be_between:
  min_value: 950000
  max_value: 1050000

# Soda Core
checks for customer_events:
  - row_count > 950000:
      name: Minimum daily row count
  - row_count < 1050000:
      name: Maximum daily row count
```

---

**Rule ID:** DQ-VOL-002
**Name:** Row Count Anomaly Detection
**Dimension:** Volume
**Description:** Daily row count should not deviate more than 20% from 7-day average
**Severity:** Medium
**Threshold:** Within 20% of rolling average
**Action:** Alert on anomaly

**Implementation:**
```sql
-- Monte Carlo / Anomalo anomaly detection
-- Configured in data observability platform
```

---

## Quality Rule Summary Matrix

| Rule ID | Dimension | Severity | Threshold | Action | Framework |
|---------|-----------|----------|-----------|--------|-----------|
| DQ-COMP-001 | Completeness | Critical | 100% | Block | GE + dbt |
| DQ-COMP-002 | Completeness | High | 99% | Alert | GE + Soda |
| DQ-UNIQ-001 | Uniqueness | Critical | 100% | Block | GE + dbt |
| DQ-UNIQ-002 | Uniqueness | Medium | <0.1% | Alert | dbt |
| DQ-VALID-001 | Validity | High | 100% | Quarantine | GE + dbt |
| DQ-VALID-002 | Validity | High | 100% | Block | GE + Soda |
| DQ-VALID-003 | Validity | Low | 100% | Log | GE |
| DQ-VALID-004 | Validity | Medium | 100% | Alert | GE |
| DQ-CONS-001 | Consistency | Medium | 100% | Alert | dbt |
| DQ-CONS-002 | Consistency | Medium | 95% | Alert | dbt |
| DQ-ACC-001 | Accuracy | High | 100% | Quarantine | GE |
| DQ-ACC-002 | Accuracy | Medium | 99% | Alert | dbt |
| DQ-TIME-001 | Timeliness | Critical | 15 min | Alert | dbt + GE |
| DQ-TIME-002 | Timeliness | Critical | >0 rows | Block | dbt |
| DQ-VOL-001 | Volume | High | 950K-1.05M | Alert | GE + Soda |
| DQ-VOL-002 | Volume | Medium | ±20% | Alert | Monte Carlo |

## Great Expectations Suite

```python
# great_expectations/expectations/customer_events_suite.py
import great_expectations as gx

suite = gx.get_context().add_expectation_suite("customer_events_quality_suite")

# Completeness
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="event_id")
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="customer_id",
        mostly=0.99
    )
)

# Uniqueness
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeUnique(column="event_id")
)

# Validity - Event Type
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeInSet(
        column="event_type",
        value_set=["page_view", "button_click", "form_submit", "purchase",
                   "signup", "login", "logout", "add_to_cart", "remove_from_cart"]
    )
)

# Validity - UUID Format
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="event_id",
        regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
    )
)

# Timeliness
suite.add_expectation(
    gx.expectations.ExpectColumnMaxToBeBetween(
        column="event_timestamp",
        min_value="now - 15 minutes",
        max_value="now"
    )
)

# Volume
suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(
        min_value=950000,
        max_value=1050000
    )
)
```

## dbt Tests Configuration

```yaml
# models/analytics/customer_events.yml
version: 2

models:
  - name: customer_events
    description: Customer interaction events

    # Data freshness
    freshness:
      warn_after: {count: 15, period: minute}
      error_after: {count: 30, period: minute}
    loaded_at_field: event_timestamp

    columns:
      - name: event_id
        description: Unique event identifier
        tests:
          - not_null
          - unique

      - name: customer_id
        description: Customer identifier
        tests:
          - not_null:
              config:
                severity: warn
                warn_if: ">1%"
          - relationships:
              to: ref('customers')
              field: customer_id
              config:
                severity: warn

      - name: event_type
        description: Type of event
        tests:
          - not_null
          - accepted_values:
              values: ['page_view', 'button_click', 'form_submit', 'purchase',
                       'signup', 'login', 'logout', 'add_to_cart', 'remove_from_cart']

      - name: event_timestamp
        description: Event occurrence time
        tests:
          - not_null

      - name: country_code
        description: ISO 3166-1 alpha-2 country code
        tests:
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 100
              inclusive: false
```

## Soda Core Checks

```yaml
# soda/checks/customer_events.yml
checks for customer_events:
  # Completeness
  - missing_count(event_id) = 0:
      name: Event ID must be complete
  - missing_count(customer_id) < 1%:
      name: Customer ID 99% complete

  # Uniqueness
  - duplicate_count(event_id) = 0:
      name: Event ID must be unique

  # Validity
  - invalid_count(event_id) = 0:
      valid format: uuid
      name: Event ID must be valid UUID
  - invalid_count(event_type) = 0:
      valid values: ['page_view', 'button_click', 'form_submit', 'purchase',
                     'signup', 'login', 'logout', 'add_to_cart', 'remove_from_cart']

  # Volume
  - row_count > 950000:
      name: Minimum daily row count check
  - row_count < 1050000:
      name: Maximum daily row count check

  # Custom SQL check
  - failed rows:
      name: Future-dated events
      fail query: |
        SELECT * FROM customer_events
        WHERE event_timestamp > CURRENT_TIMESTAMP
```

## Monitoring & Alerting

**Quality Dashboard:** https://monitoring.example.com/data-quality/customer_events

**Alert Routing:**
- Critical failures: PagerDuty (data-platform-oncall) + Slack (#data-alerts-critical)
- High severity: Slack (#data-quality) + Email (data-team@example.com)
- Medium/Low severity: Slack (#data-quality)

**Metrics Tracked:**
- Quality rules pass rate (target: >98%)
- Critical rule failures (target: 0)
- Data freshness SLI (target: <15 minutes)
- Volume anomalies detected

## Execution Schedule

- Great Expectations: Run on every pipeline execution (continuous)
- dbt tests: Run after each dbt model build (continuous)
- Soda scans: Hourly automated scans
- Anomaly detection: Real-time monitoring (Monte Carlo)

## Remediation Procedures

**Critical Failure (e.g., uniqueness violation):**
1. Block pipeline execution
2. Page on-call engineer
3. Investigate root cause
4. Fix and backfill if needed
5. Resume pipeline after validation

**High Severity (e.g., completeness below threshold):**
1. Alert data team
2. Investigate within 2 hours
3. Assess data impact
4. Implement fix
5. Document in incident log

**Medium/Low Severity:**
1. Log to monitoring system
2. Review during daily standup
3. Schedule fix if needed

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | Data Engineering Team | Initial quality rules |

## Approvals

- Data Product Owner: _____________ Date: _______
- Data Quality Lead: _____________ Date: _______
- Data Governance Committee: _____________ Date: _______
