# Name: governance.manager

# Purpose:
Create comprehensive program and project governance artifacts including project charters, RAID logs (Risks, Assumptions, Issues, Decisions), decision logs, governance frameworks, compliance matrices, and steering committee artifacts. Applies governance frameworks (PMBOK, PRINCE2, COBIT) to ensure proper oversight, accountability, and compliance for programs and projects.

# Inputs:
- Program or project description
- Stakeholders and governance structure
- Objectives and success criteria
- Compliance or regulatory requirements
- Risks, issues, and assumptions (optional)
- Decisions to be documented (optional)

# Outputs:
- project-charter: Project charter with authority, scope, objectives, and success criteria
- raid-log: Comprehensive RAID log (Risks, Assumptions, Issues, Decisions)
- decision-log: Decision register with context, options, rationale, and outcomes
- governance-framework: Governance structure with roles, committees, and decision rights
- compliance-matrix: Compliance mapping to regulatory and policy requirements
- stakeholder-analysis: Stakeholder analysis with power/interest grid and engagement strategy
- steering-committee-report: Executive steering committee reporting pack
- change-control-process: Change management and approval workflow
- benefits-realization-plan: Benefits tracking and realization framework

# Constraints:
- Must define clear governance structure and roles
- Should include decision-making authority and escalation
- Must track risks with mitigation strategies
- Should map to compliance frameworks (SOX, GDPR, COBIT)
- Must ensure audit trail for decisions
- Should align with organizational governance standards

# Examples:

## Example 1: Create Project Charter
Input: "Cloud migration program for enterprise applications. $10M budget, 18-month timeline. Executive sponsor: CTO. Governance through steering committee."

Output: Generates project-charter.yaml with:
- Project purpose and business justification
- Scope and deliverables (migrate 50 applications to AWS)
- Objectives and success criteria (90% cost reduction, zero downtime)
- Authority and decision rights
- Governance structure (steering committee, PMO oversight)
- Budget and resource allocation
- Assumptions and constraints
- Approval signatures

## Example 2: RAID Log Management
Input: "Large-scale system integration project with multiple vendor dependencies and regulatory compliance requirements."

Output: Generates raid-log.yaml with:
- Risks: 15-20 identified risks with impact, probability, mitigation
- Assumptions: Business continuity, vendor SLAs, budget availability
- Issues: Current issues with severity, owner, and resolution plan
- Decisions: Key decisions with rationale and stakeholder approval
- Cross-references to related artifacts

## Example 3: Governance Framework
Input: "Establish program governance for digital transformation initiative spanning 5 workstreams with 100+ team members."

Output: Generates governance-framework.yaml with:
- Governance structure (executive steering, program board, workstream leads)
- Decision-making authority and escalation paths
- Meeting cadence and reporting requirements
- RACI matrix for key decisions and deliverables
- Compliance and risk management processes
- Change control and approval workflow
