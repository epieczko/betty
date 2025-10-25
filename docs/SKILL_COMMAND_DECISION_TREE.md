# Skill vs Command Decision Tree

This document provides a decision framework for determining whether to create a skill, a command, or both, and when commands should delegate to skills.

## Quick Decision Matrix

| Scenario | Create | Pattern | Example |
|----------|--------|---------|---------|
| Simple bash orchestration (1-3 steps) | Command only | Inline instructions | `/hello` - echo greeting |
| Complex autonomous task (10+ steps) | Skill + Command | Command delegates to skill | `/optimize-build` → `build.optimize` |
| Reusable atomic operation | Skill only | Direct skill invocation | `api.validate` (no command) |
| User-facing workflow | Command + Skill | Command orchestrates skill calls | `/api-design` calls multiple skills |
| Policy enforcement | Hook only | Automatic validation | `pre-commit` hook validates code |

## Decision Tree

```
┌─────────────────────────────────────┐
│ Is this user-facing?                │
└─────────┬───────────────────────────┘
          │
    ┌─────┴─────┐
    │           │
   YES         NO
    │           │
    │           └──> Create SKILL ONLY
    │               (Reusable component)
    │
    ▼
┌─────────────────────────────────────┐
│ How many distinct steps/operations? │
└─────────┬───────────────────────────┘
          │
    ┌─────┴─────────┬──────────────┐
    │               │              │
  1-3 steps     4-9 steps      10+ steps
    │               │              │
    │               │              │
    ▼               ▼              ▼
COMMAND ONLY    HYBRID         SKILL + COMMAND
(inline)        (evaluate)     (delegation)
```

## Pattern 1: Command Only (Inline Instructions)

**When to use:**
- Simple orchestration (1-3 bash commands)
- Task doesn't need to be reusable outside the command
- No complex logic or autonomous decision-making
- Fast, straightforward execution

**Example:**
```markdown
# /api-validate command
1. Run: `python skills/api.validate/api_validate.py $ARGUMENTS`
2. Show results to user
3. Suggest fixes if errors found
```

**Characteristics:**
- ✅ Simple and direct
- ✅ Easy to understand and modify
- ✅ No additional skill creation overhead
- ❌ Logic not reusable elsewhere
- ❌ Can become unwieldy if task grows

## Pattern 2: Skill Only (No Command)

**When to use:**
- Reusable atomic operation
- Called by other skills, agents, or workflows
- Not a primary user-facing entry point
- Part of a larger composition

**Example:**
```python
# skills/api.validate/api_validate.py
# No corresponding /api-validate command
# Called by /api-design and other commands
```

**Characteristics:**
- ✅ Maximum reusability
- ✅ Composable building block
- ✅ Testable in isolation
- ✅ Clean separation of concerns
- ❌ Requires skill creation overhead
- ❌ Not directly accessible to users

## Pattern 3: Skill + Command (Delegation)

**When to use:**
- Complex autonomous task (10+ steps)
- Requires decision-making and context awareness
- Task logic should be reusable
- User needs simple entry point to complex functionality

**Example:**
```markdown
# /optimize-build command (simple wrapper)
Run the build optimization skill with provided arguments
Invoke: python skills/build.optimize/build_optimize.py $ARGUMENTS
```

```python
# skills/build.optimize/build_optimize.py (complex logic)
class BuildOptimizer:
    def analyze_build_system(self):
        # 19 steps of sophisticated build analysis
        pass
```

**Characteristics:**
- ✅ Best of both worlds
- ✅ Simple user interface
- ✅ Complex logic encapsulated and reusable
- ✅ Skill can be called by other components
- ✅ Command remains simple and maintainable
- ❌ Requires creating both artifacts
- ❌ Slight indirection overhead

## Pattern 4: Hybrid (Command Orchestrates Multiple Skills)

**When to use:**
- Multi-step workflow with user interaction points
- Orchestrates multiple skills in sequence
- Needs to show progress and gather feedback
- Each step is independently useful

**Example:**
```markdown
# /api-design command (orchestrator)
1. Run: python skills/api.define/api_define.py $SERVICE_NAME
   - Show created spec to user
2. Run: python skills/api.validate/api_validate.py specs/$SERVICE_NAME.yaml
   - Show validation results
   - Stop if errors found
3. Run: python skills/api.generate-models/modelina_generate.py specs/$SERVICE_NAME.yaml typescript
   - Show generated models
4. Summary and next steps
```

**Characteristics:**
- ✅ Clear workflow visibility
- ✅ User feedback at each step
- ✅ Reuses existing skills
- ✅ Flexible and modifiable
- ❌ More complex command definition
- ❌ Orchestration logic in command (not reusable)

## Complexity Threshold Analysis

### 1-3 Steps: Command Only
```
Example: /hello
- Echo greeting
- Show timestamp
- Log interaction
→ Inline in command
```

### 4-9 Steps: Evaluate Case by Case
```
Example: /api-check
- Load spec
- Validate format
- Check standards
- Analyze security
- Generate report
- Save results
→ Could be either:
  - Command with inline steps (if simple bash)
  - Skill + Command (if complex logic)
```

### 10+ Steps: Skill + Command
```
Example: /optimize-build
- Identify build system (5 sub-steps)
- Analyze dependencies (8 sub-steps)
- Optimize caching (6 sub-steps)
- Configure bundling (7 sub-steps)
- Test and validate (5 sub-steps)
- Generate report (4 sub-steps)
→ Must be: Skill (complex logic) + Command (simple wrapper)
```

## Decision Factors

### Factor 1: Autonomy Required

| Autonomy Level | Pattern |
|----------------|---------|
| None (just run commands) | Command only |
| Low (simple branching) | Command with inline logic |
| Medium (context-aware decisions) | Command orchestrates skills |
| High (sophisticated reasoning) | Skill + Command delegation |

### Factor 2: Reusability

| Reusability Need | Pattern |
|------------------|---------|
| One-time user task | Command only |
| Used by other commands | Skill + Command |
| Used by workflows/agents | Skill only |
| Core building block | Skill only |

### Factor 3: Complexity

| Complexity | Lines of Logic | Pattern |
|------------|----------------|---------|
| Trivial | 1-20 lines | Command only |
| Simple | 20-100 lines | Command only or Skill |
| Moderate | 100-500 lines | Skill + Command |
| Complex | 500+ lines | Skill + Command |

### Factor 4: Maintenance

| Maintenance Concern | Pattern |
|---------------------|---------|
| Frequently changing workflow | Command only (easy to edit) |
| Stable, testable logic | Skill + Command |
| Needs version control | Skill (has versioning) |
| Quick iterations | Command only |

## For Meta-Agents: Automated Decision Logic

When `meta.command` receives a command description, apply this logic:

```python
def decide_pattern(description):
    # Extract characteristics
    steps = count_steps(description)
    complexity = estimate_complexity(description)
    keywords = extract_keywords(description)

    # Decision tree
    if steps <= 3 and complexity == "low":
        return "COMMAND_ONLY"

    if steps >= 10 or complexity == "high":
        return "SKILL_AND_COMMAND"

    # Check for autonomy keywords
    autonomy_keywords = [
        "analyze", "optimize", "decide", "evaluate",
        "complex", "multi-step", "autonomous",
        "intelligent", "adaptive"
    ]

    if any(kw in keywords for kw in autonomy_keywords):
        return "SKILL_AND_COMMAND"

    # Check for reusability keywords
    reusability_keywords = [
        "reusable", "composable", "building block",
        "library", "utility", "helper"
    ]

    if any(kw in keywords for kw in reusability_keywords):
        if steps <= 3:
            return "SKILL_ONLY"
        else:
            return "SKILL_AND_COMMAND"

    # Default for medium complexity
    return "COMMAND_ONLY"  # Can be upgraded later
```

## Recommended Workflow for Command Creation

### Step 1: Analyze Request
```
User wants: /optimize-build with 19 steps of build analysis

Analysis:
- Steps: 19 (HIGH - exceeds 10 threshold)
- Complexity: High (sophisticated analysis)
- Autonomy: High (requires decision-making)
- Reusability: High (other workflows may need it)
- Keywords: "optimize", "analyze", "complex"

→ Decision: SKILL_AND_COMMAND
```

### Step 2: Create Skill First
```bash
# Use meta.skill to create build.optimize
python agents/meta.skill/meta_skill.py examples/build-optimize-skill.md
```

### Step 3: Create Command Wrapper
```bash
# Use meta.command to create /optimize-build
python agents/meta.command/meta_command.py examples/optimize-build-command.md
```

### Step 4: Verify Integration
```bash
# Test the skill directly
python skills/build.optimize/build_optimize.py --analyze

# Test via command
/optimize-build
```

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Complex Logic in Commands
```markdown
# BAD: /optimize-build with 500 lines of bash logic
Don't put sophisticated analysis logic directly in command files
```

### ❌ Anti-Pattern 2: Command for Every Skill
```markdown
# BAD: Creating /api-validate just to wrap api.validate skill
If the skill is already user-friendly and properly documented,
a command wrapper adds unnecessary indirection
```

### ❌ Anti-Pattern 3: Skill Without Command (When User-Facing)
```python
# BAD: Complex user-facing task only as skill
Users shouldn't need to remember:
python skills/build.optimize/build_optimize.py --mode=full --cache=true

They should use:
/optimize-build
```

### ❌ Anti-Pattern 4: Duplicate Logic
```markdown
# BAD: Same logic in both command and skill
Either:
- Command delegates to skill (skill has logic)
- Command has inline logic (no skill needed)
Never duplicate!
```

## Examples from Betty Framework

### Example 1: Command Only - /api-validate
```markdown
# Simple 3-step process
1. Run validation skill
2. Show results
3. Suggest fixes
→ Inline in command (no need for wrapper skill)
```

### Example 2: Skill + Command - /optimize-build (NEW)
```markdown
# Complex 19-step process
Command: /optimize-build
↓
Delegates to: skills/build.optimize/build_optimize.py
(Contains all 19 steps of sophisticated logic)
```

### Example 3: Hybrid - /api-design
```markdown
# Orchestrates multiple existing skills
1. Call: api.define skill
2. Call: api.validate skill
3. Call: api.generate-models skill
4. Summarize results
→ Command orchestrates, skills do the work
```

### Example 4: Skill Only - api.validate
```python
# Core validation logic
# Used by multiple commands and workflows
# No dedicated command wrapper needed
```

## Migration Path

If you start with a simple command and it grows:

```
Phase 1: Command Only (inline)
  ↓
  Task grows to 5-7 steps
  ↓
Phase 2: Still Command Only (but getting complex)
  ↓
  Task exceeds 10 steps or needs autonomy
  ↓
Phase 3: Extract to Skill + Command
  - Move logic to new skill
  - Update command to delegate
  - Maintain backward compatibility
```

## Summary

**Use Command Only when:**
- 1-3 simple steps
- No reusability needed
- Direct bash orchestration
- Fast iterations required

**Use Skill Only when:**
- Building block / library function
- Not primary user entry point
- Called by other components
- Needs version control and testing

**Use Skill + Command when:**
- 10+ steps
- High complexity or autonomy
- Task should be reusable
- Users need simple entry point

**Use Hybrid when:**
- Orchestrating multiple skills
- User feedback at each step
- Flexible workflow with variants

---

**Meta-Agent Guidance:**
When receiving a command creation request, analyze the description against these factors and automatically recommend or create the appropriate pattern. For SKILL_AND_COMMAND pattern, create the skill first, then create a command that properly delegates to it.
