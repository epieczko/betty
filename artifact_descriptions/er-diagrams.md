# Name: er-diagrams

## Executive Summary

Entity-Relationship Diagrams are fundamental visual artifacts for data modeling, depicting entities, their attributes, and the relationships between them. These diagrams provide a standardized, graphical representation of database structures that facilitates communication between business stakeholders, data architects, developers, and database administrators.

Created using industry-standard notations including Crow's Foot (IE notation), IDEF1X, Chen notation, UML class diagrams, and Barker notation, ER diagrams leverage tools like Lucidchart, draw.io, dbdiagram.io, ERwin, ER/Studio, MySQL Workbench, and pgModeler. They document cardinality (one-to-one, one-to-many, many-to-many), optionality, identifying vs. non-identifying relationships, and support normalization analysis (1NF, 2NF, 3NF, BCNF) to ensure data integrity and optimal database design across relational and dimensional modeling approaches.

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

This artifact provides visual representation of entity-relationship models using standardized notation systems. It depicts entities, attributes, primary/foreign keys, relationships, cardinality, and constraints in a format that enables database design, communication with stakeholders, normalization analysis, and generation of physical database schemas.

### Scope

**In Scope**:
- Entities (strong, weak, associative)
- Attributes (simple, composite, multivalued, derived)
- Primary keys, candidate keys, foreign keys
- Relationships (one-to-one, one-to-many, many-to-many)
- Cardinality and optionality notation
- Identifying vs. non-identifying relationships
- Relationship participation (total, partial)
- Supertype/subtype (generalization/specialization) hierarchies
- Normalization level indicators
- Conceptual, logical, and physical ER diagrams

**Out of Scope**:
- Physical storage details (tablespaces, file groups)
- Index and partition specifications (documented in physical models)
- ETL data flows (covered by data flow diagrams)
- Application logic and business rules (covered in domain models)
- Real-time event flows (covered by event schemas)

### Target Audience

**Primary Audience**:
- Data Architects designing relational databases
- Database Administrators implementing schemas
- Data Modelers creating logical/physical models
- Backend Developers understanding data structures

**Secondary Audience**:
- Business Analysts validating data requirements
- System Architects reviewing data architecture
- QA Engineers designing data-driven test scenarios
- Technical Writers documenting data structures

## Document Information

**Format**: Multiple

**File Pattern**: `*.er-diagrams.*`

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

**Notation Consistency**:
- **Single Notation**: Use one consistent notation throughout (Crow's Foot recommended for clarity)
- **Legend**: Always include notation legend; don't assume readers know all symbols
- **Standard Symbols**: Use standard shapes (rectangles for entities, diamonds for relationships in Chen notation)
- **Color Coding**: Apply consistent color schemes (e.g., blue for entities, green for relationships)

**Entity Design**:
- **Meaningful Names**: Use clear, business-meaningful entity names (Customer, not CUST_TBL)
- **Singular Naming**: Name entities in singular form (Customer, not Customers)
- **Strong vs Weak**: Clearly distinguish weak entities with double borders or notation
- **Unique Identifiers**: Always identify primary keys; mark with PK prefix or underline
- **Natural Keys**: Document natural business keys even when using surrogate keys

**Relationship Modeling**:
- **Resolve Many-to-Many**: Always resolve M:N relationships with associative entities
- **Cardinality Accuracy**: Verify cardinality with business stakeholders; incorrect cardinality causes data integrity issues
- **Relationship Names**: Name relationships with verb phrases (Customer places Order)
- **Recursive Relationships**: Clearly label recursive relationship roles (Employee manages Employee: Manager/Subordinate)
- **Identifying Relationships**: Use identifying relationships only when child cannot exist without parent

**Attribute Management**:
- **Atomic Attributes**: Ensure all attributes are atomic (1NF); break composite attributes into components
- **Derived Attributes**: Mark calculated/derived attributes; consider whether to store or calculate
- **Multivalued Attributes**: Model multivalued attributes as separate entities
- **Mandatory vs Optional**: Clearly indicate nullable attributes (NULL vs NOT NULL)
- **Domain Constraints**: Document allowed value ranges, formats, and constraints

**Normalization**:
- **Start Normalized**: Begin with fully normalized model (3NF/BCNF)
- **Denormalize Consciously**: Denormalize only for proven performance needs; document justification
- **Eliminate Redundancy**: Remove duplicate data; ensure each fact stored in one place
- **Functional Dependencies**: Document functional dependencies that drove normalization decisions

**Hierarchy Modeling**:
- **Supertype/Subtype**: Use supertype/subtype for "is-a" relationships (Vehicle → Car, Truck)
- **Inheritance Rules**: Specify complete/incomplete and overlapping/disjoint constraints
- **Discriminator Attributes**: Include discriminator to identify subtype membership

**Diagram Organization**:
- **Subject Areas**: Organize complex models into subject area diagrams
- **Layered Views**: Create conceptual, logical, and physical diagram layers
- **Manageable Scope**: Limit entities per diagram (7-15 for readability)
- **Cross-References**: Use connector symbols when entities span multiple diagram pages

**Documentation**:
- **Entity Definitions**: Document business purpose of each entity
- **Attribute Definitions**: Provide business definitions for all attributes
- **Relationship Business Rules**: Explain business rules governing relationships
- **Assumptions**: Document modeling assumptions and decisions

**Tool Usage**:
- **Version Control**: Store diagrams in version control; use text-based formats when possible (dbml, PlantUML)
- **Metadata Repository**: Maintain diagrams in enterprise data modeling tools with metadata repositories
- **Forward/Reverse Engineering**: Keep diagrams synchronized with physical databases
- **Export Formats**: Export to multiple formats (PNG for documentation, SQL DDL for implementation)

**Review & Validation**:
- **Business Validation**: Review with business stakeholders to verify entity/relationship correctness
- **Technical Review**: Have senior data architects review normalization and design patterns
- **Cross-Check**: Validate that ER diagram matches data dictionary and requirements
- **Sample Data**: Test model with realistic sample data scenarios

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

**ER Modeling Notations**:
- Crow's Foot notation (Information Engineering style) - most popular
- IDEF1X (Integration Definition for Information Modeling) - US Federal standard
- Chen notation - original ER diagram notation
- UML 2.5 Class Diagrams - object-oriented approach
- Barker notation - Oracle methodology
- Martin notation (IE notation variant)

**Cardinality Notation**:
- One-to-One (1:1) - single instance relationships
- One-to-Many (1:N) - parent-child hierarchies
- Many-to-Many (M:N) - requires associative/junction entity
- Zero or One (0..1) - optional single instance
- Zero or Many (0..*) - optional multiple instances
- One or Many (1..*) - mandatory multiple instances

**Entity Types**:
- Strong entities (independent existence)
- Weak entities (existence dependent on strong entity)
- Associative entities (resolving M:N relationships)
- Supertype/subtype entities (generalization hierarchies)

**Relationship Types**:
- Identifying relationships (weak entity depends on strong entity)
- Non-identifying relationships (independent entities)
- Recursive relationships (entity relates to itself)
- Ternary relationships (three entities)
- Exclusive relationships (OR conditions)

**Normalization Forms**:
- First Normal Form (1NF): Atomic values, no repeating groups
- Second Normal Form (2NF): No partial dependencies on composite keys
- Third Normal Form (3NF): No transitive dependencies
- Boyce-Codd Normal Form (BCNF): Stricter 3NF
- Fourth Normal Form (4NF): No multivalued dependencies
- Fifth Normal Form (5NF): No join dependencies

**Codd's Rules for Relational Databases**:
- Entity integrity (primary keys)
- Referential integrity (foreign keys)
- Domain integrity (data type constraints)

**ER Diagram Tools**:
- Online: Lucidchart, draw.io (diagrams.net), dbdiagram.io, SqlDBM, Creately
- Desktop: ERwin Data Modeler, ER/Studio, MySQL Workbench, pgAdmin, pgModeler
- Enterprise: Oracle SQL Developer Data Modeler, IBM InfoSphere, PowerDesigner (SAP)
- Open Source: DBeaver, DbSchema, SchemaSpy

**Database Design Patterns**:
- Star schema (dimensional modeling)
- Snowflake schema (normalized dimensions)
- Galaxy schema (multiple fact tables)
- Slowly Changing Dimensions (SCD Type 1, 2, 3, 4, 6)
- Bridge tables for many-to-many
- Hierarchy modeling (adjacency list, nested set, path enumeration)

**Standards & Methodologies**:
- ISO/IEC 11179 Metadata Registries
- ANSI/SPARC three-schema architecture (external, conceptual, internal)
- Information Engineering (IE) methodology
- Relational Model (Codd 1970)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application. Refer to "Database Design for Mere Mortals" by Michael Hernandez and "SQL and Relational Theory" by C.J. Date.

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
