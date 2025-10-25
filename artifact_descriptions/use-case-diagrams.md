# Name: use-case-diagrams

## Executive Summary

Use Case Diagrams are UML 2.5 visual models that depict system functionality from an external user perspective, showing actors (users, external systems), use cases (system capabilities), system boundary, and relationships (associations, includes, extends, generalizations). Following IEEE 29148 and UML standards, these diagrams are created using tools like Enterprise Architect, Lucidchart, Draw.io, PlantUML, or Visual Paradigm to provide high-level functional scope visualization that supports requirements elicitation, stakeholder communication, and system boundary definition.

These standardized diagrams complement textual requirements by visualizing who interacts with the system (actors), what the system does (use cases), relationships between use cases, and the system boundary separating internal functionality from external interactions. Use case diagrams serve as essential communication artifacts between business stakeholders, business analysts, requirements engineers, system architects, and development teams, providing a shared visual language for discussing system scope and user interactions.

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

This artifact serves as a visual representation of system functionality showing actors, use cases, system boundary, and relationships using standardized UML 2.5 notation. It supports requirements elicitation by providing a high-level view of what the system does, who uses it, and how use cases relate to each other, facilitating stakeholder communication and scope validation.

### Scope

**In Scope**:
- Actors (primary users, secondary users, external systems, time triggers)
- Use cases representing system capabilities and user goals
- System boundary showing internal vs. external scope
- Actor-to-use case associations (which actors interact with which use cases)
- Use case relationships: Include (required sub-functionality), Extend (optional variations), Generalization (inheritance)
- Actor generalizations (role hierarchies)
- UML 2.5 standard notation and semantics
- Context diagrams showing system in broader environment
- Package diagrams for organizing large use case models

**Out of Scope**:
- Detailed use case specifications with flows (covered in Use Case Models)
- Implementation details and design decisions
- User interface designs and wireframes
- Detailed business process flows (use BPMN for processes)
- Sequence diagrams showing interaction timing
- Data models and entity relationships

### Target Audience

**Primary Audience**:
- Business Analysts who create and maintain use case diagrams
- Requirements Engineers who validate functional scope coverage
- Product Managers who review and approve system scope
- System Architects who understand functional requirements visually
- UX Designers who understand user interactions with system

**Secondary Audience**:
- Business stakeholders who validate system capabilities
- Development Teams who understand high-level functional scope
- QA Engineers who identify test scenarios from use cases
- Project Managers who estimate effort from use case complexity
- Technical Writers who document user-facing functionality

## Document Information

**Format**: Multiple

**File Pattern**: `*.use-case-diagrams.*`

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

**UML 2.5 Compliance**: Follow standard UML notation (stick figures for actors, ovals for use cases, rectangles for system boundary)
**User-Goal Orientation**: Name use cases as user goals (verb-noun format like "Process Payment" not "Payment Processing")
**Appropriate Granularity**: Keep diagrams at appropriate abstraction level; avoid overly detailed or overly abstract use cases
**Actor Identification**: Identify all primary actors (initiate use cases), secondary actors (support), and external systems
**System Boundary**: Clearly delineate system boundary; place use cases inside, actors outside the boundary
**Limited Include/Extend**: Use <<include>> for required common functionality, <<extend>> for optional variations; avoid overuse
**Actor Generalization**: Use generalization to show role hierarchies (e.g., Admin generalizes from User)
**One Primary Actor**: Each use case should have one primary actor who initiates and benefits from the use case
**Readable Layout**: Organize diagrams for readability; group related use cases, minimize crossing lines
**Consistent Naming**: Use consistent naming conventions across diagrams; maintain glossary of terms
**Package Organization**: For large systems, organize use cases into packages by subsystem or functional area
**Complementary Documentation**: Link use case diagrams to detailed use case specifications
**Stakeholder Review**: Review diagrams with stakeholders to validate scope and actor identification
**Tool-Based Creation**: Use modeling tools (Enterprise Architect, Lucidchart, PlantUML) for maintainability
**Version Control**: Store diagram source files (not just images) in version control
**Traceability**: Link use cases to functional requirements and user stories in RTM
**Avoid Design**: Keep diagrams at requirements level; avoid including design or implementation details

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

**UML Standards and Specifications**:
- UML 2.5.1: Unified Modeling Language specification by OMG (use case diagram notation)
- ISO/IEC 19505-2: UML Superstructure specification
- OMG UML: Object Management Group UML standards and best practices
- Use Case 2.0: Ivar Jacobson's modern use case practices (use case slices, stories)

**Use Case Methodologies**:
- Alistair Cockburn Use Case Writing: Goal-oriented use case templates and best practices
- Ivar Jacobson Use Cases: Original use case methodology and notation
- ICONIX Process: Use case-driven development methodology
- User-Goal Technique: Focus on user goals rather than system functions
- Essential Use Cases: Technology-free use case specifications

**Modeling Tools**:
- Enterprise Architect: Sparx Systems UML and use case modeling
- Visual Paradigm: UML, BPMN, and use case diagram tool
- Lucidchart: Cloud-based diagramming with UML support
- Draw.io (diagrams.net): Free open-source diagramming tool
- PlantUML: Text-based UML diagram generation
- StarUML: Open-source UML modeling tool
- ArgoUML: Open-source UML modeling tool
- MagicDraw/Cameo: NoMagic UML and SysML modeling
- IBM Rational Software Architect: UML and requirements modeling
- Creately: Online collaborative diagramming
- Miro: Collaborative whiteboarding with UML templates
- Microsoft Visio: General-purpose diagramming with UML stencils

**Requirements Engineering Integration**:
- IEEE 29148: Requirements engineering (use cases as requirements specification technique)
- IREB/CPRE: Use case analysis in requirements engineering curriculum
- BABOK v3: Use case modeling in business analysis practices
- Use Case Points: Effort estimation technique based on use cases

**Related Modeling Techniques**:
- BPMN 2.0: Business Process Model and Notation for detailed process flows
- Activity Diagrams: UML diagrams showing workflow and control flow
- Sequence Diagrams: UML interaction diagrams showing message timing
- Context Diagrams: System context and external entity identification
- User Story Mapping: Agile alternative/complement to use case diagrams
- Event Storming: Collaborative domain modeling technique

**Use Case Testing and Validation**:
- Use Case-Based Testing: Deriving test scenarios from use cases
- Scenario-Based Testing: Testing based on use case scenarios
- Acceptance Testing: Validating use cases with stakeholders
- Use Case Walkthroughs: Reviewing use case diagrams with stakeholders

**Systems Modeling Integration**:
- SysML: Systems Modeling Language (extends UML for systems engineering)
- OOSEM: Object-Oriented Systems Engineering Method (use case-driven)
- Harmony-SE: Systems engineering process with use case analysis
- Use Cases in Model-Based Systems Engineering (MBSE)

**Agile and Lean Integration**:
- User Stories: Agile lightweight alternative to detailed use cases
- Epics and Features: Agile hierarchy mapping to use case packages
- Story Mapping: Jeff Patton's user story mapping (visual use case alternative)
- Use Case Slicing: Breaking use cases into Minimal Marketable Features

**Documentation Standards**:
- Use Case Specifications: Detailed textual descriptions complementing diagrams
- Use Case Templates: Structured formats (brief, casual, fully-dressed)
- Glossary: Common terminology for actors and use cases
- Supplementary Specifications: Non-functional requirements complementing use cases

**Academic and Industry References**:
- "Writing Effective Use Cases" by Alistair Cockburn
- "Use Case Modeling" by Kurt Bittner and Ian Spence
- "Applying UML and Patterns" by Craig Larman
- IEEE Software Engineering Standards Collection

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

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
