# registry.diff

Compare current and previous versions of skills/agents and report differences.

## Overview

The `registry.diff` skill analyzes changes between a current manifest file (skill.yaml or agent.yaml) and its existing registry entry. It detects various types of changes, determines the required action, and provides suggestions for proper version management and breaking change prevention.

## Purpose

- **Version Control**: Ensure proper semantic versioning when updating skills/agents
- **Breaking Change Detection**: Identify changes that break backward compatibility
- **Permission Auditing**: Track permission changes and flag unauthorized modifications
- **Workflow Integration**: Enable automated validation in CI/CD pipelines

## Usage

```bash
# Compare a skill manifest against the registry
./skills/registry.diff/registry_diff.py path/to/skill.yaml

# Compare an agent manifest
./skills/registry.diff/registry_diff.py path/to/agent.yaml

# Using with betty command (if configured)
betty registry.diff <manifest_path>
```

## Input

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `manifest_path` | string | Yes | Path to skill.yaml or agent.yaml file to analyze |

## Output

The skill returns a JSON response with the following structure:

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "path": "path/to/manifest.yaml",
  "details": {
    "manifest_path": "path/to/manifest.yaml",
    "manifest_type": "skill",
    "diff_type": "version_bump",
    "required_action": "register",
    "suggestions": [
      "Version upgraded: 0.1.0 -> 0.2.0",
      "Clean version bump with no breaking changes"
    ],
    "details": {
      "name": "example.skill",
      "current_version": "0.2.0",
      "previous_version": "0.1.0",
      "version_comparison": "upgrade",
      "permission_changed": false,
      "added_permissions": [],
      "removed_permissions": [],
      "removed_fields": [],
      "status_changed": false,
      "current_status": "active",
      "previous_status": "active"
    },
    "timestamp": "2025-10-23T12:00:00+00:00"
  }
}
```

### Diff Types

| Type | Description |
|------|-------------|
| `new` | Entry does not exist in registry (first-time registration) |
| `version_bump` | Version was properly incremented |
| `version_downgrade` | Version was decreased (breaking change) |
| `permission_change` | Permissions were added or removed |
| `breaking_change` | Breaking changes detected (removed fields, etc.) |
| `status_change` | Status field changed (active, deprecated, etc.) |
| `needs_version_bump` | Changes detected without version increment |
| `no_change` | No significant changes detected |

### Required Actions

| Action | Description | Exit Code |
|--------|-------------|-----------|
| `register` | Changes are acceptable, proceed with registration | 0 |
| `review` | Manual review recommended before registration | 0 |
| `reject` | Breaking/unauthorized changes, registration blocked | 1 |
| `skip` | No changes detected, no action needed | 0 |

## Examples

### Example 1: New Skill Registration

```bash
$ ./skills/registry.diff/registry_diff.py skills/new.skill/skill.yaml
```

Output:
```json
{
  "ok": true,
  "status": "success",
  "details": {
    "diff_type": "new",
    "required_action": "register",
    "suggestions": [
      "New skill 'new.skill' ready for registration"
    ]
  }
}
```

### Example 2: Clean Version Bump

```bash
$ ./skills/registry.diff/registry_diff.py skills/example.skill/skill.yaml
```

Output:
```json
{
  "ok": true,
  "status": "success",
  "details": {
    "diff_type": "version_bump",
    "required_action": "register",
    "suggestions": [
      "Version upgraded: 0.1.0 -> 0.2.0",
      "Clean version bump with no breaking changes"
    ]
  }
}
```

### Example 3: Breaking Change Detected

```bash
$ ./skills/registry.diff/registry_diff.py skills/example.skill/skill.yaml
```

Output:
```json
{
  "ok": false,
  "status": "failed",
  "errors": [
    "Fields removed without version bump: dependencies",
    "Removing fields requires a version bump",
    "Suggested version: 0.2.0"
  ],
  "details": {
    "diff_type": "breaking_change",
    "required_action": "reject",
    "details": {
      "removed_fields": ["dependencies"],
      "current_version": "0.1.0",
      "previous_version": "0.1.0"
    }
  }
}
```
Exit code: 1

### Example 4: Permission Change

```bash
$ ./skills/registry.diff/registry_diff.py skills/example.skill/skill.yaml
```

Output:
```json
{
  "ok": true,
  "status": "success",
  "details": {
    "diff_type": "permission_change",
    "required_action": "review",
    "suggestions": [
      "New permissions added: network",
      "Review: Ensure new permissions are necessary and documented"
    ],
    "details": {
      "added_permissions": ["network"],
      "removed_permissions": []
    }
  }
}
```

### Example 5: Version Downgrade (Rejected)

```bash
$ ./skills/registry.diff/registry_diff.py skills/example.skill/skill.yaml
```

Output:
```json
{
  "ok": false,
  "status": "failed",
  "errors": [
    "Version downgrade detected: 0.2.0 -> 0.1.0",
    "Version downgrades are not permitted",
    "Suggested action: Restore version to at least 0.2.0"
  ],
  "details": {
    "diff_type": "version_downgrade",
    "required_action": "reject"
  }
}
```
Exit code: 1

## Exit Codes

- **0**: Success - Changes are acceptable or no changes detected
- **1**: Failure - Breaking or unauthorized changes detected

## Workflow Integration

### Pre-Commit Hook

```yaml
# .git/hooks/pre-commit
#!/bin/bash
changed_files=$(git diff --cached --name-only | grep -E "skill\.yaml|agent\.yaml")

for file in $changed_files; do
  echo "Checking $file..."
  ./skills/registry.diff/registry_diff.py "$file"
  if [ $? -ne 0 ]; then
    echo "❌ Registry diff failed for $file"
    exit 1
  fi
done
```

### CI/CD Pipeline

```yaml
# .github/workflows/validate-changes.yml
name: Validate Skill Changes

on: [pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Check skill changes
        run: |
          for file in $(git diff --name-only origin/main | grep -E "skill\.yaml|agent\.yaml"); do
            python3 skills/registry.diff/registry_diff.py "$file"
          done
```

## Change Detection Rules

### Breaking Changes (Exit 1)

1. **Version Downgrade**: Current version < Previous version
2. **Removed Fields**: Fields removed without version bump
3. **Removed Permissions**: Permissions removed without version bump

### Requires Review (Exit 0, but flagged)

1. **Permission Addition**: New permissions added
2. **Status Change**: Status changed to deprecated/archived
3. **Needs Version Bump**: Changes without version increment

### Acceptable Changes (Exit 0)

1. **New Entry**: First-time registration
2. **Clean Version Bump**: Version incremented properly
3. **No Changes**: No significant changes detected

## Semantic Versioning Guidelines

The skill follows semantic versioning principles:

- **Major (X.0.0)**: Breaking changes, removed functionality
- **Minor (0.X.0)**: New features, deprecated functionality, significant changes
- **Patch (0.0.X)**: Bug fixes, documentation updates, minor tweaks

### Suggested Version Bumps

| Change Type | Suggested Bump |
|-------------|----------------|
| Remove fields | Minor |
| Remove permissions | Minor |
| Add permissions | Patch or Minor |
| Status to deprecated | Minor |
| Bug fixes | Patch |
| New features | Minor |
| Breaking changes | Major |

## Dependencies

- Python 3.6+
- `packaging` library (for version comparison)
- Betty Framework core utilities
- PyYAML

## Related Skills

- `registry.update`: Update registry entries
- `skill.define`: Define and validate skill manifests
- `audit.log`: Audit trail for registry changes

## Notes

- Automatically detects whether input is a skill or agent manifest
- Compares against appropriate registry (skills.json or agents.json)
- Provides human-readable output to stderr for CLI usage
- Returns structured JSON for programmatic integration
- Thread-safe registry reading using Betty Framework utilities

## Troubleshooting

### "Manifest file not found"

Ensure the path to the manifest file is correct and the file exists.

### "Empty manifest file"

The YAML file exists but contains no data. Check for valid YAML content.

### "Registry file not found"

The registry hasn't been initialized yet. This is normal for new Betty Framework installations.

### "Invalid YAML in manifest"

The manifest file contains syntax errors. Validate with a YAML parser.

## Future Enhancements

- [ ] Support for dependency tree validation
- [ ] Integration with semantic version recommendation engine
- [ ] Diff visualization in HTML format
- [ ] Support for comparing arbitrary versions (not just latest)
- [ ] Batch mode for comparing multiple manifests
