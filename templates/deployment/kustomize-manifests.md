# Kustomize Manifests

## Document Information

**Purpose**: Define template-free Kubernetes configuration management using Kustomize bases, overlays, patches, and generators for GitOps-based deployments with environment parity.

**Format**: Markdown with Kustomize directory structures and YAML examples

**Target Audience**: Platform Engineers, DevOps Engineers, Application Developers, SRE Teams

**Related Artifacts**:
- Kubernetes Deployment Manifests
- Environment Matrix
- Helm Charts
- GitOps Application Definitions (ArgoCD, Flux)
- CI/CD Pipeline Definitions

---

## Metadata

```yaml
version: "1.3.0"
created: "2024-01-10"
lastModified: "2024-01-20"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
approvers:
  - name: "Jamie Chen"
    role: "Principal Platform Engineer"
    date: "2024-01-20"
  - name: "Marcus Rodriguez"
    role: "DevOps Lead"
    date: "2024-01-20"
```

---

## 1. Kustomize Overview

### 1.1 Core Principles

**Kustomize** is a Kubernetes-native configuration management tool that provides:
- **Template-free**: Pure Kubernetes YAML without templating languages
- **Declarative overlays**: Environment-specific customizations through layers
- **Strategic merge patches**: Partial resource modifications
- **Component composition**: Reusable configuration modules
- **GitOps-ready**: Seamless integration with ArgoCD and Flux

### 1.2 Directory Structure Pattern

```
k8s/
├── base/                          # Common base configurations
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── kustomization.yaml
│
├── components/                    # Reusable components
│   ├── monitoring/
│   │   ├── servicemonitor.yaml
│   │   └── kustomization.yaml
│   └── security/
│       ├── networkpolicy.yaml
│       └── kustomization.yaml
│
└── overlays/                      # Environment-specific overlays
    ├── dev/
    │   ├── kustomization.yaml
    │   ├── patches/
    │   │   └── replica-count.yaml
    │   └── configmap-dev.yaml
    ├── staging/
    │   ├── kustomization.yaml
    │   ├── patches/
    │   │   ├── replica-count.yaml
    │   │   └── resources.yaml
    │   └── configmap-staging.yaml
    └── production/
        ├── kustomization.yaml
        ├── patches/
        │   ├── replica-count.yaml
        │   ├── resources.yaml
        │   └── hpa.yaml
        └── configmap-production.yaml
```

---

## 2. Base Manifests

### 2.1 Base Deployment

**File**: `k8s/base/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  labels:
    app: api-service
    component: backend
spec:
  replicas: 2  # Will be overridden by overlays
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
        component: backend
    spec:
      containers:
      - name: api
        image: ghcr.io/company/api-service:latest  # Will be updated by CI/CD
        ports:
        - containerPort: 8080
          name: http
          protocol: TCP
        env:
        - name: NODE_ENV
          value: production
        - name: LOG_LEVEL
          value: info
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: http
          initialDelaySeconds: 5
          periodSeconds: 5
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
          capabilities:
            drop:
              - ALL
```

### 2.2 Base Service

**File**: `k8s/base/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
  labels:
    app: api-service
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: http
    protocol: TCP
    name: http
  selector:
    app: api-service
```

### 2.3 Base ConfigMap

**File**: `k8s/base/configmap.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-service-config
data:
  app.conf: |
    server {
      port = 8080
      timeout = 30s
    }
  database.conf: |
    pool_size = 10
    max_connections = 100
```

### 2.4 Base Kustomization

**File**: `k8s/base/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: default

commonLabels:
  app.kubernetes.io/name: api-service
  app.kubernetes.io/managed-by: kustomize

commonAnnotations:
  description: "API Service - Base Configuration"

resources:
  - deployment.yaml
  - service.yaml
  - configmap.yaml

# Generate ConfigMaps from files with hash suffixes
configMapGenerator:
  - name: api-service-env
    literals:
      - NODE_ENV=production
      - LOG_LEVEL=info
    options:
      disableNameSuffixHash: false  # Add hash for rolling updates

# Common resource modifications
images:
  - name: ghcr.io/company/api-service
    newTag: latest  # Will be updated by CI/CD
```

---

## 3. Environment Overlays

### 3.1 Development Overlay

**File**: `k8s/overlays/dev/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: development

# Reference base
bases:
  - ../../base

# Development-specific labels
commonLabels:
  environment: development
  tier: non-production

commonAnnotations:
  contact: "dev-team@company.com"

# Development-specific replicas
replicas:
  - name: api-service
    count: 1

# Development ConfigMap with debug settings
configMapGenerator:
  - name: api-service-env
    behavior: merge
    literals:
      - NODE_ENV=development
      - LOG_LEVEL=debug
      - DEBUG=true
      - ENABLE_PROFILING=true

# Strategic merge patch for resources
patches:
  - path: patches/replica-count.yaml
  - path: patches/debug-settings.yaml

# Development-specific resources
resources:
  - ingress-dev.yaml
```

**File**: `k8s/overlays/dev/patches/replica-count.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
spec:
  replicas: 1
```

**File**: `k8s/overlays/dev/patches/debug-settings.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
spec:
  template:
    spec:
      containers:
      - name: api
        env:
        - name: DEBUG
          value: "true"
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 256Mi
```

### 3.2 Staging Overlay

**File**: `k8s/overlays/staging/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: staging

bases:
  - ../../base

# Include monitoring component
components:
  - ../../components/monitoring
  - ../../components/security

commonLabels:
  environment: staging
  tier: non-production

replicas:
  - name: api-service
    count: 2

configMapGenerator:
  - name: api-service-env
    behavior: merge
    literals:
      - NODE_ENV=staging
      - LOG_LEVEL=info
      - ENABLE_APM=true

# Staging patches
patches:
  - path: patches/replica-count.yaml
  - path: patches/resources.yaml
  - path: patches/monitoring.yaml

resources:
  - ingress-staging.yaml
  - pdb.yaml  # PodDisruptionBudget

images:
  - name: ghcr.io/company/api-service
    newTag: staging-latest
```

**File**: `k8s/overlays/staging/patches/resources.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
spec:
  template:
    spec:
      containers:
      - name: api
        resources:
          requests:
            cpu: 250m
            memory: 256Mi
          limits:
            cpu: 1000m
            memory: 1Gi
```

**File**: `k8s/overlays/staging/pdb.yaml`

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-service-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: api-service
```

### 3.3 Production Overlay

**File**: `k8s/overlays/production/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

bases:
  - ../../base

components:
  - ../../components/monitoring
  - ../../components/security
  - ../../components/backup

commonLabels:
  environment: production
  tier: production
  compliance: pci-dss

commonAnnotations:
  contact: "sre-team@company.com"
  escalation: "pagerduty"

replicas:
  - name: api-service
    count: 10

configMapGenerator:
  - name: api-service-env
    behavior: merge
    literals:
      - NODE_ENV=production
      - LOG_LEVEL=warn
      - ENABLE_APM=true
      - ENABLE_PROFILING=false

# Production patches with security hardening
patches:
  - path: patches/replica-count.yaml
  - path: patches/resources.yaml
  - path: patches/security.yaml
  - path: patches/affinity.yaml

# JSON patch for precise modifications
patchesJson6902:
  - target:
      group: apps
      version: v1
      kind: Deployment
      name: api-service
    patch: |-
      - op: add
        path: /spec/template/spec/priorityClassName
        value: high-priority

resources:
  - ingress-production.yaml
  - hpa.yaml  # HorizontalPodAutoscaler
  - pdb.yaml
  - networkpolicy.yaml

images:
  - name: ghcr.io/company/api-service
    newName: ghcr.io/company/api-service
    newTag: v1.2.3  # Managed by CI/CD
```

**File**: `k8s/overlays/production/patches/security.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: api
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
          capabilities:
            drop:
              - ALL
```

**File**: `k8s/overlays/production/hpa.yaml`

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-service-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-service
  minReplicas: 10
  maxReplicas: 100
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
```

---

## 4. Components (Reusable Modules)

### 4.1 Monitoring Component

**File**: `k8s/components/monitoring/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - servicemonitor.yaml
  - podmonitor.yaml
```

**File**: `k8s/components/monitoring/servicemonitor.yaml`

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: api-service
  labels:
    prometheus: kube-prometheus
spec:
  selector:
    matchLabels:
      app: api-service
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
    scrapeTimeout: 10s
```

### 4.2 Security Component

**File**: `k8s/components/security/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - networkpolicy.yaml
  - podsecuritypolicy.yaml
```

**File**: `k8s/components/security/networkpolicy.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-service-netpol
spec:
  podSelector:
    matchLabels:
      app: api-service
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
  - to:
    - namespaceSelector:
        matchLabels:
          name: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector: {}
      podSelector:
        matchLabels:
          k8s-app: kube-dns
    ports:
    - protocol: UDP
      port: 53
```

---

## 5. Advanced Kustomization Features

### 5.1 Remote Bases

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  # Reference remote base from Git repository
  - github.com/company/k8s-base/api-service?ref=v1.2.0

  # Reference from OCI registry
  - oci://ghcr.io/company/k8s-manifests/api-service:v1.0.0
```

### 5.2 Replacements (Variable Substitution)

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

replacements:
  - source:
      kind: ConfigMap
      name: app-config
      fieldPath: data.api_url
    targets:
      - select:
          kind: Deployment
        fieldPaths:
          - spec.template.spec.containers.[name=api].env.[name=API_URL].value
```

### 5.3 Secret Generation

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

secretGenerator:
  - name: api-secrets
    envs:
      - secrets.env
    options:
      disableNameSuffixHash: false
      immutable: true
```

---

## 6. GitOps Integration

### 6.1 ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: api-service-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/company/k8s-manifests
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### 6.2 Flux Kustomization

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: api-service-prod
  namespace: flux-system
spec:
  interval: 5m
  path: ./overlays/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: k8s-manifests
  targetNamespace: production
  validation: client
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: api-service
      namespace: production
```

---

## 7. Build and Validation

### 7.1 Build Kustomization

```bash
# Build and preview manifests
kustomize build overlays/production

# Build and apply
kustomize build overlays/production | kubectl apply -f -

# Build with kubectl (v1.14+)
kubectl apply -k overlays/production

# Diff before applying
kustomize build overlays/production | kubectl diff -f -
```

### 7.2 Validation

```bash
# Validate with kubeval
kustomize build overlays/production | kubeval --strict

# Validate with kubeconform
kustomize build overlays/production | kubeconform -strict -summary

# Policy validation with conftest
kustomize build overlays/production | conftest test -p policies/ -
```

---

## 8. Best Practices

### 8.1 Overlay Strategy

1. **Minimal Overlays**: Override only what differs from base
2. **Strategic Merge First**: Use strategic merge patches for readability
3. **JSON Patches for Precision**: Use JSON patches for complex or array modifications
4. **Component Composition**: Extract cross-cutting concerns (monitoring, security)
5. **Hash Suffixes**: Enable for ConfigMaps/Secrets to trigger rolling updates

### 8.2 Directory Organization

```
k8s/
├── base/                    # Common to all environments
├── components/              # Reusable, optional features
├── overlays/
│   ├── dev/                # Development
│   ├── staging/            # Staging
│   └── production/         # Production
└── apps/                   # Multi-app monorepo structure
    ├── api-service/
    │   ├── base/
    │   └── overlays/
    └── web-app/
        ├── base/
        └── overlays/
```

---

## 9. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.3.0 | 2024-01-20 | Jamie Chen | Added components, replacements, GitOps examples |
| 1.2.0 | 2023-12-10 | Marcus Rodriguez | Added production security patches, HPA |
| 1.1.0 | 2023-10-15 | Platform Team | Added staging overlay, monitoring component |
| 1.0.0 | 2023-08-01 | DevOps Team | Initial Kustomize structure |

---

## 10. Related Documentation

- [Kubernetes Deployment Guide](./kubernetes-deployment.md)
- [Environment Matrix](./environment-matrix.yaml)
- [GitOps Workflow](./gitops-workflow.md)
- [Helm Charts](./helm-charts.md)
- [CI/CD Pipeline Definitions](./ci-cd-pipeline-definitions.md)
