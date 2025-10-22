"""
Tests for betty.errors module
"""

import pytest
from betty.errors import (
    BettyError,
    SkillNotFoundError,
    SkillValidationError,
    RegistryError,
    WorkflowError,
    ManifestError,
    format_error_response
)


class TestBettyError:
    """Tests for base BettyError class."""

    def test_betty_error_creation(self):
        """Test creating a BettyError."""
        error = BettyError("Test error", details={"key": "value"})
        assert str(error) == "Test error"
        assert error.details == {"key": "value"}

    def test_betty_error_to_dict(self):
        """Test converting error to dict."""
        error = BettyError("Test error", details={"key": "value"})
        error_dict = error.to_dict()
        assert error_dict["error"] == "BettyError"
        assert error_dict["message"] == "Test error"
        assert error_dict["details"] == {"key": "value"}

    def test_betty_error_to_json(self):
        """Test converting error to JSON."""
        error = BettyError("Test error")
        json_str = error.to_json()
        assert "Test error" in json_str
        assert "BettyError" in json_str


class TestErrorSubclasses:
    """Tests for Betty error subclasses."""

    def test_skill_not_found_error(self):
        """Test SkillNotFoundError."""
        error = SkillNotFoundError("Skill not found")
        assert isinstance(error, BettyError)
        assert error.to_dict()["error"] == "SkillNotFoundError"

    def test_skill_validation_error(self):
        """Test SkillValidationError."""
        error = SkillValidationError("Validation failed")
        assert isinstance(error, BettyError)

    def test_registry_error(self):
        """Test RegistryError."""
        error = RegistryError("Registry error")
        assert isinstance(error, BettyError)

    def test_workflow_error(self):
        """Test WorkflowError."""
        error = WorkflowError("Workflow failed")
        assert isinstance(error, BettyError)

    def test_manifest_error(self):
        """Test ManifestError."""
        error = ManifestError("Manifest error")
        assert isinstance(error, BettyError)


class TestFormatErrorResponse:
    """Tests for format_error_response function."""

    def test_format_betty_error(self):
        """Test formatting a BettyError."""
        error = BettyError("Test error", details={"key": "value"})
        response = format_error_response(error)
        assert response["error"] == "BettyError"
        assert response["message"] == "Test error"

    def test_format_standard_exception(self):
        """Test formatting a standard Python exception."""
        error = ValueError("Invalid value")
        response = format_error_response(error)
        assert response["error"] == "ValueError"
        assert response["message"] == "Invalid value"

    def test_format_with_traceback(self):
        """Test formatting with traceback included."""
        error = ValueError("Test")
        response = format_error_response(error, include_traceback=True)
        assert "traceback" in response
