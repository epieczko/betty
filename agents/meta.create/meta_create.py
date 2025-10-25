#!/usr/bin/env python3
"""
meta.create - Orchestrator Meta-Agent

Intelligently orchestrates the creation of skills, commands, and agents.
Checks inventory, determines what needs to be created, validates compatibility,
and fills gaps automatically.

This is the main entry point for creating Betty components from descriptions.
"""

import json
import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)

# Import other meta agents by adding their paths
meta_command_path = Path(parent_dir) / "agents" / "meta.command"
meta_skill_path = Path(parent_dir) / "agents" / "meta.skill"
meta_agent_path = Path(parent_dir) / "agents" / "meta.agent"
meta_compatibility_path = Path(parent_dir) / "agents" / "meta.compatibility"
registry_query_path = Path(parent_dir) / "skills" / "registry.query"

sys.path.insert(0, str(meta_command_path))
sys.path.insert(0, str(meta_skill_path))
sys.path.insert(0, str(meta_agent_path))
sys.path.insert(0, str(meta_compatibility_path))
sys.path.insert(0, str(registry_query_path))

import meta_command
import meta_skill
import meta_agent
import meta_compatibility
import registry_query

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.traceability import get_tracer, RequirementInfo

logger = setup_logger(__name__)


class ComponentCreator:
    """Orchestrates the creation of skills, commands, and agents"""

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize orchestrator"""
        self.base_dir = Path(base_dir)
        self.created_components = []
        self.compatibility_analyzer = None

    def check_duplicate(self, component_type: str, name: str) -> Optional[Dict[str, Any]]:
        """
        Check if a component already exists in registry

        Args:
            component_type: 'skills', 'commands', or 'agents'
            name: Component name to check

        Returns:
            Existing component info if found, None otherwise
        """
        try:
            result = registry_query.query_registry(
                registry=component_type,
                name=name,
                fuzzy=False
            )

            if result.get("ok") and result.get("details", {}).get("matching_entries", 0) > 0:
                matches = result["details"]["results"]
                # Check for exact match
                for match in matches:
                    if match["name"] == name:
                        return match
            return None

        except Exception as e:
            logger.warning(f"Error checking duplicate for {name}: {e}")
            return None

    def parse_description_type(self, description_path: str) -> Dict[str, Any]:
        """
        Determine what type of component is being described

        Args:
            description_path: Path to description file

        Returns:
            Dict with component_type and parsed metadata
        """
        path = Path(description_path)
        content = path.read_text()

        # Try to determine type from content
        result = {
            "is_skill": False,
            "is_command": False,
            "is_agent": False,
            "path": str(path)
        }

        content_lower = content.lower()

        # Check for skill indicators
        if any(x in content_lower for x in ["# produces artifacts:", "# consumes artifacts:",
                                              "skill.yaml", "artifact_metadata"]):
            result["is_skill"] = True

        # Check for command indicators
        if any(x in content_lower for x in ["# execution type:", "# parameters:",
                                              "command manifest"]):
            result["is_command"] = True

        # Check for agent indicators
        if any(x in content_lower for x in ["# skills:", "skills_available",
                                              "agent purpose", "multi-step", "orchestrat"]):
            result["is_agent"] = True

        # If ambiguous, look at explicit markers
        if "# type: skill" in content_lower:
            result["is_skill"] = True
            result["is_command"] = False
            result["is_agent"] = False
        elif "# type: command" in content_lower:
            result["is_command"] = True
            result["is_skill"] = False
            result["is_agent"] = False
        elif "# type: agent" in content_lower:
            result["is_agent"] = True
            result["is_skill"] = False
            result["is_command"] = False

        return result

    def create_skill(
        self,
        description_path: str,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create a skill using meta.skill

        Args:
            description_path: Path to skill description
            requirement: Optional requirement info

        Returns:
            Creation result
        """
        logger.info(f"Creating skill from {description_path}")

        creator = meta_skill.SkillCreator(base_dir=str(self.base_dir))
        result = creator.create_skill(description_path, requirement=requirement)

        self.created_components.append({
            "type": "skill",
            "name": result.get("skill_name"),
            "files": result.get("created_files", []),
            "trace_id": result.get("trace_id")
        })

        return result

    def create_command(
        self,
        description_path: str,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create a command using meta.command

        Args:
            description_path: Path to command description
            requirement: Optional requirement info

        Returns:
            Creation result with complexity analysis
        """
        logger.info(f"Creating command from {description_path}")

        creator = meta_command.CommandCreator(base_dir=str(self.base_dir))
        result = creator.create_command(description_path, requirement=requirement)

        self.created_components.append({
            "type": "command",
            "name": result.get("command_name"),
            "manifest": result.get("manifest_file"),
            "analysis": result.get("complexity_analysis"),
            "trace_id": result.get("trace_id")
        })

        return result

    def create_agent(
        self,
        description_path: str,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create an agent using meta.agent

        Args:
            description_path: Path to agent description
            requirement: Optional requirement info

        Returns:
            Creation result
        """
        logger.info(f"Creating agent from {description_path}")

        creator = meta_agent.AgentCreator(
            registry_path=str(self.base_dir / "registry" / "skills.json")
        )
        result = creator.create_agent(description_path, requirement=requirement)

        self.created_components.append({
            "type": "agent",
            "name": result.get("name"),
            "files": [result.get("agent_yaml"), result.get("readme")],
            "skills": result.get("skills", []),
            "trace_id": result.get("trace_id")
        })

        return result

    def validate_compatibility(self, agent_name: str) -> Dict[str, Any]:
        """
        Validate agent compatibility using meta.compatibility

        Args:
            agent_name: Name of agent to validate

        Returns:
            Compatibility analysis
        """
        logger.info(f"Validating compatibility for {agent_name}")

        if not self.compatibility_analyzer:
            self.compatibility_analyzer = meta_compatibility.CompatibilityAnalyzer(
                base_dir=str(self.base_dir)
            )
            self.compatibility_analyzer.scan_agents()
            self.compatibility_analyzer.build_compatibility_map()

        return self.compatibility_analyzer.analyze_agent(agent_name)

    def orchestrate_creation(
        self,
        description_path: str,
        auto_fill_gaps: bool = False,
        check_duplicates: bool = True,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Main orchestration method that intelligently creates components

        Args:
            description_path: Path to description file
            auto_fill_gaps: Whether to automatically create missing dependencies
            check_duplicates: Whether to check for existing components
            requirement: Optional requirement info for traceability

        Returns:
            Comprehensive creation report
        """
        print(f"🎯 meta.create - Orchestrating component creation from {description_path}\n")

        report = {
            "ok": True,
            "description_path": description_path,
            "component_type": None,
            "created_components": [],
            "skipped_components": [],
            "compatibility_analysis": None,
            "gaps": [],
            "recommendations": [],
            "errors": []
        }

        try:
            # Step 1: Determine what's being described
            print("📋 Step 1: Analyzing description...")
            desc_type = self.parse_description_type(description_path)
            print(f"   Detected types: Skill={desc_type['is_skill']}, "
                  f"Command={desc_type['is_command']}, Agent={desc_type['is_agent']}\n")

            # Step 2: Check for duplicates if requested
            if check_duplicates:
                print("🔍 Step 2: Checking for existing components...")

                # Parse name from description
                content = Path(description_path).read_text()
                name_match = None
                for line in content.split('\n'):
                    if line.strip().startswith('# Name:'):
                        name_match = line.replace('# Name:', '').strip()
                        break

                if name_match:
                    # Check all registries
                    for comp_type in ['skills', 'commands', 'agents']:
                        existing = self.check_duplicate(comp_type, name_match)
                        if existing:
                            print(f"   ⚠️  Found existing {comp_type[:-1]}: {name_match}")
                            report["skipped_components"].append({
                                "type": comp_type[:-1],
                                "name": name_match,
                                "reason": "Already exists",
                                "existing": existing
                            })

                if not report["skipped_components"]:
                    print("   ✅ No duplicates found\n")
                else:
                    print()

            # Step 3: Create components based on type
            print("🛠️  Step 3: Creating components...\n")

            # If it's a command, analyze complexity first
            if desc_type["is_command"]:
                print("   📊 Analyzing command complexity...")
                creator = meta_command.CommandCreator(base_dir=str(self.base_dir))

                # Read content for analysis
                with open(description_path) as f:
                    full_content = f.read()

                cmd_desc = creator.parse_description(description_path)
                analysis = creator.analyze_complexity(cmd_desc, full_content)

                print(f"   Recommended pattern: {analysis['recommended_pattern']}")
                print(f"   Should create skill: {analysis['should_create_skill']}\n")

                # Update desc_type based on analysis
                if analysis['should_create_skill']:
                    desc_type['is_skill'] = True

            # Create skill first if needed
            if desc_type["is_skill"]:
                print("   🔧 Creating skill...")
                skill_result = self.create_skill(description_path, requirement)

                if skill_result.get("errors"):
                    report["errors"].extend(skill_result["errors"])
                    print(f"   ⚠️  Skill creation had warnings\n")
                else:
                    print(f"   ✅ Skill '{skill_result['skill_name']}' created\n")
                    report["created_components"].append({
                        "type": "skill",
                        "name": skill_result["skill_name"],
                        "files": skill_result.get("created_files", [])
                    })

            # Create command if needed
            if desc_type["is_command"]:
                print("   📜 Creating command...")
                command_result = self.create_command(description_path, requirement)

                if command_result.get("ok"):
                    print(f"   ✅ Command '{command_result['command_name']}' created\n")
                    report["created_components"].append({
                        "type": "command",
                        "name": command_result["command_name"],
                        "manifest": command_result.get("manifest_file"),
                        "pattern": command_result.get("complexity_analysis", {}).get("recommended_pattern")
                    })
                else:
                    report["errors"].append(f"Command creation failed: {command_result.get('error')}")
                    print(f"   ❌ Command creation failed\n")

            # Create agent if needed
            if desc_type["is_agent"]:
                print("   🤖 Creating agent...")
                agent_result = self.create_agent(description_path, requirement)

                print(f"   ✅ Agent '{agent_result['name']}' created")
                print(f"   Skills: {', '.join(agent_result.get('skills', []))}\n")

                report["created_components"].append({
                    "type": "agent",
                    "name": agent_result["name"],
                    "files": [agent_result.get("agent_yaml"), agent_result.get("readme")],
                    "skills": agent_result.get("skills", [])
                })

                # Step 4: Validate compatibility for agents
                print("🔬 Step 4: Validating compatibility...\n")
                compatibility = self.validate_compatibility(agent_result["name"])

                if "error" not in compatibility:
                    report["compatibility_analysis"] = compatibility

                    # Check for gaps
                    gaps = compatibility.get("gaps", [])
                    if gaps:
                        print(f"   ⚠️  Found {len(gaps)} gap(s):")
                        for gap in gaps:
                            print(f"      • {gap['artifact']}: {gap['issue']}")
                            report["gaps"].append(gap)
                        print()

                        # Add recommendations
                        for gap in gaps:
                            report["recommendations"].append(
                                f"Create skill to produce '{gap['artifact']}' artifact"
                            )
                    else:
                        print("   ✅ No compatibility gaps found\n")

                    # Show compatible agents
                    if compatibility.get("can_feed_to"):
                        print(f"   ➡️  Can feed to {len(compatibility['can_feed_to'])} agent(s)")
                    if compatibility.get("can_receive_from"):
                        print(f"   ⬅️  Can receive from {len(compatibility['can_receive_from'])} agent(s)")
                    print()

            # Step 5: Auto-fill gaps if requested
            if auto_fill_gaps and report["gaps"]:
                print("🔧 Step 5: Auto-filling gaps...\n")
                for gap in report["gaps"]:
                    print(f"   TODO: Auto-create skill for '{gap['artifact']}'")
                    # TODO: Implement auto-gap-filling
                print()

            # Final summary
            print("=" * 80)
            print("✨ CREATION SUMMARY")
            print("=" * 80)

            if report["created_components"]:
                print(f"\n✅ Created {len(report['created_components'])} component(s):")
                for comp in report["created_components"]:
                    print(f"   • {comp['type'].upper()}: {comp['name']}")

            if report["skipped_components"]:
                print(f"\n⏭️  Skipped {len(report['skipped_components'])} component(s) (already exist):")
                for comp in report["skipped_components"]:
                    print(f"   • {comp['type'].upper()}: {comp['name']}")

            if report["gaps"]:
                print(f"\n⚠️  Found {len(report['gaps'])} compatibility gap(s)")

            if report["recommendations"]:
                print("\n💡 Recommendations:")
                for rec in report["recommendations"]:
                    print(f"   • {rec}")

            print("\n" + "=" * 80 + "\n")

            return report

        except Exception as e:
            logger.error(f"Error during orchestration: {e}", exc_info=True)
            report["ok"] = False
            report["errors"].append(str(e))
            print(f"\n❌ Error: {e}\n")
            return report


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.create - Intelligent component creation orchestrator"
    )
    parser.add_argument(
        "description",
        help="Path to component description file (.md or .json)"
    )
    parser.add_argument(
        "--auto-fill-gaps",
        action="store_true",
        help="Automatically create missing dependencies"
    )
    parser.add_argument(
        "--skip-duplicate-check",
        action="store_true",
        help="Skip checking for existing components"
    )
    parser.add_argument(
        "--output-format",
        choices=["json", "yaml", "text"],
        default="text",
        help="Output format for final report"
    )

    # Traceability arguments
    parser.add_argument(
        "--requirement-id",
        help="Requirement identifier (e.g., REQ-2025-001)"
    )
    parser.add_argument(
        "--requirement-description",
        help="What this component accomplishes"
    )
    parser.add_argument(
        "--requirement-source",
        help="Source document"
    )
    parser.add_argument(
        "--issue-id",
        help="Issue tracking ID (e.g., JIRA-123)"
    )
    parser.add_argument(
        "--requested-by",
        help="Who requested this"
    )
    parser.add_argument(
        "--rationale",
        help="Why this is needed"
    )

    args = parser.parse_args()

    # Create requirement info if provided
    requirement = None
    if args.requirement_id and args.requirement_description:
        requirement = RequirementInfo(
            id=args.requirement_id,
            description=args.requirement_description,
            source=args.requirement_source,
            issue_id=args.issue_id,
            requested_by=args.requested_by,
            rationale=args.rationale
        )

    orchestrator = ComponentCreator()
    result = orchestrator.orchestrate_creation(
        description_path=args.description,
        auto_fill_gaps=args.auto_fill_gaps,
        check_duplicates=not args.skip_duplicate_check,
        requirement=requirement
    )

    # Output final report in requested format
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
    elif args.output_format == "yaml":
        print(yaml.dump(result, default_flow_style=False))

    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
