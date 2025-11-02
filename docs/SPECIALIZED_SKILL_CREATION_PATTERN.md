# Specialized Skill Creation Pattern

**Version**: 1.0.0
**Last Updated**: 2025-11-02
**Purpose**: Document the repeatable process for creating specialized skills in Betty Framework

---

## Overview

This document describes the step-by-step process for creating specialized skills that provide domain-specific intelligence beyond generic artifact creation. This pattern was established during the creation of `threat.model.generate` as the first P1 specialized skill.

---

## When to Create a Specialized Skill vs Using Generic `artifact.create`

### Use Specialized Skill When:
- ✅ Artifact requires **domain-specific algorithms** (e.g., STRIDE threat modeling, CVSS scoring)
- ✅ Needs **external tool integration** (e.g., diagram generation, code analysis)
- ✅ Requires **structured analysis** (e.g., compliance gap analysis, breaking change detection)
- ✅ Benefits from **pre-built templates/frameworks** (e.g., STRIDE categories, compliance frameworks)
- ✅ Provides significantly **higher quality** than AI + template alone

### Use Generic `artifact.create` When:
- ⬜ Artifact is primarily **documentation/content** (e.g., admin guides, user manuals)
- ⬜ Template + AI context is **sufficient** for quality output
- ⬜ No specialized **domain knowledge** required
- ⬜ **Simple validation** against schema is adequate

---

## The 5-Step Skill Creation Process

### Step 1: Write Comprehensive Skill Description

Create a detailed skill description in `skill_descriptions/{skill-name}.md` that serves as the specification.

**Template**: See [skill_descriptions/threat.model.generate.md](/home/user/betty/skill_descriptions/threat.model.generate.md) as reference

**Required Sections**:

```markdown
# Skill Description: {skill.name}

## Overview
[1-2 sentence summary]

## Skill Name
{domain}.{action}

## Purpose
[Detailed explanation of what makes this skill specialized]

## Inputs
### Required
- **{input_name}** ({type}): {description}

### Optional
- **{input_name}** ({type}): {description} [Default: {value}]

## Outputs
- **{output_name}** ({type}): {description}

## Artifact Metadata
### Produces
- **{artifact-type}**: {description}
  - File pattern: `{pattern}`
  - Content type: `{mime-type}`
  - Schema: `{schema-path}`

### Consumes (Optional)
- **{artifact-type}**: {description} (enriches output if available)

## Implementation Requirements
### Core Logic
1. [Step-by-step algorithm]
2. [Key processing steps]

### Data Structures
[Key data structures/formats used]

### External Dependencies
- {library}: {purpose}

## Permissions
- filesystem:read - {why needed}
- filesystem:write - {why needed}

## Tags
- {domain}
- {methodology}
- {category}

## Usage Examples
### Example 1: {scenario}
```bash
betty skill {skill.name} \
  --{param} "{value}" \
  --output_path {path}
```

## Integration with Agents
[Which agents will use this skill and how]

## Success Criteria
- ✅ [Quality metric 1]
- ✅ [Quality metric 2]

## Quality Standards
- [Performance target]
- [Accuracy target]
- [Coverage target]

## References
- [Methodology documentation]
- [Standards/frameworks]
```

**Example**: `threat.model.generate.md` has comprehensive sections on STRIDE methodology, CVSS scoring, data structures, and usage examples.

---

### Step 2: Create Skill Structure Using `skill.create`

Use Betty's `skill.create` skill to generate the foundational structure:

```bash
PYTHONPATH=/home/user/betty python3 skills/skill.create/skill_create.py \
  {skill.name} \
  "{description}" \
  --inputs "{comma-separated-inputs}" \
  --outputs "{comma-separated-outputs}"
```

**Example**:
```bash
PYTHONPATH=/home/user/betty python3 skills/skill.create/skill_create.py \
  threat.model.generate \
  "Generate STRIDE-based threat models with intelligent threat analysis, CVSS risk scoring, and mitigation recommendations" \
  --inputs "system_description,data_flows,trust_boundaries,assets,frameworks,risk_tolerance,output_path" \
  --outputs "threat_model,threat_model_file,threat_count,high_risk_count,coverage_report"
```

**What Gets Created**:
```
skills/threat.model.generate/
├── skill.yaml                      # Basic manifest (to be enhanced)
├── threat_model_generate.py        # Python stub (to be implemented)
├── SKILL.md                        # Auto-generated docs
└── (tests will be added manually)
```

**Note**: Validation/registry update may fail due to missing dependencies (pydantic, etc.) - this is okay. The skill structure is created successfully.

---

### Step 3: Enhance `skill.yaml` with Complete Metadata

The auto-generated `skill.yaml` is minimal. Enhance it with full metadata from your skill description:

**What to Add**:

1. **Detailed Input/Output Schemas**:
```yaml
inputs:
  - name: system_description
    type: string
    required: true
    description: Detailed description of system architecture

  - name: frameworks
    type: array
    required: false
    default: ["STRIDE"]
    description: Threat modeling frameworks to apply
```

2. **Artifact Metadata** (critical for agent composition):
```yaml
artifact_metadata:
  produces:
    - type: threat-model
      description: STRIDE-based threat model with CVSS scores
      file_pattern: "*.threat-model.yaml"
      content_type: application/yaml
      schema: schemas/artifacts/threat-model-schema.json

  consumes:
    - type: architecture-overview
      description: System architecture (optional, enriches model)
      file_pattern: "*.architecture-overview.md"
      content_type: text/markdown
```

3. **Tags** (for discoverability):
```yaml
tags:
  - security
  - threat-modeling
  - stride
  - specialized
```

4. **Entrypoints** with complete parameter documentation:
```yaml
entrypoints:
  - command: /skill/{domain}/{action}
    handler: {skill}_handler.py
    runtime: python
    description: >
      Detailed description of what skill does
    parameters:
      - name: system_description
        type: string
        required: true
        description: System description for analysis
    permissions:
      - filesystem:read
      - filesystem:write
```

5. **Dependencies**:
```yaml
dependencies:
  - PyYAML
  - jsonschema
  - {domain-specific-library}
```

**Reference**: See `/home/user/betty/skills/threat.model.generate/skill.yaml` for complete example

---

### Step 4: Implement Core Logic (Future Work)

**For MVP/POC**: Keep the stub implementation. The skill manifest documents the contract.

**For Production**: Implement the algorithm described in the skill description:

```python
#!/usr/bin/env python3
"""
threat.model.generate - STRIDE Threat Modeling Implementation
"""

import os
import sys
import json
import yaml
import argparse
from typing import Dict, List, Any
from betty.logging_utils import setup_logger
from betty.errors import format_error_response

logger = setup_logger(__name__)


class STRIDEThreatModeler:
    """Implements Microsoft STRIDE threat modeling methodology."""

    STRIDE_CATEGORIES = {
        "Spoofing": "Can attacker impersonate users/systems?",
        "Tampering": "Can attacker modify data/code?",
        "Repudiation": "Can actions be denied/hidden?",
        "Information Disclosure": "Can sensitive data be exposed?",
        "Denial of Service": "Can system availability be disrupted?",
        "Elevation of Privilege": "Can attacker gain unauthorized access?"
    }

    def __init__(self, risk_tolerance: str = "medium"):
        self.risk_tolerance = risk_tolerance
        self.threats = []

    def analyze_system(self, system_description: str,
                      data_flows: Dict = None,
                      trust_boundaries: List = None,
                      assets: List = None) -> Dict[str, Any]:
        """
        Analyze system and generate threat model.

        Returns:
            Complete threat model with threats, risks, and mitigations
        """
        # 1. Parse system description
        components = self._extract_components(system_description)

        # 2. Identify trust boundaries (auto-detect if not provided)
        if not trust_boundaries:
            trust_boundaries = self._detect_trust_boundaries(components)

        # 3. Identify assets (auto-detect if not provided)
        if not assets:
            assets = self._detect_assets(system_description)

        # 4. Apply STRIDE to each component
        for component in components:
            self._apply_stride(component, trust_boundaries, assets)

        # 5. Calculate risk scores
        self._calculate_cvss_scores()

        # 6. Recommend mitigations
        self._recommend_mitigations()

        # 7. Generate coverage report
        coverage = self._generate_coverage_report()

        return {
            "metadata": {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "methodology": "STRIDE",
                "risk_tolerance": self.risk_tolerance
            },
            "system": {
                "description": system_description,
                "components": components,
                "trust_boundaries": trust_boundaries,
                "assets": assets
            },
            "threats": self.threats,
            "summary": {
                "total_threats": len(self.threats),
                "high_risk": len([t for t in self.threats if t["cvss_score"] >= 7.0]),
                "medium_risk": len([t for t in self.threats if 4.0 <= t["cvss_score"] < 7.0]),
                "low_risk": len([t for t in self.threats if t["cvss_score"] < 4.0])
            },
            "coverage": coverage
        }

    # ... additional methods for each step


def main():
    """Main entry point for threat.model.generate."""
    parser = argparse.ArgumentParser(
        description="Generate STRIDE-based threat models"
    )
    parser.add_argument("--system_description", required=True,
                       help="System description for threat modeling")
    parser.add_argument("--data_flows", type=json.loads,
                       help="Data flows (JSON)")
    parser.add_argument("--trust_boundaries", type=json.loads,
                       help="Trust boundaries (JSON array)")
    parser.add_argument("--assets", type=json.loads,
                       help="Critical assets (JSON array)")
    parser.add_argument("--frameworks", type=json.loads,
                       default=["STRIDE"],
                       help="Threat frameworks")
    parser.add_argument("--risk_tolerance", default="medium",
                       choices=["low", "medium", "high"],
                       help="Risk tolerance")
    parser.add_argument("--output_path", default="./threat-model.yaml",
                       help="Output file path")

    args = parser.parse_args()

    try:
        logger.info("Starting STRIDE threat modeling...")

        # Initialize threat modeler
        modeler = STRIDEThreatModeler(risk_tolerance=args.risk_tolerance)

        # Generate threat model
        threat_model = modeler.analyze_system(
            system_description=args.system_description,
            data_flows=args.data_flows,
            trust_boundaries=args.trust_boundaries,
            assets=args.assets
        )

        # Save to file
        with open(args.output_path, 'w') as f:
            yaml.dump(threat_model, f, default_flow_style=False, sort_keys=False)

        # Return results
        result = {
            "ok": True,
            "status": "success",
            "threat_model": threat_model,
            "threat_model_file": args.output_path,
            "threat_count": threat_model["summary"]["total_threats"],
            "high_risk_count": threat_model["summary"]["high_risk"],
            "coverage_report": threat_model["coverage"]
        }

        print(json.dumps(result, indent=2))
        logger.info(f"✅ Generated threat model: {args.output_path}")

    except Exception as e:
        logger.error(f"Error generating threat model: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
```

---

### Step 5: Document the Skill

Update `SKILL.md` with comprehensive documentation:

**Sections**:
1. **Purpose & Overview**
2. **Usage Examples** (copy from skill description)
3. **Integration with Agents** (which agents use this skill)
4. **Artifact Flow** (what artifacts it consumes/produces)
5. **Quality Standards** (what makes a good output)

**Note**: This can be auto-generated from skill description using a future `docs.generate.skilldocs` skill.

---

## Validation & Registration

### Manual Validation Checklist

Until `pydantic` and other dependencies are installed, manually validate:

- ✅ `skill.yaml` has all required fields:
  - name, version, description
  - inputs (with type, required, description)
  - outputs (with type, description)
  - artifact_metadata (produces/consumes)
  - tags
  - entrypoints
  - permissions
  - status

- ✅ Artifact metadata references **registered artifact types** from `registry/artifact_types.json`

- ✅ Tags follow conventions:
  - Domain tag (security, data, api, etc.)
  - Methodology tag (stride, cvss, etc.)
  - Category tag (specialized, analysis, validation, etc.)

- ✅ Naming follows `domain.action` pattern

### Future: Automated Registration

When dependencies are available:

```bash
# Validate skill
PYTHONPATH=/home/user/betty python3 skills/skill.define/skill_define.py \
  skills/threat.model.generate/skill.yaml

# Update registry
PYTHONPATH=/home/user/betty python3 skills/registry.update/registry_update.py \
  skills/threat.model.generate/skill.yaml
```

---

## Testing Strategy

### Unit Tests
Create `skills/{skill.name}/test_{skill}_handler.py`:

```python
import pytest
from threat_model_generate import STRIDEThreatModeler

def test_stride_analysis():
    """Test STRIDE threat identification."""
    modeler = STRIDEThreatModeler()
    result = modeler.analyze_system(
        system_description="Web app with SQL database"
    )
    assert result["summary"]["total_threats"] > 0
    assert "Tampering" in [t["category"] for t in result["threats"]]

def test_cvss_scoring():
    """Test CVSS score calculation."""
    # Test implementation
    pass
```

### Integration Tests
Test with real agents:

```bash
# Test skill independently
betty skill threat.model.generate \
  --system_description "E-commerce platform" \
  --output_path test-threat-model.yaml

# Test with security.architect agent
betty agent security.architect \
  "Create threat model for e-commerce platform"
```

---

## Rollout Process

### Phase 1: Skill Definition (✅ Complete)
- ✅ Create skill description
- ✅ Generate skill structure
- ✅ Enhance skill.yaml metadata

### Phase 2: Implementation (Future)
- ⬜ Implement core algorithm
- ⬜ Add STRIDE templates
- ⬜ Implement CVSS calculator
- ⬜ Add unit tests

### Phase 3: Integration (Future)
- ⬜ Update `security.architect` agent to use skill
- ⬜ Add to agent's `skills_available` list
- ⬜ Update agent workflow to orchestrate skill
- ⬜ Test end-to-end agent execution

### Phase 4: Documentation (Future)
- ⬜ Create usage examples
- ⬜ Record demo video
- ⬜ Update agent documentation
- ⬜ Add to marketplace

---

## Repeating for Additional P1 Skills

Use this pattern to create:

1. **compliance.matrix.generate** - Map controls to frameworks (SOC2, ISO27001, GDPR, HIPAA, PCI-DSS)
2. **requirements.trace.generate** - Link requirements → design → code → tests
3. **data.lineage.generate** - Trace data flows through systems
4. **security.gap.analyze** - Find unmitigated threats
5. **compliance.gap.analyze** - Find compliance gaps

**Each skill**:
- Gets a comprehensive `skill_descriptions/{name}.md`
- Created via `skill.create`
- Enhanced `skill.yaml` with full metadata
- Stub implementation (production later)
- Ready for agent integration

---

## Benefits of This Approach

### For Skills
- ✅ **Comprehensive specification** before any code
- ✅ **Consistent structure** across all specialized skills
- ✅ **Clear artifact contracts** for agent composition
- ✅ **Documentation-first** approach

### For Agents
- ✅ **Clear skill capabilities** via artifact metadata
- ✅ **Autonomous discovery** of compatible skills
- ✅ **Composable workflows** based on artifact flow

### For Ecosystem
- ✅ **Repeatable pattern** for adding skills
- ✅ **Quality standards** enforced through template
- ✅ **Marketplace-ready** skills from day one

---

## Next Steps

1. ✅ **Complete**: `threat.model.generate` skill definition
2. ⬜ **Next**: Create skill descriptions for remaining P1 skills
3. ⬜ **Then**: Update agents to use new specialized skills
4. ⬜ **Finally**: Implement production algorithms

---

## References

- [Betty Architecture](/home/user/betty/docs/betty-architecture.md) - 5-layer architecture
- [Artifact Standards](/home/user/betty/docs/ARTIFACT_STANDARDS.md) - Artifact type definitions
- [Skill Framework](/home/user/betty/docs/skills-framework.md) - Skill manifest schema
- [threat.model.generate Example](/home/user/betty/skills/threat.model.generate/skill.yaml) - Complete skill example
