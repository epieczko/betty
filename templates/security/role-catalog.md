# Security Role Catalog

**Document Version:** 2.4.0
**Last Updated:** 2024-10-26
**Owner:** Identity and Access Management Team
**Classification:** Internal
**Status:** Active

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ROLE-CAT-2024-001 |
| Total Roles | 42 |
| Active Roles | 38 |
| Deprecated Roles | 4 |
| Last Review Date | 2024-10-15 |
| Next Review Date | 2024-11-15 |
| Compliance Frameworks | NIST RBAC Model, ISO 27001, Zero Trust |

## Executive Summary

This Security Role Catalog defines all security and system roles within the organization, aligned with NIST RBAC (Role-Based Access Control) model, ISO 27001 standards, and Zero Trust principles. Each role specifies responsibilities, required skills, certifications, experience requirements, and access levels necessary for security operations, engineering, and governance functions.

**Catalog Statistics:**
- Executive & Management Roles: 9
- Security Engineering Roles: 12
- Security Operations Roles: 11
- Governance, Risk & Compliance Roles: 6
- Specialized Security Roles: 4

---

## Role Categories

### Executive & Management Roles

#### Chief Information Security Officer (CISO)

**Role ID:** EXEC-001
**Role Type:** Executive
**Department:** Information Security
**Reports To:** CEO

**Description:**
Executive responsible for organization's information security strategy, governance, risk management, and compliance programs. Sets security direction and oversees all security functions.

**Primary Responsibilities:**
- Define and maintain organizational security strategy and vision
- Oversee enterprise security risk management program
- Ensure compliance with regulatory and industry security requirements
- Lead security governance and policy framework
- Manage security budget and resource allocation ($5M+ annually)
- Report security posture to board and executive leadership

**Required Skills:**
- **Technical:** Enterprise security architecture, Risk management frameworks (NIST, ISO 27001), Cloud security (AWS, Azure, GCP)
- **Business:** Executive leadership, Strategic planning, Vendor management, Board-level reporting
- **Certifications Required:** CISSP, CISM
- **Certifications Preferred:** CRISC, CGEIT

**Experience Requirements:**
- 15+ years total experience
- 10+ years in leadership roles
- Industry experience in technology or related field

**Access Requirements:**
- Clearance Level: Executive
- Background Check: Enhanced
- MFA Required: Yes
- Privileged Access: Yes

**Tools & Systems:**
- Executive dashboards and BI tools
- GRC platforms (Archer, ServiceNow GRC)
- Risk management systems
- Board reporting tools

**Delegation Authority:**
- Budget Approval: Unlimited
- Personnel Actions: Full authority for security org
- Policy Approval: All security policies
- Vendor Contracts: Up to $5M

---

### Security Operations Roles

#### SOC Analyst - Tier 3 (Senior)

**Role ID:** SOC-001
**Role Type:** Individual Contributor
**Level:** Senior
**Department:** Security Operations Center
**Reports To:** Security Manager

**Description:**
Senior SOC analyst responsible for advanced threat hunting, complex incident investigation, and tier 2/3 escalations. Leads incident response efforts and develops detection content.

**Primary Responsibilities:**
- Conduct proactive threat hunting activities
- Lead complex security incident investigations
- Develop and tune security detection rules (SIEM, EDR)
- Perform malware and forensic analysis
- Mentor tier 1 and tier 2 analysts
- Coordinate with external threat intelligence sources

**Secondary Responsibilities:**
- Develop incident response playbooks
- Participate in purple team exercises
- Contribute to security architecture improvements

**Required Skills:**
- **Technical:**
  - SIEM platforms (Splunk, Elastic, Sentinel)
  - EDR/XDR platforms (CrowdStrike, SentinelOne)
  - Network traffic analysis (Wireshark, Zeek)
  - Malware analysis and reverse engineering
  - MITRE ATT&CK framework
  - Threat intelligence platforms
  - Digital forensics

- **Analysis Skills:**
  - Advanced log analysis
  - Memory forensics
  - Network forensics
  - Behavioral analysis

- **Certifications Required:** GCIH, GCIA, or equivalent
- **Certifications Preferred:** GREM, GCFA, CISSP

**Experience Requirements:**
- 6+ years total experience
- 5+ years SOC or incident response
- 2+ years threat hunting
- Experience with multiple SIEM platforms

**Work Schedule:**
- Shift Work: Yes (rotating including nights/weekends)
- On-Call: Yes
- Schedule Flexibility: Rotating shifts

**Typical Tools:**
- SIEM: Splunk, Elastic Security
- EDR: CrowdStrike, SentinelOne
- Threat Intelligence: MISP, ThreatConnect
- Forensics: EnCase, FTK, Volatility
- Network Analysis: Wireshark, Zeek
- Malware Sandboxes: Cuckoo, ANY.RUN

---

#### SOC Analyst - Tier 2

**Role ID:** SOC-002
**Level:** Mid-Level
**Reports To:** Security Manager

**Description:**
Intermediate SOC analyst performing triage, investigation, and response to security alerts. Handles escalations from Tier 1 and escalates complex issues to Tier 3.

**Primary Responsibilities:**
- Investigate security alerts and incidents
- Perform initial containment actions
- Conduct host and network-based analysis
- Document incidents and findings
- Escalate complex incidents to Tier 3
- Tune detection rules to reduce false positives

**Required Skills:**
- SIEM query languages (SPL, KQL)
- Log analysis and correlation
- Basic malware analysis
- Network protocols and analysis
- Windows and Linux security

**Certifications:**
- Required: Security+ or GIAC GSEC
- Preferred: GCIH, CEH

**Experience:** 3+ years (2+ years SOC)

**Work Schedule:** Shift work required, on-call rotation

---

#### SOC Analyst - Tier 1

**Role ID:** SOC-003
**Level:** Entry
**Reports To:** SOC Team Lead

**Description:**
Entry-level SOC analyst responsible for monitoring security alerts, performing initial triage, and escalating incidents according to established procedures.

**Primary Responsibilities:**
- Monitor security alerts and events
- Perform initial triage and classification
- Execute runbooks and playbooks
- Escalate incidents per SOP
- Document all activities in ticketing system

**Required Skills:**
- Basic networking fundamentals
- Operating system fundamentals (Windows, Linux)
- Security concepts and terminology
- Log analysis basics

**Certifications:**
- Required: Security+
- Preferred: Network+, CySA+

**Experience:** 1+ years (IT or security internship acceptable)

**Work Schedule:** Shift work required, no on-call initially

---

### Security Engineering Roles

#### Senior Security Engineer

**Role ID:** ENG-001
**Level:** Senior
**Department:** Security Engineering
**Reports To:** Security Manager

**Description:**
Senior-level security engineer responsible for designing, implementing, and maintaining security controls, tools, and infrastructure. Provides technical leadership and mentorship.

**Primary Responsibilities:**
- Design and implement security controls and solutions
- Develop and maintain security automation and tooling
- Conduct security architecture reviews
- Lead security projects and initiatives
- Mentor junior security engineers
- Research and evaluate new security technologies

**Required Skills:**
- **Technical:**
  - Cloud security (AWS, Azure, GCP)
  - Infrastructure as Code (Terraform, CloudFormation)
  - Security automation and scripting (Python, Go)
  - Container and Kubernetes security
  - Network security and architecture
  - Identity and access management

- **Programming Languages:** Python, Bash/Shell, Go or Rust

- **Certifications Required:** CISSP, OSCP, or equivalent
- **Certifications Preferred:** AWS Security Specialty, GPEN, GXPN, CKS

**Experience:**
- 7+ years total
- 5+ years security engineering
- 3+ years cloud security
- 2+ years infrastructure automation

**Typical Tools:**
- Cloud platforms (AWS, Azure, GCP)
- IaC tools (Terraform, Ansible)
- Security scanning tools (Prisma Cloud, Wiz)
- SIEM and logging platforms
- Secrets management (Vault, AWS Secrets Manager)
- CI/CD platforms

---

### Application Security Roles

#### Application Security Engineer

**Role ID:** APPSEC-001
**Level:** Mid-Senior
**Reports To:** Security Manager

**Description:**
Ensures security of applications through secure development practices, security testing, code review, and developer enablement.

**Primary Responsibilities:**
- Conduct application security assessments and penetration testing
- Perform security code reviews
- Develop and maintain secure coding standards
- Integrate security into CI/CD pipelines
- Train developers on secure coding practices
- Manage application security tools (SAST, DAST, SCA)

**Required Skills:**
- Web application security (OWASP Top 10)
- Secure coding practices (Java, Python, JavaScript, Go)
- Application security testing (SAST, DAST, IAST)
- API security
- Container and serverless security
- Security testing frameworks (Burp Suite, ZAP)

**Programming Languages:** At least 3 of: Java, Python, JavaScript/TypeScript, Go, C#

**Certifications:**
- Required: OSWE, GWAPT, or equivalent
- Preferred: CSSLP, GWEB

**Experience:**
- 5+ years total
- 4+ years application security
- 3+ years software development or security testing

**Tools:**
- SAST: SonarQube, Checkmarx
- DAST: Burp Suite, ZAP
- SCA: Snyk, Dependabot
- Container Security: Trivy, Grype

---

### Governance, Risk & Compliance Roles

#### Security Compliance Manager

**Role ID:** GRC-001
**Role Type:** Management
**Reports To:** CISO

**Description:**
Manages security compliance programs including SOC 2, ISO 27001, PCI DSS, and other regulatory requirements. Coordinates audits and ensures ongoing compliance.

**Primary Responsibilities:**
- Manage compliance programs (SOC 2, ISO 27001, PCI DSS)
- Coordinate internal and external audits
- Maintain compliance documentation and evidence
- Implement compliance controls and frameworks
- Track and report compliance metrics
- Conduct risk assessments

**Required Skills:**
- **Technical:** Compliance frameworks (SOC 2, ISO 27001, PCI DSS, NIST), GRC platforms (Archer, ServiceNow GRC, Vanta), Risk assessment methodologies, Audit management
- **Business:** Project management, Stakeholder management, Documentation and reporting

**Certifications:**
- Required: CISSP, CISA, or CRISC
- Preferred: ISO 27001 Lead Auditor, CISM

**Experience:**
- 7+ years total
- 5+ years compliance or audit
- 3+ years managing audit programs

---

### Specialized Security Roles

#### Penetration Tester (Senior)

**Role ID:** PENTEST-001
**Level:** Senior

**Description:**
Conducts advanced penetration testing and security assessments across applications, infrastructure, and networks. Simulates real-world attacks to identify vulnerabilities.

**Primary Responsibilities:**
- Conduct penetration tests (web, mobile, API, infrastructure)
- Perform red team exercises
- Identify and exploit vulnerabilities
- Develop proof-of-concept exploits
- Write detailed technical reports
- Provide remediation guidance to development teams

**Required Skills:**
- Advanced penetration testing methodologies
- Vulnerability assessment and exploitation
- Web application testing (OWASP)
- Network penetration testing
- Active Directory attacks
- Cloud penetration testing
- Social engineering techniques

**Programming Languages:** Python, Bash/PowerShell, Go or C/C++

**Certifications:**
- Required: OSCP
- Preferred: OSEP, OSED, OSWE, GPEN, GXPN, GWAPT

**Experience:**
- 6+ years total
- 5+ years penetration testing
- Experience with multiple attack techniques and tools

**Tools:**
- Burp Suite Professional
- Metasploit Framework
- Cobalt Strike
- BloodHound / SharpHound
- Custom exploitation tools

---

## Career Paths

### Security Operations Path

| Level | Role | Typical Duration |
|-------|------|------------------|
| Entry | SOC Analyst - Tier 1 | 1-2 years |
| Mid | SOC Analyst - Tier 2 | 2-3 years |
| Senior | SOC Analyst - Tier 3 | 3+ years |
| Lead | SOC Team Lead / Incident Response Lead | Variable |
| Management | Security Manager | - |

### Security Engineering Path

| Level | Role | Typical Duration |
|-------|------|------------------|
| Mid | Security Engineer | 2-3 years |
| Senior | Senior Security Engineer | 3-5 years |
| Principal/Staff | Staff Security Engineer / Security Architect | 5+ years |
| Management | Security Manager / Director | - |

---

## Role Assignment Policies

### Approval Requirements

**Standard Roles:**
- Approvers: Hiring Manager, IAM Team
- SLA: 3 business days

**Privileged Roles:**
- Approvers: Hiring Manager, Security Manager, CISO
- SLA: 5 business days
- Additional Requirements:
  - Background check completion
  - Security clearance (if applicable)
  - Training completion

**Executive Roles:**
- Approvers: CISO, CEO
- Additional Requirements:
  - Enhanced background check
  - Board approval (for C-level)

### Onboarding Requirements

**All Roles:**
- Complete security awareness training
- Sign acceptable use policy
- MFA enrollment
- Review role-specific policies

**Technical Roles:**
- Complete hands-on tool training
- Shadow senior team member (1 week minimum)
- Review relevant runbooks and procedures

**Privileged Roles:**
- Enhanced security training
- Privileged access agreement signed
- Manager review of access requirements

### Access Reviews

- **Frequency:** Quarterly
- **Scope:** Validate role assignments, review privileged access, check for role accumulation, verify separation of duties
- **Remediation SLA:** 10 business days

---

## Change History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 2.4.0 | 2024-10-26 | Patricia Williams, IAM Director | Added 4 new cloud security roles, updated certification requirements, enhanced career paths | Michael Zhang, CISO |
| 2.0.0 | 2024-06-01 | James Cooper, Security Architect | Major restructure for new security operating model, consolidated 8 legacy roles | Michael Zhang, CISO |
| 1.0.0 | 2024-01-05 | Patricia Williams, IAM Director | Initial role catalog with 30 security roles | CISO |

---

**Next Review Date:** 2024-11-15
**Review Frequency:** Monthly
**Document Owner:** IAM Director
**Compliance Frameworks:** NIST RBAC Model, ISO 27001, Zero Trust Architecture
