# Name: remediation-tracker

## Executive Summary

The Remediation Tracker is a critical vulnerability and compliance gap management artifact that provides systematic tracking of security findings, audit exceptions, and control deficiencies through to resolution. Organizations using integrated GRC platforms like Vanta, Drata, Secureframe, or dedicated remediation tools like Jira/ServiceNow can achieve 50-60% faster remediation cycles through automated SLA monitoring, escalation workflows, and evidence collection that ensures timely resolution of security and compliance findings.

This operational artifact establishes remediation workflows, risk-based prioritization using CVSS scoring, SLA management (Critical: 7-15 days, High: 30 days, Medium: 90 days), and audit-ready tracking of all findings through to verified closure. The tracker supports SOC 2 corrective action requirements, ISO 27001 nonconformity management, PCI-DSS vulnerability remediation (ASV scans, penetration testing), and GDPR breach remediation—reducing mean time to remediation (MTTR) by 40-50% while maintaining complete audit trails for compliance validation.

### Strategic Importance

- **Risk Reduction**: Systematically eliminates security vulnerabilities and compliance gaps with risk-based prioritization and automated SLA enforcement
- **Audit Excellence**: Provides comprehensive evidence of timely remediation for SOC 2, ISO 27001, PCI-DSS audits with 100% finding closure documentation
- **Compliance Velocity**: Accelerates certification readiness through structured gap closure with executive visibility into overdue remediations
- **Tool Integration**: Connects vulnerability scanners (Tenable, Qualys, Rapid7), GRC platforms (Vanta, Drata), and ticketing systems (Jira, ServiceNow) for unified remediation tracking
- **Metrics-Driven**: Enables data-driven security program management through MTTR tracking, SLA compliance rates, and remediation velocity dashboards

## Purpose & Scope

### Primary Purpose

This artifact provides centralized tracking and management of all security findings, audit exceptions, vulnerability scan results, penetration testing findings, and compliance gaps from identification through validated closure. The tracker enables risk-based prioritization, SLA enforcement, escalation management, and audit-ready documentation of remediation activities across the enterprise security and compliance program.

### Scope

**In Scope**:
- Vulnerability scan findings from Tenable, Qualys, Rapid7, Wiz, Snyk
- Penetration testing and red team findings with remediation validation
- Security audit findings (SOC 2, ISO 27001, PCI-DSS QSA assessments)
- Internal security assessment findings and control deficiencies  
- Bug bounty program submissions requiring remediation
- Security questionnaire gaps identified during customer assessments
- SAST/DAST findings from application security testing
- Cloud security posture findings (AWS Security Hub, Azure Defender, GCP Security Command Center)
- Compliance gap analysis findings from GRC platforms (Vanta, Drata, Secureframe)
- Third-party risk assessment findings requiring vendor remediation
- Risk-based prioritization using CVSS v3.1/v4.0 scoring
- SLA tracking with automated escalations (Critical: 7-15 days, High: 30 days, Medium: 90 days, Low: 180 days)
- Remediation status workflows (Open, In Progress, Pending Validation, Closed, Risk Accepted)
- Evidence collection for remediation verification (screenshots, scan results, code commits)
- Exception and risk acceptance processes with executive approval
- Integration with Jira, ServiceNow, Linear, Asana for task management
- MTTR metrics and remediation velocity dashboards

**Out of Scope**:
- Incident response ticket tracking (covered in Incident Response Plan)
- General IT support tickets unrelated to security findings
- Change management processes (covered in Change Management procedures)
- Proactive security project tracking (handled in Security Roadmap)
- Product feature requests or enhancements

### Target Audience

**Primary Audience**:
- Security Engineers executing remediation activities and validating closure
- Compliance Officers tracking audit finding remediation for attestations
- Development teams addressing application vulnerabilities and code defects
- Infrastructure teams remediating system and network vulnerabilities
- Security Operations teams managing vulnerability lifecycle

**Secondary Audience**:
- External auditors validating finding remediation for SOC 2/ISO 27001/PCI-DSS
- Executive leadership monitoring overdue high-risk findings
- Risk Management committees reviewing risk acceptance requests
- Customer security reviewers validating commitment to remediation SLAs

## Document Information

**Format**: Excel/CSV, Jira Board, ServiceNow, Vanta/Drata Remediation Module

**File Pattern**: `*.remediation-tracker.{xlsx|csv|jira|servicenow}`

**Naming Convention**: `[YYYY-MM]-Remediation-Tracker-v[X.Y]` or Jira project key

**Template Location**: Access approved template from GRC platform or IT Service Management system

**Storage & Access**: Store in GRC platform (Vanta, Drata, Secureframe), Jira, ServiceNow, or secure SharePoint with role-based access controls

**Classification**: Confidential (contains vulnerability details and security weaknesses)

**Retention**: 7 years post-remediation (aligned with SOC 2 audit evidence retention)

## Best Practices

**Document Management**:
- **Centralized Tracking**: Maintain single source of truth in GRC platform or ITSM tool vs. disparate spreadsheets across teams
- **Real-Time Updates**: Configure automated sync from vulnerability scanners and penetration testing tools for real-time finding ingestion
- **Version Control**: For spreadsheet-based trackers, maintain version history in SharePoint/Confluence with clear change documentation
- **Access Controls**: Limit vulnerability detail access to security team, restrict read-only access for auditors and management dashboards
- **Audit Trail**: Enable full activity logging showing all status changes, assignments, and SLA modifications with timestamps and user attribution

**Remediation Workflow & Prioritization**:
- **CVSS-Based Prioritization**: Auto-assign remediation priority based on CVSS score (9.0-10.0: Critical, 7.0-8.9: High, 4.0-6.9: Medium, 0.1-3.9: Low)
- **KEV Integration**: Escalate CISA Known Exploited Vulnerabilities to Critical priority with 7-day remediation SLA regardless of CVSS score
- **EPSS Scoring**: Incorporate Exploit Prediction Scoring System (EPSS) for dynamic risk assessment beyond static CVSS scores
- **Business Context**: Factor asset criticality, data classification, and internet exposure into prioritization decisions
- **Risk-Based SLAs**: Critical: 7-15 days, High: 30 days, Medium: 90 days, Low: 180 days with executive approval for extensions

**Integration & Automation**:
- **Vulnerability Scanner Integration**: Auto-create tickets from Tenable.io, Qualys VMDR, Rapid7 InsightVM, Wiz, Snyk with bi-directional sync
- **Jira/ServiceNow Workflows**: Map remediation statuses to ticket workflows with automatic SLA countdown and escalation rules
- **Slack/Teams Notifications**: Configure real-time alerts for new Critical/High findings, approaching SLA deadlines, and overdue remediations
- **GitHub/GitLab Integration**: Link code commits and pull requests to remediation tickets for automatic status updates upon merge
- **GRC Platform Sync**: Bi-directional integration with Vanta, Drata, Secureframe to auto-close findings when controls pass automated testing

**SLA Management & Escalation**:
- **Automated SLA Monitoring**: Configure daily SLA calculations with color-coded status (Green: >50% time remaining, Yellow: 25-50%, Red: <25%, Black: Overdue)
- **Progressive Escalation**: 75% SLA consumed: notify assignee, 90%: escalate to manager, 100%: escalate to director, 110%: executive escalation
- **SLA Pause Mechanism**: Allow temporary SLA pauses for vendor dependency, pending risk acceptance, or legitimate blockers with approval and documentation
- **SLA Compliance Metrics**: Track SLA attainment rates by priority (target: 95% Critical, 90% High, 85% Medium) and team for performance management
- **Exception Management**: Document all SLA extensions with business justification, compensating controls, and executive approval in audit trail

**Evidence & Validation**:
- **Remediation Evidence**: Require proof of fix before closure (re-scan results showing vulnerability absent, code review approval, configuration screenshots)
- **Independent Validation**: Critical/High findings require independent security team validation vs. developer self-attestation
- **Re-Scan Integration**: Auto-trigger vulnerability re-scans 24-48 hours post-claimed remediation to confirm fix effectiveness
- **False Positive Management**: Track false positive rate by scanner/test, document false positive justifications with screenshots/evidence
- **Audit Evidence Pack**: Maintain remediation evidence for 7 years including original finding, remediation evidence, validation proof, and closure approvals

**Metrics & Reporting**:
- **MTTR Tracking**: Calculate mean time to remediation by severity and trend monthly (target: Critical <10 days, High <25 days)
- **Open Finding Aging**: Report all findings by age brackets (0-30 days, 31-60 days, 61-90 days, 90+ days) with ownership assignment
- **SLA Performance**: Calculate SLA attainment % by team and severity for quarterly security metrics reviews
- **Velocity Metrics**: Track remediation velocity (findings closed per week/month) and net new finding rate to assess program effectiveness
- **Executive Dashboard**: Provide real-time executive view of critical/high overdue findings, top CVEs, and remediation trends

**Risk Acceptance**:
- **Formal Risk Acceptance Process**: Critical/High findings requiring risk acceptance must have business justification, compensating controls, and CISO/CRO approval
- **Time-Bound Acceptance**: Risk acceptances expire (max 12 months) and require annual re-review vs. indefinite acceptance
- **Compensating Controls**: Document compensating controls for risk accepted findings with validation evidence
- **Risk Register Integration**: Track risk accepted findings in enterprise risk register with regular executive review
- **Annual Re-Assessment**: Re-evaluate all risk acceptances annually or when threat landscape changes significantly

**Vulnerability Management Best Practices**:
- **Continuous Scanning**: Run authenticated scans weekly for critical assets, monthly for all systems vs. quarterly point-in-time scans
- **Penetration Testing Remediation**: Track pentest findings separately with required retest upon claim of remediation to validate fixes
- **Patch Management Integration**: Link vulnerability findings to patch management system for coordinated remediation and deployment tracking
- **Container & Cloud Security**: Integrate container scanning (Snyk, Aqua, Prisma Cloud) and CSPM findings into unified remediation workflow
- **Zero-Day Response**: Establish expedited workflow for zero-day vulnerabilities with <24 hour triage and <48 hour remediation for affected critical systems

**Compliance-Specific Requirements**:
- **SOC 2**: Document corrective actions for all audit findings with target completion dates and actual closure dates for Management's Response letter
- **ISO 27001**: Track nonconformities and opportunities for improvement with root cause analysis and corrective action plans
- **PCI-DSS**: Remediate all ASV scan failures within 30 days (critical), maintain quarterly remediation evidence for QSA audits
- **HIPAA**: Remediate identified security vulnerabilities affecting PHI systems with documented risk analysis and mitigation timeline

## Related Standards & Frameworks

**Vulnerability Management Standards**:
- NIST SP 800-40 Rev. 4 (Patch and Vulnerability Management)
- NIST SP 800-53 Rev. 5 (SI-2 Flaw Remediation, RA-5 Vulnerability Monitoring)
- NIST CSF 2.0 (DE.CM-8 Vulnerability Scans, RS.MA-1 Incident Management)
- CIS Controls v8 (7.2 Vulnerability Remediation, 7.5 Vulnerability Remediation Process)
- ISO/IEC 27001:2022 (A.8.8 Management of Technical Vulnerabilities)
- PCI-DSS v4.0 (Requirement 6.3.1 Vulnerability Management, 11.3.1 External Penetration Testing)

**Vulnerability Scoring Systems**:
- CVSS v3.1 (Common Vulnerability Scoring System)
- CVSS v4.0 (latest version with improved environmental scoring)
- EPSS (Exploit Prediction Scoring System for threat prioritization)
- CISA KEV Catalog (Known Exploited Vulnerabilities requiring priority remediation)
- OWASP Top 10 2021 (web application vulnerability categories)
- CWE Top 25 (most dangerous software weaknesses)
- SANS Top 25 (most dangerous programming errors)

**GRC & Remediation Tracking Tools**:
- Vanta (automated finding remediation for SOC 2, ISO 27001, PCI-DSS)
- Drata (compliance gap remediation workflows and evidence collection)
- Secureframe (unified control deficiency and vulnerability remediation)
- ServiceNow GRC (integrated risk and vulnerability management)
- ServiceNow Security Incident Response (finding remediation workflows)
- Jira (remediation ticket tracking and workflow management)
- Asana/Monday.com (remediation project management)
- PlexTrac (penetration test finding remediation and collaboration)

**Vulnerability Scanning & Assessment Tools**:
- Tenable.io / Tenable.sc (vulnerability management and compliance scanning)
- Qualys VMDR (vulnerability management, detection, and response)
- Rapid7 InsightVM (vulnerability management and risk analytics)
- Wiz (cloud security posture and vulnerability management)
- Snyk (application and container vulnerability scanning)
- Aqua Security (container and Kubernetes security)
- Prisma Cloud (Palo Alto cloud security and vulnerability management)
- AWS Security Hub (AWS environment vulnerability aggregation)
- Azure Defender / Microsoft Defender for Cloud
- Google Security Command Center (GCP security posture management)

**Application Security Testing**:
- Veracode (SAST/DAST application security testing)
- Checkmarx (static application security testing)
- Fortify (static and dynamic application security testing)
- SonarQube (code quality and security vulnerability detection)
- OWASP ZAP (web application penetration testing)
- Burp Suite (web application security testing)

**Penetration Testing & Red Teaming**:
- Cobalt Strike (adversary simulation and red teaming)
- Metasploit (penetration testing framework)
- PlexTrac (penetration testing reporting and remediation tracking)
- Offensive Security (OSCP penetration testing methodology)

**Bug Bounty Platforms**:
- HackerOne (managed bug bounty program)
- Bugcrowd (crowdsourced security testing)
- Synack (hybrid bug bounty platform)
- YesWeHack (bug bounty and vulnerability disclosure)

**Compliance Frameworks Requiring Remediation Tracking**:
- SOC 2 Type II (CC7.2 - System Monitoring, CC7.3 - Quality of Monitoring)
- ISO 27001:2022 (A.12.6 Technical Vulnerability Management)
- PCI-DSS v4.0 (Requirement 6 Secure Systems, Requirement 11 Testing)
- HIPAA Security Rule (45 CFR § 164.308(a)(8) Evaluation)
- FedRAMP (Vulnerability Scanning and Patch Management)
- CMMC Level 2 (RA.L2-3.11.1 Vulnerability Scanning)
- NIST RMF (Risk Management Framework vulnerability assessment)

## Integration Points

### Upstream Dependencies (Required Inputs)

- Vulnerability scan results from Tenable, Qualys, Rapid7
- Penetration testing reports and findings
- SOC 2/ISO 27001/PCI-DSS audit findings and management responses
- Application security testing results (SAST/DAST/SCA)
- Cloud security posture findings (CSPM tools)
- Security questionnaire gaps requiring remediation
- Bug bounty program submissions
- Asset inventory with criticality ratings for prioritization

### Downstream Consumers (Who Uses This)

- Security Engineers executing remediation activities
- External auditors validating corrective action completion
- Compliance teams tracking finding closure for attestations
- Executive leadership reviewing overdue high-risk findings
- Customer security reviews requesting remediation commitments
- Risk committees evaluating risk acceptance requests
- Development and Infrastructure teams addressing assigned findings

### Related Artifacts

- Vulnerability Management Policy (remediation SLA requirements)
- Penetration Testing Reports (source of findings requiring remediation)
- SOC 2/ISO 27001 Audit Reports (audit findings and corrective actions)
- Risk Register (tracking risk accepted findings)
- Incident Response Playbooks (for exploited vulnerability response)
- Patch Management Procedures (coordinated remediation deployment)
- Change Management Records (remediation changes requiring CAB approval)

## Review & Approval Process

### Review Workflow

1. **Daily Triage**: Security team triages new findings within 24 hours, assigns priority/severity, and creates remediation tickets
2. **Weekly Review**: Security leadership reviews all Critical/High findings approaching SLA deadlines and overdue remediations
3. **Monthly Metrics Review**: Security and Compliance teams review MTTR, SLA performance, and remediation velocity metrics
4. **Quarterly Executive Review**: Present remediation dashboard to executive leadership showing overdue findings, risk acceptances, and program trends
5. **Annual Audit Preparation**: Compile remediation evidence for all findings identified during SOC 2/ISO 27001/PCI-DSS audit observation periods

### Approval Requirements

**Required Approvers**:
- Security Engineer: Validates technical remediation and evidence of closure
- Security Manager: Approves risk acceptance for Medium findings
- CISO: Approves risk acceptance for Critical/High findings
- CRO/CIO: Approves risk acceptance for findings with significant business impact
- External Auditor: Validates corrective action completion for audit findings

**Approval Evidence**:
- Remediation evidence attached to ticket (re-scan results, code commits, screenshots)
- Independent validation for Critical/High findings
- Risk acceptance justification with compensating controls documented
- Executive approval documented in audit trail for risk accepted findings

## Maintenance & Lifecycle

### Update Frequency

**Daily**: Auto-sync from vulnerability scanners, pentest tools, and GRC platforms with real-time finding ingestion
**Weekly**: Security team review of all new findings, SLA status updates, and escalation management
**Monthly**: Cleanup of stale findings, false positive removals, and MTTR metric calculations
**Quarterly**: Comprehensive review of remediation program effectiveness, SLA tuning, and process improvements

**Event-Triggered Updates**: Update immediately when:
- Critical zero-day vulnerability announced affecting environment
- New penetration test or audit finding identified
- Finding marked as exploited in the wild (CISA KEV, active exploitation)
- Remediation claimed complete (triggers validation workflow)
- Risk acceptance request submitted (triggers approval workflow)
- SLA deadline approaching or exceeded (triggers escalation)

### Version Control Standards

For spreadsheet-based trackers use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant tracker redesign or remediation process overhaul
- **MINOR**: New finding categories, SLA adjustments, or additional data fields
- **PATCH**: Individual finding updates, status changes, or data corrections

### Change Log Requirements

Maintain change log documenting:
- All status transitions with timestamp and user
- SLA modifications with justification and approver
- Risk acceptance approvals with business justification
- False positive determinations with supporting evidence
- Remediation evidence additions and validation results

### Archival & Retention

**Retention Period**: 7 years post-remediation closure (aligned with SOC 2 audit requirements)

**Archival Process**:
- Archive closed findings quarterly to separate historical tracker
- Maintain searchable archive for auditor review and trend analysis
- Retain full remediation evidence (scans, screenshots, approvals) in GRC platform
- Purge findings per retention policy with CISO approval after 7 years

### Ownership & Accountability

**Document Owner**: Head of Security Operations or Vulnerability Management Lead

**Responsibilities**:
- Maintain remediation tracker accuracy and completeness
- Enforce SLA compliance and escalation procedures
- Coordinate remediation activities across Security, Engineering, and Infrastructure teams
- Report remediation metrics to executive leadership monthly
- Manage risk acceptance process and approvals
- Provide remediation evidence to external auditors
- Drive continuous improvement of remediation velocity and MTTR

## Metrics & Success Criteria

### Key Performance Indicators

- **Mean Time to Remediation (MTTR)**: Critical <10 days, High <25 days, Medium <75 days (30-40% improvement year-over-year)
- **SLA Attainment**: 95% Critical, 90% High, 85% Medium findings remediated within SLA
- **Remediation Velocity**: 80-100 findings closed per month for mature programs
- **Re-Open Rate**: <5% of closed findings re-opened due to ineffective remediation
- **False Positive Rate**: <10% of findings marked false positive after triage

### Operational Metrics

- **Open Finding Count by Severity**: Track trend of open Critical/High/Medium/Low findings weekly
- **Finding Aging**: % of findings in each age bracket (0-30, 31-60, 61-90, 90+ days)
- **Risk Acceptance Rate**: % of findings risk accepted vs. remediated (target: <5% Critical/High risk accepted)
- **Validation Success Rate**: % of claimed remediations validated successful on first attempt
- **Scanner Coverage**: % of assets scanned monthly for comprehensive vulnerability visibility

### Continuous Improvement

- Quarterly review of SLA tuning based on remediation capacity and business risk tolerance
- Post-mortem analysis of overdue Critical findings to identify process bottlenecks
- Annual assessment of remediation tool effectiveness and integration opportunities
- Regular feedback sessions with development and infrastructure teams on remediation workflow efficiency

## Metadata Tags

**Phase**: Operate & Manage

**Category**: Operations

**Typical Producers**: Security Operations, Vulnerability Management, Compliance Officers

**Typical Consumers**: Security Engineers, Development Teams, Infrastructure Teams, External Auditors, Executive Leadership

**Effort Estimate**: 10-20 hours weekly for ongoing remediation tracking and triage

**Complexity Level**: Medium to High (requires integration across multiple tools and cross-functional coordination)

**Business Criticality**: Mission Critical (directly impacts security posture, audit outcomes, and regulatory compliance)

**Change Frequency**: Frequent (daily updates from automated scans, continuous remediation activities)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Operate & Manage Phase - Version 3.0*
