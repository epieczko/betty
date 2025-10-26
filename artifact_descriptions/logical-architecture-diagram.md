# Name: logical-architecture-diagram

## Executive Summary

The Logical Architecture Diagram is a critical visual artifact that represents the conceptual structure and organization of a system's key components, their relationships, and logical groupings independent of physical implementation details. This artifact uses industry-standard notations (UML 2.5, ArchiMate 3.1, C4 Model) to communicate the system's logical design to technical and business stakeholders.

As a foundational element of enterprise architecture practice, this diagram bridges business requirements and technical implementation by showing how functional capabilities map to logical components, services, and data flows. It supports architecture governance, design decisions, and impact analysis while maintaining technology independence to enable flexible deployment strategies.

### Strategic Importance

- **Architecture Communication**: Provides technology-neutral view of system structure using TOGAF, Zachman Framework, or C4 Model notations
- **Design Validation**: Enables architecture review boards to validate alignment with patterns (microservices, layered, hexagonal, event-driven)
- **Technology Independence**: Separates logical design from physical infrastructure to support cloud-native, hybrid, and multi-cloud strategies
- **Impact Analysis**: Facilitates assessment of change impacts across logical boundaries and dependencies
- **Standards Compliance**: Demonstrates adherence to enterprise architecture frameworks (TOGAF ADM, ArchiMate) and architecture decision records (ADR)

## Purpose & Scope

### Primary Purpose

This artifact documents the logical architecture of a system using standardized notation (UML 2.5 Component/Package diagrams, ArchiMate, C4 Container/Component diagrams) to show functional decomposition, component responsibilities, service boundaries, and logical data flows. Created using tools like Lucidchart, draw.io/diagrams.net, PlantUML, Mermaid, or Structurizr, it supports architecture decisions, pattern selection, and technical communication.

### Scope

**In Scope**:
- Logical component decomposition and service boundaries using C4 Model levels 2-3 (Container and Component)
- Logical relationships, dependencies, and integration patterns (REST, GraphQL, messaging, events)
- Application of architectural patterns: microservices, layered architecture, hexagonal/ports-and-adapters, CQRS, event sourcing, service mesh
- Logical data flows and information exchange using ArchiMate notation or UML sequence diagrams
- Technology stack categories (API Gateway, Service Bus, Cache Layer) without vendor-specific details
- Diagrams-as-code implementations using PlantUML, Mermaid, Structurizr DSL for version control

**Out of Scope**:
- Physical infrastructure details (covered in Physical Architecture Diagram)
- Network topology, IP addressing, firewall rules (see Network Architecture Diagram)
- Detailed security controls and encryption (see Security Architecture Diagram)
- Database schema and detailed data models (see Data Architecture artifacts)
- Deployment pipelines and CI/CD processes (see Deployment Architecture)

### Target Audience

**Primary Audience**:
- Solution Architects and Enterprise Architects using TOGAF ADM or Zachman Framework for design governance
- Technical Leads selecting architectural patterns and evaluating technology approaches
- Development teams understanding component boundaries, interfaces, and integration requirements

**Secondary Audience**:
- Architecture Review Boards (ARB) validating design decisions against enterprise standards and ADRs
- Platform Engineers planning infrastructure requirements based on logical component needs
- Product Managers and Business Analysts understanding system capabilities and functional organization

## Document Information

**Format**: Multiple

**File Pattern**: `*.logical-architecture-diagram.*`

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

**Architecture Frameworks & Methodologies**:
- TOGAF 10 ADM (Architecture Development Method) - Phase B: Business Architecture, Phase C: Information Systems Architecture
- Zachman Framework - Rows 2-3 (Business Model, System Model) for logical perspective
- C4 Model (Context, Container, Component, Code) - Levels 2-3 for logical architecture visualization
- ArchiMate 3.1 - Application Layer modeling for logical components and services
- arc42 Documentation Template - Section 5: Building Block View for logical decomposition
- AWS Well-Architected Framework - Architectural principles and best practices
- Microsoft Azure Architecture Framework - Design principles and reference architectures
- Google Cloud Architecture Framework - System design guidance
- ISO/IEC/IEEE 42010 (Architecture Description) - Standard for architecture documentation

**Diagramming Notations & Standards**:
- UML 2.5 (Unified Modeling Language) - Component Diagrams, Package Diagrams, Deployment Diagrams
- ArchiMate 3.1 Notation - Visual language for enterprise architecture modeling
- C4 Model Notation - Context, Container, Component diagram standards
- BPMN 2.0 (Business Process Model and Notation) - For process-centric logical views
- SysML (Systems Modeling Language) - For systems engineering perspectives

**Diagramming Tools & Platforms**:
- Lucidchart - Cloud-based diagramming with UML, ArchiMate, C4 templates
- draw.io / diagrams.net - Open-source diagramming tool with extensive shape libraries
- PlantUML - Text-based UML diagram generation with version control integration
- Mermaid - Markdown-based diagram creation for diagrams-as-code
- Structurizr - C4 Model tooling with DSL for architecture as code
- Enterprise Architect (Sparx Systems) - Full-featured UML and ArchiMate modeling
- Archi - Open-source ArchiMate modeling tool
- Visual Paradigm - UML, BPMN, ArchiMate modeling platform

**Architectural Patterns & Styles**:
- Microservices Architecture - Distributed services with bounded contexts (Domain-Driven Design)
- Layered Architecture (N-Tier) - Presentation, Business Logic, Data Access layers
- Hexagonal Architecture (Ports and Adapters) - Alistair Cockburn's pattern for testability
- Event-Driven Architecture - Event sourcing, CQRS (Command Query Responsibility Segregation)
- Service-Oriented Architecture (SOA) - Enterprise service bus, service composition
- Clean Architecture (Robert C. Martin) - Dependency inversion and separation of concerns
- Serverless Architecture - Function-as-a-Service (FaaS) and Backend-as-a-Service (BaaS)
- Reactive Architecture - Responsive, resilient, elastic, message-driven systems

**Documentation & Governance**:
- Architecture Decision Records (ADR) - Lightweight architecture documentation format (Michael Nygard)
- Request for Comments (RFC) - Collaborative decision-making documentation
- Diagrams-as-Code - Version-controlled, text-based diagram definitions (PlantUML, Mermaid, Structurizr DSL)
- Living Documentation - Continuous documentation aligned with code (Cyrille Martraire)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application, notation standards, and tool selection for your specific context

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
