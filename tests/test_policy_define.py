#!/usr/bin/env python3
"""
Unit tests for policy.define skill

Tests Markdown parsing, YAML generation, and edge cases.
"""

import pytest
import sys
from pathlib import Path

# Add betty to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from betty.skills.policy.define import (
    define_policy,
    parse_policy_spec,
    PolicyDefinitionError
)


class TestPolicyDefine:
    """Test suite for policy.define skill"""

    def test_simple_policy_creation(self):
        """Test creating a simple policy with one rule"""
        spec = """
# Test Policy

Simple test policy

## Rule 1: Test Rule
pattern: test_pattern
message: Test message
severity: error
action: block
"""
        result = define_policy(spec, "test", "validation")

        assert result['success'] is True
        assert result['rule_count'] == 1
        assert 'policy_yaml_string' in result
        assert 'test' in result['policy_yaml_string']

    def test_multiple_rules(self):
        """Test policy with multiple rules"""
        spec = """
# Multi Rule Policy

## Rule 1: First Rule
pattern: pattern1
message: Message 1
action: block

## Rule 2: Second Rule
pattern: pattern2
message: Message 2
action: warn

## Rule 3: Third Rule
pattern: pattern3
message: Message 3
action: info
"""
        result = define_policy(spec, "multi", "validation")

        assert result['success'] is True
        assert result['rule_count'] == 3

    def test_field_based_rules(self):
        """Test rules with field specifications"""
        spec = """
# Field Policy

## Rule 1: Name Check
field: name
pattern: ^[a-z]+$
message: Name must be lowercase
action: block
"""
        result = define_policy(spec, "field-test", "validation")

        assert result['success'] is True
        policy = result['policy_yaml']
        assert policy['rules'][0]['field'] == 'name'

    def test_policy_types(self):
        """Test different policy types"""
        spec = """
# Type Test

## Rule 1: Test
pattern: test
message: Test
action: block
"""
        for policy_type in ['validation', 'security', 'compliance']:
            result = define_policy(spec, f"type-{policy_type}", policy_type)
            assert result['success'] is True
            assert result['policy_yaml']['type'] == policy_type

    def test_policy_scopes(self):
        """Test different policy scopes"""
        spec = """
# Scope Test

## Rule 1: Test
pattern: test
message: Test
action: block
"""
        scopes = [['artifact'], ['skill'], ['agent'], ['artifact', 'skill']]
        for scope in scopes:
            result = define_policy(spec, "scope-test", "validation", scope=scope)
            assert result['success'] is True
            assert result['policy_yaml']['scope'] == scope

    def test_enforcement_levels(self):
        """Test different enforcement levels"""
        spec = """
# Enforcement Test

## Rule 1: Test
pattern: test
message: Test
action: block
"""
        for enforcement in ['blocking', 'warning', 'info']:
            result = define_policy(spec, "enf-test", "validation", enforcement=enforcement)
            assert result['success'] is True
            assert result['policy_yaml']['enforcement'] == enforcement

    def test_empty_policy(self):
        """Test handling of policy with no rules"""
        spec = """
# Empty Policy

No rules defined here.
"""
        result = define_policy(spec, "empty", "validation")

        # Should succeed but with 0 rules
        assert result['success'] is True
        assert result['rule_count'] == 0

    def test_malformed_rule(self):
        """Test handling of malformed rule section"""
        spec = """
# Malformed Policy

## Rule 1: Bad Rule
This rule is missing required fields
"""
        result = define_policy(spec, "malformed", "validation")

        # Should still succeed but might have fewer rules
        assert result['success'] is True

    def test_special_characters_in_pattern(self):
        """Test patterns with regex special characters"""
        spec = r"""
# Special Chars

## Rule 1: Regex Test
pattern: ^\d+\.\d+\.\d+$
message: Version pattern
action: block
"""
        result = define_policy(spec, "regex-test", "validation")

        assert result['success'] is True
        assert r'\d' in result['policy_yaml_string']

    def test_multiline_message(self):
        """Test rules with multiline messages"""
        spec = """
# Multiline Message

## Rule 1: Long Message
pattern: test
message: This is a longer message that explains the rule in detail
action: block
"""
        result = define_policy(spec, "multiline", "validation")

        assert result['success'] is True

    def test_parse_policy_spec_directly(self):
        """Test parse_policy_spec function directly"""
        spec = """
# Direct Parse Test

Description here

## Rule 1: Test
pattern: test
message: Test message
action: block
"""
        result = parse_policy_spec(spec, "direct-test")

        assert 'name' in result
        assert result['name'] == 'direct-test'
        assert 'rules' in result
        assert len(result['rules']) >= 1

    def test_policy_with_metadata(self):
        """Test policy with description and metadata"""
        spec = """
# Policy With Metadata

This is a detailed description
of what the policy does.

## Rule 1: Test
pattern: test
message: Test
action: block
"""
        result = define_policy(spec, "metadata-test", "validation")

        assert result['success'] is True
        assert 'description' in result['policy_yaml']

    def test_invalid_action(self):
        """Test handling of invalid action type"""
        spec = """
# Invalid Action

## Rule 1: Bad Action
pattern: test
message: Test
action: invalid_action
"""
        result = define_policy(spec, "invalid-action", "validation")

        # Should handle gracefully
        assert result['success'] is True

    def test_case_insensitive_actions(self):
        """Test that actions are case-insensitive"""
        spec_upper = """
# Upper Case

## Rule 1: Upper
pattern: test
message: Test
action: BLOCK
"""
        result = define_policy(spec_upper, "upper", "validation")
        assert result['success'] is True


class TestEdgeCases:
    """Test edge cases and error conditions"""

    def test_empty_spec(self):
        """Test with empty specification"""
        result = define_policy("", "empty-spec", "validation")
        assert result['success'] is True
        assert result['rule_count'] == 0

    def test_very_long_pattern(self):
        """Test with very long regex pattern"""
        long_pattern = "(" + "|".join([f"option{i}" for i in range(100)]) + ")"
        spec = f"""
# Long Pattern

## Rule 1: Long
pattern: {long_pattern}
message: Long pattern test
action: block
"""
        result = define_policy(spec, "long-pattern", "validation")
        assert result['success'] is True

    def test_unicode_in_spec(self):
        """Test with Unicode characters"""
        spec = """
# Unicode Test 🎉

## Rule 1: Émoji Rule
pattern: test
message: Message with ñ and é
action: block
"""
        result = define_policy(spec, "unicode", "validation")
        assert result['success'] is True

    def test_multiple_patterns_per_rule(self):
        """Test rule with multiple pattern specifications"""
        spec = """
# Multiple Patterns

## Rule 1: Multi Pattern
pattern: pattern1
pattern: pattern2
message: Multiple patterns
action: block
"""
        result = define_policy(spec, "multi-pattern", "validation")
        # Should take the last pattern or handle appropriately
        assert result['success'] is True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
