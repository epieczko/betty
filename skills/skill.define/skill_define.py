#!/usr/bin/env python3
"""
skill_define.py – Implementation of the skill.define Skill
Validates skill manifests (.skill.yaml) and registers them in the Skill Registry.
"""

import os
import sys
import json
import yaml
import subprocess
from typing import Dict, Any, List
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REQUIRED_SKILL_FIELDS
from betty.validation import validate_path, validate_manifest_fields
from betty.logging_utils import setup_logger
from betty.errors import SkillValidationError, format_error_response

logger = setup_logger(__name__)


def load_skill_manifest(path: str) -> Dict[str, Any]:
    """
    Load and parse a skill manifest from YAML file.

    Args:
        path: Path to skill manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        SkillValidationError: If manifest cannot be loaded or parsed
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise SkillValidationError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise SkillValidationError(f"Failed to parse YAML: {e}")


def validate_manifest(path: str) -> Dict[str, Any]:
    """
    Validate that required fields exist in a skill manifest.

    Args:
        path: Path to skill manifest file

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if manifest is valid
        - missing: List of missing required fields (if any)
        - manifest: The parsed manifest (if valid)
        - path: Path to the manifest file

    Raises:
        SkillValidationError: If validation fails
    """
    validate_path(path, must_exist=True)

    logger.info(f"Validating manifest: {path}")

    try:
        manifest = load_skill_manifest(path)
    except SkillValidationError as e:
        return {
            "valid": False,
            "error": str(e),
            "path": path
        }

    # Validate required fields
    missing = validate_manifest_fields(manifest, REQUIRED_SKILL_FIELDS)

    if missing:
        logger.warning(f"Missing required fields: {missing}")
        return {
            "valid": False,
            "missing": missing,
            "path": path
        }

    logger.info("✅ Manifest validation passed")
    return {
        "valid": True,
        "missing": [],
        "path": path,
        "manifest": manifest
    }


def delegate_to_registry_update(manifest_path: str) -> bool:
    """
    Delegate registry update to registry.update skill.

    Args:
        manifest_path: Path to skill manifest

    Returns:
        True if registry update succeeded, False otherwise
    """
    registry_updater = os.path.join(BASE_DIR, "skills", "registry.update", "registry_update.py")

    if not os.path.exists(registry_updater):
        logger.warning("registry.update skill not found - skipping registry update")
        return False

    logger.info("🔁 Delegating registry update to registry.update skill...")

    result = subprocess.run(
        [sys.executable, registry_updater, manifest_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logger.error(f"Registry update failed: {result.stderr}")
        return False

    logger.info("Registry update succeeded")
    return True


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        error = {
            "error": "UsageError",
            "message": "Usage: skill_define.py <path_to_skill.yaml>",
            "details": {}
        }
        print(json.dumps(error, indent=2))
        sys.exit(1)

    path = sys.argv[1]

    try:
        result = validate_manifest(path)

        if result["valid"]:
            # Delegate to registry.update
            registry_updated = delegate_to_registry_update(path)
            result["status"] = "registered" if registry_updated else "validated"
            result["registry_updated"] = registry_updated

        print(json.dumps(result, indent=2))

        # Exit with error code if validation failed
        if not result["valid"]:
            sys.exit(1)

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
