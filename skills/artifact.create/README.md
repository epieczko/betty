# artifact.create

## ⚙️ **Integration Note: Claude Code Plugin**

**This skill is a Claude Code plugin.** You do not invoke it via `python skills/artifact.create/artifact_create.py`. Instead:

- **Ask Claude Code** to use the skill: `"Use artifact.create to create a threat-model artifact..."`
- **Claude Code handles** validation, execution, and output interpretation
- **Direct Python execution** is only for development/testing outside Claude Code

---

AI-assisted artifact generation from professional templates.

## Purpose

The `artifact.create` skill enables rapid, high-quality artifact creation by:

1. Loading pre-built templates for 406+ artifact types
2. Populating templates with user-provided business context
3. Applying metadata and document control standards
4. Generating professional, ready-to-review artifacts

## Usage

### Via Claude Code (Recommended)

Simply ask Claude to use the skill:

```
"Use artifact.create to create a business-case artifact for a new customer portal
that improves self-service capabilities and reduces support costs by 40%.
Save it to ./artifacts/customer-portal-business-case.yaml,
authored by Jane Smith, with Internal classification."

"Use artifact.create to create a threat-model artifact for a payment processing API
with PCI-DSS compliance requirements. Save to ./artifacts/payment-api-threat-model.yaml,
authored by Security Team, with Confidential classification."

"Use artifact.create to create a portfolio-roadmap artifact for a digital transformation
initiative covering cloud migration, API platform, and customer experience improvements
over 18 months. Save to ./artifacts/digital-transformation-roadmap.yaml,
authored by Strategy Office."
```

### Direct Execution (Development/Testing)

When working outside Claude Code or for testing:

```bash
python3 skills/artifact.create/artifact_create.py \
  <artifact_type> \
  <context> \
  <output_path> \
  [--author "Your Name"] \
  [--classification Internal]
```

#### Examples

**Create a Business Case:**
```bash
python3 skills/artifact.create/artifact_create.py \
  business-case \
  "New customer portal to improve self-service capabilities and reduce support costs by 40%" \
  ./artifacts/customer-portal-business-case.yaml \
  --author "Jane Smith" \
  --classification Internal
```

**Create a Threat Model:**
```bash
python3 skills/artifact.create/artifact_create.py \
  threat-model \
  "Payment processing API with PCI-DSS compliance requirements" \
  ./artifacts/payment-api-threat-model.yaml \
  --author "Security Team" \
  --classification Confidential
```

**Create a Portfolio Roadmap:**
```bash
python3 skills/artifact.create/artifact_create.py \
  portfolio-roadmap \
  "Digital transformation initiative covering cloud migration, API platform, and customer experience improvements over 18 months" \
  ./artifacts/digital-transformation-roadmap.yaml \
  --author "Strategy Office"
```

## How It Works

### 1. Template Selection
- Validates artifact type against KNOWN_ARTIFACT_TYPES registry (406 types)
- Locates appropriate template in `templates/` directory
- Loads template structure (YAML or Markdown format)

### 2. Metadata Population
- Substitutes placeholders: `{{date}}`, `{{your_name}}`, `{{role}}`, etc.
- Applies document control metadata (version, status, classification)
- Sets ownership and approval workflow metadata

### 3. Context Integration
- **YAML artifacts**: Adds context hints within content sections
- **Markdown artifacts**: Inserts context at document beginning
- Preserves TODO markers for manual refinement

### 4. Output Generation
- Creates output directory if needed
- Saves populated artifact to specified path
- Generates detailed report with next steps

## Supported Artifact Types

All 406 registered artifact types are supported, organized in 21 categories:

| Category | Examples |
|----------|----------|
| **Governance** | business-case, portfolio-roadmap, raid-log, decision-log |
| **Architecture** | threat-model, logical-architecture-diagram, data-flow-diagram |
| **Data** | data-model, schema-definition, data-dictionary |
| **Testing** | test-plan, test-results, acceptance-criteria |
| **Security** | security-assessment, vulnerability-report, incident-response-plan |
| **Deployment** | deployment-plan, release-checklist, rollback-plan |
| **Requirements** | requirements-specification, use-case-diagram, user-story |
| **AI/ML** | model-card, training-dataset-description, model-evaluation-report |

See `skills/artifact.define/artifact_define.py` for the complete list.

## Output Formats

### YAML Templates (312 artifacts)
Structured data artifacts for:
- Schemas, models, specifications
- Plans, roadmaps, matrices
- Configurations, manifests, definitions

Example: `business-case.yaml`, `threat-model.yaml`, `data-model.yaml`

### Markdown Templates (94 artifacts)
Documentation artifacts for:
- Reports, guides, manuals
- Policies, procedures, handbooks
- Assessments, analyses, reviews

Example: `incident-report.md`, `runbook.md`, `architecture-guide.md`

## Generated Artifact Structure

Every generated artifact includes:

- ✅ **Document Control**: Version, dates, author, status, classification
- ✅ **Ownership Metadata**: Document owner, approvers, approval workflow
- ✅ **Related Documents**: Links to upstream/downstream dependencies
- ✅ **Structured Content**: Context-aware sections with TODO guidance
- ✅ **Change History**: Version tracking with dates and authors
- ✅ **Reference Links**: Pointers to comprehensive artifact descriptions

## Next Steps After Generation

1. **Review** the generated artifact at the output path
2. **Consult** the comprehensive guidance in `artifact_descriptions/{artifact-type}.md`
3. **Replace** any remaining TODO markers with specific details
4. **Validate** the structure and content against requirements
5. **Update** metadata (status → Review → Approved → Published)
6. **Link** related documents in the metadata section

## Integration with Artifact Framework

### Artifact Metadata

```yaml
artifact_metadata:
  produces:
    - type: "*"  # Dynamically produces any registered artifact type
      description: Generated from professional templates
      file_pattern: "{{output_path}}"
      content_type: application/yaml, text/markdown

  consumes:
    - type: artifact-type-description
      description: References comprehensive artifact descriptions
      file_pattern: "artifact_descriptions/*.md"
```

### Workflow Integration

```
User Context → artifact.create → Generated Artifact → artifact.validate → artifact.review
```

Future skills:
- `artifact.validate`: Schema and quality validation
- `artifact.review`: AI-powered content review and recommendations

## Error Handling

### Unknown Artifact Type
```
Error: Unknown artifact type: invalid-type
Available artifact types (showing first 10):
  - business-case
  - threat-model
  - portfolio-roadmap
  ...
```

### Missing Template
```
Error: No template found for artifact type: custom-type
```

## Performance

- **Template loading**: <50ms
- **Content population**: <200ms
- **Total generation time**: <1 second
- **Output size**: Typically 2-5 KB (YAML), 3-8 KB (Markdown)

## Dependencies

- Python 3.7+
- `artifact.define` skill (for KNOWN_ARTIFACT_TYPES registry)
- Templates in `templates/` directory (406 templates)
- Artifact descriptions in `artifact_descriptions/` (391 files, ~160K lines)

## Status

**Active** - Phase 1 implementation complete

## Tags

artifacts, templates, generation, ai-assisted, tier2

## Version History

- **0.1.0** (2024-10-25): Initial implementation
  - Support for all 406 artifact types
  - YAML and Markdown template population
  - Metadata substitution
  - Context integration
  - Generation reporting
