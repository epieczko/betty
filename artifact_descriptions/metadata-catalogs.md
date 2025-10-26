# Name: metadata-catalogs

## Executive Summary

Metadata Catalogs are centralized inventories that document and organize technical, business, and operational metadata across data assets, systems, and analytics resources. These catalogs serve as the authoritative source for understanding what data exists, where it resides, how it's structured, who owns it, and how it can be accessed—enabling data discovery, governance, and effective utilization.

In modern data ecosystems, metadata catalogs are essential infrastructure that breaks down data silos and enables self-service analytics. They provide searchable inventories of databases, tables, columns, reports, dashboards, data pipelines, and ML models, enriched with business context, lineage information, quality metrics, and usage statistics. This transparency accelerates analytics initiatives and ensures regulatory compliance.

### Strategic Importance

- **Data Discovery**: Enables users to find and understand available data assets without relying on tribal knowledge
- **Governance Foundation**: Provides visibility and control needed for data quality, security, and compliance programs
- **Productivity Acceleration**: Reduces time spent searching for data and understanding its meaning and lineage
- **Risk Mitigation**: Documents data lineage, ownership, and sensitivity to support compliance and audit requirements
- **Collaboration Enhancement**: Creates shared vocabulary and understanding across technical and business teams

## Purpose & Scope

### Primary Purpose

Metadata Catalogs serve as the centralized, searchable inventory of data assets, enriched with technical specifications, business context, lineage information, and governance metadata to enable discovery, understanding, and appropriate use of organizational data.

### Scope

**In Scope**:
- Data source inventories (databases, data warehouses, data lakes, SaaS applications)
- Table and column-level metadata with data types, constraints, and descriptions
- Business glossary terms and their mappings to physical data assets
- Data lineage from sources through transformations to consumption points
- Data quality metrics, profiling results, and validation rules
- Access permissions, security classifications, and PII/sensitivity indicators
- Usage analytics showing who accesses data and how frequently
- Report and dashboard inventory with ownership and dependencies
- ETL/ELT pipeline documentation and data flow diagrams
- API and data service catalogs with endpoints and specifications
- ML model registry with features, metrics, and deployment information
- Data steward and owner assignments for accountability

**Out of Scope**:
- Actual data storage or query execution (catalog is metadata only)
- Real-time data synchronization or operational database functions
- Complete data quality remediation processes
- Full data masking or anonymization implementations
- Detailed application source code or business logic
- Infrastructure monitoring and performance management
- Project management or workflow orchestration

### Target Audience

**Primary Audience**:
- Data analysts and scientists discovering datasets for analysis
- Data engineers documenting pipelines and data transformations
- Data governance teams establishing policies and monitoring compliance
- Business users searching for reports and understanding data definitions
- Data architects designing integrations and understanding system dependencies

**Secondary Audience**:
- Compliance and audit teams verifying data handling and lineage
- Security teams managing access controls and identifying sensitive data
- Executive leadership assessing data asset inventory and governance maturity
- Vendor and partner teams accessing sanctioned data through APIs
- Project teams evaluating data availability for new initiatives

## Document Information

**Format**: Markdown

**File Pattern**: `*.metadata-catalogs.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal

**Retention**: Retain indefinitely as active governance documentation


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

**Automated Scanning**: Use automated discovery tools to populate catalog from source systems
**Business Context**: Enrich technical metadata with business descriptions and ownership
**Data Lineage**: Document end-to-end data flows from source to consumption
**Search Optimization**: Implement robust search with filters, facets, and relevance ranking
**Collaborative Editing**: Allow business users to contribute descriptions and tag assets
**Quality Metrics**: Include data profiling statistics and quality scores
**Access Integration**: Integrate with IAM systems to reflect actual access permissions
**Usage Tracking**: Capture which users and applications access which datasets
**Versioning**: Track schema changes and maintain historical metadata
**Certification**: Mark trusted or certified datasets for production use
**Sensitivity Tagging**: Classify data by sensitivity level and regulatory requirements
**Deprecation Workflow**: Flag obsolete datasets and establish sunset processes
**API First**: Provide programmatic access to metadata for tool integration
**Stakeholder Engagement**: Regularly engage data stewards to improve metadata quality
**Change Notifications**: Alert users when upstream data assets change
**Cross-System Linking**: Connect related assets across different platforms
**Documentation Standards**: Establish naming conventions and description templates
**Regular Audits**: Periodically review catalog completeness and accuracy
**Training Programs**: Educate users on catalog capabilities and best practices
**Glossary Integration**: Link technical terms to business glossary definitions
**Metadata Governance**: Define roles, responsibilities, and processes for metadata management

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

**Data Catalog Platforms**: Alation, Collibra, Atlan, data.world, AWS Glue Data Catalog, Azure Purview, Google Cloud Data Catalog, Informatica Enterprise Data Catalog, Alex Solutions, Apache Atlas, LinkedIn DataHub, Amundsen, OpenMetadata

**Metadata Management**: DAMA-DMBOK (Data Management Body of Knowledge), DCAM (Data Management Capability Assessment Model), EDM Council CDMC, ISO 8000 (Data Quality), ISO 11179 (Metadata Registries)

**Data Governance**: GDPR, CCPA, HIPAA, SOX, BCBS 239, FedRAMP, NIST Cybersecurity Framework, CIS Controls

**Business Glossary**: Collibra Glossary, Alation Glossary, Informatica Business Glossary, erwin Data Intelligence

**Data Lineage**: Manta Data Lineage, Informatica Metadata Manager, Collibra Lineage, Azure Purview Lineage

**Data Quality**: Informatica Data Quality, Talend Data Quality, Ataccama ONE, Precisely Data Integrity Suite

**Discovery & Search**: Elasticsearch, Apache Solr, Algolia, Azure Cognitive Search

**APIs & Integration**: REST APIs, GraphQL, Apache Kafka (event streaming), Apache NiFi, Talend, Fivetran

**Cloud Data Platforms**: Snowflake Information Schema, Databricks Unity Catalog, BigQuery Information Schema, Redshift System Tables

**Data Warehousing**: Snowflake, BigQuery, Redshift, Synapse Analytics, Teradata, Oracle Autonomous Data Warehouse

**ETL/ELT Tools**: dbt (data build tool), Informatica PowerCenter, Talend, Matillion, Apache Airflow, Prefect, Dagster

**Data Lakes**: AWS S3 with Lake Formation, Azure Data Lake Storage, Google Cloud Storage, Databricks Delta Lake

**Semantic Layer**: LookML (Looker), DAX/Tabular Models (Power BI), Cube.js, AtScale, dbt Metrics

**Data Observability**: Monte Carlo, Bigeye, Soda, Acceldata, Databand

**Master Data Management**: Informatica MDM, SAP Master Data Governance, Profisee, Semarchy

**Schema Registry**: Confluent Schema Registry, AWS Glue Schema Registry, Azure Schema Registry

**ML/AI Platforms**: MLflow, Kubeflow, AWS SageMaker, Azure ML, Google Vertex AI, DataRobot

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Data architecture documentation and system inventory
- Existing data dictionaries and schema documentation
- Business glossary terms and definitions
- Data steward assignments and ownership records
- Security classifications and access control policies
- Data quality rules and validation requirements
- Existing lineage documentation and data flow diagrams

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Data discovery and self-service analytics initiatives
- Data governance programs and compliance reporting
- Impact analysis for system changes and migrations
- Data quality improvement programs
- Access request and provisioning workflows
- Training and onboarding materials for data consumers
- Regulatory audit and compliance demonstrations

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Data governance policies and standards
- Business glossary and taxonomy
- Data architecture and system landscape diagrams
- Security and access control documentation
- Data quality scorecards and metrics
- Data lineage and flow diagrams
- Master data management specifications

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
- Primary Approver: Chief Data Officer or Data Governance Lead
- Secondary Approver: Data Architecture Lead and Security Officer
- Governance Approval: Data Governance Council

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review of catalog completeness and accuracy

**Event-Triggered Updates**: Update immediately when:
- New data sources or systems are deployed
- Schemas or data structures change significantly
- Ownership or stewardship assignments change
- Security classifications or access policies are modified
- Regulatory requirements impose new metadata obligations

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

**Retention Period**: Retain indefinitely as active governance documentation

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Chief Data Officer or Data Governance Manager

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/metadata-catalogs-template.md`

**Alternative Formats**: JSON Schema, XML Schema, CSV

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/metadata-catalogs-example-*.md`

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

- SOC 2: Supports audit trails and access controls (CC6.1, CC6.3)
- ISO 27001: Information asset inventory (A.8.1)
- GDPR/Privacy: Data inventory and processing records (Article 30)
- Industry-Specific: BCBS 239 (banking), HIPAA (healthcare), SOX (financial reporting)

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

- Data governance policies and standards
- Information security and classification policies
- Privacy and data protection regulations
- Records retention and archival policies
- Access control and identity management standards

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

**Phase**: Data Governance, Data Management

**Category**: Metadata Management, Data Catalog, Governance

**Typical Producers**: Data Governance Teams, Data Engineers, Data Stewards, Data Architects

**Typical Consumers**: Data Analysts, Business Users, Compliance Teams, Auditors, Data Scientists

**Effort Estimate**: Ongoing effort; initial setup 4-12 weeks, continuous maintenance

**Complexity Level**: High

**Business Criticality**: Mission Critical

**Change Frequency**: Regular (continuous updates)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Data & Analytics - Version 2.0*
