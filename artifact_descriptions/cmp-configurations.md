# Name: cmp-configurations

## Executive Summary

The CMP Configurations artifact documents the technical and operational settings for Consent Management Platforms (CMPs) such as OneTrust, TrustArc, Cookiebot, Osano, and Usercentrics. This artifact ensures regulatory compliance with GDPR, CCPA/CPRA, ePrivacy Directive, and IAB Transparency & Consent Framework (TCF) 2.2 while optimizing for user experience and consent capture rates.

Modern CMPs manage complex consent workflows across web, mobile, and connected TV platforms, handling 50-200+ advertising vendors, 10-12 IAB TCF purposes, and geo-specific privacy regulations. Properly configured CMPs achieve 70-90% consent rates while maintaining GDPR Article 7 compliance (freely given, specific, informed, unambiguous consent) and supporting data subject rights under GDPR Articles 15-22.

CMP configurations directly impact business outcomes: a 10% improvement in consent rates can translate to significant advertising revenue gains, while misconfiguration risks regulatory fines up to 4% of global annual revenue (GDPR) or $7,500 per violation (CCPA). This artifact provides the authoritative reference for CMP administrators, privacy engineers, legal counsel, and compliance teams to deploy privacy-compliant consent mechanisms that balance regulatory requirements with business objectives.

### Strategic Importance

- **Regulatory Compliance**: Ensures GDPR Article 6/7, CCPA Section 1798.100, ePrivacy Directive, and IAB TCF 2.2 compliance across all digital properties
- **Consent Rate Optimization**: Balances privacy compliance with business needs, targeting 70-90% opt-in rates through UX optimization and A/B testing
- **Cross-Platform Consistency**: Maintains uniform consent experience across web, mobile apps (iOS/Android), AMP pages, and connected TV
- **Vendor Management**: Configures and maintains IAB Global Vendor List (GVL) integration for 800+ registered vendors
- **Audit Readiness**: Provides documented evidence of consent mechanisms, banner configurations, and privacy controls for regulatory examinations
- **Risk Mitigation**: Reduces exposure to GDPR fines (up to EUR 20M or 4% revenue), CCPA penalties ($2,500-$7,500 per violation), and class action litigation
- **Data Subject Rights**: Enables GDPR-mandated rights (access, rectification, erasure, portability, objection) with 30-day response SLAs

## Purpose & Scope

### Primary Purpose

This artifact documents the complete configuration specification for Consent Management Platform (CMP) deployments, ensuring privacy-compliant consent collection across all digital touchpoints. It serves as the authoritative reference for CMP technical settings, banner designs, purpose definitions, vendor configurations, geo-targeting rules, and integration parameters. The configuration enables organizations to capture legally valid consent under GDPR Article 7, CCPA opt-out mechanisms, and IAB TCF 2.2 transparency requirements while optimizing user experience to achieve target consent rates.

### Scope

**In Scope**:
- CMP platform configurations for OneTrust, TrustArc, Cookiebot, Osano, Usercentrics, Didomi, Sourcepoint, and Quantcast Choice
- Consent banner design specifications including layout, copy, button styling, and mobile/desktop responsive behavior
- IAB TCF 2.2 Global Vendor List (GVL) integration and vendor purpose mappings (Purposes 1-11, Special Purposes, Features, Special Features)
- Cookie categorization schema: Strictly Necessary, Functional, Analytics/Performance, Advertising/Targeting
- Geo-targeting rules and regulatory jurisdiction detection (GDPR/EEA, CCPA/California, LGPD/Brazil, PIPEDA/Canada, APPI/Japan)
- Consent string generation (IAB TC String v2.0, Google Additional Consent Mode)
- Integration specifications for Google Consent Mode v2, Google Tag Manager, Adobe Experience Platform, Segment
- Privacy preference center UI/UX configurations and self-service consent withdrawal mechanisms
- Consent refresh and re-solicitation logic (annually or upon material policy changes per GDPR Article 7(3))
- A/B testing configurations for consent rate optimization experiments
- Multi-language support for 20-50+ locales with culturally appropriate messaging
- Data subject rights request workflows integrated with CMP (access, deletion, portability under GDPR Articles 15-20)
- Consent audit logging and proof-of-consent record retention (GDPR Article 5(2) accountability principle)
- Mobile SDK configurations for iOS (App Tracking Transparency integration) and Android consent flows
- AMP (Accelerated Mobile Pages) consent configurations using amp-consent component

**Out of Scope**:
- Privacy policy content and legal disclosures (covered in Privacy Policy artifact)
- Data protection impact assessments (DPIAs) and legitimate interest assessments (covered in DPIA artifact)
- Cookie technical implementations and first-party vs third-party cookie strategies (covered in Cookie Policy Inventory)
- Data processing agreements (DPAs) and vendor contract terms (covered in Vendor Management)
- Server-side consent enforcement logic and backend validation (covered in Technical Architecture documentation)

### Target Audience

**Primary Audience**:
- Privacy Officers and Data Protection Officers (DPOs) responsible for GDPR/CCPA compliance strategy
- CMP Administrators configuring OneTrust, TrustArc, Cookiebot platforms
- Privacy Engineers implementing consent mechanisms and integrations
- Web Development Teams integrating CMP SDKs and consent APIs
- Marketing Technology Teams managing tag management and advertising technology stacks

**Secondary Audience**:
- Legal Counsel reviewing consent mechanisms for regulatory compliance
- Compliance Auditors assessing consent collection practices
- Product Managers balancing privacy requirements with user experience
- UX Designers optimizing consent banner conversion rates
- QA Engineers testing consent workflows across platforms and geographies

## Document Information

**Format**: Markdown

**File Pattern**: `*.cmp-configurations.md`

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

**Consent Banner Optimization**: Design banners for minimal friction while maintaining compliance - avoid dark patterns, use clear language, position "Accept" and "Reject" buttons with equal prominence per GDPR Article 7(4)
**A/B Testing for Consent Rates**: Systematically test banner copy, button colors, positioning (bottom vs top), and interaction models (modal vs banner) to optimize for 70-90% consent rates
**Purpose Granularity**: Configure specific, granular purposes rather than bundled consent - allow users to accept analytics while rejecting advertising per GDPR Article 7(2) specificity requirement
**Geo-Targeting Accuracy**: Implement IP geolocation with 99%+ accuracy using MaxMind GeoIP2 or IP2Location to serve jurisdiction-appropriate consent flows (GDPR for EEA, CCPA for California)
**IAB TCF 2.2 Compliance**: Register as CMP with IAB, implement TC String v2.0 correctly, sync with Global Vendor List weekly, validate CMP ID and vendor configurations
**Consent String Validation**: Implement client-side and server-side validation of IAB TC Strings, Google Consent Mode parameters, and custom consent formats to prevent malformed data
**Cookie Categorization Consistency**: Align cookie categories across CMP, privacy policy, and cookie inventory - use industry-standard categories (Strictly Necessary, Functional, Analytics, Advertising)
**Consent Refresh Logic**: Re-prompt users annually or upon material privacy policy changes per GDPR Article 7(3), tracking last consent timestamp and policy version
**Mobile SDK Integration**: Implement native consent flows for iOS (App Tracking Transparency pre-prompt + CMP) and Android, respecting platform-specific privacy requirements
**Google Consent Mode v2**: Configure Consent Mode for ads_data_redaction, analytics_storage, ad_storage, ad_user_data, and ad_personalization with appropriate defaults
**Accessibility Compliance**: Ensure WCAG 2.1 AA compliance for consent banners - keyboard navigation, screen reader support, sufficient color contrast (4.5:1 minimum)
**Consent Audit Logging**: Log all consent events (grant, withdraw, update) with timestamp, user ID, consent string, banner version, and IP address for GDPR Article 5(2) accountability
**Performance Optimization**: Lazy-load CMP SDK (async/defer), minimize banner render time (<200ms), avoid blocking page load, implement consent caching with 13-month expiry
**Multi-Language Support**: Provide translations in all supported locales (20-50+ languages), culturally adapt messaging, use professional translation services for legal accuracy
**Vendor Management**: Maintain current IAB GVL integration, audit vendor list quarterly, disable vendors not in active use, document legitimate interest assessments per vendor
**Testing Coverage**: Test consent flows across browsers (Chrome, Safari, Firefox, Edge), devices (desktop, mobile, tablet), platforms (iOS, Android, web), and geographies (GDPR, CCPA, LGPD)
**Consent Withdrawal UX**: Provide easy-to-find preference center link in footer, support one-click consent withdrawal, apply changes immediately without page reload
**Third-Party Script Blocking**: Implement tag management integration to block non-consented cookies/scripts, validate blocking works via automated tests
**Consent Rate Monitoring**: Track daily consent rates by geography, device type, and banner variation - investigate drops >5% immediately, target 70-90% acceptance rates
**Version Control**: Maintain configuration version history in Git, tag releases, document all banner copy changes, track A/B test results and winning variations
**Incident Response**: Define runbook for consent mechanism failures - fallback to strictest privacy settings, alert privacy team, document incident per GDPR Article 33
**Stakeholder Alignment**: Review CMP configurations quarterly with Legal, Privacy, Marketing, and Engineering teams to ensure alignment on compliance and business objectives
**Documentation**: Maintain detailed configuration documentation including purpose definitions, vendor mappings, geo-rules, and integration specifications for audit readiness

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

**GDPR (General Data Protection Regulation)**:
- GDPR Article 6 - Lawfulness of Processing (consent, legitimate interest, legal obligation)
- GDPR Article 7 - Conditions for Consent (freely given, specific, informed, unambiguous, withdrawable)
- GDPR Article 7(3) - Withdrawal of Consent (as easy as giving consent)
- GDPR Article 7(4) - Conditioning Services on Consent (prohibition of bundled consent)
- GDPR Article 12 - Transparent Information (clear and plain language requirements)
- GDPR Article 13 - Information to be Provided (privacy notice requirements)
- GDPR Article 15 - Right of Access by the Data Subject
- GDPR Article 16 - Right to Rectification
- GDPR Article 17 - Right to Erasure ("Right to be Forgotten")
- GDPR Article 18 - Right to Restriction of Processing
- GDPR Article 20 - Right to Data Portability
- GDPR Article 21 - Right to Object
- GDPR Article 25 - Data Protection by Design and by Default
- GDPR Article 30 - Records of Processing Activities
- GDPR Article 33 - Notification of Personal Data Breach (72-hour requirement)
- GDPR Recital 32 - Consent should be given by clear affirmative action

**CCPA/CPRA (California Privacy Rights)**:
- CCPA Section 1798.100 - Consumer Right to Know
- CCPA Section 1798.105 - Consumer Right to Delete
- CCPA Section 1798.120 - Right to Opt-Out of Sale of Personal Information
- CCPA Section 1798.130 - Notice Requirements
- CPRA Section 1798.135 - Right to Limit Use of Sensitive Personal Information
- CPRA Global Privacy Control (GPC) Signal Recognition

**IAB Transparency & Consent Framework (TCF)**:
- IAB TCF v2.2 Specifications
- IAB Global Vendor List (GVL) - 800+ registered vendors
- IAB TC String v2.0 Format
- IAB Purpose Definitions (Purposes 1-11: Store/Access Info, Basic Ads, Personalized Ads, etc.)
- IAB Special Purposes (Security, Debugging, Technical Delivery)
- IAB Features (Matching Data to Offline Sources, Linking Devices, Precise Geolocation)
- IAB Special Features (Precise Geolocation, Device Characteristics for Identification)
- IAB Legitimate Interest Disclosures

**Other Privacy Regulations**:
- ePrivacy Directive 2002/58/EC (Cookie Law) - Article 5(3)
- LGPD (Brazil Lei Geral de Proteção de Dados) - Articles 7-11
- PIPEDA (Canada Personal Information Protection) - Consent Principles
- APPI (Japan Act on Protection of Personal Information) - Consent Requirements
- POPIA (South Africa Protection of Personal Information Act)
- PDPA (Singapore Personal Data Protection Act)
- Privacy Shield successor frameworks (EU-US Data Privacy Framework)

**CMP Platforms & Tools**:
- OneTrust Cookie Consent & Preference Management
- TrustArc Consent Manager
- Cookiebot CMP
- Osano Consent Management Platform
- Usercentrics Consent Management
- Didomi Consent & Preference Management
- Sourcepoint Consent Management Platform (CMP)
- Quantcast Choice CMP

**Privacy Engineering & Standards**:
- ISO/IEC 27701:2019 - Privacy Information Management System (PIMS)
- ISO/IEC 29100:2011 - Privacy Framework
- NIST Privacy Framework v1.0
- Privacy by Design (PbD) - 7 Foundational Principles
- W3C Privacy Interest Group (PING) Standards
- WCAG 2.1 Level AA - Web Content Accessibility Guidelines

**Integration Standards**:
- Google Consent Mode v2 (ads_storage, analytics_storage, ad_user_data, ad_personalization)
- Google Additional Consent Mode (AC String for non-IAB vendors)
- Google Tag Manager Consent Variables
- Apple App Tracking Transparency (ATT) Framework - iOS 14.5+
- Android Advertising ID (AAID) Consent Requirements
- AMP (Accelerated Mobile Pages) amp-consent Component

**Reference**: Consult Privacy Engineering, Legal Counsel, and IAB TCF technical specifications for detailed implementation guidance

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
