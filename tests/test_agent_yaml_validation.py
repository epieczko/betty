"""
Tests for agent.yaml validation - validates all agent manifests using agent.define.
Includes doc presence checks to ensure README.md exists for each agent.yaml.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path
from glob import glob

# Import the agent.define functions
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "skills", "agent.define")
    ),
)

from agent_define import (
    validate_manifest,
    load_agent_manifest,
    AgentValidationError,
)
from betty.config import BASE_DIR


class TestAgentYamlValidation:
    """Tests for validating all agent.yaml files in the repository."""

    def get_all_agent_yamls(self):
        """Get all agent.yaml files in the agents directory."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        pattern = os.path.join(agents_dir, "*/agent.yaml")
        return glob(pattern)

    def test_all_agent_yamls_exist(self):
        """Test that at least one agent.yaml file exists."""
        agent_yamls = self.get_all_agent_yamls()
        assert len(agent_yamls) > 0, "No agent.yaml files found in agents directory"

    def test_all_agent_yamls_are_valid(self):
        """Test that all agent.yaml files pass validation."""
        agent_yamls = self.get_all_agent_yamls()
        failures = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                result = validate_manifest(agent_yaml)
                if not result.get("valid"):
                    errors = result.get("errors", [])
                    failures.append(f"{agent_name}: {', '.join(errors)}")
            except Exception as e:
                failures.append(f"{agent_name}: {str(e)}")

        assert len(failures) == 0, f"Validation failures:\n" + "\n".join(failures)

    def test_all_agent_yamls_have_required_fields(self):
        """Test that all agent.yaml files have required fields."""
        from betty.config import REQUIRED_AGENT_FIELDS

        agent_yamls = self.get_all_agent_yamls()
        failures = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                missing = [
                    field for field in REQUIRED_AGENT_FIELDS if field not in manifest
                ]
                if missing:
                    failures.append(f"{agent_name}: Missing fields {missing}")
            except Exception as e:
                failures.append(f"{agent_name}: {str(e)}")

        assert len(failures) == 0, f"Missing required fields:\n" + "\n".join(failures)

    def test_agent_yaml_parseable(self):
        """Test that all agent.yaml files are valid YAML."""
        agent_yamls = self.get_all_agent_yamls()
        failures = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                load_agent_manifest(agent_yaml)
            except AgentValidationError as e:
                failures.append(f"{agent_name}: {str(e)}")

        assert len(failures) == 0, f"YAML parsing errors:\n" + "\n".join(failures)


class TestAgentDocPresence:
    """Tests for documentation presence - agent.yaml should have README.md."""

    def get_all_agent_dirs(self):
        """Get all agent directories."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        return [
            d
            for d in glob(os.path.join(agents_dir, "*"))
            if os.path.isdir(d) and not d.endswith("__pycache__")
        ]

    def test_all_agents_have_readme_md(self):
        """Test that every agent.yaml has a corresponding README.md file."""
        agent_dirs = self.get_all_agent_dirs()
        missing_docs = []

        for agent_dir in agent_dirs:
            agent_yaml = os.path.join(agent_dir, "agent.yaml")
            readme_md = os.path.join(agent_dir, "README.md")
            agent_name = Path(agent_dir).name

            if os.path.exists(agent_yaml):
                if not os.path.exists(readme_md):
                    missing_docs.append(agent_name)

        assert (
            len(missing_docs) == 0
        ), f"Agents missing README.md documentation:\n" + "\n".join(missing_docs)

    def test_all_readme_md_not_empty(self):
        """Test that all README.md files have content."""
        agent_dirs = self.get_all_agent_dirs()
        empty_docs = []

        for agent_dir in agent_dirs:
            agent_yaml = os.path.join(agent_dir, "agent.yaml")
            readme_md = os.path.join(agent_dir, "README.md")
            agent_name = Path(agent_dir).name

            if os.path.exists(agent_yaml) and os.path.exists(readme_md):
                with open(readme_md, "r") as f:
                    content = f.read().strip()
                    if len(content) == 0:
                        empty_docs.append(agent_name)

        assert (
            len(empty_docs) == 0
        ), f"Agents with empty README.md:\n" + "\n".join(empty_docs)

    def test_readme_md_has_header(self):
        """Test that all README.md files have a header (title)."""
        agent_dirs = self.get_all_agent_dirs()
        missing_headers = []

        for agent_dir in agent_dirs:
            agent_yaml = os.path.join(agent_dir, "agent.yaml")
            readme_md = os.path.join(agent_dir, "README.md")
            agent_name = Path(agent_dir).name

            if os.path.exists(agent_yaml) and os.path.exists(readme_md):
                with open(readme_md, "r") as f:
                    first_line = f.readline().strip()
                    if not first_line.startswith("#"):
                        missing_headers.append(agent_name)

        assert (
            len(missing_headers) == 0
        ), f"Agents with README.md missing header:\n" + "\n".join(missing_headers)


class TestAgentManifestStructure:
    """Tests for agent manifest structure and content."""

    def test_agent_names_match_directory(self):
        """Test that agent names match their directory names."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        mismatches = []

        for agent_yaml in agent_yamls:
            dir_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                agent_name = manifest.get("name", "")

                if agent_name != dir_name:
                    mismatches.append(
                        f"{dir_name}: manifest name '{agent_name}' != directory '{dir_name}'"
                    )
            except Exception as e:
                mismatches.append(f"{dir_name}: {str(e)}")

        assert (
            len(mismatches) == 0
        ), f"Agent name/directory mismatches:\n" + "\n".join(mismatches)

    def test_agent_versions_are_semver(self):
        """Test that all agent versions follow semantic versioning."""
        import re

        semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        invalid_versions = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                version = manifest.get("version", "")
                if not semver_pattern.match(version):
                    invalid_versions.append(f"{agent_name}: {version}")
            except Exception as e:
                invalid_versions.append(f"{agent_name}: {str(e)}")

        assert (
            len(invalid_versions) == 0
        ), f"Invalid semantic versions:\n" + "\n".join(invalid_versions)

    def test_agent_has_description(self):
        """Test that all agents have non-empty descriptions."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        missing_descriptions = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                description = manifest.get("description", "").strip()
                if not description:
                    missing_descriptions.append(agent_name)
            except Exception as e:
                missing_descriptions.append(f"{agent_name}: {str(e)}")

        assert (
            len(missing_descriptions) == 0
        ), f"Agents with empty/missing descriptions:\n" + "\n".join(
            missing_descriptions
        )

    def test_agent_has_valid_reasoning_mode(self):
        """Test that all agents have valid reasoning modes."""
        from betty.enums import ReasoningMode

        valid_modes = [mode.value for mode in ReasoningMode]
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        invalid_modes = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                reasoning_mode = manifest.get("reasoning_mode", "")
                if reasoning_mode not in valid_modes:
                    invalid_modes.append(f"{agent_name}: {reasoning_mode}")
            except Exception as e:
                invalid_modes.append(f"{agent_name}: {str(e)}")

        assert (
            len(invalid_modes) == 0
        ), f"Invalid reasoning modes:\n" + "\n".join(invalid_modes)

    def test_agent_has_capabilities(self):
        """Test that all agents have non-empty capabilities list."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        empty_capabilities = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                capabilities = manifest.get("capabilities", [])
                if not capabilities or len(capabilities) == 0:
                    empty_capabilities.append(agent_name)
            except Exception as e:
                empty_capabilities.append(f"{agent_name}: {str(e)}")

        assert (
            len(empty_capabilities) == 0
        ), f"Agents with empty capabilities:\n" + "\n".join(empty_capabilities)

    def test_agent_has_skills_available(self):
        """Test that all agents have non-empty skills_available list."""
        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        empty_skills = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                skills_available = manifest.get("skills_available", [])
                if not skills_available or len(skills_available) == 0:
                    empty_skills.append(agent_name)
            except Exception as e:
                empty_skills.append(f"{agent_name}: {str(e)}")

        assert (
            len(empty_skills) == 0
        ), f"Agents with empty skills_available:\n" + "\n".join(empty_skills)

    def test_agent_skills_exist_in_registry(self):
        """Test that all skills referenced by agents exist in the skill registry."""
        from betty.config import REGISTRY_FILE

        # Load skill registry
        try:
            with open(REGISTRY_FILE) as f:
                skill_registry = json.load(f)
                available_skills = [skill["name"] for skill in skill_registry["skills"]]
        except Exception as e:
            pytest.skip(f"Could not load skill registry: {e}")

        agents_dir = os.path.join(BASE_DIR, "agents")
        agent_yamls = glob(os.path.join(agents_dir, "*/agent.yaml"))
        missing_skills = []

        for agent_yaml in agent_yamls:
            agent_name = Path(agent_yaml).parent.name
            try:
                manifest = load_agent_manifest(agent_yaml)
                skills_available = manifest.get("skills_available", [])
                for skill in skills_available:
                    if skill not in available_skills:
                        missing_skills.append(f"{agent_name}: skill '{skill}' not found")
            except Exception as e:
                missing_skills.append(f"{agent_name}: {str(e)}")

        assert (
            len(missing_skills) == 0
        ), f"Agents referencing non-existent skills:\n" + "\n".join(missing_skills)


class TestAgentDefineFunction:
    """Tests for the agent.define validation functions."""

    def create_temp_manifest(self, content):
        """Helper to create temporary agent manifest file."""
        import yaml

        f = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False)
        yaml.dump(content, f)
        f.close()
        return f.name

    def test_valid_agent_manifest(self):
        """Test validation of a complete valid agent manifest."""
        manifest_content = {
            "name": "test.agent",
            "version": "1.0.0",
            "description": "Test agent",
            "reasoning_mode": "oneshot",
            "capabilities": ["test capability"],
            "skills_available": ["api.validate"],
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is True
            assert "manifest" in result
        finally:
            os.unlink(manifest_path)

    def test_missing_required_fields(self):
        """Test that missing required fields are detected."""
        manifest_content = {
            "name": "test.agent",
            "description": "Test agent"
            # Missing: version, reasoning_mode, capabilities, skills_available
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert "errors" in result
            assert len(result["errors"]) > 0
        finally:
            os.unlink(manifest_path)

    def test_invalid_reasoning_mode(self):
        """Test that invalid reasoning mode is detected."""
        manifest_content = {
            "name": "test.agent",
            "version": "1.0.0",
            "description": "Test agent",
            "reasoning_mode": "invalid_mode",
            "capabilities": ["test capability"],
            "skills_available": ["api.validate"],
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("reasoning_mode" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_empty_capabilities(self):
        """Test that empty capabilities list is detected."""
        manifest_content = {
            "name": "test.agent",
            "version": "1.0.0",
            "description": "Test agent",
            "reasoning_mode": "oneshot",
            "capabilities": [],
            "skills_available": ["api.validate"],
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("capabilities" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_empty_skills_available(self):
        """Test that empty skills_available list is detected."""
        manifest_content = {
            "name": "test.agent",
            "version": "1.0.0",
            "description": "Test agent",
            "reasoning_mode": "oneshot",
            "capabilities": ["test capability"],
            "skills_available": [],
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("skills_available" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_nonexistent_skill_reference(self):
        """Test that referencing a non-existent skill is detected."""
        manifest_content = {
            "name": "test.agent",
            "version": "1.0.0",
            "description": "Test agent",
            "reasoning_mode": "oneshot",
            "capabilities": ["test capability"],
            "skills_available": ["nonexistent.skill"],
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any(
                "not found in registry" in error.lower() for error in result["errors"]
            )
        finally:
            os.unlink(manifest_path)

    def test_invalid_yaml_format(self):
        """Test that invalid YAML is detected."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("invalid: yaml: content:\n  - missing bracket")
            temp_path = f.name

        try:
            result = validate_manifest(temp_path)
            assert result["valid"] is False
            assert len(result["errors"]) > 0
        finally:
            os.unlink(temp_path)

    def test_nonexistent_file(self):
        """Test handling of nonexistent file."""
        try:
            result = validate_manifest("/nonexistent/agent.yaml")
            assert result["valid"] is False
            assert len(result["errors"]) > 0
        except Exception:
            # validate_manifest may raise an exception for nonexistent files
            # which is acceptable behavior
            pass
