#!/usr/bin/env python3
"""
Refactor artifact_define.py to load from JSON registry

This script:
1. Backs up the current artifact_define.py with hardcoded dictionary
2. Creates a new version that loads from registry/artifact_types.json
3. Adds timestamps to the JSON files
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone

# Add betty to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def update_json_timestamps():
    """Add timestamps to JSON files"""
    logger.info("Updating JSON file timestamps...")

    # Update artifact_types.json
    registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"
    with open(registry_file, 'r') as f:
        data = json.load(f)

    data['generated_at'] = datetime.now(timezone.utc).isoformat()

    with open(registry_file, 'w') as f:
        json.dump(data, f, indent=2)

    logger.info(f"Updated {registry_file}")

    # Update audit report
    audit_file = Path(BASE_DIR) / "registry" / "artifact_registry_audit.json"
    with open(audit_file, 'r') as f:
        data = json.load(f)

    data['audit_timestamp'] = datetime.now(timezone.utc).isoformat()

    with open(audit_file, 'w') as f:
        json.dump(data, f, indent=2)

    logger.info(f"Updated {audit_file}")


def create_registry_loader():
    """Create the registry loader module"""
    logger.info("Creating registry loader module...")

    loader_code = '''#!/usr/bin/env python3
"""
Artifact Registry Loader - Load artifact types from JSON

This module provides the single source of truth for artifact types.
The registry is loaded from registry/artifact_types.json at runtime.
"""

import json
from pathlib import Path
from typing import Dict, Any
from functools import lru_cache

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


@lru_cache(maxsize=1)
def load_artifact_registry() -> Dict[str, Dict[str, Any]]:
    """
    Load artifact types from JSON registry file.

    Returns:
        Dictionary mapping artifact type names to their metadata

    Raises:
        FileNotFoundError: If registry file doesn't exist
        json.JSONDecodeError: If registry file is invalid JSON
    """
    registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"

    if not registry_file.exists():
        logger.error(f"Registry file not found: {registry_file}")
        raise FileNotFoundError(f"Artifact registry not found at {registry_file}")

    try:
        with open(registry_file, 'r') as f:
            data = json.load(f)

        # Convert list format to dictionary format
        registry = {}
        for artifact in data.get('artifact_types', []):
            name = artifact.get('name')
            if not name:
                continue

            # Build metadata dictionary (exclude name since it's the key)
            metadata = {}
            if artifact.get('description'):
                metadata['description'] = artifact['description']
            if artifact.get('file_pattern'):
                metadata['file_pattern'] = artifact['file_pattern']
            if artifact.get('content_type'):
                metadata['content_type'] = artifact['content_type']
            if artifact.get('schema'):
                metadata['schema'] = artifact['schema']

            registry[name] = metadata

        logger.info(f"Loaded {len(registry)} artifact types from registry")
        return registry

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in registry file: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading registry: {e}")
        raise


# Load the registry on module import
try:
    KNOWN_ARTIFACT_TYPES = load_artifact_registry()
except Exception as e:
    logger.warning(f"Failed to load artifact registry: {e}")
    logger.warning("Using empty registry as fallback")
    KNOWN_ARTIFACT_TYPES = {}


def reload_registry():
    """
    Reload the artifact registry from disk.

    This clears the cache and forces a fresh load from the JSON file.
    Useful for development and testing.
    """
    load_artifact_registry.cache_clear()
    global KNOWN_ARTIFACT_TYPES
    KNOWN_ARTIFACT_TYPES = load_artifact_registry()
    logger.info("Registry reloaded")
    return KNOWN_ARTIFACT_TYPES


def get_artifact_count() -> int:
    """Get the number of registered artifact types"""
    return len(KNOWN_ARTIFACT_TYPES)


def is_registered(artifact_type: str) -> bool:
    """Check if an artifact type is registered"""
    return artifact_type in KNOWN_ARTIFACT_TYPES


def get_artifact_metadata(artifact_type: str) -> Dict[str, Any]:
    """
    Get metadata for a specific artifact type.

    Args:
        artifact_type: The artifact type identifier

    Returns:
        Dictionary with artifact metadata, or empty dict if not found
    """
    return KNOWN_ARTIFACT_TYPES.get(artifact_type, {})
'''

    loader_file = Path(BASE_DIR) / "skills" / "artifact.define" / "registry_loader.py"
    with open(loader_file, 'w') as f:
        f.write(loader_code)

    logger.info(f"Created {loader_file}")
    return loader_file


def refactor_artifact_define():
    """Refactor artifact_define.py to use JSON registry"""
    logger.info("Refactoring artifact_define.py...")

    artifact_define_file = Path(BASE_DIR) / "skills" / "artifact.define" / "artifact_define.py"

    # Create backup
    backup_file = artifact_define_file.with_suffix('.py.backup')
    shutil.copy2(artifact_define_file, backup_file)
    logger.info(f"Created backup: {backup_file}")

    # Read current content
    with open(artifact_define_file, 'r') as f:
        content = f.read()

    # Find where KNOWN_ARTIFACT_TYPES starts and ends
    start_marker = "# Known artifact types and their metadata\nKNOWN_ARTIFACT_TYPES = {"
    end_marker = "\n}\n\n\ndef get_artifact_definition"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        logger.error("Could not find KNOWN_ARTIFACT_TYPES in file")
        return None

    # Build new content
    new_content = content[:start_idx]
    new_content += '''# Known artifact types - loaded from registry/artifact_types.json
# To update the registry, modify registry/artifact_types.json and reload
from skills.artifact.define.registry_loader import (
    KNOWN_ARTIFACT_TYPES,
    load_artifact_registry,
    reload_registry,
    get_artifact_count,
    is_registered,
    get_artifact_metadata
)

# For backward compatibility, expose the registry as module-level variable
# Note: The registry is now data-driven and loaded from JSON
# Do not modify this file to add new artifact types
# Instead, update registry/artifact_types.json


'''
    new_content += content[end_idx+2:]  # Skip the closing brace and blank line

    # Write refactored version
    with open(artifact_define_file, 'w') as f:
        f.write(new_content)

    logger.info(f"Refactored {artifact_define_file}")
    return artifact_define_file


def create_readme():
    """Create README for the registry directory"""
    logger.info("Creating registry README...")

    readme_content = '''# Artifact Registry

This directory contains the central artifact registry for the Betty Framework.

## Files

### artifact_types.json
The **single source of truth** for all artifact type definitions. This file is loaded at runtime by `skills/artifact.define/artifact_define.py`.

**Structure:**
```json
{
  "version": "1.0.0",
  "generated_at": "ISO 8601 timestamp",
  "artifact_types": [
    {
      "name": "artifact-type-name",
      "description": "Human-readable description",
      "file_pattern": "*.pattern.{md,yaml}",
      "content_type": "text/markdown or application/yaml",
      "schema": "schemas/artifact-schema.json (optional)"
    }
  ]
}
```

**Adding a new artifact type:**
1. Add entry to `artifact_types` array in this file
2. Create description in `artifact_descriptions/{name}.md`
3. Optionally create JSON Schema in `schemas/artifacts/{name}-schema.json`
4. Run `python tools/audit_artifact_registry.py` to verify

### artifact_registry_audit.json
Comprehensive audit report showing:
- Registry consistency
- Missing artifact types
- Unused artifact types
- References across skills, agents, and templates

Generated by: `python tools/audit_artifact_registry.py`

## Workflow

### 1. Define New Artifact Type
Use the `meta.artifact` agent or add manually to `artifact_types.json`:

```bash
# Using meta.artifact agent
betty run meta.artifact create --description artifact_descriptions/my-type.md

# Or edit directly
vim registry/artifact_types.json
```

### 2. Validate Registry
Run the audit tool to ensure consistency:

```bash
python tools/audit_artifact_registry.py
```

### 3. Use Artifact Type
Reference the artifact in skill.yaml:

```yaml
artifact_metadata:
  produces:
    - type: my-artifact-type
      description: "What this produces"
```

## Data-Driven Approach

The registry follows a **data-driven** philosophy:
- ✅ Artifact types are defined in JSON (data)
- ✅ Code loads from JSON at runtime
- ❌ No hardcoded dictionaries in Python code
- ❌ No self-modifying source code

This enables:
- Version control of artifact definitions
- Easier auditing and validation
- Separation of concerns (data vs code)
- Runtime flexibility

## Automation

### Nightly CI
The audit tool should run in CI to catch inconsistencies:

```yaml
# .github/workflows/audit-registry.yml
- name: Audit Artifact Registry
  run: python tools/audit_artifact_registry.py
```

### Pre-commit Hook
Validate registry on commit:

```yaml
# .claude-code/hooks.yaml
before-commit:
  - command: python tools/audit_artifact_registry.py
    description: Validate artifact registry consistency
```

## Maintenance

- **Owner:** Betty Framework Core Team
- **Review Cycle:** Quarterly
- **Last Audit:** Check `artifact_registry_audit.json` for timestamp
- **Documentation:** See `docs/ARTIFACT_STANDARDS.md`
'''

    readme_file = Path(BASE_DIR) / "registry" / "README.md"
    with open(readme_file, 'w') as f:
        f.write(readme_content)

    logger.info(f"Created {readme_file}")


def main():
    """Main refactoring function"""
    logger.info("Starting artifact registry refactoring...")

    try:
        # Step 1: Update timestamps in JSON files
        update_json_timestamps()

        # Step 2: Create registry loader module
        create_registry_loader()

        # Step 3: Refactor artifact_define.py
        refactor_artifact_define()

        # Step 4: Create README
        create_readme()

        logger.info("Refactoring completed successfully!")
        logger.info("\nNext steps:")
        logger.info("1. Test the refactored code with artifact.create, artifact.validate, etc.")
        logger.info("2. Run the test suite to ensure no regressions")
        logger.info("3. Commit changes with descriptive message")

        return 0

    except Exception as e:
        logger.error(f"Refactoring failed: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
