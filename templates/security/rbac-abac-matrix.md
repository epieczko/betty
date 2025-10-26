# RBAC/ABAC Authorization Matrix

**Document Version:** 3.2.0
**Last Updated:** 2024-10-26
**Owner:** Identity and Access Management Team
**Classification:** Confidential
**Status:** Active

## Document Control

| Field | Value |
|-------|-------|
| Document ID | RBAC-MATRIX-2024-001 |
| Last Review Date | 2024-10-15 |
| Next Review Date | 2024-11-15 |
| Total Roles | 28 |
| Total Resources | 45 |
| Access Model | Hybrid RBAC + ABAC |
| Approvers | CISO, IAM Director |

## Executive Summary

This RBAC/ABAC Authorization Matrix defines role-based and attribute-based access control policies across all organizational resources. The hybrid model combines traditional RBAC for predictable access patterns with ABAC for dynamic, context-aware authorization decisions based on user attributes, resource classifications, environmental conditions, and risk scores.

**Key Statistics:**
- 28 defined roles spanning administrative, engineering, data, and business functions
- 45+ protected resources including compute, storage, databases, applications
- Hybrid RBAC + ABAC model supporting Zero Trust principles
- Quarterly access certification for all privileged roles

---

## Access Control Models

### RBAC (Role-Based Access Control)

Access determined by assigned roles. Users inherit all permissions associated with their role(s).

**Benefits:**
- Simple to understand and manage
- Predictable access patterns
- Aligns with org structure

**Example:**
```
User: jane.doe@company.com
Roles: [Senior_Developer, API_Developer]
→ Inherits: Code commit, PR approval, API deployment (non-prod)
```

### ABAC (Attribute-Based Access Control)

Access determined dynamically by evaluating attributes:
- **User Attributes:** Department, clearance level, location, device posture
- **Resource Attributes:** Classification, owner, environment (prod/staging/dev)
- **Environmental Attributes:** Time of day, network location, risk score

**Benefits:**
- Fine-grained control
- Context-aware decisions
- Supports Zero Trust

**Example:**
```
IF user.security_clearance == "secret" AND
   resource.classification IN ["public", "internal", "confidential"] AND
   request.network == "corporate_vpn" AND
   request.time.hour BETWEEN 6 AND 22
THEN ALLOW READ, WRITE
```

---

## RBAC Role Definitions

### Administrative Roles

#### System Administrator

**Role ID:** ROLE-ADMIN-001
**Role Type:** Administrative

**Permissions:**

| Resource Category | Specific Access |
|-------------------|----------------|
| **Compute** | EC2: full access; VMs: full access; Containers: full access |
| **Storage** | S3: full access; Databases: create/read/update/delete/backup/restore |
| **Network** | VPCs, Security Groups, Load Balancers: full access; Firewalls: configure/read/update |
| **Identity** | Users: create/read/update/disable; Groups: full access; Service Accounts: full access |
| **Monitoring** | Logs: read/export/delete; Metrics: read/create dashboards; Alerts: full access |

**Constraints:**
- MFA required: Yes
- Session recording required: Yes
- Approval required for: Delete production resources, User creation
- Max session duration: 4 hours
- Allowed IP ranges: Corporate network + VPN only
- Time-based access: Business hours only for production changes

---

#### Security Administrator

**Role ID:** ROLE-ADMIN-002

**Permissions:**

| Resource Category | Specific Access |
|-------------------|----------------|
| **Security Tools** | SIEM: full access; IDS/IPS: configure; DLP: configure; EDR: investigate/remediate |
| **Identity** | Users: read/disable/force password reset; Groups: read/update membership; Roles: read/audit |
| **Compliance** | Audit logs: read/export/retain; Security policies: full access; Compliance reports: full access |
| **Network** | Security Groups: read/update; Firewall rules: full access; WAF rules: full access |

**Constraints:**
- MFA required: Yes
- Justification required for all actions: Yes
- All actions audited: Yes
- Max session duration: 8 hours

---

### Developer Roles

#### Senior Developer

**Role ID:** ROLE-DEV-001

**Permissions:**

| Resource | Allowed Actions |
|----------|----------------|
| **Code Repositories** | Read: All repos; Write: Team repos; Merge: Requires review; Create branch: Allowed; Delete branch: Feature branches only |
| **CI/CD** | View all pipelines; Trigger builds (non-prod); Deploy to dev/staging; Rollback dev/staging |
| **Cloud Resources** | EC2: read/start/stop; S3: read/write (non-prod); Databases: read/write (non-prod); Lambda: create/read/update/delete (non-prod) |
| **Monitoring** | Logs: read; Metrics: read/create dashboards; Traces: read |

**Constraints:**
- MFA required: Yes
- No production database write access
- Code review required: 2 approvers minimum
- Max session duration: 12 hours

---

#### Junior Developer

**Role ID:** ROLE-DEV-002

**Permissions:**

| Resource | Allowed Actions |
|----------|----------------|
| **Code Repositories** | Read: Team repos only; Write: Assigned repos; Merge: Requires senior review; Create branch: Feature branches only |
| **CI/CD** | View team pipelines; Trigger builds (development only) |
| **Cloud Resources** | EC2: read only; S3: read (non-prod); Databases: read (development only) |
| **Monitoring** | Logs: read (team services only) |

**Constraints:**
- Require mentor approval for: Production deployments, Infrastructure changes
- Max session duration: 8 hours

---

### Data Roles

#### Data Scientist

**Role ID:** ROLE-DATA-001

**Permissions:**

| Resource | Allowed Actions |
|----------|----------------|
| **Data Access** | Data Lake: read; Data Warehouse: read/create views; ML Platforms: full access |
| **Compute** | Jupyter notebooks: full access; ML training clusters: create/read/delete; GPU instances: request (budget limited) |
| **Storage** | Personal workspace: full access; Shared datasets: read; Model registry: read/write/version |

**Constraints:**
- PII data masked: Yes
- Data export restrictions: Anonymized only
- Cost limits: $500/month compute budget
- Data classification training required: Yes

---

## Permission Matrix (RBAC)

**Legend:**
- **R** = Read
- **W** = Write
- **D** = Delete
- **E** = Execute
- **A** = Admin
- **-** = No Access

### Compute Resources

| Resource | System Admin | DevOps Engineer | Senior Developer | Junior Developer | Security Analyst |
|----------|-------------|-----------------|------------------|------------------|------------------|
| **EC2 Production** | RWDEA | RWE | RE | R | R |
| **EC2 Staging** | RWDEA | RWDEA | RWDE | RE | R |
| **Kubernetes Prod** | RWDEA | RWE | R | - | R |
| **Kubernetes Non-Prod** | RWDEA | RWDEA | RWDE | RWE | R |

### Data Resources

| Resource | DB Admin | System Admin | Senior Dev | Data Engineer | Data Scientist | Junior Dev |
|----------|----------|--------------|------------|---------------|----------------|------------|
| **Production Database** | RWDEA | RA | R | R | R | - |
| **Staging Database** | RWDEA | RA | RWD | RWDE | R | RW |
| **Data Warehouse** | RWDEA | RA | R | RWDE | RW | - |
| **Data Lake** | RA | RA | - | RWDEA | RW | - |

### Security Resources

| Resource | Security Admin | Security Engineer | Security Analyst | Compliance Auditor | System Admin |
|----------|---------------|-------------------|------------------|-------------------|--------------|
| **SIEM Platform** | RWDEA | RWDE | RWE | R | R |
| **Vulnerability Scanner** | RWDEA | RWDE | RE | - | R |
| **Secret Vault** | RWDEA | RWDE | - | - | RE (limited) |
| **Audit Logs** | RWE | R | RE | RE | R |

### Application Resources

| Resource | DevOps Engineer | Senior Developer | Junior Developer | Product Manager |
|----------|----------------|------------------|------------------|-----------------|
| **Production Deployment** | E | E (with approval) | - | - |
| **Staging Deployment** | E | E | E (with approval) | - |
| **Feature Flags** | RWDE | RWE | - | RW (non-prod) |
| **API Keys** | RWDEA | RWE | RE | - |

---

## ABAC Policies

### Policy 1: Data Classification-Based Access

**Policy ID:** ABAC-001
**Description:** Access to data based on classification level and user clearance

**Rules:**

| Rule ID | Condition | Effect | Actions |
|---------|-----------|--------|---------|
| ABAC-001-R1 | user.security_clearance == "confidential" AND resource.classification == "public" | ALLOW | read |
| ABAC-001-R2 | user.security_clearance == "secret" AND resource.classification IN ["public", "internal", "confidential"] | ALLOW | read, write |
| ABAC-001-R3 | user.security_clearance == "top_secret" AND resource.classification IN ["public", "internal", "confidential", "secret"] | ALLOW | read, write, delete |

**Example:**
```json
{
  "user": {
    "id": "alice@company.com",
    "security_clearance": "secret"
  },
  "resource": {
    "id": "customer-pii-database",
    "classification": "confidential"
  },
  "action": "read",
  "result": "ALLOW"
}
```

---

### Policy 2: Time-Based Access Control

**Policy ID:** ABAC-002
**Description:** Restrict production access to business hours (with on-call exception)

**Rules:**

| Rule ID | Condition | Effect |
|---------|-----------|--------|
| ABAC-002-R1 | resource.environment == "production" AND request.time.hour BETWEEN 6 AND 22 AND request.time.day IN ["Mon", "Tue", "Wed", "Thu", "Fri"] | ALLOW |
| ABAC-002-R2 | resource.environment == "production" AND user.on_call_status == "active" | ALLOW (24/7) |
| ABAC-002-R3 | resource.environment IN ["staging", "development"] | ALLOW (24/7) |

---

### Policy 3: Location-Based Access

**Policy ID:** ABAC-003
**Description:** Restrict access based on geographic location and network

**Rules:**

| Rule ID | Condition | Effect | Note |
|---------|-----------|--------|------|
| ABAC-003-R1 | user.location.country IN ["US", "CA", "UK", "DE"] AND (request.network == "corporate_vpn" OR request.network == "office") | ALLOW | Approved countries + secure network |
| ABAC-003-R2 | user.location.country NOT IN ["US", "CA", "UK", "DE"] AND resource.contains_pii == true | DENY | GDPR/data residency compliance |

---

### Policy 4: Dynamic Data Masking

**Policy ID:** ABAC-004
**Description:** Mask PII based on user role and purpose

**Masking Rules:**

| Data Type | User Role Conditions | Masking Applied |
|-----------|---------------------|----------------|
| **Email** | User NOT IN ["compliance_auditor", "legal", "customer_support_manager"] | Hash (show domain only) |
| **SSN** | User NOT IN ["hr_manager", "payroll_admin"] | Mask except last 4 |
| **Phone** | User NOT IN ["customer_support", "sales"] | Mask except last 4 |
| **Credit Card** | User NOT IN ["payment_processor", "fraud_analyst"] | Mask all except last 4 |

**Example:**
```yaml
User: data_scientist@company.com
Access: customer_database
PII Masking Rules Applied:
  - email: "j***@example.com" (masked)
  - ssn: "***-**-1234" (last 4 visible)
  - phone: "***-***-5678" (last 4 visible)
  - credit_card: "************3456" (last 4 visible)
```

---

### Policy 5: Separation of Duties (SOD)

**Policy ID:** ABAC-005
**Description:** Enforce separation of duties for critical operations

**Rules:**

| Rule ID | Condition | Effect | Reason |
|---------|-----------|--------|--------|
| ABAC-005-R1 | resource.action == "approve_payment" AND resource.created_by == user.id | DENY | Users cannot approve their own payment requests |
| ABAC-005-R2 | resource.action == "deploy_production" AND user.id IN resource.code_authors | REQUIRE_ADDITIONAL_APPROVAL | Code authors cannot deploy their own code without peer approval |
| ABAC-005-R3 | resource.action == "security_audit" AND user.department == resource.audited_department | DENY | Cannot audit own department |

---

### Policy 6: Risk-Based Adaptive Access

**Policy ID:** ABAC-006
**Description:** Adjust access requirements based on calculated risk score

**Risk Scoring:**
- User risk score: Based on recent activity, failed logins, anomalous behavior
- Request risk score: Based on resource sensitivity, unusual time/location, action type

**Adaptive Controls:**

| Combined Risk Score | Effect | Additional Controls |
|-------------------|--------|---------------------|
| **< 30** (Low) | ALLOW | None |
| **30-70** (Medium) | ALLOW | Require step-up authentication (re-enter password or MFA) |
| **> 70** (High) | DENY | Trigger security review; user must contact security team |

**Example Scenario:**
```
User: john.doe@company.com
User Risk Score: 25 (low - normal behavior)
Resource: production_database
Resource Sensitivity: High
Request: Read customer PII
Time: 2:00 AM (unusual)
Location: New IP address (unusual)

Calculated Request Risk Score: 65 (medium)

Result: ALLOW with STEP_UP_AUTHENTICATION required
Action: User must re-authenticate with MFA before access granted
```

---

## Access Request Workflows

### Standard Access Request

**Resource Type:** Production Database

**Approval Chain:**
1. Database Administrator (required)
2. Security Administrator (required if access duration > 7 days)
3. CISO (required if access level includes write/delete)

**SLA:**
- Standard request: 2 business days
- Urgent request: 4 hours

**Requirements:**
- Business justification required
- Manager approval required
- MFA enrollment verified
- Security training completed within last 90 days

---

### Just-In-Time (JIT) Access

**Resource Type:** Production Systems

**Eligibility:**
- User has base role of DevOps Engineer or System Administrator
- Completed production access training
- Not on performance improvement plan or disciplinary action

**Activation Triggers:**
- On-call rotation
- Incident response
- Emergency change
- Approved maintenance window

**Duration:**
- Default: 4 hours
- Max: 12 hours
- Extension allowed: Yes (requires approval)

**Monitoring:**
- Session recording: Yes
- Real-time monitoring: Yes
- Automatic deactivation: Yes
- User notification: 15 minutes before expiration

---

## Privileged Access Management (PAM)

### Shared Account Management

**Root/Admin Accounts:**
- Check-out required: Yes
- Approval required: Yes
- Session recording: Yes
- Password rotation: After each use
- Max session duration: 2 hours

**Database Admin Accounts:**
- Check-out required: Yes
- Approval required: For production only
- Password rotation: Daily

**Service Accounts:**
- Programmatic access only: Yes
- Credential rotation: Every 90 days
- Usage monitoring: Yes

### Session Management

**Security Controls:**
- Recording enabled: Yes
- Recording retention: 7 years
- Real-time monitoring: Yes
- Suspicious command blocking: Yes

**Blocked Commands:**
```bash
rm -rf /
DROP DATABASE
DELETE FROM * WHERE 1=1
format c:
```

---

## Access Reviews & Certifications

### Review Schedule

| Review Type | Frequency | Scope | Reviewer | SLA |
|-------------|-----------|-------|----------|-----|
| **Manager Review** | Quarterly | Direct reports' access | People Managers | 5 business days |
| **Resource Owner Review** | Quarterly | Access to owned systems | System Owners | 5 business days |
| **Security Review** | Quarterly | High-risk access | Security Team | 3 business days |
| **Automatic Revocation** | After review deadline | Uncertified access | IAM System | 7-day grace period |

### Current Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Completion Rate | 100% | 98% | Yellow |
| Completion Time | 15 business days | 14 days | Green |
| Findings Remediated | 100% | 95% | Yellow |

---

## Compliance Mapping

### NIST 800-53

| Control | Description | Implementation |
|---------|-------------|----------------|
| **AC-2** | Account Management | Role definitions, approval workflows, access reviews |
| **AC-3** | Access Enforcement | RBAC/ABAC policies, permission matrix |
| **AC-5** | Separation of Duties | ABAC policy ABAC-005, approval workflows |
| **AC-6** | Least Privilege | Role-based permissions, JIT access |

### PCI-DSS

| Requirement | Description | Implementation |
|-------------|-------------|----------------|
| **7.1** | Limit access to system components and cardholder data | Role-based access control, permission matrix |
| **7.2** | Establish an access control system | RBAC/ABAC policies, access request workflows |

### GDPR

| Article | Description | Implementation |
|---------|-------------|----------------|
| **Article 32** | Security of processing | ABAC policies for PII, dynamic data masking |
| **Article 5** | Data minimization | Role-based data access, purpose-based access control |

---

## Integration with Identity Providers

### Primary IdP: Okta

- Protocol: SAML 2.0 / OIDC
- Sync frequency: Real-time
- Group sync: Enabled
- Role mapping: Automated

### Secondary IdP: Azure AD

- Protocol: SAML 2.0
- Use case: Microsoft 365 integration
- Sync frequency: Hourly

### Service Account Provider: HashiCorp Vault

- Credential types: API Keys, Certificates, Passwords
- Rotation policy: Automated 90-day rotation
- Dynamic secrets: Enabled for databases

---

## Change History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 3.2.0 | 2024-10-26 | Patricia Williams, IAM Director | Added ABAC risk-based adaptive access, JIT access for customer data, break glass procedures | Michael Zhang, CISO |
| 3.0.0 | 2024-07-01 | James Cooper, Security Architect | Major revision: Added ABAC policies, dynamic data masking, location/time-based controls | Michael Zhang, CISO |
| 2.0.0 | 2024-01-10 | Patricia Williams, IAM Director | Initial comprehensive RBAC matrix with 25 roles and 40 resources | CISO |

---

**Next Review Date:** 2024-11-15
**Review Frequency:** Monthly
**Document Owner:** IAM Director
**Compliance Frameworks:** NIST 800-53, PCI-DSS, GDPR, ISO 27001, Zero Trust Architecture
