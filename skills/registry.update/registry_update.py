#!/usr/bin/env python3
"""
registry_update.py – Implementation of the registry.update Skill
Adds, updates, or removes entries in the Betty Framework Skill Registry.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, Optional, List
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REGISTRY_FILE, REGISTRY_VERSION
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import RegistryError, format_error_response

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


def load_manifest(path: str) -> Dict[str, Any]:
    """
    Load a skill manifest from YAML file.

    Args:
        path: Path to skill manifest file

    Returns:
        Parsed manifest dictionary

    Raises:
        RegistryError: If manifest cannot be loaded
    """
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except FileNotFoundError:
        raise RegistryError(f"Manifest file not found: {path}")
    except yaml.YAMLError as e:
        raise RegistryError(f"Invalid YAML in manifest: {e}")


def update_registry_data(manifest_path: str) -> Dict[str, Any]:
    """
    Update the registry with a skill manifest.

    Uses file locking to ensure thread-safe updates.

    Args:
        manifest_path: Path to skill manifest file

    Returns:
        Result dictionary with update status

    Raises:
        RegistryError: If update fails
    """
    # Validate path
    validate_path(manifest_path, must_exist=True)

    # Load manifest
    manifest = load_manifest(manifest_path)

    if not manifest.get("name"):
        raise RegistryError("Manifest missing required 'name' field")

    skill_name = manifest["name"]
    logger.info(f"Updating registry with skill: {skill_name}")

    def update_fn(registry_data):
        """Update function for safe_update_json."""
        # Ensure registry has proper structure
        if not registry_data or "skills" not in registry_data:
            registry_data = {
                "registry_version": REGISTRY_VERSION,
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "skills": []
            }

        # Remove existing entry if present
        registry_data["skills"] = [
            s for s in registry_data["skills"]
            if s.get("name") != skill_name
        ]

        # Add new entry
        registry_data["skills"].append(manifest)

        # Update timestamp
        registry_data["generated_at"] = datetime.now(timezone.utc).isoformat()

        return registry_data

    # Default registry structure
    default_registry = {
        "registry_version": REGISTRY_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skills": []
    }

    try:
        # Use safe atomic update with file locking
        updated_registry = safe_update_json(REGISTRY_FILE, update_fn, default=default_registry)

        result = {
            "status": "success",
            "updated": skill_name,
            "registry_path": REGISTRY_FILE,
            "total_skills": len(updated_registry["skills"]),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        logger.info(f"✅ Successfully updated registry for: {skill_name}")
        return result

    except Exception as e:
        logger.error(f"Failed to update registry: {e}")
        raise RegistryError(f"Failed to update registry: {e}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: registry_update.py <path_to_skill.yaml>"
        response = build_response(
            False,
            path="",
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    manifest_path = sys.argv[1]

    try:
        details = update_registry_data(manifest_path)
        response = build_response(
            True,
            path=details.get("registry_path", REGISTRY_FILE),
            errors=[],
            details=details,
        )
        print(json.dumps(response, indent=2))
        sys.exit(0)
    except RegistryError as e:
        logger.error(str(e))
        error_info = format_error_response(e)
        response = build_response(
            False,
            path=manifest_path,
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
            path=manifest_path,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info},
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
