# artifact.review

AI-powered artifact content review for quality, completeness, and best practices compliance.

## Purpose

The `artifact.review` skill provides intelligent content quality assessment to ensure:
- Complete and substantive content
- Professional writing quality
- Best practices adherence
- Industry standards alignment
- Readiness for approval/publication

## Features

✅ **Content Analysis**: Depth, completeness, placeholder detection
✅ **Professional Quality**: Tone, structure, clarity assessment
✅ **Best Practices**: Versioning, governance, traceability checks
✅ **Industry Standards**: Framework and compliance alignment
✅ **Readiness Scoring**: 0-100 publication readiness score
✅ **Quality Rating**: Excellent, Good, Fair, Needs Improvement, Poor
✅ **Smart Recommendations**: Prioritized, actionable feedback
✅ **Multiple Review Levels**: Quick, standard, comprehensive

## Usage

### Basic Review

```bash
python3 skills/artifact.review/artifact_review.py <artifact-path>
```

### With Artifact Type

```bash
python3 skills/artifact.review/artifact_review.py \
  my-artifact.yaml \
  --artifact-type business-case
```

### Review Level

```bash
python3 skills/artifact.review/artifact_review.py \
  my-artifact.yaml \
  --review-level comprehensive
```

**Review Levels**:
- `quick` - Basic checks (future: < 1 second)
- `standard` - Comprehensive review (default)
- `comprehensive` - Deep analysis (future enhancement)

### Save Review Report

```bash
python3 skills/artifact.review/artifact_review.py \
  my-artifact.yaml \
  --output review-report.yaml
```

## Review Dimensions

### 1. Content Completeness (35% weight)

**Analyzes**:
- Word count and content depth
- Placeholder content (TODO, TBD, etc.)
- Field population percentage
- Section completeness

**Scoring Factors**:
- Content too brief (< 100 words): Major issue
- Limited depth (< 300 words): Issue
- Good depth (300+ words): Strength
- Many placeholders (> 10): Major issue
- Few placeholders (< 5): Recommendation
- No placeholders: Strength
- Content fields populated: Percentage-based score

**Example Feedback**:
```
Content Completeness: 33/100
  Word Count: 321
  Placeholders: 21
  ✅ Good content depth (321 words)
  ❌ Many placeholders found (21) - content is incomplete
```

### 2. Professional Quality (25% weight)

**Analyzes**:
- Executive summary presence
- Clear document structure
- Professional tone and language
- Passive voice usage
- Business jargon overuse

**Checks For**:
- ❌ Informal contractions (gonna, wanna)
- ❌ Internet slang (lol, omg)
- ❌ Excessive exclamation marks
- ❌ Multiple question marks
- 🟡 Excessive passive voice (> 50% of sentences)
- 🟡 Jargon overload (> 3 instances)

**Example Feedback**:
```
Professional Quality: 100/100
  ✅ Includes executive summary/overview
  ✅ Clear document structure
```

### 3. Best Practices (25% weight)

**Analyzes**:
- Semantic versioning (1.0.0 format)
- Document classification standards
- Approval workflow definition
- Change history maintenance
- Related document links

**Artifact-Specific Checks**:
- **business-case**: ROI analysis, financial justification
- **threat-model**: STRIDE methodology, threat frameworks
- **test-plan**: Test criteria (pass/fail conditions)

**Example Feedback**:
```
Best Practices: 100/100
  ✅ Uses semantic versioning
  ✅ Proper document classification set
  ✅ Approval workflow defined
  ✅ Maintains change history
  ✅ Links to related documents
```

### 4. Industry Standards (15% weight)

**Detects References To**:
- TOGAF - Architecture framework
- ISO 27001 - Information security
- NIST - Cybersecurity framework
- PCI-DSS - Payment card security
- GDPR - Data privacy
- SOC 2 - Service organization controls
- HIPAA - Healthcare privacy
- SAFe - Scaled agile framework
- ITIL - IT service management
- COBIT - IT governance
- PMBOK - Project management
- OWASP - Application security

**Recommendations Based On Type**:
- Security artifacts → ISO 27001, NIST, OWASP
- Architecture → TOGAF, Zachman
- Governance → COBIT, PMBOK
- Compliance → SOC 2, GDPR, HIPAA

**Example Feedback**:
```
Industry Standards: 100/100
  ✅ References: PCI-DSS, ISO 27001
  ✅ References industry standards: PCI-DSS, ISO 27001
```

## Readiness Score Calculation

```
Readiness Score =
  (Completeness × 0.35) +
  (Professional Quality × 0.25) +
  (Best Practices × 0.25) +
  (Industry Standards × 0.15)
```

## Quality Ratings

| Score | Rating | Meaning | Recommendation |
|-------|--------|---------|----------------|
| 90-100 | Excellent | Ready for publication | Submit for approval |
| 75-89 | Good | Ready for approval | Minor polish recommended |
| 60-74 | Fair | Needs refinement | Address key recommendations |
| 40-59 | Needs Improvement | Significant gaps | Major content work needed |
| < 40 | Poor | Major revision required | Substantial rework needed |

## Review Report Structure

```yaml
success: true
review_results:
  artifact_path: /path/to/artifact.yaml
  artifact_type: business-case
  file_format: yaml
  review_level: standard
  reviewed_at: 2025-10-25T19:30:00

  completeness:
    score: 33
    word_count: 321
    placeholder_count: 21
    issues:
      - "Many placeholders found (21) - content is incomplete"
    strengths:
      - "Good content depth (321 words)"
    recommendations:
      - "Replace 21 placeholder(s) with actual content"

  professional_quality:
    score: 100
    issues: []
    strengths:
      - "Includes executive summary/overview"
      - "Clear document structure"
    recommendations: []

  best_practices:
    score: 100
    issues: []
    strengths:
      - "Uses semantic versioning"
      - "Proper document classification set"
    recommendations: []

  industry_standards:
    score: 100
    referenced_standards:
      - "PCI-DSS"
      - "ISO 27001"
    strengths:
      - "References industry standards: PCI-DSS, ISO 27001"
    recommendations: []

readiness_score: 72
quality_rating: "Fair"
summary_recommendations:
  - "🔴 CRITICAL: Many placeholders found (21)"
  - "🟡 Add ROI/financial justification"
strengths:
  - "Good content depth (321 words)"
  - "Includes executive summary/overview"
  # ... more strengths
```

## Recommendations System

### Recommendation Priorities

**🔴 CRITICAL**: Issues that must be fixed
- Incomplete content sections
- Many placeholders (> 10)
- Missing required analysis

**🟡 RECOMMENDED**: Improvements that should be made
- Few placeholders (< 10)
- Missing best practice elements
- Industry standard gaps

**🟢 OPTIONAL**: Nice-to-have enhancements
- Minor polish suggestions
- Additional context recommendations

### Top 10 Recommendations

The review returns the top 10 most important recommendations, prioritized by:
1. Critical issues first
2. Standard recommendations
3. Most impactful improvements

## Usage Examples

### Example 1: Review Business Case

```bash
$ python3 skills/artifact.review/artifact_review.py \
    artifacts/customer-portal-business-case.yaml

======================================================================
Artifact Content Review Report
======================================================================
Artifact:        artifacts/customer-portal-business-case.yaml
Type:            business-case
Review Level:    standard

Quality Rating:  Fair
Readiness Score: 66/100

Content Completeness: 18/100
  Word Count: 312
  Placeholders: 16
  ✅ Good content depth (312 words)
  ❌ Many placeholders found (16) - content is incomplete

Professional Quality: 100/100
  ✅ Includes executive summary/overview
  ✅ Clear document structure

Best Practices: 100/100
  ✅ Uses semantic versioning
  ✅ Approval workflow defined

Industry Standards: 70/100

Top Recommendations:
  🔴 CRITICAL: Many placeholders found (16)
  🟡 Add ROI/financial justification

Overall Assessment:
  🟡 Fair quality - needs refinement before approval
======================================================================
```

### Example 2: Comprehensive Review

```bash
$ python3 skills/artifact.review/artifact_review.py \
    artifacts/threat-model.yaml \
    --review-level comprehensive \
    --output threat-model-review.yaml

# Review saved to threat-model-review.yaml
# Use for audit trail and tracking improvements
```

## Integration with artifact.validate

**Recommended workflow**:

```bash
# 1. Validate structure first
python3 skills/artifact.validate/artifact_validate.py my-artifact.yaml --strict

# 2. If valid, review content quality
if [ $? -eq 0 ]; then
  python3 skills/artifact.review/artifact_review.py my-artifact.yaml
fi
```

**Combined quality gate**:

```bash
# Both validation and review must pass
python3 skills/artifact.validate/artifact_validate.py my-artifact.yaml --strict && \
python3 skills/artifact.review/artifact_review.py my-artifact.yaml | grep -q "Excellent\|Good"
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Artifact Quality Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Review artifact quality
        run: |
          score=$(python3 skills/artifact.review/artifact_review.py \
            artifacts/my-artifact.yaml | \
            grep "Readiness Score:" | \
            awk '{print $3}' | \
            cut -d'/' -f1)

          if [ $score -lt 75 ]; then
            echo "❌ Quality score too low: $score/100"
            exit 1
          fi

          echo "✅ Quality score acceptable: $score/100"
```

### Quality Gates

```bash
#!/bin/bash
# quality-gate.sh

ARTIFACT=$1
MIN_SCORE=${2:-75}

score=$(python3 skills/artifact.review/artifact_review.py "$ARTIFACT" | \
  grep "Readiness Score:" | awk '{print $3}' | cut -d'/' -f1)

if [ $score -ge $MIN_SCORE ]; then
  echo "✅ PASSED: Quality score $score >= $MIN_SCORE"
  exit 0
else
  echo "❌ FAILED: Quality score $score < $MIN_SCORE"
  exit 1
fi
```

## Command-Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `artifact_path` | string | required | Path to artifact file |
| `--artifact-type` | string | auto-detect | Artifact type override |
| `--review-level` | string | standard | quick, standard, comprehensive |
| `--output` | string | none | Save report to file |

## Exit Codes

- `0`: Review completed successfully
- `1`: Review failed (file not found, format error)

Note: Exit code does NOT reflect quality score. Use output parsing for quality gates.

## Performance

- **Review time**: < 1 second per artifact
- **Memory usage**: < 15MB
- **Scalability**: Can review 1000+ artifacts in batch

## Artifact Type Intelligence

The review adapts recommendations based on artifact type:

| Artifact Type | Special Checks |
|---------------|----------------|
| business-case | ROI analysis, financial justification |
| threat-model | STRIDE methodology, attack vectors |
| test-plan | Pass/fail criteria, test coverage |
| architecture-* | Framework references, design patterns |
| *-policy | Enforcement mechanisms, compliance |

## Dependencies

- Python 3.7+
- `yaml` (PyYAML) - YAML parsing
- `artifact.define` skill - Artifact registry
- `artifact_descriptions/` - Best practices reference (optional)

## Status

**Active** - Phase 2 implementation complete

## Tags

artifacts, review, quality, ai-powered, best-practices, tier2, phase2

## Version History

- **0.1.0** (2025-10-25): Initial implementation
  - Content completeness analysis
  - Professional quality assessment
  - Best practices compliance
  - Industry standards detection
  - Readiness scoring
  - Quality ratings
  - Actionable recommendations

## See Also

- `artifact.validate` - Structure and schema validation
- `artifact.create` - Generate artifacts from templates
- `artifact_descriptions/` - Best practices guides
- `docs/ARTIFACT_USAGE_GUIDE.md` - Complete usage guide
- `PHASE2_COMPLETE.md` - Phase 2 overview
