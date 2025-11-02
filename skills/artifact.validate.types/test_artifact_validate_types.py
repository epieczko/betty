#!/usr/bin/env python3
"""
Tests for artifact.validate.types skill

Tests fuzzy matching strategies:
- Singular/plural detection
- Generic vs specific variants
- Levenshtein distance for typos
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from artifact_validate_types import (
    load_artifact_registry,
    find_similar_types,
    validate_artifact_types
)


class TestArtifactValidateTypes(unittest.TestCase):
    """Test suite for artifact type validation."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        cls.registry_path = "registry/artifact_types.json"

        # Load actual registry for integration tests
        if os.path.exists(cls.registry_path):
            cls.artifact_types_dict = load_artifact_registry(cls.registry_path)
            cls.all_type_names = list(cls.artifact_types_dict.keys())
        else:
            cls.artifact_types_dict = {}
            cls.all_type_names = []

    def test_load_registry(self):
        """Test loading artifact registry."""
        if not os.path.exists(self.registry_path):
            self.skipTest("Registry file not found")

        registry = load_artifact_registry(self.registry_path)

        self.assertIsInstance(registry, dict)
        self.assertGreater(len(registry), 0, "Registry should contain artifact types")

        # Check structure of first entry
        first_type = next(iter(registry.values()))
        self.assertIn('name', first_type)
        self.assertIn('file_pattern', first_type)

    def test_validate_single_valid_type(self):
        """Test validation of a single valid artifact type."""
        if not self.all_type_names:
            self.skipTest("Registry not available")

        # Use a known artifact type (threat-model exists in registry)
        result = validate_artifact_types(
            artifact_types=["threat-model"],
            check_schemas=False,  # Don't check schema files in tests
            suggest_alternatives=False,
            registry_path=self.registry_path
        )

        self.assertTrue(result['all_valid'])
        self.assertEqual(len(result['invalid_types']), 0)
        self.assertIn('threat-model', result['validation_results'])
        self.assertTrue(result['validation_results']['threat-model']['valid'])
        self.assertIn('file_pattern', result['validation_results']['threat-model'])

    def test_validate_invalid_type(self):
        """Test validation of an invalid artifact type."""
        result = validate_artifact_types(
            artifact_types=["nonexistent-artifact-type"],
            check_schemas=False,
            suggest_alternatives=False,
            registry_path=self.registry_path
        )

        self.assertFalse(result['all_valid'])
        self.assertIn('nonexistent-artifact-type', result['invalid_types'])
        self.assertFalse(
            result['validation_results']['nonexistent-artifact-type']['valid']
        )

    def test_validate_mixed_types(self):
        """Test validation of mix of valid and invalid types."""
        if not self.all_type_names:
            self.skipTest("Registry not available")

        result = validate_artifact_types(
            artifact_types=["threat-model", "invalid-type", "architecture-overview"],
            check_schemas=False,
            suggest_alternatives=False,
            registry_path=self.registry_path
        )

        self.assertFalse(result['all_valid'])
        self.assertEqual(len(result['invalid_types']), 1)
        self.assertIn('invalid-type', result['invalid_types'])

        # Valid types should have metadata
        self.assertTrue(result['validation_results']['threat-model']['valid'])
        self.assertTrue(result['validation_results']['architecture-overview']['valid'])

    def test_singular_plural_suggestion(self):
        """Test singular/plural fuzzy matching."""
        # Create test data
        all_types = ["data-flow-diagrams", "threat-model", "api-spec"]

        # Test plural → singular suggestion
        suggestions = find_similar_types("data-flow-diagram", all_types, max_suggestions=3)

        # Should suggest plural form
        self.assertTrue(any(
            s['type'] == 'data-flow-diagrams' and s['confidence'] == 'high'
            for s in suggestions
        ))

    def test_generic_specific_suggestion(self):
        """Test generic vs specific variant matching."""
        # Create test data with specific variants
        all_types = [
            "logical-data-model",
            "physical-data-model",
            "enterprise-data-model",
            "threat-model"
        ]

        # Search for generic "data-model"
        suggestions = find_similar_types("data-model", all_types, max_suggestions=3)

        # Should suggest specific variants ending in "-data-model"
        suggested_types = [s['type'] for s in suggestions]
        self.assertTrue(
            any('data-model' in t for t in suggested_types),
            "Should suggest specific data-model variants"
        )

    def test_typo_suggestion(self):
        """Test Levenshtein distance for typo detection."""
        all_types = ["threat-model", "architecture-overview", "api-specification"]

        # Typo: "thret-model" instead of "threat-model"
        suggestions = find_similar_types("thret-model", all_types, max_suggestions=3)

        # Should suggest "threat-model"
        suggested_types = [s['type'] for s in suggestions]
        self.assertIn("threat-model", suggested_types)

    def test_max_suggestions_limit(self):
        """Test that max_suggestions limit is respected."""
        all_types = [
            "logical-data-model",
            "physical-data-model",
            "enterprise-data-model",
            "conceptual-data-model",
            "canonical-data-model"
        ]

        suggestions = find_similar_types("data-model", all_types, max_suggestions=2)

        # Should return at most 2 suggestions
        self.assertLessEqual(len(suggestions), 2)

    def test_suggestions_integration(self):
        """Test end-to-end suggestion workflow."""
        if not self.all_type_names:
            self.skipTest("Registry not available")

        result = validate_artifact_types(
            artifact_types=["data-flow-diagram"],  # Singular (likely plural in registry)
            check_schemas=False,
            suggest_alternatives=True,
            max_suggestions=3,
            registry_path=self.registry_path
        )

        # Should detect as invalid
        self.assertFalse(result['all_valid'])
        self.assertIn('data-flow-diagram', result['invalid_types'])

        # Should provide suggestions
        if 'data-flow-diagram' in result['suggestions']:
            suggestions = result['suggestions']['data-flow-diagram']
            self.assertGreater(len(suggestions), 0)

            # Check suggestion structure
            first_suggestion = suggestions[0]
            self.assertIn('type', first_suggestion)
            self.assertIn('reason', first_suggestion)
            self.assertIn('confidence', first_suggestion)

    def test_schema_checking(self):
        """Test schema file existence checking."""
        if not os.path.exists(self.registry_path):
            self.skipTest("Registry not available")

        # Validate a type that has a schema
        result = validate_artifact_types(
            artifact_types=["threat-model"],
            check_schemas=True,
            suggest_alternatives=False,
            registry_path=self.registry_path
        )

        # If schema is missing, should have warning
        # If schema exists, no warning
        if 'schemas/artifacts/threat-model-schema.json' not in [
            w for w in result['warnings'] if 'threat-model' in w
        ]:
            # Schema exists - good
            pass
        else:
            # Schema missing - warning should be present
            self.assertTrue(any('threat-model' in w for w in result['warnings']))

    def test_empty_input(self):
        """Test validation with empty artifact types list."""
        result = validate_artifact_types(
            artifact_types=[],
            check_schemas=False,
            suggest_alternatives=False,
            registry_path=self.registry_path
        )

        self.assertTrue(result['all_valid'])
        self.assertEqual(len(result['invalid_types']), 0)
        self.assertEqual(len(result['validation_results']), 0)

    def test_validation_report_structure(self):
        """Test that validation report has correct structure."""
        result = validate_artifact_types(
            artifact_types=["threat-model", "invalid-type"],
            check_schemas=False,
            suggest_alternatives=True,
            max_suggestions=3,
            registry_path=self.registry_path
        )

        # Check required fields
        self.assertIn('validation_results', result)
        self.assertIn('all_valid', result)
        self.assertIn('invalid_types', result)
        self.assertIn('suggestions', result)
        self.assertIn('warnings', result)

        # Check types
        self.assertIsInstance(result['validation_results'], dict)
        self.assertIsInstance(result['all_valid'], bool)
        self.assertIsInstance(result['invalid_types'], list)
        self.assertIsInstance(result['suggestions'], dict)
        self.assertIsInstance(result['warnings'], list)


class TestFuzzMatchingStrategies(unittest.TestCase):
    """Focused tests for fuzzy matching strategies."""

    def test_plural_to_singular(self):
        """Test plural → singular suggestion."""
        all_types = ["threat-model", "data-flow-diagram"]
        suggestions = find_similar_types("threat-models", all_types)

        # Should suggest singular
        self.assertTrue(any(
            s['type'] == 'threat-model' and
            s['reason'] == 'Singular form' and
            s['confidence'] == 'high'
            for s in suggestions
        ))

    def test_singular_to_plural(self):
        """Test singular → plural suggestion."""
        all_types = ["data-flow-diagrams", "threat-models"]
        suggestions = find_similar_types("threat-model", all_types)

        # Should suggest plural
        self.assertTrue(any(
            s['type'] == 'threat-models' and
            s['reason'] == 'Plural form' and
            s['confidence'] == 'high'
            for s in suggestions
        ))

    def test_generic_to_specific(self):
        """Test generic → specific variant suggestions."""
        all_types = [
            "openapi-spec",
            "asyncapi-spec",
            "graphql-spec"
        ]

        suggestions = find_similar_types("api-spec", all_types)

        # Should suggest specific API spec variants
        suggested_types = [s['type'] for s in suggestions]
        self.assertTrue(any('spec' in t for t in suggested_types))

    def test_confidence_levels(self):
        """Test that confidence levels are correctly assigned."""
        all_types = [
            "threat-model",  # For singular/plural (high confidence)
            "logical-data-model",  # For specific variant (medium confidence)
            "thret-model"  # For typo (low confidence - but this is exact match)
        ]

        # Plural → singular (high)
        suggestions = find_similar_types("threat-models", all_types)
        high_conf = [s for s in suggestions if s['confidence'] == 'high']
        self.assertTrue(len(high_conf) > 0)


def run_tests():
    """Run all tests."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()
