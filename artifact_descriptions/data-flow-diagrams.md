# Name: data-flow-diagrams

## Executive Summary

Data Flow Diagrams (DFDs) are analytical artifacts that visualize how data moves through a system, showing processes, data stores, external entities, and the transformations data undergoes as it flows between components. Using structured analysis notation (Yourdon-DeMarco, Gane-Sarson) and modern adaptations, DFDs communicate data movement, processing logic, storage requirements, and integration points without implementation details.

As fundamental tools for data-centric analysis, DFDs support requirements analysis, data governance, privacy compliance (GDPR, CCPA), security boundary definition, and data lineage documentation. They enable data architects to design data pipelines, ETL/ELT processes, stream processing workflows, and data integration patterns while supporting compliance teams in mapping data flows for regulatory requirements and identifying sensitive data handling touchpoints.

### Strategic Importance

- **Data Governance**: Maps data lineage, ownership, and transformation points supporting data catalogs (Collibra, Alation, Purview) and metadata management
- **Privacy Compliance**: Documents personal data flows for GDPR Article 30 records of processing, CCPA data mapping, and privacy impact assessments
- **Security Analysis**: Identifies data exposure points, encryption boundaries, and trust zones for threat modeling and security architecture
- **Integration Design**: Specifies data exchange patterns for APIs, message queues, batch transfers, CDC (Change Data Capture), and event streaming
- **Process Optimization**: Reveals data movement inefficiencies, redundant transformations, and opportunities for caching, denormalization, or pipeline consolidation

## Purpose & Scope

### Primary Purpose

This artifact documents data movement using multi-level DFD notation (Context Diagram, Level 0, Level 1+) showing external entities, processes, data stores, and data flows. Created using Lucidchart, draw.io, Visio, or specialized tools (ER/Studio, Enterprise Architect), it specifies data transformations, storage points, API data exchanges, batch transfers, and streaming flows to guide data architecture, integration design, and compliance assessment.

### Scope

**In Scope**:
- Context Diagram (Level 0): System boundary, external entities, major data flows to/from the system
- Level 1 DFD: Major processes, primary data stores, key data flows within system boundary
- Level 2+ DFDs: Detailed decomposition of specific processes, transformations, and sub-flows
- Data transformation logic: ETL processes, data enrichment, aggregation, filtering, validation, cleansing
- Data storage: Databases (relational, NoSQL, data warehouses, data lakes), caches, file systems, object storage
- Integration patterns: RESTful APIs, GraphQL, message queues, event streams, batch file transfers, database replication
- Data flow types: Synchronous API calls, asynchronous messages, batch transfers, real-time streaming (Kafka, Kinesis)
- External system integration: Third-party APIs, SaaS platforms, legacy systems, partner data exchanges
- Data lineage: Source-to-target mapping, transformation chain, data provenance for governance and compliance
- Sensitive data flows: PII (Personally Identifiable Information), PHI (Protected Health Information), payment data (PCI)

**Out of Scope**:
- Detailed database schema and entity relationships (see Entity-Relationship Diagrams)
- Logical component structure and service boundaries (see Logical Architecture Diagram)
- Runtime interaction sequences and API choreography (see Sequence Diagrams)
- Network topology and infrastructure (see Physical Architecture Diagram)
- Security controls implementation (see Security Architecture Diagram)

### Target Audience

**Primary Audience**:
- Data Architects designing data pipelines, integration architectures, and data platform solutions
- Data Engineers implementing ETL/ELT processes, stream processing, and data replication using Spark, Airflow, Kafka, or cloud services
- Business Analysts understanding information flow, system integration points, and data transformation requirements

**Secondary Audience**:
- Privacy Officers mapping personal data flows for GDPR compliance, data subject access requests, and privacy impact assessments
- Security Architects identifying data exposure points, encryption requirements, and sensitive data handling controls
- Compliance Teams validating data retention, cross-border transfers, and regulatory compliance (HIPAA, PCI DSS, SOX)

## Document Information

**Format**: Multiple

**File Pattern**: `*.data-flow-diagrams.*`

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

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use approved templates to ensure completeness and consistency across teams
**Peer Review**: Have at least one qualified peer review before submitting for approval
**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management
**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in
**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon
**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively
**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation
**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes
**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats
**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates
**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy

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

**Data Flow Diagram Notations**:
- Yourdon-DeMarco Notation - Circles for processes, arrows for data flows, parallel lines for data stores, rectangles for external entities
- Gane-Sarson Notation - Rounded rectangles for processes, arrows for flows, open-ended boxes for data stores
- UML Data Flow Extensions - Adapted UML notation for data flow modeling
- IDEF0 - Integration Definition for Function Modeling (process-centric with data flows)
- Data Flow Modeling Standards - IEEE standards for structured analysis

**Diagramming Tools**:
- Lucidchart - DFD templates with Yourdon-DeMarco and Gane-Sarson shapes
- draw.io / diagrams.net - Free DFD diagramming with template libraries
- Microsoft Visio - Professional diagramming with DFD stencils
- ER/Studio Data Architect - Enterprise data modeling with data flow capabilities
- Enterprise Architect - UML and data flow modeling
- Visual Paradigm - Multi-notation data flow and process modeling
- yEd Graph Editor - Free graph visualization for data flows
- Creately - Online DFD creation and collaboration

**Data Management Frameworks**:
- DAMA-DMBOK (Data Management Body of Knowledge) - 11 knowledge areas including data architecture, integration, governance
- DCAM (Data Management Capability Assessment Model) - Data management maturity framework by EDM Council
- Data Governance Framework - Policies, standards, and processes for data management
- COBIT for Data & Information - IT governance framework for data management
- ISO 8000 Data Quality - International standard for data quality management

**Data Architecture Patterns**:
- Lambda Architecture - Batch and speed layers for big data processing
- Kappa Architecture - Stream-only data processing architecture
- Medallion Architecture - Bronze/Silver/Gold data lake layering (Databricks)
- Data Mesh - Domain-oriented decentralized data architecture
- Data Fabric - Integrated data architecture layer across distributed environments
- Hub-and-Spoke Integration - Central integration hub with spoke connections
- Point-to-Point Integration - Direct system-to-system connections

**Data Integration Technologies**:
- ETL Tools - Informatica PowerCenter, IBM DataStage, Talend, Microsoft SSIS
- Cloud ETL/ELT - AWS Glue, Azure Data Factory, Google Cloud Dataflow, Fivetran, Stitch
- Stream Processing - Apache Kafka, Apache Flink, Apache Spark Streaming, AWS Kinesis, Azure Event Hubs
- Data Replication - Debezium, Oracle GoldenGate, AWS DMS, Qlik Replicate
- iPaaS (Integration Platform as a Service) - MuleSoft, Dell Boomi, Informatica Cloud, SnapLogic
- API Management - Apigee, Kong, AWS API Gateway, Azure API Management, MuleSoft Anypoint

**Data Governance & Cataloging**:
- Collibra - Enterprise data governance and cataloging platform
- Alation - Data catalog with collaboration and data intelligence
- Microsoft Purview - Unified data governance for on-premises and multi-cloud
- Informatica Data Catalog - Enterprise data cataloging and metadata management
- Atlan - Modern data workspace and collaboration platform
- Apache Atlas - Open-source metadata management and data governance
- Data Lineage Tools - Manta, Octopai for automated lineage discovery

**Privacy & Compliance**:
- GDPR (General Data Protection Regulation) - EU data protection and privacy law requiring data flow documentation
- CCPA (California Consumer Privacy Act) - California privacy law with data mapping requirements
- HIPAA (Health Insurance Portability and Accountability Act) - US healthcare data protection standards
- PCI DSS (Payment Card Industry Data Security Standard) - Payment data security requirements
- SOX (Sarbanes-Oxley Act) - Financial data controls and audit trails
- Data Privacy Impact Assessment (DPIA) - Systematic assessment of data processing risks

**Data Quality & Validation**:
- ISO 8000 - Data quality standards
- Data Quality Dimensions - Accuracy, completeness, consistency, timeliness, validity, uniqueness
- Great Expectations - Python-based data validation framework
- dbt (data build tool) - Data transformation with testing and documentation
- Apache Griffin - Data quality service with accuracy and profiling

**Metadata Management**:
- Common Warehouse Metamodel (CWM) - OMG standard for metadata interchange
- Metadata Repositories - Centralized storage for technical and business metadata
- Data Dictionary - Comprehensive catalog of data elements and definitions
- Business Glossary - Business terminology and definitions for data governance

**Data Pipeline Orchestration**:
- Apache Airflow - Workflow orchestration for data pipelines with Python DAGs
- Prefect - Modern workflow orchestration with dynamic pipelines
- Dagster - Data orchestrator for machine learning, analytics, and ETL
- AWS Step Functions - Serverless orchestration for AWS services
- Azure Data Factory - Cloud ETL/ELT with visual pipeline designer
- Google Cloud Composer - Managed Apache Airflow on GCP

**Streaming & Event-Driven Architecture**:
- Apache Kafka - Distributed event streaming platform
- Apache Pulsar - Cloud-native distributed messaging and streaming
- AWS Kinesis - Real-time data streaming on AWS
- Azure Event Hubs - Big data streaming service
- Google Cloud Pub/Sub - Messaging and event ingestion
- Event Sourcing - Storing state as sequence of events
- CDC (Change Data Capture) - Capturing database changes for replication

**Reference**: Consult data architecture, data engineering, and data governance teams for detailed guidance on data flow modeling standards, integration patterns, privacy compliance requirements, and data pipeline design for your organization's data ecosystem

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
