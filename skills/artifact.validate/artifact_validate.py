#!/usr/bin/env python3
"""
artifact.validate skill - Comprehensive artifact validation

Validates artifacts against structure, schema, and quality criteria.
Generates detailed validation reports with scores and recommendations.
"""

import sys
import os
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import yaml
import json


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

    start_idx += len(start_marker) - 1

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
    artifacts = eval(dict_str)
    return artifacts


def detect_artifact_type(file_path: Path, content: str) -> Optional[str]:
    """Detect artifact type from filename or content"""
    # Try to detect from filename
    filename = file_path.stem

    # Load registry to check against known types
    registry = load_artifact_registry()

    # Direct match
    if filename in registry:
        return filename

    # Check for partial matches
    for artifact_type in registry.keys():
        if artifact_type in filename:
            return artifact_type

    # Try to detect from content (YAML metadata)
    if file_path.suffix in ['.yaml', '.yml']:
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and 'metadata' in data:
                # Check for artifact type in metadata
                metadata = data['metadata']
                if 'artifactType' in metadata:
                    return metadata['artifactType']
        except:
            pass

    return None


def validate_yaml_syntax(content: str) -> Tuple[bool, Optional[str]]:
    """Validate YAML syntax"""
    try:
        yaml.safe_load(content)
        return True, None
    except yaml.YAMLError as e:
        return False, f"YAML syntax error: {str(e)}"


def validate_markdown_structure(content: str) -> Tuple[bool, List[str]]:
    """Validate Markdown structure"""
    issues = []

    # Check for at least one heading
    if not re.search(r'^#+ ', content, re.MULTILINE):
        issues.append("No headings found - document should have structured sections")

    # Check for document control section
    if 'Document Control' not in content and 'Metadata' not in content:
        issues.append("Missing document control/metadata section")

    return len(issues) == 0, issues


def check_metadata_completeness(data: Dict[str, Any], file_format: str) -> Dict[str, Any]:
    """Check metadata section completeness"""
    issues = []
    warnings = []
    metadata = {}

    if file_format in ['yaml', 'yml']:
        if 'metadata' not in data:
            issues.append("Missing 'metadata' section")
            return {
                'complete': False,
                'score': 0,
                'issues': issues,
                'warnings': warnings
            }

        metadata = data['metadata']

        # Required fields
        required = ['version', 'created', 'author', 'status']
        for field in required:
            if field not in metadata or not metadata[field] or metadata[field] == 'TODO':
                issues.append(f"Missing or incomplete required field: {field}")

        # Recommended fields
        recommended = ['lastModified', 'classification', 'documentOwner']
        for field in recommended:
            if field not in metadata or not metadata[field]:
                warnings.append(f"Missing recommended field: {field}")

        # Check for TODO placeholders
        if isinstance(metadata, dict):
            for key, value in metadata.items():
                if isinstance(value, str) and 'TODO' in value:
                    warnings.append(f"Field '{key}' contains TODO marker: {value}")

    score = max(0, 100 - (len(issues) * 25) - (len(warnings) * 10))

    return {
        'complete': len(issues) == 0,
        'score': score,
        'issues': issues,
        'warnings': warnings,
        'metadata': metadata
    }


def count_todo_markers(content: str) -> List[str]:
    """Count and locate TODO markers in content"""
    todos = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        if 'TODO' in line:
            # Extract the TODO text
            todo_text = line.strip()
            if len(todo_text) > 100:
                todo_text = todo_text[:100] + "..."
            todos.append(f"Line {i}: {todo_text}")

    return todos


def validate_required_sections(data: Dict[str, Any], artifact_type: str, file_format: str) -> Dict[str, Any]:
    """Validate that required sections are present"""
    issues = []
    warnings = []

    if file_format in ['yaml', 'yml']:
        # Common required sections for YAML artifacts
        if 'metadata' not in data:
            issues.append("Missing 'metadata' section")

        if 'content' not in data and artifact_type not in ['schema-definition', 'data-model']:
            warnings.append("Missing 'content' section - artifact may be incomplete")

        # Check for empty content
        if 'content' in data:
            content = data['content']
            if isinstance(content, dict):
                empty_fields = [k for k, v in content.items() if not v or (isinstance(v, str) and v.strip() == 'TODO: ')]
                if empty_fields:
                    warnings.append(f"Empty content fields: {', '.join(empty_fields)}")

    score = max(0, 100 - (len(issues) * 30) - (len(warnings) * 15))

    return {
        'valid': len(issues) == 0,
        'score': score,
        'issues': issues,
        'warnings': warnings
    }


def validate_against_schema(data: Dict[str, Any], schema_path: Optional[Path]) -> Dict[str, Any]:
    """Validate artifact against JSON schema if available"""
    if not schema_path or not schema_path.exists():
        return {
            'validated': False,
            'score': None,
            'message': 'No schema available for validation'
        }

    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)

        # Note: Would need jsonschema library for full validation
        # For now, just indicate schema was found
        return {
            'validated': False,
            'score': None,
            'message': 'Schema validation not yet implemented (requires jsonschema library)'
        }
    except Exception as e:
        return {
            'validated': False,
            'score': None,
            'message': f'Schema validation error: {str(e)}'
        }


def calculate_quality_score(validation_results: Dict[str, Any]) -> int:
    """Calculate overall quality score from validation results"""
    scores = []
    weights = []

    # Syntax validation (weight: 30%)
    if validation_results['syntax']['valid']:
        scores.append(100)
    else:
        scores.append(0)
    weights.append(0.30)

    # Metadata completeness (weight: 25%)
    scores.append(validation_results['metadata']['score'])
    weights.append(0.25)

    # Required sections (weight: 25%)
    scores.append(validation_results['sections']['score'])
    weights.append(0.25)

    # TODO markers - penalty (weight: 20%)
    todo_count = len(validation_results['todos'])
    todo_score = max(0, 100 - (todo_count * 5))
    scores.append(todo_score)
    weights.append(0.20)

    # Calculate weighted average
    quality_score = sum(s * w for s, w in zip(scores, weights))

    return int(quality_score)


def generate_recommendations(validation_results: Dict[str, Any]) -> List[str]:
    """Generate actionable recommendations based on validation results"""
    recommendations = []

    # Syntax issues
    if not validation_results['syntax']['valid']:
        recommendations.append("🔴 CRITICAL: Fix syntax errors before proceeding")

    # Metadata issues
    metadata = validation_results['metadata']
    if metadata['issues']:
        recommendations.append(f"🔴 Fix {len(metadata['issues'])} required metadata field(s)")
    if metadata['warnings']:
        recommendations.append(f"🟡 Complete {len(metadata['warnings'])} recommended metadata field(s)")

    # Section issues
    sections = validation_results['sections']
    if sections['issues']:
        recommendations.append(f"🔴 Add {len(sections['issues'])} required section(s)")
    if sections['warnings']:
        recommendations.append(f"🟡 Review {len(sections['warnings'])} section warning(s)")

    # TODO markers
    todo_count = len(validation_results['todos'])
    if todo_count > 0:
        if todo_count > 10:
            recommendations.append(f"🔴 Replace {todo_count} TODO markers with actual content")
        else:
            recommendations.append(f"🟡 Replace {todo_count} TODO marker(s) with actual content")

    # Quality score recommendations
    quality_score = validation_results['quality_score']
    if quality_score < 50:
        recommendations.append("🔴 Artifact needs significant work before it's ready for review")
    elif quality_score < 70:
        recommendations.append("🟡 Artifact needs refinement before it's ready for approval")
    elif quality_score < 90:
        recommendations.append("🟢 Artifact is good - minor improvements recommended")
    else:
        recommendations.append("✅ Artifact meets quality standards")

    return recommendations


def validate_artifact(
    artifact_path: str,
    artifact_type: Optional[str] = None,
    strict: bool = False,
    schema_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Validate an artifact against structure, schema, and quality criteria

    Args:
        artifact_path: Path to artifact file
        artifact_type: Type of artifact (auto-detected if not provided)
        strict: Strict mode - treat warnings as errors
        schema_path: Optional path to JSON schema

    Returns:
        Validation report with scores and recommendations
    """
    file_path = Path(artifact_path)

    # Check file exists
    if not file_path.exists():
        return {
            'success': False,
            'error': f"Artifact file not found: {artifact_path}",
            'is_valid': False,
            'quality_score': 0
        }

    # Read file
    with open(file_path, 'r') as f:
        content = f.read()

    # Detect format
    file_format = file_path.suffix.lstrip('.')
    if file_format not in ['yaml', 'yml', 'md']:
        return {
            'success': False,
            'error': f"Unsupported file format: {file_format}. Expected yaml, yml, or md",
            'is_valid': False,
            'quality_score': 0
        }

    # Detect or validate artifact type
    detected_type = detect_artifact_type(file_path, content)
    if artifact_type and detected_type and artifact_type != detected_type:
        print(f"Warning: Specified type '{artifact_type}' differs from detected type '{detected_type}'")

    final_type = artifact_type or detected_type or "unknown"

    # Initialize validation results
    validation_results = {
        'artifact_path': str(file_path.absolute()),
        'artifact_type': final_type,
        'file_format': file_format,
        'file_size': len(content),
        'validated_at': datetime.now().isoformat()
    }

    # 1. Syntax validation
    if file_format in ['yaml', 'yml']:
        is_valid, error = validate_yaml_syntax(content)
        validation_results['syntax'] = {
            'valid': is_valid,
            'error': error
        }

        # Parse for further validation
        if is_valid:
            data = yaml.safe_load(content)
        else:
            # Cannot continue without valid syntax
            return {
                'success': True,
                'validation_results': validation_results,
                'is_valid': False,
                'quality_score': 0,
                'recommendations': ['🔴 CRITICAL: Fix YAML syntax errors before proceeding']
            }
    else:  # Markdown
        is_valid, issues = validate_markdown_structure(content)
        validation_results['syntax'] = {
            'valid': is_valid,
            'issues': issues if not is_valid else []
        }
        data = {}  # Markdown doesn't parse to structured data

    # 2. Metadata completeness
    if file_format in ['yaml', 'yml']:
        validation_results['metadata'] = check_metadata_completeness(data, file_format)
    else:
        validation_results['metadata'] = {
            'complete': True,
            'score': 100,
            'issues': [],
            'warnings': []
        }

    # 3. TODO markers
    validation_results['todos'] = count_todo_markers(content)

    # 4. Required sections
    if file_format in ['yaml', 'yml']:
        validation_results['sections'] = validate_required_sections(data, final_type, file_format)
    else:
        validation_results['sections'] = {
            'valid': True,
            'score': 100,
            'issues': [],
            'warnings': []
        }

    # 5. Schema validation (if schema provided)
    if schema_path:
        validation_results['schema'] = validate_against_schema(data, Path(schema_path))

    # Calculate quality score
    quality_score = calculate_quality_score(validation_results)
    validation_results['quality_score'] = quality_score

    # Generate recommendations
    recommendations = generate_recommendations(validation_results)
    validation_results['recommendations'] = recommendations

    # Determine overall validity
    has_critical_issues = (
        not validation_results['syntax']['valid'] or
        len(validation_results['metadata']['issues']) > 0 or
        len(validation_results['sections']['issues']) > 0
    )

    has_warnings = (
        len(validation_results['metadata']['warnings']) > 0 or
        len(validation_results['sections']['warnings']) > 0 or
        len(validation_results['todos']) > 0
    )

    if strict:
        is_valid = not has_critical_issues and not has_warnings
    else:
        is_valid = not has_critical_issues

    return {
        'success': True,
        'validation_results': validation_results,
        'is_valid': is_valid,
        'quality_score': quality_score,
        'recommendations': recommendations
    }


def main():
    """Main entry point for artifact.validate skill"""
    parser = argparse.ArgumentParser(
        description='Validate artifacts against structure, schema, and quality criteria'
    )
    parser.add_argument(
        'artifact_path',
        type=str,
        help='Path to artifact file to validate'
    )
    parser.add_argument(
        '--artifact-type',
        type=str,
        help='Type of artifact (auto-detected if not provided)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Strict mode - treat warnings as errors'
    )
    parser.add_argument(
        '--schema-path',
        type=str,
        help='Path to JSON schema for validation'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save validation report to file'
    )

    args = parser.parse_args()

    # Validate artifact
    result = validate_artifact(
        artifact_path=args.artifact_path,
        artifact_type=args.artifact_type,
        strict=args.strict,
        schema_path=args.schema_path
    )

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)
        print(f"\nValidation report saved to: {output_path}")

    # Print report
    if not result['success']:
        print(f"\n{'='*70}")
        print(f"✗ Validation Failed")
        print(f"{'='*70}")
        print(f"Error: {result['error']}")
        print(f"{'='*70}\n")
        return 1

    vr = result['validation_results']

    print(f"\n{'='*70}")
    print(f"Artifact Validation Report")
    print(f"{'='*70}")
    print(f"Artifact:     {vr['artifact_path']}")
    print(f"Type:         {vr['artifact_type']}")
    print(f"Format:       {vr['file_format']}")
    print(f"Size:         {vr['file_size']} bytes")
    print(f"")
    print(f"Overall Status: {'✅ VALID' if result['is_valid'] else '❌ INVALID'}")
    print(f"Quality Score:  {result['quality_score']}/100")
    print(f"")

    # Syntax
    print(f"Syntax Validation:")
    if vr['syntax']['valid']:
        print(f"  ✅ Valid {vr['file_format'].upper()} syntax")
    else:
        print(f"  ❌ {vr['syntax'].get('error', 'Syntax errors found')}")
        if 'issues' in vr['syntax']:
            for issue in vr['syntax']['issues']:
                print(f"     - {issue}")
    print()

    # Metadata
    print(f"Metadata Completeness: {vr['metadata']['score']}/100")
    if vr['metadata']['issues']:
        print(f"  Issues:")
        for issue in vr['metadata']['issues']:
            print(f"    ❌ {issue}")
    if vr['metadata']['warnings']:
        print(f"  Warnings:")
        for warning in vr['metadata']['warnings']:
            print(f"    🟡 {warning}")
    if not vr['metadata']['issues'] and not vr['metadata']['warnings']:
        print(f"  ✅ All metadata fields complete")
    print()

    # Sections
    print(f"Required Sections: {vr['sections']['score']}/100")
    if vr['sections']['issues']:
        print(f"  Issues:")
        for issue in vr['sections']['issues']:
            print(f"    ❌ {issue}")
    if vr['sections']['warnings']:
        print(f"  Warnings:")
        for warning in vr['sections']['warnings']:
            print(f"    🟡 {warning}")
    if not vr['sections']['issues'] and not vr['sections']['warnings']:
        print(f"  ✅ All required sections present")
    print()

    # TODOs
    todo_count = len(vr['todos'])
    print(f"TODO Markers: {todo_count}")
    if todo_count > 0:
        print(f"  🟡 Found {todo_count} TODO marker(s) - artifact incomplete")
        if todo_count <= 5:
            for todo in vr['todos']:
                print(f"     - {todo}")
        else:
            for todo in vr['todos'][:5]:
                print(f"     - {todo}")
            print(f"     ... and {todo_count - 5} more")
    else:
        print(f"  ✅ No TODO markers found")
    print()

    # Recommendations
    print(f"Recommendations:")
    for rec in result['recommendations']:
        print(f"  {rec}")

    print(f"{'='*70}\n")

    return 0 if result['is_valid'] else 1


if __name__ == '__main__':
    sys.exit(main())
