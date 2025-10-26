# Installer Manifests

## Document Information

**Purpose**: Define declarative installation, upgrade, and lifecycle management configurations using Helm charts, Kubernetes Operators, and package managers to enable repeatable, automated, and self-service application deployments across environments.

**Format**: Markdown with Helm, Operator, and installer examples

**Target Audience**: Platform Engineers, Application Developers, DevOps Engineers, Customer Support (for on-premise installations)

**Related Artifacts**:
- Kubernetes Manifests
- Kustomize Overlays
- Operator SDK Configurations
- Deployment Plans

---

## Metadata

```yaml
version: "1.3.0"
created: "2024-01-12"
lastModified: "2024-01-23"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
```

---

## 1. Helm Charts

### 1.1 Chart Structure

```
api-service/
├── Chart.yaml           # Chart metadata
├── values.yaml          # Default values
├── values-dev.yaml      # Dev environment overrides
├── values-staging.yaml  # Staging overrides
├── values-prod.yaml     # Production overrides
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── serviceaccount.yaml
│   ├── _helpers.tpl    # Template helpers
│   └── NOTES.txt       # Post-install notes
├── charts/             # Chart dependencies
└── README.md
```

### 1.2 Chart.yaml

```yaml
apiVersion: v2
name: api-service
description: Production-grade API service with autoscaling and observability
type: application
version: 1.5.0  # Chart version
appVersion: "2.3.1"  # Application version

keywords:
  - api
  - backend
  - microservice

home: https://github.com/company/api-service
sources:
  - https://github.com/company/api-service

maintainers:
  - name: Platform Team
    email: platform@company.com
    url: https://platform.company.com

dependencies:
  - name: postgresql
    version: 12.x.x
    repository: https://charts.bitnami.com/bitnami
    condition: postgresql.enabled

  - name: redis
    version: 17.x.x
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled

annotations:
  category: Infrastructure
  licenses: Apache-2.0
```

### 1.3 values.yaml (Default Values)

```yaml
# Default values for api-service
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 2

image:
  repository: ghcr.io/company/api-service
  pullPolicy: IfNotPresent
  tag: ""  # Overrides appVersion in Chart.yaml

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

serviceAccount:
  create: true
  annotations: {}
  name: ""

podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "8080"
  prometheus.io/path: "/metrics"

podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 1000

securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true

service:
  type: ClusterIP
  port: 80
  targetPort: 8080
  annotations: {}

ingress:
  enabled: false
  className: "nginx"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
  hosts:
    - host: api.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: api-tls
      hosts:
        - api.example.com

resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

podDisruptionBudget:
  enabled: true
  minAvailable: 1

nodeSelector: {}

tolerations: []

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
                  - api-service
          topologyKey: kubernetes.io/hostname

env:
  - name: NODE_ENV
    value: production
  - name: LOG_LEVEL
    value: info
  - name: PORT
    value: "8080"

envFrom: []

secrets: {}

postgresql:
  enabled: true
  auth:
    username: apiuser
    password: changeme
    database: apidb

redis:
  enabled: true
  auth:
    enabled: true
    password: changeme
```

### 1.4 Production Values Override

**File**: `values-prod.yaml`

```yaml
replicaCount: 10

image:
  tag: "v2.3.1"

ingress:
  enabled: true
  hosts:
    - host: api.company.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: api-prod-tls
      hosts:
        - api.company.com

resources:
  limits:
    cpu: 2000m
    memory: 2Gi
  requests:
    cpu: 500m
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 10
  maxReplicas: 100
  targetCPUUtilizationPercentage: 70

env:
  - name: NODE_ENV
    value: production
  - name: LOG_LEVEL
    value: warn
  - name: ENABLE_APM
    value: "true"

postgresql:
  enabled: true
  primary:
    persistence:
      size: 100Gi
    resources:
      limits:
        cpu: 4000m
        memory: 8Gi
      requests:
        cpu: 1000m
        memory: 2Gi

redis:
  enabled: true
  master:
    persistence:
      size: 20Gi
    resources:
      limits:
        cpu: 1000m
        memory: 2Gi
```

### 1.5 Deployment Template

**File**: `templates/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "api-service.fullname" . }}
  labels:
    {{- include "api-service.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "api-service.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      labels:
        {{- include "api-service.selectorLabels" . | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "api-service.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
      - name: {{ .Chart.Name }}
        securityContext:
          {{- toYaml .Values.securityContext | nindent 12 }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: {{ .Values.service.targetPort }}
          protocol: TCP
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
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
        env:
          {{- toYaml .Values.env | nindent 12 }}
        {{- with .Values.envFrom }}
        envFrom:
          {{- toYaml . | nindent 12 }}
        {{- end }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
```

### 1.6 Helm Commands

```bash
# Install chart
helm install api-service ./api-service \
  --namespace production \
  --create-namespace \
  --values values-prod.yaml

# Upgrade chart
helm upgrade api-service ./api-service \
  --namespace production \
  --values values-prod.yaml \
  --set image.tag=v2.3.2

# Rollback
helm rollback api-service 3 --namespace production

# Uninstall
helm uninstall api-service --namespace production

# Dry-run (test without applying)
helm install api-service ./api-service --dry-run --debug

# Template rendering (view generated manifests)
helm template api-service ./api-service --values values-prod.yaml
```

---

## 2. Kubernetes Operators

### 2.1 Custom Resource Definition (CRD)

**File**: `config/crd/apiservice.yaml`

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: apiservices.platform.company.com
spec:
  group: platform.company.com
  versions:
    - name: v1alpha1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                version:
                  type: string
                  description: API service version
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 100
                  default: 2
                database:
                  type: object
                  properties:
                    enabled:
                      type: boolean
                      default: true
                    size:
                      type: string
                      default: "10Gi"
                resources:
                  type: object
                  properties:
                    limits:
                      type: object
                      properties:
                        cpu:
                          type: string
                        memory:
                          type: string
            status:
              type: object
              properties:
                ready:
                  type: boolean
                conditions:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                      status:
                        type: string
                      lastTransitionTime:
                        type: string
                      reason:
                        type: string
                      message:
                        type: string
      subresources:
        status: {}
  scope: Namespaced
  names:
    plural: apiservices
    singular: apiservice
    kind: APIService
    shortNames:
      - apisvc
```

### 2.2 Custom Resource Example

```yaml
apiVersion: platform.company.com/v1alpha1
kind: APIService
metadata:
  name: production-api
  namespace: production
spec:
  version: "2.3.1"
  replicas: 10

  database:
    enabled: true
    size: "100Gi"
    backupSchedule: "0 2 * * *"

  resources:
    limits:
      cpu: "2000m"
      memory: "2Gi"
    requests:
      cpu: "500m"
      memory: "512Mi"

  ingress:
    enabled: true
    host: api.company.com
    tls: true

  monitoring:
    enabled: true
    scrapeInterval: 30s
```

### 2.3 Operator Reconciliation Logic (Go)

```go
package controller

import (
    "context"
    "k8s.io/apimachinery/pkg/runtime"
    ctrl "sigs.k8s.io/controller-runtime"
    "sigs.k8s.io/controller-runtime/pkg/client"

    platformv1alpha1 "github.com/company/operator/api/v1alpha1"
)

type APIServiceReconciler struct {
    client.Client
    Scheme *runtime.Scheme
}

func (r *APIServiceReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // Fetch the APIService instance
    apiService := &platformv1alpha1.APIService{}
    err := r.Get(ctx, req.NamespacedName, apiService)
    if err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }

    // Reconcile Deployment
    deployment := r.constructDeployment(apiService)
    if err := r.reconcileDeployment(ctx, apiService, deployment); err != nil {
        return ctrl.Result{}, err
    }

    // Reconcile Service
    service := r.constructService(apiService)
    if err := r.reconcileService(ctx, apiService, service); err != nil {
        return ctrl.Result{}, err
    }

    // Reconcile Database (if enabled)
    if apiService.Spec.Database.Enabled {
        db := r.constructDatabase(apiService)
        if err := r.reconcileDatabase(ctx, apiService, db); err != nil {
            return ctrl.Result{}, err
        }
    }

    // Update status
    apiService.Status.Ready = true
    if err := r.Status().Update(ctx, apiService); err != nil {
        return ctrl.Result{}, err
    }

    return ctrl.Result{}, nil
}
```

---

## 3. Package-Based Installers

### 3.1 Homebrew Formula (macOS/Linux)

```ruby
# Formula/api-cli.rb
class ApiCli < Formula
  desc "Command-line tool for Company API"
  homepage "https://github.com/company/api-cli"
  url "https://github.com/company/api-cli/archive/v2.3.1.tar.gz"
  sha256 "abc123..."
  license "Apache-2.0"

  depends_on "go" => :build

  def install
    system "go", "build", *std_go_args
    bin.install "api-cli"
  end

  test do
    assert_match "version 2.3.1", shell_output("#{bin}/api-cli version")
  end
end
```

### 3.2 APT Package (Debian/Ubuntu)

```bash
# Install via APT repository
curl -fsSL https://packages.company.com/gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://packages.company.com/apt stable main"
sudo apt update
sudo apt install api-service
```

### 3.3 RPM Package (RHEL/CentOS)

```bash
# Install via YUM repository
sudo rpm --import https://packages.company.com/gpg.key
sudo yum-config-manager --add-repo https://packages.company.com/rpm/api-service.repo
sudo yum install api-service
```

---

## 4. Installation Best Practices

### 4.1 Pre-Installation Checks

```bash
#!/bin/bash
# pre-install.sh

set -e

echo "Running pre-installation checks..."

# Check Kubernetes version
K8S_VERSION=$(kubectl version --short | grep "Server Version" | awk '{print $3}')
echo "Kubernetes version: $K8S_VERSION"

# Check cluster capacity
echo "Checking cluster resources..."
kubectl top nodes

# Check for required CRDs
echo "Checking for required CRDs..."
kubectl get crd

# Verify namespace exists
kubectl get namespace production || kubectl create namespace production

echo "Pre-installation checks complete!"
```

### 4.2 Post-Installation Validation

```bash
#!/bin/bash
# post-install-validation.sh

set -e

echo "Validating installation..."

# Wait for pods to be ready
kubectl wait --for=condition=ready pod \
  -l app=api-service \
  -n production \
  --timeout=300s

# Check endpoints
kubectl get endpoints -n production

# Run smoke tests
curl -f https://api.company.com/health || exit 1

echo "Installation validated successfully!"
```

---

## 5. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.3.0 | 2024-01-23 | Platform Team | Added Kubernetes Operator examples, CRD definitions |
| 1.2.0 | 2024-01-18 | DevOps Team | Added production Helm values, package managers |
| 1.1.0 | 2024-01-15 | Engineering | Enhanced Helm chart templates, added HPA |
| 1.0.0 | 2024-01-12 | Platform Team | Initial Helm chart and installer documentation |

---

## 6. Related Documentation

- [Helm Best Practices](https://helm.sh/docs/chart_best_practices/)
- [Operator SDK](https://sdk.operatorframework.io/)
- [Kubernetes Manifests](./kubernetes-manifests.md)
- [Kustomize Overlays](./kustomize-manifests.md)
- [Deployment Plan](./deployment-plan.md)
