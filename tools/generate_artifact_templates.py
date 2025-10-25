#!/usr/bin/env python3
"""
Artifact Template Generator

Generates usable templates for all 391 artifact types by converting
comprehensive artifact descriptions into pre-structured starter files.
"""

import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


# Category to directory mapping
CATEGORY_DIRS = {
    "Governance & Planning": "governance",
    "Business & Strategy": "governance",
    "Requirements & Analysis": "requirements",
    "High-Level and Platform": "architecture",
    "Application and Integration": "architecture",
    "Data and Information": "data",
    "Security Architecture": "security",
    "Design & UX": "design",
    "Development": "development",
    "Quality Assurance": "testing",
    "Release Management": "deployment",
    "Operations & Reliability": "operations",
    "Data Platform": "data",
    "Model Development & Governance": "ai-ml",
    "Product & Market": "product",
    "Build & Release Automation": "cicd",
    "Platform Engineering": "infrastructure",
    "Governance, Risk & Compliance": "compliance",
    "Knowledge & Enablement": "documentation",
    "Client Distribution": "mobile",
    "Access & Identity": "hr",
    "Performance & Optimization": "performance",
    "Project Closure": "closure",
    "Legal & External": "legal",
}


def infer_format_from_name(artifact_name: str) -> str:
    """Infer best format for template based on artifact name"""

    # Structured data artifacts should be YAML
    if any(x in artifact_name for x in [
        'schema', 'model', 'specification', 'definition', 'config',
        'manifest', 'plan', 'matrix', 'catalog', 'registry', 'inventory',
        'roadmap', 'charter', 'framework'
    ]):
        return "yaml"

    # Documentation artifacts should be Markdown
    if any(x in artifact_name for x in [
        'report', 'guide', 'manual', 'handbook', 'document', 'policy',
        'procedure', 'assessment', 'analysis', 'review', 'readme',
        'contributing', 'vision', 'mission', 'statement'
    ]):
        return "md"

    # Log/tracking artifacts should be YAML
    if any(x in artifact_name for x in ['log', 'register', 'tracker']):
        return "yaml"

    # Default to YAML for structured content
    return "yaml"


def generate_yaml_template(artifact_name: str, description: str, category: str) -> str:
    """Generate YAML template with proper structure"""

    display_name = artifact_name.replace('-', ' ').title()

    template = f"""# {display_name}
# Auto-generated template - Customize for your needs
# See artifact_descriptions/{artifact_name}.md for complete guidance

metadata:
  # Document Control
  version: "1.0.0"
  created: "{{{{date}}}}"  # YYYY-MM-DD
  lastModified: "{{{{date}}}}"
  author: "{{{{your_name}}}}"  # TODO: Add your name
  status: "Draft"  # Draft | Review | Approved | Published
  classification: "Internal"  # Public | Internal | Confidential | Restricted

  # Ownership
  documentOwner: "{{{{role}}}}"  # TODO: Define owning role
  approvers:
    - name: "{{{{approver_name}}}}"  # TODO: Add approvers
      role: "{{{{approver_role}}}}"
      approvalDate: null

  # Related Documents
  relatedDocuments:
    - type: "{{{{artifact_type}}}}"  # TODO: Add upstream dependencies
      path: "{{{{path}}}}"
      relationship: "depends-on | references | supersedes"

"""

    # Add context-specific sections based on artifact type
    if 'roadmap' in artifact_name:
        template += """
# Strategic Context
strategicAlignment:
  objectives:
    - "TODO: Strategic objective 1"
    - "TODO: Strategic objective 2"
  valueStreams:
    - "TODO: Value stream 1"

# Initiatives
initiatives:
  - id: "INIT-001"
    name: "TODO: Initiative name"
    description: "TODO: Describe the initiative"
    status: "Proposed"  # Proposed | Approved | Active | Paused | Completed
    priority: "P1"  # P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)
    timeline:
      start: "2024-Q1"
      end: "2024-Q4"
    owner: "TODO: Business owner"
    budget: 0  # TODO: Estimated budget
"""

    elif 'log' in artifact_name:
        template += """
# Log Entries
entries:
  - id: "001"
    date: "{{date}}"
    category: "TODO: Category"  # Risk | Issue | Decision | Change
    title: "TODO: Entry title"
    description: |
      TODO: Detailed description
    status: "Open"  # Open | In Progress | Resolved | Closed
    owner: "TODO: Owner"
    priority: "Medium"  # Low | Medium | High | Critical

  # Add more entries as needed
"""

    elif 'plan' in artifact_name:
        template += """
# Executive Summary
executiveSummary: |
  TODO: 2-3 paragraph overview
  - What is being planned
  - Why it matters
  - Key success criteria

# Objectives
objectives:
  - objective: "TODO: Primary objective"
    successCriteria:
      - "TODO: Measurable criterion 1"
      - "TODO: Measurable criterion 2"

# Scope
scope:
  inScope:
    - "TODO: What is included"
  outOfScope:
    - "TODO: What is excluded"

# Timeline
timeline:
  phases:
    - name: "Phase 1"
      startDate: "2024-Q1"
      endDate: "2024-Q2"
      milestones:
        - name: "Milestone 1"
          date: "2024-01-31"
          deliverables:
            - "TODO: Deliverable"

# Resources
resources:
  team:
    - role: "TODO: Role"
      allocation: "100%"  # FTE percentage
  budget:
    total: 0
    breakdown:
      - category: "Personnel"
        amount: 0

# Risks
risks:
  - id: "RISK-001"
    description: "TODO: Risk description"
    likelihood: "Medium"  # Low | Medium | High
    impact: "High"  # Low | Medium | High
    mitigation: "TODO: Mitigation strategy"
"""

    elif 'matrix' in artifact_name:
        template += """
# Matrix Definition
dimensions:
  rows:
    - "TODO: Row dimension 1"
    - "TODO: Row dimension 2"
  columns:
    - "TODO: Column dimension 1"
    - "TODO: Column dimension 2"

# Matrix Data
data:
  - row: "TODO: Row 1"
    column: "TODO: Column 1"
    value: "TODO: Value or relationship"
    notes: "TODO: Additional context"
"""

    elif 'charter' in artifact_name:
        template += """
# Charter Overview
purpose: |
  TODO: Why this initiative/body exists
  What problem it solves or opportunity it addresses

# Scope
scope:
  inScope:
    - "TODO: Area 1 within scope"
  outOfScope:
    - "TODO: Area 1 explicitly excluded"

# Authority & Governance
authority:
  sponsor: "TODO: Executive sponsor"
  decisionAuthority: "TODO: Who can make what decisions"
  escalationPath:
    - level: "L1"
      role: "TODO: First escalation point"

# Objectives
objectives:
  - "TODO: Objective 1"
  - "TODO: Objective 2"

# Success Criteria
successCriteria:
  - criterion: "TODO: Measurable success criterion"
    target: "TODO: Specific target"

# Stakeholders
stakeholders:
  - name: "TODO: Stakeholder or group"
    role: "TODO: Their role"
    interest: "High"  # Low | Medium | High
    influence: "High"  # Low | Medium | High
"""

    elif 'policy' in artifact_name:
        template += """
# Policy Statement
policyStatement: |
  TODO: Clear, concise statement of the policy
  What is required, prohibited, or permitted

# Purpose
purpose: |
  TODO: Why this policy exists
  What risks it mitigates or objectives it supports

# Scope
applicability:
  appliesTo:
    - "TODO: Who/what this policy applies to"
  exceptions:
    - "TODO: Specific exceptions if any"

# Requirements
requirements:
  - requirement: "TODO: Specific requirement"
    rationale: "TODO: Why this is required"
    enforcement: "TODO: How compliance is ensured"

# Roles & Responsibilities
responsibilities:
  - role: "TODO: Role name"
    responsibilities:
      - "TODO: Responsibility 1"

# Compliance
compliance:
  reviewFrequency: "Annual"  # Monthly | Quarterly | Annual
  owner: "TODO: Policy owner"
  approver: "TODO: Approval authority"
  effectiveDate: "{{date}}"

# Exceptions
exceptionProcess: |
  TODO: Describe how exceptions are requested and approved
"""

    elif any(x in artifact_name for x in ['assessment', 'analysis', 'evaluation']):
        template += """
# Assessment Overview
assessmentType: "TODO: Type of assessment"
assessmentDate: "{{date}}"
assessedBy:
  - "TODO: Assessor name and role"

# Scope
scope:
  systemsAssessed:
    - "TODO: System or area assessed"
  methodology: "TODO: Assessment framework or approach"

# Findings
findings:
  - id: "F-001"
    title: "TODO: Finding title"
    severity: "High"  # Low | Medium | High | Critical
    category: "TODO: Finding category"
    description: |
      TODO: Detailed description
    evidence: "TODO: Supporting evidence"
    recommendation: "TODO: Remediation recommendation"
    owner: "TODO: Remediation owner"
    targetDate: "{{date}}"

# Summary
summary:
  overallRating: "TODO: Overall assessment result"
  keyFindings:
    - "TODO: Key finding 1"
  priorityActions:
    - "TODO: Priority action 1"
"""

    elif 'specification' in artifact_name or 'schema' in artifact_name:
        template += """
# Specification Overview
specificationName: "TODO: Name of what is being specified"
version: "1.0.0"
status: "Draft"  # Draft | Review | Approved | Deprecated

# Requirements
requirements:
  functional:
    - id: "FR-001"
      requirement: "TODO: Functional requirement"
      priority: "Must Have"  # Must Have | Should Have | Could Have

  nonFunctional:
    - id: "NFR-001"
      category: "Performance"  # Performance | Security | Scalability | etc.
      requirement: "TODO: Non-functional requirement"
      metric: "TODO: How it's measured"
      target: "TODO: Target value"

# Design
design:
  architecture: |
    TODO: High-level architecture description
  components:
    - name: "TODO: Component name"
      purpose: "TODO: Component purpose"
      interfaces:
        - "TODO: Interface description"

# Validation
validation:
  testCriteria:
    - "TODO: How this specification will be validated"
"""

    else:
        # Generic template for other types
        template += """
# Content
# TODO: Add artifact-specific content here
# Refer to artifact_descriptions/{artifact_name}.md for detailed structure

content:
  overview: |
    TODO: Provide overview

  details: |
    TODO: Add detailed content

  conclusions: |
    TODO: Summarize conclusions or outcomes

# Next Steps
nextSteps:
  - action: "TODO: Next action"
    owner: "TODO: Responsible party"
    dueDate: "{{date}}"
""".replace('{artifact_name}', artifact_name)

    template += """
# Notes
notes: |
  TODO: Add any additional notes or context

# Change History
changeHistory:
  - version: "1.0.0"
    date: "{{date}}"
    author: "{{your_name}}"
    changes: "Initial version"
"""

    return template


def generate_markdown_template(artifact_name: str, description: str, category: str) -> str:
    """Generate Markdown template for documentation artifacts"""

    display_name = artifact_name.replace('-', ' ').title()

    template = f"""# {display_name}

> **Status**: Draft | Review | Approved | Published
> **Version**: 1.0.0
> **Last Updated**: {{{{date}}}}
> **Owner**: {{{{your_name}}}}

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | TODO: Unique identifier |
| **Classification** | Internal |
| **Approvers** | TODO: List approvers |
| **Review Date** | TODO: Next review date |

## Executive Summary

<!-- TODO: 2-3 paragraph overview for executive audience -->
<!-- What is this document about? -->
<!-- Why does it matter? -->
<!-- What are the key takeaways? -->

## Purpose & Scope

### Purpose

<!-- TODO: Explain why this document exists -->

### Scope

**In Scope:**
- TODO: What is covered

**Out of Scope:**
- TODO: What is not covered

### Target Audience

**Primary:**
- TODO: Primary readers

**Secondary:**
- TODO: Secondary readers

"""

    # Add content sections based on artifact type
    if 'report' in artifact_name:
        template += """
## Key Findings

### Finding 1: [Title]

**Severity**: High | Medium | Low

**Description:**
<!-- TODO: Describe the finding -->

**Impact:**
<!-- TODO: Describe business or technical impact -->

**Recommendation:**
<!-- TODO: Provide specific recommendation -->

### Finding 2: [Title]

<!-- Repeat structure for additional findings -->

## Analysis

<!-- TODO: Detailed analysis of findings -->

## Recommendations

1. **[Recommendation Title]**
   - **Priority**: P0 | P1 | P2 | P3
   - **Owner**: TODO: Responsible party
   - **Timeline**: TODO: Implementation timeline
   - **Effort**: TODO: Effort estimate

## Conclusion

<!-- TODO: Summarize key points and next steps -->
"""

    elif 'guide' in artifact_name or 'manual' in artifact_name or 'handbook' in artifact_name:
        template += """
## Overview

<!-- TODO: Introduce what this guide covers -->

## Prerequisites

- TODO: What readers need to know before starting
- TODO: Required access or tools

## Instructions

### Step 1: [Step Title]

**Objective:** TODO: What this step accomplishes

**Instructions:**
1. TODO: First action
2. TODO: Second action
3. TODO: Third action

**Expected Outcome:** TODO: What should happen

**Troubleshooting:**
- **Problem**: TODO: Common issue
  - **Solution**: TODO: How to resolve

### Step 2: [Step Title]

<!-- Repeat structure for additional steps -->

## Best Practices

- ✅ **DO**: TODO: Recommended practice
- ❌ **DON'T**: TODO: Anti-pattern to avoid

## Reference

### Glossary

- **Term 1**: Definition
- **Term 2**: Definition

### Related Resources

- [Resource Name](url): Description
"""

    elif 'policy' in artifact_name or 'procedure' in artifact_name:
        template += """
## Policy Statement

<!-- TODO: Clear, concise statement of what is required, prohibited, or permitted -->

## Rationale

<!-- TODO: Why this policy exists, what risks it mitigates -->

## Scope

This policy applies to:
- TODO: Who or what is covered

This policy does NOT apply to:
- TODO: Exceptions or exclusions

## Requirements

### Requirement 1: [Title]

**Description:** TODO: Specific requirement

**Rationale:** TODO: Why this is required

**Compliance:** TODO: How compliance is measured

### Requirement 2: [Title]

<!-- Repeat for additional requirements -->

## Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **[Role Name]** | TODO: What this role is responsible for |

## Compliance & Enforcement

**Review Frequency:** Annual | Quarterly | Monthly

**Monitoring:** TODO: How compliance is monitored

**Enforcement:** TODO: Consequences of non-compliance

**Exceptions:** TODO: Process for requesting exceptions

## Related Policies

- [Policy Name]: Description and link
"""

    elif 'statement' in artifact_name:
        template += """
## Statement

<!-- TODO: The formal statement (vision, mission, etc.) -->
<!-- Keep it concise, inspirational, and actionable -->

## Background

<!-- TODO: Context for why this statement was created -->

## Strategic Alignment

<!-- TODO: How this aligns with organizational strategy -->

## Implications

<!-- TODO: What this means for the organization -->

## Communication Plan

<!-- TODO: How this will be communicated to stakeholders -->
"""

    else:
        # Generic documentation template
        template += """
## Background

<!-- TODO: Provide necessary background information -->

## Main Content

### Section 1

<!-- TODO: Add content -->

### Section 2

<!-- TODO: Add content -->

## Summary

<!-- TODO: Summarize key points -->

## Next Steps

- [ ] TODO: Action item 1
- [ ] TODO: Action item 2
"""

    template += """
## References

- [Reference 1](url): Description
- See also: `artifact_descriptions/{artifact_name}.md` for detailed guidance

## Appendix

<!-- Add supporting materials as needed -->

---

**Document History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | {{{{date}}}} | {{{{your_name}}}} | Initial version |
""".replace('{artifact_name}', artifact_name)

    return template


def generate_template(artifact_name: str, description: str, category: str = "General") -> tuple[str, str]:
    """Generate template content and determine file extension"""

    # Determine format
    format_ext = infer_format_from_name(artifact_name)

    # Generate appropriate template
    if format_ext == "yaml":
        content = generate_yaml_template(artifact_name, description, category)
    else:  # markdown
        content = generate_markdown_template(artifact_name, description, category)

    return content, format_ext


def load_artifact_registry() -> Dict[str, Any]:
    """Load artifact registry by parsing the artifact_define.py file"""

    registry_file = Path("skills/artifact.define/artifact_define.py")
    with open(registry_file, 'r') as f:
        content = f.read()

    # Find KNOWN_ARTIFACT_TYPES dictionary
    start_marker = "KNOWN_ARTIFACT_TYPES = {"
    end_marker = "\n}\n"

    start_idx = content.find(start_marker)
    if start_idx == -1:
        raise ValueError("Could not find KNOWN_ARTIFACT_TYPES in artifact_define.py")

    # Find matching closing brace
    start_idx += len(start_marker) - 1  # Include the {

    # Simple parsing - find the matching }
    brace_count = 0
    end_idx = start_idx
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break

    dict_str = content[start_idx:end_idx]

    # Evaluate the dictionary (safe since it's our own code)
    artifacts = eval(dict_str)
    return artifacts


def main():
    """Generate all artifact templates"""

    # Load artifact registry
    KNOWN_ARTIFACT_TYPES = load_artifact_registry()

    templates_dir = Path("templates")

    print(f"Generating templates for {len(KNOWN_ARTIFACT_TYPES)} artifact types...\n")

    success = 0
    failed = 0

    for i, (artifact_name, artifact_info) in enumerate(sorted(KNOWN_ARTIFACT_TYPES.items()), 1):
        try:
            description = artifact_info.get('description', '')

            # Determine category directory (simplified mapping)
            category_dir = "governance"  # default

            if any(x in artifact_name for x in ['security', 'threat', 'vulnerability', 'penetration', 'encryption']):
                category_dir = "security"
            elif any(x in artifact_name for x in ['test', 'quality', 'defect']):
                category_dir = "testing"
            elif any(x in artifact_name for x in ['architecture', 'design', 'diagram', 'topology']):
                category_dir = "architecture"
            elif any(x in artifact_name for x in ['requirements', 'user-stories', 'acceptance']):
                category_dir = "requirements"
            elif any(x in artifact_name for x in ['deploy', 'release', 'pipeline']):
                category_dir = "deployment"
            elif any(x in artifact_name for x in ['incident', 'runbook', 'sop', 'monitoring']):
                category_dir = "operations"
            elif any(x in artifact_name for x in ['data', 'schema', 'model', 'etl']):
                category_dir = "data"
            elif any(x in artifact_name for x in ['ai', 'ml', 'model-card', 'training']):
                category_dir = "ai-ml"
            elif any(x in artifact_name for x in ['compliance', 'audit', 'soc', 'iso', 'gdpr']):
                category_dir = "compliance"
            elif any(x in artifact_name for x in ['guide', 'manual', 'readme', 'documentation']):
                category_dir = "documentation"

            # Generate template
            content, ext = generate_template(artifact_name, description)

            # Save to appropriate directory
            output_dir = templates_dir / category_dir
            output_dir.mkdir(parents=True, exist_ok=True)

            output_file = output_dir / f"{artifact_name}.{ext}"
            with open(output_file, 'w') as f:
                f.write(content)

            print(f"[{i}/{len(KNOWN_ARTIFACT_TYPES)}] ✓ {artifact_name} → {output_file}")
            success += 1

        except Exception as e:
            print(f"[{i}/{len(KNOWN_ARTIFACT_TYPES)}] ✗ {artifact_name}: {e}")
            failed += 1

    print(f"\n{'='*70}")
    print(f"Template Generation Complete:")
    print(f"  Successfully generated: {success}")
    print(f"  Failed: {failed}")
    print(f"\nTemplates location: {templates_dir}/")
    print(f"\nNext: Use these templates manually or via artifact.create skill")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
