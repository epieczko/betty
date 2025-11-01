#!/usr/bin/env python3
"""
Unit tests for risk.review skill

Tests security, privacy, operational, and compliance risk assessments.
"""

import sys
import pytest
from pathlib import Path

# Add parent directory to path to import risk_review module
sys.path.insert(0, str(Path(__file__).parent.parent))

from risk_review import (
    load_artifact,
    assess_security_risks,
    assess_privacy_risks,
    assess_operational_risks,
    assess_compliance_risks,
    calculate_overall_risk_score,
    determine_risk_rating,
    generate_remediation_plan,
    review_risk,
    POLICY_FRAMEWORKS
)


# Test fixtures directory
FIXTURES_DIR = Path(__file__).parent / "fixtures"


class TestLoadArtifact:
    """Test artifact loading functionality"""

    def test_load_valid_yaml_artifact(self):
        """Test loading a valid YAML artifact"""
        artifact_path = FIXTURES_DIR / "low-risk-artifact.yaml"
        content, data, file_format = load_artifact(artifact_path)

        assert content is not None
        assert len(content) > 0
        assert isinstance(data, dict)
        assert file_format == "yaml"
        assert "metadata" in data
        assert data["metadata"]["name"] == "secure-healthcare-platform"

    def test_load_nonexistent_artifact(self):
        """Test loading a non-existent artifact raises FileNotFoundError"""
        artifact_path = FIXTURES_DIR / "does-not-exist.yaml"
        with pytest.raises(FileNotFoundError):
            load_artifact(artifact_path)

    def test_load_invalid_yaml(self):
        """Test loading invalid YAML still returns content"""
        artifact_path = FIXTURES_DIR / "invalid-artifact.yaml"
        content, data, file_format = load_artifact(artifact_path)

        # Should still load content even if YAML parsing fails
        assert content is not None
        assert file_format == "yaml"
        # Data should be empty dict on parse failure
        assert data == {}


class TestSecurityRiskAssessment:
    """Test security risk assessment functionality"""

    def test_high_risk_security_issues(self):
        """Test detection of high-risk security issues"""
        content = """
        database_url: http://db.example.com:5432
        admin_password: hardcoded_admin123
        api_key: sk_live_1234567890abcdef
        No encryption or authentication mentioned
        """
        data = {}

        result = assess_security_risks(content, data)

        assert result["risk_level"] > 50  # Should be high risk
        assert len(result["risks"]) > 0

        # Check for specific security issues
        findings = [r["finding"] for r in result["risks"]]
        assert any("hardcoded" in f.lower() for f in findings)
        assert any("http" in f.lower() for f in findings)

    def test_low_risk_security_profile(self):
        """Test artifact with good security controls"""
        content = """
        Authentication via multi-factor authentication
        Authorization with role-based access control
        Data encrypted at rest using AES-256
        Data encrypted in transit using TLS 1.3
        Comprehensive audit logging and monitoring
        No hardcoded credentials - using vault
        Regular vulnerability scanning and penetration testing
        """
        data = {}

        result = assess_security_risks(content, data)

        assert result["risk_level"] < 30  # Should be low risk
        assert len(result["compliant_items"]) > 0
        assert result["coverage_score"] > 70

    def test_detect_hardcoded_credentials(self):
        """Test detection of hardcoded credentials"""
        content = "password: hardcoded_secret123"
        result = assess_security_risks(content, {})

        assert any(r["severity"] == "critical" for r in result["risks"])
        assert any("hardcoded" in r["finding"].lower() for r in result["risks"])

    def test_detect_unencrypted_http(self):
        """Test detection of unencrypted HTTP connections"""
        content = "Connect to http://api.example.com"
        result = assess_security_risks(content, {})

        assert any(r["severity"] == "high" for r in result["risks"])
        assert any("http" in r["finding"].lower() for r in result["risks"])

    def test_missing_authentication_controls(self):
        """Test detection of missing authentication/authorization"""
        content = "Deploy application to production"
        result = assess_security_risks(content, {})

        # Should flag missing auth controls
        assert any("authentication" in r["finding"].lower() or "authorization" in r["finding"].lower()
                   for r in result["risks"])

    def test_security_coverage_scoring(self):
        """Test security coverage scoring"""
        content_good = """
        authentication, authorization, encryption,
        password management, api key rotation,
        vulnerability scanning, audit logging
        """
        result_good = assess_security_risks(content_good, {})
        assert result_good["coverage_score"] > 80

        content_bad = "basic application deployment"
        result_bad = assess_security_risks(content_bad, {})
        assert result_bad["coverage_score"] < 30


class TestPrivacyRiskAssessment:
    """Test privacy risk assessment functionality"""

    def test_high_privacy_risk(self):
        """Test detection of high privacy risks"""
        content = """
        Collect user personal data including SSN and health records
        Share data with third party marketing partners
        No consent mechanism or privacy policy
        """
        data = {}

        result = assess_privacy_risks(content, data)

        assert result["risk_level"] > 40
        assert len(result["risks"]) > 0

    def test_gdpr_compliant_privacy(self):
        """Test GDPR-compliant privacy controls"""
        content = """
        Explicit consent from data subjects required
        Privacy by design principles applied
        Data anonymization and pseudonymization
        Data processing agreements in place
        Privacy policy published
        """
        data = {}

        result = assess_privacy_risks(content, data)

        assert result["risk_level"] < 20
        assert len(result["compliant_items"]) > 0

    def test_missing_consent_mechanism(self):
        """Test detection of missing consent for personal data"""
        content = "Process sensitive personal data for analytics"
        result = assess_privacy_risks(content, {})

        assert any("consent" in r["finding"].lower() for r in result["risks"])

    def test_missing_data_anonymization(self):
        """Test detection of missing anonymization"""
        content = "Process personal data for machine learning"
        result = assess_privacy_risks(content, {})

        assert any("anonymization" in r["finding"].lower() or "de-identification" in r["finding"].lower()
                   for r in result["risks"])

    def test_third_party_sharing_risk(self):
        """Test detection of third-party data sharing without agreements"""
        content = "Share customer data with third party vendors"
        result = assess_privacy_risks(content, {})

        assert any("third" in r["finding"].lower() and "party" in r["finding"].lower()
                   for r in result["risks"])


class TestOperationalRiskAssessment:
    """Test operational risk assessment functionality"""

    def test_high_operational_risk(self):
        """Test detection of high operational risks"""
        content = """
        Deploy to production
        No backup plan
        No incident response
        No change management
        """
        data = {}

        result = assess_operational_risks(content, data)

        assert result["risk_level"] > 40
        assert len(result["risks"]) > 0

    def test_robust_operational_controls(self):
        """Test artifact with strong operational controls"""
        content = """
        Comprehensive incident response plan in place
        Regular backup and disaster recovery testing
        Business continuity plan with defined RTO/RPO
        Formal change management and change control process
        Service level agreements and uptime commitments
        """
        data = {}

        result = assess_operational_risks(content, data)

        assert result["risk_level"] < 20
        assert len(result["compliant_items"]) > 0

    def test_missing_business_continuity(self):
        """Test detection of missing BC/DR"""
        content = "Production deployment plan"
        result = assess_operational_risks(content, {})

        assert any("business continuity" in r["finding"].lower() or "disaster recovery" in r["finding"].lower()
                   for r in result["risks"])

    def test_missing_incident_response(self):
        """Test detection of missing incident response"""
        content = "Security monitoring enabled"
        result = assess_operational_risks(content, {})

        assert any("incident response" in r["finding"].lower() for r in result["risks"])

    def test_missing_change_management(self):
        """Test detection of missing change management"""
        content = "Deploy updates to production"
        result = assess_operational_risks(content, {})

        assert any("change management" in r["finding"].lower() or "change control" in r["finding"].lower()
                   for r in result["risks"])


class TestComplianceAssessment:
    """Test compliance framework assessment functionality"""

    def test_soc2_compliance_assessment(self):
        """Test SOC2 compliance assessment"""
        content = """
        Access control policies implemented
        Data encryption at rest and in transit
        Security monitoring and alerting
        Incident response procedures documented
        Change management process defined
        """
        result = assess_compliance_risks(content, {}, ["SOC2"])

        assert "SOC2" in result
        assert result["SOC2"]["framework_name"] == "SOC 2 Type II"
        assert result["SOC2"]["compliance_score"] > 50

    def test_gdpr_compliance_assessment(self):
        """Test GDPR compliance assessment"""
        artifact_path = FIXTURES_DIR / "gdpr-compliant-artifact.yaml"
        content, data, _ = load_artifact(artifact_path)

        result = assess_compliance_risks(content, data, ["GDPR"])

        assert "GDPR" in result
        assert result["GDPR"]["compliance_score"] > 70
        assert result["GDPR"]["status"] in ["compliant", "partial"]

    def test_iso27001_compliance_assessment(self):
        """Test ISO27001 compliance assessment"""
        content = """
        Risk assessment and management framework
        Information security policy documented
        Asset inventory and classification
        Access management controls
        Regular security audits conducted
        """
        result = assess_compliance_risks(content, {}, ["ISO27001"])

        assert "ISO27001" in result
        assert result["ISO27001"]["framework_name"] == "ISO/IEC 27001"
        assert result["ISO27001"]["compliance_score"] > 60

    def test_hipaa_compliance_assessment(self):
        """Test HIPAA compliance assessment"""
        content = """
        PHI encryption at rest and in transit
        Protected health information access controls
        Minimum necessary principle applied
        Audit logs for PHI access
        Breach notification procedures
        """
        result = assess_compliance_risks(content, {}, ["HIPAA"])

        assert "HIPAA" in result
        assert result["HIPAA"]["compliance_score"] > 70

    def test_multiple_frameworks(self):
        """Test assessment against multiple frameworks"""
        content = """
        GDPR privacy by design
        SOC2 security controls
        ISO 27001 risk management
        NIST cybersecurity framework
        """
        result = assess_compliance_risks(content, {}, ["GDPR", "SOC2", "ISO27001", "NIST"])

        assert len(result) == 4
        assert all(fw in result for fw in ["GDPR", "SOC2", "ISO27001", "NIST"])

    def test_compliance_gap_identification(self):
        """Test identification of compliance gaps"""
        content = "Basic application deployment"
        result = assess_compliance_risks(content, {}, ["SOC2"])

        assert "SOC2" in result
        assert len(result["SOC2"]["gaps"]) > 0
        assert result["SOC2"]["status"] == "non-compliant"

    def test_invalid_framework(self):
        """Test handling of invalid framework"""
        content = "Test content"
        result = assess_compliance_risks(content, {}, ["INVALID_FRAMEWORK"])

        # Should not include invalid framework
        assert "INVALID_FRAMEWORK" not in result


class TestRiskScoringAndRating:
    """Test risk scoring and rating functionality"""

    def test_calculate_overall_risk_score(self):
        """Test overall risk score calculation"""
        assessments = {
            "security": {"risk_level": 80},
            "privacy": {"risk_level": 60},
            "operational": {"risk_level": 40},
            "compliance": {
                "SOC2": {"compliance_score": 30},
                "GDPR": {"compliance_score": 50}
            }
        }

        risk_score = calculate_overall_risk_score(assessments)

        assert 0 <= risk_score <= 100
        assert isinstance(risk_score, int)
        # Should be weighted toward security (40%) and privacy (25%)
        assert risk_score > 50

    def test_risk_score_weights(self):
        """Test risk score weighting"""
        # High security risk should dominate
        assessments_high_security = {
            "security": {"risk_level": 100},
            "privacy": {"risk_level": 0},
            "operational": {"risk_level": 0},
            "compliance": {}
        }
        score = calculate_overall_risk_score(assessments_high_security)
        assert score >= 40  # 40% weight on security

    def test_determine_risk_rating(self):
        """Test risk rating determination"""
        assert determine_risk_rating(85) == ("CRITICAL", "red")
        assert determine_risk_rating(75) == ("CRITICAL", "red")
        assert determine_risk_rating(60) == ("HIGH", "orange")
        assert determine_risk_rating(50) == ("HIGH", "orange")
        assert determine_risk_rating(35) == ("MEDIUM", "yellow")
        assert determine_risk_rating(25) == ("MEDIUM", "yellow")
        assert determine_risk_rating(15) == ("LOW", "green")
        assert determine_risk_rating(0) == ("LOW", "green")


class TestRemediationPlan:
    """Test remediation plan generation"""

    def test_generate_remediation_plan(self):
        """Test remediation plan generation"""
        risks = [
            {
                "category": "security",
                "severity": "critical",
                "finding": "Hardcoded credentials",
                "impact": "Unauthorized access",
                "remediation": "Use secure credential management"
            },
            {
                "category": "privacy",
                "severity": "high",
                "finding": "No consent mechanism",
                "impact": "GDPR violation",
                "remediation": "Implement consent management"
            },
            {
                "category": "operational",
                "severity": "medium",
                "finding": "No backup plan",
                "impact": "Data loss risk",
                "remediation": "Implement backup strategy"
            }
        ]

        plan = generate_remediation_plan(risks)

        assert len(plan) == 3
        # Should be sorted by severity
        assert plan[0]["severity"] == "critical"
        assert plan[1]["severity"] == "high"
        assert plan[2]["severity"] == "medium"
        # Should have priority numbers
        assert plan[0]["priority"] == 1
        assert plan[2]["priority"] == 3

    def test_remediation_plan_priority_sorting(self):
        """Test remediation plan sorts by severity priority"""
        risks = [
            {"severity": "low", "category": "test", "finding": "Low", "impact": "Low", "remediation": "Fix"},
            {"severity": "critical", "category": "test", "finding": "Critical", "impact": "High", "remediation": "Fix"},
            {"severity": "medium", "category": "test", "finding": "Medium", "impact": "Med", "remediation": "Fix"},
            {"severity": "high", "category": "test", "finding": "High", "impact": "High", "remediation": "Fix"}
        ]

        plan = generate_remediation_plan(risks)

        severities = [item["severity"] for item in plan]
        assert severities == ["critical", "high", "medium", "low"]


class TestIntegrationWorkflow:
    """Integration tests for complete risk review workflow"""

    def test_high_risk_artifact_workflow(self):
        """Test complete workflow on high-risk artifact"""
        artifact_path = str(FIXTURES_DIR / "high-risk-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["SOC2", "GDPR"],
            risk_threshold="high"
        )

        assert result["success"] is True
        assert result["risk_assessment"]["risk_score"] > 50
        assert result["risk_assessment"]["risk_rating"] in ["HIGH", "CRITICAL"]
        assert len(result["remediation_plan"]) > 0
        assert "SOC2" in result["compliance_status"]
        assert "GDPR" in result["compliance_status"]

    def test_low_risk_artifact_workflow(self):
        """Test complete workflow on low-risk artifact"""
        artifact_path = str(FIXTURES_DIR / "low-risk-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["HIPAA", "ISO27001", "SOC2"],
            risk_threshold="medium"
        )

        assert result["success"] is True
        assert result["risk_assessment"]["risk_score"] < 30
        assert result["risk_assessment"]["risk_rating"] == "LOW"
        # Should still have some recommendations even for low-risk
        assert "remediation_plan" in result

    def test_medium_risk_artifact_workflow(self):
        """Test workflow on medium-risk artifact"""
        artifact_path = str(FIXTURES_DIR / "medium-risk-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["PCI-DSS"],
            risk_threshold="medium"
        )

        assert result["success"] is True
        assert 20 < result["risk_assessment"]["risk_score"] < 60
        assert result["risk_assessment"]["risk_rating"] in ["MEDIUM", "HIGH"]

    def test_nonexistent_file_error_handling(self):
        """Test error handling for non-existent file"""
        artifact_path = str(FIXTURES_DIR / "does-not-exist.yaml")

        result = review_risk(artifact_path=artifact_path)

        assert result["success"] is False
        assert "error" in result
        assert result["risk_score"] == 100
        assert result["risk_rating"] == "CRITICAL"

    def test_default_frameworks(self):
        """Test default frameworks when none specified"""
        artifact_path = str(FIXTURES_DIR / "medium-risk-artifact.yaml")

        result = review_risk(artifact_path=artifact_path)

        assert result["success"] is True
        # Should use default frameworks
        assert len(result["compliance_status"]) > 0
        assert any(fw in result["compliance_status"] for fw in ["SOC2", "ISO27001", "GDPR"])

    def test_audit_report_structure(self):
        """Test audit report has required structure"""
        artifact_path = str(FIXTURES_DIR / "low-risk-artifact.yaml")

        result = review_risk(artifact_path=artifact_path)

        audit_report = result["audit_report"]
        required_fields = [
            "artifact_path", "artifact_type", "assessment_date",
            "assessor", "policy_frameworks", "risk_score", "risk_rating",
            "total_findings", "critical_findings", "high_findings",
            "medium_findings", "findings", "remediation_plan"
        ]

        for field in required_fields:
            assert field in audit_report, f"Missing required field: {field}"

    def test_risk_assessment_structure(self):
        """Test risk assessment has required structure"""
        artifact_path = str(FIXTURES_DIR / "medium-risk-artifact.yaml")

        result = review_risk(artifact_path=artifact_path)

        risk_assessment = result["risk_assessment"]
        assert "risk_score" in risk_assessment
        assert "risk_rating" in risk_assessment
        assert "security" in risk_assessment
        assert "privacy" in risk_assessment
        assert "operational" in risk_assessment

        # Check security assessment structure
        security = risk_assessment["security"]
        assert "risk_level" in security
        assert "coverage_score" in security
        assert "risks" in security
        assert "compliant_items" in security


class TestPolicyFrameworks:
    """Test policy framework definitions"""

    def test_all_frameworks_defined(self):
        """Test all supported frameworks are properly defined"""
        expected_frameworks = ["SOC2", "ISO27001", "GDPR", "HIPAA", "PCI-DSS", "NIST"]

        for framework in expected_frameworks:
            assert framework in POLICY_FRAMEWORKS
            assert "name" in POLICY_FRAMEWORKS[framework]
            assert "categories" in POLICY_FRAMEWORKS[framework]
            assert "keywords" in POLICY_FRAMEWORKS[framework]

    def test_framework_structure(self):
        """Test framework definitions have required structure"""
        for framework_key, framework in POLICY_FRAMEWORKS.items():
            assert isinstance(framework["name"], str)
            assert isinstance(framework["categories"], list)
            assert isinstance(framework["keywords"], list)
            assert len(framework["categories"]) > 0
            assert len(framework["keywords"]) > 0


if __name__ == "__main__":
    # Run pytest with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
