# [Product Name] Installation Guide

> **Version**: 2.1.0 | **Last Updated**: 2025-01-15 | **Estimated Time**: 20-45 minutes

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Pre-Installation Checklist](#pre-installation-checklist)
- [Installation Methods](#installation-methods)
  - [Docker (Recommended)](#docker-recommended)
  - [Kubernetes with Helm](#kubernetes-with-helm)
  - [Package Manager Installation](#package-manager-installation)
  - [Binary Installation](#binary-installation)
  - [Build from Source](#build-from-source)
  - [Air-Gapped/Offline Installation](#air-gappedoffline-installation)
- [Post-Installation Configuration](#post-installation-configuration)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)
- [Next Steps](#next-steps)

## Overview

This guide provides comprehensive installation instructions for [Product Name] across multiple platforms and deployment methods. Choose the installation method that best matches your infrastructure and use case.

**Supported Platforms:**
- Linux: Ubuntu 20.04+, RHEL/CentOS 8+, Debian 11+
- macOS: 12+ (Monterey) on Intel and Apple Silicon
- Windows: 10/11, Server 2019/2022
- Container: Docker 20.10+, Kubernetes 1.24+

**Installation Time Estimates:**
- Docker: 5-10 minutes
- Kubernetes: 15-20 minutes
- Package Manager: 10-15 minutes
- Source Build: 30-45 minutes

## Prerequisites

### System Requirements

**Minimum Requirements:**

| Component | Requirement |
|-----------|-------------|
| CPU | 2 cores (x86_64 or ARM64) |
| RAM | 4GB |
| Disk Space | 10GB available |
| Network | Internet connectivity for installation |
| OS | Linux kernel 4.4+, macOS 12+, Windows 10+ |

**Recommended for Production:**

| Component | Requirement |
|-----------|-------------|
| CPU | 8+ cores |
| RAM | 16GB+ |
| Disk Space | 50GB SSD |
| Network | 100Mbps+ bandwidth |

### Software Dependencies

Required for all installations:

1. **Database**: PostgreSQL 13+ or 14+ (recommended)
   ```bash
   # Verify PostgreSQL version
   psql --version
   # Expected: psql (PostgreSQL) 14.x
   ```

2. **Cache (Optional but Recommended)**: Redis 6.2+ or 7.x
   ```bash
   # Verify Redis version
   redis-cli --version
   # Expected: redis-cli 7.x.x
   ```

3. **Runtime Environment** (method-specific):
   - Docker: Docker 20.10+ and Docker Compose 2.0+
   - Kubernetes: kubectl 1.24+, Helm 3.10+
   - Python: Python 3.10+ (for source installation)

### Network Requirements

**Required Ports:**

| Port | Protocol | Purpose | Access |
|------|----------|---------|--------|
| 8080 | TCP | HTTP API | External |
| 8443 | TCP | HTTPS API | External |
| 9090 | TCP | Metrics (Prometheus) | Internal |
| 5432 | TCP | PostgreSQL | Internal |
| 6379 | TCP | Redis | Internal |

**Firewall Configuration:**
```bash
# Example: Allow required ports (Ubuntu/Debian with ufw)
sudo ufw allow 8080/tcp
sudo ufw allow 8443/tcp
sudo ufw allow 9090/tcp
```

**Outbound Connectivity Required For:**
- Package repository access
- Docker Hub / container registries
- License validation server (license.example.com)
- Update check service (updates.example.com)

### Permissions Required

**Linux/macOS:**
- `sudo` access for system-wide installation
- User account with Docker group membership (for Docker method)
- Read/write access to `/opt/product-name` or chosen installation directory

**Windows:**
- Administrator privileges for service installation
- PowerShell execution policy: RemoteSigned or Bypass

## Pre-Installation Checklist

Run this validation script to verify your system meets all requirements:

```bash
#!/bin/bash
# pre-install-check.sh - System readiness validation

echo "=== Product Name Pre-Installation Check ==="

# Check CPU cores
CORES=$(nproc 2>/dev/null || sysctl -n hw.ncpu)
echo "CPU Cores: $CORES $([ $CORES -ge 2 ] && echo '✓' || echo '✗ Need 2+')"

# Check RAM
RAM_GB=$(free -g 2>/dev/null | awk '/Mem:/ {print $2}' || sysctl -n hw.memsize | awk '{print int($1/1024/1024/1024)}')
echo "RAM: ${RAM_GB}GB $([ $RAM_GB -ge 4 ] && echo '✓' || echo '✗ Need 4GB+')"

# Check disk space
DISK_GB=$(df -BG . | awk 'NR==2 {print int($4)}')
echo "Disk Space: ${DISK_GB}GB $([ $DISK_GB -ge 10 ] && echo '✓' || echo '✗ Need 10GB+')"

# Check PostgreSQL
psql --version >/dev/null 2>&1 && echo "PostgreSQL: ✓" || echo "PostgreSQL: ✗ Not found"

# Check Redis (optional)
redis-cli --version >/dev/null 2>&1 && echo "Redis: ✓" || echo "Redis: ⚠ Optional but recommended"

# Check network connectivity
curl -sI https://pkg.product.com >/dev/null 2>&1 && echo "Network: ✓" || echo "Network: ✗ Cannot reach package server"

echo "=== Check Complete ==="
```

Run the script:
```bash
bash pre-install-check.sh
```

## Installation Methods

### Docker (Recommended)

Docker provides the fastest and most consistent installation experience.

#### Step 1: Install Docker

<details>
<summary><b>Ubuntu/Debian</b></summary>

```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
sudo docker run hello-world
# Expected: "Hello from Docker!" message

# Add your user to docker group (optional, avoids sudo)
sudo usermod -aG docker $USER
newgrp docker  # Activate group membership
```
</details>

<details>
<summary><b>RHEL/CentOS/Fedora</b></summary>

```bash
# Remove old versions
sudo yum remove docker docker-client docker-client-latest docker-common \
  docker-latest docker-latest-logrotate docker-logrotate docker-engine

# Install yum-utils
sudo yum install -y yum-utils

# Add Docker repository
sudo yum-config-manager --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine
sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
sudo docker run hello-world
```
</details>

<details>
<summary><b>macOS</b></summary>

```bash
# Install via Homebrew (recommended)
brew install --cask docker

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Start Docker Desktop from Applications
# Verify installation
docker --version
docker-compose --version
```
</details>

<details>
<summary><b>Windows</b></summary>

```powershell
# Option 1: Install Docker Desktop
# Download from: https://www.docker.com/products/docker-desktop

# Option 2: Install via Chocolatey
choco install docker-desktop

# Verify installation (PowerShell)
docker --version
docker-compose --version
```
</details>

#### Step 2: Pull and Run Product Image

```bash
# Pull the latest stable image
docker pull product-org/product-name:2.1.0

# Create directories for persistent data
mkdir -p ~/product-data/postgres ~/product-data/redis ~/product-data/logs

# Run with Docker Compose (recommended)
cat > docker-compose.yml <<EOF
version: '3.8'

services:
  app:
    image: product-org/product-name:2.1.0
    container_name: product-app
    ports:
      - "8080:8080"
      - "9090:9090"
    environment:
      - DATABASE_URL=postgresql://product:changeme@postgres:5432/product_db
      - REDIS_URL=redis://redis:6379/0
      - LOG_LEVEL=INFO
      - API_KEY=\${API_KEY:-your_api_key_here}
    volumes:
      - ./config.yml:/app/config.yml:ro
      - ./logs:/app/logs
    depends_on:
      - postgres
      - redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  postgres:
    image: postgres:14-alpine
    container_name: product-postgres
    environment:
      - POSTGRES_DB=product_db
      - POSTGRES_USER=product
      - POSTGRES_PASSWORD=changeme  # Change in production!
    volumes:
      - ~/product-data/postgres:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U product"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: product-redis
    command: redis-server --appendonly yes
    volumes:
      - ~/product-data/redis:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

networks:
  default:
    name: product-network
EOF

# Create minimal configuration file
cat > config.yml <<EOF
server:
  host: 0.0.0.0
  port: 8080
  workers: 4

logging:
  level: INFO
  format: json
EOF

# Start all services
docker-compose up -d

# Check service status
docker-compose ps
# Expected: All services "healthy"

# View logs
docker-compose logs -f app
```

**Verification:**
```bash
# Check health endpoint
curl http://localhost:8080/health
# Expected: {"status": "healthy", "version": "2.1.0"}

# Check metrics endpoint
curl http://localhost:9090/metrics | head -20
```

### Kubernetes with Helm

Production-grade deployment on Kubernetes clusters.

#### Prerequisites

```bash
# Verify kubectl is configured
kubectl version --client
kubectl cluster-info

# Install Helm 3 if not present
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

#### Step 1: Add Helm Repository

```bash
# Add Product Helm repository
helm repo add product https://charts.product.com
helm repo update

# Search for available charts
helm search repo product/product-name
```

#### Step 2: Create Namespace

```bash
# Create dedicated namespace
kubectl create namespace production

# Set as default namespace (optional)
kubectl config set-context --current --namespace=production
```

#### Step 3: Configure Values

Create `values-production.yml`:

```yaml
# values-production.yml - Production configuration

replicaCount: 3

image:
  repository: product-org/product-name
  tag: "2.1.0"
  pullPolicy: IfNotPresent

service:
  type: LoadBalancer
  port: 8080
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"

ingress:
  enabled: true
  className: nginx
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
  hosts:
    - host: product.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: product-tls
      hosts:
        - product.example.com

resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "4Gi"
    cpu: "2000m"

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

postgresql:
  enabled: true
  auth:
    username: product
    password: "changeme"  # Use secret in production
    database: product_db
  primary:
    persistence:
      enabled: true
      size: 50Gi
      storageClass: "gp3"

redis:
  enabled: true
  architecture: standalone
  auth:
    enabled: true
    password: "changeme"  # Use secret in production
  master:
    persistence:
      enabled: true
      size: 10Gi

env:
  - name: LOG_LEVEL
    value: "INFO"
  - name: API_KEY
    valueFrom:
      secretKeyRef:
        name: product-secrets
        key: api-key

monitoring:
  serviceMonitor:
    enabled: true
    interval: 30s
```

#### Step 4: Install with Helm

```bash
# Create secrets (before helm install)
kubectl create secret generic product-secrets \
  --from-literal=api-key='your_production_api_key_here' \
  --namespace=production

# Dry run to validate configuration
helm install product-release product/product-name \
  --namespace production \
  --values values-production.yml \
  --dry-run --debug

# Install for real
helm install product-release product/product-name \
  --namespace production \
  --values values-production.yml \
  --wait --timeout 10m

# Check deployment status
helm status product-release -n production
kubectl get pods -n production -w
```

**Verification:**
```bash
# Check all pods are running
kubectl get pods -n production
# Expected: All pods STATUS="Running", READY="1/1"

# Check services
kubectl get svc -n production

# Test health endpoint
kubectl port-forward svc/product-release 8080:8080 -n production &
curl http://localhost:8080/health

# View logs
kubectl logs -f deployment/product-release -n production

# Check resource usage
kubectl top pods -n production
```

### Package Manager Installation

Native package installation for Linux and macOS.

#### Ubuntu/Debian (APT)

```bash
# Add Product package repository
curl -fsSL https://pkg.product.com/gpg | \
  sudo gpg --dearmor -o /usr/share/keyrings/product.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/product.gpg] \
  https://pkg.product.com/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/product.list

# Update package index
sudo apt-get update

# Install Product
sudo apt-get install -y product-name

# Verify installation
product-name --version
# Expected: product-name version 2.1.0

# Enable and start service
sudo systemctl enable product-name
sudo systemctl start product-name

# Check service status
sudo systemctl status product-name
# Expected: "active (running)"
```

#### RHEL/CentOS/Fedora (YUM/DNF)

```bash
# Add Product repository
sudo tee /etc/yum.repos.d/product.repo <<EOF
[product]
name=Product Repository
baseurl=https://pkg.product.com/yum/\$basearch
enabled=1
gpgcheck=1
gpgkey=https://pkg.product.com/gpg
EOF

# Install Product
sudo yum install -y product-name
# Or on Fedora/newer RHEL: sudo dnf install -y product-name

# Verify installation
product-name --version

# Enable and start service
sudo systemctl enable product-name
sudo systemctl start product-name
sudo systemctl status product-name
```

#### macOS (Homebrew)

```bash
# Add Product tap
brew tap product-org/tap

# Install Product
brew install product-name

# Verify installation
product-name --version

# Start service (as background service)
brew services start product-name

# Check service status
brew services list | grep product-name
# Expected: "started"
```

#### Windows (Chocolatey)

```powershell
# Install Chocolatey if not already installed
# See: https://chocolatey.org/install

# Install Product
choco install product-name -y

# Verify installation
product-name --version

# Start service
Start-Service product-name

# Check service status
Get-Service product-name
# Expected: Status "Running"
```

### Binary Installation

Manual installation from pre-built binaries.

#### Step 1: Download Binary

```bash
# Set version and platform
VERSION="2.1.0"
PLATFORM="linux-amd64"  # Options: linux-amd64, linux-arm64, darwin-amd64, darwin-arm64, windows-amd64

# Download binary
curl -LO https://releases.product.com/v${VERSION}/product-name-${VERSION}-${PLATFORM}.tar.gz

# Download checksums
curl -LO https://releases.product.com/v${VERSION}/checksums.txt

# Verify checksum
sha256sum -c checksums.txt 2>&1 | grep OK
# Expected: "product-name-2.1.0-linux-amd64.tar.gz: OK"
```

#### Step 2: Install Binary

```bash
# Extract archive
tar -xzf product-name-${VERSION}-${PLATFORM}.tar.gz

# Move binary to system path
sudo mv product-name-${VERSION}-${PLATFORM}/product-name /usr/local/bin/

# Set permissions
sudo chmod +x /usr/local/bin/product-name

# Verify installation
product-name --version
# Expected: product-name version 2.1.0

# Create configuration directory
sudo mkdir -p /etc/product-name
sudo mkdir -p /var/lib/product-name
sudo mkdir -p /var/log/product-name
```

#### Step 3: Create Systemd Service (Linux)

```bash
# Create service file
sudo tee /etc/systemd/system/product-name.service <<EOF
[Unit]
Description=Product Name Service
After=network.target postgresql.service

[Service]
Type=simple
User=product
Group=product
WorkingDirectory=/var/lib/product-name
ExecStart=/usr/local/bin/product-name start --config /etc/product-name/config.yml
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=product-name

# Security hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/lib/product-name /var/log/product-name

[Install]
WantedBy=multi-user.target
EOF

# Create service user
sudo useradd --system --shell /usr/sbin/nologin --home-dir /var/lib/product-name product

# Set ownership
sudo chown -R product:product /var/lib/product-name /var/log/product-name /etc/product-name

# Reload systemd
sudo systemctl daemon-reload

# Enable and start service
sudo systemctl enable product-name
sudo systemctl start product-name

# Check status
sudo systemctl status product-name
```

### Build from Source

For custom builds and development.

#### Step 1: Install Build Dependencies

```bash
# Install Go 1.21+ or Python 3.11+ (depending on project)
# Python example:
sudo apt-get install -y python3.11 python3.11-dev python3.11-venv build-essential

# Or for Go:
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

#### Step 2: Clone and Build

```bash
# Clone repository
git clone https://github.com/product-org/product-name.git
cd product-name
git checkout v2.1.0  # Specific version

# Python build example:
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -e ".[all]"

# Or Go build example:
go mod download
go build -o product-name ./cmd/product-name
go test ./...

# Verify build
./product-name --version
```

#### Step 3: Install Built Binary

```bash
# Install to system
sudo cp product-name /usr/local/bin/
sudo chmod +x /usr/local/bin/product-name

# Create configuration
sudo mkdir -p /etc/product-name
sudo cp config.example.yml /etc/product-name/config.yml
```

### Air-Gapped/Offline Installation

For environments without internet access.

#### Step 1: Prepare Installation Bundle (On Connected System)

```bash
# Download all required packages
mkdir product-offline-bundle
cd product-offline-bundle

# Download binary
curl -LO https://releases.product.com/v2.1.0/product-name-2.1.0-linux-amd64.tar.gz

# Download dependency packages (example for Python)
pip download -d ./packages product-name==2.1.0

# Download Docker images
docker pull product-org/product-name:2.1.0
docker save product-org/product-name:2.1.0 -o product-name-2.1.0-docker.tar

# Create bundle archive
cd ..
tar -czf product-offline-bundle.tar.gz product-offline-bundle/

# Transfer to air-gapped environment via USB/secure file transfer
```

#### Step 2: Install on Air-Gapped System

```bash
# Extract bundle
tar -xzf product-offline-bundle.tar.gz
cd product-offline-bundle

# Load Docker image (if using Docker)
docker load -i product-name-2.1.0-docker.tar

# Or install binary
tar -xzf product-name-2.1.0-linux-amd64.tar.gz
sudo mv product-name /usr/local/bin/
sudo chmod +x /usr/local/bin/product-name

# Install Python dependencies (if applicable)
pip install --no-index --find-links ./packages product-name

# Proceed with configuration as per standard installation
```

## Post-Installation Configuration

### Step 1: Generate Configuration File

```bash
# Generate default configuration
product-name config init > /etc/product-name/config.yml

# Or create manually
cat > /etc/product-name/config.yml <<EOF
server:
  host: 0.0.0.0
  port: 8080
  workers: 4
  timeout: 30

database:
  url: postgresql://product:changeme@localhost:5432/product_db
  pool_size: 20
  pool_timeout: 30
  ssl_mode: prefer

redis:
  host: localhost
  port: 6379
  db: 0
  password: ""  # Set if Redis auth enabled

logging:
  level: INFO
  format: json
  output: /var/log/product-name/app.log

security:
  api_key: "REPLACE_WITH_SECURE_KEY"
  tls:
    enabled: true
    cert_file: /etc/product-name/tls/cert.pem
    key_file: /etc/product-name/tls/key.pem

monitoring:
  enabled: true
  metrics_port: 9090
EOF
```

### Step 2: Initialize Database

```bash
# Run database migrations
product-name migrate upgrade head

# Verify migrations
product-name migrate current
# Expected: Current revision: abc123...

# Create initial admin user (if applicable)
product-name user create --admin \
  --username admin \
  --email admin@example.com \
  --password "SECURE_PASSWORD"
```

### Step 3: Configure TLS/SSL (Production)

```bash
# Generate self-signed certificate (development only)
openssl req -x509 -newkey rsa:4096 \
  -keyout /etc/product-name/tls/key.pem \
  -out /etc/product-name/tls/cert.pem \
  -days 365 -nodes \
  -subj "/CN=product.example.com"

# For production, use Let's Encrypt or your CA-signed certificate
# Copy your certificates to:
# /etc/product-name/tls/cert.pem (certificate)
# /etc/product-name/tls/key.pem (private key)

# Set secure permissions
chmod 600 /etc/product-name/tls/key.pem
chmod 644 /etc/product-name/tls/cert.pem
```

### Step 4: Configure Firewall

```bash
# Ubuntu/Debian (ufw)
sudo ufw allow 8080/tcp
sudo ufw allow 8443/tcp
sudo ufw reload

# RHEL/CentOS (firewalld)
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --permanent --add-port=8443/tcp
sudo firewall-cmd --reload
```

## Verification

### Health Checks

```bash
# 1. Service status
systemctl status product-name
# Expected: "active (running)"

# 2. Health endpoint
curl http://localhost:8080/health
# Expected: {"status": "healthy", "version": "2.1.0", "database": "connected", "redis": "connected"}

# 3. Readiness check
curl http://localhost:8080/health/ready
# Expected: HTTP 200 OK

# 4. Liveness check
curl http://localhost:8080/health/live
# Expected: HTTP 200 OK

# 5. Metrics endpoint
curl http://localhost:9090/metrics | grep ^product_
# Expected: Prometheus metrics output
```

### Smoke Tests

```bash
# Run built-in smoke tests
product-name test smoke

# Or manual API test
curl -X POST http://localhost:8080/api/v1/test \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
# Expected: HTTP 200 with response data

# Test database connectivity
product-name db ping
# Expected: "Database connection successful"

# Test Redis connectivity
product-name cache ping
# Expected: "Cache connection successful"
```

### Log Verification

```bash
# Check application logs
sudo journalctl -u product-name -f

# Or for file-based logs
tail -f /var/log/product-name/app.log

# Look for successful startup messages:
# - "Server started on port 8080"
# - "Database connection established"
# - "All systems operational"
```

## Troubleshooting

### Common Issues

#### Issue: Database Connection Refused

**Symptom:**
```
FATAL: connection refused at localhost:5432
```

**Solution:**
```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql
# If not running:
sudo systemctl start postgresql

# Verify PostgreSQL is listening
sudo netstat -an | grep 5432
# Or:
sudo ss -tlnp | grep 5432

# Test connection manually
psql -h localhost -U product -d product_db
# If authentication fails, check pg_hba.conf

# Fix PostgreSQL authentication
sudo nano /etc/postgresql/14/main/pg_hba.conf
# Add line: host product_db product 127.0.0.1/32 md5
sudo systemctl restart postgresql
```

#### Issue: Port Already in Use

**Symptom:**
```
Error: bind: address already in use (port 8080)
```

**Solution:**
```bash
# Find process using port 8080
sudo lsof -i :8080
# Or:
sudo netstat -tlnp | grep :8080

# Kill the conflicting process
sudo kill <PID>

# Or change Product port in config.yml
nano /etc/product-name/config.yml
# Change: server.port: 8081

# Restart service
sudo systemctl restart product-name
```

#### Issue: Permission Denied Errors

**Symptom:**
```
PermissionError: [Errno 13] Permission denied: '/var/log/product-name/app.log'
```

**Solution:**
```bash
# Fix directory ownership
sudo chown -R product:product /var/lib/product-name /var/log/product-name

# Fix file permissions
sudo chmod 755 /var/log/product-name
sudo chmod 644 /etc/product-name/config.yml
sudo chmod 600 /etc/product-name/tls/key.pem

# Ensure service runs as correct user
sudo systemctl edit product-name
# Add:
# [Service]
# User=product
# Group=product
```

#### Issue: Out of Memory

**Symptom:**
```
OOMKilled: Out of memory
```

**Solution:**
```bash
# Check memory usage
free -h
docker stats  # For Docker installations

# Reduce worker count in config.yml
nano /etc/product-name/config.yml
# Change: server.workers: 2  # From 4

# Increase system swap (if physical RAM limited)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# For Docker, increase container memory limit
docker update --memory="4g" product-app
```

### Diagnostic Commands

```bash
# Full system diagnostic
product-name doctor --verbose

# Configuration validation
product-name config validate

# Database connectivity test
product-name db test-connection

# Show version and build info
product-name version --verbose

# Generate support bundle
product-name support-bundle generate
# Sends logs, config (redacted), and diagnostics to /tmp/support-bundle.tar.gz
```

### Getting Support

If issues persist:

1. **Check Logs**: `sudo journalctl -u product-name -n 100`
2. **Search Known Issues**: https://github.com/product-org/product-name/issues
3. **Community Forum**: https://community.product.com
4. **Support Email**: support@product.com (Enterprise customers)

Include the following when requesting help:
- Product version: `product-name --version`
- Operating system: `uname -a`
- Installation method used
- Relevant log excerpts
- Support bundle if requested

## Uninstallation

### Docker

```bash
# Stop and remove containers
docker-compose down

# Remove volumes (WARNING: deletes all data)
docker-compose down -v

# Remove images
docker rmi product-org/product-name:2.1.0
```

### Package Manager

```bash
# Ubuntu/Debian
sudo systemctl stop product-name
sudo systemctl disable product-name
sudo apt-get remove --purge product-name
sudo apt-get autoremove

# RHEL/CentOS
sudo systemctl stop product-name
sudo systemctl disable product-name
sudo yum remove product-name

# macOS (Homebrew)
brew services stop product-name
brew uninstall product-name
```

### Binary Installation

```bash
# Stop service
sudo systemctl stop product-name
sudo systemctl disable product-name

# Remove binary
sudo rm /usr/local/bin/product-name

# Remove service file
sudo rm /etc/systemd/system/product-name.service
sudo systemctl daemon-reload

# Remove configuration and data (optional)
sudo rm -rf /etc/product-name
sudo rm -rf /var/lib/product-name
sudo rm -rf /var/log/product-name

# Remove user account
sudo userdel product
```

## Next Steps

After successful installation:

1. **Security Hardening**: Review [Security Guide](docs/security-hardening.md)
2. **Configuration Tuning**: See [Configuration Reference](docs/configuration.md)
3. **Monitoring Setup**: Configure [Monitoring & Alerts](docs/monitoring.md)
4. **Backup Configuration**: Set up [Backup & Recovery](docs/backup.md)
5. **User Guide**: Start using [Product User Manual](docs/user-guide.md)
6. **API Integration**: Explore [API Documentation](https://docs.product.com/api)

---

**Need Help?** Visit [Product Documentation](https://docs.product.com) or join our [Community Forum](https://community.product.com)

**Version**: 2.1.0 | **Last Updated**: 2025-01-15 | **Feedback**: docs@product.com
