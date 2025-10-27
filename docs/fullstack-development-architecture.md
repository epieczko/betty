# Full-Stack Development Architecture in Betty

## Overview

This document explains how to build a **technology-agnostic full-stack development system** in Betty using the agent-skill composition pattern.

## Architecture Philosophy

### ❌ Anti-Pattern: Technology-Prescriptive Agents

```yaml
# DON'T DO THIS
name: fullstack-developer
description: |
  Uses Express.js for backend, React for frontend, PostgreSQL for database...

  ### Backend with Express.js
  ```typescript
  import express from 'express';
  // 500 lines of Express-specific code...
  ```
```

**Problems:**
- Hardcodes technology choices
- Not reusable for different stacks
- Difficult to maintain and update
- Violates separation of concerns

### ✅ Correct Pattern: Orchestrator + Technology Skills

```yaml
# Agent: High-level orchestration
name: fullstack.developer
description: Orchestrates full-stack development using technology-specific skills
skills_available:
  - api.define           # Define API contracts
  - backend.*            # Technology-specific backend (user chooses)
  - frontend.*           # Technology-specific frontend (user chooses)
  - database.*           # Technology-specific database (user chooses)
  - deployment.*         # Technology-specific deployment (user chooses)
```

**Benefits:**
- Mix and match technologies per project
- Skills are reusable across agents
- Easy to add new technologies
- Clear separation of concerns

## Component Architecture

### Layer 1: Orchestrator Agent

**Role:** Workflow coordination, architecture decisions, integration planning

```
fullstack.developer (agent)
├─ Analyzes requirements
├─ Recommends architecture patterns
├─ Selects appropriate technology skills
├─ Orchestrates workflow across layers
└─ Validates integration points
```

**Does NOT:** Implement technology-specific code

### Layer 2: Technology Skills

**Role:** Specific technology implementation

```
Backend Skills:
├─ backend.express     → Express.js + Node.js
├─ backend.fastapi     → FastAPI + Python
├─ backend.rails       → Rails + Ruby
├─ backend.django      → Django + Python
└─ backend.springboot  → Spring Boot + Java

Frontend Skills:
├─ frontend.react      → React + TypeScript
├─ frontend.vue        → Vue.js + TypeScript
├─ frontend.svelte     → Svelte + TypeScript
├─ frontend.angular    → Angular + TypeScript
└─ frontend.nextjs     → Next.js (full-stack React)

Database Skills:
├─ database.postgres   → PostgreSQL
├─ database.mongodb    → MongoDB
├─ database.mysql      → MySQL/MariaDB
├─ database.redis      → Redis (caching)
└─ database.dynamodb   → DynamoDB

Deployment Skills:
├─ deployment.docker   → Docker containers
├─ deployment.k8s      → Kubernetes
├─ deployment.aws      → AWS (Lambda, ECS, etc.)
├─ deployment.vercel   → Vercel deployment
└─ deployment.railway  → Railway deployment
```

## Usage Examples

### Example 1: Create React + FastAPI + PostgreSQL App

```bash
# User specifies their stack choice
cat > project-config.yaml <<EOF
project: ecommerce-platform
backend: fastapi
frontend: react
database: postgres
deployment: docker
EOF

# Agent orchestrates using chosen skills
claude: "Use fullstack.developer to create an ecommerce platform based on project-config.yaml"

# Behind the scenes, the agent:
# 1. Uses api.define to create OpenAPI spec
# 2. Invokes backend.fastapi to generate Python API
# 3. Invokes frontend.react to generate React app
# 4. Invokes database.postgres to generate schema
# 5. Invokes deployment.docker to create containers
# 6. Validates integration and creates documentation
```

### Example 2: Create Next.js + MongoDB App

```bash
cat > project-config.yaml <<EOF
project: blog-platform
stack: nextjs  # Full-stack framework
database: mongodb
deployment: vercel
EOF

# Agent adapts to full-stack framework
claude: "Use fullstack.developer to create a blog platform with Next.js and MongoDB"

# Behind the scenes:
# 1. Recognizes Next.js is full-stack (no separate backend needed)
# 2. Invokes frontend.nextjs with API routes
# 3. Invokes database.mongodb to generate schemas
# 4. Invokes deployment.vercel for deployment
```

### Example 3: Microservices Architecture

```bash
cat > project-config.yaml <<EOF
project: microservices-platform
architecture: microservices
services:
  - name: user-service
    backend: express
    database: postgres
  - name: order-service
    backend: fastapi
    database: mongodb
  - name: notification-service
    backend: express
    database: redis
frontend: react
deployment: k8s
EOF

# Agent orchestrates multiple services
claude: "Use fullstack.developer to create microservices platform from project-config.yaml"

# Behind the scenes:
# 1. Creates API gateway specification
# 2. For each service, invokes appropriate backend skill
# 3. For each service, invokes appropriate database skill
# 4. Invokes frontend.react for unified UI
# 5. Invokes deployment.k8s for orchestration
# 6. Creates service mesh configuration
```

## Creating Components with Meta.Agent

### Step 1: Create the Orchestrator Agent

```bash
# Use meta.agent to create the orchestrator
python agents/meta.agent/meta_agent.py agent_descriptions/fullstack.developer.md
```

**Output:**
```
✨ Agent 'fullstack.developer' created successfully!

📄 Agent definition: agents/fullstack.developer/agent.yaml
📖 Documentation: agents/fullstack.developer/README.md

🔧 Skills: api.define, workflow.compose, artifact.validate
```

### Step 2: Create Technology Skills

```bash
# Create backend skills
python agents/meta.skill/meta_skill.py skill_descriptions/backend.express.md
python agents/meta.skill/meta_skill.py skill_descriptions/backend.fastapi.md
python agents/meta.skill/meta_skill.py skill_descriptions/backend.rails.md

# Create frontend skills
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.react.md
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.vue.md
python agents/meta.skill/meta_skill.py skill_descriptions/frontend.nextjs.md

# Create database skills
python agents/meta.skill/meta_skill.py skill_descriptions/database.postgres.md
python agents/meta.skill/meta_skill.py skill_descriptions/database.mongodb.md

# Create deployment skills
python agents/meta.skill/meta_skill.py skill_descriptions/deployment.docker.md
python agents/meta.skill/meta_skill.py skill_descriptions/deployment.k8s.md
```

### Step 3: Implement Skill Handlers

Each skill gets a Python handler that implements the actual technology-specific logic:

```python
# skills/backend.fastapi/backend_fastapi.py
def generate_fastapi_app(api_spec: dict, db_schema: dict, auth_config: dict):
    """
    Generate FastAPI application from specifications

    This is where the actual FastAPI-specific code generation happens
    """
    # Parse OpenAPI spec
    # Generate Pydantic models
    # Create FastAPI routes
    # Add authentication middleware
    # Generate database integration
    # Create tests
    pass
```

## Benefits of This Architecture

### 1. **Technology Freedom**

Users can choose their stack per project:
- E-commerce: React + Express + PostgreSQL
- Blog: Next.js + MongoDB
- Analytics: Vue + FastAPI + PostgreSQL + Redis

### 2. **Skill Reusability**

Skills can be used by multiple agents:
- `backend.fastapi` used by: fullstack.developer, api.developer, microservices.architect
- `frontend.react` used by: fullstack.developer, spa.developer, mobile.developer
- `database.postgres` used by: fullstack.developer, data.engineer, migration.specialist

### 3. **Easy to Extend**

Adding a new technology is just creating a new skill:

```bash
# Someone wants to add Rust backend support
python agents/meta.skill/meta_skill.py skill_descriptions/backend.actix.md

# Now available to all agents!
```

### 4. **Maintainable**

Technology updates happen in one place:

```bash
# Express v5 released? Update one skill:
vim skills/backend.express/backend_express.py

# All agents using backend.express get the update
```

### 5. **Testable**

Each skill is independently testable:

```bash
# Test Express skill in isolation
pytest skills/backend.express/test_backend_express.py

# Test FastAPI skill in isolation
pytest skills/backend.fastapi/test_backend_fastapi.py

# Test full integration
pytest tests/integration/test_fullstack_workflow.py
```

## Comparison: Old vs New Approach

### ❌ Monolithic Agent Approach

```
fullstack-developer agent (3000 lines)
├─ Express documentation (500 lines)
├─ FastAPI documentation (500 lines)
├─ React documentation (500 lines)
├─ Vue documentation (500 lines)
├─ PostgreSQL documentation (500 lines)
└─ MongoDB documentation (500 lines)

Problems:
- Choose ONE stack per agent instance
- Can't mix technologies
- Agent prompt is huge and unfocused
- Updates require changing agent definition
```

### ✅ Modular Skill Approach

```
fullstack.developer agent (200 lines)
├─ Orchestrates workflow
└─ Delegates to skills

backend.express skill (300 lines)
backend.fastapi skill (300 lines)
frontend.react skill (300 lines)
frontend.vue skill (300 lines)
database.postgres skill (300 lines)
database.mongodb skill (300 lines)

Benefits:
- Mix and match ANY combination
- Agent stays focused on orchestration
- Skills are reusable across agents
- Easy to add new technologies
```

## Implementation Workflow

### Phase 1: Core Skills (Week 1-2)

Create foundational technology skills:

1. **Backend Skills**
   - [ ] backend.express
   - [ ] backend.fastapi
   - [ ] backend.django

2. **Frontend Skills**
   - [ ] frontend.react
   - [ ] frontend.vue
   - [ ] frontend.nextjs

3. **Database Skills**
   - [ ] database.postgres
   - [ ] database.mongodb
   - [ ] database.redis

4. **Deployment Skills**
   - [ ] deployment.docker
   - [ ] deployment.k8s

### Phase 2: Orchestrator Agent (Week 3)

1. Create fullstack.developer agent using meta.agent
2. Configure skill composition logic
3. Implement technology selection workflow
4. Add integration validation

### Phase 3: Advanced Features (Week 4+)

1. Add more technology options
2. Implement best practices validation
3. Add performance optimization
4. Create migration skills (e.g., Express → FastAPI)

## Best Practices

### 1. Keep Agents Technology-Agnostic

**Agent responsibilities:**
- Architecture decisions
- Workflow orchestration
- Integration validation
- Pattern recommendations

**NOT agent responsibilities:**
- Specific framework syntax
- Technology implementation details
- Library-specific patterns

### 2. Make Skills Technology-Specific

**Skill responsibilities:**
- Generate technology-specific code
- Follow framework best practices
- Handle technology-specific errors
- Implement technology patterns

**NOT skill responsibilities:**
- High-level architecture decisions
- Cross-technology orchestration

### 3. Use Artifact Flows

Connect skills through artifacts:

```yaml
api.define:
  produces: openapi-spec

backend.fastapi:
  consumes: openapi-spec
  produces: fastapi-application

frontend.react:
  consumes: openapi-spec
  produces: react-application

# Agent ensures artifact flow is valid
```

### 4. Version Skills Independently

```yaml
backend.express:
  version: 2.0.0  # Updated for Express v5

backend.fastapi:
  version: 1.5.0  # Still on older version

# Users can pin skill versions per project
```

## Conclusion

The **Orchestrator Agent + Technology Skills** pattern provides:

✅ **Flexibility** - Choose any tech stack
✅ **Reusability** - Skills used across agents
✅ **Maintainability** - Update in one place
✅ **Extensibility** - Add technologies easily
✅ **Testability** - Test components independently

This is the **Betty Way** for full-stack development.

## Next Steps

1. Review skill descriptions in `skill_descriptions/`
2. Use meta.skill to create technology skills
3. Use meta.agent to create orchestrator agent
4. Implement skill handlers with actual code generation
5. Test with real projects
6. Iterate based on feedback

## Related Documentation

- [META_AGENTS.md](./META_AGENTS.md) - Meta-agent architecture
- [skills-framework.md](./skills-framework.md) - Skill design patterns
- [agent-define-implementation-plan.md](./agent-define-implementation-plan.md) - Agent composition
