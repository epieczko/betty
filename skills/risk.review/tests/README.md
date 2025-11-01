# risk.review Skill - Test Suite

Comprehensive test suite for the `risk.review` skill covering security, privacy, operational, and compliance risk assessments.

## Test Coverage

### Unit Tests (40 tests total)

#### 1. Artifact Loading (3 tests)
- `test_load_valid_yaml_artifact` - Validates YAML artifact loading
- `test_load_nonexistent_artifact` - Error handling for missing files
- `test_load_invalid_yaml` - Graceful handling of malformed YAML

#### 2. Security Risk Assessment (6 tests)
- `test_high_risk_security_issues` - Detects high-risk security patterns
- `test_low_risk_security_profile` - Validates good security posture detection
- `test_detect_hardcoded_credentials` - Identifies hardcoded secrets/passwords
- `test_detect_unencrypted_http` - Flags unencrypted HTTP connections
- `test_missing_authentication_controls` - Identifies missing auth/authz
- `test_security_coverage_scoring` - Validates security coverage metrics

#### 3. Privacy Risk Assessment (5 tests)
- `test_high_privacy_risk` - Detects high-risk privacy issues
- `test_gdpr_compliant_privacy` - Validates GDPR compliance detection
- `test_missing_consent_mechanism` - Identifies missing consent controls
- `test_missing_data_anonymization` - Detects lack of anonymization
- `test_third_party_sharing_risk` - Flags third-party sharing without DPA

#### 4. Operational Risk Assessment (5 tests)
- `test_high_operational_risk` - Detects operational risk patterns
- `test_robust_operational_controls` - Validates operational best practices
- `test_missing_business_continuity` - Identifies missing BC/DR plans
- `test_missing_incident_response` - Detects missing IR procedures
- `test_missing_change_management` - Flags missing change control

#### 5. Compliance Assessment (7 tests)
- `test_soc2_compliance_assessment` - SOC2 compliance evaluation
- `test_gdpr_compliance_assessment` - GDPR compliance evaluation
- `test_iso27001_compliance_assessment` - ISO27001 compliance evaluation
- `test_hipaa_compliance_assessment` - HIPAA compliance evaluation
- `test_multiple_frameworks` - Multi-framework assessment
- `test_compliance_gap_identification` - Gap analysis validation
- `test_invalid_framework` - Error handling for invalid frameworks

#### 6. Risk Scoring and Rating (3 tests)
- `test_calculate_overall_risk_score` - Overall risk score calculation
- `test_risk_score_weights` - Validates weighted scoring algorithm
- `test_determine_risk_rating` - Rating determination (CRITICAL/HIGH/MEDIUM/LOW)

#### 7. Remediation Planning (2 tests)
- `test_generate_remediation_plan` - Remediation plan generation
- `test_remediation_plan_priority_sorting` - Priority-based sorting

#### 8. Integration Workflow (7 tests)
- `test_high_risk_artifact_workflow` - End-to-end high-risk assessment
- `test_low_risk_artifact_workflow` - End-to-end low-risk assessment
- `test_medium_risk_artifact_workflow` - End-to-end medium-risk assessment
- `test_nonexistent_file_error_handling` - Error handling validation
- `test_default_frameworks` - Default framework selection
- `test_audit_report_structure` - Audit report schema validation
- `test_risk_assessment_structure` - Risk assessment schema validation

#### 9. Policy Frameworks (2 tests)
- `test_all_frameworks_defined` - Validates framework definitions
- `test_framework_structure` - Framework schema validation

## Test Fixtures

Located in `tests/fixtures/`:

### high-risk-artifact.yaml
- Hardcoded credentials
- Unencrypted HTTP connections
- No encryption or authentication
- Personal data handling without consent
- No backup/DR plan

**Expected:** Risk Score > 50, Rating: HIGH or CRITICAL

### medium-risk-artifact.yaml
- OAuth authentication ✓
- TLS encryption ✓
- RBAC access control ✓
- Missing incident response
- Missing change management
- Missing BC/DR
- Third-party sharing without DPA

**Expected:** Risk Score 20-60, Rating: MEDIUM or HIGH

### low-risk-artifact.yaml
- Comprehensive security controls
- HIPAA/SOC2/ISO27001/NIST compliance
- MFA authentication
- Encryption at rest and in transit
- Privacy by design (GDPR)
- Incident response and BC/DR plans
- Full audit logging and monitoring

**Expected:** Risk Score < 30, Rating: LOW

### gdpr-compliant-artifact.yaml
- GDPR-specific controls
- Data subject rights
- Privacy by design
- DPO designation
- Breach notification procedures

**Used for:** GDPR compliance testing

### invalid-artifact.yaml
- Malformed YAML syntax

**Used for:** Error handling testing

## Running Tests

### Run Full Test Suite
```bash
cd /home/user/betty/skills/risk.review
python3 -m pytest tests/test_risk_review.py -v
```

### Run Specific Test Class
```bash
python3 -m pytest tests/test_risk_review.py::TestSecurityRiskAssessment -v
```

### Run Single Test
```bash
python3 -m pytest tests/test_risk_review.py::TestSecurityRiskAssessment::test_detect_hardcoded_credentials -v
```

### Run with Coverage
```bash
python3 -m pytest tests/test_risk_review.py --cov=risk_review --cov-report=html
```

### Run with Verbose Output
```bash
python3 -m pytest tests/test_risk_review.py -vv --tb=long
```

## Test Requirements

- Python 3.11+
- pytest >= 8.0
- pyyaml

Install dependencies:
```bash
pip install pytest pyyaml
```

## Key Features Tested

### 1. Negation Detection
Tests validate that phrases like "No backup plan" and "Missing incident response" are properly detected as risks, not as positive controls.

### 2. Pattern Matching
- Hardcoded credentials: `password: value`, `api_key: secret123`
- Unencrypted connections: `http://` URLs
- Missing controls: absence of security keywords

### 3. Risk Scoring Algorithm
- Security risks: 40% weight
- Privacy risks: 25% weight
- Operational risks: 20% weight
- Compliance risks: 15% weight

### 4. Compliance Frameworks
Tests validate assessment against:
- SOC2 Type II
- ISO/IEC 27001
- GDPR
- HIPAA
- PCI-DSS
- NIST Cybersecurity Framework

### 5. Risk Ratings
- CRITICAL: Score >= 75
- HIGH: Score >= 50
- MEDIUM: Score >= 25
- LOW: Score < 25

## Continuous Integration

The test suite is designed for CI/CD integration:

```yaml
# Example GitHub Actions workflow
- name: Run risk.review tests
  run: |
    cd skills/risk.review
    python3 -m pytest tests/test_risk_review.py -v --tb=short
```

## Test Maintenance

### Adding New Tests
1. Create test method in appropriate class
2. Use descriptive test names starting with `test_`
3. Follow AAA pattern: Arrange, Act, Assert
4. Add docstring explaining test purpose

### Adding New Fixtures
1. Create YAML file in `tests/fixtures/`
2. Include realistic artifact structure
3. Document expected risk score range
4. Add corresponding integration test

### Updating Risk Detection
When modifying risk assessment logic:
1. Update corresponding unit tests
2. Update test fixtures if needed
3. Verify all integration tests pass
4. Update expected risk scores in documentation

## Known Limitations

1. **Pattern Matching:** Uses regex patterns, not semantic analysis
2. **Negation Detection:** Looks for negation words within 20 characters before match
3. **Compound Phrases:** "No X or Y" requires separate bullet points for proper detection
4. **Language:** English-only content analysis

## Future Enhancements

- [ ] Add performance benchmarks
- [ ] Add mutation testing
- [ ] Add property-based testing
- [ ] Add test coverage reporting
- [ ] Add integration with Betty CI/CD pipeline
- [ ] Add tests for CLI argument parsing
- [ ] Add tests for output file generation
