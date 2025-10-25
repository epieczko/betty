# Betty Traceability System

Complete audit trail linking requirements to verification results for compliance and quality assurance.

## Overview

The Betty Traceability System provides full lifecycle tracking for all components, recording:
- **Requirement Linkage**: What requirement led to creation
- **Creation Metadata**: Who/what created it, when, from what input
- **Verification Results**: All validation and testing performed

All records are stored as JSON files in `.betty-traces/` for easy loading into document databases (MongoDB, CouchDB, etc.).

## Quick Start

### Create Component with Traceability

```bash
# Create agent with requirement linkage
python3 agents/atum/atum.py examples/agents/code_reviewer_agent.md \
  --requirement-id "REQ-2025-001" \
  --requirement-description "Automated code review for security" \
  --issue-id "JIRA-123" \
  --requested-by "security-team@example.com" \
  --rationale "Reduce manual review time"

# Output includes trace ID:
# 📝 Traceability: trace-20251025-code.reviewer

# Create skill with requirement linkage
python3 agents/meta.skill/meta_skill.py examples/skills/file_compare_skill.md \
  --requirement-id "REQ-2025-002" \
  --requirement-description "File comparison for change detection" \
  --issue-id "JIRA-124" \
  --requested-by "dev-team@example.com" \
  --rationale "Enable automated file diff analysis"

# Output includes trace ID:
# 📝 Traceability: trace-20251025-file.compare

# Create hook with requirement linkage
python3 agents/meta.hook/meta_hook.py examples/hooks/pre_commit_lint_hook.md \
  --requirement-id "REQ-2025-003" \
  --requirement-description "Pre-commit code quality checks" \
  --issue-id "JIRA-125" \
  --requested-by "qa-team@example.com" \
  --rationale "Enforce code quality standards before commits"

# Output includes trace ID:
# 📝 Traceability: trace-20251025-hook.pre_commit_lint
```

### View Traceability Record

```bash
# View complete audit trail
python3 betty/trace_cli.py show code.reviewer
```

Output:
```
======================================================================
Traceability Record: trace-20251025-code.reviewer
======================================================================

Component:  Code Reviewer (agent)
ID:         code.reviewer
Version:    0.1.0
Location:   agents/code.reviewer/agent.yaml

──────────────────────────────────────────────────────────────────────
CREATION
──────────────────────────────────────────────────────────────────────
Created:    2025-10-25 02:24:18 UTC
By:         meta.agent v0.1.0
From:       examples/agents/code_reviewer_agent.md
Hash:       sha256:183ab...
Betty:      v1.0.0

──────────────────────────────────────────────────────────────────────
REQUIREMENT
──────────────────────────────────────────────────────────────────────
ID:          REQ-2025-001
Description: Automated code review for security
Issue:       JIRA-123
Requested:   security-team@example.com
Rationale:   Reduce manual review time

──────────────────────────────────────────────────────────────────────
VERIFICATION
──────────────────────────────────────────────────────────────────────
Status:      PASSED
Total Checks: 1
  ✅ Passed:   1
  ❌ Failed:   0
  ⚠️  Warnings: 0

Verification Checks:
  1. validation - ✅ PASSED
     Tool:      meta.agent
     Timestamp: 2025-10-25 02:24:18 UTC
     Details:
       - ✅ agent_structure
       - ✅ artifact_metadata
       - ✅ skills_compatibility
```

## CLI Commands

### View Trace

```bash
# View specific component trace
python3 betty/trace_cli.py show COMPONENT_ID

# View as JSON
python3 betty/trace_cli.py --format json show COMPONENT_ID
```

### List All Traces

```bash
# List all traceability records
python3 betty/trace_cli.py list

# List as JSON
python3 betty/trace_cli.py --format json list
```

### Search by Requirement

```bash
# Find all components for a requirement
python3 betty/trace_cli.py requirement REQ-2025-001

# Search as JSON
python3 betty/trace_cli.py --format json requirement REQ-2025-001
```

### Export for Database

```bash
# Export all traces to JSON file
python3 betty/trace_cli.py export traces.json

# Load into MongoDB
mongoimport --db betty --collection traces --file traces.json --jsonArray

# Load into CouchDB
curl -X POST http://localhost:5984/betty/_bulk_docs \
  -H 'Content-Type: application/json' \
  -d @traces.json
```

## Requirement Fields

### Required

- **requirement_id**: Unique requirement identifier (e.g., "REQ-2025-001")
- **requirement_description**: What this component accomplishes

### Optional

- **requirement_source**: Source document (e.g., "requirements/Q1-2025.md")
- **issue_id**: Issue tracking ID (e.g., "JIRA-123", "BETTY-456")
- **requested_by**: Who requested (e.g., "security-team@example.com")
- **rationale**: Why this is needed

## Verification Tracking

The traceability system automatically logs verification checks:

### Automatic Checks

When components are created, these checks are automatically logged:

1. **Validation**: Structure and standards compliance
2. **Compatibility**: Artifact metadata consistency
3. **Skills Compatibility**: For agents, number of compatible skills found

### Check Types

- **validation**: Standards validation
- **compatibility**: Agent/skill compatibility
- **integration_test**: Integration test results
- **unit_test**: Unit test results
- **security_scan**: Security scanning results
- **manual_review**: Manual review sign-off

### Adding Custom Verification

```python
from betty.traceability import get_tracer

tracer = get_tracer()

# Log integration test results
tracer.log_verification(
    component_id="code.reviewer",
    check_type="integration_test",
    tool="pytest",
    result="passed",
    details={
        "tests_run": 12,
        "tests_passed": 12,
        "tests_failed": 0,
        "coverage": "85%"
    },
    evidence_data=test_output_logs  # Optional: save detailed logs
)
```

## Data Storage

### Directory Structure

```
.betty-traces/
├── trace-20251025-code.reviewer.json    # Traceability record
├── trace-20251025-api.validator.json
├── trace-20251026-data.transform.json
└── evidence/                              # Detailed verification logs
    ├── trace-20251025-code.reviewer-validation.log
    ├── trace-20251025-code.reviewer-integration_test.log
    └── ...
```

### Record Format

Each trace is a JSON file with this structure:

```json
{
  "trace_id": "trace-20251025-code.reviewer",
  "component": {
    "id": "code.reviewer",
    "name": "Code Reviewer",
    "type": "agent",
    "version": "0.1.0",
    "file_path": "agents/code.reviewer/agent.yaml"
  },
  "creation": {
    "timestamp": "2025-10-25T02:24:18Z",
    "created_by": {
      "tool": "meta.agent",
      "version": "0.1.0"
    },
    "input_source": {
      "path": "examples/agents/code_reviewer_agent.md",
      "hash": "sha256:183ab..."
    },
    "betty_version": "1.0.0"
  },
  "requirement": {
    "id": "REQ-2025-001",
    "description": "Automated code review for security",
    "issue_id": "JIRA-123",
    "requested_by": "security-team@example.com",
    "rationale": "Reduce manual review time"
  },
  "verification": {
    "status": "passed",
    "checks": [ /* verification checks */ ],
    "summary": {
      "total_checks": 3,
      "passed": 3,
      "failed": 0,
      "warnings": 0
    }
  },
  "metadata": {
    "tags": ["agent", "auto-generated"],
    "project": "Betty Framework"
  }
}
```

## Compliance Use Cases

### SOC2 Compliance

Track requirement → implementation → testing:

```bash
# Create component with SOC2 requirement
python3 agents/atum/atum.py security_agent.md \
  --requirement-id "SOC2-AC-2.1" \
  --requirement-description "Implement automated access control review" \
  --requirement-source "SOC2 Controls Matrix" \
  --rationale "SOC2 Trust Services Criteria compliance"

# Export audit trail
python3 betty/trace_cli.py export soc2-audit-trail.json
```

### ISO 27001 Compliance

Document security controls:

```bash
# Create security control
python3 agents/atum/atum.py access_monitor.md \
  --requirement-id "ISO-A.9.2.1" \
  --requirement-description "User access provisioning monitoring" \
  --requirement-source "ISO 27001:2013 Annex A" \
  --rationale "Ensure appropriate access rights"
```

### GDPR Compliance

Track data processing components:

```bash
# Create data handler
python3 agents/atum/atum.py data_anonymizer.md \
  --requirement-id "GDPR-Art25" \
  --requirement-description "Data protection by design" \
  --requirement-source "GDPR Article 25" \
  --rationale "Privacy by design and default"
```

### FDA 21 CFR Part 11

Electronic records and signatures:

```bash
# Create audit logging component
python3 agents/atum/atum.py audit_logger.md \
  --requirement-id "21CFR11-10" \
  --requirement-description "Audit trail for record changes" \
  --requirement-source "21 CFR Part 11.10" \
  --rationale "FDA electronic records compliance"
```

## Integration with CI/CD

### GitHub Actions

```yaml
# .github/workflows/traceability.yml
name: Traceability Check

on: [pull_request]

jobs:
  verify-traceability:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Check Component Traceability
        run: |
          # Verify all new components have traceability
          for agent in agents/*/agent.yaml; do
            agent_name=$(basename $(dirname $agent))
            if ! python3 betty/trace_cli.py show $agent_name > /dev/null 2>&1; then
              echo "❌ No traceability record for: $agent_name"
              exit 1
            fi
          done

      - name: Export Audit Trail
        run: |
          python3 betty/trace_cli.py export audit-trail.json

      - name: Upload Audit Trail
        uses: actions/upload-artifact@v2
        with:
          name: audit-trail
          path: audit-trail.json
```

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Ensure all components have traceability before commit
for agent in agents/*/agent.yaml; do
  agent_name=$(basename $(dirname $agent))

  if ! python3 betty/trace_cli.py show $agent_name > /dev/null 2>&1; then
    echo "❌ Missing traceability for: $agent_name"
    echo "   Create with: --requirement-id and --requirement-description"
    exit 1
  fi
done
```

## Querying Traces

### Python API

```python
from betty.traceability import get_tracer

tracer = get_tracer()

# Get specific trace
trace = tracer.get_trace("code.reviewer")
print(f"Requirement: {trace['requirement']['id']}")
print(f"Status: {trace['verification']['status']}")

# Search by requirement
traces = tracer.search_by_requirement("REQ-2025-001")
for trace in traces:
    print(f"{trace['component']['name']}: {trace['verification']['status']}")

# List all traces
all_traces = tracer.list_all_traces()
print(f"Total components: {len(all_traces)}")
```

### MongoDB Queries

After loading into MongoDB:

```javascript
// Find all components for a requirement
db.traces.find({ "requirement.id": "REQ-2025-001" })

// Find failed verifications
db.traces.find({ "verification.status": "failed" })

// Find components by team
db.traces.find({ "metadata.team": "Platform Engineering" })

// Compliance report
db.traces.aggregate([
  { $match: { "requirement.source": /SOC2/ } },
  { $group: {
      _id: "$verification.status",
      count: { $sum: 1 }
  }}
])
```

## Best Practices

### 1. Always Provide Requirements

```bash
# ✅ Good: Full requirement linkage
python3 agents/atum/atum.py agent.md \
  --requirement-id "REQ-2025-001" \
  --requirement-description "Clear description" \
  --issue-id "JIRA-123"

# ❌ Bad: No traceability
python3 agents/atum/atum.py agent.md
```

### 2. Use Descriptive Requirement IDs

```bash
# ✅ Good: Clear, traceable IDs
REQ-2025-001, SOC2-AC-2.1, GDPR-Art25

# ❌ Bad: Vague IDs
REQ-1, TODO, FIXME
```

### 3. Link to Issue Trackers

```bash
# Always include issue tracker IDs
--issue-id "JIRA-123"
--issue-id "GITHUB-456"
```

### 4. Regular Exports

```bash
# Export weekly for backup
python3 betty/trace_cli.py export traces-$(date +%Y%m%d).json

# Load into database for querying
mongoimport --db betty --collection traces --file traces-*.json --jsonArray
```

### 5. Verify Before Release

```bash
# Before release, ensure all components traced
python3 betty/trace_cli.py list | grep -q "pending" && echo "❌ Pending verifications!"

# Check requirement coverage
python3 betty/trace_cli.py list --format json | \
  jq '.[] | select(.requirement.id == null)' && echo "❌ Missing requirements!"
```

## Troubleshooting

### No Trace Found

```bash
$ python3 betty/trace_cli.py show my.component
❌ No traceability record found for: my.component

# Solution: Component was created without --requirement-id
# Re-create with requirement information
```

### Missing Evidence

Evidence files are optional and only created when `evidence_data` is provided to `log_verification()`.

### Export Fails

```bash
# Ensure .betty-traces directory exists
ls -la .betty-traces/

# Check permissions
chmod 755 .betty-traces
```

## Future Enhancements

Planned features:
- Automatic test result capture from pytest and other test frameworks
- Git commit linkage for change tracking
- Change history tracking across component versions
- Automated compliance report generation
- Web UI dashboard for viewing and searching traces
- Integration with CI/CD pipelines for automated verification

## Support

- **Schema**: See `schemas/traceability-record.json`
- **API**: See `betty/traceability.py`
- **CLI**: See `betty/trace_cli.py --help`

---

**Full audit trail from requirement to verification!**
