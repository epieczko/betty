#!/usr/bin/env python3
"""
Atum - Meta-agent that creates other agents

Named after the Egyptian deity who creates by speaking existence into being.
Transforms natural language descriptions into complete, functional agents.
"""

import json
import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)

# Import skill modules directly
agent_compose_path = Path(parent_dir) / "skills" / "agent.compose"
artifact_define_path = Path(parent_dir) / "skills" / "artifact.define"

sys.path.insert(0, str(agent_compose_path))
sys.path.insert(0, str(artifact_define_path))

import agent_compose
import artifact_define


class AgentCreator:
    """Creates agents from natural language descriptions"""

    def __init__(self, registry_path: str = "registry/skills.json"):
        """Initialize with registry path"""
        self.registry_path = Path(registry_path)
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load skills registry"""
        if not self.registry_path.exists():
            raise FileNotFoundError(f"Registry not found: {self.registry_path}")

        with open(self.registry_path) as f:
            return json.load(f)

    def parse_description(self, description_path: str) -> Dict[str, Any]:
        """
        Parse agent description from Markdown or JSON file

        Args:
            description_path: Path to agent_description.md or agent_description.json

        Returns:
            Parsed description with name, purpose, inputs, outputs, constraints
        """
        path = Path(description_path)

        if not path.exists():
            raise FileNotFoundError(f"Description not found: {description_path}")

        # Handle JSON format
        if path.suffix == ".json":
            with open(path) as f:
                return json.load(f)

        # Handle Markdown format
        with open(path) as f:
            content = f.read()

        # Parse Markdown sections
        description = {
            "name": "",
            "purpose": "",
            "inputs": [],
            "outputs": [],
            "constraints": {},
            "examples": []
        }

        current_section = None
        for line in content.split('\n'):
            line = line.strip()

            # Section headers
            if line.startswith('# Name:'):
                description["name"] = line.replace('# Name:', '').strip()
            elif line.startswith('# Purpose:'):
                current_section = "purpose"
            elif line.startswith('# Inputs:'):
                current_section = "inputs"
            elif line.startswith('# Outputs:'):
                current_section = "outputs"
            elif line.startswith('# Constraints:'):
                current_section = "constraints"
            elif line.startswith('# Examples:'):
                current_section = "examples"
            elif line and not line.startswith('#'):
                # Content for current section
                if current_section == "purpose":
                    description["purpose"] += line + " "
                elif current_section == "inputs" and line.startswith('-'):
                    # Extract artifact type (before parentheses or description)
                    artifact = line[1:].strip()
                    # Remove anything in parentheses and any extra description
                    if '(' in artifact:
                        artifact = artifact.split('(')[0].strip()
                    description["inputs"].append(artifact)
                elif current_section == "outputs" and line.startswith('-'):
                    # Extract artifact type (before parentheses or description)
                    artifact = line[1:].strip()
                    # Remove anything in parentheses and any extra description
                    if '(' in artifact:
                        artifact = artifact.split('(')[0].strip()
                    description["outputs"].append(artifact)
                elif current_section == "examples" and line.startswith('-'):
                    description["examples"].append(line[1:].strip())

        description["purpose"] = description["purpose"].strip()
        return description

    def find_compatible_skills(
        self,
        purpose: str,
        required_artifacts: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Find compatible skills for agent purpose

        Args:
            purpose: Natural language description of agent purpose
            required_artifacts: List of artifact types the agent needs

        Returns:
            Dictionary with recommended skills and rationale
        """
        return agent_compose.find_skills_for_purpose(
            self.registry,
            purpose,
            required_artifacts
        )

    def generate_artifact_metadata(
        self,
        inputs: List[str],
        outputs: List[str]
    ) -> Dict[str, Any]:
        """
        Generate artifact metadata from inputs/outputs

        Args:
            inputs: List of input artifact types
            outputs: List of output artifact types

        Returns:
            Artifact metadata structure
        """
        metadata = {}

        if inputs:
            metadata["consumes"] = []
            for input_type in inputs:
                artifact_def = artifact_define.get_artifact_definition(input_type)
                if artifact_def:
                    metadata["consumes"].append(artifact_def)
                else:
                    # Create basic definition
                    metadata["consumes"].append({
                        "type": input_type,
                        "description": f"Input artifact of type {input_type}"
                    })

        if outputs:
            metadata["produces"] = []
            for output_type in outputs:
                artifact_def = artifact_define.get_artifact_definition(output_type)
                if artifact_def:
                    metadata["produces"].append(artifact_def)
                else:
                    # Create basic definition
                    metadata["produces"].append({
                        "type": output_type,
                        "description": f"Output artifact of type {output_type}"
                    })

        return metadata

    def infer_permissions(self, skills: List[str]) -> List[str]:
        """
        Infer required permissions from skills

        Args:
            skills: List of skill names

        Returns:
            List of required permissions
        """
        permissions = set()
        skills_list = self.registry.get("skills", [])

        for skill_name in skills:
            # Find skill in registry
            skill = next(
                (s for s in skills_list if s.get("name") == skill_name),
                None
            )

            if skill and "permissions" in skill:
                for perm in skill["permissions"]:
                    permissions.add(perm)

        return sorted(list(permissions))

    def generate_agent_yaml(
        self,
        name: str,
        description: str,
        skills: List[str],
        artifact_metadata: Dict[str, Any],
        permissions: List[str],
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate agent.yaml content

        Args:
            name: Agent name
            description: Agent description
            skills: List of skill names
            artifact_metadata: Artifact metadata structure
            permissions: List of permissions
            system_prompt: Optional system prompt

        Returns:
            YAML content as string
        """
        agent_def = {
            "name": name,
            "description": description,
            "skills_available": skills,
            "permissions": permissions
        }

        if artifact_metadata:
            agent_def["artifact_metadata"] = artifact_metadata

        if system_prompt:
            agent_def["system_prompt"] = system_prompt

        return yaml.dump(
            agent_def,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True
        )

    def generate_readme(
        self,
        name: str,
        purpose: str,
        skills: List[str],
        inputs: List[str],
        outputs: List[str],
        examples: List[str]
    ) -> str:
        """
        Generate README.md content

        Args:
            name: Agent name
            purpose: Agent purpose
            skills: List of skill names
            inputs: Input artifacts
            outputs: Output artifacts
            examples: Example use cases

        Returns:
            Markdown content
        """
        readme = f"""# {name.title()} Agent

## Purpose

{purpose}

## Skills

This agent uses the following skills:

"""
        for skill in skills:
            readme += f"- `{skill}`\n"

        if inputs or outputs:
            readme += "\n## Artifact Flow\n\n"

            if inputs:
                readme += "### Consumes\n\n"
                for inp in inputs:
                    readme += f"- `{inp}`\n"
                readme += "\n"

            if outputs:
                readme += "### Produces\n\n"
                for out in outputs:
                    readme += f"- `{out}`\n"
                readme += "\n"

        if examples:
            readme += "## Example Use Cases\n\n"
            for example in examples:
                readme += f"- {example}\n"
            readme += "\n"

        readme += """## Usage

```bash
# Activate the agent
/agent {name}

# Or invoke directly
betty agent run {name} --input <path>
```

## Created By

This agent was created by **Atum**, the meta-agent that speaks agents into existence.

---

*Part of the Betty Framework*
""".format(name=name)

        return readme

    def create_agent(
        self,
        description_path: str,
        output_dir: Optional[str] = None,
        validate: bool = True
    ) -> Dict[str, str]:
        """
        Create a complete agent from description

        Args:
            description_path: Path to agent description file
            output_dir: Output directory (default: agents/{name}/)
            validate: Whether to validate with registry.certify

        Returns:
            Dictionary with paths to created files
        """
        # Parse description
        desc = self.parse_description(description_path)
        name = desc["name"]

        if not name:
            raise ValueError("Agent name is required")

        # Determine output directory
        if not output_dir:
            output_dir = f"agents/{name}"

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Find compatible skills
        skill_recommendations = self.find_compatible_skills(
            desc["purpose"],
            desc.get("inputs", []) + desc.get("outputs", [])
        )

        skills = skill_recommendations.get("recommended_skills", [])

        # Generate artifact metadata
        artifact_metadata = self.generate_artifact_metadata(
            desc.get("inputs", []),
            desc.get("outputs", [])
        )

        # Infer permissions
        permissions = self.infer_permissions(skills)

        # Generate agent.yaml
        agent_yaml_content = self.generate_agent_yaml(
            name=name,
            description=desc["purpose"],
            skills=skills,
            artifact_metadata=artifact_metadata,
            permissions=permissions
        )

        agent_yaml_path = output_path / "agent.yaml"
        with open(agent_yaml_path, 'w') as f:
            f.write(agent_yaml_content)

        # Generate README.md
        readme_content = self.generate_readme(
            name=name,
            purpose=desc["purpose"],
            skills=skills,
            inputs=desc.get("inputs", []),
            outputs=desc.get("outputs", []),
            examples=desc.get("examples", [])
        )

        readme_path = output_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)

        return {
            "agent_yaml": str(agent_yaml_path),
            "readme": str(readme_path),
            "name": name,
            "skills": skills,
            "rationale": skill_recommendations.get("rationale", "")
        }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Atum - Create agents from natural language descriptions"
    )
    parser.add_argument(
        "description",
        help="Path to agent description file (.md or .json)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory (default: agents/{name}/)"
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip validation step"
    )

    args = parser.parse_args()

    # Create agent
    creator = AgentCreator()

    print(f"🔮 Atum speaks {args.description} into existence...")

    try:
        result = creator.create_agent(
            args.description,
            output_dir=args.output,
            validate=not args.no_validate
        )

        print(f"\n✨ Agent '{result['name']}' created successfully!\n")
        print(f"📄 Agent definition: {result['agent_yaml']}")
        print(f"📖 Documentation: {result['readme']}\n")
        print(f"🔧 Skills: {', '.join(result['skills'])}\n")

        if result.get("rationale"):
            print(f"💡 Rationale:\n{result['rationale']}\n")

    except Exception as e:
        print(f"\n❌ Error creating agent: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
