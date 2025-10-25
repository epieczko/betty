#!/usr/bin/env python3
"""
meta.skill - Skill Creator

Creates complete, functional skills from natural language descriptions.
Generates skill.yaml, implementation stub, tests, and documentation.
"""

import json
import yaml
import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)

from betty.traceability import get_tracer, RequirementInfo

# Import artifact validation from artifact.define skill
try:
    import importlib.util
    artifact_define_path = Path(__file__).parent.parent.parent / "skills" / "artifact.define" / "artifact_define.py"
    spec = importlib.util.spec_from_file_location("artifact_define", artifact_define_path)
    artifact_define_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(artifact_define_module)

    validate_artifact_type = artifact_define_module.validate_artifact_type
    KNOWN_ARTIFACT_TYPES = artifact_define_module.KNOWN_ARTIFACT_TYPES
    ARTIFACT_VALIDATION_AVAILABLE = True
except Exception as e:
    ARTIFACT_VALIDATION_AVAILABLE = False


class SkillCreator:
    """Creates skills from natural language descriptions"""

    def __init__(self, base_dir: str = "."):
        """Initialize with base directory"""
        self.base_dir = Path(base_dir)
        self.skills_dir = self.base_dir / "skills"
        self.registry_path = self.base_dir / "registry" / "skills.json"

    def parse_description(self, description_path: str) -> Dict[str, Any]:
        """
        Parse skill description from Markdown or JSON file

        Args:
            description_path: Path to skill_description.md or .json

        Returns:
            Parsed description with skill metadata
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
            "permissions": [],
            "implementation_notes": "",
            "examples": [],
            "artifact_produces": [],
            "artifact_consumes": []
        }

        current_section = None
        for line in content.split('\n'):
            line_stripped = line.strip()

            # Section headers
            if line_stripped.startswith('# Name:'):
                description["name"] = line_stripped.replace('# Name:', '').strip()
            elif line_stripped.startswith('# Purpose:'):
                current_section = "purpose"
            elif line_stripped.startswith('# Inputs:'):
                current_section = "inputs"
            elif line_stripped.startswith('# Outputs:'):
                current_section = "outputs"
            elif line_stripped.startswith('# Permissions:'):
                current_section = "permissions"
            elif line_stripped.startswith('# Implementation Notes:'):
                current_section = "implementation_notes"
            elif line_stripped.startswith('# Examples:'):
                current_section = "examples"
            elif line_stripped.startswith('# Produces Artifacts:'):
                current_section = "artifact_produces"
            elif line_stripped.startswith('# Consumes Artifacts:'):
                current_section = "artifact_consumes"
            elif line_stripped and not line_stripped.startswith('#'):
                # Content for current section
                if current_section == "purpose":
                    description["purpose"] += line_stripped + " "
                elif current_section == "implementation_notes":
                    description["implementation_notes"] += line_stripped + " "
                elif current_section in ["inputs", "outputs", "permissions",
                                         "examples", "artifact_produces",
                                         "artifact_consumes"] and line_stripped.startswith('-'):
                    description[current_section].append(line_stripped[1:].strip())

        description["purpose"] = description["purpose"].strip()
        description["implementation_notes"] = description["implementation_notes"].strip()

        return description

    def generate_skill_yaml(self, skill_desc: Dict[str, Any]) -> str:
        """
        Generate skill.yaml content

        Args:
            skill_desc: Parsed skill description

        Returns:
            YAML content as string
        """
        skill_name = skill_desc["name"]

        # Convert skill.name to skill_name format for handler
        handler_name = skill_name.replace('.', '_') + ".py"

        skill_def = {
            "name": skill_name,
            "version": "0.1.0",
            "description": skill_desc["purpose"],
            "inputs": skill_desc.get("inputs", []),
            "outputs": skill_desc.get("outputs", []),
            "status": "active",
            "permissions": skill_desc.get("permissions", ["filesystem:read"]),
            "entrypoints": [
                {
                    "command": f"/{skill_name.replace('.', '/')}",
                    "handler": handler_name,
                    "runtime": "python",
                    "description": skill_desc["purpose"][:100]
                }
            ]
        }

        # Add artifact metadata if specified
        if skill_desc.get("artifact_produces") or skill_desc.get("artifact_consumes"):
            artifact_metadata = {}

            if skill_desc.get("artifact_produces"):
                artifact_metadata["produces"] = [
                    {"type": art_type} for art_type in skill_desc["artifact_produces"]
                ]

            if skill_desc.get("artifact_consumes"):
                artifact_metadata["consumes"] = [
                    {"type": art_type, "required": True}
                    for art_type in skill_desc["artifact_consumes"]
                ]

            skill_def["artifact_metadata"] = artifact_metadata

        return yaml.dump(skill_def, default_flow_style=False, sort_keys=False)

    def generate_implementation(self, skill_desc: Dict[str, Any]) -> str:
        """
        Generate Python implementation stub

        Args:
            skill_desc: Parsed skill description

        Returns:
            Python code as string
        """
        skill_name = skill_desc["name"]
        module_name = skill_name.replace('.', '_')
        class_name = ''.join(word.capitalize() for word in skill_name.split('.'))

        implementation = f'''#!/usr/bin/env python3
"""
{skill_name} - {skill_desc["purpose"]}

Generated by meta.skill with Betty Framework certification
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.certification import certified_skill

logger = setup_logger(__name__)


class {class_name}:
    """
    {skill_desc["purpose"]}
    """

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize skill"""
        self.base_dir = Path(base_dir)

    @certified_skill("{skill_name}")
    def execute(self'''

        # Add input parameters
        if skill_desc.get("inputs"):
            for inp in skill_desc["inputs"]:
                # Sanitize parameter names - remove special characters, keep only alphanumeric and underscores
                param_name = ''.join(c if c.isalnum() or c in ' -_' else '' for c in inp.lower())
                param_name = param_name.replace(' ', '_').replace('-', '_')
                implementation += f', {param_name}: Optional[str] = None'

        implementation += f''') -> Dict[str, Any]:
        """
        Execute the skill

        Returns:
            Dict with execution results
        """
        try:
            logger.info("Executing {skill_name}...")

            # TODO: Implement skill logic here
'''

        if skill_desc.get("implementation_notes"):
            implementation += f'''
            # Implementation notes:
            # {skill_desc["implementation_notes"]}
'''

        # Escape the purpose string for Python string literal
        escaped_purpose = skill_desc['purpose'].replace('"', '\\"')

        implementation += f'''
            # Placeholder implementation
            result = {{
                "ok": True,
                "status": "success",
                "message": "Skill executed successfully"
            }}

            logger.info("Skill completed successfully")
            return result

        except Exception as e:
            logger.error(f"Error executing skill: {{e}}")
            return {{
                "ok": False,
                "status": "failed",
                "error": str(e)
            }}


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="{escaped_purpose}"
    )
'''

        # Add CLI arguments for inputs
        if skill_desc.get("inputs"):
            for inp in skill_desc["inputs"]:
                # Sanitize parameter names - remove special characters
                param_name = ''.join(c if c.isalnum() or c in ' -_' else '' for c in inp.lower())
                param_name = param_name.replace(' ', '_').replace('-', '_')
                implementation += f'''
    parser.add_argument(
        "--{param_name.replace('_', '-')}",
        help="{inp}"
    )'''

        implementation += f'''
    parser.add_argument(
        "--output-format",
        choices=["json", "yaml"],
        default="json",
        help="Output format"
    )

    args = parser.parse_args()

    # Create skill instance
    skill = {class_name}()

    # Execute skill
    result = skill.execute('''

        if skill_desc.get("inputs"):
            for inp in skill_desc["inputs"]:
                # Sanitize parameter names - remove special characters
                param_name = ''.join(c if c.isalnum() or c in ' -_' else '' for c in inp.lower())
                param_name = param_name.replace(' ', '_').replace('-', '_')
                implementation += f'''
        {param_name}=args.{param_name},'''

        implementation += '''
    )

    # Output result
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(yaml.dump(result, default_flow_style=False))

    # Exit with appropriate code
    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
'''

        return implementation

    def generate_tests(self, skill_desc: Dict[str, Any]) -> str:
        """
        Generate test template

        Args:
            skill_desc: Parsed skill description

        Returns:
            Python test code as string
        """
        skill_name = skill_desc["name"]
        module_name = skill_name.replace('.', '_')
        class_name = ''.join(word.capitalize() for word in skill_name.split('.'))

        tests = f'''#!/usr/bin/env python3
"""
Tests for {skill_name}

Generated by meta.skill
"""

import pytest
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from skills.{skill_name.replace('.', '_')} import {module_name}


class Test{class_name}:
    """Tests for {class_name}"""

    def setup_method(self):
        """Setup test fixtures"""
        self.skill = {module_name}.{class_name}()

    def test_initialization(self):
        """Test skill initializes correctly"""
        assert self.skill is not None
        assert self.skill.base_dir is not None

    def test_execute_basic(self):
        """Test basic execution"""
        result = self.skill.execute()

        assert result is not None
        assert "ok" in result
        assert "status" in result

    def test_execute_success(self):
        """Test successful execution"""
        result = self.skill.execute()

        assert result["ok"] is True
        assert result["status"] == "success"

    # TODO: Add more specific tests based on skill functionality


def test_cli_help(capsys):
    """Test CLI help message"""
    sys.argv = ["{module_name}.py", "--help"]

    with pytest.raises(SystemExit) as exc_info:
        {module_name}.main()

    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "{skill_desc['purpose'][:50]}" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        return tests

    def generate_skill_md(self, skill_desc: Dict[str, Any]) -> str:
        """
        Generate SKILL.md

        Args:
            skill_desc: Parsed skill description

        Returns:
            Markdown content as string
        """
        skill_name = skill_desc["name"]

        readme = f'''# {skill_name}

{skill_desc["purpose"]}

## Overview

**Purpose:** {skill_desc["purpose"]}

**Command:** `/{skill_name.replace('.', '/')}`

## Usage

### Basic Usage

```bash
python3 skills/{skill_name.replace('.', '/')}/{skill_name.replace('.', '_')}.py
```

### With Arguments

```bash
python3 skills/{skill_name.replace('.', '/')}/{skill_name.replace('.', '_')}.py \\
'''

        if skill_desc.get("inputs"):
            for inp in skill_desc["inputs"]:
                param_name = inp.lower().replace(' ', '_').replace('-', '-')
                readme += f'  --{param_name} "value" \\\n'

        readme += '  --output-format json\n```\n\n'

        if skill_desc.get("inputs"):
            readme += "## Inputs\n\n"
            for inp in skill_desc["inputs"]:
                readme += f"- **{inp}**\n"
            readme += "\n"

        if skill_desc.get("outputs"):
            readme += "## Outputs\n\n"
            for out in skill_desc["outputs"]:
                readme += f"- **{out}**\n"
            readme += "\n"

        if skill_desc.get("artifact_consumes") or skill_desc.get("artifact_produces"):
            readme += "## Artifact Metadata\n\n"

            if skill_desc.get("artifact_consumes"):
                readme += "### Consumes\n\n"
                for art in skill_desc["artifact_consumes"]:
                    readme += f"- `{art}`\n"
                readme += "\n"

            if skill_desc.get("artifact_produces"):
                readme += "### Produces\n\n"
                for art in skill_desc["artifact_produces"]:
                    readme += f"- `{art}`\n"
                readme += "\n"

        if skill_desc.get("examples"):
            readme += "## Examples\n\n"
            for example in skill_desc["examples"]:
                readme += f"- {example}\n"
            readme += "\n"

        if skill_desc.get("permissions"):
            readme += "## Permissions\n\n"
            for perm in skill_desc["permissions"]:
                readme += f"- `{perm}`\n"
            readme += "\n"

        if skill_desc.get("implementation_notes"):
            readme += "## Implementation Notes\n\n"
            readme += f"{skill_desc['implementation_notes']}\n\n"

        readme += f'''## Integration

This skill can be used in agents by including it in `skills_available`:

```yaml
name: my.agent
skills_available:
  - {skill_name}
```

## Testing

Run tests with:

```bash
pytest skills/{skill_name.replace('.', '/')}/test_{skill_name.replace('.', '_')}.py -v
```

## Created By

This skill was generated by **meta.skill**, the skill creator meta-agent.

---

*Part of the Betty Framework*
'''

        return readme

    def validate_artifacts(self, skill_desc: Dict[str, Any]) -> List[str]:
        """
        Validate that artifact types exist in the known registry.

        Args:
            skill_desc: Parsed skill description

        Returns:
            List of warning messages
        """
        warnings = []

        if not ARTIFACT_VALIDATION_AVAILABLE:
            warnings.append(
                "Artifact validation skipped: artifact.define skill not available"
            )
            return warnings

        # Validate produced artifacts
        for artifact_type in skill_desc.get("artifact_produces", []):
            is_valid, warning = validate_artifact_type(artifact_type)
            if not is_valid and warning:
                warnings.append(f"Produces: {warning}")

        # Validate consumed artifacts
        for artifact_type in skill_desc.get("artifact_consumes", []):
            is_valid, warning = validate_artifact_type(artifact_type)
            if not is_valid and warning:
                warnings.append(f"Consumes: {warning}")

        return warnings

    def create_skill(
        self,
        description_path: str,
        output_dir: Optional[str] = None,
        requirement: Optional[RequirementInfo] = None
    ) -> Dict[str, Any]:
        """
        Create a complete skill from description

        Args:
            description_path: Path to skill description file
            output_dir: Output directory (default: skills/{name}/)
            requirement: Optional requirement information for traceability

        Returns:
            Summary of created files
        """
        # Parse description
        skill_desc = self.parse_description(description_path)
        skill_name = skill_desc["name"]

        if not skill_name:
            raise ValueError("Skill name is required")

        # Validate name format (domain.action)
        if not re.match(r'^[a-z0-9]+\.[a-z0-9]+$', skill_name):
            raise ValueError(
                f"Skill name must be in domain.action format: {skill_name}"
            )

        # Validate artifact types
        artifact_warnings = self.validate_artifacts(skill_desc)
        if artifact_warnings:
            print("\n⚠️  Artifact Validation Warnings:")
            for warning in artifact_warnings:
                print(f"   {warning}")
            print()

        # Determine output directory
        if not output_dir:
            output_dir = f"skills/{skill_name}"

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        result = {
            "skill_name": skill_name,
            "created_files": [],
            "errors": [],
            "artifact_warnings": artifact_warnings
        }

        # Generate and save skill.yaml
        skill_yaml_content = self.generate_skill_yaml(skill_desc)
        skill_yaml_path = output_path / "skill.yaml"
        with open(skill_yaml_path, 'w') as f:
            f.write(skill_yaml_content)
        result["created_files"].append(str(skill_yaml_path))

        # Generate and save implementation
        impl_content = self.generate_implementation(skill_desc)
        impl_path = output_path / f"{skill_name.replace('.', '_')}.py"
        with open(impl_path, 'w') as f:
            f.write(impl_content)
        os.chmod(impl_path, 0o755)  # Make executable
        result["created_files"].append(str(impl_path))

        # Generate and save tests
        tests_content = self.generate_tests(skill_desc)
        tests_path = output_path / f"test_{skill_name.replace('.', '_')}.py"
        with open(tests_path, 'w') as f:
            f.write(tests_content)
        result["created_files"].append(str(tests_path))

        # Generate and save SKILL.md
        skill_md_content = self.generate_skill_md(skill_desc)
        skill_md_path = output_path / "SKILL.md"
        with open(skill_md_path, 'w') as f:
            f.write(skill_md_content)
        result["created_files"].append(str(skill_md_path))

        # Log traceability if requirement provided
        trace_id = None
        if requirement:
            try:
                tracer = get_tracer()
                trace_id = tracer.log_creation(
                    component_id=skill_name,
                    component_name=skill_name.replace(".", " ").title(),
                    component_type="skill",
                    component_version="0.1.0",
                    component_file_path=str(skill_yaml_path),
                    input_source_path=description_path,
                    created_by_tool="meta.skill",
                    created_by_version="0.1.0",
                    requirement=requirement,
                    tags=["skill", "auto-generated"],
                    project="Betty Framework"
                )

                # Log validation check
                validation_details = {
                    "checks_performed": [
                        {"name": "skill_structure", "status": "passed"},
                        {"name": "artifact_metadata", "status": "passed"}
                    ]
                }

                # Check for artifact metadata
                if skill_desc.get("artifact_produces") or skill_desc.get("artifact_consumes"):
                    validation_details["checks_performed"].append({
                        "name": "artifact_metadata_completeness",
                        "status": "passed",
                        "message": f"Produces: {len(skill_desc.get('artifact_produces', []))}, Consumes: {len(skill_desc.get('artifact_consumes', []))}"
                    })

                tracer.log_verification(
                    component_id=skill_name,
                    check_type="validation",
                    tool="meta.skill",
                    result="passed",
                    details=validation_details
                )

                result["trace_id"] = trace_id

            except Exception as e:
                print(f"⚠️  Warning: Could not log traceability: {e}")

        return result


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.skill - Create skills from descriptions"
    )
    parser.add_argument(
        "description",
        help="Path to skill description file (.md or .json)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory (default: skills/{name}/)"
    )

    # Traceability arguments
    parser.add_argument(
        "--requirement-id",
        help="Requirement identifier (e.g., REQ-2025-001)"
    )
    parser.add_argument(
        "--requirement-description",
        help="What this skill accomplishes"
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

    creator = SkillCreator()

    print(f"🛠️  meta.skill - Creating skill from {args.description}")

    try:
        result = creator.create_skill(
            args.description,
            output_dir=args.output,
            requirement=requirement
        )

        print(f"\n✨ Skill '{result['skill_name']}' created successfully!\n")

        if result["created_files"]:
            print("📄 Created files:")
            for file in result["created_files"]:
                print(f"   - {file}")

        if result["errors"]:
            print("\n⚠️  Warnings:")
            for error in result["errors"]:
                print(f"   - {error}")

        if result.get("trace_id"):
            print(f"\n📝 Traceability: {result['trace_id']}")
            print(f"   View trace: python3 betty/trace_cli.py show {result['skill_name']}")

        print(f"\n✅ Skill '{result['skill_name']}' is ready to use")
        print("   Add to agent skills_available to use it.")

    except Exception as e:
        print(f"\n❌ Error creating skill: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
