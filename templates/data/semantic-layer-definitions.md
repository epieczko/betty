# Semantic Layer Definitions

> **Purpose**: Business-friendly abstraction layer defining metrics, dimensions, and business logic centrally for consistent analytics across BI tools (Looker LookML, dbt Metrics, Cube.js, AtScale).
>
> **See also**: `artifact_descriptions/semantic-layer-definitions.md` | YAML version: `semantic-layer-definitions.yaml`

## Overview

```yaml
version: 1.0.0
platform: LookML (Looker) | dbt Metrics | Cube.js | AtScale
owner: Analytics Engineering Team
classification: Internal
lastUpdated: 2025-01-15
```

---

## Example 1: Revenue Metrics (LookML)

```lookml
view: orders {
  sql_table_name: analytics.prod.orders ;;

  dimension: order_id {
    primary_key: yes
    type: string
    sql: ${TABLE}.order_id ;;
  }

  dimension_group: ordered {
    type: time
    timeframes: [date, week, month, quarter, year]
    convert_tz: no
    datatype: timestamp
    sql: ${TABLE}.ordered_at ;;
  }

  dimension: customer_id {
    type: string
    sql: ${TABLE}.customer_id ;;
    hidden: yes
  }

  measure: total_revenue {
    type: sum
    sql: ${TABLE}.order_total ;;
    value_format_name: usd
    drill_fields: [order_id, customer.name, ordered_date, order_total]
  }

  measure: order_count {
    type: count_distinct
    sql: ${order_id} ;;
    drill_fields: [order_detail*]
  }

  measure: average_order_value {
    type: number
    sql: ${total_revenue} / NULLIF(${order_count}, 0) ;;
    value_format_name: usd
  }

  set: order_detail {
    fields: [order_id, ordered_date, customer.name, total_revenue]
  }
}
```

---

## Example 2: Customer Metrics (dbt Metrics)

```yaml
# models/metrics/customer_metrics.yml
version: 2

metrics:
  - name: monthly_recurring_revenue
    label: Monthly Recurring Revenue (MRR)
    model: ref('customers')
    description: Total MRR from all active subscriptions

    calculation_method: sum
    expression: mrr_amount

    timestamp: created_at
    time_grains: [day, week, month, quarter, year]

    dimensions:
      - customer_tier
      - plan_type
      - region

    filters:
      - field: subscription_status
        operator: '='
        value: "'active'"

    meta:
      owner: finance-team@company.com
      business_definition: |
        Sum of normalized monthly revenue from all active
        paying customers as of snapshot date.

  - name: customer_churn_rate
    label: Customer Churn Rate
    model: ref('customers')
    description: Percentage of customers who churned this month

    calculation_method: derived
    expression: "{{ metric('churned_customers') }} / {{ metric('total_customers_start_of_month') }}"

    timestamp: churn_date
    time_grains: [month, quarter]

    meta:
      format: percent
      decimals: 2
```

---

## Example 3: Product Analytics (Cube.js)

```javascript
cube(`UsageEvents`, {
  sql: `SELECT * FROM analytics.prod.usage_events`,

  dimensions: {
    userId: {
      sql: `user_id`,
      type: `string`,
      primaryKey: true
    },

    featureName: {
      sql: `feature_name`,
      type: `string`
    },

    eventDate: {
      sql: `event_timestamp`,
      type: `time`
    },

    companySize: {
      sql: `company_size`,
      type: `string`,
      case: {
        when: [
          { sql: `${CUBE}.company_employee_count < 50`, label: 'SMB' },
          { sql: `${CUBE}.company_employee_count < 500`, label: 'Mid-Market' },
          { sql: `${CUBE}.company_employee_count >= 500`, label: 'Enterprise' }
        ]
      }
    }
  },

  measures: {
    count: {
      type: `count`
    },

    dailyActiveUsers: {
      sql: `user_id`,
      type: `countDistinct`,
      rollingWindow: {
        trailing: `1 day`
      }
    },

    weeklyActiveUsers: {
      sql: `user_id`,
      type: `countDistinct`,
      rollingWindow: {
        trailing: `7 day`
      }
    },

    avgSessionDuration: {
      sql: `session_duration_seconds`,
      type: `avg`,
      format: `time`
    },

    featureAdoptionRate: {
      sql: `CASE WHEN ${CUBE}.feature_name = 'advanced_feature' THEN ${CUBE}.user_id END`,
      type: `countDistinct`,
      drillMembers: [userId, featureName, eventDate]
    }
  },

  preAggregations: {
    dailyRollup: {
      measures: [dailyActiveUsers, count],
      dimensions: [featureName, companySize],
      timeDimension: eventDate,
      granularity: `day`,
      partitionGranularity: `month`,
      refreshKey: {
        every: `1 hour`
      }
    }
  }
});
```

---

## Metric Catalog

| Metric Name | Definition | Grain | Dimensions | Owner |
|-------------|------------|-------|------------|-------|
| **Revenue Metrics** |
| MRR | SUM(subscription_amount) WHERE status='active' | Monthly | tier, region | Finance |
| ARR | MRR * 12 | Annual | tier, region | Finance |
| ARPU | MRR / active_customers | Monthly | tier | Product |
| **Growth Metrics** |
| Customer Growth Rate | (customers_end - customers_start) / customers_start | Monthly | segment | Growth |
| Revenue Growth Rate | (revenue_curr - revenue_prev) / revenue_prev * 100 | Monthly | product_line | Finance |
| **Engagement Metrics** |
| DAU | COUNT(DISTINCT user_id) per day | Daily | feature, cohort | Product |
| WAU | COUNT(DISTINCT user_id) per 7 days | Weekly | feature, cohort | Product |
| DAU/MAU Ratio | DAU / MAU * 100 (stickiness) | Daily | - | Product |

---

## Business Logic Documentation

### Metric: Net Revenue Retention (NRR)

```sql
-- Business Definition
-- NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR

WITH cohort_revenue AS (
  SELECT
    DATE_TRUNC('month', cohort_month) as cohort_month,
    SUM(CASE WHEN month_number = 0 THEN mrr ELSE 0 END) as starting_mrr,
    SUM(CASE WHEN month_number = 12 THEN mrr ELSE 0 END) as month_12_mrr,
    SUM(CASE WHEN month_number = 12 AND mrr > starting_customer_mrr THEN mrr - starting_customer_mrr ELSE 0 END) as expansion,
    SUM(CASE WHEN month_number = 12 AND mrr < starting_customer_mrr THEN starting_customer_mrr - mrr ELSE 0 END) as contraction,
    SUM(CASE WHEN churned_flag = TRUE THEN starting_customer_mrr ELSE 0 END) as churn
  FROM customer_cohorts
  WHERE month_number <= 12
  GROUP BY 1
)
SELECT
  cohort_month,
  starting_mrr,
  month_12_mrr,
  (month_12_mrr / NULLIF(starting_mrr, 0)) * 100 as nrr_percentage,
  expansion,
  contraction,
  churn
FROM cohort_revenue;
```

**Dimensions**:
- customer_segment (SMB, Mid-Market, Enterprise)
- plan_type (Monthly, Annual)
- acquisition_channel

**Grain**: Monthly cohort

**SLA**: Updated within 24 hours of month close

---

**Document Owner**: Analytics Engineering Team
**Last Updated**: 2025-01-15
