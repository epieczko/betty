"""
Minimal test coverage for command.define skill itself.
Note: test_commands.py contains comprehensive tests for command validation logic.
This file tests the command.define skill manifest and basic structure.
"""

import os
import json
import pytest

from betty.config import BASE_DIR


class TestCommandDefineSkillExistence:
    """Test that command.define skill exists with required files."""

    def test_command_define_directory_exists(self):
        """Test that command.define skill directory exists."""
        skill_dir = os.path.join(BASE_DIR, "skills", "command.define")
        assert os.path.exists(skill_dir), "command.define skill directory not found"
        assert os.path.isdir(skill_dir), "command.define is not a directory"

    def test_command_define_skill_yaml_exists(self):
        """Test that command.define/skill.yaml exists."""
        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        assert os.path.exists(skill_yaml), "command.define/skill.yaml not found"

    def test_command_define_skill_md_exists(self):
        """Test that command.define/SKILL.md exists."""
        skill_md = os.path.join(BASE_DIR, "skills", "command.define", "SKILL.md")
        assert os.path.exists(skill_md), "command.define/SKILL.md not found"

    def test_command_define_handler_exists(self):
        """Test that command.define/command_define.py exists."""
        handler = os.path.join(
            BASE_DIR, "skills", "command.define", "command_define.py"
        )
        assert os.path.exists(handler), "command.define/command_define.py not found"


class TestCommandDefineSkillManifest:
    """Test command.define skill manifest structure."""

    def test_command_define_manifest_valid(self):
        """Test that command.define skill.yaml is valid."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        assert manifest is not None, "Failed to load command.define skill.yaml"
        assert manifest["name"] == "command.define", "Incorrect skill name"
        assert "version" in manifest, "Missing version field"
        assert "description" in manifest, "Missing description field"
        assert "inputs" in manifest, "Missing inputs field"
        assert "outputs" in manifest, "Missing outputs field"
        # Check for either handler or entrypoints
        assert "handler" in manifest or "entrypoints" in manifest, "Missing handler/entrypoints field"

    def test_command_define_has_version(self):
        """Test that command.define has a valid semantic version."""
        import yaml
        import re

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        version = manifest.get("version", "")
        semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
        assert semver_pattern.match(version), f"Invalid semantic version: {version}"

    def test_command_define_has_description(self):
        """Test that command.define has a non-empty description."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        description = manifest.get("description", "").strip()
        assert len(description) > 0, "Empty description"
        assert len(description) > 10, "Description too short"


class TestCommandDefineSkillHandler:
    """Test command.define skill handler."""

    def test_command_define_handler_imports(self):
        """Test that command_define.py can be imported."""
        from betty.skills.command.define import command_define

        assert hasattr(command_define, "main"), "Missing main function"
        assert hasattr(
            command_define, "validate_manifest"
        ), "Missing validate_manifest function"
        assert hasattr(
            command_define, "load_command_manifest"
        ), "Missing load_command_manifest function"
        assert hasattr(
            command_define, "update_command_registry"
        ), "Missing update_command_registry function"

    def test_command_define_has_custom_errors(self):
        """Test that command_define defines custom error classes."""
        from betty.skills.command.define import command_define

        assert hasattr(
            command_define, "CommandValidationError"
        ), "Missing CommandValidationError"
        assert hasattr(
            command_define, "CommandRegistryError"
        ), "Missing CommandRegistryError"


class TestCommandDefineSkillDocumentation:
    """Test command.define skill documentation."""

    def test_command_define_skill_md_not_empty(self):
        """Test that command.define SKILL.md is not empty."""
        skill_md = os.path.join(BASE_DIR, "skills", "command.define", "SKILL.md")
        with open(skill_md) as f:
            content = f.read().strip()

        assert len(content) > 0, "SKILL.md is empty"
        assert len(content) > 100, "SKILL.md is too short"

    def test_command_define_skill_md_has_header(self):
        """Test that command.define SKILL.md has a header."""
        skill_md = os.path.join(BASE_DIR, "skills", "command.define", "SKILL.md")
        with open(skill_md) as f:
            content = f.read()

        # Check for markdown header anywhere in first 500 chars
        assert "#" in content[:500], "SKILL.md missing markdown header"

    def test_command_define_skill_md_has_usage_info(self):
        """Test that command.define SKILL.md contains usage information."""
        skill_md = os.path.join(BASE_DIR, "skills", "command.define", "SKILL.md")
        with open(skill_md) as f:
            content = f.read().lower()

        # Check for usage-related keywords
        has_usage_info = (
            "usage" in content
            or "example" in content
            or "how to" in content
            or "input" in content
            or "command" in content
        )
        assert has_usage_info, "SKILL.md missing usage information"


class TestCommandDefineSkillRegistry:
    """Test command.define skill registry integration."""

    def test_command_define_in_skill_registry(self):
        """Test that command.define is registered in the skill registry."""
        from betty.config import REGISTRY_FILE

        with open(REGISTRY_FILE) as f:
            registry = json.load(f)

        skill_names = [skill["name"] for skill in registry["skills"]]
        assert "command.define" in skill_names, "command.define not in skill registry"

    def test_command_define_registry_entry_valid(self):
        """Test that command.define registry entry is valid."""
        from betty.config import REGISTRY_FILE

        with open(REGISTRY_FILE) as f:
            registry = json.load(f)

        command_define = next(
            (skill for skill in registry["skills"] if skill["name"] == "command.define"),
            None,
        )

        assert command_define is not None, "command.define not found in registry"
        assert "version" in command_define, "Missing version in registry entry"
        assert "description" in command_define, "Missing description in registry entry"
        # Check for either handler or entrypoints
        assert "handler" in command_define or "entrypoints" in command_define, "Missing handler/entrypoints in registry entry"


class TestCommandDefineSkillInputsOutputs:
    """Test command.define skill inputs and outputs."""

    def test_command_define_has_valid_inputs(self):
        """Test that command.define has valid input specifications."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        inputs = manifest.get("inputs", [])
        assert len(inputs) > 0, "No inputs defined"

        # Check that each input has required fields
        for input_spec in inputs:
            assert "name" in input_spec, "Input missing name field"
            assert "type" in input_spec, "Input missing type field"

    def test_command_define_has_valid_outputs(self):
        """Test that command.define has valid output specifications."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        outputs = manifest.get("outputs", [])
        assert len(outputs) > 0, "No outputs defined"

        # Check that each output has required fields
        for output_spec in outputs:
            assert "name" in output_spec, "Output missing name field"
            assert "type" in output_spec, "Output missing type field"

    def test_command_define_handler_points_to_file(self):
        """Test that command.define handler field points to existing file."""
        import yaml

        skill_yaml = os.path.join(BASE_DIR, "skills", "command.define", "skill.yaml")
        with open(skill_yaml) as f:
            manifest = yaml.safe_load(f)

        handler = manifest.get("handler", "")
        handler_path = os.path.join(BASE_DIR, "skills", "command.define", handler)
        assert os.path.exists(handler_path), f"Handler file not found: {handler}"
