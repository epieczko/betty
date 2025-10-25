# Name: ai-use-case-inventory

## Executive Summary

The AI Use Case Inventory is a comprehensive catalog of all machine learning models and AI systems across the organization, providing centralized visibility into the AI portfolio for governance, risk management, and regulatory compliance. This artifact tracks model metadata, risk classifications, deployment status, and ownership information to enable effective AI governance at scale.

This inventory aligns with EU AI Act risk classification requirements (unacceptable, high-risk, limited risk, minimal risk), NIST AI RMF use case documentation, and Model Registry best practices from MLflow, AWS SageMaker Model Registry, and Azure ML Model Registry. It documents model lineage, training data sources, performance metrics, fairness assessments, and approval status to support model lifecycle management.

The inventory enables AI Governance Teams to conduct portfolio-wide risk assessments, identify high-risk AI systems requiring enhanced oversight per EU AI Act Article 6, track model retirement schedules, manage model versioning, and ensure compliance with organizational AI policies. It integrates with MLOps platforms (MLflow, Kubeflow, Vertex AI) to automatically sync model metadata and deployment status.

### Strategic Importance

- **Portfolio Visibility**: Provides enterprise-wide view of all AI/ML models across business units and applications
- **Risk Classification**: Categorizes AI systems by risk tier (EU AI Act: high-risk, limited risk, minimal risk)
- **Regulatory Compliance**: Supports EU AI Act Article 16 record-keeping, NYC Local Law 144, and sector-specific regulations
- **Resource Optimization**: Identifies duplicate models, consolidation opportunities, and underutilized AI investments
- **Governance Enforcement**: Enables policy compliance monitoring, approval gate enforcement, and audit readiness
- **Model Lifecycle Management**: Tracks models from development through production to retirement
- **Incident Response**: Provides rapid model identification for security incidents, bias concerns, or performance degradation

## Purpose & Scope

### Primary Purpose

This artifact serves as the single source of truth for all AI/ML models and use cases across the organization, enabling centralized governance, risk management, and regulatory compliance tracking. It supports model discovery, duplicate identification, risk-based prioritization, and audit preparedness.

### Scope

**In Scope**:
- Model catalog: All ML models (supervised, unsupervised, reinforcement learning, LLMs, GenAI)
- Risk classification: EU AI Act risk tiers (unacceptable, high-risk, limited risk, minimal risk)
- Model metadata: Model type, algorithm, framework (TensorFlow, PyTorch, scikit-learn)
- Deployment status: Development, staging, production, retired, deprecated
- Model ownership: Model owner, data science team, business sponsor
- Training data lineage: Data sources, dataset versions, data quality scores
- Performance metrics: Accuracy, precision, recall, F1, AUC-ROC by model version
- Fairness assessment status: Bias testing completed, fairness metrics, mitigation applied
- Model versioning: Version history, champion/challenger status, A/B test results
- Regulatory classification: High-risk determination, compliance requirements, approval status
- Business use case: Problem statement, business value, KPIs, ROI
- Technical architecture: Serving infrastructure, API endpoints, batch vs. real-time
- Integration points: Upstream data sources, downstream consumers, system dependencies
- Approval workflow: Development approval, UAT approval, production approval dates
- Monitoring status: Performance monitoring, drift detection, fairness monitoring

**Out of Scope**:
- Model training code (stored in Git repositories)
- Detailed model documentation (handled by Model Cards)
- Training datasets themselves (stored in data lakes/warehouses)
- Model explainability reports (separate artifacts)
- Detailed risk assessments (separate Model Risk Assessment artifacts)
- Production monitoring dashboards (MLOps platform tools)

### Target Audience

**Primary Audience**:
- AI Governance Teams: Oversee AI portfolio, enforce policies, conduct risk assessments
- Model Risk Managers: Identify high-risk models, prioritize risk reviews, track remediation
- ML Engineers: Register models, update metadata, track deployment status
- Data Scientists: Document use cases, report performance metrics, manage model versions

**Secondary Audience**:
- Compliance Officers: Audit AI inventory for regulatory compliance (EU AI Act, sector regulations)
- Executive Leadership: Understand AI portfolio composition, risk exposure, investment priorities
- Product Managers: Identify AI capabilities, assess model readiness, plan feature releases
- Internal Audit: Verify model governance controls, review approval evidence, assess compliance

## Document Information

**Format**: Markdown

**File Pattern**: `*.ai-use-case-inventory.md`

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

### Main Content Sections

(Content structure will vary based on specific artifact type. Include all relevant sections needed to fully document the subject matter.)

**Core Information**:
- Document the primary information this artifact is meant to capture
- Organize in logical sections appropriate to the content type
- Use consistent formatting and structure
- Include sufficient detail for intended audience
- Provide examples where helpful

**Supporting Information**:
- Background context necessary for understanding
- Assumptions and constraints
- Dependencies on other artifacts or systems
- Related information and cross-references


## Best Practices

**Automated Registration**: Integrate model registration into CI/CD pipelines; auto-register models from MLflow, SageMaker, or Vertex AI
**Unique Model IDs**: Assign globally unique identifiers (UUIDs) to each model; maintain ID consistency across environments
**Complete Metadata**: Require mandatory fields (owner, risk tier, business use case, training data) before production promotion
**Risk Classification**: Apply EU AI Act risk classification framework; document classification rationale and evidence
**Regular Reconciliation**: Quarterly reconciliation between inventory and production deployments; identify shadow AI
**Automated Sync**: Use APIs to sync model metadata from MLflow, SageMaker, or Vertex AI; avoid manual data entry
**Version Control**: Track all model versions with semantic versioning; link to Git commits and training run IDs
**Ownership Assignment**: Assign clear model owner (accountable), data science lead (responsible), and business sponsor
**Lifecycle Status**: Maintain accurate deployment status (dev, staging, production, retired); automate status updates
**Retirement Tracking**: Define model retention policies; track deprecated models and ensure complete decommissioning
**High-Risk Flagging**: Prominently flag EU AI Act high-risk systems; trigger enhanced governance workflows
**Search & Discovery**: Implement full-text search, faceted filtering, and tagging for model discovery
**Dashboard Views**: Provide executive dashboards showing model counts by risk tier, status, and business unit
**Audit Trail**: Log all inventory changes with timestamp, user, and change reason; maintain immutable audit log
**Access Control**: Restrict edit permissions; implement approval workflows for metadata changes
**Integration Testing**: Validate inventory integrations with MLOps platforms quarterly; test API endpoints
**Data Quality**: Implement validation rules for required fields, enum values, and data formats
**Duplication Detection**: Use NLP similarity matching to identify duplicate or redundant models
**Portfolio Analytics**: Generate reports on model age, retraining frequency, risk distribution, and compliance gaps
**Stakeholder Communication**: Notify model owners of upcoming reviews, compliance requirements, and policy changes

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

**AI Governance Frameworks**:
- NIST AI Risk Management Framework (AI RMF): Use case documentation and risk management
- EU AI Act: Risk classification system (Annex III high-risk AI systems)
- ISO/IEC 42001: AI Management System inventory requirements
- ISO/IEC 23894: AI Risk Management
- Singapore Model AI Governance Framework: AI inventory and documentation
- OECD AI Principles: Transparency and accountability through documentation

**Model Registry Standards & Tools**:
- MLflow Model Registry: Open-source model versioning and lifecycle management
- AWS SageMaker Model Registry: Model packaging, versioning, and deployment
- Azure ML Model Registry: Centralized model storage and management
- Google Vertex AI Model Registry: Model versioning and monitoring
- Databricks MLflow: Unified model tracking and registry
- Kubeflow Model Registry: Kubernetes-native model management

**EU AI Act Risk Classifications**:
- Prohibited AI (Unacceptable Risk): Social scoring, real-time biometric identification
- High-Risk AI Systems (Annex III): Employment, credit scoring, law enforcement, critical infrastructure
- Limited Risk AI: Chatbots, deepfakes (transparency obligations)
- Minimal Risk AI: Spam filters, video games (no specific obligations)

**Model Lifecycle Management**:
- MLOps maturity model: Level 0 (manual) to Level 4 (full automation)
- Model versioning: Semantic versioning for ML models
- Champion/Challenger framework: A/B testing and gradual rollout
- Model retirement policies: Deprecation schedules and sunset procedures

**Industry-Specific Frameworks**:
- SR 11-7 (Banking): Model inventory and risk tiering requirements
- OCC 2011-12 (Banking): Sound practices for model risk management
- FDA AI/ML Software as Medical Device: Predetermined change control plan
- HIPAA (Healthcare): PHI protection in ML models
- GDPR Article 22: Automated decision-making documentation

**Metadata Standards**:
- Model Cards for Model Reporting (Mitchell et al., 2019)
- Datasheets for Datasets (Gebru et al., 2018)
- FactSheets (IBM): Comprehensive AI system documentation
- ML Model Schema (ml-metadata): Standardized model metadata format

**Risk Tiering Methodologies**:
- Three-tier model: High, Medium, Low risk
- Four-tier model: Critical, High, Moderate, Low risk
- EU AI Act four-tier: Unacceptable, High, Limited, Minimal risk
- NIST AI RMF: Context-specific risk assessment

**Compliance & Regulatory**:
- NYC Local Law 144: Automated employment decision tool registry
- Colorado AI Act (SB 24-205): High-risk AI system disclosure
- Illinois AI Video Interview Act: AI system inventory for employment
- California Delete Act: AI system data handling documentation
- White House AI Bill of Rights: Impact assessment documentation

**Reference**: Consult AI Governance Office and Legal Counsel for jurisdiction-specific classification and documentation requirements

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
