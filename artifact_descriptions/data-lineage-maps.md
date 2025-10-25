# Name: data-lineage-maps

## Executive Summary

Data Lineage Maps are visual and technical documentation artifacts that trace the complete end-to-end flow of data from source systems through transformations, integrations, and consumption points. These artifacts provide critical transparency into how data moves, transforms, and derives through ETL/ELT pipelines, streaming architectures, and analytical workflows, enabling impact analysis, root cause diagnosis, and regulatory compliance.

Modern data lineage solutions leverage automated metadata extraction from Apache Atlas, DataHub, Amundsen, Collibra Lineage, Alation, and Informatica Enterprise Data Catalog to capture column-level lineage across diverse technology stacks. Implementation follows emerging standards like OpenLineage (LF AI & Data Foundation), PROV-DM (W3C Provenance Data Model), and integrates with orchestration platforms (Apache Airflow, Prefect, Dagster) to maintain real-time lineage accuracy aligned with DAMA DMBoK data lineage management practices.

### Strategic Importance

- **Impact Analysis**: Enables upstream/downstream impact assessment before making schema changes or retiring data sources
- **Root Cause Analysis**: Accelerates troubleshooting of data quality issues by tracing problems to source systems or transformation logic
- **Regulatory Compliance**: Supports GDPR Article 30, BCBS 239, SOX, and CCPA requirements for data flow documentation and auditability
- **Data Governance**: Provides visibility into data provenance, transformation logic, and business rule implementation for stewardship
- **Migration Planning**: Facilitates system modernization and cloud migration by documenting complete data dependencies
- **Trust & Transparency**: Builds confidence in analytics and reporting by showing complete data transformation history
- **Technical Debt Management**: Identifies redundant pipelines, unused transformations, and complex dependencies for optimization

## Purpose & Scope

### Primary Purpose

This artifact documents the complete data flow topology from source extraction through transformation pipelines to consumption endpoints, capturing table-level and column-level lineage, transformation logic, data dependencies, and processing sequences. It enables impact analysis, debugging, compliance documentation, and data trustworthiness assessment.

### Scope

**In Scope**:
- Source-to-target mappings across ETL/ELT pipelines (Informatica, Talend, Azure Data Factory, AWS Glue, dbt)
- Column-level lineage showing field-to-field transformations and derivations
- Data flow through streaming platforms (Apache Kafka, AWS Kinesis, Azure Event Hubs, Confluent)
- Transformation logic documentation including SQL queries, Python/Scala scripts, and business rules
- Dependencies between datasets, tables, views, and materialized views
- Orchestration flow captured from Apache Airflow, Prefect, Dagster, or Azure Data Factory DAGs
- BI report and dashboard dependencies (Tableau, Power BI, Looker, Qlik)
- Data lake/lakehouse lineage across bronze/silver/gold layers (Delta Lake, Apache Iceberg, Apache Hudi)
- Real-time and batch processing lineage
- OpenLineage event streams for automated lineage capture
- Impact analysis visualizations showing upstream/downstream dependencies

**Out of Scope**:
- Actual ETL/ELT code implementation (documented in pipeline repositories)
- Data quality measurement results (covered by data quality reports)
- Performance metrics and SLA monitoring (covered by observability tools)
- Access control and data security policies (documented in security artifacts)
- Physical infrastructure topology (covered by infrastructure architecture diagrams)

### Target Audience

**Primary Audience**:
- Data Engineers: Understand data flow dependencies when modifying pipelines or troubleshooting data issues
- Analytics Engineers: Trace dbt model dependencies and transformations for impact analysis
- Data Architects: Design and validate end-to-end data architecture and integration patterns
- Data Stewards: Validate data provenance and ensure compliance with data governance policies

**Secondary Audience**:
- Business Analysts: Understand how reports and KPIs are calculated from source data
- Compliance Officers: Audit data flows for GDPR, CCPA, SOX, and BCBS 239 compliance
- Data Scientists: Trace feature engineering pipelines and understand data preparation steps
- DevOps/DataOps Engineers: Manage CI/CD pipelines and monitor data pipeline health

## Document Information

**Format**: Multiple

**File Pattern**: `*.data-lineage-maps.*`

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

**Automate Lineage Capture**: Implement automated lineage harvesting using OpenLineage, DataHub extractors, or Apache Atlas hooks to avoid manual documentation drift
**Column-Level Granularity**: Capture field-level lineage wherever possible to enable precise impact analysis and debugging of data quality issues
**dbt DAG Integration**: Leverage dbt's built-in lineage graph generation and integrate with DataHub or Collibra for enterprise-wide visibility
**OpenLineage Events**: Emit OpenLineage events from Airflow, Spark, and custom pipelines to maintain real-time lineage accuracy
**Bi-directional Lineage**: Capture both upstream (where data comes from) and downstream (where data is used) lineage for comprehensive impact analysis
**Transformation Logic Documentation**: Include SQL snippets, transformation rules, and business logic in lineage nodes for debugging context
**Version Control Lineage Metadata**: Store lineage definitions (YAML, JSON) in Git alongside pipeline code for change tracking and audit
**Impact Analysis Automation**: Build automated impact analysis reports that show all affected downstream assets when upstream changes occur
**Lineage Validation**: Regularly reconcile lineage maps against actual data flows using query log analysis and metadata extraction
**Visual Complexity Management**: Use hierarchical views and filtering to manage complex lineage graphs with hundreds of nodes
**Cross-Platform Coverage**: Ensure lineage spans all technology layers (databases, ETL, streaming, BI) not just single platforms
**Real-time Streaming Lineage**: Capture Kafka topic lineage showing producer/consumer relationships and schema evolution
**BI Dependency Tracking**: Extract lineage from Tableau, Power BI, and Looker to show report dependencies on data models
**Data Lakehouse Layers**: Map lineage across medallion architecture (bronze/silver/gold) in Delta Lake, Iceberg, or Hudi environments
**Metadata as Code**: Treat lineage configuration as infrastructure-as-code using Terraform, Pulumi, or declarative YAML specifications
**Lineage Quality Metrics**: Track lineage coverage (% of pipelines documented), accuracy (validated vs. actual), and freshness (last update)
**GDPR Data Flow Mapping**: Maintain lineage for all personal data flows to support Article 30 ROPA and data subject access requests
**Deprecation Tracking**: Document deprecated data sources and migration paths in lineage to prevent continued dependencies

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

**Data Lineage Standards**:
- OpenLineage (LF AI & Data Foundation): Open standard for capturing and sharing data lineage metadata across platforms
- PROV-DM (W3C Provenance Data Model): Standard for representing and exchanging provenance information
- OSLC (Open Services for Lifecycle Collaboration): Integration specification for lineage across lifecycle tools
- ISO/IEC 11179-6: Metadata registry standard for data provenance and lineage documentation

**Data Governance & Management Frameworks**:
- DAMA DMBoK Chapter 14: Data Lineage and impact analysis best practices
- DCAM (Data Management Capability Assessment Model): Lineage capability assessment criteria
- EDM Council DCAM: Financial services critical data element (CDE) lineage requirements
- Data Mesh principles: Data product lineage and observability as key components

**Regulatory Compliance Requirements**:
- GDPR Article 30: Record of Processing Activities requiring data flow documentation
- BCBS 239 (Basel Committee): Risk data aggregation and reporting lineage requirements for banking
- SOX (Sarbanes-Oxley): Financial data lineage for audit trail and controls documentation
- CCPA: Consumer data flow mapping for privacy compliance
- FDA 21 CFR Part 11: Pharmaceutical data lineage and audit trail requirements
- HIPAA: Healthcare data flow documentation and access tracking

**Data Lineage & Catalog Tools**:
- Apache Atlas: Open-source metadata framework with native lineage capabilities for Hadoop/Spark ecosystems
- DataHub (LinkedIn): Automated lineage extraction from dbt, Airflow, Spark, and SQL queries
- Amundsen (Lyft): Data discovery platform with table and column-level lineage visualization
- Collibra Lineage: Enterprise lineage harvesting across ETL tools, databases, and BI platforms
- Alation Data Catalog: Automated lineage from query logs, ETL metadata, and BI tools
- Informatica Enterprise Data Catalog: Cross-platform lineage with AI-powered scanner technology
- Manta Data Lineage: Automated end-to-end lineage across on-premise and cloud platforms
- Azure Purview: Microsoft lineage capabilities for Azure data services
- AWS Glue Data Catalog: Lineage tracking for AWS data pipeline and analytics services
- Marquez (WeWork): OpenLineage reference implementation for metadata collection

**ETL/ELT & Orchestration Platforms**:
- dbt (data build tool): Lineage graph generation from SQL transformations and model dependencies
- Apache Airflow: DAG-based lineage with OpenLineage integration via Marquez
- Prefect: Modern workflow orchestration with built-in lineage tracking
- Dagster: Software-defined assets with automatic lineage graph generation
- Azure Data Factory: Visual pipeline lineage and impact analysis
- AWS Glue: Managed ETL with automatic lineage capture in Glue Data Catalog
- Informatica PowerCenter: Enterprise ETL with comprehensive metadata and lineage extraction
- Talend: Open-source and enterprise ETL with lineage documentation capabilities

**Streaming & Real-time Lineage**:
- Apache Kafka: Stream lineage tracking using Confluent Schema Registry and Streams
- Confluent Platform: Real-time data lineage for Kafka topics and stream processing
- Apache Flink: Stream processing lineage through Apache Atlas integration
- Apache Spark Structured Streaming: Lineage via Spark listener integration with DataHub/Atlas

**BI & Analytics Lineage**:
- Tableau: Lineage extraction via Tableau Metadata API and catalog integration
- Power BI: Lineage tracking through Power BI REST API and scanner API
- Looker: LookML-based lineage generation and catalog integration
- Qlik Sense: Metadata extraction for lineage visualization
- Looker: Git-based LookML lineage with dbt integration capabilities

**Reference**: Consult data engineering and architecture teams for platform-specific lineage implementation patterns and automated metadata harvesting configuration

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
