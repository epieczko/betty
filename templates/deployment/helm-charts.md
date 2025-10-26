# Helm Charts - Production-Ready Template

## Chart Overview

**Chart Name:** `{{ .Chart.Name }}`
**Chart Version:** `{{ .Chart.Version }}`
**Application Version:** `{{ .Chart.AppVersion }}`
**Description:** Production-ready Helm chart for cloud-native application deployment

This template provides a complete Helm chart structure following industry best practices for Kubernetes deployments with high availability, security, and observability.

---

## Chart.yaml

```yaml
apiVersion: v2
name: myapp
description: A production-ready microservice application chart
type: application
version: 1.0.0
appVersion: "1.0.0"

maintainers:
  - name: Platform Engineering Team
    email: platform-eng@company.com
    url: https://engineering.company.com

keywords:
  - microservice
  - api
  - production
  - kubernetes

home: https://github.com/company/myapp
sources:
  - https://github.com/company/myapp

dependencies:
  - name: postgresql
    version: 12.x.x
    repository: https://charts.bitnami.com/bitnami
    condition: postgresql.enabled
    tags:
      - database
  - name: redis
    version: 17.x.x
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
    tags:
      - cache

annotations:
  category: Application
  licenses: Apache-2.0
  org.opencontainers.image.vendor: "Company Name"
  org.opencontainers.image.source: "https://github.com/company/myapp"
```

---

## values.yaml - Default Configuration

```yaml
# Default values for production-ready deployment
# This is a YAML-formatted file declaring variables for templates

## Global Configuration
global:
  imageRegistry: ""
  imagePullSecrets: []
  storageClass: ""

## Replica Configuration
replicaCount: 3

## Image Configuration
image:
  registry: docker.io
  repository: company/myapp
  pullPolicy: IfNotPresent
  tag: ""  # Overrides appVersion from Chart.yaml
  digest: ""  # sha256:abc... for immutable deployments

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

## Service Account Configuration
serviceAccount:
  create: true
  annotations: {}
  # Example: eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT:role/myapp
  name: ""
  automount: true

## Pod Security Context (Pod-level security settings)
podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  fsGroupChangePolicy: "OnRootMismatch"
  seccompProfile:
    type: RuntimeDefault

## Container Security Context (Container-level security)
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  runAsNonRoot: true
  runAsUser: 1000
  capabilities:
    drop:
      - ALL
    add:
      - NET_BIND_SERVICE

## Application Configuration
application:
  env:
    - name: ENVIRONMENT
      value: "production"
    - name: LOG_LEVEL
      value: "info"
    - name: LOG_FORMAT
      value: "json"
    - name: DATABASE_HOST
      value: "{{ .Release.Name }}-postgresql"
    - name: REDIS_HOST
      value: "{{ .Release.Name }}-redis-master"
  envFrom:
    - secretRef:
        name: "{{ include \"myapp.fullname\" . }}-secrets"
    - configMapRef:
        name: "{{ include \"myapp.fullname\" . }}-config"

## Service Configuration
service:
  type: ClusterIP
  port: 80
  targetPort: 8080
  annotations: {}
  sessionAffinity: None
  # Example annotations:
  # service.beta.kubernetes.io/aws-load-balancer-type: nlb
  # cloud.google.com/neg: '{"ingress": true}'

## Ingress Configuration
ingress:
  enabled: true
  className: "nginx"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/proxy-body-size: "10m"
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-tls
      hosts:
        - myapp.example.com

## Resource Limits and Requests (REQUIRED for production)
resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 250m
    memory: 256Mi

## Health Check Probes
livenessProbe:
  httpGet:
    path: /health/live
    port: 8080
    scheme: HTTP
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  successThreshold: 1
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
    scheme: HTTP
  initialDelaySeconds: 10
  periodSeconds: 5
  timeoutSeconds: 3
  successThreshold: 1
  failureThreshold: 3

startupProbe:
  httpGet:
    path: /health/startup
    port: 8080
    scheme: HTTP
  initialDelaySeconds: 0
  periodSeconds: 10
  timeoutSeconds: 3
  successThreshold: 1
  failureThreshold: 30

## Horizontal Pod Autoscaler (HPA)
autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 60
        - type: Pods
          value: 2
          periodSeconds: 60
      selectPolicy: Min
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 30
        - type: Pods
          value: 4
          periodSeconds: 30
      selectPolicy: Max

## Pod Disruption Budget (PDB) for high availability
podDisruptionBudget:
  enabled: true
  minAvailable: 1
  # maxUnavailable: 1

## Pod Annotations and Labels
podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "8080"
  prometheus.io/path: "/metrics"

podLabels:
  app.kubernetes.io/component: api

## Node Selector for pod placement
nodeSelector: {}
  # kubernetes.io/arch: amd64
  # node-type: applications

## Tolerations for dedicated nodes
tolerations: []
  # - key: "dedicated"
  #   operator: "Equal"
  #   value: "applications"
  #   effect: "NoSchedule"

## Affinity Rules for pod distribution
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
              - key: app.kubernetes.io/name
                operator: In
                values:
                  - myapp
          topologyKey: kubernetes.io/hostname
      - weight: 50
        podAffinityTerm:
          labelSelector:
            matchExpressions:
              - key: app.kubernetes.io/name
                operator: In
                values:
                  - myapp
          topologyKey: topology.kubernetes.io/zone

## ConfigMap for application configuration
configMap:
  enabled: true
  data:
    app.conf: |
      server_timeout=30
      max_connections=100
      cache_ttl=3600
      feature_flags_enabled=true

## Secrets (INSECURE - use external-secrets in production)
secrets:
  enabled: true
  stringData:
    # WARNING: Use external-secrets or sealed-secrets in production
    DB_PASSWORD: "CHANGE_ME_IN_PRODUCTION"
    API_KEY: "CHANGE_ME_IN_PRODUCTION"
    JWT_SECRET: "CHANGE_ME_IN_PRODUCTION"

## External Secrets Operator Integration (RECOMMENDED)
externalSecrets:
  enabled: false
  backend: aws-secretsmanager  # aws-secretsmanager, vault, gcpsm, azurekv
  secretStoreRef:
    name: aws-secretsmanager
    kind: SecretStore
  refreshInterval: 1h
  data:
    - secretKey: DB_PASSWORD
      remoteRef:
        key: /prod/myapp/db-password
    - secretKey: API_KEY
      remoteRef:
        key: /prod/myapp/api-key
    - secretKey: JWT_SECRET
      remoteRef:
        key: /prod/myapp/jwt-secret

## Persistent Volume Claim
persistence:
  enabled: true
  storageClass: ""  # Use default StorageClass
  accessModes:
    - ReadWriteOnce
  size: 10Gi
  annotations: {}
  mountPath: /data
  subPath: ""

## ServiceMonitor for Prometheus Operator
serviceMonitor:
  enabled: true
  namespace: ""
  interval: 30s
  scrapeTimeout: 10s
  labels:
    prometheus: kube-prometheus
  relabelings: []
  metricRelabelings: []

## NetworkPolicy for pod-level firewall
networkPolicy:
  enabled: true
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8080
  egress:
    # Allow DNS
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
    # Allow PostgreSQL
    - to:
        - podSelector:
            matchLabels:
              app.kubernetes.io/name: postgresql
      ports:
        - protocol: TCP
          port: 5432
    # Allow Redis
    - to:
        - podSelector:
            matchLabels:
              app.kubernetes.io/name: redis
      ports:
        - protocol: TCP
          port: 6379
    # Allow HTTPS egress
    - to:
        - namespaceSelector: {}
      ports:
        - protocol: TCP
          port: 443

## PostgreSQL Dependency (Bitnami Chart)
postgresql:
  enabled: true
  auth:
    username: myapp
    password: CHANGE_ME_IN_PRODUCTION
    database: myapp_production
    existingSecret: ""  # Use in production
  primary:
    persistence:
      enabled: true
      size: 20Gi
    resources:
      limits:
        memory: 2Gi
        cpu: 1000m
      requests:
        memory: 512Mi
        cpu: 250m
    podSecurityContext:
      enabled: true
      fsGroup: 1001
    containerSecurityContext:
      enabled: true
      runAsUser: 1001
      runAsNonRoot: true

## Redis Dependency (Bitnami Chart)
redis:
  enabled: true
  architecture: standalone  # or replication for HA
  auth:
    enabled: true
    password: CHANGE_ME_IN_PRODUCTION
    existingSecret: ""  # Use in production
  master:
    persistence:
      enabled: true
      size: 5Gi
    resources:
      limits:
        memory: 1Gi
        cpu: 500m
      requests:
        memory: 256Mi
        cpu: 100m
  replica:
    replicaCount: 0  # Set >0 for HA
```

---

## values-dev.yaml - Development Environment

```yaml
# Development environment overrides
replicaCount: 1

image:
  tag: "dev-latest"
  pullPolicy: Always

ingress:
  enabled: true
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-staging"
  hosts:
    - host: myapp-dev.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-dev-tls
      hosts:
        - myapp-dev.example.com

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 100m
    memory: 128Mi

autoscaling:
  enabled: false

podDisruptionBudget:
  enabled: false

postgresql:
  enabled: true
  auth:
    password: dev-password
  primary:
    persistence:
      size: 5Gi
    resources:
      limits:
        memory: 512Mi
        cpu: 500m
      requests:
        memory: 256Mi
        cpu: 100m

redis:
  enabled: true
  auth:
    password: dev-password
  master:
    persistence:
      size: 1Gi
    resources:
      limits:
        memory: 256Mi
        cpu: 250m
      requests:
        memory: 128Mi
        cpu: 50m

externalSecrets:
  enabled: false

networkPolicy:
  enabled: false
```

---

## values-prod.yaml - Production Environment

```yaml
# Production environment overrides
replicaCount: 5

image:
  # Use immutable digest for production
  digest: "sha256:abc123def456..."
  pullPolicy: IfNotPresent

ingress:
  enabled: true
  className: "nginx"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rate-limit: "1000"
    nginx.ingress.kubernetes.io/enable-cors: "true"
    nginx.ingress.kubernetes.io/cors-allow-origin: "https://example.com"
  hosts:
    - host: api.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: api-tls-production
      hosts:
        - api.example.com

resources:
  limits:
    cpu: 2000m
    memory: 4Gi
  requests:
    cpu: 1000m
    memory: 2Gi

autoscaling:
  enabled: true
  minReplicas: 5
  maxReplicas: 50
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

podDisruptionBudget:
  enabled: true
  minAvailable: 2

externalSecrets:
  enabled: true
  backend: aws-secretsmanager

secrets:
  enabled: false  # Use externalSecrets instead

postgresql:
  enabled: true
  architecture: replication
  auth:
    existingSecret: postgresql-credentials
  primary:
    persistence:
      size: 100Gi
    resources:
      limits:
        memory: 8Gi
        cpu: 4000m
      requests:
        memory: 4Gi
        cpu: 2000m
  readReplicas:
    replicaCount: 2
    persistence:
      size: 100Gi
    resources:
      limits:
        memory: 8Gi
        cpu: 4000m

redis:
  enabled: true
  architecture: replication
  auth:
    existingSecret: redis-credentials
  master:
    persistence:
      size: 20Gi
    resources:
      limits:
        memory: 2Gi
        cpu: 1000m
  replica:
    replicaCount: 3
    persistence:
      size: 20Gi
    resources:
      limits:
        memory: 2Gi
        cpu: 1000m

networkPolicy:
  enabled: true

serviceMonitor:
  enabled: true
```

---

## templates/_helpers.tpl - Template Helper Functions

```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "myapp.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "myapp.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "myapp.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "myapp.labels" -}}
helm.sh/chart: {{ include "myapp.chart" . }}
{{ include "myapp.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: {{ include "myapp.name" . }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "myapp.selectorLabels" -}}
app.kubernetes.io/name: {{ include "myapp.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "myapp.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "myapp.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
```

---

## Deployment Commands

### Installation and Upgrades

```bash
# Lint and validate chart
helm lint ./myapp
helm template myapp ./myapp --values ./myapp/values.yaml --debug | kubeval

# Dry-run installation
helm install myapp ./myapp --dry-run --debug

# Install to development
helm install myapp ./myapp \
  --namespace dev \
  --create-namespace \
  --values ./myapp/values-dev.yaml \
  --wait \
  --timeout 5m

# Install to production with atomic rollback on failure
helm install myapp ./myapp \
  --namespace production \
  --create-namespace \
  --values ./myapp/values-prod.yaml \
  --atomic \
  --wait \
  --timeout 10m

# Upgrade existing release
helm upgrade myapp ./myapp \
  --namespace production \
  --values ./myapp/values-prod.yaml \
  --atomic \
  --wait \
  --timeout 10m

# Upgrade with history limit
helm upgrade myapp ./myapp \
  --namespace production \
  --values ./myapp/values-prod.yaml \
  --history-max 10 \
  --atomic

# Rollback to previous version
helm rollback myapp 0 --namespace production --wait

# Rollback to specific revision
helm rollback myapp 3 --namespace production --wait
```

### Management Commands

```bash
# List releases
helm list --namespace production

# Get release status
helm status myapp --namespace production

# Get release history
helm history myapp --namespace production

# Get values for release
helm get values myapp --namespace production

# Get rendered manifests
helm get manifest myapp --namespace production

# Uninstall release (keeps history)
helm uninstall myapp --namespace production

# Uninstall and delete history
helm uninstall myapp --namespace production --no-hooks

# Test release (requires test pods)
helm test myapp --namespace production
```

### Chart Packaging and Distribution

```bash
# Package chart
helm package ./myapp

# Update dependencies
helm dependency update ./myapp

# Push to OCI registry (Harbor, ECR, ACR, GAR)
helm package ./myapp
helm push myapp-1.0.0.tgz oci://registry.company.com/helm-charts

# Install from OCI registry
helm install myapp oci://registry.company.com/helm-charts/myapp --version 1.0.0

# Sign chart with GPG
helm package --sign --key 'Company Key' --keyring ~/.gnupg/secring.gpg ./myapp

# Verify signed chart
helm verify myapp-1.0.0.tgz --keyring ~/.gnupg/pubring.gpg
```

---

## Best Practices Checklist

### Security
- [ ] Use semantic versioning for chart and app versions
- [ ] Pin all dependency versions explicitly
- [ ] Use immutable image tags (digests) in production
- [ ] Set pod security context (runAsNonRoot, readOnlyRootFilesystem)
- [ ] Drop ALL capabilities and add only required ones
- [ ] Use External Secrets Operator or Sealed Secrets for secrets
- [ ] Configure RBAC with least privilege ServiceAccount
- [ ] Implement NetworkPolicy for pod-level firewall
- [ ] Sign Helm charts with GPG for supply chain security

### High Availability
- [ ] Set minimum 3 replicas for production
- [ ] Configure HPA for auto-scaling based on CPU/memory
- [ ] Enable PodDisruptionBudget (minAvailable: 1)
- [ ] Add pod anti-affinity for zone/node distribution
- [ ] Use readiness probes to prevent traffic to unhealthy pods
- [ ] Configure liveness probes for automatic pod restart
- [ ] Set appropriate startup probes for slow-starting apps

### Resource Management
- [ ] Define resource requests and limits for all containers
- [ ] Set memory and CPU requests matching typical usage
- [ ] Set limits 2-4x higher than requests for burstability
- [ ] Configure resource quotas per namespace
- [ ] Monitor actual resource usage and adjust

### Observability
- [ ] Add Prometheus annotations for metrics scraping
- [ ] Configure ServiceMonitor for Prometheus Operator
- [ ] Implement /health/live and /health/ready endpoints
- [ ] Use structured JSON logging
- [ ] Add tracing integration (Jaeger, Zipkin)
- [ ] Include deployment metadata in labels/annotations

### Operations
- [ ] Test rollback procedures regularly
- [ ] Document all values.yaml parameters
- [ ] Use helm lint and kubeval for validation
- [ ] Test with --dry-run before production
- [ ] Use --atomic for automatic rollback on failure
- [ ] Limit revision history (--history-max 10)
- [ ] Store charts in OCI-compliant registry
- [ ] Implement CI/CD pipeline for chart validation
- [ ] Version control all Helm charts and values files

### Dependencies
- [ ] Pin PostgreSQL/Redis versions explicitly
- [ ] Use existingSecret for database credentials
- [ ] Enable replication for production databases
- [ ] Configure appropriate storage sizes
- [ ] Set resource limits for all dependencies
- [ ] Back up persistent volumes regularly

---

## GitOps Integration (ArgoCD / Flux)

### ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/company/helm-charts
    targetRevision: HEAD
    path: charts/myapp
    helm:
      valueFiles:
        - values-prod.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### Flux HelmRelease

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: myapp
  namespace: production
spec:
  interval: 10m
  chart:
    spec:
      chart: myapp
      version: 1.0.0
      sourceRef:
        kind: HelmRepository
        name: company-charts
        namespace: flux-system
  values:
    # Inline values or reference to values file
  valuesFrom:
    - kind: ConfigMap
      name: myapp-values
```

---

## Troubleshooting

### Common Issues

```bash
# Check pod status
kubectl get pods -n production -l app.kubernetes.io/name=myapp

# View pod logs
kubectl logs -n production -l app.kubernetes.io/name=myapp --tail=100 -f

# Describe problematic pod
kubectl describe pod -n production POD_NAME

# Check events
kubectl get events -n production --sort-by='.lastTimestamp'

# Debug with ephemeral container
kubectl debug -n production POD_NAME -it --image=busybox

# View Helm release notes
helm get notes myapp -n production

# Check if values are applied correctly
helm get values myapp -n production
```

---

**Template Version:** 1.0.0
**Last Updated:** 2025-10-26
**Maintainer:** Platform Engineering Team
