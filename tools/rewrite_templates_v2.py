#!/usr/bin/env python3
"""
Rewrite artifact templates with industry best practices and proper field structures.

This script uses AI knowledge of industry standards to generate complete,
realistic template structures for each artifact type.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import date


class IndustryTemplateGenerator:
    """Generate artifact templates based on industry best practices."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.descriptions_dir = self.base_dir / "artifact_descriptions"
        self.templates_dir = self.base_dir / "templates"
        self.stats = {
            "total_descriptions": 0,
            "templates_rewritten": 0,
            "errors": []
        }

    def find_template_path(self, artifact_name: str) -> Optional[Path]:
        """Find the template file path for an artifact."""
        for ext in ['.yaml', '.md']:
            matches = list(self.templates_dir.rglob(f"{artifact_name}{ext}"))
            if matches:
                return matches[0]
        return None

    def parse_description(self, desc_path: Path) -> Dict:
        """Parse artifact description to extract key information."""
        with open(desc_path, 'r') as f:
            content = f.read()

        data = {
            'artifact_name': desc_path.stem,
            'content': content,
            'category': '',
            'executive_summary': '',
            'purpose': '',
            'scope_in': [],
            'best_practices': [],
            'target_audience': {'primary': [], 'secondary': []},
        }

        # Detect category from path or content
        if 'security' in content.lower()[:500] or 'threat' in desc_path.stem:
            data['category'] = 'security'
        elif 'api' in desc_path.stem or 'openapi' in content.lower()[:500]:
            data['category'] = 'api'
        elif 'data' in content.lower()[:500] or 'schema' in desc_path.stem:
            data['category'] = 'data'
        elif 'architecture' in content.lower()[:500] or 'diagram' in desc_path.stem:
            data['category'] = 'architecture'
        elif 'test' in desc_path.stem or 'quality' in desc_path.stem:
            data['category'] = 'testing'
        elif 'policy' in desc_path.stem or 'governance' in content.lower()[:500]:
            data['category'] = 'governance'
        else:
            data['category'] = 'general'

        # Extract executive summary
        exec_match = re.search(
            r'## Executive Summary\s*\n\n(.*?)(?=\n##|\Z)',
            content, re.DOTALL
        )
        if exec_match:
            summary = exec_match.group(1).strip()
            data['executive_summary'] = summary.split('\n\n')[0][:300]

        # Extract purpose
        purpose_match = re.search(
            r'### Primary Purpose\s*\n\n(.*?)(?=\n###|\n##|\Z)',
            content, re.DOTALL
        )
        if purpose_match:
            data['purpose'] = purpose_match.group(1).strip()[:400]

        # Extract scope
        scope_in_match = re.search(
            r'\*\*In Scope\*\*:\s*\n(.*?)(?=\n\*\*Out of Scope|\n##|\Z)',
            content, re.DOTALL
        )
        if scope_in_match:
            items = re.findall(r'^-\s*(.+)$', scope_in_match.group(1), re.MULTILINE)
            data['scope_in'] = [item.strip() for item in items]

        # Extract best practices
        bp_section = re.search(
            r'## Best Practices\s*\n\n(.*?)(?=\n##|\Z)',
            content, re.DOTALL
        )
        if bp_section:
            practices = re.findall(r'^\*\*(.+?)\*\*:\s*(.+)$', bp_section.group(1), re.MULTILINE)
            data['best_practices'] = [(title.strip(), desc.strip()) for title, desc in practices]

        return data

    def generate_threat_model_yaml(self, data: Dict) -> str:
        """Generate threat model template with STRIDE methodology."""
        return """# Threat Model
# See also: artifact_descriptions/threat-model.md for complete guidance

metadata:
  version: "1.0.0"
  created: "YYYY-MM-DD"
  lastModified: "YYYY-MM-DD"
  status: "Draft"

  # Ownership
  author: "Security Architect Name"
  securityReviewer: "Security Team Lead"
  documentOwner: "Product Security Team"
  classification: "Confidential"

  # System Under Analysis
  systemName: "System or Application Name"
  systemVersion: "1.0.0"
  environment: "Production | Staging | Development"

# Threat Modeling Methodology
methodology: "STRIDE"  # STRIDE | PASTA | LINDDUN | Attack Trees

# System Overview
system:
  description: |
    Brief description of the system being threat modeled.
    What does it do? Who uses it? What data does it process?

  boundaries:
    - name: "External Network Boundary"
      description: "Separates internet from DMZ"
      trustLevel: "Untrusted → Trusted"

    - name: "DMZ to Internal Network"
      description: "Separates DMZ from internal systems"
      trustLevel: "Low Trust → High Trust"

  components:
    - name: "Web Application Server"
      type: "Web Service"
      location: "DMZ"
      technologies: ["Node.js", "Express"]
      dataProcessed: ["User credentials", "Session tokens"]

    - name: "Database Server"
      type: "Data Store"
      location: "Internal Network"
      technologies: ["PostgreSQL"]
      dataProcessed: ["User PII", "Financial records"]

  dataFlows:
    - id: "DF-001"
      source: "Internet User"
      destination: "Web Application Server"
      protocol: "HTTPS"
      dataClassification: "Public | Internal | Confidential"
      authentication: "Required | Optional | None"

# Assets
assets:
  - id: "ASSET-001"
    name: "User Credentials Database"
    type: "Data Store"
    classification: "Highly Confidential"
    businessValue: "Critical"
    owner: "Security Team"

  - id: "ASSET-002"
    name: "Payment Processing API Keys"
    type: "Credentials"
    classification: "Restricted"
    businessValue: "Critical"
    owner: "Finance Team"

# Threat Actors
threatActors:
  - name: "External Attacker"
    type: "Opportunistic"
    motivation: "Financial gain"
    capabilities: "Medium"  # Low | Medium | High | Advanced
    resources: "Limited"

  - name: "Insider Threat"
    type: "Malicious Insider"
    motivation: "Data theft, sabotage"
    capabilities: "High"
    resources: "Privileged access"

# Threats (STRIDE Framework)
threats:
  # Spoofing Identity
  - id: "THREAT-001"
    title: "Attacker spoofs legitimate user identity"
    strideCategory: "Spoofing"
    description: |
      An attacker could steal or guess user credentials to impersonate
      a legitimate user and gain unauthorized access to the system.

    affectedAssets: ["ASSET-001"]
    affectedComponents: ["Web Application Server"]
    threatActor: "External Attacker"

    attackScenario: |
      1. Attacker performs credential stuffing attack
      2. Obtains valid username/password combination
      3. Logs in as legitimate user
      4. Accesses sensitive user data

    # DREAD Risk Rating
    dread:
      damage: 8              # 1-10 scale
      reproducibility: 7
      exploitability: 6
      affectedUsers: 9
      discoverability: 5
      total: 35             # Sum / 5 = 7.0 (High)
      rating: "High"        # Low (0-3.3) | Medium (3.4-6.6) | High (6.7-10)

    # Alternative: CVSS Score
    cvss:
      vector: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N"
      score: 9.1
      severity: "Critical"

    mitigations:
      - id: "MIT-001"
        control: "Implement multi-factor authentication (MFA)"
        type: "Preventive"
        status: "Planned"
        owner: "Engineering Team"
        dueDate: "YYYY-MM-DD"

      - id: "MIT-002"
        control: "Rate limiting on login attempts"
        type: "Detective"
        status: "Implemented"
        owner: "Security Team"
        effectiveness: "Medium"

    residualRisk: "Medium"  # After mitigations applied
    mitreAttack: "T1110.003"  # Password Spraying

  # Tampering with Data
  - id: "THREAT-002"
    title: "Unauthorized modification of data in transit"
    strideCategory: "Tampering"
    description: |
      Attacker performs man-in-the-middle attack to intercept and
      modify data being transmitted between client and server.

    affectedAssets: ["ASSET-001"]
    affectedComponents: ["Web Application Server"]
    threatActor: "External Attacker"

    dread:
      damage: 7
      reproducibility: 4
      exploitability: 5
      affectedUsers: 8
      discoverability: 6
      total: 30
      rating: "Medium"

    mitigations:
      - id: "MIT-003"
        control: "Enforce TLS 1.3 for all communications"
        type: "Preventive"
        status: "Implemented"
        effectiveness: "High"

      - id: "MIT-004"
        control: "Implement certificate pinning in mobile apps"
        type: "Preventive"
        status: "Planned"
        owner: "Mobile Team"

    residualRisk: "Low"
    mitreAttack: "T1557"  # Man-in-the-Middle

  # Repudiation
  - id: "THREAT-003"
    title: "User denies performing unauthorized action"
    strideCategory: "Repudiation"
    description: "Insufficient audit logging allows users to deny actions"

    affectedAssets: []
    affectedComponents: ["Web Application Server", "Database Server"]

    dread:
      damage: 6
      reproducibility: 8
      exploitability: 7
      affectedUsers: 5
      discoverability: 4
      total: 30
      rating: "Medium"

    mitigations:
      - id: "MIT-005"
        control: "Comprehensive audit logging of all user actions"
        type: "Detective"
        status: "In Progress"
        owner: "Engineering Team"

      - id: "MIT-006"
        control: "Tamper-proof log storage with integrity checking"
        type: "Detective"
        status: "Planned"

    residualRisk: "Low"

# Security Controls (Mapped to Threats)
securityControls:
  - id: "CTRL-001"
    name: "Multi-Factor Authentication"
    type: "Preventive"
    category: "Authentication"
    implementation: "Auth0 MFA"
    threatsAddressed: ["THREAT-001"]
    status: "Planned"

  - id: "CTRL-002"
    name: "TLS 1.3 Encryption"
    type: "Preventive"
    category: "Cryptography"
    implementation: "NGINX with TLS 1.3"
    threatsAddressed: ["THREAT-002"]
    status: "Implemented"

# Attack Trees (Optional detailed analysis)
attackTrees:
  - goal: "Gain unauthorized access to user data"
    rootNode:
      description: "Compromise user account"
      operator: "OR"
      children:
        - description: "Steal credentials"
          operator: "OR"
          children:
            - description: "Phishing attack"
              likelihood: "High"
              impact: "High"
            - description: "Credential stuffing"
              likelihood: "Medium"
              impact: "High"

        - description: "Exploit authentication bypass"
          likelihood: "Low"
          impact: "Critical"

# Risk Summary
riskSummary:
  critical: 0
  high: 1
  medium: 2
  low: 0

  overallRiskRating: "High"

  topRisks:
    - threatId: "THREAT-001"
      summary: "Credential theft leading to account compromise"
      priority: 1

# Next Steps
recommendations:
  - priority: "P0"
    action: "Implement MFA for all user accounts"
    owner: "Engineering Team"
    dueDate: "YYYY-MM-DD"

  - priority: "P1"
    action: "Conduct penetration test focusing on authentication"
    owner: "Security Team"
    dueDate: "YYYY-MM-DD"

# Approvals
approvals:
  - role: "Security Architect"
    name: "Name"
    date: null
    status: "Pending"

  - role: "CISO"
    name: "Name"
    date: null
    status: "Pending"

# Change History
changeHistory:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    author: "Author Name"
    changes: "Initial threat model"
"""

    def generate_api_versioning_policy_md(self, data: Dict) -> str:
        """Generate API versioning policy with industry standards."""
        return """# API Versioning Policy

> **Version**: 1.0.0
> **Status**: Draft
> **Effective Date**: YYYY-MM-DD
> **Review Date**: YYYY-MM-DD
> **Owner**: API Platform Team
> **Approver**: Chief Architect

---

## Executive Summary

This policy establishes mandatory requirements for versioning all organizational APIs (REST, GraphQL, gRPC, and event-driven APIs). It ensures consistent evolution practices, protects API consumers from unexpected breaking changes, and enables controlled deprecation of legacy API versions while maintaining innovation velocity.

**Key Requirements:**
- All APIs MUST use semantic versioning (SemVer 2.0.0)
- Breaking changes REQUIRE major version increment
- Minimum 12-month deprecation notice period
- Support N-1 versions concurrently during migration

---

## Purpose & Scope

### Purpose

Define mandatory standards for API evolution, backward compatibility, and deprecation management across all REST, GraphQL, gRPC, and event-driven APIs to balance innovation velocity with consumer stability.

### Scope

**In Scope:**
- REST APIs (internal and external)
- GraphQL APIs and schema evolution
- gRPC/Protobuf service definitions
- Event schemas (Kafka, EventBridge, RabbitMQ)
- WebSocket and Server-Sent Events APIs
- API Gateway configurations (Kong, Apigee, AWS API Gateway, Azure APIM)

**Out of Scope:**
- Application version numbering
- Database schema versioning
- Infrastructure versioning
- UI/Frontend versioning

---

## Policy Statements

### 1. Versioning Strategy

**1.1 Primary Versioning Method**

All APIs MUST use **URI path versioning** with major version only:

```
✅ Correct:
GET https://api.example.com/v1/users
GET https://api.example.com/v2/products

❌ Incorrect:
GET https://api.example.com/v1.2/users
GET https://api.example.com/users?version=1
```

**Rationale**: URI versioning provides clear, discoverable, and cacheable version identification.

**1.2 Semantic Versioning Application**

All APIs MUST follow Semantic Versioning 2.0.0 (SemVer):

```
MAJOR.MINOR.PATCH

Example: 2.3.1
- MAJOR (2): Breaking changes, incompatible API changes
- MINOR (3): Backward-compatible new features
- PATCH (1): Backward-compatible bug fixes
```

**Version Tracking:**
- URI exposes MAJOR version: `/v2/`
- OpenAPI `info.version` includes full SemVer: `"2.3.1"`
- Response headers include full version: `API-Version: 2.3.1`

---

### 2. Breaking vs. Non-Breaking Changes

**2.1 Breaking Changes (REQUIRE Major Version Increment)**

The following changes are BREAKING and REQUIRE major version increment:

- ❌ Removing an endpoint
- ❌ Removing a field from request or response
- ❌ Renaming a field
- ❌ Changing field data type (string → number)
- ❌ Adding required request parameter
- ❌ Changing HTTP status codes for existing scenarios
- ❌ Modifying error response structure
- ❌ Tightening validation rules
- ❌ Changing authentication/authorization requirements
- ❌ Modifying rate limiting behavior

**2.2 Non-Breaking Changes (Minor or Patch)**

The following changes are NON-BREAKING:

- ✅ Adding new endpoint (MINOR)
- ✅ Adding optional request parameter (MINOR)
- ✅ Adding new field to response (MINOR)
- ✅ Adding new error code (MINOR)
- ✅ Bug fixes not changing contract (PATCH)
- ✅ Performance improvements (PATCH)
- ✅ Documentation updates (PATCH)

**2.3 Breaking Change Approval**

Breaking changes REQUIRE approval from:
1. API Product Manager
2. Architecture Review Board
3. Affected consumer teams (if internal)

Approval process: Submit Architecture Decision Record (ADR) → Review Board → Consumer notification → Implementation

---

### 3. Version Lifecycle & Support

**3.1 Concurrent Version Support**

**Requirement**: Support N-1 versions concurrently.

```
Current: v3 (active development)
Previous: v2 (maintenance mode, bug fixes only)
Deprecated: v1 (sunset scheduled)
```

**3.2 Support Windows**

| Version Status | Support Level | Duration |
|---------------|---------------|----------|
| **Current (vN)** | Full support | Ongoing |
| **Previous (vN-1)** | Maintenance only | 12-18 months after vN release |
| **Deprecated (≤vN-2)** | Security fixes only | 6 months notice before sunset |
| **Sunset** | No support | Decommissioned |

**3.3 Version Status Tracking**

Maintain version status in API Catalog:

```yaml
/v1/users:
  status: "deprecated"
  releaseDate: "2023-01-15"
  deprecationDate: "2024-06-01"
  sunsetDate: "2025-01-01"
  replacedBy: "/v2/users"

/v2/users:
  status: "active"
  releaseDate: "2024-06-01"

/v3/users:
  status: "beta"
  releaseDate: "2025-02-01"
```

---

### 4. Deprecation Requirements

**4.1 Minimum Deprecation Window**

**Requirement**: 12-month minimum notice before sunset

**Timeline:**
```
T+0:   Announce deprecation (90-day notice begins)
T+90:  Deprecation effective, version marked deprecated
T+180: Second reminder sent to consumers
T+270: Final 90-day warning
T+365: Version sunset, endpoints return 410 Gone
```

**4.2 Deprecation Communication**

**Required Notifications:**

1. **T-90 Days**: Email to registered API consumers
2. **T-60 Days**: Second email + Developer portal banner
3. **T-30 Days**: Final email + API response warnings
4. **T-0 Days**: Sunset, 410 Gone response

**Example Email Template:**
```
Subject: [Action Required] API v1 Deprecation - Sunset in 90 days

The /v1/products API will be sunset on YYYY-MM-DD.

Action Required:
1. Migrate to /v2/products by YYYY-MM-DD
2. Review migration guide: https://docs.api.example.com/migrate-v1-to-v2

Migration Support:
- Office hours: Tuesdays 2-4pm
- Slack: #api-migration-support
```

**4.3 In-API Deprecation Signals**

Deprecated API versions MUST return HTTP headers:

```http
HTTP/1.1 200 OK
Deprecation: Sun, 01 Jan 2025 00:00:00 GMT
Sunset: Sun, 01 Jan 2025 00:00:00 GMT
Link: <https://docs.api.example.com/migrate>; rel="deprecation"
API-Version: 1.5.2
```

---

### 5. Technology-Specific Requirements

**5.1 REST APIs**

**OpenAPI Specification Requirements:**

```yaml
openapi: 3.1.0
info:
  title: "Products API"
  version: "2.3.1"  # Full SemVer
  description: |
    Products API v2

    **Deprecation Notice**: v1 will sunset on 2025-01-01

    Migration guide: https://docs.api.example.com/migrate

servers:
  - url: https://api.example.com/v2
    description: Production

paths:
  /products:
    get:
      summary: "List products"
      deprecated: false  # Set true when deprecating endpoint
```

**5.2 GraphQL APIs**

**Schema Evolution Requirements:**

```graphql
type Product {
  id: ID!
  name: String!
  price: Float!

  # Deprecated field - use 'description' instead
  details: String @deprecated(reason: "Use 'description' field. Will be removed in v3 (2025-06-01)")

  description: String!
}
```

**Breaking Changes for GraphQL:**
- Removing field
- Changing field type
- Adding non-nullable field
- Removing enum value

**Non-Breaking:**
- Adding nullable field
- Adding enum value
- Deprecating field with @deprecated

**5.3 gRPC/Protobuf APIs**

**Compatibility Rules:**

```protobuf
syntax = "proto3";

// v2 of the Product service
service ProductService {
  rpc GetProduct(GetProductRequest) returns (Product);
  rpc ListProducts(ListProductsRequest) returns (ListProductsResponse);
}

message Product {
  string id = 1;
  string name = 2;
  double price = 3;

  // Added in v2.1 (non-breaking)
  string description = 4;

  // NEVER reuse field numbers
  reserved 5;  // Previously used for 'internal_code'
  reserved "internal_code";
}
```

**Breaking Changes:**
- Removing service method
- Changing method signature
- Removing message field
- Changing field type
- Renaming field

**Non-Breaking:**
- Adding service method
- Adding optional field
- Adding enum value

**5.4 Event Schemas**

**Kafka/EventBridge Schema Versioning:**

```json
{
  "topic": "user.created.v2",
  "eventType": "user.created",
  "eventVersion": "2.0.0",
  "data": {
    "userId": "123",
    "email": "user@example.com",
    "createdAt": "2025-01-15T10:00:00Z"
  }
}
```

**Schema Registry Configuration:**

- Use Confluent Schema Registry or AWS Glue Schema Registry
- Compatibility mode: `BACKWARD` (consumers can read old data)
- Schema validation: REQUIRED before publishing

---

### 6. API Gateway Configuration

**6.1 Version Routing**

API Gateways MUST route based on URI version:

```yaml
# Kong Gateway Example
routes:
  - name: products-v1
    paths: ["/v1/products"]
    service: products-service-v1
    plugins:
      - name: response-transformer
        config:
          add:
            headers:
              - "Deprecation: Sun, 01 Jan 2025 00:00:00 GMT"
              - "Sunset: Sun, 01 Jan 2025 00:00:00 GMT"

  - name: products-v2
    paths: ["/v2/products"]
    service: products-service-v2
```

**6.2 Sunset Enforcement**

After sunset date, return:

```http
HTTP/1.1 410 Gone
Content-Type: application/json

{
  "error": "API version sunset",
  "message": "API v1 was sunset on 2025-01-01. Please migrate to v2.",
  "documentation": "https://docs.api.example.com/migrate",
  "currentVersion": "v2"
}
```

---

### 7. Migration Support

**7.1 Migration Guides REQUIRED**

For each major version, provide:

1. **What Changed** - Detailed changelog
2. **Breaking Changes** - Specific incompatibilities
3. **Migration Steps** - Step-by-step guide
4. **Code Examples** - Before/after comparisons
5. **Testing Guidance** - How to validate migration

**7.2 Overlap Period**

Run v(N) and v(N-1) concurrently for minimum 6 months.

**7.3 Canary Migration**

Recommend consumers:
1. Implement against new version in test environment
2. Run parallel comparison (dual-write if needed)
3. Gradual traffic shift (10% → 50% → 100%)
4. Monitor for errors/degradation

---

### 8. Monitoring & Analytics

**8.1 Required Metrics**

Track per API version:
- Request volume
- Error rates
- Response times
- Consumer adoption (% on each version)

**8.2 Deprecation Dashboard**

Publish version adoption dashboard showing:
- Current version distribution
- Migration progress
- Consumers still on deprecated versions

**8.3 Sunset Readiness**

Block sunset if >5% traffic still on deprecated version.

---

### 9. Emergency Breaking Changes

**9.1 Security Exception Process**

For critical security vulnerabilities:

1. Security team approval REQUIRED
2. Minimum 7-day notice (vs. standard 90-day)
3. Clear security advisory published
4. Direct outreach to affected consumers

**9.2 Emergency Change Template**

```markdown
# SECURITY ADVISORY: Emergency Breaking Change

**Severity**: Critical
**Affected Version**: v2.x
**Issue**: CVE-2025-XXXXX
**Action Required By**: YYYY-MM-DD (7 days)

## Vulnerability
[Description]

## Required Action
Upgrade to v2.4.5 by YYYY-MM-DD

## Breaking Change
[Specific changes]

## Support
Contact security@example.com
```

---

### 10. Compliance & Enforcement

**10.1 Pre-Production Checks**

CI/CD pipeline MUST validate:
- [ ] OpenAPI spec includes version
- [ ] No breaking changes in minor/patch versions
- [ ] Deprecated APIs return proper headers
- [ ] API documented in API catalog

**10.2 Breaking Change Detection**

Use automated tools:
- `openapi-diff` for REST APIs
- `buf breaking` for gRPC
- `graphql-inspector` for GraphQL

**10.3 Non-Compliance**

APIs not following this policy:
- Blocked from production deployment
- Escalated to Architecture Review Board
- Require exception approval

---

### 11. Exceptions

**11.1 Exception Process**

To request policy exception:

1. Submit exception request with justification
2. Architecture Review Board review
3. CTO approval required
4. Time-boxed exception (max 6 months)
5. Remediation plan required

---

### 12. Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **API Product Owner** | Define version roadmap, approve breaking changes |
| **API Engineers** | Implement versioning, maintain OpenAPI specs |
| **Platform Team** | API Gateway configuration, monitoring |
| **Security Team** | Review security implications of changes |
| **Architecture Review Board** | Approve breaking changes, grant exceptions |

---

## Related Policies

- API Design Standards
- Data Retention Policy
- Change Management Policy
- Security Policy

---

## References

- [Semantic Versioning 2.0.0](https://semver.org/)
- [RFC 8594 - Sunset HTTP Header](https://www.rfc-editor.org/rfc/rfc8594.html)
- [OpenAPI Specification 3.1](https://spec.openapis.org/oas/v3.1.0)

---

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Chief Architect | | YYYY-MM-DD | Pending |
| VP Engineering | | YYYY-MM-DD | Pending |
| CISO | | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | API Platform Team | Initial policy |

---

*See also: `artifact_descriptions/api-versioning-policy.md` for complete guidance*
"""

    def generate_data_contract_yaml(self, data: Dict) -> str:
        """Generate data contract template with data governance standards."""
        return """# Data Contract
# See also: artifact_descriptions/data-contracts.md for complete guidance

metadata:
  version: "1.0.0"
  created: "YYYY-MM-DD"
  lastModified: "YYYY-MM-DD"
  status: "Draft"  # Draft | Review | Active | Deprecated

  # Contract Ownership
  dataProductOwner: "Data Product Owner Name"
  dataProductName: "Customer Analytics Data Product"
  team: "Analytics Engineering Team"

  # Technical Ownership
  upstream:
    system: "CRM System"
    owner: "CRM Team"
    contact: "crm-team@example.com"

  downstream:
    - system: "Analytics Dashboard"
      owner: "BI Team"
      contact: "bi-team@example.com"
    - system: "ML Training Pipeline"
      owner: "Data Science Team"
      contact: "ds-team@example.com"

# Contract Definition
contract:
  # Dataset Identifier
  dataset:
    name: "customer_events"
    fullyQualifiedName: "analytics.production.customer_events"
    type: "table"  # table | view | stream | file | api
    platform: "Snowflake"  # Snowflake | BigQuery | Redshift | Databricks | S3

  # Service Level Agreement (SLA)
  sla:
    # Data Freshness
    freshness:
      maxStaleness: "15 minutes"
      freshnessCheck: "event_timestamp"
      schedule: "*/15 * * * *"  # Every 15 minutes
      alertThreshold: "30 minutes"

    # Availability
    availability:
      uptime: "99.9%"
      maintenanceWindows:
        - day: "Sunday"
          startTime: "02:00 UTC"
          duration: "2 hours"

    # Completeness
    completeness:
      expectedRowsPerDay: 1000000
      tolerance: 0.05  # 5% variance acceptable
      checkSchedule: "0 1 * * *"  # Daily at 1 AM

    # Latency
    latency:
      p50: "5 seconds"
      p95: "15 seconds"
      p99: "30 seconds"

  # Schema Definition
  schema:
    format: "avro"  # avro | parquet | json | protobuf
    compatibility: "BACKWARD"  # BACKWARD | FORWARD | FULL | NONE

    fields:
      - name: "event_id"
        type: "string"
        required: true
        primaryKey: true
        description: "Unique identifier for the event (UUID v4)"
        example: "550e8400-e29b-41d4-a716-446655440000"
        constraints:
          - type: "regex"
            pattern: "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"

      - name: "customer_id"
        type: "string"
        required: true
        foreignKey:
          table: "customers"
          column: "customer_id"
        description: "Customer identifier"
        pii: true
        classification: "Confidential"
        constraints:
          - type: "not_null"
          - type: "length"
            min: 1
            max: 50

      - name: "event_type"
        type: "string"
        required: true
        description: "Type of customer event"
        example: "page_view"
        constraints:
          - type: "enum"
            values:
              - "page_view"
              - "button_click"
              - "purchase"
              - "signup"
              - "login"

      - name: "event_timestamp"
        type: "timestamp"
        required: true
        description: "When the event occurred (UTC)"
        example: "2025-01-15T10:30:00Z"
        constraints:
          - type: "not_null"
          - type: "not_future"

      - name: "event_properties"
        type: "json"
        required: false
        description: "Event-specific properties as JSON object"
        example: '{"page": "/products", "referrer": "google"}'

      - name: "user_agent"
        type: "string"
        required: false
        description: "Browser user agent string"
        constraints:
          - type: "length"
            max: 500

      - name: "ip_address"
        type: "string"
        required: false
        description: "Client IP address (anonymized)"
        pii: true
        classification: "Confidential"
        constraints:
          - type: "regex"
            pattern: "^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$"

      - name: "session_id"
        type: "string"
        required: false
        description: "Session identifier"

      - name: "created_at"
        type: "timestamp"
        required: true
        description: "When record was created in data warehouse"
        systemGenerated: true

      - name: "updated_at"
        type: "timestamp"
        required: true
        description: "When record was last updated"
        systemGenerated: true

      - name: "_partition_date"
        type: "date"
        required: true
        description: "Partition key (event date)"
        partitionKey: true
        systemGenerated: true

    # Partitioning Strategy
    partitioning:
      type: "date"
      field: "_partition_date"
      granularity: "day"
      retention: "2 years"

    # Clustering/Sorting
    clustering:
      fields: ["customer_id", "event_type", "event_timestamp"]

  # Data Quality Rules
  qualityRules:
    - name: "event_id_uniqueness"
      type: "uniqueness"
      field: "event_id"
      threshold: 1.0  # 100% unique
      severity: "critical"

    - name: "customer_id_not_null"
      type: "completeness"
      field: "customer_id"
      threshold: 0.99  # 99% complete
      severity: "critical"

    - name: "event_type_valid_values"
      type: "validity"
      field: "event_type"
      validValues: ["page_view", "button_click", "purchase", "signup", "login"]
      threshold: 1.0
      severity: "high"

    - name: "timestamp_freshness"
      type: "timeliness"
      field: "event_timestamp"
      maxAge: "24 hours"
      severity: "medium"

    - name: "row_count_consistency"
      type: "volume"
      minRows: 950000  # 95% of expected 1M
      maxRows: 1050000  # 105% of expected 1M
      period: "daily"
      severity: "high"

  # Data Lineage
  lineage:
    upstream:
      - source: "kafka://events-cluster/customer-events"
        type: "streaming"
        transformations:
          - "Schema validation"
          - "PII anonymization"
          - "Timestamp conversion to UTC"

      - source: "postgres://crm-db/customers"
        type: "batch"
        joinCondition: "customer_events.customer_id = customers.id"
        transformations:
          - "Customer ID enrichment"

    downstream:
      - destination: "analytics.marts.customer_behavior"
        type: "materialized_view"
        transformations:
          - "Event aggregation by customer"
          - "Session calculation"

      - destination: "ml.features.customer_features"
        type: "feature_store"
        transformations:
          - "Feature engineering pipeline"

  # Data Classification & Privacy
  privacy:
    containsPII: true
    piiFields: ["customer_id", "ip_address"]
    dataClassification: "Confidential"

    regulations:
      - name: "GDPR"
        applicability: "EU customers"
        requirements:
          - "Right to erasure (customer_id must be deletable)"
          - "Data minimization (anonymize IP after 90 days)"

      - name: "CCPA"
        applicability: "California customers"
        requirements:
          - "Right to deletion"
          - "Do not sell customer data"

    retention:
      period: "2 years"
      deletionMethod: "Hard delete"
      exceptions: []

  # Access Control
  access:
    readAccess:
      - role: "analytics_engineer"
        scope: "all_fields"

      - role: "data_scientist"
        scope: "all_fields"
        purpose: "ML model training"

      - role: "bi_analyst"
        scope: "non_pii_fields"
        excludedFields: ["ip_address", "customer_id"]

    writeAccess:
      - role: "etl_service_account"
        operations: ["INSERT", "UPDATE"]

    approvalRequired: true
    approver: "Data Governance Team"

# Service Level Indicators (SLI)
sli:
  - metric: "data_freshness"
    measurement: "MAX(CURRENT_TIMESTAMP - event_timestamp)"
    target: "< 15 minutes"
    query: |
      SELECT MAX(CURRENT_TIMESTAMP - event_timestamp) AS staleness
      FROM analytics.production.customer_events
      WHERE _partition_date = CURRENT_DATE

  - metric: "completeness"
    measurement: "COUNT(*) / expected_count"
    target: "> 95%"
    query: |
      SELECT COUNT(*) AS actual_rows,
             1000000 AS expected_rows,
             COUNT(*) / 1000000.0 AS completeness_ratio
      FROM analytics.production.customer_events
      WHERE _partition_date = CURRENT_DATE

# Alerts & Monitoring
monitoring:
  alerts:
    - name: "data_freshness_sla_breach"
      condition: "staleness > 30 minutes"
      severity: "critical"
      notification:
        - channel: "pagerduty"
          team: "data-platform-oncall"
        - channel: "slack"
          channel: "#data-alerts"

    - name: "quality_rule_failure"
      condition: "any quality rule fails"
      severity: "high"
      notification:
        - channel: "slack"
          channel: "#data-quality"

    - name: "volume_anomaly"
      condition: "row_count outside expected range"
      severity: "medium"
      notification:
        - channel: "email"
          recipients: ["data-team@example.com"]

  dashboard:
    url: "https://monitoring.example.com/dashboards/customer-events"
    metrics:
      - "Row count trend"
      - "Freshness over time"
      - "Quality rule pass rate"
      - "Query performance"

# Testing & Validation
testing:
  unitTests:
    - name: "schema_validation"
      description: "Validate all rows conform to schema"
      frequency: "every pipeline run"

    - name: "quality_rules_check"
      description: "Run all quality rules"
      frequency: "every pipeline run"

  integrationTests:
    - name: "end_to_end_latency"
      description: "Measure source to warehouse latency"
      frequency: "hourly"

    - name: "downstream_compatibility"
      description: "Ensure downstream systems can consume data"
      frequency: "on schema change"

# Contract Evolution
evolution:
  compatibilityMode: "BACKWARD"

  allowedChanges:
    - "Add optional field"
    - "Remove deprecated field (after 6 months notice)"
    - "Expand enum values"

  prohibitedChanges:
    - "Remove required field"
    - "Change field type"
    - "Rename field"
    - "Remove enum value"

  deprecationPolicy:
    noticePerio: "6 months"
    communicationChannels:
      - "Email to downstream consumers"
      - "Data catalog annotation"
      - "Slack announcement"

# Documentation
documentation:
  businessGlossary:
    - term: "customer_id"
      definition: "Unique identifier for a customer in the CRM system"
      businessOwner: "Product Team"

    - term: "event_type"
      definition: "Category of user interaction tracked for analytics"
      businessOwner: "Analytics Team"

  usageExamples:
    - title: "Get events for specific customer"
      query: |
        SELECT *
        FROM analytics.production.customer_events
        WHERE customer_id = 'CUST-12345'
          AND _partition_date >= CURRENT_DATE - 7

    - title: "Count events by type"
      query: |
        SELECT event_type, COUNT(*) AS event_count
        FROM analytics.production.customer_events
        WHERE _partition_date = CURRENT_DATE
        GROUP BY event_type

# Change History
changeHistory:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    author: "Data Product Owner"
    changes: "Initial data contract"
    breaking: false

# Approvals
approvals:
  - role: "Data Product Owner"
    name: ""
    date: null
    status: "Pending"

  - role: "Data Governance Lead"
    name: ""
    date: null
    status: "Pending"

  - role: "Downstream Consumer Representative"
    name: ""
    date: null
    status: "Pending"
"""

    def generate_generic_yaml(self, data: Dict) -> str:
        """Generate a generic well-structured YAML template."""
        artifact_name = data['artifact_name']
        title = artifact_name.replace('-', ' ').title()

        lines = [
            f"# {title}",
            f"# See also: artifact_descriptions/{artifact_name}.md for complete guidance",
            "",
        ]

        if data['executive_summary']:
            summary = data['executive_summary'][:200]
            lines.append(f"# {summary}...")
            lines.append("")

        lines.extend([
            "metadata:",
            "  version: \"1.0.0\"",
            "  created: \"YYYY-MM-DD\"",
            "  lastModified: \"YYYY-MM-DD\"",
            "  status: \"Draft\"",
            "  author: \"Author Name\"",
            "  documentOwner: \"Owner Name/Role\"",
            "  classification: \"Internal\"",
            "",
            "  approvers:",
            "    - name: \"Approver Name\"",
            "      role: \"Approver Role\"",
            "      date: null",
            "",
        ])

        if data['purpose']:
            lines.append("# PURPOSE")
            purpose = data['purpose'][:300].replace('\n', ' ')
            lines.append(f"# {purpose}")
            lines.append("")

        if data['best_practices']:
            lines.append("# BEST PRACTICES")
            for title, desc in data['best_practices'][:5]:
                lines.append(f"# - {title}: {desc[:100]}")
            lines.append("")

        lines.extend([
            "# Main content - customize based on artifact type",
            "content:",
            "  summary: |",
            "    Provide overview and context for this artifact.",
            "  ",
        ])

        if data['scope_in']:
            lines.extend([
                "  scope:",
                "    included:",
            ])
            for item in data['scope_in'][:3]:
                clean_item = item.split(':')[0][:80]
                lines.append(f"      - \"{clean_item}\"")
            lines.extend([
                "    ",
                "    excluded:",
                "      - \"Items explicitly out of scope\"",
                "  ",
            ])

        lines.extend([
            "# Related artifacts",
            "relatedArtifacts:",
            "  - type: \"Related Artifact Type\"",
            "    path: \"path/to/artifact\"",
            "    relationship: \"depends-on | references | implements\"",
            "",
            "# Change history",
            "changeHistory:",
            "  - version: \"1.0.0\"",
            "    date: \"YYYY-MM-DD\"",
            "    author: \"Author Name\"",
            "    changes: \"Initial version\"",
        ])

        return '\n'.join(lines) + '\n'

    def generate_generic_markdown(self, data: Dict) -> str:
        """Generate a generic well-structured Markdown template."""
        artifact_name = data['artifact_name']
        title = artifact_name.replace('-', ' ').title()

        lines = [
            f"# {title}",
            "",
            f"> **See also**: `artifact_descriptions/{artifact_name}.md` for complete guidance",
            "",
            "## Document Control",
            "",
            "| Field | Value |",
            "|-------|-------|",
            "| **Version** | 1.0.0 |",
            "| **Status** | Draft |",
            "| **Created** | YYYY-MM-DD |",
            "| **Last Updated** | YYYY-MM-DD |",
            "| **Author** | Author Name |",
            "| **Owner** | Owner Name/Role |",
            "| **Classification** | Internal |",
            "",
        ]

        if data['executive_summary']:
            lines.extend([
                "## Executive Summary",
                "",
                data['executive_summary'],
                "",
            ])

        if data['purpose']:
            lines.extend([
                "## Purpose",
                "",
                data['purpose'][:400],
                "",
            ])

        if data['scope_in']:
            lines.extend([
                "## Scope",
                "",
                "### In Scope",
                "",
            ])
            for item in data['scope_in'][:5]:
                clean_item = item.split(':')[0]
                lines.append(f"- {clean_item}")
            lines.extend([
                "",
                "### Out of Scope",
                "",
                "- Items explicitly not covered",
                "",
            ])

        lines.extend([
            "## Main Content",
            "",
            "<!-- Provide detailed content specific to this artifact type -->",
            "<!-- Refer to the artifact description for required sections -->",
            "",
        ])

        if data['best_practices']:
            lines.extend([
                "## Best Practices",
                "",
            ])
            for title, desc in data['best_practices'][:8]:
                lines.append(f"**{title}**: {desc}")
                lines.append("")

        lines.extend([
            "## Related Documents",
            "",
            "- [Related Artifact]: Relationship description",
            "",
            "## Approvals",
            "",
            "| Role | Name | Date | Status |",
            "|------|------|------|--------|",
            "| Approver | | YYYY-MM-DD | Pending |",
            "",
            "---",
            "",
            "## Document History",
            "",
            "| Version | Date | Author | Changes |",
            "|---------|------|--------|---------|",
            "| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |",
        ])

        return '\n'.join(lines) + '\n'

    def generate_template(self, data: Dict, is_yaml: bool) -> str:
        """Generate appropriate template based on artifact type."""
        artifact_name = data['artifact_name']

        # Use specialized templates for key artifacts
        if artifact_name == 'threat-model' and is_yaml:
            return self.generate_threat_model_yaml(data)
        elif artifact_name == 'api-versioning-policy' and not is_yaml:
            return self.generate_api_versioning_policy_md(data)
        elif 'data-contract' in artifact_name and is_yaml:
            return self.generate_data_contract_yaml(data)
        # Add more specialized templates here as needed

        # Fall back to generic templates
        if is_yaml:
            return self.generate_generic_yaml(data)
        else:
            return self.generate_generic_markdown(data)

    def rewrite_template(self, desc_path: Path) -> bool:
        """Rewrite a single template."""
        try:
            data = self.parse_description(desc_path)
            artifact_name = data['artifact_name']

            print(f"Processing: {artifact_name}")

            template_path = self.find_template_path(artifact_name)
            if not template_path:
                print(f"  ⚠ Template not found for {artifact_name}")
                self.stats['errors'].append(f"Template not found: {artifact_name}")
                return False

            is_yaml = template_path.suffix == '.yaml'
            new_content = self.generate_template(data, is_yaml)

            with open(template_path, 'w') as f:
                f.write(new_content)

            print(f"  ✓ Rewrote {template_path.relative_to(self.base_dir)}")
            self.stats['templates_rewritten'] += 1
            return True

        except Exception as e:
            error_msg = f"Error processing {desc_path.name}: {str(e)}"
            print(f"  ✗ {error_msg}")
            self.stats['errors'].append(error_msg)
            return False

    def rewrite_all(self):
        """Rewrite all templates."""
        desc_files = sorted(self.descriptions_dir.glob("*.md"))
        self.stats['total_descriptions'] = len(desc_files)

        print(f"Found {len(desc_files)} artifact descriptions")
        print("=" * 80)

        for desc_file in desc_files:
            self.rewrite_template(desc_file)

        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total descriptions: {self.stats['total_descriptions']}")
        print(f"Templates rewritten: {self.stats['templates_rewritten']}")
        print(f"Errors: {len(self.stats['errors'])}")

        if self.stats['errors']:
            print("\nErrors encountered:")
            for error in self.stats['errors'][:10]:
                print(f"  - {error}")

        return self.stats


def main():
    generator = IndustryTemplateGenerator()
    stats = generator.rewrite_all()
    exit(0 if not stats['errors'] else 1)


if __name__ == "__main__":
    main()
