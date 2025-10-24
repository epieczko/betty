#!/usr/bin/env python3
"""
agent_compose.py - Recommend skills for Betty agents based on purpose

Analyzes skill artifact metadata to suggest compatible skill combinations.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional, Set
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_registry() -> Dict[str, Any]:
    """Load skills registry."""
    registry_path = os.path.join(BASE_DIR, "registry", "skills.json")
    with open(registry_path) as f:
        return json.load(f)


def extract_artifact_metadata(skill: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract artifact metadata from a skill.

    Returns:
        Dict with 'produces' and 'consumes' sets
    """
    metadata = skill.get("artifact_metadata", {})
    return {
        "produces": set(a.get("type") for a in metadata.get("produces", [])),
        "consumes": set(a.get("type") for a in metadata.get("consumes", []))
    }


def find_skills_by_artifacts(
    registry: Dict[str, Any],
    produces: Optional[List[str]] = None,
    consumes: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Find skills that produce or consume specific artifacts.

    Args:
        registry: Skills registry
        produces: Artifact types to produce
        consumes: Artifact types to consume

    Returns:
        List of matching skills with metadata
    """
    skills = registry.get("skills", [])
    matches = []

    for skill in skills:
        if skill.get("status") != "active":
            continue

        artifacts = extract_artifact_metadata(skill)

        # Check if skill produces required artifacts
        produces_match = not produces or any(
            artifact in artifacts["produces"] for artifact in produces
        )

        # Check if skill consumes specified artifacts
        consumes_match = not consumes or any(
            artifact in artifacts["consumes"] for artifact in consumes
        )

        if produces_match or consumes_match:
            matches.append({
                "name": skill["name"],
                "description": skill.get("description", ""),
                "produces": list(artifacts["produces"]),
                "consumes": list(artifacts["consumes"]),
                "tags": skill.get("tags", [])
            })

    return matches


def find_skills_for_purpose(
    registry: Dict[str, Any],
    purpose: str,
    required_artifacts: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Find skills for agent purpose (alias for recommend_skills_for_purpose).

    Args:
        registry: Skills registry (for compatibility, currently unused)
        purpose: Description of agent purpose
        required_artifacts: Artifact types agent needs to work with

    Returns:
        Recommendation result with skills and rationale
    """
    return recommend_skills_for_purpose(purpose, required_artifacts)


def recommend_skills_for_purpose(
    agent_purpose: str,
    required_artifacts: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Recommend skills based on agent purpose and required artifacts.

    Args:
        agent_purpose: Description of agent purpose
        required_artifacts: Artifact types agent needs to work with

    Returns:
        Recommendation result with skills and rationale
    """
    registry = load_registry()
    recommended = []
    rationale = {}

    # Keyword matching for purpose
    purpose_lower = agent_purpose.lower()
    keywords = {
        "api": ["api.define", "api.validate", "api.generate-models", "api.compatibility"],
        "workflow": ["workflow.validate", "workflow.compose"],
        "hook": ["hook.define"],
        "validate": ["api.validate", "workflow.validate"],
        "design": ["api.define"],
    }

    # Find skills by keywords
    matched_by_keyword = set()
    for keyword, skill_names in keywords.items():
        if keyword in purpose_lower:
            matched_by_keyword.update(skill_names)

    # Find skills by required artifacts
    matched_by_artifacts = set()
    if required_artifacts:
        artifact_skills = find_skills_by_artifacts(
            registry,
            produces=required_artifacts,
            consumes=required_artifacts
        )
        matched_by_artifacts.update(s["name"] for s in artifact_skills)

    # Combine matches
    all_matches = matched_by_keyword | matched_by_artifacts

    # Build recommendation with rationale
    skills = registry.get("skills", [])
    for skill in skills:
        skill_name = skill.get("name")

        if skill_name in all_matches:
            reasons = []

            if skill_name in matched_by_keyword:
                reasons.append(f"Purpose matches skill capabilities")

            artifacts = extract_artifact_metadata(skill)
            if required_artifacts:
                produces_match = artifacts["produces"] & set(required_artifacts)
                consumes_match = artifacts["consumes"] & set(required_artifacts)

                if produces_match:
                    reasons.append(f"Produces: {', '.join(produces_match)}")
                if consumes_match:
                    reasons.append(f"Consumes: {', '.join(consumes_match)}")

            recommended.append(skill_name)
            rationale[skill_name] = {
                "description": skill.get("description", ""),
                "reasons": reasons,
                "produces": list(artifacts["produces"]),
                "consumes": list(artifacts["consumes"])
            }

    return {
        "recommended_skills": recommended,
        "rationale": rationale,
        "total_recommended": len(recommended)
    }


def analyze_artifact_flow(skills_metadata: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze artifact flow between recommended skills.

    Args:
        skills_metadata: List of skill metadata

    Returns:
        Flow analysis showing how artifacts move between skills
    """
    all_produces = set()
    all_consumes = set()
    flows = []

    for skill in skills_metadata:
        produces = set(skill.get("produces", []))
        consumes = set(skill.get("consumes", []))

        all_produces.update(produces)
        all_consumes.update(consumes)

        for artifact in produces:
            consumers = [
                s["name"] for s in skills_metadata
                if artifact in s.get("consumes", [])
            ]
            if consumers:
                flows.append({
                    "artifact": artifact,
                    "producer": skill["name"],
                    "consumers": consumers
                })

    # Find gaps (consumed but not produced)
    gaps = all_consumes - all_produces

    return {
        "flows": flows,
        "gaps": list(gaps),
        "fully_covered": len(gaps) == 0
    }


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Recommend skills for a Betty agent"
    )
    parser.add_argument(
        "agent_purpose",
        help="Description of what the agent should do"
    )
    parser.add_argument(
        "--required-artifacts",
        nargs="+",
        help="Artifact types the agent needs to work with"
    )
    parser.add_argument(
        "--output-format",
        choices=["yaml", "json", "markdown"],
        default="yaml",
        help="Output format"
    )

    args = parser.parse_args()

    logger.info(f"Finding skills for agent purpose: {args.agent_purpose}")

    try:
        # Get recommendations
        result = recommend_skills_for_purpose(
            args.agent_purpose,
            args.required_artifacts
        )

        # Analyze artifact flow
        skills_metadata = list(result["rationale"].values())
        for skill_name, metadata in result["rationale"].items():
            metadata["name"] = skill_name

        flow_analysis = analyze_artifact_flow(skills_metadata)
        result["artifact_flow"] = flow_analysis

        # Format output
        if args.output_format == "yaml":
            print("\n# Recommended Skills for Agent\n")
            print(f"# Purpose: {args.agent_purpose}\n")
            print("skills_available:")
            for skill in result["recommended_skills"]:
                print(f"  - {skill}")

            print("\n# Rationale:")
            for skill_name, rationale in result["rationale"].items():
                print(f"\n# {skill_name}:")
                print(f"#   {rationale['description']}")
                for reason in rationale["reasons"]:
                    print(f"#   - {reason}")

        elif args.output_format == "markdown":
            print(f"\n## Recommended Skills for: {args.agent_purpose}\n")
            print("### Skills\n")
            for skill in result["recommended_skills"]:
                rationale = result["rationale"][skill]
                print(f"**{skill}**")
                print(f"- {rationale['description']}")
                for reason in rationale["reasons"]:
                    print(f"  - {reason}")
                print()

        else:  # json
            print(json.dumps(result, indent=2))

        # Show warnings for gaps
        if flow_analysis["gaps"]:
            logger.warning(f"\n⚠️  Artifact gaps detected:")
            for gap in flow_analysis["gaps"]:
                logger.warning(f"  - '{gap}' is consumed but not produced")
            logger.warning("  Consider adding skills that produce these artifacts")

        logger.info(f"\n✅ Recommended {result['total_recommended']} skills")

        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to compose agent: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
