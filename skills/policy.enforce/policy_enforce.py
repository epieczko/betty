#!/usr/bin/env python3
"""
policy_enforce.py – Implementation of the policy.enforce Skill
Validates operations against organizational policies before execution.
"""

import os
import sys
import json
import yaml
import re
from typing import Dict, Any, List
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.errors import SkillValidationError, format_error_response

logger = setup_logger(__name__)

# Default policies directory
POLICIES_DIR = Path(BASE_DIR) / "registry" / "policies"


class PolicyViolation:
    """Represents a single policy violation."""

    def __init__(self, policy_name: str, rule: str, message: str, severity: str = "error"):
        self.policy_name = policy_name
        self.rule = rule
        self.message = message
        self.severity = severity

    def to_dict(self) -> Dict[str, Any]:
        return {
            "policy": self.policy_name,
            "rule": self.rule,
            "message": self.message,
            "severity": self.severity
        }


class PolicyEngine:
    """Core policy enforcement engine."""

    def __init__(self, policies_dir: Path = POLICIES_DIR):
        self.policies_dir = policies_dir
        self.policies = self._load_policies()

    def _load_policies(self) -> List[Dict[str, Any]]:
        """Load all policy definitions from the policies directory."""
        policies = []

        if not self.policies_dir.exists():
            logger.warning(f"Policies directory not found: {self.policies_dir}")
            return policies

        for policy_file in self.policies_dir.glob("*.yaml"):
            try:
                with open(policy_file) as f:
                    policy = yaml.safe_load(f)
                    if policy and "policy" in policy:
                        policies.append(policy["policy"])
                        logger.info(f"Loaded policy: {policy['policy'].get('name', 'unnamed')}")
            except Exception as e:
                logger.error(f"Failed to load policy {policy_file}: {e}")

        return policies

    def enforce(self, action: str, target: Dict[str, Any], policy_set: str = None) -> List[PolicyViolation]:
        """
        Enforce policies against a target object.

        Args:
            action: The action being performed (create, update, delete, execute)
            target: The target object to validate (skill manifest, workflow, etc.)
            policy_set: Optional specific policy set to enforce (defaults to all)

        Returns:
            List of policy violations (empty if all policies pass)
        """
        violations = []

        # Filter policies based on action and policy_set
        applicable_policies = [
            p for p in self.policies
            if self._is_applicable(p, action, policy_set)
        ]

        if not applicable_policies:
            logger.info(f"No applicable policies found for action: {action}")
            return violations

        logger.info(f"Enforcing {len(applicable_policies)} policies for action: {action}")

        for policy in applicable_policies:
            policy_violations = self._check_policy(policy, target, action)
            violations.extend(policy_violations)

        return violations

    def _is_applicable(self, policy: Dict[str, Any], action: str, policy_set: str = None) -> bool:
        """Check if a policy applies to the given action and policy set."""
        # Check policy set filter
        if policy_set and policy.get("name") != policy_set:
            return False

        # Check if action matches policy scope
        scope = policy.get("scope", [])
        if scope and action not in scope:
            return False

        return True

    def _check_policy(self, policy: Dict[str, Any], target: Dict[str, Any], action: str) -> List[PolicyViolation]:
        """Check a single policy against the target."""
        violations = []
        policy_name = policy.get("name", "unnamed")
        rules = policy.get("rules", [])

        for rule in rules:
            violation = self._check_rule(policy_name, rule, target, action)
            if violation:
                violations.append(violation)

        return violations

    def _check_rule(
        self,
        policy_name: str,
        rule: Dict[str, Any],
        target: Dict[str, Any],
        action: str
    ) -> PolicyViolation | None:
        """Check a single rule against the target."""
        field = rule.get("field")
        pattern = rule.get("pattern")
        allowed_values = rule.get("allowed_values")
        forbidden_values = rule.get("forbidden_values")
        required = rule.get("required", False)
        message = rule.get("message", f"Policy violation in field: {field}")
        severity = rule.get("severity", "error")

        # Get field value from target
        field_value = target.get(field)

        # Check required fields
        if required and not field_value:
            return PolicyViolation(
                policy_name,
                f"required:{field}",
                f"Required field '{field}' is missing",
                severity
            )

        # Skip remaining checks if field is not present and not required
        if field_value is None:
            return None

        # Check pattern matching
        if pattern:
            if not re.match(pattern, str(field_value)):
                return PolicyViolation(
                    policy_name,
                    f"pattern:{field}",
                    message,
                    severity
                )

        # Check allowed values
        if allowed_values and field_value not in allowed_values:
            return PolicyViolation(
                policy_name,
                f"allowed_values:{field}",
                f"Field '{field}' must be one of: {', '.join(allowed_values)}",
                severity
            )

        # Check forbidden values
        if forbidden_values and field_value in forbidden_values:
            return PolicyViolation(
                policy_name,
                f"forbidden_values:{field}",
                f"Field '{field}' cannot be: {field_value}",
                severity
            )

        return None


def enforce_policies(action: str, target_path: str = None, target_data: Dict[str, Any] = None, policy_set: str = None) -> Dict[str, Any]:
    """
    Main policy enforcement function.

    Args:
        action: Action being performed (create, update, delete, execute)
        target_path: Path to target file (for skills/workflows)
        target_data: Direct target data (alternative to target_path)
        policy_set: Optional specific policy set to enforce

    Returns:
        Result dictionary with validation status and violations
    """
    # Load target data
    if target_data is None:
        if target_path is None:
            raise SkillValidationError("Either target_path or target_data must be provided")

        try:
            with open(target_path) as f:
                if target_path.endswith('.yaml') or target_path.endswith('.yml'):
                    target_data = yaml.safe_load(f)
                else:
                    target_data = json.load(f)
        except FileNotFoundError:
            raise SkillValidationError(f"Target file not found: {target_path}")
        except (yaml.YAMLError, json.JSONDecodeError) as e:
            raise SkillValidationError(f"Invalid target file format: {e}")

    # Run policy enforcement
    engine = PolicyEngine()
    violations = engine.enforce(action, target_data, policy_set)

    # Determine if enforcement should block
    blocking_violations = [v for v in violations if v.severity == "error"]
    warning_violations = [v for v in violations if v.severity == "warning"]

    passed = len(blocking_violations) == 0

    result = {
        "passed": passed,
        "action": action,
        "target": target_path or "inline",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "policies_checked": len(engine.policies),
        "violations": {
            "errors": [v.to_dict() for v in blocking_violations],
            "warnings": [v.to_dict() for v in warning_violations]
        },
        "total_violations": len(violations),
        "status": "allowed" if passed else "blocked"
    }

    if passed:
        logger.info(f"✅ Policy enforcement passed for action: {action}")
    else:
        logger.warning(f"❌ Policy enforcement FAILED for action: {action} ({len(blocking_violations)} errors)")

    return result


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Enforce Betty Framework policies")
    parser.add_argument("--action", required=True, help="Action being performed (create, update, delete, execute)")
    parser.add_argument("--target", help="Path to target file (skill manifest, workflow, etc.)")
    parser.add_argument("--policy-set", help="Optional specific policy set to enforce")
    parser.add_argument("--target-json", help="Direct JSON target data")

    args = parser.parse_args()

    try:
        target_data = None
        if args.target_json:
            target_data = json.loads(args.target_json)

        result = enforce_policies(
            action=args.action,
            target_path=args.target,
            target_data=target_data,
            policy_set=args.policy_set
        )

        print(json.dumps(result, indent=2))

        # Exit with error code if policy enforcement failed
        sys.exit(0 if result["passed"] else 1)

    except SkillValidationError as e:
        logger.error(str(e))
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(json.dumps(format_error_response(e, include_traceback=True), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
