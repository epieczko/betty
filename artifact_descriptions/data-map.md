# Name: data-map

## Executive Summary

A Data Map is a comprehensive inventory and visualization artifact that documents the location, movement, and relationships of data across an organization's entire data landscape—from source systems through integration layers to consumption endpoints. This artifact provides enterprise-wide visibility into data asset distribution, supporting privacy compliance (GDPR Article 30 ROPA, CCPA), data governance, system migration planning, and strategic data architecture decisions.

Data maps encompass system inventories, data store catalogs, cross-system data flows, data element ownership, sensitivity classifications, and geographical data residency. Modern implementations leverage automated discovery tools (Collibra, Alation, Azure Purview, AWS Glue Data Catalog) combined with business context from data stewards to create living documentation aligned with DAMA DMBoK data architecture and metadata management practices, supporting Data Mesh domain-oriented data ownership and Data Fabric distributed data management architectures.

### Strategic Importance

- **Privacy Compliance**: Enables GDPR Article 30 Records of Processing Activities (ROPA) and CCPA data inventory requirements
- **Data Governance Foundation**: Establishes enterprise data asset inventory for governance policy application and stewardship assignment
- **Migration & Modernization**: Supports cloud migration, system consolidation, and legacy system retirement planning
- **Data Sovereignty**: Documents data residency and cross-border data flows for regulatory compliance (GDPR, data localization laws)
- **Risk Management**: Identifies data sprawl, shadow IT data stores, and unmanaged data repositories
- **Cost Optimization**: Reveals redundant data storage, duplicate systems, and opportunities for consolidation
- **Strategic Planning**: Provides enterprise data landscape visibility for data strategy and architecture roadmapping

## Purpose & Scope

### Primary Purpose

This artifact provides a comprehensive enterprise-level inventory of all data storage locations, data movement patterns, data ownership assignments, sensitivity classifications, and geographical data residency across the organization's data ecosystem to support governance, compliance, and strategic decision-making.

### Scope

**In Scope**:
- Inventory of all data stores (databases, data warehouses, data lakes, SaaS applications, file shares, data marts)
- Database catalog with RDBMS (Oracle, SQL Server, PostgreSQL, MySQL), NoSQL (MongoDB, Cassandra, DynamoDB), and cloud data warehouses (Snowflake, Redshift, BigQuery, Synapse)
- Data lake/lakehouse inventory (S3, ADLS, GCS) with storage layer organization (bronze/silver/gold, raw/curated/trusted)
- SaaS application data inventory (Salesforce, Workday, ServiceNow, SAP, Netsuite)
- Streaming platforms (Kafka clusters, Kinesis streams, Event Hubs, Pub/Sub topics)
- BI and analytics platforms (Tableau Server, Power BI workspaces, Looker instances, Qlik environments)
- Data sensitivity classification (PII, PHI, PCI, confidential, internal, public) per GDPR/CCPA requirements
- Data steward and data owner assignments for all data assets
- Geographical data residency and cross-border data flow documentation
- System-to-system data integration patterns and data exchange mechanisms
- Data retention policies and archival locations
- Cloud region and availability zone mapping for data assets
- Third-party data sharing and vendor data exchange documentation

**Out of Scope**:
- Detailed schema definitions and data element specifications (covered by data-dictionaries artifact)
- Transformation logic and pipeline implementation details (covered by data-lineage-maps artifact)
- Data quality metrics and monitoring (covered by data quality reports)
- Access control lists and user permissions (documented in security artifacts)
- Application architecture and business process flows (covered by application architecture diagrams)

### Target Audience

**Primary Audience**:
- Data Architects: Maintain enterprise data landscape and plan strategic data architecture initiatives
- Data Governance Officers: Oversee data asset inventory, policy compliance, and stewardship assignments
- Privacy Officers: Document personal data processing for GDPR ROPA and CCPA compliance requirements
- Enterprise Architects: Understand data distribution across technology portfolio for strategic planning

**Secondary Audience**:
- Cloud Migration Teams: Assess current state data landscape for migration planning and prioritization
- Compliance Auditors: Verify data inventory completeness for regulatory audits (SOX, GDPR, industry-specific)
- Security Teams: Identify data repositories requiring security controls and monitoring
- Business Analysts: Locate authoritative data sources for reporting and analytics initiatives

## Document Information

**Format**: Multiple

**File Pattern**: `*.data-map.*`

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

**Automated Discovery**: Use data catalog tools (Collibra, Alation, Azure Purview, AWS Glue) with automated scanning to discover and inventory data assets continuously
**CMDB Integration**: Integrate data map with Configuration Management Database (ServiceNow CMDB, BMC Remedy) for unified IT asset inventory
**Cloud Provider APIs**: Leverage cloud provider APIs (AWS Config, Azure Resource Graph, GCP Asset Inventory) to automatically catalog cloud data resources
**Network Scanning**: Deploy network discovery tools to identify shadow IT databases and unmanaged data stores
**Data Classification Automation**: Use AI-powered classification tools (Microsoft Purview, BigID, OneTrust) to automatically classify data sensitivity
**GDPR ROPA Alignment**: Structure data map to directly support Article 30 ROPA requirements including purpose, legal basis, and retention
**Data Residency Mapping**: Document cloud region, availability zone, and data center location for all data assets to support data sovereignty requirements
**Ownership Assignment**: Assign business data owner and technical data custodian for every data asset with contact information
**Quarterly Validation**: Schedule quarterly data map validation campaigns with data stewards to verify accuracy and completeness
**Decommissioning Tracking**: Maintain separate inventory of decommissioned systems with retention and destruction timelines
**Cost Tag Integration**: Include cloud cost tags and FinOps metadata to enable data storage cost analysis and optimization
**API & Integration Documentation**: Document all APIs, file transfers, and integration patterns connecting data systems
**Vendor Data Mapping**: Inventory third-party vendor data sharing agreements and cross-organizational data flows
**Data Domain Organization**: Structure data map by business domains aligned with Data Mesh principles for scalability
**Visualization Layers**: Create multiple views (technical, business, compliance, geographical) for different stakeholder audiences
**Risk Scoring**: Apply data risk scores based on sensitivity, criticality, and exposure to prioritize governance attention
**Change Management Integration**: Update data map automatically when new systems are provisioned via IaC (Terraform, CloudFormation)
**Metadata Completeness KPIs**: Track percentage of data assets with complete metadata (owner, classification, retention, location)

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

**Privacy & Compliance Regulations**:
- GDPR Article 30: Records of Processing Activities (ROPA) requiring comprehensive data inventory
- CCPA: California Consumer Privacy Act data inventory and mapping requirements
- LGPD (Brazil): Lei Geral de Proteção de Dados personal data processing records
- PIPEDA (Canada): Personal Information Protection and Electronic Documents Act data inventory
- APPI (Japan): Act on Protection of Personal Information data flow documentation
- Data Localization Laws: Russia, China, India requirements for in-country data storage mapping

**Data Governance Frameworks**:
- DAMA DMBoK Chapter 3: Data Architecture and data landscape documentation
- DAMA DMBoK Chapter 12: Metadata Management including data asset inventories
- DCAM (Data Management Capability Assessment Model): Data architecture and metadata capabilities
- EDM Council DCAM: Financial services data landscape and critical data elements
- DGI Data Governance Framework: Data inventory and classification as governance foundation

**Data Discovery & Cataloging Tools**:
- Collibra Data Intelligence Platform: Enterprise data catalog with automated asset discovery
- Alation Data Catalog: Collaborative cataloging with behavioral metadata and search
- Azure Purview: Microsoft unified data governance with automated scanning across Azure, on-prem, multi-cloud
- AWS Glue Data Catalog: Serverless metadata repository with crawler-based discovery
- Google Cloud Data Catalog: Managed metadata service with auto-tagging and classification
- Informatica Enterprise Data Catalog: AI-powered discovery across on-premise and cloud
- BigID: Data discovery and classification platform for privacy compliance
- OneTrust: Privacy management platform with data mapping and ROPA automation

**Data Classification & Privacy Tools**:
- Microsoft Purview Information Protection: Automated data classification and sensitivity labeling
- Varonis Data Classification Engine: Content-aware classification for structured and unstructured data
- Spirion (formerly Identity Finder): Sensitive data discovery across endpoints, file shares, databases
- Ground Labs Enterprise Recon: Data discovery for PII, PCI, PHI across diverse environments
- BigID: Privacy-centric data discovery with GDPR/CCPA compliance mapping

**Asset Management & CMDB**:
- ServiceNow CMDB: Configuration management database for IT asset inventory integration
- BMC Remedy CMDB: Enterprise configuration management for federated asset data
- Device42: Auto-discovery and CMDB for data center and cloud infrastructure mapping
- Flexera: IT asset management with software and hardware inventory integration

**Cloud Resource Discovery**:
- AWS Config: Configuration tracking and resource inventory for AWS accounts
- Azure Resource Graph: Query and explore Azure resources at scale
- GCP Cloud Asset Inventory: Real-time visibility into GCP resource metadata
- CloudHealth by VMware: Multi-cloud asset inventory and cost allocation
- Cloudability: Cloud cost management with resource inventory and tagging

**Data Architecture Patterns**:
- Data Mesh: Domain-oriented decentralized data ownership requiring domain data catalogs
- Data Fabric: Distributed data architecture with unified metadata and cataloging layer
- Data Lakehouse: Medallion architecture (bronze/silver/gold) data organization patterns
- Lambda Architecture: Speed/batch layer data storage mapping
- Kappa Architecture: Unified stream processing data topology mapping

**Industry-Specific Standards**:
- BCBS 239: Banking risk data aggregation requiring data inventory and lineage
- HIPAA: Healthcare data inventory and access controls for PHI
- PCI DSS: Payment card data inventory and segmentation requirements
- SOX Section 404: Financial data controls requiring system inventory
- FISMA: Federal information security requiring asset categorization
- NIST Cybersecurity Framework: Asset management and inventory requirements

**Metadata Standards**:
- ISO 11179: Metadata registries for data asset documentation
- Dublin Core: Metadata element set for resource description
- PROV-DM (W3C): Provenance data model for data origin tracking
- DCAT (W3C): Data Catalog Vocabulary for publishing catalogs

**Reference**: Consult privacy, compliance, and data governance teams for jurisdiction-specific requirements and tool selection aligned with your regulatory obligations and technology landscape

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
