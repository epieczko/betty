# Docker Compose Manifests

## Document Information

**Purpose**: Define multi-container application orchestration for local development, integration testing, CI/CD pipelines, and small-scale production deployments using Docker Compose, enabling developers to spin up complete application stacks with a single command.

**Format**: Markdown with Docker Compose YAML examples

**Target Audience**: Application Developers, QA Engineers, DevOps Engineers, Platform Engineers

**Related Artifacts**:
- Dockerfile
- Kubernetes Manifests
- Environment Matrix
- CI/CD Pipeline Definitions

---

## Metadata

```yaml
version: "1.1.0"
created: "2024-01-10"
lastModified: "2024-01-20"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
```

---

## 1. Full-Stack Application Example

### 1.1 Complete Multi-Service Stack

**File**: `docker-compose.yml`

```yaml
version: '3.9'

services:
  # =========================================================================
  # FRONTEND - React Application
  # =========================================================================
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: development
      args:
        NODE_VERSION: '20'
    image: myapp/frontend:latest
    container_name: myapp-frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules  # Anonymous volume for node_modules
    environment:
      - NODE_ENV=development
      - REACT_APP_API_URL=http://localhost:8080/api
      - CHOKIDAR_USEPOLLING=true  # For hot reload in Docker
    depends_on:
      - api
    networks:
      - frontend-network
    restart: unless-stopped

  # =========================================================================
  # API - Node.js/Express Backend
  # =========================================================================
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: development
    image: myapp/api:latest
    container_name: myapp-api
    ports:
      - "8080:8080"
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - PORT=8080
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/myapp_dev
      - REDIS_URL=redis://redis:6379
      - KAFKA_BROKERS=kafka:9092
      - JWT_SECRET=dev-secret-change-in-production
      - LOG_LEVEL=debug
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      kafka:
        condition: service_started
    networks:
      - frontend-network
      - backend-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # =========================================================================
  # WORKER - Background Job Processor
  # =========================================================================
  worker:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: development
    image: myapp/worker:latest
    container_name: myapp-worker
    command: npm run worker
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/myapp_dev
      - REDIS_URL=redis://redis:6379
      - KAFKA_BROKERS=kafka:9092
    depends_on:
      - postgres
      - redis
      - kafka
    networks:
      - backend-network
    restart: unless-stopped

  # =========================================================================
  # POSTGRES - Primary Database
  # =========================================================================
  postgres:
    image: postgres:15-alpine
    container_name: myapp-postgres
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=myapp_dev
      - POSTGRES_INITDB_ARGS=--encoding=UTF-8
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./database/init:/docker-entrypoint-initdb.d  # Initialization scripts
    networks:
      - backend-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # =========================================================================
  # REDIS - Cache & Session Store
  # =========================================================================
  redis:
    image: redis:7-alpine
    container_name: myapp-redis
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes --requirepass redis-dev-password
    volumes:
      - redis-data:/data
    networks:
      - backend-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

  # =========================================================================
  # KAFKA - Message Broker
  # =========================================================================
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: myapp-zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    volumes:
      - zookeeper-data:/var/lib/zookeeper/data
      - zookeeper-logs:/var/lib/zookeeper/log
    networks:
      - backend-network

  kafka:
    image: confluentinc/cp-kafka:latest
    container_name: myapp-kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"
    volumes:
      - kafka-data:/var/lib/kafka/data
    depends_on:
      - zookeeper
    networks:
      - backend-network

  # =========================================================================
  # NGINX - Reverse Proxy
  # =========================================================================
  nginx:
    image: nginx:alpine
    container_name: myapp-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      - frontend
      - api
    networks:
      - frontend-network
    restart: unless-stopped

  # =========================================================================
  # ADMINER - Database Management UI
  # =========================================================================
  adminer:
    image: adminer:latest
    container_name: myapp-adminer
    ports:
      - "8081:8080"
    environment:
      ADMINER_DEFAULT_SERVER: postgres
    networks:
      - backend-network
    profiles:
      - tools  # Only start with --profile tools

  # =========================================================================
  # MAILHOG - Email Testing
  # =========================================================================
  mailhog:
    image: mailhog/mailhog:latest
    container_name: myapp-mailhog
    ports:
      - "1025:1025"  # SMTP
      - "8025:8025"  # Web UI
    networks:
      - backend-network
    profiles:
      - tools

# =============================================================================
# NETWORKS
# =============================================================================
networks:
  frontend-network:
    driver: bridge
  backend-network:
    driver: bridge

# =============================================================================
# VOLUMES
# =============================================================================
volumes:
  postgres-data:
    driver: local
  redis-data:
    driver: local
  kafka-data:
    driver: local
  zookeeper-data:
    driver: local
  zookeeper-logs:
    driver: local
```

---

## 2. Environment-Specific Overrides

### 2.1 Production Override

**File**: `docker-compose.prod.yml`

```yaml
version: '3.9'

services:
  frontend:
    build:
      target: production
    environment:
      - NODE_ENV=production
      - REACT_APP_API_URL=https://api.myapp.com
    restart: always

  api:
    build:
      target: production
    environment:
      - NODE_ENV=production
      - LOG_LEVEL=warn
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    restart: always

  postgres:
    image: postgres:15
    command: postgres -c max_connections=200 -c shared_buffers=256MB
    volumes:
      - /data/postgres:/var/lib/postgresql/data
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

  redis:
    command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

**Usage**:
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### 2.2 Testing Override

**File**: `docker-compose.test.yml`

```yaml
version: '3.9'

services:
  api:
    environment:
      - NODE_ENV=test
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/myapp_test
    command: npm run test:integration

  postgres:
    environment:
      - POSTGRES_DB=myapp_test
    tmpfs:
      - /var/lib/postgresql/data  # In-memory for faster tests

  test-runner:
    build:
      context: ./backend
      dockerfile: Dockerfile.test
    command: npm run test
    environment:
      - CI=true
    depends_on:
      - api
      - postgres
    networks:
      - backend-network
```

---

## 3. CI/CD Integration

### 3.1 CI Pipeline Integration

```yaml
# .github/workflows/test.yml
name: Integration Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Build and test with docker-compose
        run: |
          docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build --abort-on-container-exit
          docker-compose -f docker-compose.yml -f docker-compose.test.yml down -v
```

### 3.2 Local Development Script

**File**: `dev.sh`

```bash
#!/bin/bash

set -e

# Colors for output
GREEN='\033[0.32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting development environment...${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}Creating .env from .env.example${NC}"
    cp .env.example .env
fi

# Build and start services
docker-compose up --build -d

# Wait for services to be healthy
echo -e "${GREEN}Waiting for services to be ready...${NC}"
docker-compose exec -T api curl -f http://localhost:8080/health || sleep 10

# Run database migrations
echo -e "${GREEN}Running database migrations...${NC}"
docker-compose exec -T api npm run migrate

# Show logs
echo -e "${GREEN}Environment ready! Showing logs...${NC}"
docker-compose logs -f
```

---

## 4. Advanced Patterns

### 4.1 Multi-Stage Builds

**File**: `backend/Dockerfile`

```dockerfile
# Development stage
FROM node:20-alpine AS development
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
EXPOSE 8080
CMD ["npm", "run", "dev"]

# Build stage
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
COPY --from=build --chown=nodejs:nodejs /app/dist ./dist
COPY --from=build --chown=nodejs:nodejs /app/node_modules ./node_modules
USER nodejs
EXPOSE 8080
CMD ["node", "dist/server.js"]
```

### 4.2 Health Checks & Dependencies

```yaml
services:
  api:
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### 4.3 Resource Limits

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
```

---

## 5. Best Practices

### 5.1 Environment Variables

```yaml
# .env.example
NODE_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379
JWT_SECRET=change-me-in-production
API_PORT=8080
FRONTEND_PORT=3000
```

**Never commit `.env` to version control!**

### 5.2 Volume Management

```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect myapp_postgres-data

# Remove unused volumes
docker volume prune

# Backup volume
docker run --rm -v myapp_postgres-data:/data -v $(pwd):/backup alpine tar czf /backup/postgres-backup.tar.gz -C /data .
```

### 5.3 Networking

```yaml
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # No external access
```

---

## 6. Troubleshooting

### 6.1 Common Commands

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Restart single service
docker-compose restart api

# Rebuild without cache
docker-compose build --no-cache api

# Execute command in running container
docker-compose exec api npm run migrate

# Check service health
docker-compose ps

# Stop and remove all containers
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### 6.2 Common Issues

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| Port already in use | `Error: port is already allocated` | Change port mapping or stop conflicting service |
| Permission denied | Volume mount issues | Check file permissions, use named volumes |
| Service not starting | Check logs with `docker-compose logs` | Fix configuration, check dependencies |
| Out of disk space | `no space left on device` | Run `docker system prune -a` |
| Network issues | Cannot connect between services | Check network configuration, service names |

---

## 7. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1.0 | 2024-01-20 | Platform Team | Added Kafka, Nginx, health checks |
| 1.0.0 | 2024-01-10 | DevOps Team | Initial Docker Compose stack |

---

## 8. Related Documentation

- [Dockerfile Best Practices](./dockerfile-best-practices.md)
- [Kubernetes Manifests](./kubernetes-manifests.md)
- [Environment Matrix](./environment-matrix.md)
- [Local Development Guide](../documentation/local-development.md)
