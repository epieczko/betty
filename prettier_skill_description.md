# Name: code.format

# Purpose:
Format code using Prettier, supporting multiple languages and file types. This skill can format individual files or entire directories, check formatting without making changes, and respect custom Prettier configurations.

# Inputs:
- path (required) - File or directory path to format
- config_path (optional) - Path to custom Prettier configuration file
- check_only (optional) - Boolean flag to only check formatting without modifying files
- file_patterns (optional) - Glob patterns to filter which files to format (e.g., "**/*.{js,ts,jsx,tsx}")
- write (optional) - Boolean flag to write formatted output to files (default: true)

# Outputs:
- formatting_report.json - JSON report with formatting results, files processed, and any errors
- formatted files - Updated files with proper formatting (when write=true)

# Permissions:
- filesystem:read
- filesystem:write
- process:execute

# Produces Artifacts:
- formatting-report

# Implementation Notes:

## Core Functionality
1. **File Discovery**: Recursively find files matching patterns in directory or process single file
2. **Prettier Execution**: Use Prettier CLI or JavaScript API to format code
3. **Configuration Support**: Auto-detect .prettierrc, prettier.config.js, or use provided config
4. **Dry Run Mode**: Support --check mode to validate formatting without changes
5. **Error Handling**: Gracefully handle syntax errors and unsupported file types
6. **Reporting**: Provide detailed report of formatted files, skipped files, and errors

## Supported File Types
- JavaScript (.js, .jsx, .mjs, .cjs)
- TypeScript (.ts, .tsx)
- CSS/SCSS/Less (.css, .scss, .less)
- HTML (.html, .htm)
- JSON (.json)
- YAML (.yaml, .yml)
- Markdown (.md, .mdx)
- GraphQL (.graphql, .gql)
- Vue (.vue)

## Dependencies
- Requires Prettier to be installed (npm install -g prettier or npx prettier)
- Should check for Prettier availability before execution
- Should support both global and local (node_modules) Prettier installations

## CLI Interface
The skill should provide:
- `--path <path>` - File or directory to format
- `--config <path>` - Custom config file
- `--check` - Check formatting without writing
- `--patterns <patterns>` - File patterns to include
- `--no-write` - Don't write changes (dry run)
- `--output-format <format>` - Report format (json/yaml)

## Return Structure
```json
{
  "ok": true,
  "status": "success",
  "formatted_count": 5,
  "checked_count": 5,
  "error_count": 0,
  "files_formatted": ["path/to/file1.js", "path/to/file2.ts"],
  "files_already_formatted": ["path/to/file3.json"],
  "files_with_errors": [],
  "errors": []
}
```

## Error Scenarios
- Prettier not installed: Clear error message with installation instructions
- Invalid configuration: Report config file errors
- Syntax errors in files: Report which files have syntax errors
- Permission errors: Report files that couldn't be read/written
- Unsupported file types: Skip with warning

## Testing Strategy
1. Test single file formatting
2. Test directory formatting
3. Test with custom config
4. Test check-only mode
5. Test file pattern filtering
6. Test error handling (invalid syntax, missing Prettier)
7. Test various file types
