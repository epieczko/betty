#!/usr/bin/env python3
"""
Artifact Type Validation Skill for Betty Framework

Validates artifact type names against registry/artifact_types.json and provides
fuzzy matching suggestions for invalid types using:
- Singular/plural detection
- Generic vs specific variant matching
- Levenshtein distance for typos

Usage:
    python artifact_validate_types.py --artifact_types '["threat-model", "data-flow-diagram"]'
"""

import argparse
import json
import logging
import os
import sys
from difflib import get_close_matches
from pathlib import Path
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_artifact_registry(registry_path: str = "registry/artifact_types.json") -> Dict[str, Any]:
    """
    Load the artifact types registry.

    Args:
        registry_path: Path to artifact_types.json

    Returns:
        Dictionary with artifact types indexed by name

    Raises:
        FileNotFoundError: If registry file doesn't exist
        json.JSONDecodeError: If registry file is invalid JSON
    """
    if not os.path.exists(registry_path):
        raise FileNotFoundError(f"Artifact registry not found: {registry_path}")

    try:
        with open(registry_path, 'r') as f:
            registry = json.load(f)

        # Index by name for O(1) lookup
        artifact_types_dict = {
            artifact['name']: artifact
            for artifact in registry.get('artifact_types', [])
        }

        logger.info(f"Loaded {len(artifact_types_dict)} artifact types from registry")
        return artifact_types_dict

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in registry file: {e}")
        raise


def find_similar_types(
    invalid_type: str,
    all_types: List[str],
    max_suggestions: int = 3
) -> List[Dict[str, str]]:
    """
    Find similar artifact types using multiple strategies.

    Strategies:
    1. Singular/Plural variants (high confidence)
    2. Generic vs Specific variants (medium confidence)
    3. Levenshtein distance for typos (low confidence)

    Args:
        invalid_type: The artifact type that wasn't found
        all_types: List of all valid artifact type names
        max_suggestions: Maximum number of suggestions to return

    Returns:
        List of suggestion dictionaries with type, reason, and confidence
    """
    suggestions = []

    # Strategy 1: Singular/Plural variants
    if invalid_type.endswith('s'):
        singular = invalid_type[:-1]
        if singular in all_types:
            suggestions.append({
                'type': singular,
                'reason': 'Singular form',
                'confidence': 'high'
            })
    else:
        plural = invalid_type + 's'
        if plural in all_types:
            suggestions.append({
                'type': plural,
                'reason': 'Plural form',
                'confidence': 'high'
            })

    # Strategy 2: Generic vs Specific variants
    # e.g., "data-model" → ["logical-data-model", "physical-data-model"]
    if '-' in invalid_type:
        parts = invalid_type.split('-')
        base_term = parts[-1]  # e.g., "model" from "data-model"

        # Find types that end with "-{base_term}"
        matches = [t for t in all_types if t.endswith('-' + base_term)]

        for match in matches[:max_suggestions]:
            if match not in [s['type'] for s in suggestions]:
                suggestions.append({
                    'type': match,
                    'reason': f'Specific variant of {base_term}',
                    'confidence': 'medium'
                })

    # Strategy 3: Levenshtein distance for typos
    close_matches = get_close_matches(
        invalid_type,
        all_types,
        n=max_suggestions,
        cutoff=0.6  # 60% similarity threshold
    )

    for match in close_matches:
        if match not in [s['type'] for s in suggestions]:
            suggestions.append({
                'type': match,
                'reason': 'Similar spelling',
                'confidence': 'low'
            })

    return suggestions[:max_suggestions]


def validate_artifact_types(
    artifact_types: List[str],
    check_schemas: bool = True,
    suggest_alternatives: bool = True,
    max_suggestions: int = 3,
    registry_path: str = "registry/artifact_types.json"
) -> Dict[str, Any]:
    """
    Validate artifact types against the registry.

    Args:
        artifact_types: List of artifact type names to validate
        check_schemas: Whether to verify schema files exist
        suggest_alternatives: Whether to suggest similar types for invalid ones
        max_suggestions: Maximum suggestions per invalid type
        registry_path: Path to artifact registry JSON file

    Returns:
        Dictionary with validation results:
        {
            'validation_results': {type_name: {valid, file_pattern, ...}},
            'all_valid': bool,
            'invalid_types': [type_names],
            'suggestions': {type_name: [suggestions]},
            'warnings': [warning_messages]
        }
    """
    # Load registry
    artifact_types_dict = load_artifact_registry(registry_path)
    all_type_names = list(artifact_types_dict.keys())

    # Initialize results
    results = {}
    invalid_types = []
    suggestions_dict = {}
    warnings = []

    # Validate each type
    for artifact_type in artifact_types:
        if artifact_type in artifact_types_dict:
            # Valid - get metadata
            metadata = artifact_types_dict[artifact_type]

            # Check schema file exists (if check_schemas=true)
            if check_schemas and metadata.get('schema'):
                schema_path = metadata['schema']
                if not os.path.exists(schema_path):
                    warning_msg = f"Schema file missing: {schema_path}"
                    warnings.append(warning_msg)
                    logger.warning(warning_msg)

            results[artifact_type] = {
                'valid': True,
                'file_pattern': metadata.get('file_pattern'),
                'content_type': metadata.get('content_type'),
                'schema': metadata.get('schema'),
                'description': metadata.get('description')
            }

            logger.info(f"✓ {artifact_type} - valid")

        else:
            # Invalid - mark as invalid and find suggestions
            results[artifact_type] = {'valid': False}
            invalid_types.append(artifact_type)

            logger.warning(f"✗ {artifact_type} - not found in registry")

            # Generate suggestions if enabled
            if suggest_alternatives:
                suggestions = find_similar_types(
                    artifact_type,
                    all_type_names,
                    max_suggestions
                )
                if suggestions:
                    suggestions_dict[artifact_type] = suggestions
                    logger.info(
                        f"  Suggestions for '{artifact_type}': "
                        f"{', '.join(s['type'] for s in suggestions)}"
                    )

    # Compile final results
    return {
        'validation_results': results,
        'all_valid': len(invalid_types) == 0,
        'invalid_types': invalid_types,
        'suggestions': suggestions_dict,
        'warnings': warnings
    }


def main():
    """Main entry point for artifact.validate.types skill."""
    parser = argparse.ArgumentParser(
        description="Validate artifact types against Betty Framework registry"
    )

    parser.add_argument(
        '--artifact_types',
        type=str,
        required=True,
        help='JSON array of artifact type names to validate (e.g., \'["threat-model", "data-flow-diagram"]\')'
    )

    parser.add_argument(
        '--check_schemas',
        type=bool,
        default=True,
        help='Whether to verify schema files exist on filesystem (default: true)'
    )

    parser.add_argument(
        '--suggest_alternatives',
        type=bool,
        default=True,
        help='Whether to suggest similar types for invalid ones (default: true)'
    )

    parser.add_argument(
        '--max_suggestions',
        type=int,
        default=3,
        help='Maximum number of suggestions per invalid type (default: 3)'
    )

    parser.add_argument(
        '--registry_path',
        type=str,
        default='registry/artifact_types.json',
        help='Path to artifact registry file (default: registry/artifact_types.json)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file path for validation report (optional)'
    )

    args = parser.parse_args()

    try:
        # Parse artifact_types JSON
        artifact_types = json.loads(args.artifact_types)

        if not isinstance(artifact_types, list):
            logger.error("artifact_types must be a JSON array")
            sys.exit(1)

        logger.info(f"Validating {len(artifact_types)} artifact types...")

        # Perform validation
        result = validate_artifact_types(
            artifact_types=artifact_types,
            check_schemas=args.check_schemas,
            suggest_alternatives=args.suggest_alternatives,
            max_suggestions=args.max_suggestions,
            registry_path=args.registry_path
        )

        # Add metadata
        result['ok'] = result['all_valid']
        result['status'] = 'success' if result['all_valid'] else 'validation_failed'

        # Save to file if output path specified
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)

            logger.info(f"Validation report saved to: {output_path}")
            result['validation_report_path'] = str(output_path)

        # Print results
        print(json.dumps(result, indent=2))

        # Exit with error code if validation failed
        sys.exit(0 if result['all_valid'] else 1)

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in artifact_types parameter: {e}")
        print(json.dumps({
            'ok': False,
            'status': 'error',
            'error': f'Invalid JSON: {str(e)}'
        }, indent=2))
        sys.exit(1)

    except FileNotFoundError as e:
        logger.error(str(e))
        print(json.dumps({
            'ok': False,
            'status': 'error',
            'error': str(e)
        }, indent=2))
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(json.dumps({
            'ok': False,
            'status': 'error',
            'error': str(e)
        }, indent=2))
        sys.exit(1)


if __name__ == '__main__':
    main()
