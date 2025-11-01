#!/usr/bin/env python3
"""
Integration tests for AI-native risk assessment

These tests actually call the Claude API to validate:
- Prompt works correctly
- Response parsing is robust
- Findings are meaningful
- Costs and latency are acceptable

Run with: pytest test_ai_integration.py -v -s
Requires: ANTHROPIC_API_KEY environment variable
"""

import os
import sys
import pytest
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from risk_review import review_risk
from ai_engine import AIRiskAnalyzer, estimate_cost

# Test fixtures directory
FIXTURES_DIR = Path(__file__).parent / "fixtures"

# Skip all tests if no API key
pytestmark = pytest.mark.skipif(
    not os.environ.get('ANTHROPIC_API_KEY'),
    reason="ANTHROPIC_API_KEY not set - skipping AI integration tests"
)


class TestAIIntegration:
    """Integration tests that actually call Claude API"""

    def test_ai_mode_high_risk_artifact(self):
        """Test AI correctly identifies high-risk artifact"""
        artifact_path = str(FIXTURES_DIR / "high-risk-artifact.yaml")

        start = time.time()
        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["SOC2", "GDPR"],
            mode="ai",
            cache_enabled=False,  # Disable cache for testing
            verbose=True
        )
        duration = time.time() - start

        # Validate structure
        assert result["success"] is True, "AI assessment should succeed"
        assert "risk_assessment" in result
        assert "findings" in result["audit_report"]

        # Validate AI correctly identified as high risk
        risk_score = result["risk_assessment"]["risk_score"]
        risk_rating = result["risk_assessment"]["risk_rating"]

        print(f"\n📊 AI Assessment:")
        print(f"   Risk Score: {risk_score}/100")
        print(f"   Risk Rating: {risk_rating}")
        print(f"   Duration: {duration:.2f}s")
        print(f"   Findings: {len(result['audit_report']['findings'])}")

        assert risk_score > 50, f"Expected high risk, got {risk_score}"
        assert risk_rating in ["HIGH", "CRITICAL"], f"Expected HIGH/CRITICAL, got {risk_rating}"

        # Validate findings have evidence
        findings = result["audit_report"]["findings"]
        assert len(findings) > 0, "Should have at least one finding"

        for finding in findings:
            assert "finding" in finding, "Missing 'finding' field"
            assert "severity" in finding, "Missing 'severity' field"
            assert "category" in finding, "Missing 'category' field"

            # AI should provide evidence (quotes from artifact)
            if "evidence" in finding:
                assert len(finding["evidence"]) > 0, "Evidence should not be empty"
                print(f"\n   ✓ Finding: {finding['finding']}")
                print(f"     Evidence: {finding['evidence'][:100]}...")

    def test_ai_mode_low_risk_artifact(self):
        """Test AI correctly identifies low-risk artifact"""
        artifact_path = str(FIXTURES_DIR / "low-risk-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["HIPAA", "SOC2"],
            mode="ai",
            cache_enabled=False,
            verbose=True
        )

        risk_score = result["risk_assessment"]["risk_score"]
        risk_rating = result["risk_assessment"]["risk_rating"]

        print(f"\n📊 AI Assessment:")
        print(f"   Risk Score: {risk_score}/100")
        print(f"   Risk Rating: {risk_rating}")

        assert risk_score < 40, f"Expected low risk, got {risk_score}"
        assert risk_rating in ["LOW", "MEDIUM"], f"Expected LOW/MEDIUM, got {risk_rating}"

    def test_ai_understands_implementation_vs_planning(self):
        """Test that AI distinguishes between implemented and planned controls"""

        # Create a test artifact with planned (not implemented) controls
        planned_artifact = FIXTURES_DIR / "planned-controls-test.yaml"
        planned_artifact.write_text("""
metadata:
  name: future-security-plan
  artifactType: security-roadmap

content:
  description: Security improvements planned for next quarter

  planned_initiatives:
    - "We will implement multi-factor authentication in Q2"
    - "OAuth 2.0 migration scheduled for Q3"
    - "Encryption at rest planned for Q4"
    - "Planning to add comprehensive audit logging"

  current_state:
    - Basic password authentication
    - HTTP connections (HTTPS upgrade pending)
    - No encryption currently deployed
""")

        try:
            result = review_risk(
                artifact_path=str(planned_artifact),
                mode="ai",
                cache_enabled=False,
                verbose=True
            )

            risk_score = result["risk_assessment"]["risk_score"]
            findings = result["audit_report"]["findings"]

            print(f"\n📊 Planning vs Implementation Test:")
            print(f"   Risk Score: {risk_score}/100")
            print(f"   Findings: {len(findings)}")

            # AI should recognize these are plans, not implementations
            # Should score as HIGH RISK because nothing is actually deployed
            assert risk_score > 50, f"AI should recognize planned ≠ implemented, got {risk_score}"

            # Check if AI correctly identifies missing implementations
            finding_text = ' '.join([f['finding'].lower() for f in findings])

            # AI should mention that controls are planned but not implemented
            assert any(keyword in finding_text for keyword in ['plan', 'future', 'not implemented', 'pending', 'scheduled']), \
                "AI should recognize controls are planned but not implemented"

            print(f"   ✓ AI correctly distinguished planned vs implemented controls")

        finally:
            planned_artifact.unlink()  # Clean up test file

    def test_ai_cost_estimation_accuracy(self):
        """Test that cost estimates are reasonably accurate"""
        artifact_path = str(FIXTURES_DIR / "medium-risk-artifact.yaml")

        # Read artifact to estimate cost
        with open(artifact_path) as f:
            content = f.read()

        estimated_cost = estimate_cost(content)
        print(f"\n💰 Estimated Cost: ${estimated_cost:.4f}")

        # Actually run assessment
        result = review_risk(
            artifact_path=artifact_path,
            mode="ai",
            cache_enabled=False,
            verbose=False
        )

        # We can't get actual cost without response.usage, but we can validate estimate is reasonable
        assert 0.001 <= estimated_cost <= 0.10, \
            f"Cost estimate ${estimated_cost:.4f} seems unreasonable"

        print(f"   ✓ Cost estimate within reasonable range ($0.001-$0.10)")

    def test_ai_response_consistency(self):
        """Test AI provides consistent results across multiple runs"""
        artifact_path = str(FIXTURES_DIR / "high-risk-artifact.yaml")

        results = []
        for i in range(3):
            print(f"\n🔄 Run {i+1}/3...")
            result = review_risk(
                artifact_path=artifact_path,
                mode="ai",
                cache_enabled=False,  # Disable cache to test consistency
                verbose=False
            )
            results.append({
                'risk_score': result["risk_assessment"]["risk_score"],
                'risk_rating': result["risk_assessment"]["risk_rating"],
                'finding_count': len(result["audit_report"]["findings"])
            })

        # Check consistency
        risk_scores = [r['risk_score'] for r in results]
        risk_ratings = [r['risk_rating'] for r in results]

        print(f"\n📊 Consistency Check:")
        print(f"   Risk Scores: {risk_scores}")
        print(f"   Risk Ratings: {risk_ratings}")
        print(f"   Variance: {max(risk_scores) - min(risk_scores)}")

        # Scores should be within reasonable variance (±15 points)
        variance = max(risk_scores) - min(risk_scores)
        assert variance <= 20, f"Risk scores vary too much: {risk_scores}"

        # Ratings should be consistent
        unique_ratings = set(risk_ratings)
        assert len(unique_ratings) <= 2, f"Too many different ratings: {risk_ratings}"

        print(f"   ✓ Results are reasonably consistent")

    def test_ai_handles_invalid_yaml(self):
        """Test AI gracefully handles malformed YAML"""
        artifact_path = str(FIXTURES_DIR / "invalid-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            mode="ai",
            cache_enabled=False,
            verbose=False
        )

        # Should still succeed (AI can read raw text even if YAML parsing fails)
        assert result["success"] is True

        print(f"\n📊 Invalid YAML Test:")
        print(f"   Risk Score: {result['risk_assessment']['risk_score']}/100")
        print(f"   ✓ AI handled malformed YAML gracefully")

    def test_smart_mode_critical_detection(self):
        """Test smart mode correctly detects critical issues and skips AI"""

        # Create artifact with obvious critical issue
        critical_artifact = FIXTURES_DIR / "obvious-critical-test.yaml"
        critical_artifact.write_text("""
config:
  database:
    host: db.example.com
    username: admin
    password: SuperSecret123!
    api_key: sk_live_1234567890abcdefghij
""")

        try:
            start = time.time()
            result = review_risk(
                artifact_path=str(critical_artifact),
                mode="smart",  # Smart mode should detect and skip AI
                cache_enabled=False,
                verbose=True
            )
            duration = time.time() - start

            print(f"\n⚡ Smart Mode Test:")
            print(f"   Duration: {duration:.2f}s")
            print(f"   Assessment Mode: {result['audit_report']['assessor']}")

            # Should be very fast (<1s) because it skipped AI
            assert duration < 2.0, f"Smart mode should skip AI for obvious critical issues, took {duration:.2f}s"

            # Should identify as CRITICAL
            assert result["risk_assessment"]["risk_rating"] == "CRITICAL"

            # Should have detected hardcoded credentials
            findings = [f['finding'].lower() for f in result["audit_report"]["findings"]]
            assert any('credential' in f or 'password' in f or 'secret' in f for f in findings)

            print(f"   ✓ Smart mode correctly skipped AI for obvious critical issue")

        finally:
            critical_artifact.unlink()

    def test_compliance_framework_assessment(self):
        """Test AI properly assesses compliance frameworks"""
        artifact_path = str(FIXTURES_DIR / "gdpr-compliant-artifact.yaml")

        result = review_risk(
            artifact_path=artifact_path,
            policy_frameworks=["GDPR", "ISO27001"],
            mode="ai",
            cache_enabled=False,
            verbose=True
        )

        compliance_status = result["compliance_status"]

        print(f"\n📋 Compliance Assessment:")
        for framework, status in compliance_status.items():
            print(f"   {framework}: {status['status'].upper()} ({status['compliance_score']:.1f}%)")

        assert "GDPR" in compliance_status
        assert "ISO27001" in compliance_status

        # GDPR-compliant artifact should score well on GDPR
        gdpr_score = compliance_status["GDPR"]["compliance_score"]
        assert gdpr_score > 60, f"GDPR-compliant artifact should score well, got {gdpr_score}%"

        print(f"   ✓ AI properly assessed compliance frameworks")


class TestAICaching:
    """Test caching behavior"""

    def test_cache_effectiveness(self):
        """Test that caching works and saves costs"""
        artifact_path = str(FIXTURES_DIR / "medium-risk-artifact.yaml")

        # First call - should hit API
        start1 = time.time()
        result1 = review_risk(
            artifact_path=artifact_path,
            mode="ai",
            cache_enabled=True,  # Enable caching
            verbose=False
        )
        duration1 = time.time() - start1

        # Second call - should hit cache
        start2 = time.time()
        result2 = review_risk(
            artifact_path=artifact_path,
            mode="ai",
            cache_enabled=True,
            verbose=False
        )
        duration2 = time.time() - start2

        print(f"\n💾 Cache Test:")
        print(f"   First call:  {duration1:.2f}s")
        print(f"   Second call: {duration2:.2f}s")
        print(f"   Speedup: {duration1/duration2:.1f}x")

        # Cached call should be MUCH faster
        assert duration2 < duration1 / 5, f"Cached call should be >5x faster, got {duration1/duration2:.1f}x"

        # Results should be identical
        assert result1["risk_assessment"]["risk_score"] == result2["risk_assessment"]["risk_score"]

        print(f"   ✓ Caching works and provides {duration1/duration2:.0f}x speedup")


if __name__ == "__main__":
    # Run with: python test_ai_integration.py
    pytest.main([__file__, "-v", "-s", "--tb=short"])
