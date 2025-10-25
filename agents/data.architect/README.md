# Data.Architect Agent

## Purpose

Create comprehensive data architecture and governance artifacts including data models, schema definitions, data flow diagrams, data dictionaries, data governance policies, and data quality frameworks. Applies data management best practices (DMBOK, DAMA) and ensures artifacts support data-driven decision making, compliance, and analytics initiatives.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `Business requirements or use cases`
- `Data sources and systems`
- `Data domains or subject areas`
- `Compliance requirements`
- `Data quality expectations`
- `Analytics or reporting needs`

### Produces

- `data-model: Logical and physical data models with entities, relationships, and attributes`
- `schema-definition: Database schemas with tables, columns, constraints, and indexes`
- `data-flow-diagram: Data flow between systems with transformations and quality checks`
- `data-dictionary: Comprehensive data dictionary with business definitions`
- `data-governance-policy: Data governance framework with roles, policies, and procedures`
- `data-quality-framework: Data quality measurement and monitoring framework`
- `master-data-management-plan: MDM strategy for critical data domains`
- `data-lineage-diagram: End-to-end data lineage with source-to-target mappings`
- `data-catalog: Enterprise data catalog with metadata and discovery`

## Example Use Cases

- Entities: Customer, Account, Contact, Interaction, Order, SupportTicket, Product
- Relationships and cardinality
- Attributes with data types and constraints
- Integration patterns for source systems
- Master data management approach
- Data quality rules
- Data governance organization and roles (CDO, data stewards, owners)
- Data classification and handling policies
- Data quality standards and SLAs
- Metadata management standards
- GDPR compliance procedures (consent, right to erasure)
- SOX data retention and audit requirements
- Data access control policies
- data-flow-diagram.yaml showing systems, transformations, quality gates
- data-lineage-diagram.yaml with source-to-target mappings
- data-quality-framework.yaml with validation rules and monitoring

## Usage

```bash
# Activate the agent
/agent data.architect

# Or invoke directly
betty agent run data.architect --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
