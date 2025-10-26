# Tenancy And Isolation Model

> **Purpose**: Define data isolation strategies for multi-tenant systems including tenant identification, data partitioning, security boundaries, and resource allocation across shared infrastructure.
>
> **See also**: `artifact_descriptions/tenancy-and-isolation-model.md`

## Model Overview

```yaml
version: 1.0.0
tenancyModel: Single-Tenant | Multi-Tenant (Shared DB) | Multi-Tenant (Isolated DB) | Hybrid
isolationLevel: Physical | Logical | Schema | Row-Level
owner: Architecture Team
classification: Confidential
lastUpdated: 2025-01-15
```

---

## Tenancy Models Comparison

| Model | Data Isolation | Cost | Scalability | Use Case |
|-------|----------------|------|-------------|----------|
| **Single-Tenant** | Dedicated DB per customer | High | Low | Enterprise customers, regulatory requirements |
| **Multi-Tenant (Shared DB)** | Row-level security | Low | High | SMB SaaS, high volume of small tenants |
| **Multi-Tenant (Isolated DB)** | Separate DB, shared infra | Medium | Medium | Mid-market, data residency requirements |
| **Hybrid** | Mixed (tiered by customer size) | Medium | High | Enterprise + SMB customers |

---

## Example 1: Row-Level Multi-Tenancy (SaaS Platform)

### Data Model with Tenant ID

```sql
-- All tables include tenant_id for isolation
CREATE TABLE customers (
  customer_id UUID PRIMARY KEY,
  tenant_id UUID NOT NULL,  -- Foreign key to tenants table
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,

  -- Unique constraint scoped to tenant
  CONSTRAINT uk_customers_email_tenant UNIQUE (tenant_id, email)
);

-- Create index on tenant_id for query performance
CREATE INDEX idx_customers_tenant ON customers(tenant_id);

-- Tenant registry
CREATE TABLE tenants (
  tenant_id UUID PRIMARY KEY,
  tenant_name VARCHAR(255) NOT NULL,
  subscription_tier VARCHAR(50) NOT NULL,  -- free, pro, enterprise
  data_region VARCHAR(50),  -- us-east-1, eu-west-1, etc.
  max_users INTEGER,
  created_at TIMESTAMPTZ NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
);
```

### Row-Level Security (PostgreSQL)

```sql
-- Enable Row-Level Security on table
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only see their own tenant's data
CREATE POLICY tenant_isolation_policy ON customers
  FOR ALL
  TO app_user
  USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

-- Application sets tenant context
-- SET app.current_tenant_id = 'a1b2c3d4-...';

-- Queries automatically filtered by policy
SELECT * FROM customers;  -- Returns only current tenant's customers
```

### Application-Level Enforcement

```javascript
// Express.js middleware to set tenant context
const tenantMiddleware = async (req, res, next) => {
  const tenantId = req.user.tenant_id;  // From JWT or session

  // Set tenant context in database session
  await db.query('SET app.current_tenant_id = $1', [tenantId]);

  // Also filter queries explicitly (defense in depth)
  req.tenantId = tenantId;

  next();
};

// All queries include tenant_id filter
app.get('/api/customers', tenantMiddleware, async (req, res) => {
  const customers = await db.query(
    'SELECT * FROM customers WHERE tenant_id = $1',
    [req.tenantId]
  );

  res.json(customers.rows);
});
```

### Data Partitioning for Performance

```sql
-- PostgreSQL: Partition by tenant_id for large tables
CREATE TABLE orders (
  order_id UUID,
  tenant_id UUID NOT NULL,
  customer_id UUID,
  order_total DECIMAL(12,2),
  created_at TIMESTAMPTZ
) PARTITION BY LIST (tenant_id);

-- Create partition per large tenant (enterprise customers)
CREATE TABLE orders_tenant_a1b2c3d4 PARTITION OF orders
  FOR VALUES IN ('a1b2c3d4-e5f6-...');

-- Small tenants share partitions
CREATE TABLE orders_tenant_default PARTITION OF orders
  DEFAULT;
```

---

## Example 2: Schema-Level Multi-Tenancy

### Dedicated Schema Per Tenant

```sql
-- Create schema for each tenant
CREATE SCHEMA tenant_acme_corp;
CREATE SCHEMA tenant_globex_inc;

-- Identical table structure in each schema
CREATE TABLE tenant_acme_corp.customers (
  customer_id UUID PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  -- No tenant_id needed (schema provides isolation)
  created_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE tenant_globex_inc.customers (
  customer_id UUID PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMPTZ NOT NULL
);

-- Application routes queries to correct schema
SET search_path TO tenant_acme_corp;
SELECT * FROM customers;  -- Queries tenant_acme_corp.customers
```

**Advantages**:
- Simpler queries (no tenant_id in WHERE clauses)
- Easier to backup/restore single tenant
- Better query plan caching

**Disadvantages**:
- Schema migrations must run on ALL schemas
- Cross-tenant analytics complex
- Database connection limits (1 connection per schema)

---

## Example 3: Database-Level Multi-Tenancy (Snowflake)

### Isolated Database Per Tenant

```sql
-- Create dedicated database for each tenant
CREATE DATABASE tenant_acme_corp;
CREATE DATABASE tenant_globex_inc;

-- Shared reference data (in centralized database)
CREATE DATABASE shared_reference_data;

-- Grant access to tenant databases
GRANT USAGE ON DATABASE tenant_acme_corp TO ROLE tenant_acme_corp_role;

-- Tenant-specific virtual warehouse (compute isolation)
CREATE WAREHOUSE tenant_acme_corp_wh
  WITH WAREHOUSE_SIZE = 'MEDIUM'
       AUTO_SUSPEND = 300
       AUTO_RESUME = TRUE;

GRANT USAGE ON WAREHOUSE tenant_acme_corp_wh TO ROLE tenant_acme_corp_role;
```

**Resource Quotas**:
```sql
-- Set resource limits per tenant
ALTER WAREHOUSE tenant_acme_corp_wh
  SET RESOURCE_MONITOR = acme_corp_monthly_limit;

CREATE RESOURCE MONITOR acme_corp_monthly_limit
  WITH CREDIT_QUOTA = 1000  -- Max 1000 credits/month
       TRIGGERS
         ON 75 PERCENT DO NOTIFY
         ON 90 PERCENT DO SUSPEND
         ON 100 PERCENT DO SUSPEND_IMMEDIATE;
```

---

## Tenant Identification Strategies

### 1. Subdomain-Based

```
https://acme.app.com      -> tenant: acme
https://globex.app.com    -> tenant: globex
```

```javascript
// Extract tenant from subdomain
const getTenantFromSubdomain = (req) => {
  const host = req.headers.host;  // acme.app.com
  const subdomain = host.split('.')[0];
  return await Tenant.findOne({ subdomain });
};
```

### 2. Path-Based

```
https://app.com/acme/dashboard    -> tenant: acme
https://app.com/globex/dashboard  -> tenant: globex
```

### 3. Header-Based

```http
GET /api/customers HTTP/1.1
Host: api.app.com
X-Tenant-ID: acme-corp
Authorization: Bearer <token>
```

### 4. Token-Based (JWT)

```javascript
// JWT payload includes tenant_id
{
  "user_id": "user-123",
  "tenant_id": "acme-corp",
  "role": "admin",
  "exp": 1735689600
}
```

---

## Cross-Tenant Data Access

### Controlled Cross-Tenant Queries (Analytics)

```sql
-- Dedicated analytics role can query across tenants
CREATE ROLE analytics_admin;

-- Grant SELECT on all tenant data
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analytics_admin;

-- Analytics queries aggregate across tenants
SELECT
  tenant_id,
  COUNT(*) as customer_count,
  AVG(lifetime_value) as avg_ltv
FROM customers
WHERE is_active = TRUE
GROUP BY tenant_id;
```

### Data Sharing (Snowflake Secure Data Sharing)

```sql
-- Create secure share for tenant data export
CREATE SHARE acme_corp_data_share;

-- Add database to share
GRANT USAGE ON DATABASE tenant_acme_corp TO SHARE acme_corp_data_share;
GRANT SELECT ON ALL TABLES IN SCHEMA tenant_acme_corp.public TO SHARE acme_corp_data_share;

-- Share with external Snowflake account (customer's own account)
ALTER SHARE acme_corp_data_share ADD ACCOUNTS = external_account_123;
```

---

## Data Residency & Compliance

### Geographic Data Isolation

```yaml
tenant_data_residency:
  acme_corp:
    region: us-east-1
    database: tenant_acme_corp_us
    compliance: HIPAA, SOC 2

  european_customer:
    region: eu-west-1
    database: tenant_european_customer_eu
    compliance: GDPR
    data_transfer_restrictions:
      - No cross-region replication
      - No US-based analytics processing
```

### Encryption Isolation

```sql
-- Tenant-specific encryption keys (AWS KMS)
CREATE DATABASE tenant_acme_corp
  ENCRYPTION_CONFIGURATION = {
    kmsKeyArn: 'arn:aws:kms:us-east-1:123456789:key/acme-corp-key'
  };

-- Different key per tenant for compliance
CREATE DATABASE tenant_globex_inc
  ENCRYPTION_CONFIGURATION = {
    kmsKeyArn: 'arn:aws:kms:us-east-1:123456789:key/globex-inc-key'
  };
```

---

## Tenant Lifecycle Management

### Tenant Provisioning

```python
def provision_new_tenant(tenant_name, tier='pro'):
    """Provision database resources for new tenant."""

    tenant_id = generate_uuid()

    # Create tenant record
    db.execute('''
        INSERT INTO tenants (tenant_id, tenant_name, subscription_tier)
        VALUES ($1, $2, $3)
    ''', [tenant_id, tenant_name, tier])

    # Schema-level multi-tenancy
    if tier == 'enterprise':
        # Create dedicated schema
        db.execute(f'CREATE SCHEMA tenant_{tenant_id}')

        # Run schema migrations
        run_migrations(schema=f'tenant_{tenant_id}')

    # Create default admin user
    create_admin_user(tenant_id, email=f'admin@{tenant_name}.com')

    # Initialize sample data
    if tier != 'enterprise':
        load_sample_data(tenant_id)

    return tenant_id
```

### Tenant Offboarding

```python
def offboard_tenant(tenant_id, retention_days=90):
    """Soft-delete tenant data with retention period."""

    # Soft delete (mark inactive)
    db.execute('''
        UPDATE tenants
        SET is_active = FALSE, deleted_at = NOW()
        WHERE tenant_id = $1
    ''', [tenant_id])

    # Schedule data purge after retention period
    schedule_task(
        task='purge_tenant_data',
        args={'tenant_id': tenant_id},
        eta=datetime.now() + timedelta(days=retention_days)
    )

    # Export tenant data for compliance
    export_tenant_data(tenant_id, destination=f's3://backups/{tenant_id}/')
```

---

## Performance & Scalability

### Connection Pooling

```javascript
// Tenant-aware connection pool
const { Pool } = require('pg');

const tenantPools = new Map();

function getPoolForTenant(tenantId) {
  if (!tenantPools.has(tenantId)) {
    tenantPools.set(tenantId, new Pool({
      max: 20,  // Max connections per tenant
      schema: `tenant_${tenantId}`,
    }));
  }

  return tenantPools.get(tenantId);
}
```

### Caching Strategy

```javascript
// Tenant-scoped cache keys
const cacheKey = `tenant:${tenantId}:customers:${customerId}`;

// Redis HASH per tenant
HSET tenant:acme-corp:customers customer-123 '{"name":"Alice",...}'

// Automatic cache invalidation on tenant data changes
```

### Monitoring Per Tenant

```sql
-- Query performance by tenant
SELECT
  tenant_id,
  COUNT(*) as query_count,
  AVG(duration_ms) as avg_duration,
  MAX(duration_ms) as max_duration
FROM query_logs
WHERE timestamp > NOW() - INTERVAL '1 hour'
GROUP BY tenant_id
ORDER BY query_count DESC;
```

---

## Security Best Practices

1. **Defense in Depth**: Enforce tenant isolation at application AND database level
2. **Least Privilege**: Grant minimum necessary permissions per tenant role
3. **Audit Logging**: Log all cross-tenant data access attempts
4. **Regular Testing**: Automated tests to verify tenant isolation
5. **Code Review**: Require approval for any cross-tenant queries

---

## Testing Tenant Isolation

```python
import pytest

def test_tenant_isolation():
    """Verify tenant A cannot access tenant B's data."""

    # Create test data for two tenants
    tenant_a_customer = create_customer(tenant_id='tenant-a', email='user@a.com')
    tenant_b_customer = create_customer(tenant_id='tenant-b', email='user@b.com')

    # Authenticate as tenant A
    session = login_as_tenant('tenant-a')

    # Query should only return tenant A's data
    customers = session.query(Customer).all()

    assert len(customers) == 1
    assert customers[0].tenant_id == 'tenant-a'
    assert tenant_b_customer not in customers  # Isolation verified

def test_rls_policy():
    """Verify Row-Level Security policy enforcement."""

    # Set tenant context
    db.execute("SET app.current_tenant_id = 'tenant-a'")

    # Query should be automatically filtered
    result = db.execute("SELECT * FROM customers")

    # All rows must belong to tenant-a
    for row in result:
        assert row['tenant_id'] == 'tenant-a'
```

---

**Document Owner**: Architecture Team
**Last Updated**: 2025-01-15
