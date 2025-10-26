# Name: crash-triage-playbooks

## Executive Summary

The Crash Triage Playbooks artifact provides standardized, repeatable procedures for rapidly diagnosing, categorizing, and responding to application crashes and system failures. These playbooks enable security operations and development teams to systematically investigate crashes that may indicate security incidents, perform root cause analysis, and coordinate remediation efforts while maintaining evidence integrity for potential forensic investigation.

As a critical component of incident response and security operations, this artifact serves both technical responders who need step-by-step guidance during high-pressure triage situations and security leadership who require assurance that crashes are evaluated for security implications. It bridges the gap between traditional crash debugging and security incident response, ensuring that potential exploitation attempts, vulnerabilities, or malicious activity are identified during crash investigation.

### Strategic Importance

- **Security-First Response**: Ensures crashes are evaluated for security implications before treating as operational issues
- **Evidence Preservation**: Maintains forensic integrity of crash artifacts for potential security investigations
- **Response Consistency**: Standardizes triage procedures across teams and incident types
- **Threat Detection**: Identifies patterns that may indicate active exploitation or attack campaigns
- **Integration with SIEM/SOAR**: Enables automated enrichment and correlation with security event data
- **Compliance Support**: Demonstrates systematic approach to investigating potential security incidents

## Purpose & Scope

### Primary Purpose

This artifact serves as the definitive procedural guide for triaging application crashes and system failures with a security-first mindset, ensuring rapid classification, appropriate escalation, evidence preservation, and coordinated response while distinguishing between benign software defects and potential security incidents.

### Scope

**In Scope**:
- Crash detection and initial classification procedures
- Security-focused triage decision trees and criteria
- Memory dump collection and analysis procedures
- Crash signature extraction and correlation techniques
- MITRE ATT&CK technique identification from crash patterns
- Integration with SIEM, SOAR, and ticketing systems
- Evidence preservation and chain of custody procedures
- Escalation paths for suspected exploitation attempts
- Communication templates for stakeholder notifications
- Post-crash system state validation procedures
- Automated crash analysis tool integration
- Correlation with vulnerability intelligence and threat feeds
- Metrics collection for crash trend analysis
- Playbook versioning and continuous improvement

**Out of Scope**:
- Detailed code-level debugging procedures (covered by development documentation)
- Long-term application performance tuning (covered by operational runbooks)
- Infrastructure capacity planning (handled by infrastructure team)
- Product feature decisions based on crash data (product management responsibility)
- Legal proceedings and litigation support (legal department handles)

### Target Audience

**Primary Audience**:
- Security Operations Center (SOC) analysts performing initial crash triage
- Incident Response team members investigating suspected security incidents
- DevSecOps engineers integrating security into crash analysis workflows
- Site Reliability Engineers (SREs) evaluating production system stability

**Secondary Audience**:
- Application security engineers reviewing crash patterns for vulnerability indicators
- Threat intelligence analysts correlating crashes with known attack campaigns
- Security leadership requiring visibility into potential security-related failures
- Compliance teams documenting incident response capabilities
- Development teams implementing crash mitigation and remediation

## Document Information

**Format**: Markdown

**File Pattern**: `*.crash-triage-playbooks.md`

**Naming Convention**: `{system-name}.{environment}.crash-triage-playbooks.md` (e.g., `payment-api.production.crash-triage-playbooks.md`)

**Template Location**: `templates/crash-triage-playbooks-template.md`

**Storage & Access**: Store in security operations repository with access controls limiting to security and incident response personnel

**Classification**: Confidential (contains sensitive operational security procedures)

**Retention**: Retain for 7 years minimum to support security incident investigations and compliance audits


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Quarterly review required, or after any critical security incident
- `documentOwner`: Security Operations Manager or Incident Response Lead
- `classification`: Confidential
- `retentionPeriod`: 7 years

**Authorship & Review**:
- `primaryAuthor`: Security Operations team lead with incident response expertise
- `contributors`: Application security engineers, SREs, threat analysts
- `reviewers`: CISO or designee, Incident Response Manager, SOC Manager
- `approvers`: CISO, VP Engineering
- `reviewStatus`: Current review status (Draft | In Review | Approved | Archived)
- `approvalDate`: Date of formal approval by CISO

**Document Purpose**:
- `executiveSummary`: Standardized crash triage procedures with security-first approach
- `businessContext`: Ensures crashes are systematically evaluated for security implications and enables rapid, consistent response
- `scope`: Covers crash detection through remediation coordination for all production systems
- `applicability`: Mandatory for all security operations and incident response personnel
- `relatedDocuments`: Incident Response Plan, Security Monitoring Runbooks, Forensics Procedures

### Main Content Sections

**Crash Detection & Classification**:
- Automated crash detection mechanisms (monitoring, APM, SIEM integration)
- Initial severity classification matrix (Critical, High, Medium, Low)
- Security indicator checklist (exploitation signatures, abnormal patterns)
- Decision tree for security vs. operational routing
- Timeframe requirements for each severity level

**Security-Focused Triage Procedures**:
- Memory dump acquisition and secure storage procedures
- Crash signature extraction and normalization techniques
- Correlation with CVE databases and exploit intelligence
- MITRE ATT&CK technique mapping from crash characteristics
- User context and access level analysis
- Network activity correlation around crash time
- File system and registry changes detection

**Evidence Preservation & Forensics**:
- Chain of custody documentation requirements
- Secure artifact storage procedures and access controls
- Forensic imaging procedures for suspected compromises
- Log aggregation and timeline reconstruction
- Preservation of volatile vs. non-volatile data
- Integration with forensic analysis tools

**Escalation & Communication**:
- Escalation criteria and decision matrices
- Stakeholder notification templates and timing requirements
- Incident declaration procedures
- War room activation criteria
- External reporting requirements (regulators, customers, partners)
- Post-incident communication protocols


## Best Practices

**Automated Detection Integration**: Deploy crash detection across all monitoring platforms (APM, SIEM, logging aggregators) with automated enrichment and correlation
**Security-First Mindset**: Always evaluate crashes for security implications before treating as pure operational issues
**Evidence Preservation**: Immediately secure crash artifacts, memory dumps, and logs before any remediation activities
**Standardized Classification**: Use consistent severity and security risk classification across all crash types and systems
**MITRE ATT&CK Mapping**: Map crash characteristics to MITRE ATT&CK techniques to identify potential attack patterns
**Chain of Custody**: Maintain strict chain of custody for all crash artifacts that may become forensic evidence
**Automated Correlation**: Integrate with threat intelligence feeds and vulnerability databases for real-time correlation
**Playbook Versioning**: Version control all playbooks and track changes to ensure teams use current procedures
**Regular Testing**: Conduct tabletop exercises and simulated crash scenarios quarterly to validate procedures
**Metrics & KPIs**: Track triage time, escalation accuracy, and false positive rates to optimize procedures
**Tool Integration**: Integrate with SOAR platforms for automated playbook execution and decision support
**Knowledge Base**: Maintain searchable repository of historical crashes and resolutions for pattern analysis
**Cross-Team Collaboration**: Establish clear handoff procedures between SOC, IR, SRE, and development teams
**Continuous Learning**: Incorporate lessons learned from each significant crash into playbook updates
**Secure Communication**: Use encrypted channels for discussing potential security incidents
**Sandbox Analysis**: Utilize isolated sandbox environments for analyzing suspicious crash artifacts
**Third-Party Coordination**: Establish procedures for coordinating with vendors on third-party component crashes
**Compliance Alignment**: Ensure procedures meet regulatory requirements for incident documentation
**Resource Accessibility**: Ensure playbooks are accessible during outages via offline copies or redundant systems
**Training & Certification**: Require annual training and certification for all personnel executing playbooks
**Escalation Awareness**: Maintain updated contact information and escalation paths with 24/7 availability
**Documentation Quality**: Use clear, concise language with visual decision trees and flowcharts
**Regular Reviews**: Review and update playbooks quarterly and after any major incident or infrastructure change
**Stakeholder Engagement**: Include input from all affected teams (security, operations, development) in playbook development
**Incident Simulation**: Conduct realistic crash simulations to identify gaps in procedures and improve response times

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

**Security Operations**: NIST SP 800-61 (Incident Handling), NIST SP 800-86 (Forensics), ISO/IEC 27035 (Incident Management), SANS Incident Response, FIRST CSIRT Framework
**Threat Intelligence**: MITRE ATT&CK Framework, MITRE D3FEND, Cyber Kill Chain, Diamond Model of Intrusion Analysis
**Forensics**: NIST SP 800-86, RFC 3227 (Evidence Collection), ISO/IEC 27037 (Digital Evidence), ACPO Digital Evidence Principles
**Application Security**: OWASP Top 10, CWE Top 25, SANS Top 25 Software Errors, NIST SSDF
**Monitoring & Observability**: OpenTelemetry, W3C Trace Context, OTEL Semantic Conventions
**Vulnerability Management**: CVSS v3.1/v4.0, CVE, NVD, FIRST EPSS
**Compliance**: SOC 2 (CC7 Incident Response), ISO 27001 A.16, PCI DSS v4.0 (Req 12.10), GDPR Article 33, HIPAA 45 CFR 164.308(a)(6)
**DevSecOps**: NIST SP 800-218 (SSDF), OWASP DevSecOps Maturity Model, BSIMM
**Cloud Security**: AWS Well-Architected Security Pillar, Azure Security Benchmark, GCP Security Best Practices, CSA CCM v4
**Logging**: NIST SP 800-92 (Log Management), OWASP Logging Cheat Sheet, Common Event Format (CEF), Syslog RFC 5424
**SIEM/SOAR Integration**: OASIS STIX/TAXII, OpenC2, MISP, Sigma Rules
**Memory Analysis**: Volatility Framework, Rekall, Windows Memory Forensics
**Crash Analysis**: Microsoft Debugging Tools, GDB, LLDB, Crashlytics standards
**Service Management**: ITIL v4 Incident Management, ISO/IEC 20000
**Business Continuity**: ISO 22301, NIST SP 800-34 (Contingency Planning)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Security Monitoring Strategy and SIEM configuration
- Incident Response Plan and escalation procedures
- Asset inventory with criticality classifications
- Vulnerability management program and CVE tracking
- Threat intelligence feeds and indicator sources
- Forensics procedures and evidence handling policies
- System architecture documentation for each application
- Logging standards and log aggregation infrastructure
- Access control policies and role definitions

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Incident Response Plan execution and case management
- Security Operations Center (SOC) runbooks and procedures
- Post-incident review and lessons learned documentation
- Threat intelligence analysis and adversary profiling
- Vulnerability remediation prioritization decisions
- Security metrics and KPI dashboards
- Compliance audit evidence and documentation
- Training materials for security operations personnel

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Incident Response Plan and procedures
- Security Monitoring Runbooks
- Forensics Investigation Procedures
- Vulnerability Management Policy
- Security Test Results and penetration testing reports
- Security Detections Catalog
- Triage Rules for automated classification
- DDoS Posture Assessments
- Purple Team Reports and Red Team Reports

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: SOC analysts and incident responders review for technical accuracy and operational feasibility
3. **Stakeholder Review**: SRE, development, and application security teams review for alignment
4. **Security Architecture Review**: Security architecture team reviews for standards compliance and integration
5. **Compliance Review**: Compliance team reviews for regulatory alignment
6. **Legal Review**: Legal counsel reviews if procedures involve evidence collection for potential legal action
7. **Final Approval**: CISO and VP Engineering provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: CISO or Security Operations Director
- Secondary Approver: VP Engineering or Infrastructure Lead
- Governance Approval: Security Governance Committee for major changes

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records in compliance management system for 7 years

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review required minimum

**Event-Triggered Updates**: Update immediately when:
- Major security incident reveals playbook deficiency
- New attack techniques or exploitation methods emerge
- Organizational infrastructure or architecture changes significantly
- Regulatory requirements change
- Major tool or platform changes occur
- Post-incident reviews identify improvement opportunities

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring, new crash types, or fundamental approach changes
- **MINOR**: New procedures, additional integrations, or substantial enhancements
- **PATCH**: Corrections, clarifications, contact updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why (incident-driven vs. proactive)
- Impact assessment (affected teams, required training)
- Approver of changes
- Related incident or improvement ticket IDs

### Archival & Retention

**Retention Period**: 7 years minimum (compliance and legal requirements)

**Archival Process**:
- Move superseded versions to secure archive with access logging
- Maintain complete version history for audit and investigation purposes
- Archive includes all supporting documentation and approval evidence
- Ensure archived versions remain accessible for historical incident investigation

### Ownership & Accountability

**Document Owner**: Security Operations Manager

**Responsibilities**:
- Ensure playbooks remain current, accurate, and aligned with infrastructure
- Coordinate quarterly reviews and post-incident updates
- Manage review and approval process
- Respond to questions and clarification requests from SOC and IR teams
- Track playbook usage metrics and effectiveness
- Coordinate training and tabletop exercises

## Templates & Examples

### Template Access

**Primary Template**: `templates/crash-triage-playbooks-template.md`

**Alternative Formats**: Word, PDF for offline access during incidents

**Template Version**: Use latest approved template version from security operations repository

### Example Artifacts

**Reference Examples**: `examples/crash-triage-playbooks-example-{application-type}.md`

**Annotated Guidance**: See annotated examples showing best practices for different application types (web applications, APIs, microservices, databases)

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified all critical applications and systems requiring crash triage procedures
- [ ] Gathered monitoring and detection capabilities inventory
- [ ] Obtained access to SIEM, APM, and forensics tools
- [ ] Engaged SOC, IR, SRE, and development teams
- [ ] Identified reviewers and approvers
- [ ] Understood applicable regulatory and compliance requirements

While creating this artifact:

- [ ] Following approved template structure
- [ ] Documenting specific tools, commands, and procedures
- [ ] Including decision trees and visual aids
- [ ] Specifying timeframes and SLAs for each procedure
- [ ] Defining clear escalation criteria
- [ ] Incorporating lessons learned from previous incidents

Before submitting for approval:

- [ ] Completed all required sections with sufficient detail
- [ ] Verified technical accuracy with SMEs
- [ ] Validated procedures through tabletop exercise
- [ ] Obtained peer review feedback from SOC and IR teams
- [ ] Addressed all review comments
- [ ] Completed all metadata fields
- [ ] Verified integration points with related systems
- [ ] Ready for formal approval process

## Governance & Compliance

### Regulatory Considerations

This artifact supports compliance with multiple regulatory frameworks:

- **SOC 2**: CC7.3 (Incident response), CC7.4 (Analysis and resolution)
- **ISO 27001**: A.16.1 (Incident management), A.12.4 (Logging and monitoring)
- **PCI DSS v4.0**: Requirement 12.10 (Incident response), 10.2 (Logging)
- **GDPR**: Article 33 (Breach notification), Article 32 (Security measures)
- **HIPAA**: 45 CFR 164.308(a)(6) (Security incident procedures)
- **NIST CSF**: DE.AE (Anomalies and events), RS.AN (Analysis), RS.MI (Mitigation)

### Audit Requirements

This artifact may be subject to:

- Internal security audits quarterly
- External SOC 2 and ISO 27001 audits annually
- Regulatory examinations by industry-specific regulators
- Customer security assessments and vendor reviews
- Penetration testing and red team validation

**Audit Preparation**:
- Maintain complete version history in secure repository
- Document all approvals with timestamps and approver details
- Keep detailed change log showing continuous improvement
- Ensure artifact and all supporting documentation accessible to auditors
- Track playbook usage metrics and incident response effectiveness

### Policy Alignment

This artifact must align with:

- Incident Response Policy and procedures
- Security Monitoring and Detection Policy
- Evidence Handling and Forensics Policy
- Data Classification and Handling Policy
- Access Control and Least Privilege policies
- Security Operations Charter and scope
- Vulnerability Disclosure and Remediation policies

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: 100% of template sections completed with specific procedures
- **Review Cycle Time**: Quarterly reviews completed within 30 days
- **Stakeholder Coverage**: Input from all affected teams (SOC, IR, SRE, Dev)
- **Approval Time**: Initial approval within 45 days of draft completion

### Usage Metrics

- **Playbook Execution Frequency**: Number of crashes triaged using playbooks per month
- **Mean Time to Triage (MTTT)**: Average time from crash detection to classification
- **Escalation Accuracy**: Percentage of security escalations that are true positives
- **Security Detection Rate**: Percentage of crashes with security implications identified
- **False Positive Rate**: Percentage of security escalations that are operational issues
- **Coverage**: Percentage of production systems with applicable playbooks

### Continuous Improvement

- Conduct post-incident reviews for all security-related crashes
- Track playbook gaps or deficiencies identified during incidents
- Analyze trends in crash types and security indicators
- Incorporate threat intelligence on new exploitation techniques
- Update procedures based on tooling and infrastructure changes
- Share lessons learned across security and engineering organizations
- Benchmark against industry standards and peer organizations

## Metadata Tags

**Phase**: Security Operations

**Category**: Incident Response & Triage

**Typical Producers**: Security Operations team, Incident Response team, Application Security engineers

**Typical Consumers**: SOC analysts, Incident responders, SREs, On-call engineers, Forensics analysts

**Effort Estimate**: 40-80 hours for initial creation, 8-16 hours per quarterly update

**Complexity Level**: High (requires deep security, forensics, and application architecture expertise)

**Business Criticality**: Mission Critical (essential for security incident response)

**Change Frequency**: Regular (quarterly reviews plus event-triggered updates)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Security Operations - Version 2.0*
