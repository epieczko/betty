# API Catalog

## Document Information

**Version**: 1.0.0
**Status**: Active
**Owner**: API Platform Team
**Last Updated**: 2025-10-26
**Review Cycle**: Continuous (updated with each API release)
**Classification**: Internal

## Purpose

This catalog provides a centralized, authoritative registry of all APIs across the organization, documenting REST, GraphQL, and gRPC interfaces with their endpoints, authentication methods, versioning status, SLAs, ownership, and dependencies. It serves as the single source of truth for API discovery, governance, and integration planning.

## Scope

**In Scope**:
- Public-facing APIs (external customers, partners)
- Internal APIs (service-to-service, microservices)
- Partner APIs (B2B integrations)
- REST, GraphQL, gRPC, and WebSocket APIs
- API versions, deprecation status, and lifecycle stage
- Authentication and authorization methods
- Rate limits and throttling policies
- SLAs and performance characteristics

**Out of Scope**:
- Database schemas (covered in data dictionaries)
- Message queue topics (covered in topic catalogs)
- Internal function calls within monolithic applications
- UI component APIs

---

## REST APIs

### User Service API

**API Name**: User Service API
**Base URL**: `https://api.company.com/users/v2`
**Protocol**: REST (HTTP/JSON)
**OpenAPI Spec**: [users-api-v2.yaml](https://github.com/company/api-specs/blob/main/users-api-v2.yaml)
**Version**: v2 (current), v1 (deprecated)
**Status**: Production
**Owner**: Identity Team (identity-team@company.com)
**On-Call**: PagerDuty rotation "Identity Service"

#### Description
Provides CRUD operations for user accounts, authentication, profile management, and preferences. Supports user registration, login, password management, and profile updates.

#### Authentication
- **Method**: OAuth 2.0 (Bearer tokens)
- **Scopes**: `users:read`, `users:write`, `users:admin`
- **Token Endpoint**: `https://auth.company.com/oauth/token`
- **Token Expiry**: 1 hour (access token), 30 days (refresh token)

#### Endpoints

| Method | Endpoint | Description | Auth Required | Rate Limit |
|--------|----------|-------------|---------------|------------|
| POST | `/v2/users` | Create new user account | No (public registration) | 10/min per IP |
| GET | `/v2/users/{userId}` | Retrieve user profile | Yes (`users:read`) | 1000/min |
| PUT | `/v2/users/{userId}` | Update user profile | Yes (`users:write`) | 100/min |
| DELETE | `/v2/users/{userId}` | Deactivate user account | Yes (`users:admin`) | 10/min |
| GET | `/v2/users/{userId}/preferences` | Get user preferences | Yes (`users:read`) | 1000/min |
| POST | `/v2/users/{userId}/password/reset` | Initiate password reset | No (email verification) | 3/hour per email |
| GET | `/v2/users/search?q={query}` | Search users by name/email | Yes (`users:admin`) | 100/min |

#### Request/Response Examples

**Create User (POST /v2/users)**
```json
// Request
{
  "email": "jane.doe@example.com",
  "password": "SecureP@ssw0rd!",
  "firstName": "Jane",
  "lastName": "Doe",
  "acceptedTerms": true
}

// Response (201 Created)
{
  "userId": "usr_7h3k9l2m",
  "email": "jane.doe@example.com",
  "firstName": "Jane",
  "lastName": "Doe",
  "createdAt": "2025-10-26T14:32:10Z",
  "status": "active"
}
```

#### Performance SLAs
- **Availability**: 99.9% uptime
- **Latency**: P95 < 200ms, P99 < 500ms
- **Throughput**: 10,000 requests/second

#### Error Codes
- `400 Bad Request`: Invalid input (missing required fields, invalid format)
- `401 Unauthorized`: Missing or invalid authentication token
- `403 Forbidden`: Insufficient permissions for operation
- `404 Not Found`: User not found
- `409 Conflict`: Email already registered
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server-side error
- `503 Service Unavailable`: Service temporarily down

#### Dependencies
- **Upstream**: None (entry point API)
- **Downstream**:
  - Email Service (for verification emails)
  - Audit Log Service (for user activity logging)
  - Analytics Service (for user behavior tracking)

#### Versioning & Deprecation
- **Current Version**: v2 (released 2025-01-15)
- **Previous Version**: v1 (deprecated 2025-01-15, sunset 2025-07-15)
- **Breaking Changes in v2**:
  - Renamed `username` field to `email`
  - Removed `phoneNumber` from required fields
  - Added `acceptedTerms` boolean (required)

---

### Payment Processing API

**API Name**: Payment Processing API
**Base URL**: `https://api.company.com/payments/v1`
**Protocol**: REST (HTTP/JSON)
**OpenAPI Spec**: [payments-api-v1.yaml](https://github.com/company/api-specs/blob/main/payments-api-v1.yaml)
**Version**: v1
**Status**: Production
**Owner**: Payments Team (payments-team@company.com)
**On-Call**: PagerDuty rotation "Payments Service"
**Compliance**: PCI-DSS Level 1 compliant

#### Description
Processes payment transactions, manages payment methods, handles refunds, and provides transaction history. Integrates with Stripe, PayPal, and internal payment gateway.

#### Authentication
- **Method**: API Key (Header: `X-API-Key`)
- **Key Rotation**: 90 days
- **Environment-specific keys**: Separate keys for sandbox and production

#### Endpoints

| Method | Endpoint | Description | Auth Required | Rate Limit | Idempotent |
|--------|----------|-------------|---------------|------------|------------|
| POST | `/v1/charges` | Create payment charge | Yes | 100/min | Yes (idempotency-key) |
| GET | `/v1/charges/{chargeId}` | Retrieve charge details | Yes | 1000/min | N/A |
| POST | `/v1/refunds` | Process refund | Yes | 50/min | Yes (idempotency-key) |
| GET | `/v1/customers/{customerId}/payment-methods` | List payment methods | Yes | 500/min | N/A |
| POST | `/v1/customers/{customerId}/payment-methods` | Add payment method | Yes | 100/min | No |
| DELETE | `/v1/payment-methods/{methodId}` | Delete payment method | Yes | 100/min | Yes |

#### Request/Response Examples

**Create Charge (POST /v1/charges)**
```json
// Request
{
  "amount": 4999,
  "currency": "USD",
  "paymentMethodId": "pm_card_visa_4242",
  "customerId": "cus_abc123",
  "description": "Order #ORD-2025-001234",
  "metadata": {
    "orderId": "ORD-2025-001234",
    "userId": "usr_7h3k9l2m"
  }
}

// Response (201 Created)
{
  "chargeId": "ch_5f8g9h1j",
  "status": "succeeded",
  "amount": 4999,
  "currency": "USD",
  "createdAt": "2025-10-26T14:35:22Z",
  "receiptUrl": "https://receipts.company.com/ch_5f8g9h1j"
}
```

#### Performance SLAs
- **Availability**: 99.95% uptime (critical business service)
- **Latency**: P95 < 500ms, P99 < 1s
- **Throughput**: 5,000 requests/second

#### Security Controls
- **TLS**: TLS 1.3 required
- **PCI Compliance**: Level 1 certified
- **Data Encryption**: Card data encrypted at rest with AES-256
- **Tokenization**: Card numbers tokenized, never stored in plaintext
- **IP Allowlist**: Production keys restricted to known server IPs
- **Webhook Signatures**: All webhooks signed with HMAC-SHA256

#### Monitoring & Alerting
- **Success Rate**: Alert if < 99.5% over 5 minutes
- **Latency**: Alert if P99 > 2s
- **Error Rate**: Alert if 5xx errors > 0.5%
- **Fraud Detection**: Alert on suspicious transaction patterns

#### Dependencies
- **Upstream**: Order Service, Cart Service
- **Downstream**:
  - Stripe API (payment processing)
  - Fraud Detection Service
  - Notification Service (payment confirmations)
  - Accounting Service (revenue recognition)

---

## GraphQL APIs

### Product Catalog API (GraphQL)

**API Name**: Product Catalog GraphQL API
**Endpoint**: `https://api.company.com/graphql`
**Protocol**: GraphQL (HTTP/JSON)
**Schema**: [product-catalog-schema.graphql](https://github.com/company/api-specs/blob/main/product-catalog-schema.graphql)
**Version**: 1.0 (schema versioning via deprecation)
**Status**: Production
**Owner**: Catalog Team (catalog-team@company.com)
**Playground**: `https://api.company.com/graphql/playground` (staging only)

#### Description
Provides flexible querying and filtering of product catalog, including products, categories, inventory, pricing, and reviews. Optimized for mobile and web frontends with complex data requirements.

#### Authentication
- **Method**: OAuth 2.0 Bearer tokens (for mutations), API Key (for queries)
- **Public Access**: Read queries allowed without authentication (rate limited)

#### Schema Overview

**Types**:
- `Product`: Product details, pricing, inventory
- `Category`: Product categories, hierarchical structure
- `Review`: Customer reviews and ratings
- `Inventory`: Stock levels, availability
- `PricePoint`: Price history, discounts

**Queries**:
- `product(id: ID!)`: Get single product
- `products(filter: ProductFilter, limit: Int, offset: Int)`: Search products
- `category(id: ID!)`: Get category with products
- `searchProducts(query: String!)`: Full-text search

**Mutations**:
- `createProduct(input: ProductInput!)`: Create product (admin only)
- `updateProduct(id: ID!, input: ProductInput!)`: Update product
- `deleteProduct(id: ID!)`: Soft-delete product

#### Query Examples

```graphql
# Get product with reviews and related products
query GetProductDetails($productId: ID!) {
  product(id: $productId) {
    id
    name
    description
    price {
      amount
      currency
      discount
    }
    inventory {
      inStock
      quantity
      availableAt
    }
    reviews(limit: 10, sort: MOST_RECENT) {
      rating
      comment
      author {
        name
        verifiedPurchase
      }
      createdAt
    }
    relatedProducts(limit: 5) {
      id
      name
      price {
        amount
        currency
      }
      imageUrl
    }
  }
}

# Search products with filtering
query SearchProducts($query: String!, $category: ID, $priceRange: PriceRangeInput) {
  searchProducts(
    query: $query
    filter: {
      categoryId: $category
      priceRange: $priceRange
      inStockOnly: true
    }
    limit: 20
  ) {
    totalCount
    products {
      id
      name
      price {
        amount
        currency
      }
      imageUrl
      rating
    }
  }
}
```

#### Performance SLAs
- **Availability**: 99.9% uptime
- **Latency**: P95 < 300ms, P99 < 800ms
- **Query Complexity**: Max depth 5, max fields 100
- **Rate Limiting**:
  - Authenticated: 2000 queries/minute
  - Anonymous: 100 queries/minute

#### Cost Controls
- **Query Complexity Limits**: Prevent expensive queries
- **Persisted Queries**: Cache frequent query patterns
- **DataLoader**: Batch and cache database queries
- **CDN Caching**: Cache product data for 5 minutes

---

## gRPC APIs

### Order Fulfillment Service (gRPC)

**Service Name**: OrderFulfillment
**Endpoint**: `fulfillment.company.internal:50051`
**Protocol**: gRPC (Protocol Buffers)
**Proto File**: [order_fulfillment.proto](https://github.com/company/protos/blob/main/order_fulfillment.proto)
**Version**: v1
**Status**: Production
**Owner**: Fulfillment Team (fulfillment-team@company.com)
**Network**: Internal only (VPC private subnet)

#### Description
High-performance internal API for order fulfillment operations, warehouse management, inventory allocation, and shipping coordination. Used by order processing pipeline and warehouse management systems.

#### Authentication
- **Method**: mTLS (mutual TLS with client certificates)
- **Certificate Authority**: Internal PKI
- **Certificate Rotation**: 90 days

#### Service Definition

```protobuf
service OrderFulfillment {
  // Allocate inventory for order
  rpc AllocateInventory(AllocationRequest) returns (AllocationResponse);

  // Create shipment for order
  rpc CreateShipment(ShipmentRequest) returns (ShipmentResponse);

  // Get fulfillment status
  rpc GetFulfillmentStatus(StatusRequest) returns (StatusResponse);

  // Stream inventory updates
  rpc StreamInventoryUpdates(InventoryFilter) returns (stream InventoryUpdate);
}

message AllocationRequest {
  string order_id = 1;
  repeated LineItem line_items = 2;
  string warehouse_preference = 3;
}

message AllocationResponse {
  string allocation_id = 1;
  AllocationStatus status = 2;
  repeated AllocatedItem allocated_items = 3;
  google.protobuf.Timestamp estimated_ship_date = 4;
}
```

#### Performance SLAs
- **Availability**: 99.95% uptime
- **Latency**: P95 < 50ms, P99 < 100ms (internal network)
- **Throughput**: 50,000 requests/second

#### Monitoring
- **gRPC Status Codes**: Track OK, FAILED_PRECONDITION, DEADLINE_EXCEEDED
- **Request Duration**: Histogram by RPC method
- **Active Streams**: Gauge for streaming RPCs

---

## API Governance

### API Lifecycle

1. **Design**: Define API contract (OpenAPI, GraphQL schema, Proto)
2. **Review**: Architecture review board approval
3. **Implementation**: Develop with automated tests
4. **Testing**: Integration tests, load tests, security scans
5. **Staging**: Deploy to staging, validate with consumers
6. **Production**: Gradual rollout, monitor SLOs
7. **Maintenance**: Monitor, optimize, version upgrades
8. **Deprecation**: Announce deprecation, provide migration guide, sunset

### Versioning Policy

- **REST APIs**: URL versioning (`/v1/`, `/v2/`)
- **GraphQL**: Schema evolution with `@deprecated` directive
- **gRPC**: Proto package versioning (`company.service.v1`)
- **Deprecation Notice**: 6 months minimum before sunset
- **Breaking Changes**: Require new major version

### Rate Limiting

| API Type | Public | Authenticated | Partner | Internal |
|----------|--------|---------------|---------|----------|
| REST | 60/min | 1000/min | 10000/min | Unlimited |
| GraphQL | 100/min | 2000/min | 20000/min | Unlimited |
| gRPC | N/A | N/A | N/A | Unlimited |

### Security Standards

- **Authentication**: OAuth 2.0 (public APIs), mTLS (internal gRPC)
- **Authorization**: RBAC with scopes/permissions
- **TLS**: TLS 1.3 minimum for all APIs
- **Input Validation**: All inputs validated, sanitized
- **Rate Limiting**: Applied per API key/user
- **API Keys**: Rotated every 90 days
- **Audit Logging**: All mutations logged to audit trail

### SLO Framework

All production APIs must define:
- **Availability SLO**: Target uptime percentage
- **Latency SLO**: P95 and P99 targets
- **Error Rate SLO**: Maximum error rate
- **Success Rate SLO**: Minimum success rate

Error budgets calculated monthly. SLO violations trigger incident response.

---

## API Discovery

### Developer Portal
- **URL**: https://developers.company.com
- **Features**:
  - Interactive API documentation
  - API key management
  - Code samples (curl, JavaScript, Python, Java)
  - Sandbox environments for testing
  - Changelogs and migration guides

### OpenAPI Registry
- **Repository**: https://github.com/company/api-specs
- **Validation**: CI/CD validates OpenAPI schemas on merge
- **Documentation**: Auto-generated from OpenAPI specs

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-26 | API Platform Team | Initial API catalog with REST, GraphQL, gRPC APIs |

---

## References

- API Design Guidelines
- OAuth 2.0 Implementation Guide
- GraphQL Schema Best Practices
- gRPC Service Standards
