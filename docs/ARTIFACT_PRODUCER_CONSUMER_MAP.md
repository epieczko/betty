# Artifact Producer/Consumer Map

**Version**: 1.0.0
**Last Updated**: 2025-10-25
**Status**: Phase 3 Complete

## Overview

This document provides a comprehensive map of which agents and skills produce and consume which artifacts in the Betty Framework. This enables autonomous composition of workflows and intelligent agent selection based on artifact requirements.

## Table of Contents

1. [Producer Map](#producer-map) - Who creates what
2. [Consumer Map](#consumer-map) - Who needs what
3. [Artifact Dependency Graph](#artifact-dependency-graph)
4. [Workflow Artifact Sets](#workflow-artifact-sets)
5. [Agent Capability Matrix](#agent-capability-matrix)

---

## Producer Map

### Artifacts by Producer

#### strategy.architect Agent
**Purpose**: Business strategy and planning artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| business-case | business-case-schema.json | Business justification with ROI |
| portfolio-roadmap | - | Multi-initiative strategic roadmap |
| market-analysis | - | Market opportunity assessment |
| competitive-analysis | - | Competitive landscape analysis |
| feasibility-study | - | Technical/business feasibility |
| strategic-plan | - | Multi-year strategic plan |
| value-proposition-canvas | - | Customer value proposition |
| roi-model | - | Financial ROI model |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

#### security.architect Agent
**Purpose**: Security architecture and assessment artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| threat-model | threat-model-schema.json | STRIDE-based threat assessment |
| security-architecture-diagram | - | Security architecture with trust boundaries |
| penetration-testing-report | - | Pentest findings with CVSS scores |
| vulnerability-management-plan | - | Vulnerability management program |
| incident-response-plan | - | Incident response playbook |
| security-assessment | - | Security posture assessment |
| zero-trust-design | - | Zero trust architecture design |
| compliance-matrix | - | Regulatory compliance mapping |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

#### data.architect Agent
**Purpose**: Data architecture and governance artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| data-model | - | Logical/physical data models |
| schema-definition | - | Database schemas with constraints |
| data-flow-diagram | - | System data flows |
| data-dictionary | - | Data element definitions |
| data-governance-policy | - | Data governance framework |
| data-quality-framework | - | Data quality measurement |
| master-data-management-plan | - | MDM strategy |
| data-lineage-diagram | - | End-to-end data lineage |
| data-catalog | - | Enterprise data catalog |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

#### governance.manager Agent
**Purpose**: Program and project governance artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| project-charter | - | Project authority and scope |
| raid-log | - | Risks, Assumptions, Issues, Decisions |
| decision-log | - | Decision register |
| governance-framework | - | Governance structure and roles |
| compliance-matrix | - | Compliance requirements mapping |
| stakeholder-analysis | - | Stakeholder power/interest analysis |
| steering-committee-report | - | Executive reporting pack |
| change-control-process | - | Change management workflow |
| benefits-realization-plan | - | Benefits tracking framework |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

#### test.engineer Agent
**Purpose**: Testing and quality assurance artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| test-plan | - | Comprehensive test strategy |
| test-cases | - | Detailed test scenarios |
| test-results | - | Test execution results |
| test-automation-strategy | - | Automation framework selection |
| acceptance-criteria | - | User story acceptance criteria |
| performance-test-plan | - | Performance/load testing strategy |
| integration-test-plan | - | Integration testing approach |
| regression-test-suite | - | Regression test suite |
| quality-assurance-report | - | QA summary and metrics |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

#### deployment.engineer Agent
**Purpose**: Deployment and release artifacts

| Artifact Type | Schema | Description |
|---------------|--------|-------------|
| deployment-plan | - | Deployment strategy and procedures |
| cicd-pipeline-definition | - | CI/CD pipeline configuration |
| release-checklist | - | Pre-deployment checklist |
| rollback-plan | - | Rollback procedures |
| runbooks | - | Operational runbooks |
| infrastructure-as-code | - | Infrastructure provisioning templates |
| deployment-pipeline | - | Deployment automation scripts |
| smoke-test-suite | - | Post-deployment smoke tests |
| production-readiness-checklist | - | Production readiness assessment |

**Skills Used**: artifact.create, artifact.validate, artifact.review

---

### Core Skills

#### artifact.create
**Purpose**: Generate artifacts from templates

**Produces**: Any of the 406 registered artifact types
**Consumes**: User context/requirements

---

#### artifact.validate
**Purpose**: Validate artifact structure and quality

**Produces**: validation-report
**Consumes**: Any artifact type

---

#### artifact.review
**Purpose**: AI-powered content quality review

**Produces**: review-report
**Consumes**: Any artifact type

---

#### workflow.orchestrate
**Purpose**: Multi-artifact workflow coordination

**Produces**:
- workflow-execution-report
- artifact-manifest
- All artifacts in selected workflow

**Consumes**: User context for workflow initiation

---

## Consumer Map

### Artifacts by Consumer

| Artifact Type | Consumed By | Purpose |
|---------------|-------------|---------|
| business-case | governance.manager | Input for project charter |
| business-case | test.engineer | Understanding of business context |
| business-case | deployment.engineer | Release impact assessment |
| project-charter | All agents | Project scope and authority reference |
| threat-model | data.architect | Security requirements for data design |
| threat-model | deployment.engineer | Security controls for deployment |
| data-model | test.engineer | Test data requirements |
| data-model | deployment.engineer | Database deployment planning |
| test-plan | deployment.engineer | QA gates for deployment |
| architecture-* | security.architect | Architecture to threat model |
| architecture-* | test.engineer | System understanding for testing |
| requirements-* | All agents | Requirements as inputs |

---

## Artifact Dependency Graph

### SDLC Artifact Flow

```
Business Strategy
├── business-case (strategy.architect)
│   ├── project-charter (governance.manager) [depends-on: business-case]
│   │   ├── raid-log (governance.manager)
│   │   └── stakeholder-analysis (governance.manager)
│   └── portfolio-roadmap (strategy.architect)
│
Security & Compliance
├── threat-model (security.architect)
│   ├── security-architecture-diagram (security.architect) [depends-on: threat-model]
│   ├── compliance-matrix (governance.manager)
│   └── incident-response-plan (security.architect)
│
Data Architecture
├── data-model (data.architect)
│   ├── schema-definition (data.architect) [depends-on: data-model]
│   ├── data-flow-diagram (data.architect)
│   └── data-governance-policy (data.architect)
│
Testing
├── test-plan (test.engineer)
│   ├── test-cases (test.engineer) [depends-on: test-plan]
│   ├── test-automation-strategy (test.engineer)
│   └── acceptance-criteria (test.engineer)
│
Deployment
├── deployment-plan (deployment.engineer)
│   ├── cicd-pipeline-definition (deployment.engineer)
│   ├── runbooks (deployment.engineer)
│   └── rollback-plan (deployment.engineer) [depends-on: deployment-plan]
```

---

## Workflow Artifact Sets

### project-initiation Workflow
**Agents**: strategy.architect, governance.manager

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | business-case | strategy.architect | - |
| 2 | project-charter | governance.manager | business-case |
| 3 | raid-log | governance.manager | - |
| 3 | stakeholder-analysis | governance.manager | - |

---

### security-review Workflow
**Agents**: security.architect

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | threat-model | security.architect | - |
| 2 | security-architecture-diagram | security.architect | threat-model |
| 2 | security-assessment | security.architect | - |
| 3 | vulnerability-management-plan | security.architect | - |

---

### data-design Workflow
**Agents**: data.architect

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | data-model | data.architect | - |
| 2 | schema-definition | data.architect | data-model |
| 2 | data-flow-diagram | data.architect | - |
| 3 | data-governance-policy | data.architect | - |

---

### test-planning Workflow
**Agents**: test.engineer

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | test-plan | test.engineer | - |
| 2 | test-automation-strategy | test.engineer | - |
| 2 | acceptance-criteria | test.engineer | - |
| 3 | test-cases | test.engineer | test-plan |

---

### deployment-planning Workflow
**Agents**: deployment.engineer

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | deployment-plan | deployment.engineer | - |
| 2 | cicd-pipeline-definition | deployment.engineer | - |
| 2 | runbooks | deployment.engineer | - |
| 3 | rollback-plan | deployment.engineer | deployment-plan |

---

### full-sdlc Workflow
**Agents**: strategy.architect, governance.manager, security.architect, data.architect, test.engineer, deployment.engineer

| Priority | Artifact | Agent | Depends On |
|----------|----------|-------|------------|
| 1 | business-case | strategy.architect | - |
| 2 | project-charter | governance.manager | business-case |
| 3 | threat-model | security.architect | - |
| 3 | data-model | data.architect | - |
| 4 | test-plan | test.engineer | threat-model, data-model |
| 5 | deployment-plan | deployment.engineer | test-plan |

---

## Agent Capability Matrix

| Artifact Category | Primary Agent | Secondary Agents | Key Skills |
|-------------------|---------------|------------------|------------|
| Business Strategy | strategy.architect | - | artifact.create, artifact.validate, artifact.review |
| Governance | governance.manager | - | artifact.create, artifact.validate, artifact.review |
| Security | security.architect | - | artifact.create, artifact.validate, artifact.review |
| Data Architecture | data.architect | - | artifact.create, artifact.validate, artifact.review |
| Testing | test.engineer | - | artifact.create, artifact.validate, artifact.review |
| Deployment | deployment.engineer | - | artifact.create, artifact.validate, artifact.review |
| Workflows | workflow.orchestrate | All agents | artifact.create, artifact.validate |
| Quality Assurance | artifact.validate, artifact.review | - | - |

---

## Usage Patterns

### Pattern 1: Single Artifact Creation
```bash
# Use specific agent for artifact type
# Example: strategy.architect for business-case
```

### Pattern 2: Workflow Execution
```bash
# Use workflow.orchestrate for multi-artifact sets
python3 skills/workflow.orchestrate/workflow_orchestrate.py \
  project-initiation \
  "Cloud migration program" \
  ./artifacts/cloud-migration
```

### Pattern 3: Custom Artifact Chain
```bash
# Create artifacts sequentially with dependencies
# 1. Create business-case with strategy.architect
# 2. Create project-charter with governance.manager (references business-case)
# 3. Create threat-model with security.architect
# 4. Create test-plan with test.engineer (references threat-model)
```

---

## Artifact Traceability

### Upstream Dependencies
Artifacts that commonly serve as inputs to others:
- `business-case` → `project-charter`, `portfolio-roadmap`
- `threat-model` → `security-architecture-diagram`, `incident-response-plan`
- `data-model` → `schema-definition`, `data-flow-diagram`
- `test-plan` → `test-cases`, `test-automation-strategy`
- `deployment-plan` → `rollback-plan`, `runbooks`

### Downstream Consumers
Artifacts that commonly reference others:
- `project-charter` ← `business-case`
- `test-cases` ← `test-plan`, `requirements-specification`
- `deployment-plan` ← `test-plan`, `infrastructure-as-code`
- `security-architecture-diagram` ← `threat-model`, `compliance-matrix`

---

## Future Extensions

### Planned Additions
- **requirements.engineer** agent for requirements artifacts
- **architecture.designer** agent for architecture diagrams
- **product.manager** agent for product artifacts
- **release.manager** agent for release management
- Additional workflow types for specialized SDLC patterns

### Enhanced Traceability
- Automatic dependency resolution
- Impact analysis (what artifacts are affected by changes)
- Coverage analysis (which requirements are tested/implemented)
- Compliance tracing (which controls address which threats)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-10-25 | Initial producer/consumer map for Phase 3 |

---

## See Also

- [ARTIFACT_FRAMEWORK_INTEGRATION.md](ARTIFACT_FRAMEWORK_INTEGRATION.md) - Architecture overview
- [ARTIFACT_USAGE_GUIDE.md](ARTIFACT_USAGE_GUIDE.md) - Usage patterns
- [PHASE3_COMPLETE.md](../PHASE3_COMPLETE.md) - Phase 3 implementation details
