#!/usr/bin/env python3
"""
Tests for expanded smart mode critical pattern detection
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from risk_review import RiskReviewer


class TestSmartModeCriticalPatterns:
    """Test expanded critical pattern detection (12 patterns)"""

    def test_detects_hardcoded_credentials(self):
        """Test detection of hardcoded credentials"""
        content = "password = 'admin123'"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert 'Hardcoded credentials' in result['issues'][0]

    def test_detects_unencrypted_transmission(self):
        """Test detection of unencrypted transmission"""
        content = "Using http:// for data transmission"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('Unencrypted' in issue for issue in result['issues'])

    def test_detects_sql_injection(self):
        """Test detection of SQL injection vectors"""
        content = "sql_query = 'SELECT * FROM users WHERE id = ' + user_input"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('SQL injection' in issue for issue in result['issues'])

    def test_detects_command_injection(self):
        """Test detection of command injection vectors"""
        content = "os.system('rm -rf ' + user_input)"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('command injection' in issue for issue in result['issues'])

    def test_detects_missing_authentication(self):
        """Test detection of missing authentication"""
        content = "public_access enabled for all endpoints"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('authentication' in issue.lower() for issue in result['issues'])

    def test_detects_disabled_security_features(self):
        """Test detection of disabled security features"""
        content = "disable_ssl_verification = true"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('disabled' in issue.lower() for issue in result['issues'])

    def test_detects_debug_mode(self):
        """Test detection of debug mode in production"""
        content = "debug_mode = true"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('debug' in issue.lower() for issue in result['issues'])

    def test_detects_missing_logging(self):
        """Test detection of missing audit logging"""
        content = "System configured without_logging"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('logging' in issue.lower() for issue in result['issues'])

    def test_detects_weak_crypto(self):
        """Test detection of weak cryptographic algorithms"""
        content = "Using MD5 hash for password storage"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('weak' in issue.lower() or 'cryptographic' in issue.lower() for issue in result['issues'])

    def test_detects_permissive_access(self):
        """Test detection of overly permissive access controls"""
        content = "chmod 777 /data/sensitive"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('permissive' in issue.lower() or 'access' in issue.lower() for issue in result['issues'])

    def test_detects_missing_backup(self):
        """Test detection of missing backup procedures"""
        content = "Database configured without_backup"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert any('backup' in issue.lower() for issue in result['issues'])

    def test_skips_negated_patterns(self):
        """Test that negated patterns are not flagged"""
        content = "Policy requires: must not use http:// for sensitive data"
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        # Should not flag because "must not use" negates the issue
        assert result['has_critical'] is False

    def test_multiple_critical_issues(self):
        """Test detection of multiple critical issues"""
        content = """
        password = "admin123"
        Using http:// endpoints
        debug_mode = true
        """
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is True
        assert len(result['findings']) >= 3  # At least 3 critical issues

    def test_no_false_positives_on_compliant_content(self):
        """Test no false positives on compliant content"""
        content = """
        Authentication: OAuth 2.0 with JWT
        Encryption: TLS 1.3 for all data in transit
        Logging: Comprehensive audit trail
        Access: Role-based access control (RBAC)
        Backup: Daily automated backups with 30-day retention
        """
        reviewer = RiskReviewer(mode='smart')
        result = reviewer._check_critical_patterns(content)
        assert result['has_critical'] is False
