# Name: terms-of-service

## Executive Summary

Terms of Service (ToS) are binding legal agreements governing user access to SaaS platforms, web applications, APIs, and digital services. These contracts establish acceptable use policies, service level commitments, intellectual property rights, payment terms, liability limitations, and dispute resolution mechanisms. Modern ToS must balance business protection (limitation of liability, indemnification clauses, data usage rights) with regulatory compliance (GDPR Article 7, CCPA disclosure requirements, accessibility standards, and jurisdiction-specific consumer protection laws).

Digital service providers face evolving legal landscapes requiring ToS adaptation for data privacy (GDPR, CCPA, LGPD), AI/ML transparency (EU AI Act), content moderation (DSA/DMA in EU), and cross-border data transfers (Privacy Shield invalidation, Standard Contractual Clauses). Automated ToS acceptance tracking, version control, and user notification of changes have become essential compliance requirements. Organizations must implement clickwrap agreements (requiring affirmative consent) or browsewrap agreements (consent by use), with strong preference for clickwrap to ensure enforceability in litigation.

### Strategic Importance

- **Legal Enforceability**: Establishes contractual relationship with users, enabling breach remedies, account termination, and dispute resolution
- **Liability Protection**: Limits damages, disclaims warranties, and establishes indemnification obligations to cap legal exposure
- **GDPR/CCPA Compliance**: Satisfies disclosure requirements for data collection, processing purposes, and user rights under privacy regulations
- **Acceptable Use Policy**: Defines prohibited activities (spam, malware, IP infringement, illegal content) enabling account termination and platform integrity
- **Intellectual Property Protection**: Asserts ownership of service IP while granting limited user licenses and protecting trademark rights
- **Jurisdictional Control**: Establishes governing law, venue for disputes, and arbitration clauses to manage litigation risk and forum shopping
- **Service Level Transparency**: Documents uptime commitments, maintenance windows, and availability guarantees managing customer expectations

## Purpose & Scope

### Primary Purpose

This artifact establishes the legal contract between service providers and users, defining rights, responsibilities, restrictions, and remedies for platform access and usage. It protects organizational interests through liability limitations, indemnification clauses, and termination rights while satisfying regulatory disclosure requirements under GDPR, CCPA, and consumer protection laws. The ToS enables enforcement of acceptable use policies, intellectual property protection, and payment collection while managing legal risk through venue selection, arbitration clauses, and warranty disclaimers.

### Scope

**In Scope**:
- Account registration, eligibility requirements (age restrictions, geographic limitations, business vs. personal use)
- Acceptable Use Policy (AUP): prohibited content, spam, malware, illegal activities, IP infringement, resource abuse
- Service Level Agreements (SLA): uptime commitments, maintenance windows, performance guarantees, compensation for downtime
- Payment terms: pricing, billing cycles, automatic renewal, refund policies, payment method requirements, late fees
- Intellectual property: service ownership, user-generated content licenses, trademark usage, DMCA takedown procedures
- Privacy and data: data collection practices, GDPR/CCPA rights, data retention, cross-border transfers, cookies
- Liability limitations: damages caps, consequential damages disclaimers, force majeure, third-party content exclusions
- Indemnification: user obligation to defend provider against claims arising from user conduct or content
- Termination: grounds for suspension/termination, data export rights, survival clauses, effect on payment obligations
- Dispute resolution: governing law, jurisdiction, arbitration clauses (JAMS, AAA), class action waivers, small claims carve-outs
- Modification rights: provider's ability to update ToS, user notification requirements, continued use as acceptance

**Out of Scope**:
- Detailed privacy policy (separate Privacy Policy document required under GDPR Article 13)
- Enterprise Master Services Agreements (MSA) and custom contract terms for large customers
- API-specific terms of service (may be separate Developer Agreement)
- Data Processing Agreements (DPA) for GDPR Article 28 processor obligations
- Service Level Agreements (SLA) with specific uptime percentages (often separate exhibit)
- Open-source software licenses for code distributed to users

### Target Audience

**Primary Audience**:
- Legal Counsel: ToS drafting, regulatory compliance review, dispute resolution clause design, enforceability analysis
- Product/Business Teams: Acceptable use policy definition, service scope boundaries, pricing terms, feature limitations
- Compliance Officers: GDPR Article 7 consent requirements, CCPA disclosure obligations, FTC Act Section 5 review
- Risk Management: Liability exposure assessment, insurance policy alignment, indemnification scope evaluation

**Secondary Audience**:
- Customer Success: User inquiries about ToS terms, account termination appeals, refund policy interpretation
- Security/Trust Teams: Abuse reporting workflows, account suspension criteria, law enforcement cooperation terms
- Engineering: ToS acceptance tracking implementation, version control, user notification automation
- Sales: Enterprise customer ToS negotiation, MSA vs. ToS applicability, custom terms approval workflows

## Document Information

**Format**: Markdown

**File Pattern**: `*.terms-of-service.md`

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

**Clickwrap over Browsewrap**: Use affirmative acceptance (checkbox + "I agree" button) rather than implied consent for stronger enforceability
**Plain Language Drafting**: Write ToS in accessible language (8th-grade reading level) to satisfy FTC reasonableness standards and EU clarity requirements
**Conspicuous Terms**: Highlight key provisions (liability limitations, arbitration clauses) in bold or larger font to prevent unconscionability challenges
**Separate Privacy Policy**: Link to distinct Privacy Policy to satisfy GDPR Article 13 requirement for detailed data processing disclosures
**Version Control**: Append version number and "Last Updated" date; maintain archive of all historical versions for litigation defense
**Material Change Notification**: Email users about significant ToS updates; require re-acceptance for material changes affecting rights or liabilities
**Acceptance Tracking**: Log timestamped acceptance events (IP address, user ID, ToS version) in immutable audit trail
**GDPR Consent Separation**: Don't bundle ToS acceptance with marketing consent; GDPR Article 7 requires granular, unbundled consent
**Arbitration Clause Carve-Outs**: Include small claims court exception and individual arbitration requirement to satisfy consumer fairness standards
**Class Action Waiver Review**: Post-Epic Systems v. Lewis, review enforceability; some jurisdictions limit consumer class action waivers
**Geographic Scope**: Specify which ToS applies to which regions (EU users may need separate ToS for DSA/GDPR compliance)
**Severability Clause**: If one provision is unenforceable, remaining terms survive rather than invalidating entire agreement
**Force Majeure**: Define service disruption exceptions (natural disasters, cyberattacks, infrastructure failures) to limit breach liability
**DMCA Safe Harbor**: Include proper DMCA agent designation and takedown procedures to maintain Section 512 safe harbor protections
**Payment Processor Terms**: Coordinate ToS with Stripe/PayPal ToS requirements; payment processor violations can cause ToS breaches
**Refund Policy Clarity**: Clearly state refund eligibility, timelines, and procedures to avoid chargeback disputes and FTC deception findings
**Data Retention Terms**: Specify how long data is retained post-termination; align with GDPR Article 17 right-to-erasure obligations
**Third-Party Integrations**: Disclaim liability for third-party services (OAuth providers, CDNs, analytics) that users interact with
**Accessibility Compliance**: Ensure ToS page meets WCAG 2.1 Level AA for screen readers; accessibility of legal terms may be required
**Regular Legal Review**: Have counsel review ToS annually or when regulations change (GDPR, state privacy laws, new case law)

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

**Privacy Regulations**:
- GDPR (General Data Protection Regulation) Articles 7, 12, 13, 14 (consent and transparency requirements)
- CCPA (California Consumer Privacy Act) Section 1798.100 (disclosure obligations)
- LGPD (Brazil Lei Geral de Proteção de Dados)
- PIPEDA (Canadian Personal Information Protection and Electronic Documents Act)
- UK Data Protection Act 2018
- Virginia CDPA, Colorado CPA, Connecticut CTDPA (state privacy laws)

**Consumer Protection Laws**:
- FTC Act Section 5 (unfair or deceptive practices)
- EU Consumer Rights Directive 2011/83/EU
- UK Consumer Rights Act 2015
- California's CLRA (Consumer Legal Remedies Act)
- Unfair Contract Terms Act 1977 (UK)
- Australian Consumer Law (ACL)

**Content and Platform Regulation**:
- EU Digital Services Act (DSA) and Digital Markets Act (DMA)
- DMCA (Digital Millennium Copyright Act) Section 512 safe harbor provisions
- Communications Decency Act Section 230 (US platform immunity)
- UK Online Safety Act 2023
- NetzDG (German Network Enforcement Act)
- Australia's Online Safety Act 2021

**Accessibility Requirements**:
- WCAG 2.1 Level AA (Web Content Accessibility Guidelines)
- Section 508 (US federal accessibility standards)
- ADA Title III (Americans with Disabilities Act web accessibility)
- EN 301 549 (European accessibility standard)

**Electronic Contracting**:
- E-SIGN Act (US Electronic Signatures in Global and National Commerce Act)
- UETA (Uniform Electronic Transactions Act)
- eIDAS Regulation (EU electronic identification and trust services)
- UNCITRAL Model Law on Electronic Commerce

**Arbitration and Dispute Resolution**:
- Federal Arbitration Act (FAA) 9 USC
- JAMS (Judicial Arbitration and Mediation Services) rules
- AAA (American Arbitration Association) Consumer Arbitration Rules
- UNCITRAL Arbitration Rules (international disputes)
- EU Mediation Directive 2008/52/EC

**Industry-Specific Regulations**:
- COPPA (Children's Online Privacy Protection Act) for services directed at children under 13
- FERPA (Family Educational Rights and Privacy Act) for educational services
- HIPAA (Health Insurance Portability and Accountability Act) for health services
- GLBA (Gramm-Leach-Bliley Act) for financial services
- PCI DSS (Payment Card Industry Data Security Standard) for payment processing

**Contractual Best Practices**:
- Restatement (Second) of Contracts (US contract law principles)
- Uniform Commercial Code (UCC) Article 2 (sales of goods)
- ProCD v. Zeidenberg (clickwrap enforceability precedent)
- Specht v. Netscape (browsewrap insufficient notice precedent)
- AT&T Mobility v. Concepcion (arbitration clause enforceability)

**ToS Management Tools**:
- TermsFeed (automated ToS/Privacy Policy generator)
- Iubenda (compliance management platform)
- OneTrust (consent and preference management)
- TrustArc (privacy compliance platform)
- Termly (ToS and cookie consent automation)

**Version Control and Acceptance Tracking**:
- ToS version history and change logs
- Timestamped user acceptance records
- Email notification of ToS updates
- Re-acceptance workflows for material changes
- Archived ToS versions for litigation defense

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
