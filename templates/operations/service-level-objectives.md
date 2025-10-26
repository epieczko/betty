# Service Level Objectives (SLOs)

## Document Control

**Version**: 1.0.0
**Last Updated**: 2025-10-26
**Owner**: SRE Team
**Review Cycle**: Quarterly
**Classification**: Internal

## Executive Summary

This document defines Service Level Objectives (SLOs), Service Level Indicators (SLIs), and error budget policies for our services. SLOs establish measurable reliability targets that balance feature velocity with system stability using Google SRE methodology.

## SLO Framework

### SLO Tiers

| Tier | Availability | Monthly Downtime | Use Case | Example Services |
|------|-------------|------------------|----------|------------------|
| Tier 0 - Critical | 99.99% | 4.3 minutes | Revenue-critical, user-facing | Payment API, Authentication |
| Tier 1 - High | 99.9% | 43.2 minutes | Core user experience | Product Catalog, Search |
| Tier 2 - Standard | 99.5% | 3.6 hours | Internal tools, batch jobs | Admin Dashboard, Reports |
| Tier 3 - Best Effort | 99.0% | 7.2 hours | Development, testing | Staging Environment |

### Measurement Window

**Standard Window**: 30-day rolling window
**Compliance Calculation**: Total good requests / total valid requests over 30 days
**Data Completeness Requirement**: >95% data availability for valid SLO measurement

## Service SLO Definitions

### 1. Payment Processing API (Tier 0)

**Service**: payment-api
**Owner**: Payments Team (@payments-team)
**Business Impact**: Direct revenue impact, regulatory compliance (PCI-DSS)

#### Availability SLI/SLO

**SLI Definition**: Percentage of successful API requests (HTTP 2xx, 4xx) vs total requests
```promql
sum(rate(http_requests_total{service="payment-api",status=~"2..|4.."}[5m]))
/
sum(rate(http_requests_total{service="payment-api"}[5m]))
```

**SLO Target**: 99.99% availability
**Error Budget**: 0.01% = 4.3 minutes/month = 25,920 failed requests/month (@ 6M requests/month)

**Exclusions**:
- Planned maintenance (with 72h notice)
- Upstream payment gateway failures (Stripe, PayPal outages)
- Client errors (HTTP 4xx except 429 rate limiting)
- DDoS attacks and abuse traffic

#### Latency SLO

**SLI Definition**: P99 API response time < 500ms
```promql
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket{service="payment-api"}[5m])) by (le)
)
```

**SLO Target**: 99% of requests complete in < 500ms
**Error Budget**: 1% of requests may exceed 500ms

#### Error Rate SLO

**SLI Definition**: Percentage of 5xx errors
```promql
sum(rate(http_requests_total{service="payment-api",status=~"5.."}[5m]))
/
sum(rate(http_requests_total{service="payment-api"}[5m]))
```

**SLO Target**: <0.1% error rate
**Error Budget**: 0.1% = 6,000 errors/month

### 2. User Authentication Service (Tier 0)

**Service**: auth-service
**Owner**: Platform Team (@platform-team)
**Business Impact**: Blocks all user access, cascading failure to all services

#### Availability SLI/SLO

**SLI Definition**: Successful authentication attempts vs total attempts
```promql
sum(rate(auth_attempts_total{service="auth-service",result="success"}[5m]))
/
sum(rate(auth_attempts_total{service="auth-service"}[5m]))
```

**SLO Target**: 99.99% availability
**Error Budget**: 4.3 minutes/month

**Exclusions**:
- Invalid credentials (user error, not system failure)
- Account lockouts (security feature)
- MFA verification delays (third-party dependency)

#### Latency SLO

**SLI Definition**: P95 authentication latency < 200ms
```promql
histogram_quantile(0.95,
  sum(rate(auth_duration_seconds_bucket{service="auth-service"}[5m])) by (le)
)
```

**SLO Target**: 95th percentile < 200ms
**Error Budget**: 5% of requests may exceed 200ms

### 3. Product Search API (Tier 1)

**Service**: search-api
**Owner**: Search Team (@search-team)
**Business Impact**: Core discovery experience, affects conversion rate

#### Availability SLI/SLO

**SLI Definition**: Successful search queries vs total queries
```promql
sum(rate(search_requests_total{service="search-api",status="success"}[5m]))
/
sum(rate(search_requests_total{service="search-api"}[5m]))
```

**SLO Target**: 99.9% availability
**Error Budget**: 43.2 minutes/month = 720 seconds

#### Latency SLO

**SLI Definition**: P99 search latency < 1 second
```promql
histogram_quantile(0.99,
  sum(rate(search_latency_seconds_bucket{service="search-api"}[5m])) by (le)
)
```

**SLO Target**: 99% of searches complete in < 1 second

#### Freshness SLO

**SLI Definition**: Product index lag < 5 minutes
```promql
max(time() - search_index_last_updated_timestamp_seconds{service="search-api"})
```

**SLO Target**: Index freshness < 5 minutes for 99% of time

## Error Budget Policy

### Error Budget Calculation

**Formula**:
```
Error Budget Remaining = (1 - Error Rate) - SLO Target
Error Budget Consumed = 1 - (Error Budget Remaining / Total Error Budget)
```

**Example** (99.9% SLO):
- SLO Target: 99.9% (43.2 min/month downtime allowed)
- Current Availability: 99.85%
- Downtime: 64.8 minutes
- Error Budget Consumed: 150% (1.5x budget exhausted)

### Burn Rate Thresholds

| Window | Burn Rate | Budget Consumed | Action | Alert Severity |
|--------|-----------|-----------------|--------|----------------|
| 1 hour | 14.4x | Exhausts monthly budget in 2 days | Page on-call | Critical |
| 6 hours | 6x | Exhausts monthly budget in 5 days | Page on-call | High |
| 3 days | 1x | Normal consumption rate | Ticket | Medium |
| 30 days | Cumulative | Monthly status | Dashboard | Info |

### Multi-Window Multi-Burn-Rate Alerts

**Fast Burn Alert** (1 hour window):
```promql
(
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[1h])) / sum(rate(http_requests_total[1h])))
  > 14.4 * (1 - 0.999)
)
and
(
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[5m])) / sum(rate(http_requests_total[5m])))
  > 14.4 * (1 - 0.999)
)
```

**Slow Burn Alert** (6 hour window):
```promql
(
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[6h])) / sum(rate(http_requests_total[6h])))
  > 6 * (1 - 0.999)
)
and
(
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[30m])) / sum(rate(http_requests_total[30m])))
  > 6 * (1 - 0.999)
)
```

### Error Budget Policy Actions

#### Error Budget > 25% Remaining
- **Status**: Healthy
- **Actions**:
  - Normal feature development velocity
  - Proactive reliability improvements encouraged
  - Launch new features without restrictions

#### Error Budget 10-25% Remaining
- **Status**: Warning
- **Actions**:
  - Increased deployment scrutiny
  - Require canary deployments for risky changes
  - Prioritize SLO-impacting bugs
  - SRE review for architectural changes

#### Error Budget 0-10% Remaining
- **Status**: Critical
- **Actions**:
  - Deployment freeze for non-critical features
  - Only SLO improvement and critical bug fixes allowed
  - Mandatory SRE approval for all deploys
  - Daily error budget review meetings
  - Root cause analysis for all incidents

#### Error Budget Exhausted (< 0%)
- **Status**: Emergency
- **Actions**:
  - Complete deployment freeze (except emergency fixes)
  - All engineering effort on reliability
  - Required postmortem for all incidents
  - Executive stakeholder notification
  - Error budget postmortem to identify systemic issues
  - Reset only after reliability improvements proven

### Postmortem Requirements

| Error Budget Consumed | Postmortem Required | Timeline | Attendees |
|----------------------|---------------------|----------|-----------|
| < 5% | Optional | N/A | Team discretion |
| 5-10% | Recommended | Within 5 days | Service team |
| 10-25% | Required | Within 3 days | Service team + SRE |
| > 25% | Required + Executive Review | Within 48 hours | Service team + SRE + Leadership |

## SLO Review and Maintenance

### Quarterly SLO Review

**Review Checklist**:
- [ ] Analyze actual performance vs SLO targets
- [ ] Review error budget consumption patterns
- [ ] Assess SLO achievability (too tight or too loose)
- [ ] Validate SLI measurement accuracy
- [ ] Update SLO targets based on business requirements
- [ ] Review and update exclusions
- [ ] Assess user impact correlation with SLO violations
- [ ] Update alert thresholds and runbooks

### SLO Adjustment Criteria

**Tighten SLO** (increase target) when:
- Actual performance consistently exceeds SLO by >1% for 3 months
- Business requirements demand higher reliability
- User feedback indicates reliability issues despite meeting SLO

**Loosen SLO** (decrease target) when:
- Consistently failing to meet SLO (< 80% compliance)
- SLO not aligned with user experience
- Cost of achieving SLO exceeds business value

### SLA Alignment

**SLO-to-SLA Buffer**: Internal SLOs must be stricter than customer-facing SLAs

| Service | Internal SLO | Customer SLA | Buffer |
|---------|-------------|--------------|--------|
| Payment API | 99.99% | 99.9% | 0.09% |
| Auth Service | 99.99% | 99.95% | 0.04% |
| Search API | 99.9% | 99.5% | 0.4% |

**Buffer Purpose**: Prevents SLA breaches even when consuming error budget

## SLO Tooling and Automation

### Monitoring Stack

**Metrics Platform**: Prometheus + Grafana
**SLO Tracking**: Grafana SLO Plugin, Sloth (SLO generator)
**Alerting**: Prometheus AlertManager → PagerDuty
**Dashboards**: Grafana SLO dashboards with error budget burn rate

### SLO Dashboard Components

1. **Current SLO Compliance**: Real-time compliance percentage
2. **Error Budget Remaining**: Visual gauge (green/yellow/red)
3. **Burn Rate**: 1h, 6h, 3d, 30d windows
4. **Time to Exhaustion**: Projected days until budget exhausted
5. **Historical Trends**: 90-day SLO compliance chart
6. **Incident Correlation**: SLO drops correlated with incidents

### Automated Reports

**Daily**: Error budget status email to service owners
**Weekly**: SLO compliance summary to engineering leadership
**Monthly**: Executive SLO report with trends and action items

## Related Documents

- **Alert Catalogs**: Alert definitions and runbook links
- **Incident Management Plan**: Incident response procedures
- **Error Budget Policy**: Detailed policy enforcement
- **Postmortem Template**: Incident analysis format
- **Monitoring Dashboards**: SLO visualization dashboards

## Appendix: SLO Calculation Examples

### Availability Calculation

**Scenario**: Payment API over 30 days
- Total requests: 10,000,000
- Successful requests (2xx, 4xx): 9,998,500
- Failed requests (5xx): 1,500
- Availability: 9,998,500 / 10,000,000 = 99.985%
- SLO Target: 99.99%
- Error Budget: 0.01% = 1,000 failed requests
- Actual Errors: 1,500
- Error Budget Consumed: 150% (exhausted)

### Latency SLO Calculation

**Scenario**: Search API P99 latency
- 1,000,000 requests in 30 days
- P99 threshold: 1 second
- Requests > 1s: 15,000 (1.5%)
- SLO Target: 99% under 1s (1% allowed to exceed)
- Error Budget: 10,000 slow requests
- Actual Slow: 15,000
- Error Budget Consumed: 150% (exhausted)

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | SRE Team | Initial SLO definitions for Tier 0 and Tier 1 services |
