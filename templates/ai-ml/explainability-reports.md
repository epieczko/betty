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

<!-- Provide a 2-3 paragraph overview for executive audience -->
<!-- What is this document about and why does it matter? -->

## Purpose

<!-- This artifact serves as the documentation standard for generating and publishing AI/ML model explainability reports using SHAP, LIME, and other interpretability frameworks. Reports translate model pre... -->

## Scope

### In Scope

- SHAP (Shapley Additive Explanations) feature importance reports for tabular, tree-based, and deep learning models
- LIME (Local Interpretable Model-Agnostic Explanations) for individual prediction explanations
- Feature importance rankings (global and local explanations)
- Counterfactual explanations (minimal changes needed to flip prediction)
- Partial dependence plots (how predictions change with feature values)

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- Data Science Teams: Generate explainability reports for model validation and stakeholder communication
- Model Risk Management: Review model explanations for compliance and risk assessment
- Compliance Officers: Ensure AI systems meet EU AI Act and GDPR transparency requirements

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Model-Appropriate Explainer**: Use TreeExplainer for tree-based models (XGBoost, LightGBM, Random Forest), KernelExplainer for model-agnostic explanations

**SHAP for Global Importance**: Generate SHAP summary plots showing feature importance distributions across entire dataset

**LIME for Individual Explanations**: Use LIME to explain specific high-stakes predictions (loan denials, fraud flags)

**Counterfactual Scenarios**: Provide actionable counterfactuals ("If income increased $5K, loan would be approved")

**Protected Class Analysis**: Always disaggregate model performance and explanations by protected classes (race, gender, age)

## Quality Checklist

Before finalizing this artifact, verify:

- [ ] **Completeness**: All required sections present and adequately detailed
- [ ] **Accuracy**: Information verified and validated by appropriate subject matter experts
- [ ] **Clarity**: Written in clear, unambiguous language appropriate for intended audience
- [ ] **Consistency**: Aligns with organizational standards, templates, and related artifacts
- [ ] **Currency**: Based on current information; outdated content removed or updated

## Related Documents

- [Related Artifact]: Description and relationship

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | Name | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
