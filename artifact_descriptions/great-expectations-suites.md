# Name: great-expectations-suites

## Executive Summary

The Great Expectations Suites artifact defines data quality validation rules, expectation suites, validation checkpoints, and automated testing procedures using Great Expectations, dbt tests, Soda Core, Monte Carlo Data, and data contracts frameworks. This artifact establishes comprehensive data quality assertions that prevent data pipeline failures, catch data anomalies, and ensure downstream consumers receive clean, reliable data.

Data quality issues are among the most common causes of ML model failures, incorrect business decisions, and customer-facing bugs. This artifact specifies expectation suites that validate data schemas, value ranges, null rates, uniqueness constraints, distribution properties, and referential integrity. It leverages Great Expectations' extensive expectations catalog (expect_column_values_to_be_between, expect_column_to_exist, expect_table_row_count_to_be_between), integrates with data pipelines through validation checkpoints, and provides data profiling capabilities that automatically generate expectations from historical data patterns.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact defines comprehensive data quality validation suites that programmatically test data at rest and in motion, ensuring data meets quality standards before being consumed by downstream applications, ML models, and business intelligence tools. It prevents data quality issues from propagating through data pipelines and provides early detection of schema changes, data drift, and anomalies.

### Scope

**In Scope**:
- Great Expectations expectation suites and validation definitions
- Data profiling and automatic expectation generation
- Validation checkpoints integrated into data pipelines
- Schema validation (column presence, data types, column order)
- Value constraints (range, regex, enum, null rate limits)
- Statistical expectations (mean, std dev, quantiles, distribution tests)
- Referential integrity checks (foreign key validation)
- Uniqueness and duplicate detection expectations
- Custom expectations for domain-specific validation
- dbt tests (schema tests, data tests, custom generic tests)
- Soda Core checks and anomaly detection
- Data contracts between producers and consumers
- Validation failure alerting and incident response

**Out of Scope**:
- Data transformation logic (covered by ETL/ELT documentation)
- Feature engineering validation (covered by feature-store-contracts)
- ML model evaluation metrics (covered by evaluation-protocols)
- Data pipeline orchestration configuration

### Target Audience

**Primary Audience**:
- Data Engineers building and maintaining data quality tests
- Analytics Engineers implementing dbt tests and data contracts
- Data Platform Engineers integrating validation into pipelines
- ML Engineers ensuring training data quality

**Secondary Audience**:
- Data Scientists consuming validated datasets
- Data Analysts relying on clean data for reporting
- Data Quality teams monitoring data health metrics
- Product Managers understanding data quality SLAs

## Document Information

**Format**: Markdown

**File Pattern**: `*.great-expectations-suites.md`

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

**Start with Schema Validation**: Always validate schema (columns exist, types correct) before value-level validation
**Profile First**: Use data profiling to automatically generate baseline expectations from historical data
**Critical vs. Warning**: Distinguish critical expectations (fail pipeline) from warnings (alert but continue)
**Version Expectation Suites**: Version control expectation suites alongside data pipeline code
**Test in Development**: Run validation on development/staging data before deploying to production
**Incremental Testing**: Add expectations incrementally; don't try to define all expectations upfront
**Validate at Boundaries**: Add checkpoints at data ingestion, transformation stages, and before consumption
**Document Business Logic**: Include business context in expectation descriptions for maintainability
**Monitor Test Coverage**: Track which columns and tables have validation coverage
**Fail Fast**: Place critical schema validations early in pipeline to prevent wasted computation
**Alert on Anomalies**: Use statistical expectations to detect anomalous patterns, not just hard failures
**Maintain Test Suites**: Regularly review and update expectations as data evolves
**Automate Data Docs**: Leverage auto-generated data documentation for transparency
**Test Freshness**: Include freshness checks for time-sensitive data
**Validate Uniqueness**: Always test uniqueness constraints on ID columns
**Range Validation**: Set reasonable bounds on numeric columns to catch data corruption
**Null Rate Thresholds**: Allow some nulls but alert when null rates exceed historical baselines
**Cross-Column Checks**: Validate relationships between columns (e.g., start_date < end_date)
**Reference Data Validation**: Validate against reference tables and lookup tables
**Custom Expectations**: Build custom expectations for complex business logic not covered by built-in expectations
**Integration Testing**: Test expectations against representative sample data before deployment
**Checkpoint Placement**: Add validation checkpoints after major transformations and before serving data

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

**Data Quality Frameworks**:
- Great Expectations (Python-based data validation framework)
- dbt tests (schema tests, data tests, custom tests)
- Soda Core (open-source data quality testing)
- Monte Carlo Data (data observability platform)
- Datafold (data diff and quality monitoring)
- Elementary Data (dbt-native data observability)
- Anomalo (ML-powered data quality monitoring)
- AWS Deequ (Spark-based data quality library)

**Great Expectations Core Concepts**:
- Expectation Suites (collections of expectations for datasets)
- Expectations (assertions about data properties)
- Validation Results (outcomes of running expectations)
- Checkpoints (validation runs at pipeline stages)
- Data Contexts (project configuration and metadata)
- Data Docs (auto-generated validation documentation)
- Profilers (automatic expectation generation from data)

**Common Great Expectations**:
- expect_table_row_count_to_be_between (validate row counts)
- expect_column_to_exist (schema validation)
- expect_column_values_to_be_in_set (enum validation)
- expect_column_values_to_be_between (range validation)
- expect_column_values_to_not_be_null (null rate validation)
- expect_column_values_to_be_unique (uniqueness validation)
- expect_column_values_to_match_regex (pattern validation)
- expect_column_mean_to_be_between (statistical validation)
- expect_column_values_to_be_of_type (type validation)
- expect_table_columns_to_match_ordered_list (schema order validation)

**dbt Test Types**:
- Schema tests (unique, not_null, accepted_values, relationships)
- Data tests (custom SQL assertions)
- Generic tests (reusable parameterized tests)
- Singular tests (one-off SQL assertions)
- dbt-expectations package (Great Expectations for dbt)
- dbt test severity levels (warn, error)

**Soda Core Checks**:
- Schema checks (column presence, types)
- Metric checks (row count, null count, distinct count)
- Anomaly detection (automatic threshold learning)
- Reference checks (comparing datasets)
- Custom SQL checks
- Distribution checks
- Freshness checks (data recency)

**Data Contracts**:
- Schema contracts (column names, types, constraints)
- SLA contracts (freshness, completeness, accuracy)
- Semantic contracts (business logic validation)
- Version contracts (schema evolution guarantees)
- Consumer expectations (downstream requirements)

**Schema Validation**:
- Column existence and naming conventions
- Data type validation and compatibility
- Column order requirements
- Required vs. optional columns
- Schema evolution (backward/forward compatibility)
- Nested schema validation (JSON, struct columns)

**Value Validation**:
- Range constraints (min/max bounds)
- Enum validation (allowed values)
- Regex pattern matching
- Custom value validation logic
- Cross-column validation (relationship checks)
- Conditional validation (if-then rules)

**Statistical Validation**:
- Distribution checks (mean, median, std dev, skewness)
- Quantile validation (p50, p95, p99)
- Outlier detection (IQR, z-score methods)
- Correlation validation (between columns)
- Time-series validation (trend, seasonality)
- Drift detection (comparing to baseline)

**Data Freshness**:
- Maximum data age validation
- Update frequency checks
- Partition recency validation
- Streaming data lag monitoring
- SLA compliance for freshness

**Referential Integrity**:
- Foreign key validation
- Parent-child relationship checks
- Join integrity validation
- Orphaned record detection
- Many-to-many relationship validation

**Data Profiling**:
- Automatic statistic generation
- Value distribution analysis
- Column correlation discovery
- Missing value analysis
- Pattern extraction (regex generation)
- Automated expectation suite generation

**Integration Patterns**:
- Airflow operators for validation checkpoints
- dbt post-hooks for test execution
- Spark DataFrame validation
- Pandas DataFrame validation
- SQL-based validation
- Streaming data validation (Kafka, Kinesis)

**Validation Actions**:
- Fail pipeline on critical validation failures
- Send alerts (Slack, PagerDuty, email)
- Log validation results to data catalog
- Update data quality dashboards
- Quarantine invalid data
- Trigger data quality incidents

**Monitoring & Observability**:
- Data quality dashboards (validation pass rate)
- Test execution monitoring
- Expectation failure trending
- Data drift detection over time
- Anomaly detection and alerting
- Data lineage with quality annotations

**Tools & Libraries**:
- great_expectations Python package
- dbt Core and dbt Cloud
- Soda Core CLI
- AWS Deequ (Scala/Spark)
- Cerberus (Python validation)
- Pandera (Pandas DataFrame validation)
- pydantic (Python data validation)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

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
