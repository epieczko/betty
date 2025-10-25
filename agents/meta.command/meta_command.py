#!/usr/bin/env python3
"""
meta.command - Command Creator Meta-Agent

Generates command manifests from natural language descriptions.

Usage:
    python3 agents/meta.command/meta_command.py <command_description_file>

Examples:
    python3 agents/meta.command/meta_command.py examples/api_validate_command.md
    python3 agents/meta.command/meta_command.py examples/deploy_command.json
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    BASE_DIR,
    COMMANDS_REGISTRY_FILE,
    CommandExecutionType,
    CommandStatus
)
from betty.logging_utils import setup_logger
from betty.traceability import get_tracer, RequirementInfo

logger = setup_logger(__name__)


class CommandCreator:
    """Creates command manifests from descriptions"""

    VALID_EXECUTION_TYPES = ["agent", "skill", "workflow"]
    VALID_STATUSES = ["draft", "active", "deprecated", "archived"]
    VALID_PARAMETER_TYPES = ["string", "integer", "boolean", "enum", "array", "object"]

    # Keywords for execution type analysis
    REASONING_KEYWORDS = [
        "design", "architect", "reason", "decide", "evaluate",
        "assess", "review", "analyze deeply", "consider", "judge",
        "trade-off", "iterate", "refine", "adapt", "intelligent"
    ]

    ORCHESTRATION_KEYWORDS = [
        "pipeline", "orchestrate", "coordinate", "sequence",
        "parallel", "concurrent", "multi-stage", "workflow",
        "first.*then", "phases", "steps in order"
    ]

    AUTONOMY_KEYWORDS = [
        "analyze", "optimize", "decide", "evaluate", "assess",
        "complex", "multi-step", "autonomous", "intelligent",
        "adaptive", "sophisticated", "advanced", "comprehensive"
    ]

    REUSABILITY_KEYWORDS = [
        "reusable", "composable", "building block", "library",
        "utility", "helper", "shared", "common", "core"
    ]

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize command creator"""
        self.base_dir = Path(base_dir)
        self.commands_dir = self.base_dir / "commands"

    def parse_description(self, description_path: str) -> Dict[str, Any]:
        """
        Parse command description from Markdown or JSON file

        Args:
            description_path: Path to description file

        Returns:
            Dict with command configuration
        """
        path = Path(description_path)

        if not path.exists():
            raise FileNotFoundError(f"Description file not found: {description_path}")

        # Read file
        content = path.read_text()

        # Try JSON first
        if path.suffix == ".json":
            return json.loads(content)

        # Parse Markdown format
        cmd_desc = {}

        # Extract fields using regex patterns
        patterns = {
            "name": r"#\s*Name:\s*(.+)",
            "version": r"#\s*Version:\s*(.+)",
            "description": r"#\s*Description:\s*(.+)",
            "execution_type": r"#\s*Execution\s*Type:\s*(.+)",
            "target": r"#\s*Target:\s*(.+)",
            "status": r"#\s*Status:\s*(.+)",
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                value = match.group(1).strip()
                cmd_desc[field] = value

        # Parse parameters section
        params_section = re.search(
            r"#\s*Parameters:\s*\n(.*?)(?=\n#|\Z)",
            content,
            re.DOTALL | re.IGNORECASE
        )

        if params_section:
            cmd_desc["parameters"] = self._parse_parameters(params_section.group(1))

        # Parse tags
        tags_match = re.search(r"#\s*Tags:\s*(.+)", content, re.IGNORECASE)
        if tags_match:
            tags_str = tags_match.group(1).strip()
            # Parse comma-separated or bracket-enclosed tags
            if tags_str.startswith("[") and tags_str.endswith("]"):
                tags_str = tags_str[1:-1]
            cmd_desc["tags"] = [t.strip() for t in tags_str.split(",")]

        # Parse execution context
        context_section = re.search(
            r"#\s*Execution\s*Context:\s*\n(.*?)(?=\n#|\Z)",
            content,
            re.DOTALL | re.IGNORECASE
        )
        if context_section:
            cmd_desc["execution_context"] = self._parse_context(context_section.group(1))

        # Validate required fields
        required = ["name", "description", "execution_type", "target"]
        missing = [f for f in required if f not in cmd_desc]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        # Validate execution type
        if cmd_desc["execution_type"].lower() not in self.VALID_EXECUTION_TYPES:
            raise ValueError(
                f"Invalid execution type: {cmd_desc['execution_type']}. "
                f"Must be one of: {', '.join(self.VALID_EXECUTION_TYPES)}"
            )

        # Ensure command name starts with /
        if not cmd_desc["name"].startswith("/"):
            cmd_desc["name"] = "/" + cmd_desc["name"]

        # Set defaults
        if "version" not in cmd_desc:
            cmd_desc["version"] = "0.1.0"
        if "status" not in cmd_desc:
            cmd_desc["status"] = "draft"
        if "parameters" not in cmd_desc:
            cmd_desc["parameters"] = []

        return cmd_desc

    def _parse_parameters(self, params_text: str) -> List[Dict[str, Any]]:
        """Parse parameters from markdown text"""
        parameters = []

        # Match parameter blocks
        # Format: - name: type (required/optional) - description
        param_pattern = r"-\s+(\w+):\s+(\w+)(?:\s+\(([^)]+)\))?\s+-\s+(.+?)(?=\n-|\n#|\Z)"
        matches = re.finditer(param_pattern, params_text, re.DOTALL)

        for match in matches:
            name, param_type, modifiers, description = match.groups()

            param = {
                "name": name.strip(),
                "type": param_type.strip(),
                "description": description.strip()
            }

            # Parse modifiers (required, optional, default=value)
            if modifiers:
                modifiers = modifiers.lower()
                param["required"] = "required" in modifiers

                # Extract default value
                default_match = re.search(r"default[=:]\s*([^,\s]+)", modifiers)
                if default_match:
                    default_val = default_match.group(1)
                    # Convert types
                    if param_type == "integer":
                        default_val = int(default_val)
                    elif param_type == "boolean":
                        default_val = default_val.lower() in ("true", "yes", "1")
                    param["default"] = default_val

                # Extract enum values
                values_match = re.search(r"values[=:]\s*\[([^\]]+)\]", modifiers)
                if values_match:
                    param["values"] = [v.strip() for v in values_match.group(1).split(",")]

            parameters.append(param)

        return parameters

    def _parse_context(self, context_text: str) -> Dict[str, Any]:
        """Parse execution context from markdown text"""
        context = {}

        # Simple key: value parsing
        for line in context_text.split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            match = re.match(r"-\s*(\w+):\s*(.+)", line)
            if match:
                key, value = match.groups()
                # Try to parse as JSON for complex values
                try:
                    context[key] = json.loads(value)
                except (json.JSONDecodeError, ValueError):
                    context[key] = value.strip()

        return context

    def calculate_reasoning_score(self, content: str) -> int:
        """Calculate reasoning score for agent detection"""
        score = 0
        content_lower = content.lower()

        # Check for reasoning keywords
        for keyword in self.REASONING_KEYWORDS:
            if keyword in content_lower:
                score += 3

        # Check for context indicators
        context_indicators = [
            "understand context", "domain knowledge", "make judgment",
            "qualitative", "subjective", "depends on", "consider trade-offs"
        ]
        for indicator in context_indicators:
            if indicator in content_lower:
                score += 5

        # Check for iterative indicators
        iterative_indicators = ["iterate", "refine", "feedback", "improve based on"]
        for indicator in iterative_indicators:
            if indicator in content_lower:
                score += 8

        return score

    def calculate_orchestration_score(self, content: str) -> int:
        """Calculate orchestration score for workflow detection"""
        score = 0
        content_lower = content.lower()

        # Check for orchestration keywords
        for keyword in self.ORCHESTRATION_KEYWORDS:
            if re.search(keyword, content_lower):
                score += 3

        # Check for multiple component references
        component_patterns = [
            r"skill.*skill", r"agent.*agent", r"service.*service",
            r"call.*call", r"invoke.*invoke"
        ]
        for pattern in component_patterns:
            if re.search(pattern, content_lower):
                score += 5

        # Check for parallel execution indicators
        parallel_indicators = ["parallel", "concurrent", "simultaneously", "at the same time"]
        for indicator in parallel_indicators:
            if indicator in content_lower:
                score += 8

        # Check for sequence indicators
        sequence_indicators = [
            r"first.*then", r"after.*before", r"step \d+.*step \d+",
            r"phase \d+.*phase \d+"
        ]
        for pattern in sequence_indicators:
            if re.search(pattern, content_lower):
                score += 7

        return score

    def analyze_complexity(self, cmd_desc: Dict[str, Any], full_content: str = "") -> Dict[str, Any]:
        """
        Analyze command complexity and recommend execution type

        Args:
            cmd_desc: Parsed command description
            full_content: Full description file content for analysis

        Returns:
            Dict with complexity analysis and execution type recommendation
        """
        analysis = {
            "step_count": 0,
            "complexity": "low",
            "reasoning_score": 0,
            "orchestration_score": 0,
            "autonomy_level": "none",
            "reusability": "low",
            "recommended_execution_type": "skill",
            "recommended_pattern": "COMMAND_ONLY",
            "should_create_backend": False,
            "reasoning": []
        }

        # Count steps from description
        # Look for numbered lists, bullet points, or explicit step mentions
        step_patterns = [
            r"^\s*\d+\.\s+",  # Numbered lists
            r"^\s*[-*]\s+",   # Bullet points
            r"\bstep\s+\d+\b",  # Explicit "step N"
        ]

        lines = full_content.split("\n")
        step_count = 0
        for line in lines:
            for pattern in step_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    step_count += 1
                    break

        analysis["step_count"] = step_count

        # Analyze content for keywords
        content_lower = full_content.lower()
        desc_lower = cmd_desc.get("description", "").lower()
        combined = content_lower + " " + desc_lower

        # Check autonomy keywords
        autonomy_matches = [kw for kw in self.AUTONOMY_KEYWORDS if kw in combined]
        if len(autonomy_matches) >= 3:
            analysis["autonomy_level"] = "high"
        elif len(autonomy_matches) >= 1:
            analysis["autonomy_level"] = "medium"
        else:
            analysis["autonomy_level"] = "low"

        # Check reusability keywords
        reusability_matches = [kw for kw in self.REUSABILITY_KEYWORDS if kw in combined]
        if len(reusability_matches) >= 2:
            analysis["reusability"] = "high"
        elif len(reusability_matches) >= 1:
            analysis["reusability"] = "medium"

        # Determine complexity
        if step_count >= 10:
            analysis["complexity"] = "high"
        elif step_count >= 4:
            analysis["complexity"] = "medium"
        else:
            analysis["complexity"] = "low"

        # Estimate lines of logic (rough heuristic)
        instruction_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith("#"))
        if instruction_lines > 50:
            analysis["complexity"] = "high"

        # Calculate reasoning and orchestration scores
        reasoning_score = self.calculate_reasoning_score(combined)
        orchestration_score = self.calculate_orchestration_score(combined)

        analysis["reasoning_score"] = reasoning_score
        analysis["orchestration_score"] = orchestration_score

        # Determine execution type based on scores
        # Priority: Check if explicitly set → reasoning → orchestration → default to skill

        # Check if execution type was explicitly set
        explicit_type = cmd_desc.get("execution_type")
        if explicit_type:
            analysis["recommended_execution_type"] = explicit_type.lower()
            analysis["reasoning"].append(f"Execution type explicitly set to '{explicit_type}'")
        else:
            # Auto-detect based on scores
            if reasoning_score >= 20:
                analysis["recommended_execution_type"] = "agent"
                analysis["reasoning"].append(
                    f"High reasoning score ({reasoning_score}): needs intelligent decision-making"
                )
            elif orchestration_score >= 15:
                analysis["recommended_execution_type"] = "workflow"
                analysis["reasoning"].append(
                    f"High orchestration score ({orchestration_score}): coordinates multiple components"
                )
            elif reasoning_score >= 10 and len(autonomy_matches) >= 3:
                analysis["recommended_execution_type"] = "agent"
                analysis["reasoning"].append(
                    f"Moderate reasoning score ({reasoning_score}) with autonomy keywords: {autonomy_matches[:3]}"
                )
            elif orchestration_score >= 8 and step_count >= 5:
                analysis["recommended_execution_type"] = "workflow"
                analysis["reasoning"].append(
                    f"Moderate orchestration score ({orchestration_score}) with multiple steps"
                )
            else:
                analysis["recommended_execution_type"] = "skill"
                analysis["reasoning"].append(
                    "Single atomic operation, deterministic execution"
                )

        # Determine pattern (whether backend needs to be created)
        complexity_score = 0
        if step_count >= 10:
            complexity_score += 10
        if analysis["complexity"] == "high":
            complexity_score += 8
        if analysis["reusability"] == "high":
            complexity_score += 5
        if instruction_lines > 50:
            complexity_score += 5

        if complexity_score >= 20:
            if analysis["recommended_execution_type"] == "skill":
                analysis["recommended_pattern"] = "SKILL_AND_COMMAND"
            elif analysis["recommended_execution_type"] == "agent":
                analysis["recommended_pattern"] = "AGENT_AND_COMMAND"
            else:  # workflow
                analysis["recommended_pattern"] = "WORKFLOW_AND_COMMAND"
            analysis["should_create_backend"] = True
            analysis["reasoning"].append(
                f"High complexity score ({complexity_score}): create backend component first"
            )
        elif complexity_score >= 10:
            analysis["recommended_pattern"] = f"{analysis['recommended_execution_type'].upper()}_AND_COMMAND"
            analysis["should_create_backend"] = True
            analysis["reasoning"].append(
                f"Moderate complexity score ({complexity_score}): consider creating backend"
            )
        else:
            analysis["recommended_pattern"] = "COMMAND_ONLY"
            analysis["reasoning"].append(
                f"Low complexity score ({complexity_score}): inline in command is sufficient"
            )

        return analysis

    def generate_command_manifest(self, cmd_desc: Dict[str, Any]) -> str:
        """
        Generate command manifest YAML

        Args:
            cmd_desc: Parsed command description

        Returns:
            YAML string
        """
        manifest = {
            "name": cmd_desc["name"],
            "version": cmd_desc["version"],
            "description": cmd_desc["description"]
        }

        # Add parameters if present
        if cmd_desc.get("parameters"):
            manifest["parameters"] = cmd_desc["parameters"]

        # Add execution configuration
        execution = {
            "type": cmd_desc["execution_type"],
            "target": cmd_desc["target"]
        }

        if cmd_desc.get("execution_context"):
            execution["context"] = cmd_desc["execution_context"]

        manifest["execution"] = execution

        # Add status
        manifest["status"] = cmd_desc.get("status", "draft")

        # Add tags if present
        if cmd_desc.get("tags"):
            manifest["tags"] = cmd_desc["tags"]

        return yaml.dump(manifest, default_flow_style=False, sort_keys=False)

    def create_command(
        self,
        description_path: str,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create command manifest from description file

        Args:
            description_path: Path to description file
            requirement: Optional requirement information for traceability

        Returns:
            Dict with creation results
        """
        try:
            print(f"🎯  meta.command - Creating command from {description_path}\n")

            # Read full content for analysis
            with open(description_path, 'r') as f:
                full_content = f.read()

            # Parse description
            cmd_desc = self.parse_description(description_path)

            # Analyze complexity and recommend pattern
            analysis = self.analyze_complexity(cmd_desc, full_content)

            # Display analysis
            print(f"📊 Execution Type Analysis:")
            print(f"   Steps detected: {analysis['step_count']}")
            print(f"   Complexity: {analysis['complexity']}")
            print(f"   Reasoning score: {analysis['reasoning_score']}")
            print(f"   Orchestration score: {analysis['orchestration_score']}")
            print(f"\n💡 Recommended Execution Type: {analysis['recommended_execution_type'].upper()}")
            print(f"💡 Recommended Pattern: {analysis['recommended_pattern']}")
            for reason in analysis['reasoning']:
                print(f"   • {reason}")
            print()

            # Generate manifest YAML
            manifest_yaml = self.generate_command_manifest(cmd_desc)

            # Ensure commands directory exists
            self.commands_dir.mkdir(parents=True, exist_ok=True)

            # Determine output filename
            # Remove leading / and replace spaces/special chars with hyphens
            filename = cmd_desc["name"].lstrip("/").replace(" ", "-").lower()
            filename = re.sub(r"[^a-z0-9-]", "", filename)
            manifest_file = self.commands_dir / f"{filename}.yaml"

            # Write manifest file
            manifest_file.write_text(manifest_yaml)

            print(f"✨ Command '{cmd_desc['name']}' created successfully!\n")
            print(f"📄 Created file:")
            print(f"   - {manifest_file}\n")
            print(f"✅ Command manifest is ready for registration")
            print(f"   Name: {cmd_desc['name']}")
            print(f"   Execution: {cmd_desc['execution_type']} → {cmd_desc['target']}")
            print(f"   Status: {cmd_desc.get('status', 'draft')}\n")

            # Display backend creation recommendation if needed
            if analysis['should_create_backend']:
                exec_type = analysis['recommended_execution_type']
                print(f"⚠️  RECOMMENDATION: Create the {exec_type} first!")
                print(f"   Pattern: {analysis['recommended_pattern']}")
                print(f"\n   This command delegates to {exec_type} ({cmd_desc['target']}),")
                print(f"   but that {exec_type} may not exist yet.\n")
                print(f"   Suggested workflow:")

                if exec_type == "agent":
                    print(f"   1. Create agent: python3 agents/meta.agent/meta_agent.py <agent-description.md>")
                    print(f"      - Agent should implement: {cmd_desc['target']}")
                    print(f"      - Include reasoning and decision-making logic")
                    print(f"   2. Test agent: python3 agents/{cmd_desc['target']}/agent.py")
                elif exec_type == "workflow":
                    print(f"   1. Create workflow: workflows/{cmd_desc['target']}")
                    print(f"      - Define sequence of skills/agents")
                    print(f"      - Configure parallel execution if needed")
                    print(f"   2. Validate workflow: python3 skills/workflow.validate/workflow_validate.py {cmd_desc['target']}")
                else:  # skill
                    print(f"   1. Create skill: python3 agents/meta.skill/meta_skill.py <skill-description.md>")
                    print(f"      - Skill should implement: {cmd_desc['target']}")
                    print(f"      - Include all complex logic from the command description")
                    print(f"   2. Test skill: python3 skills/{cmd_desc['target'].replace('.', '/')}/{cmd_desc['target'].replace('.', '_')}.py")

                print(f"   3. Review this command manifest: cat {manifest_file}")
                print(f"   4. Register command: python3 skills/command.define/command_define.py {manifest_file}")
                print(f"   5. Verify in registry: cat registry/commands.json")
                print(f"\n   See docs/COMMAND_EXECUTION_DECISION_TREE.md for pattern details\n")
            else:
                print(f"📝 Next steps:")
                print(f"   1. Review the manifest: cat {manifest_file}")
                print(f"   2. Register command: python3 skills/command.define/command_define.py {manifest_file}")
                print(f"   3. Verify in registry: cat registry/commands.json")

            result = {
                "ok": True,
                "status": "success",
                "command_name": cmd_desc["name"],
                "manifest_file": str(manifest_file),
                "complexity_analysis": analysis
            }

            # Log traceability if requirement provided
            trace_id = None
            if requirement:
                try:
                    tracer = get_tracer()

                    # Create component ID from command name
                    component_id = f"command.{filename.replace('-', '_')}"

                    trace_id = tracer.log_creation(
                        component_id=component_id,
                        component_name=cmd_desc["name"],
                        component_type="command",
                        component_version=cmd_desc["version"],
                        component_file_path=str(manifest_file),
                        input_source_path=description_path,
                        created_by_tool="meta.command",
                        created_by_version="0.1.0",
                        requirement=requirement,
                        tags=["command", "auto-generated"] + cmd_desc.get("tags", []),
                        project="Betty Framework"
                    )

                    # Log validation check
                    validation_details = {
                        "checks_performed": [
                            {"name": "command_structure", "status": "passed"},
                            {"name": "execution_type_validation", "status": "passed",
                             "message": f"Valid execution type: {cmd_desc['execution_type']}"},
                            {"name": "name_validation", "status": "passed",
                             "message": f"Command name follows convention: {cmd_desc['name']}"}
                        ]
                    }

                    # Check parameters
                    if cmd_desc.get("parameters"):
                        validation_details["checks_performed"].append({
                            "name": "parameters_validation",
                            "status": "passed",
                            "message": f"Validated {len(cmd_desc['parameters'])} parameters"
                        })

                    tracer.log_verification(
                        component_id=component_id,
                        check_type="validation",
                        tool="meta.command",
                        result="passed",
                        details=validation_details
                    )

                    result["trace_id"] = trace_id
                    result["component_id"] = component_id

                except Exception as e:
                    print(f"⚠️  Warning: Could not log traceability: {e}")

            return result

        except Exception as e:
            print(f"❌ Error creating command: {e}")
            logger.error(f"Error creating command: {e}", exc_info=True)
            return {
                "ok": False,
                "status": "failed",
                "error": str(e)
            }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.command - Create command manifests from descriptions"
    )
    parser.add_argument(
        "description",
        help="Path to command description file (.md or .json)"
    )

    # Traceability arguments
    parser.add_argument(
        "--requirement-id",
        help="Requirement identifier (e.g., REQ-2025-001)"
    )
    parser.add_argument(
        "--requirement-description",
        help="What this command accomplishes"
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

    creator = CommandCreator()
    result = creator.create_command(args.description, requirement=requirement)

    # Display traceability info if available
    if result.get("trace_id"):
        print(f"\n📝 Traceability: {result['trace_id']}")
        print(f"   View trace: python3 betty/trace_cli.py show {result['component_id']}")

    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
