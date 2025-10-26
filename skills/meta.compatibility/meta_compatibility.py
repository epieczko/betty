#!/usr/bin/env python3
"""
meta.compatibility skill - Automatic artifact dependency graph validation

Validates artifact dependency graphs, detects cycles, orphan nodes, and unresolved
dependencies. Provides actionable diagnostics for artifact compatibility issues.
"""

import sys
import os
import argparse
import json
from pathlib import Path
from typing import Dict, Any, List, Set, Tuple, Optional
import yaml

try:
    import networkx as nx
except ImportError:
    print("Error: networkx is required. Install with: pip install networkx>=3.0")
    sys.exit(1)

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


def load_skill_metadata(skills_dir: Path) -> List[Dict[str, Any]]:
    """Load artifact metadata from all skills"""
    skills = []

    if not skills_dir.exists():
        return skills

    for skill_path in skills_dir.iterdir():
        if not skill_path.is_dir() or skill_path.name.startswith('.'):
            continue

        # Try to load skill.yaml
        skill_yaml = skill_path / "skill.yaml"
        if not skill_yaml.exists():
            continue

        try:
            with open(skill_yaml, 'r') as f:
                skill_data = yaml.safe_load(f)

            if not skill_data:
                continue

            # Extract artifact metadata
            if 'artifact_metadata' in skill_data:
                skills.append({
                    'name': skill_data.get('name', skill_path.name),
                    'path': str(skill_path),
                    'produces': skill_data['artifact_metadata'].get('produces', []),
                    'consumes': skill_data['artifact_metadata'].get('consumes', [])
                })
        except Exception as e:
            print(f"Warning: Failed to load {skill_yaml}: {e}", file=sys.stderr)
            continue

    return skills


def build_artifact_graph(artifacts: List[Dict[str, Any]]) -> nx.DiGraph:
    """
    Build artifact dependency graph from skill metadata.

    Nodes represent artifact types.
    Edges represent dependencies: if skill A produces artifact X and skill B consumes X,
    there's an edge from X (as produced by A) to X (as consumed by B).

    We also track which skills produce/consume each artifact type.
    """
    g = nx.DiGraph()

    # Track artifact types and their producers/consumers
    artifact_types: Set[str] = set()
    producers: Dict[str, List[str]] = {}  # artifact_type -> [skill_names]
    consumers: Dict[str, List[str]] = {}  # artifact_type -> [skill_names]

    # First pass: collect all artifact types and track producers/consumers
    for skill in artifacts:
        skill_name = skill.get('name', 'unknown')

        # Process produces
        for artifact in skill.get('produces', []):
            if isinstance(artifact, dict):
                artifact_type = artifact.get('type')
            else:
                artifact_type = artifact

            if artifact_type:
                artifact_types.add(artifact_type)
                if artifact_type not in producers:
                    producers[artifact_type] = []
                producers[artifact_type].append(skill_name)

        # Process consumes
        for artifact in skill.get('consumes', []):
            if isinstance(artifact, dict):
                artifact_type = artifact.get('type')
            else:
                artifact_type = artifact

            if artifact_type and artifact_type != '*':  # Ignore wildcard consumers
                artifact_types.add(artifact_type)
                if artifact_type not in consumers:
                    consumers[artifact_type] = []
                consumers[artifact_type].append(skill_name)

    # Add nodes for each artifact type
    for artifact_type in artifact_types:
        g.add_node(
            artifact_type,
            producers=producers.get(artifact_type, []),
            consumers=consumers.get(artifact_type, [])
        )

    # Add edges representing artifact flows
    # If artifact A is consumed by a skill that produces artifact B,
    # create edge A -> B (artifact A flows into creating artifact B)
    for skill in artifacts:
        consumed_artifacts = []
        produced_artifacts = []

        # Get consumed artifact types
        for artifact in skill.get('consumes', []):
            if isinstance(artifact, dict):
                artifact_type = artifact.get('type')
            else:
                artifact_type = artifact

            if artifact_type and artifact_type != '*':
                consumed_artifacts.append(artifact_type)

        # Get produced artifact types
        for artifact in skill.get('produces', []):
            if isinstance(artifact, dict):
                artifact_type = artifact.get('type')
            else:
                artifact_type = artifact

            if artifact_type:
                produced_artifacts.append(artifact_type)

        # Create edges from consumed to produced artifacts
        for consumed in consumed_artifacts:
            for produced in produced_artifacts:
                if consumed in g and produced in g:
                    g.add_edge(consumed, produced, skill=skill.get('name'))

    return g


def detect_cycles(g: nx.DiGraph) -> List[List[str]]:
    """Detect cycles in the artifact dependency graph"""
    try:
        cycles = list(nx.simple_cycles(g))
        return cycles
    except Exception:
        return []


def identify_isolated_nodes(g: nx.DiGraph) -> List[str]:
    """Identify nodes with no incoming or outgoing edges"""
    isolated = []
    for node in g.nodes():
        if g.in_degree(node) == 0 and g.out_degree(node) == 0:
            isolated.append(node)
    return isolated


def identify_unresolved_dependencies(g: nx.DiGraph, skills: List[Dict[str, Any]]) -> List[str]:
    """Identify artifact types that are consumed but never produced"""
    unresolved = []

    for node in g.nodes():
        node_data = g.nodes[node]
        producers = node_data.get('producers', [])
        consumers = node_data.get('consumers', [])

        # If consumed but not produced, it's unresolved
        if consumers and not producers:
            unresolved.append(node)

    return unresolved


def identify_orphan_producers(g: nx.DiGraph) -> List[str]:
    """Identify artifact types that are produced but never consumed"""
    orphans = []

    for node in g.nodes():
        node_data = g.nodes[node]
        producers = node_data.get('producers', [])
        consumers = node_data.get('consumers', [])

        # If produced but not consumed, it's an orphan
        if producers and not consumers:
            orphans.append(node)

    return orphans


def validate_artifact_graph(skills_dir: str = "skills") -> Dict[str, Any]:
    """
    Validate artifact dependency graph and generate diagnostic report

    Args:
        skills_dir: Path to skills directory

    Returns:
        Validation report with graph health metrics
    """
    skills_path = Path(skills_dir)

    # Load skill metadata
    skills = load_skill_metadata(skills_path)

    if not skills:
        return {
            'success': False,
            'error': 'No skills with artifact metadata found',
            'total_artifacts': 0,
            'total_skills': 0,
            'status': 'error'
        }

    # Build graph
    g = build_artifact_graph(skills)

    # Detect issues
    cycles = detect_cycles(g)
    isolated = identify_isolated_nodes(g)
    unresolved = identify_unresolved_dependencies(g, skills)
    orphans = identify_orphan_producers(g)

    # Calculate connected artifacts (not isolated)
    connected = len(g.nodes()) - len(isolated)

    # Determine status
    status = 'healthy'
    if cycles or unresolved:
        status = 'error'
    elif isolated or orphans:
        status = 'warning'

    # Build report
    report = {
        'success': True,
        'total_artifacts': len(g.nodes()),
        'total_skills': len(skills),
        'connected': connected,
        'isolated': isolated,
        'cyclic': [list(cycle) for cycle in cycles],
        'unresolved': unresolved,
        'orphans': orphans,
        'status': status,
        'graph_stats': {
            'nodes': g.number_of_nodes(),
            'edges': g.number_of_edges(),
            'density': nx.density(g) if g.number_of_nodes() > 0 else 0
        }
    }

    return report


def print_human_readable_report(report: Dict[str, Any]) -> None:
    """Print human-readable graph validation summary"""
    if not report.get('success'):
        print(f"\n❌ Graph Validation Failed")
        print(f"Error: {report.get('error', 'Unknown error')}")
        return

    total = report.get('total_artifacts', 0)
    connected = report.get('connected', 0)
    isolated = report.get('isolated', [])
    cycles = report.get('cyclic', [])
    unresolved = report.get('unresolved', [])
    orphans = report.get('orphans', [])
    status = report.get('status', 'unknown')

    print(f"\n{'='*70}")
    print(f"Artifact Dependency Graph Validation")
    print(f"{'='*70}")
    print(f"Total Skills:     {report.get('total_skills', 0)}")
    print(f"Total Artifacts:  {total}")
    print(f"Graph Density:    {report['graph_stats']['density']:.2%}")
    print(f"")

    # Connected artifacts
    if connected > 0:
        print(f"✅ {connected} artifacts connected")

    # Isolated artifacts
    if isolated:
        print(f"⚠️  {len(isolated)} isolated")
        for artifact in isolated[:5]:  # Show first 5
            print(f"   - {artifact}")
        if len(isolated) > 5:
            print(f"   ... and {len(isolated) - 5} more")

    # Cycles
    if cycles:
        print(f"❌ {len(cycles)} cycle(s) detected")
        for i, cycle in enumerate(cycles[:3], 1):  # Show first 3
            cycle_path = ' → '.join(cycle + [cycle[0]])
            print(f"   {i}. {cycle_path}")
        if len(cycles) > 3:
            print(f"   ... and {len(cycles) - 3} more")

    # Unresolved dependencies
    if unresolved:
        print(f"❌ {len(unresolved)} unresolved dependencies")
        for artifact in unresolved[:5]:
            print(f"   - {artifact} (consumed but never produced)")
        if len(unresolved) > 5:
            print(f"   ... and {len(unresolved) - 5} more")

    # Orphan producers
    if orphans:
        print(f"⚠️  {len(orphans)} orphan producers")
        for artifact in orphans[:5]:
            print(f"   - {artifact} (produced but never consumed)")
        if len(orphans) > 5:
            print(f"   ... and {len(orphans) - 5} more")

    print(f"")

    # Overall status
    if status == 'healthy':
        print(f"✅ Graph Status: HEALTHY")
    elif status == 'warning':
        print(f"⚠️  Graph Status: WARNING (non-critical issues)")
    else:
        print(f"❌ Graph Status: ERROR (critical issues)")

    print(f"{'='*70}\n")


def main():
    """Main entry point for meta.compatibility skill"""
    parser = argparse.ArgumentParser(
        description='Validate artifact dependency graph and detect compatibility issues'
    )
    parser.add_argument(
        '--check',
        type=str,
        choices=['artifacts', 'skills', 'all'],
        default='artifacts',
        help='What to check (default: artifacts)'
    )
    parser.add_argument(
        '--skills-dir',
        type=str,
        default='skills',
        help='Path to skills directory (default: skills)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save JSON report to file'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output JSON only (no human-readable output)'
    )

    args = parser.parse_args()

    # Validate artifact graph
    report = validate_artifact_graph(skills_dir=args.skills_dir)

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        if not args.json:
            print(f"Report saved to: {output_path}")

    # Print output
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_human_readable_report(report)

    # Exit with appropriate code
    status = report.get('status', 'error')
    if status == 'healthy':
        return 0
    elif status == 'warning':
        return 0  # Warnings don't fail the check
    else:
        return 1


if __name__ == '__main__':
    sys.exit(main())
