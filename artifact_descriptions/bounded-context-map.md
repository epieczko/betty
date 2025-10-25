# Name: bounded-context-map

## Executive Summary

The Bounded Context Map is a strategic design artifact from Domain-Driven Design (DDD) that visualizes the boundaries between different domains, their relationships, and integration patterns. This artifact, rooted in Eric Evans' DDD and refined by Vaughn Vernon's strategic design patterns, defines context boundaries, identifies upstream/downstream relationships, and specifies integration patterns (Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer, Published Language, Open Host Service, Separate Ways).

The context map provides critical input for microservices decomposition, team organization (aligned with Conway's Law), and integration architecture decisions. It identifies autonomous bounded contexts with clear ownership and ubiquitous language, maps context relationships to determine integration complexity, and highlights where anti-corruption layers are needed to protect domain integrity. The artifact integrates with C4 Model container diagrams to show physical system boundaries and with team topologies to align organizational structure with architectural boundaries.

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

This artifact defines strategic domain boundaries and integration patterns for complex systems, enabling microservices decomposition, team organization, and integration architecture design. It supports decisions about service boundaries, API contracts, data ownership, and organizational structure aligned with domain model.

### Scope

**In Scope**:
- Bounded contexts: autonomous domains with clear boundaries, single ubiquitous language, and dedicated team ownership
- Context boundaries: explicit demarcation of what is inside vs. outside each bounded context
- Context relationships: upstream/downstream, customer/supplier, shared kernel, conformist patterns
- Integration patterns: Published Language (APIs), Open Host Service (generic interface), Anti-Corruption Layer (translation)
- Shared Kernel: overlapping models shared between contexts with joint ownership and synchronized changes
- Customer-Supplier: upstream context serves downstream context's needs through negotiated contracts
- Conformist: downstream context accepts upstream's model without negotiation
- Anti-Corruption Layer (ACL): translation layer protecting downstream context from upstream changes
- Published Language: well-defined, documented integration language (OpenAPI, AsyncAPI, Protobuf)
- Open Host Service: generic service interface supporting multiple downstream consumers
- Separate Ways: contexts with no integration relationship, operating independently
- Partnership: two contexts with mutual dependency requiring coordinated changes
- Core domains: high-value, differentiating domains requiring custom development and domain expertise
- Supporting subdomains: necessary but not differentiating, candidates for COTS or low-cost development
- Generic subdomains: solved problems available as standard solutions (payment, auth, email)
- Context ownership: team responsibility for each bounded context (aligning with Team Topologies)
- Ubiquitous language: domain-specific vocabulary consistent within context boundary
- Data ownership: which context owns master data for entities, preventing distributed data ownership issues

**Out of Scope**:
- Internal domain model details (aggregates, entities, value objects) - handled in detailed domain models
- API specifications and contracts - referenced from API documentation
- Database schemas and data models - captured in data architecture artifacts
- Implementation details and code structure - documented in code repositories
- Business processes and workflows - captured in business process models

### Target Audience

**Primary Audience**:
- Enterprise Architects: understand domain boundaries for microservices decomposition and enterprise integration
- Solution Architects: design integration patterns and API contracts between bounded contexts
- Technical Architects: implement anti-corruption layers, adapters, and integration infrastructure
- Architecture Review Board (ARB) Members: evaluate context boundaries and integration approach

**Secondary Audience**:
- Domain Experts: validate context boundaries align with business domain understanding
- Product Owners: understand service boundaries for feature planning and team coordination
- Development Teams: implement within bounded context using ubiquitous language
- Engineering Managers: organize teams aligned with bounded contexts (Team Topologies)

## Document Information

**Format**: Markdown

**File Pattern**: `*.bounded-context-map.md`

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

**Event Storming Workshops**: Use collaborative Event Storming to discover bounded contexts with domain experts, developers, architects; identify domain events, aggregates, context boundaries
**Business Capability Alignment**: Align bounded contexts with business capabilities; avoid technical decomposition (database, UI, API); follow domain boundaries not technical layers
**Ubiquitous Language**: Ensure each bounded context has consistent vocabulary; same term may mean different things in different contexts (e.g., "Customer" in Sales vs. Support)
**Single Team Ownership**: Assign one team per bounded context; avoid shared ownership to maintain autonomy and reduce coordination overhead (Team Topologies stream-aligned teams)
**Right-Size Contexts**: Balance context size - too large loses modularity benefits, too small creates integration complexity; typical microservice 100-1000 lines of domain logic
**Explicit Relationships**: Clearly label all context relationships with specific patterns (Shared Kernel, Customer-Supplier, ACL); avoid ambiguous "depends on" arrows
**Minimize Shared Kernel**: Shared Kernel creates tight coupling requiring synchronized changes; prefer Customer-Supplier or Published Language for loose coupling
**Anti-Corruption Layers**: Implement ACL when integrating with legacy systems or external APIs to protect domain model from foreign concepts
**Published Language for APIs**: Define explicit Published Language using OpenAPI, AsyncAPI, or Protobuf; version APIs to manage evolution
**Core Domain Protection**: Identify core domains (high business value, competitive differentiation); invest in deep domain modeling; protect with anti-corruption layers
**Generic Subdomain COTS**: Use commercial off-the-shelf (COTS) or open-source solutions for generic subdomains (auth, email, payments); avoid custom development
**Context Map Evolution**: Treat context map as living document; update as domain understanding deepens; refactor contexts when boundaries proven wrong
**Upstream-Downstream Clarity**: Explicitly identify upstream (provider) and downstream (consumer) in relationships; upstream changes impact downstream
**Conway's Law Alignment**: Align team boundaries with context boundaries; architecture will mirror communication structure
**Database Per Context**: Each bounded context owns its database; avoid shared databases causing tight coupling and conflicting transaction boundaries
**Asynchronous Integration**: Prefer event-driven asynchronous integration between contexts for loose coupling; synchronous APIs create temporal coupling
**Eventual Consistency**: Accept eventual consistency across bounded contexts; implement saga patterns or choreography for distributed transactions
**Strangler Fig for Legacy**: Wrap legacy monoliths in bubble contexts; gradually extract bounded contexts using Strangler Fig pattern
**Visualization Tools**: Use Context Mapper DSL, C4 Model, or hand-drawn diagrams; store as code (PlantUML, Mermaid) for version control
**Domain Expert Validation**: Review context boundaries with domain experts; ensure contexts match real-world domain concepts and responsibilities
**Integration Complexity**: Minimize number of integration points; consolidate through API gateways or event buses where appropriate

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

**Domain-Driven Design (DDD)**:
- Eric Evans' "Domain-Driven Design" - bounded contexts, ubiquitous language, strategic design patterns
- Vaughn Vernon's "Implementing Domain-Driven Design" - context mapping patterns, practical DDD application
- DDD Strategic Design - core domains, supporting subdomains, generic subdomains classification
- Context Mapping Patterns - Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer, Published Language, Open Host Service, Separate Ways, Partnership, Big Ball of Mud
- Ubiquitous Language - domain-specific vocabulary consistent within bounded context
- Aggregates - consistency boundaries within bounded contexts, transactional boundaries

**Microservices Architecture**:
- Microservices Patterns (Chris Richardson) - service decomposition by business capability and subdomain
- Building Microservices (Sam Newman) - defining service boundaries, distributed systems patterns
- Bounded Context as Service Boundary - one microservice per bounded context (typical pattern)
- API Gateway Pattern - single entry point for client access to multiple bounded contexts
- Service Mesh - infrastructure layer for service-to-service communication (Istio, Linkerd, Consul Connect)
- Database per Service - each bounded context owns its data, no shared databases

**Integration Patterns**:
- Enterprise Integration Patterns (Hohpe & Woolf) - messaging, routing, transformation patterns
- Published Language - well-defined APIs using OpenAPI/Swagger, AsyncAPI, GraphQL, gRPC/Protobuf
- Open Host Service - generic service interface serving multiple downstream contexts
- Anti-Corruption Layer - translator/adapter preventing upstream model from polluting downstream
- Shared Kernel - overlapping model elements with synchronized changes across contexts
- Customer-Supplier - upstream provides services to downstream with negotiated contracts
- Conformist - downstream accepts upstream's model without influence
- Partnership - bidirectional dependency requiring coordinated evolution
- Separate Ways - no integration, independent operation with duplicate functionality if needed

**API Design**:
- OpenAPI 3.0 (Swagger) - RESTful API specification for Published Language
- AsyncAPI - asynchronous/event-driven API specification
- GraphQL - query language for flexible client-driven APIs
- gRPC/Protocol Buffers - high-performance RPC with strong typing
- JSON:API - specification for building APIs in JSON with hypermedia
- HAL (Hypertext Application Language) - hypermedia API standard

**Event-Driven Architecture**:
- Event Sourcing - storing state changes as sequence of events within bounded context
- CQRS (Command Query Responsibility Segregation) - separate read and write models
- Domain Events - events published by bounded context for integration with other contexts
- Event Storming - collaborative workshop for discovering domain events and bounded contexts
- Saga Pattern - distributed transaction coordination across bounded contexts
- Event Streaming - Kafka, Pulsar, Kinesis for asynchronous context integration

**Team Organization**:
- Team Topologies (Skelton & Pais) - stream-aligned teams, enabling teams, complicated subsystem teams, platform teams
- Conway's Law - organizational structure reflects communication structure, align teams with bounded contexts
- Inverse Conway Maneuver - designing team boundaries to achieve desired architecture
- Stream-Aligned Teams - teams organized around flow of work through bounded context
- Cognitive Load - limiting team responsibility to manageable bounded context scope

**Context Mapping Notation**:
- Context Map Visualization - boxes for contexts, arrows for relationships, labels for patterns
- UML Component Diagrams - representing contexts as components with interfaces
- C4 Model Context/Container Diagrams - showing bounded contexts as containers
- ArchiMate Application Collaboration - modeling context relationships
- PlantUML/Mermaid - text-based context map diagrams

**Strategic Design**:
- Core Domain Chart - identifying core, supporting, and generic subdomains
- Domain Vision Statement - articulating the core domain's strategic value
- Context Distillation - identifying and protecting the core domain
- Big Ball of Mud - identifying legacy systems as monolithic contexts requiring anti-corruption layers
- Bubble Context - introducing bounded context as wrapper around legacy system

**Data Management**:
- Database per Service Pattern - each bounded context owns its data
- Shared Database Anti-Pattern - avoiding coupling through database integration
- Data Ownership - master data source identified per entity type
- Eventual Consistency - accepting data consistency delays across contexts
- CQRS - separate read models for cross-context queries
- Data Mesh - domain-oriented decentralized data ownership aligned with bounded contexts

**Service Communication**:
- Synchronous Communication - REST APIs, GraphQL, gRPC for request-response
- Asynchronous Communication - events, messages for loose coupling
- Choreography - distributed coordination through events
- Orchestration - centralized coordination through orchestrator (anti-pattern in DDD)
- Backend for Frontend (BFF) - context-specific APIs for different client types

**Legacy Integration**:
- Strangler Fig Pattern - incrementally replacing legacy monolith with bounded contexts
- Anti-Corruption Layer - protecting new contexts from legacy system models
- Bubble Context - wrapping legacy system in DDD-friendly interface
- Branch by Abstraction - introducing abstraction layer for parallel implementation
- Parallel Run - operating legacy and new context simultaneously during migration

**Tools & Modeling**:
- Context Mapper - DSL and tools for context mapping (contextmapper.org)
- Event Storming - collaborative workshop for discovering contexts and events
- Domain Storytelling - collaborative modeling using pictographs
- C4 Model - hierarchical architecture diagrams including bounded contexts
- ArchiMate - enterprise architecture modeling with application components
- PlantUML/Mermaid - text-based context map diagrams
- Structurizr - architecture as code including context boundaries

**Quality Attributes**:
- Modularity - bounded contexts provide modular decomposition
- Autonomy - contexts operate independently with loose coupling
- Scalability - contexts can scale independently based on load
- Team Autonomy - teams own contexts end-to-end reducing coordination overhead
- Deployability - contexts deployed independently enabling continuous delivery

**Reference**: Consult organizational architecture team for context mapping standards, microservices decomposition guidelines, and integration pattern governance

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
