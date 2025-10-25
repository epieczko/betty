# Name: data-dictionaries

## Executive Summary

The Data Dictionary is a foundational metadata management artifact that provides comprehensive documentation of data elements, business definitions, and technical specifications across an organization's data landscape. This artifact serves as the single source of truth for understanding data semantics, ensuring consistent interpretation and usage of data assets across analytics, engineering, and business teams.

As a core component of enterprise data governance and metadata management programs, the Data Dictionary supports regulatory compliance (GDPR Article 30, CCPA), data quality management (ISO 8000), and metadata standardization (ISO 11179). Modern data catalog platforms like Collibra, Alation, Apache Atlas, DataHub, and Amundsen provide technical implementations of data dictionaries, enabling searchable, collaborative, and automated metadata management aligned with DAMA DMBoK best practices.

### Strategic Importance

- **Metadata Standardization**: Implements ISO 11179 metadata registry standards for consistent data element definitions
- **Business Glossary Integration**: Links technical metadata to business terminology using Collibra or Alation capabilities
- **Data Governance Foundation**: Supports DCAM (Data Management Capability Assessment Model) and EDM Council frameworks
- **Regulatory Compliance**: Enables GDPR Article 30 ROPA (Record of Processing Activities) and data classification requirements
- **Data Quality**: Defines data types, constraints, valid values, and business rules that feed data quality frameworks
- **Cross-functional Communication**: Bridges business analysts, data engineers, and data scientists with common vocabulary
- **Data Lineage Support**: Provides technical metadata (tables, columns, types) that feeds data lineage tracking systems

## Purpose & Scope

### Primary Purpose

This artifact serves as a comprehensive registry of all data elements within a database, data warehouse, data lake, or data product, documenting entity definitions, attribute specifications, data types, constraints, business rules, and valid value domains. It enables consistent understanding and usage of data across technical and business stakeholders.

### Scope

**In Scope**:
- Entity and table definitions with business purpose and ownership
- Attribute/column specifications including data types (VARCHAR, INTEGER, DECIMAL, TIMESTAMP, etc.)
- Primary keys, foreign keys, and referential integrity constraints
- Business rules, validation rules, and data quality expectations
- Valid value domains, enumerations, and reference data specifications
- Data sensitivity classification (PII, confidential, public) per GDPR/CCPA requirements
- Business glossary terms mapped to technical metadata
- Data steward assignments and ownership information
- System of record and authoritative source identification
- Metadata synchronized from data catalog tools (Collibra, Alation, Apache Atlas, DataHub)

**Out of Scope**:
- Actual data lineage flows (covered by data-lineage-maps artifact)
- Physical implementation details like indexes and partitioning (covered by physical-data-model artifact)
- Data quality measurement results (covered by data quality reports)
- ETL/ELT transformation logic (documented in data pipeline specifications)
- API specifications for data access (covered by API documentation artifacts)

### Target Audience

**Primary Audience**:
- Data Engineers: Use data dictionaries to understand table schemas, data types, and constraints when building pipelines
- Data Analysts: Reference business definitions and valid values when creating reports and analyses
- Analytics Engineers: Leverage metadata for dbt model development and documentation
- Data Stewards: Maintain and govern data element definitions and business rules

**Secondary Audience**:
- Data Architects: Ensure consistency with logical and physical data models
- Business Analysts: Understand data semantics and business terminology
- Compliance Officers: Verify data classification and regulatory compliance mappings
- Software Engineers: Reference data contracts when integrating with data platforms

## Document Information

**Format**: Markdown

**File Pattern**: `*.data-dictionaries.md`

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

**Automated Metadata Discovery**: Leverage data catalog tools (Collibra, Alation, Apache Atlas, DataHub) to automatically harvest technical metadata from databases, reducing manual effort and ensuring accuracy
**ISO 11179 Naming Conventions**: Follow ISO 11179 standards for data element naming including object class, property, and representation terms (e.g., customer_birth_date, product_unit_price)
**Business Glossary Integration**: Link every technical data element to business glossary terms to ensure business context and consistent interpretation across the organization
**Data Classification Tagging**: Apply sensitivity classifications (PII, PHI, PCI, confidential, public) to all data elements per GDPR Article 30 and CCPA requirements
**Data Steward Assignment**: Assign both business data stewards (define semantics) and technical data custodians (manage implementation) for every critical data element
**Mandatory Fields**: Require business definition, data type, nullability, constraints, and steward assignment for all data dictionary entries
**Valid Value Domains**: Document enumerated values, reference data sets, and validation rules for controlled vocabularies and lookup tables
**Source System Documentation**: Identify system of record (SOR) and authoritative sources for each data element to enable data lineage and trust assessment
**Example Values**: Provide realistic example values (with PII redacted) to clarify format, precision, and business meaning
**Relationship Documentation**: Document foreign key relationships and conceptual entity relationships to show how data elements connect across tables
**Version Control**: Store data dictionaries in Git or integrate with data catalog version control to maintain complete change history
**Search Optimization**: Use consistent tagging, synonyms, and descriptions to improve discoverability in data catalog search interfaces
**dbt Integration**: Leverage dbt model documentation and schema.yml files to maintain data dictionaries as code alongside data transformation logic
**Metadata Lineage**: Trace metadata changes through environments (dev, test, prod) using catalog tools to ensure consistency across SDLC
**Regular Reconciliation**: Schedule quarterly reconciliation between data dictionary and actual database schemas using automated schema drift detection
**Quality Metrics**: Track metadata completeness KPIs (% of tables documented, % with business definitions, % with steward assignments)
**Cross-reference Data Models**: Ensure consistency between data dictionaries, logical data models, and physical data models
**Retirement Tracking**: Document deprecated fields and tables with retirement dates and migration guidance to prevent continued usage

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

**Metadata Management Standards**:
- ISO 11179: Metadata registries standard for data element definitions and naming conventions
- ISO/IEC 8000: Data quality standards including accuracy, completeness, and consistency dimensions
- CDMC (Common Data Management Curriculum): Metadata management competency framework
- Dublin Core Metadata Initiative: Standardized metadata vocabulary and schema

**Data Governance Frameworks**:
- DAMA DMBoK (Data Management Body of Knowledge): Chapter 12 - Metadata Management
- DCAM (Data Management Capability Assessment Model): Metadata management capability areas
- EDM Council DCAM: Financial services data management framework
- DGI Data Governance Framework: Metadata and business glossary governance

**Data Catalog & Metadata Tools**:
- Collibra Data Intelligence Cloud: Enterprise data catalog with business glossary and stewardship workflows
- Alation Data Catalog: Collaborative data catalog with automated metadata discovery and curation
- Apache Atlas: Open-source metadata management and data governance platform for Hadoop ecosystems
- DataHub (LinkedIn): Open-source metadata platform with lineage, quality, and discovery capabilities
- Amundsen (Lyft): Open-source data discovery and metadata engine
- AWS Glue Data Catalog: Serverless metadata repository for AWS data lakes
- Azure Purview: Microsoft unified data governance service with automated scanning
- Google Cloud Data Catalog: Managed metadata service for GCP data assets

**Data Classification Standards**:
- GDPR Article 30: Record of Processing Activities (ROPA) requirements for personal data inventory
- CCPA: California Consumer Privacy Act data inventory and classification requirements
- NIST SP 800-60: Guide for mapping types of information and information systems to security categories
- ISO 27001 Annex A.8.2: Information classification and labeling requirements
- PCI DSS: Payment Card Industry data classification for cardholder data elements

**Business Glossary Standards**:
- FIBO (Financial Industry Business Ontology): Financial services business semantics
- ACORD (Association for Cooperative Operations Research and Development): Insurance industry data standards
- HL7 FHIR: Healthcare data interoperability standards
- MISMO (Mortgage Industry Standards Maintenance Organization): Mortgage data standards

**Data Modeling Standards**:
- ISO/IEC 11404: Language-independent data types
- SQL:2016 Standard: Data type specifications for relational databases
- JSON Schema: Schema vocabulary for JSON data structures
- Apache Avro, Parquet, ORC: Modern data serialization and storage formats with schema definitions

**Data Stewardship & Ownership**:
- RACI Matrix for Data Governance: Responsible, Accountable, Consulted, Informed for data element ownership
- Data Mesh principles: Domain-oriented data ownership with data products as first-class citizens
- Data Ownership frameworks: Business data steward and technical data custodian assignment models

**Integration Standards**:
- OpenMetadata: Open standard for metadata interchange and collaboration
- Common Information Model (CIM): Schema for enterprise metadata exchange
- W3C DCAT (Data Catalog Vocabulary): RDF vocabulary for publishing data catalogs on the web
- Schema.org Dataset markup: Structured data for dataset discoverability

**Reference**: Consult organizational data architecture and governance teams for detailed guidance on framework application and tool selection based on technology stack and compliance requirements

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
