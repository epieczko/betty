# Analytics Model Documentation

> **Purpose**: Comprehensive documentation for machine learning models, statistical models, and analytics pipelines following Model Cards (Google), Datasheets for Datasets (Microsoft), and ML metadata frameworks.
>
> **See also**: `artifact_descriptions/analytics-model-documentation.md` | YAML version: `analytics-model-documentation.yaml`

## Document Metadata

```yaml
version: 1.0.0
modelId: churn-prediction-v3
created: 2025-01-15
owner: Data Science Team
classification: Confidential
regulatoryScope: GDPR Article 22, EU AI Act
lastReviewed: 2025-01-15
productionStatus: Active
```

---

## Example 1: Customer Churn Prediction (SaaS)

### Model Overview

```yaml
model:
  name: customer_churn_prediction_v3
  version: 3.2.1
  type: Binary Classification (XGBoost)
  use_case: Predict 30-day customer churn probability
  business_impact: $2.5M annual revenue retention
  owner: jane.doe@company.com

algorithm:
  name: XGBoost Classifier
  library: xgboost==1.7.4
  hyperparameters:
    n_estimators: 500
    max_depth: 6
    learning_rate: 0.05
    objective: binary:logistic

training_data:
  dataset: customer_features_2024Q4
  rows: 125,000 customers
  positive_class: 18,500 (14.8% churn rate)
  train_split: 70% (2023-01 to 2024-06)
  val_split: 15% (2024-07 to 2024-08)
  test_split: 15% (2024-09 to 2024-09)
```

### Features (42 total)

| Feature | Type | Description | SHAP Importance | Source |
|---------|------|-------------|-----------------|--------|
| `days_since_last_login` | Numeric | Days since last platform login | 0.18 | app_events |
| `support_tickets_30d` | Numeric | Support tickets (last 30 days) | 0.15 | zendesk |
| `feature_adoption_score` | Numeric | % of key features used | 0.12 | usage_analytics |
| `payment_failures_90d` | Numeric | Payment failures (last 90 days) | 0.11 | stripe |

### Performance Metrics

| Metric | Test Set | Production (30d) | Threshold |
|--------|----------|------------------|-----------|
| AUC-ROC | 0.872 | 0.865 | >= 0.850 |
| Precision @ 20% recall | 78.3% | 76.1% | >= 75.0% |
| False Positive Rate | 4.5% | 4.8% | <= 5.0% |

**Confusion Matrix (Test, threshold=0.5)**:
- True Negatives: 14,850 | False Positives: 700
- False Negatives: 1,200 | True Positives: 2,000

### Fairness Analysis

```yaml
fairness_assessment:
  sensitive_attributes:
    - company_size (SMB, Mid-market, Enterprise)
    - geographic_region (US, EMEA, APAC)

  disparity_metrics:
    fpr_parity:
      smb_fpr: 4.8%
      enterprise_fpr: 4.2%
      ratio: 1.14 (< 1.25 threshold: PASS)

  mitigation:
    - Oversampled underrepresented industries
    - Per-segment calibration
    - Human review for high-risk predictions
```

### Deployment

```yaml
deployment:
  platform: AWS SageMaker
  endpoint: churn-prediction-v3-prod
  instance: ml.m5.large (2-10 auto-scale)

  api:
    url: https://api.company.com/ml/churn/predict
    latency_p95: 120ms (target: < 150ms)

  monitoring:
    psi_threshold: 0.10 (retraining trigger)
    drift_checks: Daily
    retraining_cadence: Quarterly (minimum)
```

---

## Example 2: Product Recommendation (E-Commerce)

### Model Overview

```yaml
model:
  name: product_recommendations_transformer
  version: 2.1.0
  type: Two-Tower Neural Network
  framework: tensorflow==2.13.0
  use_case: Personalized homepage recommendations

architecture:
  user_tower:
    - Embedding (user_id, purchase_history, browsing)
    - Dense layers: [512, 256, 128]
    - Output: 128-dim embedding

  item_tower:
    - Embedding (product_id, category, attributes)
    - Dense layers: [512, 256, 128]
    - Output: 128-dim embedding

  retrieval:
    - Dot product similarity
    - FAISS approximate nearest neighbors
    - Top-50 candidates -> XGBoost re-ranker -> Top-10
```

### Performance

| Metric | Offline | Online A/B Test |
|--------|---------|-----------------|
| Recall@10 | 0.42 | - |
| NDCG@10 | 0.58 | - |
| CTR | - | 8.2% (+18% vs baseline) |
| Revenue/User | - | $12.40 (+15%) |

**Latency Budget**:
- User embedding: 15ms
- FAISS retrieval: 8ms
- Re-ranking: 12ms
- Total p95: < 50ms

---

## Example 3: Fraud Detection (FinTech)

### Model Overview

```yaml
model:
  name: transaction_fraud_detector
  version: 4.5.2
  type: Ensemble (XGBoost + Rules)
  use_case: Real-time fraud detection
  latency_p95: 100ms (max: 500ms timeout)
  throughput: 15,000 TPS (peak)
  compliance: PCI-DSS, SOC 2

decision_thresholds:
  - score >= 0.90: Decline transaction
  - score 0.70-0.89: Step-up auth (SMS OTP)
  - score 0.30-0.69: Allow + manual review flag
  - score < 0.30: Allow

performance:
  precision: 0.87
  recall: 0.72
  false_positive_rate: 0.3%
  fraud_prevented: $8.5M/year
  false_decline_cost: $420K/year
```

### Real-Time Feature Engineering

```python
# Apache Flink streaming features
features = (
    transaction_stream
    .join(customer_profile)
    .join(merchant_risk)
    .select(
        "amount",
        "customer_lifetime_value",
        "customer_fraud_history_30d",
        "merchant_fraud_rate_7d",
        "transaction_velocity_1h",
        "device_fingerprint_risk",
        "geolocation_anomaly"
    )
)
```

---

## Model Card Template (Following Google Model Cards Standard)

### Model Details
- **Developer**: Data Science Team
- **Model date**: 2024-12-01
- **Model version**: 3.2.1
- **Model type**: XGBoost Binary Classifier
- **License**: Proprietary

### Intended Use
- **Primary use**: Customer churn prediction for retention campaigns
- **Primary users**: Customer Success teams, Marketing
- **Out-of-scope**: Pricing decisions, credit scoring, employment

### Factors
- **Relevant factors**: Company size, industry, account age
- **Evaluation factors**: Tested across all customer segments

### Metrics
- **Performance**: AUC 0.872, Precision@20%Recall 78.3%
- **Thresholds**: High risk >= 0.7, Medium 0.4-0.7, Low < 0.4
- **Uncertainty**: 95% confidence intervals reported

### Training Data
- **Dataset**: 125K customers, 18 months (Jan 2023 - Sep 2024)
- **Preprocessing**: SMOTE oversampling, feature normalization
- **Label**: Churn within 30 days of observation

### Quantitative Analysis
- **Overall**: AUC 0.872 on held-out test set
- **Intersectional**: Evaluated across company size, region, industry
- **Fairness**: FPR parity within 1.14x across segments

### Ethical Considerations
- **PII usage**: Customer behavioral data (consented)
- **Human review**: Required for high-risk scores (>= 0.7)
- **Mitigation**: Opt-out available, transparency in communications

### Caveats
- **Limitations**: 12% lower accuracy for customers < 90 days tenure
- **Recommendations**: Use with human-in-the-loop for enterprise customers

---

## Explainability Example (SHAP)

```python
import shap

# Generate SHAP explanations
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)

# Feature importance
shap.plots.bar(shap_values)

# Individual prediction explanation
customer_id = "CUST-98765"
prediction = model.predict_proba(customer_features)[0][1]  # 0.82

print(f"Churn probability: {prediction:.2f}")
print("Top factors:")
print("- 45 days since last login (+0.25 SHAP)")
print("- 8 support tickets in 30d (+0.18 SHAP)")
print("- 2 payment failures (+0.12 SHAP)")
```

---

## Monitoring Dashboard

```sql
-- Model Performance Monitoring
WITH predictions AS (
  SELECT
    DATE_TRUNC('day', prediction_timestamp) as pred_date,
    AVG(churn_probability) as avg_score,
    STDDEV(churn_probability) as std_score,
    COUNT(*) as prediction_count
  FROM ml_predictions.churn_scores
  WHERE prediction_timestamp > CURRENT_DATE - 30
  GROUP BY 1
)
SELECT
  pred_date,
  avg_score,
  CASE
    WHEN ABS(avg_score - 0.148) > 2 * std_score THEN 'ALERT: Score drift detected'
    ELSE 'OK'
  END as drift_status
FROM predictions
ORDER BY pred_date DESC;
```

---

**Document Owner**: Data Science Team
**Last Updated**: 2025-01-15
**Approvals**: VP Engineering, Legal, AI Ethics Committee
