# Full-Stack Development Quick Start

## TL;DR

**Question:** Can we use Meta.Agent to create a fullstack-developer agent?

**Answer:** Yes, but NOT the way you showed. Here's the right approach:

### ❌ Wrong: Prescriptive Agent

```yaml
# DON'T create an agent with hardcoded technologies
name: fullstack-developer
system_prompt: |
  Use Express.js for backend
  Use React for frontend
  Use PostgreSQL for database
  # ... 2000 lines of technology-specific code examples ...
```

### ✅ Right: Orchestrator Agent + Technology Skills

```yaml
# DO create a generic orchestrator agent
name: fullstack.developer
description: Orchestrates full-stack development using technology-specific skills
skills_available:
  - api.define
  - backend.*      # User chooses: express, fastapi, rails, etc.
  - frontend.*     # User chooses: react, vue, svelte, etc.
  - database.*     # User chooses: postgres, mongodb, mysql, etc.
  - deployment.*   # User chooses: docker, k8s, vercel, etc.
```

## Why Skills Instead of Hardcoding?

| Aspect | Hardcoded Agent | Skills-Based Agent |
|--------|----------------|-------------------|
| **Flexibility** | Locked to one stack | Mix and match technologies |
| **Reusability** | One agent, one purpose | Skills used across agents |
| **Maintenance** | Update entire agent | Update individual skills |
| **Extensibility** | Rewrite agent | Add new skills |
| **Testing** | Test everything together | Test skills independently |

## Quick Start: Build It The Right Way

### Step 1: Create Technology Skills

```bash
# Backend options
python agents/meta.skill/meta_skill.py skill_descriptions/backend.express.md
python agents/meta.skill/meta_skill.py skill_descriptions/backend.fastapi.md
python agents/meta.skill/meta_skill.py skill_descriptions/backend.django.md

# Frontend options
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.react.md
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.vue.md
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.nextjs.md

# Database options
python agents/meta.skill/meta_skill.py skill_descriptions/database.postgres.md
python agents/meta.skill/meta_skill.py skill_descriptions/database.mongodb.md
```

### Step 2: Create Orchestrator Agent

```bash
# Generic orchestrator that uses the skills
python agents/meta.agent/meta_agent.py agent_descriptions/fullstack.developer.md
```

### Step 3: Use With Any Stack Combination

```bash
# Project 1: React + Express + PostgreSQL
claude: "Use fullstack.developer with backend.express, frontend.react, database.postgres"

# Project 2: Vue + FastAPI + MongoDB
claude: "Use fullstack.developer with backend.fastapi, frontend.vue, database.mongodb"

# Project 3: Next.js (full-stack) + PostgreSQL
claude: "Use fullstack.developer with frontend.nextjs, database.postgres"
```

## Files Created For You

I've created starter files:

### Agent Description
- `agent_descriptions/fullstack.developer.md` - Generic orchestrator agent

### Skill Descriptions
- `skill_descriptions/backend.express.md` - Express.js backend
- `skill_descriptions/backend.fastapi.md` - FastAPI backend
- `skill_descriptions/frontend.react.md` - React frontend
- `skill_descriptions/database.postgres.md` - PostgreSQL database

### Documentation
- `docs/fullstack-development-architecture.md` - Complete architecture guide

## Example: E-commerce Platform

### Traditional Approach (Wrong)
```bash
# Locked into React + Express + PostgreSQL
claude: "Use fullstack-developer to build e-commerce platform"
# Always generates same stack
```

### Betty Approach (Right)
```bash
# Choose your stack
cat > ecommerce-stack.yaml <<EOF
backend: fastapi     # Python instead of Node
frontend: vue        # Vue instead of React
database: mongodb    # NoSQL instead of SQL
EOF

claude: "Use fullstack.developer with ecommerce-stack.yaml"
# Generates FastAPI + Vue + MongoDB
```

### Want to Try Different Stack?
```bash
# Different project, different choices
cat > ecommerce-stack-v2.yaml <<EOF
backend: express
frontend: react
database: postgres
EOF

claude: "Use fullstack.developer with ecommerce-stack-v2.yaml"
# Generates Express + React + PostgreSQL
```

## Implement Skill Handlers

Each skill needs a Python handler:

```python
# skills/backend.fastapi/backend_fastapi.py
def generate_fastapi_app(api_spec, db_schema, auth_config):
    """
    This is where FastAPI-specific code generation happens.

    Inputs:
    - api_spec: OpenAPI specification
    - db_schema: Database schema
    - auth_config: Authentication requirements

    Outputs:
    - FastAPI application code
    - Pydantic models
    - Tests
    - Documentation
    """
    # Parse OpenAPI spec
    routes = parse_openapi(api_spec)

    # Generate Pydantic models
    models = generate_pydantic_models(db_schema)

    # Create FastAPI app
    app_code = create_fastapi_app(routes, models, auth_config)

    # Generate tests
    tests = generate_tests(routes, models)

    return {
        'application': app_code,
        'models': models,
        'tests': tests
    }
```

## Benefits Summary

1. **Technology Freedom**: Choose any stack per project
2. **Skill Reusability**: `backend.fastapi` used by multiple agents
3. **Easy Extension**: Add `backend.actix` for Rust support
4. **Maintainable**: Update Express patterns in one place
5. **Testable**: Test each skill independently

## Architecture Diagram

```
┌─────────────────────────────────────┐
│   fullstack.developer (Agent)      │
│   - Orchestrates workflow           │
│   - Validates architecture          │
│   - Manages integration             │
└───────────────┬─────────────────────┘
                │
        ┌───────┴───────┐
        │               │
┌───────▼──────┐   ┌───▼──────────┐
│ Backend      │   │ Frontend     │
│ Skills       │   │ Skills       │
├──────────────┤   ├──────────────┤
│ • express    │   │ • react      │
│ • fastapi    │   │ • vue        │
│ • django     │   │ • nextjs     │
│ • rails      │   │ • svelte     │
└──────────────┘   └──────────────┘
        │               │
        └───────┬───────┘
                │
    ┌───────────▼────────────┐
    │ Database Skills        │
    ├────────────────────────┤
    │ • postgres             │
    │ • mongodb              │
    │ • mysql                │
    │ • redis                │
    └────────────────────────┘
```

## Next Steps

1. **Review Files**: Check `agent_descriptions/` and `skill_descriptions/`
2. **Generate Skills**: Use meta.skill to create skills
3. **Generate Agent**: Use meta.agent to create orchestrator
4. **Implement Handlers**: Write Python code for each skill
5. **Test**: Build a real project
6. **Iterate**: Add more technology options

## Key Takeaway

> **Agents orchestrate workflows. Skills implement technologies.**
>
> Keep your agents technology-agnostic and delegate implementation to composable, reusable skills.

## Full Documentation

See `docs/fullstack-development-architecture.md` for:
- Complete architecture explanation
- Usage examples
- Implementation phases
- Best practices
- Migration guides

## Questions?

**Q: Can I still use the prescriptive agent approach?**
A: Technically yes, but you'll lose flexibility and reusability. Not recommended.

**Q: How many skills should I create?**
A: Start with your most common stack, then add more as needed.

**Q: Can skills depend on other skills?**
A: Yes! Example: `frontend.react` can use `api.generatemodels` to create TypeScript types.

**Q: What if I need a technology that doesn't have a skill?**
A: Create it with meta.skill! That's the beauty of the system.
