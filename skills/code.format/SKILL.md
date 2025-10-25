# code.format

Format code using Prettier, supporting multiple languages and file types. This skill can format individual files or entire directories, check formatting without making changes, and respect custom Prettier configurations.

## Overview

**Purpose:** Automatically format code using Prettier to maintain consistent code style across your project.

**Command:** `/code/format`

**Version:** 0.1.0

## Features

- Format individual files or entire directories
- Support for 15+ file types (JavaScript, TypeScript, CSS, HTML, JSON, YAML, Markdown, and more)
- Auto-detect Prettier configuration files (.prettierrc, prettier.config.js, etc.)
- Check-only mode to validate formatting without modifying files
- Custom file pattern filtering
- Detailed formatting reports
- Automatic discovery of local and global Prettier installations

## Supported File Types

- **JavaScript**: .js, .jsx, .mjs, .cjs
- **TypeScript**: .ts, .tsx
- **CSS/Styles**: .css, .scss, .less
- **HTML**: .html, .htm
- **JSON**: .json
- **YAML**: .yaml, .yml
- **Markdown**: .md, .mdx
- **GraphQL**: .graphql, .gql
- **Vue**: .vue

## Prerequisites

Prettier must be installed either globally or locally in your project:

```bash
# Global installation
npm install -g prettier

# Or local installation (recommended)
npm install --save-dev prettier
```

## Usage

### Basic Usage

Format a single file:

```bash
python3 skills/code.format/code_format.py --path src/index.js
```

Format an entire directory:

```bash
python3 skills/code.format/code_format.py --path src/
```

### Advanced Usage

**Check formatting without modifying files:**

```bash
python3 skills/code.format/code_format.py --path src/ --check
```

**Format only specific file types:**

```bash
python3 skills/code.format/code_format.py --path src/ --patterns "**/*.ts,**/*.tsx"
```

**Use custom Prettier configuration:**

```bash
python3 skills/code.format/code_format.py --path src/ --config-path .prettierrc.custom
```

**Dry run (check without writing):**

```bash
python3 skills/code.format/code_format.py --path src/ --no-write
```

**Output as YAML:**

```bash
python3 skills/code.format/code_format.py --path src/ --output-format yaml
```

## CLI Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--path` | Yes | - | File or directory path to format |
| `--config-path` | No | Auto-detect | Path to custom Prettier configuration file |
| `--check` | No | false | Only check formatting without modifying files |
| `--patterns` | No | All supported | Comma-separated glob patterns (e.g., "**/*.js,**/*.ts") |
| `--no-write` | No | false | Don't write changes (dry run mode) |
| `--output-format` | No | json | Output format: json or yaml |

## Configuration

The skill will automatically search for Prettier configuration files in this order:

1. Custom config specified via `--config-path`
2. `.prettierrc` in the target directory or parent directories
3. `.prettierrc.json`, `.prettierrc.yml`, `.prettierrc.yaml`
4. `.prettierrc.js`, `.prettierrc.cjs`
5. `prettier.config.js`, `prettier.config.cjs`
6. Prettier defaults if no config found

## Output Format

The skill returns a JSON object with detailed formatting results:

```json
{
  "ok": true,
  "status": "success",
  "message": "Formatted 5 files. 3 already formatted.",
  "formatted_count": 5,
  "already_formatted_count": 3,
  "needs_formatting_count": 0,
  "checked_count": 8,
  "error_count": 0,
  "files_formatted": [
    "src/components/Header.tsx",
    "src/utils/helpers.js"
  ],
  "files_already_formatted": [
    "src/index.ts",
    "src/App.tsx",
    "src/config.json"
  ],
  "files_need_formatting": [],
  "files_with_errors": []
}
```

### Response Fields

- **ok**: Boolean indicating overall success
- **status**: Status string ("success" or "failed")
- **message**: Human-readable summary
- **formatted_count**: Number of files that were formatted
- **already_formatted_count**: Number of files that were already properly formatted
- **needs_formatting_count**: Number of files that need formatting (check mode only)
- **checked_count**: Total number of files processed
- **error_count**: Number of files that encountered errors
- **files_formatted**: List of files that were formatted
- **files_already_formatted**: List of files that were already formatted
- **files_need_formatting**: List of files needing formatting (check mode)
- **files_with_errors**: List of files with errors and error messages

## Error Handling

The skill gracefully handles various error scenarios:

- **Prettier not installed**: Clear error message with installation instructions
- **Invalid path**: Validation error if path doesn't exist
- **Syntax errors**: Reports files with syntax errors without stopping
- **Permission errors**: Reports files that couldn't be read/written
- **Timeouts**: 30-second timeout per file with clear error reporting

## Integration with Agents

Include this skill in your agent's configuration:

```yaml
name: my.agent
version: 1.0.0
skills_available:
  - code.format
```

Then invoke it programmatically:

```python
from skills.code_format.code_format import CodeFormat

formatter = CodeFormat()
result = formatter.execute(
    path="src/",
    check_only=True,
    file_patterns="**/*.{ts,tsx}"
)

if result["ok"]:
    print(f"Checked {result['checked_count']} files")
    print(f"{result['needs_formatting_count']} files need formatting")
```

## Examples

### Example 1: Format a React Project

```bash
python3 skills/code.format/code_format.py \
  --path src/ \
  --patterns "**/*.{js,jsx,ts,tsx,css,json}"
```

### Example 2: Pre-commit Check

```bash
python3 skills/code.format/code_format.py \
  --path src/ \
  --check \
  --output-format json

# Exit code 0 if all files formatted, 1 otherwise
```

### Example 3: Format Only Changed Files

```bash
# Get changed files from git
CHANGED_FILES=$(git diff --name-only --diff-filter=ACMR | grep -E '\.(js|ts|jsx|tsx)$' | tr '\n' ',')

# Format only those files
python3 skills/code.format/code_format.py \
  --path . \
  --patterns "$CHANGED_FILES"
```

## Testing

Run the test suite:

```bash
pytest skills/code.format/test_code_format.py -v
```

Run specific tests:

```bash
pytest skills/code.format/test_code_format.py::TestCodeFormat::test_single_file -v
```

## Permissions

This skill requires the following permissions:

- **filesystem:read** - To read files and configurations
- **filesystem:write** - To write formatted files
- **process:execute** - To run the Prettier command

## Artifact Metadata

**Produces:**
- `formatting-report` (application/json) - Detailed formatting operation results

## Troubleshooting

**Issue**: "Prettier is not installed"
- **Solution**: Install Prettier globally (`npm install -g prettier`) or locally in your project

**Issue**: No files found to format
- **Solution**: Check your file patterns and ensure files exist in the target path

**Issue**: Configuration file not found
- **Solution**: Ensure your config file exists and the path is correct, or let it auto-detect

**Issue**: Timeout errors
- **Solution**: Very large files may timeout (30s limit). Format them individually or increase timeout in code

## Created By

This skill was generated by **meta.skill**, the skill creator meta-agent, and enhanced with full Prettier integration.

---

*Part of the Betty Framework*
