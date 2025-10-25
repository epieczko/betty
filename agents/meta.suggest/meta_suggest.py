#!/usr/bin/env python3
"""
meta.suggest - Context-Aware Next-Step Recommender

Helps Claude decide what to do next after an agent completes by analyzing
context and suggesting compatible next steps.
"""

import json
import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from datetime import datetime

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)

# Import meta.compatibility
meta_comp_path = parent_dir + "/agents/meta.compatibility"
sys.path.insert(0, meta_comp_path)
import meta_compatibility


class SuggestionEngine:
    """Context-aware suggestion engine"""

    def __init__(self, base_dir: str = "."):
        """Initialize with base directory"""
        self.base_dir = Path(base_dir)
        self.compatibility_analyzer = meta_compatibility.CompatibilityAnalyzer(base_dir)
        self.compatibility_analyzer.scan_agents()
        self.compatibility_analyzer.build_compatibility_map()

    def suggest_next_steps(
        self,
        context_agent: str,
        artifacts_produced: Optional[List[str]] = None,
        goal: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Suggest next steps based on context

        Args:
            context_agent: Agent that just ran
            artifacts_produced: List of artifact file paths produced
            goal: Optional user goal

        Returns:
            Suggestion report with recommendations
        """
        # Get compatibility info for the agent
        compatibility = self.compatibility_analyzer.find_compatible(context_agent)

        if "error" in compatibility:
            return {
                "error": compatibility["error"],
                "context": {
                    "agent": context_agent,
                    "artifacts": artifacts_produced or []
                }
            }

        # Determine artifact types produced
        artifact_types = set()
        if artifacts_produced:
            artifact_types = self._infer_artifact_types(artifacts_produced)
        else:
            artifact_types = set(compatibility.get("produces", []))

        suggestions = []

        # Suggestion 1: Validate/analyze what was created
        if context_agent not in ["meta.compatibility", "meta.suggest"]:
            suggestions.append({
                "action": "Analyze compatibility",
                "agent": "meta.compatibility",
                "command": f"python3 agents/meta.compatibility/meta_compatibility.py analyze {context_agent}",
                "rationale": f"Understand what agents can work with {context_agent}'s outputs",
                "artifacts_needed": [],
                "produces": ["compatibility-graph"],
                "priority": "medium",
                "estimated_duration": "< 1 minute"
            })

        # Suggestion 2: Use compatible agents
        can_feed_to = compatibility.get("can_feed_to", [])
        for compatible in can_feed_to[:3]:  # Top 3
            next_agent = compatible["agent"]
            artifact = compatible["artifact"]

            suggestions.append({
                "action": f"Process with {next_agent}",
                "agent": next_agent,
                "rationale": compatible["rationale"],
                "artifacts_needed": [artifact],
                "produces": self._get_agent_produces(next_agent),
                "priority": "high",
                "estimated_duration": "varies"
            })

        # Suggestion 3: If agent created something, suggest testing/validation
        if artifact_types and context_agent in ["meta.agent", "meta.artifact"]:
            suggestions.append({
                "action": "Test the created artifact",
                "rationale": "Verify the artifact works as expected",
                "artifacts_needed": list(artifact_types),
                "priority": "high",
                "manual": True
            })

        # Suggestion 4: If gaps exist, suggest filling them
        gaps = compatibility.get("gaps", [])
        if gaps:
            for gap in gaps[:2]:  # Top 2 gaps
                suggestions.append({
                    "action": f"Create producer for '{gap['artifact']}'",
                    "rationale": gap["issue"],
                    "severity": gap.get("severity", "medium"),
                    "priority": "low",
                    "manual": True
                })

        # Rank suggestions
        suggestions = self._rank_suggestions(suggestions, goal)

        # Build report
        report = {
            "context": {
                "agent": context_agent,
                "artifacts_produced": artifacts_produced or [],
                "artifact_types": list(artifact_types),
                "timestamp": datetime.now().isoformat()
            },
            "suggestions": suggestions,
            "primary_suggestion": suggestions[0] if suggestions else None,
            "alternatives": suggestions[1:4] if len(suggestions) > 1 else [],
            "warnings": self._generate_warnings(context_agent, compatibility, gaps)
        }

        return report

    def _infer_artifact_types(self, artifact_paths: List[str]) -> Set[str]:
        """Infer artifact types from file paths"""
        types = set()

        for path in artifact_paths:
            path_lower = path.lower()

            # Pattern matching
            if ".openapi." in path_lower:
                types.add("openapi-spec")
            elif "agent.yaml" in path_lower:
                types.add("agent-definition")
            elif "readme.md" in path_lower:
                if "agent" in path_lower:
                    types.add("agent-documentation")
            elif ".validation." in path_lower:
                types.add("validation-report")
            elif ".optimization." in path_lower:
                types.add("optimization-report")
            elif ".compatibility." in path_lower:
                types.add("compatibility-graph")
            elif ".pipeline." in path_lower:
                types.add("pipeline-suggestion")
            elif ".workflow." in path_lower:
                types.add("workflow-definition")

        return types

    def _get_agent_produces(self, agent_name: str) -> List[str]:
        """Get what an agent produces"""
        if agent_name in self.compatibility_analyzer.agents:
            agent_def = self.compatibility_analyzer.agents[agent_name]
            produces, _ = self.compatibility_analyzer.extract_artifacts(agent_def)
            return list(produces)
        return []

    def _rank_suggestions(self, suggestions: List[Dict], goal: Optional[str] = None) -> List[Dict]:
        """Rank suggestions by relevance"""
        priority_order = {"high": 3, "medium": 2, "low": 1}

        # Sort by priority, then by manual (auto first)
        return sorted(
            suggestions,
            key=lambda s: (
                -priority_order.get(s.get("priority", "medium"), 2),
                s.get("manual", False)  # Auto suggestions first
            )
        )

    def _generate_warnings(
        self,
        agent: str,
        compatibility: Dict,
        gaps: List[Dict]
    ) -> List[Dict]:
        """Generate warnings based on context"""
        warnings = []

        # Warn about gaps
        if gaps:
            warnings.append({
                "type": "gaps",
                "message": f"{agent} requires artifacts that aren't produced by any agent",
                "details": [g["artifact"] for g in gaps],
                "severity": "medium"
            })

        # Warn if no compatible agents
        if not compatibility.get("can_feed_to") and not compatibility.get("can_receive_from"):
            warnings.append({
                "type": "isolated",
                "message": f"{agent} has no compatible agents",
                "details": "This agent can't be used in multi-agent pipelines",
                "severity": "low"
            })

        return warnings

    def analyze_project(self) -> Dict[str, Any]:
        """Analyze entire project and suggest improvements"""
        # Generate compatibility graph
        graph = self.compatibility_analyzer.generate_compatibility_graph()

        suggestions = []

        # Suggest filling gaps
        for gap in graph.get("gaps", []):
            suggestions.append({
                "action": f"Create agent/skill to produce '{gap['artifact']}'",
                "rationale": gap["issue"],
                "priority": "medium",
                "impact": f"Enables {len(gap.get('consumers', []))} agents"
            })

        # Suggest creating more agents if few exist
        if graph["metadata"]["total_agents"] < 5:
            suggestions.append({
                "action": "Create more agents using meta.agent",
                "rationale": "Expand agent ecosystem for more capabilities",
                "priority": "low"
            })

        # Suggest documentation if gaps exist
        if graph.get("gaps"):
            suggestions.append({
                "action": "Document artifact standards for gaps",
                "rationale": "Clarify requirements for missing artifacts",
                "priority": "low"
            })

        return {
            "project_analysis": {
                "total_agents": graph["metadata"]["total_agents"],
                "total_artifacts": graph["metadata"]["total_artifact_types"],
                "total_relationships": len(graph["relationships"]),
                "total_gaps": len(graph["gaps"])
            },
            "suggestions": suggestions,
            "gaps": graph["gaps"],
            "timestamp": datetime.now().isoformat()
        }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.suggest - Context-Aware Next-Step Recommender"
    )

    parser.add_argument(
        "--context",
        help="Agent that just ran"
    )
    parser.add_argument(
        "--artifacts",
        nargs="+",
        help="Artifacts that were produced"
    )
    parser.add_argument(
        "--goal",
        help="User's goal (for better suggestions)"
    )
    parser.add_argument(
        "--analyze-project",
        action="store_true",
        help="Analyze entire project and suggest improvements"
    )
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    engine = SuggestionEngine()

    if args.analyze_project:
        print("🔍 Analyzing project...\n")
        result = engine.analyze_project()

        if args.format == "text":
            print(f"📊 Project Analysis:")
            print(f"   Total Agents: {result['project_analysis']['total_agents']}")
            print(f"   Total Artifacts: {result['project_analysis']['total_artifacts']}")
            print(f"   Relationships: {result['project_analysis']['total_relationships']}")
            print(f"   Gaps: {result['project_analysis']['total_gaps']}")

            if result.get("suggestions"):
                print(f"\n💡 Suggestions ({len(result['suggestions'])}):")
                for i, suggestion in enumerate(result["suggestions"], 1):
                    print(f"\n   {i}. {suggestion['action']}")
                    print(f"      {suggestion['rationale']}")
                    print(f"      Priority: {suggestion['priority']}")

        else:
            print(json.dumps(result, indent=2))

    elif args.context:
        print(f"💡 Suggesting next steps after '{args.context}'...\n")
        result = engine.suggest_next_steps(
            args.context,
            args.artifacts,
            args.goal
        )

        if args.format == "text":
            if "error" in result:
                print(f"❌ Error: {result['error']}")
                return

            print(f"Context: {result['context']['agent']}")
            if result['context']['artifact_types']:
                print(f"Produced: {', '.join(result['context']['artifact_types'])}")

            if result.get("primary_suggestion"):
                print(f"\n🌟 Primary Suggestion:")
                ps = result["primary_suggestion"]
                print(f"   {ps['action']}")
                print(f"   Rationale: {ps['rationale']}")
                if not ps.get("manual"):
                    print(f"   Command: {ps.get('command', 'N/A')}")
                print(f"   Priority: {ps['priority']}")

            if result.get("alternatives"):
                print(f"\n🔄 Alternatives:")
                for i, alt in enumerate(result["alternatives"], 1):
                    print(f"\n   {i}. {alt['action']}")
                    print(f"      {alt['rationale']}")

            if result.get("warnings"):
                print(f"\n⚠️  Warnings:")
                for warning in result["warnings"]:
                    print(f"   • {warning['message']}")

        else:
            print(json.dumps(result, indent=2))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
