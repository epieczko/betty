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
from typing import Dict, Any, List, Optional
from pydantic import ValidationError as PydanticValidationError
from datetime import datetime, timezone


from betty.config import BASE_DIR, REQUIRED_SKILL_FIELDS
from betty.validation import validate_path, validate_manifest_fields
from betty.logging_utils import setup_logger
from betty.errors import SkillValidationError, format_error_response
from betty.models import SkillManifest

logger = setup_logger(__name__)


def build_response(ok: bool, path: str, errors: Optional[List[str]] = None, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "path": path,
    }

    if details is not None:
        response["details"] = details

    return response


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


def validate_skill_schema(manifest: Dict[str, Any]) -> List[str]:
    """
    Validate skill manifest using Pydantic schema.

    Args:
        manifest: Skill manifest dictionary

    Returns:
        List of validation errors (empty if valid)
    """
    errors: List[str] = []

    try:
        SkillManifest.model_validate(manifest)
        logger.info("Pydantic schema validation passed for skill manifest")
    except PydanticValidationError as exc:
        logger.warning("Pydantic schema validation failed for skill manifest")
        for error in exc.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            message = error["msg"]
            error_type = error["type"]
            errors.append(f"Schema validation error at '{field}': {message} (type: {error_type})")

    return errors


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

    # Validate with Pydantic schema first
    schema_errors = validate_skill_schema(manifest)
    if schema_errors:
        return {
            "valid": False,
            "errors": schema_errors,
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
        message = "Usage: skill_define.py <path_to_skill.yaml>"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    path = sys.argv[1]

    try:
        validation = validate_manifest(path)
        details = dict(validation)

        if validation.get("valid"):
            registry_updated = delegate_to_registry_update(path)
            details["status"] = "registered" if registry_updated else "validated"
            details["registry_updated"] = registry_updated

        errors: List[str] = []
        if not validation.get("valid"):
            if validation.get("missing"):
                errors.append("Missing required fields: " + ", ".join(validation["missing"]))
            if validation.get("error"):
                errors.append(str(validation["error"]))
            if validation.get("errors"):
                errors.extend(validation.get("errors"))

            # Check if there are schema validation errors
            has_schema_errors = any("Schema validation error" in err for err in validation.get("errors", []))
            if has_schema_errors:
                details["error"] = {
                    "type": "SchemaError",
                    "error": "SchemaError",
                    "message": "Skill manifest schema validation failed",
                    "details": {"errors": validation.get("errors", [])}
                }

        response = build_response(
            bool(validation.get("valid")),
            path=path,
            errors=errors,
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0 if response["ok"] else 1)

    except SkillValidationError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        error_info = format_error_response(e, include_traceback=True)
        response = build_response(
            False,
            path=path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)



if __name__ == "__main__":
    main()
