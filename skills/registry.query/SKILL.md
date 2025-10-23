# registry.query

Search Betty registries programmatically for skills, agents, commands, and hooks.

## Overview

The `registry.query` skill provides a powerful interface for discovering and filtering entries in Betty's registries. It enables users and workflows to dynamically look up available skills, agents, commands, and hooks based on various criteria such as tags, status, capabilities, and more.

## Use Cases

- **Discovery**: Find all skills in a specific domain (e.g., all API-related skills)
- **Workflow Automation**: Dynamically select skills/agents based on tags or capabilities
- **Status Monitoring**: List all draft or deprecated entries
- **CLI Autocompletion**: Generate lists of available skills for shell completion (future)
- **Documentation**: Generate inventory reports of available capabilities
- **Dependency Resolution**: Find skills that match required capabilities

## Installation

This skill is part of the core Betty framework and requires no additional installation.

## Usage

### Command Line

```bash
python skills/registry.query/registry_query.py <registry> [options]
```

### Basic Examples

#### Find all API-related skills
```bash
python skills/registry.query/registry_query.py skills --domain api
```

#### Find active skills with 'validation' tag
```bash
python skills/registry.query/registry_query.py skills --tag validation --status active
```

#### Find agents with specific capability
```bash
python skills/registry.query/registry_query.py agents --capability "API design"
```

#### Search for skills by partial name
```bash
python skills/registry.query/registry_query.py skills --name compatibility --partial
```

#### Get all hook names (for scripting)
```bash
python skills/registry.query/registry_query.py hooks --format names
```

#### Detailed view of all draft agents
```bash
python skills/registry.query/registry_query.py agents --status draft --format detailed
```

### Advanced Examples

#### Find skills with multiple tags
```bash
python skills/registry.query/registry_query.py skills --tags api validation openapi
```

#### Custom field selection
```bash
python skills/registry.query/registry_query.py skills --domain api --format detailed --fields name version tags
```

#### JSON output for programmatic use
```bash
python skills/registry.query/registry_query.py agents --status active --format json | jq '.results[].name'
```

## Parameters

### Required

- **registry**: Registry to query
  - Values: `skills`, `agents`, `commands`, `hooks`

### Optional Filters

- **--name**: Filter by name (exact match unless --partial is used)
- **--partial**: Enable partial/substring name matching
- **--version**: Filter by exact version (semantic versioning)
- **--tag**: Filter by single tag (entries must have this tag)
- **--tags**: Filter by multiple tags (entries must have at least one)
- **--status**: Filter by status
  - Values: `draft`, `active`, `deprecated`, `archived`
- **--capability**: Filter by capability substring (agents only)
- **--domain**: Filter by domain prefix (e.g., 'api' matches 'api.define', 'api.validate')

### Output Options

- **--format**: Output format (default: `summary`)
  - `summary`: Brief listing with descriptions
  - `detailed`: Full entry details
  - `json`: Structured JSON output
  - `names`: Names only (one per line)
- **--fields**: Specific fields to include in output (for detailed format)

## Output Formats

### Summary Format (Default)

```
Found 3 matching skills:

  • api.compatibility (v0.1.0) [active]
    Detect breaking changes between API specification versions
    Tags: api, compatibility, breaking-changes, versioning, openapi

  • api.define (v0.1.0) [active]
    Define OpenAPI specifications with validation and best practices
    Tags: api, openapi, specification, design, validation

  • api.validate (v0.1.0) [active]
    Validate OpenAPI specifications against standards
    Tags: api, validation, openapi, standards
```

### Names Format

```
api.compatibility
api.define
api.validate
```

### JSON Format

```json
{
  "count": 3,
  "results": [
    {
      "name": "api.compatibility",
      "version": "0.1.0",
      "description": "Detect breaking changes between API specification versions",
      "status": "active",
      "tags": ["api", "compatibility", "breaking-changes", "versioning", "openapi"],
      ...
    }
  ]
}
```

### Detailed Format

```
Found 3 matching skills:

--- Entry 1 ---
name: api.compatibility
version: 0.1.0
description: Detect breaking changes between API specification versions
status: active
tags:
  [
    "api",
    "compatibility",
    "breaking-changes",
    "versioning",
    "openapi"
  ]
...
```

## Exit Codes

- **0**: Query successful, results found
- **1**: Query successful, no results found
- **2**: Error occurred (invalid parameters, registry not found, etc.)

## Filtering Logic

### Name Filtering
- Default: Exact match
- With `--partial`: Case-insensitive substring match

### Tag Filtering
- Entries must have **at least one** of the specified tags
- Multiple tags use OR logic

### Capability Filtering (Agents Only)
- Case-insensitive substring match
- Searches all capability descriptions

### Domain Filtering
- Matches the prefix before the first dot in the name
- Example: domain `api` matches `api.define`, `api.compatibility`, `api.validate`

### Status Filtering
- Exact match on status field
- Valid values: `draft`, `active`, `deprecated`, `archived`

## Python API

You can also use the skill programmatically:

```python
from pathlib import Path
import sys

# Add betty to path
BETTY_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BETTY_ROOT))

from skills.registry.query.registry_query import RegistryQuery

# Create query engine
query = RegistryQuery("skills")

# Execute query
results = query.query(
    domain="api",
    status="active",
    tags=["validation"]
)

# Format results
output = query.format_results(results, output_format="json")
print(output)
```

## Future Enhancements

- **Fuzzy Matching**: Implement fuzzy string matching for typo tolerance
- **CLI Autocompletion**: Serve as data source for shell completion
- **Regex Filtering**: Support regex patterns for advanced filtering
- **Performance Optimization**: Add caching for faster repeated queries
- **Cross-Registry Queries**: Search multiple registries simultaneously
- **Semantic Search**: Natural language capability matching
- **Sorting Options**: Sort results by various fields (name, version, date)

## Integration Examples

### Workflow Automation

```bash
# Find all active API skills and run validation
for skill in $(python skills/registry.query/registry_query.py skills --domain api --status active --format names); do
    echo "Processing $skill..."
    # Your workflow logic here
done
```

### Documentation Generation

```bash
# Generate markdown documentation of all active skills
python skills/registry.query/registry_query.py skills --status active --format detailed > active_skills.md
```

### CI/CD Pipeline

```bash
# Check if any skills are in draft status before deployment
if python skills/registry.query/registry_query.py skills --status draft --format names | grep -q .; then
    echo "Warning: Draft skills detected"
    exit 1
fi
```

## Related Skills

- **registry.update**: Update registry entries
- **registry.diff**: Compare manifest against registry
- **skill.create**: Create new skills
- **plugin.sync**: Synchronize plugin configurations

## Troubleshooting

### No results found
- Verify the filter criteria are correct
- Use `--format json` to see full query details
- Try broadening the search (remove some filters)

### Invalid registry type
- Ensure registry parameter is one of: skills, agents, commands, hooks
- Check for typos

### Permission errors
- Ensure registry JSON files are readable
- Check file permissions in `/home/user/betty/registry/`

## Contributing

To enhance this skill:
1. Add new filtering criteria in `RegistryQuery.query()`
2. Implement new output formats in `format_results()`
3. Update this documentation
4. Add test cases

## Metadata

- **Version**: 0.1.0
- **Status**: Active
- **Tags**: registry, query, search, discovery, lookup, automation, workflow, metadata
- **Dependencies**: None (uses core Betty utilities)
- **Permissions**: filesystem:read
