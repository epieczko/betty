# Name: model-governance-policy

## Executive Summary

The Model Governance Policy establishes mandatory requirements, standards, and procedures for the entire ML model lifecycle from development through retirement. This policy defines roles and responsibilities, approval gates, risk classification criteria, monitoring requirements, and compliance obligations to ensure responsible AI deployment and effective model risk management.

This policy implements governance frameworks aligned with NIST AI RMF, EU AI Act requirements, SR 11-7 (for banking), and ISO/IEC 42001 AI Management System standards. It defines model approval gates (development, UAT, production), champion/challenger testing requirements, A/B testing protocols, model monitoring thresholds, and incident response procedures for model failures or bias incidents.

The policy governs ML Engineers, Data Scientists, and AI teams in model development, AI Governance Teams in oversight and approval, Model Risk Managers in risk assessment, and executives in accountability for high-risk AI systems. It establishes Model Risk Committee authority, approval workflows, documentation requirements (Model Cards, risk assessments), and consequences for policy violations.

### Strategic Importance

- **Risk Management**: Mitigates model risk, algorithmic bias, and regulatory non-compliance through systematic governance
- **Regulatory Compliance**: Ensures adherence to EU AI Act, GDPR, sector-specific regulations (SR 11-7, FDA, HIPAA)
- **Accountability**: Defines clear roles (model owner, validator, approver) and escalation paths
- **Quality Assurance**: Mandates development standards, testing requirements, and approval gates
- **Incident Prevention**: Establishes controls to prevent model failures, bias incidents, and discriminatory outcomes

## Purpose & Scope

### Primary Purpose

This policy establishes mandatory governance requirements for all ML models and AI systems, defining approval gates, risk classification, monitoring obligations, documentation standards, and accountability structures. It ensures consistent, risk-based oversight of the AI portfolio while enabling innovation within guardrails.

### Scope

**In Scope**:
- Model risk classification: EU AI Act risk tiers (high-risk, limited risk, minimal risk), internal risk tiers
- Model approval gates: Development approval, UAT approval, production deployment approval
- Model Risk Committee: Authority, membership, meeting cadence, decision-making process
- Champion/Challenger framework: A/B testing requirements, statistical significance criteria, traffic allocation
- Model documentation requirements: Model Cards, risk assessments, bias assessments, technical specifications
- Model monitoring requirements: Performance monitoring, drift detection, fairness monitoring, SLA thresholds
- Retraining policies: Triggers for retraining (performance degradation, data drift, fairness drift)
- Model retirement: Deprecation procedures, sunset timelines, decommissioning verification
- Incident response: Model failure escalation, bias incident procedures, regulatory reporting
- Roles and responsibilities: Model owner, data science lead, model validator, business sponsor, approver
- Third-party models: Vendor model assessment, due diligence, ongoing monitoring requirements
- Shadow AI prevention: Discovery procedures, registration requirements, penalties for non-compliance
- Bias testing requirements: Fairness metrics, protected classes, testing frequency, threshold violations
- Explainability requirements: When SHAP/LIME analysis is required, documentation standards
- Data governance: Training data quality, data lineage, PII protection, data retention
- Model versioning: Semantic versioning, rollback procedures, version control requirements
- Audit rights: Internal audit access, regulatory examinations, documentation retention

**Out of Scope**:
- Detailed technical implementation (handled by technical standards and guidelines)
- Specific model architectures or algorithms (technical decisions delegated to data science teams)
- Data engineering practices (handled by separate data governance policy)
- IT infrastructure and MLOps tooling (handled by IT policies)
- Individual model risk assessments (conducted per this policy, not included in policy document)

### Target Audience

**Primary Audience**:
- ML Engineers & Data Scientists: Understand mandatory requirements for model development and deployment
- AI Governance Teams: Enforce policy, conduct reviews, escalate violations
- Model Risk Managers: Assess compliance, conduct risk reviews, report to Model Risk Committee
- Executive Leadership: Accountable for policy compliance, approve policy exceptions

**Secondary Audience**:
- Product Managers: Understand constraints and requirements for AI feature development
- Legal & Compliance: Verify regulatory compliance, advise on policy interpretation
- Internal Audit: Audit policy compliance, assess control effectiveness
- Board of Directors: Oversee model risk governance at enterprise level

## Document Information

**Format**: Markdown

**File Pattern**: `*.model-governance-policy.md`

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

### Specification Overview

**Specification Purpose**:
- `specificationGoal`: What this specification is defining
- `userStories`: User needs being addressed
- `requirements`: High-level requirements this spec satisfies
- `designPrinciples`: Guiding principles for this specification
- `constraints`: Technical, business, or regulatory constraints

### Technical Specification

**System Components**:
- `componentName`: Name of each system component
- `componentType`: Service | Library | Integration | Data Store | UI Component
- `purpose`: Why this component exists
- `responsibilities`: What this component is responsible for
- `interfaces`: How other components interact with it
- `dependencies`: What this component depends on
- `dataModel`: Data structures used or managed
- `apiEndpoints`: API endpoints exposed (if applicable)

**Functional Requirements**:
- `requirementId`: Unique identifier (e.g., FR-001)
- `requirement`: Detailed requirement statement
- `acceptance Criteria`: How requirement is verified
- `priority`: Must Have | Should Have | Could Have | Won't Have
- `complexity`: Estimation of implementation complexity
- `risks`: Risks associated with this requirement

**Non-Functional Requirements**:
- `performance`: Response time, throughput, capacity targets
- `scalability`: How system scales with load or data volume
- `availability`: Uptime requirements and SLAs
- `reliability`: Error rates, MTBF, MTTR targets
- `security`: Authentication, authorization, encryption requirements
- `compliance`: Regulatory or policy requirements
- `usability`: User experience and accessibility requirements
- `maintainability`: Code quality, documentation, testing standards
- `portability`: Platform independence or migration requirements

### Design Details

**Architecture**:
- `architecturePattern`: Microservices | Monolith | Serverless | Event-Driven
- `componentDiagram`: Visual representation of components and relationships
- `dataFlow`: How data moves through the system
- `integrationPoints`: External system integrations
- `deploymentModel`: How components are deployed and distributed

**Data Model**:
- `entities`: Core data entities
- `relationships`: How entities relate to each other
- `constraints`: Data validation and business rules
- `indexes`: Performance optimization through indexing
- `archival`: Data retention and archival strategy

**Security Design**:
- `authenticationMechanism`: How users/services authenticate
- `authorizationModel`: RBAC | ABAC | ACL approach
- `dataProtection`: Encryption at rest and in transit
- `auditLogging`: What is logged for security audit
- `threatModel`: Key threats and mitigations

### Implementation Guidance

**Development Standards**:
- `codingStandards`: Language-specific coding standards to follow
- `testingRequirements`: Unit test coverage, integration tests required
- `documentationRequirements`: Code comments, API docs, README
- `versionControl`: Branching strategy and commit conventions
- `codeReview`: Review process and criteria

**Quality Gates**:
- `buildRequirements`: Must compile without errors/warnings
- `testRequirements`: All tests must pass, minimum coverage %
- `securityRequirements`: No high/critical vulnerabilities
- `performanceRequirements`: Must meet performance SLAs
- `accessibilityRequirements`: WCAG 2.1 AA compliance (if applicable)


## Best Practices

**Risk-Based Governance**: Apply governance rigor proportional to model risk; streamline approval for low-risk models
**Clear Approval Gates**: Define explicit go/no-go criteria for each approval gate; avoid subjective criteria
**Model Risk Committee**: Establish committee with cross-functional representation (data science, risk, legal, business)
**Automated Compliance Checks**: Integrate policy checks into CI/CD pipelines; prevent non-compliant deployments
**Champion/Challenger Standard**: Require statistical significance testing (p < 0.05) before replacing production models
**Mandatory Monitoring**: Enforce automated monitoring for all production models; no exceptions
**Fairness Thresholds**: Define quantitative fairness thresholds (e.g., disparate impact ratio > 0.80); trigger alerts
**Shadow AI Discovery**: Conduct quarterly scans for undocumented models; require immediate registration
**Third-Party Due Diligence**: Require same governance standards for vendor models as internal models
**Incident Playbooks**: Document step-by-step procedures for model failures, bias incidents, regulatory inquiries
**Exception Process**: Require executive approval for policy exceptions; log all exceptions with rationale
**Policy Training**: Mandate annual policy training for all ML practitioners; track completion
**Version Control**: Store policy in Git; use semantic versioning; maintain change log
**Stakeholder Input**: Solicit feedback from data science teams before policy changes; balance control with enablement
**Regulatory Alignment**: Review policy annually against evolving regulations (EU AI Act updates, new local laws)
**Audit Readiness**: Design policy to facilitate internal audit and regulatory examinations
**Plain Language**: Write policy in clear, actionable language; avoid ambiguous terms like "appropriate" or "reasonable"
**Flowcharts & Decision Trees**: Provide visual guides for risk classification, approval workflows, escalation paths
**Policy Metrics**: Track metrics (% models compliant, approval cycle time, policy exceptions granted)
**Continuous Improvement**: Review policy annually; incorporate lessons learned from incidents and audits

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
- NIST AI Risk Management Framework (AI RMF 1.0): Govern, Map, Measure, Manage functions
- EU AI Act: High-risk AI requirements, conformity assessment, quality management system
- ISO/IEC 42001:2023: AI Management System requirements
- ISO/IEC 23894:2023: AI Risk Management guidelines
- OECD AI Principles: Human-centered values, transparency, robustness, accountability
- Singapore Model AI Governance Framework: Internal governance structures and measures
- Partnership on AI: Tenets for responsible AI development and deployment

**Model Risk Management Standards**:
- SR 11-7 (Federal Reserve): Supervisory guidance on model risk management for banking
- OCC 2011-12: Sound practices for model risk management
- Basel Committee: Principles for effective risk data aggregation and reporting (BCBS 239)
- CCAR/DFAST: Model risk management for stress testing (banking)
- Solvency II: Model governance for insurance industry
- SOX Section 404: Internal controls for financial reporting models

**Industry-Specific Regulations**:
- FDA AI/ML Software as Medical Device (SaMD): Predetermined change control plans
- HIPAA: PHI protection in healthcare ML models
- GDPR Article 22: Automated decision-making and profiling rights
- Fair Lending laws (ECOA, FHA): Non-discrimination in credit decisioning
- EEOC Uniform Guidelines: Adverse impact analysis for employment decisioning
- NYC Local Law 144: Bias audit requirements for automated employment tools

**MLOps & Model Lifecycle Management**:
- MLOps Maturity Model: Levels 0-4 (manual to full automation)
- CI/CD for Machine Learning: Testing, versioning, deployment automation
- Model Cards (Mitchell et al.): Transparent model reporting
- Datasheets for Datasets (Gebru et al.): Training data documentation
- MLflow Model Registry: Model versioning and lifecycle management

**Champion/Challenger & A/B Testing**:
- Frequentist hypothesis testing: Statistical significance criteria (p-value < 0.05)
- Bayesian A/B testing: Posterior probability of superiority
- Multi-armed bandit algorithms: Thompson sampling, UCB
- Sequential testing: Early stopping rules to minimize sample size
- Traffic allocation: Gradual rollout strategies (canary, blue-green deployment)

**Model Monitoring & Observability**:
- Performance monitoring: Accuracy, precision, recall, F1, AUC-ROC tracking
- Data drift detection: PSI (Population Stability Index), KL divergence, Kolmogorov-Smirnov test
- Concept drift: Model performance degradation over time
- Fairness drift: Temporal changes in demographic parity, equalized odds
- Prediction drift: Distribution changes in model outputs
- Evidently AI, Fiddler AI, Arthur AI: ML monitoring platforms

**Bias & Fairness Standards**:
- NIST AI RMF: Trustworthy AI characteristics including fairness
- IEEE 7000-2021: Addressing ethical concerns during system design
- Fairlearn, AIF360: Fairness assessment and mitigation toolkits
- EU AI Act Article 10: Data governance for fairness and bias mitigation

**Documentation & Audit Standards**:
- Model Cards for Model Reporting: Transparent documentation of model characteristics
- FactSheets (IBM): Comprehensive AI documentation
- Model Risk Assessment templates: SR 11-7 compliant documentation
- Audit trail requirements: SOX, GDPR, industry-specific regulations

**Roles & Responsibilities Frameworks**:
- RACI matrix: Responsible, Accountable, Consulted, Informed
- Three Lines of Defense: Business (1st line), Risk (2nd line), Internal Audit (3rd line)
- Model Risk Committee: Governance structure, authority, escalation procedures

**Reference**: Consult Legal, Compliance, and AI Governance Office for jurisdiction and industry-specific requirements

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
