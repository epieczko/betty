# Skill Description: threat.model.generate

## Overview
Create STRIDE-based threat models with attack trees, risk scoring, and control recommendations using Microsoft threat modeling methodology.

## Skill Name
`threat.model.generate`

## Purpose
Generate comprehensive threat models that identify security threats using the STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege). This skill goes beyond simple template filling to provide intelligent threat analysis based on system architecture.

## Inputs

### Required
- **system_description** (string): Detailed description of the system architecture, components, and functionality to be threat modeled

### Optional
- **data_flows** (object): Data flows between components. If not provided, skill will attempt to infer from system description
- **trust_boundaries** (array): Trust boundaries in the system (e.g., "Internet/DMZ", "DMZ/Internal Network"). Auto-detected if not provided
- **assets** (array): Critical assets to protect (data, services, credentials). Auto-detected if not provided
- **frameworks** (array): Threat modeling frameworks to apply. Default: ["STRIDE"]. Options: STRIDE, PASTA, LINDDUN
- **risk_tolerance** (enum): Organization's risk tolerance. Options: low, medium, high. Default: medium
- **output_path** (string): Path where threat model should be saved. Default: "./threat-model.yaml"

## Outputs

- **threat_model** (object): Complete threat model object with threats, risks, and mitigations
- **threat_model_file** (string): Path to generated threat model YAML file
- **threat_count** (number): Total number of threats identified
- **high_risk_count** (number): Number of high-risk threats (CVSS >= 7.0)
- **coverage_report** (object): STRIDE coverage analysis showing which threat categories were analyzed

## Artifact Metadata

### Produces
- **threat-model**: STRIDE-based threat model with attack vectors, risk scoring (CVSS), and security controls
  - File pattern: `*.threat-model.yaml`
  - Content type: `application/yaml`
  - Schema: `schemas/artifacts/threat-model-schema.json`

### Consumes (Optional - enriches threat model if available)
- **architecture-overview**: System architecture description
  - File pattern: `*.architecture-overview.md`
  - Content type: `text/markdown`

- **data-flow-diagram**: Data flows to identify threat vectors
  - File pattern: `*.data-flow-diagram.drawio`
  - Content type: `application/xml`

- **data-model**: Data structures and sensitive data to protect
  - File pattern: `*.data-model.yaml`
  - Content type: `application/yaml`

## Implementation Requirements

### Core Logic
1. **Parse system description** to identify:
   - Components (web servers, databases, APIs, services)
   - Trust boundaries (Internet, DMZ, Internal Network, Database tier)
   - Data flows (authentication, data storage, external APIs)
   - Assets (user credentials, PII, financial data, API keys)

2. **Apply STRIDE methodology** for each component and data flow:
   - **S**poofing: Can attacker impersonate users/systems?
   - **T**ampering: Can attacker modify data/code?
   - **R**epudiation: Can actions be denied/hidden?
   - **I**nformation Disclosure: Can sensitive data be exposed?
   - **D**enial of Service: Can system availability be disrupted?
   - **E**levation of Privilege: Can attacker gain unauthorized access?

3. **Calculate risk scores** using CVSS 3.1:
   - Base score: Exploitability + Impact
   - Temporal score: Account for exploit availability
   - Environmental score: Adjusted for organization context

4. **Recommend mitigations** for each threat:
   - Preventive controls (authentication, encryption, input validation)
   - Detective controls (logging, monitoring, alerting)
   - Responsive controls (incident response, backup/recovery)

5. **Generate attack trees** showing attack paths and prerequisites

### Data Structures

#### Threat Object
```yaml
threat:
  id: TM-001
  title: "SQL Injection in User Login"
  category: Tampering
  description: "Attacker can inject SQL code through login form"
  affected_component: "Web Application - Login Form"
  attack_vector: "User-supplied input to SQL query"
  likelihood: High
  impact: High
  cvss_score: 9.3
  cvss_vector: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N"
  mitigations:
    - control: "Use parameterized queries"
      status: recommended
      effectiveness: high
    - control: "Input validation and sanitization"
      status: recommended
      effectiveness: medium
  references:
    - "OWASP Top 10 - A03:2021 Injection"
    - "CWE-89: SQL Injection"
```

### STRIDE Templates
The skill should include built-in templates for each STRIDE category with common threats:

- `stride_templates/spoofing.yaml`: Impersonation, credential theft, session hijacking
- `stride_templates/tampering.yaml`: Data modification, code injection, parameter manipulation
- `stride_templates/repudiation.yaml`: Log manipulation, non-repudiation failures
- `stride_templates/information_disclosure.yaml`: Data leaks, insufficient encryption, information exposure
- `stride_templates/denial_of_service.yaml`: Resource exhaustion, flood attacks, algorithmic complexity
- `stride_templates/elevation_of_privilege.yaml`: Privilege escalation, authentication bypass, authorization failures

### CVSS Scoring Logic
Implement CVSS 3.1 calculator with:
- Attack Vector (AV): Network, Adjacent, Local, Physical
- Attack Complexity (AC): Low, High
- Privileges Required (PR): None, Low, High
- User Interaction (UI): None, Required
- Scope (S): Unchanged, Changed
- Confidentiality (C): None, Low, High
- Integrity (I): None, Low, High
- Availability (A): None, Low, High

## Permissions
- `filesystem:read` - Read architecture diagrams, data models if provided
- `filesystem:write` - Write threat model to output file

## Tags
- security
- threat-modeling
- stride
- risk-assessment
- cvss

## Dependencies
- PyYAML (for YAML parsing/generation)
- jsonschema (for threat model validation)

## Usage Examples

### Example 1: Basic E-commerce Platform
```bash
betty skill threat.model.generate \
  --system_description "E-commerce web application with React frontend, Node.js API, PostgreSQL database. Handles customer PII, payment card data (processed by Stripe), and order information. Deployed on AWS with CloudFront CDN." \
  --output_path security/threat-model.yaml
```

### Example 2: Microservices Architecture
```bash
betty skill threat.model.generate \
  --system_description "Microservices architecture with 5 services: Auth Service (JWT), User Service, Order Service, Payment Service (PCI-DSS scope), Notification Service. Message queue via RabbitMQ. API Gateway with rate limiting." \
  --trust_boundaries '["Internet/API Gateway", "API Gateway/Internal Services", "Services/Database"]' \
  --risk_tolerance low \
  --output_path architecture/threat-model.yaml
```

### Example 3: With Existing Architecture Artifacts
```bash
betty skill threat.model.generate \
  --system_description "Healthcare patient portal" \
  --architecture_overview docs/architecture-overview.md \
  --data_model schemas/data-model.yaml \
  --frameworks '["STRIDE", "LINDDUN"]' \
  --output_path compliance/threat-model.yaml
```

## Integration with Agents

This skill is designed to be used by the `security.architect` agent as part of comprehensive security assessment workflows:

```yaml
# security.architect workflow
1. threat.model.generate → Generate threat model
2. compliance.matrix.generate → Map threats to compliance controls
3. security.gap.analyze → Identify unmitigated threats
4. artifact.review → Quality check
5. Output: Complete security assessment package
```

## Success Criteria

A successful threat model should:
- ✅ Cover all STRIDE categories for each component
- ✅ Identify at least 80% of common threats (validated against OWASP Top 10, CWE Top 25)
- ✅ Provide actionable mitigations for each threat
- ✅ Include accurate CVSS scores
- ✅ Pass validation against `threat-model-schema.json`
- ✅ Be ready for security review without manual editing

## Quality Standards

- Threat coverage: ≥80% of attack surface analyzed
- Risk scoring: CVSS 3.1 compliant
- Mitigation quality: Each threat has ≥2 recommended controls
- Documentation: Each threat includes references (OWASP, CWE, CAPEC)
- Validation: Passes schema validation
- Performance: Complete threat model in <30 seconds for typical system

## References

- [Microsoft Threat Modeling Tool](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [STRIDE Methodology](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [CVSS 3.1 Specification](https://www.first.org/cvss/v3.1/specification-document)
- [NIST SP 800-154: Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/publications/detail/sp/800-154/draft)
