# Api.Architect Agent

## Purpose

An agent that designs comprehensive REST APIs and validates them against best practices. Takes API requirements as input and produces validated OpenAPI specifications with generated data models ready for implementation.

## Skills

This agent uses the following skills:

- `workflow.validate`
- `api.validate`
- `api.define`

## Artifact Flow

### Consumes

- `API requirements`
- `Domain constraints and business rules`

### Produces

- `openapi-spec`
- `api-models`
- `validation-report`

## Example Use Cases

- Design a RESTful API for an e-commerce platform with products, orders, and customers
- Create an API for a task management system with projects, tasks, and user assignments
- Design a multi-tenant SaaS API with proper authentication and authorization

## Usage

```bash
# Activate the agent
/agent api.architect

# Or invoke directly
betty agent run api.architect --input <path>
```

## Created By

This agent was created by **Atum**, the meta-agent that speaks agents into existence.

---

*Part of the Betty Framework*
