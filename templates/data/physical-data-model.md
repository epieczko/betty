# Physical Data Model

> **Purpose**: Database-specific implementation including tables, columns, indexes, partitions, constraints, and performance optimization for specific DBMS (Postgres, MySQL, Snowflake, BigQuery).
>
> **See also**: `artifact_descriptions/physical-data-model.md`

## Model Overview

```yaml
version: 2.1.0
database: Snowflake | PostgreSQL | MySQL | BigQuery | Oracle
schema: prod
owner: Database Administration Team
created: 2024-10-01
lastModified: 2025-01-15
```

---

## Example 1: E-Commerce (Snowflake)

### Table: CUSTOMERS

```sql
CREATE OR REPLACE TABLE analytics.prod.customers (
  customer_id VARCHAR(36) NOT NULL,
  email VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP_NTZ NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  updated_at TIMESTAMP_NTZ NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  lifetime_value NUMBER(12,2) DEFAULT 0.00,
  loyalty_tier VARCHAR(20) DEFAULT 'Bronze',
  is_active BOOLEAN DEFAULT TRUE,
  deleted_at TIMESTAMP_NTZ,

  -- Primary Key
  CONSTRAINT pk_customers PRIMARY KEY (customer_id),

  -- Unique Constraints
  CONSTRAINT uk_customers_email UNIQUE (email),

  -- Check Constraints
  CONSTRAINT ck_customers_loyalty_tier
    CHECK (loyalty_tier IN ('Bronze', 'Silver', 'Gold', 'Platinum')),
  CONSTRAINT ck_customers_lifetime_value
    CHECK (lifetime_value >= 0)
)
COMMENT = 'Golden customer record combining CRM, billing, and product usage'
CLUSTER BY (customer_id)
;

-- Indexes (Snowflake uses automatic clustering)
-- Manual clustering key on high-cardinality customer_id for joins
```

### Table: ORDERS (Partitioned)

```sql
CREATE OR REPLACE TABLE analytics.prod.orders (
  order_id VARCHAR(36) NOT NULL,
  customer_id VARCHAR(36) NOT NULL,
  order_total NUMBER(12,2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  payment_method VARCHAR(50),
  ordered_at TIMESTAMP_NTZ NOT NULL,
  shipped_at TIMESTAMP_NTZ,
  delivered_at TIMESTAMP_NTZ,
  created_at TIMESTAMP_NTZ NOT NULL DEFAULT CURRENT_TIMESTAMP(),

  -- Primary Key
  CONSTRAINT pk_orders PRIMARY KEY (order_id),

  -- Foreign Keys
  CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES analytics.prod.customers(customer_id),

  -- Check Constraints
  CONSTRAINT ck_orders_total CHECK (order_total > 0),
  CONSTRAINT ck_orders_status
    CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled'))
)
COMMENT = 'Customer orders from checkout service'
-- Time-based clustering for date-range queries
CLUSTER BY (TO_DATE(ordered_at))
;
```

**Partitioning Strategy**:
- Automatic micro-partitions based on CLUSTER BY (ordered_at)
- Pruning on date filters improves query performance 10-100x
- Partition by month for orders older than 2 years

---

## Example 2: Analytics Warehouse (BigQuery)

### Partitioned & Clustered Table

```sql
CREATE OR REPLACE TABLE `company-prod.analytics.usage_events`
(
  event_id STRING NOT NULL,
  user_id STRING NOT NULL,
  session_id STRING,
  event_type STRING NOT NULL,
  event_timestamp TIMESTAMP NOT NULL,
  properties JSON,
  device_type STRING,
  country_code STRING(2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
-- Partition by day on event_timestamp (reduces scan cost)
PARTITION BY DATE(event_timestamp)

-- Cluster by high-cardinality columns used in WHERE/JOIN
CLUSTER BY user_id, event_type

-- Table options
OPTIONS(
  description="User activity events from web and mobile apps",
  partition_expiration_days=730,  -- Auto-delete partitions older than 2 years
  require_partition_filter=TRUE,  -- Force partition filter in queries
  labels=[("team", "analytics"), ("env", "prod")]
)
;

-- Create partition-aligned search index
CREATE SEARCH INDEX idx_events_properties
ON `company-prod.analytics.usage_events`(ALL COLUMNS)
OPTIONS(analyzer='LOG_ANALYZER');
```

**Query Performance**:
```sql
-- GOOD: Uses partition pruning (scans 1 day)
SELECT COUNT(*)
FROM `company-prod.analytics.usage_events`
WHERE DATE(event_timestamp) = '2025-01-15'
  AND event_type = 'purchase';

-- BAD: Scans all partitions (expensive!)
SELECT COUNT(*)
FROM `company-prod.analytics.usage_events`
WHERE event_type = 'purchase';  -- No partition filter!
```

---

## Example 3: OLTP Database (PostgreSQL)

### Optimized for Transactional Workloads

```sql
-- Create schema
CREATE SCHEMA IF NOT EXISTS ecommerce;

-- Table with extensive indexing
CREATE TABLE ecommerce.orders (
  order_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id UUID NOT NULL,
  order_total DECIMAL(12,2) NOT NULL CHECK (order_total > 0),
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  ordered_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_customer FOREIGN KEY (customer_id)
    REFERENCES ecommerce.customers(customer_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- Indexes for common query patterns
CREATE INDEX idx_orders_customer_id ON ecommerce.orders(customer_id);
CREATE INDEX idx_orders_status ON ecommerce.orders(status) WHERE status != 'delivered';
CREATE INDEX idx_orders_ordered_at ON ecommerce.orders(ordered_at DESC);

-- Composite index for customer order history queries
CREATE INDEX idx_orders_customer_ordered
  ON ecommerce.orders(customer_id, ordered_at DESC);

-- Partial index for active orders only (smaller, faster)
CREATE INDEX idx_orders_active
  ON ecommerce.orders(order_id)
  WHERE status IN ('pending', 'confirmed', 'shipped');

-- GIN index for JSONB columns (if using)
CREATE INDEX idx_orders_metadata_gin
  ON ecommerce.orders USING GIN(metadata);

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_orders_updated_at
  BEFORE UPDATE ON ecommerce.orders
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

-- Table partitioning (for very large tables)
CREATE TABLE ecommerce.orders_2024 PARTITION OF ecommerce.orders
  FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
CREATE TABLE ecommerce.orders_2025 PARTITION OF ecommerce.orders
  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

---

## Index Design Patterns

### B-Tree Indexes (Default)

```sql
-- Single column (for equality and range queries)
CREATE INDEX idx_customers_email ON customers(email);

-- Composite index (query must use leftmost columns)
CREATE INDEX idx_orders_composite ON orders(customer_id, ordered_at DESC, status);

-- Covers query: SELECT order_id FROM orders WHERE customer_id = ? AND ordered_at > ?
```

### Covering Indexes (INCLUDE columns - PostgreSQL 11+)

```sql
-- Include frequently selected columns to avoid table lookups
CREATE INDEX idx_orders_covering
  ON orders(customer_id, ordered_at)
  INCLUDE (order_total, status);

-- Query uses index-only scan (no table access needed)
-- SELECT order_total, status FROM orders WHERE customer_id = ? AND ordered_at > ?
```

### Partial Indexes

```sql
-- Index only active customers (smaller, faster)
CREATE INDEX idx_customers_active ON customers(customer_id)
  WHERE is_active = TRUE AND deleted_at IS NULL;

-- Index only pending/confirmed orders (not delivered/cancelled)
CREATE INDEX idx_orders_pending ON orders(order_id, ordered_at)
  WHERE status IN ('pending', 'confirmed');
```

### Expression Indexes

```sql
-- Index on computed column
CREATE INDEX idx_customers_lower_email ON customers(LOWER(email));

-- Enables case-insensitive search:
-- SELECT * FROM customers WHERE LOWER(email) = 'user@example.com';
```

---

## Partitioning Strategies

### Range Partitioning (Time-based)

```sql
-- PostgreSQL declarative partitioning
CREATE TABLE orders (
  order_id UUID,
  ordered_at TIMESTAMPTZ NOT NULL,
  -- columns...
) PARTITION BY RANGE (ordered_at);

-- Create monthly partitions
CREATE TABLE orders_2025_01 PARTITION OF orders
  FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');
CREATE TABLE orders_2025_02 PARTITION OF orders
  FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- Benefits: Partition pruning, faster deletes, parallel query
```

### Hash Partitioning (Even distribution)

```sql
-- Snowflake: Use CLUSTER BY for similar effect
ALTER TABLE large_table CLUSTER BY (HASH(customer_id));

-- PostgreSQL: Hash partitioning
CREATE TABLE customers_partitioned (
  customer_id UUID,
  -- columns...
) PARTITION BY HASH (customer_id);

CREATE TABLE customers_p0 PARTITION OF customers_partitioned
  FOR VALUES WITH (MODULUS 4, REMAINDER 0);
-- Create p1, p2, p3...
```

---

## Constraints & Data Integrity

### Primary Keys

```sql
-- UUID primary key (distributed systems)
customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid()

-- Auto-increment (single server)
order_id SERIAL PRIMARY KEY

-- Composite primary key
CONSTRAINT pk_order_line_items PRIMARY KEY (order_id, line_number)
```

### Foreign Keys with Referential Actions

```sql
-- Restrict delete (default)
CONSTRAINT fk_order_customer FOREIGN KEY (customer_id)
  REFERENCES customers(customer_id)
  ON DELETE RESTRICT  -- Prevent customer deletion if orders exist

-- Cascade delete (delete child records)
CONSTRAINT fk_order_lines FOREIGN KEY (order_id)
  REFERENCES orders(order_id)
  ON DELETE CASCADE  -- Delete all line items when order deleted

-- Set null (orphan records)
CONSTRAINT fk_optional_promo FOREIGN KEY (promo_code)
  REFERENCES promotions(code)
  ON DELETE SET NULL  -- Clear promo_code if promotion deleted
```

### Check Constraints

```sql
-- Value range validation
CONSTRAINT ck_order_total CHECK (order_total BETWEEN 0.01 AND 1000000)

-- Enum-like validation
CONSTRAINT ck_status CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered'))

-- Multi-column constraints
CONSTRAINT ck_dates CHECK (shipped_at IS NULL OR shipped_at >= ordered_at)
```

---

## Performance Tuning

### Table Statistics (PostgreSQL)

```sql
-- Update statistics for query planner
ANALYZE customers;

-- Set statistics target for better cardinality estimates
ALTER TABLE customers ALTER COLUMN email SET STATISTICS 1000;

-- Auto-vacuum tuning
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.05,  -- Vacuum more frequently
  autovacuum_analyze_scale_factor = 0.02
);
```

### Materialized Views

```sql
-- Pre-compute expensive aggregations
CREATE MATERIALIZED VIEW daily_sales_summary AS
SELECT
  DATE_TRUNC('day', ordered_at) as order_date,
  COUNT(*) as order_count,
  SUM(order_total) as total_revenue,
  AVG(order_total) as avg_order_value
FROM orders
WHERE status = 'delivered'
GROUP BY 1;

-- Create index on materialized view
CREATE UNIQUE INDEX idx_daily_sales_date ON daily_sales_summary(order_date);

-- Refresh materialized view
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_sales_summary;
```

---

## Storage Optimization

### Compression (Snowflake)

```sql
-- Snowflake automatically compresses
-- Typical compression ratio: 10:1 to 100:1 for text/varchar

-- Use appropriate data types to maximize compression
-- VARIANT for semi-structured data (JSON)
CREATE TABLE events (
  event_id VARCHAR(36),
  payload VARIANT  -- Auto-compressed JSON
);
```

### Column-Oriented Storage (BigQuery)

```sql
-- BigQuery automatically uses columnar storage
-- Benefits:
--   - Only scan columns used in SELECT
--   - Better compression (similar values grouped)
--   - Faster aggregations

-- Query scans only 2 columns (not full table)
SELECT event_type, COUNT(*)
FROM usage_events
WHERE DATE(event_timestamp) = '2025-01-15'
GROUP BY event_type;
```

---

**Document Owner**: Database Administration Team
**Last Updated**: 2025-01-15
