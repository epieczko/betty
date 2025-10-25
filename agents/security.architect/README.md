# Security.Architect Agent

## Purpose

Create comprehensive security architecture and assessment artifacts including threat models, security architecture diagrams, penetration testing reports, vulnerability management plans, and incident response plans. Applies security frameworks (STRIDE, NIST, ISO 27001, OWASP) and creates artifacts ready for security review and compliance audit.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `System or application description`
- `Architecture components and data flows`
- `Security requirements or compliance needs`
- `Assets and data classification`
- `Existing security controls`
- `Threat intelligence or vulnerability data`

### Produces

- `threat-model: STRIDE-based threat model with attack vectors, risk scoring, and security controls`
- `security-architecture-diagram: Security architecture with trust boundaries, security zones, and control points`
- `penetration-testing-report: Penetration test findings with CVSS scores and remediation recommendations`
- `vulnerability-management-plan: Vulnerability management program with policies and procedures`
- `incident-response-plan: Incident response playbook with roles, procedures, and escalation`
- `security-assessment: Security posture assessment against frameworks`
- `zero-trust-design: Zero trust architecture design with identity, device, and data controls`
- `compliance-matrix: Compliance mapping to regulatory requirements`

## Example Use Cases

- System description with components (API gateway, tokenization service, payment processor)
- Trust boundaries (external, DMZ, internal)
- Asset inventory (credit card data, transaction records)
- STRIDE threat catalog with 15-20 threats
- Security controls mapped to each threat
- Residual risk assessment
- PCI-DSS compliance mapping
- Network segmentation and security zones
- Identity and access management (IAM) controls
- Data encryption (at rest and in transit)
- Tenant isolation mechanisms
- Logging and monitoring infrastructure
- Compliance controls for SOC 2
- Incident classification and severity levels
- Response team roles and responsibilities
- Incident response procedures by type
- Communication and escalation protocols
- Forensics and evidence collection
- Post-incident review process

## Usage

```bash
# Activate the agent
/agent security.architect

# Or invoke directly
betty agent run security.architect --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
