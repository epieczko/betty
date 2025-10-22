"""
Tests for betty.config module
"""

import os
import pytest
from betty.config import (
    get_skill_path,
    get_skill_manifest_path,
    get_skill_handler_path,
    SkillStatus
)


class TestSkillPaths:
    """Tests for skill path helper functions."""

    def test_get_skill_path(self):
        """Test skill path generation."""
        path = get_skill_path("skill.create")
        assert path.endswith("skills/skill.create")

    def test_get_skill_manifest_path(self):
        """Test manifest path generation."""
        path = get_skill_manifest_path("skill.create")
        assert path.endswith("skills/skill.create/skill.yaml")

    def test_get_skill_handler_path(self):
        """Test handler path generation."""
        path = get_skill_handler_path("skill.create")
        assert path.endswith("skills/skill.create/skill_create.py")

    def test_get_skill_handler_path_with_dots(self):
        """Test handler path generation with dots in name."""
        path = get_skill_handler_path("registry.update")
        assert path.endswith("skills/registry.update/registry_update.py")


class TestSkillStatus:
    """Tests for SkillStatus enum."""

    def test_skill_status_values(self):
        """Test that SkillStatus enum has correct values."""
        assert SkillStatus.DRAFT.value == "draft"
        assert SkillStatus.ACTIVE.value == "active"
        assert SkillStatus.DEPRECATED.value == "deprecated"
        assert SkillStatus.ARCHIVED.value == "archived"
