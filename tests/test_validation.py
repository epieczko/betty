"""
Tests for betty.validation module
"""

import pytest
from betty.validation import (
    validate_skill_name,
    validate_path,
    validate_manifest_fields,
    validate_version,
    ValidationError
)


class TestValidateSkillName:
    """Tests for skill name validation."""

    def test_valid_skill_names(self):
        """Test that valid skill names pass validation."""
        valid_names = [
            "skill.create",
            "skill.define",
            "registry.update",
            "workflow.compose",
            "runtime-execute",
            "test_skill",
            "a",
            "skill123",
        ]
        for name in valid_names:
            validate_skill_name(name)  # Should not raise

    def test_invalid_skill_names(self):
        """Test that invalid skill names raise ValidationError."""
        invalid_names = [
            "",  # Empty
            "Skill.Create",  # Uppercase
            "123skill",  # Starts with number
            "skill name",  # Contains space
            "skill@test",  # Invalid character
            "-skill",  # Starts with hyphen
        ]
        for name in invalid_names:
            with pytest.raises(ValidationError):
                validate_skill_name(name)


class TestValidatePath:
    """Tests for path validation."""

    def test_valid_path(self):
        """Test that valid paths pass validation."""
        validate_path("/home/user/file.txt")
        validate_path("relative/path/file.txt")

    def test_empty_path(self):
        """Test that empty path raises ValidationError."""
        with pytest.raises(ValidationError, match="Path cannot be empty"):
            validate_path("")

    def test_path_traversal(self):
        """Test that path traversal is detected."""
        with pytest.raises(ValidationError, match="Path traversal"):
            validate_path("../../../etc/passwd")

    def test_null_byte(self):
        """Test that null bytes are detected."""
        with pytest.raises(ValidationError, match="Null byte"):
            validate_path("/path/to/file\x00.txt")


class TestValidateManifestFields:
    """Tests for manifest field validation."""

    def test_valid_manifest(self):
        """Test that manifest with all required fields is valid."""
        manifest = {
            "name": "test.skill",
            "version": "1.0.0",
            "description": "Test skill",
            "inputs": [],
            "outputs": [],
            "status": "active"
        }
        required = ["name", "version", "description"]
        missing = validate_manifest_fields(manifest, required)
        assert missing == []

    def test_missing_fields(self):
        """Test that missing fields are detected."""
        manifest = {
            "name": "test.skill",
            "description": "Test skill"
        }
        required = ["name", "version", "description"]
        missing = validate_manifest_fields(manifest, required)
        assert "version" in missing

    def test_invalid_manifest_type(self):
        """Test that non-dict manifest raises error."""
        with pytest.raises(ValidationError, match="must be a dictionary"):
            validate_manifest_fields("not a dict", ["field"])


class TestValidateVersion:
    """Tests for version validation."""

    def test_valid_versions(self):
        """Test that valid semantic versions pass validation."""
        valid_versions = [
            "0.1.0",
            "1.0.0",
            "1.2.3",
            "1.0.0-alpha",
            "1.0.0-beta.1",
        ]
        for version in valid_versions:
            validate_version(version)  # Should not raise

    def test_invalid_versions(self):
        """Test that invalid versions raise ValidationError."""
        invalid_versions = [
            "",  # Empty
            "1.0",  # Missing patch
            "v1.0.0",  # Has 'v' prefix
            "1.0.0.0",  # Too many parts
            "a.b.c",  # Non-numeric
        ]
        for version in invalid_versions:
            with pytest.raises(ValidationError):
                validate_version(version)
