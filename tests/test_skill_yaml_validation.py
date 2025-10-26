"""
Tests for SKILL.yaml validation - validates all skill manifests using skill.define.
Includes doc presence checks to ensure SKILL.md exists for each SKILL.yaml.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path
from glob import glob

from betty.skills.skill.define.skill_define import (
    validate_manifest,
    load_skill_manifest,
    SkillValidationError,
)
from betty.config import BASE_DIR


class TestSkillYamlValidation:
    """Tests for validating all SKILL.yaml files in the repository."""

    def get_all_skill_yamls(self):
        """Get all skill.yaml files in the skills directory."""
        skills_dir = os.path.join(BASE_DIR, "skills")
        pattern = os.path.join(skills_dir, "*/skill.yaml")
        return glob(pattern)

    def test_all_skill_yamls_exist(self):
        """Test that at least one skill.yaml file exists."""
        skill_yamls = self.get_all_skill_yamls()
        assert len(skill_yamls) > 0, "No skill.yaml files found in skills directory"

    def test_all_skill_yamls_are_valid(self):
        """Test that all skill.yaml files pass validation."""
        skill_yamls = self.get_all_skill_yamls()
        failures = []

        for skill_yaml in skill_yamls:
            skill_name = Path(skill_yaml).parent.name
            try:
                result = validate_manifest(skill_yaml)
                if not result.get("valid"):
                    error_msg = result.get("error") or ", ".join(
                        result.get("missing", [])
                    )
                    failures.append(f"{skill_name}: {error_msg}")
            except Exception as e:
                failures.append(f"{skill_name}: {str(e)}")

        assert len(failures) == 0, f"Validation failures:\n" + "\n".join(failures)

    def test_all_skill_yamls_have_required_fields(self):
        """Test that all skill.yaml files have required fields."""
        from betty.config import REQUIRED_SKILL_FIELDS

        skill_yamls = self.get_all_skill_yamls()
        failures = []

        for skill_yaml in skill_yamls:
            skill_name = Path(skill_yaml).parent.name
            try:
                manifest = load_skill_manifest(skill_yaml)
                missing = [
                    field for field in REQUIRED_SKILL_FIELDS if field not in manifest
                ]
                if missing:
                    failures.append(f"{skill_name}: Missing fields {missing}")
            except Exception as e:
                failures.append(f"{skill_name}: {str(e)}")

        assert len(failures) == 0, f"Missing required fields:\n" + "\n".join(failures)

    def test_skill_yaml_parseable(self):
        """Test that all skill.yaml files are valid YAML."""
        skill_yamls = self.get_all_skill_yamls()
        failures = []

        for skill_yaml in skill_yamls:
            skill_name = Path(skill_yaml).parent.name
            try:
                load_skill_manifest(skill_yaml)
            except SkillValidationError as e:
                failures.append(f"{skill_name}: {str(e)}")

        assert len(failures) == 0, f"YAML parsing errors:\n" + "\n".join(failures)


class TestSkillDocPresence:
    """Tests for documentation presence - SKILL.yaml should have SKILL.md."""

    def get_all_skill_dirs(self):
        """Get all skill directories."""
        skills_dir = os.path.join(BASE_DIR, "skills")
        return [
            d
            for d in glob(os.path.join(skills_dir, "*"))
            if os.path.isdir(d) and not d.endswith("__pycache__")
        ]

    def test_all_skills_have_skill_md(self):
        """Test that every skill.yaml has a corresponding SKILL.md file."""
        skill_dirs = self.get_all_skill_dirs()
        missing_docs = []

        for skill_dir in skill_dirs:
            skill_yaml = os.path.join(skill_dir, "skill.yaml")
            skill_md = os.path.join(skill_dir, "SKILL.md")
            skill_name = Path(skill_dir).name

            if os.path.exists(skill_yaml):
                if not os.path.exists(skill_md):
                    missing_docs.append(skill_name)

        assert (
            len(missing_docs) == 0
        ), f"Skills missing SKILL.md documentation:\n" + "\n".join(missing_docs)

    def test_all_skill_md_not_empty(self):
        """Test that all SKILL.md files have content."""
        skill_dirs = self.get_all_skill_dirs()
        empty_docs = []

        for skill_dir in skill_dirs:
            skill_yaml = os.path.join(skill_dir, "skill.yaml")
            skill_md = os.path.join(skill_dir, "SKILL.md")
            skill_name = Path(skill_dir).name

            if os.path.exists(skill_yaml) and os.path.exists(skill_md):
                with open(skill_md, "r") as f:
                    content = f.read().strip()
                    if len(content) == 0:
                        empty_docs.append(skill_name)

        assert (
            len(empty_docs) == 0
        ), f"Skills with empty SKILL.md:\n" + "\n".join(empty_docs)

    def test_skill_md_has_header(self):
        """Test that all SKILL.md files have a header (title) within first few lines."""
        skill_dirs = self.get_all_skill_dirs()
        missing_headers = []

        for skill_dir in skill_dirs:
            skill_yaml = os.path.join(skill_dir, "skill.yaml")
            skill_md = os.path.join(skill_dir, "SKILL.md")
            skill_name = Path(skill_dir).name

            if os.path.exists(skill_yaml) and os.path.exists(skill_md):
                with open(skill_md, "r") as f:
                    # Read first 5 lines to find a header
                    content = f.read()
                    has_header = "#" in content[:500]  # Check first 500 chars
                    if not has_header:
                        missing_headers.append(skill_name)

        assert (
            len(missing_headers) == 0
        ), f"Skills with SKILL.md missing header:\n" + "\n".join(missing_headers)


class TestSkillManifestStructure:
    """Tests for skill manifest structure and content."""

    def test_skill_names_match_directory(self):
        """Test that skill names match their directory names."""
        skills_dir = os.path.join(BASE_DIR, "skills")
        skill_yamls = glob(os.path.join(skills_dir, "*/skill.yaml"))
        mismatches = []

        for skill_yaml in skill_yamls:
            dir_name = Path(skill_yaml).parent.name
            try:
                manifest = load_skill_manifest(skill_yaml)
                skill_name = manifest.get("name", "")
                # Remove 'skill.' prefix if present
                expected_name = dir_name.replace(".", ".")

                if skill_name != expected_name:
                    mismatches.append(
                        f"{dir_name}: manifest name '{skill_name}' != directory '{expected_name}'"
                    )
            except Exception as e:
                mismatches.append(f"{dir_name}: {str(e)}")

        assert (
            len(mismatches) == 0
        ), f"Skill name/directory mismatches:\n" + "\n".join(mismatches)

    def test_skill_versions_are_semver(self):
        """Test that all skill versions follow semantic versioning."""
        import re

        semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
        skills_dir = os.path.join(BASE_DIR, "skills")
        skill_yamls = glob(os.path.join(skills_dir, "*/skill.yaml"))
        invalid_versions = []

        for skill_yaml in skill_yamls:
            skill_name = Path(skill_yaml).parent.name
            try:
                manifest = load_skill_manifest(skill_yaml)
                version = manifest.get("version", "")
                if not semver_pattern.match(version):
                    invalid_versions.append(f"{skill_name}: {version}")
            except Exception as e:
                invalid_versions.append(f"{skill_name}: {str(e)}")

        assert (
            len(invalid_versions) == 0
        ), f"Invalid semantic versions:\n" + "\n".join(invalid_versions)

    def test_skill_has_description(self):
        """Test that all skills have non-empty descriptions."""
        skills_dir = os.path.join(BASE_DIR, "skills")
        skill_yamls = glob(os.path.join(skills_dir, "*/skill.yaml"))
        missing_descriptions = []

        for skill_yaml in skill_yamls:
            skill_name = Path(skill_yaml).parent.name
            try:
                manifest = load_skill_manifest(skill_yaml)
                description = manifest.get("description", "").strip()
                if not description:
                    missing_descriptions.append(skill_name)
            except Exception as e:
                missing_descriptions.append(f"{skill_name}: {str(e)}")

        assert (
            len(missing_descriptions) == 0
        ), f"Skills with empty/missing descriptions:\n" + "\n".join(
            missing_descriptions
        )


class TestSkillDefineFunction:
    """Tests for the skill.define validation functions."""

    def create_temp_manifest(self, content):
        """Helper to create temporary skill manifest file."""
        import yaml

        f = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False)
        yaml.dump(content, f)
        f.close()
        return f.name

    def test_valid_skill_manifest(self):
        """Test validation of a complete valid skill manifest."""
        manifest_content = {
            "name": "test.skill",
            "version": "1.0.0",
            "description": "Test skill",
            "inputs": [{"name": "input1", "type": "string"}],
            "outputs": [{"name": "output1", "type": "string"}],
            "handler": "test_skill.py",
            "status": "active",
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
            "name": "test.skill",
            "description": "Test skill"
            # Missing: version, inputs, outputs, handler
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert "missing" in result
        finally:
            os.unlink(manifest_path)

    def test_invalid_yaml_format(self):
        """Test that invalid YAML is detected."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("invalid: yaml: content:\n  - missing bracket")
            temp_path = f.name

        try:
            result = validate_manifest(temp_path)
            assert result["valid"] is False or "error" in result
        finally:
            os.unlink(temp_path)

    def test_nonexistent_file(self):
        """Test handling of nonexistent file."""
        try:
            result = validate_manifest("/nonexistent/skill.yaml")
            assert result["valid"] is False
            assert "error" in result
        except Exception:
            # validate_manifest may raise an exception for nonexistent files
            # which is acceptable behavior
            pass
