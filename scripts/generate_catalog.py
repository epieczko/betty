#!/usr/bin/env python3
"""
Repository Catalog Generator for Betty
Scans skills, agents, hooks, commands, and artifact types to generate comprehensive catalogs
"""

import os
import json
import yaml
import glob
import re
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict

# Base directory
BASE_DIR = Path("/home/user/betty")
OUTPUT_DIR = BASE_DIR / "registry" / "taxonomy"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Canonical domains
CANONICAL_DOMAINS = [
    "architecture", "api", "data", "security", "testing",
    "deployment", "governance", "docs", "operations", "ai"
]

# Functional roles
FUNCTIONAL_ROLES = [
    "create", "validate", "review", "analyze", "orchestrate", "govern", "observe"
]


def scan_skills() -> List[Dict[str, Any]]:
    """Scan all skills/**/skill.yaml files"""
    print("📚 Scanning skills...")
    skills = []
    skill_files = glob.glob(str(BASE_DIR / "skills" / "**" / "skill.yaml"), recursive=True)

    for skill_file in skill_files:
        try:
            with open(skill_file, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    skill_path = Path(skill_file).parent.name
                    skills.append({
                        "type": "skill",
                        "name": data.get("name", skill_path),
                        "description": data.get("description", ""),
                        "inputs": data.get("inputs", []),
                        "outputs": data.get("outputs", []),
                        "tags": data.get("tags", []),
                        "artifact_metadata": data.get("artifact_metadata", {}),
                        "path": skill_file,
                        "domain": extract_domain_from_name(data.get("name", skill_path)),
                    })
        except Exception as e:
            print(f"  ⚠️  Error reading {skill_file}: {e}")

    print(f"  ✓ Found {len(skills)} skills")
    return skills


def scan_agents() -> List[Dict[str, Any]]:
    """Scan all agents/**/agent.yaml files"""
    print("🤖 Scanning agents...")
    agents = []
    agent_files = glob.glob(str(BASE_DIR / "agents" / "**" / "agent.yaml"), recursive=True)

    for agent_file in agent_files:
        try:
            with open(agent_file, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    agent_path = Path(agent_file).parent.name
                    agents.append({
                        "type": "agent",
                        "name": data.get("name", agent_path),
                        "role": data.get("role", ""),
                        "description": data.get("description", ""),
                        "skills_used": data.get("skills", []),
                        "skills_available": data.get("skills_available", []),
                        "tags": data.get("tags", []),
                        "path": agent_file,
                        "domain": extract_domain_from_name(data.get("name", agent_path)),
                    })
        except Exception as e:
            print(f"  ⚠️  Error reading {agent_file}: {e}")

    print(f"  ✓ Found {len(agents)} agents")
    return agents


def scan_hooks() -> List[Dict[str, Any]]:
    """Scan .claude/hooks.yaml"""
    print("🪝 Scanning hooks...")
    hooks = []
    hooks_file = BASE_DIR / ".claude" / "hooks.yaml"

    try:
        with open(hooks_file, 'r') as f:
            data = yaml.safe_load(f)
            if data and "hooks" in data and isinstance(data["hooks"], list):
                for hook_config in data["hooks"]:
                    hooks.append({
                        "type": "hook",
                        "name": hook_config.get("name", ""),
                        "event": hook_config.get("event", ""),
                        "condition": hook_config.get("condition", ""),
                        "target_command": hook_config.get("command", ""),
                        "description": hook_config.get("description", ""),
                        "tags": hook_config.get("tags", []),
                        "enabled": hook_config.get("enabled", True),
                        "path": str(hooks_file),
                    })
    except Exception as e:
        print(f"  ⚠️  Error reading hooks: {e}")

    print(f"  ✓ Found {len(hooks)} hooks")
    return hooks


def scan_commands() -> List[Dict[str, Any]]:
    """Scan .claude/commands/*.md files"""
    print("⚡ Scanning commands...")
    commands = []
    command_files = glob.glob(str(BASE_DIR / ".claude" / "commands" / "*.md"))

    for cmd_file in command_files:
        if "README.md" in cmd_file:
            continue

        try:
            with open(cmd_file, 'r') as f:
                content = f.read()

            # Extract command name from filename
            cmd_name = "/" + Path(cmd_file).stem

            # Extract summary (first non-empty line or first heading)
            lines = content.split("\n")
            summary = ""
            mapped_skill = None
            mapped_agent = None

            for line in lines:
                if line.strip() and not summary:
                    summary = line.strip("# ").strip()

                # Look for skill/agent references
                if "skill:" in line.lower():
                    match = re.search(r'skill:\s*([a-z.]+)', line, re.IGNORECASE)
                    if match:
                        mapped_skill = match.group(1)

                if "agent:" in line.lower():
                    match = re.search(r'agent:\s*([a-z.]+)', line, re.IGNORECASE)
                    if match:
                        mapped_agent = match.group(1)

            commands.append({
                "type": "command",
                "name": cmd_name,
                "summary": summary,
                "mapped_skill": mapped_skill,
                "mapped_agent": mapped_agent,
                "path": cmd_file,
            })
        except Exception as e:
            print(f"  ⚠️  Error reading {cmd_file}: {e}")

    print(f"  ✓ Found {len(commands)} commands")
    return commands


def parse_artifact_types() -> List[Dict[str, Any]]:
    """Parse registry/artifact_types.json"""
    print("📦 Parsing artifact types...")
    artifact_types = []

    try:
        artifact_file = BASE_DIR / "registry" / "artifact_types.json"
        with open(artifact_file, 'r') as f:
            data = json.load(f)

        # Handle both list and dict formats
        artifacts_list = data.get("artifact_types", []) if isinstance(data, dict) else data

        for artifact_data in artifacts_list:
            artifact_types.append({
                "type": "artifact_type",
                "id": artifact_data.get("name", ""),
                "name": artifact_data.get("name", ""),
                "description": artifact_data.get("description", ""),
                "file_pattern": artifact_data.get("file_pattern", ""),
                "content_type": artifact_data.get("content_type", ""),
                "schema": artifact_data.get("schema", ""),
            })
    except Exception as e:
        print(f"  ⚠️  Error parsing artifact types: {e}")

    print(f"  ✓ Found {len(artifact_types)} artifact types")
    return artifact_types


def extract_domain_from_name(name: str) -> str:
    """Extract domain from component name (e.g., 'api.validate' -> 'api')"""
    if "." in name:
        prefix = name.split(".")[0].lower()
        # Map common prefixes to canonical domains
        domain_map = {
            "api": "api",
            "data": "data",
            "docs": "docs",
            "security": "security",
            "test": "testing",
            "deploy": "deployment",
            "workflow": "operations",
            "policy": "governance",
            "meta": "ai",
            "agent": "ai",
            "artifact": "architecture",
            "skill": "architecture",
            "command": "architecture",
            "hook": "architecture",
            "registry": "governance",
            "plugin": "deployment",
            "telemetry": "operations",
            "audit": "governance",
            "code": "operations",
            "build": "operations",
            "git": "operations",
            "epic": "architecture",
            "story": "architecture",
            "generate": "ai",
            "file": "operations",
        }
        return domain_map.get(prefix, "operations")
    return "operations"


def assign_role(component: Dict[str, Any]) -> str:
    """Assign functional role based on component name and metadata"""
    name = component.get("name", "").lower()

    # Role mapping based on verbs in names
    if any(verb in name for verb in ["create", "define", "write", "compose", "generate", "scaffold"]):
        return "create"
    elif any(verb in name for verb in ["validate", "test", "check"]):
        return "validate"
    elif any(verb in name for verb in ["review", "audit", "lint"]):
        return "review"
    elif any(verb in name for verb in ["analyze", "query", "diff", "compare"]):
        return "analyze"
    elif any(verb in name for verb in ["orchestrate", "run", "execute", "compose"]):
        return "orchestrate"
    elif any(verb in name for verb in ["govern", "enforce", "policy", "manage"]):
        return "govern"
    elif any(verb in name for verb in ["observe", "capture", "log", "monitor"]):
        return "observe"

    # Default based on component type
    if component.get("type") == "agent":
        if "architect" in name:
            return "create"
        elif "manager" in name:
            return "govern"
        else:
            return "analyze"

    return "analyze"


def normalize_component(component: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize component data"""
    normalized = component.copy()

    # Normalize name
    if "name" in normalized:
        normalized["name"] = normalized["name"].lower().strip()

    # Add role if not present
    if "role" not in normalized or not normalized["role"]:
        normalized["role"] = assign_role(component)

    # Ensure domain is canonical
    if "domain" in normalized and normalized["domain"] not in CANONICAL_DOMAINS:
        normalized["domain"] = "operations"

    return normalized


def build_relationships(skills: List[Dict], agents: List[Dict],
                       hooks: List[Dict], commands: List[Dict],
                       artifact_types: List[Dict]) -> Dict[str, List]:
    """Map relationships between components"""
    print("🔗 Building relationships...")

    relationships = {
        "skills_to_agents": [],
        "agents_to_hooks": [],
        "hooks_to_commands": [],
        "skills_to_artifacts": [],
        "artifact_producers": {},
        "artifact_consumers": {},
    }

    # Map skills to agents (read agent files to get actual skill usage)
    skill_names = {s["name"] for s in skills}
    for agent in agents:
        # Try to read the agent's manifest to get skills
        agent_path = agent.get("path", "")
        if agent_path and os.path.exists(agent_path):
            try:
                with open(agent_path, 'r') as f:
                    agent_data = yaml.safe_load(f)
                    # Check both 'skills' and 'skills_available' fields
                    skills_used = agent_data.get("skills", agent_data.get("skills_available", []))
                    for skill in skills_used:
                        # Handle both direct names and skill references
                        skill_name = skill if isinstance(skill, str) else skill.get("name", "")
                        if skill_name and skill_name in skill_names:
                            relationships["skills_to_agents"].append({
                                "skill": skill_name,
                                "agent": agent["name"]
                            })
            except:
                pass

    # Map hooks to commands
    for hook in hooks:
        target = hook.get("target_command", "")
        if target:
            # Extract command name from the target
            cmd_match = re.search(r'/[\w-]+', target)
            if cmd_match:
                relationships["hooks_to_commands"].append({
                    "hook": hook["name"],
                    "command": cmd_match.group(0)
                })

    # Map skills to artifacts (producers and consumers)
    for skill in skills:
        artifact_meta = skill.get("artifact_metadata", {})

        # Check outputs for produced artifacts
        outputs = skill.get("outputs", [])
        for output in outputs:
            output_type = output.get("type", "") if isinstance(output, dict) else output
            if output_type:
                if output_type not in relationships["artifact_producers"]:
                    relationships["artifact_producers"][output_type] = []
                relationships["artifact_producers"][output_type].append(skill["name"])

        # Check inputs for consumed artifacts
        inputs = skill.get("inputs", [])
        for inp in inputs:
            input_type = inp.get("type", "") if isinstance(inp, dict) else inp
            if input_type:
                if input_type not in relationships["artifact_consumers"]:
                    relationships["artifact_consumers"][input_type] = []
                relationships["artifact_consumers"][input_type].append(skill["name"])

        # Also check artifact_metadata
        if artifact_meta:
            produces = artifact_meta.get("produces", [])
            for artifact in produces:
                # Handle both string and dict formats
                artifact_name = artifact if isinstance(artifact, str) else artifact.get("type", "") if isinstance(artifact, dict) else ""
                if artifact_name:
                    if artifact_name not in relationships["artifact_producers"]:
                        relationships["artifact_producers"][artifact_name] = []
                    relationships["artifact_producers"][artifact_name].append(skill["name"])

            consumes = artifact_meta.get("consumes", [])
            for artifact in consumes:
                # Handle both string and dict formats
                artifact_name = artifact if isinstance(artifact, str) else artifact.get("type", "") if isinstance(artifact, dict) else ""
                if artifact_name:
                    if artifact_name not in relationships["artifact_consumers"]:
                        relationships["artifact_consumers"][artifact_name] = []
                    relationships["artifact_consumers"][artifact_name].append(skill["name"])

    print(f"  ✓ Mapped {len(relationships['skills_to_agents'])} skill→agent relationships")
    print(f"  ✓ Mapped {len(relationships['artifact_producers'])} artifact producers")
    print(f"  ✓ Mapped {len(relationships['artifact_consumers'])} artifact consumers")
    return relationships


def build_category_matrix(components: List[Dict]) -> Dict[str, Dict]:
    """Build category matrix grouped by domain"""
    print("📊 Building category matrix...")

    matrix = defaultdict(lambda: {
        "skills": [],
        "agents": [],
        "hooks": [],
        "commands": [],
        "missing": []
    })

    for comp in components:
        domain = comp.get("domain", "operations")
        comp_type = comp.get("type", "unknown")

        if comp_type == "skill":
            matrix[domain]["skills"].append(comp["name"])
        elif comp_type == "agent":
            matrix[domain]["agents"].append(comp["name"])
        elif comp_type == "hook":
            matrix[domain]["hooks"].append(comp["name"])
        elif comp_type == "command":
            matrix[domain]["commands"].append(comp["name"])

    return dict(matrix)


def detect_gaps(components: List[Dict], artifact_types: List[Dict],
                category_matrix: Dict, relationships: Dict) -> Dict[str, Any]:
    """Detect missing components and gaps"""
    print("🔍 Detecting gaps...")

    gaps = {
        "missing_producers": [],
        "missing_consumers": [],
        "missing_orchestrators": [],
        "naming_violations": [],
        "underutilized_artifacts": [],
    }

    # Get artifact producer/consumer mappings
    artifact_producers = relationships.get("artifact_producers", {})
    artifact_consumers = relationships.get("artifact_consumers", {})

    # Sample check for missing producers/consumers (checking first 20 artifact types)
    checked_artifacts = artifact_types[:20] if len(artifact_types) > 20 else artifact_types

    for artifact in checked_artifacts:
        artifact_name = artifact.get("name", "")
        artifact_id = artifact.get("id", artifact_name)

        # Check for missing producers
        if artifact_name not in artifact_producers and artifact_id not in artifact_producers:
            gaps["missing_producers"].append({
                "artifact": artifact_name,
                "description": artifact.get("description", "")[:60]
            })

        # Check for missing consumers
        if artifact_name not in artifact_consumers and artifact_id not in artifact_consumers:
            gaps["missing_consumers"].append({
                "artifact": artifact_name,
                "description": artifact.get("description", "")[:60]
            })

    # Check for missing orchestrators per domain
    for domain in CANONICAL_DOMAINS:
        domain_agents = category_matrix.get(domain, {}).get("agents", [])
        has_orchestrator = any(
            comp.get("role") == "orchestrate"
            for comp in components
            if comp.get("type") == "agent" and comp.get("name") in domain_agents
        )
        if not has_orchestrator and len(domain_agents) > 0:
            gaps["missing_orchestrators"].append({
                "domain": domain,
                "reason": "No orchestrator agent found"
            })

    # Check naming conventions
    for comp in components:
        name = comp.get("name", "")
        comp_type = comp.get("type", "")

        violations = []
        if comp_type == "skill" and "." not in name:
            violations.append(f"Skill '{name}' should use domain.action format")
        elif comp_type == "agent" and "." not in name:
            violations.append(f"Agent '{name}' should use domain.role format")
        elif comp_type == "hook" and not (name.startswith("on_") or name.startswith("pre_") or name.startswith("post_")):
            violations.append(f"Hook '{name}' should follow on_/pre_/post_ naming")
        elif comp_type == "command" and not name.startswith("/"):
            violations.append(f"Command '{name}' should start with /")

        if violations:
            gaps["naming_violations"].extend(violations)

    print(f"  ✓ Found {len(gaps['missing_producers'])} artifacts without producers (sampled)")
    print(f"  ✓ Found {len(gaps['missing_consumers'])} artifacts without consumers (sampled)")
    print(f"  ✓ Found {len(gaps['missing_orchestrators'])} missing orchestrators")
    print(f"  ✓ Found {len(gaps['naming_violations'])} naming violations")

    return gaps


def generate_catalog_markdown(components: List[Dict], output_file: Path):
    """Generate catalog.md"""
    print("📝 Generating catalog.md...")

    # Group by domain and role
    grouped = defaultdict(lambda: defaultdict(list))
    for comp in components:
        domain = comp.get("domain", "operations")
        role = comp.get("role", "analyze")
        grouped[domain][role].append(comp)

    md_lines = ["# Betty Component Catalog", "", "Generated catalog of all components grouped by domain and role.", ""]

    for domain in sorted(grouped.keys()):
        md_lines.append(f"## {domain.upper()}")
        md_lines.append("")

        for role in sorted(grouped[domain].keys()):
            md_lines.append(f"### {role.title()}")
            md_lines.append("")
            md_lines.append("| Type | Name | Description |")
            md_lines.append("|------|------|-------------|")

            for comp in sorted(grouped[domain][role], key=lambda x: x.get("name", "")):
                comp_type = comp.get("type", "").title()
                name = comp.get("name", "")
                desc = comp.get("description", "").replace("|", "\\|")[:80]
                md_lines.append(f"| {comp_type} | `{name}` | {desc} |")

            md_lines.append("")

    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"  ✓ Written to {output_file}")


def generate_relationships_markdown(relationships: Dict, output_file: Path):
    """Generate relationships.md with diagrams"""
    print("📝 Generating relationships.md...")

    md_lines = ["# Component Relationships", "", "Inter-component dependencies and flows.", ""]

    # Skills to Agents
    md_lines.append("## Skills → Agents")
    md_lines.append("")
    md_lines.append("```mermaid")
    md_lines.append("graph LR")
    for rel in relationships.get("skills_to_agents", [])[:20]:  # Limit to avoid huge diagrams
        skill = rel["skill"].replace(".", "_")
        agent = rel["agent"].replace(".", "_")
        md_lines.append(f"    {skill}[{rel['skill']}] --> {agent}[{rel['agent']}]")
    md_lines.append("```")
    md_lines.append("")

    # Hooks to Commands
    md_lines.append("## Hooks → Commands")
    md_lines.append("")
    md_lines.append("| Hook | Command |")
    md_lines.append("|------|---------|")
    for rel in relationships.get("hooks_to_commands", []):
        md_lines.append(f"| `{rel['hook']}` | `{rel['command']}` |")
    md_lines.append("")

    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"  ✓ Written to {output_file}")


def generate_gaps_markdown(gaps: Dict, output_file: Path):
    """Generate gaps.md summary"""
    print("📝 Generating gaps.md...")

    md_lines = ["# Gap Analysis Report", "", "Identified gaps and issues in the repository.", ""]

    # Missing Producers
    md_lines.append("## Missing Artifact Producers")
    md_lines.append("")
    md_lines.append("Artifacts that have no skills producing them (sampled from first 20 artifact types):")
    md_lines.append("")
    if gaps.get("missing_producers"):
        md_lines.append("| Artifact | Description |")
        md_lines.append("|----------|-------------|")
        for gap in gaps["missing_producers"][:10]:  # Limit to 10 for readability
            md_lines.append(f"| `{gap['artifact']}` | {gap['description']} |")
        if len(gaps["missing_producers"]) > 10:
            md_lines.append(f"\n*...and {len(gaps['missing_producers']) - 10} more*")
    else:
        md_lines.append("✓ All sampled artifacts have producers")
    md_lines.append("")

    # Missing Consumers
    md_lines.append("## Missing Artifact Consumers")
    md_lines.append("")
    md_lines.append("Artifacts that have no skills consuming them (sampled from first 20 artifact types):")
    md_lines.append("")
    if gaps.get("missing_consumers"):
        md_lines.append("| Artifact | Description |")
        md_lines.append("|----------|-------------|")
        for gap in gaps["missing_consumers"][:10]:  # Limit to 10 for readability
            md_lines.append(f"| `{gap['artifact']}` | {gap['description']} |")
        if len(gaps["missing_consumers"]) > 10:
            md_lines.append(f"\n*...and {len(gaps['missing_consumers']) - 10} more*")
    else:
        md_lines.append("✓ All sampled artifacts have consumers")
    md_lines.append("")

    # Missing Orchestrators
    md_lines.append("## Missing Orchestrators")
    md_lines.append("")
    md_lines.append("Domains that lack orchestrator agents:")
    md_lines.append("")
    if gaps.get("missing_orchestrators"):
        for gap in gaps["missing_orchestrators"]:
            md_lines.append(f"- **{gap['domain']}**: {gap['reason']}")
    else:
        md_lines.append("✓ All domains have orchestrators")
    md_lines.append("")

    # Naming Violations
    md_lines.append("## Naming Violations")
    md_lines.append("")
    md_lines.append("Components that don't follow naming conventions:")
    md_lines.append("")
    if gaps.get("naming_violations"):
        for violation in gaps["naming_violations"]:
            md_lines.append(f"- {violation}")
    else:
        md_lines.append("✓ No naming violations found")
    md_lines.append("")

    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"  ✓ Written to {output_file}")


def generate_implementation_blueprint(gaps: Dict, output_file: Path):
    """Generate implementation_blueprint.md"""
    print("📝 Generating implementation_blueprint.md...")

    md_lines = ["# Implementation Blueprint", "", "Prioritized roadmap of missing components.", ""]

    md_lines.append("## High Priority")
    md_lines.append("")
    for gap in gaps.get("missing_orchestrators", []):
        md_lines.append(f"- [ ] Create orchestrator agent for **{gap['domain']}** domain")
    md_lines.append("")

    md_lines.append("## Medium Priority")
    md_lines.append("")
    md_lines.append("- [ ] Fix naming convention violations")
    md_lines.append("")

    md_lines.append("## Low Priority")
    md_lines.append("")
    md_lines.append("- [ ] Add missing producers/consumers")
    md_lines.append("")

    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"  ✓ Written to {output_file}")


def generate_taxonomy_markdown(category_matrix: Dict, output_file: Path):
    """Generate taxonomy.md specification"""
    print("📝 Generating taxonomy.md...")

    md_lines = [
        "# Betty Taxonomy Specification",
        "",
        "## Canonical Domains",
        "",
        "The following ten domains organize all Betty components:",
        ""
    ]

    for domain in CANONICAL_DOMAINS:
        skills_count = len(category_matrix.get(domain, {}).get("skills", []))
        agents_count = len(category_matrix.get(domain, {}).get("agents", []))
        md_lines.append(f"- **{domain}**: {skills_count} skills, {agents_count} agents")

    md_lines.extend([
        "",
        "## Functional Roles",
        "",
        "Components are assigned one of seven functional roles:",
        ""
    ])

    for role in FUNCTIONAL_ROLES:
        md_lines.append(f"- **{role}**: Components that {role} artifacts or processes")

    md_lines.extend([
        "",
        "## Naming Standards",
        "",
        "### Skills",
        "- Format: `domain.action`",
        "- Example: `api.validate`, `docs.sync.readme`",
        "",
        "### Agents",
        "- Format: `domain.role`",
        "- Example: `api.analyzer`, `security.architect`",
        "",
        "### Hooks",
        "- Format: `on_<event>__<target>` or `pre_/post_<event>`",
        "- Example: `on_commit__policy-enforce`",
        "",
        "### Commands",
        "- Format: `/domain-action`",
        "- Example: `/api-validate`, `/create-pr`",
        ""
    ])

    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"  ✓ Written to {output_file}")


def main():
    """Main execution"""
    print("=" * 60)
    print("🚀 Betty Repository Catalog Generator")
    print("=" * 60)
    print()

    # Phase 1: Repository Analysis
    print("📋 PHASE 1: Repository Analysis")
    print("-" * 60)

    skills = scan_skills()
    agents = scan_agents()
    hooks = scan_hooks()
    commands = scan_commands()
    artifact_types = parse_artifact_types()

    # Normalize all components
    print("\n🔧 Normalizing components...")
    skills = [normalize_component(s) for s in skills]
    agents = [normalize_component(a) for a in agents]

    # Combine all components
    all_components = skills + agents + hooks + commands

    # Save individual catalogs
    print("\n💾 Saving individual catalogs...")
    with open(OUTPUT_DIR / "skills_catalog.json", 'w') as f:
        json.dump(skills, f, indent=2)
    with open(OUTPUT_DIR / "agents_catalog.json", 'w') as f:
        json.dump(agents, f, indent=2)
    with open(OUTPUT_DIR / "hooks_catalog.json", 'w') as f:
        json.dump(hooks, f, indent=2)
    with open(OUTPUT_DIR / "commands_catalog.json", 'w') as f:
        json.dump(commands, f, indent=2)
    with open(OUTPUT_DIR / "artifact_types_catalog.json", 'w') as f:
        json.dump(artifact_types, f, indent=2)

    # Save combined registry
    with open(OUTPUT_DIR / "component_registry.json", 'w') as f:
        json.dump(all_components, f, indent=2)

    print(f"  ✓ Saved to {OUTPUT_DIR}")

    # Build relationships
    relationships = build_relationships(skills, agents, hooks, commands, artifact_types)
    with open(OUTPUT_DIR / "relationships.json", 'w') as f:
        json.dump(relationships, f, indent=2)

    # Build category matrix
    category_matrix = build_category_matrix(all_components)
    with open(OUTPUT_DIR / "category_matrix.json", 'w') as f:
        json.dump(category_matrix, f, indent=2)

    # Phase 2: Gap Analysis
    print("\n📋 PHASE 2: Gap Analysis")
    print("-" * 60)

    gaps = detect_gaps(all_components, artifact_types, category_matrix, relationships)
    with open(OUTPUT_DIR / "gaps.json", 'w') as f:
        json.dump(gaps, f, indent=2)

    # Phase 3: Documentation Generation
    print("\n📋 PHASE 3: Documentation Generation")
    print("-" * 60)

    generate_catalog_markdown(all_components, OUTPUT_DIR / "catalog.md")
    generate_taxonomy_markdown(category_matrix, OUTPUT_DIR / "taxonomy.md")
    generate_relationships_markdown(relationships, OUTPUT_DIR / "relationships.md")
    generate_gaps_markdown(gaps, OUTPUT_DIR / "gaps.md")
    generate_implementation_blueprint(gaps, OUTPUT_DIR / "implementation_blueprint.md")

    # Summary
    print("\n" + "=" * 60)
    print("✅ CATALOG GENERATION COMPLETE")
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"  - {len(skills)} skills")
    print(f"  - {len(agents)} agents")
    print(f"  - {len(hooks)} hooks")
    print(f"  - {len(commands)} commands")
    print(f"  - {len(artifact_types)} artifact types")
    print(f"\n📁 Output directory: {OUTPUT_DIR}")
    print()


if __name__ == "__main__":
    main()
