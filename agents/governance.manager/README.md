# Governance.Manager Agent

## Purpose

Create comprehensive program and project governance artifacts including project charters, RAID logs (Risks, Assumptions, Issues, Decisions), decision logs, governance frameworks, compliance matrices, and steering committee artifacts. Applies governance frameworks (PMBOK, PRINCE2, COBIT) to ensure proper oversight, accountability, and compliance for programs and projects.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `Program or project description`
- `Stakeholders and governance structure`
- `Objectives and success criteria`
- `Compliance or regulatory requirements`
- `Risks, issues, and assumptions`
- `Decisions to be documented`

### Produces

- `project-charter: Project charter with authority, scope, objectives, and success criteria`
- `raid-log: Comprehensive RAID log`
- `decision-log: Decision register with context, options, rationale, and outcomes`
- `governance-framework: Governance structure with roles, committees, and decision rights`
- `compliance-matrix: Compliance mapping to regulatory and policy requirements`
- `stakeholder-analysis: Stakeholder analysis with power/interest grid and engagement strategy`
- `steering-committee-report: Executive steering committee reporting pack`
- `change-control-process: Change management and approval workflow`
- `benefits-realization-plan: Benefits tracking and realization framework`

## Example Use Cases

- Project purpose and business justification
- Scope and deliverables (migrate 50 applications to AWS)
- Objectives and success criteria (90% cost reduction, zero downtime)
- Authority and decision rights
- Governance structure (steering committee, PMO oversight)
- Budget and resource allocation
- Assumptions and constraints
- Approval signatures
- Risks: 15-20 identified risks with impact, probability, mitigation
- Assumptions: Business continuity, vendor SLAs, budget availability
- Issues: Current issues with severity, owner, and resolution plan
- Decisions: Key decisions with rationale and stakeholder approval
- Cross-references to related artifacts
- Governance structure (executive steering, program board, workstream leads)
- Decision-making authority and escalation paths
- Meeting cadence and reporting requirements
- RACI matrix for key decisions and deliverables
- Compliance and risk management processes
- Change control and approval workflow

## Usage

```bash
# Activate the agent
/agent governance.manager

# Or invoke directly
betty agent run governance.manager --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
