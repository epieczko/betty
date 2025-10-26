# Name: logical-data-model

## Executive Summary

A Logical Data Model is a technology-independent, business-oriented representation of data structures that captures entities, attributes, relationships, and business rules without concern for physical implementation details. This model bridges business terminology and technical implementation, using Entity-Relationship Diagrams (ERD), UML class diagrams, or dimensional models to represent data semantics aligned with business processes and requirements.

Logical models typically apply normalization techniques (First Normal Form through Third Normal Form or Boyce-Codd Normal Form) for transactional systems, dimensional modeling (star schema, snowflake schema) for analytics, or Data Vault 2.0 for enterprise data warehouses. Modern tooling includes ER/Studio, PowerDesigner, ERwin Data Modeler, Lucidchart, draw.io, and data catalog platforms (Collibra, Alation) with model documentation capabilities, supporting DAMA DMBoK data modeling and design best practices and integrating with enterprise architecture frameworks.

### Strategic Importance

- **Business-IT Alignment**: Provides shared understanding between business stakeholders and technical teams using business terminology
- **Data Standardization**: Establishes enterprise-wide agreement on entity definitions, attribute semantics, and relationship cardinalities
- **Quality Foundation**: Defines business rules, constraints, and data integrity requirements that feed data quality specifications
- **Implementation Blueprint**: Serves as specification for physical database design across RDBMS, NoSQL, and data warehouse platforms
- **Change Impact Analysis**: Enables assessment of how business requirement changes affect data structures and downstream systems
- **Regulatory Compliance**: Documents data relationships and attribute definitions supporting GDPR, BCBS 239, and audit requirements
- **Knowledge Repository**: Captures institutional knowledge about business entities and their relationships for long-term organizational learning

## Purpose & Scope

### Primary Purpose

This artifact provides a platform-independent, business-oriented data structure specification defining entities, attributes, relationships, business rules, and constraints using normalized forms, dimensional models, or Data Vault architectures to serve as the blueprint for physical database implementation.

### Scope

**In Scope**:
- Entity definitions with business names, descriptions, and purposes (Customer, Order, Product, Transaction)
- Attribute specifications with business names, data types (at logical level: string, number, date, boolean), optionality, and business definitions
- Relationship definitions with cardinality (one-to-one, one-to-many, many-to-many) and participation constraints (mandatory, optional)
- Primary key and unique key identification (natural keys, composite keys)
- Foreign key relationships and referential integrity constraints
- Normalization specifications (1NF, 2NF, 3NF, BCNF) for transactional models
- Dimensional modeling (fact tables, dimension tables, star schema, snowflake schema, constellation schema) for analytics
- Data Vault 2.0 structures (hubs, links, satellites) for enterprise data warehouses
- Business rules and constraints (check constraints, derivation rules, validation rules)
- Subject area models and domain decomposition
- Entity-Relationship Diagrams (ERD) using Crow's Foot, IE (Information Engineering), or UML notation
- Attribute domain definitions and valid value specifications
- Slowly Changing Dimension (SCD) type specifications (Type 1, 2, 3) for dimensional models
- Supertype/subtype relationships and inheritance hierarchies

**Out of Scope**:
- Physical implementation details (indexes, partitions, tablespaces, storage) - covered by physical-data-model artifact
- Actual DDL (Data Definition Language) scripts and SQL implementation - covered by physical-data-model artifact
- ETL/ELT transformation logic - documented in data pipeline specifications
- Performance tuning and optimization strategies - covered by physical design documentation
- Technology-specific data type mappings (VARCHAR2 vs VARCHAR, INT vs BIGINT) - covered by physical-data-model

### Target Audience

**Primary Audience**:
- Data Architects: Design and maintain enterprise logical data models aligned with business requirements
- Data Modelers: Create subject area models and dimensional models for specific business domains
- Business Analysts: Validate entity definitions, relationships, and business rules with business stakeholders
- Database Designers: Transform logical models into platform-specific physical database designs

**Secondary Audience**:
- Data Stewards: Review entity and attribute definitions for governance and standardization
- Application Developers: Understand data structures when building applications and integrations
- Analytics Engineers: Use dimensional models as basis for dbt models and semantic layers
- Enterprise Architects: Ensure logical models align with enterprise architecture principles

## Document Information

**Format**: Markdown

**File Pattern**: `*.logical-data-model.md`

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

**Business Language First**: Use business terminology for entity and attribute names, avoiding technical jargon or abbreviations
**Normalization for OLTP**: Apply Third Normal Form (3NF) or Boyce-Codd Normal Form (BCNF) for transactional operational systems
**Dimensional for Analytics**: Use star schema or snowflake schema for data warehouses and analytical data marts
**Data Vault for EDW**: Consider Data Vault 2.0 (hubs, links, satellites) for enterprise data warehouses requiring historization and auditability
**Consistent Notation**: Standardize on one ERD notation (Crow's Foot, IE, UML) across the enterprise for consistency
**Complete Definitions**: Provide business definitions for every entity and attribute, not just technical descriptions
**Cardinality Precision**: Specify exact relationship cardinality (1:1, 1:M, M:M) and participation constraints (mandatory, optional)
**Natural Keys**: Identify natural business keys (customer number, order ID) even if surrogate keys will be used physically
**Subject Area Decomposition**: Break complex enterprise models into manageable subject areas (Customer, Product, Finance, Operations)
**Reusable Entities**: Design common entities (Party, Address, Contact) for reuse across subject areas
**SCD Type Selection**: Define Slowly Changing Dimension handling (Type 1 overwrite, Type 2 historize, Type 3 limited history) for each dimension
**Business Rule Documentation**: Explicitly document business rules, constraints, and derivation logic in model annotations
**Stakeholder Review**: Conduct structured walkthroughs with business stakeholders to validate entities, relationships, and attributes
**Model Patterns**: Apply proven modeling patterns (Party-Role, Product-Instance, Account-Transaction) to common business scenarios
**Supertypes/Subtypes**: Use generalization hierarchies for entities with common attributes and specialized subtypes
**Version Control**: Store models in version-controlled repositories (Git with .dmm files, or modeling tool repositories)
**Forward Engineering**: Maintain ability to forward-engineer logical models to physical DDL with tooling
**Reverse Engineering**: Periodically reverse-engineer existing databases to validate logical models remain synchronized
**Integration with Catalog**: Publish logical model metadata to data catalogs (Collibra, Alation) for enterprise visibility

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

**Data Modeling Standards & Methodologies**:
- DAMA DMBoK Chapter 5: Data Modeling and Design best practices
- IDEF1X (Integration Definition for Information Modeling): Federal standard for data modeling
- ISO/IEC 11179: Metadata registry standards including naming conventions
- ANSI SPARC Three Schema Architecture: Conceptual, logical, physical model separation
- Unified Modeling Language (UML): Class diagrams for object-oriented data modeling

**Normalization Theory**:
- Codd's Normal Forms: First Normal Form (1NF) through Sixth Normal Form (6NF)
- Third Normal Form (3NF): Industry standard for transactional database normalization
- Boyce-Codd Normal Form (BCNF): Stronger version of 3NF eliminating certain anomalies
- Domain-Key Normal Form (DK/NF): Ultimate normal form based on domain and key constraints

**Dimensional Modeling (Kimball Methodology)**:
- Star Schema: Fact table surrounded by denormalized dimension tables
- Snowflake Schema: Normalized dimension tables with multiple levels
- Constellation Schema (Galaxy Schema): Multiple fact tables sharing dimensions
- Fact Table Design: Additive, semi-additive, non-additive measures
- Dimension Table Design: SCD Types 0-7 for handling dimension changes
- Conformed Dimensions: Shared dimensions across data marts for enterprise consistency
- Degenerate Dimensions: Dimension attributes stored in fact tables
- Role-Playing Dimensions: Single dimension used multiple times in different contexts

**Data Vault 2.0 (Dan Linstedt)**:
- Hub: Core business entities with business keys
- Link: Relationships between hubs (many-to-many associations)
- Satellite: Descriptive attributes and temporal tracking for hubs and links
- Same-As Link (SAL): Entity resolution and master data integration
- Point-In-Time (PIT) Tables: Query optimization structures
- Bridge Tables: Many-to-many relationship resolution

**Data Modeling Tools**:
- ER/Studio Data Architect: Enterprise data modeling with forward/reverse engineering
- PowerDesigner (SAP): Comprehensive data modeling and metadata management
- ERwin Data Modeler: Database design and data modeling platform
- Oracle SQL Developer Data Modeler: Free tool for logical and physical modeling
- MySQL Workbench: Open-source data modeling for MySQL
- pgModeler: PostgreSQL-specific database modeling tool
- Lucidchart: Cloud-based ERD diagramming with collaboration
- draw.io (diagrams.net): Free, open-source diagramming tool with ERD support
- PlantUML: Text-based UML diagram generation including class diagrams
- DbSchema: Visual database designer with reverse engineering

**ERD Notation Standards**:
- Crow's Foot Notation (Martin Notation): Most popular ERD notation showing cardinality
- Information Engineering (IE) Notation: James Martin's notation with detailed cardinality
- Chen Notation: Original ERD notation by Peter Chen (1976)
- UML Class Diagrams: Object-oriented representation of data structures
- IDEF1X: Integration Definition notation used in government and defense

**Enterprise Architecture Frameworks**:
- TOGAF (The Open Group Architecture Framework): Data architecture domain including logical models
- Zachman Framework: Row 2 (Business Model) and Row 3 (System Model) data perspectives
- Federal Enterprise Architecture Framework (FEAF): Data Reference Model (DRM)

**Industry Data Models**:
- IBM Industry Models: Pre-built logical models for banking, insurance, healthcare, retail
- Oracle Industry Data Models: Vertical-specific models for various industries
- Teradata Industry Logical Data Models: Reference models for financial services, telecom, retail
- HL7 FHIR: Healthcare data interoperability standards and information models
- ACORD: Insurance industry data standards and reference models

**Data Governance Integration**:
- Business Glossary Linkage: Map entities and attributes to business glossary terms
- Data Stewardship: Assign stewards to entities and critical attributes
- Data Classification: Tag entities and attributes with sensitivity levels (PII, PHI, PCI)
- Data Lineage: Logical models as source for technical lineage and impact analysis

**Quality & Documentation Standards**:
- ISO 25012: Data quality model for information systems
- IEEE 1320.2: Conceptual modeling language syntax and semantics
- Data Model Scorecard: Steve Hoberman's framework for evaluating model quality

**Reference**: Consult data architecture teams, DAMA DMBoK Chapter 5, Kimball Group resources, Data Vault Alliance materials, and enterprise modeling tool documentation for detailed guidance

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
