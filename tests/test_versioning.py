"""
Unit tests for betty.versioning module.

Tests semantic version parsing, comparison, constraint satisfaction,
and version bumping utilities.
"""

import pytest
from betty.versioning import (
    parse_version,
    compare,
    satisfies,
    next_version,
    is_monotonic_increase,
    VersionError,
)


class TestParseVersion:
    """Tests for parse_version function."""

    def test_parse_simple_version(self):
        """Test parsing a simple semantic version."""
        major, minor, patch, pre = parse_version("1.2.3")
        assert major == 1
        assert minor == 2
        assert patch == 3
        assert pre is None

    def test_parse_version_with_prerelease(self):
        """Test parsing version with prerelease tag."""
        major, minor, patch, pre = parse_version("1.0.0-alpha")
        assert major == 1
        assert minor == 0
        assert patch == 0
        assert pre == "alpha"

    def test_parse_version_with_complex_prerelease(self):
        """Test parsing version with complex prerelease tag."""
        major, minor, patch, pre = parse_version("2.0.0-beta.1")
        assert major == 2
        assert minor == 0
        assert patch == 0
        assert pre == "beta.1"

    def test_parse_version_with_build_metadata(self):
        """Test parsing version with build metadata (ignored)."""
        major, minor, patch, pre = parse_version("1.0.0+build.123")
        assert major == 1
        assert minor == 0
        assert patch == 0
        assert pre is None

    def test_parse_version_with_prerelease_and_build(self):
        """Test parsing version with both prerelease and build metadata."""
        major, minor, patch, pre = parse_version("1.0.0-rc.1+build.456")
        assert major == 1
        assert minor == 0
        assert patch == 0
        assert pre == "rc.1"

    def test_parse_empty_version_raises_error(self):
        """Test that empty version string raises error."""
        with pytest.raises(VersionError, match="cannot be empty"):
            parse_version("")

    def test_parse_invalid_version_raises_error(self):
        """Test that invalid version format raises error."""
        with pytest.raises(VersionError, match="Invalid semantic version"):
            parse_version("1.2")

        with pytest.raises(VersionError, match="Invalid semantic version"):
            parse_version("v1.2.3")

        with pytest.raises(VersionError, match="Invalid semantic version"):
            parse_version("1.2.3.4")


class TestCompare:
    """Tests for compare function."""

    def test_compare_equal_versions(self):
        """Test comparing equal versions."""
        assert compare("1.0.0", "1.0.0") == 0
        assert compare("2.5.10", "2.5.10") == 0

    def test_compare_different_major(self):
        """Test comparing versions with different major numbers."""
        assert compare("1.0.0", "2.0.0") == -1
        assert compare("2.0.0", "1.0.0") == 1

    def test_compare_different_minor(self):
        """Test comparing versions with different minor numbers."""
        assert compare("1.1.0", "1.2.0") == -1
        assert compare("1.2.0", "1.1.0") == 1

    def test_compare_different_patch(self):
        """Test comparing versions with different patch numbers."""
        assert compare("1.0.1", "1.0.2") == -1
        assert compare("1.0.2", "1.0.1") == 1

    def test_compare_prerelease_vs_stable(self):
        """Test that prerelease < stable version."""
        assert compare("1.0.0-alpha", "1.0.0") == -1
        assert compare("1.0.0", "1.0.0-alpha") == 1

    def test_compare_different_prerelease(self):
        """Test comparing different prerelease versions."""
        assert compare("1.0.0-alpha", "1.0.0-beta") == -1
        assert compare("1.0.0-beta", "1.0.0-alpha") == 1
        assert compare("1.0.0-alpha", "1.0.0-alpha") == 0


class TestSatisfies:
    """Tests for satisfies function."""

    def test_satisfies_exact_match(self):
        """Test exact version matching."""
        assert satisfies("1.2.3", "1.2.3") is True
        assert satisfies("1.2.3", "=1.2.3") is True
        assert satisfies("1.2.3", "1.2.4") is False

    def test_satisfies_greater_than(self):
        """Test greater than constraint."""
        assert satisfies("2.0.0", ">1.0.0") is True
        assert satisfies("1.0.0", ">1.0.0") is False
        assert satisfies("1.0.1", ">1.0.0") is True

    def test_satisfies_greater_than_or_equal(self):
        """Test greater than or equal constraint."""
        assert satisfies("1.0.0", ">=1.0.0") is True
        assert satisfies("1.0.1", ">=1.0.0") is True
        assert satisfies("0.9.9", ">=1.0.0") is False

    def test_satisfies_less_than(self):
        """Test less than constraint."""
        assert satisfies("0.9.0", "<1.0.0") is True
        assert satisfies("1.0.0", "<1.0.0") is False
        assert satisfies("1.0.1", "<1.0.0") is False

    def test_satisfies_less_than_or_equal(self):
        """Test less than or equal constraint."""
        assert satisfies("1.0.0", "<=1.0.0") is True
        assert satisfies("0.9.9", "<=1.0.0") is True
        assert satisfies("1.0.1", "<=1.0.0") is False

    def test_satisfies_range(self):
        """Test range constraint (space-separated)."""
        assert satisfies("1.5.0", ">=1.0.0 <2.0.0") is True
        assert satisfies("2.0.0", ">=1.0.0 <2.0.0") is False
        assert satisfies("0.9.0", ">=1.0.0 <2.0.0") is False

    def test_satisfies_caret(self):
        """Test caret constraint (^x.y.z)."""
        # ^1.2.3 allows >=1.2.3 <2.0.0
        assert satisfies("1.2.3", "^1.2.3") is True
        assert satisfies("1.2.4", "^1.2.3") is True
        assert satisfies("1.3.0", "^1.2.3") is True
        assert satisfies("2.0.0", "^1.2.3") is False
        assert satisfies("1.2.2", "^1.2.3") is False

        # ^0.2.3 allows >=0.2.3 <0.3.0
        assert satisfies("0.2.3", "^0.2.3") is True
        assert satisfies("0.2.4", "^0.2.3") is True
        assert satisfies("0.3.0", "^0.2.3") is False

    def test_satisfies_tilde(self):
        """Test tilde constraint (~x.y.z)."""
        # ~1.2.3 allows >=1.2.3 <1.3.0
        assert satisfies("1.2.3", "~1.2.3") is True
        assert satisfies("1.2.4", "~1.2.3") is True
        assert satisfies("1.3.0", "~1.2.3") is False
        assert satisfies("1.2.2", "~1.2.3") is False

    def test_satisfies_empty_constraint_raises_error(self):
        """Test that empty constraint raises error."""
        with pytest.raises(VersionError, match="cannot be empty"):
            satisfies("1.0.0", "")


class TestNextVersion:
    """Tests for next_version function."""

    def test_next_version_patch(self):
        """Test incrementing patch version."""
        assert next_version("1.2.3", "patch") == "1.2.4"
        assert next_version("0.0.1", "patch") == "0.0.2"

    def test_next_version_minor(self):
        """Test incrementing minor version."""
        assert next_version("1.2.3", "minor") == "1.3.0"
        assert next_version("0.1.5", "minor") == "0.2.0"

    def test_next_version_major(self):
        """Test incrementing major version."""
        assert next_version("1.2.3", "major") == "2.0.0"
        assert next_version("0.5.7", "major") == "1.0.0"

    def test_next_version_strips_prerelease(self):
        """Test that prerelease tags are stripped when incrementing."""
        assert next_version("1.0.0-alpha", "patch") == "1.0.1"
        assert next_version("1.0.0-beta", "minor") == "1.1.0"
        assert next_version("1.0.0-rc.1", "major") == "2.0.0"

    def test_next_version_unknown_level_raises_error(self):
        """Test that unknown level raises error."""
        with pytest.raises(VersionError, match="Unknown version level"):
            next_version("1.0.0", "unknown")


class TestIsMonotonicIncrease:
    """Tests for is_monotonic_increase function."""

    def test_is_monotonic_increase_true(self):
        """Test monotonic increases."""
        assert is_monotonic_increase("0.1.0", "0.2.0") is True
        assert is_monotonic_increase("1.0.0", "2.0.0") is True
        assert is_monotonic_increase("1.2.3", "1.2.4") is True

    def test_is_monotonic_increase_false_downgrade(self):
        """Test that downgrades are not monotonic."""
        assert is_monotonic_increase("2.0.0", "1.0.0") is False
        assert is_monotonic_increase("1.5.0", "1.4.9") is False

    def test_is_monotonic_increase_false_equal(self):
        """Test that equal versions are not monotonic increases."""
        assert is_monotonic_increase("1.0.0", "1.0.0") is False
        assert is_monotonic_increase("2.5.7", "2.5.7") is False

    def test_is_monotonic_increase_prerelease_to_stable(self):
        """Test that prerelease -> stable is monotonic."""
        assert is_monotonic_increase("1.0.0-alpha", "1.0.0") is True
        assert is_monotonic_increase("1.0.0", "1.0.0-alpha") is False


class TestVersionComparisonsIntegration:
    """Integration tests for version operations."""

    def test_version_progression(self):
        """Test a typical version progression."""
        versions = ["0.1.0", "0.2.0", "0.3.0", "1.0.0", "1.1.0", "2.0.0"]

        for i in range(len(versions) - 1):
            # Each version should be less than the next
            assert compare(versions[i], versions[i + 1]) == -1
            # Each version should be monotonically increasing
            assert is_monotonic_increase(versions[i], versions[i + 1]) is True

    def test_constraint_satisfaction_scenarios(self):
        """Test common constraint scenarios."""
        # Typical development workflow
        assert satisfies("0.1.0", ">=0.0.0 <1.0.0") is True
        assert satisfies("0.9.9", ">=0.0.0 <1.0.0") is True
        assert satisfies("1.0.0", ">=0.0.0 <1.0.0") is False

        # Stable API (caret)
        assert satisfies("1.2.5", "^1.2.0") is True
        assert satisfies("1.5.0", "^1.2.0") is True
        assert satisfies("2.0.0", "^1.2.0") is False

        # Patch updates only (tilde)
        assert satisfies("1.2.3", "~1.2.0") is True
        assert satisfies("1.2.9", "~1.2.0") is True
        assert satisfies("1.3.0", "~1.2.0") is False

    def test_next_version_progression(self):
        """Test version bumping progression."""
        base = "1.0.0"

        # Patch releases
        v1 = next_version(base, "patch")
        assert v1 == "1.0.1"

        # Minor release
        v2 = next_version(v1, "minor")
        assert v2 == "1.1.0"

        # Major release
        v3 = next_version(v2, "major")
        assert v3 == "2.0.0"

        # All should be monotonically increasing
        assert is_monotonic_increase(base, v1) is True
        assert is_monotonic_increase(v1, v2) is True
        assert is_monotonic_increase(v2, v3) is True


class TestRegistryVersionEnforcement:
    """Integration tests for registry version enforcement."""

    def test_registry_requires_version_field(self):
        """Test that registry requires explicit version field."""
        from betty.errors import RegistryError
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "test.skill",
            # Missing version field
        }
        registry_data = {"skills": []}

        with pytest.raises(RegistryError, match="missing required 'version' field"):
            enforce_version_constraints(manifest, registry_data)

    def test_registry_rejects_active_version_overwrite(self):
        """Test that registry refuses to overwrite active versions."""
        from betty.errors import VersionConflictError
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "test.skill",
            "version": "1.0.0",
            "status": "active"
        }
        registry_data = {
            "skills": [
                {
                    "name": "test.skill",
                    "version": "1.0.0",
                    "status": "active"
                }
            ]
        }

        with pytest.raises(VersionConflictError, match="Cannot overwrite active version"):
            enforce_version_constraints(manifest, registry_data)

    def test_registry_rejects_downgrades(self):
        """Test that registry enforces monotonic version increases."""
        from betty.errors import VersionConflictError
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "test.skill",
            "version": "0.9.0",  # Downgrade
            "status": "draft"
        }
        registry_data = {
            "skills": [
                {
                    "name": "test.skill",
                    "version": "1.0.0",
                    "status": "draft"
                }
            ]
        }

        with pytest.raises(VersionConflictError, match="Version downgrade"):
            enforce_version_constraints(manifest, registry_data)

    def test_registry_allows_draft_same_version(self):
        """Test that registry allows same version for draft skills."""
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "test.skill",
            "version": "1.0.0",
            "status": "draft"
        }
        registry_data = {
            "skills": [
                {
                    "name": "test.skill",
                    "version": "1.0.0",
                    "status": "draft"
                }
            ]
        }

        # Should not raise
        enforce_version_constraints(manifest, registry_data)

    def test_registry_allows_version_increase(self):
        """Test that registry allows monotonic version increases."""
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "test.skill",
            "version": "1.1.0",
            "status": "active"
        }
        registry_data = {
            "skills": [
                {
                    "name": "test.skill",
                    "version": "1.0.0",
                    "status": "active"
                }
            ]
        }

        # Should not raise
        enforce_version_constraints(manifest, registry_data)

    def test_registry_allows_new_entry(self):
        """Test that registry allows new entries."""
        from betty.skills.registry.update.registry_update import enforce_version_constraints

        manifest = {
            "name": "new.skill",
            "version": "0.1.0",
            "status": "draft"
        }
        registry_data = {"skills": []}

        # Should not raise
        enforce_version_constraints(manifest, registry_data)


class TestWorkflowVersionConstraints:
    """Integration tests for workflow version constraint validation."""

    def test_workflow_requires_version_constraint(self):
        """Test that workflow validation requires version constraints on skill steps."""
        import tempfile
        import os
        import yaml
        from betty.skills.workflow.validate.workflow_validate import validate_workflow

        workflow_data = {
            "name": "test-workflow",
            "version": "1.0.0",
            "steps": [
                {
                    "skill": "test.skill",
                    # Missing version constraint
                    "args": []
                }
            ]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(workflow_data, f)
            temp_path = f.name

        try:
            result = validate_workflow(temp_path)
            assert result["valid"] is False
            assert any("missing 'version' constraint" in err for err in result["errors"])
        finally:
            os.unlink(temp_path)

    def test_workflow_rejects_invalid_version_constraint(self):
        """Test that workflow validation rejects invalid version constraints."""
        import tempfile
        import os
        import yaml
        from betty.skills.workflow.validate.workflow_validate import validate_workflow

        workflow_data = {
            "name": "test-workflow",
            "version": "1.0.0",
            "steps": [
                {
                    "skill": "nonexistent.skill",
                    "version": ">=1.0.0 <2.0.0",
                    "args": []
                }
            ]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(workflow_data, f)
            temp_path = f.name

        try:
            result = validate_workflow(temp_path)
            # Should fail version resolution
            assert result["valid"] is False
            assert any("No version" in err for err in result["errors"])
        finally:
            os.unlink(temp_path)

    def test_workflow_creates_lockfile_on_success(self):
        """Test that workflow validation creates lockfile on successful validation."""
        import tempfile
        import os
        import yaml
        import json
        from betty.skills.workflow.validate.workflow_validate import validate_workflow

        # Create a workflow that references an existing skill
        workflow_data = {
            "name": "test-workflow",
            "version": "1.0.0",
            "steps": [
                {
                    "skill": "test.hello",  # This exists in the registry
                    "version": ">=0.0.0",
                    "args": []
                }
            ]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(workflow_data, f)
            temp_path = f.name

        try:
            result = validate_workflow(temp_path)

            # Check if validation succeeded
            if result["valid"]:
                # Lockfile should be created
                assert "lockfile" in result
                assert os.path.exists(result["lockfile"])

                # Verify lockfile contents
                with open(result["lockfile"], 'r') as lf:
                    lockfile_data = json.load(lf)

                assert lockfile_data["workflow"] == "test-workflow"
                assert "timestamp" in lockfile_data
                assert "resolved" in lockfile_data
                assert isinstance(lockfile_data["resolved"], list)

                # Cleanup lockfile
                os.unlink(result["lockfile"])
        finally:
            os.unlink(temp_path)
