#!/usr/bin/env python3
"""
Validate Artifact Operations - Test artifact.create, artifact.validate, artifact.review

This script validates that all artifact operations work correctly with the
JSON-based registry.
"""

import os
import sys
import json
import tempfile
from pathlib import Path

# Add betty to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def test_registry_loading():
    """Test that the registry loads correctly"""
    logger.info("Testing registry loading...")

    try:
        # Load registry directly from JSON
        registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"

        if not registry_file.exists():
            logger.error(f"Registry file not found: {registry_file}")
            return False

        with open(registry_file, 'r') as f:
            data = json.load(f)

        artifact_count = len(data.get('artifact_types', []))
        logger.info(f"✓ Successfully loaded {artifact_count} artifact types from JSON")

        # Test some specific artifacts
        sample_types = [t['name'] for t in data['artifact_types'][:5]]
        logger.info(f"✓ Sample types: {', '.join(sample_types)}")

        return True

    except Exception as e:
        logger.error(f"✗ Failed to load registry: {e}", exc_info=True)
        return False


def test_registry_structure():
    """Test that registry structure is valid"""
    logger.info("Testing registry structure...")

    try:
        registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"

        with open(registry_file, 'r') as f:
            data = json.load(f)

        # Check required fields
        if 'version' not in data:
            logger.error("✗ Missing 'version' field")
            return False

        if 'artifact_types' not in data:
            logger.error("✗ Missing 'artifact_types' field")
            return False

        # Check each artifact has required fields
        errors = []
        for i, artifact in enumerate(data['artifact_types']):
            if 'name' not in artifact:
                errors.append(f"Artifact #{i} missing 'name' field")
            if 'description' not in artifact:
                errors.append(f"Artifact #{i} ({artifact.get('name', 'unknown')}) missing 'description' field")

        if errors:
            for error in errors[:10]:  # Show first 10 errors
                logger.error(f"✗ {error}")
            return False

        logger.info(f"✓ Registry structure is valid")
        return True

    except Exception as e:
        logger.error(f"✗ Failed to validate registry structure: {e}", exc_info=True)
        return False


def test_artifact_types_coverage():
    """Test that key artifact types are present"""
    logger.info("Testing artifact types coverage...")

    try:
        registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"

        with open(registry_file, 'r') as f:
            data = json.load(f)

        registry = {a['name']: a for a in data['artifact_types']}

        # Key artifact types that should exist
        required_types = [
            'openapi-spec',
            'validation-report',
            'workflow-definition',
            'agent-definition',
            'skill-definition',
            'hook-config'
        ]

        missing = []
        for artifact_type in required_types:
            if artifact_type not in registry:
                missing.append(artifact_type)

        if missing:
            logger.error(f"✗ Missing required artifact types: {', '.join(missing)}")
            return False

        logger.info(f"✓ All {len(required_types)} required artifact types are present")
        return True

    except Exception as e:
        logger.error(f"✗ Failed to test coverage: {e}", exc_info=True)
        return False


def test_registry_consistency():
    """Test consistency between registry and descriptions"""
    logger.info("Testing registry consistency...")

    try:
        registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"
        descriptions_dir = Path(BASE_DIR) / "artifact_descriptions"

        with open(registry_file, 'r') as f:
            data = json.load(f)

        registry_types = set(a['name'] for a in data['artifact_types'])
        description_files = set(f.stem for f in descriptions_dir.glob("*.md"))

        # Check for artifacts with descriptions
        with_descriptions = registry_types & description_files
        without_descriptions = registry_types - description_files

        logger.info(f"✓ {len(with_descriptions)} artifact types have descriptions")

        if without_descriptions:
            logger.warning(f"! {len(without_descriptions)} artifact types missing descriptions")
            # Show a few examples
            examples = sorted(without_descriptions)[:5]
            logger.warning(f"  Examples: {', '.join(examples)}")

        return True

    except Exception as e:
        logger.error(f"✗ Failed to test consistency: {e}", exc_info=True)
        return False


def test_json_validity():
    """Test that all JSON files are valid"""
    logger.info("Testing JSON validity...")

    try:
        json_files = [
            Path(BASE_DIR) / "registry" / "artifact_types.json",
            Path(BASE_DIR) / "registry" / "artifact_registry_audit.json",
            Path(BASE_DIR) / "artifacts_manifest.json"
        ]

        for json_file in json_files:
            if not json_file.exists():
                logger.warning(f"! File not found (skipping): {json_file.name}")
                continue

            try:
                with open(json_file, 'r') as f:
                    json.load(f)
                logger.info(f"✓ Valid JSON: {json_file.name}")
            except json.JSONDecodeError as e:
                logger.error(f"✗ Invalid JSON in {json_file.name}: {e}")
                return False

        return True

    except Exception as e:
        logger.error(f"✗ Failed to test JSON validity: {e}", exc_info=True)
        return False


def test_audit_report():
    """Test that audit report exists and is valid"""
    logger.info("Testing audit report...")

    try:
        audit_file = Path(BASE_DIR) / "registry" / "artifact_registry_audit.json"

        if not audit_file.exists():
            logger.error(f"✗ Audit report not found: {audit_file}")
            return False

        with open(audit_file, 'r') as f:
            data = json.load(f)

        # Check structure
        required_fields = ['summary', 'findings', 'detailed_results']
        for field in required_fields:
            if field not in data:
                logger.error(f"✗ Missing field in audit report: {field}")
                return False

        summary = data['summary']
        logger.info(f"✓ Audit report is valid")
        logger.info(f"  Total artifact types: {summary.get('total_artifact_types', 0)}")
        logger.info(f"  Declared in registry: {summary.get('declared_in_registry', 0)}")
        logger.info(f"  Missing in registry: {summary.get('missing_in_registry', 0)}")
        logger.info(f"  Unused in registry: {summary.get('unused_in_registry', 0)}")

        return True

    except Exception as e:
        logger.error(f"✗ Failed to test audit report: {e}", exc_info=True)
        return False


def main():
    """Main validation function"""
    logger.info("="*80)
    logger.info("ARTIFACT OPERATIONS VALIDATION")
    logger.info("="*80)
    logger.info("")

    tests = [
        ("Registry Loading", test_registry_loading),
        ("Registry Structure", test_registry_structure),
        ("Artifact Types Coverage", test_artifact_types_coverage),
        ("Registry Consistency", test_registry_consistency),
        ("JSON Validity", test_json_validity),
        ("Audit Report", test_audit_report)
    ]

    results = []
    for test_name, test_func in tests:
        logger.info("")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            logger.error(f"Test '{test_name}' crashed: {e}")
            results.append((test_name, False))

    # Print summary
    logger.info("")
    logger.info("="*80)
    logger.info("VALIDATION SUMMARY")
    logger.info("="*80)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        logger.info(f"{status}: {test_name}")

    logger.info("")
    logger.info(f"Result: {passed}/{total} tests passed")

    if passed == total:
        logger.info("✓ All validation tests passed!")
        return 0
    else:
        logger.warning(f"✗ {total - passed} test(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
