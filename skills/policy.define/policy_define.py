#!/usr/bin/env python3
"""
policy_define.py - Implementation of the policy.define Skill

Parses Markdown policy specifications and converts them into structured
YAML policy profiles compatible with policy.enforce.

Markdown Format:
    # Policy Profile: <name>

    ## Rule 1: <description>
    pattern: <regex_pattern>
    action: <block|warn|info>

    ## Rule 2: <description>
    check: <field> exists
    action: <block|warn|info>

    Metadata:
    version: <semantic_version>
    environments: [<env1>, <env2>]
    status: <active|draft>
    tags: [<tag1>, <tag2>]
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
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


class PolicyDefinitionError(Exception):
    """Raised when policy definition parsing fails."""
    pass


def parse_markdown_header(content: str) -> Dict[str, str]:
    """
    Extract policy name and description from Markdown header.

    Args:
        content: Markdown content

    Returns:
        Dict with 'name' and optional 'description'
    """
    result = {}

    # Look for: # Policy Profile: <name>
    header_match = re.search(r'^#\s+Policy\s+Profile:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
    if header_match:
        result['name'] = header_match.group(1).strip()

    # Look for description in first paragraph after header
    desc_match = re.search(r'^#[^\n]+\n+(.+?)(?=\n##|\nMetadata:|\Z)', content, re.MULTILINE | re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # Clean up the description (remove extra newlines)
        desc = ' '.join(line.strip() for line in desc.split('\n') if line.strip())
        if desc and not desc.startswith('#'):
            result['description'] = desc

    return result


def parse_rule_section(rule_text: str, rule_number: int) -> Dict[str, Any]:
    """
    Parse a single rule section from Markdown.

    Args:
        rule_text: Text of the rule section
        rule_number: Rule number for reference

    Returns:
        Dict representing the rule
    """
    rule = {}

    # Extract rule title/description
    title_match = re.search(r'^##\s+Rule\s+\d+:\s*(.+)$', rule_text, re.MULTILINE)
    if title_match:
        rule['description'] = title_match.group(1).strip()

    # Extract pattern
    pattern_match = re.search(r'^pattern:\s*(.+)$', rule_text, re.MULTILINE)
    if pattern_match:
        rule['pattern'] = pattern_match.group(1).strip()

    # Extract check (field existence)
    check_match = re.search(r'^check:\s*(.+?)\s+exists', rule_text, re.MULTILINE | re.IGNORECASE)
    if check_match:
        rule['field'] = check_match.group(1).strip()
        rule['required'] = True

    # Extract field name (if not from check)
    if 'field' not in rule:
        field_match = re.search(r'^field:\s*(.+)$', rule_text, re.MULTILINE)
        if field_match:
            rule['field'] = field_match.group(1).strip()

    # Extract action
    action_match = re.search(r'^action:\s*(block|warn|info)', rule_text, re.MULTILINE | re.IGNORECASE)
    if action_match:
        action = action_match.group(1).lower()
        rule['action'] = action

        # Map action to severity
        severity_map = {'block': 'error', 'warn': 'warning', 'info': 'info'}
        rule['severity'] = severity_map.get(action, 'error')

    # Extract allowed_values
    allowed_match = re.search(r'^allowed_values:\s*\[(.+?)\]', rule_text, re.MULTILINE)
    if allowed_match:
        values_str = allowed_match.group(1)
        rule['allowed_values'] = [v.strip().strip('"\'') for v in values_str.split(',')]

    # Extract forbidden_values
    forbidden_match = re.search(r'^forbidden_values:\s*\[(.+?)\]', rule_text, re.MULTILINE)
    if forbidden_match:
        values_str = forbidden_match.group(1)
        rule['forbidden_values'] = [v.strip().strip('"\'') for v in values_str.split(',')]

    # Generate message if not present
    if 'message' not in rule and 'description' in rule:
        rule['message'] = rule['description']

    return rule


def parse_metadata_section(content: str) -> Dict[str, Any]:
    """
    Parse metadata section from Markdown.

    Args:
        content: Markdown content

    Returns:
        Dict with metadata fields
    """
    metadata = {}

    # Find metadata section
    metadata_match = re.search(r'Metadata:?\s*\n((?:^[^\n#]+\n?)+)', content, re.MULTILINE)
    if not metadata_match:
        # Try alternative format: ## Metadata
        metadata_match = re.search(r'##\s*Metadata:?\s*\n((?:^[^\n#]+\n?)+)', content, re.MULTILINE)

    if metadata_match:
        metadata_text = metadata_match.group(1)

        # Parse version
        version_match = re.search(r'^version:\s*(.+)$', metadata_text, re.MULTILINE)
        if version_match:
            metadata['version'] = version_match.group(1).strip()

        # Parse environments
        env_match = re.search(r'^environments:\s*\[(.+?)\]', metadata_text, re.MULTILINE)
        if env_match:
            envs_str = env_match.group(1)
            metadata['environments'] = [e.strip().strip('"\'') for e in envs_str.split(',')]

        # Parse status
        status_match = re.search(r'^status:\s*(.+)$', metadata_text, re.MULTILINE)
        if status_match:
            metadata['status'] = status_match.group(1).strip()

        # Parse tags
        tags_match = re.search(r'^tags:\s*\[(.+?)\]', metadata_text, re.MULTILINE)
        if tags_match:
            tags_str = tags_match.group(1)
            metadata['tags'] = [t.strip().strip('"\'') for t in tags_str.split(',')]

    return metadata


def parse_policy_spec(spec_content: str, profile_name: str) -> Dict[str, Any]:
    """
    Parse complete Markdown policy specification.

    Args:
        spec_content: Markdown specification content
        profile_name: Name of the policy profile

    Returns:
        Structured policy dictionary

    Raises:
        PolicyDefinitionError: If parsing fails
    """
    # Parse header
    header = parse_markdown_header(spec_content)

    # Use provided profile_name or extracted name
    name = profile_name or header.get('name')
    if not name:
        raise PolicyDefinitionError("Policy name not found in spec and not provided")

    # Initialize policy structure
    policy = {
        'name': name,
        'version': '0.1.0',  # Default version
        'description': header.get('description', f'{name} policy profile'),
        'type': 'validation',  # Default type
        'scope': ['artifact'],  # Default scope
        'rules': [],
        'enforcement': 'blocking'  # Default enforcement
    }

    # Parse all rule sections
    rule_pattern = r'(##\s+Rule\s+\d+:.+?)(?=##\s+Rule\s+\d+:|Metadata:|##\s*Metadata|\Z)'
    rule_matches = re.finditer(rule_pattern, spec_content, re.MULTILINE | re.DOTALL)

    for idx, match in enumerate(rule_matches, 1):
        rule_text = match.group(1)
        try:
            rule = parse_rule_section(rule_text, idx)
            if rule:  # Only add non-empty rules
                policy['rules'].append(rule)
        except Exception as e:
            logger.warning(f"Failed to parse rule {idx}: {e}")

    # Parse metadata
    metadata = parse_metadata_section(spec_content)

    # Update policy with metadata
    if 'version' in metadata:
        policy['version'] = metadata['version']
    if 'environments' in metadata:
        policy['environments'] = metadata['environments']
    if 'status' in metadata:
        policy['metadata'] = policy.get('metadata', {})
        policy['metadata']['status'] = metadata['status']
    if 'tags' in metadata:
        policy['tags'] = metadata['tags']

    return policy


def convert_to_yaml(policy: Dict[str, Any]) -> str:
    """
    Convert policy dict to YAML string.

    Args:
        policy: Policy dictionary

    Returns:
        YAML string
    """
    # Wrap in 'policy' key to match existing format
    wrapped = {'policy': policy}
    return yaml.dump(wrapped, default_flow_style=False, sort_keys=False)


def define_policy(
    policy_spec: str,
    profile_name: str,
    policy_type: str = "validation",
    scope: List[str] = None,
    enforcement: str = "blocking"
) -> Dict[str, Any]:
    """
    Main function to define a policy from specification.

    Args:
        policy_spec: Markdown policy specification
        profile_name: Name of the policy profile
        policy_type: Type of policy (validation, security, compliance)
        scope: List of scopes where policy applies
        enforcement: Enforcement level (blocking, warning, info)

    Returns:
        Dict with policy_yaml, rule_count, validation_errors
    """
    try:
        # Parse the specification
        policy = parse_policy_spec(policy_spec, profile_name)

        # Apply overrides
        policy['type'] = policy_type
        if scope:
            policy['scope'] = scope
        policy['enforcement'] = enforcement

        # Convert to YAML
        policy_yaml_str = convert_to_yaml(policy)

        # Return result
        return {
            'success': True,
            'policy_yaml': policy,
            'policy_yaml_string': policy_yaml_str,
            'rule_count': len(policy.get('rules', [])),
            'validation_errors': [],
            'message': f"Successfully defined policy '{profile_name}' with {len(policy.get('rules', []))} rules"
        }

    except Exception as e:
        logger.error(f"Failed to define policy: {e}")
        return {
            'success': False,
            'policy_yaml': None,
            'policy_yaml_string': None,
            'rule_count': 0,
            'validation_errors': [str(e)],
            'message': f"Failed to define policy: {e}"
        }


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Define policy profiles from Markdown specifications"
    )
    parser.add_argument(
        'policy_spec',
        help="Path to Markdown policy specification file or spec content"
    )
    parser.add_argument(
        'profile_name',
        help="Name of the policy profile"
    )
    parser.add_argument(
        '--type',
        default='validation',
        choices=['validation', 'security', 'compliance'],
        help="Type of policy"
    )
    parser.add_argument(
        '--scope',
        nargs='+',
        default=['artifact'],
        help="Scopes where policy applies"
    )
    parser.add_argument(
        '--enforcement',
        default='blocking',
        choices=['blocking', 'warning', 'info'],
        help="Enforcement level"
    )
    parser.add_argument(
        '--output',
        help="Output file path for generated YAML"
    )

    args = parser.parse_args()

    try:
        # Read spec from file or use as content
        if os.path.exists(args.policy_spec):
            with open(args.policy_spec) as f:
                spec_content = f.read()
        else:
            spec_content = args.policy_spec

        # Define the policy
        result = define_policy(
            policy_spec=spec_content,
            profile_name=args.profile_name,
            policy_type=args.type,
            scope=args.scope,
            enforcement=args.enforcement
        )

        # Output YAML to file if specified
        if args.output and result['success']:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                f.write(result['policy_yaml_string'])
            logger.info(f"Wrote policy YAML to {args.output}")

        # Print JSON result
        output = {
            'success': result['success'],
            'message': result['message'],
            'rule_count': result['rule_count'],
            'validation_errors': result['validation_errors']
        }

        if result['success']:
            output['policy_yaml'] = result['policy_yaml']

        print(json.dumps(output, indent=2))

        sys.exit(0 if result['success'] else 1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_result = {
            'success': False,
            'error': str(e),
            'message': f"Unexpected error: {e}"
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
