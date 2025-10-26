#!/usr/bin/env python3
"""
artifact.create skill - AI-assisted artifact generation from templates

Loads templates based on artifact type, populates them with user-provided context,
and generates professional, ready-to-use artifacts.
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Tuple
import re
import yaml

# Add parent directory to path for governance imports
from betty.governance import enforce_governance, log_governance_action


def load_artifact_registry() -> Dict[str, Any]:
    """Load artifact registry from artifact.define skill"""
    registry_file = Path(__file__).parent.parent / "artifact.define" / "artifact_define.py"

    if not registry_file.exists():
        raise FileNotFoundError(f"Artifact registry not found: {registry_file}")

    with open(registry_file, 'r') as f:
        content = f.read()

    # Find KNOWN_ARTIFACT_TYPES dictionary
    start_marker = "KNOWN_ARTIFACT_TYPES = {"
    start_idx = content.find(start_marker)
    if start_idx == -1:
        raise ValueError("Could not find KNOWN_ARTIFACT_TYPES in registry file")

    start_idx += len(start_marker) - 1  # Include the {

    # Find matching closing brace
    brace_count = 0
    end_idx = start_idx
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break

    dict_str = content[start_idx:end_idx]
    artifacts = eval(dict_str)  # Safe since it's our own code
    return artifacts


def find_template_path(artifact_type: str) -> Optional[Path]:
    """Find the template file for a given artifact type"""
    templates_dir = Path(__file__).parent.parent.parent / "templates"

    if not templates_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {templates_dir}")

    # Search all subdirectories for the template
    for template_file in templates_dir.rglob(f"{artifact_type}.*"):
        if template_file.is_file() and template_file.suffix in ['.yaml', '.yml', '.md']:
            return template_file

    return None


def get_artifact_description_path(artifact_type: str) -> Optional[Path]:
    """Get path to artifact description file for reference"""
    desc_dir = Path(__file__).parent.parent.parent / "artifact_descriptions"
    desc_file = desc_dir / f"{artifact_type}.md"

    if desc_file.exists():
        return desc_file
    return None


def substitute_metadata(template_content: str, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Substitute metadata placeholders in template"""
    if metadata is None:
        metadata = {}

    # Default metadata
    today = datetime.now().strftime("%Y-%m-%d")
    defaults = {
        'date': today,
        'your_name': metadata.get('author', 'TODO: Add author name'),
        'role': metadata.get('role', 'TODO: Define role'),
        'approver_name': metadata.get('approver_name', 'TODO: Add approver name'),
        'approver_role': metadata.get('approver_role', 'TODO: Add approver role'),
        'artifact_type': metadata.get('artifact_type', 'TODO: Specify artifact type'),
        'path': metadata.get('path', 'TODO: Add path'),
    }

    # Override with provided metadata
    defaults.update(metadata)

    # Perform substitutions
    result = template_content
    for key, value in defaults.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))

    return result


def populate_yaml_template(template_content: str, context: str, artifact_type: str) -> str:
    """Populate YAML template with context-aware content"""

    # Parse the template to understand structure
    lines = template_content.split('\n')
    result_lines = []
    in_content_section = False

    for line in lines:
        # Check if we're entering the content section
        if line.strip().startswith('content:') or line.strip().startswith('# Content'):
            in_content_section = True
            result_lines.append(line)
            continue

        # If we're in content section and find a TODO, replace with context hint
        if in_content_section and 'TODO:' in line:
            indent = len(line) - len(line.lstrip())
            # Keep the TODO but add a hint about using the context
            result_lines.append(line)
            result_lines.append(f"{' ' * indent}# Context provided: {context[:100]}...")
        else:
            result_lines.append(line)

    return '\n'.join(result_lines)


def populate_markdown_template(template_content: str, context: str, artifact_type: str) -> str:
    """Populate Markdown template with context-aware content"""

    # Add context as a note in the document
    lines = template_content.split('\n')
    result_lines = []

    # Find the first heading and add context after it
    first_heading_found = False
    for line in lines:
        result_lines.append(line)

        if not first_heading_found and line.startswith('# '):
            first_heading_found = True
            result_lines.append('')
            result_lines.append(f'> **Context**: {context}')
            result_lines.append('')

    return '\n'.join(result_lines)


def load_existing_artifact_metadata(artifact_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load metadata from an existing artifact file.

    Args:
        artifact_path: Path to the existing artifact file

    Returns:
        Dictionary containing artifact metadata, or None if file doesn't exist
    """
    if not artifact_path.exists():
        return None

    try:
        with open(artifact_path, 'r') as f:
            content = f.read()

        # Try to parse as YAML first
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and 'metadata' in data:
                return data['metadata']
        except yaml.YAMLError:
            pass

        # If YAML parsing fails or no metadata found, return None
        return None

    except Exception as e:
        # If we can't read the file, return None
        return None


def generate_artifact(
    artifact_type: str,
    context: str,
    output_path: str,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Generate an artifact from template with AI-assisted population

    Args:
        artifact_type: Type of artifact (must exist in KNOWN_ARTIFACT_TYPES)
        context: Business context for populating the artifact
        output_path: Where to save the generated artifact
        metadata: Optional metadata overrides

    Returns:
        Generation report with status, path, and details
    """

    # Validate artifact type
    artifacts = load_artifact_registry()
    if artifact_type not in artifacts:
        return {
            'success': False,
            'error': f"Unknown artifact type: {artifact_type}",
            'available_types': list(artifacts.keys())[:10]  # Show first 10 as hint
        }

    # Find template
    template_path = find_template_path(artifact_type)
    if not template_path:
        return {
            'success': False,
            'error': f"No template found for artifact type: {artifact_type}",
            'artifact_type': artifact_type
        }

    # Load template
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Determine format
    artifact_format = template_path.suffix.lstrip('.')

    # Substitute metadata placeholders
    populated_content = substitute_metadata(template_content, metadata)

    # Populate with context
    if artifact_format in ['yaml', 'yml']:
        populated_content = populate_yaml_template(populated_content, context, artifact_type)
    elif artifact_format == 'md':
        populated_content = populate_markdown_template(populated_content, context, artifact_type)

    # Ensure output directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Governance check: Enforce governance on existing artifact before overwriting
    existing_metadata = load_existing_artifact_metadata(output_file)
    if existing_metadata:
        try:
            # Add artifact ID if not present
            if 'id' not in existing_metadata:
                existing_metadata['id'] = str(output_file)

            enforce_governance(existing_metadata)

            # Log successful governance check
            log_governance_action(
                artifact_id=existing_metadata.get('id', str(output_file)),
                action="write",
                outcome="allowed",
                message="Governance check passed, allowing artifact update",
                metadata={
                    'artifact_type': artifact_type,
                    'output_path': str(output_file)
                }
            )

        except PermissionError as e:
            # Governance policy violation - return error
            return {
                'success': False,
                'error': f"Governance policy violation: {str(e)}",
                'artifact_type': artifact_type,
                'policy_violation': True,
                'existing_metadata': existing_metadata
            }
        except ValueError as e:
            # Invalid metadata - log warning but allow write
            log_governance_action(
                artifact_id=str(output_file),
                action="write",
                outcome="warning",
                message=f"Invalid metadata in existing artifact: {str(e)}",
                metadata={
                    'artifact_type': artifact_type,
                    'output_path': str(output_file)
                }
            )

    # Save generated artifact
    with open(output_file, 'w') as f:
        f.write(populated_content)

    # Get artifact description path for reference
    desc_path = get_artifact_description_path(artifact_type)

    # Generate report
    report = {
        'success': True,
        'artifact_file': str(output_file.absolute()),
        'artifact_type': artifact_type,
        'artifact_format': artifact_format,
        'template_used': str(template_path.name),
        'artifact_description': str(desc_path) if desc_path else None,
        'context_length': len(context),
        'generated_at': datetime.now().isoformat(),
        'next_steps': [
            f"Review the generated artifact at: {output_file}",
            f"Refer to comprehensive guidance at: {desc_path}" if desc_path else "Review and customize the content",
            "Replace any remaining TODO markers with specific information",
            "Validate the artifact structure and content",
            "Update metadata (status, approvers, etc.) as needed"
        ]
    }

    return report


def main():
    """Main entry point for artifact.create skill"""
    parser = argparse.ArgumentParser(
        description='Create artifacts from templates with AI-assisted population'
    )
    parser.add_argument(
        'artifact_type',
        type=str,
        help='Type of artifact to create (e.g., business-case, threat-model)'
    )
    parser.add_argument(
        'context',
        type=str,
        help='Business context for populating the artifact'
    )
    parser.add_argument(
        'output_path',
        type=str,
        help='Path where the generated artifact should be saved'
    )
    parser.add_argument(
        '--author',
        type=str,
        help='Author name for metadata'
    )
    parser.add_argument(
        '--classification',
        type=str,
        choices=['Public', 'Internal', 'Confidential', 'Restricted'],
        help='Document classification level'
    )

    args = parser.parse_args()

    # Build metadata from arguments
    metadata = {}
    if args.author:
        metadata['author'] = args.author
        metadata['your_name'] = args.author
    if args.classification:
        metadata['classification'] = args.classification

    # Generate artifact
    report = generate_artifact(
        artifact_type=args.artifact_type,
        context=args.context,
        output_path=args.output_path,
        metadata=metadata if metadata else None
    )

    # Print report
    if report['success']:
        print(f"\n{'='*70}")
        print(f"✓ Artifact Generated Successfully")
        print(f"{'='*70}")
        print(f"Type:     {report['artifact_type']}")
        print(f"Format:   {report['artifact_format']}")
        print(f"Output:   {report['artifact_file']}")
        if report.get('artifact_description'):
            print(f"Guide:    {report['artifact_description']}")
        print(f"\nNext Steps:")
        for i, step in enumerate(report['next_steps'], 1):
            print(f"  {i}. {step}")
        print(f"{'='*70}\n")
        return 0
    else:
        print(f"\n{'='*70}")
        print(f"✗ Artifact Generation Failed")
        print(f"{'='*70}")
        print(f"Error: {report['error']}")
        if 'available_types' in report:
            print(f"\nAvailable artifact types (showing first 10):")
            for atype in report['available_types']:
                print(f"  - {atype}")
            print(f"  ... and more")
        print(f"{'='*70}\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
