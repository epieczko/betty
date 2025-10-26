# Name: dataset-documentation

## Executive Summary

Dataset Documentation provides comprehensive metadata and contextual information about datasets, following industry standards including Datasheets for Datasets (Microsoft), Data Nutrition Labels (MIT), and dataset metadata schemas (DCAT, Schema.org). This artifact enables data discovery, quality assessment, appropriate usage, regulatory compliance, and responsible data practices through systematic documentation of dataset characteristics, collection methodology, known limitations, and ethical considerations.

Modern dataset documentation integrates with data catalogs like DataHub, Amundsen, OpenMetadata, and Apache Atlas to provide searchable, version-controlled dataset metadata with automated lineage tracking. By documenting data sources, collection procedures, data quality metrics, sensitive attributes, bias considerations, and usage restrictions, this artifact supports data governance, GDPR compliance, informed model training decisions, and cross-functional collaboration between data engineers, data scientists, legal teams, and business stakeholders.

### Strategic Importance

- **Data Discoverability**: Enables efficient discovery of datasets through rich metadata in data catalogs
- **Informed Usage**: Ensures appropriate dataset usage through documentation of limitations and intended use cases
- **Data Quality**: Establishes quality expectations through documented completeness, accuracy, and freshness metrics
- **Regulatory Compliance**: Satisfies GDPR data inventory, CCPA consumer rights, and sector-specific requirements
- **Responsible Data Practices**: Addresses privacy, fairness, and ethical data collection considerations
- **Reproducibility**: Enables reproducible research and model training through versioned dataset snapshots
- **Risk Mitigation**: Documents data risks, biases, and limitations to prevent misuse

## Purpose & Scope

### Primary Purpose

This artifact serves as comprehensive metadata documentation for datasets, enabling discovery, assessment, appropriate usage, quality validation, and regulatory compliance. It provides essential context about data sources, collection methodology, quality characteristics, limitations, and ethical considerations necessary for informed data usage decisions.

### Scope

**In Scope**:
- Dataset overview including name, description, purpose, and business context
- Data source information with system of origin, collection methodology, and update frequency
- Schema documentation with field names, data types, constraints, and relationships
- Data quality metrics including completeness, accuracy, consistency, and timeliness
- Statistical summaries with distribution statistics, null rates, and cardinality
- Sample data and example records (where privacy-safe)
- Data lineage with upstream sources and transformation logic
- Access controls and data classification (PII, confidential, public)
- Usage guidelines including intended use cases and known limitations
- Privacy considerations with sensitive attributes and de-identification methods
- Bias assessment documenting known biases and representation gaps
- Version history with dataset versioning and snapshot management
- Refresh schedule and staleness indicators
- Data ownership with steward, owner, and contact information
- Regulatory metadata for GDPR, CCPA, HIPAA compliance
- Known issues and caveats with workarounds or mitigation strategies
- Related datasets and dependencies
- Retention policies and archival procedures

**Out of Scope**:
- Actual dataset contents (reference data storage location instead)
- Data processing code and ETL pipelines (reference code repositories)
- Model documentation (covered in model documentation artifact)
- General data governance policies (reference organization policies)
- Specific analytical insights derived from the data
- Business intelligence reports and dashboards
- Real-time data monitoring and alerting (operational concern)

### Target Audience

**Primary Audience**:
- Data scientists selecting datasets for analysis and model training
- Data engineers building data pipelines and integrations
- Analytics engineers creating data transformations and marts
- Data consumers evaluating dataset fitness for purpose

**Secondary Audience**:
- Data stewards managing data quality and governance
- Privacy officers assessing data privacy compliance
- Legal teams evaluating data usage restrictions
- Compliance teams ensuring regulatory adherence
- Business stakeholders understanding data availability
- External researchers or partners accessing shared datasets

## Document Information

**Format**: Markdown

**File Pattern**: `*.dataset-documentation.md`

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

**Dataset Documentation Standards**:
- Datasheets for Datasets (Microsoft): Comprehensive dataset documentation framework
- Data Nutrition Labels (MIT): Dataset health and transparency labels
- Dataset Documentation (Hugging Face): ML dataset cards and documentation
- OpenML Dataset Metadata: Machine learning dataset descriptions
- Croissant (MLCommons): ML-ready dataset metadata format

**Metadata Standards**:
- DCAT (Data Catalog Vocabulary): W3C standard for dataset catalogs
- Schema.org Dataset: Structured data markup for datasets
- Dublin Core Metadata Terms: Cross-domain resource description
- ISO 19115: Geographic information metadata standards
- DDI (Data Documentation Initiative): Social science data documentation
- PROV-O: W3C provenance ontology for data lineage

**Data Catalogs & Discovery**:
- DataHub (LinkedIn): Open-source metadata platform with data discovery
- Amundsen (Lyft): Data discovery and metadata engine
- OpenMetadata: Open-source metadata platform for data teams
- Apache Atlas: Data governance and metadata management
- Alation: Enterprise data catalog with collaborative features
- Collibra: Data intelligence and governance platform
- Google Data Catalog: GCP-native metadata management
- AWS Glue Data Catalog: AWS metadata repository

**Data Quality Frameworks**:
- DAMA-DMBOK: Data Management Body of Knowledge
- ISO 8000: Data quality standards
- DCAM (Data Management Capability Assessment Model): EDM Council framework
- Great Expectations: Data validation and documentation
- Soda Core: Data quality testing and monitoring
- deequ (Amazon): Data quality validation library

**Data Governance & Compliance**:
- GDPR (General Data Protection Regulation): EU data privacy requirements
- CCPA (California Consumer Privacy Act): California privacy law
- HIPAA: Healthcare data protection standards
- SOX (Sarbanes-Oxley): Financial data controls
- BCBS 239: Banking data risk principles
- ISO 27001: Information security management

**Data Lineage & Provenance**:
- OpenLineage: Open standard for data lineage collection
- PROV-DM (W3C): Provenance data model
- Marquez (OpenLineage): Metadata service for lineage tracking
- Spline (Apache): Data lineage tracking for Spark
- Egeria (ODPi): Open metadata and governance framework

**Privacy & De-identification**:
- k-anonymity / l-diversity / t-closeness: Privacy models
- Differential Privacy: Privacy-preserving data analysis
- NIST Privacy Framework: Privacy risk management
- ISO 29100: Privacy framework standards
- Anonymization techniques: Generalization, suppression, perturbation

**Data Versioning & Reproducibility**:
- DVC (Data Version Control): Git-like versioning for data
- LakeFS: Git-like version control for data lakes
- Pachyderm: Data versioning and pipelines
- Delta Lake: ACID transactions and versioning for data lakes
- Apache Iceberg: Table format with snapshot isolation

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

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
