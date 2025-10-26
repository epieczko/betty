"""
Unit tests for the betty.governance module.

Tests immutability and retention policy enforcement.
"""

import pytest
import sys
import os
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any

# Add betty module to path
BASE_PATH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_PATH))

from betty.governance import (
    enforce_governance,
    log_governance_action,
    check_artifact_accessibility,
    get_governance_log_path
)


class TestImmutabilityEnforcement:
    """Tests for immutability policy enforcement."""

    def test_immutable_artifact_draft_status_allowed(self):
        """Draft artifacts should be modifiable even if immutability is set."""
        artifact_meta = {
            "id": "test-artifact-1",
            "immutability": True,
            "status": "draft"
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)

    def test_immutable_artifact_published_status_blocked(self):
        """Published artifacts with immutability should be blocked."""
        artifact_meta = {
            "id": "test-artifact-2",
            "immutability": True,
            "status": "published"
        }

        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "test-artifact-2" in str(exc_info.value)
        assert "immutable" in str(exc_info.value).lower()

    def test_immutable_artifact_approved_status_blocked(self):
        """Approved artifacts with immutability should be blocked."""
        artifact_meta = {
            "id": "test-artifact-3",
            "immutability": True,
            "status": "approved"
        }

        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "test-artifact-3" in str(exc_info.value)

    def test_mutable_artifact_allowed(self):
        """Artifacts without immutability flag should be allowed."""
        artifact_meta = {
            "id": "test-artifact-4",
            "immutability": False,
            "status": "published"
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)

    def test_no_immutability_field_allowed(self):
        """Artifacts without immutability field should be allowed."""
        artifact_meta = {
            "id": "test-artifact-5",
            "status": "published"
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)


class TestRetentionPolicyEnforcement:
    """Tests for retention policy enforcement."""

    def test_expired_artifact_blocked(self):
        """Artifacts past retention period should be blocked."""
        # Create an artifact created 60 days ago with 30-day retention
        created_at = datetime.utcnow() - timedelta(days=60)

        artifact_meta = {
            "id": "test-artifact-6",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "test-artifact-6" in str(exc_info.value)
        assert "expired" in str(exc_info.value).lower()
        assert "30 days" in str(exc_info.value)

    def test_valid_artifact_within_retention_allowed(self):
        """Artifacts within retention period should be allowed."""
        # Create an artifact created 10 days ago with 30-day retention
        created_at = datetime.utcnow() - timedelta(days=10)

        artifact_meta = {
            "id": "test-artifact-7",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)

    def test_retention_boundary_case(self):
        """Artifact at exactly retention boundary should be blocked."""
        # Create an artifact created exactly 30 days ago with 30-day retention
        # Add a small buffer to ensure it's over the limit
        created_at = datetime.utcnow() - timedelta(days=30, seconds=1)

        artifact_meta = {
            "id": "test-artifact-8",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "expired" in str(exc_info.value).lower()

    def test_retention_with_timezone_z_suffix(self):
        """Handle ISO format with 'Z' suffix for UTC."""
        created_at = datetime.utcnow() - timedelta(days=10)

        artifact_meta = {
            "id": "test-artifact-9",
            "retention_days": 30,
            "created_at": created_at.isoformat() + "Z"
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)

    def test_no_retention_policy_allowed(self):
        """Artifacts without retention policy should be allowed."""
        artifact_meta = {
            "id": "test-artifact-10",
            "created_at": "2020-01-01T00:00:00"
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)

    def test_retention_missing_created_at_raises_error(self):
        """Retention policy without created_at should raise ValueError."""
        artifact_meta = {
            "id": "test-artifact-11",
            "retention_days": 30
        }

        with pytest.raises(ValueError) as exc_info:
            enforce_governance(artifact_meta)

        assert "created_at" in str(exc_info.value).lower()

    def test_retention_invalid_date_format_raises_error(self):
        """Invalid date format should raise ValueError."""
        artifact_meta = {
            "id": "test-artifact-12",
            "retention_days": 30,
            "created_at": "invalid-date-format"
        }

        with pytest.raises(ValueError) as exc_info:
            enforce_governance(artifact_meta)

        assert "invalid" in str(exc_info.value).lower() or "format" in str(exc_info.value).lower()


class TestValidationErrors:
    """Tests for validation and error handling."""

    def test_empty_metadata_raises_error(self):
        """Empty metadata should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            enforce_governance({})

        assert "empty" in str(exc_info.value).lower() or "id" in str(exc_info.value).lower()

    def test_missing_id_raises_error(self):
        """Missing 'id' field should raise ValueError."""
        artifact_meta = {
            "status": "published"
        }

        with pytest.raises(ValueError) as exc_info:
            enforce_governance(artifact_meta)

        assert "id" in str(exc_info.value).lower()

    def test_none_metadata_raises_error(self):
        """None metadata should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            enforce_governance(None)

        assert "empty" in str(exc_info.value).lower() or "cannot" in str(exc_info.value).lower()


class TestCombinedPolicies:
    """Tests for combined policy enforcement."""

    def test_immutable_and_expired_artifact_immutability_checked_first(self):
        """When both policies would block, immutability is checked first."""
        created_at = datetime.utcnow() - timedelta(days=60)

        artifact_meta = {
            "id": "test-artifact-13",
            "immutability": True,
            "status": "published",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        # Should raise PermissionError for immutability (checked first)
        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "immutable" in str(exc_info.value).lower()

    def test_mutable_but_expired_artifact_blocked(self):
        """Mutable but expired artifact should be blocked for retention."""
        created_at = datetime.utcnow() - timedelta(days=60)

        artifact_meta = {
            "id": "test-artifact-14",
            "immutability": False,
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        with pytest.raises(PermissionError) as exc_info:
            enforce_governance(artifact_meta)

        assert "expired" in str(exc_info.value).lower()

    def test_immutable_draft_with_valid_retention_allowed(self):
        """Immutable draft with valid retention should be allowed."""
        created_at = datetime.utcnow() - timedelta(days=10)

        artifact_meta = {
            "id": "test-artifact-15",
            "immutability": True,
            "status": "draft",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        # Should not raise an exception
        enforce_governance(artifact_meta)


class TestGovernanceLogging:
    """Tests for governance logging functionality."""

    def test_log_governance_action_creates_log_file(self, tmp_path):
        """Logging should create governance.log file."""
        # Note: This test uses the actual log path
        log_governance_action(
            artifact_id="test-log-1",
            action="test",
            outcome="allowed",
            message="Test log entry"
        )

        log_path = Path(get_governance_log_path())
        assert log_path.exists()

    def test_log_governance_action_valid_json(self, tmp_path):
        """Log entries should be valid JSON."""
        log_governance_action(
            artifact_id="test-log-2",
            action="write",
            outcome="blocked",
            message="Test governance violation",
            metadata={"policy": "immutability"}
        )

        log_path = Path(get_governance_log_path())
        with open(log_path, 'r') as f:
            lines = f.readlines()
            # Get the last line (our log entry)
            last_line = lines[-1].strip()
            log_entry = json.loads(last_line)

        assert log_entry["artifact_id"] == "test-log-2"
        assert log_entry["action"] == "write"
        assert log_entry["outcome"] == "blocked"
        assert "timestamp" in log_entry

    def test_enforce_governance_logs_on_block(self):
        """Enforce governance should log when blocking access."""
        artifact_meta = {
            "id": "test-log-3",
            "immutability": True,
            "status": "published"
        }

        with pytest.raises(PermissionError):
            enforce_governance(artifact_meta)

        # Check that log entry was created
        log_path = Path(get_governance_log_path())
        with open(log_path, 'r') as f:
            lines = f.readlines()
            # Find log entry for our artifact
            found = False
            for line in lines:
                entry = json.loads(line.strip())
                if entry.get("artifact_id") == "test-log-3":
                    assert entry["outcome"] == "blocked"
                    found = True
                    break

            assert found, "Log entry for blocked artifact not found"


class TestAccessibilityCheck:
    """Tests for non-throwing accessibility check."""

    def test_check_accessibility_for_valid_artifact(self):
        """Accessible artifact should return accessible=True."""
        artifact_meta = {
            "id": "test-access-1",
            "status": "draft"
        }

        result = check_artifact_accessibility(artifact_meta)

        assert result["accessible"] is True
        assert result["reason"] is None
        assert len(result["violations"]) == 0

    def test_check_accessibility_for_immutable_artifact(self):
        """Immutable artifact should return accessible=False."""
        artifact_meta = {
            "id": "test-access-2",
            "immutability": True,
            "status": "published"
        }

        result = check_artifact_accessibility(artifact_meta)

        assert result["accessible"] is False
        assert result["reason"] is not None
        assert "immutable" in result["reason"].lower()
        assert len(result["violations"]) == 1
        assert result["violations"][0]["type"] == "PermissionError"

    def test_check_accessibility_for_expired_artifact(self):
        """Expired artifact should return accessible=False."""
        created_at = datetime.utcnow() - timedelta(days=60)

        artifact_meta = {
            "id": "test-access-3",
            "retention_days": 30,
            "created_at": created_at.isoformat()
        }

        result = check_artifact_accessibility(artifact_meta)

        assert result["accessible"] is False
        assert result["reason"] is not None
        assert "expired" in result["reason"].lower()
        assert len(result["violations"]) == 1

    def test_check_accessibility_for_invalid_metadata(self):
        """Invalid metadata should return accessible=False."""
        artifact_meta = {
            "retention_days": 30
            # Missing both 'id' and 'created_at'
        }

        result = check_artifact_accessibility(artifact_meta)

        assert result["accessible"] is False
        assert result["reason"] is not None
        assert len(result["violations"]) == 1
        assert result["violations"][0]["type"] == "ValueError"
