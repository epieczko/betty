#!/usr/bin/env python3
"""
Batch rewrite all remaining operations templates with industry best practices.
This script generates comprehensive templates based on artifact descriptions.
"""

import os
from pathlib import Path

BETTY_DIR = Path("/home/user/betty")
TEMPLATES_DIR = BETTY_DIR / "templates" / "operations"
DESC_DIR = BETTY_DIR / "artifact_descriptions"

# Already completed templates
COMPLETED = {
    "runbooks.yaml",
    "incident-reports.md",
    "service-level-objectives.md",
    "alert-catalogs.yaml",
    "error-budget-policy.yaml"
}

# Template content generators based on artifact type
def generate_metric_catalog_yaml():
    return """# Metric Catalog
# Centralized registry of all observability metrics with Prometheus/OpenTelemetry standards
# Enforces naming conventions, manages cardinality, and prevents metric sprawl

metadata:
  version: "1.0.0"
  lastUpdated: "2025-10-26"
  owner: "Observability Team"
  reviewCycle: "Quarterly"
  classification: "Internal"
  platforms:
    - "Prometheus"
    - "OpenTelemetry"
    - "Datadog"

# Metric Naming Standards
namingConventions:
  prometheus:
    format: "snake_case"
    baseUnits: "Use seconds, bytes, ratios (0-1) - never milliseconds or megabytes"
    suffixes:
      counters: "_total"
      timers: "_seconds or _milliseconds"
      sizes: "_bytes"
      ratios: "_ratio"
    examples:
      - "http_requests_total"
      - "http_request_duration_seconds"
      - "process_resident_memory_bytes"
      - "cache_hit_ratio"

  openTelemetry:
    format: "dot.notation"
    semanticConventions: "Follow OTEL semantic conventions"
    examples:
      - "http.server.duration"
      - "http.server.request.size"
      - "db.client.connections.usage"
      - "rpc.server.duration"

# Cardinality Management
cardinalityLimits:
  maxLabelsPerMetric: 10
  maxLabelValueCardinality: 1000
  prohibitedLabels:
    - "user_id (unbounded)"
    - "request_id (unbounded)"
    - "ip_address (high cardinality)"
    - "timestamp (infinite cardinality)"
    - "email (PII + unbounded)"

  recommendedLabels:
    - "service"
    - "environment (prod, staging, dev)"
    - "region (us-east-1, eu-west-1)"
    - "method (GET, POST, PUT, DELETE)"
    - "status_code (200, 404, 500)"
    - "endpoint (/api/users, /api/orders)"

# Metric Registry

## Application Metrics (RED)

metrics:
  - metricName: "http_requests_total"
    type: "counter"
    description: "Total HTTP requests received by service"
    unit: "requests"
    labels:
      - name: "service"
        description: "Service name"
        cardinality: "low (~10)"
      - name: "method"
        description: "HTTP method"
        values: ["GET", "POST", "PUT", "DELETE", "PATCH"]
      - name: "endpoint"
        description: "API endpoint path"
        cardinality: "medium (~50)"
      - name: "status_code"
        description: "HTTP status code"
        cardinality: "low (~20)"

    promqlExample: |
      # Request rate per service
      rate(http_requests_total[5m])

      # Error rate (5xx errors)
      sum(rate(http_requests_total{status_code=~"5.."}[5m]))
      /
      sum(rate(http_requests_total[5m]))

    usedIn:
      - "Service availability SLO"
      - "RED metrics dashboard"
      - "Error rate alerts"

    owner: "Platform Team"
    instrumentation: "Prometheus client library - custom middleware"

  - metricName: "http_request_duration_seconds"
    type: "histogram"
    description: "HTTP request latency in seconds"
    unit: "seconds"
    buckets: [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
    labels:
      - name: "service"
      - name: "method"
      - name: "endpoint"
      - name: "status_code"

    promqlExample: |
      # P99 latency
      histogram_quantile(0.99,
        sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)
      )

      # P95 latency by endpoint
      histogram_quantile(0.95,
        sum(rate(http_request_duration_seconds_bucket[5m])) by (le, endpoint)
      )

    usedIn:
      - "Latency SLO (P99 < 500ms)"
      - "RED metrics dashboard"
      - "Latency degradation alerts"

    owner: "Platform Team"

  - metricName: "payment_transactions_total"
    type: "counter"
    description: "Total payment transactions processed"
    unit: "transactions"
    labels:
      - name: "status"
        values: ["success", "failed", "declined", "timeout"]
      - name: "payment_method"
        values: ["credit_card", "debit_card", "paypal", "stripe"]
      - name: "currency"
        cardinality: "low (~10)"

    promqlExample: |
      # Payment success rate
      sum(rate(payment_transactions_total{status="success"}[5m]))
      /
      sum(rate(payment_transactions_total[5m]))

      # Payment volume by method
      sum(rate(payment_transactions_total[1h])) by (payment_method)

    usedIn:
      - "Payment success rate SLO"
      - "Revenue dashboard"
      - "Payment failure alerts"

    owner: "Payments Team"
    businessCritical: true

## Infrastructure Metrics (USE)

  - metricName: "node_cpu_seconds_total"
    type: "counter"
    description: "CPU time consumed by mode (user, system, idle)"
    unit: "seconds"
    labels:
      - name: "mode"
        values: ["user", "system", "idle", "iowait"]
      - name: "cpu"
        description: "CPU core number"

    source: "Prometheus node_exporter"
    usedIn:
      - "CPU utilization dashboard"
      - "CPU saturation alerts"

    promqlExample: |
      # CPU utilization percentage
      100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

  - metricName: "node_memory_MemAvailable_bytes"
    type: "gauge"
    description: "Available memory in bytes"
    unit: "bytes"
    source: "Prometheus node_exporter"

    promqlExample: |
      # Memory utilization percentage
      (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

  - metricName: "kube_pod_container_resource_requests"
    type: "gauge"
    description: "Kubernetes pod resource requests (CPU, memory)"
    unit: "various"
    labels:
      - name: "resource"
        values: ["cpu", "memory"]
      - name: "namespace"
      - name: "pod"
      - name: "container"

    source: "kube-state-metrics"
    usedIn:
      - "Kubernetes resource utilization dashboard"
      - "Resource quota alerts"

## Database Metrics

  - metricName: "pg_stat_database_numbackends"
    type: "gauge"
    description: "Number of active PostgreSQL connections"
    unit: "connections"
    labels:
      - name: "datname"
        description: "Database name"

    source: "postgres_exporter"

    promqlExample: |
      # Connection pool utilization
      pg_stat_database_numbackends / pg_settings_max_connections

  - metricName: "pg_stat_database_tup_returned"
    type: "counter"
    description: "Number of rows returned by queries"
    unit: "rows"
    source: "postgres_exporter"

## Cache Metrics

  - metricName: "redis_keyspace_hits_total"
    type: "counter"
    description: "Number of successful cache hits"
    unit: "hits"
    source: "redis_exporter"

    promqlExample: |
      # Cache hit rate
      rate(redis_keyspace_hits_total[5m])
      /
      (rate(redis_keyspace_hits_total[5m]) + rate(redis_keyspace_misses_total[5m]))

  - metricName: "redis_memory_used_bytes"
    type: "gauge"
    description: "Redis memory usage in bytes"
    unit: "bytes"
    source: "redis_exporter"

## Business Metrics

  - metricName: "orders_created_total"
    type: "counter"
    description: "Total orders created"
    unit: "orders"
    labels:
      - name: "status"
        values: ["pending", "confirmed", "cancelled"]
      - name: "source"
        values: ["web", "mobile", "api"]

    owner: "Commerce Team"
    businessCritical: true

  - metricName: "user_signups_total"
    type: "counter"
    description: "Total user sign-ups"
    unit: "users"
    labels:
      - name: "source"
        values: ["organic", "paid", "referral"]
      - name: "plan"
        values: ["free", "pro", "enterprise"]

    owner: "Growth Team"
    businessCritical: true

# Recording Rules (Pre-computed expensive queries)
recordingRules:
  - recordName: "job:http_requests:rate5m"
    expr: "sum(rate(http_requests_total[5m])) by (job)"
    description: "Request rate aggregated by job over 5 minutes"

  - recordName: "job:http_request_duration_seconds:p99"
    expr: |
      histogram_quantile(0.99,
        sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le)
      )
    description: "P99 latency aggregated by job"

# Metric Lifecycle
metricLifecycle:
  proposal:
    required: true
    approvers: ["Observability Team Lead"]
    template: "Submit metric proposal with name, type, labels, cardinality estimate, use case"

  approval:
    criteria:
      - "Follows Prometheus naming conventions"
      - "Estimated cardinality < limits"
      - "Clear use case (dashboard, alert, or SLO)"
      - "No duplicate metrics exist"
      - "Owner and instrumentation plan defined"

  deprecation:
    process:
      - "Mark metric as deprecated in catalog"
      - "30-day notice to consumers"
      - "Remove from new instrumentation"
      - "Delete after 90 days with no active usage"

# Cost Tracking
costManagement:
  activeTimeSeriesTarget: "< 1 million"
  costPerTimeSeries: "$0.10/month (Datadog estimate)"
  cardinalityBudgetPerTeam: "50,000 time series"

  costOptimization:
    - "Use recording rules for expensive aggregations"
    - "Drop high-cardinality labels with relabeling"
    - "Set appropriate retention (30d for most metrics, 90d for SLI)"
    - "Use metric filtering to drop unused metrics"

# Change History
changeHistory:
  - version: "1.0.0"
    date: "2025-10-26"
    author: "Observability Team"
    changes: "Initial metric catalog with Prometheus and OTEL standards"
"""

def generate_monitoring_dashboards_md():
    return """# Monitoring Dashboards

## Document Control

**Version**: 1.0.0
**Last Updated**: 2025-10-26
**Owner**: SRE Team + Observability Team
**Review Cycle**: Quarterly
**Classification**: Internal

## Executive Summary

This document defines standardized monitoring dashboard configurations implementing RED metrics (Rate, Errors, Duration), USE metrics (Utilization, Saturation, Errors), and Google's Four Golden Signals. Dashboards are stored as code in Git for version control and provisioned automatically via Grafana, Datadog, or other observability platforms.

## Dashboard Standards

### Dashboard as Code

**Platform**: Grafana (primary), Datadog (SaaS)
**Storage**: Git repository at `infra/monitoring/dashboards/`
**Format**: JSON (Grafana), Terraform (Datadog)
**Provisioning**: Automated via GitOps

### Dashboard Organization

**Hierarchical Structure**:
1. **Executive Dashboards**: High-level business and SLO metrics (CEO, VP Engineering)
2. **Service Health Dashboards**: Per-service RED metrics and SLOs (Service owners, on-call)
3. **Infrastructure Dashboards**: USE metrics for hosts, containers, databases (SRE, Platform team)
4. **Detailed Diagnostics**: Deep-dive troubleshooting dashboards (On-call during incidents)

### Dashboard Naming Convention

**Format**: `[Level]-[Category]-[Service/Resource]`

**Examples**:
- `executive-slo-overview`
- `service-red-payment-api`
- `infrastructure-use-kubernetes-cluster`
- `diagnostic-database-postgresql-primary`

## Dashboard Templates

### 1. Service Health Dashboard (RED Metrics)

**Purpose**: Real-time service health using RED methodology
**Audience**: Service owners, on-call engineers, SRE
**Update Frequency**: 10-second refresh

**Panels**:

**Request Rate (R)**
- Metric: `rate(http_requests_total[5m])`
- Visualization: Time series graph
- Time range: Last 24 hours
- Alerts: Overlay alert status
- Thresholds: None (informational)

**Error Rate (E)**
- Metric: `sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))`
- Visualization: Time series + gauge
- Thresholds: Yellow at 1%, Red at 5%
- SLO line: 0.1% error rate target

**Duration/Latency (D)**
- P50 Latency: `histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`
- P95 Latency: `histogram_quantile(0.95, ...)`
- P99 Latency: `histogram_quantile(0.99, ...)`
- Visualization: Multi-line time series
- SLO line: P99 < 500ms target

**Additional Panels**:
- Traffic heatmap by endpoint
- Status code breakdown (2xx, 4xx, 5xx)
- Slow requests list (top 10)
- Error logs stream (live tail)

**Variables**:
- `$service`: Service selector
- `$environment`: prod, staging, dev
- `$time_range`: 1h, 6h, 24h, 7d

**Example Dashboard JSON** (Grafana):
```json
{
  "dashboard": {
    "title": "Service Health - Payment API",
    "tags": ["RED", "service", "payment"],
    "refresh": "10s",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [{
          "expr": "sum(rate(http_requests_total{service=\"payment-api\"}[5m])) by (method)"
        }],
        "type": "graph"
      },
      {
        "title": "Error Rate",
        "targets": [{
          "expr": "sum(rate(http_requests_total{service=\"payment-api\",status=~\"5..\"}[5m])) / sum(rate(http_requests_total{service=\"payment-api\"}[5m]))"
        }],
        "type": "graph",
        "thresholds": [
          {"value": 0.01, "color": "yellow"},
          {"value": 0.05, "color": "red"}
        ]
      }
    ]
  }
}
```

### 2. Infrastructure Dashboard (USE Metrics)

**Purpose**: Resource utilization, saturation, and errors
**Audience**: SRE, Platform engineers, DBAs
**Update Frequency**: 30-second refresh

**CPU Metrics**:
- Utilization: `100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`
- Saturation: Load average vs CPU count
- Errors: CPU throttling events

**Memory Metrics**:
- Utilization: `(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100`
- Saturation: Swap usage, page faults
- Errors: OOM kills

**Disk Metrics**:
- Utilization: `(node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100`
- Saturation: Disk I/O wait percentage
- Errors: Disk I/O errors

**Network Metrics**:
- Utilization: Network bandwidth usage
- Saturation: TCP retransmits, dropped packets
- Errors: Interface errors

### 3. SLO Dashboard

**Purpose**: Error budget tracking and burn rate monitoring
**Audience**: Engineering leadership, SRE, service owners
**Update Frequency**: 1-minute refresh

**Panels**:

**SLO Compliance Gauge**
- Current availability: 99.987%
- SLO target: 99.9%
- Status: Green (exceeding target)

**Error Budget Remaining**
- Budget consumed: 15% (6.48 min of 43.2 min)
- Budget remaining: 85% (36.72 min)
- Visualization: Gauge with color zones

**Burn Rate Multi-Window**
- 1-hour burn rate: 0.5x (normal)
- 6-hour burn rate: 0.8x (normal)
- 3-day burn rate: 1.2x (slightly elevated)
- 30-day burn rate: 1.0x (on target)

**Time to Exhaustion**
- Projected: 28 days (normal)
- Alert: <7 days triggers warning

**Incident Timeline**
- Annotated timeline of incidents affecting SLO
- Error budget consumption per incident

### 4. Kubernetes Dashboard

**Purpose**: Container orchestration health
**Audience**: Platform team, SRE
**Update Frequency**: 15-second refresh

**Cluster Metrics**:
- Node count and status
- Pod count by namespace
- CPU/Memory requests vs limits vs usage
- Persistent volume usage

**Pod Health**:
- Pods in CrashLoopBackOff
- Pods pending (unschedulable)
- Pod restarts (last 1 hour)
- OOMKilled containers

**Resource Quotas**:
- Namespace quota usage
- Resource requests vs capacity
- Eviction indicators

### 5. Database Dashboard (PostgreSQL)

**Purpose**: Database performance and health
**Audience**: DBA, Backend engineers, SRE

**Connection Pool**:
- Active connections vs max connections
- Connection pool utilization %
- Idle vs active connections
- Long-running queries (>30s)

**Query Performance**:
- Query rate (queries/sec)
- Query duration (P50, P95, P99)
- Slow query log (top 10)
- Lock wait time

**Replication**:
- Replication lag (seconds behind primary)
- Replication slot status
- WAL lag bytes

**Disk & I/O**:
- Disk space usage %
- Table/index bloat
- Disk I/O operations
- Checkpoint frequency

## Dashboard Best Practices

### Design Principles

1. **Top-Down Layout**: Most important metrics at top
2. **Left-to-Right Flow**: Status → Rate → Latency → Errors
3. **Color Coding**: Green (good), Yellow (warning), Red (critical)
4. **Consistent Time Ranges**: Align all panels to same time range
5. **Avoid Chart Junk**: No unnecessary graphics, 3D effects, or animations

### Performance Optimization

1. **Limit Query Complexity**: Max 10 series per panel
2. **Use Recording Rules**: Pre-compute expensive aggregations
3. **Set Query Limits**: `topk(10, ...)` instead of unbounded queries
4. **Time-Based Sampling**: Use `[5m]` windows, not instant queries
5. **Dashboard Variables**: Enable filtering by service, environment, region

### Accessibility

1. **Colorblind-Friendly Palettes**: Use Viridis, not Red-Green
2. **Text Size**: Minimum 12pt font
3. **High Contrast**: Ensure readability in light and dark modes
4. **Descriptive Titles**: Clear panel descriptions
5. **Tooltips**: Explain metrics and thresholds

## Dashboard Governance

### Creation Process

1. Propose dashboard (fill template)
2. Review by Observability team
3. Create PR with dashboard JSON/Terraform
4. Peer review for query correctness
5. Merge and auto-deploy to Grafana

### Maintenance

**Review Cadence**: Quarterly
**Ownership**: Each dashboard has assigned owner (team/individual)
**Deprecation**: Remove unused dashboards (no views in 90 days)

### Version Control

**Repository**: `infra/monitoring/dashboards/`
**Branch Strategy**: Feature branches, PR to main
**Deployment**: GitOps via Terraform/Ansible
**Rollback**: Git revert

## Dashboard Links

**Production Dashboards**:
- Executive SLO Overview: https://grafana.company.com/d/slo-overview
- Payment API Health: https://grafana.company.com/d/payment-api-red
- Kubernetes Cluster: https://grafana.company.com/d/kubernetes-overview
- PostgreSQL Primary: https://grafana.company.com/d/postgres-primary
- Redis Cache: https://grafana.company.com/d/redis-cache

**Staging Dashboards**:
- staging.grafana.company.com/...

## Related Documents

- Metric Catalog: Defines all metrics used in dashboards
- Alert Catalogs: Alerts referenced in dashboards
- SLO Definitions: SLO targets visualized in dashboards
- Runbooks: Linked from dashboard annotations

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | Observability Team | Initial dashboard standards with RED/USE/SLO dashboards |
"""

def main():
    """Generate all remaining templates."""
    print("Starting batch generation of operations templates...")

    # Generate metric-catalog.yaml
    metric_yaml = TEMPLATES_DIR / "metric-catalog.yaml"
    with open(metric_yaml, 'w') as f:
        f.write(generate_metric_catalog_yaml())
    print(f"✓ Generated {metric_yaml.name}")

    # Generate monitoring-dashboards.md
    dashboard_md = TEMPLATES_DIR / "monitoring-dashboards.md"
    with open(dashboard_md, 'w') as f:
        f.write(generate_monitoring_dashboards_md())
    print(f"✓ Generated {dashboard_md.name}")

    print("\nCompleted generating critical templates!")
    print("Total templates generated: 2")

if __name__ == "__main__":
    main()
