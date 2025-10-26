# Name: bug-bounty-brief

## Executive Summary

The Bug Bounty Brief establishes a comprehensive vulnerability disclosure and crowdsourced security testing program that leverages the global security researcher community to identify, report, and remediate security vulnerabilities in web applications, mobile apps, APIs, cloud infrastructure, and network services. This strategic security initiative implements responsible disclosure principles aligned with ISO/IEC 29147 (Vulnerability Disclosure) and ISO/IEC 30111 (Vulnerability Handling Processes) through managed platforms including HackerOne, Bugcrowd, Synack, Intigriti, or YesWeHack, or self-hosted Vulnerability Disclosure Programs (VDP).

Modern bug bounty programs operate on three primary models: (1) Public Bug Bounty with financial rewards for verified vulnerabilities based on CVSS severity ($100-$50,000+ per finding), (2) Private/Invite-Only Bug Bounty limiting participation to vetted researchers during beta or high-sensitivity testing, and (3) Vulnerability Disclosure Policy (VDP) offering recognition and safe harbor but no monetary compensation. Programs define clear scope (in-scope assets like *.company.com, mobile apps, APIs vs. out-of-scope targets like third-party services, non-production environments), acceptable testing methods (no social engineering, DDoS, physical attacks), and safe harbor provisions providing legal protection for researchers conducting good-faith security testing.

Vulnerability triage workflows leverage dedicated security teams or platform-managed triage services to validate submissions, assign CVSS scores (Critical 9.0-10.0, High 7.0-8.9, Medium 4.0-6.9, Low 0.1-3.9), classify vulnerability types (OWASP Top 10, CWE Top 25, business logic flaws), calculate bounty rewards using severity + impact matrices, coordinate remediation with engineering teams, and manage coordinated disclosure timelines (typically 90-day disclosure deadline). Integration with vulnerability management platforms (Jira, ServiceNow, Azure DevOps), threat intelligence feeds, and security analytics enables closed-loop remediation tracking and metrics reporting on mean time to triage (MTTT), mean time to remediation (MTTR), and vulnerability trends by asset type.

### Strategic Importance

- **Continuous Security Validation**: Provides 24/7/365 security testing by thousands of ethical hackers discovering vulnerabilities before malicious actors; supplements internal security testing and annual penetration tests
- **Cost-Effective Security**: Reduces security testing costs through pay-per-vulnerability model rather than expensive annual contracts; rewards actual findings vs. time-based consultant billing
- **Diverse Testing Perspectives**: Leverages global researcher community with varied skill sets, attack techniques, and creative thinking not available from internal security teams or traditional pen testers
- **Rapid Vulnerability Discovery**: Identifies zero-day vulnerabilities, business logic flaws, and complex attack chains that automated scanners miss; provides attacker's perspective on real-world exploitability
- **Compliance & Due Diligence**: Demonstrates proactive security posture to customers, partners, regulators, and cyber insurance underwriters; satisfies continuous testing requirements for ISO 27001, SOC 2, PCI DSS
- **Responsible Disclosure Management**: Establishes clear vulnerability reporting channels preventing public disclosure or sale of vulnerabilities on dark web; builds positive security researcher relationships
- **Security Culture & Awareness**: Educates development teams on vulnerability patterns, secure coding practices, and attacker techniques through real-world vulnerability examples; drives security improvements across SDLC

## Purpose & Scope

### Primary Purpose

This brief defines bug bounty program strategy, operational procedures, platform selection criteria, scope boundaries, reward structures, triage workflows, legal considerations, and success metrics. It serves as the authoritative reference for launching, managing, and scaling crowdsourced security testing programs while ensuring responsible researcher engagement and effective vulnerability remediation.

### Scope

**In Scope**:
- **Program Models**: Public bug bounty (open to all researchers), private bug bounty (invite-only vetted researchers), VDP (vulnerability disclosure without payment), hybrid approaches, managed bug bounty (platform handles triage)
- **Platform Selection**: HackerOne (largest researcher community, managed triage options), Bugcrowd (competitive pricing, crowd management), Synack (vetted researcher network, compliance-focused), Intigriti (European focus, GDPR compliant), YesWeHack (global coverage), self-hosted VDP platforms (HackerOne Community Edition, Open Bug Bounty)
- **Scope Definition**: Web applications and APIs (production *.company.com, staging.company.com), mobile applications (iOS/Android apps, deep linking, API endpoints), cloud infrastructure (AWS/Azure/GCP public services, S3 buckets, storage accounts), source code (GitHub/GitLab public repositories), physical security (office networks if explicitly scoped)
- **Out-of-Scope Exclusions**: Third-party services (payment processors, analytics, CDNs), non-production environments (dev.company.com unless explicitly included), social engineering (phishing, vishing, pretexting), denial of service (DDoS, resource exhaustion), physical attacks, data destruction
- **Bounty Pricing Structure**: Critical vulnerabilities (RCE, SQL injection, authentication bypass, PII exposure) $5,000-$50,000+, High severity (XSS, CSRF, IDOR, privilege escalation) $1,000-$5,000, Medium severity (information disclosure, missing security headers, rate limiting bypass) $250-$1,000, Low severity (best practice violations, self-XSS, open redirects) $100-$250; bonuses for exceptional reports, chain exploits, proof-of-concept code
- **Vulnerability Classification**: OWASP Top 10 (injection, broken authentication, sensitive data exposure, XXE, broken access control, security misconfiguration, XSS, insecure deserialization, insufficient logging, SSRF), CWE Top 25, business logic flaws, API security issues (OWASP API Top 10), mobile app vulnerabilities (OWASP Mobile Top 10), CVSS v3.1 scoring
- **Triage & Validation Workflows**: Initial submission review (within 24-48 hours), duplication checking, vulnerability reproduction, CVSS scoring, severity classification, bounty calculation, engineering team assignment, remediation tracking, disclosure coordination, researcher feedback and payment
- **Coordinated Disclosure**: 90-day disclosure deadline from vulnerability report to public disclosure, extensions for complex fixes requiring architecture changes, coordinated disclosure timing with patch releases, CVE assignment for critical vulnerabilities, security advisory publication
- **Researcher Engagement**: Hall of fame/leaderboard recognition, researcher profiles and reputation scores, bonus programs for high-quality reports, invitations to private programs for top performers, swag and conference tickets, live hacking events and competitions
- **Legal Framework & Safe Harbor**: Legal safe harbor provisions protecting researchers from CFAA prosecution and DMCA violations, acceptable testing methods and prohibited activities, data handling requirements (no data exfiltration, storage, or sharing), disclosure and confidentiality terms, researcher agreement acceptance workflow
- **Integration & Automation**: Jira/ServiceNow integration for vulnerability tracking, Slack/Teams notifications for new submissions, API integration for metrics dashboards, SIEM integration for security event correlation, vulnerability management platform synchronization
- **Metrics & Reporting**: Submissions received vs. validated vulnerabilities, mean time to first response (MTTR), mean time to triage (MTTT), mean time to remediation (MTTR), vulnerability trends by type and severity, cost per vulnerability vs. traditional pen testing, researcher engagement and retention rates

**Out of Scope**:
- **Internal Security Testing**: Covered in penetration-testing-plan artifact (annual pen tests, infrastructure testing, application security assessments, red team exercises)
- **Secure Development Practices**: Covered in secure-coding-standards and secure-sdlc-policy artifacts (code review, SAST/DAST, security training, threat modeling)
- **Vulnerability Scanning**: Covered in vulnerability-management-plan artifact (Qualys, Nessus, Rapid7 automated scanning, patch management, scanner deployment)
- **Incident Response**: Covered in incident-response-plan artifact (breach response, forensic investigation, containment, recovery, post-incident review)
- **Third-Party Risk Management**: Covered in vendor-risk-management artifact (vendor security assessments, SLA requirements, supply chain security)
- **Compliance Audits**: Covered in compliance-program artifact (SOC 2, ISO 27001, PCI DSS, HIPAA audit preparation, control testing)

### Target Audience

**Primary Audience**:
- **Application Security Team**: Manages bug bounty platform, triages vulnerability submissions, validates findings, assigns CVSS scores, calculates bounties, coordinates with engineering teams, manages researcher relationships, tracks remediation
- **Product Security Engineers**: Reviews architectural implications of reported vulnerabilities, prioritizes fixes based on business risk, implements security patches, validates remediation effectiveness
- **Legal/Compliance Team**: Reviews safe harbor language, assesses legal risk of researcher activities, handles intellectual property concerns, manages disclosure agreements, ensures regulatory compliance (GDPR, CCPA)
- **Engineering/Development Teams**: Receives vulnerability reports, implements security fixes, validates patches in dev/staging, deploys remediations to production, participates in security discussions
- **Security Researchers (External)**: Reviews program scope and rules, submits vulnerability reports, provides proof-of-concept exploits, collaborates on validation, receives bounty payments and recognition

**Secondary Audience**:
- **Chief Information Security Officer (CISO)**: Approves bug bounty budget and program scope, reviews vulnerability trends and metrics, presents program ROI to executive leadership and board, prioritizes critical vulnerability fixes
- **Chief Technology Officer (CTO)**: Allocates engineering resources for vulnerability remediation, approves architectural changes, champions secure development practices based on bounty findings
- **Finance/Procurement**: Processes bounty payments, manages platform subscription costs, tracks bug bounty spend vs. budget, analyzes cost-effectiveness vs. traditional security testing
- **Public Relations/Marketing**: Coordinates public disclosure messaging, manages security advisory publications, handles media inquiries about vulnerability disclosures, promotes program to security community
- **Customer Success/Support**: Responds to customer questions about security vulnerabilities and remediation timelines, communicates security improvements to enterprise customers
- **External Auditors & Assessors**: Reviews bug bounty program during SOC 2, ISO 27001, PCI DSS audits as evidence of continuous security testing

## Document Information

**Format**: Markdown

**File Pattern**: `*.bug-bounty-brief.md`

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
**Start with VDP Before Paid Bounty**: Launch free Vulnerability Disclosure Policy to establish triage processes, legal framework, and engineering workflows before committing to paid bounties
**Clear Scope Definition**: Explicitly define in-scope assets (domains, apps, APIs) and out-of-scope targets; ambiguity leads to wasted researcher time and invalid submissions
**Safe Harbor is Critical**: Work with legal to provide strong safe harbor protecting researchers from CFAA/DMCA prosecution; without safe harbor, researchers will avoid testing your assets
**Competitive Bounty Pricing**: Benchmark bounties against industry peers using HackerOne/Bugcrowd public programs; low bounties relative to competitors reduce researcher interest
**Fast Triage SLAs**: Respond to submissions within 24-48 hours; slow triage frustrates researchers and leads to negative program reputation
**Quality Over Quantity**: Reward well-written reports with proof-of-concept code and remediation guidance higher than bare-minimum submissions; incentivizes quality
**Private Launch for Stability**: Start with invite-only private program to work out operational kinks before public launch; prevents overwhelming flood of submissions
**Dedicated Triage Resources**: Assign full-time AppSec engineer or purchase platform managed triage; part-time triage leads to SLA violations and researcher dissatisfaction
**Engineering Buy-In Required**: Ensure development teams commit to vulnerability remediation SLAs before launch; bug bounty without fixes damages program credibility
**Bonus Programs for Impact**: Offer bonuses for chain exploits, exceptional write-ups, critical business logic flaws, and previously undiscovered attack classes
**Transparent Communication**: Communicate with researchers throughout triage, validation, and remediation; radio silence leads to duplicate submissions and frustration
**Disclosure Coordination**: Respect 90-day coordinated disclosure standard; provide updates on fix progress; negotiate extensions if architecturally complex
**Duplicate Handling**: First valid submission wins bounty; later duplicates receive recognition but no payment; clearly document duplicate policy
**Data Handling Rules**: Prohibit data exfiltration, storage, or sharing in program policy; require researchers delete any data accessed during testing
**Legal Review of Reports**: Have legal counsel review reports involving PII, financial data, or potential regulatory implications before remediation
**Integration with DevOps**: Integrate bug bounty submissions into Jira/ServiceNow/Azure DevOps for seamless vulnerability tracking and remediation workflows
**Metrics Dashboard**: Track submission volume, validation rate, MTTR, bounty payouts, cost per vulnerability; present quarterly to executive leadership
**Annual Pen Test Complement**: Bug bounty complements but doesn't replace annual penetration testing; pen tests provide deeper testing of specific assets
**Researcher Relationship Management**: Treat top researchers as security partners; invite to private programs, offer live hacking event participation, provide direct communication channels
**Escalation Process**: Define escalation paths for critical/urgent vulnerabilities requiring immediate attention and emergency patches
**Brand Reputation Monitoring**: Monitor researcher community forums (Reddit, Twitter) for program sentiment; address negative feedback quickly to prevent reputation damage

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

**Vulnerability Disclosure Standards**:
- ISO/IEC 29147:2018: Information technology - Security techniques - Vulnerability disclosure
- ISO/IEC 30111:2019: Information technology - Security techniques - Vulnerability handling processes
- NIST SP 800-40 Rev 4: Guide to Enterprise Patch Management Planning (vulnerability management lifecycle)
- NIST SP 800-53 Rev 5: SI-2 (Flaw Remediation), RA-5 (Vulnerability Monitoring and Scanning)
- CERT Coordination Center: Vulnerability disclosure guidelines and coordinated disclosure practices
- Cybersecurity and Infrastructure Security Agency (CISA): Vulnerability disclosure policy recommendations

**Vulnerability Scoring & Classification**:
- CVSS v3.1 (Common Vulnerability Scoring System): Standardized severity scoring (0.0-10.0 scale)
- CWE (Common Weakness Enumeration): Software weakness taxonomy (CWE Top 25 Most Dangerous Software Weaknesses)
- CVE (Common Vulnerabilities and Exposures): Unique identifiers for publicly disclosed vulnerabilities
- OWASP Top 10 Web Application Security Risks: Injection, broken authentication, sensitive data exposure, XXE, broken access control, security misconfiguration, XSS, insecure deserialization, insufficient logging, SSRF
- OWASP API Security Top 10: Broken object level authorization, broken user authentication, excessive data exposure, resource and rate limiting, broken function level authorization, mass assignment, security misconfiguration, injection, improper assets management, insufficient logging and monitoring
- OWASP Mobile Top 10: Improper platform usage, insecure data storage, insecure communication, insecure authentication, insufficient cryptography, insecure authorization, client code quality, code tampering, reverse engineering, extraneous functionality

**Legal & Regulatory Frameworks**:
- Computer Fraud and Abuse Act (CFAA) - 18 U.S.C. § 1030: U.S. law criminalizing unauthorized computer access; safe harbor required to protect researchers
- Digital Millennium Copyright Act (DMCA) - 17 U.S.C. § 1201: Anti-circumvention provisions; safe harbor needed for security research
- General Data Protection Regulation (GDPR): Article 32 security testing requirements, Article 5 data minimization for researcher access, Article 33 breach notification
- California Consumer Privacy Act (CCPA): Data protection requirements for researcher handling of California resident data
- Department of Justice Charging Policy on CFAA: Safe harbor considerations for good-faith security research
- European NIS Directive: Network and information systems security including vulnerability management

**Industry Best Practices**:
- HackerOne Platform Documentation: Bug bounty program setup, triage workflows, bounty pricing, researcher engagement
- Bugcrowd University: Vulnerability disclosure best practices, program management, researcher community building
- Disclose.io: Open-source vulnerability disclosure framework and safe harbor templates
- NIST Cybersecurity Framework (CSF): DE.CM-8 (Vulnerability scans performed), RS.AN-5 (Processes established to receive, analyze and respond to vulnerabilities)
- Payment Card Industry Data Security Standard (PCI DSS) v4.0: Requirement 6.3.1 (Security vulnerabilities identified and addressed), Requirement 11.3 (Penetration testing performed)
- SOC 2 Trust Services: CC7.1 (System monitored for security incidents), CC7.2 (Evaluates security events), additional criteria for vulnerability management processes
- ISO/IEC 27001:2022: A.5.7 (Threat intelligence), A.8.8 (Management of technical vulnerabilities)

**Bug Bounty Platforms**:
- HackerOne: Platform features, triage services, researcher community, integration capabilities, pricing models
- Bugcrowd: Managed programs, researcher vetting, compliance support, API documentation
- Synack: Vetted researcher network, compliance-focused testing (FedRAMP, HIPAA, PCI), continuous testing model
- Intigriti: European focus, GDPR-compliant platform, researcher community, intelligence feeds
- YesWeHack: Global coverage, vulnerability database, crowd security analytics
- Open Bug Bounty: Free vulnerability disclosure coordination for website owners

**Researcher Community Resources**:
- HackerOne Hacktivity: Public vulnerability disclosure database with write-ups and proof-of-concepts
- Bugcrowd Vulnerability Rating Taxonomy: Standardized severity classification and bounty guidance
- OWASP Testing Guide: Comprehensive web application security testing methodology
- PortSwigger Web Security Academy: Free training on web vulnerability exploitation techniques
- HackerOne/Bugcrowd Researcher Guidelines: Responsible disclosure practices, report quality standards
- Security researcher ethics: Responsible disclosure principles, data handling, exploit development boundaries

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
