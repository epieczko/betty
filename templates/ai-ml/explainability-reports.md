# Explainability Reports

> **See also**: `artifact_descriptions/explainability-reports.md` for complete guidance

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Author** | Author Name |
| **Owner** | Owner Name/Role |
| **Classification** | Internal |

## Executive Summary

The Explainability Reports provide structured, human-readable explanations of AI/ML model predictions using techniques like SHAP (Shapley values), LIME, InterpretML, and AI Explainability 360. These reports translate complex model behaviors into understandable feature importance rankings, decision b

## Purpose

This artifact serves as the documentation standard for generating and publishing AI/ML model explainability reports using SHAP, LIME, and other interpretability frameworks. Reports translate model predictions into human-understandable explanations through feature importance, decision boundaries, counterfactual scenarios, and prediction confidence intervals.

## Scope

### In Scope

- SHAP (Shapley Additive Explanations) feature importance reports for tabular, tree-based, and deep learning models
- LIME (Local Interpretable Model-Agnostic Explanations) for individual prediction explanations
- Feature importance rankings (global and local explanations)
- Counterfactual explanations (minimal changes needed to flip prediction)
- Partial dependence plots (how predictions change with feature values)

### Out of Scope

- Items explicitly not covered

## Main Content

<!-- Provide detailed content specific to this artifact type -->
<!-- Refer to the artifact description for required sections -->

## Best Practices

**Model-Appropriate Explainer**: Use TreeExplainer for tree-based models (XGBoost, LightGBM, Random Forest), KernelExplainer for model-agnostic explanations

**SHAP for Global Importance**: Generate SHAP summary plots showing feature importance distributions across entire dataset

**LIME for Individual Explanations**: Use LIME to explain specific high-stakes predictions (loan denials, fraud flags)

**Counterfactual Scenarios**: Provide actionable counterfactuals ("If income increased $5K, loan would be approved")

**Protected Class Analysis**: Always disaggregate model performance and explanations by protected classes (race, gender, age)

**Plain Language Explanations**: Translate technical feature names to business terms ("credit_utilization" → "percentage of available credit used")

**Visual Explanations**: Use SHAP force plots, waterfall charts, and feature importance bar charts for stakeholder communication

**Confidence Intervals**: Report prediction confidence alongside explanations to communicate uncertainty

## Related Documents

- [Related Artifact]: Relationship description

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
