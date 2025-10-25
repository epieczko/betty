# Name: model-risk-assessments

## Executive Summary

The Model Risk Assessments are comprehensive evaluations of ML model risks including model performance risk, implementation risk, data quality risk, algorithmic bias risk, and operational risk. These assessments align with SR 11-7 (banking), OCC 2011-12, and NIST AI RMF to classify model risk tiers, identify vulnerabilities, and define risk mitigation controls.

This assessment documents quantitative risk analysis including back-testing results, stress testing scenarios, sensitivity analysis, and out-of-sample validation. It evaluates model limitations, assumptions, data quality, bias testing results, explainability, and operational controls (monitoring, incident response, change management) to provide holistic risk evaluation.

The assessment supports Model Risk Managers in risk classification and mitigation planning, Model Risk Committee in approval decisions, AI Governance Teams in risk-based oversight prioritization, and regulators in demonstrating sound model risk management. It informs model approval gates, monitoring thresholds, validation frequency, and capital allocation for model risk.

### Strategic Importance

- **Regulatory Compliance**: Demonstrates adherence to SR 11-7, OCC 2011-12, EU AI Act, and industry-specific regulations
- **Risk Quantification**: Provides quantitative risk metrics (VaR, expected loss, risk scores) for portfolio management
- **Approval Evidence**: Supports Model Risk Committee approval with comprehensive risk analysis
- **Mitigation Planning**: Identifies specific risks and defines mitigation controls and monitoring requirements
- **Capital Allocation**: Informs risk-based capital requirements and model risk reserves (banking)
- **Audit Defense**: Provides documentation for internal audit, regulatory exams, and third-party assessments
- **Risk-Based Oversight**: Enables prioritization of governance resources based on model risk tier

## Purpose & Scope

### Primary Purpose

This artifact provides comprehensive risk assessment of ML models to classify risk tier, identify vulnerabilities, quantify potential impact, and define risk mitigation controls. It supports risk-based model governance decisions including approval, validation frequency, and monitoring requirements.

### Scope

**In Scope**:
- Risk classification: High, Medium, Low risk tier determination per SR 11-7 framework
- Model performance risk: Accuracy degradation, overfitting, underfitting, generalization failure
- Implementation risk: Coding errors, integration issues, incorrect model use
- Data quality risk: Data errors, missing values, data drift, training-serving skew
- Algorithmic bias risk: Discriminatory outcomes, fairness violations, disparate impact
- Model complexity risk: Interpretability challenges, validation difficulty, opacity
- Operational risk: Monitoring failures, incident response gaps, change management issues
- Back-testing: Historical performance validation, out-of-time testing
- Stress testing: Extreme scenario analysis, adversarial testing, edge case evaluation
- Sensitivity analysis: Feature importance, hyperparameter sensitivity, input perturbation
- Assumption testing: Validation of modeling assumptions, stationarity tests
- Limitations documentation: Known model limitations, out-of-scope use cases, failure modes
- Third-party model risk: Vendor model due diligence, black-box risk, vendor dependency
- Concentration risk: Over-reliance on single model, correlated model failures
- Control effectiveness: Evaluation of monitoring, validation, governance controls
- Residual risk: Risk remaining after mitigation controls

**Out of Scope**:
- Detailed bias testing (handled by dedicated bias assessments)
- Ongoing monitoring results (handled by monitoring reports)
- Technical implementation details (handled by technical documentation)
- Business case and ROI (handled by business justification documents)

### Target Audience

**Primary Audience**:
- Model Risk Managers: Conduct risk assessments, classify risk tiers, recommend mitigation
- Model Risk Committee: Review assessments, approve high-risk models, set validation frequency
- Model Validators: Independent validation based on risk assessment findings
- Regulatory Examiners: Review model risk management practices (bank exams)

**Secondary Audience**:
- ML Engineers & Data Scientists: Understand risk findings, implement mitigation controls
- AI Governance Teams: Prioritize oversight based on risk classification
- Internal Audit: Evaluate model risk management control effectiveness
- Executive Leadership: Understand model risk exposure and mitigation status

## Document Information

**Format**: Markdown

**File Pattern**: `*.model-risk-assessments.md`

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

### Assessment Methodology

**Approach**:
- `assessmentFramework`: Framework or standard used (e.g., NIST, ISO, proprietary)
- `assessmentScope`: Systems, processes, or areas assessed
- `evaluationCriteria`: Specific criteria used for evaluation
- `maturityModel`: Maturity levels if applicable (Initial, Managed, Defined, etc.)
- `scoringMethodology`: How scores or ratings are assigned

**Assessment Execution**:
- `assessmentPeriod`: Time period covered by the assessment
- `dataCollectionMethods`: Interviews, documentation review, testing, observation
- `participantsInterviewed`: Roles and number of people interviewed
- `evidenceReviewed`: Types and volume of evidence examined
- `limitations`: Any limitations or constraints on the assessment

### Findings & Results

**Summary Results**:
- `overallRating`: Aggregate assessment result
- `maturityLevel`: Current maturity level if using maturity model
- `complianceScore`: Percentage compliance if applicable
- `trendAnalysis`: Comparison to previous assessments

**Detailed Findings**:
- `findingId`: Unique identifier for each finding
- `findingCategory`: Category or control area
- `findingTitle`: Concise title
- `description`: Detailed description of finding
- `severity`: Critical | High | Medium | Low
- `evidence`: Supporting evidence for finding
- `impact`: Business or technical impact
- `likelihood`: Probability of occurrence if risk-related
- `currentState`: Current state or practice observed
- `desiredState`: Target state or required practice
- `gap`: Specific gap between current and desired
- `recommendations`: Specific remediation recommendations
- `priority`: Prioritization for remediation
- `estimatedEffort`: Effort required to remediate

### Remediation Plan

**Recommendations Summary**:
- `totalRecommendations`: Count by severity
- `quickWins`: High-value, low-effort improvements
- `strategicInitiatives`: Long-term, high-effort improvements
- `costBenefitAnalysis`: Estimated cost vs. benefit for major recommendations

**Remediation Roadmap**:
- `phase1Immediate`: 0-3 months, critical items
- `phase2NearTerm`: 3-6 months, high priority items
- `phase3MidTerm`: 6-12 months, medium priority items
- `phase4LongTerm`: 12+ months, strategic initiatives

**Implementation Tracking**:
- `recommendationOwner`: Who is responsible for each item
- `targetCompletionDate`: When remediation should be complete
- `statusTracking`: Mechanism for tracking progress
- `successCriteria`: How completion will be verified


## Best Practices

**Risk-Based Approach**: Apply SR 11-7 risk classification factors (materiality, complexity, business context) consistently
**Quantitative Analysis**: Include quantitative risk metrics (VaR, expected loss, risk scores) not just qualitative assessments
**Back-Testing Required**: Always conduct back-testing on holdout data or out-of-time validation set
**Stress Testing**: Test model under adverse scenarios relevant to business context (market crash, recession, outliers)
**Sensitivity Analysis**: Identify most influential features and hyperparameters; test robustness to perturbations
**Assumption Documentation**: Explicitly document all modeling assumptions and test their validity
**Limitations First**: Start assessment by documenting known model limitations and failure modes
**Independent Validation**: Ensure model validator is independent from model development team
**Control Evaluation**: Assess effectiveness of monitoring, validation, and governance controls
**Residual Risk Quantification**: Calculate residual risk after mitigation controls applied
**Third-Party Rigor**: Apply same risk assessment rigor to vendor models as internal models
**Bias Risk Mandatory**: Include algorithmic bias risk assessment for all models impacting individuals
**Comparative Analysis**: Compare model risk to baseline models, prior versions, and industry benchmarks
**Scenario Planning**: Develop specific failure scenarios and document potential impacts
**Mitigation Specificity**: Define specific, measurable risk mitigation controls not generic statements
**Control Ownership**: Assign clear ownership for each mitigation control with accountability
**Risk Register Integration**: Log all identified risks in centralized risk register with tracking
**Approval Workflow**: Route high-risk models through Model Risk Committee for formal approval
**Validation Frequency**: Set validation frequency based on risk tier (annual/biennial/triennial)
**Living Document**: Update risk assessment when model changes, retraining occurs, or incidents happen

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

**Model Risk Management Regulations**:
- SR 11-7 (Federal Reserve): Supervisory Guidance on Model Risk Management for banking
- OCC 2011-12: Sound Practices for Model Risk Management (OCC bulletin)
- CCAR/DFAST: Comprehensive Capital Analysis and Review stress testing requirements
- Basel Committee BCBS 239: Risk data aggregation and risk reporting principles
- Solvency II: Insurance model risk management (EIOPA guidelines)
- MAS TRM Guidelines: Singapore Monetary Authority technology risk management

**Risk Classification Frameworks**:
- Three-tier model: High, Medium, Low risk
- SR 11-7 factors: Materiality, complexity, business context
- EU AI Act: Unacceptable, High-risk, Limited risk, Minimal risk
- Quantitative risk tiers: Risk score > 70 (high), 40-70 (medium), < 40 (low)

**Risk Types & Categories**:
- Model development risk: Data quality, methodology, assumptions
- Model implementation risk: Coding errors, integration, incorrect use
- Model usage risk: Misapplication, overreliance, misinterpretation
- Operational risk: Monitoring, controls, change management, incident response
- Compliance risk: Regulatory violations, bias/discrimination, privacy

**Quantitative Risk Methods**:
- Back-testing: Compare model predictions to actual outcomes over historical period
- Stress testing: Evaluate model under extreme scenarios, market shocks
- Sensitivity analysis: Measure impact of input changes on model outputs
- Scenario analysis: Assess model behavior under specific business scenarios
- Monte Carlo simulation: Stochastic risk quantification
- Value at Risk (VaR): Quantify potential loss at confidence level
- Expected Shortfall: Conditional VaR, tail risk measurement

**Model Validation Standards**:
- Conceptual soundness: Theory, methodology, assumptions, limitations
- Ongoing monitoring: Performance tracking, drift detection, threshold violations
- Outcomes analysis: Back-testing, benchmark comparison, profitability analysis
- Independent validation: Three Lines of Defense model
- Validation frequency: Annual (high-risk), biennial (medium), triennial (low)

**Bias & Fairness Risk**:
- Disparate impact analysis: 80% rule (EEOC), four-fifths rule
- Fairness metrics: Demographic parity, equalized odds, calibration
- ProPublica COMPAS analysis: Case study for algorithmic bias risk
- EU AI Act Article 9: Risk management system for high-risk AI
- Protected classes: Race, gender, age, disability, religion, national origin

**Operational Risk Standards**:
- ISO 31000: Risk management principles and guidelines
- COSO ERM: Enterprise risk management integrated framework
- NIST AI RMF: AI risk management framework (Map, Measure, Manage, Govern)
- FAIR: Factor Analysis of Information Risk quantitative framework
- Bow-tie analysis: Causal and consequence analysis visualization

**Third-Party Model Risk**:
- Vendor due diligence: Model documentation, validation, performance evidence
- Black-box risk: Lack of transparency, vendor dependency, limited control
- Escrow agreements: Access to model code and documentation
- Ongoing monitoring: Vendor model performance tracking, incident reporting

**Documentation Standards**:
- Model Cards: Include limitations and ethical considerations sections
- Model Risk Assessment templates: SR 11-7 compliant format
- Validation reports: Independent validator assessment of model risk
- Risk register: Centralized tracking of model risks and mitigation status

**Regulatory Examination Focus**:
- Model inventory completeness: All material models identified and classified
- Governance framework: Policies, Model Risk Committee, roles/responsibilities
- Validation independence: Separation between model development and validation
- Ongoing monitoring: Automated monitoring, threshold violations, incident response
- Documentation quality: Risk assessments, validation reports, approval evidence
- Issue tracking: Findings log, remediation plans, aging analysis

**Reference**: Consult Model Risk Management Office and Regulatory Compliance for jurisdiction-specific requirements

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
