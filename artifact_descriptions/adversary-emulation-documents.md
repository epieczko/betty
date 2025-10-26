# Name: adversary-emulation-documents

## Executive Summary

The Adversary Emulation Documents establish comprehensive threat-informed defense capabilities through structured replication of real-world attacker tactics, techniques, and procedures (TTPs) mapped to the MITRE ATT&CK framework. These technical playbooks enable security teams to validate detection capabilities, test incident response procedures, measure security control effectiveness, and identify defensive gaps through controlled adversary simulation exercises including red team operations, purple team collaborations, breach and attack simulation (BAS), and automated adversary emulation.

Modern adversary emulation leverages industry-standard frameworks and tools including MITRE ATT&CK Enterprise/Mobile/ICS matrices, ATT&CK Navigator for campaign visualization, Atomic Red Team for discrete technique testing, MITRE Caldera for automated attack chains, and commercial platforms (SafeBreach, Cymulate, AttackIQ, Palo Alto Cortex XSOAR, Pentera). Emulation scenarios replicate threat actor behaviors from specific APT groups (APT29/Cozy Bear, APT28/Fancy Bear, Lazarus Group, FIN7, Carbanak), ransomware families (Conti, LockBit, BlackCat/ALPHV, Hive), and common attack patterns (phishing → credential access → lateral movement → data exfiltration).

Purple team exercises bring together offensive security teams (red team executing attacks) and defensive teams (blue team monitoring/responding) in collaborative assessment cycles to validate SIEM detection rules, EDR/XDR response capabilities, SOAR playbook effectiveness, threat hunting procedures, and security analyst training. Emulation plans document pre-attack preparation (scope, rules of engagement, cleanup procedures), execution steps (command-line syntax, tool configurations, expected artifacts), detection opportunities (log sources, signatures, behavioral analytics), and post-exercise analysis (gaps identified, detection improvements, control enhancements).

### Strategic Importance

- **Detection Engineering Validation**: Tests SIEM correlation rules, EDR behavioral analytics, network IDS/IPS signatures, DLP policies, and UEBA baselines against real attack techniques to reduce false negatives
- **Security Control Effectiveness**: Measures actual defensive capability against specific threats rather than theoretical compliance; quantifies risk reduction from security investments (firewall, EDR, PAM, MFA)
- **Threat-Informed Defense**: Prioritizes security improvements based on adversary TTPs most relevant to organization's threat model, industry targeting, and asset criticality
- **Incident Response Readiness**: Exercises IR playbooks, tests communication procedures, validates forensic tooling, trains analysts, and identifies process gaps before real incidents
- **Purple Team Collaboration**: Breaks down silos between offensive and defensive security teams; accelerates detection development through shared understanding of attack mechanics
- **Compliance & Assurance**: Demonstrates proactive security testing for auditors, regulators, board, and cyber insurance underwriters; satisfies NIST CSF, ISO 27001, and PCI DSS testing requirements
- **Security Awareness & Training**: Provides realistic attack scenarios for tabletop exercises, phishing simulations, and security awareness training; educates executives on modern threats

## Purpose & Scope

### Primary Purpose

This artifact documents adversary emulation scenarios, execution procedures, detection validation requirements, and purple team exercise plans that replicate real-world cyber attacks in controlled environments. It provides technical runbooks for security teams to execute threat-informed assessments, measure defensive capabilities, identify gaps, and drive continuous security improvement through evidence-based testing.

### Scope

**In Scope**:
- **MITRE ATT&CK Mapping**: Comprehensive TTP coverage across Initial Access (T1078, T1566), Execution (T1059, T1053), Persistence (T1098, T1136), Privilege Escalation (T1068, T1078), Defense Evasion (T1070, T1027), Credential Access (T1003, T1558), Discovery (T1087, T1135), Lateral Movement (T1021, T1080), Collection (T1005, T1114), Exfiltration (T1041, T1567), Impact (T1486, T1490)
- **APT Group Emulation Plans**: Documented scenarios replicating APT29 (SolarWinds supply chain), APT28 (credential harvesting), APT41 (dual espionage/financial), Lazarus Group (WannaCry/crypto theft), FIN7 (point-of-sale compromise), Carbanak (financial institution targeting), Dragonfly/Energetic Bear (ICS/SCADA)
- **Ransomware Simulation**: Safe emulation of ransomware kill chains including Conti, LockBit 3.0, BlackCat/ALPHV, REvil/Sodinokibi, Hive; validation of ransomware detection, backup recovery, and incident response
- **Atomic Red Team Tests**: Discrete technique validation using Atomic Red Team library; automated testing of individual ATT&CK techniques with cleanup scripts; GitHub integration for test library updates
- **Purple Team Exercise Plans**: Quarterly purple team sprint planning, joint red/blue team kickoffs, real-time attack-defense collaboration, gap analysis workshops, detection tuning sessions, lessons learned documentation
- **Automated Emulation Platforms**: MITRE Caldera adversary emulation, SafeBreach BAS continuous validation, AttackIQ security validation platform, Cymulate exposure analytics, Pentera automated penetration testing, Palo Alto Cortex XSOAR attack simulation
- **Attack Tool Documentation**: Cobalt Strike team server setup and malleable C2 profiles, Metasploit module selection and payload generation, PowerShell Empire/Covenant C2 frameworks, Sliver adversary emulation, custom exploit development, living-off-the-land binaries (LOLBins)
- **Phishing Simulation**: Gophish campaigns, KnowBe4 PhishER, Proofpoint security awareness, realistic credential harvesting pages, QR code phishing (quishing), attachment-based delivery (macros, LNK files)
- **Detection Development**: SIEM correlation rule creation (Splunk SPL, Elastic KQL, Sentinel KQL), Sigma rule conversion, YARA rule development, Snort/Suricata IDS signatures, EDR behavioral rules, custom detection scripts
- **Logging & Artifacts**: Windows Event Log requirements (4688 process creation, 4624/4625 logon, 4672 special privileges, 7045 service installation), Sysmon configuration, EDR telemetry, network flow logs (NetFlow, IPFIX), DNS query logs
- **Blue Team Validation**: SOC analyst detection during exercises, SIEM alert generation, incident ticket creation, escalation procedures, forensic artifact collection, containment actions, eradication verification
- **Metrics & Reporting**: Dwell time (attack initiation → detection), mean time to detect (MTTD), mean time to respond (MTTR), detection coverage by ATT&CK technique, gap analysis by kill chain phase, remediation tracking

**Out of Scope**:
- **Traditional Penetration Testing**: Covered in penetration-testing-plan artifact (OWASP testing methodology, web application scanning, infrastructure penetration testing, social engineering assessments, physical penetration)
- **Vulnerability Scanning & Management**: Covered in vulnerability-management-plan artifact (Qualys, Nessus, Rapid7 scanning, patch prioritization, remediation SLAs, scanner deployment)
- **Threat Intelligence Collection**: Covered in threat-intelligence-program artifact (OSINT collection, dark web monitoring, threat actor profiling, IOC feeds, intelligence sharing via ISACs)
- **Incident Response Execution**: Covered in incident-response-plan artifact (actual breach response, containment procedures, forensic investigation, recovery operations, post-incident review)
- **Security Awareness Training Content**: Covered in security-awareness-program artifact (annual training curriculum, compliance training, role-based modules, gamification)
- **Bug Bounty & Responsible Disclosure**: Covered in bug-bounty-brief artifact (HackerOne/Bugcrowd programs, vulnerability disclosure policy, bounty pricing, researcher engagement)
- **Production Environment Testing**: Live production systems excluded unless explicitly scoped with change control approval and rollback procedures

### Target Audience

**Primary Audience**:
- **Red Team Operators**: Executes adversary emulation scenarios, develops custom TTPs, operates attack tools (Cobalt Strike, Metasploit), documents attack chains, collaborates with blue team during purple team exercises
- **Purple Team Lead**: Coordinates joint red/blue exercises, facilitates gap analysis sessions, tracks detection improvements, reports metrics to leadership, manages exercise calendar
- **SOC Analysts & Detection Engineers**: Monitors for emulated attacks, tunes SIEM rules, develops new detections based on exercise gaps, validates alert fidelity, documents detection logic
- **Threat Intelligence Analysts**: Maps APT TTPs to ATT&CK framework, identifies relevant threat actors targeting organization's industry, updates emulation scenarios based on new campaigns, briefs teams on emerging threats
- **Security Engineering Team**: Deploys detection tools (EDR, SIEM, NDR), configures logging sources, implements blocking controls based on emulation findings, validates security architecture

**Secondary Audience**:
- **Chief Information Security Officer (CISO)**: Reviews purple team metrics and gap analysis, approves red team scope and rules of engagement, presents security validation results to board, funds detection engineering improvements
- **Incident Response Team**: Observes purple team exercises to improve IR playbooks, validates forensic procedures, tests communication protocols, practices containment techniques
- **Security Architects**: Incorporates adversary emulation findings into security architecture, designs defense-in-depth controls, prioritizes security investments based on gap analysis
- **Compliance & Risk Teams**: Uses emulation results as evidence for audits (SOC 2, ISO 27001, PCI DSS testing requirements), quantifies residual risk, validates control effectiveness
- **IT Operations & Infrastructure Teams**: Remediates configuration weaknesses discovered during emulation, assists with safe test environment setup, reviews logging and monitoring gaps
- **Executive Leadership & Board**: Reviews executive summaries of security posture, understands realistic attack scenarios, approves budget for remediation priorities

## Document Information

**Format**: Markdown

**File Pattern**: `*.adversary-emulation-documents.md`

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
**Scope Clearly Defined**: Document explicit in-scope systems, out-of-scope restrictions, testing windows, and rules of engagement; obtain written approval before testing
**Test Environment First**: Validate attack techniques in isolated lab before executing in production-like or production environments
**Deconfliction with SOC**: Coordinate test timing with SOC leadership; optionally notify SOC to measure unassisted detection vs. assisted validation
**Safe Attack Simulation**: Avoid destructive techniques (encryption, deletion, DoS) in production; use benign payloads and reversible actions
**Comprehensive Cleanup**: Document and execute cleanup procedures for all artifacts (files, registry keys, scheduled tasks, accounts, services, firewall rules)
**Purple Team Over Pure Red Team**: Prioritize collaborative purple team exercises to accelerate detection development vs. adversarial red team assessments
**ATT&CK Technique Coverage**: Track cumulative coverage of ATT&CK techniques tested; prioritize gaps in high-severity techniques relevant to threat model
**Detection Before Prevention**: Validate detection capabilities before deploying blocking controls; ensures visibility before enforcement
**Metrics-Driven Improvement**: Track dwell time, MTTD, MTTR trends quarter-over-quarter; set improvement targets and celebrate wins
**Automation for Scale**: Leverage Atomic Red Team or BAS platforms for continuous validation; reserve manual red team for complex attack chains
**Realistic Scenarios**: Base emulation on actual threat intelligence (CISA advisories, vendor threat reports) relevant to organization's industry and geography
**Logging Prerequisite Validation**: Verify required logging is enabled (Sysmon, process creation, PowerShell logging) before testing to ensure detectability
**Blue Team Skill Development**: Use purple team exercises as training opportunities for SOC analysts; explain attack mechanics during debrief
**Executive Communication**: Present results in business context (risk reduction, control effectiveness) not technical jargon; use ATT&CK heatmaps for visualization
**Vendor Product Validation**: Test vendor claims (EDR behavioral blocking, NGFW threat prevention) through emulation to validate before purchase
**Tabletop Before Technical**: Conduct tabletop exercises to validate IR playbooks before expensive technical red team assessments
**Legal and Insurance Review**: Involve legal counsel for acceptable use of offensive tools; notify cyber insurance carrier of red team program for potential premium reduction
**Third-Party Red Team Rotation**: Supplement internal purple team with annual external red team assessment for fresh perspective and advanced tradecraft
**Threat-Informed Prioritization**: Focus emulation on threats most likely to target organization based on threat intelligence, not all possible techniques
**Continuous Program Maturity**: Evolve from basic Atomic Red Team tests → internal purple team → advanced manual red team → automated BAS continuous validation

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

**Adversary Tactics & Techniques**:
- MITRE ATT&CK Framework: Enterprise Matrix (Windows, Linux, macOS, Cloud), Mobile Matrix (Android, iOS), ICS Matrix (industrial control systems), technique descriptions, detection guidance, mitigation strategies
- MITRE ATT&CK Navigator: Campaign visualization, technique heatmaps, coverage analysis, gap identification
- MITRE Cyber Analytics Repository (CAR): Analytics and sensors for ATT&CK technique detection
- MITRE D3FEND: Defensive countermeasures and techniques mapped to ATT&CK
- ATT&CK Evaluations: Independent testing of EDR/XDR vendor detection capabilities against APT29, Carbanak+FIN7, Wizard Spider+Sandworm emulation plans
- Atomic Red Team: Open-source library of technique tests with automation and cleanup (Red Canary project)
- MITRE Caldera: Automated adversary emulation platform for red/purple team exercises

**Threat Actor & Campaign Documentation**:
- MITRE ATT&CK Groups: APT29, APT28, FIN7, Lazarus Group, Carbanak profiles with associated techniques
- MITRE Engenuity ATT&CK Evaluations: Publicly documented emulation plans for major APT groups
- CISA Cybersecurity Advisories: AA series advisories with IOCs and TTPs for current threats
- NCSC (UK) Advisory Reports: Threat actor profiles and mitigation guidance
- FBI Flash Alerts: Law enforcement threat intelligence on active campaigns

**Security Testing Standards**:
- NIST SP 800-115: Technical Guide to Information Security Testing and Assessment
- NIST SP 800-53 Rev 5: CA-8 (Penetration Testing), RA-5 (Vulnerability Monitoring and Scanning)
- OWASP Testing Guide: Web application security testing methodology (complementary to adversary emulation)
- PTES (Penetration Testing Execution Standard): Seven-phase methodology for penetration testing
- OSSTMM (Open Source Security Testing Methodology Manual): Scientific security testing methodology
- PCI DSS v4.0: Requirement 11.4 (External and internal penetration testing) - adversary emulation satisfies testing requirements

**Compliance & Regulatory Frameworks**:
- ISO/IEC 27001:2022: A.5.7 (Threat intelligence), A.8.8 (Management of technical vulnerabilities), A.8.25 (Secure development lifecycle)
- NIST Cybersecurity Framework (CSF): DE.DP-5 (Detection processes continuously improved), RS.IM-1 (Response plans incorporate lessons learned)
- CIS Controls v8: 15.1 (Establish and Maintain Security Awareness Program), 18.3 (Practice Incident Response), 18.5 (Conduct Penetration Tests)
- SOC 2: CC7.3 (Evaluates security events to identify security incidents), additional criteria for penetration testing maturity
- GDPR Article 32: Security testing as part of "regular testing and evaluation of effectiveness"
- CMMC (Defense Industrial Base): CA.L2-3.12.1, CA.L2-3.12.4 (Security assessment and penetration testing)
- FedRAMP: Penetration testing requirements for cloud service providers

**Red Team Tools & Platforms**:
- Cobalt Strike: Commercial red team platform with malleable C2, beacon deployment, post-exploitation modules
- Metasploit Framework: Open-source penetration testing platform with exploit modules and payloads
- PowerShell Empire / Covenant: Post-exploitation C2 frameworks for Windows environments
- Sliver: Open-source adversary emulation framework (alternative to Cobalt Strike)
- Mythic: Multi-platform C2 framework with extensible agent development
- BloodHound: Active Directory attack path analysis and privilege escalation discovery
- Impacket: Python library for working with network protocols (SMB, Kerberos, WMI)
- Responder / Inveigh: LLMNR/NBT-NS poisoning and relay attacks
- Mimikatz: Credential extraction from Windows memory
- CrackMapExec: Swiss army knife for pentesting Windows/Active Directory environments

**Purple Team & BAS Platforms**:
- MITRE Caldera: Free, open-source adversary emulation with autonomous attack chains
- SafeBreach: Continuous security validation and breach and attack simulation
- AttackIQ: Security optimization platform with purple team exercises
- Cymulate: Immediate threat exposure analytics platform
- Pentera: Automated security validation platform (formerly Pcysys)
- Palo Alto Cortex XSOAR: SOAR platform with attack simulation playbooks
- Vectra AI: Network detection and response with automated attack replay
- Rapid7 InsightIDR: User behavior analytics with attacker behavior analytics

**Detection Engineering Resources**:
- Sigma Rules: Generic signature format for SIEM detection rules (community-driven)
- Elastic Detection Rules: Pre-built KQL rules for Elastic Security mapped to ATT&CK
- Splunk Security Content: Analytic stories and detection searches aligned to ATT&CK
- Microsoft Sentinel Detection Rules: KQL analytics rules for Azure Sentinel
- YARA Rules: Pattern matching for malware detection and memory analysis
- Snort / Suricata Rules: Network intrusion detection signatures
- SOC Prime Threat Detection Marketplace: Community threat detection content
- Detection-as-Code: Version-controlled, tested, and automated detection development

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
