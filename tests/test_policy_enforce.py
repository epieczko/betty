#!/usr/bin/env python3
"""
Unit tests for policy.enforce skill

Tests config loading, rule engine, and manifest validation.
"""

import pytest
import sys
import tempfile
import yaml
from pathlib import Path

# Add betty to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from betty.skills.policy.enforce.policy_enforce import (
    validate_name_format,
    validate_version_format,
    validate_status,
    validate_permissions,
    load_policy_profile,
    _load_policy_config,
    PolicyEnforcementError
)


class TestNameValidation:
    """Test name format validation"""

    def test_valid_names(self):
        """Test valid name formats"""
        valid_names = [
            'test',
            'my.skill',
            'api.validate',
            'artifact.review',
            'test123',
            'a.b.c.d'
        ]
        for name in valid_names:
            violation = validate_name_format(name)
            assert violation is None, f"'{name}' should be valid"

    def test_invalid_uppercase(self):
        """Test rejection of uppercase names"""
        violation = validate_name_format("Test.Skill")
        assert violation is not None
        assert 'uppercase' in violation.message.lower()

    def test_invalid_spaces(self):
        """Test rejection of names with spaces"""
        violation = validate_name_format("test skill")
        assert violation is not None
        assert 'spaces' in violation.message.lower()

    def test_invalid_format(self):
        """Test rejection of invalid formats"""
        invalid_names = [
            '.test',  # starts with dot
            'test.',  # ends with dot
            '',  # empty
        ]
        for name in invalid_names:
            violation = validate_name_format(name)
            assert violation is not None, f"'{name}' should be invalid"


class TestVersionValidation:
    """Test semantic versioning validation"""

    def test_valid_versions(self):
        """Test valid semantic versions"""
        valid_versions = [
            '1.0.0',
            '0.1.0',
            '10.20.30',
            '1.0.0-beta'
        ]
        for version in valid_versions:
            violation = validate_version_format(version)
            assert violation is None, f"'{version}' should be valid"

    def test_invalid_versions(self):
        """Test invalid version formats"""
        invalid_versions = [
            '1.0',  # missing patch
            'v1.0.0',  # has 'v' prefix
            '1',  # too short
            'latest',  # not a version
        ]
        for version in invalid_versions:
            violation = validate_version_format(version)
            assert violation is not None, f"'{version}' should be invalid"


class TestStatusValidation:
    """Test status field validation"""

    def test_valid_statuses(self):
        """Test valid status values"""
        valid_statuses = ['draft', 'active', 'deprecated', 'archived']
        config = _load_policy_config()
        for status in valid_statuses:
            violation = validate_status(status)
            assert violation is None, f"'{status}' should be valid"

    def test_invalid_status(self):
        """Test invalid status values"""
        violation = validate_status('invalid')
        assert violation is not None
        assert 'invalid' in violation.message.lower()

    def test_empty_status(self):
        """Test empty status"""
        violation = validate_status('')
        assert violation is not None


class TestPermissionsValidation:
    """Test permissions validation"""

    def test_valid_skill_permissions(self):
        """Test valid skill permissions"""
        manifest = {
            'entrypoints': [
                {'permissions': ['filesystem', 'network']},
                {'permissions': ['read', 'write']},
                {'permissions': ['filesystem:read', 'network:write']}
            ]
        }
        violations = validate_permissions(manifest, 'skill')
        assert len(violations) == 0

    def test_invalid_skill_permission(self):
        """Test invalid skill permission"""
        manifest = {
            'entrypoints': [
                {'permissions': ['invalid_permission']}
            ]
        }
        violations = validate_permissions(manifest, 'skill')
        assert len(violations) > 0
        assert 'invalid_permission' in violations[0].message

    def test_valid_agent_permissions(self):
        """Test valid agent permissions"""
        manifest = {
            'permissions': ['filesystem', 'network:read']
        }
        violations = validate_permissions(manifest, 'agent')
        assert len(violations) == 0

    def test_no_permissions(self):
        """Test manifest with no permissions"""
        manifest_skill = {}
        violations = validate_permissions(manifest_skill, 'skill')
        assert len(violations) == 0  # No permissions is valid


class TestPolicyProfileLoading:
    """Test policy profile loading"""

    def test_load_existing_profile(self):
        """Test loading an existing profile"""
        profile = load_policy_profile('betty-core')
        assert 'name' in profile
        assert 'rules' in profile
        assert profile['name'] == 'betty-core'

    def test_load_nonexistent_profile(self):
        """Test loading nonexistent profile raises error"""
        with pytest.raises(PolicyEnforcementError) as exc_info:
            load_policy_profile('nonexistent-profile-xyz')
        assert 'not found' in str(exc_info.value).lower()

    def test_profile_structure(self):
        """Test loaded profile has correct structure"""
        profile = load_policy_profile('betty-core')
        assert isinstance(profile, dict)
        assert 'name' in profile
        assert 'version' in profile
        assert 'rules' in profile
        assert isinstance(profile['rules'], list)


class TestConfigLoading:
    """Test policy configuration loading"""

    def test_config_loaded(self):
        """Test that config loads successfully"""
        config = _load_policy_config()
        assert 'allowed_permissions' in config
        assert 'allowed_statuses' in config
        assert 'valid_name_pattern' in config

    def test_config_has_defaults(self):
        """Test config contains expected defaults"""
        config = _load_policy_config()
        assert 'filesystem' in config['allowed_permissions']
        assert 'network' in config['allowed_permissions']
        assert 'active' in config['allowed_statuses']
        assert 'draft' in config['allowed_statuses']

    def test_config_cached(self):
        """Test that config is cached on subsequent loads"""
        config1 = _load_policy_config()
        config2 = _load_policy_config()
        # Should be the same object (cached)
        assert config1 is config2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
