# Name: enterprise-data-model

## Executive Summary

The Enterprise Data Model is a critical artifact for enterprise data architecture, providing conceptual, logical, and physical representations of organizational data assets. This model establishes the canonical data model (CDM), enterprise entities, reference data standards, and master data structures that ensure consistency across all systems and applications.

Built using industry-standard modeling methodologies including DAMA-DMBOK, Data Vault 2.0, dimensional modeling (Kimball), and normalized modeling (Inmon), the Enterprise Data Model leverages tools like ERwin, ER/Studio, IBM InfoSphere Data Architect, Oracle SQL Developer Data Modeler, and open-source solutions like dbdiagram.io. It follows modeling standards such as IDEF1X, Crow's Foot notation, UML class diagrams, and supports Master Data Management (MDM), data governance, and data lineage initiatives across the enterprise.

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

This artifact establishes the authoritative enterprise-wide data model spanning conceptual, logical, and physical layers. It defines canonical enterprise entities, master data structures, reference data standards, and data relationships that ensure consistency, integration, and governance across all organizational data assets.

### Scope

**In Scope**:
- Conceptual data model (high-level business entities and relationships)
- Logical data model (normalized entities, attributes, relationships, keys)
- Physical data model (database-specific schemas, tables, indexes, partitions)
- Canonical Data Model (CDM) for enterprise integration
- Master Data entities (Customer, Product, Location, Employee, etc.)
- Reference data and code tables
- Subject area models and data domains
- Data lineage and traceability
- Naming standards and metadata definitions
- Data quality rules and constraints

**Out of Scope**:
- Application-specific transactional models (covered by application data models)
- Real-time event schemas (covered by event schemas)
- API data contracts (covered by API specifications)
- Unstructured data organization (documents, media)
- Data warehouse ETL processes (covered by data pipeline documentation)

### Target Audience

**Primary Audience**:
- Enterprise Data Architects defining data standards
- Data Architects designing system-specific models
- Data Engineers implementing physical schemas
- MDM Teams managing master data
- Data Governance Teams establishing data policies

**Secondary Audience**:
- Database Administrators optimizing schemas
- BI Analysts understanding data sources
- Application Architects aligning with enterprise standards
- Compliance Teams ensuring data regulatory compliance

## Document Information

**Format**: Markdown

**File Pattern**: `*.enterprise-data-model.md`

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

**Modeling Layer Separation**:
- **Conceptual Models**: Focus on business concepts; keep implementation details out; use for stakeholder communication
- **Logical Models**: Design platform-independent normalized structures; apply 3NF/BCNF; document all constraints
- **Physical Models**: Optimize for specific DBMS; apply indexes, partitions, denormalization where justified by performance

**Master Data Management**:
- **Golden Records**: Establish clear rules for creating golden records from multiple source systems
- **Data Stewardship**: Assign data stewards to each master data domain; document ownership and accountability
- **Unique Identification**: Use enterprise-wide unique identifiers (UUIDs) for master entities
- **Hierarchy Management**: Model product, organizational, and geographic hierarchies with effective dating
- **Reference Data**: Centralize reference data management; version code lists and taxonomies

**Normalization & Design**:
- **Normalize First**: Start with fully normalized logical models (3NF/BCNF); denormalize only with justification
- **Natural Keys**: Document natural business keys even when using surrogate keys
- **Slowly Changing Dimensions**: Model temporal changes using SCD Type 1 (overwrite), Type 2 (history), or Type 3 (limited history)
- **Avoid Over-Normalization**: Balance normalization with practical performance considerations

**Enterprise Integration**:
- **Canonical Data Model**: Maintain CDM as integration layer; map all system-specific models to CDM
- **Subject Areas**: Organize models into logical subject areas (Customer, Product, Finance, etc.)
- **Cross-Reference Tables**: Model system-to-system mappings and data crosswalks
- **Data Lineage**: Document data flow from source systems through transformations to targets

**Naming Standards**:
- **Consistent Nomenclature**: Establish and enforce naming conventions (PascalCase, snake_case, etc.)
- **Abbreviation Registry**: Maintain approved abbreviation list; avoid ambiguous abbreviations
- **Semantic Naming**: Use business-meaningful names; avoid technical jargon
- **Metadata Definitions**: Document business definitions for all entities and attributes

**Data Governance Integration**:
- **Data Ownership**: Tag entities with data owner and data steward
- **Data Classification**: Mark sensitive/PII data; apply appropriate security classifications
- **Data Quality Rules**: Embed validation rules, acceptable value ranges, and constraints
- **Regulatory Compliance**: Model data retention periods, consent management, and privacy requirements

**Tooling & Version Control**:
- **Model Repository**: Use enterprise modeling tools with centralized repositories (ERwin, ER/Studio)
- **Version Control**: Store model definitions in Git; track changes to DDL scripts
- **Model Comparison**: Use diff tools to compare model versions; track structural changes
- **Forward/Reverse Engineering**: Sync models with physical databases; automate DDL generation

**Performance Optimization**:
- **Index Strategy**: Define indexes on foreign keys, frequently queried columns, and composite search keys
- **Partitioning**: Model horizontal/vertical partitions for large tables
- **Archival Strategy**: Design data archival patterns for historical data
- **Denormalization**: Document denormalization decisions with performance justification

**Review & Validation**:
- **Data Architect Review**: Validate adherence to enterprise standards and patterns
- **DBA Review**: Verify physical model optimization and database-specific features
- **Business Stakeholder Review**: Confirm logical model matches business understanding
- **Impact Analysis**: Assess downstream impact before making model changes

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

**Data Management Frameworks**:
- DAMA-DMBOK (Data Management Body of Knowledge) v2
- DCAM (Data Management Capability Assessment Model)
- EDM Council CDMC (Cloud Data Management Capabilities)
- ISO/IEC 38505 (Data Governance framework)
- COBIT Data Governance framework

**Data Modeling Methodologies**:
- Normalized Modeling (Inmon approach, 3NF/BCNF)
- Dimensional Modeling (Kimball star/snowflake schemas)
- Data Vault 2.0 (Hub, Link, Satellite patterns)
- Anchor Modeling (temporal 6NF)
- Conceptual-Logical-Physical (CLP) modeling layers

**Modeling Notations & Standards**:
- IDEF1X (Integration Definition for Information Modeling)
- Crow's Foot notation (also called IE notation)
- UML 2.5 Class Diagrams for data structures
- Barker's notation (Oracle methodology)
- Chen ERD notation
- ISO/IEC 11179 Metadata Registries

**Master Data Management (MDM)**:
- Golden record creation and matching
- Entity resolution and deduplication
- Data stewardship workflows
- Hierarchy management (product, organizational)
- Survivorship rules for attribute prioritization
- MDM styles: Registry, Consolidation, Coexistence, Centralized

**Normalization Theory**:
- First Normal Form (1NF): Atomic values, no repeating groups
- Second Normal Form (2NF): No partial dependencies
- Third Normal Form (3NF): No transitive dependencies
- Boyce-Codd Normal Form (BCNF): Stricter 3NF
- Fourth Normal Form (4NF): Multivalued dependencies
- Fifth Normal Form (5NF): Join dependencies
- Denormalization patterns for performance

**Data Governance**:
- Data domains and data ownership
- Data quality dimensions (accuracy, completeness, consistency, timeliness)
- Metadata management and business glossary
- Data lineage and impact analysis
- Data classification and sensitivity tagging
- Privacy by Design (GDPR, CCPA compliance)

**Data Architecture Patterns**:
- Canonical Data Model (CDM) for enterprise integration
- Operational Data Store (ODS)
- Data Warehouse (DW) dimensional models
- Data Lake (schema-on-read)
- Data Lakehouse (Delta Lake, Apache Iceberg)
- Lambda and Kappa architectures

**Tooling & Platforms**:
- ERwin Data Modeler
- ER/Studio (Idera)
- IBM InfoSphere Data Architect
- Oracle SQL Developer Data Modeler
- PowerDesigner (SAP)
- Hackolade (NoSQL modeling)
- dbdiagram.io, SqlDBM (online tools)
- Informatica MDM, Reltio, Profisee (MDM platforms)

**Data Quality & Profiling**:
- Data profiling standards
- Data quality scorecards
- Validation rules and constraints
- Data quality monitoring

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application. Refer to DAMA-DMBOK for comprehensive data management practices.

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
