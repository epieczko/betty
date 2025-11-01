# risk.review Skill

## Overview

The `risk.review` skill performs comprehensive policy compliance and risk assessment on Betty Framework artifacts using **AI-native semantic analysis**. It analyzes artifacts for security risks, policy compliance, regulatory alignment, and generates detailed audit reports with prioritized remediation recommendations.

### 🆕 AI-Native Assessment

This skill leverages Claude for context-aware risk analysis that:
- Distinguishes implemented controls vs future plans ("will implement" ≠ "is implemented")
- Detects implicit risks (e.g., "public S3 bucket" → data exposure)
- Provides evidence-based findings with specific quotes from artifacts
- Understands semantic context that pattern matching cannot

**📖 See [AI Modes Documentation](README_AI_MODES.md) for complete details**

## Features

### Core Assessment
- **🤖 AI-Powered Semantic Analysis**: Context-aware risk detection using Claude API
- **⚡ Four Assessment Modes**: Smart (AI+fast), AI (pure), Fast (regex-only), Hybrid (AI vs regex comparison)
- **💰 Cost Optimization**: Automatic caching and smart pre-checks
- **Multi-Framework Compliance Assessment**: Evaluate against SOC2, ISO27001, GDPR, HIPAA, PCI-DSS, and NIST frameworks
- **Comprehensive Risk Analysis**: Security, privacy, operational, and compliance risk assessment
- **Risk Scoring**: Quantitative risk scoring (0-100) with severity ratings
- **Audit Report Generation**: Detailed findings with impact analysis and remediation guidance
- **Automated Gap Analysis**: Identify compliance gaps across policy frameworks
- **Prioritized Remediation Plans**: Actionable recommendations sorted by severity and priority

### Advanced Features
- **🔄 Hybrid Comparison Mode**: Run both AI and regex engines side-by-side to compare findings
- **📊 Metrics & Telemetry**: Track usage, costs, performance, and error rates for continuous improvement
- **👤 Human Review Workflow**: Automatically flag low-confidence findings for manual review by security professionals
- **✅ Confidence Scoring**: AI provides confidence scores (0.0-1.0) for each finding
- **🎯 Smart Prioritization**: Low-confidence critical findings get escalated for immediate review

## Usage

### Command Line

```bash
/skill/risk/review <artifact_path> [options]
```

### Options

**Assessment Options:**
- `--artifact-type`: Type of artifact (auto-detected if not provided)
- `--policy-frameworks`: Frameworks to assess against (SOC2, ISO27001, GDPR, HIPAA, PCI-DSS, NIST)
- `--risk-threshold`: Risk threshold level (low, medium, high, critical) - default: medium
- `--mode`: Assessment mode (`smart`, `ai`, `fast`, `hybrid`) - default: smart
  - `smart`: AI with fast pre-checks (recommended)
  - `ai`: Pure AI semantic analysis
  - `fast`: Regex patterns only (free, for CI/CD)
  - `hybrid`: Run both AI and regex, compare results

**Performance Options:**
- `--no-cache`: Disable caching for AI assessments
- `--quiet`: Suppress progress output
- `--output`: Save assessment report to file

**Advanced Features:**
- `--show-metrics`: Display session metrics summary at end
- `--show-historical-metrics`: Show historical metrics (all-time statistics)
- `--show-review-queue`: Display pending human review queue
- `--disable-human-review`: Disable automatic flagging for human review

### Examples

```bash
# Basic risk assessment (AI smart mode)
/skill/risk/review artifacts/deployment-plan.yaml

# Pure AI mode for maximum accuracy
/skill/risk/review artifacts/security-policy.yaml --mode=ai

# Fast mode for CI/CD pipelines
/skill/risk/review artifacts/config.yaml --mode=fast

# Hybrid mode - compare AI vs regex findings
/skill/risk/review artifacts/security-policy.yaml --mode=hybrid

# Assess against specific frameworks
/skill/risk/review artifacts/security-policy.yaml --policy-frameworks SOC2 HIPAA GDPR

# Save detailed report
/skill/risk/review artifacts/architecture.yaml --output reports/risk-assessment.yaml --mode=ai

# Show metrics after assessment
/skill/risk/review artifacts/config.yaml --show-metrics

# View pending human review queue
/skill/risk/review --show-review-queue

# Disable caching for fresh assessment
/skill/risk/review artifacts/data-processing.yaml --no-cache
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| artifact_path | string | Yes | Path to artifact file to assess |
| artifact_type | string | No | Type of artifact (auto-detected) |
| policy_frameworks | array | No | Policy frameworks to assess against |
| risk_threshold | string | No | Risk threshold (low/medium/high/critical) |
| assessment_scope | array | No | Focus areas (security/privacy/compliance/operational) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| risk_assessment | object | Comprehensive risk assessment with findings and risk ratings |
| compliance_status | object | Policy compliance status by framework with gap analysis |
| risk_score | number | Overall risk score from 0-100 (higher = more risk) |
| audit_report | object | Detailed audit report with remediation plan |

## Risk Assessment Categories

### Security Risks
- Authentication and authorization controls
- Encryption and data protection
- Credential management
- Vulnerability management
- Audit logging and monitoring

### Privacy Risks
- Personal data handling
- Consent management
- Data subject rights
- Third-party data sharing
- Data anonymization/pseudonymization

### Operational Risks
- Business continuity planning
- Disaster recovery
- Incident response procedures
- Change management
- Service level agreements

### Compliance Assessment
- Policy framework alignment
- Control coverage analysis
- Gap identification
- Compliance scoring by framework

## Risk Ratings

- **CRITICAL** (75-100): Immediate action required, do not proceed
- **HIGH** (50-74): Significant risks, address before production
- **MEDIUM** (25-49): Moderate risks, remediate based on threshold
- **LOW** (0-24): Acceptable risk level, monitor and maintain

## Artifacts Produced

### risk-assessment.yaml
Comprehensive risk assessment with:
- Risk scores by category
- Security, privacy, operational findings
- Compliance status by framework
- Overall risk rating

### audit-report.yaml
Detailed audit report containing:
- Executive summary
- All findings with severity ratings
- Impact analysis
- Prioritized remediation plan
- Compliance gap analysis

## Dependencies

- `artifact.define`: Artifact type definitions and validation
- `artifact.validate`: Artifact schema validation

## Maintainer

**RiskOps Team**
riskops@riskexec.com

## Version

1.0.0

## License

Proprietary - RiskExec Betty Framework

## Related Skills

- `artifact.review`: Content quality review
- `artifact.validate`: Schema validation
- `compliance.check`: Policy compliance verification
- `security.scan`: Security vulnerability scanning
