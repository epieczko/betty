# Name: dag-definitions

## Executive Summary

The DAG Definitions artifact is a critical deliverable for data engineering and workflow orchestration teams, documenting Directed Acyclic Graph (DAG) configurations for Apache Airflow, Prefect, Dagster, and similar workflow orchestration platforms. This artifact provides comprehensive specifications for task dependencies, scheduling patterns, retry logic, SLA monitoring, and execution parameters that enable reliable, scalable data pipeline automation.

As orchestration platforms become the backbone of modern data infrastructure, this artifact serves multiple constituencies—from Data Engineers implementing complex ETL/ELT workflows to Platform Engineers managing orchestration infrastructure, and from Analytics Engineers scheduling dbt transformations to SRE teams monitoring pipeline reliability and performance. It bridges technical implementation details with operational requirements, ensuring workflows are maintainable, observable, and aligned with organizational data governance standards.

### Strategic Importance

- **Workflow Automation**: Defines automated data pipelines using Apache Airflow, Prefect, Dagster, AWS Step Functions, Azure Logic Apps, or Google Cloud Composer
- **Task Orchestration**: Specifies task dependencies (upstream/downstream), execution order, parallelization strategies, and dynamic task generation
- **Reliability Engineering**: Documents retry policies, failure handling, circuit breakers, SLA definitions, alerting thresholds, and backfill strategies
- **Scheduling Patterns**: Defines cron expressions (@daily, @hourly, custom schedules), catchup behavior, execution dates, and timezone handling
- **Observability**: Enables pipeline monitoring, execution metrics, duration tracking, cost attribution, and troubleshooting through structured DAG documentation
- **Data Lineage**: Supports data governance by documenting data flow, transformation dependencies, and system integration points
- **Operational Excellence**: Facilitates knowledge transfer, reduces mean time to recovery (MTTR), and enables consistent deployment across environments

## Purpose & Scope

### Primary Purpose

This artifact documents Apache Airflow DAG configurations (or equivalent orchestration platform definitions) including task specifications, dependency graphs, scheduling parameters, execution settings, and operational metadata. It enables Data Engineers to define repeatable, maintainable workflow orchestration for data pipelines, ETL/ELT processes, ML model training, and business process automation.

### Scope

**In Scope**:
- DAG configuration: DAG ID, description, owner, tags, schedule_interval, start_date, end_date, catchup settings
- Task definitions: PythonOperator, BashOperator, DockerOperator, KubernetesPodOperator, custom operators
- Task dependencies: set_upstream/set_downstream, bit-shift operators (>> <<), cross-DAG dependencies (TriggerDagRunOperator)
- Scheduling patterns: Cron expressions, preset schedules (@daily, @weekly, @monthly), data interval concepts
- Retry logic: retries, retry_delay, retry_exponential_backoff, max_retry_delay
- SLA monitoring: sla, sla_miss_callback, execution_timeout, dagrun_timeout
- Execution parameters: concurrency, max_active_runs, max_active_tasks, pool assignments
- Connection & variable management: Airflow Connections, Variables, XCom for task communication
- Sensor configurations: FileSensor, S3KeySensor, ExternalTaskSensor, time-based sensors
- Dynamic DAG generation: DAG factory patterns, configuration-driven DAG creation

**Out of Scope**:
- Infrastructure configuration (Airflow deployment architecture, executor configuration, scaling policies)
- Detailed transformation logic within tasks (covered in ETL/ELT Specifications)
- Monitoring dashboards and alerting configurations (covered in operational runbooks)
- Data quality validation rules (covered in Data Quality Specifications)

### Target Audience

**Primary Audience**:
- Data Engineers implementing and maintaining orchestrated data pipelines
- Analytics Engineers scheduling dbt transformations and data modeling workflows
- Platform Engineers managing workflow orchestration infrastructure

**Secondary Audience**:
- SRE Teams monitoring pipeline reliability and performance
- Data Platform Architects designing orchestration patterns and standards
- DevOps Engineers implementing CI/CD for DAG deployment

## Document Information

**Format**: Markdown

**File Pattern**: `*.dag-definitions.md`

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

**DAG Design Patterns**: Use idempotent tasks, implement task retries with exponential backoff, leverage task groups for logical organization
**Naming Conventions**: Use descriptive DAG IDs with environment prefixes (prod_, dev_), follow snake_case for task IDs, tag DAGs by domain/team
**Version Control**: Store DAG files in Git with feature branch workflows, implement CI/CD for DAG deployment, use pre-commit hooks for validation
**Testing Strategy**: Implement unit tests for custom operators, validate DAG structure with dag.test(), use staging environments for testing
**Scheduling Best Practices**: Set appropriate start_date (not dynamic), disable catchup for most DAGs, use timezone-aware datetime objects
**Dependency Management**: Keep task dependencies explicit and minimal, avoid circular dependencies, document cross-DAG dependencies
**Resource Management**: Configure task pools for resource-intensive operations, set appropriate concurrency limits, use Kubernetes executor for isolation
**Error Handling**: Implement comprehensive retry logic, use on_failure_callback for alerting, document expected failure scenarios
**Observability**: Add detailed task logging, use XCom sparingly, implement custom metrics for business KPIs, configure SLA monitoring
**Security**: Store credentials in Airflow Connections (not code), use role-based access control (RBAC), encrypt sensitive XCom data
**Performance**: Avoid top-level code in DAG files, use dynamic task generation judiciously, optimize sensor poke_interval
**Documentation**: Document DAG purpose and owner, specify data lineage and dependencies, maintain runbook for operational procedures
**Monitoring**: Configure alerts for SLA misses, track DAG run duration trends, monitor task failure rates and retry patterns

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

**Workflow Orchestration Platforms**:
- Apache Airflow (open-source, Python-based workflow orchestration)
- Prefect (modern workflow orchestration with dynamic DAGs)
- Dagster (data orchestrator with software-defined assets)
- AWS Step Functions (serverless workflow orchestration)
- Azure Logic Apps (cloud-based workflow automation)
- Google Cloud Composer (managed Airflow on GCP)
- Temporal (microservice orchestration platform)
- Argo Workflows (Kubernetes-native workflow engine)
- Luigi (Python workflow orchestration by Spotify)
- Kedro (data pipeline framework with orchestration)

**Airflow Operators & Integrations**:
- Airflow Providers (AWS, GCP, Azure, Snowflake, dbt, Kubernetes, Docker)
- PythonOperator, BashOperator, DockerOperator, KubernetesPodOperator
- Sensors (FileSensor, S3KeySensor, ExternalTaskSensor, TimeSensor)
- TriggerDagRunOperator, SubDagOperator, TaskGroup
- Custom Operators (extending BaseOperator)

**Scheduling & Execution Standards**:
- Cron expressions (Unix-style scheduling syntax)
- ISO 8601 (datetime and timezone standards)
- UTC timezone conventions for distributed systems
- Airflow schedule presets (@daily, @weekly, @hourly, @monthly, @yearly, @once)
- Timetables (custom scheduling logic in Airflow 2.2+)

**Data Pipeline Patterns**:
- ETL/ELT orchestration patterns
- Medallion architecture (Bronze/Silver/Gold data layers)
- Lambda architecture (batch + streaming)
- Kappa architecture (streaming-first)
- Data mesh (domain-oriented data ownership)
- Change Data Capture (CDC) orchestration

**Observability & Monitoring**:
- OpenTelemetry (distributed tracing standard)
- Prometheus metrics for workflow monitoring
- StatsD for custom metrics collection
- SLA monitoring and alerting patterns
- DataDog, New Relic, Grafana integration

**CI/CD for DAGs**:
- GitOps workflows for DAG deployment
- GitHub Actions, GitLab CI, Jenkins for DAG testing
- Pre-commit hooks for DAG validation
- Integration testing frameworks (pytest-airflow)
- Blue/green deployment for DAG updates

**Data Governance & Lineage**:
- OpenLineage (data lineage standard)
- Apache Atlas (metadata management)
- Data Catalog integration (Alation, Collibra)
- RBAC (Role-Based Access Control) in Airflow
- Data classification and PII handling

**Reference**: Consult organizational data platform and orchestration standards team for detailed guidance on framework application

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
