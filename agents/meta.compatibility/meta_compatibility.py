#!/usr/bin/env python3
"""
meta.compatibility - Agent Compatibility Analyzer

Analyzes agent and skill compatibility to discover multi-agent workflows.
Helps Claude orchestrate by showing which agents can work together.
"""

import json
import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from collections import defaultdict

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)

from betty.provenance import compute_hash, get_provenance_logger
from betty.config import REGISTRY_FILE, REGISTRY_DIR


class CompatibilityAnalyzer:
    """Analyzes agent compatibility based on artifact flows"""

    def __init__(self, base_dir: str = "."):
        """Initialize with base directory"""
        self.base_dir = Path(base_dir)
        self.agents_dir = self.base_dir / "agents"
        self.agents = {}  # name -> agent definition
        self.compatibility_map = {}  # artifact_type -> {producers: [], consumers: []}

    def scan_agents(self) -> Dict[str, Any]:
        """
        Scan agents directory and load all agent definitions

        Returns:
            Dictionary of agent_name -> agent_definition
        """
        self.agents = {}

        if not self.agents_dir.exists():
            return self.agents

        for agent_dir in self.agents_dir.iterdir():
            if agent_dir.is_dir():
                agent_yaml = agent_dir / "agent.yaml"
                if agent_yaml.exists():
                    with open(agent_yaml) as f:
                        agent_def = yaml.safe_load(f)
                        if agent_def and "name" in agent_def:
                            self.agents[agent_def["name"]] = agent_def

        return self.agents

    def extract_artifacts(self, agent_def: Dict[str, Any]) -> Tuple[Set[str], Set[str]]:
        """
        Extract artifact types from agent definition

        Args:
            agent_def: Agent definition dictionary

        Returns:
            Tuple of (produces_set, consumes_set)
        """
        produces = set()
        consumes = set()

        artifact_metadata = agent_def.get("artifact_metadata", {})

        # Extract produced artifacts
        for artifact in artifact_metadata.get("produces", []):
            if isinstance(artifact, dict) and "type" in artifact:
                produces.add(artifact["type"])
            elif isinstance(artifact, str):
                produces.add(artifact)

        # Extract consumed artifacts
        for artifact in artifact_metadata.get("consumes", []):
            if isinstance(artifact, dict) and "type" in artifact:
                consumes.add(artifact["type"])
            elif isinstance(artifact, str):
                consumes.add(artifact)

        return produces, consumes

    def build_compatibility_map(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Build map of artifact types to producers/consumers

        Returns:
            Dictionary mapping artifact_type -> {producers: [], consumers: []}
        """
        self.compatibility_map = defaultdict(lambda: {"producers": [], "consumers": []})

        for agent_name, agent_def in self.agents.items():
            produces, consumes = self.extract_artifacts(agent_def)

            for artifact_type in produces:
                self.compatibility_map[artifact_type]["producers"].append(agent_name)

            for artifact_type in consumes:
                self.compatibility_map[artifact_type]["consumers"].append(agent_name)

        return dict(self.compatibility_map)

    def find_compatible(self, agent_name: str) -> Dict[str, Any]:
        """
        Find agents compatible with the specified agent

        Args:
            agent_name: Name of agent to analyze

        Returns:
            Dictionary with compatible agents and rationale
        """
        if agent_name not in self.agents:
            return {
                "error": f"Agent '{agent_name}' not found",
                "available_agents": list(self.agents.keys())
            }

        agent_def = self.agents[agent_name]
        produces, consumes = self.extract_artifacts(agent_def)

        result = {
            "agent": agent_name,
            "produces": list(produces),
            "consumes": list(consumes),
            "can_feed_to": [],      # Agents that can consume this agent's outputs
            "can_receive_from": [], # Agents that can provide this agent's inputs
            "gaps": []              # Missing artifacts
        }

        # Find agents that can consume this agent's outputs
        for artifact_type in produces:
            consumers = self.compatibility_map.get(artifact_type, {}).get("consumers", [])
            for consumer in consumers:
                if consumer != agent_name:
                    result["can_feed_to"].append({
                        "agent": consumer,
                        "artifact": artifact_type,
                        "rationale": f"{agent_name} produces '{artifact_type}' which {consumer} consumes"
                    })

        # Find agents that can provide this agent's inputs
        for artifact_type in consumes:
            producers = self.compatibility_map.get(artifact_type, {}).get("producers", [])
            if not producers:
                result["gaps"].append({
                    "artifact": artifact_type,
                    "issue": f"No agents produce '{artifact_type}' (required by {agent_name})",
                    "severity": "high"
                })
            else:
                for producer in producers:
                    if producer != agent_name:
                        result["can_receive_from"].append({
                            "agent": producer,
                            "artifact": artifact_type,
                            "rationale": f"{producer} produces '{artifact_type}' which {agent_name} needs"
                        })

        return result

    def suggest_pipeline(self, goal: str, required_artifacts: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Suggest multi-agent pipeline for a goal

        Args:
            goal: Natural language description of what to accomplish
            required_artifacts: Optional list of artifact types needed

        Returns:
            Suggested pipeline with steps and rationale
        """
        # Simple keyword matching for now (can be enhanced with ML later)
        goal_lower = goal.lower()

        keywords_to_agents = {
            "api": ["api.architect", "meta.agent"],
            "design api": ["api.architect"],
            "validate": ["api.architect"],
            "create agent": ["meta.agent"],
            "agent": ["meta.agent"],
            "artifact": ["meta.artifact"],
            "optimize": [],  # No optimizer yet, but we have the artifact type
        }

        # Find relevant agents
        relevant_agents = set()
        for keyword, agents in keywords_to_agents.items():
            if keyword in goal_lower:
                relevant_agents.update([a for a in agents if a in self.agents])

        if not relevant_agents and required_artifacts:
            # Find agents that produce the required artifacts
            for artifact_type in required_artifacts:
                producers = self.compatibility_map.get(artifact_type, {}).get("producers", [])
                relevant_agents.update(producers)

        if not relevant_agents:
            return {
                "error": "Could not determine relevant agents for goal",
                "suggestion": "Try being more specific or mention required artifact types",
                "goal": goal
            }

        # Build pipeline by analyzing artifact flows
        pipelines = []

        for start_agent in relevant_agents:
            pipeline = self._build_pipeline_from_agent(start_agent, goal)
            if pipeline:
                pipelines.append(pipeline)

        # Rank pipelines by completeness and length
        pipelines.sort(key=lambda p: (
            -len([s for s in p.get("steps", [])]),  # Prefer shorter pipelines
            -p.get("confidence_score", 0)            # Higher confidence
        ))

        if not pipelines:
            return {
                "error": "Could not build complete pipeline",
                "relevant_agents": list(relevant_agents),
                "goal": goal
            }

        return {
            "goal": goal,
            "pipelines": pipelines[:3],  # Top 3 suggestions
            "confidence": "medium" if len(pipelines) > 1 else "low"
        }

    def _build_pipeline_from_agent(self, start_agent: str, goal: str) -> Optional[Dict[str, Any]]:
        """
        Build a pipeline starting from a specific agent

        Args:
            start_agent: Agent to start pipeline from
            goal: Goal description

        Returns:
            Pipeline dictionary or None
        """
        if start_agent not in self.agents:
            return None

        agent_def = self.agents[start_agent]
        produces, consumes = self.extract_artifacts(agent_def)

        pipeline = {
            "name": f"{start_agent.title()} Pipeline",
            "description": f"Pipeline starting with {start_agent}",
            "steps": [
                {
                    "step": 1,
                    "agent": start_agent,
                    "description": agent_def.get("description", "").split("\n")[0],
                    "produces": list(produces),
                    "consumes": list(consumes)
                }
            ],
            "artifact_flow": [],
            "confidence_score": 0.5
        }

        # Try to add compatible next steps
        compatibility = self.find_compatible(start_agent)

        for compatible in compatibility.get("can_feed_to", [])[:2]:  # Max 2 next steps
            next_agent = compatible["agent"]
            if next_agent in self.agents:
                next_def = self.agents[next_agent]
                next_produces, next_consumes = self.extract_artifacts(next_def)

                pipeline["steps"].append({
                    "step": len(pipeline["steps"]) + 1,
                    "agent": next_agent,
                    "description": next_def.get("description", "").split("\n")[0],
                    "produces": list(next_produces),
                    "consumes": list(next_consumes)
                })

                pipeline["artifact_flow"].append({
                    "from": start_agent,
                    "to": next_agent,
                    "artifact": compatible["artifact"]
                })

                pipeline["confidence_score"] += 0.2

        # Calculate if pipeline has gaps
        all_produces = set()
        all_consumes = set()
        for step in pipeline["steps"]:
            all_produces.update(step.get("produces", []))
            all_consumes.update(step.get("consumes", []))

        gaps = all_consumes - all_produces
        if not gaps:
            pipeline["confidence_score"] += 0.3
            pipeline["complete"] = True
        else:
            pipeline["complete"] = False
            pipeline["gaps"] = list(gaps)

        return pipeline

    def generate_compatibility_graph(self) -> Dict[str, Any]:
        """
        Generate complete compatibility graph for all agents

        Returns:
            Compatibility graph structure
        """
        graph = {
            "agents": [],
            "relationships": [],
            "artifact_types": [],
            "gaps": [],
            "metadata": {
                "total_agents": len(self.agents),
                "total_artifact_types": len(self.compatibility_map)
            }
        }

        # Add agents
        for agent_name, agent_def in self.agents.items():
            produces, consumes = self.extract_artifacts(agent_def)

            graph["agents"].append({
                "name": agent_name,
                "description": agent_def.get("description", "").split("\n")[0],
                "produces": list(produces),
                "consumes": list(consumes)
            })

        # Add relationships
        for agent_name in self.agents:
            compatibility = self.find_compatible(agent_name)

            for compatible in compatibility.get("can_feed_to", []):
                graph["relationships"].append({
                    "from": agent_name,
                    "to": compatible["agent"],
                    "artifact": compatible["artifact"],
                    "type": "produces_for"
                })

        # Add artifact types
        for artifact_type, info in self.compatibility_map.items():
            graph["artifact_types"].append({
                "type": artifact_type,
                "producers": info["producers"],
                "consumers": info["consumers"],
                "producer_count": len(info["producers"]),
                "consumer_count": len(info["consumers"])
            })

        # Find global gaps
        for artifact_type, info in self.compatibility_map.items():
            if not info["producers"] and info["consumers"]:
                graph["gaps"].append({
                    "artifact": artifact_type,
                    "issue": f"Consumed by {len(info['consumers'])} agents but no producers",
                    "consumers": info["consumers"],
                    "severity": "high"
                })

        return graph

    def analyze_agent(self, agent_name: str) -> Dict[str, Any]:
        """
        Complete compatibility analysis for one agent

        Args:
            agent_name: Name of agent to analyze

        Returns:
            Comprehensive analysis
        """
        compatibility = self.find_compatible(agent_name)

        if "error" in compatibility:
            return compatibility

        # Add suggested workflows
        workflows = []

        # Workflow 1: As a starting point
        if compatibility["can_feed_to"]:
            workflow = {
                "name": f"Start with {agent_name}",
                "description": f"Use {agent_name} as the first step",
                "agents": [agent_name] + [c["agent"] for c in compatibility["can_feed_to"][:2]]
            }
            workflows.append(workflow)

        # Workflow 2: As a middle step
        if compatibility["can_receive_from"] and compatibility["can_feed_to"]:
            workflow = {
                "name": f"{agent_name} in pipeline",
                "description": f"Use {agent_name} as a processing step",
                "agents": [
                    compatibility["can_receive_from"][0]["agent"],
                    agent_name,
                    compatibility["can_feed_to"][0]["agent"]
                ]
            }
            workflows.append(workflow)

        compatibility["suggested_workflows"] = workflows

        return compatibility

    def verify_registry_integrity(self) -> Dict[str, Any]:
        """
        Verify integrity of registry files using provenance hashes.

        Returns:
            Dictionary with verification results
        """
        provenance = get_provenance_logger()

        results = {
            "verified": [],
            "failed": [],
            "missing": [],
            "summary": {
                "total_checked": 0,
                "verified_count": 0,
                "failed_count": 0,
                "missing_count": 0
            }
        }

        # List of registry files to verify
        registry_files = [
            ("skills.json", REGISTRY_FILE),
            ("agents.json", str(Path(REGISTRY_DIR) / "agents.json")),
            ("workflow_history.json", str(Path(REGISTRY_DIR) / "workflow_history.json")),
        ]

        for artifact_id, file_path in registry_files:
            results["summary"]["total_checked"] += 1

            # Check if file exists
            if not os.path.exists(file_path):
                results["missing"].append({
                    "artifact": artifact_id,
                    "path": file_path,
                    "reason": "File does not exist"
                })
                results["summary"]["missing_count"] += 1
                continue

            try:
                # Load the registry file
                with open(file_path, 'r') as f:
                    content = json.load(f)

                # Get stored hash from file (if present)
                stored_hash = content.get("content_hash")

                # Remove content_hash field to compute original hash
                content_without_hash = {k: v for k, v in content.items() if k != "content_hash"}

                # Compute current hash
                current_hash = compute_hash(content_without_hash)

                # Get latest hash from provenance log
                latest_provenance_hash = provenance.get_latest_hash(artifact_id)

                # Verify
                if stored_hash and stored_hash == current_hash:
                    # Hash matches what's in the file
                    verification_status = "verified"

                    # Also check against provenance log
                    if latest_provenance_hash:
                        provenance_match = (stored_hash == latest_provenance_hash)
                    else:
                        provenance_match = None

                    results["verified"].append({
                        "artifact": artifact_id,
                        "path": file_path,
                        "hash": current_hash[:16] + "...",
                        "stored_hash_valid": True,
                        "provenance_logged": latest_provenance_hash is not None,
                        "provenance_match": provenance_match
                    })
                    results["summary"]["verified_count"] += 1

                elif stored_hash and stored_hash != current_hash:
                    # Hash mismatch - file may have been modified
                    results["failed"].append({
                        "artifact": artifact_id,
                        "path": file_path,
                        "reason": "Content hash mismatch",
                        "stored_hash": stored_hash[:16] + "...",
                        "computed_hash": current_hash[:16] + "...",
                        "severity": "high"
                    })
                    results["summary"]["failed_count"] += 1

                else:
                    # No hash stored in file
                    results["missing"].append({
                        "artifact": artifact_id,
                        "path": file_path,
                        "reason": "No content_hash field in file",
                        "computed_hash": current_hash[:16] + "...",
                        "provenance_available": latest_provenance_hash is not None
                    })
                    results["summary"]["missing_count"] += 1

            except Exception as e:
                results["failed"].append({
                    "artifact": artifact_id,
                    "path": file_path,
                    "reason": f"Verification error: {str(e)}",
                    "severity": "high"
                })
                results["summary"]["failed_count"] += 1

        return results


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.compatibility - Agent Compatibility Analyzer"
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Find compatible command
    find_parser = subparsers.add_parser('find-compatible', help='Find compatible agents')
    find_parser.add_argument("agent", help="Agent name to analyze")

    # Suggest pipeline command
    suggest_parser = subparsers.add_parser('suggest-pipeline', help='Suggest multi-agent pipeline')
    suggest_parser.add_argument("goal", help="Goal description")
    suggest_parser.add_argument("--artifacts", nargs="+", help="Required artifact types")

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze agent compatibility')
    analyze_parser.add_argument("agent", help="Agent name to analyze")

    # List all command
    list_parser = subparsers.add_parser('list-all', help='List all compatibility')

    # Verify integrity command
    verify_parser = subparsers.add_parser('verify-integrity', help='Verify registry integrity using provenance hashes')

    # Output format
    parser.add_argument(
        "--format",
        choices=["json", "yaml", "text"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    analyzer = CompatibilityAnalyzer()
    analyzer.scan_agents()
    analyzer.build_compatibility_map()

    result = None

    if args.command == 'find-compatible':
        print(f"🔍 Finding agents compatible with '{args.agent}'...\n")
        result = analyzer.find_compatible(args.agent)

        if args.format == "text" and "error" not in result:
            print(f"Agent: {result['agent']}")
            print(f"Produces: {', '.join(result['produces']) if result['produces'] else 'none'}")
            print(f"Consumes: {', '.join(result['consumes']) if result['consumes'] else 'none'}")

            if result['can_feed_to']:
                print(f"\n✅ Can feed outputs to ({len(result['can_feed_to'])} agents):")
                for comp in result['can_feed_to']:
                    print(f"   • {comp['agent']} (via {comp['artifact']})")

            if result['can_receive_from']:
                print(f"\n⬅️  Can receive inputs from ({len(result['can_receive_from'])} agents):")
                for comp in result['can_receive_from']:
                    print(f"   • {comp['agent']} (via {comp['artifact']})")

            if result['gaps']:
                print(f"\n⚠️  Gaps ({len(result['gaps'])}):")
                for gap in result['gaps']:
                    print(f"   • {gap['artifact']}: {gap['issue']}")

    elif args.command == 'suggest-pipeline':
        print(f"💡 Suggesting pipeline for: {args.goal}\n")
        result = analyzer.suggest_pipeline(args.goal, args.artifacts)

        if args.format == "text" and "pipelines" in result:
            for i, pipeline in enumerate(result["pipelines"], 1):
                print(f"\n📋 Pipeline {i}: {pipeline['name']}")
                print(f"   {pipeline['description']}")
                print(f"   Complete: {'✅ Yes' if pipeline.get('complete', False) else '❌ No'}")
                print(f"   Steps:")
                for step in pipeline['steps']:
                    print(f"      {step['step']}. {step['agent']} - {step['description'][:60]}...")

                if pipeline.get('gaps'):
                    print(f"   Gaps: {', '.join(pipeline['gaps'])}")

    elif args.command == 'analyze':
        print(f"📊 Analyzing '{args.agent}'...\n")
        result = analyzer.analyze_agent(args.agent)

        if args.format == "text" and "error" not in result:
            print(f"Agent: {result['agent']}")
            print(f"Produces: {', '.join(result['produces']) if result['produces'] else 'none'}")
            print(f"Consumes: {', '.join(result['consumes']) if result['consumes'] else 'none'}")

            if result.get('suggested_workflows'):
                print(f"\n🔄 Suggested Workflows:")
                for workflow in result['suggested_workflows']:
                    print(f"\n   {workflow['name']}")
                    print(f"   {workflow['description']}")
                    print(f"   Pipeline: {' → '.join(workflow['agents'])}")

    elif args.command == 'list-all':
        print("🗺️  Generating complete compatibility graph...\n")
        result = analyzer.generate_compatibility_graph()

        if args.format == "text":
            print(f"Total Agents: {result['metadata']['total_agents']}")
            print(f"Total Artifact Types: {result['metadata']['total_artifact_types']}")
            print(f"Total Relationships: {len(result['relationships'])}")

            if result['gaps']:
                print(f"\n⚠️  Global Gaps ({len(result['gaps'])}):")
                for gap in result['gaps']:
                    print(f"   • {gap['artifact']}: {gap['issue']}")

    elif args.command == 'verify-integrity':
        print("🔐 Verifying registry integrity using provenance hashes...\n")
        result = analyzer.verify_registry_integrity()

        if args.format == "text":
            summary = result['summary']
            print(f"Total Checked: {summary['total_checked']}")
            print(f"✅ Verified: {summary['verified_count']}")
            print(f"❌ Failed: {summary['failed_count']}")
            print(f"⚠️  Missing Hash: {summary['missing_count']}")

            if result['verified']:
                print(f"\n✅ Verified Artifacts ({len(result['verified'])}):")
                for item in result['verified']:
                    print(f"   • {item['artifact']}: {item['hash']}")
                    if item.get('provenance_logged'):
                        match_status = "✓" if item.get('provenance_match') else "✗"
                        print(f"     Provenance: {match_status}")

            if result['failed']:
                print(f"\n❌ Failed Verifications ({len(result['failed'])}):")
                for item in result['failed']:
                    print(f"   • {item['artifact']}: {item['reason']}")
                    if 'stored_hash' in item:
                        print(f"     Expected: {item['stored_hash']}")
                        print(f"     Computed: {item['computed_hash']}")

            if result['missing']:
                print(f"\n⚠️  Missing Hashes ({len(result['missing'])}):")
                for item in result['missing']:
                    print(f"   • {item['artifact']}: {item['reason']}")

    # Output result
    if result:
        if args.format == "json":
            print(json.dumps(result, indent=2))
        elif args.format == "yaml":
            print(yaml.dump(result, default_flow_style=False))
        elif "error" in result:
            print(f"\n❌ Error: {result['error']}")
            if "suggestion" in result:
                print(f"💡 {result['suggestion']}")


if __name__ == "__main__":
    main()
