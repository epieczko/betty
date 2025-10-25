# Name: baseline-hardening-guides

## Executive Summary

The Baseline Hardening Guides establish comprehensive security configuration standards for operating systems, network devices, databases, cloud platforms, and enterprise applications based on industry-recognized benchmarks including CIS (Center for Internet Security) Benchmarks, DISA STIGs (Defense Information Systems Agency Security Technical Implementation Guides), vendor security baselines (Microsoft Security Baselines, AWS Security Best Practices, Google Cloud Platform hardening guides), and regulatory requirements (NIST SP 800-53, PCI DSS, HIPAA, FedRAMP).

These technical hardening guides provide step-by-step configuration instructions, automated remediation scripts (PowerShell, Bash, Ansible, Chef, Puppet), and compliance validation procedures using Security Content Automation Protocol (SCAP) scanners (OpenSCAP, SCAP Compliance Checker, Nessus, Qualys Policy Compliance), configuration management tools, and cloud security posture management (CSPM) platforms (Prisma Cloud, Wiz, Orca Security, Microsoft Defender for Cloud). Hardening standards cover Windows Server 2016/2019/2022, RHEL/CentOS 7/8/9, Ubuntu 20.04/22.04, network devices (Cisco IOS, Palo Alto PAN-OS, Fortinet FortiOS), databases (Oracle, SQL Server, PostgreSQL, MySQL), cloud IaaS/PaaS (AWS EC2, Azure VMs, GCP Compute), Kubernetes/containers, and enterprise applications (Active Directory, Exchange, SharePoint).

Configuration domains include account management (password complexity, account lockout, privileged account restrictions), authentication mechanisms (MFA enforcement, Kerberos settings, certificate-based authentication), audit logging (event log sizing, retention, forwarding to SIEM), network security (firewall rules, port restrictions, protocol disable), service hardening (unnecessary service disable, service account least privilege), patch management (automatic updates, testing procedures), encryption (BitLocker, LUKS, TLS 1.2+ enforcement), and application allowlisting (AppLocker, Windows Defender Application Control).

### Strategic Importance

- **Attack Surface Reduction**: Eliminates unnecessary services, protocols, accounts, and software to minimize exploitable vulnerabilities; disables legacy protocols (SMBv1, TLS 1.0/1.1, weak ciphers)
- **Compliance & Audit Readiness**: Satisfies mandatory security configuration requirements for SOC 2, ISO 27001, PCI DSS 2.2.2, HIPAA 164.312, FedRAMP, CMMC, and government contracts requiring DISA STIG compliance
- **Consistent Security Posture**: Establishes repeatable, automated configuration standards across thousands of systems; prevents configuration drift through continuous compliance monitoring
- **Privileged Access Governance**: Implements least privilege principles for local admin rights, service accounts, database permissions, and cloud IAM roles; restricts administrative console access
- **Defense-in-Depth**: Provides foundational security layer that complements network controls, endpoint protection, and application security; increases attacker effort required for lateral movement
- **Vulnerability Mitigation**: Reduces exploitability of known vulnerabilities through compensating controls; addresses configuration-based weaknesses not resolved by patching alone
- **Operational Efficiency**: Automates security baseline deployment through infrastructure-as-code (Terraform, CloudFormation, ARM templates) and configuration management; reduces manual configuration errors

## Purpose & Scope

### Primary Purpose

This artifact provides authoritative security configuration standards, implementation procedures, validation testing methods, and automated remediation capabilities for all enterprise technology platforms. It translates high-level security policies into specific technical settings, enables Infrastructure-as-Code security integration, and establishes continuous compliance monitoring frameworks.

### Scope

**In Scope**:
- **Windows Operating Systems**: Windows Server 2016/2019/2022 Datacenter/Standard, Windows 10/11 Enterprise, Microsoft Security Baselines (Level 1/Level 2), CIS Windows Benchmarks, DISA Windows STIGs, Group Policy Objects (GPOs), PowerShell DSC configurations, Microsoft Intune compliance policies
- **Linux Operating Systems**: RHEL 7/8/9, CentOS 7/8, Ubuntu 20.04/22.04 LTS, Amazon Linux 2, SUSE Linux Enterprise, CIS Linux Benchmarks, DISA RHEL/Ubuntu STIGs, OpenSCAP profiles, Ansible hardening roles, SELinux/AppArmor mandatory access controls
- **Network Infrastructure**: Cisco IOS/IOS-XE routers and switches, Palo Alto PAN-OS firewalls, Fortinet FortiOS UTM, F5 BIG-IP load balancers, Juniper JUNOS, CIS Network Device Benchmarks, DISA network STIGs, NSA switch/router security guides, AAA (TACACS+/RADIUS) integration
- **Virtualization & Hypervisors**: VMware vSphere/ESXi 7.x/8.x, Microsoft Hyper-V, KVM/QEMU, CIS VMware Benchmarks, DISA Virtualization STIGs, virtual machine isolation, hypervisor hardening, VM escape prevention
- **Cloud Infrastructure**: AWS EC2 instances (AMI hardening), Azure Virtual Machines, GCP Compute Engine, AWS Security Best Practices, Azure Security Benchmark, GCP CIS Benchmark, CSPM policy enforcement, cloud-init/user-data hardening scripts, IMDSv2 enforcement
- **Cloud-Native & Containers**: Kubernetes CIS Benchmark, Docker CIS Benchmark, container image hardening (minimal base images, non-root users, read-only filesystems), Pod Security Standards, service mesh security (Istio, Linkerd), OPA/Gatekeeper policies
- **Database Systems**: Oracle Database 19c/21c, Microsoft SQL Server 2016/2019/2022, PostgreSQL 12/13/14/15, MySQL 5.7/8.0, MongoDB, CIS Database Benchmarks, DISA Database STIGs, transparent data encryption (TDE), role-based access, audit logging
- **Active Directory**: Domain controller hardening, Group Policy security settings, privileged account management (Tier 0/1/2 model), LAPS (Local Administrator Password Solution), Kerberos delegation restrictions, SMB signing enforcement, LDAP channel binding
- **Enterprise Applications**: Microsoft Exchange Server/Exchange Online, SharePoint Server/Online, Apache/Nginx web servers, Tomcat application servers, Redis/Memcached, Elasticsearch, vendor-specific hardening guides, TLS configuration, authentication integration
- **Automated Configuration**: Ansible hardening playbooks (RHEL System Roles, CIS roles), Chef InSpec compliance profiles, Puppet hardening modules, PowerShell DSC desired state configurations, Terraform security modules, CloudFormation templates with security hardening
- **Compliance Validation**: OpenSCAP scanning and reporting, SCAP Compliance Checker (SCC), Nessus Policy Compliance scans, Qualys Policy Compliance, Tenable.sc SCAP integration, AWS Config Rules, Azure Policy, GCP Security Command Center
- **Configuration Management**: Desired state enforcement via configuration management platforms, drift detection and remediation, compliance dashboards, exception tracking, baseline versioning and change control

**Out of Scope**:
- **Application-Specific Security**: Covered in secure-coding-standards artifact (OWASP Top 10 remediation, input validation, authentication/authorization logic, secure API design)
- **Patch Management Procedures**: Covered in patch-management-policy artifact (patch testing, deployment schedules, emergency patching, vulnerability prioritization, patch compliance tracking)
- **Network Architecture & Segmentation**: Covered in network-security-architecture artifact (VLAN design, firewall rulesets, zero trust architecture, micro-segmentation, DMZ design)
- **Endpoint Protection Configuration**: Covered in endpoint-security-standards artifact (EDR/XDR tuning, antivirus exclusions, application control policies, USB device restrictions)
- **Cloud Security Architecture**: Covered in cloud-security-architecture artifact (landing zones, account structure, identity federation, network design, data residency)
- **Backup & Recovery Procedures**: Covered in backup-recovery-plan artifact (backup schedules, retention policies, restore testing, disaster recovery)
- **Incident Response Playbooks**: Covered in incident-response-plan artifact (detection, containment, eradication, recovery, post-incident review)

### Target Audience

**Primary Audience**:
- **Systems Administrators (Windows/Linux)**: Implements hardening configurations on servers and workstations, applies GPOs, executes Ansible playbooks, validates compliance, remediates findings
- **Security Engineers**: Develops automated hardening scripts, creates compliance policies, integrates SCAP scanning into CI/CD pipelines, tunes security baselines, investigates compliance violations
- **Cloud Platform Engineers**: Applies hardening to cloud infrastructure, configures CSPM policies, implements infrastructure-as-code security, manages cloud configuration compliance
- **DevOps/SRE Teams**: Integrates security baselines into deployment pipelines, automates compliance validation, manages configuration drift, implements policy-as-code
- **Network Engineers**: Hardens network devices, configures secure management protocols, implements AAA integration, validates configuration compliance against CIS/STIG baselines

**Secondary Audience**:
- **Chief Information Security Officer (CISO)**: Reviews compliance metrics, approves baseline standards, prioritizes remediation efforts, reports security posture to board and regulators
- **Compliance & Audit Teams**: Validates hardening implementation for audits (SOC 2, ISO 27001, PCI DSS, FedRAMP), samples configuration compliance, reviews exception justifications
- **Vulnerability Management Team**: Correlates configuration weaknesses with vulnerability scan findings, prioritizes configuration-based risks, validates compensating controls
- **IT Service Desk**: Troubleshoots hardening-related application issues, processes exception requests, assists with compliance remediation tickets
- **Application Development Teams**: Understands server hardening requirements that may affect application deployment, tests applications against hardened baselines, requests justified exceptions
- **Third-Party Auditors & Assessors**: Reviews hardening standards during SOC 2, ISO 27001, PCI QSA, and FedRAMP 3PAO assessments

## Document Information

**Format**: Markdown

**File Pattern**: `*.baseline-hardening-guides.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: [Define typical classification level - Public | Internal | Confidential | Restricted]

**Retention**: [Define retention period per organizational records management policy]


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Scheduled date for next formal review
- `documentOwner`: Role/person responsible for maintenance
- `classification`: Information classification level
- `retentionPeriod`: How long document must be retained

**Authorship & Review**:
- `primaryAuthor`: Lead author name and role
- `contributors`: Additional contributors and their roles
- `reviewers`: Designated reviewers (technical, security, compliance, etc.)
- `approvers`: Formal approvers with sign-off authority
- `reviewStatus`: Current review status
- `approvalDate`: Date of formal approval

**Document Purpose**:
- `executiveSummary`: 2-3 paragraph overview for executive audience
- `businessContext`: Why this document exists and its business value
- `scope`: What is covered and what is explicitly out of scope
- `applicability`: Who this applies to and under what circumstances
- `relatedDocuments`: References to related artifacts and dependencies

### Main Content Sections

(Content structure will vary based on specific artifact type. Include all relevant sections needed to fully document the subject matter.)

**Core Information**:
- Document the primary information this artifact is meant to capture
- Organize in logical sections appropriate to the content type
- Use consistent formatting and structure
- Include sufficient detail for intended audience
- Provide examples where helpful

**Supporting Information**:
- Background context necessary for understanding
- Assumptions and constraints
- Dependencies on other artifacts or systems
- Related information and cross-references


## Best Practices

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use approved templates to ensure completeness and consistency across teams
**Peer Review**: Have at least one qualified peer review before submitting for approval
**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management
**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in
**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon
**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively
**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation
**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes
**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats
**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates
**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy
**Start with Industry Standards**: Adopt CIS Benchmarks or vendor baselines as foundation rather than creating from scratch; customize based on risk tolerance and operational requirements
**Level 1 Before Level 2**: Implement CIS Level 1 (least restrictive, minimal operational impact) before Level 2 (defense-in-depth, may affect legacy applications)
**Test Before Production**: Validate hardening configurations in dev/test environments; identify application compatibility issues before production rollout
**Phased Deployment**: Pilot hardening on subset of systems, gather feedback, tune configurations, then expand deployment progressively
**Exception Process**: Establish formal risk acceptance process for configurations that cannot meet baseline due to application requirements; document compensating controls
**Automation over Manual**: Automate hardening deployment via Ansible/Chef/Puppet/GPO; manual configurations lead to inconsistency and configuration drift
**Continuous Compliance Monitoring**: Implement automated scanning (OpenSCAP, Nessus PC, CSPM) to detect configuration drift; alert on non-compliance
**Version Control**: Maintain baseline configurations in Git repositories; track changes, enable rollback, peer review modifications
**Immutable Infrastructure**: For cloud workloads, bake hardening into golden AMIs/images rather than post-deployment configuration
**Security vs. Usability Balance**: Engage application owners early; overly restrictive hardening that breaks applications leads to shadow IT and exceptions
**Prioritize by Risk**: Focus on internet-facing systems, privileged account workstations, and systems processing sensitive data first
**Disable Legacy Protocols**: Eliminate SMBv1, TLS 1.0/1.1, SSLv2/v3, Telnet, FTP, NTLM where possible; mandate secure alternatives
**Service Minimization**: Disable all unnecessary services; principle of least functionality reduces attack surface significantly
**Local Admin Restrictions**: Remove local admin rights except where absolutely necessary; implement LAPS for unique local admin passwords
**Audit Logging Prerequisites**: Ensure robust logging is configured before hardening to facilitate troubleshooting if issues arise
**Hardening as Code**: Integrate security baseline validation into CI/CD pipelines; fail deployments that don't meet minimum security posture
**Scheduled Baseline Reviews**: Review and update hardening standards quarterly; incorporate new CIS Benchmark releases and vendor guidance
**Metrics & Dashboards**: Track compliance percentages by system type; trend over time; set improvement targets and executive reporting
**Training & Documentation**: Provide administrators with training on hardening rationale and troubleshooting; reduces improper exceptions and workarounds
**Cloud-Native Tooling**: Leverage native cloud security tools (AWS Config, Azure Policy, GCP Security Command Center) for cloud infrastructure compliance
**Container Image Scanning**: Integrate hardening validation into container registries; scan images for configuration issues before deployment

## Quality Criteria

Before considering this artifact complete and ready for approval, verify:

✓ **Completeness**: All required sections present and adequately detailed
✓ **Accuracy**: Information verified and validated by appropriate subject matter experts
✓ **Clarity**: Written in clear, unambiguous language appropriate for intended audience
✓ **Consistency**: Aligns with organizational standards, templates, and related artifacts
✓ **Currency**: Based on current information; outdated content removed or updated
✓ **Traceability**: Includes references to source materials and related documents
✓ **Stakeholder Review**: Reviewed by all key stakeholders with feedback incorporated
✓ **Technical Review**: Technical accuracy verified by qualified technical reviewers
✓ **Compliance**: Meets all applicable regulatory, policy, and contractual requirements
✓ **Approval**: All required approvals obtained and documented
✓ **Accessibility**: Stored in accessible location with appropriate permissions
✓ **Metadata**: Complete metadata enables search, categorization, and lifecycle management

## Common Pitfalls & How to Avoid

❌ **Incomplete Information**: Rushing to complete without gathering all necessary inputs
   ✓ *Solution*: Create comprehensive checklist of required information; allocate sufficient time

❌ **Lack of Stakeholder Input**: Creating in isolation without engaging affected parties
   ✓ *Solution*: Identify all stakeholders early; schedule working sessions for collaborative development

❌ **Outdated Content**: Using old information or not updating when conditions change
   ✓ *Solution*: Establish refresh schedule; define triggers requiring immediate update

❌ **Inconsistent Format**: Not following organizational templates and standards
   ✓ *Solution*: Always start from approved template; verify against style guide before submission

❌ **Missing Approvals**: Publishing without proper authorization
   ✓ *Solution*: Understand approval chain; route through all required approvers with evidence

❌ **Poor Version Control**: Making changes without maintaining history
   ✓ *Solution*: Use proper version control system; never directly edit published version

❌ **Inadequate Distribution**: Completing artifact but stakeholders unaware it exists
   ✓ *Solution*: Define distribution list; actively communicate availability and location

❌ **No Maintenance Plan**: Creating artifact as one-time activity with no ongoing ownership
   ✓ *Solution*: Assign owner; schedule regular reviews; define update triggers

## Related Standards & Frameworks

**Industry Hardening Benchmarks**:
- CIS (Center for Internet Security) Benchmarks: Windows Server, RHEL, Ubuntu, Debian, macOS, AWS, Azure, GCP, Kubernetes, Docker, Oracle, SQL Server, PostgreSQL, MySQL, Apache, Nginx, Cisco IOS, and 100+ technology platforms
- DISA STIGs (Security Technical Implementation Guides): Windows, RHEL, Ubuntu, Oracle Linux, Solaris, network devices, databases, applications; required for DoD and federal contractors
- Microsoft Security Baselines: Windows 10/11, Windows Server 2016/2019/2022, Microsoft 365 Apps, Edge browser; provided via Security Compliance Toolkit
- NSA Security Configuration Guides: Network infrastructure devices, operating systems; focused on nation-state threat mitigation
- Australian Cyber Security Centre (ACSC) Hardening Guides: Microsoft, Linux, network devices; aligned with Australian Government security requirements
- Cloud Security Alliance (CSA) Security Guidance: Cloud-specific hardening recommendations for AWS, Azure, GCP

**Government & Regulatory Standards**:
- NIST SP 800-53 Rev 5: CM-6 (Configuration Settings), CM-7 (Least Functionality), SI-2 (Flaw Remediation), SI-7 (Software, Firmware, and Information Integrity)
- NIST SP 800-123: Guide to General Server Security (operating system hardening)
- NIST SP 800-125: Guide to Security for Full Virtualization Technologies
- NIST SP 800-125A/B: Security for Server and Desktop Virtualization, Hypervisor Security
- NIST SP 800-190: Application Container Security Guide (Kubernetes, Docker hardening)
- NIST Cybersecurity Framework (CSF): PR.IP-1 (Baseline configurations), PR.PT-3 (Least functionality)
- FedRAMP Security Controls: Configuration management requirements for cloud service providers
- FISMA: Federal system security requirements including SCAP compliance validation

**Compliance Requirements**:
- PCI DSS v4.0: Requirement 2.2 (Configure systems securely), 2.2.1 (Vendor defaults changed), 2.2.2 (Configuration standards for system components), 2.2.3 (Primary functions on separate servers), 2.2.4 (Inventory of system components), 2.2.5 (Insecure services disabled), 2.2.6 (System security parameters configured), 2.2.7 (All non-console admin access encrypted)
- HIPAA Security Rule: 164.308(a)(8) (Evaluation - security configuration reviews), 164.312(a)(1) (Access control - unique user IDs, automatic logoff), 164.312(b) (Audit controls)
- SOC 2 Trust Services: CC6.6 (Logical access controls configured), CC7.1 (Detection of security events), CC8.1 (Change management)
- ISO/IEC 27001:2022: A.8.9 (Configuration management), A.8.19 (Installation of software on operational systems), A.8.23 (Web filtering)
- GDPR Article 32: Security of processing - appropriate technical measures including system hardening
- CMMC (Defense Industrial Base): CM.L2-3.4.1 through CM.L2-3.4.9 (Configuration management controls)

**SCAP (Security Content Automation Protocol) Standards**:
- SCAP 1.3 / 2.0: Standardized security compliance checking framework
- XCCDF (Extensible Configuration Checklist Description Format): Benchmark and rule definitions
- OVAL (Open Vulnerability and Assessment Language): System state definitions for compliance checking
- CPE (Common Platform Enumeration): Standardized system and software naming
- CCE (Common Configuration Enumeration): Unique identifiers for configuration issues
- CVSS (Common Vulnerability Scoring System): Severity scoring for configuration vulnerabilities
- OpenSCAP: Open-source SCAP implementation and scanning tools

**Automation & Configuration Management**:
- Ansible Automation Platform: RHEL System Roles (security hardening), CIS hardening roles, custom playbooks
- Chef InSpec: Compliance-as-code framework with CIS, STIG, and custom profiles
- Puppet: Hardening modules for OS, database, and application configuration
- PowerShell DSC (Desired State Configuration): Windows configuration enforcement
- Terraform: Infrastructure-as-code with security module libraries (AWS CIS Module, Azure CAF Terraform modules)
- AWS CloudFormation / Azure ARM Templates / GCP Deployment Manager: Cloud infrastructure hardening templates
- Kubernetes Operators: Automated security configuration for Kubernetes clusters

**Cloud Security Standards**:
- AWS Foundational Security Best Practices: Automated checks via AWS Security Hub
- Azure Security Benchmark: Microsoft cloud security recommendations aligned to CIS Controls
- GCP Security Foundations Blueprint: Terraform-based secure landing zone
- CIS AWS Foundations Benchmark: Independent AWS configuration standard
- CIS Microsoft Azure Foundations Benchmark: Independent Azure configuration standard
- CIS Google Cloud Platform Foundation Benchmark: Independent GCP configuration standard
- Well-Architected Framework (AWS/Azure/GCP): Security pillar guidance

**Vendor-Specific Security Guides**:
- Microsoft Security Baselines: Windows, Office, Edge, Security Compliance Toolkit (GPO exports, Policy Analyzer)
- Red Hat Enterprise Linux Security Guide: SCAP profiles, SELinux policies, FIPS 140-2 compliance
- Oracle Database Security Guide: TDE, VPD, database vault, audit vault configuration
- Cisco Security Configuration Guides: IOS hardening, ASA firewall, switch port security
- VMware vSphere Hardening Guide: ESXi, vCenter, VM security recommendations
- Palo Alto Networks Best Practice Assessment (BPA): Automated NGFW configuration review

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- [List artifacts that provide input to this one]
- [Data sources that feed this artifact]
- [Prerequisites that must be satisfied]

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- [Artifacts that consume information from this one]
- [Processes that use this artifact]
- [Teams or roles that rely on this information]

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- [Complementary artifacts in same phase]
- [Artifacts in adjacent phases]
- [Cross-cutting artifacts (e.g., risk register)]

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: [If applicable] Architecture board review for standards compliance
5. **Security Review**: [If applicable] Security team review for security requirements
6. **Compliance Review**: [If applicable] Compliance review for regulatory requirements
7. **Legal Review**: [If applicable] Legal counsel review
8. **Final Approval**: Designated approver(s) provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: [Define role - e.g., Program Manager, Architecture Lead, CISO]
- Secondary Approver: [For high-risk or cross-functional artifacts]
- Governance Approval: [If requires board or committee approval]

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: [Define cadence - e.g., Quarterly, Annually]

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur
- Regulatory requirements change
- Major incidents reveal deficiencies
- Stakeholder requests identify needed updates
- Related artifacts are substantially updated

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring, scope changes, or approach changes
- **MINOR**: New sections, substantial additions, or enhancements
- **PATCH**: Corrections, clarifications, minor updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: [Define based on regulatory and business requirements]

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: [Define role responsible for maintenance]

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/{artifact_name}-template.{format_type.lower()}`

**Alternative Formats**: [If multiple formats supported]

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/{artifact_name}-example-*.{format_type.lower()}`

**Annotated Guidance**: See annotated examples showing best practices and common approaches

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified and engaged all required stakeholders
- [ ] Gathered prerequisite information and inputs
- [ ] Obtained access to necessary systems and data
- [ ] Allocated sufficient time for quality completion
- [ ] Identified reviewers and approvers
- [ ] Understood applicable standards and requirements

While creating this artifact:

- [ ] Following approved template structure
- [ ] Documenting sources and references
- [ ] Writing clearly for intended audience
- [ ] Including visual aids where helpful
- [ ] Self-reviewing against quality criteria
- [ ] Seeking input from stakeholders

Before submitting for approval:

- [ ] Completed all required sections
- [ ] Verified accuracy of all information
- [ ] Obtained peer review feedback
- [ ] Addressed all review comments
- [ ] Spell-checked and proofread
- [ ] Completed all metadata fields
- [ ] Verified compliance with standards
- [ ] Ready for formal approval process

## Governance & Compliance

### Regulatory Considerations

[Define any regulatory requirements applicable to this artifact type, such as:]

- SOC 2: [If artifact supports SOC 2 controls]
- ISO 27001: [If part of ISMS documentation]
- GDPR/Privacy: [If contains or references personal data]
- Industry-Specific: [Healthcare, Financial Services, etc.]

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team
- External audits by third-party auditors
- Regulatory examinations
- Customer security assessments

**Audit Preparation**:
- Maintain complete version history
- Document all approvals with evidence
- Keep change log current
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- [Relevant organizational policies]
- [Industry regulations and standards]
- [Contractual obligations]
- [Governance framework requirements]

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Access Frequency**: How often artifact is accessed/referenced
- **Update Frequency**: How often artifact requires updates
- **Downstream Impact**: How many artifacts/processes depend on this

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: {phase}

**Category**: {category}

**Typical Producers**: [Roles/teams that typically create this artifact]

**Typical Consumers**: [Roles/teams that typically use this artifact]

**Effort Estimate**: [Typical hours/days required to complete]

**Complexity Level**: [Low | Medium | High | Very High]

**Business Criticality**: [Low | Medium | High | Mission Critical]

**Change Frequency**: [Static | Infrequent | Regular | Frequent]

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: {phase} - Version 2.0*
