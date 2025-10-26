# Name: data-quality-rules

## Executive Summary

Data Quality Rules are executable specifications that define acceptable data characteristics, constraints, thresholds, and validation logic across the six DAMA data quality dimensions: accuracy, completeness, consistency, validity, timeliness, and uniqueness. These rules enable automated, continuous data quality testing within pipelines using frameworks like Great Expectations, dbt tests, Soda Core, and data observability platforms, shifting from reactive quality firefighting to proactive quality engineering.

Modern data quality rules implement declarative expectations (Great Expectations suites), SQL-based assertions (dbt tests, Soda checks), statistical anomaly detection (Monte Carlo, Bigeye), and schema validation (JSON Schema, Avro, Protobuf) integrated directly into data pipelines and orchestration frameworks. Implementation aligns with ISO 8000 data quality standards, DAMA DMBoK data quality management, and emerging DataOps practices that treat data quality as code with version control, testing, and CI/CD integration.

### Strategic Importance

- **Trust in Data**: Establishes measurable quality standards that build confidence in analytics, ML models, and operational decisions
- **Early Detection**: Catches data quality issues at ingestion or transformation rather than at consumption, reducing downstream impact
- **Automated Monitoring**: Eliminates manual spot-checking through continuous, automated validation in production pipelines
- **Quality SLOs**: Defines service-level objectives for data quality enabling data product reliability guarantees
- **Regulatory Compliance**: Supports data quality requirements in SOX, BCBS 239, GDPR accuracy obligations, and industry regulations
- **Cost Avoidance**: Prevents costly business decisions, compliance failures, and customer impacts from poor quality data
- **Cultural Shift**: Embeds quality ownership with domain teams through federated, automated quality engineering

## Purpose & Scope

### Primary Purpose

This artifact documents executable data quality rules, validation logic, acceptance thresholds, and testing specifications that are implemented in data pipelines and monitored continuously to ensure data meets defined quality standards across accuracy, completeness, consistency, validity, timeliness, and uniqueness dimensions.

### Scope

**In Scope**:
- DAMA data quality dimension rules (accuracy, completeness, consistency, validity, timeliness, uniqueness)
- Great Expectations test suites with expectation definitions and validation thresholds
- dbt test specifications (schema tests, data tests, custom singular tests)
- Soda Core checks with SQL-based quality assertions and anomaly detection
- Schema validation rules (JSON Schema, Avro schema, Protobuf definitions)
- Completeness rules (null checks, required field validation, record count thresholds)
- Validity rules (data type validation, format verification, range checks, enumeration constraints)
- Accuracy rules (business rule validation, cross-system reconciliation, referential integrity)
- Consistency rules (cross-column validation, temporal consistency, cross-table consistency)
- Uniqueness rules (primary key constraints, duplicate detection, deduplication logic)
- Timeliness rules (freshness SLOs, latency thresholds, staleness detection)
- Statistical anomaly detection (distribution checks, volume anomalies, trend deviations)
- Quality scoring and composite quality metrics
- Alert definitions and escalation procedures for quality failures
- Remediation workflows and data quality incident response procedures

**Out of Scope**:
- Data profiling results and quality measurement outcomes (covered by quality reports)
- Root cause analysis of specific quality incidents (documented in incident reports)
- Data cleansing and transformation logic (implemented in ETL/ELT pipelines)
- Master data management rules (covered by MDM governance)
- Data governance policies and organizational standards (enterprise governance framework)

### Target Audience

**Primary Audience**:
- Data Engineers: Implement quality rules in pipelines using Great Expectations, dbt, or Soda Core
- Analytics Engineers: Define and maintain quality tests for dbt models and semantic layers
- Data Quality Engineers: Design comprehensive quality rule suites and monitoring strategies
- DataOps Engineers: Integrate quality testing into CI/CD pipelines and orchestration workflows

**Secondary Audience**:
- Data Stewards: Define business rules and acceptable quality thresholds for domain data
- Data Scientists: Validate input data quality for ML models and feature pipelines
- Business Analysts: Understand quality guarantees and limitations of analytical datasets
- Compliance Officers: Verify data quality controls for regulatory requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-quality-rules.md`

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

**Quality as Code**: Store all quality rules in version control (Git) alongside data transformation code using Great Expectations, dbt, or Soda YAML
**DAMA Dimension Coverage**: Ensure quality rules cover all six DAMA dimensions (accuracy, completeness, consistency, validity, timeliness, uniqueness)
**Test Pyramid Approach**: Layer tests from simple schema checks to complex business rule validations, balancing coverage and execution cost
**Critical Path Focus**: Prioritize quality rules for business-critical fields, regulatory data elements, and downstream dependencies
**Threshold Calibration**: Set realistic pass/fail thresholds based on data profiling and business tolerance for quality issues
**Tiered Severity**: Classify quality failures as critical (block pipeline), warning (alert but continue), or informational (log only)
**Great Expectations Suites**: Organize expectations into logical suites (source validation, transformation validation, output validation)
**dbt Test Strategy**: Combine generic tests (unique, not_null, relationships) with custom singular tests for business logic
**Soda Checks Organization**: Structure checks by data domain, quality dimension, and criticality with clear naming conventions
**Automated Profiling**: Use automated profiling (Great Expectations profiler, dbt-utils, Soda scan) to suggest initial quality rules
**Sample Data Testing**: Validate rules on representative sample data before deploying to production pipelines
**CI/CD Integration**: Run quality tests in pull requests and deployment pipelines to catch issues before production
**Monitoring Dashboards**: Visualize quality test results over time to identify trends and chronic quality issues
**Alert Routing**: Configure smart alerting with appropriate escalation to avoid alert fatigue while ensuring rapid response
**Quality SLOs**: Define measurable quality SLOs (e.g., 99.9% completeness, 99.5% accuracy) aligned with data product contracts
**Remediation Runbooks**: Document standard remediation procedures for common quality failure patterns
**Business Context**: Include business rationale and impact description for each quality rule to guide prioritization
**Incremental Adoption**: Start with high-value quality rules and expand coverage iteratively based on incidents and priorities

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

**Data Quality Standards**:
- ISO 8000: International standard for data quality including accuracy, completeness, consistency, and timeliness
- DAMA DMBoK Chapter 13: Data Quality Management with six quality dimensions framework
- ISO 25012: Software product quality model for data quality characteristics
- ISO/IEC 25024: Measurement of data quality with metrics and evaluation methods
- TDQM (Total Data Quality Management): MIT framework for data quality assessment

**DAMA Data Quality Dimensions**:
- Accuracy: Degree to which data correctly represents real-world entities
- Completeness: Extent to which required data is present (null handling, mandatory fields)
- Consistency: Agreement of data across systems and over time (referential integrity, cross-system reconciliation)
- Validity: Data conforms to defined formats, types, and business rules (format, range, enumeration validation)
- Timeliness: Data is available when needed and represents current state (freshness, latency, staleness)
- Uniqueness: No unintended duplication of entities (primary key constraints, deduplication)

**Data Quality Testing Frameworks**:
- Great Expectations: Python-based framework for declarative data validation with 300+ built-in expectations
- dbt (data build tool): SQL-based testing with schema tests, data tests, and custom test macros
- Soda Core: Open-source data quality framework with SQL-based checks and anomaly detection
- Apache Griffin: Big data quality solution for Hadoop/Spark with profiling and validation
- Deequ: Data quality library for Spark from Amazon with constraint-based validation
- Cerberus: Lightweight Python data validation library
- Pandera: Statistical data validation for pandas DataFrames and schema enforcement

**Data Observability Platforms**:
- Monte Carlo: ML-powered data observability with automated anomaly detection and incident management
- Bigeye: Data quality monitoring with automated metric generation and lineage-aware alerts
- Datafold: Data quality diffing and CI/CD validation for analytics code changes
- Metaplane: Automated data observability with anomaly detection and impact analysis
- Anomalo: Self-service data quality monitoring with automated checks and root cause analysis
- Lightup: Data quality platform with automated monitoring and collaborative incident resolution

**Schema Validation Tools**:
- JSON Schema: Specification for validating JSON document structure and data types
- Apache Avro: Data serialization with schema evolution and compatibility checking
- Protocol Buffers (Protobuf): Google's schema definition language with strict typing
- Cerberus: Python validation library for dictionaries and JSON
- Pydantic: Data validation using Python type annotations
- Marshmallow: Object serialization and deserialization with validation

**Regulatory Quality Requirements**:
- GDPR Article 5(1)(d): Accuracy principle requiring data to be accurate and kept up to date
- BCBS 239: Banking risk data quality requirements (accuracy, completeness, timeliness)
- SOX Section 404: Internal controls over financial data quality
- HIPAA: Healthcare data integrity and accuracy requirements
- FDA 21 CFR Part 11: Pharmaceutical data quality and validation requirements

**Quality Management Methodologies**:
- Six Sigma: DMAIC (Define, Measure, Analyze, Improve, Control) applied to data quality
- Total Quality Management (TQM): Continuous quality improvement principles
- Statistical Process Control (SPC): Control charts and statistical monitoring for data quality
- Root Cause Analysis (RCA): Fishbone diagrams, 5 Whys for quality incident investigation

**DataOps & Testing Best Practices**:
- Test-Driven Development (TDD): Write quality tests before implementing transformations
- Shift-Left Testing: Early quality validation in development before production deployment
- Continuous Testing: Automated quality checks in CI/CD pipelines
- Test Pyramid: Balance unit tests, integration tests, and end-to-end quality validation

**Data Profiling & Discovery**:
- Pandas Profiling: Automated EDA and quality profiling for pandas DataFrames
- Great Expectations Data Profiler: Automated expectation suite generation from data profiling
- Talend Data Preparation: Data profiling and quality assessment capabilities
- Informatica Data Quality: Enterprise profiling, standardization, and matching
- AWS Glue DataBrew: Visual data profiling and preparation service

**Reference**: Consult data quality engineering teams, Great Expectations documentation, dbt testing guides, and DAMA DMBoK Chapter 13 for comprehensive data quality implementation patterns

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
