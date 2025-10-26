"""
Minimal test coverage for api.* skills (api.define, api.validate, api.compatibility, api.generate-models).
Tests basic functionality and skill manifest validation.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path

from betty.config import BASE_DIR


class TestApiSkillsExistence:
    """Test that all api.* skills exist with required files."""

    def test_api_define_exists(self):
        """Test that api.define skill directory and files exist."""
        skill_dir = os.path.join(BASE_DIR, "skills", "api.define")
        assert os.path.exists(skill_dir), "api.define skill directory not found"
        assert os.path.exists(
            os.path.join(skill_dir, "skill.yaml")
        ), "api.define/skill.yaml not found"
        assert os.path.exists(
            os.path.join(skill_dir, "SKILL.md")
        ), "api.define/SKILL.md not found"
        assert os.path.exists(
            os.path.join(skill_dir, "api_define.py")
        ), "api.define/api_define.py not found"

    def test_api_validate_exists(self):
        """Test that api.validate skill directory and files exist."""
        skill_dir = os.path.join(BASE_DIR, "skills", "api.validate")
        assert os.path.exists(skill_dir), "api.validate skill directory not found"
        assert os.path.exists(
            os.path.join(skill_dir, "skill.yaml")
        ), "api.validate/skill.yaml not found"
        assert os.path.exists(
            os.path.join(skill_dir, "SKILL.md")
        ), "api.validate/SKILL.md not found"
        assert os.path.exists(
            os.path.join(skill_dir, "api_validate.py")
        ), "api.validate/api_validate.py not found"

    def test_api_compatibility_exists(self):
        """Test that api.compatibility skill directory and files exist."""
        skill_dir = os.path.join(BASE_DIR, "skills", "api.compatibility")
        assert os.path.exists(skill_dir), "api.compatibility skill directory not found"
        assert os.path.exists(
            os.path.join(skill_dir, "skill.yaml")
        ), "api.compatibility/skill.yaml not found"
        assert os.path.exists(
            os.path.join(skill_dir, "SKILL.md")
        ), "api.compatibility/SKILL.md not found"
        assert os.path.exists(
            os.path.join(skill_dir, "check_compatibility.py")
        ), "api.compatibility/check_compatibility.py not found"

    def test_api_generate_models_exists(self):
        """Test that api.generate-models skill directory and files exist."""
        skill_dir = os.path.join(BASE_DIR, "skills", "api.generate-models")
        assert (
            os.path.exists(skill_dir)
        ), "api.generate-models skill directory not found"
        assert os.path.exists(
            os.path.join(skill_dir, "skill.yaml")
        ), "api.generate-models/skill.yaml not found"
        assert os.path.exists(
            os.path.join(skill_dir, "SKILL.md")
        ), "api.generate-models/SKILL.md not found"
        assert os.path.exists(
            os.path.join(skill_dir, "modelina_generate.py")
        ), "api.generate-models/modelina_generate.py not found"


class TestApiDefineSkill:
    """Test api.define skill basic functionality."""

    def test_api_define_manifest_valid(self):
        """Test that api.define skill.yaml is valid."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "api.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        assert manifest["name"] == "api.define"
        assert "version" in manifest
        assert "description" in manifest
        assert "inputs" in manifest
        assert "outputs" in manifest
        # Check for either handler or entrypoints
        assert "handler" in manifest or "entrypoints" in manifest

    def test_api_define_handler_imports(self):
        """Test that api.define handler can be imported."""
        from betty.skills.api.define import api_define

        assert hasattr(api_define, "main")

    def test_api_define_has_templates(self):
        """Test that api.define has templates directory."""
        templates_dir = os.path.join(BASE_DIR, "skills", "api.define", "templates")
        assert os.path.exists(templates_dir), "api.define templates directory not found"
        assert os.path.isdir(templates_dir), "api.define templates is not a directory"


class TestApiValidateSkill:
    """Test api.validate skill basic functionality."""

    def test_api_validate_manifest_valid(self):
        """Test that api.validate skill.yaml is valid."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "api.validate", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        assert manifest["name"] == "api.validate"
        assert "version" in manifest
        assert "description" in manifest
        assert "inputs" in manifest
        assert "outputs" in manifest
        # Check for either handler or entrypoints
        assert "handler" in manifest or "entrypoints" in manifest

    def test_api_validate_handler_imports(self):
        """Test that api.validate handler can be imported."""
        from betty.skills.api.validate import api_validate

        assert hasattr(api_validate, "main")

    def test_api_validate_has_validators(self):
        """Test that api.validate has validators directory."""
        validators_dir = os.path.join(
            BASE_DIR, "skills", "api.validate", "validators"
        )
        assert (
            os.path.exists(validators_dir)
        ), "api.validate validators directory not found"
        assert os.path.isdir(
            validators_dir
        ), "api.validate validators is not a directory"

    def test_api_validate_has_zalando_rules(self):
        """Test that api.validate has Zalando rules validator."""
        zalando_rules = os.path.join(
            BASE_DIR, "skills", "api.validate", "validators", "zalando_rules.py"
        )
        assert os.path.exists(
            zalando_rules
        ), "api.validate zalando_rules.py not found"


class TestApiCompatibilitySkill:
    """Test api.compatibility skill basic functionality."""

    def test_api_compatibility_manifest_valid(self):
        """Test that api.compatibility skill.yaml is valid."""
        import yaml

        skill_yaml = os.path.join(
            BASE_DIR, "skills", "api.compatibility", "skill.yaml"
        )
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        assert manifest["name"] == "api.compatibility"
        assert "version" in manifest
        assert "description" in manifest
        assert "inputs" in manifest
        assert "outputs" in manifest
        # Check for either handler or entrypoints
        assert "handler" in manifest or "entrypoints" in manifest

    def test_api_compatibility_handler_imports(self):
        """Test that api.compatibility handler can be imported."""
        from betty.skills.api.compatibility import check_compatibility

        assert hasattr(check_compatibility, "main")


class TestApiGenerateModelsSkill:
    """Test api.generate-models skill basic functionality."""

    def test_api_generate_models_manifest_valid(self):
        """Test that api.generate-models skill.yaml is valid."""
        import yaml

        skill_yaml = os.path.join(
            BASE_DIR, "skills", "api.generate-models", "skill.yaml"
        )
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        assert manifest["name"] == "api.generate-models"
        assert "version" in manifest
        assert "description" in manifest
        assert "inputs" in manifest
        assert "outputs" in manifest
        # Check for either handler or entrypoints
        assert "handler" in manifest or "entrypoints" in manifest

    def test_api_generate_models_handler_imports(self):
        """Test that api.generate-models handler can be imported."""
        from betty.skills.api.generatemodels import modelina_generate

        assert hasattr(modelina_generate, "main")


class TestApiSkillsIntegration:
    """Integration tests for api.* skills working together."""

    def test_all_api_skills_in_registry(self):
        """Test that all api.* skills are registered in the skill registry."""
        from betty.config import REGISTRY_FILE

        with open(REGISTRY_FILE) as f:
            registry = json.load(f)

        skill_names = [skill["name"] for skill in registry["skills"]]

        assert "api.define" in skill_names, "api.define not in skill registry"
        assert "api.validate" in skill_names, "api.validate not in skill registry"
        assert (
            "api.compatibility" in skill_names
        ), "api.compatibility not in skill registry"
        assert (
            "api.generate-models" in skill_names
        ), "api.generate-models not in skill registry"

    def test_api_agents_reference_api_skills(self):
        """Test that api agents reference the correct api skills."""
        import yaml

        # Test api.designer agent
        designer_yaml = os.path.join(BASE_DIR, "agents", "api.designer", "agent.yaml")
        if os.path.exists(designer_yaml):
            with open(designer_yaml) as f:
                designer = yaml.safe_load(f)

            skills = designer.get("skills_available", [])
            assert "api.define" in skills or "api.validate" in skills, \
                "api.designer should reference api skills"

        # Test api.analyzer agent
        analyzer_yaml = os.path.join(BASE_DIR, "agents", "api.analyzer", "agent.yaml")
        if os.path.exists(analyzer_yaml):
            with open(analyzer_yaml) as f:
                analyzer = yaml.safe_load(f)

            skills = analyzer.get("skills_available", [])
            assert "api.compatibility" in skills or "api.validate" in skills, \
                "api.analyzer should reference api skills"

    def test_api_skills_have_consistent_structure(self):
        """Test that all api.* skills follow consistent naming/structure."""
        api_skills = ["api.define", "api.validate", "api.compatibility", "api.generate-models"]

        for skill_name in api_skills:
            skill_dir = os.path.join(BASE_DIR, "skills", skill_name)
            assert os.path.exists(skill_dir), f"{skill_name} directory not found"

            # Check for skill.yaml
            skill_yaml = os.path.join(skill_dir, "skill.yaml")
            assert os.path.exists(skill_yaml), f"{skill_name}/skill.yaml not found"

            # Check for SKILL.md
            skill_md = os.path.join(skill_dir, "SKILL.md")
            assert os.path.exists(skill_md), f"{skill_name}/SKILL.md not found"

            # Verify skill.yaml name matches directory
            import yaml
            with open(skill_yaml) as f:
                manifest = yaml.safe_load(f)
            assert manifest["name"] == skill_name, \
                f"{skill_name} manifest name mismatch"


class TestApiSkillsDocumentation:
    """Test documentation quality for api.* skills."""

    def test_api_skills_have_comprehensive_docs(self):
        """Test that all api.* skills have comprehensive documentation."""
        api_skills = ["api.define", "api.validate", "api.compatibility", "api.generate-models"]

        for skill_name in api_skills:
            skill_md = os.path.join(BASE_DIR, "skills", skill_name, "SKILL.md")
            with open(skill_md) as f:
                content = f.read()

            # Check for key documentation sections
            assert len(content) > 100, f"{skill_name} documentation is too short"
            assert "#" in content, f"{skill_name} missing markdown headers"

    def test_api_skills_have_usage_examples(self):
        """Test that api.* skill docs contain usage information."""
        api_skills = ["api.define", "api.validate", "api.compatibility", "api.generate-models"]

        for skill_name in api_skills:
            skill_md = os.path.join(BASE_DIR, "skills", skill_name, "SKILL.md")
            with open(skill_md) as f:
                content = f.read().lower()

            # Check for usage-related keywords
            has_usage_info = (
                "usage" in content
                or "example" in content
                or "how to" in content
                or "input" in content
            )
            assert has_usage_info, f"{skill_name} missing usage information in docs"
