# Scheduling SLAs
<!-- See also: artifact_descriptions/scheduling-slas.md for complete guidance -->

## Purpose

Scheduling SLAs define service level agreements for **scheduled jobs, batch processing, data pipelines, and recurring workflows**. Unlike real-time API SLAs, these focus on job completion time, data freshness, and processing windows.

**Use Cases**:
- ETL/ELT pipelines (data warehouse loads)
- Batch processing jobs (reports, aggregations)
- Scheduled ML model retraining
- Nightly data syncs and backups
- Report generation and distribution

---

## Scheduling SLA Template

### Job: Daily Data Warehouse ETL

**Schedule**: Daily at 2:00 AM UTC

**SLA Commitments**:
- **Completion Time**: Must complete by 6:00 AM UTC (4-hour window)
- **Success Rate**: 99.5% of runs succeed (1-2 failures per month acceptable)
- **Data Freshness**: Data must be < 24 hours old
- **Retry Policy**: Auto-retry failed jobs 3 times with exponential backoff

**Measurement**:
```sql
-- Success rate over last 30 days
SELECT 
  COUNT(CASE WHEN status = 'success' THEN 1 END) / COUNT(*) * 100 AS success_rate
FROM job_runs
WHERE job_name = 'daily_etl'
  AND start_time >= CURRENT_DATE - INTERVAL '30 days'
```

**Penalties for SLA Breach**:
- **1-2 hours late**: Warning to on-call, escalate if recurring
- **> 2 hours late**: Page on-call, escalate to data engineering lead
- **Job failure > 3 retries**: Page on-call, create incident ticket

---

## Example: ML Model Retraining

**Job**: Recommendation Model Retraining

**Schedule**: Weekly (Sunday 1:00 AM UTC)

**SLA**:
- **Completion**: Must complete within 6 hours (by 7:00 AM)
- **Model Accuracy**: New model must achieve ≥ baseline accuracy on validation set
- **Deployment**: New model deployed to production by 8:00 AM if accuracy threshold met

**Dependencies**:
- Training data available (data pipeline completes by 12:00 AM)
- GPU resources available (reserved capacity)
- Validation dataset up-to-date

**Failure Handling**:
- If retraining fails, use previous week's model (no deployment)
- Alert ML Ops team
- Investigate root cause within 24 hours

---

## Monitoring & Alerting

**Metrics to Track**:
- Job start time (actual vs. scheduled)
- Job duration (actual vs. expected)
- Job success/failure rate
- Data freshness (time since last successful run)
- Resource utilization (CPU, memory during job execution)

**Alerts**:
- Job started late (> 15 minutes past scheduled time)
- Job running longer than expected (> 2x typical duration)
- Job failed after all retries
- Data freshness SLA breach (data > 25 hours old)

---

## Scheduling Patterns

### Time-Based Scheduling
- **Cron syntax**: `0 2 * * *` (daily at 2 AM)
- **Airflow**: DAG with schedule_interval
- **AWS EventBridge**: Cron expression

### Dependency-Based Scheduling
- **Upstream dependency**: Wait for data pipeline to complete
- **Fan-out pattern**: Trigger multiple downstream jobs after completion
- **Conditional execution**: Run job only if new data available

### Window-Based Scheduling
- **Processing window**: 2 AM - 6 AM (4-hour window)
- **Backfill window**: Process last 7 days of data on failure recovery

---

## Related Artifacts

- **DAG Definitions**: `dag-definitions.yaml` (Airflow/Prefect workflows)
- **SLA/SLO Schedules**: `sla-slo-schedules.yaml` (real-time API SLAs)
- **Data Freshness SLAs**: `data-freshness-slas.yaml` (data timeliness requirements)

---

**Note**: For batch processing jobs, consider separating SLAs for job execution (completion time) and data quality (accuracy, completeness).
