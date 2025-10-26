# Name: explainability-reports

## Executive Summary

The Explainability Reports provide structured, human-readable explanations of AI/ML model predictions using techniques like SHAP (Shapley values), LIME, InterpretML, and AI Explainability 360. These reports translate complex model behaviors into understandable feature importance rankings, decision boundaries, and prediction rationales that enable stakeholders to trust, validate, and comply with regulatory transparency requirements (EU AI Act Article 13, GDPR automated decision-making).

As AI systems increasingly impact high-stakes decisions (credit scoring, medical diagnosis, hiring, pricing), regulators and customers demand explainability beyond black-box predictions. Explainability reports address this by generating feature attributions (which input features most influenced the prediction), counterfactual explanations (what would need to change for a different outcome), and global model behavior summaries. These reports support EU AI Act transparency obligations, model risk management frameworks, and customer trust in automated decision systems.

### Strategic Importance

- **Regulatory Compliance**: Meets EU AI Act Article 13 transparency requirements and GDPR Article 22 (automated decision-making explanation rights)
- **Model Risk Management**: Supports SR 11-7 (OCC model risk management) with documented model behavior and validation evidence
- **Customer Trust**: Provides explanation interfaces for decisions affecting individuals (loan denials, pricing, content moderation)
- **Bias Detection**: Identifies discriminatory patterns through feature importance analysis across protected classes
- **Model Debugging**: Accelerates model improvement by identifying problematic features, data quality issues, and unexpected behaviors
- **Stakeholder Alignment**: Enables non-technical business stakeholders to understand and validate model logic
- **Audit Trail**: Creates documentation trail for regulatory audits, compliance reviews, and bias assessments

## Purpose & Scope

### Primary Purpose

This artifact serves as the documentation standard for generating and publishing AI/ML model explainability reports using SHAP, LIME, and other interpretability frameworks. Reports translate model predictions into human-understandable explanations through feature importance, decision boundaries, counterfactual scenarios, and prediction confidence intervals.

### Scope

**In Scope**:
- SHAP (Shapley Additive Explanations) feature importance reports for tabular, tree-based, and deep learning models
- LIME (Local Interpretable Model-Agnostic Explanations) for individual prediction explanations
- Feature importance rankings (global and local explanations)
- Counterfactual explanations (minimal changes needed to flip prediction)
- Partial dependence plots (how predictions change with feature values)
- Model Cards (structured documentation per Google model card framework)
- EU AI Act transparency documentation (Article 13 high-risk AI systems)
- GDPR Article 22 automated decision-making explanations
- Bias and fairness analysis (disparate impact across protected classes)
- Model performance reporting (accuracy, precision, recall, F1 across subgroups)

**Out of Scope**:
- Complete model development documentation (covered in ML pipeline documentation)
- Training data provenance (handled through data lineage and provenance attestations)
- Model deployment and infrastructure (managed through MLOps documentation)
- Real-time prediction APIs (documented in API specifications)
- Model monitoring and drift detection (covered in ML observability systems)
- Adversarial robustness testing (specialized security assessment)

### Target Audience

**Primary Audience**:
- Data Science Teams: Generate explainability reports for model validation and stakeholder communication
- Model Risk Management: Review model explanations for compliance and risk assessment
- Compliance Officers: Ensure AI systems meet EU AI Act and GDPR transparency requirements

**Secondary Audience**:
- Business Stakeholders: Understand model logic and validate alignment with business rules
- Customer-Facing Teams: Explain automated decisions to affected individuals (GDPR right to explanation)
- Regulators & Auditors: Review model transparency documentation during examinations

## Document Information

**Format**: Markdown

**File Pattern**: `*.explainability-reports.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: [Define typical classification level - Public | Internal | Confidential | Restricted]

**Retention**: [Define retention period per organizational records management policy]


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Scheduled date for next formal review
- `documentOwner`: Role/person responsible for maintenance
- `classification`: Information classification level
- `retentionPeriod`: How long document must be retained

**Authorship & Review**:
- `primaryAuthor`: Lead author name and role
- `contributors`: Additional contributors and their roles
- `reviewers`: Designated reviewers (technical, security, compliance, etc.)
- `approvers`: Formal approvers with sign-off authority
- `reviewStatus`: Current review status
- `approvalDate`: Date of formal approval

**Document Purpose**:
- `executiveSummary`: 2-3 paragraph overview for executive audience
- `businessContext`: Why this document exists and its business value
- `scope`: What is covered and what is explicitly out of scope
- `applicability`: Who this applies to and under what circumstances
- `relatedDocuments`: References to related artifacts and dependencies

### Report Overview

**Reporting Period**:
- `reportingPeriod`: Time period covered (e.g., Q2 2024, Jan 2024, etc.)
- `reportDate`: Date report was generated
- `reportType`: Regular | Ad-hoc | Special Investigation | Executive Briefing
- `frequency`: How often this report is generated
- `distribution`: Intended recipients and distribution method

### Executive Summary

**Key Highlights**:
- `criticalFindings`: Top 3-5 most important findings for executive attention
- `trendAnalysis`: Key trends compared to previous periods
- `recommendations`: Priority recommendations requiring executive decision
- `impactAssessment`: Business impact of findings or metrics

### Detailed Analysis

**Metrics & KPIs**:
- `metricName`: Name of each metric or KPI
- `currentValue`: Value for this reporting period
- `targetValue`: Target or goal
- `previousValue`: Value from previous period for trending
- `variance`: Difference from target and trend direction
- `variances`: Explanation of significant variances
- `dataSource`: Where data comes from
- `collectionMethod`: How data is collected and validated

**Analysis by Category**:
- `category`: Grouping for related metrics or findings
- `observations`: What was observed or measured
- `analysis`: Interpretation and meaning
- `rootCauses`: Underlying causes for significant findings
- `impact`: Business or operational impact
- `trends`: Patterns over time
- `comparatives`: Benchmarking against industry or peer data

### Recommendations & Actions

**Priority Actions**:
- `actionId`: Unique identifier
- `actionDescription`: What needs to be done
- `rationale`: Why this action is needed
- `priority`: P0 | P1 | P2 | P3
- `owner`: Who is responsible
- `dueDate`: Target completion date
- `estimatedEffort`: Resource requirement
- `dependencies`: Prerequisites or dependencies
- `successMetrics`: How success will be measured

**Follow-up Items**:
- `openItems`: Items from previous reports still in progress
- `closedItems`: Items completed since last report
- `escalations`: Items requiring escalation to higher authority


## Best Practices

**Model-Appropriate Explainer**: Use TreeExplainer for tree-based models (XGBoost, LightGBM, Random Forest), KernelExplainer for model-agnostic explanations
**SHAP for Global Importance**: Generate SHAP summary plots showing feature importance distributions across entire dataset
**LIME for Individual Explanations**: Use LIME to explain specific high-stakes predictions (loan denials, fraud flags)
**Counterfactual Scenarios**: Provide actionable counterfactuals ("If income increased $5K, loan would be approved")
**Protected Class Analysis**: Always disaggregate model performance and explanations by protected classes (race, gender, age)
**Plain Language Explanations**: Translate technical feature names to business terms ("credit_utilization" → "percentage of available credit used")
**Visual Explanations**: Use SHAP force plots, waterfall charts, and feature importance bar charts for stakeholder communication
**Confidence Intervals**: Report prediction confidence alongside explanations to communicate uncertainty
**Model Card Publication**: Publish model cards for customer-facing AI systems (EU AI Act transparency requirement)
**Quarterly Bias Audits**: Re-run fairness metrics quarterly to detect model drift and discriminatory patterns
**Explanation Validation**: Test that explanations accurately reflect model behavior (explanation faithfulness testing)
**Regulatory Documentation**: Maintain explainability reports as evidence for EU AI Act and SR 11-7 compliance audits
**User-Facing Explanations**: Provide simplified explanations in customer portals for GDPR Article 22 compliance
**Disagreement Analysis**: When SHAP and LIME disagree, investigate why and document findings
**Feature Dependency**: Use partial dependence plots to show non-linear feature relationships
**Subgroup Performance**: Report model accuracy separately for protected classes to identify disparate performance
**Explanation Stability**: Test explanation consistency across similar inputs (stable models produce stable explanations)
**Automated Report Generation**: Integrate explainability reporting into CI/CD for continuous documentation
**Explanation APIs**: Expose SHAP/LIME explanations through APIs for customer-facing applications
**Third-Party Validation**: Have independent reviewers validate explanations for high-risk AI systems (credit, hiring, healthcare)

## Quality Criteria

Before considering this artifact complete and ready for approval, verify:

✓ **Completeness**: All required sections present and adequately detailed
✓ **Accuracy**: Information verified and validated by appropriate subject matter experts
✓ **Clarity**: Written in clear, unambiguous language appropriate for intended audience
✓ **Consistency**: Aligns with organizational standards, templates, and related artifacts
✓ **Currency**: Based on current information; outdated content removed or updated
✓ **Traceability**: Includes references to source materials and related documents
✓ **Stakeholder Review**: Reviewed by all key stakeholders with feedback incorporated
✓ **Technical Review**: Technical accuracy verified by qualified technical reviewers
✓ **Compliance**: Meets all applicable regulatory, policy, and contractual requirements
✓ **Approval**: All required approvals obtained and documented
✓ **Accessibility**: Stored in accessible location with appropriate permissions
✓ **Metadata**: Complete metadata enables search, categorization, and lifecycle management

## Common Pitfalls & How to Avoid

❌ **Incomplete Information**: Rushing to complete without gathering all necessary inputs
   ✓ *Solution*: Create comprehensive checklist of required information; allocate sufficient time

❌ **Lack of Stakeholder Input**: Creating in isolation without engaging affected parties
   ✓ *Solution*: Identify all stakeholders early; schedule working sessions for collaborative development

❌ **Outdated Content**: Using old information or not updating when conditions change
   ✓ *Solution*: Establish refresh schedule; define triggers requiring immediate update

❌ **Inconsistent Format**: Not following organizational templates and standards
   ✓ *Solution*: Always start from approved template; verify against style guide before submission

❌ **Missing Approvals**: Publishing without proper authorization
   ✓ *Solution*: Understand approval chain; route through all required approvers with evidence

❌ **Poor Version Control**: Making changes without maintaining history
   ✓ *Solution*: Use proper version control system; never directly edit published version

❌ **Inadequate Distribution**: Completing artifact but stakeholders unaware it exists
   ✓ *Solution*: Define distribution list; actively communicate availability and location

❌ **No Maintenance Plan**: Creating artifact as one-time activity with no ongoing ownership
   ✓ *Solution*: Assign owner; schedule regular reviews; define update triggers

## Related Standards & Frameworks

**Explainability Frameworks & Libraries**:
- SHAP (SHapley Additive exPlanations): Python library for unified feature importance (tree, kernel, deep, gradient explainers)
- LIME (Local Interpretable Model-Agnostic Explanations): Model-agnostic local explanation framework
- InterpretML (Microsoft): Glass-box models (EBM) and black-box explanations
- AI Explainability 360 (IBM): Comprehensive explainability algorithms and metrics
- Captum (Meta/PyTorch): Model interpretability for PyTorch deep learning models
- DALEX (DrWhy.AI): Model-agnostic explanations for R and Python
- Alibi (Seldon): Black-box and white-box explainability algorithms
- What-If Tool (Google): Visual interface for model understanding and fairness
- Explainable Boosting Machine (EBM): Inherently interpretable gradient boosting (Microsoft)

**Model Cards & Documentation Standards**:
- Model Cards for Model Reporting (Google): Structured documentation template for ML models
- FactSheets (IBM): AI transparency documentation framework
- Datasheets for Datasets: Dataset documentation template (analogous to model cards)
- ML Test Score (Google): Rubric for ML production readiness
- IEEE 7000-2021: Model process for addressing ethical concerns in system design

**Regulatory & Compliance Frameworks**:
- EU AI Act Article 13: Transparency obligations for high-risk AI systems (2025 enforcement)
- EU AI Act Article 52: Transparency obligations for certain AI systems (emotion recognition, biometric categorization)
- GDPR Article 22: Right not to be subject to automated decision-making (requires explanation capability)
- GDPR Article 15: Right of access (includes right to meaningful information about logic of automated processing)
- CCPA Section 1798.185: Automated decision-making disclosure requirements
- OECD AI Principles: Transparency and explainability requirements
- NIST AI Risk Management Framework: Explainability and interpretability guidance

**Financial Services Model Risk Management**:
- SR 11-7 (OCC): Supervisory Guidance on Model Risk Management (banking model validation)
- SR 15-18 / SR 15-19 (Federal Reserve): Model risk management for machine learning
- TRIM (Targeted Review of Internal Models): ECB model validation framework
- IFRS 9 / CECL: Credit risk model validation and documentation requirements

**Explainability Techniques**:
- Global Explanations: Feature importance across entire model (permutation importance, SHAP summary plots)
- Local Explanations: Individual prediction explanations (SHAP force plots, LIME)
- Counterfactual Explanations: Minimal changes to flip prediction (Dice, Alibi counterfactuals)
- Partial Dependence Plots (PDP): How predictions vary with feature values
- Individual Conditional Expectation (ICE): Per-instance partial dependence plots
- Accumulated Local Effects (ALE): Unbiased feature effect estimates
- Anchors: High-precision rule-based explanations (Alibi anchors)

**Bias & Fairness Assessment**:
- Disparate Impact Analysis: Protected class outcome disparities (80% rule)
- Equalized Odds: Error rate parity across groups
- Demographic Parity: Equal positive prediction rates across groups
- Calibration: Prediction confidence accuracy across subgroups
- Fairness Indicators (TensorFlow): Bias metrics visualization
- AI Fairness 360 (IBM): Bias detection and mitigation algorithms
- Aequitas (University of Chicago): Bias and fairness audit toolkit

**High-Risk AI System Categories (EU AI Act)**:
- Biometric identification and categorization
- Critical infrastructure management
- Education and vocational training (admissions, grading)
- Employment decisions (hiring, promotion, termination)
- Access to essential services (credit scoring, insurance underwriting)
- Law enforcement (predictive policing, crime risk assessment)
- Migration and asylum (visa decisions, border control)
- Justice system (recidivism prediction, case prioritization)

**Explanation Types**:
- Feature Attribution: Which features contributed most to prediction (SHAP, LIME)
- Example-Based: Similar training examples that influenced prediction (influence functions)
- Rule-Based: Decision rules that led to prediction (decision trees, rule extraction)
- Saliency Maps: Visual highlighting of important image regions (GradCAM, attention maps)
- Natural Language: Text-based explanations generated from model internals

**Model Interpretability Spectrum**:
- Inherently Interpretable: Linear regression, decision trees, rule-based systems, GAMs
- Post-Hoc Interpretable: Neural networks, ensemble models, SVMs with SHAP/LIME explanations
- Opaque Models: Complex deep learning, black-box ensembles requiring explanation frameworks

**Performance & Fairness Metrics**:
- Accuracy, Precision, Recall, F1 Score (overall and per subgroup)
- AUC-ROC, AUC-PR (ranking quality)
- Calibration Plots (prediction reliability)
- Confusion Matrices (per protected class)
- Mean Absolute Error (MAE), Root Mean Squared Error (RMSE) for regression

**Reference**: Consult AI ethics, model risk management, and legal/compliance teams for detailed guidance on explainability requirements and regulatory obligations

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- [List artifacts that provide input to this one]
- [Data sources that feed this artifact]
- [Prerequisites that must be satisfied]

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- [Artifacts that consume information from this one]
- [Processes that use this artifact]
- [Teams or roles that rely on this information]

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- [Complementary artifacts in same phase]
- [Artifacts in adjacent phases]
- [Cross-cutting artifacts (e.g., risk register)]

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: [If applicable] Architecture board review for standards compliance
5. **Security Review**: [If applicable] Security team review for security requirements
6. **Compliance Review**: [If applicable] Compliance review for regulatory requirements
7. **Legal Review**: [If applicable] Legal counsel review
8. **Final Approval**: Designated approver(s) provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: [Define role - e.g., Program Manager, Architecture Lead, CISO]
- Secondary Approver: [For high-risk or cross-functional artifacts]
- Governance Approval: [If requires board or committee approval]

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: [Define cadence - e.g., Quarterly, Annually]

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur
- Regulatory requirements change
- Major incidents reveal deficiencies
- Stakeholder requests identify needed updates
- Related artifacts are substantially updated

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring, scope changes, or approach changes
- **MINOR**: New sections, substantial additions, or enhancements
- **PATCH**: Corrections, clarifications, minor updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: [Define based on regulatory and business requirements]

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: [Define role responsible for maintenance]

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/{artifact_name}-template.{format_type.lower()}`

**Alternative Formats**: [If multiple formats supported]

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/{artifact_name}-example-*.{format_type.lower()}`

**Annotated Guidance**: See annotated examples showing best practices and common approaches

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified and engaged all required stakeholders
- [ ] Gathered prerequisite information and inputs
- [ ] Obtained access to necessary systems and data
- [ ] Allocated sufficient time for quality completion
- [ ] Identified reviewers and approvers
- [ ] Understood applicable standards and requirements

While creating this artifact:

- [ ] Following approved template structure
- [ ] Documenting sources and references
- [ ] Writing clearly for intended audience
- [ ] Including visual aids where helpful
- [ ] Self-reviewing against quality criteria
- [ ] Seeking input from stakeholders

Before submitting for approval:

- [ ] Completed all required sections
- [ ] Verified accuracy of all information
- [ ] Obtained peer review feedback
- [ ] Addressed all review comments
- [ ] Spell-checked and proofread
- [ ] Completed all metadata fields
- [ ] Verified compliance with standards
- [ ] Ready for formal approval process

## Governance & Compliance

### Regulatory Considerations

[Define any regulatory requirements applicable to this artifact type, such as:]

- SOC 2: [If artifact supports SOC 2 controls]
- ISO 27001: [If part of ISMS documentation]
- GDPR/Privacy: [If contains or references personal data]
- Industry-Specific: [Healthcare, Financial Services, etc.]

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team
- External audits by third-party auditors
- Regulatory examinations
- Customer security assessments

**Audit Preparation**:
- Maintain complete version history
- Document all approvals with evidence
- Keep change log current
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- [Relevant organizational policies]
- [Industry regulations and standards]
- [Contractual obligations]
- [Governance framework requirements]

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Access Frequency**: How often artifact is accessed/referenced
- **Update Frequency**: How often artifact requires updates
- **Downstream Impact**: How many artifacts/processes depend on this

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: {phase}

**Category**: {category}

**Typical Producers**: [Roles/teams that typically create this artifact]

**Typical Consumers**: [Roles/teams that typically use this artifact]

**Effort Estimate**: [Typical hours/days required to complete]

**Complexity Level**: [Low | Medium | High | Very High]

**Business Criticality**: [Low | Medium | High | Mission Critical]

**Change Frequency**: [Static | Infrequent | Regular | Frequent]

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: {phase} - Version 2.0*
