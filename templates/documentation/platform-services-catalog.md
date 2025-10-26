# Platform Services Catalog

## Document Information

**Version**: 1.0.0
**Status**: Active
**Owner**: Platform Engineering Team
**Last Updated**: 2025-10-26
**Review Cycle**: Quarterly
**Classification**: Internal

## Purpose

This catalog documents all shared platform services, capabilities, and infrastructure offerings that application teams can consume. It provides service descriptions, SLAs, onboarding procedures, usage patterns, cost models, and support contacts to enable self-service adoption of platform capabilities.

## Scope

**In Scope**:
- Compute platforms (Kubernetes, serverless, VMs)
- Data platforms (databases, caching, messaging, streaming)
- CI/CD and deployment services
- Observability and monitoring services
- Security services (secrets, authentication, authorization)
- Developer experience tools
- Cost, SLAs, and support models

**Out of Scope**:
- Business applications (covered in application portfolio)
- Individual team-specific services
- Desktop productivity tools
- End-user facing applications

---

## Compute Services

### Kubernetes Platform (EKS)

**Service Name**: Kubernetes Platform
**Platform**: AWS EKS (Elastic Kubernetes Service)
**Maturity**: Production
**Owner**: Cloud Platform Team
**Support**: Slack #platform-kubernetes, platform-k8s@company.com

#### Description
Managed Kubernetes clusters for containerized workloads. Provides multi-tenant namespaces, autoscaling, service mesh, ingress controllers, and integrated CI/CD deployment pipelines.

#### Capabilities
- **Cluster Versions**: Kubernetes 1.28, 1.29, 1.30
- **Node Types**:
  - General Purpose: m6i.xlarge, m6i.2xlarge
  - Compute Optimized: c6i.xlarge, c6i.2xlarge
  - Memory Optimized: r6i.xlarge, r6i.2xlarge
  - GPU: g5.xlarge, g5.2xlarge (for ML workloads)
- **Autoscaling**: Cluster Autoscaler + Karpenter for node provisioning
- **Service Mesh**: Istio 1.20 with mTLS, traffic management, observability
- **Ingress**: AWS ALB Ingress Controller, NGINX Ingress Controller
- **Storage**: EBS CSI driver (gp3), EFS CSI driver (shared storage)
- **Secrets**: External Secrets Operator (integrates with Vault)
- **Policy Enforcement**: OPA Gatekeeper for admission control

#### Onboarding Process
1. Submit namespace request via platform portal
2. Platform team provisions namespace with resource quotas
3. Receive RBAC credentials, kubeconfig, and namespace details
4. Configure CI/CD pipeline for deployments
5. Deploy applications using Helm charts or Kustomize

#### SLA
- **Cluster Availability**: 99.9% uptime (AWS EKS SLA)
- **Node Replacement**: Failed nodes replaced within 5 minutes
- **Support Response**:
  - P1 (production down): 15 minutes
  - P2 (degraded performance): 2 hours
  - P3 (questions): 1 business day

#### Cost Model
- **Node Costs**: Pass-through AWS EC2 pricing
- **EKS Control Plane**: $0.10/hour per cluster (shared across teams)
- **Data Transfer**: Charged per GB egress
- **Chargeback**: Monthly cost allocation by namespace resource usage

#### Resource Quotas (per namespace)
- **CPU**: 32 cores (default), 128 cores (max with approval)
- **Memory**: 128 GB (default), 512 GB (max with approval)
- **Pods**: 200 pods (default), 1000 pods (max)
- **Persistent Volumes**: 10 volumes, 1 TB total

#### Usage Patterns
```yaml
# Example deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: team-alpha
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: web
        image: company.ecr.us-east-1.amazonaws.com/web-app:v1.2.3
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
          limits:
            cpu: 1000m
            memory: 1Gi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
```

#### Getting Started
- **Documentation**: https://docs.platform.company.com/kubernetes
- **Examples**: https://github.com/company/k8s-examples
- **Training**: Monthly Kubernetes onboarding workshops

---

### Serverless Functions (Lambda)

**Service Name**: Serverless Functions Platform
**Platform**: AWS Lambda
**Maturity**: Production
**Owner**: Cloud Platform Team
**Support**: Slack #platform-lambda, platform-serverless@company.com

#### Description
Event-driven serverless compute for lightweight, scalable functions. Ideal for API backends, event processing, scheduled jobs, and data transformations.

#### Capabilities
- **Runtimes**: Python 3.11, Node.js 20, Go 1.21, Java 17
- **Memory**: 128 MB to 10 GB
- **Timeout**: 15 minutes maximum
- **Concurrency**: 1000 concurrent executions (default), increasable
- **Triggers**: API Gateway, EventBridge, S3, DynamoDB Streams, SQS, SNS
- **VPC Integration**: Access RDS, ElastiCache, internal services
- **Layers**: Shared libraries, dependencies, SDKs

#### Onboarding Process
1. Define function requirements (runtime, memory, timeout)
2. Develop function locally using SAM or CDK
3. Deploy via CI/CD pipeline (GitHub Actions)
4. Configure event triggers (API Gateway, EventBridge)
5. Monitor via CloudWatch Logs and Datadog

#### SLA
- **Availability**: 99.95% uptime (AWS Lambda SLA)
- **Cold Start Latency**: P99 < 2s (mitigated with provisioned concurrency)
- **Execution Duration**: Variable, up to 15 minutes

#### Cost Model
- **Compute**: $0.0000166667 per GB-second
- **Requests**: $0.20 per 1M requests
- **Free Tier**: 1M free requests, 400,000 GB-seconds per month
- **Provisioned Concurrency**: $0.000004 per GB-second (keeps functions warm)

#### Usage Patterns
```python
# Example Lambda function
import json

def lambda_handler(event, context):
    """Process incoming API request"""
    body = json.loads(event['body'])
    user_id = body.get('userId')

    # Business logic here
    result = process_user_request(user_id)

    return {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {'Content-Type': 'application/json'}
    }
```

#### Best Practices
- Use environment variables for configuration
- Implement idempotency for retry scenarios
- Set appropriate memory allocation (affects CPU)
- Use Lambda Layers for shared dependencies
- Enable X-Ray tracing for observability
- Set reserved concurrency for critical functions

---

## Data Services

### PostgreSQL Database (RDS)

**Service Name**: Managed PostgreSQL Database
**Platform**: AWS RDS PostgreSQL
**Maturity**: Production
**Owner**: Data Platform Team
**Support**: Slack #platform-databases, data-platform@company.com

#### Description
Fully managed PostgreSQL relational databases with automated backups, patching, high availability, and read replicas. Optimized for OLTP workloads, analytics, and application databases.

#### Capabilities
- **Versions**: PostgreSQL 15.5, 16.1
- **Instance Types**:
  - db.t3.medium (2 vCPU, 4 GB) - development
  - db.m6i.xlarge (4 vCPU, 16 GB) - production
  - db.r6i.2xlarge (8 vCPU, 64 GB) - high-memory workloads
- **Storage**: gp3 SSD (up to 64 TB, 16,000 IOPS)
- **High Availability**: Multi-AZ deployments with automatic failover
- **Read Replicas**: Up to 5 replicas for read scaling
- **Backups**: Automated daily snapshots (35-day retention)
- **Encryption**: At-rest (AES-256), in-transit (TLS)
- **Extensions**: pgvector, PostGIS, pg_cron, timescaledb

#### Onboarding Process
1. Submit database request via platform portal
   - Environment (dev/staging/prod)
   - Size estimate (storage, IOPS, connections)
   - High availability requirements
2. Platform team provisions database instance
3. Receive connection details (endpoint, port, credentials via Vault)
4. Configure application connection pooling (recommended: PgBouncer)
5. Set up monitoring dashboards in Datadog

#### SLA
- **Availability**:
  - Single-AZ: 99.5% uptime
  - Multi-AZ: 99.95% uptime
- **Backup Recovery**: RTO 30 minutes, RPO 5 minutes (point-in-time recovery)
- **Maintenance Windows**: Monthly patching, scheduled during low-traffic hours

#### Cost Model
- **Instance**: $0.50 - $5.00/hour (depends on instance type)
- **Storage**: $0.115/GB-month (gp3)
- **IOPS**: Included up to baseline, $0.20/IOPS-month for provisioned
- **Backup Storage**: Free up to 100% of database size, $0.095/GB-month beyond
- **Data Transfer**: $0.09/GB egress

#### Connection String Example
```
postgresql://app_user:password@prod-db.abc123.us-east-1.rds.amazonaws.com:5432/app_database?sslmode=require
```

#### Best Practices
- Use connection pooling (PgBouncer, pgpool)
- Enable query logging for slow queries (> 100ms)
- Set appropriate `work_mem` and `shared_buffers`
- Create indexes for frequent queries
- Use read replicas for analytics queries
- Enable RDS Performance Insights

---

### Redis Cache (ElastiCache)

**Service Name**: Managed Redis Cache
**Platform**: AWS ElastiCache Redis
**Maturity**: Production
**Owner**: Data Platform Team
**Support**: Slack #platform-databases, data-platform@company.com

#### Description
Fully managed Redis in-memory data store for caching, session storage, real-time leaderboards, rate limiting, and pub/sub messaging.

#### Capabilities
- **Version**: Redis 7.1
- **Cluster Modes**:
  - Standalone (single node)
  - Cluster Mode (sharded, up to 500 nodes)
  - Replication (primary + replicas)
- **Node Types**:
  - cache.t3.micro (0.5 GB) - dev/testing
  - cache.r6g.large (13 GB) - production
  - cache.r6g.4xlarge (104 GB) - high-memory
- **Features**:
  - Redis Streams, Sorted Sets, HyperLogLog
  - Lua scripting support
  - Redis JSON, Redis Search modules
- **Persistence**:
  - No persistence (cache-only)
  - AOF (append-only file)
  - RDB snapshots
- **Encryption**: At-rest, in-transit (TLS)

#### Onboarding Process
1. Define use case (caching, session store, queue, pub/sub)
2. Estimate data size and throughput requirements
3. Submit request via platform portal
4. Receive Redis endpoint and credentials
5. Integrate using Redis client library

#### SLA
- **Availability**:
  - Single node: 99.5%
  - Multi-node (replica): 99.9%
- **Latency**: P99 < 5ms (sub-millisecond typical)

#### Cost Model
- **Node**: $0.034/hour (cache.r6g.large) to $5.44/hour (cache.r6g.16xlarge)
- **Data Transfer**: $0.09/GB egress

#### Usage Example (Python)
```python
import redis

# Connect to Redis cluster
r = redis.Redis(
    host='prod-redis.abc123.cache.amazonaws.com',
    port=6379,
    ssl=True,
    decode_responses=True
)

# Cache user session
r.setex('session:user123', 3600, '{"userId": "123", "role": "admin"}')

# Get cached value
session = r.get('session:user123')
```

---

## Messaging & Streaming Services

### Kafka Event Streaming (MSK)

**Service Name**: Kafka Event Streaming Platform
**Platform**: AWS MSK (Managed Streaming for Apache Kafka)
**Maturity**: Production
**Owner**: Data Platform Team
**Support**: Slack #platform-kafka, data-platform@company.com

#### Description
High-throughput, distributed event streaming platform for real-time data pipelines, event-driven architectures, and data integration between systems.

#### Capabilities
- **Version**: Apache Kafka 3.6
- **Cluster Sizes**: 3, 6, 9 brokers (multi-AZ)
- **Broker Types**: kafka.m5.large to kafka.m5.24xlarge
- **Storage**: 1 TB to 16 TB per broker (EBS gp3)
- **Throughput**: Up to 200 MB/s per broker
- **Retention**: 7 days (default), configurable up to 365 days
- **Replication**: 3x replication factor (cross-AZ)
- **Encryption**: TLS in-transit, encryption at-rest
- **Authentication**: SASL/SCRAM, IAM

#### Onboarding Process
1. Define topics, partitions, retention requirements
2. Submit Kafka access request
3. Receive broker endpoints and SASL credentials
4. Create topics via platform portal or Kafka Admin API
5. Integrate producers/consumers using Kafka client libraries
6. Monitor via Datadog Kafka integration

#### SLA
- **Availability**: 99.9% uptime
- **Durability**: 99.999999999% (11 nines) with 3x replication
- **Latency**: P99 < 50ms (producer to consumer)

#### Cost Model
- **Broker Hours**: $0.21/hour (kafka.m5.large) to $10.24/hour (kafka.m5.24xlarge)
- **Storage**: $0.10/GB-month
- **Data Transfer**: Inter-AZ transfer charged

#### Topic Naming Convention
```
{domain}.{entity}.{event-type}.{version}

Examples:
- orders.order.created.v1
- users.user.updated.v1
- payments.transaction.completed.v2
```

#### Usage Example (Python)
```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer
producer = KafkaProducer(
    bootstrap_servers=['b-1.msk-cluster.kafka.us-east-1.amazonaws.com:9096'],
    security_protocol='SASL_SSL',
    sasl_mechanism='SCRAM-SHA-512',
    sasl_plain_username='app-producer',
    sasl_plain_password='...',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('orders.order.created.v1', {'orderId': '12345', 'amount': 99.99})

# Consumer
consumer = KafkaConsumer(
    'orders.order.created.v1',
    bootstrap_servers=['b-1.msk-cluster.kafka.us-east-1.amazonaws.com:9096'],
    group_id='order-processor',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    process_order(message.value)
```

---

## Observability Services

### Datadog Monitoring Platform

**Service Name**: Datadog Observability
**Platform**: Datadog (SaaS)
**Maturity**: Production
**Owner**: SRE Team
**Support**: Slack #observability, sre-team@company.com

#### Description
Unified monitoring, logging, tracing, and alerting platform for infrastructure, applications, and business metrics. Provides dashboards, anomaly detection, APM, and incident management.

#### Capabilities
- **Infrastructure Monitoring**: EC2, ECS, EKS, Lambda metrics
- **APM (Application Performance Monitoring)**: Distributed tracing, service maps, profiling
- **Log Management**: Centralized logging, log aggregation, parsing, search
- **Synthetics**: Uptime checks, API tests, browser tests
- **RUM (Real User Monitoring)**: Frontend performance, user sessions
- **Alerting**: Metric-based, log-based, anomaly detection, forecasting
- **Integrations**: 600+ integrations (AWS, PostgreSQL, Redis, Kafka, etc.)

#### Onboarding Process
1. Request Datadog access via platform portal
2. Receive API key and application key
3. Install Datadog Agent on infrastructure (automated via Terraform)
4. Instrument applications with APM libraries (dd-trace)
5. Create dashboards and alerts in Datadog UI

#### SLA
- **Platform Availability**: 99.9% uptime (Datadog SLA)
- **Data Retention**:
  - Metrics: 15 months
  - Logs: 30 days (default), 90 days (extended)
  - Traces: 15 days

#### Cost Model
- **Infrastructure Monitoring**: $15/host/month
- **APM**: $31/host/month + $1.27/million spans
- **Log Management**: $0.10/GB ingested + $1.70/million log events
- **Monthly Budget**: ~$50,000 (allocated across teams)

#### Dashboard Examples
- **Service Health**: Request rate, error rate, latency (RED metrics)
- **Infrastructure**: CPU, memory, disk, network usage
- **Business Metrics**: Orders/hour, revenue, active users
- **Kubernetes**: Pod status, resource utilization, deployments

---

## Security Services

### Secrets Management (Vault)

**Service Name**: HashiCorp Vault
**Platform**: Self-hosted (EKS)
**Maturity**: Production
**Owner**: Security Team
**Support**: Slack #security, security-team@company.com

#### Description
Centralized secrets management for API keys, database credentials, TLS certificates, and encryption keys. Provides secret rotation, access control, and audit logging.

#### Capabilities
- **Secret Engines**: KV (key-value), Database (dynamic credentials), PKI (certificates), AWS, SSH
- **Authentication**: Kubernetes, AWS IAM, LDAP, OIDC
- **Dynamic Secrets**: Auto-generated database credentials with TTL
- **Secret Rotation**: Automatic rotation for databases, cloud providers
- **Encryption**: Transit encryption engine for application data encryption
- **Audit Logging**: All access logged to S3 for compliance

#### Onboarding Process
1. Request Vault namespace for team/application
2. Authenticate using Kubernetes ServiceAccount or AWS IAM
3. Create secrets in namespace using Vault CLI/API
4. Access secrets from applications using Vault Agent or SDK
5. Configure secret rotation policies

#### SLA
- **Availability**: 99.95% uptime
- **Secret Access Latency**: P95 < 50ms

#### Usage Example
```bash
# Write secret
vault kv put secret/myapp/db username=dbuser password=SecureP@ss

# Read secret
vault kv get secret/myapp/db

# Dynamic PostgreSQL credentials (auto-rotated)
vault read database/creds/myapp-role
# Output: username=v-token-myapp-role-abc123, password=auto-generated, ttl=1h
```

---

## Developer Experience Services

### CI/CD Platform (GitHub Actions)

**Service Name**: CI/CD Platform
**Platform**: GitHub Actions (GitHub Enterprise)
**Maturity**: Production
**Owner**: DevOps Team
**Support**: Slack #devops, devops-team@company.com

#### Description
Automated build, test, and deployment pipelines for continuous integration and delivery. Supports multi-stage deployments, security scanning, and GitOps workflows.

#### Capabilities
- **Workflows**: YAML-based pipeline definitions
- **Runners**: Self-hosted runners (Linux, macOS, Windows)
- **Environments**: Dev, staging, production with approval gates
- **Secrets Management**: Encrypted secrets, integration with Vault
- **Artifact Storage**: Build artifacts, container images (ECR)
- **Reusable Workflows**: Shared workflow templates

#### Onboarding Process
1. Create GitHub repository (or use existing)
2. Add `.github/workflows/ci.yaml` with pipeline definition
3. Configure repository secrets (API keys, credentials)
4. Push code to trigger CI/CD pipeline
5. Review deployment in GitHub Actions UI

#### Example Workflow
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin
          docker push myapp:${{ github.sha }}

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to EKS
        run: kubectl apply -f k8s/staging/
```

---

## Cost Transparency

All platform services provide detailed cost allocation:
- **Monthly Reports**: Cost breakdowns by team, project, environment
- **Tagging**: Resource tagging for cost attribution
- **Budgets**: Budget alerts at 80%, 90%, 100% thresholds
- **Recommendations**: Cost optimization suggestions (rightsizing, reserved instances)

---

## Service Request Process

1. **Request**: Submit via platform portal (https://platform.company.com)
2. **Review**: Platform team reviews within 1 business day
3. **Provisioning**: Service provisioned (SLA: 24 hours for standard requests)
4. **Onboarding**: Credentials delivered, documentation provided
5. **Support**: Ongoing support via Slack channels

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | Platform Engineering | Initial platform services catalog |

---

## References

- Platform Documentation: https://docs.platform.company.com
- Service Request Portal: https://platform.company.com
- Cost Dashboard: https://cost.platform.company.com
