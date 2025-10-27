# Name: database.postgres

# Purpose:
Design and implement PostgreSQL database schemas, migrations, and integrations. Creates normalized schemas, indexes, constraints, and connection configurations. Follows PostgreSQL best practices for performance and data integrity.

# Inputs:
- data-model
- performance-requirements
- scaling-requirements

# Outputs:
- database-schema (SQL DDL)
- migration-scripts
- connection-configuration
- index-strategy

# Dependencies:
- PostgreSQL 14+
- Migration tool (Flyway, Liquibase, or Alembic)

# Constraints:
- Follow database normalization principles
- Include proper indexing strategy
- Implement foreign key constraints
- Design for scalability and performance

# Examples:
- Generate PostgreSQL schema from data model
- Create migration scripts for schema evolution
- Design indexes for query optimization
