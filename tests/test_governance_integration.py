"""
Integration tests for governance enforcement in artifact.create skill.

Tests that governance policies are enforced when creating/updating artifacts.
"""

import pytest
import yaml
from datetime import datetime, timedelta

from betty.skills.artifact.create.artifact_create import generate_artifact


class TestArtifactCreateGovernance:
    """Tests for governance enforcement in artifact.create."""

    def test_create_new_artifact_without_existing(self, tmp_path):
        """Creating a new artifact should succeed without governance checks."""
        output_path = tmp_path / "test-artifact.yaml"

        result = generate_artifact(
            artifact_type="business-case",
            context="Test business case",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is True
        assert output_path.exists()

    def test_update_mutable_artifact(self, tmp_path):
        """Updating a mutable artifact should succeed."""
        output_path = tmp_path / "mutable-artifact.yaml"

        # Create initial artifact with mutable metadata
        initial_content = """
metadata:
  id: mutable-artifact-1
  version: "1.0.0"
  created: "2024-01-01"
  status: "published"
  immutability: false

content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it
        result = generate_artifact(
            artifact_type="business-case",
            context="Updated business case",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is True

    def test_update_immutable_artifact_blocked(self, tmp_path):
        """Updating an immutable artifact should be blocked."""
        output_path = tmp_path / "immutable-artifact.yaml"

        # Create initial artifact with immutable metadata
        initial_content = """
metadata:
  id: immutable-artifact-1
  version: "1.0.0"
  created: "2024-01-01"
  status: "published"
  immutability: true

content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it - should fail
        result = generate_artifact(
            artifact_type="business-case",
            context="Attempt to update",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is False
        assert "governance policy violation" in result["error"].lower()
        assert result.get("policy_violation") is True

    def test_update_draft_immutable_artifact_allowed(self, tmp_path):
        """Updating a draft artifact with immutability should be allowed."""
        output_path = tmp_path / "draft-artifact.yaml"

        # Create initial artifact with immutable metadata but draft status
        initial_content = """
metadata:
  id: draft-artifact-1
  version: "1.0.0"
  created: "2024-01-01"
  status: "draft"
  immutability: true

content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it - should succeed because it's draft
        result = generate_artifact(
            artifact_type="business-case",
            context="Update draft",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is True

    def test_update_expired_artifact_blocked(self, tmp_path):
        """Updating an expired artifact should be blocked."""
        output_path = tmp_path / "expired-artifact.yaml"

        # Create artifact with expired retention
        created_at = datetime.utcnow() - timedelta(days=60)
        initial_content = f"""
metadata:
  id: expired-artifact-1
  version: "1.0.0"
  created_at: "{created_at.isoformat()}"
  status: "published"
  retention_days: 30

content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it - should fail due to retention policy
        result = generate_artifact(
            artifact_type="business-case",
            context="Attempt to update expired",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is False
        assert "governance policy violation" in result["error"].lower()
        assert "expired" in result["error"].lower()

    def test_update_artifact_within_retention_allowed(self, tmp_path):
        """Updating an artifact within retention period should succeed."""
        output_path = tmp_path / "valid-retention-artifact.yaml"

        # Create artifact with valid retention
        created_at = datetime.utcnow() - timedelta(days=10)
        initial_content = f"""
metadata:
  id: valid-retention-1
  version: "1.0.0"
  created_at: "{created_at.isoformat()}"
  status: "published"
  retention_days: 30

content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it - should succeed
        result = generate_artifact(
            artifact_type="business-case",
            context="Update within retention",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is True

    def test_artifact_without_metadata_section_allowed(self, tmp_path):
        """Updating an artifact without metadata section should be allowed."""
        output_path = tmp_path / "no-metadata-artifact.yaml"

        # Create artifact without metadata section
        initial_content = """
# This is a simple artifact without metadata
content:
  overview: Initial content
"""
        output_path.write_text(initial_content)

        # Try to update it - should succeed
        result = generate_artifact(
            artifact_type="business-case",
            context="Update artifact without metadata",
            output_path=str(output_path),
            metadata={"author": "Test User"}
        )

        assert result["success"] is True
