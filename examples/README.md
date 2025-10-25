# Betty Framework Examples

This directory contains ready-to-use examples demonstrating Betty Framework capabilities.

## Directory Structure

```
examples/
├── agents/         # Example agent descriptions
├── skills/         # Example skill descriptions
├── hooks/          # Example hook descriptions
└── README.md       # This file
```

## Example Agents

### 1. code.reviewer
**Location**: `examples/agents/code_reviewer_agent.md`

**Purpose**: Analyzes code changes and provides comprehensive feedback on quality, security, and best practices.

**Features**:
- Security vulnerability scanning
- Code style checking
- Performance analysis
- Code smell detection
- Actionable suggestions with examples

**Generated Agent**: `agents/code.reviewer/`

**Usage**:
```bash
# Generate the agent
python3 agents/atum/atum.py examples/agents/code_reviewer_agent.md

# View generated configuration
cat agents/code.reviewer/agent.yaml
```

### 2. file.processor
**Location**: `examples/agents/file_processor_agent.md`

**Purpose**: Processes files through various transformations including format conversion, compression, and encryption.

**Features**:
- Format conversion (JSON ↔ YAML ↔ XML ↔ CSV)
- File compression (gzip, zip, tar.gz)
- Encryption/decryption
- Batch operations
- Pipeline transformations

**Generated Agent**: `agents/file.processor/`

**Usage**:
```bash
# Generate the agent
python3 agents/atum/atum.py examples/agents/file_processor_agent.md
```

### 3. data.validator
**Location**: `examples/agents/data_validator_agent.md`

**Purpose**: Validates data files against schemas, business rules, and quality standards.

**Features**:
- Schema compliance validation
- Business rule checking
- Data quality profiling
- Multiple format support (JSON, CSV, XML, Parquet)
- Compliance reporting (GDPR, HIPAA)

**Generated Agent**: `agents/data.validator/`

**Usage**:
```bash
# Generate the agent
python3 agents/atum/atum.py examples/agents/data_validator_agent.md
```

## Example Skills

### 1. file.compare
**Location**: `examples/skills/file_compare_skill.md`

**Purpose**: Compare two files and generate detailed diff reports.

**Features**:
- Line-by-line comparison
- Multiple output formats (unified, context, HTML, JSON)
- Diff statistics
- Binary file detection

**Generated Skill**: `skills/file.compare/`

**Usage**:
```bash
# Generate the skill
python3 agents/meta.skill/meta_skill.py examples/skills/file_compare_skill.md

# Test the skill
python3 skills/file.compare/file_compare.py \
  --file-path-1 file1.txt \
  --file-path-2 file2.txt \
  --output-format json
```

### 2. data.transform
**Location**: `examples/skills/data_transform_skill.md`

**Purpose**: Transform data between different formats with validation.

**Features**:
- Multi-format support (JSON, YAML, XML, CSV)
- Schema validation
- Data type preservation
- Data loss warnings
- Custom transformation rules

**Generated Skill**: `skills/data.transform/`

**Usage**:
```bash
# Generate the skill
python3 agents/meta.skill/meta_skill.py examples/skills/data_transform_skill.md

# Transform data
python3 skills/data.transform/data_transform.py \
  --input-file-path data.json \
  --source-format json \
  --target-format yaml
```

### 3. api.test
**Location**: `examples/skills/api_test_skill.md`

**Purpose**: Test REST API endpoints and validate responses.

**Features**:
- Multiple HTTP methods support
- OpenAPI/Swagger integration
- Authentication (Bearer, Basic, OAuth2)
- Performance metrics
- HTML test reports
- Parallel test execution

**Generated Skill**: `skills/api.test/`

**Usage**:
```bash
# Generate the skill
python3 agents/meta.skill/meta_skill.py examples/skills/api_test_skill.md

# Run API tests
python3 skills/api.test/api_test.py \
  --api-spec-path openapi.yaml \
  --base-url https://api.example.com
```

## Example Hooks

### 1. pre-commit-lint
**Location**: `examples/hooks/pre_commit_lint_hook.md`

**Purpose**: Run linter before git commits.

**Features**:
- Runs ruff and mypy before commits
- Prevents committing code with style issues
- 30-second timeout

**Usage**:
```bash
# Generate the hook
python3 agents/meta.hook/meta_hook.py examples/hooks/pre_commit_lint_hook.md

# Verify it's created
cat .claude/hooks.yaml
```

### 2. pre-commit-test
**Location**: `examples/hooks/pre_commit_test_hook.md`

**Purpose**: Run test suite before commits.

**Features**:
- Executes pytest before commits
- Prevents broken code from being committed
- 60-second timeout

**Usage**:
```bash
python3 agents/meta.hook/meta_hook.py examples/hooks/pre_commit_test_hook.md
```

### 3. error-notification
**Location**: `examples/hooks/error_notification_hook.md`

**Purpose**: Send notifications when tools fail.

**Features**:
- Triggers on any tool error
- Sends email notifications
- Rapid incident response

**Usage**:
```bash
python3 agents/meta.hook/meta_hook.py examples/hooks/error_notification_hook.md
```

### 4. post-deploy-verify
**Location**: `examples/hooks/post_deploy_verify_hook.md`

**Purpose**: Verify deployments with health checks.

**Features**:
- Runs after deployment tools
- Executes smoke tests
- 2-minute timeout for verification

**Usage**:
```bash
python3 agents/meta.hook/meta_hook.py examples/hooks/post_deploy_verify_hook.md
```

## Common Workflows

### Workflow 1: Code Quality Pipeline

```bash
# 1. Create code reviewer agent
python3 agents/atum/atum.py examples/agents/code_reviewer_agent.md

# 2. Add pre-commit hooks
python3 agents/meta.hook/meta_hook.py examples/hooks/pre_commit_lint_hook.md
python3 agents/meta.hook/meta_hook.py examples/hooks/pre_commit_test_hook.md

# 3. Now git commits will automatically lint and test
git add .
git commit -m "feature: add new functionality"
# Hooks run automatically before commit
```

### Workflow 2: Data Processing Pipeline

```bash
# 1. Create data validator agent
python3 agents/atum/atum.py examples/agents/data_validator_agent.md

# 2. Create transformation skill
python3 agents/meta.skill/meta_skill.py examples/skills/data_transform_skill.md

# 3. Process data
python3 skills/data.transform/data_transform.py \
  --input-file-path input.json \
  --source-format json \
  --target-format yaml

# 4. Validate output (when agent is fully implemented)
# python3 agents/data.validator/validate.py output.yaml
```

### Workflow 3: API Development & Testing

```bash
# 1. Create API test skill
python3 agents/meta.skill/meta_skill.py examples/skills/api_test_skill.md

# 2. Add deployment verification hook
python3 agents/meta.hook/meta_hook.py examples/hooks/post_deploy_verify_hook.md

# 3. Deploy and test automatically
./deploy.sh  # Hook runs verification after deployment
```

## Generating All Examples

Generate all examples at once:

```bash
# Generate all agents
for agent in examples/agents/*.md; do
    python3 agents/atum/atum.py "$agent"
done

# Generate all skills
for skill in examples/skills/*.md; do
    python3 agents/meta.skill/meta_skill.py "$skill"
done

# Generate all hooks (CAREFUL: This modifies .claude/hooks.yaml)
for hook in examples/hooks/*.md; do
    python3 agents/meta.hook/meta_hook.py "$hook"
done
```

## Customizing Examples

### Modify Agent Descriptions

Edit the markdown files in `examples/agents/` to change:
- Agent name and purpose
- Input/output artifact types
- Required skills
- Implementation notes

Then regenerate:
```bash
python3 agents/atum/atum.py examples/agents/YOUR_AGENT.md
```

### Modify Skill Descriptions

Edit the markdown files in `examples/skills/` to change:
- Skill name and purpose
- Input/output parameters
- Permissions required
- Artifact metadata
- Implementation notes

Then regenerate:
```bash
python3 agents/meta.skill/meta_skill.py examples/skills/YOUR_SKILL.md
```

### Modify Hook Descriptions

Edit the markdown files in `examples/hooks/` to change:
- Hook name and event type
- Tool filter
- Command to execute
- Timeout and enabled status

Then regenerate:
```bash
python3 agents/meta.hook/meta_hook.py examples/hooks/YOUR_HOOK.md
```

## Learning Path

### Beginner
1. Start with **file.compare** skill - simple and self-contained
2. Try **pre-commit-lint** hook - demonstrates event-driven automation
3. Explore **data.validator** agent - shows artifact flows

### Intermediate
1. Build **data.transform** skill - more complex with multiple formats
2. Create custom agent descriptions combining multiple skills
3. Set up complete CI/CD pipeline with multiple hooks

### Advanced
1. Implement **api.test** skill with full functionality
2. Build multi-agent workflows with compatibility analysis
3. Create custom artifact types for domain-specific needs

## Next Steps

After exploring examples:

1. **Read Documentation**:
   - [GETTING_STARTED.md](../GETTING_STARTED.md) - Quick start guide
   - [META_AGENTS.md](../docs/META_AGENTS.md) - Meta-agent details
   - [ARTIFACT_STANDARDS.md](../docs/ARTIFACT_STANDARDS.md) - Artifact system

2. **Build Your Own**:
   - Create agent descriptions for your use cases
   - Develop skills for your workflows
   - Set up hooks for your CI/CD needs

3. **Contribute**:
   - Share your agents and skills
   - Submit improvements to examples
   - Help expand the Betty ecosystem

## Troubleshooting

**Problem**: Example generation fails

```bash
# Solution: Ensure meta-agents are working
bash tests/integration/test_meta_agents.sh
```

**Problem**: Generated code has errors

```bash
# Solution: Check Python syntax
python3 -m py_compile skills/SKILL_NAME/skill_name.py
```

**Problem**: Hooks don't trigger

```bash
# Solution: Verify hooks.yaml format
cat .claude/hooks.yaml

# Check event type and tool filter match
```

## Support

- **Issues**: Report problems with examples
- **Discussions**: Share your custom examples
- **Documentation**: Improve example descriptions

---

**Start building with Betty Framework examples!**
