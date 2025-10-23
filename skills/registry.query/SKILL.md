# registry.query

**Version:** 0.1.0
**Status:** Active
**Tags:** registry, search, query, discovery, metadata, cli

## Overview

The `registry.query` skill enables programmatic searching of Betty registries (skills, agents, and commands) with flexible filtering capabilities. It's designed for dynamic discovery, workflow automation, and CLI autocompletion.

## Features

- **Multi-Registry Support**: Query skills, agents, or commands registries
- **Flexible Filtering**: Filter by name, version, status, tags, domain, and capability
- **Fuzzy Matching**: Optional fuzzy search for name and capability fields
- **Result Limiting**: Control the number of results returned
- **Rich Metadata**: Returns key metadata for each matching entry
- **JSON Output**: Structured output suitable for programmatic use

## Usage

### Command Line

```bash
# List all skills
python3 skills/registry.query/registry_query.py skills

# Find skills with 'api' tag
python3 skills/registry.query/registry_query.py skills --tag api

# Find agents with 'design' capability
python3 skills/registry.query/registry_query.py agents --capability design

# Find active skills with name containing 'validate'
python3 skills/registry.query/registry_query.py skills --name validate --status active

# Fuzzy search for commands
python3 skills/registry.query/registry_query.py commands --name test --fuzzy

# Limit results to top 5
python3 skills/registry.query/registry_query.py skills --tag api --limit 5

# Get full JSON output
python3 skills/registry.query/registry_query.py skills --tag validation --json
```

### Programmatic Use

```python
from skills.registry.query.registry_query import query_registry

# Query skills with API tag
result = query_registry(
    registry="skills",
    tag="api",
    status="active"
)

if result["ok"]:
    matching_entries = result["details"]["results"]
    for entry in matching_entries:
        print(f"{entry['name']}: {entry['description']}")
```

### Betty CLI

```bash
# Via Betty CLI (when registered)
betty registry query skills --tag api
betty registry query agents --capability "API design"
```

## Parameters

### Required

- **`registry`** (string): Registry to query
  - Valid values: `skills`, `agents`, `commands`

### Optional Filters

- **`name`** (string): Filter by name (substring match, case-insensitive)
- **`version`** (string): Filter by exact version match
- **`status`** (string): Filter by status (e.g., `active`, `draft`, `deprecated`, `archived`)
- **`tag`** (string): Filter by single tag
- **`tags`** (array): Filter by multiple tags (matches any)
- **`capability`** (string): Filter by capability (agents only, substring match)
- **`domain`** (string): Filter by domain (alias for tag filter)
- **`fuzzy`** (boolean): Enable fuzzy matching for name and capability
- **`limit`** (integer): Maximum number of results to return

## Output Format

### Success Response

```json
{
  "ok": true,
  "status": "success",
  "errors": [],
  "timestamp": "2025-10-23T10:30:00.000000Z",
  "details": {
    "registry": "skills",
    "query": {
      "name": "api",
      "version": null,
      "status": "active",
      "tags": ["validation"],
      "capability": null,
      "domain": null,
      "fuzzy": false,
      "limit": null
    },
    "total_entries": 21,
    "matching_entries": 3,
    "results": [
      {
        "name": "api.validate",
        "version": "0.1.0",
        "description": "Validates OpenAPI or AsyncAPI specifications...",
        "status": "active",
        "tags": ["api", "validation", "openapi", "asyncapi"],
        "dependencies": ["context.schema"],
        "entrypoints": [
          {
            "command": "/api/validate",
            "runtime": "python",
            "description": "Validate API specification files"
          }
        ],
        "inputs": [...],
        "outputs": [...]
      }
    ]
  }
}
```

### Error Response

```json
{
  "ok": false,
  "status": "failed",
  "errors": ["Invalid registry: invalid_type"],
  "timestamp": "2025-10-23T10:30:00.000000Z"
}
```

## Metadata Fields by Registry Type

### Skills

- `name`, `version`, `description`, `status`, `tags`
- `dependencies`: List of required skills
- `entrypoints`: Available commands and handlers
- `inputs`: Expected input parameters
- `outputs`: Generated outputs

### Agents

- `name`, `version`, `description`, `status`, `tags`
- `capabilities`: List of agent capabilities
- `skills_available`: Skills the agent can invoke
- `reasoning_mode`: `oneshot` or `iterative`
- `context_requirements`: Required context fields

### Commands

- `name`, `version`, `description`, `status`, `tags`
- `execution`: Execution configuration (type, target)
- `parameters`: Command parameters

## Use Cases

### 1. Dynamic Discovery

Find skills related to a specific domain:

```bash
python3 skills/registry.query/registry_query.py skills --domain api
```

### 2. Workflow Automation

Programmatically find and invoke skills:

```python
# Find validation skills
result = query_registry(registry="skills", tag="validation", status="active")

for skill in result["details"]["results"]:
    print(f"Found validation skill: {skill['name']}")
    # Invoke skill programmatically
```

### 3. CLI Autocompletion

Generate autocompletion data:

```python
# Get all active skill names for tab completion
result = query_registry(registry="skills", status="active")
skill_names = [s["name"] for s in result["details"]["results"]]
```

### 4. Dependency Resolution

Find skills with specific dependencies:

```python
result = query_registry(registry="skills", status="active")
for skill in result["details"]["results"]:
    if "context.schema" in skill.get("dependencies", []):
        print(f"{skill['name']} depends on context.schema")
```

### 5. Capability Search

Find agents by capability:

```bash
python3 skills/registry.query/registry_query.py agents --capability "API design"
```

### 6. Status Monitoring

Find deprecated or draft entries:

```bash
python3 skills/registry.query/registry_query.py skills --status deprecated
python3 skills/registry.query/registry_query.py skills --status draft
```

## Future Extensions

The skill is designed with these future enhancements in mind:

1. **Advanced Fuzzy Matching**: Implement more sophisticated fuzzy matching algorithms (e.g., Levenshtein distance)
2. **Full-Text Search**: Search within descriptions and documentation
3. **Dependency Graph**: Query dependency relationships between skills
4. **Version Ranges**: Support semantic version range queries (e.g., `>=1.0.0,<2.0.0`)
5. **Sorting Options**: Sort results by name, version, or relevance
6. **Regular Expression Support**: Use regex patterns for advanced filtering
7. **Marketplace Integration**: Query marketplace catalogs with certification status
8. **Performance Caching**: Cache registry data for faster repeated queries

## Examples

### Example 1: Find all API-related skills

```bash
$ python3 skills/registry.query/registry_query.py skills --tag api

================================================================================
REGISTRY QUERY: SKILLS
================================================================================

Total entries: 21
Matching entries: 5

--------------------------------------------------------------------------------
RESULTS:
--------------------------------------------------------------------------------

1. api.define (v0.1.0)
   Status: active
   Description: Generates OpenAPI 3.1 or AsyncAPI 2.6 specifications from natural language...
   Tags: api, openapi, asyncapi, scaffolding
   Commands: /api/define

2. api.validate (v0.1.0)
   Status: active
   Description: Validates OpenAPI or AsyncAPI specifications against their respective schemas...
   Tags: api, validation, openapi, asyncapi
   Commands: /api/validate

...
```

### Example 2: Find agents that can design APIs

```bash
$ python3 skills/registry.query/registry_query.py agents --capability design

================================================================================
REGISTRY QUERY: AGENTS
================================================================================

Total entries: 2
Matching entries: 1

--------------------------------------------------------------------------------
RESULTS:
--------------------------------------------------------------------------------

1. api.designer (v0.1.0)
   Status: draft
   Description: Design RESTful APIs following best practices and guidelines...
   Tags: api, design, openapi
   Capabilities: 7 capabilities
   Reasoning: iterative
```

### Example 3: Fuzzy search with limit

```bash
$ python3 skills/registry.query/registry_query.py skills --name vld --fuzzy --limit 3

# Finds: api.validate, context.validate, etc.
```

## Error Handling

The skill handles various error conditions:

- **Invalid registry type**: Returns error with valid options
- **Missing registry file**: Returns empty results with warning
- **Invalid JSON**: Returns error with details
- **Invalid filter combinations**: Logs warnings and proceeds with valid filters

## Performance Considerations

- Registry files are loaded once per query
- Filtering is performed in memory (O(n) complexity)
- For large registries, use `--limit` to control result size
- Consider caching registry data for repeated queries in production

## Dependencies

- **None**: This skill has no dependencies on other Betty skills
- **Python Standard Library**: Uses `json`, `re`, `pathlib`
- **Betty Framework**: Requires `betty.config`, `betty.logging_utils`, `betty.errors`

## Permissions

- **`filesystem:read`**: Required to read registry JSON files

## Contributing

To extend this skill:

1. Add new filter types in `filter_entries()`
2. Enhance fuzzy matching in `matches_pattern()`
3. Add new metadata extractors in `extract_key_metadata()`
4. Update tests and documentation

## See Also

- **skill.define**: Define new skills
- **agent.define**: Define new agents
- **plugin.sync**: Sync registry files
- **marketplace**: Betty marketplace catalog
