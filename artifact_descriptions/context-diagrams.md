# Name: context-diagrams

## Executive Summary

The Context Diagram (C4 Model Level 1) provides the highest-level architectural view showing how the system fits within its environment, illustrating external actors, dependencies, and integration points. This diagram is the entry point for the C4 Model hierarchical architecture visualization (Context → Containers → Components → Code) and is designed for non-technical stakeholders including business leaders, product owners, and executive management.

The context diagram identifies the system boundary, shows all external users and personas interacting with the system, depicts external systems and services the system integrates with (SaaS platforms, legacy systems, third-party APIs), and illustrates data flows and communication protocols. It uses simple box-and-line notation without technical implementation details, making it accessible to business stakeholders while providing sufficient context for understanding system scope, external dependencies, integration complexity, and data privacy boundaries. Tools like Structurizr, PlantUML, draw.io, or Mermaid are used to create these diagrams following C4 Model notation standards.

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

This artifact communicates system scope and external dependencies to stakeholders, enabling understanding of what the system does, who uses it, and what it integrates with. It supports scope definition, dependency identification, privacy impact assessment, and executive communication about system purpose and boundaries.

### Scope

**In Scope**:
- System boundary: clear demarcation of what is inside vs. outside the system being documented
- System description: concise statement of system purpose, key capabilities, and business value
- External actors: human users, personas, roles that interact with the system
- User types: customers, administrators, operators, support staff, partners with different access levels
- External systems: third-party SaaS platforms, legacy systems, partner systems, cloud services
- Integration dependencies: APIs consumed, data feeds, authentication providers, payment gateways
- Data flows: direction of communication (inbound/outbound), data exchanged, protocols used (HTTPS, SFTP, messaging)
- Communication methods: synchronous (REST, GraphQL, gRPC), asynchronous (messaging, events, webhooks)
- External databases: external data sources, data warehouses, third-party analytics platforms
- Technology agnostic view: no implementation details, programming languages, or infrastructure components
- Multiple viewpoints: separate diagrams for different personas if needed (customer view vs. administrator view)
- Security boundaries: trust boundaries between internal system and external actors/systems

**Out of Scope**:
- Internal system structure (containers, components) - covered in C4 Level 2 Container Diagram
- Implementation details (databases, services, frameworks) - covered in C4 Level 2 and 3
- Code structure and classes - covered in C4 Level 4 Code Diagram
- Infrastructure topology (servers, networks) - covered in deployment diagram
- Detailed API specifications - referenced from API documentation
- Data models and schemas - captured in data architecture artifacts
- Sequence of interactions - shown in sequence diagrams
- Business processes - documented in business process models

### Target Audience

**Primary Audience**:
- Executive Leadership (CTO, CIO, CEO): understand system scope, external dependencies, strategic alignment
- Product Owners: define system scope, prioritize features, understand user types
- Business Stakeholders: understand what system does, who uses it, business value delivered
- Non-Technical Stakeholders: accessible high-level view without technical jargon

**Secondary Audience**:
- Enterprise Architects: understand how system fits in enterprise landscape
- Solution Architects: identify integration points and external dependencies
- Technical Architects: high-level context before drilling into technical details
- Architecture Review Board (ARB) Members: evaluate scope and external dependencies

## Document Information

**Format**: Multiple

**File Pattern**: `*.context-diagrams.*`

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

**Single System Focus**: Create one context diagram per system; avoid enterprise-wide diagrams showing all systems (use ArchiMate for enterprise landscape)
**Clear System Boundary**: Use distinct visual styling (bold box, shading) to clearly separate system from external entities
**Technology Agnostic**: Avoid technical details like programming languages, databases, frameworks; keep at business capability level
**Named Actors**: Use specific actor names (not generic "User"); distinguish personas (Customer, Administrator, Support Agent) with different access
**Directional Arrows**: Show direction of data flow and initiation (who calls whom); bidirectional when both systems initiate communication
**Labeled Relationships**: Add concise labels to arrows describing purpose ("sends orders", "authenticates users", "retrieves customer data")
**Protocol Notation**: Optionally include communication protocol on arrows (HTTPS, SFTP, Kafka) if helpful for understanding integration complexity
**External System Grouping**: Group related external systems (e.g., all AWS services) to reduce visual clutter while maintaining clarity
**Legend Inclusion**: Include legend explaining box types (person, external system, internal system), arrow types, colors used
**Consistent Notation**: Follow C4 Model standard notation - rectangles for systems, stick figures or circles for people, straight arrows for relationships
**Appropriate Abstraction**: Show the right level of detail for audience - executives need less detail than architects
**Color Coding**: Use consistent colors - one color for system, different color for external systems, another for people; maintain contrast for accessibility
**Annotations**: Add brief descriptions to boxes explaining purpose (e.g., "Customer-facing e-commerce platform")
**Multiple Views**: Create separate diagrams for different viewpoints if single diagram becomes cluttered (customer view, admin view, integration view)
**Diagrams-as-Code**: Use Structurizr DSL, PlantUML, or Mermaid to version control diagrams alongside code; enable automated rendering
**Regular Updates**: Update context diagram when external dependencies change, new integrations added, actors change
**Stakeholder Validation**: Review with business stakeholders to ensure actor identification is complete and accurate
**Privacy Awareness**: Highlight data flows containing personal information for GDPR/privacy assessment
**Trust Boundaries**: Visually indicate security boundaries where data crosses from trusted to untrusted zones
**Dependency Risk**: Identify critical external dependencies that pose business continuity risk if unavailable
**Integration Complexity**: Use diagram to communicate integration scope for project planning and risk assessment

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

**C4 Model Architecture Diagrams**:
- C4 Model (Simon Brown) - hierarchical software architecture diagrams: Context (Level 1), Containers (Level 2), Components (Level 3), Code (Level 4)
- System Context Diagram - Level 1 showing system, users, external systems
- Container Diagram - Level 2 showing applications, services, data stores
- Component Diagram - Level 3 showing internal components and their relationships
- Code Diagram - Level 4 showing code-level classes and interfaces (rarely used)
- C4 Model Notation - simple boxes and arrows with consistent styling

**Diagram Visualization Tools**:
- Structurizr - diagrams-as-code for C4 Model using DSL, Java, .NET, TypeScript
- PlantUML - text-based C4 Model diagrams using @startuml/@enduml syntax
- Mermaid - markdown-like C4 diagram syntax for documentation
- draw.io (diagrams.net) - visual diagramming with C4 Model template
- Lucidchart - collaborative diagramming with C4 Model shapes
- Archi - ArchiMate tool that can represent context views
- IcePanel - C4 Model diagramming with live collaboration

**System Context Modeling**:
- System Boundary Definition - clear demarcation of inside vs. outside
- External Actors - identifying all users, personas, external systems
- Integration Points - documenting all inbound and outbound integrations
- Data Flow Arrows - showing direction and type of communication
- Abstraction Level - appropriate detail for executive/business audience

**UML Context Diagrams**:
- UML Use Case Diagrams - actors and use cases (alternative to C4 for context)
- UML Component Diagrams - high-level component view with external interfaces
- System Context Notation - boxes for systems, stick figures for actors, arrows for relationships

**Enterprise Architecture**:
- ArchiMate 3.1 Application Collaboration - modeling context and relationships
- TOGAF 9.2 Baseline Architecture (Phase B) - documenting current state context
- TOGAF Architecture Vision (Phase A) - communicating scope to stakeholders
- Zachman Framework Row 1 (Scope/Contextual) - planner's perspective of system scope

**Integration Architecture**:
- Integration Patterns - point-to-point, hub-and-spoke, ESB, API gateway, event mesh
- API Gateway Pattern - single entry point for external access
- Backend for Frontend (BFF) - separate backends for different client types
- External Service Integration - REST APIs, GraphQL, gRPC, SOAP, messaging
- Data Integration Patterns - ETL, CDC (Change Data Capture), real-time streaming

**Security & Privacy**:
- Trust Boundaries - identifying security boundaries between system and external entities
- Data Flow Analysis - understanding what data crosses boundaries for privacy assessment
- Attack Surface - identifying all external interfaces as potential attack vectors
- Zero Trust Architecture - never trust, verify all external interactions
- Privacy Impact Assessment - identifying personal data flows across boundaries

**Communication Protocols**:
- Synchronous Protocols - HTTPS/REST, GraphQL, gRPC, SOAP for request-response
- Asynchronous Protocols - message queues (RabbitMQ, Kafka), webhooks, polling
- File Transfer - SFTP, S3, Azure Blob, Google Cloud Storage for batch data
- Real-Time - WebSockets, Server-Sent Events (SSE) for streaming
- API Standards - OpenAPI 3.0, AsyncAPI, GraphQL schema, gRPC Protobuf

**External Dependencies**:
- Third-Party SaaS - Salesforce, Workday, ServiceNow, Zendesk, Stripe
- Cloud Services - AWS (S3, Lambda, RDS), Azure (Functions, CosmosDB), GCP (BigQuery, Cloud Functions)
- Identity Providers - Auth0, Okta, Azure AD, Google Workspace, on-premise LDAP
- Payment Gateways - Stripe, PayPal, Square, Braintree, Adyen
- Communication Services - Twilio, SendGrid, Mailchimp, Slack, Microsoft Teams
- Analytics Platforms - Google Analytics, Mixpanel, Segment, Amplitude

**Stakeholder Communication**:
- Executive Summaries - one-page system overview with context diagram
- Architecture Decision Records (ADR) - linking decisions to context elements
- System Scope Documentation - what's in vs. out of scope
- Dependency Mapping - identifying critical external dependencies
- Risk Assessment - external dependencies as risk sources

**Modeling Best Practices**:
- Abstraction - hide internal complexity, show only external interfaces
- Clarity - use simple notation understandable by non-technical stakeholders
- Consistency - follow C4 Model notation standards consistently
- Annotations - add descriptions to boxes and arrows explaining purpose
- Legend - include legend explaining symbols, colors, arrow types

**Documentation Standards**:
- Diagrams-as-Code - version control using Structurizr DSL, PlantUML, Mermaid
- Living Documentation - keep diagrams up-to-date as system evolves
- Single Source of Truth - generate diagrams from architecture model
- Accessibility - provide both visual diagrams and text descriptions
- Versioning - track diagram changes alongside code changes

**Quality Frameworks**:
- ISO 25010 - documenting quality attributes at system context level
- SEI Quality Attribute Scenarios - identifying quality requirements from context
- Architectural Significant Requirements (ASR) - requirements affecting external interfaces
- Non-Functional Requirements - performance, security, availability visible at context level

**Reference**: Consult organizational architecture team for C4 Model standards, diagramming tool choices, and context documentation templates

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
