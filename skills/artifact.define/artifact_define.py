#!/usr/bin/env python3
"""
artifact_define.py - Define artifact metadata for Betty Framework skills

Helps create artifact_metadata blocks that declare what artifacts a skill
produces and consumes, enabling interoperability.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)

# Known artifact types and their metadata
KNOWN_ARTIFACT_TYPES = {
    "openapi-spec": {
        "schema": "schemas/openapi-spec.json",
        "file_pattern": "*.openapi.yaml",
        "content_type": "application/yaml",
        "description": "OpenAPI 3.0+ specification"
    },
    "validation-report": {
        "schema": "schemas/validation-report.json",
        "file_pattern": "*.validation.json",
        "content_type": "application/json",
        "description": "Structured validation results"
    },
    "workflow-definition": {
        "schema": "schemas/workflow-definition.json",
        "file_pattern": "*.workflow.yaml",
        "content_type": "application/yaml",
        "description": "Betty workflow definition"
    },
    "hook-config": {
        "schema": "schemas/hook-config.json",
        "file_pattern": "hooks.yaml",
        "content_type": "application/yaml",
        "description": "Claude Code hook configuration"
    },
    "api-models": {
        "file_pattern": "*.{py,ts,go}",
        "description": "Generated API data models"
    },
    "agent-description": {
        "schema": "schemas/agent-description.json",
        "file_pattern": "**/agent_description.md",
        "content_type": "text/markdown",
        "description": "Natural language description of agent purpose and requirements"
    },
    "agent-definition": {
        "schema": "schemas/agent-definition.json",
        "file_pattern": "agents/*/agent.yaml",
        "content_type": "application/yaml",
        "description": "Complete agent configuration with skills and metadata"
    },
    "agent-documentation": {
        "file_pattern": "agents/*/README.md",
        "content_type": "text/markdown",
        "description": "Human-readable agent documentation"
    },
    "optimization-report": {
        "schema": "schemas/optimization-report.json",
        "file_pattern": "*.optimization.json",
        "content_type": "application/json",
        "description": "Performance and security optimization recommendations for APIs and workflows. Contains actionable suggestions for improving efficiency, security posture, and adherence to best practices."
    },
    "compatibility-graph": {
        "schema": "schemas/compatibility-graph.json",
        "file_pattern": "*.compatibility.json",
        "content_type": "application/json",
        "description": "Agent relationship graph showing which agents can work together based on artifact flows. Maps producers to consumers, enabling intelligent multi-agent orchestration."
    },
    "pipeline-suggestion": {
        "schema": "schemas/pipeline-suggestion.json",
        "file_pattern": "*.pipeline.json",
        "content_type": "application/json",
        "description": "Suggested multi-agent workflow with step-by-step execution plan. Ensures artifact compatibility and provides rationale for agent selection."
    },
    "suggestion-report": {
        "schema": "schemas/suggestion-report.json",
        "file_pattern": "*.suggestions.json",
        "content_type": "application/json",
        "description": "Context-aware recommendations for what to do next after an agent completes. Includes ranked suggestions with rationale, required artifacts, and expected outcomes."
    },
    "skill-description": {
        "schema": "schemas/skill-description.json",
        "file_pattern": "**/skill_description.md",
        "content_type": "text/markdown",
        "description": "Natural language description of a skill's requirements, inputs, outputs, and implementation details. Used by meta.skill to generate complete skill implementations."
    },
    "skill-definition": {
        "schema": "schemas/skill-definition.json",
        "file_pattern": "skills/*/skill.yaml",
        "content_type": "application/yaml",
        "description": "Complete skill configuration in YAML format. Defines skill metadata, inputs, outputs, artifact metadata, permissions, and entrypoints."
    },

}


def get_artifact_definition(artifact_type: str) -> Optional[Dict[str, Any]]:
    """
    Get the definition for a known artifact type.

    Args:
        artifact_type: Artifact type identifier

    Returns:
        Artifact definition dictionary with schema, file_pattern, etc., or None if unknown
    """
    if artifact_type in KNOWN_ARTIFACT_TYPES:
        definition = {"type": artifact_type}
        definition.update(KNOWN_ARTIFACT_TYPES[artifact_type])
        return definition
    return None


def validate_artifact_type(artifact_type: str) -> tuple[bool, Optional[str]]:
    """
    Validate that an artifact type is known or suggest registering it.

    Args:
        artifact_type: Artifact type identifier

    Returns:
        Tuple of (is_valid, warning_message)
    """
    if artifact_type in KNOWN_ARTIFACT_TYPES:
        return True, None

    warning = f"Artifact type '{artifact_type}' is not in the known registry. "
    warning += "Consider documenting it in docs/ARTIFACT_STANDARDS.md and creating a schema."
    return False, warning


def generate_artifact_metadata(
    skill_name: str,
    produces: Optional[List[str]] = None,
    consumes: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Generate artifact metadata structure.

    Args:
        skill_name: Name of the skill
        produces: List of artifact types produced
        consumes: List of artifact types consumed

    Returns:
        Artifact metadata dictionary
    """
    metadata = {}
    warnings = []

    # Build produces section
    if produces:
        produces_list = []
        for artifact_type in produces:
            is_known, warning = validate_artifact_type(artifact_type)
            if warning:
                warnings.append(warning)

            artifact_def = {"type": artifact_type}

            # Add known metadata if available
            if artifact_type in KNOWN_ARTIFACT_TYPES:
                known = KNOWN_ARTIFACT_TYPES[artifact_type]
                if "schema" in known:
                    artifact_def["schema"] = known["schema"]
                if "file_pattern" in known:
                    artifact_def["file_pattern"] = known["file_pattern"]
                if "content_type" in known:
                    artifact_def["content_type"] = known["content_type"]
                if "description" in known:
                    artifact_def["description"] = known["description"]

            produces_list.append(artifact_def)

        metadata["produces"] = produces_list

    # Build consumes section
    if consumes:
        consumes_list = []
        for artifact_type in consumes:
            is_known, warning = validate_artifact_type(artifact_type)
            if warning:
                warnings.append(warning)

            artifact_def = {
                "type": artifact_type,
                "required": True  # Default to required
            }

            # Add description if known
            if artifact_type in KNOWN_ARTIFACT_TYPES:
                known = KNOWN_ARTIFACT_TYPES[artifact_type]
                if "description" in known:
                    artifact_def["description"] = known["description"]

            consumes_list.append(artifact_def)

        metadata["consumes"] = consumes_list

    return metadata, warnings


def format_as_yaml(metadata: Dict[str, Any]) -> str:
    """
    Format artifact metadata as YAML for inclusion in skill.yaml.

    Args:
        metadata: Artifact metadata dictionary

    Returns:
        Formatted YAML string
    """
    yaml_str = "artifact_metadata:\n"
    yaml_str += yaml.dump(metadata, default_flow_style=False, indent=2, sort_keys=False)
    return yaml_str


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Define artifact metadata for Betty Framework skills"
    )
    parser.add_argument(
        "skill_name",
        help="Name of the skill (e.g., api.define)"
    )
    parser.add_argument(
        "--produces",
        nargs="+",
        help="Artifact types this skill produces"
    )
    parser.add_argument(
        "--consumes",
        nargs="+",
        help="Artifact types this skill consumes"
    )
    parser.add_argument(
        "--output-file",
        default="artifact_metadata.yaml",
        help="Output file path"
    )

    args = parser.parse_args()

    logger.info(f"Generating artifact metadata for skill: {args.skill_name}")

    try:
        # Generate metadata
        metadata, warnings = generate_artifact_metadata(
            args.skill_name,
            produces=args.produces,
            consumes=args.consumes
        )

        # Format as YAML
        yaml_content = format_as_yaml(metadata)

        # Save to file
        output_path = args.output_file
        with open(output_path, 'w') as f:
            f.write(yaml_content)

        logger.info(f"✅ Generated artifact metadata: {output_path}")

        # Print to stdout
        print("\n# Add this to your skill.yaml:\n")
        print(yaml_content)

        # Show warnings
        if warnings:
            logger.warning("\n⚠️  Warnings:")
            for warning in warnings:
                logger.warning(f"  - {warning}")

        # Print summary
        logger.info("\n📋 Summary:")
        if metadata.get("produces"):
            logger.info(f"  Produces: {', '.join(a['type'] for a in metadata['produces'])}")
        if metadata.get("consumes"):
            logger.info(f"  Consumes: {', '.join(a['type'] for a in metadata['consumes'])}")

        # Success result
        result = {
            "ok": True,
            "status": "success",
            "skill_name": args.skill_name,
            "metadata": metadata,
            "output_file": output_path,
            "warnings": warnings
        }

        print("\n" + json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to generate artifact metadata: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
