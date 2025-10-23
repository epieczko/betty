# docs.expand.glossary

**Version**: 0.1.0
**Status**: active

## Overview

The `docs.expand.glossary` skill automatically discovers undocumented terms from Betty manifests and documentation, then enriches `glossary.md` with auto-generated definitions. This ensures comprehensive documentation coverage and helps maintain consistency across the Betty ecosystem.

## Purpose

- Extract field names and values from `skill.yaml` and `agent.yaml` manifests
- Scan markdown documentation for capitalized terms that may need definitions
- Identify gaps in the existing glossary
- Auto-generate definitions for common technical terms
- Update `glossary.md` with new entries organized alphabetically
- Emit JSON summary of changes for auditing

## Inputs

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `glossary_path` | string | No | `docs/glossary.md` | Path to the glossary file to expand |
| `base_dir` | string | No | Project root | Base directory to scan for manifests |
| `dry_run` | boolean | No | `false` | Preview changes without writing to file |
| `include_auto_generated` | boolean | No | `true` | Include auto-generated definitions |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| `summary` | object | Summary with counts, file paths, and operation metadata |
| `new_definitions` | object | Dictionary mapping new terms to their definitions |
| `manifest_terms` | object | Categorized terms extracted from manifests |
| `skipped_terms` | array | Terms that were skipped (already documented or too common) |

## What Gets Scanned

### Manifest Files

**skill.yaml fields:**
- `status` values (active, draft, deprecated, archived)
- `runtime` values (python, javascript, bash)
- `permissions` (filesystem:read, filesystem:write, network:http)
- Input/output `type` values
- `entrypoints` parameters

**agent.yaml fields:**
- `reasoning_mode` (iterative, oneshot)
- `status` values
- `capabilities`
- Error handling strategies (on_validation_failure, etc.)
- Timeout and retry configurations

### Documentation

- Scans all `docs/*.md` files for capitalized multi-word phrases
- Identifies technical terms that may need glossary entries
- Filters out common words and overly generic terms

## How It Works

1. **Load Existing Glossary**: Parses `glossary.md` to identify already-documented terms
2. **Scan Manifests**: Recursively walks `skills/` and `agents/` directories for YAML files
3. **Extract Terms**: Collects field names, values, and configuration options from manifests
4. **Scan Docs**: Looks for capitalized terms in markdown documentation
5. **Generate Definitions**: Creates concise, accurate definitions for common technical terms
6. **Update Glossary**: Inserts new terms alphabetically into appropriate sections
7. **Report**: Returns JSON summary with all changes and statistics

## Auto-Generated Definitions

The skill includes predefined definitions for common terms:

- **Status values**: active, draft, deprecated, archived
- **Runtimes**: python, javascript, bash
- **Permissions**: filesystem:read, filesystem:write, network:http
- **Reasoning modes**: iterative, oneshot
- **Types**: string, boolean, integer, object, array
- **Configuration**: max_retries, timeout_seconds, blocking, fuzzy
- **Modes**: dry_run, strict, overwrite

For unknown terms, the skill can generate contextual definitions based on category and usage patterns.

## Usage Examples

### Basic Usage

```bash
# Expand glossary with all undocumented terms
python glossary_expand.py

# Preview changes without writing
python glossary_expand.py --dry-run

# Use custom glossary location
python glossary_expand.py --glossary-path /path/to/glossary.md
```

### Programmatic Usage

```python
from skills.docs.expand.glossary.glossary_expand import expand_glossary

# Expand glossary
result = expand_glossary(
    glossary_path="docs/glossary.md",
    dry_run=False,
    include_auto_generated=True
)

# Check results
if result['ok']:
    summary = result['details']['summary']
    print(f"Added {summary['new_terms_count']} new terms")
    print(f"New terms: {summary['new_terms']}")
```

### Output Format

#### Summary Mode (Default)

```
================================================================================
GLOSSARY EXPANSION SUMMARY
================================================================================

Glossary: /home/user/betty/docs/glossary.md
Existing terms: 45
New terms added: 8
Scanned: 25 skills, 2 agents

--------------------------------------------------------------------------------
NEW TERMS:
--------------------------------------------------------------------------------

### Archived
A status indicating that a component has been retired and is no longer
maintained or available.

### Dry Run
A mode that previews an operation without actually executing it or making
changes.

### Handler
The script or function that implements the core logic of a skill or operation.

...

--------------------------------------------------------------------------------

Glossary updated successfully!

================================================================================
```

#### JSON Mode

```json
{
  "ok": true,
  "status": "success",
  "timestamp": "2025-10-23T19:54:00Z",
  "details": {
    "summary": {
      "glossary_path": "docs/glossary.md",
      "existing_terms_count": 45,
      "new_terms_count": 8,
      "new_terms": ["Archived", "Dry Run", "Handler", ...],
      "scanned_files": {
        "skills": 25,
        "agents": 2
      }
    },
    "new_definitions": {
      "Archived": "A status indicating...",
      "Dry Run": "A mode that previews...",
      ...
    },
    "manifest_terms": {
      "status": ["active", "draft", "deprecated", "archived"],
      "runtime": ["python", "bash"],
      "permissions": ["filesystem:read", "filesystem:write"]
    }
  }
}
```

## Integration

### With CI/CD

```yaml
# .github/workflows/docs-check.yml
- name: Check glossary completeness
  run: |
    python skills/docs.expand.glossary/glossary_expand.py --dry-run
    # Fail if new terms found
    if [ $? -eq 0 ]; then
      echo "Glossary is complete"
    else
      echo "Missing glossary terms - run skill to update"
      exit 1
    fi
```

### As a Hook

Can be integrated as a pre-commit hook to ensure glossary stays current:

```yaml
# .claude/hooks.yaml
- name: glossary-completeness-check
  event: on_commit
  command: python skills/docs.expand.glossary/glossary_expand.py --dry-run
  blocking: false
```

## Skipped Terms

The skill automatically skips:

- Terms already in the glossary
- Common words (name, version, description, etc.)
- Generic types (string, boolean, file, path, etc.)
- Single-character or overly generic terms

## Limitations

- Auto-generated definitions may need manual refinement for domain-specific terms
- Complex or nuanced terms may require human review
- Alphabetical insertion may need manual adjustment for optimal organization
- Does not detect duplicate or inconsistent definitions

## Future Enhancements

- Detect and flag duplicate definitions
- Identify outdated or inconsistent glossary entries
- Generate contextual definitions using LLM analysis
- Support for multi-language glossaries
- Integration with documentation linting tools

## Dependencies

- `context.schema` - For validating manifest structure

## Tags

`documentation`, `glossary`, `automation`, `analysis`, `manifests`

## Related Skills

- `generate.docs` - Generate SKILL.md documentation from manifests
- `registry.query` - Query registries for specific terms and metadata
- `skill.define` - Define and register new skills

## See Also

- [Glossary](../../docs/glossary.md) - The Betty Framework glossary
- [Contributing](../../docs/contributing.md) - Documentation contribution guidelines
- [Developer Guide](../../docs/developer-guide.md) - Building and extending Betty
