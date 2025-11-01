#!/usr/bin/env python3
"""
meta_policy_profile.py - Meta-agent for generating policy profiles

Orchestrates the policy profile creation workflow:
1. Parse Markdown spec (policy.define)
2. Validate generated YAML (policy.validate)
3. Write to registry (fs.write)
4. Create audit log (audit.log)
"""

import sys
import json
import yaml
from typing import Dict, Any, Optional, List
from pathlib import Path

# Betty imports
from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

# Skill imports - direct module imports (no subprocess!)
from betty.skills.policy.define import define_policy, PolicyDefinitionError
from betty.skills.policy.validate import validate_policy, PolicyValidationError
from betty.skills.audit.log import create_audit_entry, append_audit_entry

logger = setup_logger(__name__)

# Paths
POLICIES_DIR = Path(BASE_DIR) / "registry" / "policies"


def generate_policy_profile(
    profile_name: str,
    policy_spec: str,
    policy_type: str = "validation",
    scope: List[str] = None,
    enforcement: str = "blocking",
    output_mode: str = "both"
) -> Dict[str, Any]:
    """
    Generate a policy profile from Markdown specification.

    Args:
        profile_name: Name of the policy profile
        policy_spec: Markdown policy specification
        policy_type: Type of policy (validation, security, compliance)
        scope: Scopes where policy applies
        enforcement: Enforcement level
        output_mode: preview, register, or both

    Returns:
        Dict with results including policy_profile_file, rule_count, etc.
    """
    results = {
        "profile_name": profile_name,
        "steps": {},
        "success": False
    }

    if scope is None:
        scope = ["artifact"]

    try:
        # Step 1: Define policy (Markdown → YAML)
        logger.info(f"Step 1: Defining policy '{profile_name}'")

        output_path = POLICIES_DIR / f"{profile_name}.yaml"

        # Call policy.define directly (no subprocess!)
        define_result = define_policy(
            policy_spec=policy_spec,
            profile_name=profile_name,
            policy_type=policy_type,
            scope=scope,
            enforcement=enforcement
        )

        results['steps']['policy.define'] = define_result

        if not define_result.get('success'):
            results['error'] = "Failed to define policy"
            results['message'] = define_result.get('message', 'Unknown error')
            return results

        # Write policy YAML to file
        POLICIES_DIR.mkdir(parents=True, exist_ok=True)
        policy_yaml_string = define_result.get('policy_yaml_string') or define_result.get('policy_yaml')
        with open(output_path, 'w') as f:
            f.write(policy_yaml_string)

        logger.info(f"Wrote policy to {output_path}")

        # Step 2: Validate policy
        logger.info(f"Step 2: Validating policy '{profile_name}'")

        # Use the policy dict directly if available, otherwise load from file
        policy_dict = define_result.get('policy_yaml')
        if isinstance(policy_dict, str):
            policy_dict = yaml.safe_load(policy_dict)

        validate_result = validate_policy(policy_dict, strict=False)
        results['steps']['policy.validate'] = validate_result

        if not validate_result.get('valid'):
            results['error'] = "Policy validation failed"
            results['message'] = validate_result.get('message', 'Validation failed')
            results['validation_errors'] = validate_result.get('errors', [])
            return results

        # Step 3: Audit log
        logger.info(f"Step 3: Creating audit log entry")

        # Create and append audit entry directly (no subprocess!)
        audit_entry = create_audit_entry(
            skill_name='meta.policy.profile',
            status='success',
            metadata={
                "profile_name": profile_name,
                "policy_type": policy_type,
                "rule_count": define_result.get('rule_count', 0),
                "output_path": str(output_path)
            }
        )

        audit_result = append_audit_entry(audit_entry)
        results['steps']['audit.log'] = audit_result

        # Build final result
        results['success'] = True
        results['policy_profile_file'] = str(output_path)
        results['rule_count'] = define_result.get('rule_count', 0)
        results['validation_result'] = 'pass'
        results['trace_id'] = audit_result.get('audit_entry', {}).get('timestamp', 'unknown')
        results['message'] = f"Successfully created policy profile '{profile_name}' with {results['rule_count']} rules"

        return results

    except (PolicyDefinitionError, PolicyValidationError) as e:
        logger.error(f"Policy error: {e}")
        results['success'] = False
        results['error'] = type(e).__name__
        results['message'] = str(e)
        return results
    except Exception as e:
        logger.error(f"Error generating policy profile: {e}")
        results['success'] = False
        results['error'] = type(e).__name__
        results['message'] = f"Failed to generate policy profile: {e}"
        return results


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Meta-agent for generating policy profiles from Markdown"
    )
    parser.add_argument(
        'profile_name',
        help="Name of the policy profile"
    )
    parser.add_argument(
        'policy_spec',
        help="Path to Markdown policy specification file"
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
        '--output-mode',
        default='both',
        choices=['preview', 'register', 'both'],
        help="Output mode"
    )

    args = parser.parse_args()

    try:
        # Read policy spec
        with open(args.policy_spec) as f:
            spec_content = f.read()

        # Generate profile
        result = generate_policy_profile(
            profile_name=args.profile_name,
            policy_spec=spec_content,
            policy_type=args.type,
            scope=args.scope,
            enforcement=args.enforcement,
            output_mode=args.output_mode
        )

        # Print result
        print(json.dumps(result, indent=2))

        sys.exit(0 if result.get('success') else 1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_result = {
            "success": False,
            "error": str(e),
            "message": f"Unexpected error: {e}"
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
