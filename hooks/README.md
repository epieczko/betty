# Betty Framework Hooks

Hooks enable automated validation and policy enforcement across the Betty ecosystem.

## Available Hooks

### artifact.policy.validate

Automatically validates every AI-generated artifact against a named policy profile using `policy.enforce`.

**Trigger**: `artifact.generated`
**Status**: Active

**Purpose**: Ensures compliance scanning is applied post-generation before merge, deployment, or downstream reuse.

**Actions**:
1. Enforces policy using `policy.enforce` skill
2. Logs audit event with `audit.log`
3. Notifies humans if policy fails
4. Stops execution on policy violations

**Configuration**:
```yaml
trigger:
  event: artifact.generated
  conditions:
    artifact_type: any
    policy_profile: "default"
```

**Outputs**:
- `policy_status` - Overall validation status
- `violation_report` - Detailed violation report
- `audit_trace_id` - Audit trail identifier

## Hook Development

To create new hooks, use the `meta.hook` agent or `hook.define` skill.

## Related Documentation

- [Policy Profiles](../registry/policies/)
- [meta.policy.profile Agent](../agents/meta.policy.profile/)
- [Audit System](../registry/audit_log.json)
