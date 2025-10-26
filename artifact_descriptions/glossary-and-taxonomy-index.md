# Name: glossary-and-taxonomy-index

## Executive Summary

The Glossary and Taxonomy Index provides a centralized, authoritative index of business glossaries, data dictionaries, taxonomy structures, and controlled vocabularies managed through data governance platforms like Collibra, Alation, Apache Atlas, and Informatica. This artifact establishes the metadata foundation for data governance, enabling consistent data definitions, semantic understanding, and regulatory compliance across analytics, AI/ML, and data sharing initiatives.

Data governance programs fail when organizations lack consensus on fundamental data definitions. The glossary and taxonomy index solves this by maintaining authoritative business definitions (what is a "customer," "revenue," "active user"), hierarchical taxonomies (product categories, geographic regions, organizational structure), and controlled vocabularies that ensure consistent data usage across systems. This artifact integrates with data catalogs, lineage tools, and governance platforms to provide self-service access to approved terminology.

### Strategic Importance

- **Data Governance Foundation**: Establishes authoritative business glossary and taxonomy structure for enterprise data governance programs
- **Regulatory Compliance**: Supports GDPR Article 30 records of processing, BCBS 239 data aggregation, and regulatory reporting requirements
- **Semantic Interoperability**: Enables consistent data interpretation across business units, systems, and analytics initiatives
- **AI/ML Trust**: Provides ground truth definitions for training data, model features, and prediction outputs (model transparency)
- **Data Catalog Integration**: Powers search, discovery, and lineage capabilities in data catalog platforms (Collibra, Alation, Atlas)
- **Cross-Functional Alignment**: Resolves definitional conflicts between finance, sales, product, and engineering teams
- **Knowledge Preservation**: Captures institutional knowledge about data definitions before key personnel depart

## Purpose & Scope

### Primary Purpose

This artifact serves as the master index to enterprise business glossaries, data dictionaries, and taxonomy hierarchies, providing a single source of truth for data definitions across the organization. It documents where authoritative terminology is maintained, how to access it, governance approval processes, and integration points with data catalog and lineage tools.

### Scope

**In Scope**:
- Business glossary definitions (customer, product, revenue, active user, churn, conversion)
- Data dictionary schemas (table definitions, column metadata, data types, constraints)
- Taxonomy hierarchies (product categories, geographic regions, cost centers, data classifications)
- Controlled vocabularies (status codes, country codes, currency codes, data sensitivity labels)
- Data governance platform configuration (Collibra, Alation, Apache Atlas, Informatica EDC)
- Metadata standards (ISO 25964 thesaurus, SKOS ontologies, Dublin Core metadata)
- Term approval workflows (business ownership, stewardship review, governance council approval)
- Data lineage integration (glossary term to database column mappings)
- Semantic reconciliation (resolving conflicts between business unit definitions)

**Out of Scope**:
- Physical data models and database schemas (maintained in data architecture documentation)
- API documentation and field definitions (owned by product and engineering teams)
- Code-level variable naming conventions (covered in software development standards)
- Customer-facing terminology and product copy (managed by product marketing)
- Industry-specific ontologies without business adoption (nice-to-have, not governance-critical)
- Historical deprecated terminology (archived separately from active glossary)

### Target Audience

**Primary Audience**:
- Data Governance Teams: Maintain authoritative glossary, approve new terms, resolve definitional conflicts
- Data Stewards: Own business glossary terms for their domain (finance, sales, product, operations)
- Analytics Engineers: Use glossary definitions to ensure consistent metric calculations

**Secondary Audience**:
- Compliance Officers: Reference glossary for GDPR processing records and regulatory reporting
- Data Scientists: Understand authoritative feature definitions for ML model development
- Business Analysts: Self-service access to approved data definitions and taxonomy structures

## Document Information

**Format**: Markdown

**File Pattern**: `*.glossary-and-taxonomy-index.md`

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

**Single Source of Truth**: Designate one data governance platform (Collibra, Alation, Atlas) as authoritative glossary source; avoid duplicate term management
**Business-First Definitions**: Write glossary definitions from business perspective before technical; avoid jargon (bad: "FK to dim_customer," good: "unique customer identifier")
**Data Steward Ownership**: Assign explicit data steward to each glossary term with accountability for definition accuracy and currency
**Plain Language Standard**: Write definitions at 8th-grade reading level; business users should understand without technical background
**Usage Examples**: Include concrete examples in glossary entries (e.g., "Revenue" definition includes "Recognized when invoice is paid, not when contract is signed")
**Synonym Mapping**: Capture regional and departmental synonyms ("customer" vs "account" vs "client") to improve discoverability
**Hierarchical Taxonomies**: Build parent-child relationships (Product > Product Line > Product Family > SKU) for navigation
**Crowdsourced Contributions**: Allow business users to propose new glossary terms with governance approval workflow
**Automated Lineage**: Link glossary terms to database columns, BI reports, and ML features for impact analysis
**Quarterly Review Cadence**: Review high-use glossary terms quarterly to ensure definitions remain current
**Deprecation Process**: Mark obsolete terms as deprecated rather than deleting; maintain historical context
**Cross-Platform Sync**: If using multiple tools, automate glossary synchronization (Collibra ↔ dbt ↔ Snowflake)
**Search Optimization**: Tag glossary terms with keywords, acronyms, and common misspellings for findability
**Related Terms Network**: Build semantic relationships between glossary terms (e.g., "Churn" related to "Retention," "Customer Lifetime Value")
**Data Classification Integration**: Tag glossary terms with data sensitivity (PII, PHI, confidential) for compliance
**Metrics Calculation Logic**: For calculated metrics (revenue, churn, MAU), document exact calculation formulas in glossary
**Multi-Language Support**: Provide translations for global organizations (English, Spanish, German, French, Mandarin)
**Version History**: Maintain change history for glossary definitions; who changed what, when, and why
**Governance Council Approval**: Require governance council sign-off for contested definitions or cross-functional impacts
**Self-Service Access**: Publish glossary in user-friendly interface accessible to all employees (not just data team)

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

**Data Governance Platforms**:
- Collibra Data Intelligence Cloud (enterprise data governance and business glossary)
- Alation Data Catalog (collaborative data catalog with crowdsourced glossary)
- Apache Atlas (open-source metadata management and data governance)
- Informatica Enterprise Data Catalog (EDC) (automated metadata discovery and glossary)
- Atlan (modern data catalog with active metadata and glossary management)
- data.world (collaborative data catalog and knowledge graph)
- Amundsen (Lyft open-source data discovery and metadata engine)
- DataHub (LinkedIn open-source metadata platform)
- Stemma (data catalog with automated data lineage)

**Business Glossary Standards**:
- ISO 25964: Thesauri and interoperability with other vocabularies
- SKOS (Simple Knowledge Organization System): W3C standard for controlled vocabularies
- Dublin Core Metadata Initiative (DCMI): Metadata element set for resource description
- ANSI/NISO Z39.19: Guidelines for construction, format, and management of monolingual controlled vocabularies
- ISO 11179: Metadata registries (MDR) for semantic standardization

**Data Dictionary & Metadata Standards**:
- ISO 11179-3: Metadata registry metamodel and basic attributes
- DAMA-DMBOK (Data Management Body of Knowledge): Data governance and metadata management
- Common Data Model (CDM): Healthcare data standardization (OMOP CDM, FHIR)
- SDMX (Statistical Data and Metadata Exchange): Statistical data exchange standard
- DDI (Data Documentation Initiative): Social science data documentation

**Taxonomy & Classification Frameworks**:
- UNSPSC (United Nations Standard Products and Services Code): Product and service taxonomy
- NAICS (North American Industry Classification System): Industry taxonomy
- HS Codes (Harmonized System): International trade product classification
- SIC Codes (Standard Industrial Classification): Industry categories
- GICS (Global Industry Classification Standard): Sector/industry taxonomy

**Data Governance Frameworks**:
- DAMA-DMBOK: Data governance, data quality, and metadata management
- DGI Data Governance Framework: Data Governance Institute best practices
- DCAM (Data Management Capability Assessment Model): EDM Council maturity assessment
- COBIT (Control Objectives for Information and Related Technology): IT governance
- TOGAF (The Open Group Architecture Framework): Enterprise architecture

**Regulatory & Compliance**:
- GDPR Article 30: Records of processing activities (requires data inventory and definitions)
- BCBS 239: Principles for effective risk data aggregation (banking data governance)
- SOX (Sarbanes-Oxley): Financial data definitions and controls
- HIPAA: Protected Health Information (PHI) definitions and taxonomies
- FISMA: Federal information security metadata requirements

**Data Classification & Sensitivity**:
- Data Sensitivity Taxonomy: Public, Internal, Confidential, Restricted, Highly Confidential
- PII Classification: Direct identifiers, quasi-identifiers, sensitive attributes
- Data Residency Requirements: US, EU, UK, China, Russia data localization taxonomies
- Information Security Classifications: TLP (Traffic Light Protocol) - White, Green, Amber, Red

**Semantic Web & Ontology Standards**:
- RDF (Resource Description Framework): W3C semantic web standard
- OWL (Web Ontology Language): W3C ontology language
- SPARQL: Query language for RDF data
- JSON-LD: JSON-based linked data format
- schema.org: Structured data vocabulary

**Master Data Management (MDM)**:
- Customer MDM: Golden record customer definitions
- Product MDM: Product hierarchy and taxonomy
- Location MDM: Geographic hierarchies and region definitions
- Financial MDM: Chart of accounts, cost center taxonomies

**Data Quality Dimensions (Taxonomy)**:
- Accuracy: Correctness of data values
- Completeness: Presence of required data elements
- Consistency: Uniform data representation across systems
- Timeliness: Data freshness and currency
- Validity: Conformance to business rules
- Uniqueness: Absence of duplicate records

**Glossary Term Attributes (Metadata)**:
- Business Definition: Plain language explanation
- Technical Definition: System-level implementation
- Data Steward: Accountable owner
- Synonyms: Alternative terms
- Related Terms: Semantic relationships
- Usage Examples: Contextual illustrations
- Data Type: String, integer, decimal, date, boolean
- Valid Values: Enumerated list or range

**Reference**: Consult data governance office, enterprise architecture, and data stewardship teams for detailed guidance on glossary and taxonomy management standards

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
