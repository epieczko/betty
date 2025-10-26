# Metric Catalog
<!-- See also: artifact_descriptions/metric-catalog.md for complete guidance -->
<!-- YAML version available at: metric-catalog.yaml -->

**YAML Version**: Use `metric-catalog.yaml` for structured metric definitions, Prometheus/OpenTelemetry queries, and automated processing. This markdown version provides narrative documentation and governance policies.

---

## Purpose

The Metric Catalog is the centralized registry of all observability metrics following Prometheus and OpenTelemetry naming conventions. It enforces naming standards, manages cardinality, prevents metric sprawl, and enables metric governance.

**Key Benefits**:
- **Standardization**: Consistent metric naming (snake_case for Prometheus, dot.notation for OTel)
- **Cardinality Control**: Prevent high-cardinality explosions that drive up costs
- **Discoverability**: Single source of truth for all metrics, their purpose, and usage
- **Cost Management**: Track and optimize observability costs (time series limits, retention policies)

---

## Metric Naming Standards

### Prometheus Conventions

**Format**: `snake_case`

**Base Units**: Always use base units (seconds, bytes, ratios 0-1) - never milliseconds or megabytes

**Suffixes**:
- Counters: `_total`
- Timers: `_seconds` or `_milliseconds`
- Sizes: `_bytes`
- Ratios: `_ratio`

**Examples**:
- `http_requests_total` ✓
- `http_request_duration_seconds` ✓
- `process_resident_memory_bytes` ✓
- `cache_hit_ratio` ✓

**Anti-patterns**:
- `httpRequests` ✗ (camelCase)
- `http_request_duration_ms` ✗ (should use `_seconds`)
- `memory_mb` ✗ (should use `_bytes`)

### OpenTelemetry Semantic Conventions

**Format**: `dot.notation`

**Follow OTEL semantic conventions**: https://opentelemetry.io/docs/specs/semconv/

**Examples**:
- `http.server.duration`
- `http.server.request.size`
- `db.client.connections.usage`
- `rpc.server.duration`

---

## Cardinality Management

**Limits**:
- Max labels per metric: **10**
- Max label value cardinality: **1,000**
- Active time series budget: **< 1 million** (organization-wide)
- Cost per time series: **~$0.10/month** (Datadog estimate)

**Prohibited High-Cardinality Labels**:
- ✗ `user_id` (unbounded)
- ✗ `request_id` (unbounded)
- ✗ `ip_address` (high cardinality)
- ✗ `timestamp` (infinite cardinality)
- ✗ `email` (PII + unbounded)

**Recommended Low-Cardinality Labels**:
- ✓ `service` (~10 values)
- ✓ `environment` (prod, staging, dev)
- ✓ `region` (us-east-1, eu-west-1, etc.)
- ✓ `method` (GET, POST, PUT, DELETE)
- ✓ `status_code` (200, 404, 500, etc.)
- ✓ `endpoint` (/api/users, /api/orders - keep bounded)

---

## Metric Categories

### Application Metrics (RED Method)

**RED** = Rate, Errors, Duration (Google SRE best practice for request-driven services)

**Example Metrics**:
- `http_requests_total` (counter) - Request rate
- `http_requests_errors_total{status=~"5.."}` (counter) - Error rate
- `http_request_duration_seconds` (histogram) - Request latency/duration

### Infrastructure Metrics (USE Method)

**USE** = Utilization, Saturation, Errors (for resource monitoring)

**Example Metrics**:
- `node_cpu_seconds_total` (counter) - CPU utilization
- `node_memory_MemAvailable_bytes` (gauge) - Memory utilization
- `node_disk_io_time_seconds_total` (counter) - Disk saturation

### Business Metrics

**Example Metrics**:
- `orders_created_total{status="confirmed"}` (counter)
- `payment_transactions_total{status="success"}` (counter)
- `user_signups_total{plan="pro"}` (counter)
- `revenue_dollars_total{currency="USD"}` (counter)

See `metric-catalog.yaml` for complete metric definitions with PromQL examples.

---

## Metric Lifecycle

### Proposal & Approval

**Before creating a new metric**:
1. Check if similar metric already exists in catalog
2. Submit metric proposal to Observability Team
3. Include: name, type, labels, estimated cardinality, use case (dashboard/alert/SLO)
4. Approval required from Observability Team Lead

**Approval Criteria**:
- ✓ Follows Prometheus/OTel naming conventions
- ✓ Estimated cardinality < limits
- ✓ Clear use case documented (dashboard, alert, or SLO)
- ✓ No duplicate metrics exist
- ✓ Owner and instrumentation plan defined

### Deprecation

**When to deprecate**:
- Metric no longer used (no active dashboards/alerts referencing it)
- Replaced by better alternative
- High cardinality causing cost issues

**Deprecation Process**:
1. Mark metric as `deprecated` in catalog
2. 30-day notice to consumers (Slack announcement, documentation update)
3. Remove from new instrumentation (stop emitting)
4. Delete after 90 days with zero active usage

---

## Cost Management

**Active Time Series Target**: < 1 million (organization-wide)

**Cost per Time Series**: ~$0.10/month (Datadog), $0.05/month (Prometheus in AWS)

**Cardinality Budget per Team**: 50,000 time series

**Cost Optimization Strategies**:
- Use **recording rules** for expensive aggregations (pre-compute at write time)
- **Drop high-cardinality labels** with relabeling rules
- Set appropriate **retention**: 30 days for most metrics, 90 days for SLI metrics
- Use **metric filtering** to drop unused metrics before they reach storage

---

## PromQL Examples (from YAML catalog)

### Request Rate
```promql
# Requests per second, last 5 minutes
rate(http_requests_total[5m])
```

### Error Rate
```promql
# Percentage of 5xx errors
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

### P99 Latency
```promql
# 99th percentile latency by service
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)
)
```

### Cache Hit Rate
```promql
rate(redis_keyspace_hits_total[5m])
/
(rate(redis_keyspace_hits_total[5m]) + rate(redis_keyspace_misses_total[5m]))
```

---

## Recording Rules

Pre-compute expensive queries for faster dashboard rendering:

```yaml
# Example recording rule (defined in metric-catalog.yaml)
- record: job:http_requests:rate5m
  expr: sum(rate(http_requests_total[5m])) by (job)

- record: job:http_request_duration_seconds:p99
  expr: |
    histogram_quantile(0.99,
      sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le)
    )
```

---

## Governance

**Metric Ownership**: Every metric must have a designated team owner responsible for instrumentation, accuracy, and lifecycle management.

**Review Cadence**: Quarterly metric catalog review to identify unused metrics, optimize cardinality, and update documentation.

**Instrumentation Standards**:
- Use official Prometheus client libraries (avoid custom implementations)
- Instrument at application boundaries (HTTP, gRPC, database calls)
- Use middleware for automatic instrumentation (avoid manual instrumentation scattered in code)

---

## Related Artifacts

- **YAML Catalog**: `metric-catalog.yaml` (structured metrics with PromQL queries)
- **Alert Catalog**: `alert-catalogs.yaml` (alerts referencing these metrics)
- **SLO Definitions**: `sla-slo-schedules.yaml` (SLIs using these metrics)
- **Dashboards**: Grafana dashboards (link in each metric's `usedIn` field)

---

**Note**: For complete metric definitions including labels, PromQL examples, and usage documentation, see `metric-catalog.yaml`. This markdown version focuses on governance, naming standards, and cardinality management policies.
