# generate.docs

## Overview

**generate.docs** automatically generates or updates SKILL.md documentation from skill.yaml manifest files, ensuring consistent and comprehensive documentation across all Betty skills.

## Purpose

Eliminate manual documentation drift by:
- **Before**: Developers manually write and update SKILL.md files, leading to inconsistency and outdated docs
- **After**: Documentation is automatically generated from the authoritative skill.yaml manifest

This skill helps maintain high-quality documentation by:
- Reading skill.yaml manifest files
- Extracting inputs, outputs, and metadata
- Creating standardized SKILL.md documentation
- Ensuring consistency across all Betty skills
- Supporting dry-run previews and safe overwrites

## Usage

### Basic Usage

```bash
python skills/generate.docs/generate_docs.py <manifest_path> [options]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `manifest_path` | string | Yes | - | Path to skill.yaml manifest file to generate documentation from |
| `--overwrite` | boolean | No | `false` | Overwrite existing SKILL.md file if it exists |
| `--dry-run` | boolean | No | `false` | Preview the generated documentation without writing to disk |
| `--output-path` | string | No | - | Custom output path for SKILL.md (defaults to same directory as manifest) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `doc_path` | string | Path to generated or updated SKILL.md file |
| `doc_content` | string | Generated documentation content |
| `dry_run_preview` | string | Preview of documentation (when dry_run=true) |

## Examples

### Example 1: Generate Documentation for a New Skill

```bash
python skills/generate.docs/generate_docs.py skills/api.define/skill.yaml
```

**Output**: Creates `skills/api.define/SKILL.md` with comprehensive documentation

**Result**:
```json
{
  "status": "success",
  "data": {
    "doc_path": "skills/api.define/SKILL.md",
    "skill_name": "api.define",
    "dry_run": false
  }
}
```

### Example 2: Preview Documentation Without Writing

```bash
python skills/generate.docs/generate_docs.py \
  skills/hook.define/skill.yaml \
  --dry-run=true
```

**Result**: Prints formatted documentation preview to console without creating any files

```
================================================================================
DRY RUN PREVIEW
================================================================================
# hook.define

## Overview
...
================================================================================
```

### Example 3: Overwrite Existing Documentation

```bash
python skills/generate.docs/generate_docs.py \
  skills/api.validate/skill.yaml \
  --overwrite=true
```

**Result**: Replaces existing `skills/api.validate/SKILL.md` with newly generated version

### Example 4: Custom Output Path

```bash
python skills/generate.docs/generate_docs.py \
  skills/workflow.compose/skill.yaml \
  --output-path=docs/skills/workflow-compose.md
```

**Result**: Generates documentation at `docs/skills/workflow-compose.md` instead of default location

### Example 5: Batch Documentation Generation

```bash
# Generate docs for all skills in the repository
for manifest in skills/*/skill.yaml; do
  echo "Generating docs for $manifest..."
  python skills/generate.docs/generate_docs.py "$manifest" --overwrite=true
done
```

**Result**: Updates documentation for all skills, ensuring consistency across the entire framework

## Generated Documentation Structure

The generated SKILL.md includes the following sections:

1. **Overview** - Skill name and brief description from manifest
2. **Purpose** - Detailed explanation of what the skill does
3. **Usage** - Command-line usage examples with proper syntax
4. **Parameters** - Detailed table of all inputs with types, requirements, and defaults
5. **Outputs** - Description of all skill outputs
6. **Usage Template** - Practical examples showing common use cases
7. **Integration Notes** - How to use with workflows, other skills, and batch operations
8. **Dependencies** - Required dependencies from manifest
9. **Tags** - Skill tags for categorization
10. **Version** - Skill version from manifest

## Integration Notes

### Use in Workflows

```yaml
# workflows/maintain_docs.yaml
name: Documentation Maintenance
description: Keep all skill documentation up to date

steps:
  - name: Update skill docs
    skill: generate.docs
    args:
      - "${skill_manifest_path}"
      - "--overwrite=true"

  - name: Commit changes
    command: git add ${doc_path} && git commit -m "docs: update skill documentation"
```

### Use with skill.create

When creating a new skill, automatically generate its documentation:

```bash
# Create new skill
python skills/skill.create/skill_create.py my.new.skill

# Generate documentation
python skills/generate.docs/generate_docs.py \
  skills/my.new.skill/skill.yaml
```

### Integration with CI/CD

Add to your CI pipeline to ensure documentation stays in sync:

```yaml
# .github/workflows/docs.yml
- name: Check documentation is up to date
  run: |
    for manifest in skills/*/skill.yaml; do
      python skills/generate.docs/generate_docs.py "$manifest" --dry-run=true > /tmp/preview.md
      skill_dir=$(dirname "$manifest")
      if ! diff -q "$skill_dir/SKILL.md" /tmp/preview.md; then
        echo "Documentation out of sync for $manifest"
        exit 1
      fi
    done
```

### Use with Hooks

Automatically regenerate docs when skill.yaml is modified:

```bash
python skills/hook.define/hook_define.py \
  on_file_save \
  "python skills/generate.docs/generate_docs.py {file_path} --overwrite=true" \
  --pattern="*/skill.yaml" \
  --blocking=false \
  --description="Auto-regenerate SKILL.md when skill.yaml changes"
```

## Benefits

### For Developers
- No manual documentation writing
- Consistent format across all skills
- Preview changes before committing
- Safe overwrite protection

### For Teams
- Single source of truth (skill.yaml)
- Automated documentation updates
- Standardized skill documentation
- Easy onboarding with clear docs

### For Maintenance
- Detect documentation drift
- Batch regeneration for all skills
- CI/CD integration for validation
- Version-controlled documentation

## Error Handling

### Manifest Not Found

```bash
$ python skills/generate.docs/generate_docs.py nonexistent/skill.yaml
```

**Error**:
```json
{
  "status": "error",
  "error": "Manifest file not found: nonexistent/skill.yaml"
}
```

### File Already Exists (Without Overwrite)

```bash
$ python skills/generate.docs/generate_docs.py skills/api.define/skill.yaml
```

**Error**:
```json
{
  "status": "error",
  "error": "SKILL.md already exists at skills/api.define/SKILL.md. Use --overwrite=true to replace it or --dry-run=true to preview."
}
```

### Invalid YAML Manifest

```bash
$ python skills/generate.docs/generate_docs.py broken-skill.yaml
```

**Error**:
```json
{
  "status": "error",
  "error": "Failed to parse YAML manifest: ..."
}
```

## Customization

After generation, you can manually enhance the documentation:

1. **Add detailed examples** - The generated docs include basic examples; add more complex ones
2. **Include diagrams** - Add architecture or flow diagrams
3. **Expand integration notes** - Add specific team or project integration details
4. **Add troubleshooting** - Document common issues and solutions

**Note**: Manual changes will be overwritten if you regenerate with `--overwrite=true`. Consider adding custom sections to the generator or maintaining separate docs for detailed content.

## Best Practices

1. **Run in dry-run mode first** - Preview changes before writing
2. **Use version control** - Track documentation changes via git
3. **Regenerate after manifest changes** - Keep docs in sync with manifest
4. **Include in PR reviews** - Ensure manifest and docs are updated together
5. **Automate in CI** - Validate docs match manifests in automated checks

## Dependencies

- **PyYAML**: Required for YAML manifest parsing
  ```bash
  pip install pyyaml
  ```

- **context.schema**: For validation rule definitions

## Files Created

- `SKILL.md` - Generated skill documentation (in same directory as skill.yaml by default)

## See Also

- [skill.create](../skill.create/SKILL.md) - Create new skills
- [skill.define](../skill.define/SKILL.md) - Define skill manifests
- [Betty Architecture](../../docs/betty-architecture.md) - Five-layer model
- [Skill Development Guide](../../docs/skill-development.md) - Creating new skills

## Version

**0.1.0** - Initial implementation with manifest-to-markdown generation
