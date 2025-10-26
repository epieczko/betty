# Dockerfiles - Production-Ready Multi-Stage Build Templates

This document provides production-ready Dockerfile templates with security hardening, multi-stage builds, and optimization patterns for various programming languages and frameworks.

---

## Table of Contents
1. [Node.js/TypeScript Dockerfile](#nodejs-typescript)
2. [Python FastAPI/Django Dockerfile](#python)
3. [Go Dockerfile](#go)
4. [Java Spring Boot Dockerfile](#java)
5. [.NET Core Dockerfile](#dotnet)
6. [Ruby on Rails Dockerfile](#ruby)
7. [Dockerfile Best Practices](#best-practices)
8. [Security Scanning](#security)

---

## <a name="nodejs-typescript"></a>Node.js / TypeScript - Production Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM node:20.11-alpine AS builder

# Install build dependencies
RUN apk add --no-cache \
    python3 \
    make \
    g++ \
    git

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY yarn.lock* ./

# Install dependencies with caching
# Mount npm cache for faster builds
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production && \
    npm cache clean --force

# Copy application source
COPY . .

# Build TypeScript application
RUN npm run build

####################
# Production Stage
####################
FROM node:20.11-alpine AS production

# Install dumb-init for proper signal handling
RUN apk add --no-cache dumb-init

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy production dependencies from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules

# Copy built application
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/package*.json ./

# Use non-root user
USER nodejs

# Set environment variables
ENV NODE_ENV=production \
    PORT=8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD node -e "require('http').get('http://localhost:8080/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

EXPOSE 8080

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Start application
CMD ["node", "dist/main.js"]
```

### Node.js with BuildKit Optimizations

```dockerfile
# syntax=docker/dockerfile:1

FROM node:20.11-alpine AS base
RUN apk add --no-cache dumb-init
WORKDIR /app
RUN addgroup -g 1001 nodejs && adduser -S nodejs -u 1001

FROM base AS dependencies
# Mount cache for faster dependency installation
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

FROM base AS build
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci
COPY . .
RUN npm run build

FROM base AS production
ENV NODE_ENV=production PORT=8080
COPY --from=dependencies --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=build --chown=nodejs:nodejs /app/dist ./dist
COPY --from=build --chown=nodejs:nodejs /app/package*.json ./
USER nodejs
EXPOSE 8080
HEALTHCHECK CMD node -e "require('http').get('http://localhost:8080/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/main.js"]
```

---

## <a name="python"></a>Python - FastAPI/Django Production Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM python:3.12-slim AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies with caching
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --user --no-cache-dir -r requirements.txt

####################
# Production Stage
####################
FROM python:3.12-slim AS production

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --shell /bin/bash --uid 1000 appuser

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser . .

# Update PATH
ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

# Run application with uvicorn (FastAPI) or gunicorn (Django)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# For Django: CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
```

### Python with Poetry

```dockerfile
FROM python:3.12-slim AS builder

# Install Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1
RUN pip install --no-cache-dir poetry==1.7.1

WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pypoetry \
    poetry install --only=main --no-root --no-directory

# Copy application
COPY . .
RUN poetry install --only=main

FROM python:3.12-slim AS production

RUN useradd --create-home --uid 1000 appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder --chown=appuser:appuser /app/.venv ./.venv
COPY --from=builder --chown=appuser:appuser /app .

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## <a name="go"></a>Go - Production Dockerfile with Static Binaries

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM golang:1.22-alpine AS builder

# Install build dependencies
RUN apk add --no-cache git make ca-certificates tzdata

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./

# Download dependencies with caching
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download && go mod verify

# Copy source code
COPY . .

# Build static binary
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags='-w -s -extldflags "-static"' \
    -a -installsuffix cgo \
    -o /app/main .

####################
# Production Stage (Scratch - Minimal)
####################
FROM scratch AS production

# Copy CA certificates for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Copy timezone data
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

# Copy /etc/passwd for non-root user
COPY --from=builder /etc/passwd /etc/passwd

# Copy binary
COPY --from=builder /app/main /main

# Use non-root user (create in builder if needed)
USER 1001

EXPOSE 8080

# Health check (requires compiled health check binary)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["/main", "healthcheck"]

ENTRYPOINT ["/main"]
```

### Go with Distroless

```dockerfile
FROM golang:1.22-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod go mod download
COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 go build -ldflags='-w -s' -o /app/main .

FROM gcr.io/distroless/static-debian12:nonroot AS production

COPY --from=builder /app/main /main

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/main"]
```

---

## <a name="java"></a>Java - Spring Boot Production Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM maven:3.9-eclipse-temurin-21-alpine AS builder

WORKDIR /app

# Copy pom.xml first for dependency caching
COPY pom.xml .
RUN --mount=type=cache,target=/root/.m2 \
    mvn dependency:go-offline -B

# Copy source and build
COPY src ./src
RUN --mount=type=cache,target=/root/.m2 \
    mvn clean package -DskipTests -B

####################
# Production Stage
####################
FROM eclipse-temurin:21-jre-alpine AS production

# Create non-root user
RUN addgroup -g 1001 -S spring && \
    adduser -S spring -u 1001 -G spring

WORKDIR /app

# Copy JAR from builder
COPY --from=builder --chown=spring:spring /app/target/*.jar app.jar

# Switch to non-root user
USER spring:spring

ENV JAVA_OPTS="-XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0 -Djava.security.egd=file:/dev/./urandom" \
    SPRING_PROFILES_ACTIVE=production

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=60s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

### Java with Jib (No Dockerfile needed)

```xml
<!-- In pom.xml -->
<plugin>
    <groupId>com.google.cloud.tools</groupId>
    <artifactId>jib-maven-plugin</artifactId>
    <version>3.4.0</version>
    <configuration>
        <from>
            <image>eclipse-temurin:21-jre-alpine</image>
        </from>
        <to>
            <image>myregistry/myapp</image>
            <tags>
                <tag>latest</tag>
                <tag>${project.version}</tag>
            </tags>
        </to>
        <container>
            <jvmFlags>
                <jvmFlag>-XX:+UseContainerSupport</jvmFlag>
                <jvmFlag>-XX:MaxRAMPercentage=75.0</jvmFlag>
            </jvmFlags>
            <user>1001</user>
            <ports>
                <port>8080</port>
            </ports>
        </container>
    </configuration>
</plugin>
```

---

## <a name="dotnet"></a>.NET Core - Production Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS builder

WORKDIR /app

# Copy csproj and restore dependencies
COPY *.csproj ./
RUN --mount=type=cache,target=/root/.nuget/packages \
    dotnet restore

# Copy source and build
COPY . ./
RUN --mount=type=cache,target=/root/.nuget/packages \
    dotnet publish -c Release -o out --no-restore

####################
# Production Stage
####################
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS production

# Create non-root user
RUN addgroup -g 1001 -S dotnet && \
    adduser -S dotnet -u 1001 -G dotnet

WORKDIR /app

# Copy published application
COPY --from=builder --chown=dotnet:dotnet /app/out .

USER dotnet

ENV ASPNETCORE_URLS=http://+:8080 \
    DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false \
    ASPNETCORE_ENVIRONMENT=Production

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

ENTRYPOINT ["dotnet", "MyApp.dll"]
```

---

## <a name="ruby"></a>Ruby on Rails - Production Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

####################
# Build Stage
####################
FROM ruby:3.3-alpine AS builder

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    nodejs \
    yarn \
    git

WORKDIR /app

# Install Ruby gems
COPY Gemfile Gemfile.lock ./
RUN --mount=type=cache,target=/usr/local/bundle \
    bundle config set --local deployment 'true' && \
    bundle config set --local without 'development test' && \
    bundle install

# Install Node dependencies
COPY package.json yarn.lock ./
RUN --mount=type=cache,target=/root/.yarn \
    yarn install --frozen-lockfile --production

# Copy application
COPY . .

# Precompile assets
RUN bundle exec rails assets:precompile

####################
# Production Stage
####################
FROM ruby:3.3-alpine AS production

# Install runtime dependencies
RUN apk add --no-cache \
    postgresql-client \
    nodejs \
    tzdata

# Create non-root user
RUN addgroup -g 1001 -S rails && \
    adduser -S rails -u 1001 -G rails

WORKDIR /app

# Copy gems from builder
COPY --from=builder --chown=rails:rails /usr/local/bundle /usr/local/bundle

# Copy application
COPY --from=builder --chown=rails:rails /app .

USER rails

ENV RAILS_ENV=production \
    RAILS_SERVE_STATIC_FILES=true \
    RAILS_LOG_TO_STDOUT=true

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
```

---

## <a name="best-practices"></a>Dockerfile Best Practices

### .dockerignore File

```bash
# Git
.git
.gitignore
.gitattributes

# CI/CD
.github
.gitlab-ci.yml
Jenkinsfile

# Docker
Dockerfile*
docker-compose*
.dockerignore

# Documentation
README.md
docs/
*.md

# Tests
__tests__
*.test.js
*.spec.ts
test/
tests/
coverage/

# Development
.env
.env.local
.env.development
*.log
npm-debug.log*
.DS_Store
.vscode/
.idea/

# Dependencies (will be installed in image)
node_modules/
vendor/
__pycache__/
*.pyc
.pytest_cache/

# Build artifacts
dist/
build/
target/
out/
*.class
```

### Security Best Practices Checklist

- [ ] Use official base images from trusted sources
- [ ] Pin specific image versions/digests, avoid `latest` tag
- [ ] Use minimal base images (Alpine, Distroless, Scratch)
- [ ] Run containers as non-root user (USER directive)
- [ ] Use multi-stage builds to minimize final image size
- [ ] Set read-only root filesystem when possible
- [ ] Drop all capabilities and add only required ones
- [ ] Scan images for vulnerabilities (Trivy, Grype, Snyk)
- [ ] Don't include secrets in images (use secrets management)
- [ ] Use .dockerignore to exclude unnecessary files
- [ ] Minimize layers by combining RUN commands
- [ ] Order instructions from least to most frequently changing
- [ ] Use BuildKit cache mounts for dependencies
- [ ] Add HEALTHCHECK for container health monitoring
- [ ] Use COPY instead of ADD (except for tar extraction)
- [ ] Set appropriate WORKDIR, avoid WORKDIR /
- [ ] Use exec form for ENTRYPOINT and CMD
- [ ] Add metadata labels (version, git sha, build date)
- [ ] Verify checksums of downloaded files
- [ ] Clean up package manager caches in same RUN layer

### Image Size Optimization

```dockerfile
# ❌ Bad - Large image with unnecessary layers
FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install flask
COPY app.py .
CMD ["python3", "app.py"]

# ✅ Good - Optimized with Alpine and combined layers
FROM python:3.12-alpine
RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --no-cache-dir flask && \
    apk del .build-deps
COPY app.py .
USER 1000
CMD ["python3", "app.py"]
```

---

## <a name="security"></a>Security Scanning Integration

### Trivy Scanning

```bash
# Scan Dockerfile
trivy config Dockerfile

# Scan built image
trivy image myapp:latest

# Fail on HIGH and CRITICAL vulnerabilities
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest

# Generate SBOM
trivy image --format cyclonedx --output sbom.json myapp:latest
```

### Grype Scanning

```bash
# Scan image
grype myapp:latest

# Output formats
grype myapp:latest -o json
grype myapp:latest -o cyclonedx

# Fail on CRITICAL
grype myapp:latest --fail-on critical
```

### Docker Scout (Docker Hub)

```bash
# Analyze image
docker scout cves myapp:latest

# Compare with base image
docker scout compare --to myapp:previous myapp:latest

# Get recommendations
docker scout recommendations myapp:latest
```

### Snyk Container Scanning

```bash
# Test image
snyk container test myapp:latest

# Monitor image
snyk container monitor myapp:latest

# Test Dockerfile
snyk container test myapp:latest --file=Dockerfile
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Build and Scan Docker Image

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          load: true
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Run Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
```

---

## Build Commands

```bash
# Build with BuildKit
DOCKER_BUILDKIT=1 docker build -t myapp:latest .

# Build with build arguments
docker build --build-arg VERSION=1.0.0 -t myapp:1.0.0 .

# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# Build with cache from registry
docker buildx build \
  --cache-from type=registry,ref=myregistry/myapp:cache \
  --cache-to type=registry,ref=myregistry/myapp:cache,mode=max \
  -t myapp:latest .

# Build and push
docker buildx build --push -t myregistry/myapp:latest .

# Build with secrets (never in image layers)
docker buildx build --secret id=npmrc,src=$HOME/.npmrc -t myapp:latest .
```

---

**Template Version:** 1.0.0
**Last Updated:** 2025-10-26
**Best Practices:** CIS Docker Benchmark v1.6.0, NIST SP 800-190
