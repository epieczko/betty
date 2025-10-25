# Data.Validator Agent

## Purpose

Validates data files against schemas, business rules, and data quality standards. Ensures data integrity, completeness, and compliance.

## Skills

This agent uses the following skills:

- `workflow.validate`
- `api.validate`

## Artifact Flow

### Consumes

- `data-file`
- `schema-definition`
- `validation-rules`

### Produces

- `validation-report`
- `data-quality-metrics`
- `data.validatejson`
- `schema.validate`
- `data.profile`
- `Structural: Schema and format validation`
- `Semantic: Business rule validation`
- `Statistical: Data quality profiling`
- `Validation status`
- `List of violations with severity`
- `Data quality score`
- `Statistics`
- `Recommendations for fixing issues`
- `Compliance status with standards`

## Usage

```bash
# Activate the agent
/agent data.validator

# Or invoke directly
betty agent run data.validator --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
