# meta.compatibility

Automatic artifact dependency graph validation and diagnostics for the Betty Framework.

## Overview

The `meta.compatibility` skill analyzes the artifact dependency graph across all Betty skills, detecting compatibility issues, cycles, orphan nodes, and unresolved dependencies. It provides actionable diagnostics to maintain a healthy skill ecosystem.

## Features

- **Graph Construction**: Builds directed graph from skill artifact metadata
- **Cycle Detection**: Identifies recursive dependencies (marks as `recursive:true`)
- **Orphan Detection**: Finds isolated nodes with no connections
- **Dependency Analysis**: Detects unresolved dependencies (consumed but never produced)
- **Producer Analysis**: Identifies orphan producers (produced but never consumed)
- **Health Reporting**: Comprehensive JSON and human-readable reports

## Usage

### Basic Validation

```bash
betty run /meta/compatibility --check artifacts
```

### Save Report to File

```bash
betty run /meta/compatibility --check artifacts --output graph-report.json
```

### JSON Output Only

```bash
betty run /meta/compatibility --check artifacts --json
```

### Custom Skills Directory

```bash
betty run /meta/compatibility --check artifacts --skills-dir /path/to/skills
```

## Output Format

### Human-Readable Output

```
======================================================================
Artifact Dependency Graph Validation
======================================================================
Total Skills:     25
Total Artifacts:  42
Graph Density:    12.50%

✅ 38 artifacts connected
⚠️  3 isolated
   - report.template
   - legacy.format
   - experimental.data
❌ 1 cycle(s) detected
   1. model-a → model-b → model-a

✅ Graph Status: HEALTHY
======================================================================
```

### JSON Report

```json
{
  "total_artifacts": 42,
  "total_skills": 25,
  "connected": 38,
  "isolated": ["report.template", "legacy.format"],
  "cyclic": [["model-a", "model-b", "model-a"]],
  "unresolved": ["dataset.missing"],
  "orphans": ["deprecated.artifact"],
  "status": "warning",
  "graph_stats": {
    "nodes": 42,
    "edges": 58,
    "density": 0.125
  }
}
```

## Report Fields

| Field | Type | Description |
|-------|------|-------------|
| `total_artifacts` | number | Total artifact types in the graph |
| `total_skills` | number | Total skills with artifact metadata |
| `connected` | number | Artifacts with at least one connection |
| `isolated` | array | Artifact types with no connections |
| `cyclic` | array | Lists of artifact cycles (recursive dependencies) |
| `unresolved` | array | Artifacts consumed but never produced |
| `orphans` | array | Artifacts produced but never consumed |
| `status` | string | Overall health: `healthy`, `warning`, or `error` |
| `graph_stats` | object | Graph metrics (nodes, edges, density) |

## Status Levels

- **healthy**: No critical issues detected
- **warning**: Non-critical issues (isolated nodes, orphan producers)
- **error**: Critical issues (cycles, unresolved dependencies)

## Validation Rules

### Critical Issues (Error Status)

1. **Cycles**: Circular dependencies in artifact flow
   - Example: Skill A produces X, consumes Y; Skill B produces Y, consumes X
   - Can cause infinite loops in workflows

2. **Unresolved Dependencies**: Artifacts consumed but never produced
   - Example: Skill requires `api-spec` but no skill produces it
   - Breaks skill composition and workflows

### Warnings (Warning Status)

1. **Isolated Nodes**: Artifacts with no producers or consumers
   - May indicate deprecated or unused artifact types
   - Not critical but suggests cleanup needed

2. **Orphan Producers**: Artifacts produced but never consumed
   - May indicate missing consumer skills
   - Not critical but suggests incomplete workflows

## Example Scenarios

### Scenario 1: Healthy Graph

```
Skills:
  - api.define: produces openapi-spec
  - api.validate: consumes openapi-spec, produces validation-report
  - api.test: consumes openapi-spec, produces test-results

Result: ✅ All connected, no issues
```

### Scenario 2: Cycle Detected

```
Skills:
  - transform.a: consumes data-raw, produces data-interim
  - transform.b: consumes data-interim, produces data-processed
  - transform.c: consumes data-processed, produces data-raw

Result: ❌ Cycle detected: data-raw → data-interim → data-processed → data-raw
```

### Scenario 3: Unresolved Dependency

```
Skills:
  - api.test: consumes api-spec
  - (no skill produces api-spec)

Result: ❌ Unresolved dependency: api-spec consumed but never produced
```

### Scenario 4: Isolated Artifact

```
Skills:
  - legacy.export: produces legacy-format
  - (no skill consumes legacy-format)
  - (no skill produces legacy-format to feed others)

Result: ⚠️  Isolated: legacy-format (if also not consumed, orphan producer)
```

## Implementation Details

### Graph Construction

The skill builds a directed graph where:
- **Nodes**: Artifact types (e.g., `openapi-spec`, `validation-report`)
- **Edges**: Dependency flows (A → B means artifact A is consumed by a skill that produces B)
- **Attributes**: Each node tracks its producers and consumers (skill names)

```python
import networkx as nx

def build_artifact_graph(artifacts):
    g = nx.DiGraph()
    for artifact in artifacts:
        g.add_node(artifact["id"])
        for dep in artifact.get("consumes", []):
            g.add_edge(dep, artifact["id"])
    return g
```

### Validation Algorithms

1. **Cycle Detection**: Uses `networkx.simple_cycles()` to find all cycles
2. **Isolated Nodes**: Checks `in_degree == 0 and out_degree == 0`
3. **Unresolved**: Nodes with consumers but no producers
4. **Orphans**: Nodes with producers but no consumers

## Integration

This skill is part of the meta-skills layer and can be used to:

1. **Pre-flight Checks**: Validate graph before deploying new skills
2. **CI/CD**: Run in pipelines to ensure artifact compatibility
3. **Documentation**: Generate artifact flow diagrams
4. **Debugging**: Identify why skill compositions fail

## Dependencies

- `networkx>=3.0`: Graph analysis library
- `PyYAML>=6.0`: Parse skill.yaml files

## Related Skills

- `artifact.validate`: Validates individual artifact files
- `artifact.define`: Defines artifact metadata schemas
- `registry.query`: Queries skill registry for artifact information

## Exit Codes

- `0`: Success (healthy or warning status)
- `1`: Error (critical issues detected)

## Limitations

- Does not validate actual artifact files, only metadata
- Wildcard consumers (`type: "*"`) are ignored in graph construction
- Does not check runtime compatibility, only structural compatibility

## Future Enhancements

- Visual graph rendering (GraphViz output)
- Suggested fixes for detected issues
- Artifact version compatibility checking
- Runtime dependency validation
