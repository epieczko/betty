# Runbooks
# See also: artifact_descriptions/runbooks.md for complete guidance

metadata:
  version: "1.0.0"
  created: "YYYY-MM-DD"
  lastModified: "YYYY-MM-DD"
  author: "Author Name"
  owner: "Team/Department"
  status: "Draft"  # Draft | Review | Approved | Archived
  classification: "Internal"  # Public | Internal | Confidential | Restricted


systemName: "System or Service Name"
systemOwner: "Team Name"
onCallRotation: "PagerDuty/Opsgenie rotation name"

# RUNBOOK OVERVIEW
purpose: |
  This runbook provides step-by-step procedures for operating, maintaining,
  and troubleshooting [System Name]. It enables on-call engineers to respond
  to alerts, perform routine maintenance, and recover from failures.

scope:
  - Alert response procedures
  - Common troubleshooting scenarios
  - Routine maintenance tasks
  - Disaster recovery procedures

prerequisites:
  access:
    - "Production AWS account access"
    - "Kubernetes cluster kubectl access"
    - "Datadog/monitoring dashboard access"
    - "PagerDuty/on-call tool access"
  knowledge:
    - "Basic Kubernetes operations"
    - "Understanding of system architecture"
    - "Familiarity with monitoring tools"

# ALERT RESPONSE PROCEDURES
alertProcedures:
  - alertName: "High Error Rate"
    alertSource: "Datadog"
    severity: "P1 - Critical"
    description: "Error rate exceeds 5% for 5 minutes"

    investigationSteps:
      - step: 1
        action: "Check current error rate and affected endpoints"
        command: |
          # View error rate dashboard
          open https://datadog.com/dashboard/errors

          # Check logs for errors
          kubectl logs -l app=api-service --tail=100 | grep ERROR

      - step: 2
        action: "Identify error patterns and root cause"
        command: |
          # Check for common error types
          kubectl logs -l app=api-service --tail=1000 | awk '/ERROR/ {print $5}' | sort | uniq -c

      - step: 3
        action: "Check dependent services health"
        command: |
          # Check database connectivity
          kubectl exec -it deploy/api-service -- nc -zv postgres-service 5432

          # Check Redis cache
          kubectl exec -it deploy/api-service -- nc -zv redis-service 6379

    remediationSteps:
      - step: 1
        action: "If database connection issues, restart connection pool"
        command: |
          kubectl rollout restart deployment/api-service

      - step: 2
        action: "If bad deployment, rollback to previous version"
        command: |
          kubectl rollout undo deployment/api-service

      - step: 3
        action: "Scale up if resource exhaustion"
        command: |
          kubectl scale deployment/api-service --replicas=10

    escalation:
      condition: "If error rate doesn't decrease after 15 minutes"
      escalateTo: "Engineering Manager"
      contactMethod: "Page via PagerDuty"

  - alertName: "Database Connection Pool Exhausted"
    alertSource: "Application Metrics"
    severity: "P2 - High"
    description: "Database connection pool utilization > 90%"

    investigationSteps:
      - step: 1
        action: "Check current connection pool stats"
        command: |
          # View connection pool metrics
          curl http://api-service:8080/metrics | grep db_pool

      - step: 2
        action: "Identify slow queries holding connections"
        command: |
          # Access database and check running queries
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT pid, query_start, state, query FROM pg_stat_activity WHERE state != 'idle' ORDER BY query_start;"

    remediationSteps:
      - step: 1
        action: "Terminate long-running queries if safe"
        command: |
          # Terminate specific query by PID
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT pg_terminate_backend(<PID>);"

      - step: 2
        action: "Increase connection pool size temporarily"
        command: |
          # Update ConfigMap
          kubectl edit configmap api-service-config
          # Increase max_connections: 100 -> 150
          # Restart deployment
          kubectl rollout restart deployment/api-service

# ROUTINE MAINTENANCE TASKS
maintenanceProcedures:
  - taskName: "Weekly Log Rotation"
    frequency: "Weekly"
    schedule: "Sundays at 2 AM UTC"
    duration: "15 minutes"

    steps:
      - step: 1
        description: "Archive old logs to S3"
        command: |
          kubectl exec -it logging-aggregator -- /scripts/archive-logs.sh --days=7

      - step: 2
        description: "Verify archive completion"
        command: |
          aws s3 ls s3://company-logs/archive/$(date +%Y-%m-%d)/

      - step: 3
        description: "Clean up local log files"
        command: |
          kubectl exec -it logging-aggregator -- /scripts/cleanup-old-logs.sh

    rollback:
      - "Logs are archived before deletion, restore from S3 if needed"
      - "aws s3 cp s3://company-logs/archive/YYYY-MM-DD/ /var/log/ --recursive"

  - taskName: "Database Vacuum and Analyze"
    frequency: "Weekly"
    schedule: "Saturdays at 3 AM UTC"
    duration: "2-3 hours"

    steps:
      - step: 1
        description: "Check database bloat"
        command: |
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size FROM pg_tables ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC LIMIT 10;"

      - step: 2
        description: "Run vacuum analyze"
        command: |
          kubectl exec -it postgres-0 -- psql -U app -c "VACUUM ANALYZE;"

      - step: 3
        description: "Verify completion and check stats"
        command: |
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT schemaname, tablename, n_dead_tup, n_live_tup FROM pg_stat_user_tables WHERE n_dead_tup > 0 ORDER BY n_dead_tup DESC;"

# TROUBLESHOOTING GUIDES
troubleshootingGuides:
  - problem: "Service Not Responding"
    symptoms:
      - "Health check endpoint returns 503"
      - "Pod restarts frequently"
      - "High CPU or memory usage"

    diagnosticSteps:
      - "Check pod status: kubectl get pods -l app=api-service"
      - "View pod logs: kubectl logs <pod-name> --tail=100"
      - "Check resource usage: kubectl top pod <pod-name>"
      - "Describe pod: kubectl describe pod <pod-name>"

    solutions:
      - condition: "OOMKilled in pod status"
        action: "Increase memory limits"
        steps:
          - "kubectl edit deployment api-service"
          - "Increase resources.limits.memory from 512Mi to 1Gi"
          - "Save and let deployment rollout"

      - condition: "CrashLoopBackOff"
        action: "Check application logs for startup errors"
        steps:
          - "kubectl logs <pod-name> --previous"
          - "Look for configuration errors, missing environment variables"
          - "Verify ConfigMap and Secret mounts"

# DISASTER RECOVERY PROCEDURES
disasterRecoveryProcedures:
  - scenario: "Complete Database Failure"
    rto: "4 hours"
    rpo: "15 minutes"

    steps:
      - step: 1
        description: "Verify database is truly down"
        command: |
          kubectl exec -it postgres-0 -- pg_isready
          kubectl logs postgres-0 --tail=100

      - step: 2
        description: "Identify latest backup"
        command: |
          aws s3 ls s3://company-backups/postgres/ --recursive | sort | tail -n 10

      - step: 3
        description: "Restore from backup"
        command: |
          # Stop applications
          kubectl scale deployment/api-service --replicas=0

          # Restore database
          kubectl exec -it postgres-0 -- /scripts/restore-from-backup.sh s3://company-backups/postgres/2024-01-15-03-00-00.dump

      - step: 4
        description: "Verify data integrity"
        command: |
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT COUNT(*) FROM users;"
          kubectl exec -it postgres-0 -- psql -U app -c "SELECT MAX(created_at) FROM orders;"

      - step: 5
        description: "Resume normal operations"
        command: |
          kubectl scale deployment/api-service --replicas=5
          # Monitor for errors
          kubectl logs -f deploy/api-service

    verification:
      - "Verify latest data is present in restored database"
      - "Check application can connect and query database"
      - "Monitor error rates return to normal"
      - "Verify no data loss beyond RPO threshold"

# CONTACTS & ESCALATION
contacts:
  primaryOnCall:
    role: "On-Call Engineer"
    contact: "PagerDuty rotation 'api-service-oncall'"

  escalation:
    - level: 1
      role: "Engineering Manager"
      contact: "engineering-manager@example.com"
      escalateAfter: "30 minutes for P1, 2 hours for P2"

    - level: 2
      role: "Director of Engineering"
      contact: "director@example.com"
      escalateAfter: "1 hour for P1"

    - level: 3
      role: "CTO"
      contact: "cto@example.com"
      escalateAfter: "2 hours for P1"

  vendorSupport:
    - vendor: "AWS Support"
      account: "Enterprise Support"
      contact: "+1-XXX-XXX-XXXX"
      caseURL: "https://console.aws.amazon.com/support"

    - vendor: "Datadog Support"
      tier: "Premium Support"
      contact: "support@datadog.com"
      sla: "1 hour response for critical issues"

# RELATED DOCUMENTS
relatedDocuments:
  - type: "Architecture Diagram"
    location: "architecture/system-architecture.md"

  - type: "Service Level Objectives"
    location: "operations/service-level-objectives.yaml"

  - type: "Incident Response Plan"
    location: "operations/incident-management-plan.yaml"

  - type: "Disaster Recovery Plan"
    location: "operations/disaster-recovery-runbooks.yaml"

# CHANGE HISTORY
changeHistory:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    author: "Author Name"
    changes: "Initial runbook creation"
