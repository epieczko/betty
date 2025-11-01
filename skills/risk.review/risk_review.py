#!/usr/bin/env python3
"""
risk.review skill - Policy compliance and risk assessment

Performs comprehensive risk assessment and policy compliance analysis on artifacts.
Evaluates security, privacy, compliance, and operational risks.
"""

import sys
import os
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import yaml


# Policy framework compliance criteria
POLICY_FRAMEWORKS = {
    'SOC2': {
        'name': 'SOC 2 Type II',
        'categories': ['security', 'availability', 'processing_integrity', 'confidentiality', 'privacy'],
        'keywords': ['access control', 'encryption', 'monitoring', 'incident response', 'change management']
    },
    'ISO27001': {
        'name': 'ISO/IEC 27001',
        'categories': ['information_security', 'risk_management', 'asset_management', 'access_control'],
        'keywords': ['risk assessment', 'security policy', 'asset inventory', 'access management', 'audit']
    },
    'GDPR': {
        'name': 'General Data Protection Regulation',
        'categories': ['data_protection', 'privacy', 'consent', 'data_subject_rights'],
        'keywords': ['personal data', 'consent', 'data subject', 'privacy by design', 'breach notification']
    },
    'HIPAA': {
        'name': 'Health Insurance Portability and Accountability Act',
        'categories': ['privacy', 'security', 'breach_notification'],
        'keywords': ['PHI', 'protected health information', 'minimum necessary', 'encryption', 'audit logs']
    },
    'PCI-DSS': {
        'name': 'Payment Card Industry Data Security Standard',
        'categories': ['network_security', 'data_protection', 'access_control', 'monitoring'],
        'keywords': ['cardholder data', 'encryption', 'firewall', 'penetration testing', 'vulnerability']
    },
    'NIST': {
        'name': 'NIST Cybersecurity Framework',
        'categories': ['identify', 'protect', 'detect', 'respond', 'recover'],
        'keywords': ['asset management', 'data security', 'anomaly detection', 'incident response', 'recovery planning']
    }
}


def load_artifact(file_path: Path) -> Tuple[str, Dict[str, Any], str]:
    """Load artifact and parse content"""
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
            print(f"Warning: Failed to parse YAML: {e}", file=sys.stderr)
            data = {}

    return content, data, file_format


def assess_security_risks(content: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Assess security-related risks"""
    risks = []
    compliant_items = []
    risk_level = 0

    # Check for security keywords and patterns
    security_patterns = {
        'authentication': r'\b(authentication|auth|login|credentials)\b',
        'authorization': r'\b(authorization|access control|permissions|roles)\b',
        'encryption': r'\b(encryption|encrypted|TLS|SSL|AES|RSA)\b',
        'secrets': r'\b(password|secret|api[_\s]?key|token|private[_\s]?key)\b',
        'vulnerability': r'\b(vulnerability|exploit|CVE|security flaw)\b',
        'audit': r'\b(audit|logging|monitoring|tracing)\b'
    }

    security_coverage = []
    for category, pattern in security_patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            security_coverage.append(category)
            compliant_items.append(f"Addresses {category}")

    coverage_score = (len(security_coverage) / len(security_patterns)) * 100

    # Check for security anti-patterns
    if re.search(r'\bhardcoded\s+(password|secret|key)\b', content, re.IGNORECASE):
        risks.append({
            'category': 'security',
            'severity': 'critical',
            'finding': 'Hardcoded credentials detected',
            'impact': 'Unauthorized access, credential exposure',
            'remediation': 'Use secure credential management (e.g., vault, environment variables)'
        })
        risk_level += 30

    if re.search(r'\bhttp://\b', content, re.IGNORECASE):
        risks.append({
            'category': 'security',
            'severity': 'high',
            'finding': 'Unencrypted HTTP connections detected',
            'impact': 'Data transmission in clear text, susceptible to interception',
            'remediation': 'Use HTTPS/TLS for all network communications'
        })
        risk_level += 20

    if not re.search(r'\b(encryption|encrypted)\b', content, re.IGNORECASE):
        risks.append({
            'category': 'security',
            'severity': 'medium',
            'finding': 'No encryption mentioned',
            'impact': 'Data may be stored or transmitted without encryption',
            'remediation': 'Implement encryption for sensitive data at rest and in transit'
        })
        risk_level += 15

    if not re.search(r'\b(authentication|authorization)\b', content, re.IGNORECASE):
        risks.append({
            'category': 'security',
            'severity': 'high',
            'finding': 'No authentication/authorization controls mentioned',
            'impact': 'Potential unauthorized access to systems/data',
            'remediation': 'Implement robust authentication and authorization mechanisms'
        })
        risk_level += 20

    if not re.search(r'\b(audit|logging|monitoring)\b', content, re.IGNORECASE):
        risks.append({
            'category': 'security',
            'severity': 'medium',
            'finding': 'No audit/logging controls mentioned',
            'impact': 'Limited visibility into security events and incidents',
            'remediation': 'Implement comprehensive audit logging and monitoring'
        })
        risk_level += 10

    return {
        'risk_level': min(risk_level, 100),
        'coverage_score': coverage_score,
        'security_coverage': security_coverage,
        'risks': risks,
        'compliant_items': compliant_items
    }


def assess_compliance_risks(content: str, data: Dict[str, Any], frameworks: List[str]) -> Dict[str, Any]:
    """Assess policy compliance against specified frameworks"""
    compliance_status = {}

    for framework_key in frameworks:
        if framework_key not in POLICY_FRAMEWORKS:
            continue

        framework = POLICY_FRAMEWORKS[framework_key]
        gaps = []
        compliant_areas = []

        # Check for framework-specific keywords
        keyword_matches = 0
        for keyword in framework['keywords']:
            if keyword.lower() in content.lower():
                keyword_matches += 1
                compliant_areas.append(f"Addresses {keyword}")

        coverage_pct = (keyword_matches / len(framework['keywords'])) * 100

        # Identify gaps
        if coverage_pct < 40:
            gaps.append({
                'gap': f'Limited {framework_key} compliance coverage',
                'requirement': f'Address core {framework_key} requirements',
                'priority': 'high'
            })

        for category in framework['categories']:
            category_clean = category.replace('_', ' ')
            if category_clean not in content.lower():
                gaps.append({
                    'gap': f'{framework_key} - Missing {category_clean} controls',
                    'requirement': f'Implement {category_clean} controls per {framework_key}',
                    'priority': 'medium' if coverage_pct > 50 else 'high'
                })

        compliance_status[framework_key] = {
            'framework_name': framework['name'],
            'compliance_score': coverage_pct,
            'status': 'compliant' if coverage_pct >= 80 else 'partial' if coverage_pct >= 50 else 'non-compliant',
            'gaps': gaps,
            'compliant_areas': compliant_areas
        }

    return compliance_status


def assess_privacy_risks(content: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Assess privacy-related risks"""
    risks = []
    compliant_items = []
    risk_level = 0

    # Check for privacy keywords
    privacy_keywords = ['personal data', 'PII', 'PHI', 'privacy', 'consent', 'data subject', 'anonymization']
    privacy_mentions = sum(1 for kw in privacy_keywords if kw.lower() in content.lower())

    if privacy_mentions > 0:
        compliant_items.append("Addresses privacy considerations")

    # Check for privacy risks
    if re.search(r'\b(personal|sensitive)\s+data\b', content, re.IGNORECASE):
        if not re.search(r'\b(consent|authorization)\b', content, re.IGNORECASE):
            risks.append({
                'category': 'privacy',
                'severity': 'high',
                'finding': 'Personal data processing without explicit consent mechanism',
                'impact': 'GDPR/privacy regulation violations, legal liability',
                'remediation': 'Implement consent management and data subject rights'
            })
            risk_level += 25

        if not re.search(r'\b(anonymization|pseudonymization|de-identification)\b', content, re.IGNORECASE):
            risks.append({
                'category': 'privacy',
                'severity': 'medium',
                'finding': 'No data anonymization or de-identification mentioned',
                'impact': 'Privacy exposure, regulatory compliance gaps',
                'remediation': 'Implement data anonymization/pseudonymization techniques'
            })
            risk_level += 15

    if re.search(r'\b(share|sharing|third[_\s]?party)\b', content, re.IGNORECASE):
        if not re.search(r'\b(privacy policy|data processing agreement|DPA)\b', content, re.IGNORECASE):
            risks.append({
                'category': 'privacy',
                'severity': 'high',
                'finding': 'Third-party data sharing without privacy agreements',
                'impact': 'Privacy violations, regulatory non-compliance',
                'remediation': 'Establish data processing agreements with third parties'
            })
            risk_level += 20

    return {
        'risk_level': min(risk_level, 100),
        'privacy_coverage': privacy_mentions,
        'risks': risks,
        'compliant_items': compliant_items
    }


def assess_operational_risks(content: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Assess operational and business continuity risks"""
    risks = []
    compliant_items = []
    risk_level = 0

    # Check for operational controls
    if re.search(r'\b(backup|disaster recovery|business continuity)\b', content, re.IGNORECASE):
        compliant_items.append("Business continuity planning addressed")
    else:
        risks.append({
            'category': 'operational',
            'severity': 'medium',
            'finding': 'No business continuity or disaster recovery plan',
            'impact': 'Service disruption, data loss in case of incidents',
            'remediation': 'Develop and test business continuity and disaster recovery plans'
        })
        risk_level += 15

    if re.search(r'\b(incident response|incident management)\b', content, re.IGNORECASE):
        compliant_items.append("Incident response procedures defined")
    else:
        risks.append({
            'category': 'operational',
            'severity': 'high',
            'finding': 'No incident response procedures',
            'impact': 'Delayed response to security incidents, increased damage',
            'remediation': 'Establish incident response procedures and playbooks'
        })
        risk_level += 20

    if re.search(r'\b(change management|change control)\b', content, re.IGNORECASE):
        compliant_items.append("Change management processes in place")
    else:
        risks.append({
            'category': 'operational',
            'severity': 'medium',
            'finding': 'No change management process mentioned',
            'impact': 'Uncontrolled changes, potential service disruptions',
            'remediation': 'Implement formal change management procedures'
        })
        risk_level += 10

    if re.search(r'\b(SLA|service level|uptime)\b', content, re.IGNORECASE):
        compliant_items.append("Service level commitments defined")

    return {
        'risk_level': min(risk_level, 100),
        'risks': risks,
        'compliant_items': compliant_items
    }


def calculate_overall_risk_score(assessments: Dict[str, Any]) -> int:
    """Calculate overall risk score (0-100, higher = more risk)"""
    # Weight different risk categories
    security_weight = 0.40
    privacy_weight = 0.25
    operational_weight = 0.20
    compliance_weight = 0.15

    security_risk = assessments['security']['risk_level']
    privacy_risk = assessments['privacy']['risk_level']
    operational_risk = assessments['operational']['risk_level']

    # Calculate compliance risk from compliance status
    compliance_risk = 0
    if assessments['compliance']:
        avg_compliance = sum(
            100 - f['compliance_score']
            for f in assessments['compliance'].values()
        ) / len(assessments['compliance'])
        compliance_risk = avg_compliance

    overall_risk = (
        security_risk * security_weight +
        privacy_risk * privacy_weight +
        operational_risk * operational_weight +
        compliance_risk * compliance_weight
    )

    return int(overall_risk)


def determine_risk_rating(risk_score: int) -> Tuple[str, str]:
    """Determine risk rating and color from score"""
    if risk_score >= 75:
        return "CRITICAL", "red"
    elif risk_score >= 50:
        return "HIGH", "orange"
    elif risk_score >= 25:
        return "MEDIUM", "yellow"
    else:
        return "LOW", "green"


def generate_remediation_plan(all_risks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Generate prioritized remediation plan"""
    # Sort risks by severity
    severity_priority = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    sorted_risks = sorted(
        all_risks,
        key=lambda r: severity_priority.get(r['severity'], 4)
    )

    remediation_plan = []
    for i, risk in enumerate(sorted_risks, 1):
        remediation_plan.append({
            'priority': i,
            'severity': risk['severity'],
            'category': risk['category'],
            'finding': risk['finding'],
            'remediation': risk['remediation'],
            'impact': risk['impact']
        })

    return remediation_plan


def review_risk(
    artifact_path: str,
    artifact_type: Optional[str] = None,
    policy_frameworks: Optional[List[str]] = None,
    risk_threshold: str = 'medium',
    assessment_scope: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Perform comprehensive risk assessment and policy compliance review

    Args:
        artifact_path: Path to artifact file
        artifact_type: Type of artifact (optional)
        policy_frameworks: List of policy frameworks to assess against
        risk_threshold: Risk threshold level
        assessment_scope: Specific assessment areas to focus on

    Returns:
        Risk assessment report with findings and recommendations
    """
    file_path = Path(artifact_path)

    try:
        content, data, file_format = load_artifact(file_path)
    except FileNotFoundError as e:
        return {
            'success': False,
            'error': str(e),
            'risk_score': 100,
            'risk_rating': 'CRITICAL'
        }

    # Default frameworks if none specified
    if not policy_frameworks:
        policy_frameworks = ['SOC2', 'ISO27001', 'GDPR']

    # Initialize assessment
    assessment_time = datetime.now().isoformat()

    # Perform risk assessments
    security_assessment = assess_security_risks(content, data)
    privacy_assessment = assess_privacy_risks(content, data)
    operational_assessment = assess_operational_risks(content, data)
    compliance_assessment = assess_compliance_risks(content, data, policy_frameworks)

    # Collect all risks
    all_risks = (
        security_assessment['risks'] +
        privacy_assessment['risks'] +
        operational_assessment['risks']
    )

    # Calculate overall risk score
    assessments = {
        'security': security_assessment,
        'privacy': privacy_assessment,
        'operational': operational_assessment,
        'compliance': compliance_assessment
    }

    risk_score = calculate_overall_risk_score(assessments)
    risk_rating, risk_color = determine_risk_rating(risk_score)

    # Generate remediation plan
    remediation_plan = generate_remediation_plan(all_risks)

    # Generate audit report
    audit_report = {
        'artifact_path': str(file_path.absolute()),
        'artifact_type': artifact_type or 'unknown',
        'assessment_date': assessment_time,
        'assessor': 'Betty Risk Review Skill v1.0.0',
        'policy_frameworks': policy_frameworks,
        'risk_score': risk_score,
        'risk_rating': risk_rating,
        'total_findings': len(all_risks),
        'critical_findings': sum(1 for r in all_risks if r['severity'] == 'critical'),
        'high_findings': sum(1 for r in all_risks if r['severity'] == 'high'),
        'medium_findings': sum(1 for r in all_risks if r['severity'] == 'medium'),
        'findings': all_risks,
        'remediation_plan': remediation_plan
    }

    return {
        'success': True,
        'risk_assessment': {
            'risk_score': risk_score,
            'risk_rating': risk_rating,
            'security': security_assessment,
            'privacy': privacy_assessment,
            'operational': operational_assessment
        },
        'compliance_status': compliance_assessment,
        'audit_report': audit_report,
        'remediation_plan': remediation_plan
    }


def main():
    """Main entry point for risk.review skill"""
    parser = argparse.ArgumentParser(
        description='Policy compliance and risk assessment for artifacts'
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
        '--output',
        type=str,
        help='Save assessment report to file'
    )

    args = parser.parse_args()

    # Perform risk assessment
    result = review_risk(
        artifact_path=args.artifact_path,
        artifact_type=args.artifact_type,
        policy_frameworks=args.policy_frameworks,
        risk_threshold=args.risk_threshold
    )

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)
        print(f"\nRisk assessment report saved to: {output_path}")

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
    print(f"")
    print(f"OVERALL RISK RATING: {audit['risk_rating']}")
    print(f"Risk Score:          {audit['risk_score']}/100")
    print(f"")
    print(f"FINDINGS SUMMARY:")
    print(f"  Total Findings:    {audit['total_findings']}")
    print(f"  Critical:          {audit['critical_findings']}")
    print(f"  High:              {audit['high_findings']}")
    print(f"  Medium:            {audit['medium_findings']}")
    print(f"")

    # Compliance Status
    print(f"COMPLIANCE STATUS:")
    for framework, status in result['compliance_status'].items():
        print(f"\n  {status['framework_name']} ({framework}):")
        print(f"    Status: {status['status'].upper()}")
        print(f"    Compliance Score: {status['compliance_score']:.1f}%")
        if status['gaps']:
            print(f"    Gaps Identified: {len(status['gaps'])}")
    print()

    # Risk Breakdown
    print(f"RISK BREAKDOWN:")
    print(f"  Security Risk:     {risk_assessment['security']['risk_level']}/100")
    print(f"  Privacy Risk:      {risk_assessment['privacy']['risk_level']}/100")
    print(f"  Operational Risk:  {risk_assessment['operational']['risk_level']}/100")
    print()

    # Critical/High Findings
    critical_high = [r for r in audit['findings'] if r['severity'] in ['critical', 'high']]
    if critical_high:
        print(f"CRITICAL & HIGH SEVERITY FINDINGS:")
        for finding in critical_high:
            severity_marker = "🔴" if finding['severity'] == 'critical' else "🟠"
            print(f"\n  {severity_marker} {finding['severity'].upper()}: {finding['finding']}")
            print(f"     Category: {finding['category']}")
            print(f"     Impact: {finding['impact']}")
            print(f"     Remediation: {finding['remediation']}")
        print()

    # Remediation Plan
    if result['remediation_plan']:
        print(f"TOP REMEDIATION PRIORITIES:")
        for item in result['remediation_plan'][:5]:
            print(f"  {item['priority']}. [{item['severity'].upper()}] {item['finding']}")
            print(f"     → {item['remediation']}")
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
