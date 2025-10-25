# Command Execution Decision Tree

This document provides a comprehensive decision framework for determining:
1. **Whether to create a command** (user-facing entry point)
2. **What the command should execute** (skill, agent, or workflow)
3. **Whether to create the backend component** first

## Quick Reference: Three Execution Types

| Execution Type | Use When | Example | Characteristics |
|----------------|----------|---------|-----------------|
| **skill** | Direct, atomic operation | `/api-validate` → `api.validate` | Fast, deterministic, single-purpose |
| **agent** | Reasoning & adaptation needed | `/api-design` → `api.architect` | Context-aware, multi-step reasoning, feedback loops |
| **workflow** | Orchestrate multiple components | `/deploy` → `workflows/deploy.yaml` | Declarative, parallel execution, coordinated tasks |

## Master Decision Tree

```
┌─────────────────────────────────────────┐
│ Is this user-facing?                    │
└──────────┬──────────────────────────────┘
           │
     ┌─────┴─────┐
     │           │
    YES         NO
     │           │
     │           └──> Create COMPONENT ONLY
     │               (Skill/Agent/Workflow without command)
     │
     ▼
┌─────────────────────────────────────────┐
│ What type of processing is needed?      │
└──────────┬──────────────────────────────┘
           │
    ┌──────┴────────┬──────────────┐
    │               │              │
 REASONING    ORCHESTRATION    EXECUTION
    │               │              │
    ▼               ▼              ▼
  AGENT         WORKFLOW         SKILL
    │               │              │
    │               │              │
    ▼               ▼              ▼
┌─────────┐   ┌──────────┐   ┌────────┐
│Command→ │   │Command→  │   │Command→│
│ Agent   │   │ Workflow │   │ Skill  │
└─────────┘   └──────────┘   └────────┘
```

## Execution Type Decision Matrix

### When to Use: AGENT

**Characteristics:**
- Requires intelligent reasoning and decision-making
- Context-aware with adaptive behavior
- Multi-step process with feedback loops
- Iterative refinement needed
- Cannot be fully predefined

**Keywords that suggest agent:**
- "design", "architect", "analyze deeply"
- "decide based on context", "evaluate options"
- "iterate until", "refine based on feedback"
- "create comprehensive", "reason about"

**Complexity indicators:**
- Requires understanding domain context
- Needs to make judgment calls
- May need to ask clarifying questions
- Success criteria are qualitative

**Example scenarios:**
```
✅ /api-design → api.architect agent
   Reason: Needs to understand requirements, make design decisions,
   consider trade-offs, iterate based on constraints

✅ /security-review → security.analyst agent
   Reason: Must reason about threats, assess risk levels,
   understand context, make recommendations

✅ /architecture-review → architecture.reviewer agent
   Reason: Evaluates patterns, suggests improvements,
   considers scalability/maintainability trade-offs
```

### When to Use: WORKFLOW

**Characteristics:**
- Defined sequence of operations
- Orchestrates multiple skills/agents
- Can run tasks in parallel
- Declarative process definition
- Well-understood pipeline

**Keywords that suggest workflow:**
- "pipeline", "orchestrate", "coordinate"
- "first X, then Y, finally Z"
- "in parallel", "concurrently"
- "sequence of steps", "multi-stage"

**Complexity indicators:**
- Multiple distinct phases
- Some steps depend on previous results
- Some steps can run independently
- Clear success/failure checkpoints

**Example scenarios:**
```
✅ /deploy → workflows/deploy-pipeline.yaml
   Reason: Run tests → Build → Deploy → Verify (sequential)
   Some steps can run in parallel (multiple environments)

✅ /release → workflows/release-process.yaml
   Reason: Version bump → Changelog → Build → Tag → Publish
   Clear defined sequence with checkpoints

✅ /onboard-service → workflows/service-onboarding.yaml
   Reason: Create repo → Setup CI → Generate docs → Register service
   Multiple independent tasks that can be coordinated
```

### When to Use: SKILL

**Characteristics:**
- Single atomic operation
- Direct, deterministic execution
- Fast and predictable
- No reasoning required
- Clear input/output

**Keywords that suggest skill:**
- "validate", "transform", "convert"
- "check", "verify", "test"
- "generate from template", "format"
- "calculate", "measure"

**Complexity indicators:**
- Can be implemented as pure function
- No context understanding needed
- Success criteria are objective
- No decision-making required

**Example scenarios:**
```
✅ /api-validate → api.validate skill
   Reason: Direct validation against rules, no reasoning needed

✅ /format-code → code.format skill
   Reason: Deterministic transformation, no decisions

✅ /calculate-metrics → metrics.calculate skill
   Reason: Pure computation, objective result
```

## Detailed Decision Flow

### Step 1: Determine if Command Needed

```
Is this primarily user-facing?
│
├─ YES → Create Command
│  └─ Continue to Step 2
│
└─ NO → Create Component Only (Skill/Agent/Workflow)
   └─ Other components can use it directly
```

**Create command when:**
- Users will invoke it directly via CLI
- Needs to be discoverable in command list
- Represents a common user task
- Should have standardized parameters

**Don't create command when:**
- Only used internally by other components
- Part of a larger composition
- Too granular for direct user invocation

### Step 2: Determine Execution Type

```
What's the primary characteristic of this task?

┌─────────────────────────────────────────────────┐
│ Does it require REASONING?                      │
│ • Context understanding                         │
│ • Decision-making                               │
│ • Iterative refinement                          │
│ • Adaptive behavior                             │
└────┬────────────────────────────────────────────┘
     │ YES → USE AGENT
     │
     ▼ NO
┌─────────────────────────────────────────────────┐
│ Does it ORCHESTRATE multiple components?        │
│ • Sequential phases                             │
│ • Parallel execution                            │
│ • Multiple agents/skills                        │
│ • Dependency management                         │
└────┬────────────────────────────────────────────┘
     │ YES → USE WORKFLOW
     │
     ▼ NO
┌─────────────────────────────────────────────────┐
│ Is it a single ATOMIC operation?                │
│ • Direct execution                              │
│ • Deterministic                                 │
│ • Fast and predictable                          │
│ • No reasoning needed                           │
└────┬────────────────────────────────────────────┘
     │ YES → USE SKILL
     │
     ▼
   UNCLEAR → Default to SKILL
   (Can upgrade later if needed)
```

### Step 3: Assess Complexity

For each execution type, determine if the backend needs to be created:

**High Complexity (Create Backend First):**
- 10+ distinct steps or operations
- Complex logic or algorithms
- Significant state management
- Needs testing independently

**Low Complexity (Inline in Command):**
- 1-3 simple operations
- Direct bash commands
- No state or complex logic
- Only used by this command

## Pattern Examples

### Pattern A: Command → Agent

**When:**
- Complex reasoning task
- Context-aware decision-making
- Iterative refinement

**Structure:**
```
Command: /api-design
    ↓
Agent: api.architect
    - Understands requirements
    - Makes design decisions
    - Considers trade-offs
    - Produces comprehensive design
```

**Command Manifest:**
```yaml
name: /api-design
execution:
  type: agent
  target: api.architect
  context:
    reasoning_mode: iterative
    max_iterations: 10
```

### Pattern B: Command → Workflow

**When:**
- Multi-phase process
- Orchestrates multiple components
- Some parallel execution

**Structure:**
```
Command: /deploy
    ↓
Workflow: workflows/deploy-pipeline.yaml
    ├─ Run tests (skill: test.run)
    ├─ Build artifacts (skill: build.create)
    ├─ Deploy to staging (agent: deploy.orchestrator)
    └─ Verify deployment (skill: deploy.verify)
```

**Command Manifest:**
```yaml
name: /deploy
execution:
  type: workflow
  target: workflows/deploy-pipeline.yaml
parameters:
  - name: environment
    type: enum
    values: [dev, staging, production]
```

### Pattern C: Command → Skill

**When:**
- Single atomic operation
- Direct deterministic execution
- Fast and predictable

**Structure:**
```
Command: /optimize-build
    ↓
Skill: build.optimize
    - Analyzes build system
    - Identifies optimizations
    - Returns recommendations
```

**Command Manifest:**
```yaml
name: /optimize-build
execution:
  type: skill
  target: build.optimize
parameters:
  - name: project_path
    type: string
    default: "."
```

### Pattern D: Command Only (Inline)

**When:**
- Very simple orchestration
- 1-3 bash commands
- No reusability needed

**Structure:**
```
Command: /hello
    - Just echo "Hello, World!"
    - No backend needed
```

## Complexity Scoring System

Use this to help decide if backend component is needed:

### Reasoning Score (Agent Indicators)

| Indicator | Points |
|-----------|--------|
| Needs to understand domain context | +10 |
| Makes decisions based on context | +10 |
| Iterative refinement required | +8 |
| Adaptive behavior needed | +8 |
| Asks clarifying questions | +5 |
| Evaluates trade-offs | +5 |
| Keywords: design, architect, analyze | +3 each |

**Score → Decision:**
- 20+ points: Definitely use Agent
- 10-19 points: Probably use Agent
- 0-9 points: Use Skill or Workflow

### Orchestration Score (Workflow Indicators)

| Indicator | Points |
|-----------|--------|
| 5+ distinct components to coordinate | +10 |
| Parallel execution needed | +8 |
| Mix of agents and skills | +8 |
| Multiple phases with dependencies | +7 |
| Needs error handling between steps | +5 |
| Keywords: pipeline, orchestrate, coordinate | +3 each |

**Score → Decision:**
- 15+ points: Definitely use Workflow
- 8-14 points: Probably use Workflow
- 0-7 points: Use Skill or Agent

### Complexity Score (Backend Needed)

| Indicator | Points |
|-----------|--------|
| 10+ steps | +10 |
| Complex algorithms | +8 |
| State management needed | +7 |
| Multiple file operations | +5 |
| Should be testable independently | +5 |
| Used by multiple commands | +5 |
| Keywords: optimize, analyze, transform | +3 each |

**Score → Decision:**
- 20+ points: Create backend first
- 10-19 points: Consider creating backend
- 0-9 points: Inline in command is fine

## Real-World Examples

### Example 1: API Design Command

**User Request:** "Create a command to design a new API"

**Analysis:**
```
Reasoning Score:
  + Understands domain context: +10
  + Makes design decisions: +10
  + Evaluates trade-offs: +5
  + Keywords: "design": +3
  = 28 points → USE AGENT

Complexity Score:
  + Multiple steps: +10
  + Should be testable: +5
  + Used by workflows: +5
  = 20 points → CREATE BACKEND
```

**Decision:** Create Agent + Command
```
1. Create: agents/api.architect/
2. Create: commands/api-design.yaml → delegates to api.architect
```

### Example 2: Deployment Pipeline

**User Request:** "Create a command to deploy to multiple environments"

**Analysis:**
```
Orchestration Score:
  + 5+ components (test, build, deploy, verify): +10
  + Parallel execution (multiple envs): +8
  + Multiple phases with dependencies: +7
  + Keywords: "pipeline": +3
  = 28 points → USE WORKFLOW

Complexity Score:
  + Multiple steps: +10
  + Complex coordination: +8
  + Used by CI/CD: +5
  = 23 points → CREATE BACKEND
```

**Decision:** Create Workflow + Command
```
1. Create: workflows/deploy-pipeline.yaml
2. Create: commands/deploy.yaml → delegates to workflow
```

### Example 3: Build Optimization

**User Request:** "Create a command to optimize build processes"

**Analysis:**
```
Reasoning Score:
  + Keywords: "optimize, analyze": +6
  = 6 points → USE SKILL (not agent)

Orchestration Score:
  + Single focused task: +0
  = 0 points → USE SKILL (not workflow)

Complexity Score:
  + 19 steps in description: +10
  + Complex analysis algorithms: +8
  + Keywords: "optimize": +3
  = 21 points → CREATE BACKEND
```

**Decision:** Create Skill + Command ✅ (Already implemented!)
```
1. Create: skills/build.optimize/
2. Create: commands/optimize-build.yaml → delegates to build.optimize
```

### Example 4: Simple Greeting

**User Request:** "Create a command to say hello"

**Analysis:**
```
Reasoning Score: 0 (no reasoning needed)
Orchestration Score: 0 (single operation)
Complexity Score: 2 (very simple)
```

**Decision:** Command Only (Inline)
```
1. Create: commands/hello.yaml with inline instructions
   - No backend needed
```

## Migration Paths

### From Simple to Complex

```
Phase 1: Command Only
  /api-validate (inline: calls api.validate directly)
     ↓
     Task grows, needs reasoning
     ↓
Phase 2: Extract to Agent
  /api-validate → api.validator agent
     ↓
     Multiple commands need validation
     ↓
Phase 3: Create Workflow
  /api-pipeline → workflow that uses api.validator
```

### From Monolithic to Modular

```
Phase 1: Large Agent
  api.designer (does everything)
     ↓
     Break down by concerns
     ↓
Phase 2: Agent + Skills
  api.designer agent
    ├─ calls api.validate skill
    ├─ calls api.generate skill
    └─ calls api.document skill
     ↓
     Need to orchestrate without reasoning
     ↓
Phase 3: Workflow
  workflows/api-design-pipeline.yaml
    ├─ api.designer agent (architecture)
    ├─ api.validate skill (validation)
    └─ api.generate skill (code generation)
```

## For Meta-Agents: Automated Decision Logic

When `meta.command` receives a command description, apply this logic:

```python
def decide_execution_type(description):
    """
    Determine appropriate execution type for command

    Returns: ("agent" | "skill" | "workflow", reasoning)
    """
    # Calculate scores
    reasoning_score = calculate_reasoning_score(description)
    orchestration_score = calculate_orchestration_score(description)
    complexity_score = calculate_complexity_score(description)

    # Check reasoning indicators
    if reasoning_score >= 20:
        return ("agent", "High reasoning score: needs intelligent decision-making")

    # Check orchestration indicators
    if orchestration_score >= 15:
        return ("workflow", "High orchestration score: coordinates multiple components")

    # Check for workflow keywords
    workflow_keywords = [
        "pipeline", "orchestrate", "coordinate",
        "first.*then", "parallel", "sequence"
    ]
    if any(kw in description.lower() for kw in workflow_keywords):
        if orchestration_score >= 8:
            return ("workflow", "Orchestration keywords + moderate complexity")

    # Check for agent keywords
    agent_keywords = [
        "design", "architect", "analyze", "reason",
        "decide", "evaluate", "assess", "review"
    ]
    agent_matches = sum(1 for kw in agent_keywords if kw in description.lower())
    if agent_matches >= 3 and reasoning_score >= 10:
        return ("agent", f"Multiple reasoning keywords: {agent_matches}")

    # Default to skill for atomic operations
    return ("skill", "Single atomic operation, deterministic execution")
```

## Anti-Patterns

### ❌ Anti-Pattern 1: Agent for Simple Operations

```markdown
# BAD: /format-code → code.formatter agent
Don't use an agent for deterministic transformations
Use skill instead: /format-code → code.format skill
```

### ❌ Anti-Pattern 2: Skill for Complex Reasoning

```markdown
# BAD: /api-design → api.design skill
Don't use skill for tasks requiring intelligent decisions
Use agent instead: /api-design → api.architect agent
```

### ❌ Anti-Pattern 3: Workflow for Single Task

```markdown
# BAD: /validate → workflows/validate.yaml (single step)
Don't create workflow for single operation
Use skill instead: /validate → api.validate skill
```

### ❌ Anti-Pattern 4: Inline Complex Logic

```markdown
# BAD: /optimize-build with 500 lines of bash
Don't inline complex algorithms
Extract to skill or agent
```

## Summary

**Quick Decision Guide:**

1. **Is it user-facing?** → Yes: Create Command
2. **Does it need reasoning?** → Yes: `execution.type: agent`
3. **Does it orchestrate multiple components?** → Yes: `execution.type: workflow`
4. **Is it a single atomic operation?** → Yes: `execution.type: skill`
5. **Is it complex (10+ steps)?** → Yes: Create backend component first

**Remember:**
- **Agents** reason and adapt
- **Workflows** orchestrate and coordinate
- **Skills** execute and transform
- **Commands** provide user interface to all three

---

**For detailed implementation examples, see:**
- Agent Pattern: `/api-design` → `api.architect`
- Workflow Pattern: `/deploy` → `workflows/deploy-pipeline.yaml`
- Skill Pattern: `/optimize-build` → `build.optimize`
