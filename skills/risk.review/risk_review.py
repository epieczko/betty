#!/usr/bin/env python3
"""
risk.review skill - AI-Native Policy Compliance and Risk Assessment

Performs comprehensive risk assessment using AI semantic analysis with intelligent fallbacks.
"""

import sys
import os
import argparse
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
import yaml

# Import engines
from ai_engine import AIRiskAnalyzer, ArtifactCache, estimate_cost
from regex_engine import (
    assess_security_risks,
    assess_privacy_risks,
    assess_operational_risks,
    assess_compliance_risks,
    calculate_overall_risk_score,
    determine_risk_rating,
    generate_remediation_plan,
    POLICY_FRAMEWORKS
)


class RiskReviewer:
    """Orchestrates risk assessment across AI and regex engines"""

    def __init__(self, mode: str = 'smart', cache_enabled: bool = True, verbose: bool = True):
        """
        Initialize risk reviewer

        Args:
            mode: 'smart' (AI with fast pre-check), 'ai' (pure AI), 'fast' (regex only)
            cache_enabled: Enable caching for AI assessments
            verbose: Print progress and cost information
        """
        self.mode = mode
        self.verbose = verbose
        self.ai_engine = AIRiskAnalyzer() if mode in ['smart', 'ai'] else None
        self.cache = ArtifactCache() if cache_enabled and mode in ['smart', 'ai'] else None

    def review(
        self,
        artifact_path: str,
        artifact_type: Optional[str] = None,
        policy_frameworks: Optional[List[str]] = None,
        risk_threshold: str = 'medium'
    ) -> Dict[str, Any]:
        """
        Perform comprehensive risk assessment

        Args:
            artifact_path: Path to artifact file
            artifact_type: Type of artifact (optional)
            policy_frameworks: List of frameworks to assess against
            risk_threshold: Risk threshold level

        Returns:
            Risk assessment results
        """
        file_path = Path(artifact_path)

        # Load artifact
        try:
            content, data, file_format = self._load_artifact(file_path)
        except FileNotFoundError as e:
            return {
                'success': False,
                'error': str(e),
                'risk_score': 100,
                'risk_rating': 'CRITICAL'
            }

        # Default frameworks
        if not policy_frameworks:
            policy_frameworks = ['SOC2', 'ISO27001', 'GDPR']

        # Detect artifact type
        artifact_type = artifact_type or self._detect_artifact_type(file_path, data)

        # Check cache first (AI modes only)
        if self.cache and self.mode in ['smart', 'ai']:
            cached = self.cache.get(artifact_path, policy_frameworks)
            if cached:
                return self._format_result(cached, artifact_path, artifact_type, policy_frameworks)

        # Route to appropriate engine
        if self.mode == 'fast':
            result = self._assess_with_regex(content, data, artifact_type, policy_frameworks)

        elif self.mode == 'ai':
            result = self._assess_with_ai(content, data, artifact_type, policy_frameworks)

        else:  # 'smart' mode
            result = self._assess_smart(content, data, artifact_type, policy_frameworks)

        # Cache AI results
        if self.cache and self.mode in ['smart', 'ai']:
            self.cache.set(artifact_path, policy_frameworks, result)

        return self._format_result(result, artifact_path, artifact_type, policy_frameworks)

    def _load_artifact(self, file_path: Path) -> tuple:
        """Load and parse artifact"""
        if not file_path.exists():
            raise FileNotFoundError(f"Artifact file not found: {file_path}")

        with open(file_path, 'r') as f:
            content = f.read()

        file_format = file_path.suffix.lstrip('.')
        data = {}

        if file_format in ['yaml', 'yml']:
            try:
                data = yaml.safe_load(content)
                if data is None:
                    data = {}
            except Exception as e:
                if self.verbose:
                    print(f"⚠️  Failed to parse YAML: {e}", file=sys.stderr)
                data = {}

        return content, data, file_format

    def _detect_artifact_type(self, file_path: Path, data: Dict[str, Any]) -> str:
        """Detect artifact type from filename or metadata"""
        if isinstance(data, dict) and 'metadata' in data:
            if 'artifactType' in data['metadata']:
                return data['metadata']['artifactType']

        # Fallback to filename
        return file_path.stem

    def _assess_with_regex(
        self,
        content: str,
        data: Dict[str, Any],
        artifact_type: str,
        frameworks: List[str]
    ) -> Dict[str, Any]:
        """Fast regex-based assessment"""
        if self.verbose:
            print(f"⚡ Fast Mode (Regex Pattern Matching)")

        security_assessment = assess_security_risks(content, data)
        privacy_assessment = assess_privacy_risks(content, data)
        operational_assessment = assess_operational_risks(content, data)
        compliance_assessment = assess_compliance_risks(content, data, frameworks)

        # Collect all risks
        all_risks = (
            security_assessment['risks'] +
            privacy_assessment['risks'] +
            operational_assessment['risks']
        )

        # Calculate overall risk
        assessments = {
            'security': security_assessment,
            'privacy': privacy_assessment,
            'operational': operational_assessment,
            'compliance': compliance_assessment
        }

        risk_score = calculate_overall_risk_score(assessments)
        risk_rating, _ = determine_risk_rating(risk_score)

        return {
            'risk_score': risk_score,
            'risk_rating': risk_rating,
            'assessment_summary': f"Regex-based assessment found {len(all_risks)} risk(s)",
            'findings': all_risks,
            'compliance_status': compliance_assessment,
            'security_assessment': security_assessment,
            'privacy_assessment': privacy_assessment,
            'operational_assessment': operational_assessment,
            'remediation_plan': generate_remediation_plan(all_risks),
            'assessment_mode': 'regex'
        }

    def _assess_with_ai(
        self,
        content: str,
        data: Dict[str, Any],
        artifact_type: str,
        frameworks: List[str]
    ) -> Dict[str, Any]:
        """AI-powered semantic assessment"""
        result = self.ai_engine.assess(content, data, artifact_type, frameworks, self.verbose)
        result['assessment_mode'] = 'ai'
        return result

    def _assess_smart(
        self,
        content: str,
        data: Dict[str, Any],
        artifact_type: str,
        frameworks: List[str]
    ) -> Dict[str, Any]:
        """Smart mode: Fast pre-check + AI assessment"""
        if self.verbose:
            print(f"🧠 Smart Mode (Fast Check + AI Analysis)")

        # Fast critical check with regex
        critical_check = self._check_critical_patterns(content)

        if critical_check['has_critical']:
            if self.verbose:
                print(f"⚠️  Critical issues detected: {', '.join(critical_check['issues'])}")
                print(f"   Skipping AI analysis (obvious failure)")

            # Return immediate critical result
            return {
                'risk_score': 95,
                'risk_rating': 'CRITICAL',
                'assessment_summary': f"Critical security issues detected: {', '.join(critical_check['issues'])}",
                'findings': critical_check['findings'],
                'compliance_status': {fw: {
                    'compliance_score': 0,
                    'status': 'non-compliant',
                    'gaps': [{'gap': 'Critical security issues present', 'requirement': 'Address critical findings', 'priority': 'critical'}],
                    'compliant_areas': []
                } for fw in frameworks},
                'security_assessment': {
                    'risk_level': 100,
                    'coverage_score': 0,
                    'compliant_items': [],
                    'risks': critical_check['findings']
                },
                'privacy_assessment': {'risk_level': 0, 'privacy_coverage': 0, 'compliant_items': [], 'risks': []},
                'operational_assessment': {'risk_level': 0, 'compliant_items': [], 'risks': []},
                'remediation_plan': generate_remediation_plan(critical_check['findings']),
                'assessment_mode': 'fast_critical'
            }

        # No critical issues - proceed with AI analysis
        return self._assess_with_ai(content, data, artifact_type, frameworks)

    def _check_critical_patterns(self, content: str) -> Dict[str, Any]:
        """Fast check for critical security patterns"""
        findings = []

        # Hardcoded credentials patterns
        credential_patterns = [
            (r'(password|passwd|pwd|secret|api[_-]?key|private[_-]?key|token)\s*[:=]\s*["\']?[\w\-]{8,}["\']?', 'Hardcoded credentials detected'),
            (r'(admin|root|default)[_-]?(password|passwd|pwd)\s*[:=]', 'Default/admin credentials'),
        ]

        for pattern, issue in credential_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                findings.append({
                    'category': 'security',
                    'severity': 'critical',
                    'finding': issue,
                    'evidence': re.search(pattern, content, re.IGNORECASE).group(0)[:100],
                    'impact': 'Unauthorized access, credential exposure',
                    'remediation': 'Use secure credential management (vault, environment variables)'
                })

        return {
            'has_critical': len(findings) > 0,
            'issues': [f['finding'] for f in findings],
            'findings': findings
        }

    def _format_result(
        self,
        result: Dict[str, Any],
        artifact_path: str,
        artifact_type: str,
        frameworks: List[str]
    ) -> Dict[str, Any]:
        """Format result with metadata"""
        # Generate audit report
        audit_report = {
            'artifact_path': str(Path(artifact_path).absolute()),
            'artifact_type': artifact_type,
            'assessment_date': datetime.now().isoformat(),
            'assessor': f'Betty Risk Review v1.0.0 ({result.get("assessment_mode", "unknown")} mode)',
            'policy_frameworks': frameworks,
            'risk_score': result['risk_score'],
            'risk_rating': result['risk_rating'],
            'total_findings': len(result.get('findings', [])),
            'critical_findings': sum(1 for r in result.get('findings', []) if r.get('severity') == 'critical'),
            'high_findings': sum(1 for r in result.get('findings', []) if r.get('severity') == 'high'),
            'medium_findings': sum(1 for r in result.get('findings', []) if r.get('severity') == 'medium'),
            'findings': result.get('findings', []),
            'remediation_plan': result.get('remediation_plan', [])
        }

        return {
            'success': True,
            'risk_assessment': {
                'risk_score': result['risk_score'],
                'risk_rating': result['risk_rating'],
                'security': result.get('security_assessment', {}),
                'privacy': result.get('privacy_assessment', {}),
                'operational': result.get('operational_assessment', {})
            },
            'compliance_status': result.get('compliance_status', {}),
            'audit_report': audit_report,
            'remediation_plan': result.get('remediation_plan', []),
            'assessment_summary': result.get('assessment_summary', '')
        }


# Import re for critical pattern checking
import re


def review_risk(
    artifact_path: str,
    artifact_type: Optional[str] = None,
    policy_frameworks: Optional[List[str]] = None,
    risk_threshold: str = 'medium',
    assessment_scope: Optional[List[str]] = None,
    mode: str = 'smart',
    cache_enabled: bool = True,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Perform comprehensive risk assessment (API-compatible with original)

    Args:
        artifact_path: Path to artifact file
        artifact_type: Type of artifact
        policy_frameworks: List of frameworks
        risk_threshold: Risk threshold
        assessment_scope: Assessment areas (ignored for now)
        mode: 'smart', 'ai', or 'fast'
        cache_enabled: Enable caching
        verbose: Print progress

    Returns:
        Risk assessment results
    """
    reviewer = RiskReviewer(mode=mode, cache_enabled=cache_enabled, verbose=verbose)
    return reviewer.review(artifact_path, artifact_type, policy_frameworks, risk_threshold)


def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description='AI-Native Policy Compliance and Risk Assessment'
    )
    parser.add_argument(
        'artifact_path',
        type=str,
        help='Path to artifact file to assess'
    )
    parser.add_argument(
        '--artifact-type',
        type=str,
        help='Type of artifact'
    )
    parser.add_argument(
        '--policy-frameworks',
        type=str,
        nargs='+',
        choices=['SOC2', 'ISO27001', 'GDPR', 'HIPAA', 'PCI-DSS', 'NIST'],
        help='Policy frameworks to assess against'
    )
    parser.add_argument(
        '--risk-threshold',
        type=str,
        choices=['low', 'medium', 'high', 'critical'],
        default='medium',
        help='Risk threshold level'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['smart', 'ai', 'fast'],
        default='smart',
        help='Assessment mode: smart (AI+fast), ai (pure AI), fast (regex only)'
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Disable caching'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress output'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save assessment report to file'
    )

    args = parser.parse_args()

    # Perform assessment
    result = review_risk(
        artifact_path=args.artifact_path,
        artifact_type=args.artifact_type,
        policy_frameworks=args.policy_frameworks,
        risk_threshold=args.risk_threshold,
        mode=args.mode,
        cache_enabled=not args.no_cache,
        verbose=not args.quiet
    )

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)
        if not args.quiet:
            print(f"\n✓ Assessment report saved to: {output_path}")

    # Print report
    if not result['success']:
        print(f"\n{'='*80}")
        print(f"✗ Risk Assessment Failed")
        print(f"{'='*80}")
        print(f"Error: {result['error']}")
        print(f"{'='*80}\n")
        return 1

    audit = result['audit_report']
    risk_assessment = result['risk_assessment']

    print(f"\n{'='*80}")
    print(f"RISK ASSESSMENT & COMPLIANCE AUDIT REPORT")
    print(f"{'='*80}")
    print(f"Artifact:        {audit['artifact_path']}")
    print(f"Type:            {audit['artifact_type']}")
    print(f"Assessment Date: {audit['assessment_date']}")
    print(f"Assessor:        {audit['assessor']}")
    print(f"")
    print(f"OVERALL RISK RATING: {audit['risk_rating']}")
    print(f"Risk Score:          {audit['risk_score']}/100")
    print(f"")

    if result.get('assessment_summary'):
        print(f"SUMMARY:")
        print(f"  {result['assessment_summary']}")
        print(f"")

    print(f"FINDINGS SUMMARY:")
    print(f"  Total Findings:    {audit['total_findings']}")
    print(f"  Critical:          {audit['critical_findings']}")
    print(f"  High:              {audit['high_findings']}")
    print(f"  Medium:            {audit['medium_findings']}")
    print(f"")

    # Compliance Status
    if result['compliance_status']:
        print(f"COMPLIANCE STATUS:")
        for framework, status in result['compliance_status'].items():
            print(f"\n  {status.get('framework_name', framework)} ({framework}):")
            print(f"    Status: {status['status'].upper()}")
            print(f"    Compliance Score: {status['compliance_score']:.1f}%")
            if status.get('gaps'):
                print(f"    Gaps Identified: {len(status['gaps'])}")
        print()

    # Critical/High Findings
    critical_high = [r for r in audit['findings'] if r.get('severity') in ['critical', 'high']]
    if critical_high:
        print(f"CRITICAL & HIGH SEVERITY FINDINGS:")
        for finding in critical_high[:5]:  # Top 5
            severity_marker = "🔴" if finding['severity'] == 'critical' else "🟠"
            print(f"\n  {severity_marker} {finding['severity'].upper()}: {finding['finding']}")
            print(f"     Category: {finding.get('category', 'unknown')}")
            if finding.get('evidence'):
                evidence = finding['evidence'][:100] + ('...' if len(finding['evidence']) > 100 else '')
                print(f"     Evidence: {evidence}")
            print(f"     Impact: {finding.get('impact', 'N/A')}")
            print(f"     Remediation: {finding.get('remediation', 'N/A')}")
        print()

    # Top Remediation Priorities
    if result['remediation_plan']:
        print(f"TOP REMEDIATION PRIORITIES:")
        for item in result['remediation_plan'][:5]:
            print(f"  {item.get('priority', '?')}. [{item.get('severity', 'unknown').upper()}] {item.get('finding', 'N/A')}")
            print(f"     → {item.get('remediation', 'N/A')}")
        print()

    # Overall Recommendation
    print(f"RECOMMENDATION:")
    if audit['risk_score'] >= 75:
        print(f"  🔴 CRITICAL RISK - Immediate action required. Do not proceed without remediation.")
    elif audit['risk_score'] >= 50:
        print(f"  🟠 HIGH RISK - Significant risks identified. Address before production deployment.")
    elif audit['risk_score'] >= 25:
        print(f"  🟡 MEDIUM RISK - Moderate risks present. Remediate based on risk threshold.")
    else:
        print(f"  🟢 LOW RISK - Acceptable risk level. Monitor and maintain controls.")

    print(f"{'='*80}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
