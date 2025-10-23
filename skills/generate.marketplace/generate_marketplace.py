#!/usr/bin/env python3
"""
generate_marketplace.py - Implementation of the generate.marketplace Skill
Generates marketplace/skills.json and marketplace/agents.json from registry entries.
Filters by status: active and certified: true (if present).
"""

import os
import sys
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_registry_file(registry_path: str) -> Dict[str, Any]:
    """
    Load a JSON registry file.

    Args:
        registry_path: Path to the registry JSON file

    Returns:
        Parsed registry data

    Raises:
        FileNotFoundError: If registry file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    try:
        with open(registry_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Registry file not found: {registry_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {registry_path}: {e}")
        raise


def is_certified(item: Dict[str, Any]) -> bool:
    """
    Check if an item is certified for marketplace inclusion.

    Args:
        item: Skill or agent entry

    Returns:
        True if item should be included in marketplace
    """
    # Filter by status: active
    if item.get("status") != "active":
        return False

    # If certified field exists, check it
    if "certified" in item:
        return item.get("certified") is True

    # If no certified field, consider active items as certified
    return True


def convert_skill_to_marketplace(skill: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a registry skill entry to marketplace format.

    Args:
        skill: Skill entry from registry

    Returns:
        Skill entry in marketplace format
    """
    marketplace_skill = {
        "name": skill.get("name"),
        "version": skill.get("version"),
        "description": skill.get("description"),
        "status": "certified",  # Transform active -> certified for marketplace
        "tags": skill.get("tags", []),
        "maintainer": skill.get("maintainer", "Betty Core Team"),
        "usage_examples": skill.get("usage_examples", []),
        "documentation_url": f"https://betty-framework.dev/docs/skills/{skill.get('name')}",
        "dependencies": skill.get("dependencies", []),
        "entrypoints": skill.get("entrypoints", []),
        "inputs": skill.get("inputs", []),
        "outputs": skill.get("outputs", [])
    }

    # Generate usage examples if not present
    if not marketplace_skill["usage_examples"] and marketplace_skill["entrypoints"]:
        examples = []
        for entrypoint in marketplace_skill["entrypoints"]:
            command = entrypoint.get("command", "")
            desc = entrypoint.get("description", skill.get("description", ""))
            if command:
                # Create a simple example from the command
                example = f"Run {skill.get('name')}: {command}"
                examples.append(example.strip())
        marketplace_skill["usage_examples"] = examples[:2]  # Limit to 2 examples

    return marketplace_skill


def convert_agent_to_marketplace(agent: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a registry agent entry to marketplace format.

    Args:
        agent: Agent entry from registry

    Returns:
        Agent entry in marketplace format
    """
    marketplace_agent = {
        "name": agent.get("name"),
        "version": agent.get("version"),
        "description": agent.get("description"),
        "status": "certified",  # Transform active -> certified for marketplace
        "reasoning_mode": agent.get("reasoning_mode", "oneshot"),
        "skills_available": agent.get("skills_available", []),
        "capabilities": agent.get("capabilities", []),
        "tags": agent.get("tags", []),
        "maintainer": agent.get("maintainer", "Betty Core Team"),
        "documentation_url": f"https://betty-framework.dev/docs/agents/{agent.get('name')}",
        "dependencies": agent.get("dependencies", [])
    }

    return marketplace_agent


def generate_skills_marketplace(registry_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate marketplace skills catalog from registry.

    Args:
        registry_data: Parsed skills.json from registry

    Returns:
        Marketplace-formatted skills catalog
    """
    skills = registry_data.get("skills", [])

    # Filter and convert active/certified skills
    certified_skills = []
    for skill in skills:
        if is_certified(skill):
            marketplace_skill = convert_skill_to_marketplace(skill)
            certified_skills.append(marketplace_skill)
            logger.info(f"Added certified skill: {skill.get('name')}")
        else:
            logger.debug(f"Skipped non-certified skill: {skill.get('name')} (status: {skill.get('status')})")

    # Build marketplace catalog
    marketplace = {
        "marketplace_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Betty Framework Certified Skills Marketplace",
        "total_skills": len(skills),
        "certified_count": len(certified_skills),
        "draft_count": len(skills) - len(certified_skills),
        "catalog": certified_skills
    }

    return marketplace


def generate_agents_marketplace(registry_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate marketplace agents catalog from registry.

    Args:
        registry_data: Parsed agents.json from registry

    Returns:
        Marketplace-formatted agents catalog
    """
    agents = registry_data.get("agents", [])

    # Filter and convert active/certified agents
    certified_agents = []
    for agent in agents:
        if is_certified(agent):
            marketplace_agent = convert_agent_to_marketplace(agent)
            certified_agents.append(marketplace_agent)
            logger.info(f"Added certified agent: {agent.get('name')}")
        else:
            logger.debug(f"Skipped non-certified agent: {agent.get('name')} (status: {agent.get('status')})")

    # Build marketplace catalog
    marketplace = {
        "marketplace_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Betty Framework Certified Agents Marketplace",
        "total_agents": len(agents),
        "certified_count": len(certified_agents),
        "draft_count": len(agents) - len(certified_agents),
        "catalog": certified_agents
    }

    return marketplace


def write_marketplace_file(data: Dict[str, Any], output_path: str):
    """
    Write marketplace JSON file with proper formatting.

    Args:
        data: Marketplace data dictionary
        output_path: Path where to write the file
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    logger.info(f"✅ Written marketplace file to {output_path}")


def main():
    """Main CLI entry point."""
    logger.info("Starting marketplace catalog generation from registries...")

    # Define registry and output paths
    skills_registry_path = os.path.join(BASE_DIR, "registry", "skills.json")
    agents_registry_path = os.path.join(BASE_DIR, "registry", "agents.json")

    marketplace_dir = os.path.join(BASE_DIR, "marketplace")
    skills_output_path = os.path.join(marketplace_dir, "skills.json")
    agents_output_path = os.path.join(marketplace_dir, "agents.json")

    try:
        # Load registry files
        logger.info("Loading registry files...")
        skills_registry = load_registry_file(skills_registry_path)
        agents_registry = load_registry_file(agents_registry_path)

        # Generate marketplace catalogs
        logger.info("Generating marketplace catalogs...")
        skills_marketplace = generate_skills_marketplace(skills_registry)
        agents_marketplace = generate_agents_marketplace(agents_registry)

        # Write to files
        logger.info("Writing marketplace files...")
        write_marketplace_file(skills_marketplace, skills_output_path)
        write_marketplace_file(agents_marketplace, agents_output_path)

        # Report results
        result = {
            "ok": True,
            "status": "success",
            "skills_output": skills_output_path,
            "agents_output": agents_output_path,
            "skills_certified": skills_marketplace["certified_count"],
            "skills_total": skills_marketplace["total_skills"],
            "agents_certified": agents_marketplace["certified_count"],
            "agents_total": agents_marketplace["total_agents"]
        }

        # Print summary
        logger.info(f"✅ Generated marketplace catalogs:")
        logger.info(f"   Skills: {result['skills_certified']}/{result['skills_total']} certified")
        logger.info(f"   Agents: {result['agents_certified']}/{result['agents_total']} certified")
        logger.info(f"📄 Outputs:")
        logger.info(f"   - {skills_output_path}")
        logger.info(f"   - {agents_output_path}")

        print(json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to generate marketplace catalogs: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
