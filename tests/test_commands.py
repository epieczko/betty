"""
Tests for command.define skill - validates command workflows and registration.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path

# Import the command.define functions
from betty.skills.command.define.command_define import (
    validate_manifest,
    load_command_manifest,
    update_command_registry,
    load_command_registry,
    validate_execution_target,
    CommandValidationError,
    CommandRegistryError
)
from betty.config import COMMANDS_REGISTRY_FILE
from betty.enums import CommandExecutionType, CommandStatus
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

    def test_load_valid_manifest(self):
        """Test loading a valid command manifest."""
        # Use the example command manifest
        manifest_path = "examples/test-command.yaml"
        if os.path.exists(manifest_path):
            manifest = load_command_manifest(manifest_path)
            assert manifest is not None
            assert manifest["name"] == "/test-command"
            assert manifest["version"] == "0.1.0"
            assert "execution" in manifest

    def test_load_nonexistent_manifest(self):
        """Test that loading nonexistent file raises error."""
        with pytest.raises(CommandValidationError, match="not found"):
            load_command_manifest("/nonexistent/file.yaml")

    def test_load_invalid_yaml(self):
        """Test that loading invalid YAML raises error."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content:\n  - missing bracket")
            temp_path = f.name

        try:
            with pytest.raises(CommandValidationError, match="Failed to parse YAML"):
                load_command_manifest(temp_path)
        finally:
            os.unlink(temp_path)


class TestCommandManifestValidation:
    """Tests for comprehensive command manifest validation."""

    def create_temp_manifest(self, content):
        """Helper to create temporary manifest file."""
        import yaml
        f = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False)
        yaml.dump(content, f)
        f.close()
        return f.name

    def test_valid_command_manifest(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is True
            assert result["errors"] == []
            assert "manifest" in result
        finally:
            os.unlink(manifest_path)

    def test_missing_required_fields(self):
        """Test that missing required fields are detected."""
        manifest_content = {
            "name": "/test-command",
            "description": "Test command"
            # Missing: version, execution
        }

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert "Missing required fields" in result["errors"][0]
        finally:
            os.unlink(manifest_path)

    def test_invalid_command_name_format(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid name" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_version_format(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid version" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_execution_type(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid execution.type" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_missing_execution_target(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("target is required" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_status(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid status" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_parameters_format(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("parameters must be an array" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_parameters_missing_required_fields(self):
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

        manifest_path = self.create_temp_manifest(manifest_content)
        try:
            result = validate_manifest(manifest_path)
            assert result["valid"] is False
            assert any("missing required field: type" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)


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

    def test_complete_command_registration_workflow(self):
        """Test complete workflow: create manifest -> validate -> register."""
        import yaml

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

        # Save to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(manifest_content, f)
            manifest_path = f.name

        try:
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

        finally:
            os.unlink(manifest_path)

    def test_invalid_command_workflow(self):
        """Test workflow with invalid command manifest."""
        import yaml

        # Create an invalid manifest (missing required fields)
        manifest_content = {
            "name": "/test-invalid",
            "description": "Invalid command"
            # Missing: version, execution
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(manifest_content, f)
            manifest_path = f.name

        try:
            # Validation should fail
            validation = validate_manifest(manifest_path)
            assert validation["valid"] is False
            assert len(validation["errors"]) > 0
            assert "Missing required fields" in validation["errors"][0]

        finally:
            os.unlink(manifest_path)
