# Name: access-review-logs

## Executive Summary

The Access Review Logs artifact establishes comprehensive logging, retention, and audit trail requirements for all access governance activities including user access certifications, role modifications, privilege escalations, access request approvals/denials, account lifecycle events, and authentication activities. This critical compliance deliverable implements logging standards from NIST SP 800-92 (Guide to Computer Security Log Management), ISO 27001 A.12.4.1 (Event Logging), SOC 2 CC7.2 (System Monitoring), and PCI DSS Requirement 10 (Track and Monitor All Access) to provide tamper-evident evidence for regulatory audits, security investigations, and compliance attestations.

Modern access review logging leverages Security Information and Event Management (SIEM) platforms such as Splunk Enterprise Security, Elastic Security (ELK Stack), IBM QRadar, Microsoft Sentinel, Sumo Logic, or LogRhythm to aggregate, correlate, and analyze access events from IGA systems (SailPoint, Saviynt, Okta), identity providers (Active Directory, Entra ID, Okta), privileged access management (PAM) solutions (CyberArk, BeyondTrust), and application access logs. Log data includes certification campaign results, manager attestation decisions, access revocations, SOD violation detections, orphaned account discoveries, authentication successes/failures, privilege escalations, role assignments, and policy violations.

Retention policies align with regulatory requirements (7 years for SOX/financial systems, 6 years for HIPAA, 3 years for PCI DSS, GDPR-compliant deletion for EU data subjects) and legal hold procedures. Log integrity mechanisms include write-once storage, cryptographic hashing (SHA-256), digital signatures, centralized syslog aggregation, and immutable storage (AWS S3 Object Lock, Azure Immutable Blob Storage) to prevent tampering and ensure forensic validity. Automated alerting detects suspicious access patterns, failed certification campaigns, excessive privilege grants, and compliance violations in real-time.

### Strategic Importance

- **Audit Evidence & Compliance**: Provides irrefutable evidence for SOC 2, ISO 27001, PCI DSS, HIPAA, SOX, and regulatory audits; demonstrates control effectiveness and continuous monitoring
- **Forensic Investigation**: Enables incident response teams to reconstruct attack timelines, identify compromised accounts, trace lateral movement, and determine scope of unauthorized access during breach investigations
- **Non-Repudiation**: Creates legally admissible audit trail with timestamps, user identities, IP addresses, and geolocation data to prevent users from denying access certification decisions or policy violations
- **Insider Threat Detection**: Identifies anomalous access patterns including after-hours access, privilege escalation attempts, bulk data downloads, unusual application access, and access from suspicious geolocations
- **Compliance Monitoring**: Tracks certification campaign completion rates, time-to-remediation for access violations, SOD conflict resolution, orphaned account cleanup, and privileged access governance metrics
- **Root Cause Analysis**: Enables post-incident analysis to identify control failures, process gaps, and training deficiencies that contributed to security events or audit findings

## Purpose & Scope

### Primary Purpose

This artifact defines comprehensive logging requirements, retention schedules, access controls, integrity mechanisms, monitoring/alerting rules, and audit reporting capabilities for all access governance activities. It establishes technical implementation standards for SIEM integration, log aggregation, tamper-proof storage, and compliance-ready reporting to support regulatory audits, security investigations, and operational analytics.

### Scope

**In Scope**:
- **Access Certification Logs**: Campaign launch/completion timestamps, reviewer identities, certification decisions (approve/deny/exception), business justifications, bulk certification actions, delegation workflows, non-response escalations, auto-revocation events, remediation completion
- **Account Lifecycle Events**: Account creation (user ID, creation date, requester, approver), modifications (role changes, entitlement grants/revokes), deactivations (termination date, disabling authority), reactivations (requester, business justification), deletions (archival date, retention compliance)
- **Role & Entitlement Changes**: Role assignments/removals, entitlement grants/revokes, privilege escalations (temporary admin rights, sudo access), privileged access approvals, role mining results, SOD violation detections, role lifecycle changes
- **Authentication & Access Events**: Successful/failed login attempts (timestamp, source IP, geolocation, device fingerprint), multi-factor authentication (MFA) enrollments/validations, password changes/resets, single sign-on (SSO) assertions, session creations/terminations, concurrent session violations
- **Privileged Access Activity**: PAM vault checkouts/checkins, session recordings metadata (duration, commands executed), privilege elevation events, emergency access (break-glass) usage, shared account access, service account password rotations, admin console access
- **Access Request & Approval Workflows**: Access request submissions, approval chain routing, approver decisions (approved/denied), exception approvals, temporary access grants (start/end dates), access request expirations, SLA compliance (time-to-approval metrics)
- **SOD & Policy Violations**: Toxic combination detections, policy violation alerts, compensating control validations, exception approvals with business justification, remediation tracking, false positive dismissals
- **IGA System Administrative Actions**: IGA platform configuration changes, certification campaign configuration, role definition updates, SOD rule modifications, connector deployments, policy changes, user provisioning rule updates
- **SIEM Integration & Correlation**: Real-time log ingestion from IGA platforms, identity providers, PAM solutions, applications; correlation rules for suspicious access patterns; automated alert generation; integration with SOAR platforms (Palo Alto XSOAR, Splunk SOAR, IBM Resilient)
- **Log Retention & Archival**: Hot storage (0-90 days in SIEM for active analysis), warm storage (91 days - 1 year in compressed formats), cold storage (1-7 years in archival systems like AWS Glacier, Azure Archive), compliance-driven deletion after retention expiration
- **Tamper-Proof Mechanisms**: Write-once-read-many (WORM) storage, cryptographic hashing (SHA-256/SHA-512) with hash verification, digital signatures using PKI, centralized syslog with TLS encryption, immutable cloud storage configurations, blockchain-based audit trails (experimental)
- **Reporting & Analytics**: Compliance dashboards (certification completion rates, SOD violations), executive summaries, audit evidence packages, forensic timeline reconstruction, user behavior analytics (UBA), access anomaly detection

**Out of Scope**:
- **Application-Specific Logs**: Covered in application-logging-standards artifact (application errors, performance metrics, business transaction logs, debugging information)
- **Infrastructure & Network Logs**: Covered in infrastructure-logging-policy artifact (firewall logs, IDS/IPS alerts, VPN connections, network device configurations, DNS queries)
- **Data Access Audit Logs**: Covered in data-access-logging artifact (database query logs, file access logs, data export events, encryption key usage)
- **Security Incident Logs**: Covered in incident-response-plan artifact (SOC investigation notes, containment actions, eradication procedures, lessons learned)
- **Physical Access Logs**: Covered in physical-security-policy artifact (badge swipes, visitor logs, CCTV footage, alarm system events)
- **Log Analysis & Threat Hunting Procedures**: Covered in threat-hunting-playbook artifact (investigation workflows, IOC searches, threat intelligence correlation)
- **SIEM Platform Administration**: Covered in siem-administration-guide artifact (platform configuration, parser development, index management, performance tuning)

### Target Audience

**Primary Audience**:
- **Security Operations Center (SOC) Analysts**: Monitors real-time access alerts, investigates suspicious authentication patterns, triages access violations, escalates incidents, creates security tickets
- **Compliance & Audit Teams**: Extracts audit evidence for certifications (SOC 2, ISO 27001, PCI DSS), validates control effectiveness, reviews certification completion rates, samples access decisions for testing
- **Forensic Investigators**: Reconstructs incident timelines during breach investigations, identifies patient zero and lateral movement paths, determines scope of unauthorized access, preserves evidence for legal proceedings
- **IAM Operations Team**: Reviews certification campaign metrics, troubleshoots IGA platform issues, validates log completeness, manages log retention policies, responds to audit data requests
- **Privacy Officers/DPO**: Manages GDPR right-to-erasure requests for access logs, validates lawful basis for log retention, ensures compliance with data protection impact assessments (DPIA)

**Secondary Audience**:
- **Chief Information Security Officer (CISO)**: Reviews executive dashboards of access governance metrics, presents audit readiness to board/audit committee, approves log retention policies, funds SIEM platform investments
- **Internal Audit**: Tests logging controls for completeness and accuracy, validates log integrity mechanisms, reviews retention compliance, assesses segregation of duties in log administration
- **External Auditors (SOC 2, ISO, PCI QSA)**: Examines log samples for audit testing, validates timestamp accuracy and synchronization, confirms tamper-proof controls, reviews retention policy compliance
- **Legal/eDiscovery Teams**: Requests access logs for employment litigation, intellectual property theft investigations, regulatory inquiries, preserves logs under legal hold
- **Threat Intelligence Teams**: Analyzes access patterns for indicators of compromise (IOCs), correlates with external threat intelligence feeds, identifies attack patterns, shares TTPs with ISAC/ISAO
- **IT Leadership**: Reviews operational metrics (system uptime, log ingestion rates, storage utilization), approves budget for log storage expansion, prioritizes SIEM integration projects

## Document Information

**Format**: Markdown

**File Pattern**: `*.access-review-logs.md`

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
**Centralized Aggregation**: Consolidate all access logs into SIEM platform; avoid siloed logging in individual applications
**Time Synchronization**: Configure NTP on all systems; ensure sub-second timestamp accuracy for forensic correlation
**Immutable Storage**: Implement WORM or immutable blob storage for compliance-critical logs to prevent tampering
**Automated Alerting**: Configure real-time alerts for failed certifications, SOD violations, privileged access anomalies, suspicious authentication patterns
**Log Completeness Testing**: Periodically test that all systems are sending logs; alert on missing or delayed log sources
**Storage Capacity Planning**: Monitor log ingestion rates and storage growth; project 12-18 months capacity to avoid emergency expansions
**Compression & Archival**: Compress logs after 90 days to reduce storage costs; migrate to cold storage (AWS Glacier, Azure Archive) after 1 year
**Search Performance Optimization**: Index frequently queried fields (user ID, timestamp, event type); use hot/warm/cold data tiers in SIEM
**Compliance-Ready Exports**: Create pre-configured audit reports for SOC 2, PCI DSS, ISO 27001 evidence requests
**GDPR Right to Erasure**: Implement user ID pseudonymization or tokenization to enable selective log deletion without destroying audit trail
**Legal Hold Procedures**: Suspend automated log deletion when legal hold issued; preserve chain of custody for litigation
**Log Review Cadence**: Review access violation alerts daily, certification metrics weekly, compliance dashboards monthly, retention compliance quarterly
**SIEM Parser Development**: Develop custom parsers for proprietary IGA platforms to normalize log formats and extract key fields
**Correlation Rule Tuning**: Reduce false positives through iterative tuning; document exceptions for persistent false positives
**Privileged User Monitoring**: Apply enhanced logging and alerting for accounts with admin/root privileges
**Anomaly Detection Baselines**: Establish normal access patterns per user/role; alert on statistically significant deviations
**Integration with SOAR**: Automate incident ticket creation, access revocation, and notification workflows for critical access violations
**Audit Trail Integrity Validation**: Periodically verify cryptographic hashes; test ability to detect log tampering
**Vendor Log Integration**: Prioritize native integrations (SIEM app/add-on) over custom syslog parsing to accelerate time-to-value
**Cloud-Native Logging**: Leverage cloud provider audit logs (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) for infrastructure access
**Log Source Health Monitoring**: Alert when log sources stop sending data, experience delays, or show dropped events

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

**Logging & Audit Trail Standards**:
- NIST SP 800-92: Guide to Computer Security Log Management (log generation, transmission, storage, analysis, disposal)
- NIST SP 800-53 Rev 5: AU-2 (Event Logging), AU-3 (Content of Audit Records), AU-6 (Audit Record Review), AU-9 (Protection of Audit Information), AU-11 (Audit Record Retention), AU-12 (Audit Record Generation)
- ISO/IEC 27001:2022: A.8.15 (Logging), A.8.16 (Monitoring activities), A.12.4.1 (Event logging), A.12.4.2 (Protection of log information), A.12.4.3 (Administrator and operator logs), A.12.4.4 (Clock synchronization)
- ISO/IEC 27002:2022: 8.15 (Logging), 8.16 (Monitoring activities)
- CIS Controls v8: 8.2 (Collect Audit Logs), 8.3 (Ensure Adequate Audit Log Storage), 8.5 (Collect Detailed Audit Logs), 8.6 (Collect DNS Query Audit Logs), 8.9 (Centralize Account Management), 8.11 (Conduct Audit Log Reviews)

**Compliance & Regulatory Requirements**:
- SOC 2 Type II: CC7.2 (System monitored to detect security incidents), CC6.1-CC6.3 (Logical access logging and monitoring), CC6.8 (Access logs protected from unauthorized modification)
- PCI DSS v4.0: Requirement 10 (Log and Monitor All Access to System Components and Cardholder Data), 10.2 (Audit logs capture appropriate events), 10.3 (Audit log entries include sufficient detail), 10.4 (Audit logs protected from unauthorized modification), 10.6 (Audit logs reviewed), 10.7 (Audit log retention)
- HIPAA Security Rule: 164.308(a)(1)(ii)(D) (Information system activity review), 164.312(b) (Audit controls), 164.312(c)(1) (Integrity controls), 45 CFR 164.316(b)(2)(i) (Retention of documentation - 6 years)
- GDPR: Article 30 (Records of processing activities), Article 32 (Security of processing - logging), Article 17 (Right to erasure - log deletion requirements)
- SOX (Sarbanes-Oxley): ITGC audit trail requirements for financial system access, change management logging, segregation of duties enforcement
- GLBA (Financial Services): 16 CFR Part 314.4 (Safeguards Rule - audit trail requirements)
- FISMA/FedRAMP: AU family controls for federal systems, log retention per NARA schedules
- FFIEC: IT Examination Handbook - Audit Trail requirements for financial institutions
- CMMC (Defense Industrial Base): AU.L2-3.3.1 through AU.L2-3.3.9 (Audit and accountability controls)

**Industry-Specific Regulations**:
- NERC CIP (Electric Utilities): CIP-004-6 (Personnel and training - access logging), CIP-005-6 (Electronic security perimeters), CIP-007-6 (System security management - audit trails)
- FDA 21 CFR Part 11 (Pharmaceuticals): Electronic records and signatures - audit trail requirements for GxP systems
- FINRA (Financial Services): Rule 4511 (Books and records requirements including access logs)
- NYDFS Cybersecurity Regulation (23 NYCRR 500): Section 500.06 (Audit trail requirement for financial services firms in New York)

**Logging Technology Standards**:
- Syslog Protocol (RFC 5424/5425/5426): Standardized message format for log transmission
- Common Event Format (CEF): ArcSight CEF for structured log data
- Elasticsearch Common Schema (ECS): Standardized field mappings for Elastic Stack
- OCSF (Open Cybersecurity Schema Framework): Vendor-agnostic schema for security event logging
- STIX/TAXII: Structured threat information logging and sharing
- Cloud-Native Logging: AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs standards

**SIEM Platform Guidance**:
- Splunk Enterprise Security: Use cases for access governance monitoring, compliance reporting
- Elastic Security: Detection rules for access anomalies, SIEM implementation best practices
- Microsoft Sentinel: Analytics rules for access violations, workbook templates, data connectors
- IBM QRadar: Custom rule development, log source integration, compliance reporting
- Sumo Logic: Continuous intelligence for access governance, compliance dashboards
- LogRhythm: Security analytics playbooks, compliance automation

**Time Synchronization Standards**:
- NTP (Network Time Protocol) RFC 5905: Time synchronization for accurate log timestamps
- NIST Time Services: Authoritative time sources for audit log timestamping
- IEEE 1588 Precision Time Protocol (PTP): High-accuracy time synchronization
- Windows Time Service (W32Time): Active Directory time synchronization

**Log Integrity & Forensics**:
- NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response
- RFC 5848: Signed Syslog Messages for log integrity
- ISO/IEC 27037: Guidelines for identification, collection, acquisition and preservation of digital evidence
- SWGDE (Scientific Working Group on Digital Evidence): Best practices for digital evidence handling
- Chain of Custody Requirements: Forensically sound log preservation for legal proceedings

**Data Retention & Privacy**:
- NIST SP 800-88: Guidelines for Media Sanitization (secure log deletion after retention period)
- ISO/IEC 27040: Storage security including backup and archival of audit logs
- GDPR Article 5(1)(e): Storage limitation principle for log retention
- State Data Retention Laws: California, New York, Massachusetts requirements for log retention

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
