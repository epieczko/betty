# CI/CD Pipeline Definitions

## Document Information

**Purpose**: Define automated build, test, security scan, and deployment workflows that transform source code commits into production-ready artifacts and deployed services using pipeline-as-code approaches.

**Format**: Markdown with embedded pipeline configuration examples

**Target Audience**: DevOps Engineers, Platform Engineers, Software Developers, Security Engineers, Release Managers

**Related Artifacts**:
- Deployment Plan
- Release Risk Assessment
- Environment Matrix
- Security Scanning Reports
- Infrastructure as Code

---

## Metadata

```yaml
version: "2.1.0"
created: "2024-01-15"
lastModified: "2024-01-22"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
approvers:
  - name: "Alex Rodriguez"
    role: "Principal DevOps Engineer"
    date: "2024-01-22"
  - name: "Sarah Kim"
    role: "Director of Engineering"
    date: "2024-01-22"
```

---

## 1. Pipeline Strategy

### 1.1 CI/CD Platform Selection

**Primary Platform**: GitHub Actions
**Secondary Platforms**: GitLab CI, Jenkins (legacy systems)

**Rationale**:
- GitHub Actions: Native GitHub integration, extensive marketplace, matrix builds
- GitLab CI: Self-hosted runners, advanced caching, built-in container registry
- Jenkins: Existing enterprise infrastructure, complex build orchestration

### 1.2 Pipeline Principles

- **Pipeline as Code**: All pipeline definitions stored in version control
- **Fail Fast**: Run fastest tests first, fail immediately on critical issues
- **Shift-Left Security**: Integrate security scanning in every build
- **Immutable Artifacts**: Build once, deploy many times
- **Automated Testing**: No manual testing in CI/CD pipeline
- **Deployment Frequency**: Multiple deployments per day to production
- **Quality Gates**: Automated approval gates based on test results and security scans

---

## 2. Pipeline Stages

### Standard Pipeline Flow

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Source  │──▶│  Build   │──▶│   Test   │──▶│  Scan    │──▶│ Package  │──▶│  Deploy  │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

### 2.1 Source Stage
- Trigger on: Push to branches, pull requests, tags
- Actions: Checkout code, validate branch protection
- Duration: < 30 seconds

### 2.2 Build Stage
- Dependency resolution and caching
- Code compilation and transpilation
- Asset bundling and minification
- Generate build metadata (version, commit SHA, timestamp)
- Duration: 2-5 minutes

### 2.3 Test Stage
- Unit tests (coverage threshold: 80%)
- Integration tests
- End-to-end tests (critical paths only in CI)
- Performance regression tests
- Duration: 5-10 minutes

### 2.4 Security Scan Stage
- SAST (Static Application Security Testing)
- SCA (Software Composition Analysis)
- Container vulnerability scanning
- Secret scanning
- License compliance checking
- Duration: 3-7 minutes

### 2.5 Package Stage
- Docker image building (multi-stage builds)
- Semantic versioning and tagging
- Artifact signing and provenance
- Push to artifact registry
- Duration: 2-4 minutes

### 2.6 Deploy Stage
- Environment-specific deployment (dev → staging → production)
- Infrastructure provisioning (if needed)
- Database migrations
- Smoke tests
- Rollback capability
- Duration: 3-8 minutes per environment

**Total Pipeline Duration**: 15-35 minutes (target: < 20 minutes for fast feedback)

---

## 3. Pipeline Examples

### 3.1 GitHub Actions Pipeline

**File**: `.github/workflows/ci-cd.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch:

env:
  DOCKER_REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  NODE_VERSION: '20'

permissions:
  contents: read
  packages: write
  security-events: write
  id-token: write  # For OIDC authentication

jobs:
  # =============================================================================
  # BUILD & TEST
  # =============================================================================

  build-and-test:
    name: Build and Test
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for versioning

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --prefer-offline --no-audit

      - name: Lint code
        run: npm run lint

      - name: Build application
        run: npm run build
        env:
          NODE_ENV: production

      - name: Run unit tests
        run: npm run test:unit -- --coverage

      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379

      - name: Upload test coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
          fail_ci_if_error: true
          flags: unittests

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-artifacts
          path: |
            dist/
            package.json
            package-lock.json
          retention-days: 7

  # =============================================================================
  # SECURITY SCANNING
  # =============================================================================

  security-scan:
    name: Security Scanning
    runs-on: ubuntu-latest
    needs: [build-and-test]
    timeout-minutes: 15

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'  # Fail on vulnerabilities

      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high --fail-on=all

      - name: Run GitGuardian secret scanning
        uses: GitGuardian/ggshield-action@v1
        env:
          GITHUB_PUSH_BEFORE_SHA: ${{ github.event.before }}
          GITHUB_PUSH_BASE_SHA: ${{ github.event.base }}
          GITHUB_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}

  # =============================================================================
  # DOCKER IMAGE BUILD
  # =============================================================================

  build-image:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: [build-and-test, security-scan]
    timeout-minutes: 15
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
      image-digest: ${{ steps.build.outputs.digest }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.DOCKER_REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.DOCKER_REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix={{branch}}-
            type=raw,value=latest,enable={{is_default_branch}}

      - name: Build and push Docker image
        id: build
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            NODE_VERSION=${{ env.NODE_VERSION }}
            BUILD_DATE=${{ steps.meta.outputs.created }}
            VCS_REF=${{ github.sha }}
            VERSION=${{ steps.meta.outputs.version }}

      - name: Sign container image with Cosign
        uses: sigstore/cosign-installer@v3

      - name: Sign the published Docker image
        env:
          COSIGN_EXPERIMENTAL: "true"
        run: |
          cosign sign --yes \
            ${{ env.DOCKER_REGISTRY }}/${{ env.IMAGE_NAME }}@${{ steps.build.outputs.digest }}

      - name: Scan Docker image with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.DOCKER_REGISTRY }}/${{ env.IMAGE_NAME }}@${{ steps.build.outputs.digest }}
          format: 'sarif'
          output: 'trivy-image-results.sarif'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'

  # =============================================================================
  # DEPLOY TO DEVELOPMENT
  # =============================================================================

  deploy-dev:
    name: Deploy to Development
    runs-on: ubuntu-latest
    needs: [build-image]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: development
      url: https://dev.api.company.com
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Update kubeconfig
        run: |
          aws eks update-kubeconfig \
            --name dev-eks-cluster \
            --region us-east-1

      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/api-service \
            api=${{ needs.build-image.outputs.image-tag }} \
            --namespace=development \
            --record

          kubectl rollout status deployment/api-service \
            --namespace=development \
            --timeout=5m

      - name: Run smoke tests
        run: |
          curl -f https://dev.api.company.com/health || exit 1
          curl -f https://dev.api.company.com/ready || exit 1

      - name: Notify Slack
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Deployed to Development",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "✅ *Deployment to Development Successful*\n*Image:* ${{ needs.build-image.outputs.image-tag }}\n*Commit:* <${{ github.event.head_commit.url }}|${{ github.sha }}>\n*Author:* ${{ github.actor }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_DEPLOYMENTS }}

  # =============================================================================
  # DEPLOY TO STAGING
  # =============================================================================

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [build-image]
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.api.company.com
    timeout-minutes: 15

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Update kubeconfig
        run: |
          aws eks update-kubeconfig \
            --name staging-eks-cluster \
            --region us-east-1

      - name: Deploy with Helm
        run: |
          helm upgrade --install api-service ./charts/api-service \
            --namespace=staging \
            --values=./charts/api-service/values-staging.yaml \
            --set image.tag=${{ needs.build-image.outputs.image-tag }} \
            --set image.digest=${{ needs.build-image.outputs.image-digest }} \
            --wait \
            --timeout=10m

      - name: Run integration tests
        run: |
          npm run test:e2e -- --baseUrl=https://staging.api.company.com

      - name: Run performance tests
        run: |
          k6 run --out json=results.json tests/load-test.js

  # =============================================================================
  # DEPLOY TO PRODUCTION (Manual Approval Required)
  # =============================================================================

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [build-image, deploy-staging]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://api.company.com
    timeout-minutes: 20

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::987654321098:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Update kubeconfig
        run: |
          aws eks update-kubeconfig \
            --name prod-eks-cluster \
            --region us-east-1

      - name: Canary deployment (10%)
        run: |
          helm upgrade --install api-service ./charts/api-service \
            --namespace=production \
            --values=./charts/api-service/values-production.yaml \
            --set image.tag=${{ needs.build-image.outputs.image-tag }} \
            --set canary.enabled=true \
            --set canary.weight=10 \
            --wait \
            --timeout=10m

      - name: Monitor canary metrics (5 minutes)
        run: |
          sleep 300
          # Check error rates, latency, success rate
          ./scripts/check-canary-metrics.sh

      - name: Promote to full deployment
        run: |
          helm upgrade --install api-service ./charts/api-service \
            --namespace=production \
            --values=./charts/api-service/values-production.yaml \
            --set image.tag=${{ needs.build-image.outputs.image-tag }} \
            --set canary.enabled=false \
            --wait \
            --timeout=15m

      - name: Verify deployment
        run: |
          kubectl rollout status deployment/api-service \
            --namespace=production \
            --timeout=10m

          curl -f https://api.company.com/health || exit 1

      - name: Create GitHub release
        uses: softprops/action-gh-release@v1
        if: startsWith(github.ref, 'refs/tags/')
        with:
          generate_release_notes: true
          body: |
            ## What's Changed
            - Image: ${{ needs.build-image.outputs.image-tag }}
            - Digest: ${{ needs.build-image.outputs.image-digest }}

      - name: Notify Slack
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "🚀 Production Deployment Successful",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "🚀 *Production Deployment Successful*\n*Image:* ${{ needs.build-image.outputs.image-tag }}\n*Deployed by:* ${{ github.actor }}\n*URL:* https://api.company.com"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_PRODUCTION }}
```

---

### 3.2 GitLab CI Pipeline

**File**: `.gitlab-ci.yml`

```yaml
# GitLab CI/CD Pipeline
# Documentation: https://docs.gitlab.com/ee/ci/

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
  KUBERNETES_VERSION: "1.28"
  HELM_VERSION: "3.13.0"

stages:
  - build
  - test
  - security
  - package
  - deploy-dev
  - deploy-staging
  - deploy-production

# =============================================================================
# BUILD STAGE
# =============================================================================

build:
  stage: build
  image: node:20-alpine
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
      - .npm/
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run lint
    - npm run build
  artifacts:
    paths:
      - dist/
      - node_modules/
    expire_in: 1 day
  only:
    - branches
    - tags

# =============================================================================
# TEST STAGE
# =============================================================================

test:unit:
  stage: test
  image: node:20-alpine
  needs: [build]
  script:
    - npm run test:unit -- --coverage
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
      junit: junit.xml
  only:
    - branches
    - merge_requests

test:integration:
  stage: test
  image: node:20-alpine
  needs: [build]
  services:
    - name: postgres:15-alpine
      alias: postgres
    - name: redis:7-alpine
      alias: redis
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test_user
    POSTGRES_PASSWORD: test_password
    DATABASE_URL: postgresql://test_user:test_password@postgres:5432/test_db
    REDIS_URL: redis://redis:6379
  script:
    - npm run test:integration
  artifacts:
    reports:
      junit: junit-integration.xml
  only:
    - branches
    - merge_requests

# =============================================================================
# SECURITY SCANNING
# =============================================================================

security:sast:
  stage: security
  image: returntocorp/semgrep:latest
  script:
    - semgrep --config=auto --sarif --output=semgrep.sarif .
  artifacts:
    reports:
      sast: semgrep.sarif
  allow_failure: false
  only:
    - branches
    - merge_requests

security:dependency-scan:
  stage: security
  image: node:20-alpine
  needs: [build]
  script:
    - npm audit --audit-level=high
    - npx snyk test --severity-threshold=high
  allow_failure: false
  only:
    - branches
    - merge_requests

security:secret-scan:
  stage: security
  image: trufflesecurity/trufflehog:latest
  script:
    - trufflehog filesystem . --json --fail
  allow_failure: false
  only:
    - branches
    - merge_requests

# =============================================================================
# PACKAGE STAGE
# =============================================================================

package:docker:
  stage: package
  image: docker:24-dind
  services:
    - docker:24-dind
  needs: [test:unit, test:integration, security:sast, security:dependency-scan]
  before_script:
    - echo $CI_REGISTRY_PASSWORD | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY
  script:
    - |
      docker build \
        --build-arg NODE_VERSION=20 \
        --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
        --build-arg VCS_REF=$CI_COMMIT_SHORT_SHA \
        --build-arg VERSION=$CI_COMMIT_TAG \
        --cache-from $CI_REGISTRY_IMAGE:latest \
        --tag $IMAGE_TAG \
        --tag $CI_REGISTRY_IMAGE:latest \
        --file Dockerfile \
        .
    - docker push $IMAGE_TAG
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - develop
    - tags

package:scan-image:
  stage: package
  image: aquasec/trivy:latest
  needs: [package:docker]
  script:
    - trivy image --severity HIGH,CRITICAL --exit-code 1 $IMAGE_TAG
  only:
    - main
    - develop

# =============================================================================
# DEPLOY TO DEVELOPMENT
# =============================================================================

deploy:dev:
  stage: deploy-dev
  image: bitnami/kubectl:$KUBERNETES_VERSION
  needs: [package:docker, package:scan-image]
  environment:
    name: development
    url: https://dev.api.company.com
    on_stop: stop:dev
  before_script:
    - kubectl config set-cluster dev-cluster --server="$KUBE_URL_DEV" --certificate-authority="$KUBE_CA_DEV"
    - kubectl config set-credentials deployer --token="$KUBE_TOKEN_DEV"
    - kubectl config set-context dev --cluster=dev-cluster --user=deployer
    - kubectl config use-context dev
  script:
    - kubectl set image deployment/api-service api=$IMAGE_TAG -n development --record
    - kubectl rollout status deployment/api-service -n development --timeout=5m
    - curl -f https://dev.api.company.com/health || exit 1
  only:
    - develop

# =============================================================================
# DEPLOY TO STAGING
# =============================================================================

deploy:staging:
  stage: deploy-staging
  image: alpine/helm:$HELM_VERSION
  needs: [package:docker, package:scan-image]
  environment:
    name: staging
    url: https://staging.api.company.com
  before_script:
    - helm repo add stable https://charts.helm.sh/stable
    - helm repo update
  script:
    - |
      helm upgrade --install api-service ./charts/api-service \
        --namespace=staging \
        --values=./charts/api-service/values-staging.yaml \
        --set image.tag=$CI_COMMIT_SHORT_SHA \
        --wait \
        --timeout=10m
  only:
    - main

# =============================================================================
# DEPLOY TO PRODUCTION (Manual Approval)
# =============================================================================

deploy:production:
  stage: deploy-production
  image: alpine/helm:$HELM_VERSION
  needs: [deploy:staging]
  environment:
    name: production
    url: https://api.company.com
  before_script:
    - helm repo add stable https://charts.helm.sh/stable
    - helm repo update
  script:
    - |
      # Blue-Green Deployment
      helm upgrade --install api-service-green ./charts/api-service \
        --namespace=production \
        --values=./charts/api-service/values-production.yaml \
        --set image.tag=$CI_COMMIT_SHORT_SHA \
        --set service.selector.version=green \
        --wait \
        --timeout=15m

    - echo "Green deployment ready. Switching traffic..."
    - sleep 60

    - |
      # Switch traffic to green
      kubectl patch service api-service \
        -n production \
        -p '{"spec":{"selector":{"version":"green"}}}'

    - echo "Traffic switched to green. Monitoring..."
    - sleep 300

    - |
      # Remove blue deployment
      helm uninstall api-service-blue -n production || true
  when: manual
  only:
    - main
    - tags
```

---

### 3.3 Jenkins Declarative Pipeline

**File**: `Jenkinsfile`

```groovy
// Jenkins Declarative Pipeline
// Requires: Docker, Kubernetes, Helm plugins

pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: node
    image: node:20-alpine
    command: ['cat']
    tty: true
  - name: docker
    image: docker:24-dind
    command: ['cat']
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  - name: helm
    image: alpine/helm:3.13.0
    command: ['cat']
    tty: true
  - name: kubectl
    image: bitnami/kubectl:1.28
    command: ['cat']
    tty: true
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
'''
        }
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '30', daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    environment {
        DOCKER_REGISTRY = 'ghcr.io'
        IMAGE_NAME = 'company/api-service'
        IMAGE_TAG = "${DOCKER_REGISTRY}/${IMAGE_NAME}:${env.GIT_COMMIT.take(7)}"
        SLACK_CHANNEL = '#deployments'
        SONAR_HOST = 'https://sonarqube.company.com'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    env.GIT_COMMIT_MSG = sh(
                        script: 'git log -1 --pretty=%B',
                        returnStdout: true
                    ).trim()
                }
            }
        }

        stage('Build') {
            steps {
                container('node') {
                    sh '''
                        npm ci --prefer-offline --no-audit
                        npm run lint
                        npm run build
                    '''
                }
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        container('node') {
                            sh 'npm run test:unit -- --coverage --ci'
                        }
                    }
                    post {
                        always {
                            junit 'junit.xml'
                            publishHTML([
                                reportDir: 'coverage',
                                reportFiles: 'index.html',
                                reportName: 'Coverage Report'
                            ])
                        }
                    }
                }

                stage('Integration Tests') {
                    steps {
                        container('node') {
                            sh 'npm run test:integration'
                        }
                    }
                }
            }
        }

        stage('Security Scan') {
            parallel {
                stage('SAST') {
                    steps {
                        container('node') {
                            sh 'npx semgrep --config=auto --sarif --output=semgrep.sarif .'
                        }
                    }
                }

                stage('Dependency Check') {
                    steps {
                        container('node') {
                            sh '''
                                npm audit --audit-level=high
                                npx snyk test --severity-threshold=high
                            '''
                        }
                    }
                }

                stage('SonarQube Analysis') {
                    steps {
                        container('node') {
                            withSonarQubeEnv('SonarQube') {
                                sh '''
                                    npm run sonar-scanner -- \
                                      -Dsonar.projectKey=api-service \
                                      -Dsonar.sources=src \
                                      -Dsonar.tests=tests \
                                      -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info
                                '''
                            }
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Docker Image') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                container('docker') {
                    sh '''
                        docker build \
                          --build-arg NODE_VERSION=20 \
                          --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
                          --build-arg VCS_REF=${GIT_COMMIT} \
                          --tag ${IMAGE_TAG} \
                          --tag ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest \
                          --file Dockerfile \
                          .
                    '''
                }
            }
        }

        stage('Scan Docker Image') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                container('docker') {
                    sh '''
                        trivy image \
                          --severity HIGH,CRITICAL \
                          --exit-code 1 \
                          ${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                container('docker') {
                    withCredentials([usernamePassword(
                        credentialsId: 'docker-registry-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )]) {
                        sh '''
                            echo ${DOCKER_PASSWORD} | docker login ${DOCKER_REGISTRY} -u ${DOCKER_USER} --password-stdin
                            docker push ${IMAGE_TAG}
                            docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Development') {
            when {
                branch 'develop'
            }
            steps {
                container('kubectl') {
                    withKubeConfig([credentialsId: 'kube-dev-credentials']) {
                        sh '''
                            kubectl set image deployment/api-service \
                              api=${IMAGE_TAG} \
                              --namespace=development \
                              --record

                            kubectl rollout status deployment/api-service \
                              --namespace=development \
                              --timeout=5m
                        '''
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                container('helm') {
                    withKubeConfig([credentialsId: 'kube-staging-credentials']) {
                        sh '''
                            helm upgrade --install api-service ./charts/api-service \
                              --namespace=staging \
                              --values=./charts/api-service/values-staging.yaml \
                              --set image.tag=${GIT_COMMIT:0:7} \
                              --wait \
                              --timeout=10m
                        '''
                    }
                }
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    input message: 'Deploy to production?', ok: 'Deploy', submitter: 'platform-team,sre-team'
                }

                container('helm') {
                    withKubeConfig([credentialsId: 'kube-prod-credentials']) {
                        sh '''
                            # Canary deployment (10%)
                            helm upgrade --install api-service-canary ./charts/api-service \
                              --namespace=production \
                              --values=./charts/api-service/values-production.yaml \
                              --set image.tag=${GIT_COMMIT:0:7} \
                              --set canary.enabled=true \
                              --set canary.weight=10 \
                              --wait \
                              --timeout=10m

                            # Monitor canary (5 minutes)
                            sleep 300

                            # Full rollout
                            helm upgrade --install api-service ./charts/api-service \
                              --namespace=production \
                              --values=./charts/api-service/values-production.yaml \
                              --set image.tag=${GIT_COMMIT:0:7} \
                              --wait \
                              --timeout=15m
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'good',
                message: """
                    ✅ *Pipeline Successful*
                    *Job:* ${env.JOB_NAME}
                    *Build:* ${env.BUILD_NUMBER}
                    *Branch:* ${env.GIT_BRANCH}
                    *Commit:* ${env.GIT_COMMIT_MSG}
                    *Author:* ${env.GIT_AUTHOR_NAME}
                """
            )
        }

        failure {
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'danger',
                message: """
                    ❌ *Pipeline Failed*
                    *Job:* ${env.JOB_NAME}
                    *Build:* ${env.BUILD_NUMBER}
                    *Branch:* ${env.GIT_BRANCH}
                    *Failure Stage:* ${env.STAGE_NAME}
                """
            )
        }

        always {
            cleanWs()
        }
    }
}
```

---

## 4. Quality Gates

### 4.1 Automated Quality Gates

| Gate | Threshold | Action on Failure |
|------|-----------|-------------------|
| Code Coverage | ≥ 80% | Block merge/deployment |
| Test Pass Rate | 100% | Block merge/deployment |
| Linting Errors | 0 errors | Block merge/deployment |
| Security Vulnerabilities (Critical/High) | 0 vulnerabilities | Block merge/deployment |
| SonarQube Quality Gate | Pass | Block merge/deployment |
| Container Scan | No HIGH/CRITICAL | Block image push |
| License Compliance | All approved | Block merge/deployment |
| Build Duration | < 20 minutes | Alert team (investigate) |

### 4.2 Manual Approval Gates

- **Staging → Production**: Requires approval from Platform Team + Security Team
- **Production Deployment Window**: Weekdays 10:00-16:00 UTC (no deployments during nights/weekends)
- **Change Advisory Board (CAB)**: Required for major releases

---

## 5. Deployment Strategies

### 5.1 Rolling Deployment (Default)

```yaml
# Kubernetes Deployment Strategy
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 0   # Zero-downtime deployment
    maxSurge: 1         # One extra pod during rollout
```

**Use Cases**:
- Development environment
- Staging environment
- Non-critical services

### 5.2 Blue-Green Deployment

```yaml
# Blue version running
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api-service
    version: blue  # Current production

---
# Deploy green version
# Switch selector to green after validation
# Remove blue deployment
```

**Use Cases**:
- Production deployments requiring instant rollback
- Database schema changes
- Major version upgrades

### 5.3 Canary Deployment

```yaml
# Canary deployment with 10% traffic
canary:
  enabled: true
  weight: 10        # 10% of traffic to canary
  metrics:
    - name: error-rate
      threshold: 1
    - name: latency-p95
      threshold: 500
```

**Use Cases**:
- High-risk production changes
- New feature rollouts
- Performance-sensitive deployments

### 5.4 Feature Flag-Based Deployment

```javascript
// Deploy code to production with feature flag disabled
if (featureFlags.isEnabled('new-payment-flow', user)) {
  return newPaymentFlow();
} else {
  return legacyPaymentFlow();
}

// Gradually increase rollout percentage
// 1% → 5% → 25% → 50% → 100%
```

**Use Cases**:
- Gradual feature rollouts
- A/B testing
- Instant rollback without redeployment

---

## 6. Secrets Management

### 6.1 GitHub Actions Secrets

```yaml
# Organization-level secrets (shared across repos)
DOCKER_REGISTRY_USERNAME
DOCKER_REGISTRY_PASSWORD
SNYK_TOKEN
SONARQUBE_TOKEN

# Repository secrets
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
KUBE_CONFIG_DEV
KUBE_CONFIG_STAGING
KUBE_CONFIG_PROD
SLACK_WEBHOOK_URL
```

### 6.2 Vault Integration

```yaml
# Retrieve secrets from Vault in pipeline
- name: Get secrets from Vault
  uses: hashicorp/vault-action@v2
  with:
    url: https://vault.company.com
    token: ${{ secrets.VAULT_TOKEN }}
    secrets: |
      secret/data/production/database DATABASE_URL ;
      secret/data/production/api API_KEY
```

### 6.3 External Secrets Operator (Kubernetes)

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: api-secrets
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: api-secrets
    creationPolicy: Owner
  data:
  - secretKey: DATABASE_URL
    remoteRef:
      key: production/api-service/database-url
```

---

## 7. Monitoring & Observability

### 7.1 Pipeline Metrics

**DORA Metrics**:
- **Deployment Frequency**: Deployments per day
- **Lead Time for Changes**: Commit to production time
- **Change Failure Rate**: % of deployments causing failure
- **Mean Time to Recovery (MTTR)**: Time to restore service

**CI/CD Metrics**:
- Build success rate
- Average build duration
- Test pass rate
- Security scan findings
- Deployment success rate

### 7.2 Pipeline Observability

```yaml
# Prometheus metrics for pipelines
- pipeline_build_duration_seconds{job="api-service", stage="build"}
- pipeline_test_pass_rate{job="api-service", type="unit"}
- pipeline_security_vulnerabilities{job="api-service", severity="high"}
- pipeline_deployment_count{job="api-service", environment="production"}
```

### 7.3 Alerting

```yaml
# Alert on failed production deployments
- alert: ProductionDeploymentFailed
  expr: pipeline_deployment_status{environment="production", status="failed"} > 0
  for: 1m
  annotations:
    summary: "Production deployment failed for {{ $labels.job }}"
  labels:
    severity: critical
    channel: pagerduty
```

---

## 8. Rollback Procedures

### 8.1 Automated Rollback

```yaml
# GitHub Actions rollback
- name: Rollback on failure
  if: failure()
  run: |
    kubectl rollout undo deployment/api-service \
      --namespace=production

    # Notify team
    echo "Deployment failed. Rolling back to previous version."
```

### 8.2 Manual Rollback

```bash
# Kubernetes rollback to previous revision
kubectl rollout undo deployment/api-service -n production

# Rollback to specific revision
kubectl rollout undo deployment/api-service -n production --to-revision=5

# Helm rollback
helm rollback api-service -n production

# Helm rollback to specific revision
helm rollback api-service 3 -n production
```

### 8.3 Database Migration Rollback

```bash
# Run database migration rollback
npm run migrate:down

# Restore from backup (if needed)
./scripts/restore-database.sh --backup-id=<backup-id>
```

---

## 9. Compliance & Audit

### 9.1 Audit Trail

All pipeline executions maintain:
- Commit SHA and author
- Build timestamp and duration
- Test results and coverage
- Security scan results
- Deployment approvals and approvers
- Deployment timestamp and environment

### 9.2 Compliance Controls

**SOC 2 Controls**:
- CC6.6: Logical access controls (approval gates)
- CC7.2: System monitoring (pipeline observability)
- CC8.1: Change management (deployment approvals)

**Audit Reports**:
```bash
# Generate deployment audit report
./scripts/generate-audit-report.sh \
  --start-date=2024-01-01 \
  --end-date=2024-01-31 \
  --environment=production
```

---

## 10. Troubleshooting

### 10.1 Common Issues

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| Build timeout | Check build logs for hanging processes | Increase timeout, optimize build |
| Test failures | Review test logs | Fix failing tests, update test data |
| Docker build fails | Check Dockerfile syntax | Fix Dockerfile, check base images |
| Deployment timeout | Check pod events | Increase timeout, fix resource limits |
| Rollback fails | Check revision history | Manual intervention required |

### 10.2 Debug Commands

```bash
# Check pipeline logs
kubectl logs -n jenkins pod/jenkins-agent-xyz

# Check deployment status
kubectl describe deployment api-service -n production

# Check pod events
kubectl get events -n production --sort-by='.lastTimestamp'

# Check rollout history
kubectl rollout history deployment/api-service -n production

# Debug pod
kubectl debug -it pod/api-service-xyz -n production --image=busybox
```

---

## 11. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.1.0 | 2024-01-22 | Alex Rodriguez | Added canary deployment strategy, improved security scanning |
| 2.0.0 | 2024-01-01 | Sarah Kim | Migrated from Jenkins to GitHub Actions primary platform |
| 1.5.0 | 2023-11-15 | DevOps Team | Added Trivy container scanning, SBOM generation |
| 1.0.0 | 2023-09-01 | Platform Team | Initial CI/CD pipeline documentation |

---

## 12. Related Documentation

- [Deployment Plan](./deployment-plan.md)
- [Release Risk Assessment](./release-risk-assessment.md)
- [Environment Matrix](./environment-matrix.yaml)
- [Kubernetes Deployment Manifests](../k8s/)
- [Helm Charts](../charts/)
- [Rollback Runbook](../operations/runbooks/rollback-procedure.md)
