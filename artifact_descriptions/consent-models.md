# Name: consent-models

## Executive Summary

The Consent Models artifact defines the legal and technical frameworks for capturing, storing, and managing user consent across digital properties. This specification documents consent acquisition methods (opt-in vs opt-out), lawful bases for processing under GDPR Article 6, consent string formats (IAB TCF 2.2, custom schemas), and consent lifecycle management (grant, refresh, withdrawal, expiry).

Organizations operating under GDPR must implement consent models that satisfy Article 7 requirements: freely given, specific, informed, unambiguous, and as easy to withdraw as to give. CCPA/CPRA requires opt-out mechanisms for data sales and sharing, while sector-specific regulations (COPPA for children under 13, HIPAA for health data, GLBA for financial data) impose additional consent requirements. Modern consent models support granular purpose-based consent (analytics vs advertising vs personalization), cross-device consent synchronization, and integration with 50-200+ advertising technology vendors through IAB TCF.

This artifact provides the authoritative reference for Privacy Officers, DPOs, Privacy Engineers, and Legal Counsel to design consent models that balance regulatory compliance, user experience, and business requirements. Properly designed consent models reduce regulatory risk (GDPR fines up to EUR 20M or 4% revenue), enable data-driven business operations, and build user trust through transparent privacy practices.

### Strategic Importance

- **Regulatory Compliance**: Ensures GDPR Article 6/7, CCPA/CPRA, ePrivacy Directive, COPPA, and sector-specific consent requirements are met
- **Legal Defensibility**: Documents lawful bases for processing, consent mechanisms, and data subject rights enablement for regulatory audits
- **Cross-Jurisdictional Operations**: Supports multi-region deployments with jurisdiction-specific consent models (GDPR/EEA, CCPA/California, LGPD/Brazil, PIPEDA/Canada)
- **Consent Lifecycle Management**: Defines processes for consent grant, refresh (annually per GDPR 7(3)), withdrawal, and expiry handling
- **Business Enablement**: Balances privacy requirements with business needs, optimizing for 70-90% consent rates while maintaining compliance
- **Vendor Ecosystem Integration**: Enables IAB TCF 2.2 integration with 800+ registered vendors, supporting programmatic advertising and martech ecosystems
- **User Trust & Transparency**: Implements Privacy by Design principles, providing clear choices and honoring user privacy preferences

## Purpose & Scope

### Primary Purpose

This artifact defines the complete consent model architecture, specifying how consent is legally obtained, technically captured, persistently stored, and operationally managed throughout its lifecycle. It establishes the framework for distinguishing between consent models (opt-in, opt-out, legitimate interest), purpose taxonomies, consent string schemas, cross-device synchronization, and integration with consent management platforms (OneTrust, TrustArc, Cookiebot). The consent model ensures organizations can demonstrate GDPR Article 5(2) accountability while enabling data-driven business operations.

### Scope

**In Scope**:
- Consent acquisition models: explicit opt-in (GDPR), implied opt-in, opt-out (CCPA), legitimate interest assessments
- GDPR Article 6 lawful bases: consent, contract, legal obligation, vital interests, public task, legitimate interests
- Purpose taxonomy and granularity: analytics, advertising, personalization, functional, strictly necessary
- IAB TCF 2.2 consent model: purposes 1-11, special purposes, features, special features, legitimate interest framework
- Consent string formats: IAB TC String v2.0, Google Additional Consent Mode, custom JSON schemas
- Consent lifecycle states: pending, granted, denied, withdrawn, expired, refreshed
- Consent persistence: first-party cookies (13-month max), local storage, server-side consent databases
- Cross-device consent synchronization: authenticated user consent graphs, device fingerprinting, probabilistic matching
- Consent withdrawal mechanisms: preference centers, email unsubscribe, "Do Not Sell" links (CCPA), Global Privacy Control (GPC)
- Consent refresh logic: annual re-solicitation (GDPR 7(3)), material policy change triggers, consent expiry (13 months)
- Minor consent handling: COPPA age verification (under 13), parental consent mechanisms, age-appropriate consent UX
- Sector-specific consent: HIPAA authorization for health data, GLBA consent for financial data sharing, FERPA consent for education records

**Out of Scope**:
- CMP platform configurations and technical integrations (covered in CMP Configurations artifact)
- Privacy policy legal language and disclosures (covered in Privacy Policy artifact)
- Cookie technical specifications and classifications (covered in Cookie Policy Inventory)
- Data subject access request (DSAR) procedures (covered in DSAR Procedures artifact)
- Data retention policies and deletion procedures (covered in Data Retention Schedule)

### Target Audience

**Primary Audience**:
- Data Protection Officers (DPOs) and Privacy Officers designing consent strategies
- Privacy Engineers implementing consent capture and enforcement mechanisms
- Legal Counsel assessing consent model compliance with GDPR, CCPA, and sector regulations
- Product Managers balancing privacy requirements with user experience and business goals
- CMP Administrators configuring consent workflows in OneTrust, TrustArc, Cookiebot platforms

**Secondary Audience**:
- Compliance Auditors evaluating consent mechanisms for regulatory adherence
- Information Security teams ensuring consent data protection and audit logging
- Marketing Technology teams integrating consent signals with advertising and analytics platforms
- UX Designers creating intuitive consent interfaces and preference centers
- Engineering teams implementing server-side consent validation and enforcement

## Document Information

**Format**: Markdown

**File Pattern**: `*.consent-models.md`

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

### Specification Overview

**Specification Purpose**:
- `specificationGoal`: What this specification is defining
- `userStories`: User needs being addressed
- `requirements`: High-level requirements this spec satisfies
- `designPrinciples`: Guiding principles for this specification
- `constraints`: Technical, business, or regulatory constraints

### Technical Specification

**System Components**:
- `componentName`: Name of each system component
- `componentType`: Service | Library | Integration | Data Store | UI Component
- `purpose`: Why this component exists
- `responsibilities`: What this component is responsible for
- `interfaces`: How other components interact with it
- `dependencies`: What this component depends on
- `dataModel`: Data structures used or managed
- `apiEndpoints`: API endpoints exposed (if applicable)

**Functional Requirements**:
- `requirementId`: Unique identifier (e.g., FR-001)
- `requirement`: Detailed requirement statement
- `acceptance Criteria`: How requirement is verified
- `priority`: Must Have | Should Have | Could Have | Won't Have
- `complexity`: Estimation of implementation complexity
- `risks`: Risks associated with this requirement

**Non-Functional Requirements**:
- `performance`: Response time, throughput, capacity targets
- `scalability`: How system scales with load or data volume
- `availability`: Uptime requirements and SLAs
- `reliability`: Error rates, MTBF, MTTR targets
- `security`: Authentication, authorization, encryption requirements
- `compliance`: Regulatory or policy requirements
- `usability`: User experience and accessibility requirements
- `maintainability`: Code quality, documentation, testing standards
- `portability`: Platform independence or migration requirements

### Design Details

**Architecture**:
- `architecturePattern`: Microservices | Monolith | Serverless | Event-Driven
- `componentDiagram`: Visual representation of components and relationships
- `dataFlow`: How data moves through the system
- `integrationPoints`: External system integrations
- `deploymentModel`: How components are deployed and distributed

**Data Model**:
- `entities`: Core data entities
- `relationships`: How entities relate to each other
- `constraints`: Data validation and business rules
- `indexes`: Performance optimization through indexing
- `archival`: Data retention and archival strategy

**Security Design**:
- `authenticationMechanism`: How users/services authenticate
- `authorizationModel`: RBAC | ABAC | ACL approach
- `dataProtection`: Encryption at rest and in transit
- `auditLogging`: What is logged for security audit
- `threatModel`: Key threats and mitigations

### Implementation Guidance

**Development Standards**:
- `codingStandards`: Language-specific coding standards to follow
- `testingRequirements`: Unit test coverage, integration tests required
- `documentationRequirements`: Code comments, API docs, README
- `versionControl`: Branching strategy and commit conventions
- `codeReview`: Review process and criteria

**Quality Gates**:
- `buildRequirements`: Must compile without errors/warnings
- `testRequirements`: All tests must pass, minimum coverage %
- `securityRequirements`: No high/critical vulnerabilities
- `performanceRequirements`: Must meet performance SLAs
- `accessibilityRequirements`: WCAG 2.1 AA compliance (if applicable)


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

**GDPR Consent Requirements**: GDPR Article 4(11) Definition of Consent, Article 6 Lawful Basis for Processing, Article 7 Conditions for Consent, Article 7(3) Withdrawal of Consent, Article 7(4) Conditioning Services on Consent, Article 8 Child Consent (16+ or parental), Recital 32 Affirmative Action, Recital 42 Burden of Proof, Recital 43 Freely Given

**CCPA/CPRA**: CCPA Section 1798.100 Right to Know, Section 1798.105 Right to Delete, Section 1798.120 Right to Opt-Out, Section 1798.135 Do Not Sell My Personal Information, CPRA Sensitive Personal Information Limits, Global Privacy Control (GPC) Signal

**IAB TCF 2.2**: IAB TC String v2.0, Global Vendor List (GVL), Purpose Definitions (1-11), Special Purposes, Features and Special Features, Legitimate Interest Framework, Publisher Restrictions, CMP API Specification

**Sector-Specific Consent**: COPPA Children's Online Privacy Protection Act (under 13), HIPAA Authorization (45 CFR 164.508), GLBA Financial Privacy Rule (16 CFR Part 313), FERPA Education Records (34 CFR Part 99), VPPA Video Privacy (18 USC 2710)

**International Privacy Laws**: ePrivacy Directive 2002/58/EC Article 5(3), LGPD Brazil Articles 7-11, PIPEDA Canada Consent Principles, APPI Japan Consent Requirements, POPIA South Africa, PDPA Singapore, DPA UK

**Privacy Engineering Standards**: ISO/IEC 27701:2019 PIMS, ISO/IEC 29100:2011 Privacy Framework, NIST Privacy Framework, Privacy by Design 7 Principles, W3C Tracking Preference Expression (DNT)

**CMP Platforms**: OneTrust Consent & Preference Management, TrustArc Consent Manager, Cookiebot CMP, Osano Consent Management, Usercentrics, Didomi, Sourcepoint, Quantcast Choice

**Reference**: Consult IAPP (International Association of Privacy Professionals), EDPB Guidelines, and legal counsel for detailed compliance guidance

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
