# Capacity Models
<!-- See also: artifact_descriptions/capacity-models.md for complete guidance -->
<!-- YAML version available at: capacity-models.yaml -->

## Purpose

Capacity Models apply **queueing theory**, **Little's Law**, and empirical performance data to predict system behavior under varying loads and inform infrastructure sizing decisions. They translate performance requirements and load profiles into specific resource allocations.

**Key Applications**:
- Infrastructure sizing (CPU, memory, storage, network)
- Cost forecasting for cloud resources
- Growth planning (projected capacity for 6-12 months)
- Scalability testing scenarios
- Resource utilization targets to prevent saturation

---

## Little's Law

**Formula**: `L = λ × W`

Where:
- **L** = Average number of requests in system (queue depth + processing)
- **λ** (lambda) = Arrival rate (requests per second)
- **W** = Average time request spends in system (latency)

**Example**: If arrival rate is 1000 req/s and average latency is 0.1s, then L = 1000 × 0.1 = 100 concurrent requests

**Usage**: Determine required concurrency/parallelism to meet latency SLOs at target throughput

---

## Capacity Model Template

### System: API Gateway

**Current Capacity** (as of YYYY-MM-DD):
- **Instance Type**: c5.2xlarge (8 vCPUs, 16GB RAM)
- **Instance Count**: 10 instances
- **Max Throughput**: 5,000 requests/second (measured under load test)
- **Throughput per Instance**: 500 req/s
- **Current Utilization**: 60% (3,000 req/s average load)

**Resource Utilization at Target Load**:
- **CPU**: 60% average, 80% p95
- **Memory**: 50% average (8GB used / 16GB available)
- **Network**: 500 Mbps average, 800 Mbps p95

**Bottleneck Analysis**:
- **Primary Bottleneck**: CPU (saturates at 90% before other resources)
- **Secondary Bottleneck**: Network I/O during traffic spikes
- **Headroom**: 40% capacity remaining (2,000 req/s before saturation)

**Growth Projections** (12-month forecast):
| Month | Projected Load (req/s) | Required Instances | Headroom |
|-------|------------------------|--------------------| ---------|
| Current | 3,000 | 10 | 40% |
| +3 months | 3,900 (+30%) | 10 | 22% |
| +6 months | 5,070 (+69%) | 13 | 27% |
| +12 months | 6,590 (+120%) | 17 | 26% |

**Scaling Recommendations**:
- Add 3 instances by Month 6 (before headroom drops below 25%)
- Add 4 more instances by Month 12
- Auto-scaling policy: Scale up when CPU > 70% for 5 minutes

---

## Queueing Theory Models

### M/M/c Queue Model

**Use Case**: Simple capacity estimation for multi-server systems

**Parameters**:
- **λ** (lambda): Arrival rate (requests/second)
- **μ** (mu): Service rate per server (requests/second per server)
- **c**: Number of servers
- **ρ** (rho): Utilization = λ / (c × μ)

**Target Utilization**: 70% (leave 30% headroom)
- At 70% utilization, queuing delay is manageable
- Above 80% utilization, queue depth grows exponentially

**Example**:
- Arrival rate (λ) = 3,000 req/s
- Service rate (μ) = 500 req/s per server
- Required servers (c) = λ / (μ × 0.7) = 3,000 / (500 × 0.7) = 8.6 → **9 servers minimum**

---

## Resource Utilization Targets

| Resource | Target Utilization | Warning Threshold | Critical Threshold |
|----------|-------------------|-------------------|-------------------|
| CPU | 60-70% average | 80% for 15 min | 90% for 5 min |
| Memory | 60-75% average | 85% | 95% |
| Disk I/O | 50-60% average | 75% | 85% |
| Network | 50-60% average | 75% | 85% |

**Rationale**: Maintain 25-40% headroom for:
- Traffic spikes (Black Friday, product launches)
- Instance failures (auto-scaling needs time to replace)
- Gradual performance degradation at high utilization

---

## Capacity Planning Scenarios

### Scenario 1: Black Friday Traffic Spike

**Assumptions**:
- Normal traffic: 3,000 req/s
- Black Friday peak: 15,000 req/s (5x normal)
- Duration: 6 hours
- SLO: p95 latency < 500ms

**Capacity Requirements**:
- Required instances: 15,000 / (500 × 0.7) = 43 instances
- Pre-scaling strategy: Scale to 40 instances 24 hours before event
- Auto-scaling headroom: Additional 10% buffer (44 instances total)

**Cost Analysis**:
- Normal: 10 instances × $0.34/hour × 720 hours/month = $2,448/month
- Black Friday: 44 instances × $0.34/hour × 6 hours = $90 (one-time)
- **Total Monthly Cost**: $2,538

### Scenario 2: 30% YoY Growth

**Assumptions**:
- Current: 3,000 req/s
- Growth rate: 30% year-over-year
- Planning horizon: 12 months

**Capacity Timeline**:
| Quarter | Load (req/s) | Instances | Action |
|---------|--------------|-----------|--------|
| Q1 | 3,000 | 10 | Baseline |
| Q2 | 3,450 | 10 | Monitor |
| Q3 | 3,970 | 12 | Add 2 instances |
| Q4 | 4,565 | 14 | Add 2 instances |

---

## Storage Capacity Planning

### Database Storage

**Current State**:
- Total data: 5TB
- Growth rate: 500GB/month (historical average)
- Current capacity: 10TB
- Utilization: 50%

**12-Month Projection**:
- Projected data: 5TB + (500GB × 12) = 11TB
- Required capacity: 11TB / 0.7 = 15.7TB → **Provision 16TB**
- Trigger expansion: When utilization exceeds 70% (10.5TB)

**Archival Strategy**:
- Archive data > 2 years old to S3 Glacier
- Expected archival: 2TB/year
- Net growth after archival: 4TB/year

---

## Cost Forecasting

| Resource | Current Monthly Cost | Projected Cost (+12 months) | Growth |
|----------|---------------------|----------------------------|--------|
| Compute (EC2) | $2,448 | $4,161 (+70%) | Traffic growth + headroom |
| Storage (RDS) | $800 | $1,280 (+60%) | Data growth |
| Network (Data Transfer) | $400 | $680 (+70%) | Traffic growth |
| **Total** | **$3,648** | **$6,121** | **+68%** |

---

## Capacity Alerts & Monitoring

**Proactive Alerts** (before capacity exhausted):
- CPU utilization > 70% for 15 minutes → Alert ops team
- Memory utilization > 75% → Alert ops team
- Disk space > 70% → Alert ops team, plan expansion
- Network throughput > 70% → Alert ops team

**Auto-Scaling Policies**:
- Scale up: CPU > 70% for 5 minutes (add 20% instances)
- Scale down: CPU < 40% for 20 minutes (remove 10% instances)
- Min instances: 10
- Max instances: 50

---

## Related Artifacts

- **YAML Version**: `capacity-models.yaml` (structured capacity data)
- **SLA/SLO Schedules**: `sla-slo-schedules.yaml` (performance targets)
- **Performance Test Results**: `load-test-report.md` (empirical data)
- **Infrastructure Architecture**: `architecture/infrastructure-design.md`

---

**Note**: Capacity models should be updated quarterly based on actual traffic patterns and load test results. The YAML version contains detailed formulas and historical data.
