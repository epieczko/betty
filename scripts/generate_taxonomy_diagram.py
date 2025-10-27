#!/usr/bin/env python3
"""
Generate comprehensive taxonomy diagrams from relationships.json
Creates enhanced Mermaid diagrams showing component relationships
"""

import json
from pathlib import Path
from typing import Dict, List

BASE_DIR = Path("/home/user/betty")
TAXONOMY_DIR = BASE_DIR / "registry" / "taxonomy"


def load_data():
    """Load taxonomy data"""
    with open(TAXONOMY_DIR / "relationships.json", 'r') as f:
        relationships = json.load(f)

    with open(TAXONOMY_DIR / "category_matrix.json", 'r') as f:
        category_matrix = json.load(f)

    with open(TAXONOMY_DIR / "component_registry.json", 'r') as f:
        components = json.load(f)

    return relationships, category_matrix, components


def generate_domain_overview_diagram(category_matrix: Dict) -> str:
    """Generate domain overview diagram"""
    lines = [
        "```mermaid",
        "graph TB",
        "    %% Domain Overview",
        ""
    ]

    # Create domain nodes
    for domain in sorted(category_matrix.keys()):
        data = category_matrix[domain]
        skill_count = len(data.get("skills", []))
        agent_count = len(data.get("agents", []))
        label = f"{domain.upper()}<br/>{skill_count} skills, {agent_count} agents"
        lines.append(f"    {domain}[{label}]")

    lines.append("")
    lines.append("    %% Style domains by category")

    # Color code by category
    domain_colors = {
        "api": "fill:#e1f5ff,stroke:#01579b",
        "data": "fill:#f3e5f5,stroke:#4a148c",
        "security": "fill:#ffebee,stroke:#b71c1c",
        "testing": "fill:#e8f5e9,stroke:#1b5e20",
        "docs": "fill:#fff3e0,stroke:#e65100",
        "architecture": "fill:#fce4ec,stroke:#880e4f",
        "governance": "fill:#f1f8e9,stroke:#33691e",
        "deployment": "fill:#e0f2f1,stroke:#004d40",
        "operations": "fill:#ede7f6,stroke:#311b92",
        "ai": "fill:#fff9c4,stroke:#f57f17"
    }

    for domain, color in domain_colors.items():
        if domain in category_matrix:
            lines.append(f"    style {domain} {color},color:#000")

    lines.append("```")
    return "\n".join(lines)


def generate_lifecycle_diagram() -> str:
    """Generate artifact lifecycle diagram"""
    lines = [
        "```mermaid",
        "graph LR",
        "    %% Artifact Lifecycle Flow",
        "    A[Create] --> B[Validate]",
        "    B --> C[Review]",
        "    C --> D{Approved?}",
        "    D -->|Yes| E[Publish]",
        "    D -->|No| F[Revise]",
        "    F --> B",
        "    E --> G[Registry]",
        "    ",
        "    style A fill:#e1f5ff,stroke:#01579b",
        "    style B fill:#fff3e0,stroke:#e65100",
        "    style C fill:#f3e5f5,stroke:#4a148c",
        "    style E fill:#e8f5e9,stroke:#1b5e20",
        "    style G fill:#fff9c4,stroke:#f57f17",
        "```"
    ]
    return "\n".join(lines)


def generate_skill_agent_network(relationships: Dict, limit: int = 30) -> str:
    """Generate skill-to-agent network diagram"""
    lines = [
        "```mermaid",
        "graph TD",
        "    %% Skill → Agent Relationships",
        ""
    ]

    # Get relationships and limit them
    skill_agent_rels = relationships.get("skills_to_agents", [])[:limit]

    # Group by agent
    agent_skills = {}
    for rel in skill_agent_rels:
        agent = rel["agent"]
        skill = rel["skill"]
        if agent not in agent_skills:
            agent_skills[agent] = []
        agent_skills[agent].append(skill)

    # Create subgraphs by domain
    domains_found = set()
    for agent in agent_skills.keys():
        domain = agent.split(".")[0] if "." in agent else "other"
        domains_found.add(domain)

    # Generate nodes and edges
    for agent, skills in agent_skills.items():
        agent_id = agent.replace(".", "_")
        for skill in skills:
            skill_id = skill.replace(".", "_")
            lines.append(f"    {skill_id}[{skill}] --> {agent_id}[{agent}]")

    lines.append("")
    lines.append("    %% Styling")
    lines.append("    classDef skillNode fill:#e1f5ff,stroke:#01579b")
    lines.append("    classDef agentNode fill:#fff3e0,stroke:#e65100")

    # Apply styles
    all_skills = set()
    for skills in agent_skills.values():
        all_skills.update(skills)

    for skill in all_skills:
        skill_id = skill.replace(".", "_")
        lines.append(f"    class {skill_id} skillNode")

    for agent in agent_skills.keys():
        agent_id = agent.replace(".", "_")
        lines.append(f"    class {agent_id} agentNode")

    lines.append("```")
    return "\n".join(lines)


def generate_artifact_flow_diagram(relationships: Dict) -> str:
    """Generate artifact producer/consumer flow"""
    lines = [
        "```mermaid",
        "graph LR",
        "    %% Artifact Production and Consumption Flow",
        ""
    ]

    producers = relationships.get("artifact_producers", {})
    consumers = relationships.get("artifact_consumers", {})

    # Find artifacts with both producers and consumers
    common_artifacts = set(producers.keys()) & set(consumers.keys())

    # Limit to prevent diagram overload
    common_artifacts = list(common_artifacts)[:10]

    for artifact in common_artifacts:
        artifact_id = artifact.replace("-", "_").replace(".", "_")

        # Get first producer and consumer as examples
        producer_skills = producers[artifact][:1]
        consumer_skills = consumers[artifact][:1]

        for producer in producer_skills:
            producer_id = producer.replace(".", "_")
            lines.append(f"    {producer_id}[{producer}] -->|produces| {artifact_id}[{artifact}]")

        for consumer in consumer_skills:
            consumer_id = consumer.replace(".", "_")
            lines.append(f"    {artifact_id} -->|consumed by| {consumer_id}[{consumer}]")

    lines.append("")
    lines.append("    %% Styling")
    lines.append("    classDef artifactNode fill:#f3e5f5,stroke:#4a148c")
    lines.append("    classDef skillNode fill:#e1f5ff,stroke:#01579b")

    for artifact in common_artifacts:
        artifact_id = artifact.replace("-", "_").replace(".", "_")
        lines.append(f"    class {artifact_id} artifactNode")

    lines.append("```")
    return "\n".join(lines)


def update_relationships_md():
    """Update relationships.md with enhanced diagrams"""
    print("📊 Generating Enhanced Taxonomy Diagrams")
    print("=" * 60)

    relationships, category_matrix, components = load_data()

    md_lines = [
        "# Component Relationships & Taxonomy",
        "",
        "Comprehensive visualization of Betty Framework component relationships.",
        "",
        "## Table of Contents",
        "",
        "1. [Domain Overview](#domain-overview)",
        "2. [Artifact Lifecycle](#artifact-lifecycle)",
        "3. [Skill → Agent Network](#skill--agent-network)",
        "4. [Artifact Flow](#artifact-flow)",
        "5. [Hooks → Commands](#hooks--commands)",
        "",
        "---",
        "",
        "## Domain Overview",
        "",
        "Distribution of skills and agents across all 10 canonical domains.",
        ""
    ]

    print("  → Generating domain overview diagram...")
    md_lines.append(generate_domain_overview_diagram(category_matrix))

    md_lines.extend([
        "",
        "---",
        "",
        "## Artifact Lifecycle",
        "",
        "Standard lifecycle flow for all artifacts: create → validate → review → publish.",
        ""
    ])

    print("  → Generating lifecycle diagram...")
    md_lines.append(generate_lifecycle_diagram())

    md_lines.extend([
        "",
        "---",
        "",
        "## Skill → Agent Network",
        "",
        "Shows which skills are used by which agents (limited to first 30 relationships).",
        ""
    ])

    print("  → Generating skill-agent network...")
    md_lines.append(generate_skill_agent_network(relationships))

    md_lines.extend([
        "",
        "---",
        "",
        "## Artifact Flow",
        "",
        "Producer/consumer relationships for artifacts (sample of 10 artifacts).",
        ""
    ])

    print("  → Generating artifact flow diagram...")
    md_lines.append(generate_artifact_flow_diagram(relationships))

    md_lines.extend([
        "",
        "---",
        "",
        "## Hooks → Commands",
        "",
        "Event-driven hook to command mappings.",
        "",
        "| Hook | Event | Command |",
        "|------|-------|---------|"
    ])

    # Add hooks to commands table
    hook_commands = relationships.get("hooks_to_commands", [])
    for rel in hook_commands:
        md_lines.append(f"| `{rel['hook']}` | after-tool-call | `{rel['command']}` |")

    md_lines.extend([
        "",
        "---",
        "",
        "## Metrics",
        "",
        f"- **Skills**: {len([c for c in components if c.get('type') == 'skill'])}",
        f"- **Agents**: {len([c for c in components if c.get('type') == 'agent'])}",
        f"- **Hooks**: {len([c for c in components if c.get('type') == 'hook'])}",
        f"- **Commands**: {len([c for c in components if c.get('type') == 'command'])}",
        f"- **Skill→Agent Relationships**: {len(relationships.get('skills_to_agents', []))}",
        f"- **Artifact Producers**: {len(relationships.get('artifact_producers', {}))}",
        f"- **Artifact Consumers**: {len(relationships.get('artifact_consumers', {}))}",
        "",
        "---",
        "",
        "*Generated by Betty Framework Taxonomy System*"
    ])

    # Save enhanced relationships.md
    output_file = TAXONOMY_DIR / "relationships.md"
    with open(output_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"\n✅ Enhanced relationships.md saved to {output_file}")

    # Also create a standalone diagram file
    diagram_file = TAXONOMY_DIR / "taxonomy-diagram.md"
    with open(diagram_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"✅ Standalone diagram saved to {diagram_file}")

    return output_file


if __name__ == "__main__":
    update_relationships_md()
    print("\n🎨 Taxonomy diagrams generated successfully!")
