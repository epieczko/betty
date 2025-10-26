#!/usr/bin/env python3
"""
Generate or update SKILL.md documentation from skill.yaml manifest files.

This skill automatically creates comprehensive documentation for Betty skills
based on their manifest definitions, ensuring consistency and completeness.
"""

import sys
import json
import argparse
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

# Add betty module to path

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_path

logger = setup_logger(__name__)


def load_skill_manifest(manifest_path: str) -> Dict[str, Any]:
    """
    Load and parse a skill.yaml manifest file.

    Args:
        manifest_path: Path to skill.yaml file

    Returns:
        Parsed manifest data

    Raises:
        BettyError: If manifest file is invalid or not found
    """
    manifest_file = Path(manifest_path)

    if not manifest_file.exists():
        raise BettyError(f"Manifest file not found: {manifest_path}")

    if not manifest_file.is_file():
        raise BettyError(f"Manifest path is not a file: {manifest_path}")

    try:
        import yaml
        with open(manifest_file, 'r') as f:
            manifest = yaml.safe_load(f)

        if not isinstance(manifest, dict):
            raise BettyError("Manifest must be a YAML object/dictionary")

        logger.info(f"Loaded skill manifest from {manifest_path}")
        return manifest
    except yaml.YAMLError as e:
        raise BettyError(f"Failed to parse YAML manifest: {e}")
    except Exception as e:
        raise BettyError(f"Failed to load manifest: {e}")


def normalize_input(inp: Any) -> Dict[str, Any]:
    """
    Normalize input definition to standard format.

    Args:
        inp: Input definition (string or dict)

    Returns:
        Normalized input dictionary
    """
    if isinstance(inp, str):
        # Simple string format: "workflow_path"
        return {
            'name': inp,
            'type': 'any',
            'required': True,
            'description': 'No description'
        }
    elif isinstance(inp, dict):
        # Already in object format
        return inp
    else:
        return {
            'name': 'unknown',
            'type': 'any',
            'required': False,
            'description': 'Invalid input format'
        }


def format_inputs_section(inputs: List[Any]) -> str:
    """
    Format the inputs section for the documentation.

    Args:
        inputs: List of input definitions from manifest (strings or dicts)

    Returns:
        Formatted markdown table
    """
    if not inputs:
        return "_No inputs defined_\n"

    lines = [
        "| Parameter | Type | Required | Default | Description |",
        "|-----------|------|----------|---------|-------------|"
    ]

    for inp in inputs:
        normalized = normalize_input(inp)
        name = normalized.get('name', 'unknown')
        type_val = normalized.get('type', 'any')
        required = 'Yes' if normalized.get('required', False) else 'No'
        default = normalized.get('default', '-')
        if default is True:
            default = 'true'
        elif default is False:
            default = 'false'
        elif default != '-':
            default = f'`{default}`'
        description = normalized.get('description', 'No description')

        lines.append(f"| `{name}` | {type_val} | {required} | {default} | {description} |")

    return '\n'.join(lines) + '\n'


def normalize_output(out: Any) -> Dict[str, Any]:
    """
    Normalize output definition to standard format.

    Args:
        out: Output definition (string or dict)

    Returns:
        Normalized output dictionary
    """
    if isinstance(out, str):
        # Simple string format: "validation_result.json"
        return {
            'name': out,
            'type': 'any',
            'description': 'No description'
        }
    elif isinstance(out, dict):
        # Already in object format
        return out
    else:
        return {
            'name': 'unknown',
            'type': 'any',
            'description': 'Invalid output format'
        }


def format_outputs_section(outputs: List[Any]) -> str:
    """
    Format the outputs section for the documentation.

    Args:
        outputs: List of output definitions from manifest (strings or dicts)

    Returns:
        Formatted markdown table
    """
    if not outputs:
        return "_No outputs defined_\n"

    lines = [
        "| Output | Type | Description |",
        "|--------|------|-------------|"
    ]

    for out in outputs:
        normalized = normalize_output(out)
        name = normalized.get('name', 'unknown')
        type_val = normalized.get('type', 'any')
        description = normalized.get('description', 'No description')

        lines.append(f"| `{name}` | {type_val} | {description} |")

    return '\n'.join(lines) + '\n'


def generate_usage_template(manifest: Dict[str, Any]) -> str:
    """
    Generate a usage template based on the skill manifest.

    Args:
        manifest: Parsed skill manifest

    Returns:
        Usage template string
    """
    skill_name = manifest.get('name', 'skill')
    inputs = manifest.get('inputs', [])

    # Get the handler/script name
    entrypoints = manifest.get('entrypoints', [])
    if entrypoints:
        handler = entrypoints[0].get('handler', f'{skill_name.replace(".", "_")}.py')
    else:
        handler = f'{skill_name.replace(".", "_")}.py'

    # Build basic usage
    skill_dir = f"skills/{skill_name}"
    usage = f"```bash\npython {skill_dir}/{handler}"

    # Normalize inputs
    normalized_inputs = [normalize_input(inp) for inp in inputs]

    # Add required positional arguments
    required_inputs = [inp for inp in normalized_inputs if inp.get('required', False)]
    for inp in required_inputs:
        usage += f" <{inp['name']}>"

    # Add optional arguments hint
    if any(not inp.get('required', False) for inp in normalized_inputs):
        usage += " [options]"

    usage += "\n```"

    return usage


def generate_parameters_detail(inputs: List[Any]) -> str:
    """
    Generate detailed parameter documentation.

    Args:
        inputs: List of input definitions (strings or dicts)

    Returns:
        Formatted parameter details
    """
    if not inputs:
        return ""

    lines = []
    for inp in inputs:
        normalized = normalize_input(inp)
        name = normalized.get('name', 'unknown')
        description = normalized.get('description', 'No description')
        type_val = normalized.get('type', 'any')
        required = normalized.get('required', False)
        default = normalized.get('default')

        detail = f"- `--{name}` ({type_val})"
        if required:
            detail += " **[Required]**"
        detail += f": {description}"
        if default is not None:
            detail += f" (default: `{default}`)"

        lines.append(detail)

    return '\n'.join(lines) + '\n'


def generate_skill_documentation(manifest: Dict[str, Any]) -> str:
    """
    Generate complete SKILL.md documentation from manifest.

    Args:
        manifest: Parsed skill manifest

    Returns:
        Generated markdown documentation
    """
    name = manifest.get('name', 'Unknown Skill')
    description = manifest.get('description', 'No description available')
    version = manifest.get('version', '0.1.0')
    inputs = manifest.get('inputs', [])
    outputs = manifest.get('outputs', [])
    tags = manifest.get('tags', [])
    dependencies = manifest.get('dependencies', [])

    # Build documentation
    doc = f"""# {name}

## Overview

**{name}** {description}

## Purpose

{description}

This skill automatically generates documentation by:
- Reading skill.yaml manifest files
- Extracting inputs, outputs, and metadata
- Creating standardized SKILL.md documentation
- Ensuring consistency across all Betty skills

## Usage

### Basic Usage

{generate_usage_template(manifest)}

### Parameters

{format_inputs_section(inputs)}

## Outputs

{format_outputs_section(outputs)}

## Usage Template

### Example: Generate Documentation for a Skill

```bash
python skills/{name}/{'generate_docs.py' if '.' in name else name + '.py'} path/to/skill.yaml
```

### Example: Preview Without Writing

```bash
python skills/{name}/{'generate_docs.py' if '.' in name else name + '.py'} \\
  path/to/skill.yaml \\
  --dry-run=true
```

### Example: Overwrite Existing Documentation

```bash
python skills/{name}/{'generate_docs.py' if '.' in name else name + '.py'} \\
  path/to/skill.yaml \\
  --overwrite=true
```

## Integration Notes

### Use in Workflows

```yaml
# workflows/documentation.yaml
steps:
  - skill: {name}
    args:
      - "skills/my.skill/skill.yaml"
      - "--overwrite=true"
```

### Use with Other Skills

```bash
# Generate documentation for a newly created skill
python skills/skill.create/skill_create.py my.new.skill
python skills/{name}/{'generate_docs.py' if '.' in name else name + '.py'} skills/my.new.skill/skill.yaml
```

### Batch Documentation Generation

```bash
# Generate docs for all skills
for manifest in skills/*/skill.yaml; do
  python skills/{name}/{'generate_docs.py' if '.' in name else name + '.py'} "$manifest" --overwrite=true
done
```

## Output Structure

The generated SKILL.md includes:

1. **Overview** - Skill name and brief description
2. **Purpose** - Detailed explanation of what the skill does
3. **Usage** - Command-line usage examples
4. **Parameters** - Detailed input parameter documentation
5. **Outputs** - Description of skill outputs
6. **Usage Template** - Practical examples
7. **Integration Notes** - How to use with workflows and other skills

## Dependencies

"""

    if dependencies:
        for dep in dependencies:
            doc += f"- **{dep}**: Required dependency\n"
    else:
        doc += "_No external dependencies_\n"

    doc += "\n## Tags\n\n"
    if tags:
        doc += ', '.join(f'`{tag}`' for tag in tags) + '\n'
    else:
        doc += "_No tags defined_\n"

    doc += f"""
## See Also

- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [Skill Development Guide](../../docs/skill-development.md) - Creating new skills

## Version

**{version}** - Generated documentation from skill manifest
"""

    return doc


def generate_docs(
    manifest_path: str,
    overwrite: bool = False,
    dry_run: bool = False,
    output_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate SKILL.md documentation from a skill manifest.

    Args:
        manifest_path: Path to skill.yaml file
        overwrite: Whether to overwrite existing SKILL.md
        dry_run: Preview without writing
        output_path: Custom output path (optional)

    Returns:
        Result dictionary with doc path and content

    Raises:
        BettyError: If manifest is invalid or file operations fail
    """
    # Load manifest
    manifest = load_skill_manifest(manifest_path)

    # Generate documentation
    doc_content = generate_skill_documentation(manifest)

    # Determine output path
    if output_path:
        doc_path = Path(output_path)
    else:
        # Default to same directory as manifest
        manifest_file = Path(manifest_path)
        doc_path = manifest_file.parent / "SKILL.md"

    # Check if file exists and overwrite is False
    if doc_path.exists() and not overwrite and not dry_run:
        raise BettyError(
            f"SKILL.md already exists at {doc_path}. "
            f"Use --overwrite=true to replace it or --dry-run=true to preview."
        )

    result = {
        "doc_path": str(doc_path),
        "doc_content": doc_content,
        "skill_name": manifest.get('name', 'unknown'),
        "dry_run": dry_run
    }

    if dry_run:
        result["dry_run_preview"] = doc_content
        logger.info(f"DRY RUN: Would write documentation to {doc_path}")
        print("\n" + "="*80)
        print("DRY RUN PREVIEW")
        print("="*80)
        print(doc_content)
        print("="*80)
        return result

    # Write documentation to file
    try:
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        with open(doc_path, 'w') as f:
            f.write(doc_content)
        logger.info(f"Generated SKILL.md at {doc_path}")
    except Exception as e:
        raise BettyError(f"Failed to write documentation: {e}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate or update SKILL.md documentation from skill.yaml manifest"
    )
    parser.add_argument(
        "manifest_path",
        type=str,
        help="Path to skill.yaml manifest file"
    )
    parser.add_argument(
        "--overwrite",
        type=lambda x: x.lower() in ['true', '1', 'yes'],
        default=False,
        help="Overwrite existing SKILL.md file (default: false)"
    )
    parser.add_argument(
        "--dry-run",
        type=lambda x: x.lower() in ['true', '1', 'yes'],
        default=False,
        help="Preview without writing to disk (default: false)"
    )
    parser.add_argument(
        "--output-path",
        type=str,
        help="Custom output path for SKILL.md (optional)"
    )

    args = parser.parse_args()

    try:
        # Check if PyYAML is installed
        try:
            import yaml
        except ImportError:
            raise BettyError(
                "PyYAML is required for generate.docs. Install with: pip install pyyaml"
            )

        # Generate documentation
        logger.info(f"Generating documentation from {args.manifest_path}")
        result = generate_docs(
            manifest_path=args.manifest_path,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            output_path=args.output_path
        )

        # Return structured result
        output = {
            "status": "success",
            "data": result
        }

        if not args.dry_run:
            print(json.dumps(output, indent=2))

    except Exception as e:
        logger.error(f"Failed to generate documentation: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
