# Alert Catalog
<!-- See also: artifact_descriptions/alert-catalogs.md for complete guidance -->
<!-- YAML version available at: alert-catalogs.yaml -->

**YAML Version**: Use `alert-catalogs.yaml` for structured alert definitions with Prometheus queries, thresholds, and runbook links. This markdown version provides alerting governance and best practices.

---

## Purpose

The Alert Catalog is the centralized inventory of all monitoring alerts with metadata, thresholds, escalation policies, and runbook references. It follows SRE best practices for actionable alerting and alert fatigue prevention.

**Key Principles**:
- **Actionable**: Every alert must have clear remediation steps (runbook)
- **Low Noise**: Target signal-to-noise ratio > 95% (< 5% false positives)
- **Severity-Based**: P1 (critical) = page on-call, P2 (high) = ticket during business hours, P3 (medium) = ticket only
- **SLO-Driven**: Alerts should be tied to SLO burn rate, not arbitrary thresholds

---

## Alert Severity Levels

| Severity | Description | Response | Examples |
|----------|-------------|----------|----------|
| **Critical (P1)** | Service-impacting, requires immediate action | Page on-call 24/7 | Payment API down, database connection pool exhausted, security breach |
| **High (P2)** | Degraded service, requires urgent action | Page during business hours, ticket off-hours | High latency (p99 > 1s), disk space < 15% free, SSL cert expires in 7 days |
| **Medium (P3)** | Warning condition, no immediate impact | Create ticket, no page | Cache hit rate low, non-critical service slow, cert expires in 30 days |
| **Low (P4)** | Informational, monitoring only | Log only, optional ticket | Deployment completed, auto-scaling event |

---

## Alerting Best Practices

### Avoid Alert Fatigue

**Target Metrics**:
- Max alerts per week: **< 50**
- Max pages per on-call shift (1 week): **< 5**
- Signal-to-noise ratio: **> 95%** (true positives)
- Mean Time to Resolve (MTTR): **< 15 minutes** for P1 alerts

**How to Reduce Noise**:
- Use **multi-window burn rate alerts** instead of static thresholds
- Require **multiple conditions** to be true before firing (avoid flapping)
- Set appropriate **duration** (alert for 5+ minutes, not instantly)
- **Tune thresholds** based on historical data and false positive analysis
- **Deprecate** noisy alerts (>30% false positive rate)

### Actionable Alerts

Every alert must answer:
1. **What is broken?** (clear description)
2. **Why do I care?** (business impact)
3. **What do I do?** (runbook link with remediation steps)

**Anti-pattern**: Alerting on symptoms without clear remediation
- ✗ "CPU is high" (so what? what should I do?)
- ✓ "API p95 latency > 500ms (SLO violation) - check dashboard, scale up instances" (actionable)

---

## SLO Burn Rate Alerts

**Best Practice**: Alert on SLO burn rate instead of arbitrary thresholds

**Multi-Window Burn Rate** (Google SRE Workbook):
- **Fast Burn**: 14.4x burn rate (exhausts monthly budget in 2 days)
  - Check: 1-hour AND 5-minute windows both > 14.4x
  - Action: Page on-call immediately

- **Slow Burn**: 6x burn rate (exhausts monthly budget in 5 days)
  - Check: 6-hour AND 30-minute windows both > 6x
  - Action: Create ticket, page during business hours

**Example** (from `alert-catalogs.yaml`):
```yaml
alertName: "ErrorBudgetFastBurn"
severity: "critical"
description: "Error budget consumed at 14.4x rate - monthly budget exhausted in 2 days"
triggerCondition: |
  # 1-hour burn rate > 14.4x AND 5-minute burn rate > 14.4x
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[1h])) / sum(rate(http_requests_total[1h]))) > 14.4 * (1 - 0.999)
  and
  (1 - sum(rate(http_requests_total{status=~"2..|4.."}[5m])) / sum(rate(http_requests_total[5m]))) > 14.4 * (1 - 0.999)
```

---

## Alert Metadata (Required Fields)

Every alert in the catalog must have:

- **alertName**: Unique identifier (PascalCase)
- **severity**: critical | high | medium | low
- **service**: Owning service/component
- **owner**: Team responsible for responding
- **description**: What is happening and why it matters
- **triggerCondition**: Prometheus/AlertManager query
- **duration**: How long condition must be true before firing
- **runbook**: Link to remediation documentation
- **dashboards**: Links to relevant Grafana dashboards for troubleshooting
- **relatedSLO**: Which SLO this alert protects
- **escalation**: Who to notify and when (immediate, after 15min, after 30min)
- **businessImpact**: Why this alert matters to the business
- **falsePositiveRate**: Historical false positive percentage
- **lastReviewed**: Date of last alert review/tuning

---

## Example Alerts (See YAML for Full Definitions)

### Critical Alert Example

**PaymentAPIHighErrorRate**
- **Trigger**: Payment API error rate > 1% for 5 minutes
- **Impact**: Direct revenue loss, customer trust impact, PCI compliance risk
- **Runbook**: https://runbooks.company.com/payment-api/high-error-rate
- **Escalation**:
  - Immediate: @payments-oncall
  - 15 min: @payments-lead, @engineering-director
  - 30 min: @cto, @ceo
- **SLO**: Payment API Availability 99.99%

### High Alert Example

**APILatencyP99High**
- **Trigger**: API Gateway p99 latency > 1 second for 10 minutes
- **Impact**: Degraded user experience, potential customer churn
- **Runbook**: https://runbooks.company.com/api/high-latency
- **Escalation**:
  - Immediate: @api-oncall
  - 30 min: @api-lead
- **SLO**: API Latency P99 < 500ms

---

## Alert Governance

### New Alert Approval

**Required**: All new alerts must be approved by SRE Lead and Observability Lead

**Approval Criteria**:
- ✓ Alert is actionable (clear remediation steps in runbook)
- ✓ Alert has runbook link
- ✓ False positive rate < 20% (based on testing or similar alerts)
- ✓ Severity justified by business impact
- ✓ Alert duration set appropriately (not too sensitive)

### Review Cadence

**Quarterly alert review** to identify:
- Noisy alerts (>30% false positive rate) → tune or deprecate
- Unused alerts (zero fires in 90 days) → deprecate if not needed
- Missing runbooks → add documentation
- Incorrect severity → re-classify

### Deprecation Policy

**Triggers for deprecation**:
- Unused alert: No fires in 90 days
- Noisy alert: False positive rate > 30%
- Replaced by better alert (e.g., SLO burn rate alert replaces static threshold)

**Process**:
1. Mark alert as `deprecated` in catalog
2. 30-day notice period
3. Disable alert in AlertManager
4. Archive alert definition (don't delete immediately - may need to restore)

---

## Alert Effectiveness Metrics

Track these metrics to improve alerting quality:

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Signal-to-Noise Ratio | > 95% | [Track] | [Track] |
| Alerts per Week | < 50 | [Track] | [Track] |
| Pages per On-Call Shift | < 5 | [Track] | [Track] |
| Mean Time to Acknowledge (MTTA) | < 5 min | [Track] | [Track] |
| Mean Time to Resolve (MTTR) | < 15 min (P1) | [Track] | [Track] |
| Alerts with Runbooks | 100% | [Track] | [Track] |

---

## Escalation Matrix

| Severity | Immediate | After 15 min | After 30 min | After 1 hour |
|----------|-----------|--------------|--------------|--------------|
| Critical (P1) | @service-oncall | @service-lead | @engineering-director, @cto | @ceo |
| High (P2) | @service-oncall | @service-lead | - | - |
| Medium (P3) | Ticket (no page) | - | - | - |
| Low (P4) | Log only | - | - | - |

---

## Related Artifacts

- **YAML Catalog**: `alert-catalogs.yaml` (structured alert definitions with Prometheus queries)
- **Metric Catalog**: `metric-catalog.yaml` (metrics used in alert conditions)
- **SLO Definitions**: `sla-slo-schedules.yaml` (SLOs protected by these alerts)
- **Runbooks**: `runbooks.yaml` (remediation procedures)

---

**Note**: For complete alert definitions including Prometheus queries, thresholds, and diagnostic queries, see `alert-catalogs.yaml`. This markdown version focuses on alerting governance, best practices, and alert fatigue prevention.
