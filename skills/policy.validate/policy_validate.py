#!/usr/bin/env python3
"""
policy_validate.py - Implementation of the policy.validate Skill

Validates policy profile definitions for correctness, completeness, and
adherence to policy schema requirements.

Validates:
- Required fields (name, version, type, rules)
- Valid field types
- Regex pattern validity
- Severity/action values
- Scope values
- Version format
"""

import os
import sys
import re
import json
import yaml
from typing import Dict, Any, List, Optional
from pathlib import Path

# Betty imports
from betty.config import BASE_DIR
from betty.validation import validate_version, ValidationError
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


class PolicyValidationError(Exception):
    """Raised when policy validation fails."""
    pass


# Valid values for policy fields
VALID_POLICY_TYPES = {'validation', 'security', 'compliance'}
VALID_SEVERITIES = {'error', 'warning', 'info'}
VALID_ACTIONS = {'block', 'warn', 'info'}
VALID_SCOPES = {'artifact', 'agent', 'skill', 'workflow', 'create', 'update', 'register'}
VALID_ENFORCEMENTS = {'blocking', 'warning', 'info'}


def validate_required_fields(policy: Dict[str, Any]) -> List[str]:
    """
    Validate that all required fields are present.

    Args:
        policy: Policy dictionary

    Returns:
        List of error messages
    """
    errors = []
    required_fields = ['name', 'version', 'type', 'rules']

    for field in required_fields:
        if field not in policy:
            errors.append(f"Missing required field: '{field}'")
        elif not policy[field]:
            errors.append(f"Required field '{field}' is empty")

    return errors


def validate_policy_name(name: str) -> List[str]:
    """
    Validate policy name format.

    Args:
        name: Policy name

    Returns:
        List of error messages
    """
    errors = []

    if not name:
        errors.append("Policy name cannot be empty")
        return errors

    # Name should be lowercase, alphanumeric with hyphens
    if not re.match(r'^[a-z][a-z0-9-]*[a-z0-9]$', name):
        errors.append(
            f"Policy name '{name}' should be lowercase alphanumeric "
            "with hyphens (e.g., 'strict', 'default', 'prod-security')"
        )

    return errors


def validate_policy_version(version: str) -> List[str]:
    """
    Validate policy version format (semantic versioning).

    Args:
        version: Version string

    Returns:
        List of error messages
    """
    errors = []

    if not version:
        errors.append("Policy version cannot be empty")
        return errors

    try:
        validate_version(version)
    except ValidationError as e:
        errors.append(f"Invalid version format: {e}")

    return errors


def validate_policy_type(policy_type: str) -> List[str]:
    """
    Validate policy type.

    Args:
        policy_type: Type of policy

    Returns:
        List of error messages
    """
    errors = []

    if policy_type not in VALID_POLICY_TYPES:
        errors.append(
            f"Invalid policy type: '{policy_type}'. "
            f"Must be one of: {', '.join(sorted(VALID_POLICY_TYPES))}"
        )

    return errors


def validate_scope(scope: List[str]) -> List[str]:
    """
    Validate policy scope values.

    Args:
        scope: List of scope values

    Returns:
        List of error messages
    """
    errors = []

    if not isinstance(scope, list):
        errors.append("Scope must be a list")
        return errors

    for s in scope:
        if s not in VALID_SCOPES:
            errors.append(
                f"Invalid scope value: '{s}'. "
                f"Valid scopes: {', '.join(sorted(VALID_SCOPES))}"
            )

    return errors


def validate_regex_pattern(pattern: str, rule_idx: int) -> List[str]:
    """
    Validate that a regex pattern is valid.

    Args:
        pattern: Regex pattern string
        rule_idx: Rule index for error messages

    Returns:
        List of error messages
    """
    errors = []

    try:
        re.compile(pattern)
    except re.error as e:
        errors.append(f"Rule {rule_idx}: Invalid regex pattern: {e}")

    return errors


def validate_rule(rule: Dict[str, Any], rule_idx: int) -> List[str]:
    """
    Validate a single rule definition.

    Args:
        rule: Rule dictionary
        rule_idx: Rule index for error messages

    Returns:
        List of error messages
    """
    errors = []

    # Check if rule has either 'field' or 'pattern'
    if 'field' not in rule and 'pattern' not in rule:
        errors.append(
            f"Rule {rule_idx}: Must have either 'field' or 'pattern' defined"
        )

    # Validate pattern if present
    if 'pattern' in rule:
        pattern_errors = validate_regex_pattern(rule['pattern'], rule_idx)
        errors.extend(pattern_errors)

    # Validate severity if present
    if 'severity' in rule:
        if rule['severity'] not in VALID_SEVERITIES:
            errors.append(
                f"Rule {rule_idx}: Invalid severity '{rule['severity']}'. "
                f"Must be one of: {', '.join(sorted(VALID_SEVERITIES))}"
            )

    # Validate action if present
    if 'action' in rule:
        if rule['action'] not in VALID_ACTIONS:
            errors.append(
                f"Rule {rule_idx}: Invalid action '{rule['action']}'. "
                f"Must be one of: {', '.join(sorted(VALID_ACTIONS))}"
            )

    # Check for message
    if 'message' not in rule and 'description' not in rule:
        errors.append(
            f"Rule {rule_idx}: Should have either 'message' or 'description'"
        )

    # Validate allowed_values and forbidden_values are lists
    if 'allowed_values' in rule:
        if not isinstance(rule['allowed_values'], list):
            errors.append(f"Rule {rule_idx}: 'allowed_values' must be a list")

    if 'forbidden_values' in rule:
        if not isinstance(rule['forbidden_values'], list):
            errors.append(f"Rule {rule_idx}: 'forbidden_values' must be a list")

    return errors


def validate_rules(rules: List[Dict[str, Any]]) -> List[str]:
    """
    Validate all rules in a policy.

    Args:
        rules: List of rule dictionaries

    Returns:
        List of error messages
    """
    errors = []

    if not isinstance(rules, list):
        errors.append("Rules must be a list")
        return errors

    if len(rules) == 0:
        errors.append("Policy must have at least one rule")

    for idx, rule in enumerate(rules, 1):
        if not isinstance(rule, dict):
            errors.append(f"Rule {idx}: Must be a dictionary")
            continue

        rule_errors = validate_rule(rule, idx)
        errors.extend(rule_errors)

    return errors


def validate_enforcement(enforcement: str) -> List[str]:
    """
    Validate enforcement level.

    Args:
        enforcement: Enforcement level

    Returns:
        List of error messages
    """
    errors = []

    if enforcement and enforcement not in VALID_ENFORCEMENTS:
        errors.append(
            f"Invalid enforcement: '{enforcement}'. "
            f"Must be one of: {', '.join(sorted(VALID_ENFORCEMENTS))}"
        )

    return errors


def validate_policy(policy: Dict[str, Any], strict: bool = False) -> Dict[str, Any]:
    """
    Validate a complete policy definition.

    Args:
        policy: Policy dictionary
        strict: If True, warnings become errors

    Returns:
        Validation result dictionary
    """
    errors = []
    warnings = []

    # Validate required fields
    errors.extend(validate_required_fields(policy))

    # If missing required fields, return early
    if errors:
        return {
            'valid': False,
            'errors': errors,
            'warnings': warnings,
            'message': f"Policy validation failed with {len(errors)} error(s)"
        }

    # Validate name
    errors.extend(validate_policy_name(policy['name']))

    # Validate version
    errors.extend(validate_policy_version(policy['version']))

    # Validate type
    errors.extend(validate_policy_type(policy['type']))

    # Validate scope
    if 'scope' in policy:
        errors.extend(validate_scope(policy['scope']))
    else:
        warnings.append("No 'scope' field defined (recommended)")

    # Validate rules
    errors.extend(validate_rules(policy['rules']))

    # Validate enforcement
    if 'enforcement' in policy:
        errors.extend(validate_enforcement(policy['enforcement']))
    else:
        warnings.append("No 'enforcement' field defined (recommended)")

    # Check for description
    if 'description' not in policy:
        warnings.append("No 'description' field (recommended for clarity)")

    # In strict mode, warnings become errors
    if strict and warnings:
        errors.extend(warnings)
        warnings = []

    valid = len(errors) == 0

    return {
        'valid': valid,
        'errors': errors,
        'warnings': warnings,
        'rule_count': len(policy.get('rules', [])),
        'message': (
            "Policy validation passed" if valid
            else f"Policy validation failed with {len(errors)} error(s)"
        )
    }


def load_policy_file(path: str) -> Dict[str, Any]:
    """
    Load policy from YAML file.

    Args:
        path: Path to policy YAML file

    Returns:
        Policy dictionary

    Raises:
        Exception: If file cannot be loaded
    """
    try:
        with open(path) as f:
            data = yaml.safe_load(f)

        # Handle both wrapped (policy: {...}) and unwrapped formats
        if 'policy' in data:
            return data['policy']
        else:
            return data

    except FileNotFoundError:
        raise Exception(f"Policy file not found: {path}")
    except yaml.YAMLError as e:
        raise Exception(f"Failed to parse YAML: {e}")


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate policy profile definitions"
    )
    parser.add_argument(
        'policy_path',
        nargs='?',
        help="Path to policy YAML file to validate"
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help="Treat warnings as errors"
    )

    args = parser.parse_args()

    try:
        if not args.policy_path:
            print(json.dumps({
                'success': False,
                'error': 'No policy file path provided',
                'message': 'Usage: policy_validate.py <policy_path> [--strict]'
            }, indent=2))
            sys.exit(1)

        # Load policy file
        policy = load_policy_file(args.policy_path)

        # Validate policy
        result = validate_policy(policy, strict=args.strict)

        # Build output
        output = {
            'success': result['valid'],
            'valid': result['valid'],
            'message': result['message'],
            'policy_path': args.policy_path,
            'rule_count': result['rule_count'],
            'errors': result['errors'],
            'warnings': result['warnings']
        }

        # Add validation report
        output['validation_report'] = {
            'total_errors': len(result['errors']),
            'total_warnings': len(result['warnings']),
            'strict_mode': args.strict
        }

        print(json.dumps(output, indent=2))

        sys.exit(0 if result['valid'] else 1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_result = {
            'success': False,
            'valid': False,
            'error': str(e),
            'message': f"Unexpected error: {e}"
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
