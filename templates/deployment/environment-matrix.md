# Environment Matrix

## Document Information

**Purpose**: Define comprehensive infrastructure, application, and operational parameters across all deployment environments (development, staging, production) and deployment targets (regions, clouds, clusters) to ensure environment parity and enable progressive delivery.

**Format**: Markdown with YAML examples

**Target Audience**: Platform Engineers, Cloud Architects, DevOps Engineers, SRE Teams

**Related Artifacts**:
- Infrastructure as Code (Terraform, Pulumi)
- Kustomize Overlays
- Helm Values Files
- CI/CD Pipeline Definitions
- Disaster Recovery Plans

---

## Metadata

```yaml
version: "3.3.0"
created: "2023-05-01"
lastModified: "2024-01-25"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
approvers:
  - name: "David Kim"
    role: "Principal Platform Engineer"
    date: "2024-01-25"
  - name: "Rachel Thompson"
    role: "Infrastructure Manager"
    date: "2024-01-25"
```

---

## 1. Environment Strategy

### 1.1 Environment Tiers

| Environment | Purpose | SLA | Data Classification | Deployment Frequency |
|-------------|---------|-----|---------------------|---------------------|
| Development | Feature development, unit testing | None | Test data only | On every commit |
| Staging | Pre-production testing, QA validation | 95% | Anonymized production data | On merge to main |
| UAT | User acceptance testing | 99% | Anonymized production data | Weekly releases |
| Production | Live customer-facing services | 99.9% | Production (PII, PCI) | Daily with approval |

### 1.2 Environment Parity Principles

1. **Production-like Staging**: Staging environment closely mirrors production in infrastructure and configuration
2. **Minimal Configuration Drift**: Environments differ only in size, scale, and specific integrations
3. **Automated Sync**: Use Infrastructure as Code to maintain consistency across environments
4. **Progressive Promotion**: All changes flow through dev → staging → production pipeline
5. **Feature Flags**: Use feature flags to decouple deployment from release

---

## 2. Multi-Cloud Architecture

### 2.1 Cloud Provider Distribution

**Primary Cloud**: AWS (80% of workloads)
**Secondary Cloud**: Azure (15% of workloads, compliance requirements)
**Tertiary Cloud**: GCP (5% of workloads, specific services)

```yaml
cloudDistribution:
  aws:
    environments: [development, staging, production]
    regions: [us-east-1, us-west-2, eu-west-1]
    services: [EKS, RDS, ElastiCache, S3, CloudFront]

  azure:
    environments: [production]  # Compliance workloads only
    regions: [eastus, westeurope]
    services: [AKS, Azure SQL, Blob Storage]

  gcp:
    environments: [development]  # BigQuery analytics only
    regions: [us-central1]
    services: [GKE, BigQuery, Cloud Storage]
```

### 2.2 Multi-Region Strategy

**Production Regions**:
- **Primary**: us-east-1 (AWS Virginia) - 60% of traffic
- **Secondary**: us-west-2 (AWS Oregon) - 30% of traffic, DR failover
- **Tertiary**: eu-west-1 (AWS Ireland) - 10% of traffic, GDPR compliance

**Disaster Recovery**:
- **RPO** (Recovery Point Objective): 1 hour
- **RTO** (Recovery Time Objective): 4 hours
- **Failover Strategy**: DNS-based failover with Route 53, active-passive for databases

---

## 3. Development Environment

### 3.1 Infrastructure Configuration

```yaml
development:
  infrastructure:
    cloud:
      provider: AWS
      region: us-east-1
      accountId: "123456789012"
      vpcId: "vpc-dev-abc123"

    kubernetes:
      clusterName: dev-eks-cluster
      clusterVersion: "1.28"
      nodeGroups:
        - name: general-purpose
          instanceType: t3.medium
          minNodes: 2
          maxNodes: 5
          diskSize: 50  # GB

    compute:
      defaultResourceRequests:
        cpu: "100m"
        memory: "128Mi"
      defaultResourceLimits:
        cpu: "500m"
        memory: "512Mi"
```

### 3.2 Application Configuration

```yaml
development:
  application:
    deployment:
      strategy: RollingUpdate
      replicas: 1

    ingress:
      domain: dev.api.company.com
      tlsEnabled: true

    monitoring:
      logging:
        level: DEBUG
        retention: 7  # days
      datadog:
        enabled: true
        env: development
```

### 3.3 Database & Data Services

```yaml
development:
  databases:
    postgres:
      instanceClass: db.t3.micro
      engine: postgres
      engineVersion: "15.4"
      storage: 20  # GB
      multiAZ: false
      backupRetention: 1  # days

  caching:
    redis:
      nodeType: cache.t3.micro
      numCacheNodes: 1

  messaging:
    sqs:
      enabled: true
      queues:
        - name: dev-payment-queue
          visibilityTimeout: 30
```

### 3.4 Cost Management

```yaml
development:
  cost:
    monthlyBudget: 500  # USD
    autoshutdown:
      enabled: true
      schedule: "Weeknights 8PM-8AM, Weekends"
    tags:
      Environment: development
      CostCenter: engineering
      ManagedBy: terraform
```

---

## 4. Staging Environment

### 4.1 Production-Parity Configuration

```yaml
staging:
  infrastructure:
    kubernetes:
      clusterName: staging-eks-cluster
      nodeGroups:
        - name: general-purpose
          instanceType: t3.large  # Production uses m5.2xlarge
          minNodes: 3
          maxNodes: 10
        - name: high-memory
          instanceType: r5.large  # Production uses r5.2xlarge
          minNodes: 1
          maxNodes: 3
```

### 4.2 Testing & QA Configuration

```yaml
staging:
  testing:
    loadTesting:
      enabled: true
      targetRPS: 1000  # 10% of production
      duration: 30m

    chaosEngineering:
      enabled: true
      experiments:
        - pod-failure
        - network-latency
        - cpu-stress

    syntheticMonitoring:
      enabled: true
      frequency: 5m
      endpoints:
        - https://staging.api.company.com/health
        - https://staging.api.company.com/ready
```

### 4.3 Data Management

```yaml
staging:
  data:
    strategy: anonymized-production-clone
    refreshFrequency: weekly
    piiScrubbing:
      enabled: true
      fields: [email, phone, ssn, credit_card]
    dataSubset: 10%  # of production data
```

---

## 5. Production Environment

### 5.1 High-Availability Infrastructure

```yaml
production:
  infrastructure:
    regions:
      primary: us-east-1
      secondary: us-west-2  # DR region
      tertiary: eu-west-1   # GDPR compliance

    kubernetes:
      clusterName: prod-eks-cluster
      clusterVersion: "1.28"
      nodeGroups:
        - name: general-purpose
          instanceType: m5.2xlarge
          minNodes: 10
          maxNodes: 50
          diskSize: 200
        - name: high-memory
          instanceType: r5.2xlarge
          minNodes: 3
          maxNodes: 20
        - name: gpu-workloads
          instanceType: p3.2xlarge
          minNodes: 0
          maxNodes: 5
          taints:
            - key: nvidia.com/gpu
              effect: NoSchedule
```

### 5.2 Autoscaling Configuration

```yaml
production:
  autoscaling:
    horizontalPodAutoscaler:
      enabled: true
      minReplicas: 10
      maxReplicas: 100
      targetCPU: 70
      targetMemory: 80

    clusterAutoscaler:
      enabled: true
      scaleDownUtilizationThreshold: 0.5
      scaleDownUnneededTime: 10m

    verticalPodAutoscaler:
      enabled: true
      updateMode: Auto
```

### 5.3 Security & Compliance

```yaml
production:
  security:
    networkPolicy: zero-trust
    podSecurityPolicy: highly-restricted

    waf:
      enabled: true
      ruleSet: OWASP-Top-10 + Custom Rules
      rateLimiting: true
      geoBlocking:
        enabled: true
        blockedCountries: [CN, RU, KP]

    ddosProtection:
      enabled: true
      provider: AWS Shield Advanced

    compliance:
      - PCI-DSS 3.2.1
      - SOC 2 Type II
      - GDPR
      - HIPAA

    encryption:
      atRest: true
      inTransit: true
      keyRotation: 30  # days
```

### 5.4 Observability & Monitoring

```yaml
production:
  observability:
    datadog:
      enabled: true
      apm: true
      profiling: true
      logs: true
      traces: true

    logging:
      level: WARN
      retention: 90  # days
      structured: true

    alerts:
      - name: Critical Error Rate
        condition: error_rate > 1%
        channels: [pagerduty, slack-incidents]
        severity: critical
      - name: High Latency
        condition: p95_latency > 500ms
        severity: high
      - name: Low Success Rate
        condition: success_rate < 99.5%
        severity: critical
```

### 5.5 Disaster Recovery

```yaml
production:
  disasterRecovery:
    enabled: true
    rpo: "1 hour"    # Recovery Point Objective
    rto: "4 hours"   # Recovery Time Objective
    backupRegion: us-west-2

    backupSchedule:
      database:
        frequency: hourly
        retention: 30  # days
      volumeSnapshots:
        frequency: daily
        retention: 30
      crossRegionReplication: true

    failoverProcedure:
      automated: false  # Manual failover for safety
      runbook: runbooks/dr-failover.md
      testingFrequency: quarterly
```

---

## 6. Environment Promotion Rules

### 6.1 Development to Staging

```yaml
promotionRules:
  developmentToStaging:
    trigger: Merge to main branch

    requiredChecks:
      - All tests pass
      - Code coverage > 80%
      - Security scan clean
      - No HIGH/CRITICAL vulnerabilities

    approvalRequired: false
    automatedPromotion: true

    postDeployment:
      - Run smoke tests
      - Validate health endpoints
      - Check error rates < 1%
```

### 6.2 Staging to Production

```yaml
promotionRules:
  stagingToProduction:
    trigger: Manual promotion via CI/CD

    requiredChecks:
      - All staging tests pass
      - Load testing completed successfully
      - Security review approved
      - Change Advisory Board (CAB) approval
      - Runbook documentation updated

    approvalRequired: true
    approvers: [platform-team, security-team]
    minimumApprovals: 2

    deploymentStrategy: canary
    canaryPercentage: [10, 25, 50, 100]
    canaryDuration: 30m

    blackoutPeriods:
      - "Black Friday: Nov 24-27"
      - "Cyber Monday: Nov 27-30"
      - "Holiday Freeze: Dec 20 - Jan 2"

    deploymentWindow:
      weekdays: "10:00-16:00 UTC"
      weekends: disabled
```

---

## 7. Configuration Drift Detection

### 7.1 Drift Monitoring

```yaml
driftDetection:
  enabled: true
  schedule: Daily at 02:00 UTC

  tools:
    terraform:
      command: terraform plan -detailed-exitcode
      failOnDrift: false

    kustomize:
      command: kubectl diff -k overlays/production

  notifications:
    channels: [slack-platform]
    severity: warning

  autoRemediation:
    enabled: false  # Manual review required
    dryRun: true
```

### 7.2 Configuration Tracking

```yaml
configurationTracking:
  versioning:
    strategy: git-ops
    repository: github.com/company/k8s-manifests
    branch: main

  auditLog:
    enabled: true
    retention: 365  # days
    events:
      - configuration-change
      - deployment
      - rollback
      - manual-intervention

  complianceReporting:
    frequency: monthly
    format: [pdf, json]
    distribution: [compliance-team, audit-team]
```

---

## 8. Resource Sizing Guidelines

### 8.1 Compute Resources by Environment

| Resource | Development | Staging | Production |
|----------|-------------|---------|------------|
| API Pods | 1 | 2 | 10-100 (HPA) |
| Worker Pods | 1 | 2 | 5-50 (HPA) |
| CPU Request | 100m | 250m | 500m |
| CPU Limit | 500m | 1000m | 2000m |
| Memory Request | 128Mi | 256Mi | 512Mi |
| Memory Limit | 512Mi | 1Gi | 2Gi |

### 8.2 Database Sizing

| Metric | Development | Staging | Production |
|--------|-------------|---------|------------|
| Instance Class | db.t3.micro | db.t3.medium | db.r5.4xlarge |
| Storage | 20 GB | 100 GB | 1000 GB |
| IOPS | Standard | 3000 | 10000 |
| Multi-AZ | No | Yes | Yes |
| Read Replicas | 0 | 1 | 3 |
| Backup Retention | 1 day | 7 days | 30 days |

---

## 9. Cost Optimization

### 9.1 Environment Budgets

```yaml
costManagement:
  budgets:
    development:
      monthly: $500
      alerts: [80%, 90%, 100%]

    staging:
      monthly: $3,000
      alerts: [80%, 90%, 100%]

    production:
      monthly: $50,000
      alerts: [85%, 95%, 105%]

  optimization:
    reservedInstances:
      production: 70%  # of steady-state capacity
      staging: 30%

    spotInstances:
      development: 80%
      staging: 50%
      production: 20%  # non-critical workloads only

    autoshutdown:
      development:
        enabled: true
        schedule: "Weeknights 8PM-8AM EST, Weekends"
      staging:
        enabled: false
```

### 9.2 Resource Tagging Strategy

```yaml
taggingPolicy:
  required:
    - Environment: [development, staging, production]
    - ManagedBy: [terraform, pulumi, manual]
    - CostCenter: [engineering, product, sales]
    - Team: [platform, backend, frontend, data]

  optional:
    - Project: <project-name>
    - Compliance: [pci-dss, hipaa, gdpr, sox]
    - Owner: <email-address>

  enforcement:
    required: true
    validationHook: pre-deploy
    failOnMissingTags: true
```

---

## 10. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 3.3.0 | 2024-01-25 | David Kim | Added multi-region production, cost optimization guidelines |
| 3.2.0 | 2024-01-15 | Rachel Thompson | Added GPU node group, updated Kafka configurations |
| 3.1.0 | 2023-11-20 | Platform Team | Increased production database IOPS, added read replicas |
| 3.0.0 | 2023-09-01 | Infrastructure Team | Complete environment matrix overhaul |

---

## 11. Related Documentation

- [Infrastructure as Code (Terraform)](../infrastructure/terraform/)
- [Kustomize Overlays](./kustomize-manifests.md)
- [Helm Values Files](./helm-values/)
- [CI/CD Pipeline Definitions](./ci-cd-pipeline-definitions.md)
- [Disaster Recovery Plan](../operations/disaster-recovery-plan.md)
- [Cost Optimization Strategy](../governance/cost-optimization.md)

---

## 12. Quick Reference

### 12.1 Environment Access

```bash
# Configure kubectl for each environment
aws eks update-kubeconfig --name dev-eks-cluster --region us-east-1
aws eks update-kubeconfig --name staging-eks-cluster --region us-east-1
aws eks update-kubeconfig --name prod-eks-cluster --region us-east-1

# Switch between contexts
kubectl config use-context dev-eks-cluster
kubectl config use-context staging-eks-cluster
kubectl config use-context prod-eks-cluster
```

### 12.2 Common Operations

```bash
# Deploy to environment
kubectl apply -k overlays/production

# Check deployment status
kubectl rollout status deployment/api-service -n production

# Scale deployment
kubectl scale deployment/api-service --replicas=20 -n production

# View resource usage
kubectl top nodes
kubectl top pods -n production
```
