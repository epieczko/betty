# Name: microcopy-guides

## Executive Summary

Microcopy Guides are the essential reference for interface copy—the small but mighty words that guide users through products: button labels, error messages, empty states, form field instructions, tooltips, success confirmations, and all the tiny text that makes digital experiences usable or frustrating. This artifact applies UX writing principles from Nielsen Norman Group, Content Design London, and Torrey Podmajersky's "Strategic Writing for UX" to solve the problem of inconsistent, unclear, or unhelpful interface language that creates friction, confusion, and support tickets.

Drawing on content design systems, Voice & Tone frameworks (MailChimp, GOV.UK, Material Design Writing), and usability research, these guides provide specific, actionable patterns and examples for every microcopy moment—from how to write an effective CTA button ("Get started" vs. "Start free trial" vs. "Sign up now") to crafting helpful error messages that explain what went wrong and how to fix it. They serve UX Writers, Product Designers, Product Managers, and Engineers who need to make hundreds of small copy decisions that collectively determine whether users succeed or abandon tasks in frustration.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact provides specific, actionable guidance for every interface copy moment, ensuring consistency in voice, clarity in instruction, and empathy in error handling across the entire product experience. It solves the copy inconsistency problem where different designers use different button labels for the same action or engineers write technical error messages that confuse users, supporting real-time decisions during design, development, and QA reviews about what words to use in every UI element.

### Scope

**In Scope**:
- Button and CTA copy patterns (primary, secondary, destructive actions)
- Form field labels, placeholders, helper text, and validation messages
- Error message templates (client-side validation, server errors, system failures)
- Empty state messaging (first-use empty, user-cleared empty, error-state empty, no-results empty)
- Success and confirmation messages
- Loading states and progress indicators
- Tooltips and inline help text
- Onboarding copy and coach marks
- Navigation labels and breadcrumbs
- Modal dialog titles and action buttons
- Settings and preferences labeling
- Permission requests and consent language
- Character limits and truncation patterns
- Tone modulation (formal, friendly, urgent, celebratory)
- Localization considerations and internationalization patterns
- Accessibility requirements for screen readers and assistive tech

**Out of Scope**:
- Long-form content and marketing copy (covered by content strategy)
- Brand messaging and positioning (covered by messaging frameworks)
- Legal disclaimers and terms of service (covered by legal templates)
- Product documentation and help articles (covered by documentation guides)
- Email templates and transactional messaging (covered by email style guides)

### Target Audience

**Primary Audience**:
- UX Writers crafting interface copy
- Product Designers incorporating copy into design mockups
- Frontend Engineers implementing UI text
- Product Managers reviewing design specifications

**Secondary Audience**:
- QA Engineers validating copy consistency during testing
- Localization Teams translating interface strings
- Content Designers establishing content design systems
- Accessibility Specialists ensuring WCAG-compliant copy

## Document Information

**Format**: Markdown

**File Pattern**: `*.microcopy-guides.md`

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

**Front-Load Value**: Start with the key word in button labels, form fields, and instructions; users scan left-to-right, so "Download report" > "Report download"
**Action-Oriented Buttons**: Use verbs for actions ("Save changes" not "Changes"), be specific ("Create account" not "Submit"), describe the outcome ("Start 14-day trial" not "Continue")
**Error Messages: 3 Parts**: (1) What went wrong, (2) Why it happened, (3) How to fix it; "Invalid email" fails; "Email format incorrect. Use format: name@domain.com" succeeds
**Avoid Placeholder Pitfalls**: Don't use placeholder text as labels (accessibility fail); use placeholders only for format examples ("MM/DD/YYYY"), never for required instructions
**Empty States Tell Stories**: Transform "No items" into opportunity—explain why it's empty, what value filling it provides, and offer clear action: "No saved searches yet. Save your favorite searches for quick access."
**Conversational but Concise**: Write like you speak to a friend who's in a hurry; cut "please," "in order to," "you can"; test: would you say this out loud?
**Consistent Terminology**: Pick one term and stick with it—don't alternate between "delete/remove," "save/store," "settings/preferences"; build a terminology glossary
**Tone Modulation**: Adjust tone to moment—onboarding is welcoming, errors are empathetic, confirmations are reassuring, destructive actions are serious
**Avoid Technical Jargon**: Users don't care about "failed to authenticate OAuth token"; they care about "Can't sign in. Check your password and try again."
**Internationalization-First**: Write for translation—avoid idioms, metaphors, cultural references; "hit the ground running" doesn't translate; "start immediately" does
**Character Limit Reality**: Mobile screens are small—button copy should fit on one line at 320px; test real devices, not just desktop simulators
**Context Over Cleverness**: Clever copy loses to clear copy in interfaces; save creativity for marketing; in UI, clarity wins every time
**Accessibility Requirements**: All interactive elements need accessible names for screen readers; button with only icon needs aria-label; images need alt text
**Number Formatting**: Use locale-aware number formats (1,000.00 vs 1.000,00), date formats (MM/DD/YYYY vs DD/MM/YYYY), and currency symbols
**Help Text Hierarchy**: Layer help—label (what), helper text (guidance), tooltip (extra detail), link to docs (deep dive); don't overwhelm with everything upfront
**Positive Framing**: "Enable notifications to stay updated" > "Disable notifications"; lead with benefit, not negation
**Confirmation Bias**: Don't use "OK/Cancel" for destructive actions; use specific actions: "Delete account" / "Keep account" removes ambiguity
**Loading State Copy**: Long loads need reassurance—"Setting up your workspace..." better than spinning circle; if >5 seconds, add progress indicator with specific steps
**Permission Requests**: Explain value before asking for permission—"We'll use your location to show nearby stores" then request; context improves grant rates by 50%+
**Pattern Library Integration**: Build microcopy directly into design system component documentation; copy shouldn't be an afterthought in Figma
**A/B Test Critical Paths**: Test button copy, form labels, error messages in checkout, signup, onboarding; small word changes can shift conversion 10-20%
**Version Control for Strings**: Maintain string library in code repository or CMS; don't hard-code copy in codebase; enables centralized updates and localization
**Real Content in Design**: Never ship "Lorem ipsum" or placeholder copy; incomplete copy in production signals "unfinished product" to users
**Screen Reader Testing**: Test with actual screen readers (VoiceOver, NVDA, JAWS); what sounds obvious visually often makes no sense audibly

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

**UX Writing Foundations**: Strategic Writing for UX (Torrey Podmajersky), Microcopy: The Complete Guide (Kinneret Yifrah), Nicely Said (Nicole Fenton & Kate Kiefer Lee), Writing Is Designing (Michael J. Metts & Andy Welfle)

**Content Design Methods**: Content Design London principles, GOV.UK content design guidance, Content Design by Sarah Winters, Jobs-to-be-Done for UX writing, Content design patterns

**Voice & Tone Frameworks**: MailChimp Voice & Tone guide, Salesforce Lightning Design System voice principles, Material Design writing guidelines, Atlassian Design System writing style, Shopify Polaris content guidelines

**Design System Content**: Microsoft Fluent UI writing guidance, IBM Carbon Design System content, Adobe Spectrum content guidelines, GOV.UK Design System, Ant Design copywriting principles

**UX Research Organizations**: Nielsen Norman Group UX writing research, Baymard Institute checkout copy research, Forrester UX writing standards, UX Writing Hub resources

**Accessibility Standards**: WCAG 2.1/2.2 text alternatives and labels, ARIA labels and descriptions, Section 508 text requirements, W3C accessible names, WebAIM writing for accessibility

**Error Message Patterns**: Error message best practices (NN/g), Error prevention and recovery, Progressive disclosure for errors, Error message tone and empathy guidelines

**Button Copy Standards**: Call-to-action best practices, Button labeling patterns, Action-oriented vs. generic labels, Primary/secondary/tertiary button hierarchy

**Form Design**: Form field label best practices, Placeholder text guidelines (when not to use placeholders), Helper text patterns, Inline validation messaging, Required field indication

**Empty State Design**: Empty state patterns and templates, First-use empty states, User-generated empty states, Error-based empty states, No-search-results patterns

**Internationalization (i18n)**: Unicode guidelines for text, RTL (right-to-left) language considerations, CJK (Chinese-Japanese-Korean) text patterns, String externalization, Pseudo-localization testing

**Localization (L10n)**: Translation-friendly writing, String concatenation avoidance, Cultural considerations in microcopy, Number and date formatting, Gender and formality considerations

**Readability Standards**: Plain language guidelines, Flesch-Kincaid readability, Hemingway Editor principles, Reading level targets (6th-8th grade), Sentence length recommendations

**Conversational UI**: Chatbot and voice interface copy, Conversation design principles, Bot personality and tone, Error recovery in conversational flows, Slack conversational patterns

**Mobile UX Writing**: Thumb-zone considerations, Character limits for mobile, Touch target labeling, Mobile-specific abbreviations, SMS and notification copy patterns

**Notification Design**: Push notification best practices, In-app notification patterns, Email notification subject lines, Notification timing and frequency, Notification action buttons

**Industry Style Guides**: Microsoft Writing Style Guide, Google Developer Documentation Style Guide, Apple Human Interface Guidelines (Writing), Chicago Manual of Style (digital adaptations), AP Stylebook (digital)

**UX Writing Tools**: Acrolinx content governance, Writer.com style enforcement, Grammarly Business, Hemingway Editor, Readable.io, Figma content plugins (Content Buddy, Content Reel)

**Content Design Systems**: Structured content for interfaces, Content component libraries, Copy tokens in design systems, Content pattern libraries, Reusable microcopy snippets

**Research Methods**: Usability testing for copy, A/B testing microcopy variations, Card sorting for navigation labels, Tree testing for IA labels, Comprehension testing for instructions

**Reference**: Consult UX Writers Collective, Content Design London community, Write the Docs, and UX writing communities (UX Writing Hub, Slack communities) for evolving best practices and pattern libraries

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
