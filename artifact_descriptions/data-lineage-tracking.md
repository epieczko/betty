# Name: data-lineage-tracking

## Executive Summary

Data Lineage Tracking is the operational process and technical implementation for continuously capturing, updating, and maintaining data lineage metadata in real-time as data flows through pipelines, transformations, and consumption layers. Unlike static lineage maps, lineage tracking encompasses the automated instrumentation, event capture, metadata extraction, and continuous synchronization mechanisms that keep lineage information current and accurate.

Implementation leverages OpenLineage standard events, Apache Atlas hooks, DataHub metadata change events, Collibra automated scanners, and integration with orchestration platforms (Apache Airflow, Prefect, Dagster) to emit lineage events during pipeline execution. Modern approaches treat lineage as observable telemetry alongside logs, metrics, and traces, integrating with DataOps platforms and data observability tools (Monte Carlo, Bigeye, Datafold) to provide real-time visibility aligned with DAMA DMBoK operational metadata management practices.

### Strategic Importance

- **Real-time Accuracy**: Maintains up-to-date lineage through automated event capture, eliminating manual documentation lag
- **Operational Observability**: Enables real-time monitoring of data flow health, transformation success, and pipeline execution
- **Automated Compliance**: Supports continuous GDPR, BCBS 239, and SOX compliance through always-current data flow documentation
- **Incident Response**: Accelerates root cause analysis during data quality incidents by showing actual execution paths
- **Change Impact Detection**: Automatically identifies downstream impacts when upstream schemas or pipelines change
- **DataOps Integration**: Embeds lineage tracking in CI/CD pipelines for automated validation before production deployment
- **Metadata Quality**: Ensures lineage accuracy through programmatic capture versus error-prone manual documentation

## Purpose & Scope

### Primary Purpose

This artifact documents the technical implementation, configuration, and operational procedures for automated data lineage capture, including instrumentation code, event schemas, metadata extraction schedules, and integration patterns with data platforms and catalog systems.

### Scope

**In Scope**:
- OpenLineage event emission configuration for Apache Airflow, Spark, dbt, and custom pipelines
- Apache Atlas hook implementation for Hive, HBase, Kafka, and Hadoop ecosystem lineage
- DataHub metadata ingestion recipes and scheduled extraction from databases, ETL tools, and BI platforms
- Collibra scanner configuration for automated metadata harvesting and lineage extraction
- Alation query log analysis and automated lineage generation settings
- dbt metadata artifacts generation and lineage graph export to external catalogs
- Spark listener implementation for job-level and stage-level lineage tracking
- SQL parser integration for extracting column-level lineage from query logs
- Streaming lineage tracking for Kafka topic producer/consumer relationships
- BI connector configuration for Tableau, Power BI, and Looker lineage extraction
- Change data capture (CDC) integration for real-time lineage updates
- Lineage API specifications for custom application integration
- Metadata quality monitoring and lineage coverage metrics
- Lineage event schema validation and error handling procedures

**Out of Scope**:
- Visual lineage map creation and documentation (covered by data-lineage-maps artifact)
- Pipeline performance optimization (covered by performance tuning documentation)
- Data quality rule implementation (covered by data-quality-rules artifact)
- Access control and security policies (documented in security artifacts)
- Cost optimization for metadata storage (covered by infrastructure cost management)

### Target Audience

**Primary Audience**:
- Data Engineers: Implement OpenLineage instrumentation in pipelines and configure metadata extraction
- DataOps Engineers: Deploy and maintain lineage tracking infrastructure and monitoring
- Platform Engineers: Configure data catalog integrations and metadata ingestion schedules
- Analytics Engineers: Set up dbt lineage generation and integration with enterprise catalogs

**Secondary Audience**:
- Data Architects: Define lineage tracking standards and integration architecture
- Site Reliability Engineers: Monitor lineage tracking system health and performance
- DevOps Engineers: Integrate lineage tracking into CI/CD pipelines
- Compliance Officers: Validate lineage tracking coverage for regulatory requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-lineage-tracking.md`

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

**Infrastructure as Code**: Deploy lineage tracking configuration (DataHub recipes, Atlas hooks, OpenLineage configs) using Terraform, Helm charts, or GitOps patterns
**OpenLineage First**: Prioritize OpenLineage standard for new integrations to ensure portability across lineage tools and platforms
**Event-Driven Architecture**: Design lineage capture as event-driven using Kafka, AWS EventBridge, or Azure Event Grid for scalability
**Column-Level Instrumentation**: Implement SQL parsing (sqlglot, sqlparse, JSQLParser) for automatic column-level lineage extraction
**Idempotent Events**: Ensure lineage events are idempotent to handle retries and avoid duplicate metadata creation
**Schema Validation**: Validate OpenLineage events against official JSON schemas before emission to prevent malformed metadata
**Monitoring & Alerting**: Monitor lineage event emission rates, processing lag, and extraction failures with Prometheus, Datadog, or CloudWatch
**Incremental Extraction**: Configure metadata extractors for incremental updates rather than full scans to reduce load and latency
**Multi-Environment Tracking**: Maintain separate lineage tracking for dev, test, and production with environment-specific metadata tags
**Backward Compatibility**: Version lineage event schemas and maintain backward compatibility when evolving metadata structures
**Error Handling**: Implement graceful degradation where lineage capture failures don't break pipeline execution
**Sampling for Scale**: Use sampling strategies for high-volume query log analysis while maintaining representative lineage coverage
**Custom Extractors**: Build custom DataHub extractors or Apache Atlas hooks for proprietary systems using provided SDK frameworks
**API Rate Limiting**: Implement exponential backoff and rate limiting when calling catalog APIs to avoid throttling
**Metadata Retention**: Define retention policies for lineage events balancing storage costs with historical analysis needs
**Testing in CI/CD**: Validate lineage emission in pre-production using DataHub smoke tests or Atlas lineage verification scripts
**dbt Artifacts Export**: Automate dbt manifest.json and catalog.json export to data catalogs in every dbt Cloud/Core run
**Real-time Stream Lineage**: Use Kafka Streams applications with Schema Registry to track real-time topic lineage and transformations

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

**Lineage Tracking Standards**:
- OpenLineage (LF AI & Data): Open standard for lineage event schemas, facets, and metadata interchange
- OpenLineage Spec 1.0+: Run, job, dataset facets with extensible metadata model
- PROV-DM (W3C): Provenance data model for entity, activity, and agent relationships
- OpenMetadata: Open-source standard for metadata APIs and event-driven metadata management

**Lineage Tracking Tools & Platforms**:
- Marquez (WeWork): Reference OpenLineage implementation with PostgreSQL backend
- DataHub (LinkedIn): Metadata platform with OpenLineage ingestion and GraphQL API
- Apache Atlas: Hadoop-native metadata framework with hook-based lineage capture
- Amundsen (Lyft): Metadata discovery with lineage visualization and search
- Collibra Catalog: Enterprise data catalog with automated scanners and lineage harvesting
- Alation: Collaborative catalog with query log mining and automated lineage
- Informatica Enterprise Data Catalog: AI-powered metadata discovery and lineage extraction

**Orchestration Integration**:
- Apache Airflow OpenLineage provider: Native OpenLineage emission from Airflow DAGs
- Prefect: Modern orchestration with metadata tracking and observability
- Dagster: Software-defined assets with automatic lineage graph generation
- Azure Data Factory: Pipeline monitoring with lineage extraction via REST API
- AWS Step Functions: State machine lineage through CloudTrail and EventBridge

**ETL/ELT Lineage Tracking**:
- dbt Core/Cloud: manifest.json and run_results.json for lineage export
- Apache Spark: Spark Listener API for job, stage, and task-level lineage
- Informatica PowerCenter: Metadata exchange (MX) for lineage extraction
- Talend: Talend Management Console API for pipeline metadata
- Fivetran: Metadata API for connector lineage tracking
- Airbyte: Connector metadata for source-to-destination lineage

**Streaming Lineage**:
- Confluent Schema Registry: Schema evolution tracking for Kafka topics
- Apache Kafka: MirrorMaker 2 for cross-cluster lineage
- Apache Flink: Checkpointing metadata for stateful stream lineage
- Kafka Streams: Topology metadata for stream processing lineage

**SQL Parsing & Analysis**:
- sqlglot: Python SQL parser for multi-dialect column-level lineage extraction
- sqlparse: SQL parsing library for query analysis
- JSQLParser: Java SQL parser for lineage extraction from queries
- Calcite: SQL parser and optimizer for cross-database query analysis

**Data Observability Platforms**:
- Monte Carlo: Automated lineage extraction with ML-powered incident detection
- Bigeye: Data quality monitoring with automatic lineage discovery
- Datafold: Data diff and lineage for CI/CD validation
- Great Expectations: Data quality with lineage integration via OpenLineage

**Cloud Provider Lineage**:
- AWS Glue Data Catalog: Automatic lineage for Glue ETL jobs and crawlers
- Azure Purview: Automated scanning and lineage for Azure data services
- Google Cloud Data Catalog: Metadata service with BigQuery lineage tracking
- Databricks Unity Catalog: Lakehouse governance with automatic lineage capture

**Compliance & Governance**:
- GDPR Article 30: Automated ROPA generation from lineage metadata
- BCBS 239: Risk data lineage requirements for banking sector
- SOX Section 404: IT controls documentation via automated lineage
- DAMA DMBoK Chapter 14: Operational metadata and lineage management best practices

**Reference**: Consult data platform and engineering teams for tool-specific SDK documentation, API references, and integration patterns based on your technology stack

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
