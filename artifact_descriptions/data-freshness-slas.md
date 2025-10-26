# Name: data-freshness-slas

## Executive Summary

Data Freshness SLAs define the maximum acceptable latency between data generation and availability for consumption, establishing formal service level agreements for data pipelines, ETL/ELT processes, and data product delivery. These SLAs are critical governance artifacts for data engineering teams, data product managers, and business stakeholders who depend on timely data for decision-making, operational dashboards, and ML model inference.

Modern data platforms (Snowflake, BigQuery, Databricks, Redshift) support real-time (<1 min), near real-time (<15 min), and batch (<24 hour) data freshness SLAs through streaming ingestion (Kafka, Kinesis, Pub/Sub), incremental dbt models, change data capture (CDC via Debezium, Fivetran, Airbyte), and orchestrated DAG execution (Airflow, Prefect, Dagster). Data freshness monitoring tools (Monte Carlo, Datafold, dbt Cloud, Great Expectations) track SLA compliance and alert stakeholders when data pipelines violate agreed-upon latency targets.

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

Data Freshness SLAs establish formal commitments for data latency, ensuring data consumers receive timely, actionable data to support business operations, analytics, and machine learning use cases. They answer critical questions: "How fresh does our revenue dashboard data need to be?", "What latency is acceptable for fraud detection models?", and "How quickly must customer data sync from production to the data warehouse?" These SLAs enable data engineers to prioritize pipeline optimization, justify infrastructure investments (e.g., streaming vs. batch), and set realistic expectations with business stakeholders.

### Scope

**In Scope**:
- Real-time data freshness SLAs (<1 minute latency for operational dashboards, fraud detection, real-time personalization)
- Near real-time SLAs (<15 minutes for business intelligence, customer 360 views, inventory tracking)
- Hourly batch SLAs (<1 hour for marketing attribution, campaign performance)
- Daily batch SLAs (<24 hours for financial reporting, data science model training)
- Source-to-warehouse latency (CDC lag, API sync delays, file ingestion time)
- Transformation pipeline latency (dbt model refresh, Spark job duration, data quality checks)
- Data availability windows (when data becomes queryable after ingestion)
- SLA measurement methodology (p50, p95, p99 latencies vs. max latency)
- SLA monitoring and alerting (data freshness checks, SLA violation notifications)
- Escalation paths for SLA breaches (incident response, stakeholder communication)
- Streaming data freshness (Kafka consumer lag, Kinesis iterator age, Pub/Sub subscription lag)
- Incremental vs. full refresh policies (dbt incremental models, merge strategies)
- Data backfill procedures (historical data reprocessing, SLA exceptions)

**Out of Scope**:
- Data quality SLAs (accuracy, completeness, validity - see Data Quality SLAs)
- Query performance SLAs (dashboard load time, report generation speed - see Query Performance SLAs)
- Data retention and archival policies (how long data is kept - see Data Retention Schedule)
- Data pipeline cost optimization (separate from freshness requirements)
- Data governance and access controls (security, compliance - see Data Governance policies)

### Target Audience

**Primary Audience**:
- Data Engineers: Build pipelines to meet freshness SLAs, optimize ingestion/transformation speed
- Analytics Engineers: Design dbt models with appropriate refresh frequencies
- Data Product Managers: Define freshness requirements for data products, prioritize SLA investments
- Data Platform Engineers: Provision infrastructure (streaming, CDC) to enable required freshness

**Secondary Audience**:
- Business Stakeholders: Understand data timeliness limitations, set realistic expectations
- BI Developers: Build dashboards with awareness of data freshness constraints
- Data Scientists: Factor data lag into model design (e.g., feature freshness for ML)
- Executive Leadership: Review SLA compliance metrics, approve freshness investments

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-freshness-slas.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal

**Retention**: 3 years (operational records retention)


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Scheduled date for next formal review (quarterly)
- `documentOwner`: Data Engineering Lead or Data Platform Manager
- `classification`: Internal
- `retentionPeriod`: 3 years

**Authorship & Review**:
- `primaryAuthor`: Lead Data Engineer or Data Platform Architect
- `contributors`: Analytics Engineers, Data Product Managers, Business Analysts
- `reviewers`: Data Engineering Manager, Business Stakeholders, BI Teams
- `approvers`: VP of Data/Analytics, Business Unit Leaders
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

**Tiered SLA Approach**: Define 3-4 freshness tiers (Real-time <1 min, Near real-time <15 min, Hourly <1 hour, Daily <24 hours); avoid one-size-fits-all
**Business-Driven SLAs**: Tie freshness requirements to business value; 5-minute freshness is unnecessary for monthly reports
**Percentile-Based SLAs**: Use p95 or p99 latencies instead of max latency; occasional spikes shouldn't breach SLAs
**Streaming for Critical Paths**: Use Kafka/Kinesis for <5 minute SLAs; batch ETL can't reliably achieve sub-10 minute freshness
**Incremental dbt Models**: Use incremental models for large tables; full refreshes can't meet tight SLAs at scale
**CDC for Transactional Data**: Implement change data capture (Debezium, Fivetran CDC) for near real-time warehouse updates
**Freshness Monitoring**: Instrument freshness checks (dbt source freshness, Monte Carlo freshness monitors, custom SQL checks)
**Alerting Thresholds**: Alert when freshness exceeds 80% of SLA; don't wait for violations to react
**SLA Measurement Windows**: Measure freshness during business hours (9am-5pm) separately from off-hours; batch jobs can run overnight
**Graceful Degradation**: Define degraded modes (e.g., switch to cached data if live pipeline fails)
**Backfill Exceptions**: Allow SLA exceptions for historical backfills; reprocessing old data isn't real-time
**Downstream Dependencies**: Account for chained pipelines; source freshness + transformation time + BI cache refresh = total latency
**Cost vs. Freshness Tradeoffs**: Streaming infrastructure is expensive; justify <1 hour SLAs with ROI analysis
**Data Quality Gates**: Don't sacrifice quality for speed; late clean data beats fast dirty data
**Timezone Clarity**: Specify timezones in SLAs (UTC, EST, PT); avoid ambiguity
**SLA Review Cadence**: Review quarterly; business needs evolve, SLAs should adapt
**Incident Postmortems**: When SLAs breach, conduct postmortems; understand root causes (code bugs, infrastructure failures, data source delays)
**Stakeholder Communication**: Proactively notify stakeholders of SLA breaches; don't let them discover stale data
**Documentation**: Document data lineage and refresh schedules in data catalogs (Collibra, Alation, DataHub)
**Performance Budgets**: Allocate "latency budgets" to pipeline stages (ingestion 5 min, transformation 10 min, total 15 min)

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

**Data Warehouses & Streaming**:
- Snowflake: Snowpipe (continuous ingestion), Streams & Tasks (CDC), Dynamic Tables (incremental materialization)
- Google BigQuery: BigQuery Streaming API, BigQuery Data Transfer Service, scheduled queries
- Databricks: Delta Live Tables (streaming + batch), Auto Loader (incremental ingestion), Structured Streaming
- Amazon Redshift: COPY command, Redshift Streaming Ingestion (Kinesis integration), materialized views
- Azure Synapse Analytics: PolyBase, COPY command, Synapse Link for real-time sync

**Streaming Platforms**:
- Apache Kafka: Consumer lag monitoring, Kafka Connect for CDC, stream processing (Kafka Streams, ksqlDB)
- Amazon Kinesis: Data Streams, Data Firehose, iterator age metrics, Lambda stream processing
- Google Pub/Sub: Subscription lag monitoring, push subscriptions, dataflow streaming pipelines
- Azure Event Hubs: Consumer lag tracking, Event Hubs Capture, Stream Analytics
- Apache Pulsar: Multi-tenancy, geo-replication, subscription lag monitoring

**Change Data Capture (CDC)**:
- Debezium: Kafka-based CDC for MySQL, PostgreSQL, MongoDB, SQL Server, Oracle
- Fivetran: Managed CDC connectors, HVR replication engine, sub-minute latency
- Airbyte: Open-source CDC, incremental append and dedup sync modes
- AWS DMS: Database Migration Service, ongoing replication, CDC from RDS
- Qlik Replicate: Enterprise CDC, heterogeneous replication
- Striim: Real-time data integration, in-memory stream processing

**Data Transformation & Orchestration**:
- dbt (data build tool): Incremental models, source freshness checks, dbt Cloud alerting
- Apache Airflow: DAG scheduling, SLA monitoring, task retries, data-aware scheduling
- Prefect: Dataflow orchestration, conditional logic, retry policies
- Dagster: Data-aware orchestration, asset materialization, freshness policies
- Dataform: BigQuery-native transformation, incremental tables, scheduling
- Matillion: ELT for Snowflake/Redshift, CDC-based incremental loads

**Data Quality & Observability**:
- Monte Carlo: Data freshness monitoring, anomaly detection, incident management, SLA tracking
- Datafold: Data diff, freshness checks, CI/CD for data, column-level lineage
- Great Expectations: Expectation suites, data quality validation, freshness checks
- Soda: Data quality checks, anomaly detection, SQL-based assertions
- dbt Cloud: Source freshness checks, model timing dashboards
- Datadog Data Streams Monitoring: Kafka/Kinesis lag tracking, pipeline observability

**Metadata & Lineage**:
- Collibra: Enterprise data catalog, data lineage, business glossary
- Alation: Data catalog, query-based lineage, collaboration
- DataHub (LinkedIn): Open-source metadata platform, lineage tracking, data discovery
- Amundsen (Lyft): Metadata search, table/column descriptions, lineage
- Apache Atlas: Metadata management, classification, lineage for Hadoop ecosystem

**BI & Analytics Platforms**:
- Looker: PDTs (Persistent Derived Tables), datagroup triggers, cache policies
- Tableau: Extract refresh schedules, live vs. extract connections, cache warmup
- Power BI: Scheduled refresh, incremental refresh, DirectQuery vs. Import mode
- Mode: Query scheduling, report refresh intervals
- Metabase: Question caching, scheduled email reports

**Monitoring & Alerting**:
- Prometheus: Metrics collection, alerting rules, Grafana dashboards
- Datadog: Infrastructure monitoring, log aggregation, custom metrics
- PagerDuty: Incident management, on-call schedules, escalation policies
- Opsgenie: Alert routing, on-call management, incident response
- Slack: Alert notifications, chatops for data pipeline monitoring

**SLA Management Frameworks**:
- ITIL Service Level Management: SLA design, OLA (Operational Level Agreements), UC (Underpinning Contracts)
- SRE (Site Reliability Engineering): SLIs (Service Level Indicators), SLOs (Service Level Objectives), error budgets
- DAMA-DMBOK: Data quality dimensions, data lifecycle management
- Data Mesh principles: Data products, domain ownership, self-serve data platform

**Reference**: Consult organizational data platform team and data governance council for detailed guidance on data freshness standards. For data quality frameworks, see DAMA-DMBOK and Big Five methodology standards for data operations.

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Business requirements (which use cases require real-time vs. batch data)
- Source system capabilities (CDC support, API rate limits, file generation schedules)
- Data pipeline architecture (streaming vs. batch, orchestration tools)
- Infrastructure capacity (Kafka cluster size, warehouse compute resources)
- Budget constraints (streaming infrastructure costs vs. freshness benefits)

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Data pipeline development (dbt models, Airflow DAGs, streaming jobs)
- Data quality monitoring (freshness checks, SLA alerting)
- BI dashboard development (cache policies, refresh schedules)
- ML model serving (feature store refresh, real-time inference requirements)
- Incident response procedures (SLA breach escalation, stakeholder communication)
- Data platform capacity planning (compute sizing, storage optimization)

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Data Quality SLAs (accuracy, completeness alongside freshness)
- Data Contracts (schema, freshness, and quality guarantees)
- Data Pipeline Architecture (streaming vs. batch design patterns)
- Incident Response Playbooks (SLA breach escalation procedures)
- Data Catalog Metadata (documenting refresh schedules per table/dataset)

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: Data platform architecture team review for feasibility
5. **Security Review**: [If applicable] Security team review for security requirements
6. **Compliance Review**: [If applicable] Compliance review for regulatory requirements
7. **Legal Review**: [If applicable] Legal counsel review
8. **Final Approval**: Designated approver(s) provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: VP of Data & Analytics or Data Platform Lead
- Secondary Approver: Business unit leaders (for critical data products)
- Governance Approval: Data Governance Council (for enterprise-wide SLAs)

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review of SLA compliance metrics; annual comprehensive SLA update

**Event-Triggered Updates**: Update immediately when:
- New data sources onboarded (establish baseline freshness)
- Business requirements change (real-time dashboards, new use cases)
- SLA breaches become frequent (unrealistic SLAs need revision)
- Infrastructure upgrades (streaming platform, warehouse scaling)
- Data pipeline architecture changes (batch to streaming migration)

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant SLA changes (daily to hourly, batch to real-time), breaking changes
- **MINOR**: New SLAs added, SLA relaxations (hourly to daily), clarifications
- **PATCH**: Typo corrections, measurement methodology clarifications

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (which pipelines/teams affected)
- Approver of changes

### Archival & Retention

**Retention Period**: 3 years (operational records retention)

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Data Engineering Lead or Data Platform Manager

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Monitor SLA compliance
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/data-freshness-slas-template.md`

**Alternative Formats**: Confluence page, Google Doc, Notion database

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**:
- `examples/data-freshness-slas-ecommerce.md` (real-time inventory, near real-time analytics)
- `examples/data-freshness-slas-financial-services.md` (transaction monitoring, batch reporting)
- `examples/data-freshness-slas-b2b-saas.md` (customer 360, usage analytics)

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

- SOC 2: Data availability and processing controls
- ISO 27001: Information availability management
- GDPR/Privacy: Right to erasure (deletion freshness), data accuracy requirements
- Industry-Specific: Financial services real-time fraud detection, healthcare timely care coordination

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
- Track SLA compliance metrics
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- Data governance policies (data quality, data contracts)
- SLA management policies (monitoring, escalation, reporting)
- Incident management policies (breach response, communication)
- Capacity planning policies (infrastructure sizing, budget allocation)

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Access Frequency**: How often artifact is accessed/referenced
- **Update Frequency**: How often artifact requires updates
- **Downstream Impact**: How many pipelines/data products depend on this

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: Data Operations

**Category**: Data Quality & SLA Management

**Typical Producers**: Data Engineers, Analytics Engineers, Data Platform Team

**Typical Consumers**: Business Stakeholders, BI Developers, Data Scientists, Engineering Managers

**Effort Estimate**: 2-3 days for initial SLA definition; 4-8 hours for quarterly reviews

**Complexity Level**: Medium to High

**Business Criticality**: High (enables timely decision-making and operational efficiency)

**Change Frequency**: Quarterly review; event-triggered updates

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Data Operations - Version 2.0*
