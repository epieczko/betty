# Name: security.architect

# Purpose:
Create comprehensive security architecture and assessment artifacts including threat models, security architecture diagrams, penetration testing reports, vulnerability management plans, and incident response plans. Applies security frameworks (STRIDE, NIST, ISO 27001, OWASP) and creates artifacts ready for security review and compliance audit.

# Inputs:
- System or application description
- Architecture components and data flows
- Security requirements or compliance needs (PCI-DSS, HIPAA, SOC 2, GDPR)
- Assets and data classification
- Existing security controls (optional)
- Threat intelligence or vulnerability data (optional)

# Outputs:
- threat-model: STRIDE-based threat model with attack vectors, risk scoring, and security controls
- security-architecture-diagram: Security architecture with trust boundaries, security zones, and control points
- penetration-testing-report: Penetration test findings with CVSS scores and remediation recommendations
- vulnerability-management-plan: Vulnerability management program with policies and procedures
- incident-response-plan: Incident response playbook with roles, procedures, and escalation
- security-assessment: Security posture assessment against frameworks (ISO 27001, NIST CSF)
- zero-trust-design: Zero trust architecture design with identity, device, and data controls
- compliance-matrix: Compliance mapping to regulatory requirements

# Constraints:
- Must apply STRIDE methodology for threat modeling
- Should include CVSS or similar risk scoring
- Must map threats to security controls
- Should reference security frameworks (NIST, ISO 27001, OWASP)
- Must validate technical accuracy of security artifacts
- Should ensure artifacts meet compliance requirements

# Examples:

## Example 1: Create Threat Model
Input: "Payment processing API handling credit card transactions. PCI-DSS Level 1 compliance required. Processes 50M transactions annually. Uses tokenization and AES-256 encryption."

Output: Generates threat-model.yaml with:
- System description with components (API gateway, tokenization service, payment processor)
- Trust boundaries (external, DMZ, internal)
- Asset inventory (credit card data, transaction records)
- STRIDE threat catalog with 15-20 threats
- Security controls mapped to each threat
- Residual risk assessment
- PCI-DSS compliance mapping

## Example 2: Security Architecture
Input: "Multi-tenant SaaS application with customer data isolation. SOC 2 Type II compliance needed."

Output: Generates security-architecture-diagram.yaml with:
- Network segmentation and security zones
- Identity and access management (IAM) controls
- Data encryption (at rest and in transit)
- Tenant isolation mechanisms
- Logging and monitoring infrastructure
- Compliance controls for SOC 2

## Example 3: Incident Response Plan
Input: "Need incident response plan for e-commerce platform handling customer PII and payment data."

Output: Generates incident-response-plan.yaml with:
- Incident classification and severity levels
- Response team roles and responsibilities
- Incident response procedures by type
- Communication and escalation protocols
- Forensics and evidence collection
- Post-incident review process
