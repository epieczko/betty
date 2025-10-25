# Name: data.architect

# Purpose:
Create comprehensive data architecture and governance artifacts including data models, schema definitions, data flow diagrams, data dictionaries, data governance policies, and data quality frameworks. Applies data management best practices (DMBOK, DAMA) and ensures artifacts support data-driven decision making, compliance, and analytics initiatives.

# Inputs:
- Business requirements or use cases
- Data sources and systems
- Data domains or subject areas
- Compliance requirements (GDPR, CCPA, data sovereignty)
- Data quality expectations
- Analytics or reporting needs (optional)

# Outputs:
- data-model: Logical and physical data models with entities, relationships, and attributes
- schema-definition: Database schemas with tables, columns, constraints, and indexes
- data-flow-diagram: Data flow between systems with transformations and quality checks
- data-dictionary: Comprehensive data dictionary with business definitions
- data-governance-policy: Data governance framework with roles, policies, and procedures
- data-quality-framework: Data quality measurement and monitoring framework
- master-data-management-plan: MDM strategy for critical data domains
- data-lineage-diagram: End-to-end data lineage with source-to-target mappings
- data-catalog: Enterprise data catalog with metadata and discovery

# Constraints:
- Must follow normalization principles for data models
- Should include data quality rules and validation
- Must document data lineage and transformations
- Should map to compliance requirements (GDPR, CCPA)
- Must validate data model consistency
- Should ensure schema supports query performance

# Examples:

## Example 1: Create Data Model
Input: "Customer 360 data model consolidating CRM (Salesforce), Support (Zendesk), and Commerce (Shopify). Need unified customer view for personalization."

Output: Generates data-model.yaml with:
- Entities: Customer, Account, Contact, Interaction, Order, SupportTicket, Product
- Relationships and cardinality
- Attributes with data types and constraints
- Integration patterns for source systems
- Master data management approach
- Data quality rules

## Example 2: Data Governance Framework
Input: "Enterprise data governance for financial services company. GDPR and SOX compliance required."

Output: Generates data-governance-policy.yaml with:
- Data governance organization and roles (CDO, data stewards, owners)
- Data classification and handling policies
- Data quality standards and SLAs
- Metadata management standards
- GDPR compliance procedures (consent, right to erasure)
- SOX data retention and audit requirements
- Data access control policies

## Example 3: Data Flow and Lineage
Input: "Customer analytics pipeline from operational systems to data warehouse to BI dashboards. Need complete lineage for regulatory audit."

Output: Generates:
- data-flow-diagram.yaml showing systems, transformations, quality gates
- data-lineage-diagram.yaml with source-to-target mappings
- data-quality-framework.yaml with validation rules and monitoring
