# Betty Framework Governance Architecture

## Overview

Betty's governance layer provides enterprise-grade control, compliance, and observability for AI-assisted engineering workflows.

---

## Components

### 1. Policy Enforcement (`policy.enforce`)

**Purpose**: Validate skills, workflows, and operations against organizational policies before execution.

**Policy Types**:
- **Naming Policies**: Enforce skill naming conventions (e.g., `domain.action` format)
- **Permission Policies**: Control filesystem, network, and API access
- **Dependency Policies**: Restrict which skills can depend on others
- **Approval Policies**: Require human review for sensitive operations
- **Compliance Policies**: Enforce SOC2, ISO 27001, or custom standards

**Policy Definition Format** (YAML):
```yaml
policy:
  name: skill-naming-convention
  version: 1.0.0
  description: Enforce lowercase dot-separated naming
  type: validation
  rules:
    - field: name
      pattern: "^[a-z][a-z0-9]*\\.[a-z][a-z0-9]*$"
      message: "Skill names must be lowercase.dotted format"
  enforcement: blocking  # blocking | warning | audit
  scope: [skills]
```

**Policy Storage**: `/registry/policies/*.yaml`

**Enforcement Points**:
1. **Pre-creation**: Before `skill.create` generates files
2. **Pre-registration**: Before `registry.update` commits to registry
3. **Pre-execution**: Before `workflow.compose` runs workflows
4. **Continuous**: Periodic audit of existing skills

---

### 2. Telemetry & Observability (`telemetry.capture`)

**Purpose**: Collect runtime metrics, audit trails, and performance data for all Betty operations.

**Telemetry Events**:
- `skill.created` - New skill scaffolded
- `skill.validated` - Manifest validation completed
- `skill.registered` - Added to registry
- `workflow.started` - Workflow execution began
- `workflow.step.completed` - Individual step finished
- `workflow.completed` - Full workflow finished
- `policy.enforced` - Policy check performed
- `policy.violated` - Policy violation detected

**Event Schema**:
```json
{
  "event_type": "skill.created",
  "timestamp": "2025-10-23T00:00:00Z",
  "user": "engineer@riskexec.com",
  "session_id": "uuid",
  "skill_name": "data.transform",
  "context": {
    "tool": "claude-code",
    "version": "1.0.0"
  },
  "outcome": "success",
  "duration_ms": 245
}
```

**Storage**:
- Events: `/registry/telemetry/events.jsonl` (JSON Lines format)
- Metrics: `/registry/telemetry/metrics.json` (aggregated)
- Audit Trail: `/registry/audit_log.json` (compliance-focused)

**Integrations**:
- Export to Datadog, New Relic, Splunk
- Send to enterprise logging systems
- Trigger alerts on policy violations

---

### 3. Version Control & Registry Diff (`registry.diff`)

**Purpose**: Track changes to skills over time, enabling rollback and audit.

**Capabilities**:
- Compare registry versions
- Show skill manifest deltas
- Track who changed what and when
- Support semantic versioning (0.1.0 → 0.2.0)
- Enable rollback to previous versions

**Registry History Format**:
```json
{
  "version": "2025.10.23.001",
  "timestamp": "2025-10-23T00:15:30Z",
  "changes": [
    {
      "skill": "workflow.validate",
      "action": "updated",
      "field": "status",
      "old_value": "draft",
      "new_value": "active",
      "changed_by": "claude-agent"
    }
  ]
}
```

---

### 4. Approval Workflows

**Purpose**: Require human approval for sensitive operations before execution.

**Approval Gates**:
- Creating skills that access production systems
- Registering skills with elevated permissions
- Executing workflows that modify critical infrastructure
- Deploying skills to production environments

**Approval Process**:
1. Operation submitted to approval queue
2. Notification sent to approvers (Slack, email, etc.)
3. Approver reviews context and approves/rejects
4. Operation proceeds or is blocked based on decision

**Storage**: `/registry/approvals/*.json`

---

## Security Model

### Permission Levels

**Skills declare required permissions**:
```yaml
permissions:
  - filesystem.read
  - filesystem.write
  - network.http
  - secrets.read
```

**Policy enforces restrictions**:
- Skills cannot escalate permissions
- Network access requires explicit approval
- Secret access logged and audited
- File access limited to Betty workspace by default

### Audit Trail

Every operation creates immutable audit log entry:
```json
{
  "timestamp": "2025-10-23T00:00:00Z",
  "operation": "registry.update",
  "skill": "data.transform",
  "user": "engineer@riskexec.com",
  "ip_address": "10.0.1.42",
  "outcome": "success",
  "policy_checks": [
    {"policy": "naming-convention", "result": "pass"},
    {"policy": "permission-limits", "result": "pass"}
  ]
}
```

---

## Compliance Features

### SOC 2 Requirements
- ✅ Access controls (permission system)
- ✅ Change management (registry versioning)
- ✅ Audit logging (telemetry + audit trail)
- ✅ Monitoring (telemetry metrics)
- ✅ Incident response (policy violation alerts)

### ISO 27001 Requirements
- ✅ Information security controls (permission policies)
- ✅ Access management (approval workflows)
- ✅ Operations security (audit logging)
- ✅ Compliance monitoring (policy enforcement)

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
- Implement `policy.enforce` skill
- Create policy schema and parser
- Build basic policy engine

### Phase 2: Observability (Week 1-2)
- Implement `telemetry.capture` skill
- Create event collection system
- Build metrics aggregation

### Phase 3: Versioning (Week 2)
- Implement `registry.diff` skill
- Add version tracking to registry
- Build rollback mechanism

### Phase 4: Approval System (Week 3)
- Design approval workflow
- Implement approval queue
- Add notification system

### Phase 5: Integration (Week 3-4)
- Integrate governance into existing skills
- Add enforcement points
- Test end-to-end

---

## Usage Examples

### Enforcing Naming Policy
```bash
# Define policy
cat > registry/policies/naming.yaml <<EOF
policy:
  name: skill-naming-convention
  rules:
    - field: name
      pattern: "^[a-z][a-z0-9]*\\.[a-z][a-z0-9]*$"
EOF

# Enforce before creation
python skills/policy.enforce/policy_enforce.py --action create --skill-name "BadName"
# ❌ Policy violation: skill-naming-convention
#    Skill names must be lowercase.dotted format

python skills/policy.enforce/policy_enforce.py --action create --skill-name "data.transform"
# ✅ Policy check passed
```

### Capturing Telemetry
```bash
# Telemetry automatically captured by skills
python skills/skill.create/skill_create.py data.transform "Transform data"
# Creates skill + emits telemetry event

# View telemetry
python skills/telemetry.capture/telemetry_query.py --event-type skill.created --last 24h
```

### Viewing Registry Changes
```bash
# Show recent changes
python skills/registry.diff/registry_diff.py --compare HEAD~1 HEAD

# Output:
# Changed: workflow.validate
#   status: draft → active
# Added: workflow.compose
```

---

## Next Steps

1. Implement core governance skills
2. Integrate with existing Betty skills
3. Add policy templates for common use cases
4. Build observability dashboards
5. Document governance best practices
