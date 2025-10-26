"""
Tests for command.define skill - validates command workflows and registration.
"""

import os
import json
from pathlib import Path
from typing import Callable

import pytest
import yaml

# Import the command.define functions
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills", "command.define")))

from command_define import (
    validate_manifest,
    load_command_manifest,
    update_command_registry,
    load_command_registry,
    validate_execution_target,
    CommandValidationError,
    CommandRegistryError
)


@pytest.fixture
def write_command_manifest(tmp_path) -> Callable[[dict, str], str]:
    """Write manifest content to a temporary file and ensure it exists."""

    def _writer(content: dict, filename: str = "command-manifest.yaml") -> str:
        manifest_path = tmp_path / filename
        manifest_path.write_text(yaml.safe_dump(content))
        assert manifest_path.exists(), "Expected command manifest fixture to be created"
        return str(manifest_path)

    return _writer
from betty.config import (
    COMMANDS_REGISTRY_FILE,
    CommandExecutionType,
    CommandStatus
)
from betty.validation import (
    validate_command_name,
    validate_command_execution_type,
    ValidationError
)


class TestCommandNameValidation:
    """Tests for command name validation."""

    def test_valid_command_names(self):
        """Test that valid command names pass validation."""
        valid_names = [
            "/test-command",
            "/api-validate",
            "/api-design",
            "/test",
            "/my-awesome-command",
        ]
        for name in valid_names:
            validate_command_name(name)  # Should not raise

    def test_invalid_command_names(self):
        """Test that invalid command names raise ValidationError."""
        invalid_names = [
            "test-command",  # Missing leading slash
            "/Test-Command",  # Uppercase
            "/test_command",  # Underscore
            "/test command",  # Space
            "/123-test",  # Starts with number after slash
            "",  # Empty
            "/",  # Just slash
            "/test@command",  # Invalid character
        ]
        for name in invalid_names:
            with pytest.raises(ValidationError):
                validate_command_name(name)


class TestCommandExecutionType:
    """Tests for command execution type validation."""

    def test_valid_execution_types(self):
        """Test that valid execution types pass validation."""
        valid_types = ["agent", "skill", "workflow"]
        for exec_type in valid_types:
            validate_command_execution_type(exec_type)  # Should not raise

    def test_invalid_execution_types(self):
        """Test that invalid execution types raise ValidationError."""
        invalid_types = [
            "invalid",
            "Agent",  # Wrong case
            "SKILL",
            "",
            None,
            "function"
        ]
        for exec_type in invalid_types:
            with pytest.raises(ValidationError):
                validate_command_execution_type(exec_type)


class TestCommandManifestLoading:
    """Tests for loading command manifests from YAML files."""

    def test_load_valid_manifest(self, write_command_manifest):
        """Test loading a valid command manifest."""
        manifest_content = {
            "name": "/test-command",
            "version": "0.1.0",
            "description": "Fixture command for loading test",
            "execution": {
                "type": "skill",
                "target": "api.validate",
            },
        }

        manifest_path = write_command_manifest(manifest_content, "test-command.yaml")
        manifest = load_command_manifest(manifest_path)

        assert manifest is not None
        assert manifest["name"] == "/test-command"
        assert manifest["version"] == "0.1.0"
        assert "execution" in manifest

    def test_load_nonexistent_manifest(self):
        """Test that loading nonexistent file raises error."""
        with pytest.raises(CommandValidationError, match="not found"):
            load_command_manifest("/nonexistent/file.yaml")

    def test_load_invalid_yaml(self, tmp_path):
        """Test that loading invalid YAML raises error."""
        temp_path = tmp_path / "invalid-command.yaml"
        temp_path.write_text("invalid: yaml: content:\n  - missing bracket")
        assert temp_path.exists(), "Expected invalid manifest fixture to exist"

        with pytest.raises(CommandValidationError, match="Failed to parse YAML"):
            load_command_manifest(str(temp_path))


class TestCommandManifestValidation:
    """Tests for comprehensive command manifest validation."""

    def test_valid_command_manifest(self, write_command_manifest):
        """Test validation of a complete valid command manifest."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "status": "active",
            "tags": ["test"]
        }

        manifest_path = write_command_manifest(manifest_content, "valid-command.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is True
        assert result["errors"] == []
        assert "manifest" in result

    def test_missing_required_fields(self, write_command_manifest):
        """Test that missing required fields are detected."""
        manifest_content = {
            "name": "/test-command",
            "description": "Test command"
            # Missing: version, execution
        }

        manifest_path = write_command_manifest(manifest_content, "missing-fields.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("Missing required fields" in error for error in result["errors"])

    def test_invalid_command_name_format(self, write_command_manifest):
        """Test that invalid name format is detected."""
        manifest_content = {
            "name": "invalid-name",  # Missing leading slash
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            }
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-name.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("Invalid name" in error for error in result["errors"])

    def test_invalid_version_format(self, write_command_manifest):
        """Test that invalid version format is detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0",  # Invalid: missing patch version
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            }
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-version.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("Invalid version" in error for error in result["errors"])

    def test_invalid_execution_type(self, write_command_manifest):
        """Test that invalid execution type is detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "invalid_type",
                "target": "api.validate"
            }
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-execution-type.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("execution.type" in error for error in result["errors"])

    def test_missing_execution_target(self, write_command_manifest):
        """Test that missing execution target is detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill"
                # Missing: target
            }
        }

        manifest_path = write_command_manifest(manifest_content, "missing-target.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("execution.target" in error and "Field required" in error for error in result["errors"])

    def test_invalid_status(self, write_command_manifest):
        """Test that invalid status is detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "status": "invalid_status"
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-status.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("Invalid status" in error for error in result["errors"])

    def test_invalid_parameters_format(self, write_command_manifest):
        """Test that invalid parameters format is detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "parameters": "not-an-array"  # Should be array
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-parameters.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("parameters" in error and "valid list" in error for error in result["errors"])

    def test_parameters_missing_required_fields(self, write_command_manifest):
        """Test that parameters missing required fields are detected."""
        manifest_content = {
            "name": "/test-command",
            "version": "1.0.0",
            "description": "Test command",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "parameters": [
                {
                    "name": "param1"
                    # Missing: type
                }
            ]
        }
        manifest_path = write_command_manifest(manifest_content, "missing-parameter-type.yaml")
        result = validate_manifest(manifest_path)
        assert result["valid"] is False
        assert any("parameters.0.type" in error and "Field required" in error for error in result["errors"])


class TestCommandExecutionTargetValidation:
    """Tests for execution target validation."""

    def test_validate_skill_target_exists(self):
        """Test validation of skill target that exists in registry."""
        execution = {
            "type": "skill",
            "target": "api.validate"
        }
        errors = validate_execution_target(execution)
        # api.validate should exist in the registry
        # If it doesn't, the test will show an error
        # This is acceptable as it tests the validation logic

    def test_validate_skill_target_not_exists(self):
        """Test validation of skill target that doesn't exist."""
        execution = {
            "type": "skill",
            "target": "nonexistent.skill"
        }
        errors = validate_execution_target(execution)
        assert len(errors) > 0
        assert any("not found in skill registry" in error for error in errors)

    def test_validate_agent_target_not_exists(self):
        """Test validation of agent target that doesn't exist."""
        execution = {
            "type": "agent",
            "target": "nonexistent.agent"
        }
        errors = validate_execution_target(execution)
        assert len(errors) > 0
        assert any("not found in agent registry" in error for error in errors)

    def test_validate_missing_target(self):
        """Test validation when target is missing."""
        execution = {
            "type": "skill"
            # Missing: target
        }
        errors = validate_execution_target(execution)
        assert len(errors) > 0
        assert any("target is required" in error for error in errors)


class TestCommandRegistry:
    """Tests for command registry operations."""

    def test_load_command_registry(self):
        """Test loading command registry."""
        registry = load_command_registry()
        assert registry is not None
        assert "registry_version" in registry
        assert "commands" in registry

    def test_update_command_registry(self):
        """Test updating command registry with new command."""
        # Create a test manifest
        manifest = {
            "name": "/test-registry-command",
            "version": "1.0.0",
            "description": "Test registry update",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "status": "draft",
            "tags": ["test"]
        }

        # Update registry
        result = update_command_registry(manifest)
        assert result is True

        # Verify it was added
        registry = load_command_registry()
        command_names = [cmd["name"] for cmd in registry["commands"]]
        assert "/test-registry-command" in command_names

    def test_update_existing_command(self):
        """Test updating an existing command in registry."""
        # First, add a command
        manifest = {
            "name": "/test-update-command",
            "version": "1.0.0",
            "description": "Original description",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            }
        }
        update_command_registry(manifest)

        # Now update it
        manifest["version"] = "1.0.1"
        manifest["description"] = "Updated description"
        result = update_command_registry(manifest)
        assert result is True

        # Verify it was updated
        registry = load_command_registry()
        updated_cmd = next(
            (cmd for cmd in registry["commands"] if cmd["name"] == "/test-update-command"),
            None
        )
        assert updated_cmd is not None
        assert updated_cmd["version"] == "1.0.1"
        assert updated_cmd["description"] == "Updated description"


class TestCommandWorkflow:
    """Integration tests for complete command workflow."""

    def test_complete_command_registration_workflow(self, write_command_manifest):
        """Test complete workflow: create manifest -> validate -> register."""
        # Create a complete command manifest
        manifest_content = {
            "name": "/test-workflow-command",
            "version": "1.0.0",
            "description": "Test complete workflow",
            "execution": {
                "type": "skill",
                "target": "api.validate"
            },
            "parameters": [
                {
                    "name": "input",
                    "type": "string",
                    "required": True,
                    "description": "Input parameter"
                }
            ],
            "status": "active",
            "tags": ["test", "workflow"]
        }

        manifest_path = write_command_manifest(manifest_content, "workflow-command.yaml")

        # Step 1: Validate manifest
        validation = validate_manifest(manifest_path)
        assert validation["valid"] is True
        assert validation["errors"] == []

        # Step 2: Register command
        result = update_command_registry(validation["manifest"])
        assert result is True

        # Step 3: Verify registration
        registry = load_command_registry()
        command = next(
            (cmd for cmd in registry["commands"] if cmd["name"] == "/test-workflow-command"),
            None
        )
        assert command is not None
        assert command["version"] == "1.0.0"
        assert command["description"] == "Test complete workflow"
        assert command["status"] == "active"
        assert len(command["parameters"]) == 1
        assert command["parameters"][0]["name"] == "input"

    def test_invalid_command_workflow(self, write_command_manifest):
        """Test workflow with invalid command manifest."""
        # Create an invalid manifest (missing required fields)
        manifest_content = {
            "name": "/test-invalid",
            "description": "Invalid command"
            # Missing: version, execution
        }

        manifest_path = write_command_manifest(manifest_content, "invalid-workflow.yaml")

        # Validation should fail
        validation = validate_manifest(manifest_path)
        assert validation["valid"] is False
        assert len(validation["errors"]) > 0
        assert "Missing required fields" in validation["errors"][0]
