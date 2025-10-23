#!/usr/bin/env python3
"""
readme_sync.py - Implementation of the docs.sync.readme Skill
Regenerates the top-level README.md to reflect all current registered skills and agents.
"""

import os
import sys
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR, REGISTRY_FILE, AGENTS_REGISTRY_FILE
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_registry(registry_path: str) -> Dict[str, Any]:
    """
    Load a JSON registry file.

    Args:
        registry_path: Path to registry JSON file

    Returns:
        Parsed registry data
    """
    try:
        with open(registry_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Registry file not found: {registry_path}")
        return {"skills": []} if "skills" in registry_path else {"agents": []}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {registry_path}: {e}")
        raise


def categorize_skills(skills: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Categorize skills by their tags into foundation, api, infrastructure, and governance groups.

    Args:
        skills: List of skill dictionaries from registry

    Returns:
        Dictionary mapping category names to lists of skills
    """
    categories = {
        "foundation": [],
        "api": [],
        "infrastructure": [],
        "governance": []
    }

    for skill in skills:
        # Only include active skills
        if skill.get("status") != "active":
            continue

        # Skip test skills
        if skill.get("name", "").startswith("test."):
            continue

        tags = skill.get("tags", [])
        name = skill.get("name", "")

        # Categorize based on tags or name patterns
        if any(tag in ["api", "openapi", "asyncapi"] for tag in tags) or name.startswith("api."):
            categories["api"].append(skill)
        elif any(tag in ["agents", "command", "hook", "policy", "plugin", "registry"] for tag in tags):
            categories["infrastructure"].append(skill)
        elif any(tag in ["governance", "policy", "audit"] for tag in tags):
            categories["governance"].append(skill)
        elif name.startswith("skill.") or name.startswith("registry.") or name.startswith("workflow."):
            categories["foundation"].append(skill)
        else:
            # Default to infrastructure if unclear
            categories["infrastructure"].append(skill)

    # Remove duplicates and sort by name
    for category in categories:
        seen = set()
        unique_skills = []
        for skill in categories[category]:
            if skill["name"] not in seen:
                seen.add(skill["name"])
                unique_skills.append(skill)
        categories[category] = sorted(unique_skills, key=lambda s: s["name"])

    return categories


def format_skill_table(skills: List[Dict[str, Any]]) -> str:
    """
    Format a list of skills as a markdown table.

    Args:
        skills: List of skill dictionaries

    Returns:
        Markdown table string
    """
    if not skills:
        return "| Skill | Purpose |\n|--------|----------|\n| _(No skills in this category)_ | |"

    lines = ["| Skill | Purpose |", "|--------|----------|"]

    for skill in skills:
        name = skill.get("name", "")
        # Get first line of description only
        desc = skill.get("description", "").strip().split("\n")[0]
        # Clean up description (remove extra whitespace)
        desc = " ".join(desc.split())

        lines.append(f"| **{name}** | {desc} |")

    return "\n".join(lines)


def format_agents_docs(agents: List[Dict[str, Any]]) -> str:
    """
    Format agent documentation links.

    Args:
        agents: List of agent dictionaries

    Returns:
        Markdown list of agent links
    """
    if not agents:
        return "_(No agents registered)_"

    lines = []
    for agent in agents:
        name = agent.get("name", "")
        # Get first line of description only
        desc = agent.get("description", "").strip().split("\n")[0]
        desc = " ".join(desc.split())

        lines.append(f"* [{name}](agents/{name}/README.md) — {desc}")

    return "\n".join(lines)


def update_readme_section(
    content: str,
    section_marker: str,
    end_marker: str,
    new_content: str
) -> str:
    """
    Update a section of the README between two markers.

    Args:
        content: Full README content
        section_marker: Start marker (e.g., "## 🧩 Current Core Skills")
        end_marker: End marker (e.g., "---")
        new_content: New content to insert between markers

    Returns:
        Updated README content
    """
    # Find section start
    section_start = content.find(section_marker)
    if section_start == -1:
        logger.warning(f"Section marker not found: {section_marker}")
        return content

    # Find section end after the start - look for the end marker on its own line
    search_start = section_start + len(section_marker)
    end_marker_pattern = f"\n{end_marker}\n"
    section_end = content.find(end_marker_pattern, search_start)

    if section_end == -1:
        logger.warning(f"End marker not found after {section_marker}")
        return content

    # Replace the section (include the newline before end marker)
    before = content[:section_start]
    after = content[section_end + 1:]  # +1 to skip the first newline

    return before + section_marker + "\n\n" + new_content + "\n" + after


def generate_skills_section(categories: Dict[str, List[Dict[str, Any]]]) -> str:
    """
    Generate the complete skills section content.

    Args:
        categories: Dictionary of categorized skills

    Returns:
        Markdown content for skills section
    """
    lines = [
        "Betty's self-referential \"kernel\" of skills bootstraps the rest of the system:",
        ""
    ]

    # Foundation Skills
    if categories["foundation"]:
        lines.extend([
            "### Foundation Skills",
            "",
            format_skill_table(categories["foundation"]),
            ""
        ])

    # API Development Skills
    if categories["api"]:
        lines.extend([
            "### API Development Skills",
            "",
            format_skill_table(categories["api"]),
            ""
        ])

    # Infrastructure Skills
    if categories["infrastructure"]:
        lines.extend([
            "### Infrastructure Skills",
            "",
            format_skill_table(categories["infrastructure"]),
            ""
        ])

    # Governance Skills (if any)
    if categories["governance"]:
        lines.extend([
            "### Governance Skills",
            "",
            format_skill_table(categories["governance"]),
            ""
        ])

    lines.append("These skills form the baseline for an **AI-native SDLC** where creation, validation, registration, and orchestration are themselves skills.")

    return "\n".join(lines)


def update_agents_section(content: str, agents: List[Dict[str, Any]]) -> str:
    """
    Update the Agents Documentation section.

    Args:
        content: Full README content
        agents: List of active agents

    Returns:
        Updated README content
    """
    agents_docs = format_agents_docs(agents)

    # Find the "### Agents Documentation" section
    section_start = content.find("### Agents Documentation")
    if section_start == -1:
        logger.warning("Agents Documentation section not found")
        return content

    # Find the next ### or ## to determine section end
    next_section = content.find("\n##", section_start + 25)
    if next_section == -1:
        next_section = len(content)

    # Find "Each agent has a" line as the start of actual content
    intro_start = content.find("Each agent has a `README.md` in its directory:", section_start)
    if intro_start == -1:
        intro_start = section_start + 25
    else:
        intro_start += len("Each agent has a `README.md` in its directory:")

    before = content[:intro_start]
    after = content[next_section:]

    return before + "\n" + agents_docs + "\n\n" + after


def generate_readme(
    skills_data: Dict[str, Any],
    agents_data: Dict[str, Any]
) -> tuple[str, Dict[str, Any]]:
    """
    Generate updated README.md content.

    Args:
        skills_data: Parsed skills.json
        agents_data: Parsed agents.json

    Returns:
        Tuple of (updated_readme_content, report_dict)
    """
    readme_path = os.path.join(BASE_DIR, "README.md")

    # Read current README
    try:
        with open(readme_path) as f:
            content = f.read()
    except FileNotFoundError:
        logger.error(f"README.md not found at {readme_path}")
        raise

    # Categorize skills
    skills = skills_data.get("skills", [])
    categories = categorize_skills(skills)

    # Get active agents
    agents = [a for a in agents_data.get("agents", []) if a.get("status") == "active" or a.get("status") == "draft"]
    agents = sorted(agents, key=lambda a: a["name"])

    # Generate new skills section
    skills_section = generate_skills_section(categories)

    # Update skills section
    content = update_readme_section(
        content,
        "## 🧩 Current Core Skills",
        "---",
        skills_section
    )

    # Update agents section
    content = update_agents_section(content, agents)

    # Generate report
    report = {
        "skills_by_category": {
            "foundation": len(categories["foundation"]),
            "api": len(categories["api"]),
            "infrastructure": len(categories["infrastructure"]),
            "governance": len(categories["governance"])
        },
        "total_skills": sum(len(skills) for skills in categories.values()),
        "agents_count": len(agents),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    return content, report


def main():
    """Main CLI entry point."""
    logger.info("Starting README.md sync from registries...")

    try:
        # Load registries
        logger.info("Loading registry files...")
        skills_data = load_registry(REGISTRY_FILE)
        agents_data = load_registry(AGENTS_REGISTRY_FILE)

        # Generate updated README
        logger.info("Generating updated README content...")
        readme_content, report = generate_readme(skills_data, agents_data)

        # Write README
        readme_path = os.path.join(BASE_DIR, "README.md")
        with open(readme_path, 'w') as f:
            f.write(readme_content)

        logger.info(f"✅ Updated README.md")
        logger.info(f"   - Foundation skills: {report['skills_by_category']['foundation']}")
        logger.info(f"   - API skills: {report['skills_by_category']['api']}")
        logger.info(f"   - Infrastructure skills: {report['skills_by_category']['infrastructure']}")
        logger.info(f"   - Governance skills: {report['skills_by_category']['governance']}")
        logger.info(f"   - Total active skills: {report['total_skills']}")
        logger.info(f"   - Agents: {report['agents_count']}")

        # Write report
        report_path = os.path.join(BASE_DIR, "skills", "docs.sync.readme", "sync_report.json")
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        result = {
            "ok": True,
            "status": "success",
            "readme_path": readme_path,
            "report": report
        }

        print(json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to sync README: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
