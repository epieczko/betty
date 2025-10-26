# Name: physical-data-model

## Executive Summary

A Physical Data Model is a platform-specific, implementation-ready database design that translates logical data models into actual database objects with DDL (Data Definition Language) scripts, indexes, partitions, constraints, and storage specifications optimized for specific database technologies. This model incorporates performance optimization techniques including denormalization, indexing strategies, partitioning schemes, sharding patterns, compression, and caching aligned with workload requirements and SLA targets.

Physical models span diverse platforms including RDBMS (Oracle, SQL Server, PostgreSQL, MySQL), cloud data warehouses (Snowflake, Redshift, BigQuery, Synapse), NoSQL databases (MongoDB, Cassandra, DynamoDB), data lakehouses (Delta Lake, Iceberg, Hudi), and columnar stores (Vertica, ClickHouse). Design follows DAMA DMBoK physical database design best practices, leveraging platform-specific features like Oracle partitioning, PostgreSQL table inheritance, Snowflake clustering keys, BigQuery partitioned tables, or DynamoDB partition keys to achieve optimal query performance, storage efficiency, and operational scalability.

### Strategic Importance

- **Performance Optimization**: Implements indexes, partitions, and denormalization to meet query latency and throughput SLAs
- **Scalability Enablement**: Designs sharding, partitioning, and distribution strategies supporting horizontal and vertical scaling
- **Cost Efficiency**: Optimizes storage through compression, archival, and tiered storage reducing infrastructure costs
- **Platform Leverage**: Exploits platform-specific features (materialized views, columnstore indexes, zone maps) for competitive advantage
- **Operational Excellence**: Incorporates backup/recovery, archival, and maintenance requirements into physical design
- **Query Workload Alignment**: Tunes database structures for specific read/write patterns, batch processing, and real-time analytics
- **Migration Blueprint**: Provides detailed specifications for database provisioning, deployment, and cloud migration execution

## Purpose & Scope

### Primary Purpose

This artifact provides executable DDL scripts, index definitions, partitioning specifications, storage configurations, and performance optimization strategies for implementing databases on specific platforms (Oracle, PostgreSQL, Snowflake, BigQuery, MongoDB, etc.) aligned with performance, scalability, and cost requirements.

### Scope

**In Scope**:
- Complete DDL (CREATE TABLE, CREATE INDEX, ALTER TABLE) scripts for target database platform
- Physical data type mappings (VARCHAR2, NVARCHAR, TEXT, JSONB, DECIMAL, TIMESTAMP WITH TIME ZONE)
- Index design (B-tree, bitmap, hash, full-text, spatial, covering indexes, included columns)
- Partitioning strategies (range, list, hash, composite partitioning by date, geography, customer segment)
- Sharding and distribution keys for horizontally scaled databases (Cassandra partition keys, Citus distribution columns)
- Denormalization decisions with rationale (materialized aggregations, embedded documents, flattened hierarchies)
- Compression specifications (column-level compression, table compression, codec selection)
- Storage optimizations (tablespaces, filegroups, storage tiers, S3 storage classes)
- Clustering keys and sort keys (Snowflake clustering keys, Redshift sort keys, BigQuery clustering)
- Materialized views and indexed views with refresh strategies
- Constraints implementation (primary keys, foreign keys, unique constraints, check constraints, not null)
- Default values, computed columns, and generated columns
- Sequences, identity columns, and auto-increment specifications
- Statistics collection and histogram strategies
- Backup and archival strategies (hot backups, point-in-time recovery, retention policies)
- Performance tuning parameters (buffer pools, cache sizes, parallelism settings)
- Security implementation (row-level security, column masking, encryption at rest/in transit)

**Out of Scope**:
- Logical data model and business entity definitions (covered by logical-data-model artifact)
- ETL/ELT implementation and data transformation code (documented in pipeline specifications)
- Application-level ORM mappings and object-relational configurations
- Database administration procedures (backups, monitoring, patching) - covered by DBA runbooks
- Query optimization for specific reports (covered by performance tuning documentation)

### Target Audience

**Primary Audience**:
- Database Administrators (DBAs): Implement physical models, provision databases, and optimize performance
- Database Developers: Write DDL scripts and implement database objects aligned with physical design
- Data Engineers: Understand table structures, partitioning, and indexes when building data pipelines
- Platform Engineers: Deploy database infrastructure and configure storage, networking, and security

**Secondary Audience**:
- Data Architects: Review physical design decisions for alignment with standards and best practices
- Application Developers: Understand physical constraints, indexes, and performance characteristics
- Performance Engineers: Analyze physical design for query optimization and tuning opportunities
- Cloud Architects: Design infrastructure provisioning for cloud-native database deployments

## Document Information

**Format**: Markdown

**File Pattern**: `*.physical-data-model.md`

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

**Workload-Driven Design**: Analyze query patterns, read/write ratios, and access patterns before finalizing indexes and partitioning
**Platform-Native Features**: Leverage platform-specific optimizations (Snowflake micro-partitions, BigQuery partitioned tables, Postgres BRIN indexes)
**Index Strategy**: Create covering indexes for critical queries, avoid over-indexing writes-heavy tables, use filtered/partial indexes
**Partitioning by Access Pattern**: Partition by date for time-series data, by geography for regional queries, by customer segment for multi-tenant architectures
**Denormalization with Purpose**: Denormalize only when proven performance benefits outweigh maintenance complexity; document rationale
**Compression Selection**: Use columnar compression for analytics (Parquet, ORC), row compression for OLTP, evaluate compression ratios vs. CPU cost
**Statistics Maintenance**: Configure automatic statistics collection, refresh after bulk loads, use histograms for skewed distributions
**Surrogate Keys**: Use auto-incrementing surrogate keys (IDENTITY, SERIAL, sequences) for primary keys in most OLTP scenarios
**Data Type Precision**: Choose appropriate precision (INT vs. BIGINT, DECIMAL precision/scale) balancing storage and accuracy requirements
**Constraint Enforcement**: Implement constraints (foreign keys, checks) in databases for data integrity, not just application-layer validation
**Sharding Keys**: Select sharding/distribution keys ensuring even data distribution and minimizing cross-shard queries
**Materialized Views**: Use for complex aggregations with infrequent updates, configure appropriate refresh strategies (on-demand, scheduled)
**DDL in Version Control**: Store all DDL scripts in Git with migration scripts (Flyway, Liquibase, Alembic) for controlled deployments
**Naming Conventions**: Follow consistent naming (snake_case, PascalCase) aligned with platform conventions and organizational standards
**Tablespace Management**: Organize tables into tablespaces/filegroups by volatility, size, and backup requirements
**Columnar for Analytics**: Use columnstore indexes (SQL Server), columnar storage (Redshift, Synapse) for analytical queries
**Read Replicas**: Design for read replica scaling, ensuring replication lag acceptable for use cases
**Testing Physical Design**: Validate physical design with representative data volumes and actual query workloads before production

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

**Physical Database Design Standards**:
- DAMA DMBoK Chapter 5: Data Modeling and Design including physical design best practices
- SQL:2016 Standard: ANSI/ISO SQL standard for DDL, data types, and constraints
- ANSI SPARC Architecture: Physical schema layer specification and implementation
- IEEE 1320.2: Physical database design documentation standards

**RDBMS Platforms**:
- Oracle Database: Partitioning, RAC, Exadata, compression, advanced indexes
- Microsoft SQL Server: Columnstore indexes, In-Memory OLTP, partitioning, Always On
- PostgreSQL: Table inheritance, BRIN indexes, partitioning, extensions (TimescaleDB, Citus)
- MySQL/MariaDB: InnoDB storage engine, partitioning, replication
- IBM Db2: Range partitioning, MDC (Multi-Dimensional Clustering), compression

**Cloud Data Warehouses**:
- Snowflake: Micro-partitions, clustering keys, zero-copy cloning, time travel
- Amazon Redshift: Distribution styles (KEY, ALL, EVEN), sort keys, compression encodings
- Google BigQuery: Partitioned tables, clustered tables, nested/repeated fields
- Azure Synapse Analytics: Distribution strategies (hash, round-robin, replicate), columnstore
- Databricks Lakehouse: Delta Lake, Z-ordering, liquid clustering, photon engine

**NoSQL Databases**:
- MongoDB: Document modeling, embedded vs. referenced documents, indexes, sharding
- Apache Cassandra: Partition keys, clustering keys, wide-column design, replication
- Amazon DynamoDB: Partition keys, sort keys, global secondary indexes, DynamoDB Streams
- Redis: Data structures (strings, hashes, lists, sets, sorted sets), persistence options
- Neo4j: Graph modeling, index strategies, relationship properties

**Data Lakehouse Platforms**:
- Delta Lake: ACID transactions, time travel, Z-ordering, liquid clustering
- Apache Iceberg: Hidden partitioning, schema evolution, snapshot isolation
- Apache Hudi: Copy-on-write, merge-on-read, incremental queries, indexing

**Columnar & OLAP Databases**:
- Apache Druid: Segment partitioning, compression, indexing for sub-second analytics
- ClickHouse: MergeTree engine family, materialized views, compression codecs
- Vertica: Projections, encoding, segmentation, epoch-based storage
- Apache Pinot: Real-time and offline tables, star-tree indexes

**Database Migration & Schema Management Tools**:
- Flyway: Database migration version control with SQL-based migrations
- Liquibase: Database-independent schema changes with XML/YAML/JSON/SQL formats
- Alembic: Python-based database migration tool for SQLAlchemy
- gh-ost: GitHub's online schema migration tool for MySQL
- Sqitch: Database change management with dependency tracking

**Performance & Optimization**:
- Query Execution Plans: EXPLAIN/EXPLAIN ANALYZE for performance analysis
- Database Tuning Advisor: Automated index and partitioning recommendations
- Query Store: SQL Server query performance history and regression detection
- Performance Insights: AWS RDS/Aurora query performance monitoring
- Index Tuning Wizard: Automated index recommendation tools

**Data Modeling Tools with Physical Support**:
- ER/Studio: Forward/reverse engineering with platform-specific DDL generation
- PowerDesigner: Physical model generation for 60+ database platforms
- ERwin: Physical database design with DDL generation and reverse engineering
- Oracle SQL Developer Data Modeler: Oracle-optimized physical modeling
- MySQL Workbench: Forward engineering for MySQL with DDL generation
- dbForge Studio: Physical design tools for SQL Server, MySQL, PostgreSQL

**Cloud Infrastructure as Code**:
- Terraform: Infrastructure provisioning for RDS, Aurora, Synapse, BigQuery
- AWS CloudFormation: AWS database infrastructure deployment templates
- Azure ARM Templates/Bicep: Azure database infrastructure automation
- Google Cloud Deployment Manager: GCP database deployment automation

**Backup & Recovery Standards**:
- RPO (Recovery Point Objective): Maximum acceptable data loss window
- RTO (Recovery Time Objective): Maximum acceptable downtime for recovery
- PITR (Point-in-Time Recovery): Transaction log-based recovery capabilities
- Hot Backups: Online backups without downtime (RMAN, pg_basebackup)

**High Availability & Disaster Recovery**:
- Oracle RAC (Real Application Clusters): Multi-node clustering
- SQL Server Always On: Availability groups and failover clustering
- PostgreSQL Streaming Replication: Hot standby and read replicas
- MySQL Group Replication: Multi-master replication
- Cloud-native HA: Multi-AZ deployments, read replicas, failover automation

**Security & Compliance**:
- Transparent Data Encryption (TDE): Encryption at rest for Oracle, SQL Server
- Column-Level Encryption: Application-managed encryption for sensitive fields
- Row-Level Security: Dynamic data masking and access control
- Always Encrypted: SQL Server client-side encryption with secure enclaves

**Reference**: Consult database platform documentation, vendor best practices guides, DBA teams, and DAMA DMBoK Chapter 5 for platform-specific physical design patterns and optimization techniques

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
