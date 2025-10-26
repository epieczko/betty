# SLA/SLO Schedules
<!-- See also: artifact_descriptions/sla-slo-schedules.md for complete guidance -->
<!-- YAML version available at: sla-slo-schedules.yaml -->

## Purpose

SLA/SLO Schedules define **Service Level Agreements** (customer-facing commitments), **Service Level Objectives** (internal reliability targets), and **Service Level Indicators** (measurable metrics) with error budgets that govern feature velocity vs. reliability trade-offs.

**Key Concepts** (Google SRE):
- **SLI** (Service Level Indicator): Quantitative measure of service level (e.g., request success rate, latency)
- **SLO** (Service Level Objective): Internal target for SLI (e.g., 99.9% success rate, p99 < 500ms)
- **SLA** (Service Level Agreement): Customer contract with consequences for breach (e.g., 99.95% uptime with service credits)
- **Error Budget**: (1 - SLO) = allowed failure rate (e.g., 99.9% SLO = 0.1% error budget = 43.2 min/month)

---

## SLA vs SLO vs SLI

| Concept | Definition | Example | Audience |
|---------|------------|---------|----------|
| **SLI** | What you measure | Request success rate, p95 latency | Internal (engineering) |
| **SLO** | Internal target | 99.9% success rate, p95 < 200ms | Internal (engineering) |
| **SLA** | Customer promise | 99.95% uptime with credits if breached | External (customers) |

**Best Practice**: Set SLO stricter than SLA to provide buffer (e.g., SLA 99.95%, SLO 99.97%)

---

## Example SLO: API Availability

**Service**: Payment API

**SLI Definition**:
```promql
# Success rate = successful requests / total requests
sum(rate(http_requests_total{service="payment-api",status=~"2..|4.."}[30d]))
/
sum(rate(http_requests_total{service="payment-api"}[30d]))
```

**SLO Target**: 99.9% success rate over 30-day window

**Error Budget**:
- **Allowed failures**: 0.1% = 43.2 minutes of downtime per 30 days
- **Error budget policy**: If budget exhausted, freeze feature releases until reliability improved

**Measurement Window**: 30-day rolling window

**SLA** (customer-facing):
- **Target**: 99.95% monthly uptime
- **Credits**: 10% for 99.5-99.95%, 25% for 99.0-99.5%, 50% for <99.0%
- **Exclusions**: Planned maintenance (< 4 hours/month, 7 days notice)

---

## Example SLO: API Latency

**Service**: API Gateway

**SLI Definition**:
```promql
# P95 latency
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds_bucket{service="api-gateway"}[5m])) by (le)
)
```

**SLO Targets**:
- **p95 latency < 200ms**: 99% of measurement windows
- **p99 latency < 500ms**: 95% of measurement windows

**Error Budget**: 1% of 5-minute windows can exceed p95 target

**Alerting** (multi-window burn rate):
- Fast burn (2-day budget exhaustion): Page on-call immediately
- Slow burn (5-day budget exhaustion): Create ticket

---

## Error Budget Policy

**Purpose**: Balance feature velocity with reliability

**When Error Budget Healthy** (>50% remaining):
- Feature releases: Normal velocity
- Risk tolerance: Can take calculated risks
- Focus: Feature development

**When Error Budget Depleted** (<10% remaining):
- Feature releases: **Freeze** (only reliability improvements)
- Risk tolerance: **Low** (no risky changes)
- Focus: Reliability work (fix bugs, improve monitoring, reduce toil)
- Duration: Until error budget recovers to 25%

**Escalation**: If error budget exhausted 2 quarters in a row, executive review required

---

## SLO Dashboard

All SLOs should have real-time dashboard showing:
- **Current SLI value** (e.g., 99.92% success rate)
- **SLO target** (e.g., 99.9%)
- **Error budget remaining** (e.g., 28.8 minutes / 43.2 minutes = 66.7% remaining)
- **Burn rate** (e.g., 2.5x = budget exhausts in 12 days)
- **Trend** (graph over last 30 days)

---

## Common SLI Categories

### Availability SLIs
- Request success rate (non-5xx responses / total requests)
- Uptime percentage (service reachable)

### Latency SLIs
- p50, p95, p99 latency (milliseconds)
- Time to First Byte (TTFB)

### Quality SLIs
- Data freshness (staleness < 5 minutes)
- Data accuracy (% correct results)

### Throughput SLIs
- Requests per second sustained
- Batch job completion rate

---

## Related Artifacts

- **YAML Version**: `sla-slo-schedules.yaml` (structured SLI/SLO/SLA definitions)
- **Alert Catalog**: `alert-catalogs.yaml` (burn rate alerts)
- **Metric Catalog**: `metric-catalog.yaml` (SLI metric definitions)

---

**Note**: See `sla-slo-schedules.yaml` for complete SLI queries, error budget calculations, and burn rate formulas. This markdown version provides conceptual overview and policy guidance.
