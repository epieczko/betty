# docs.lint.links

## Overview

**docs.lint.links** validates Markdown links to detect broken internal or external links, with optional autofix mode to correct common issues.

## Purpose

This skill helps maintain documentation quality by:
- Scanning all `.md` files in a repository
- Detecting broken external links (404s and other HTTP errors)
- Detecting broken internal links (relative paths that don't resolve)
- Providing suggested fixes for common issues
- Automatically fixing case mismatches and `.md` extension issues

## Usage

### Basic Usage

```bash
python skills/docs.lint.links/docs_link_lint.py [root_dir] [options]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `root_dir` | string | No | `.` | Root directory to search for Markdown files |
| `--no-external` | boolean | No | false | Skip checking external links (faster) |
| `--autofix` | boolean | No | false | Automatically fix common issues (case mismatches, .md extension issues) |
| `--timeout` | integer | No | `10` | Timeout for external link checks in seconds |
| `--exclude` | string | No | - | Comma-separated list of patterns to exclude (e.g., 'node_modules,.git') |
| `--output` | string | No | `json` | Output format (json or text) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `lint_results` | object | JSON object containing link validation results with issues and statistics |
| `issues` | array | Array of link issues found, each with file, line, link, issue type, and suggested fix |
| `summary` | object | Summary statistics including files checked, issues found, and fixes applied |

## Usage Examples

### Example 1: Basic Link Validation

Check all markdown files in the current directory for broken links:

```bash
python skills/docs.lint.links/docs_link_lint.py
```

### Example 2: Skip External Link Checks

Check only internal links (much faster):

```bash
python skills/docs.lint.links/docs_link_lint.py --no-external
```

### Example 3: Auto-fix Common Issues

Automatically fix case mismatches and `.md` extension issues:

```bash
python skills/docs.lint.links/docs_link_lint.py --autofix
```

### Example 4: Check Specific Directory

Check markdown files in the `docs` directory:

```bash
python skills/docs.lint.links/docs_link_lint.py docs/
```

### Example 5: Exclude Patterns

Exclude certain directories from checking:

```bash
python skills/docs.lint.links/docs_link_lint.py --exclude "node_modules,vendor,.venv"
```

### Example 6: Text Output

Get human-readable text output instead of JSON:

```bash
python skills/docs.lint.links/docs_link_lint.py --output text
```

### Example 7: Custom Timeout

Use a longer timeout for external link checks:

```bash
python skills/docs.lint.links/docs_link_lint.py --timeout 30
```

## Output Format

### JSON Output (Default)

```json
{
  "status": "success",
  "summary": {
    "files_checked": 42,
    "files_with_issues": 3,
    "total_issues": 5,
    "autofix_enabled": false,
    "total_fixes_applied": 0
  },
  "issues": [
    {
      "file": "docs/api.md",
      "line": 15,
      "link": "../README.MD",
      "issue_type": "internal_broken",
      "message": "File not found: ../README.MD (found case mismatch: README.md)",
      "suggested_fix": "../README.md"
    },
    {
      "file": "docs/guide.md",
      "line": 23,
      "link": "https://example.com/missing",
      "issue_type": "external_broken",
      "message": "External link is broken: HTTP 404"
    }
  ]
}
```

### Text Output

```
Markdown Link Lint Results
==================================================
Files checked: 42
Files with issues: 3
Total issues: 5

Issues found:
--------------------------------------------------

docs/api.md:15
  Link: ../README.MD
  Issue: File not found: ../README.MD (found case mismatch: README.md)
  Suggested fix: ../README.md

docs/guide.md:23
  Link: https://example.com/missing
  Issue: External link is broken: HTTP 404
```

## Issue Types

### Internal Broken Links

These are relative file paths that don't resolve:

- **Case mismatches**: `README.MD` when file is `README.md`
- **Missing `.md` extension**: `guide` when file is `guide.md`
- **Extra `.md` extension**: `file.md` when file is `file`
- **File not found**: Path doesn't exist in the repository

### External Broken Links

These are HTTP/HTTPS URLs that return errors:

- **404 Not Found**: Page doesn't exist
- **403 Forbidden**: Access denied
- **500+ Server Errors**: Server-side issues
- **Timeout**: Server didn't respond in time
- **Network errors**: DNS failures, connection refused, etc.

## Autofix Behavior

When `--autofix` is enabled, the skill will automatically correct:

1. **Case mismatches**: If a link uses wrong case but a case-insensitive match exists
2. **Missing `.md` extension**: If a link is missing `.md` but the file exists with it
3. **Extra `.md` extension**: If a link has `.md` but the file exists without it

The autofix preserves:
- Anchor fragments (e.g., `#section`)
- Query parameters (e.g., `?version=1.0`)

**Note**: Autofix modifies files in place. It's recommended to use version control or create backups before using this option.

## Link Detection

The skill detects the following link formats:

1. **Standard markdown links**: `[text](url)`
2. **Angle bracket URLs**: `<https://example.com>`
3. **Reference-style links**: `[text][ref]` with `[ref]: url` definitions
4. **Implicit reference links**: `[text][]` using text as reference

## Excluded Patterns

By default, the following patterns are excluded from scanning:

- `.git/`
- `node_modules/`
- `.venv/` and `venv/`
- `__pycache__/`

Additional patterns can be excluded using the `--exclude` parameter.

## Integration Examples

### Use in CI/CD

Add to your CI pipeline to catch broken links:

```yaml
# .github/workflows/docs-lint.yml
name: Documentation Link Check

on: [push, pull_request]

jobs:
  lint-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check documentation links
        run: |
          python skills/docs.lint.links/docs_link_lint.py --no-external
```

### Use with Pre-commit Hook

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python skills/docs.lint.links/docs_link_lint.py --no-external --output text
if [ $? -ne 0 ]; then
  echo "Documentation has broken links. Please fix before committing."
  exit 1
fi
```

### Use in Documentation Workflow

```yaml
# workflows/documentation.yaml
steps:
  - skill: docs.lint.links
    args:
      - "docs/"
      - "--autofix"
  - skill: docs.lint.links
    args:
      - "docs/"
      - "--output=text"
```

## Performance Considerations

### External Link Checking

Checking external links can be slow because:
- Each link requires an HTTP request
- Some servers may rate-limit or block automated requests
- Network latency and timeouts add up

**Recommendations**:
- Use `--no-external` for fast local checks
- Use `--timeout` to adjust timeout for slow networks
- Run external checks less frequently (e.g., nightly builds)

### Large Repositories

For repositories with many markdown files:
- Use `--exclude` to skip irrelevant directories
- Consider checking specific subdirectories instead of the entire repo
- The skill automatically skips common directories like `node_modules`

## Error Handling

The skill returns:
- Exit code `0` if no broken links are found
- Exit code `1` if broken links are found or an error occurs

This makes it suitable for use in CI/CD pipelines and pre-commit hooks.

## Dependencies

_No external dependencies_

All functionality uses Python standard library modules:
- `re` - Regular expression matching for link extraction
- `urllib` - HTTP requests for external link checking
- `pathlib` - File system operations
- `json` - JSON output formatting

## Tags

`documentation`, `linting`, `validation`, `links`, `markdown`

## See Also

- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [Skills Framework](../../docs/skills-framework.md) - Betty skills framework
- [generate.docs](../generate.docs/SKILL.md) - Generate documentation from manifests

## Version

**0.1.0** - Initial implementation with link validation and autofix support
