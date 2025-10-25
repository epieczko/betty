# Betty Marketplace Ingestion System

Design and architecture for importing external components into Betty Framework.

## Overview

The Marketplace Ingestion System allows Betty to import agents, skills, hooks, and commands from external sources and adapt them to Betty standards.

## Supported Sources

### 1. Claude Code Marketplace
- **Format**: `.claude-plugin/plugin.yaml`
- **Components**: Commands, hooks
- **URL**: https://github.com/anthropics/claude-code-marketplace

### 2. NPM Packages
- **Format**: `package.json` + custom metadata
- **Components**: Skills (JavaScript/TypeScript)
- **Registry**: https://npmjs.com

### 3. PyPI Packages
- **Format**: `pyproject.toml` / `setup.py`
- **Components**: Skills (Python)
- **Registry**: https://pypi.org

### 4. GitHub Repositories
- **Format**: betty.yaml manifest
- **Components**: Agents, skills, hooks
- **Discovery**: GitHub API

## Architecture

```
External Marketplace
        ↓
   Marketplace Adapter
        ↓
   Format Transformer
        ↓
   Betty Validator
        ↓
   Betty Standards Conformer
        ↓
   Component Installer
        ↓
   Betty Framework
```

## Components

### 1. Marketplace Adapter

**Purpose**: Discover and fetch components from external sources

**Interface**:
```python
class MarketplaceAdapter:
    def list_components(self, source: str) -> List[Component]
    def fetch_component(self, component_id: str) -> ComponentPackage
    def get_metadata(self, component_id: str) -> Dict[str, Any]
```

**Implementations**:
- `ClaudeCodeAdapter`: For Claude Code plugins
- `NPMAdapter`: For NPM packages
- `PyPIAdapter`: For PyPI packages
- `GitHubAdapter`: For GitHub repositories

### 2. Format Transformer

**Purpose**: Transform external formats to Betty format

**Interface**:
```python
class FormatTransformer:
    def transform_agent(self, external_agent: Dict) -> BettyAgent
    def transform_skill(self, external_skill: Dict) -> BettySkill
    def transform_hook(self, external_hook: Dict) -> BettyHook
```

**Transformations**:
```
Claude Code Command → Betty Skill
Claude Code Hook → Betty Hook
NPM Package → Betty Skill
GitHub Agent → Betty Agent
```

### 3. Betty Validator

**Purpose**: Validate components against Betty standards

**Interface**:
```python
class BettyValidator:
    def validate_agent(self, agent: BettyAgent) -> ValidationResult
    def validate_skill(self, skill: BettySkill) -> ValidationResult
    def validate_hook(self, hook: BettyHook) -> ValidationResult
    def validate_artifact_metadata(self, metadata: Dict) -> ValidationResult
```

**Validation Rules**:
- Naming conventions (domain.action format)
- Required fields present
- Artifact metadata consistency
- Schema compliance
- Permission declarations
- No security vulnerabilities

### 4. Standards Conformer

**Purpose**: Adapt components to meet Betty standards

**Interface**:
```python
class StandardsConformer:
    def conform_agent(self, agent: BettyAgent) -> BettyAgent
    def conform_skill(self, skill: BettySkill) -> BettySkill
    def conform_hook(self, hook: BettyHook) -> BettyHook
```

**Conformance Actions**:
- Rename to Betty conventions
- Add required metadata
- Register artifact types
- Add Betty-specific fields
- Generate missing documentation
- Add provenance information

### 5. Component Installer

**Purpose**: Install components into Betty framework

**Interface**:
```python
class ComponentInstaller:
    def install_agent(self, agent: BettyAgent, source: str) -> InstallResult
    def install_skill(self, skill: BettySkill, source: str) -> InstallResult
    def install_hook(self, hook: BettyHook, source: str) -> InstallResult
    def uninstall_component(self, component_id: str) -> bool
```

**Installation Steps**:
1. Check for conflicts
2. Validate dependencies
3. Create directory structure
4. Write component files
5. Register with Betty
6. Update indexes
7. Run post-install hooks

## Data Model

### Component Package

```python
@dataclass
class ComponentPackage:
    id: str
    name: str
    version: str
    type: ComponentType  # agent, skill, hook
    source: str  # marketplace URL
    metadata: Dict[str, Any]
    files: Dict[str, bytes]  # filename → content
    dependencies: List[str]
    provenance: ProvenanceInfo
```

### Provenance Information

```python
@dataclass
class ProvenanceInfo:
    source_marketplace: str
    source_url: str
    original_format: str
    import_date: datetime
    imported_by: str  # Betty version
    transformations_applied: List[str]
    original_metadata: Dict[str, Any]
```

### Validation Result

```python
@dataclass
class ValidationResult:
    valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationWarning]
    suggestions: List[str]
```

## Workflows

### Workflow 1: Import from Claude Code Marketplace

```bash
# 1. List available components
betty marketplace list --source claude-code

# 2. Preview component
betty marketplace show claude-code:my-command

# 3. Import component
betty marketplace import claude-code:my-command

# 4. Verify installation
betty marketplace verify my-command
```

**Steps**:
1. Adapter fetches plugin.yaml from Claude Code marketplace
2. Transformer converts command to Betty skill
3. Validator checks Betty standards compliance
4. Conformer adds required Betty metadata
5. Installer creates skill in `skills/` directory
6. Registry updated with provenance information

### Workflow 2: Import from GitHub

```bash
# 1. Add repository as source
betty marketplace add-source github:user/repo

# 2. List components from repo
betty marketplace list --source github:user/repo

# 3. Import agent
betty marketplace import github:user/repo/agents/my-agent

# 4. View provenance
betty marketplace provenance my.agent
```

### Workflow 3: Batch Import

```bash
# Import multiple components from manifest
betty marketplace import-batch manifest.yaml

# Example manifest.yaml:
# components:
#   - source: claude-code:api-validate
#     rename: api.validate
#   - source: github:user/repo/agents/code-reviewer
#   - source: npm:@betty/json-validator
```

### Workflow 4: Update Components

```bash
# Check for updates
betty marketplace check-updates

# Update specific component
betty marketplace update api.validate

# Update all components
betty marketplace update-all
```

## Transformation Rules

### Claude Code Command → Betty Skill

```yaml
# Input: Claude Code plugin.yaml
commands:
  - command: /validate-api
    description: Validate API specifications
    entrypoint: validate.py
    permissions:
      - filesystem:read

# Output: Betty skill.yaml
name: api.validate
version: 1.0.0
description: Validate API specifications
entrypoints:
  - command: /api/validate
    handler: validate.py
    runtime: python
permissions:
  - filesystem:read
artifact_metadata:
  produces:
    - type: validation-report
provenance:
  source: claude-code:validate-api
  imported: 2025-01-15T10:00:00Z
```

### Claude Code Hook → Betty Hook

```yaml
# Input: Claude Code hooks.yaml
hooks:
  - name: pre-commit
    event: before-tool-call
    command: npm run lint

# Output: Betty hooks.yaml
hooks:
  - name: pre-commit-lint
    event: before-tool-call
    command: npm run lint
    tool_filter: git
    provenance:
      source: claude-code:pre-commit-hook
```

### NPM Package → Betty Skill

```json
// Input: package.json
{
  "name": "@betty/json-validator",
  "version": "1.0.0",
  "main": "dist/index.js",
  "betty": {
    "type": "skill",
    "permissions": ["filesystem:read"]
  }
}
```

```yaml
# Output: Betty skill.yaml
name: data.validatejson
version: 1.0.0
description: Validate JSON files
entrypoints:
  - command: /data/validatejson
    handler: index.js
    runtime: node
permissions:
  - filesystem:read
provenance:
  source: npm:@betty/json-validator
  original_name: @betty/json-validator
```

## Configuration

### betty_marketplace.yaml

```yaml
marketplaces:
  - name: claude-code
    url: https://github.com/anthropics/claude-code-marketplace
    enabled: true
    auto_update: false

  - name: npm
    registry: https://registry.npmjs.org
    enabled: true
    scope: "@betty"

  - name: github
    sources:
      - user/betty-agents
      - user/betty-skills
    enabled: true

import_settings:
  auto_conform: true
  require_validation: true
  backup_original: true
  provenance_tracking: true

naming:
  prefix: ""  # Add prefix to imported components
  force_betty_conventions: true

security:
  allow_network_permissions: false
  allow_filesystem_write: false  # Require manual approval
  scan_for_vulnerabilities: true
```

## CLI Commands

```bash
# Marketplace management
betty marketplace list [--source SOURCE]
betty marketplace show COMPONENT_ID
betty marketplace search QUERY
betty marketplace add-source SOURCE_URL
betty marketplace remove-source SOURCE_NAME

# Component import
betty marketplace import COMPONENT_ID [--rename NAME]
betty marketplace import-batch MANIFEST_FILE
betty marketplace update COMPONENT_ID
betty marketplace update-all

# Component management
betty marketplace installed
betty marketplace verify COMPONENT_ID
betty marketplace provenance COMPONENT_ID
betty marketplace uninstall COMPONENT_ID

# Configuration
betty marketplace config
betty marketplace enable-source SOURCE
betty marketplace disable-source SOURCE
```

## Security Considerations

### 1. Permission Validation

Imported components must declare permissions:
- Network access
- Filesystem read/write
- Process execution

Require user approval for dangerous permissions.

### 2. Code Scanning

Scan imported code for:
- Known vulnerabilities
- Malicious patterns
- Unsafe practices

### 3. Sandboxing

Run imported components in isolated environment:
- Limited filesystem access
- Network restrictions
- Resource limits

### 4. Provenance Tracking

Maintain complete audit trail:
- Source marketplace
- Import timestamp
- Transformations applied
- Original metadata

### 5. Version Pinning

Lock component versions to prevent supply chain attacks:
- Store checksums
- Verify integrity
- Alert on unexpected changes

## Implementation Plan

### Phase 1: Foundation (Week 1)
- Design data models
- Implement MarketplaceAdapter interface
- Create ClaudeCodeAdapter
- Build basic CLI

### Phase 2: Transformation (Week 2)
- Implement FormatTransformer
- Add transformation rules
- Test with Claude Code plugins
- Validate output

### Phase 3: Validation (Week 3)
- Implement BettyValidator
- Add validation rules
- Create StandardsConformer
- Test conformance

### Phase 4: Installation (Week 4)
- Implement ComponentInstaller
- Add conflict detection
- Create provenance tracking
- Build uninstall functionality

### Phase 5: Integration (Week 5)
- Integrate with Betty CLI
- Add marketplace commands
- Create configuration system
- Write documentation

### Phase 6: Testing & Polish (Week 6)
- Comprehensive testing
- Security audit
- Performance optimization
- User documentation

## Future Enhancements

1. **Marketplace Registry**: Host Betty-specific marketplace
2. **Component Publishing**: Publish Betty components to marketplaces
3. **Dependency Resolution**: Automatic dependency installation
4. **Version Management**: Semantic versioning and compatibility
5. **Component Discovery**: AI-powered component search
6. **Quality Scores**: Rate components based on usage and quality
7. **Community Ratings**: User reviews and ratings
8. **Automatic Updates**: Background update checks
9. **Migration Tools**: Migrate between Betty versions
10. **Plugin Ecosystem**: Third-party adapter plugins

## Example: Complete Import Flow

```bash
# 1. Search for API validation components
$ betty marketplace search "api validate"

Found 3 components:
  1. claude-code:api-validator (⭐ 4.5, 1.2k downloads)
  2. npm:@betty/openapi-check (⭐ 4.2, 800 downloads)
  3. github:user/api-tools/validate (⭐ 4.0, 200 downloads)

# 2. Preview component
$ betty marketplace show claude-code:api-validator

Component: api-validator
Source: Claude Code Marketplace
Version: 1.2.0
Description: Validates OpenAPI and AsyncAPI specifications
Permissions:
  - filesystem:read
Dependencies: None
Betty Compatible: Requires transformation

# 3. Import with automatic transformation
$ betty marketplace import claude-code:api-validator --rename api.validate

🔄 Fetching from Claude Code Marketplace...
✅ Component fetched
🔄 Transforming to Betty format...
✅ Transformed to Betty skill
🔄 Validating against Betty standards...
✅ Validation passed
🔄 Installing to skills/api.validate/...
✅ Installation complete

✨ Successfully imported api.validate from Claude Code Marketplace

Next steps:
  - Review: betty marketplace provenance api.validate
  - Test: python3 skills/api.validate/api_validate.py --help
  - Use: Add to agent.yaml skills_available list

# 4. Verify installation
$ betty marketplace provenance api.validate

Component: api.validate
Source: claude-code:api-validator
Imported: 2025-01-15 10:30:00
Original Format: Claude Code plugin.yaml
Transformations:
  - Command → Skill conversion
  - Added artifact metadata
  - Conformed naming convention
Status: ✅ Verified

Original Metadata:
  Name: api-validator
  Version: 1.2.0
  Author: Anthropic
  License: MIT
```

---

**Marketplace Ingestion System** - Bringing the ecosystem to Betty!
