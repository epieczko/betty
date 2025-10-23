#!/usr/bin/env python3
"""
Generate Betty Framework Marketplace Catalog

This script scans the registry and generates a curated marketplace catalog
for certified skills and agents that are ready for production use.

Usage:
    python generate_marketplace.py
    python generate_marketplace.py --include-drafts
"""

import json
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any


# Metadata configuration for certified skills
SKILL_METADATA = {
    "skill.define": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Validate a new skill manifest: /skill/define manifest.skill.yaml",
            "Check skill compliance before registration"
        ],
        "documentation_url": "https://betty-framework.dev/docs/skills/define"
    },
    "workflow.validate": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Validate workflow structure: /workflow/validate my_workflow.yaml",
            "Pre-flight check before workflow execution"
        ],
        "documentation_url": "https://betty-framework.dev/docs/workflows/validate"
    },
    "registry.update": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Register a new skill: /registry/update skill_manifest.yaml",
            "Update existing skill entry in registry"
        ],
        "documentation_url": "https://betty-framework.dev/docs/registry/update"
    },
    "hook.define": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Create validation hook: /skill/hook/define --event on_file_edit --pattern '*.yaml' --command /workflow/validate",
            "Set up pre-commit API validation hook"
        ],
        "documentation_url": "https://betty-framework.dev/docs/hooks/define"
    },
    "api.validate": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Validate OpenAPI spec: /skill/api/validate --spec_path api.openapi.yaml",
            "Check against Zalando guidelines: /skill/api/validate --spec_path api.yaml --guideline_set zalando"
        ],
        "documentation_url": "https://betty-framework.dev/docs/api/validate"
    },
    "api.define": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Create new OpenAPI spec: /skill/api/define --service_name user-service",
            "Generate AsyncAPI spec: /skill/api/define --service_name events --spec_type asyncapi"
        ],
        "documentation_url": "https://betty-framework.dev/docs/api/define"
    },
    "api.generate-models": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Generate TypeScript models: /skill/api/generate-models --spec_path api.yaml --language typescript",
            "Generate Python models: /skill/api/generate-models --spec_path api.yaml --language python --output_dir src/models"
        ],
        "documentation_url": "https://betty-framework.dev/docs/api/generate-models"
    },
    "api.compatibility": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Check for breaking changes: /skill/api/compatibility --old_spec_path v1.yaml --new_spec_path v2.yaml",
            "Analyze API evolution: /skill/api/compatibility --old_spec_path old.yaml --new_spec_path new.yaml --fail_on_breaking false"
        ],
        "documentation_url": "https://betty-framework.dev/docs/api/compatibility"
    },
    "agent.define": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Validate agent manifest: /agent/define agent.yaml",
            "Register new agent in the framework"
        ],
        "documentation_url": "https://betty-framework.dev/docs/agents/define"
    },
    "command.define": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Register command manifest: /skill/command/define command.yaml",
            "Add new CLI command to Betty"
        ],
        "documentation_url": "https://betty-framework.dev/docs/commands/define"
    },
    "hook.register": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Register hook manifest: /skill/hook/register hook.yaml",
            "Enable policy enforcement via hooks"
        ],
        "documentation_url": "https://betty-framework.dev/docs/hooks/register"
    },
    "workflow.compose": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Execute multi-step workflow: /workflow/compose pipeline.yaml",
            "Chain multiple skills together"
        ],
        "documentation_url": "https://betty-framework.dev/docs/workflows/compose"
    },
    "skill.create": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Scaffold new skill: /skill/create --skill_name my.skill --description 'My new skill'",
            "Bootstrap skill with inputs/outputs: /skill/create --skill_name process.data --inputs 'data,config' --outputs 'result'"
        ],
        "documentation_url": "https://betty-framework.dev/docs/skills/create"
    },
    "policy.enforce": {
        "maintainer": "Betty Core Team",
        "certification_status": "certified",
        "usage_examples": [
            "Validate against organizational policy: skill executes policy.enforce before operation",
            "Enforce compliance rules on API changes"
        ],
        "documentation_url": "https://betty-framework.dev/docs/policy/enforce"
    }
}


# Metadata configuration for certified agents
AGENT_METADATA = {
    "api.designer": {
        "maintainer": "Betty Core Team",
        "certification_status": "draft",
        "usage_examples": [
            "Design new API from requirements: Ask Claude to use api.designer agent",
            "Generate OpenAPI spec with Zalando guidelines applied"
        ],
        "documentation_url": "https://betty-framework.dev/docs/agents/api-designer"
    },
    "api.analyzer": {
        "maintainer": "Betty Core Team",
        "certification_status": "draft",
        "usage_examples": [
            "Analyze API compatibility: Ask Claude to use api.analyzer agent",
            "Generate breaking change report between versions"
        ],
        "documentation_url": "https://betty-framework.dev/docs/agents/api-analyzer"
    }
}


def load_json_file(file_path: Path) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json_file(file_path: Path, data: Dict[str, Any]) -> None:
    """Save data to a JSON file with pretty formatting."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def enrich_skill(skill: Dict[str, Any]) -> Dict[str, Any]:
    """Add marketplace metadata to a skill entry."""
    skill_name = skill.get('name')
    metadata = SKILL_METADATA.get(skill_name, {
        "maintainer": "Community",
        "certification_status": "draft" if skill.get('status') == 'draft' else "certified",
        "usage_examples": [],
        "documentation_url": f"https://betty-framework.dev/docs/skills/{skill_name}"
    })

    # Create marketplace entry
    marketplace_entry = {
        "name": skill.get('name'),
        "version": skill.get('version'),
        "description": skill.get('description'),
        "status": metadata.get('certification_status', 'draft'),
        "tags": skill.get('tags', []),
        "maintainer": metadata.get('maintainer'),
        "usage_examples": metadata.get('usage_examples'),
        "documentation_url": metadata.get('documentation_url'),
        "dependencies": skill.get('dependencies', []),
        "entrypoints": skill.get('entrypoints', [])
    }

    # Add optional fields if present
    if skill.get('inputs'):
        marketplace_entry['inputs'] = skill['inputs']
    if skill.get('outputs'):
        marketplace_entry['outputs'] = skill['outputs']

    return marketplace_entry


def enrich_agent(agent: Dict[str, Any]) -> Dict[str, Any]:
    """Add marketplace metadata to an agent entry."""
    agent_name = agent.get('name')
    metadata = AGENT_METADATA.get(agent_name, {
        "maintainer": "Community",
        "certification_status": agent.get('status', 'draft'),
        "usage_examples": [],
        "documentation_url": f"https://betty-framework.dev/docs/agents/{agent_name}"
    })

    # Create marketplace entry
    marketplace_entry = {
        "name": agent.get('name'),
        "version": agent.get('version'),
        "description": agent.get('description'),
        "status": metadata.get('certification_status', 'draft'),
        "tags": agent.get('tags', []),
        "maintainer": metadata.get('maintainer'),
        "usage_examples": metadata.get('usage_examples'),
        "documentation_url": metadata.get('documentation_url'),
        "reasoning_mode": agent.get('reasoning_mode'),
        "skills_available": agent.get('skills_available', []),
        "capabilities": agent.get('capabilities', []),
        "dependencies": agent.get('dependencies', [])
    }

    return marketplace_entry


def generate_skills_marketplace(
    registry_path: Path,
    output_path: Path,
    include_drafts: bool = False
) -> Dict[str, Any]:
    """Generate the skills marketplace catalog."""
    registry = load_json_file(registry_path)
    skills = registry.get('skills', [])

    # Filter for active skills (or include drafts if requested)
    if include_drafts:
        filtered_skills = [s for s in skills if s.get('status') in ['active', 'draft']]
    else:
        filtered_skills = [s for s in skills if s.get('status') == 'active']

    # Enrich with metadata
    marketplace_skills = [enrich_skill(skill) for skill in filtered_skills]

    # Sort by name
    marketplace_skills.sort(key=lambda x: x['name'])

    marketplace = {
        "marketplace_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Betty Framework Certified Skills Marketplace",
        "total_skills": len(marketplace_skills),
        "certified_count": sum(1 for s in marketplace_skills if s['status'] == 'certified'),
        "draft_count": sum(1 for s in marketplace_skills if s['status'] == 'draft'),
        "catalog": marketplace_skills
    }

    save_json_file(output_path, marketplace)
    return marketplace


def generate_agents_marketplace(
    registry_path: Path,
    output_path: Path,
    include_drafts: bool = False
) -> Dict[str, Any]:
    """Generate the agents marketplace catalog."""
    registry = load_json_file(registry_path)
    agents = registry.get('agents', [])

    # Filter agents based on status
    if include_drafts:
        filtered_agents = agents
    else:
        filtered_agents = [a for a in agents if a.get('status') == 'certified']

    # Enrich with metadata
    marketplace_agents = [enrich_agent(agent) for agent in filtered_agents]

    # Sort by name
    marketplace_agents.sort(key=lambda x: x['name'])

    marketplace = {
        "marketplace_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Betty Framework Certified Agents Marketplace",
        "total_agents": len(marketplace_agents),
        "certified_count": sum(1 for a in marketplace_agents if a['status'] == 'certified'),
        "draft_count": sum(1 for a in marketplace_agents if a['status'] == 'draft'),
        "catalog": marketplace_agents
    }

    save_json_file(output_path, marketplace)
    return marketplace


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate Betty Framework Marketplace Catalog'
    )
    parser.add_argument(
        '--include-drafts',
        action='store_true',
        help='Include draft skills and agents in the marketplace'
    )
    parser.add_argument(
        '--registry-dir',
        type=Path,
        default=Path('registry'),
        help='Path to registry directory (default: registry/)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('marketplace'),
        help='Path to output directory (default: marketplace/)'
    )

    args = parser.parse_args()

    # Ensure output directory exists
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Generate skills marketplace
    print(f"Generating skills marketplace...")
    skills_registry = args.registry_dir / 'skills.json'
    skills_output = args.output_dir / 'skills.json'
    skills_marketplace = generate_skills_marketplace(
        skills_registry,
        skills_output,
        args.include_drafts
    )
    print(f"✓ Skills marketplace generated: {skills_output}")
    print(f"  - Total: {skills_marketplace['total_skills']}")
    print(f"  - Certified: {skills_marketplace['certified_count']}")
    print(f"  - Draft: {skills_marketplace['draft_count']}")

    # Generate agents marketplace
    print(f"\nGenerating agents marketplace...")
    agents_registry = args.registry_dir / 'agents.json'
    agents_output = args.output_dir / 'agents.json'
    agents_marketplace = generate_agents_marketplace(
        agents_registry,
        agents_output,
        args.include_drafts
    )
    print(f"✓ Agents marketplace generated: {agents_output}")
    print(f"  - Total: {agents_marketplace['total_agents']}")
    print(f"  - Certified: {agents_marketplace['certified_count']}")
    print(f"  - Draft: {agents_marketplace['draft_count']}")

    print(f"\n✓ Marketplace generation complete!")


if __name__ == '__main__':
    main()
