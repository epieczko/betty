#!/usr/bin/env python3
"""
Comprehensive specialized template library for major artifact types.
Each function returns an industry-standard template.
"""

def slo_template(name):
    """Service Level Objectives with SLI/SLO/SLA and error budgets."""
    return """# Service Level Objectives (SLOs)
# See also: artifact_descriptions/service-level-objectives.md

metadata:
  version: "1.0.0"
  created: "YYYY-MM-DD"
  lastModified: "YYYY-MM-DD"
  owner: "Platform Engineering Team"
  status: "Approved"

# SERVICE INFORMATION
service:
  name: "API Service"
  description: "Core REST API serving customer requests"
  tier: "Critical"  # Critical | High | Medium | Low
  owner: "Platform Team"
  repository: "https://github.com/org/api-service"

# SERVICE LEVEL INDICATORS (SLIs)
# SLIs are carefully chosen metrics that measure service health
slis:
  - name: "Availability"
    description: "Percentage of successful requests"
    type: "availability"
    measurement:
      query: "sum(rate(http_requests_total{status!~'5..'}[5m])) / sum(rate(http_requests_total[5m]))"
      dataSource: "Prometheus"
      unit: "percentage"
    thresholds:
      good: ">= 99.9%"
      acceptable: ">= 99.5%"
      poor: "< 99.5%"

  - name: "Latency"
    description: "95th percentile response time"
    type: "latency"
    measurement:
      query: "histogram_quantile(0.95, http_request_duration_seconds_bucket)"
      dataSource: "Prometheus"
      unit: "seconds"
    thresholds:
      good: "< 200ms"
      acceptable: "< 500ms"
      poor: ">= 500ms"

  - name: "Error Rate"
    description: "Percentage of requests resulting in 5xx errors"
    type: "correctness"
    measurement:
      query: "sum(rate(http_requests_total{status=~'5..'}[5m])) / sum(rate(http_requests_total[5m]))"
      dataSource: "Prometheus"
      unit: "percentage"
    thresholds:
      good: "< 0.1%"
      acceptable: "< 1%"
      poor: ">= 1%"

# SERVICE LEVEL OBJECTIVES (SLOs)
# SLOs define target reliability over a time window
slos:
  - name: "Monthly Availability Target"
    description: "Service availability over 30-day rolling window"
    sli: "Availability"
    target: "99.9%"
    timeWindow: "30d"
    
    errorBudget:
      total: "0.1%"  # 100% - 99.9% = 0.1%
      calculation: "43.2 minutes of downtime per 30 days"
      remaining: "Tracked in real-time dashboard"
      consumptionRate: "Monitor error budget burn rate"
    
    alerting:
      - condition: "Error budget < 25% remaining"
        severity: "Warning"
        action: "Review recent changes, consider freezing non-critical deployments"
      
      - condition: "Error budget < 10% remaining"
        severity: "Critical"
        action: "Freeze all deployments, focus on reliability"
    
    consequences:
      budgetExhausted: "Deployment freeze until next period or budget replenished"
      budgetHealthy: "Normal deployment cadence permitted"

  - name: "Request Latency Target"
    description: "95% of requests complete within 200ms"
    sli: "Latency"
    target: "95% < 200ms"
    timeWindow: "7d"
    
    errorBudget:
      total: "5%"  # 5% of requests can exceed 200ms
      calculation: "5% of total requests per week"
    
    alerting:
      - condition: "P95 latency > 200ms for 10 minutes"
        severity: "Warning"
        action: "Investigate performance degradation"
    
      - condition: "P95 latency > 500ms for 5 minutes"
        severity: "Critical"
        action: "Page on-call engineer immediately"

  - name: "Error Rate Target"
    description: "Error rate below 0.1%"
    sli: "Error Rate"
    target: "< 0.1%"
    timeWindow: "7d"
    
    errorBudget:
      total: "0.1%"
      calculation: "Max 0.1% error rate sustained"
    
    alerting:
      - condition: "Error rate > 0.5% for 5 minutes"
        severity: "Critical"
        action: "Immediate investigation and potential rollback"

# SERVICE LEVEL AGREEMENTS (SLAs)
# SLAs are external commitments to customers with consequences
slas:
  - name: "Enterprise Tier Availability"
    description: "Guaranteed uptime for enterprise customers"
    target: "99.95%"
    timeWindow: "monthly"
    customerTiers: ["Enterprise", "Premium"]
    
    consequences:
      - condition: "Availability < 99.95%"
        penalty: "10% service credit"
      - condition: "Availability < 99.9%"
        penalty: "25% service credit"
      - condition: "Availability < 99.5%"
        penalty: "50% service credit"
    
    exclusions:
      - "Scheduled maintenance windows (notified 7 days in advance)"
      - "Customer-caused outages"
      - "Force majeure events"
      - "DDoS attacks (beyond reasonable protection)"

  - name: "Standard Tier Availability"
    description: "Guaranteed uptime for standard customers"
    target: "99.5%"
    timeWindow: "monthly"
    customerTiers: ["Standard"]
    
    consequences:
      - condition: "Availability < 99.5%"
        penalty: "5% service credit"

# ERROR BUDGET POLICY
errorBudgetPolicy:
  purpose: |
    Error budget policy defines how we balance velocity (new features) 
    with reliability (service stability) using data-driven decisions.
  
  budgetCalculation:
    method: "SLO-based"
    formula: "Error Budget = 100% - SLO Target"
    example: "For 99.9% SLO, error budget is 0.1% (43.2 min/month)"
  
  actionThresholds:
    - budgetRemaining: "> 75%"
      state: "Healthy"
      actions:
        - "Normal deployment velocity"
        - "Accept calculated risks"
        - "Focus on new features"
    
    - budgetRemaining: "25% - 75%"
      state: "Cautious"
      actions:
        - "Increase testing rigor"
        - "Prioritize reliability improvements"
        - "Limit high-risk changes"
    
    - budgetRemaining: "10% - 25%"
      state: "Warning"
      actions:
        - "Freeze non-critical deployments"
        - "Focus on reliability fixes only"
        - "Conduct incident review"
        - "Implement corrective actions"
    
    - budgetRemaining: "< 10%"
      state: "Critical"
      actions:
        - "Complete deployment freeze"
        - "War room for reliability"
        - "Executive notification"
        - "Postmortem required before resuming"

  burnRateAlerts:
    - window: "1 hour"
      threshold: "14.4x normal rate"
      action: "Page immediately - rapid budget consumption"
    
    - window: "6 hours"
      threshold: "6x normal rate"
      action: "Alert on-call - elevated consumption"
    
    - window: "24 hours"
      threshold: "3x normal rate"
      action: "Notify team - sustained elevated consumption"

# MONITORING & REPORTING
monitoring:
  dashboards:
    - name: "SLO Dashboard"
      url: "https://grafana.example.com/d/slo-overview"
      metrics:
        - "Current SLI values"
        - "SLO compliance over time"
        - "Error budget remaining"
        - "Error budget burn rate"
        - "Incident impact on SLO"
    
    - name: "Error Budget Dashboard"
      url: "https://grafana.example.com/d/error-budget"
      metrics:
        - "Budget consumption by time period"
        - "Top contributors to budget consumption"
        - "Projected budget depletion date"
        - "Historical budget trends"

  reporting:
    frequency: "Weekly"
    recipients: ["Engineering Leadership", "Product Management", "Customer Success"]
    contents:
      - "SLO compliance status"
      - "Error budget health"
      - "Incidents affecting SLOs"
      - "Reliability improvements"
      - "Action items and decisions"

# INCIDENT IMPACT ON SLO
incidentHandling:
  classification:
    - severity: "P0 - Critical"
      sloImpact: "Major outage, significant SLO impact"
      response: "Immediate page, all hands"
    
    - severity: "P1 - High"
      sloImpact: "Partial outage, measurable SLO impact"
      response: "Page on-call, incident commander assigned"
    
    - severity: "P2 - Medium"
      sloImpact: "Degraded performance, minor SLO impact"
      response: "Notify on-call, coordinate during business hours"

  postIncident:
    - "Calculate SLO impact (downtime minutes, affected users)"
    - "Update error budget consumption"
    - "Conduct blameless postmortem"
    - "Identify preventive measures"
    - "Update runbooks and playbooks"

# CONTINUOUS IMPROVEMENT
improvement:
  reviewCadence: "Monthly"
  
  reviewTopics:
    - "SLO appropriateness (too strict or too loose?)"
    - "SLI measurement accuracy"
    - "Error budget consumption patterns"
    - "Reliability vs velocity balance"
    - "Customer satisfaction alignment"
  
  adjustmentProcess:
    - step: 1
      action: "Propose SLO changes with data justification"
    - step: 2
      action: "Review with stakeholders (eng, product, customer success)"
    - step: 3
      action: "Communicate changes to customers if SLA affected"
    - step: 4
      action: "Implement updated SLOs and monitoring"
    - step: 5
      action: "Monitor impact over 30-90 days"

# RELATED DOCUMENTS
relatedDocuments:
  - type: "Runbooks"
    location: "operations/runbooks.yaml"
    purpose: "Operational procedures for maintaining SLOs"
  
  - type: "Incident Management Plan"
    location: "operations/incident-management-plan.yaml"
    purpose: "Response procedures for SLO violations"
  
  - type: "Monitoring Dashboards"
    location: "operations/monitoring-dashboards.yaml"
    purpose: "SLO and SLI visualization"

changeHistory:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    author: "SRE Team"
    changes: "Initial SLO definitions based on service requirements"
"""

# Continue with more templates...
# (Add 20-30 more specialized templates here)

