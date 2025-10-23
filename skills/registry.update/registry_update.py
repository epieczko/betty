#!/usr/bin/env python3
"""
registry_update.py – Implementation of the registry.update Skill
Adds, updates, or removes entries in the Betty Framework Skill Registry.
"""

import os
import sys
import json
import yaml
import subprocess
from typing import Dict, Any, Optional, List
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REGISTRY_FILE, REGISTRY_VERSION, get_skill_handler_path
from betty.file_utils import safe_update_json
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import RegistryError, format_error_response
from betty.telemetry_capture import capture_execution

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


def enforce_policy(manifest_path: str) -> Dict[str, Any]:
    """
    Run policy enforcement on the manifest before registry update.

    Args:
        manifest_path: Path to skill manifest file

    Returns:
        Policy enforcement result

    Raises:
        RegistryError: If policy enforcement fails or violations are detected
    """
    try:
        policy_handler = get_skill_handler_path("policy.enforce")
        logger.info(f"Running policy enforcement on: {manifest_path}")

        result = subprocess.run(
            [sys.executable, policy_handler, manifest_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Try to parse JSON output
        policy_result = None
        if result.stdout.strip():
            try:
                policy_result = json.loads(result.stdout.strip())
            except json.JSONDecodeError:
                logger.warning("Failed to parse policy enforcement output as JSON")

        # Check if policy enforcement passed
        if result.returncode != 0:
            errors = []
            if policy_result and isinstance(policy_result, dict):
                errors = policy_result.get("errors", [])
            if not errors:
                errors = [f"Policy enforcement failed with return code {result.returncode}"]

            error_msg = "Policy violations detected:\n" + "\n".join(f"  - {err}" for err in errors)
            logger.error(error_msg)
            raise RegistryError(error_msg)

        if policy_result and not policy_result.get("ok", False):
            errors = policy_result.get("errors", ["Unknown policy violation"])
            error_msg = "Policy violations detected:\n" + "\n".join(f"  - {err}" for err in errors)
            logger.error(error_msg)
            raise RegistryError(error_msg)

        logger.info("✅ Policy enforcement passed")
        return policy_result or {}

    except subprocess.TimeoutExpired:
        raise RegistryError("Policy enforcement timed out")
    except FileNotFoundError:
        logger.warning("policy.enforce skill not found, skipping policy enforcement")
        return {}
    except Exception as e:
        if isinstance(e, RegistryError):
            raise
        logger.error(f"Failed to run policy enforcement: {e}")
        raise RegistryError(f"Failed to run policy enforcement: {e}")


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

    # Enforce policy before updating registry
    policy_result = enforce_policy(manifest_path)

    # Load manifest
    manifest = load_manifest(manifest_path)

    if not manifest.get("name"):
        raise RegistryError("Manifest missing required 'name' field")

    skill_name = manifest["name"]
    logger.info(f"Updating registry with skill: {skill_name}")

    # Capture registry state before update for diff tracking
    registry_before = None
    try:
        if os.path.exists(REGISTRY_FILE):
            with open(REGISTRY_FILE, 'r') as f:
                registry_before = json.load(f)
    except Exception:
        pass  # Ignore errors reading before state

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
        # Capture telemetry with diff tracking
        with capture_execution(
            skill_name="registry.update",
            inputs={"manifest_path": manifest_path, "skill_name": skill_name},
            caller="cli"
        ) as ctx:
            # Use safe atomic update with file locking
            updated_registry = safe_update_json(REGISTRY_FILE, update_fn, default=default_registry)

            # Calculate diff for telemetry
            registry_diff = None
            if registry_before:
                skills_before = {s.get("name"): s for s in registry_before.get("skills", [])}
                skills_after = {s.get("name"): s for s in updated_registry.get("skills", [])}

                # Determine if this was an add, update, or no change
                if skill_name not in skills_before:
                    operation = "add"
                elif skills_before.get(skill_name) != skills_after.get(skill_name):
                    operation = "update"
                else:
                    operation = "no_change"

                registry_diff = {
                    "operation": operation,
                    "skill_name": skill_name,
                    "skills_before": len(skills_before),
                    "skills_after": len(skills_after),
                }

            # Add metadata to telemetry
            ctx.set_metadata(
                registry_path=REGISTRY_FILE,
                total_skills=len(updated_registry["skills"]),
                policy_enforced=True,
                diff=registry_diff,
            )

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
