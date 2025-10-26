"""
Tests for hook.define and hook.register skills - validates hook event triggers and workflows.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import the hook modules
from betty.skills.hook.define.hook_define import (
    define_hook,
    create_hook_config,
    add_hook_to_config,
    load_existing_hooks,
    save_hooks_config,
    VALID_EVENTS
)
from betty.skills.hook.register.hook_register import (
    validate_manifest as validate_hook_manifest,
    load_hook_manifest,
    update_hook_registry,
    load_hook_registry,
    HookValidationError,
    HookRegistryError
)
from betty.enums import HookEvent, HookStatus
from betty.validation import validate_hook_name, validate_hook_event, ValidationError


class TestHookNameValidation:
    """Tests for hook name validation."""

    def test_valid_hook_names(self):
        """Test that valid hook names pass validation."""
        valid_names = [
            "test-hook",
            "validate-openapi-spec",
            "pre-commit-check",
            "test_hook",
            "hook123",
            "my-awesome-hook",
        ]
        for name in valid_names:
            validate_hook_name(name)  # Should not raise

    def test_invalid_hook_names(self):
        """Test that invalid hook names raise ValidationError."""
        invalid_names = [
            "",  # Empty
            "Hook-Name",  # Uppercase
            "hook name",  # Space
            "hook@test",  # Invalid character
            "123hook",  # Starts with number
        ]
        for name in invalid_names:
            with pytest.raises(ValidationError):
                validate_hook_name(name)


class TestHookEventValidation:
    """Tests for hook event type validation."""

    def test_valid_hook_events(self):
        """Test that valid hook events pass validation."""
        valid_events = [
            "on_file_edit",
            "on_file_save",
            "on_commit",
            "on_push",
            "on_tool_use",
            "on_agent_start",
            "on_workflow_end"
        ]
        for event in valid_events:
            validate_hook_event(event)  # Should not raise

    def test_invalid_hook_events(self):
        """Test that invalid hook events raise ValidationError."""
        invalid_events = [
            "on_invalid_event",
            "on_file_delete",
            "invalid",
            "",
            "ON_FILE_EDIT",  # Wrong case
        ]
        for event in invalid_events:
            with pytest.raises(ValidationError):
                validate_hook_event(event)


class TestHookManifestLoading:
    """Tests for loading hook manifests from YAML files."""

    def test_load_valid_hook_manifest(self):
        """Test loading a valid hook manifest."""
        manifest_path = "examples/test-hook.yaml"
        if os.path.exists(manifest_path):
            manifest = load_hook_manifest(manifest_path)
            assert manifest is not None
            assert manifest["name"] == "test-validation-hook"
            assert manifest["version"] == "0.1.0"
            assert manifest["event"] == "on_file_edit"
            assert "command" in manifest

    def test_load_nonexistent_hook_manifest(self):
        """Test that loading nonexistent file raises error."""
        with pytest.raises(HookValidationError, match="not found"):
            load_hook_manifest("/nonexistent/hook.yaml")

    def test_load_invalid_hook_yaml(self):
        """Test that loading invalid YAML raises error."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content:\n  - missing bracket")
            temp_path = f.name

        try:
            with pytest.raises(HookValidationError, match="Failed to parse YAML"):
                load_hook_manifest(temp_path)
        finally:
            os.unlink(temp_path)


class TestHookManifestValidation:
    """Tests for comprehensive hook manifest validation."""

    def create_temp_hook_manifest(self, content):
        """Helper to create temporary hook manifest file."""
        import yaml
        f = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False)
        yaml.dump(content, f)
        f.close()
        return f.name

    def test_valid_hook_manifest(self):
        """Test validation of a complete valid hook manifest."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py {file_path}",
            "blocking": True,
            "timeout": 30000,
            "status": "active"
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is True
            assert result["errors"] == []
            assert "manifest" in result
        finally:
            os.unlink(manifest_path)

    def test_missing_required_fields(self):
        """Test that missing required fields are detected."""
        manifest_content = {
            "name": "test-hook",
            "description": "Test hook"
            # Missing: version, event, command
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert "Missing required fields" in result["errors"][0]
        finally:
            os.unlink(manifest_path)

    def test_invalid_hook_name_format(self):
        """Test that invalid name format is detected."""
        manifest_content = {
            "name": "Invalid-Hook-Name",  # Uppercase not allowed
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py"
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid name" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_event_type(self):
        """Test that invalid event type is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_invalid_event",
            "command": "python test.py"
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid event" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_empty_command(self):
        """Test that empty command is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": ""  # Empty command
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("command cannot be empty" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_blocking_type(self):
        """Test that invalid blocking type is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py",
            "blocking": "yes"  # Should be boolean
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("blocking must be a boolean" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_timeout(self):
        """Test that invalid timeout is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py",
            "timeout": -1000  # Negative timeout
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("timeout must be a positive number" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_status(self):
        """Test that invalid status is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py",
            "status": "invalid_status"
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("Invalid status" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)

    def test_invalid_when_pattern(self):
        """Test that invalid when.pattern is detected."""
        manifest_content = {
            "name": "test-hook",
            "version": "1.0.0",
            "description": "Test hook",
            "event": "on_file_edit",
            "command": "python test.py",
            "when": {
                "pattern": ""  # Empty pattern
            }
        }

        manifest_path = self.create_temp_hook_manifest(manifest_content)
        try:
            result = validate_hook_manifest(manifest_path)
            assert result["valid"] is False
            assert any("when.pattern must be a non-empty string" in error for error in result["errors"])
        finally:
            os.unlink(manifest_path)


class TestHookConfigCreation:
    """Tests for creating hook configurations."""

    def test_create_basic_hook_config(self):
        """Test creating a basic hook configuration."""
        config = create_hook_config(
            event="on_file_edit",
            command="python test.py",
            blocking=True,
            timeout=30000
        )

        assert config is not None
        assert "name" in config
        assert config["command"] == "python test.py"
        assert config["blocking"] is True
        assert config["timeout"] == 30000
        assert "description" in config

    def test_create_hook_config_with_pattern(self):
        """Test creating hook config with file pattern."""
        config = create_hook_config(
            event="on_file_edit",
            command="python test.py",
            pattern="*.yaml",
            blocking=True,
            timeout=30000
        )

        assert config is not None
        assert "when" in config
        assert config["when"]["pattern"] == "*.yaml"

    def test_create_hook_config_with_description(self):
        """Test creating hook config with custom description."""
        description = "Custom hook description"
        config = create_hook_config(
            event="on_file_edit",
            command="python test.py",
            description=description
        )

        assert config["description"] == description


class TestHookConfigManagement:
    """Tests for managing hook configurations."""

    def test_add_new_hook_to_config(self):
        """Test adding a new hook to configuration."""
        config = {"hooks": {}}
        hook_config = {
            "name": "test-hook",
            "command": "python test.py",
            "blocking": True,
            "timeout": 30000
        }

        updated_config = add_hook_to_config(config, "on_file_edit", hook_config)

        assert "on_file_edit" in updated_config["hooks"]
        assert len(updated_config["hooks"]["on_file_edit"]) == 1
        assert updated_config["hooks"]["on_file_edit"][0]["name"] == "test-hook"

    def test_update_existing_hook_in_config(self):
        """Test updating an existing hook in configuration."""
        config = {
            "hooks": {
                "on_file_edit": [
                    {
                        "name": "test-hook",
                        "command": "python old_test.py",
                        "blocking": True,
                        "timeout": 30000
                    }
                ]
            }
        }

        # Update with new command
        hook_config = {
            "name": "test-hook",
            "command": "python new_test.py",
            "blocking": False,
            "timeout": 60000
        }

        updated_config = add_hook_to_config(config, "on_file_edit", hook_config)

        assert len(updated_config["hooks"]["on_file_edit"]) == 1
        assert updated_config["hooks"]["on_file_edit"][0]["command"] == "python new_test.py"
        assert updated_config["hooks"]["on_file_edit"][0]["blocking"] is False

    def test_add_multiple_hooks_to_same_event(self):
        """Test adding multiple hooks to the same event."""
        config = {"hooks": {}}

        hook1 = {"name": "hook1", "command": "python test1.py", "blocking": True, "timeout": 30000}
        hook2 = {"name": "hook2", "command": "python test2.py", "blocking": False, "timeout": 60000}

        config = add_hook_to_config(config, "on_file_edit", hook1)
        config = add_hook_to_config(config, "on_file_edit", hook2)

        assert len(config["hooks"]["on_file_edit"]) == 2
        hook_names = [h["name"] for h in config["hooks"]["on_file_edit"]]
        assert "hook1" in hook_names
        assert "hook2" in hook_names


class TestHookRegistry:
    """Tests for hook registry operations."""

    def test_load_hook_registry(self):
        """Test loading hook registry."""
        registry = load_hook_registry()
        assert registry is not None
        assert "registry_version" in registry
        assert "hooks" in registry

    def test_update_hook_registry(self):
        """Test updating hook registry with new hook."""
        manifest = {
            "name": "test-registry-hook",
            "version": "1.0.0",
            "description": "Test registry update",
            "event": "on_file_edit",
            "command": "python test.py {file_path}",
            "blocking": True,
            "timeout": 30000,
            "status": "draft",
            "tags": ["test"]
        }

        result = update_hook_registry(manifest)
        assert result is True

        # Verify it was added
        registry = load_hook_registry()
        hook_names = [hook["name"] for hook in registry["hooks"]]
        assert "test-registry-hook" in hook_names

    def test_update_existing_hook_in_registry(self):
        """Test updating an existing hook in registry."""
        # First, add a hook
        manifest = {
            "name": "test-update-hook",
            "version": "1.0.0",
            "description": "Original description",
            "event": "on_file_edit",
            "command": "python old_test.py",
            "blocking": True,
            "timeout": 30000
        }
        update_hook_registry(manifest)

        # Now update it
        manifest["version"] = "1.0.1"
        manifest["description"] = "Updated description"
        manifest["command"] = "python new_test.py"
        result = update_hook_registry(manifest)
        assert result is True

        # Verify it was updated
        registry = load_hook_registry()
        updated_hook = next(
            (hook for hook in registry["hooks"] if hook["name"] == "test-update-hook"),
            None
        )
        assert updated_hook is not None
        assert updated_hook["version"] == "1.0.1"
        assert updated_hook["description"] == "Updated description"
        assert updated_hook["command"] == "python new_test.py"


class TestHookEventTriggers:
    """Tests for simulating hook event triggers."""

    def test_on_file_edit_trigger(self):
        """Test hook trigger on file edit event."""
        # Create a hook for file edit
        hook_config = create_hook_config(
            event="on_file_edit",
            command="python validate.py {file_path}",
            pattern="*.yaml",
            blocking=True,
            timeout=30000
        )

        # Verify hook is configured for correct event
        config = {"hooks": {}}
        config = add_hook_to_config(config, "on_file_edit", hook_config)

        assert "on_file_edit" in config["hooks"]
        assert config["hooks"]["on_file_edit"][0]["blocking"] is True

    def test_on_file_save_trigger(self):
        """Test hook trigger on file save event."""
        hook_config = create_hook_config(
            event="on_file_save",
            command="python format.py {file_path}",
            blocking=False,
            timeout=10000
        )

        config = {"hooks": {}}
        config = add_hook_to_config(config, "on_file_save", hook_config)

        assert "on_file_save" in config["hooks"]
        assert config["hooks"]["on_file_save"][0]["blocking"] is False

    def test_on_commit_trigger(self):
        """Test hook trigger on commit event."""
        hook_config = create_hook_config(
            event="on_commit",
            command="python pre_commit_check.py",
            blocking=True,
            timeout=60000,
            description="Run pre-commit validation"
        )

        config = {"hooks": {}}
        config = add_hook_to_config(config, "on_commit", hook_config)

        assert "on_commit" in config["hooks"]
        assert config["hooks"]["on_commit"][0]["timeout"] == 60000

    def test_on_push_trigger(self):
        """Test hook trigger on push event."""
        hook_config = create_hook_config(
            event="on_push",
            command="python pre_push_validation.py",
            blocking=True,
            timeout=120000,
            description="Validate before push"
        )

        config = {"hooks": {}}
        config = add_hook_to_config(config, "on_push", hook_config)

        assert "on_push" in config["hooks"]
        assert config["hooks"]["on_push"][0]["command"] == "python pre_push_validation.py"


class TestHookWorkflow:
    """Integration tests for complete hook workflow."""

    def test_complete_hook_registration_workflow(self):
        """Test complete workflow: create manifest -> validate -> register."""
        import yaml

        manifest_content = {
            "name": "test-workflow-hook",
            "version": "1.0.0",
            "description": "Test complete workflow",
            "event": "on_file_edit",
            "command": "python validate.py {file_path}",
            "when": {
                "pattern": "*.openapi.yaml"
            },
            "blocking": True,
            "timeout": 30000,
            "status": "active",
            "tags": ["test", "workflow", "openapi"]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(manifest_content, f)
            manifest_path = f.name

        try:
            # Step 1: Validate manifest
            validation = validate_hook_manifest(manifest_path)
            assert validation["valid"] is True
            assert validation["errors"] == []

            # Step 2: Register hook
            result = update_hook_registry(validation["manifest"])
            assert result is True

            # Step 3: Verify registration
            registry = load_hook_registry()
            hook = next(
                (h for h in registry["hooks"] if h["name"] == "test-workflow-hook"),
                None
            )
            assert hook is not None
            assert hook["version"] == "1.0.0"
            assert hook["event"] == "on_file_edit"
            assert hook["blocking"] is True
            assert hook["when"]["pattern"] == "*.openapi.yaml"

        finally:
            os.unlink(manifest_path)

    def test_invalid_hook_workflow(self):
        """Test workflow with invalid hook manifest."""
        import yaml

        manifest_content = {
            "name": "test-invalid-hook",
            "description": "Invalid hook"
            # Missing: version, event, command
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(manifest_content, f)
            manifest_path = f.name

        try:
            # Validation should fail
            validation = validate_hook_manifest(manifest_path)
            assert validation["valid"] is False
            assert len(validation["errors"]) > 0
            assert "Missing required fields" in validation["errors"][0]

        finally:
            os.unlink(manifest_path)

    @patch('hook_define.create_hooks_directory')
    @patch('hook_define.save_hooks_config')
    @patch('hook_define.load_existing_hooks')
    def test_define_hook_workflow(self, mock_load, mock_save, mock_create_dir):
        """Test the define_hook workflow for creating hooks programmatically."""
        # Mock the directory and file operations
        mock_create_dir.return_value = Path("/tmp/.claude")
        mock_load.return_value = {"hooks": {}}
        mock_save.return_value = None

        # Define a hook
        result = define_hook(
            event="on_file_edit",
            command="python validate.py {file_path}",
            pattern="*.yaml",
            blocking=True,
            timeout=30000,
            description="Test hook definition"
        )

        # Verify result
        assert result is not None
        assert "hook_config" in result
        assert result["event"] == "on_file_edit"
        assert result["hook_config"]["blocking"] is True
        assert result["hook_config"]["when"]["pattern"] == "*.yaml"

        # Verify save was called
        mock_save.assert_called_once()


class TestHookPatternMatching:
    """Tests for hook pattern matching scenarios."""

    def test_hook_with_yaml_pattern(self):
        """Test hook configured to match YAML files."""
        hook_config = create_hook_config(
            event="on_file_edit",
            command="python validate.py {file_path}",
            pattern="*.yaml"
        )

        assert hook_config["when"]["pattern"] == "*.yaml"

    def test_hook_with_openapi_pattern(self):
        """Test hook configured to match OpenAPI spec files."""
        hook_config = create_hook_config(
            event="on_file_edit",
            command="python validate_openapi.py {file_path}",
            pattern="*.openapi.yaml"
        )

        assert hook_config["when"]["pattern"] == "*.openapi.yaml"

    def test_hook_without_pattern(self):
        """Test hook configured to trigger on all files."""
        hook_config = create_hook_config(
            event="on_file_edit",
            command="python validate_all.py {file_path}"
        )

        assert "when" not in hook_config


class TestHookBlockingBehavior:
    """Tests for hook blocking behavior."""

    def test_blocking_hook_on_failure(self):
        """Test that blocking hook should stop operation on failure."""
        hook_config = create_hook_config(
            event="on_commit",
            command="python validate.py",
            blocking=True
        )

        assert hook_config["blocking"] is True

    def test_non_blocking_hook_on_failure(self):
        """Test that non-blocking hook should allow operation to continue."""
        hook_config = create_hook_config(
            event="on_commit",
            command="python lint.py",
            blocking=False
        )

        assert hook_config["blocking"] is False

    def test_hook_timeout_configuration(self):
        """Test hook timeout is properly configured."""
        hook_config = create_hook_config(
            event="on_file_save",
            command="python format.py",
            timeout=5000
        )

        assert hook_config["timeout"] == 5000
