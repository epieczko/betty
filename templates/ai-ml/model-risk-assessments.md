# Model Risk Assessment
<!-- See also: artifact_descriptions/model-risk-assessments.md for complete guidance -->
<!-- YAML version available at: model-risk-assessments.yaml -->

## Purpose

Model Risk Assessment evaluates AI/ML models for potential harms, biases, security vulnerabilities, regulatory compliance risks, and ethical concerns. This assessment is **mandatory for high-risk models** per EU AI Act and follows NIST AI Risk Management Framework.

**YAML Version**: Use `model-risk-assessments.yaml` for structured risk data and automated risk scoring. This markdown version provides narrative risk analysis.

---

## Model Information

**Model Name**: Credit Approval Recommendation Model

**Model Version**: 3.0.0

**Assessment Date**: 2024-10-26

**Assessment Type**: Pre-Deployment Risk Assessment

**Assessor**: AI Risk Team

**Risk Level**: **High**

---

## Risk Classification (EU AI Act)

**Risk Category**: **High-Risk AI System**

**EU AI Act Article**: Annex III, Point 5(b) - "AI systems intended to be used to evaluate the creditworthiness of natural persons"

**Regulatory Obligations**:
- Mandatory risk management system
- High-quality training data
- Technical documentation
- Transparency to users
- Human oversight
- Accuracy, robustness, cybersecurity

---

## Risk Identification & Assessment

### RISK-001: Fairness & Bias Risk

**Category**: Fairness & Bias

**Description**: Potential discriminatory impact on protected groups (age, gender, race, disability) leading to unequal access to credit

**Likelihood**: Medium (bias is common in credit scoring without mitigation)

**Impact**: High (violates ECOA, FCRA; reputational damage; regulatory fines)

**Regulatory Exposure**: 
- Equal Credit Opportunity Act (ECOA) violations (fines up to $10,000 per violation)
- Fair Housing Act violations
- EU AI Act non-compliance (fines up to €30M or 6% of global revenue)

**Mitigation Strategies**:
1. **Fairness Metrics Monitoring** (Quarterly)
   - Demographic Parity: Selection rate difference < 10% across protected groups
   - Equalized Odds: TPR and FPR difference < 5%
   - Calibration: Predicted probabilities match actual outcomes

2. **Training Data Balancing**
   - Ensure representative samples across demographic groups
   - Oversample underrepresented groups (SMOTE)
   - Remove historical bias from training data

3. **Feature Engineering**
   - Exclude protected attributes (race, gender) from model features
   - Use "fairness-aware" feature selection
   - Avoid proxy features (zip code as proxy for race)

4. **Third-Party Audits**
   - Quarterly bias audits by independent auditor
   - Document findings and remediation

**Evidence of Mitigation**: 
- Bias testing report Q4 2024: All fairness metrics within thresholds
- Demographic Parity (age groups): 7.2% difference (Pass: < 10%)
- Equalized Odds (gender): TPR diff 3.1%, FPR diff 2.8% (Pass: < 5%)

**Residual Risk**: **Low** (after mitigation)

---

### RISK-002: Model Performance Degradation

**Category**: Model Performance

**Description**: Model accuracy degrades over time due to changing economic conditions, population shifts, or concept drift

**Likelihood**: High (credit markets are dynamic)

**Impact**: Medium (poor decisions lead to financial loss, but not immediate harm)

**Mitigation Strategies**:
1. **Continuous Monitoring**
   - Daily: F1 score, precision, recall
   - Weekly: AUC-ROC, calibration error
   - Monthly: Confusion matrix analysis

2. **Automated Retraining**
   - Trigger: F1 score < 0.85 for 3 consecutive days
   - Trigger: Data drift detected (KL divergence > 0.1)
   - Scheduled: Quarterly retraining on new data

3. **Drift Detection**
   - Feature distribution monitoring
   - Prediction distribution monitoring
   - Alert ML Ops on drift detection

**Evidence of Mitigation**: 
- Monitoring dashboard live in staging: https://grafana.company.com/d/credit-model-monitoring
- Automated retraining tested in staging (triggers correctly)

**Residual Risk**: **Low**

---

### RISK-003: Explainability & Transparency

**Category**: Explainability

**Description**: Applicants denied credit without clear explanation violates GDPR Article 22 (right to explanation)

**Likelihood**: High (without mitigation, black-box model)

**Impact**: Critical (GDPR fines up to €20M or 4% of global revenue; reputational harm)

**Mitigation Strategies**:
1. **SHAP Explanations**
   - Generate SHAP values for every prediction
   - Display top 3 contributing factors to applicant
   - Example: "Credit denied due to: 1) High debt-to-income ratio, 2) Recent late payments, 3) Limited credit history"

2. **Adverse Action Notices** (FCRA Compliance)
   - Provide reason codes for denials
   - Include applicant rights and dispute process
   - Example reason codes: "Debt obligations too high", "Length of credit history too short"

3. **Human Review Process**
   - Every denial reviewed by loan officer before final decision
   - Applicant can request human review
   - Response within 5 business days

**Evidence of Mitigation**:
- SHAP explanation module tested (generates explanations in < 100ms)
- Adverse action notice template approved by Legal
- Human review process documented in SOPs

**Residual Risk**: **Low**

---

### RISK-004: Security & Adversarial Attacks

**Category**: Security

**Description**: Adversarial manipulation of inputs to fraudulently obtain loan approvals

**Likelihood**: Low (requires sophisticated attacker)

**Impact**: High (financial fraud, loan defaults)

**Mitigation Strategies**:
1. **Input Validation**
   - Sanitize all inputs
   - Range checks (income > 0, age 18-100)
   - Format validation (SSN, phone number)

2. **Anomaly Detection**
   - Flag outlier inputs (income > $1M, debt-to-income > 10x normal)
   - Alert for sudden applicant behavior changes

3. **Rate Limiting**
   - Max 10 prediction requests per applicant per day
   - Prevents brute-force adversarial attacks

4. **Human Review for High-Value Loans**
   - All loans > $50,000 require manual underwriting
   - Loan officer verifies input data authenticity

**Evidence of Mitigation**:
- Security testing completed (no successful adversarial attacks in 1000 test cases)
- Input validation tested with malformed data (100% caught)

**Residual Risk**: **Low**

---

### RISK-005: Privacy & Data Protection

**Category**: Privacy

**Description**: Model inadvertently leaks sensitive information through predictions or explanations

**Likelihood**: Low (with proper data handling)

**Impact**: High (GDPR fines, breach of trust)

**Mitigation Strategies**:
1. **Data Minimization**
   - Only collect necessary features
   - Drop PII from training data (SSN, account numbers)

2. **Differential Privacy**
   - Apply differential privacy during training (epsilon = 1.0)
   - Adds noise to prevent information leakage

3. **Encryption**
   - Encrypt all PII in transit and at rest (AES-256)
   - Use tokenization for sensitive fields

4. **Privacy Impact Assessment**
   - Completed and approved by Data Protection Officer
   - Documents data flows and privacy controls

**Evidence of Mitigation**:
- Privacy Impact Assessment approved 2024-10-20
- Differential privacy implemented and tested
- PII encryption verified

**Residual Risk**: **Low**

---

## Risk Summary Matrix

| Risk ID | Risk Category | Likelihood | Impact | Residual Risk | Status |
|---------|---------------|------------|--------|---------------|--------|
| RISK-001 | Fairness & Bias | Medium | High | Low | Mitigated |
| RISK-002 | Performance Degradation | High | Medium | Low | Mitigated |
| RISK-003 | Explainability | High | Critical | Low | Mitigated |
| RISK-004 | Security | Low | High | Low | Mitigated |
| RISK-005 | Privacy | Low | High | Low | Mitigated |

**Overall Risk Score**: **High** → **Low** (after mitigation)

**Residual Risk Acceptable**: **Yes** (approved by Chief Risk Officer)

---

## Human Oversight (EU AI Act Article 14)

**Requirement**: Mandatory for high-risk AI systems

**Implementation**:
1. **Human-in-the-loop**: Every credit denial reviewed by loan officer before final decision
2. **Right to contest**: Applicants can request human review of automated decision
3. **Override capability**: Loan officer can override model recommendation with justification
4. **Training**: Loan officers complete AI ethics training annually

**Audit Trail**: All human overrides logged and reviewed monthly

---

## Monitoring Plan

**Metrics**:
- **Performance**: F1 score daily (threshold > 0.85)
- **Fairness**: Demographic Parity weekly (threshold < 10% difference)
- **Drift**: KL divergence daily (threshold < 0.1)

**Dashboards**:
- Model Performance Dashboard (Grafana)
- Fairness Monitoring Dashboard
- Data Quality Dashboard

**Alerting**:
- Critical: Fairness violation (immediate model rollback)
- High: Performance degradation (disable model, manual underwriting)
- Medium: Data drift (schedule retraining)

---

## Compliance Checklist

| Regulation | Requirement | Status |
|------------|-------------|--------|
| EU AI Act | Technical documentation | Complete |
| EU AI Act | Risk management system | Complete |
| EU AI Act | Human oversight | Complete |
| GDPR Article 22 | Right to explanation | Complete |
| GDPR Article 22 | Right to human review | Complete |
| FCRA | Adverse action notices | Complete |
| ECOA | No discrimination | Complete (fairness testing passed) |

---

## Approval & Deployment Recommendation

**Recommendation**: **Approve for Production Deployment**

**Conditions**:
- Monthly fairness audits required
- Quarterly model retraining
- Human review for all denials
- Incident response plan tested within 30 days

**Approved By**: Chief Risk Officer

**Approval Date**: 2024-10-28

**Next Review Date**: 2025-10-26 (annual review)

---

## Related Artifacts

- **YAML Version**: `model-risk-assessments.yaml` (structured risk data)
- **Model Card**: `model-cards/credit-approval-v3.md`
- **Training Data Card**: `training-data-cards/credit-applications-2024.md`
- **Fairness Report**: `bias-and-fairness-reports/credit-approval-v3-2024q4.md`
- **Explainability Report**: `explainability-reports/credit-approval-v3.md`

---

**Note**: High-risk models require annual risk assessment updates. Any significant model changes (architecture, training data, features) trigger a new risk assessment.
