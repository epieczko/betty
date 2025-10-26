#!/usr/bin/env python3
"""
artifact_scaffold.py - Generate new artifact templates automatically from metadata inputs

Creates compliant artifact descriptors, registers them in the registry, and optionally validates them.
"""

import os
import sys
import json
import yaml
import argparse
from typing import Dict, Any, List, Optional
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.errors import format_error_response

logger = setup_logger(__name__)

# Default artifact directories
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
REGISTRY_DIR = os.path.join(BASE_DIR, "registry")
ARTIFACTS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "artifacts.json")


def ensure_directories():
    """Ensure required directories exist"""
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    os.makedirs(REGISTRY_DIR, exist_ok=True)


def load_artifacts_registry() -> Dict[str, Any]:
    """Load the artifacts registry, or create a new one if it doesn't exist"""
    if os.path.exists(ARTIFACTS_REGISTRY_FILE):
        try:
            with open(ARTIFACTS_REGISTRY_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load artifacts registry: {e}")
            return create_empty_registry()
    else:
        return create_empty_registry()


def create_empty_registry() -> Dict[str, Any]:
    """Create a new empty artifacts registry"""
    return {
        "registry_version": "1.0.0",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "artifacts": []
    }


def save_artifacts_registry(registry: Dict[str, Any]):
    """Save the artifacts registry"""
    registry["generated_at"] = datetime.utcnow().isoformat() + "Z"
    with open(ARTIFACTS_REGISTRY_FILE, 'w') as f:
        json.dump(registry, f, indent=2)
    logger.info(f"Saved artifacts registry to {ARTIFACTS_REGISTRY_FILE}")


def generate_artifact_yaml(
    artifact_id: str,
    category: str,
    extends: Optional[str] = None,
    fields: Optional[List[Dict[str, str]]] = None,
    version: str = "0.1.0"
) -> Dict[str, Any]:
    """
    Generate an artifact YAML structure

    Args:
        artifact_id: Unique identifier for the artifact (e.g., "new.artifact")
        category: Category/type of artifact (e.g., "report", "specification")
        extends: Optional base artifact to extend from
        fields: List of field definitions with name and type
        version: Semantic version (default: 0.1.0)

    Returns:
        Dictionary representing the artifact structure
    """
    artifact = {
        "id": artifact_id,
        "version": version,
        "category": category,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "metadata": {
            "description": f"{artifact_id} artifact",
            "tags": [category]
        }
    }

    if extends:
        artifact["extends"] = extends

    if fields:
        artifact["schema"] = {
            "type": "object",
            "properties": {},
            "required": []
        }

        for field in fields:
            field_name = field.get("name", "")
            field_type = field.get("type", "string")
            field_description = field.get("description", f"{field_name} field")
            field_required = field.get("required", False)

            artifact["schema"]["properties"][field_name] = {
                "type": field_type,
                "description": field_description
            }

            if field_required:
                artifact["schema"]["required"].append(field_name)

    return artifact


def get_artifact_filename(artifact_id: str) -> str:
    """
    Generate filename for artifact YAML file

    Args:
        artifact_id: The artifact ID (e.g., "new.artifact")

    Returns:
        Filename in format: {artifact_id}.artifact.yaml
    """
    # Replace dots with hyphens for filename
    safe_id = artifact_id.replace(".", "-")
    return f"{safe_id}.artifact.yaml"


def save_artifact_yaml(artifact: Dict[str, Any], output_path: Optional[str] = None) -> str:
    """
    Save artifact to YAML file

    Args:
        artifact: The artifact dictionary
        output_path: Optional custom output path

    Returns:
        Path to the saved file
    """
    artifact_id = artifact["id"]

    if output_path:
        file_path = output_path
    else:
        filename = get_artifact_filename(artifact_id)
        file_path = os.path.join(ARTIFACTS_DIR, filename)

    with open(file_path, 'w') as f:
        yaml.dump(artifact, f, default_flow_style=False, sort_keys=False)

    logger.info(f"Saved artifact to {file_path}")
    return file_path


def register_artifact(artifact: Dict[str, Any]) -> Dict[str, Any]:
    """
    Register artifact in the artifacts registry

    Args:
        artifact: The artifact dictionary

    Returns:
        The updated registry
    """
    registry = load_artifacts_registry()

    # Check if artifact already exists
    artifact_id = artifact["id"]
    existing_idx = None
    for idx, reg_artifact in enumerate(registry["artifacts"]):
        if reg_artifact["id"] == artifact_id:
            existing_idx = idx
            break

    # Create registry entry
    registry_entry = {
        "id": artifact["id"],
        "version": artifact["version"],
        "category": artifact["category"],
        "created_at": artifact["created_at"],
        "description": artifact.get("metadata", {}).get("description", ""),
        "tags": artifact.get("metadata", {}).get("tags", [])
    }

    if "extends" in artifact:
        registry_entry["extends"] = artifact["extends"]

    if "schema" in artifact:
        registry_entry["schema"] = artifact["schema"]

    # Update or add entry
    if existing_idx is not None:
        registry["artifacts"][existing_idx] = registry_entry
        logger.info(f"Updated artifact {artifact_id} in registry")
    else:
        registry["artifacts"].append(registry_entry)
        logger.info(f"Added artifact {artifact_id} to registry")

    save_artifacts_registry(registry)
    return registry


def scaffold_artifact(
    artifact_id: str,
    category: str,
    extends: Optional[str] = None,
    fields: Optional[List[Dict[str, str]]] = None,
    output_path: Optional[str] = None,
    validate: bool = False
) -> Dict[str, Any]:
    """
    Main scaffolding function

    Args:
        artifact_id: Unique identifier for the artifact
        category: Category/type of artifact
        extends: Optional base artifact to extend from
        fields: List of field definitions
        output_path: Optional custom output path
        validate: Whether to run validation after scaffolding

    Returns:
        Result dictionary with status and details
    """
    try:
        ensure_directories()

        # Generate artifact structure
        artifact = generate_artifact_yaml(
            artifact_id=artifact_id,
            category=category,
            extends=extends,
            fields=fields
        )

        # Save to file
        file_path = save_artifact_yaml(artifact, output_path)

        # Register in artifacts registry
        registry = register_artifact(artifact)

        result = {
            "ok": True,
            "status": "success",
            "artifact_id": artifact_id,
            "file_path": file_path,
            "version": artifact["version"],
            "category": category,
            "registry_path": ARTIFACTS_REGISTRY_FILE,
            "artifacts_registered": len(registry["artifacts"])
        }

        # Optional validation
        if validate:
            validation_result = validate_artifact(file_path)
            result["validation"] = validation_result

        return result

    except Exception as e:
        logger.error(f"Failed to scaffold artifact: {e}", exc_info=True)
        return {
            "ok": False,
            "status": "failed",
            "error": str(e),
            "details": format_error_response(e)
        }


def validate_artifact(file_path: str) -> Dict[str, Any]:
    """
    Validate an artifact YAML file

    Args:
        file_path: Path to the artifact YAML file

    Returns:
        Validation result dictionary
    """
    try:
        with open(file_path, 'r') as f:
            artifact = yaml.safe_load(f)

        errors = []
        warnings = []

        # Required fields
        required_fields = ["id", "version", "category", "created_at"]
        for field in required_fields:
            if field not in artifact:
                errors.append(f"Missing required field: {field}")

        # Version format check
        if "version" in artifact:
            version = artifact["version"]
            parts = version.split(".")
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                warnings.append(f"Version {version} may not follow semantic versioning (X.Y.Z)")

        # Category check
        if "category" in artifact and not artifact["category"]:
            warnings.append("Category is empty")

        # Schema validation
        if "schema" in artifact:
            schema = artifact["schema"]
            if "properties" not in schema:
                warnings.append("Schema missing 'properties' field")

        is_valid = len(errors) == 0

        return {
            "valid": is_valid,
            "errors": errors,
            "warnings": warnings,
            "file_path": file_path
        }

    except Exception as e:
        return {
            "valid": False,
            "errors": [f"Failed to validate: {str(e)}"],
            "warnings": [],
            "file_path": file_path
        }


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate new artifact templates from metadata"
    )

    parser.add_argument(
        "--id",
        required=True,
        help="Artifact ID (e.g., 'new.artifact')"
    )

    parser.add_argument(
        "--category",
        required=True,
        help="Artifact category (e.g., 'report', 'specification')"
    )

    parser.add_argument(
        "--extends",
        help="Base artifact to extend from (optional)"
    )

    parser.add_argument(
        "--fields",
        help="JSON string of field definitions (e.g., '[{\"name\":\"summary\",\"type\":\"string\"}]')"
    )

    parser.add_argument(
        "--output",
        help="Custom output path for the artifact file"
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the artifact after generation"
    )

    args = parser.parse_args()

    # Parse fields if provided
    fields = None
    if args.fields:
        try:
            fields = json.loads(args.fields)
        except json.JSONDecodeError as e:
            print(json.dumps({
                "ok": False,
                "status": "failed",
                "error": f"Invalid JSON for fields: {e}"
            }, indent=2))
            sys.exit(1)

    # Scaffold the artifact
    result = scaffold_artifact(
        artifact_id=args.id,
        category=args.category,
        extends=args.extends,
        fields=fields,
        output_path=args.output,
        validate=args.validate
    )

    # Output result as JSON
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    sys.exit(0 if result.get("ok", False) else 1)


if __name__ == "__main__":
    main()
