# Name: data.validator

# Purpose:
Validates data files against schemas, business rules, and data quality standards.
Ensures data integrity, completeness, and compliance.

# Inputs:
- data-file
- schema-definition (optional)
- validation-rules (optional)

# Outputs:
- validation-report
- data-quality-metrics

# Skills Needed:
- data.validatejson
- schema.validate
- data.profile

# Implementation Notes:
The agent should validate:
1. Schema compliance (JSON Schema, XML Schema, etc.)
2. Data types and formats
3. Required fields and constraints
4. Business rules (custom validations)
5. Data quality metrics (completeness, accuracy, consistency)
6. Referential integrity
7. Data range and boundary conditions

Validation types:
- Structural: Schema and format validation
- Semantic: Business rule validation
- Statistical: Data quality profiling

Output should include:
- Validation status (pass/fail)
- List of violations with severity
- Data quality score
- Statistics (null rates, unique values, distributions)
- Recommendations for fixing issues
- Compliance status with standards (GDPR, HIPAA, etc.)

Should support multiple data formats: JSON, CSV, XML, Parquet, Avro
