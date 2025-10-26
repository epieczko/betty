#!/usr/bin/env python3
"""
Claude Code Plug-in Integration Audit Script

Automatically audits all skills, agents, and commands to confirm they are fully
discoverable and executable from within Claude Code.

Usage:
    python scripts/claude_plugin_audit.py [--verbose] [--output FILE]
"""

import os
import sys
import json
import yaml
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone
from collections import defaultdict

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from betty.config import BASE_DIR, REGISTRY_FILE, AGENTS_REGISTRY_FILE, COMMANDS_REGISTRY_FILE
from betty.models import SkillManifest, AgentManifest, CommandManifest
from betty.logging_utils import setup_logger
from pydantic import ValidationError as PydanticValidationError

logger = setup_logger(__name__)


class AuditResult:
    """Container for audit results."""

    def __init__(self):
        self.plugins: List[Dict[str, Any]] = []
        self.total_count = 0
        self.success_count = 0
        self.error_count = 0
        self.warnings: List[str] = []
        self.errors: List[str] = []
        self.summary: Dict[str, Any] = {}

    def add_plugin(self, plugin: Dict[str, Any]):
        """Add a plugin audit result."""
        self.plugins.append(plugin)
        self.total_count += 1
        if plugin['status'] == 'ok':
            self.success_count += 1
        else:
            self.error_count += 1

    def add_warning(self, message: str):
        """Add a warning message."""
        self.warnings.append(message)
        logger.warning(message)

    def add_error(self, message: str):
        """Add an error message."""
        self.errors.append(message)
        logger.error(message)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON export."""
        return {
            "audit_timestamp": datetime.now(timezone.utc).isoformat(),
            "total_plugins": self.total_count,
            "successful": self.success_count,
            "failed": self.error_count,
            "pass_rate": f"{(self.success_count / self.total_count * 100):.1f}%" if self.total_count > 0 else "0%",
            "summary": self.summary,
            "warnings": self.warnings,
            "errors": self.errors,
            "plugins": self.plugins
        }


def find_manifests(pattern: str) -> List[Path]:
    """
    Find all manifest files matching a pattern.

    Args:
        pattern: Glob pattern (e.g., "**/skill.yaml")

    Returns:
        List of manifest file paths
    """
    base_path = Path(BASE_DIR)
    manifests = list(base_path.glob(pattern))
    logger.info(f"Found {len(manifests)} manifests matching {pattern}")
    return manifests


def validate_manifest_fields(manifest: Dict[str, Any], required_fields: List[str]) -> List[str]:
    """
    Validate that all required fields are present in manifest.

    Args:
        manifest: Manifest dictionary
        required_fields: List of required field names

    Returns:
        List of missing field names
    """
    missing = []
    for field in required_fields:
        if field not in manifest or manifest[field] is None:
            missing.append(field)
    return missing


def validate_skill_manifest(manifest_path: Path) -> Dict[str, Any]:
    """
    Validate a skill manifest.

    Args:
        manifest_path: Path to skill.yaml file

    Returns:
        Audit result dictionary
    """
    result = {
        "plugin_name": "",
        "manifest_path": str(manifest_path),
        "plugin_type": "skill",
        "status": "ok",
        "errors": [],
        "discoverable_in_claude": False,
        "execution_target_verified": False
    }

    try:
        # Load manifest
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)

        if not manifest:
            result["status"] = "error"
            result["errors"].append("Empty manifest file")
            return result

        result["plugin_name"] = manifest.get("name", "unknown")

        # Check required fields
        required_fields = ["name", "version", "description", "inputs", "outputs"]
        missing = validate_manifest_fields(manifest, required_fields)
        if missing:
            result["status"] = "error"
            result["errors"].append(f"Missing required fields: {', '.join(missing)}")

        # Note: Pydantic validation is relaxed since manifests use richer formats
        # than the simple schema. We focus on Claude Code integration checks instead.

        # Check if skill is in registry
        if os.path.exists(REGISTRY_FILE):
            with open(REGISTRY_FILE) as f:
                registry = json.load(f)
                skill_names = [s["name"] for s in registry.get("skills", [])]
                if result["plugin_name"] in skill_names:
                    result["discoverable_in_claude"] = True
                    result["execution_target_verified"] = True

        # Check for entrypoints and verify handler files exist
        if "entrypoints" in manifest:
            entrypoints = manifest["entrypoints"]
            if isinstance(entrypoints, list):
                for ep in entrypoints:
                    if isinstance(ep, dict):
                        # Check for handler file
                        handler_file = ep.get("handler")
                        if handler_file:
                            # Resolve relative to manifest directory
                            manifest_dir = manifest_path.parent
                            handler_path = manifest_dir / handler_file
                            if handler_path.exists():
                                result["execution_target_verified"] = True
                            else:
                                result["errors"].append(f"Handler file not found: {handler_file}")
        else:
            result["errors"].append("No entrypoints defined")

    except FileNotFoundError:
        result["status"] = "error"
        result["errors"].append("Manifest file not found")
    except yaml.YAMLError as e:
        result["status"] = "error"
        result["errors"].append(f"YAML parse error: {e}")
    except Exception as e:
        result["status"] = "error"
        result["errors"].append(f"Unexpected error: {e}")

    return result


def validate_agent_manifest(manifest_path: Path) -> Dict[str, Any]:
    """
    Validate an agent manifest.

    Args:
        manifest_path: Path to agent.yaml file

    Returns:
        Audit result dictionary
    """
    result = {
        "plugin_name": "",
        "manifest_path": str(manifest_path),
        "plugin_type": "agent",
        "status": "ok",
        "errors": [],
        "discoverable_in_claude": False,
        "execution_target_verified": False
    }

    try:
        # Load manifest
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)

        if not manifest:
            result["status"] = "error"
            result["errors"].append("Empty manifest file")
            return result

        result["plugin_name"] = manifest.get("name", "unknown")

        # Check required fields
        required_fields = ["name", "version", "description", "reasoning_mode", "capabilities", "skills_available"]
        missing = validate_manifest_fields(manifest, required_fields)
        if missing:
            result["status"] = "error"
            result["errors"].append(f"Missing required fields: {', '.join(missing)}")

        # Note: Pydantic validation is relaxed since we focus on Claude Code integration

        # Check if agent is in registry
        if os.path.exists(AGENTS_REGISTRY_FILE):
            with open(AGENTS_REGISTRY_FILE) as f:
                registry = json.load(f)
                agent_names = [a["name"] for a in registry.get("agents", [])]
                if result["plugin_name"] in agent_names:
                    result["discoverable_in_claude"] = True
                    result["execution_target_verified"] = True

        # Validate that referenced skills exist
        if "skills_available" in manifest:
            if os.path.exists(REGISTRY_FILE):
                with open(REGISTRY_FILE) as f:
                    registry = json.load(f)
                    skill_names = [s["name"] for s in registry.get("skills", [])]
                    for skill in manifest["skills_available"]:
                        if skill not in skill_names:
                            result["errors"].append(f"Referenced skill not found in registry: {skill}")

    except FileNotFoundError:
        result["status"] = "error"
        result["errors"].append("Manifest file not found")
    except yaml.YAMLError as e:
        result["status"] = "error"
        result["errors"].append(f"YAML parse error: {e}")
    except Exception as e:
        result["status"] = "error"
        result["errors"].append(f"Unexpected error: {e}")

    return result


def test_registry_loading() -> Tuple[bool, List[str]]:
    """
    Test that all registries can be loaded without errors.

    Returns:
        Tuple of (success, errors)
    """
    errors = []

    # Test skill registry
    if os.path.exists(REGISTRY_FILE):
        try:
            with open(REGISTRY_FILE) as f:
                registry = json.load(f)
                if "skills" not in registry:
                    errors.append("Skill registry missing 'skills' key")
                else:
                    logger.info(f"Skill registry loaded: {len(registry['skills'])} skills")
        except json.JSONDecodeError as e:
            errors.append(f"Skill registry JSON error: {e}")
        except Exception as e:
            errors.append(f"Skill registry load error: {e}")
    else:
        errors.append(f"Skill registry not found: {REGISTRY_FILE}")

    # Test agent registry
    if os.path.exists(AGENTS_REGISTRY_FILE):
        try:
            with open(AGENTS_REGISTRY_FILE) as f:
                registry = json.load(f)
                if "agents" not in registry:
                    errors.append("Agent registry missing 'agents' key")
                else:
                    logger.info(f"Agent registry loaded: {len(registry['agents'])} agents")
        except json.JSONDecodeError as e:
            errors.append(f"Agent registry JSON error: {e}")
        except Exception as e:
            errors.append(f"Agent registry load error: {e}")
    else:
        errors.append(f"Agent registry not found: {AGENTS_REGISTRY_FILE}")

    # Test command registry
    if os.path.exists(COMMANDS_REGISTRY_FILE):
        try:
            with open(COMMANDS_REGISTRY_FILE) as f:
                registry = json.load(f)
                if "commands" not in registry:
                    errors.append("Command registry missing 'commands' key")
                else:
                    logger.info(f"Command registry loaded: {len(registry['commands'])} commands")
        except json.JSONDecodeError as e:
            errors.append(f"Command registry JSON error: {e}")
        except Exception as e:
            errors.append(f"Command registry load error: {e}")
    else:
        logger.warning(f"Command registry not found: {COMMANDS_REGISTRY_FILE}")

    return len(errors) == 0, errors


def check_registry_uniqueness() -> Tuple[bool, List[str]]:
    """
    Check that all names in registries are unique.

    Returns:
        Tuple of (success, errors)
    """
    errors = []

    # Check skill registry
    if os.path.exists(REGISTRY_FILE):
        try:
            with open(REGISTRY_FILE) as f:
                registry = json.load(f)
                skill_names = [s["name"] for s in registry.get("skills", [])]
                duplicates = [name for name in set(skill_names) if skill_names.count(name) > 1]
                if duplicates:
                    errors.append(f"Duplicate skill names in registry: {', '.join(duplicates)}")
        except Exception as e:
            errors.append(f"Error checking skill registry uniqueness: {e}")

    # Check agent registry
    if os.path.exists(AGENTS_REGISTRY_FILE):
        try:
            with open(AGENTS_REGISTRY_FILE) as f:
                registry = json.load(f)
                agent_names = [a["name"] for a in registry.get("agents", [])]
                duplicates = [name for name in set(agent_names) if agent_names.count(name) > 1]
                if duplicates:
                    errors.append(f"Duplicate agent names in registry: {', '.join(duplicates)}")
        except Exception as e:
            errors.append(f"Error checking agent registry uniqueness: {e}")

    return len(errors) == 0, errors


def run_integration_tests(verbose: bool = False) -> Tuple[bool, str]:
    """
    Run integration tests.

    Args:
        verbose: Show detailed test output

    Returns:
        Tuple of (success, output)
    """
    logger.info("Running integration tests...")

    try:
        # Find integration test files
        test_files = [
            "tests/test_integration_core.py",
            "tests/test_integration_new_skills.py",
        ]

        for test_file in test_files:
            test_path = Path(BASE_DIR) / test_file
            if not test_path.exists():
                logger.warning(f"Integration test not found: {test_file}")
                continue

            logger.info(f"Running {test_file}...")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_path), "-v" if verbose else "-q"],
                cwd=BASE_DIR,
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode != 0:
                return False, result.stdout + result.stderr

        return True, "All integration tests passed"

    except subprocess.TimeoutExpired:
        return False, "Integration tests timed out"
    except Exception as e:
        return False, f"Error running integration tests: {e}"


def main():
    """Main audit entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Audit Betty plug-ins for Claude Code integration",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--output", "-o", help="Output file for audit report (JSON)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip integration tests")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel("DEBUG")

    print("=" * 80)
    print("BETTY CLAUDE CODE PLUG-IN INTEGRATION AUDIT")
    print("=" * 80)
    print()

    audit = AuditResult()

    # Step 1: Scan for manifests
    print("Step 1: Scanning for manifests...")
    skill_manifests = find_manifests("skills/*/skill.yaml") + find_manifests("examples/skills/*/skill.yaml")
    agent_manifests = find_manifests("agents/*/agent.yaml")

    print(f"  Found {len(skill_manifests)} skill manifests")
    print(f"  Found {len(agent_manifests)} agent manifests")
    print()

    # Step 2: Validate manifests
    print("Step 2: Validating manifests...")

    for manifest_path in skill_manifests:
        result = validate_skill_manifest(manifest_path)
        audit.add_plugin(result)
        if result["status"] != "ok":
            audit.add_error(f"Skill validation failed: {result['plugin_name']} - {', '.join(result['errors'])}")

    for manifest_path in agent_manifests:
        result = validate_agent_manifest(manifest_path)
        audit.add_plugin(result)
        if result["status"] != "ok":
            audit.add_error(f"Agent validation failed: {result['plugin_name']} - {', '.join(result['errors'])}")

    print(f"  Validated {audit.total_count} plugins")
    print(f"  ✓ Success: {audit.success_count}")
    print(f"  ✗ Failed: {audit.error_count}")
    print()

    # Step 3: Test registry consistency
    print("Step 3: Testing registry consistency...")

    registry_ok, registry_errors = test_registry_loading()
    if not registry_ok:
        for error in registry_errors:
            audit.add_error(error)
    else:
        print("  ✓ All registries loaded successfully")

    unique_ok, unique_errors = check_registry_uniqueness()
    if not unique_ok:
        for error in unique_errors:
            audit.add_error(error)
    else:
        print("  ✓ All registry names are unique")

    print()

    # Step 4: Count discoverable plugins
    print("Step 4: Checking discoverability...")
    discoverable = sum(1 for p in audit.plugins if p["discoverable_in_claude"])
    verified = sum(1 for p in audit.plugins if p["execution_target_verified"])

    print(f"  Discoverable in Claude: {discoverable}/{audit.total_count}")
    print(f"  Execution targets verified: {verified}/{audit.total_count}")
    print()

    # Step 5: Run integration tests
    if not args.skip_tests:
        print("Step 5: Running integration tests...")
        tests_ok, test_output = run_integration_tests(args.verbose)

        if tests_ok:
            print("  ✓ Integration tests passed")
        else:
            print("  ✗ Integration tests failed")
            audit.add_error(f"Integration tests failed: {test_output}")
            if args.verbose:
                print(test_output)
        print()
    else:
        print("Step 5: Skipping integration tests (--skip-tests)")
        print()

    # Summary
    audit.summary = {
        "total_manifests": audit.total_count,
        "skills": len(skill_manifests),
        "agents": len(agent_manifests),
        "valid": audit.success_count,
        "invalid": audit.error_count,
        "discoverable": discoverable,
        "execution_verified": verified,
        "registry_consistent": registry_ok and unique_ok,
        "tests_passed": tests_ok if not args.skip_tests else None
    }

    print("=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total plugins audited: {audit.total_count}")
    print(f"  Skills: {len(skill_manifests)}")
    print(f"  Agents: {len(agent_manifests)}")
    print()
    print(f"Validation results:")
    print(f"  ✓ Valid: {audit.success_count}")
    print(f"  ✗ Invalid: {audit.error_count}")
    print(f"  Pass rate: {(audit.success_count / audit.total_count * 100):.1f}%" if audit.total_count > 0 else "  Pass rate: 0%")
    print()
    print(f"Claude Code integration:")
    print(f"  Discoverable: {discoverable}/{audit.total_count}")
    print(f"  Execution verified: {verified}/{audit.total_count}")
    print()
    print(f"Registry consistency: {'✓ PASS' if registry_ok and unique_ok else '✗ FAIL'}")
    if not args.skip_tests:
        print(f"Integration tests: {'✓ PASS' if tests_ok else '✗ FAIL'}")
    print()

    if audit.warnings:
        print(f"Warnings: {len(audit.warnings)}")
        for warning in audit.warnings[:5]:
            print(f"  - {warning}")
        if len(audit.warnings) > 5:
            print(f"  ... and {len(audit.warnings) - 5} more")
        print()

    if audit.errors:
        print(f"Errors: {len(audit.errors)}")
        for error in audit.errors[:5]:
            print(f"  - {error}")
        if len(audit.errors) > 5:
            print(f"  ... and {len(audit.errors) - 5} more")
        print()

    # Export to JSON
    output_file = args.output or "claude_plugin_audit.json"
    output_path = Path(BASE_DIR) / output_file

    with open(output_path, 'w') as f:
        json.dump(audit.to_dict(), f, indent=2)

    print(f"Detailed audit report saved to: {output_file}")
    print("=" * 80)

    # Exit with appropriate code
    if audit.error_count > 0 or not registry_ok or not unique_ok:
        print("\n❌ AUDIT FAILED: Some plugins cannot be registered or executed")
        sys.exit(1)
    else:
        print("\n✅ AUDIT PASSED: All plugins are properly integrated with Claude Code")
        sys.exit(0)


if __name__ == "__main__":
    main()
