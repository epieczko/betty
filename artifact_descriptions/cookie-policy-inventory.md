# Name: cookie-policy-inventory

## Executive Summary

The Cookie Policy Inventory catalogs all cookies and tracking technologies deployed across web and mobile properties, providing IAB TCF 2.2 categorization (Strictly Necessary, Preferences, Statistics, Marketing), consent requirements, retention periods, and third-party vendor mappings required for GDPR Article 30, ePrivacy Directive compliance, and CCPA/CPRA disclosures.

Modern cookie inventories integrate with automated scanning tools (OneTrust Cookie Compliance, Cookiebot Scanner, TrustArc Cookie Consent) to detect first-party and third-party cookies, track changes across releases, and sync classifications with Consent Management Platforms. Cookie inventories support IAB Transparency & Consent Framework v2.2 with 10 purposes, 10 special purposes, 11 features, and 2 special features mapped to 1000+ Global Vendor List (GVL) vendors.

Organizations with comprehensive cookie inventories achieve 70-90% consent opt-in rates through transparent disclosures, reduce ePrivacy enforcement risk by 80%, and enable automated GDPR Article 30 Records of Processing Activities (RoPA) for cookie-related processing. Accurate cookie classification prevents "cookie walls" violations, ensures CCPA "Do Not Sell" compliance, and supports privacy-by-design principles through proactive tracking technology governance.

### Strategic Importance

- **ePrivacy Compliance**: Satisfies ePrivacy Directive Article 5(3) and PECR Regulation 6 cookie consent requirements across EU/UK
- **GDPR Transparency**: Fulfills Article 13/14 information obligations and Article 30 processing records for cookie-based data collection
- **CCPA/CPRA Disclosure**: Enables Section 1798.100 notice at collection and Section 1798.115 business purpose disclosures for tracking technologies
- **IAB TCF 2.2 Integration**: Maps cookies to IAB purposes (1-10), special purposes (1-2), features (1-11), and vendor consent strings
- **Consent Optimization**: Achieves 70-90% opt-in rates through granular purpose classification vs blanket accept/reject (30-50% rates)
- **Third-Party Risk Management**: Tracks 100-500+ third-party vendors (Google Analytics, Facebook Pixel, Salesforce, HubSpot) with data processing addendums
- **Privacy-by-Design**: Enables proactive cookie governance, tag management reviews, and tracking technology minimization

## Purpose & Scope

### Primary Purpose

Catalogs all cookies and tracking technologies with IAB TCF 2.2 categorization and consent requirements, enabling ePrivacy Directive compliance, GDPR Article 30 processing records, CCPA disclosures, and 70-90% consent opt-in rates through transparent cookie classification.

### Scope

**In Scope**:
- First-party cookies set by organization's domains across all web properties
- Third-party cookies from vendors (Google, Facebook, Adobe, Salesforce, HubSpot)
- IAB TCF 2.2 classification (10 purposes, 10 special purposes, 11 features, 2 special features)
- Cookie attributes (name, domain, path, expiration, httpOnly, secure, sameSite)
- Consent category mapping (Strictly Necessary, Preferences, Statistics, Marketing)
- Vendor consent string generation and Global Vendor List (GVL) mappings
- Automated cookie scanning with OneTrust, Cookiebot, TrustArc scanners
- Tag management system (GTM, Tealium, Adobe Launch) integration
- Mobile SDK tracking (Firebase, Adjust, Appsflyer, Segment)
- LocalStorage, SessionStorage, and IndexedDB fingerprinting technologies
- Cross-site tracking mechanisms and CNAME cloaking detection
- Cookie retention periods and automatic expiration policies
- Data Processing Agreement (DPA) tracking for third-party vendors
- CCPA "Do Not Sell" opt-out impact on cookie deployment

**Out of Scope**:
- Server-side tracking and backend analytics (handled by Data Processing RoPA)
- Privacy policy content authoring (handled by Legal team)
- Consent banner UI/UX design (handled by CMP vendor)
- Vendor due diligence and security assessments (handled by Vendor Management)
- Cookie consent rates optimization testing (handled by Product/Growth teams)

### Target Audience

**Primary Audience**:
- Privacy Engineers maintaining cookie inventories and CMP configurations
- Data Protection Officers (DPOs) preparing Article 30 processing records
- Legal Counsel responding to regulatory inquiries and ePrivacy enforcement
- Web Development Teams implementing tag management and consent logic

**Secondary Audience**:
- Marketing Teams understanding tracking limitations and consent impacts
- Product Managers evaluating analytics and personalization capabilities
- External Auditors validating SOC 2 Type II and ISO 27701 compliance
- Regulators (DPAs) reviewing ePrivacy and GDPR cookie compliance

## Document Information

**Format**: Markdown

**File Pattern**: `*.cookie-policy-inventory.md`

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

**Automated Scanning**: Deploy OneTrust Cookie Compliance Scanner, Cookiebot Scanner, or TrustArc Cookie Consent to automatically detect cookies across all domains every 7-14 days
**IAB TCF 2.2 Classification**: Map all cookies to IAB purposes (P1-P10), special purposes (SP1-SP2), features (F1-F11) for standardized consent management
**Four-Category Model**: Classify cookies as Strictly Necessary (no consent), Preferences, Statistics, or Marketing (consent required) per ePrivacy guidelines
**Vendor Accountability**: Maintain Data Processing Agreements (DPAs) for 100% of third-party cookie vendors with GDPR Article 28 processor obligations
**Global Vendor List (GVL) Mapping**: Reference IAB GVL vendor IDs (1000+ vendors) for standardized consent string generation and TCF compliance
**Consent Blocking**: Configure Tag Management Systems (GTM, Tealium, Adobe Launch) to block non-essential cookies until user consent obtained
**Cookie Expiration Limits**: Enforce maximum retention periods (13 months for analytics, 90 days for marketing per CNIL guidelines)
**First-Party Priority**: Migrate third-party tracking to server-side first-party implementations to reduce consent friction and improve opt-in rates
**CNAME Cloaking Detection**: Scan for CNAME subdomain tracking that bypasses browser cookie restrictions and violates ePrivacy transparency
**LocalStorage Inventory**: Include LocalStorage, SessionStorage, IndexedDB, and cache APIs in tracking technology inventory
**Mobile SDK Tracking**: Document mobile advertising IDs (IDFA, GAID), SDK trackers (Firebase, Adjust, AppsFlyer), and ATT framework compliance
**Cookie Rotation Monitoring**: Alert on new cookies discovered between scans to prevent unauthorized tracking technology deployment
**Consent Rate Benchmarking**: Track opt-in rates by category (target 70-90% Strictly Necessary + Preferences, 40-60% Statistics, 30-50% Marketing)
**Quarterly Audits**: Conduct comprehensive cookie inventory audits quarterly with automated scanning validated by manual review
**Version Control**: Maintain change history of cookie inventory with release tags synchronized to web application deployments
**Documentation Standards**: Record cookie name, domain, path, expiration, category, vendor, purpose, data elements, and legal basis
**DPA Expiration Tracking**: Monitor Data Processing Agreement renewal dates for third-party cookie vendors to prevent compliance gaps
**Cross-Domain Tracking**: Document cookie synchronization across subdomains and related domains with appropriate consent flows
**SameSite Attribute Enforcement**: Ensure all cookies set SameSite=Lax or SameSite=Strict to prevent CSRF attacks and improve privacy
**Secure & HttpOnly Flags**: Require Secure flag (HTTPS only) and HttpOnly (JavaScript inaccessible) for sensitive authentication/session cookies
**Privacy Policy Sync**: Automatically update privacy policy cookie tables from inventory to ensure accuracy and reduce manual errors
**Regulatory Mapping**: Tag cookies with applicable regulations (GDPR, ePrivacy, CCPA, LGPD) based on user geography and data flows
**Impact Analysis**: Document business impact of cookie blocking for consent-denied scenarios to inform stakeholder decisions
**Consent Management Platform (CMP) Integration**: Bi-directional sync between cookie inventory and CMP configuration for real-time accuracy
**Third-Party Risk Scoring**: Assign risk scores (Critical, High, Medium, Low) to cookie vendors based on data sensitivity and compliance posture

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

**ePrivacy Directive**: Directive 2002/58/EC Article 5(3) Cookie Consent, Directive 2009/136/EC (Cookie Law Amendment), PECR Regulation 6 (UK), ePrivacy Regulation (proposed ePR), WP29 Opinion 04/2012 on Cookie Consent Exemption, EDPB Guidelines 5/2020 on Consent

**GDPR Requirements**: Article 13 Information to be Provided (cookies/tracking), Article 14 Indirect Collection, Article 30 Records of Processing Activities (RoPA), Article 6(1)(a) Consent Legal Basis, Article 6(1)(f) Legitimate Interests for essential cookies, Recital 30 Online Identifiers

**CCPA/CPRA Disclosures**: CCPA Section 1798.100 Right to Know, Section 1798.110 Categories of Personal Information, Section 1798.115 Business Purpose, Section 1798.120 Right to Opt-Out of Sale, Section 1798.135(a) Do Not Sell My Personal Information Link, CCPA Regulations Section 999.306 Notice at Collection

**IAB Transparency & Consent Framework**: IAB TCF v2.2 Specification, 10 Purposes (P1-P10), 10 Special Purposes (SP1-SP2), 11 Features (F1-F11), 2 Special Features (SF1-SF2), Global Vendor List (GVL) 1000+ vendors, Consent Management Provider (CMP) API, TC String v2 Format

**Consent Management Platforms (CMPs)**: OneTrust Cookie Compliance, Cookiebot Consent Management, TrustArc Cookie Consent, Osano Consent Management, Usercentrics CMP, Didomi CMP, Quantcast Choice, Sourcepoint CMP, CookiePro, Termly Cookie Consent, Civic UK Cookie Control

**Automated Cookie Scanning**: OneTrust Cookie Scanner, Cookiebot Website Scanner, TrustArc Cookie Inventory, CIVIC Cookie Control Scanner, Silktide Cookie Auditor, CookieMetrix, Cookie-Script Scanner, Securiti Cookie Scanning

**Tag Management Systems**: Google Tag Manager (GTM), Adobe Experience Platform Launch, Tealium iQ Tag Management, Segment Tag Management, Ensighten Manage, Signal Tag Management, Piwik PRO Tag Manager

**Browser Cookie Policies**: Chrome SameSite Cookie Changes, Safari Intelligent Tracking Prevention (ITP 2.3), Firefox Enhanced Tracking Protection (ETP), Edge Tracking Prevention, Brave Shields, Chrome Privacy Sandbox, Topics API, FLEDGE (Interest-Based Ads)

**Cookie Technologies**: HTTP Cookies (RFC 6265), Secure Flag, HttpOnly Flag, SameSite Attribute (Lax/Strict/None), Domain Attribute, Path Attribute, Expires/Max-Age, LocalStorage API, SessionStorage API, IndexedDB API, Cache API

**Third-Party Trackers**: Google Analytics (UA/GA4), Google Ads Remarketing, Facebook Pixel, LinkedIn Insight Tag, Twitter Universal Tag, TikTok Pixel, Bing UET Tag, Salesforce Pardot, HubSpot Tracking Code, Adobe Analytics, Mixpanel, Amplitude, Heap Analytics

**Mobile Tracking**: Apple IDFA (Identifier for Advertisers), Google GAID (Google Advertising ID), Apple App Tracking Transparency (ATT) Framework iOS 14.5+, Google Play Data Safety, Firebase Analytics SDK, Adjust SDK, AppsFlyer SDK, Branch.io SDK, Segment Mobile SDKs

**Data Protection Authorities**: CNIL (France) Cookie Guidelines (13-month maximum), ICO (UK) Cookie Guidance, EDPB Guidelines on Cookie Walls, Spanish AEPD Cookie Guide, Italian Garante Cookie Rules, Belgian DPA Cookie Guidance, German DSK Cookie Guidelines

**ISO/IEC Standards**: ISO/IEC 29184:2020 Online Privacy Notices and Consent, ISO/IEC 27701:2019 Privacy Information Management, ISO/IEC 27001:2013 Information Security

**Industry Guidelines**: IAPP Cookie Consent Guide, IAB Europe TCF Implementation Guide, EDAA (European Interactive Digital Advertising Alliance), NAI (Network Advertising Initiative) Code of Conduct, DAA (Digital Advertising Alliance) Self-Regulatory Principles

**NIST Privacy Framework**: NIST Privacy Framework v1.0 Communicate Category (CM), NIST SP 800-53 Rev 5 Privacy Controls, NIST SP 800-122 Guide to Protecting PII

**Web Standards**: W3C Tracking Preference Expression (DNT), W3C Privacy Interest Group (PING), Global Privacy Control (GPC) Signal, Advanced Data Protection Control (ADPC), P3P Platform for Privacy Preferences (historical)

**Fingerprinting & Tracking**: Canvas Fingerprinting, Browser Fingerprinting, Device Fingerprinting, Cross-Site Tracking, CNAME Cloaking, Bounce Tracking, Cookie Syncing, ID Bridging, Supercookies (ETag, HSTS)

**Audit & Certification**: SOC 2 Type II Privacy Controls, ISO 27701 Lead Auditor, TrustArc Privacy Certification, ePrivacySeal, Privacy Shield (historical - invalidated Schrems II)

**Regulatory Enforcement**: CNIL €90M Google Cookie Consent Fine (2020), CNIL €60M Amazon Cookie Fine (2020), ICO Cookie Enforcement Actions, Spanish AEPD Cookie Fines, Italian Garante Google Cookie Fine €10M (2022), Belgian DPA IAB TCF Ruling

**Cookie Consent Patterns**: Cookie Walls (prohibited under GDPR), Pre-Ticked Boxes (non-compliant), Granular Consent (IAB TCF categories), Accept All / Reject All Buttons, Legitimate Interest vs Consent, Consent Refresh (12-24 months)

**Cross-Border Data Transfers**: Standard Contractual Clauses (SCCs) for cookie vendors, Binding Corporate Rules (BCRs), Adequacy Decisions (UK, Switzerland, Japan), Schrems II implications for US vendors

**Marketing Technology**: Salesforce Marketing Cloud Cookies, HubSpot Tracking Cookies, Marketo Munchkin Cookie, Eloqua Cookies, Pardot Cookies, Adobe Marketo Engage, ActiveCampaign Cookies, Mailchimp Tracking

**Analytics Platforms**: Google Analytics 4 (GA4) Privacy Controls, Adobe Analytics Privacy Settings, Matomo (Piwik) GDPR Compliance, Mixpanel GDPR, Amplitude Privacy, Heap Analytics GDPR, Plausible Analytics (privacy-first)

**Consent String Specifications**: IAB TC String v2 Format, Google Additional Consent (AC) String, GPP (Global Privacy Platform) String, MSPA (Multi-State Privacy Agreement) String

**Reference**: Consult IAB Europe TCF documentation, EDPB guidelines, national DPA guidance (CNIL, ICO, AEPD), CMP vendor specifications, and legal counsel for jurisdiction-specific requirements

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
