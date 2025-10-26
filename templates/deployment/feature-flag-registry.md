# Feature Flag Registry

## Document Information

**Purpose**: Centralized catalog of feature flags for progressive delivery, A/B testing, kill switches, and operational toggles to decouple deployment from release and enable instant rollback without redeployment.

**Format**: Markdown with feature flag definitions and examples

**Target Audience**: Product Managers, Engineering Teams, SRE Teams, QA Engineers, Operations Teams

**Related Artifacts**:
- CI/CD Pipeline Definitions
- Deployment Plan
- Release Plan
- Canary Deployment Configurations

---

## Metadata

```yaml
version: "2.1.0"
created: "2024-01-08"
lastModified: "2024-01-24"
status: "Active"
documentOwner: "Product Engineering Team"
classification: "Internal"
```

---

## 1. Feature Flag Strategy

### 1.1 Flag Types

| Type | Purpose | Lifetime | Control | Example |
|------|---------|----------|---------|---------|
| **Release Flags** | Gate new features | Temporary (weeks) | Product/Engineering | `new-checkout-flow` |
| **Experiment Flags** | A/B testing | Temporary (days-weeks) | Product/Data Science | `recommendation-algorithm-v2` |
| **Ops Flags** | Circuit breakers, kill switches | Permanent | Operations/SRE | `disable-recommendations` |
| **Permission Flags** | Access control | Long-lived | Product/Engineering | `beta-features-access` |

### 1.2 Flag Lifecycle

```
Draft → Review → Active → Completed → Archived
```

**Lifecycle Stages**:
1. **Draft**: Flag created, not yet in production
2. **Review**: Under review by stakeholders
3. **Active**: Live in production, actively used
4. **Completed**: Rollout complete (100%), ready for removal
5. **Archived**: Removed from code, historical record

---

## 2. Feature Flag Platforms

### 2.1 LaunchDarkly

**Primary platform for production feature flags**

```javascript
// Initialize LaunchDarkly SDK
import LaunchDarkly from 'launchdarkly-node-server-sdk';

const ldClient = LaunchDarkly.init(process.env.LAUNCHDARKLY_SDK_KEY);

await ldClient.waitForInitialization();

// Evaluate flag for user
const user = {
  key: 'user-123',
  email: 'user@example.com',
  custom: {
    plan: 'enterprise',
    region: 'us-east-1'
  }
};

const showNewCheckout = await ldClient.variation(
  'new-checkout-flow',
  user,
  false  // default value
);

if (showNewCheckout) {
  // New checkout experience
} else {
  // Legacy checkout
}
```

### 2.2 Progressive Delivery Example

```javascript
// Deploy code to production with flag OFF
// Gradually enable for users

// Day 1: Internal employees (1%)
// Day 3: Beta users (5%)
// Day 5: Random 10%
// Day 7: Random 25%
// Day 10: Random 50%
// Day 14: All users (100%)

const newFeatureEnabled = await ldClient.variation(
  'new-payment-flow',
  user,
  false
);

if (newFeatureEnabled) {
  return await newPaymentFlow(order);
} else {
  return await legacyPaymentFlow(order);
}
```

---

## 3. Active Feature Flags

### 3.1 Release Flags

#### New Checkout Flow

```yaml
flag:
  key: new-checkout-flow
  name: "New Checkout Flow"
  type: release
  status: active
  created: "2024-01-15"
  owner: "checkout-team@company.com"

  description: |
    Next-generation checkout experience with one-click purchasing,
    multiple payment methods, and improved mobile UX.

  targeting:
    rules:
      - name: "Internal employees"
        percentage: 100
        conditions:
          - attribute: email
            operator: ends_with
            value: "@company.com"

      - name: "Beta users"
        percentage: 100
        conditions:
          - attribute: beta_tester
            operator: equals
            value: true

      - name: "Gradual rollout"
        percentage: 25  # 25% of remaining users
        conditions: []

  metrics:
    - conversion_rate
    - average_order_value
    - checkout_abandonment_rate
    - time_to_checkout

  rolloutPlan:
    - date: "2024-01-20"
      percentage: 10
      notes: "Initial rollout to low-risk users"

    - date: "2024-01-27"
      percentage: 25
      notes: "Expand if metrics look good"

    - date: "2024-02-03"
      percentage: 50
      notes: "Half of users"

    - date: "2024-02-10"
      percentage: 100
      notes: "Complete rollout"

  rollbackPlan:
    trigger: "conversion_rate < baseline - 5%"
    action: "Immediate rollback to 0%"
    owner: "checkout-team@company.com"
```

---

### 3.2 Operational Flags (Kill Switches)

#### Disable Recommendations

```yaml
operationalFlag:
  key: disable-recommendations
  name: "Kill Switch: Recommendations Service"
  type: operational
  status: active
  lifetime: permanent
  created: "2023-09-01"
  owner: "sre-team@company.com"

  description: |
    Emergency kill switch to disable recommendations service if it's
    causing performance issues or errors. Circuit breaker for core
    shopping experience.

  defaultValue: false  # Enabled by default

  useCase: |
    - Recommendations service experiencing high latency
    - Third-party ML API unavailable
    - Database overload from recommendation queries
    - Emergency cost reduction

  fallback: "Show static popular products list"

  monitoring:
    alerts:
      - name: "Recommendations disabled"
        severity: warning
        channel: slack-ops
```

---

## 4. Best Practices

### 4.1 Naming Conventions

```
{team}-{feature}-{version}
├── checkout-flow-v3
├── recommendations-ml-v2
└── search-elasticsearch-migration
```

### 4.2 Default Values

Always provide safe defaults:

```javascript
// GOOD: Safe default
const useNewAPI = flags.get('new-api', false);

// BAD: No default (breaks if flag service down)
const useNewAPI = flags.get('new-api');
```

### 4.3 Flag Cleanup

```markdown
1. Verify flag at 100% for 30+ days
2. Create PR to remove flag
3. Replace flag checks with new code
4. Remove old code path
5. Deploy to production
6. Archive flag in platform
```

---

## 5. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.1.0 | 2024-01-24 | Product Team | Added experiment flags, progressive delivery workflows |
| 2.0.0 | 2024-01-15 | Engineering | Migrated to LaunchDarkly, added kill switches |
| 1.0.0 | 2023-09-01 | DevOps Team | Initial feature flag registry |

---

## 6. Related Documentation

- [CI/CD Pipeline Definitions](./ci-cd-pipeline-definitions.md)
- [Deployment Plan](./deployment-plan.md)
- [Canary Deployment Guide](./canary-deployment.md)
- [LaunchDarkly Documentation](https://docs.launchdarkly.com)
