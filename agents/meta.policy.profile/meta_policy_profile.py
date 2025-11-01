#!/usr/bin/env python3
"""
meta_policy_profile.py - Meta-agent for generating policy profiles

Orchestrates the policy profile creation workflow:
1. Parse Markdown spec (policy.define)
2. Validate generated YAML (policy.validate)
3. Write to registry (fs.write)
4. Create audit log (audit.log)
"""

import os
import sys
import json
import subprocess
from typing import Dict, Any, Optional
from pathlib import Path

# Betty imports
from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)

# Paths
POLICY_DEFINE = Path(BASE_DIR) / "skills" / "policy.define" / "policy_define.py"
POLICY_VALIDATE = Path(BASE_DIR) / "skills" / "policy.validate" / "policy_validate.py"
AUDIT_LOG = Path(BASE_DIR) / "skills" / "audit.log" / "audit_log.py"
POLICIES_DIR = Path(BASE_DIR) / "registry" / "policies"


def run_skill(script_path: Path, args: list) -> Dict[str, Any]:
    """
    Run a skill script and return parsed JSON output.

    Args:
        script_path: Path to Python script
        args: Command line arguments

    Returns:
        Dict with skill output

    Raises:
        Exception: If skill execution fails
    """
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{BASE_DIR}:{env.get('PYTHONPATH', '')}"

    cmd = ['python3', str(script_path)] + args

    logger.info(f"Running: {' '.join(cmd)}")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env
    )

    # Try to parse JSON output (may have log lines before JSON)
    try:
        # Try to find JSON in output
        stdout_lines = result.stdout.strip().split('\n')

        # Look for JSON starting with {
        json_start = None
        for i, line in enumerate(stdout_lines):
            if line.strip().startswith('{'):
                json_start = i
                break

        if json_start is not None:
            json_text = '\n'.join(stdout_lines[json_start:])
            output = json.loads(json_text)
        else:
            raise json.JSONDecodeError("No JSON found", result.stdout, 0)

    except json.JSONDecodeError:
        logger.warning(f"Non-JSON output: {result.stdout}")
        output = {"raw_output": result.stdout, "stderr": result.stderr}

    if isinstance(output, dict):
        output['exit_code'] = result.returncode
    else:
        output = {"data": output, "exit_code": result.returncode}

    if result.returncode != 0:
        logger.error(f"Skill failed with code {result.returncode}")
        logger.error(f"Stderr: {result.stderr}")

    return output


def generate_policy_profile(
    profile_name: str,
    policy_spec: str,
    policy_type: str = "validation",
    scope: list = None,
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

    try:
        # Step 1: Define policy (Markdown → YAML)
        logger.info(f"Step 1: Defining policy '{profile_name}'")

        output_path = POLICIES_DIR / f"{profile_name}.yaml"

        # Write spec to temp file
        spec_file = Path(f"/tmp/policy_spec_{profile_name}.md")
        with open(spec_file, 'w') as f:
            f.write(policy_spec)

        # Run policy.define
        scope_args = scope if scope else ["artifact"]
        define_args = [
            str(spec_file),
            profile_name,
            '--type', policy_type,
            '--scope'] + scope_args + [
            '--enforcement', enforcement,
            '--output', str(output_path)
        ]

        define_result = run_skill(POLICY_DEFINE, define_args)
        results['steps']['policy.define'] = define_result

        if define_result.get('exit_code') != 0 or not define_result.get('success'):
            results['error'] = "Failed to define policy"
            results['message'] = define_result.get('message', 'Unknown error')
            return results

        # Step 2: Validate policy
        logger.info(f"Step 2: Validating policy '{profile_name}'")

        validate_result = run_skill(POLICY_VALIDATE, [str(output_path)])
        results['steps']['policy.validate'] = validate_result

        if validate_result.get('exit_code') != 0 or not validate_result.get('valid'):
            results['error'] = "Policy validation failed"
            results['message'] = validate_result.get('message', 'Validation failed')
            results['validation_errors'] = validate_result.get('errors', [])
            return results

        # Step 3: Audit log
        logger.info(f"Step 3: Creating audit log entry")

        audit_args = [
            '--skill', 'meta.policy.profile',
            '--status', 'success',
            '--metadata', json.dumps({
                "profile_name": profile_name,
                "policy_type": policy_type,
                "rule_count": define_result.get('rule_count', 0),
                "output_path": str(output_path)
            })
        ]

        audit_result = run_skill(AUDIT_LOG, audit_args)
        results['steps']['audit.log'] = audit_result

        # Build final result
        results['success'] = True
        results['policy_profile_file'] = str(output_path)
        results['rule_count'] = define_result.get('rule_count', 0)
        results['validation_result'] = 'pass'
        results['trace_id'] = audit_result.get('entry_id', 'unknown')
        results['message'] = f"Successfully created policy profile '{profile_name}' with {results['rule_count']} rules"

        # Clean up temp file
        spec_file.unlink(missing_ok=True)

        return results

    except Exception as e:
        logger.error(f"Error generating policy profile: {e}")
        results['success'] = False
        results['error'] = str(e)
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
