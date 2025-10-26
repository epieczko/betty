# Data Lineage Maps
# See also: artifact_descriptions/data-lineage-maps.md for complete guidance

**Version:** 1.0.0  
**Last Updated:** 2025-10-26  
**Owner:** Data Platform Team  
**Status:** Active

## Document Control

| Field | Value |
|-------|-------|
| Lineage Scope | Customer Analytics Pipeline |
| Coverage | Source to BI Dashboard (end-to-end) |
| Lineage Tool | DataHub + OpenLineage |
| Update Frequency | Real-time (automated) |
| Classification | Internal |

## Overview

This document maps complete data lineage for the customer analytics pipeline from source systems through transformations to consumption endpoints. Lineage is captured using OpenLineage events and visualized in DataHub.

## Source Systems

### Source: PostgreSQL CRM Database

**System:** `postgres://crm-db.prod.example.com:5432/crm`  
**Tables:**
- `public.customers` → Extracted to `bronze.raw_customers`
- `public.orders` → Extracted to `bronze.raw_orders`
- `public.products` → Extracted to `bronze.raw_products`

**Extraction Method:** AWS DMS CDC (Change Data Capture)  
**Frequency:** Real-time streaming  
**SLA:** < 5 minute latency

### Source: Kafka Event Stream

**Topic:** `customer-events-prod`  
**Format:** Avro (Confluent Schema Registry)  
**Producer:** Customer Analytics Platform  
**Consumer:** Kafka Connect → S3 → Snowflake

**Lineage Path:**
```
customer-events-prod (Kafka) 
  → s3://data-lake/bronze/customer_events/ (S3 Parquet)
  → bronze.raw_customer_events (Snowflake)
```

## Data Flow: Bronze → Silver → Gold

### Bronze Layer (Raw Data)

**Location:** `analytics.bronze.*`  
**Purpose:** Unprocessed data from sources  
**Retention:** 90 days  
**Format:** Schema-on-read

**Tables:**
- `bronze.raw_customers` (from PostgreSQL)
- `bronze.raw_orders` (from PostgreSQL)  
- `bronze.raw_customer_events` (from Kafka)

### Silver Layer (Cleansed & Conformed)

**dbt Models:** `models/silver/`  
**Transformations:**

```yaml
# models/silver/stg_customers.sql
{{
  config(
    materialized='incremental',
    unique_key='customer_id',
    on_schema_change='append_new_columns'
  )
}}

SELECT
  customer_id,
  TRIM(UPPER(email)) as email_normalized,
  first_name,
  last_name,
  created_at,
  updated_at
FROM {{ source('bronze', 'raw_customers') }}
{% if is_incremental() %}
WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
{% endif %}
```

**Lineage:**
- `bronze.raw_customers` → `silver.stg_customers` (dbt model)
- `bronze.raw_orders` → `silver.stg_orders` (dbt model)
- `bronze.raw_customer_events` → `silver.stg_events` (dbt model)

**Quality Checks:**
- dbt tests: not_null, unique, relationships
- Great Expectations: format validation, range checks

### Gold Layer (Business Aggregates)

**dbt Models:** `models/gold/marts/`  
**Purpose:** Analytics-ready datasets for BI

```yaml
# models/gold/marts/customer_behavior.sql
{{
  config(
    materialized='table',
    cluster_by=['customer_id', 'event_date']
  )
}}

WITH events_agg AS (
  SELECT
    customer_id,
    DATE_TRUNC('day', event_timestamp) as event_date,
    event_type,
    COUNT(*) as event_count
  FROM {{ ref('stg_events') }}
  GROUP BY 1, 2, 3
)

SELECT
  c.customer_id,
  c.email_normalized,
  e.event_date,
  e.event_type,
  e.event_count,
  o.total_orders,
  o.total_revenue
FROM {{ ref('stg_customers') }} c
LEFT JOIN events_agg e ON c.customer_id = e.customer_id
LEFT JOIN {{ ref('customer_orders_summary') }} o ON c.customer_id = o.customer_id
```

**Lineage:**
- `silver.stg_customers` + `silver.stg_events` + `silver.stg_orders` → `gold.customer_behavior`

## Column-Level Lineage

### Example: customer_behavior.total_revenue

**Lineage Chain:**
```
Source: postgres://crm-db/public/orders.amount
  ↓ (AWS DMS CDC)
bronze.raw_orders.amount
  ↓ (dbt: stg_orders.sql - CAST(amount AS DECIMAL(10,2)))
silver.stg_orders.order_amount
  ↓ (dbt: customer_orders_summary.sql - SUM(order_amount))
gold.customer_orders_summary.total_revenue
  ↓ (dbt: customer_behavior.sql - JOIN)
gold.customer_behavior.total_revenue
  ↓ (Tableau)
Customer Analytics Dashboard.Total Revenue
```

**Transformation Logic:**
1. Extract: DMS captures `orders.amount` from PostgreSQL
2. Load: Written to `bronze.raw_orders.amount` (no transformation)
3. Transform (Silver): `CAST(amount AS DECIMAL(10,2)) as order_amount`
4. Transform (Gold): `SUM(order_amount) as total_revenue` grouped by customer
5. Consume: Tableau dashboard visualizes `Total Revenue`

## Downstream Consumers

### BI Dashboards (Tableau)

**Dashboard:** Customer Analytics Dashboard  
**Connection:** Snowflake (gold.customer_behavior)  
**Refresh:** Daily at 6 AM UTC  
**Fields Used:**
- customer_id
- email_normalized
- event_date
- total_orders
- total_revenue

**Lineage:**
```
gold.customer_behavior (Snowflake)
  → Customer Analytics Dashboard (Tableau)
  → Executive KPI Report (Tableau)
```

### ML Feature Store (Tecton)

**Feature View:** `customer_engagement_features`  
**Source:** `gold.customer_behavior`  
**Features:**
- `7_day_event_count`
- `30_day_purchase_amount`
- `days_since_last_purchase`

**Lineage:**
```
gold.customer_behavior (Snowflake)
  → customer_engagement_features (Tecton Feature Store)
  → churn_prediction_model (SageMaker)
```

## OpenLineage Events

**Event Emission:**
```python
# Airflow DAG emits OpenLineage events
from openlineage.airflow import OpenLineageAdapter

@dag(
    dag_id='customer_analytics_pipeline',
    schedule_interval='@hourly',
    start_date=datetime(2025, 1, 1)
)
def customer_analytics():
    @task
    def transform_silver():
        # dbt run emits OpenLineage events automatically
        # via dbt-openlineage integration
        run_dbt_models(['silver.*'])

    @task
    def transform_gold():
        run_dbt_models(['gold.*'])

    transform_silver() >> transform_gold()
```

**Event Structure:**
```json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-10-26T10:30:00.000Z",
  "run": {
    "runId": "550e8400-e29b-41d4-a716-446655440000",
    "facets": {}
  },
  "job": {
    "namespace": "dbt",
    "name": "silver.stg_customers",
    "facets": {
      "sql": {
        "_producer": "dbt",
        "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/SqlJobFacet.json",
        "query": "SELECT customer_id, TRIM(UPPER(email)) as email_normalized..."
      }
    }
  },
  "inputs": [
    {
      "namespace": "snowflake://analytics.prod",
      "name": "bronze.raw_customers"
    }
  ],
  "outputs": [
    {
      "namespace": "snowflake://analytics.prod",
      "name": "silver.stg_customers",
      "facets": {
        "schema": {
          "fields": [
            {"name": "customer_id", "type": "VARCHAR"},
            {"name": "email_normalized", "type": "VARCHAR"}
          ]
        }
      }
    }
  ]
}
```

## DataHub Integration

**Catalog:** https://datahub.example.com  
**Datasets Registered:**
- All bronze, silver, gold tables
- dbt models with documentation
- Tableau dashboards
- Kafka topics

**Automated Lineage Extraction:**
```yaml
# datahub-ingestion-config.yml
source:
  type: snowflake
  config:
    host_port: analytics-prod.snowflakecomputing.com
    database: analytics
    include_table_lineage: true
    include_column_lineage: true

  type: dbt
  config:
    manifest_path: target/manifest.json
    catalog_path: target/catalog.json
    run_results_path: target/run_results.json
    extract_lineage: true

  type: tableau
  config:
    connect_uri: https://tableau.example.com
    extract_lineage: true
```

## Impact Analysis

**Scenario:** Modify `bronze.raw_orders.amount` data type

**Downstream Impact:**
```
bronze.raw_orders.amount (CHANGE)
  ↓ Impacts:
silver.stg_orders.order_amount
  ↓ Impacts:
gold.customer_orders_summary.total_revenue
  ↓ Impacts:
gold.customer_behavior.total_revenue
  ↓ Impacts:
- Customer Analytics Dashboard (Tableau)
- Executive KPI Report (Tableau)
- customer_engagement_features (Tecton)
- churn_prediction_model (SageMaker)

TOTAL IMPACT: 4 downstream consumers
```

## Lineage Validation

**Automated Validation:**
- Query log analysis to verify actual lineage matches documented lineage
- Weekly reconciliation of DataHub lineage vs. OpenLineage events
- dbt lineage graph validation in CI/CD

**Manual Validation:**
- Quarterly lineage review by data governance team
- Impact analysis before major schema changes

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | Data Platform Team | Initial lineage documentation |

## Approvals

- Data Platform Lead: _____________ Date: _______
- Data Governance Committee: _____________ Date: _______
