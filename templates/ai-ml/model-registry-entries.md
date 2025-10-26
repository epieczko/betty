# Model Registry Entries
<!-- See also: artifact_descriptions/model-registry-entries.md for complete guidance -->

## Purpose

The Model Registry is the centralized catalog of all ML models across their lifecycle (development, staging, production, archived). It provides metadata, versioning, lineage, deployment history, and performance tracking for governance and MLOps.

**Model Registry Platforms**: MLflow, AWS SageMaker Model Registry, Azure ML Model Registry, Google Vertex AI Model Registry

---

## Model Registry Entry Template

### Model: fraud-detection-v2

**Model ID**: `model-fraud-detection-v2-20241026`

**Model Name**: Credit Card Fraud Detection Model v2

**Model Type**: Classification (Binary)

**Algorithm**: XGBoost Classifier

**Version**: 2.1.0 (Semantic Versioning: MAJOR.MINOR.PATCH)

**Status**: Production

**Risk Level**: High (impacts financial decisions)

---

## Model Metadata

**Owner**: Fraud Detection Team (fraud-team@company.com)

**Created Date**: 2024-08-15

**Last Updated**: 2024-10-26

**Framework**: scikit-learn 1.3.0, XGBoost 2.0.0

**Runtime**: Python 3.11

**Deployment Platform**: AWS SageMaker

**Model Artifacts**:
- Model file: `s3://models/fraud-detection/v2.1.0/model.pkl`
- Preprocessor: `s3://models/fraud-detection/v2.1.0/preprocessor.pkl`
- Feature names: `s3://models/fraud-detection/v2.1.0/features.json`

---

## Training Information

**Training Dataset**: 
- Dataset ID: `fraud-transactions-2024-q2-q3`
- Size: 5.2M transactions (100K fraudulent, 5.1M legitimate)
- Date Range: 2024-04-01 to 2024-09-30
- Class Imbalance: 1.9% fraud rate (addressed with SMOTE oversampling)

**Training Infrastructure**:
- Instance Type: ml.p3.2xlarge (GPU-accelerated)
- Training Duration: 3.2 hours
- Total Cost: $12.40

**Hyperparameters**:
```json
{
  "max_depth": 8,
  "learning_rate": 0.05,
  "n_estimators": 500,
  "scale_pos_weight": 50,
  "subsample": 0.8,
  "colsample_bytree": 0.8
}
```

**Training Metrics** (on validation set):
- Accuracy: 99.2%
- Precision: 87.3%
- Recall: 92.1%
- F1 Score: 89.6%
- AUC-ROC: 0.976

---

## Features

**Input Features** (32 total):
- `transaction_amount` (float): Transaction amount in USD
- `transaction_time` (int): Hour of day (0-23)
- `merchant_category` (categorical): MCC code
- `distance_from_home` (float): Distance in km
- `is_international` (boolean): International transaction flag
- ... (27 more features)

**Feature Engineering**:
- Rolling statistics: 24h transaction count, 7d average amount
- Velocity features: Transactions in last hour, last 24h
- Categorical encoding: One-hot encoding for merchant category

---

## Model Performance (Production Metrics - Last 30 Days)

**Online Performance**:
- Precision: 85.2% (down 2.1% from training - acceptable drift)
- Recall: 91.5% (within 1% of training)
- F1 Score: 88.2%
- False Positive Rate: 0.8% (8 false alarms per 1000 transactions)

**Prediction Latency**: 
- p50: 12ms
- p95: 28ms
- p99: 45ms

**Throughput**: 1,200 predictions/second

**Data Drift**: No significant drift detected (KL divergence < 0.05)

**Prediction Drift**: Fraud rate predictions stable at 1.8-2.0%

---

## Deployment History

| Version | Status | Deployment Date | Decommission Date | Reason |
|---------|--------|-----------------|-------------------|--------|
| 1.0.0 | Retired | 2023-05-10 | 2024-08-20 | Replaced by v2 (higher recall) |
| 2.0.0 | Retired | 2024-08-20 | 2024-10-15 | Bug fix (feature scaling issue) |
| 2.1.0 | Production | 2024-10-26 | - | Current version |

**Deployment Strategy**: Canary deployment (10% → 50% → 100% over 3 days)

**Rollback Plan**: Automated rollback if F1 score drops below 85% or false positive rate exceeds 1.5%

---

## Model Governance

**Risk Assessment**: Model Risk Assessment completed 2024-08-15 (Risk Level: High)

**Fairness Evaluation**: 
- Demographic Parity (by cardholder age): Difference < 5% (Pass)
- Equalized Odds (by gender): TPR difference < 3% (Pass)
- No significant bias detected across protected attributes

**Human Oversight**: 
- Fraud alerts reviewed by fraud analysts before card blocking
- High-value transactions (> $5,000) require manual approval

**Monitoring Dashboard**: https://grafana.company.com/d/fraud-model-monitoring

**Incident Response**: On-call ML Ops engineer (fraud-alerts channel)

---

## Model Dependencies

**Upstream Dependencies**:
- Feature Store: `fraud-features-v3` (real-time features)
- Data Pipeline: `transaction-streaming-pipeline`

**Downstream Consumers**:
- Fraud Alert Service (fraud-alert-api)
- Risk Scoring System (risk-engine)

---

## Model Lineage

**Parent Model**: fraud-detection-v1 (baseline model)

**Training Experiment**: MLflow Experiment ID `exp-fraud-20240815-v2`

**Model Card**: `model-cards/fraud-detection-v2.md`

**Training Data Card**: `training-data-cards/fraud-transactions-2024-q2-q3.md`

---

## Model Approval

**Approved By**: AI Governance Committee

**Approval Date**: 2024-08-18

**Approval Conditions**: 
- Monthly fairness audits required
- Quarterly retraining on new data
- Human review required for high-confidence fraud alerts (> 95% probability)

---

## Retraining Schedule

**Retraining Frequency**: Quarterly (every 3 months)

**Next Retraining Date**: 2025-01-26

**Retraining Trigger**: 
- Scheduled: Quarterly
- Performance degradation: F1 score < 87% for 7 consecutive days
- Data drift: KL divergence > 0.1

---

## Model Retirement

**Retirement Conditions**:
- Replaced by superior model (higher F1, lower false positive rate)
- Regulatory changes invalidate model assumptions
- Model no longer meets business requirements

**Retirement Process**:
1. Deploy replacement model (canary deployment)
2. Run both models in parallel for 30 days (shadow mode)
3. Compare performance metrics
4. Fully retire old model if replacement performs better
5. Archive model artifacts and metadata for 7 years (compliance)

---

## Related Artifacts

- **Model Card**: `model-cards/fraud-detection-v2.md`
- **Training Data Card**: `training-data-cards/fraud-transactions-2024-q2-q3.md`
- **Model Risk Assessment**: `model-risk-assessments/fraud-detection-v2.md`
- **Fairness Report**: `bias-and-fairness-reports/fraud-detection-v2-2024q4.md`
- **Experiment Logs**: MLflow Experiment ID `exp-fraud-20240815-v2`

---

**Note**: Model Registry entries should be updated after each deployment, retraining, or significant configuration change. Use MLflow API or model registry platform API for programmatic updates.
