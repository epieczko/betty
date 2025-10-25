# Artifact Creation Usage Guide

Complete guide for creating professional artifacts using the Betty Framework.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Usage Patterns](#usage-patterns)
3. [Templates Overview](#templates-overview)
4. [artifact.create Skill](#artifactcreate-skill)
5. [Examples](#examples)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Option 1: AI-Assisted Generation (Recommended)

```bash
python3 skills/artifact.create/artifact_create.py \
  <artifact-type> \
  "<context>" \
  <output-path> \
  [--author "Your Name"] \
  [--classification Internal]
```

**Example:**
```bash
python3 skills/artifact.create/artifact_create.py \
  business-case \
  "New customer portal to reduce support costs by 40%" \
  ./artifacts/customer-portal-business-case.yaml \
  --author "Jane Smith" \
  --classification Internal
```

### Option 2: Manual Template Use

```bash
# 1. Copy template
cp templates/governance/business-case.yaml my-project/business-case.yaml

# 2. Edit following inline guidance
vim my-project/business-case.yaml

# 3. Refer to comprehensive guidance
cat artifact_descriptions/business-case.md
```

---

## Usage Patterns

### Pattern 1: Fully Automated (Future - Phase 2+)

**User provides high-level intent → Specialized agent creates artifact**

```bash
# Future capability with specialized agents
betty agent strategy.architect \
  --task "Create business case for customer portal" \
  --context "@meeting-notes.md"

# Agent autonomously:
# 1. Analyzes context
# 2. Selects appropriate artifact type (business-case)
# 3. Generates complete artifact with artifact.create
# 4. Validates with artifact.validate
# 5. Returns polished artifact
```

**Status**: Phase 3-4 (Weeks 3-4)

---

### Pattern 2: Semi-Automated (Current - Phase 1)

**User specifies artifact type → artifact.create skill assists**

```bash
python3 skills/artifact.create/artifact_create.py \
  threat-model \
  "Payment API with PCI-DSS compliance" \
  ./security/payment-api-threat-model.yaml \
  --author "Security Team" \
  --classification Confidential
```

**Workflow:**
1. ✅ User provides: artifact type, context, output path
2. ✅ Skill loads appropriate template
3. ✅ Skill populates metadata (dates, author, classification)
4. ✅ Skill adds context hints throughout document
5. ✅ User reviews and refines the generated artifact
6. ✅ User replaces TODO markers with specifics

**Time Savings**: 50-75% (from 4-8 hours to 1-2 hours)

**Status**: ✅ **Available Now** (Phase 1 Complete)

---

### Pattern 3: Manual with Templates (Current - Phase 1)

**User copies template → Fills in manually**

```bash
# 1. Find appropriate template
ls templates/governance/

# 2. Copy to your project
cp templates/governance/portfolio-roadmap.yaml \
   my-project/roadmap.yaml

# 3. Edit manually
vim my-project/roadmap.yaml

# 4. Reference guidance
less artifact_descriptions/portfolio-roadmap.md
```

**Workflow:**
1. ✅ User selects appropriate template
2. ✅ User copies to project location
3. ✅ User manually edits all sections
4. ✅ User references artifact description for guidance
5. ✅ User validates structure and content

**Time Savings**: 30-50% (from 4-8 hours to 2-4 hours)

**Status**: ✅ **Available Now** (Phase 1 Complete)

---

## Templates Overview

### Organization

**406 templates** organized in **21 categories**:

```
templates/
├── governance/      (280 templates) - Business cases, roadmaps, logs, charters
├── architecture/    (27 templates)  - Diagrams, models, designs
├── data/            (32 templates)  - Schemas, models, dictionaries
├── testing/         (20 templates)  - Plans, results, reports
├── security/        (15 templates)  - Threat models, assessments
├── deployment/      (12 templates)  - Plans, pipelines, releases
├── documentation/   (11 templates)  - Guides, manuals, handbooks
├── ai-ml/           (9 templates)   - Model cards, evaluations
└── ... (13 more categories)
```

### Formats

**YAML Templates (312)**: Structured data artifacts
- Schemas, specifications, definitions
- Plans, roadmaps, matrices
- Configurations, manifests

**Markdown Templates (94)**: Documentation artifacts
- Reports, guides, manuals
- Policies, procedures
- Assessments, analyses

### Template Features

Every template includes:
- ✅ **Document Control**: Version, dates, author, status, classification
- ✅ **Ownership Metadata**: Owner, approvers, approval workflow
- ✅ **Related Documents**: Upstream/downstream dependencies
- ✅ **Structured Content**: Context-aware sections
- ✅ **TODO Markers**: Clear guidance on what to fill
- ✅ **Inline Comments**: Best practices and examples
- ✅ **Change History**: Version tracking
- ✅ **Reference Links**: To comprehensive artifact descriptions

---

## artifact.create Skill

### Purpose

AI-assisted artifact generation from professional templates.

### How It Works

```
1. Load Template
   ↓
2. Validate Artifact Type (against 406 registered types)
   ↓
3. Populate Metadata (dates, author, classification)
   ↓
4. Inject Context Hints (throughout document)
   ↓
5. Generate Artifact (save to specified path)
   ↓
6. Return Report (with next steps)
```

### Command Syntax

```bash
python3 skills/artifact.create/artifact_create.py \
  <artifact-type> \        # Required: Type from KNOWN_ARTIFACT_TYPES
  "<context>" \            # Required: Business context/requirements
  <output-path> \          # Required: Where to save the artifact
  [--author "Name"] \      # Optional: Author name
  [--classification Level] # Optional: Public|Internal|Confidential|Restricted
```

### Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `artifact-type` | ✅ Yes | Artifact type (must exist in registry) | `business-case` |
| `context` | ✅ Yes | Business context for population | `"New customer portal..."` |
| `output-path` | ✅ Yes | Output file path | `./artifacts/my-artifact.yaml` |
| `--author` | ❌ No | Author name | `"Jane Smith"` |
| `--classification` | ❌ No | Classification level | `Internal` |

### Finding Artifact Types

**Method 1: Search templates directory**
```bash
# List all templates in a category
ls templates/governance/

# Search for specific artifact
find templates -name "*threat*"
```

**Method 2: Check artifact registry**
```bash
# View all registered artifact types
grep -E "^\s+\"[a-z-]+\":" skills/artifact.define/artifact_define.py | head -20
```

**Method 3: Try and get suggestions**
```bash
# If you use wrong type, you'll get suggestions
python3 skills/artifact.create/artifact_create.py \
  invalid-type \
  "test" \
  ./test.yaml

# Output shows first 10 available types:
# Available artifact types (showing first 10):
#   - openapi-spec
#   - validation-report
#   - workflow-definition
#   ...
```

---

## Examples

### Example 1: Business Case

**Scenario**: Need business justification for new customer portal

```bash
python3 skills/artifact.create/artifact_create.py \
  business-case \
  "Self-service customer portal to reduce support ticket volume by 40% and improve customer satisfaction. Investment of $500K with expected ROI of 18 months through reduced support costs ($300K annually) and improved retention (5% reduction in churn worth $200K annually)." \
  ./governance/customer-portal-business-case.yaml \
  --author "Product Strategy" \
  --classification Internal
```

**Result**: `customer-portal-business-case.yaml` with:
- ✅ Populated metadata (author, dates, classification)
- ✅ Context hints in content sections
- ✅ TODO markers for refinement
- ✅ Reference to comprehensive guidance

**Next Steps**:
1. Review generated artifact
2. Consult `artifact_descriptions/business-case.md`
3. Replace TODOs with specifics (cost breakdown, timeline, risks)
4. Update approvers
5. Change status: Draft → Review → Approved

---

### Example 2: Threat Model

**Scenario**: Security assessment for payment API

```bash
python3 skills/artifact.create/artifact_create.py \
  threat-model \
  "Payment processing API handling credit card transactions. PCI-DSS Level 1 compliance required. Processes 50M transactions annually ($2B GMV). Uses tokenization, encryption at rest (AES-256), TLS 1.3 in transit. Integrates with Stripe and internal fraud detection system." \
  ./security/payment-api-threat-model.yaml \
  --author "Security Architecture Team" \
  --classification Confidential
```

**Result**: `payment-api-threat-model.yaml` with security-specific structure

**Next Steps**:
1. Review STRIDE analysis sections
2. Consult `artifact_descriptions/threat-model.md`
3. Add specific threats (spoofing, tampering, repudiation, etc.)
4. Document mitigations
5. Assign risk ratings
6. Schedule security review

---

### Example 3: Portfolio Roadmap

**Scenario**: Strategic roadmap for digital transformation

```bash
python3 skills/artifact.create/artifact_create.py \
  portfolio-roadmap \
  "Digital transformation initiative over 18 months. Phase 1 (Q1-Q2): Cloud migration (AWS) for cost reduction and scalability. Phase 2 (Q2-Q3): API platform modernization enabling partner ecosystem. Phase 3 (Q3-Q4): Customer experience improvements including mobile app and personalization. Total budget: $5M. Expected benefits: 30% cost reduction, 2x faster feature delivery, 25% revenue growth from new channels." \
  ./strategy/digital-transformation-roadmap.yaml \
  --author "Enterprise Architecture" \
  --classification Internal
```

**Result**: `digital-transformation-roadmap.yaml` with roadmap structure

**Next Steps**:
1. Refine timeline and milestones
2. Add dependencies between initiatives
3. Detail resource requirements per phase
4. Document risks and mitigation strategies
5. Link to individual project business cases
6. Schedule executive review

---

### Example 4: System Requirements Specification

**Scenario**: Requirements for mobile banking app

```bash
python3 skills/artifact.create/artifact_create.py \
  system-requirements-specification \
  "Mobile banking application for iOS and Android. Features: biometric authentication (Face ID, Touch ID, fingerprint), account management (checking, savings, credit cards), bill pay, mobile check deposit (OCR), real-time push notifications, P2P transfers. Must support WCAG 2.1 AA accessibility, handle 100K concurrent users, 99.9% uptime SLA, data encryption at rest and in transit." \
  ./requirements/mobile-banking-requirements.yaml \
  --author "Product Management" \
  --classification Internal
```

**Result**: `mobile-banking-requirements.yaml` with functional and non-functional requirements structure

---

### Example 5: User Manual (Markdown)

**Scenario**: End-user documentation for customer portal

```bash
python3 skills/artifact.create/artifact_create.py \
  user-manuals \
  "End-user guide for customer self-service portal. Covers: account creation and setup, password reset and security settings, submitting service requests, tracking request status, viewing and paying bills, updating contact information, downloading invoices and statements." \
  ./docs/customer-portal-user-manual.md \
  --author "Documentation Team" \
  --classification Public
```

**Result**: `customer-portal-user-manual.md` with step-by-step documentation structure

---

### Example 6: Data Model

**Scenario**: Data architecture for new feature

```bash
python3 skills/artifact.create/artifact_create.py \
  data-model \
  "Customer 360 data model consolidating data from CRM (Salesforce), Support (Zendesk), and Commerce (Shopify). Entities: Customer, Account, Contact, Interaction, Order, SupportTicket, Product. Focus on customer journey tracking and personalization use cases." \
  ./data/customer-360-data-model.yaml \
  --author "Data Architecture" \
  --classification Internal
```

---

## Best Practices

### Context Quality

**DO** ✅ Provide rich, specific context:
```bash
# Good: Specific details
"Payment API handling $2B GMV annually, PCI-DSS Level 1, tokenization with Stripe, AES-256 encryption"

# Better: Include constraints and requirements
"Payment API for e-commerce platform. Handles 50M transactions/year ($2B GMV). Must achieve PCI-DSS Level 1 compliance. Integration with Stripe for tokenization. Security requirements: AES-256 at rest, TLS 1.3 in transit, fraud detection integration. Performance: p99 latency <100ms, 99.99% uptime."
```

**DON'T** ❌ Provide vague context:
```bash
# Too vague
"Payment system"

# Missing key details
"API for payments"
```

### Artifact Type Selection

**DO** ✅ Choose the most specific type:
```bash
# Good: Specific
system-requirements-specification  # For detailed system requirements
functional-requirements-specification  # For functional requirements only

# Better: Match your use case
business-case  # For investment justification
portfolio-roadmap  # For strategic multi-initiative planning
project-roadmap  # For single project timeline
```

**DON'T** ❌ Use generic types when specific ones exist:
```bash
# Too generic
document  # Instead of user-manuals
plan      # Instead of test-plan or deployment-plan
```

### File Organization

**DO** ✅ Organize by category:
```bash
my-project/
├── governance/
│   ├── business-case.yaml
│   └── project-charter.yaml
├── architecture/
│   ├── logical-architecture-diagram.yaml
│   └── threat-model.yaml
├── requirements/
│   └── system-requirements-specification.yaml
└── testing/
    └── test-plan.yaml
```

**DON'T** ❌ Mix all artifacts in one directory:
```bash
my-project/
├── business-case.yaml
├── threat-model.yaml
├── requirements.yaml
├── test-plan.yaml
└── ...  # Hard to navigate!
```

### Metadata Management

**DO** ✅ Update metadata as artifact evolves:
```yaml
metadata:
  version: "1.0.0"  # Start at 1.0.0
  status: "Draft"   # Progress: Draft → Review → Approved → Published
  classification: "Internal"  # Appropriate level
  approvers:        # Real approvers, not TODOs
    - name: "John Doe"
      role: "VP Engineering"
      approvalDate: "2025-10-30"
```

**DON'T** ❌ Leave metadata incomplete:
```yaml
metadata:
  version: "TODO"
  status: "Draft"  # Never updated
  approvers:
    - name: "TODO: Add approver"  # Still has TODOs
```

### Workflow Integration

**DO** ✅ Link artifacts together:
```yaml
relatedDocuments:
  - type: "business-case"
    path: "../governance/customer-portal-business-case.yaml"
    relationship: "depends-on"
  - type: "threat-model"
    path: "./payment-api-threat-model.yaml"
    relationship: "references"
```

**DON'T** ❌ Create isolated artifacts:
```yaml
relatedDocuments:
  - type: "TODO: Specify artifact type"
    path: "TODO: Add path"
    relationship: "depends-on | references | supersedes"
```

---

## Troubleshooting

### Unknown Artifact Type

**Problem**:
```
Error: Unknown artifact type: my-custom-type
```

**Solutions**:
1. **Find the correct type name**:
   ```bash
   # Search templates
   find templates -name "*custom*" -type f

   # Or list category
   ls templates/governance/
   ```

2. **Check common naming differences**:
   - Plural vs singular: `runbook` → `runbooks`
   - Specificity: `requirements-specification` → `system-requirements-specification`

3. **Register new type** (if truly custom):
   ```bash
   # Add to KNOWN_ARTIFACT_TYPES in skills/artifact.define/artifact_define.py
   # Then create template in appropriate category
   ```

---

### Template Not Found

**Problem**:
```
Error: No template found for artifact type: valid-type
```

**Solutions**:
1. **Verify templates directory exists**:
   ```bash
   ls -la templates/
   ```

2. **Regenerate templates**:
   ```bash
   python3 tools/generate_artifact_templates.py
   ```

3. **Check if type is registered but template missing**:
   ```bash
   # Check registry
   grep "valid-type" skills/artifact.define/artifact_define.py

   # Check templates
   find templates -name "valid-type.*"
   ```

---

### Permission Errors

**Problem**:
```
PermissionError: [Errno 13] Permission denied: './artifacts/my-artifact.yaml'
```

**Solutions**:
1. **Ensure output directory exists and is writable**:
   ```bash
   mkdir -p ./artifacts
   chmod 755 ./artifacts
   ```

2. **Use absolute paths**:
   ```bash
   python3 skills/artifact.create/artifact_create.py \
     business-case \
     "context" \
     /home/user/betty/artifacts/business-case.yaml
   ```

---

### Context Too Long

**Best Practice**: Keep context focused (200-500 words)

**If context is very long**:
1. **Summarize in command, reference full doc**:
   ```bash
   python3 skills/artifact.create/artifact_create.py \
     business-case \
     "Customer portal project - see requirements.md for full details. Key: 40% support cost reduction, $500K investment, 18mo ROI." \
     ./artifacts/business-case.yaml
   ```

2. **Use multiple artifacts**:
   ```bash
   # Executive summary in business-case
   # Detailed requirements in requirements-specification
   # Technical design in architecture-overview
   ```

---

## Next Steps

### Current Capabilities (Phase 1 ✅)

1. ✅ **406 professional templates** ready to use
2. ✅ **artifact.create skill** for AI-assisted generation
3. ✅ **Comprehensive artifact descriptions** for guidance

### Coming Soon (Phase 2-4)

**Phase 2** (Week 2):
- `artifact.validate`: Schema and quality validation
- `artifact.review`: AI-powered content review and recommendations

**Phase 3** (Week 3):
- Specialized agents:
  - `strategy.architect`: Business cases, roadmaps, charters
  - `security.architect`: Threat models, assessments, policies
  - `data.architect`: Data models, schemas, contracts
  - `test.engineer`: Test plans, test results, test reports

**Phase 4** (Week 4):
- Multi-artifact workflows
- Autonomous artifact composition
- Producer/consumer mapping completion
- Artifact dependency management

---

## Support

### Resources

- **Templates**: `templates/` directory (406 templates)
- **Artifact Descriptions**: `artifact_descriptions/` (391 comprehensive guides)
- **Skill Documentation**: `skills/artifact.create/README.md`
- **Framework Integration**: `docs/ARTIFACT_FRAMEWORK_INTEGRATION.md`
- **Status & Roadmap**: `docs/ARTIFACT_STATUS.md`

### Getting Help

1. **Check artifact description** for specific guidance:
   ```bash
   cat artifact_descriptions/<artifact-type>.md
   ```

2. **Review template** for structure:
   ```bash
   cat templates/<category>/<artifact-type>.{yaml,md}
   ```

3. **Test with simple example** first:
   ```bash
   python3 skills/artifact.create/artifact_create.py \
     business-case \
     "Simple test project" \
     ./test.yaml
   ```

---

**Version**: 1.0.0
**Last Updated**: 2025-10-25
**Status**: Phase 1 Complete ✅
