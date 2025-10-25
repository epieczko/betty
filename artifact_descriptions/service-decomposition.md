# Name: service-decomposition

## Executive Summary

The Service Decomposition Strategy is an architectural blueprint that defines how monolithic applications or complex systems are decomposed into microservices, documenting bounded contexts, service boundaries, domain models, and integration patterns. This artifact applies Domain-Driven Design (DDD) principles, bounded context mapping, and strategic decomposition patterns (Strangler Fig, Branch by Abstraction) to transform tightly-coupled systems into loosely-coupled, independently deployable services.

As the foundation for microservices architecture and system modernization, this strategy documents the decomposition approach using domain analysis, aggregate identification, context mapping relationships (Customer-Supplier, Conformist, Anti-Corruption Layer), and service extraction patterns. It defines service granularity, API contracts between services, data ownership boundaries (Database per Service pattern), event-driven communication patterns, and migration sequencing for incremental transformation while maintaining business continuity.

### Strategic Importance

- **Domain Alignment**: Aligns service boundaries with business capabilities and domain concepts for organizational clarity
- **Team Autonomy**: Enables independent development, deployment, and scaling by different teams
- **Technology Flexibility**: Allows different services to use optimal technology stacks (polyglot architecture)
- **Scalability**: Enables selective scaling of high-demand services rather than entire monolith
- **Resilience**: Isolates failures to individual services preventing cascading system failures
- **Incremental Modernization**: Provides roadmap for gradual migration reducing big-bang rewrite risks
- **Maintenance Efficiency**: Reduces cognitive load through smaller, focused codebases with clear boundaries

## Purpose & Scope

### Primary Purpose

This strategy defines the systematic approach for decomposing monolithic or complex systems into microservices, establishing service boundaries based on domain analysis, business capabilities, and architectural principles. It solves the challenge of determining "where to cut" by applying Domain-Driven Design bounded contexts, identifying aggregates, analyzing coupling and cohesion, and planning incremental extraction that minimizes risk while delivering continuous value.

### Scope

**In Scope**:
- Domain-Driven Design (DDD) application: Domain model, bounded contexts, ubiquitous language, aggregates, entities, value objects
- Bounded context identification through event storming, domain analysis, and business capability mapping
- Context mapping patterns: Customer-Supplier, Conformist, Anti-Corruption Layer, Shared Kernel, Partnership, Published Language
- Service boundary definition: what belongs in each service, what stays outside
- Aggregate identification and transaction boundary mapping
- Data ownership and Database per Service pattern implementation
- Service extraction patterns: Strangler Fig, Branch by Abstraction, Parallel Run
- API contract design for inter-service communication (REST, GraphQL, gRPC, events)
- Event-driven communication patterns: Domain Events, Event Sourcing, Saga orchestration
- Service granularity analysis: right-sizing services (not too large, not too small)
- Shared capabilities handling: Shared Kernel vs. separate services
- Cross-cutting concerns: authentication, authorization, logging, monitoring
- Migration sequencing: which services to extract first, dependencies, risk mitigation
- Team topology alignment: Conway's Law, team ownership, bounded contexts per team

**Out of Scope**:
- Detailed implementation code (covered in service repositories)
- Infrastructure deployment architecture (covered in platform architecture)
- Detailed API specifications (covered in Interface Control Documents)
- Specific technology selection (covered in technology radar)
- Operational procedures (covered in runbooks)

### Target Audience

**Primary Audience**:
- Integration Architects: Design service boundaries and integration patterns
- Domain Architects: Apply DDD principles and identify bounded contexts
- Application Architects: Plan system decomposition and modernization strategy
- Technical Leads: Implement service extraction and refactoring

**Secondary Audience**:
- Backend Engineers: Understand service boundaries and develop within contexts
- Product Managers: Align services with business capabilities and value streams
- Engineering Managers: Plan team structure and ownership model
- Platform Engineers: Prepare infrastructure for microservices deployment
- CTO/Technical Directors: Approve decomposition strategy and investment

## Document Information

**Format**: Markdown

**File Pattern**: `*.service-decomposition.md`

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

**Start with Domain Analysis**: Conduct Event Storming or Domain Storytelling workshops with domain experts before technical decomposition
**Bounded Context First**: Identify bounded contexts based on domain language and business capabilities, not technical concerns
**Transaction Boundaries**: Keep aggregates that must be transactionally consistent within same service
**Database per Service**: Enforce data ownership - each service owns its data, no direct database sharing
**Strangler Fig Migration**: Incrementally extract services from monolith rather than big-bang rewrite
**Start Small**: Begin with lowest-risk, highest-value service extraction as proof of concept
**Event-First Integration**: Prefer event-driven communication over synchronous calls to reduce coupling
**Anti-Corruption Layer**: Use ACL pattern when integrating with legacy systems or external services
**Team Ownership**: Align one bounded context per team following Conway's Law
**Ubiquitous Language**: Establish and maintain consistent domain terminology within each bounded context
**Measure Coupling**: Use metrics (efferent/afferent coupling, instability) to validate service boundaries
**Right-Size Services**: Avoid nano-services and mini-monoliths - align with business capabilities
**Shared Kernel Carefully**: Minimize shared code/data; when necessary, treat shared kernel as versioned dependency
**Migration Sequencing**: Extract services in order: least coupled → most valuable → highest risk
**Dual-Write Strategy**: During migration, write to both old and new systems before cutover
**API-First Contracts**: Define service APIs before implementation using OpenAPI/gRPC schemas
**Idempotency by Design**: Ensure operations can be safely retried across service boundaries
**Saga Orchestration**: Use Saga pattern for distributed transactions spanning multiple services
**Context Map Documentation**: Document all context relationships (Customer-Supplier, Conformist, ACL, etc.)
**Continuous Refactoring**: Service boundaries are not set in stone - refine based on operational learnings

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
- Domain-Driven Design (Eric Evans) - foundational DDD concepts
- Implementing Domain-Driven Design (Vaughn Vernon) - practical DDD application
- Domain-Driven Design Distilled (Vaughn Vernon) - concise DDD overview
- Bounded Context pattern and context mapping
- Ubiquitous Language within bounded contexts
- Aggregates, Entities, and Value Objects
- Domain Events and Event Storming
- Context Map patterns (Customer-Supplier, Conformist, ACL, Shared Kernel, Partnership)
- Strategic DDD (context mapping) vs. Tactical DDD (implementation patterns)

**Service Decomposition Patterns**:
- Strangler Fig pattern (Martin Fowler) - incremental replacement
- Branch by Abstraction - parallel implementation during migration
- Database per Service pattern
- Decompose by Business Capability
- Decompose by Subdomain (DDD bounded contexts)
- Self-contained Service pattern
- Service per Team pattern
- Saga pattern for distributed transactions
- API Composition pattern
- Anti-Corruption Layer pattern

**Microservices Architecture**:
- Building Microservices (Sam Newman) - comprehensive microservices guide
- Microservices Patterns (Chris Richardson) - pattern catalog
- Monolith to Microservices (Sam Newman) - migration strategies
- Team Topologies (Matthew Skelton, Manuel Pais) - team structures
- The Twelve-Factor App - microservices principles
- Database per Service pattern
- API Gateway pattern
- Event-Driven Architecture
- CQRS and Event Sourcing

**Service Boundary Identification**:
- Event Storming (Alberto Brandolini) - collaborative domain exploration
- Domain Storytelling - visual collaborative modeling
- Business Capability Modeling
- Value Stream Mapping
- Context Canvas (DDD Crew) - bounded context documentation
- Wardley Mapping for service dependencies
- C4 Model for architecture visualization
- Bounded Context Canvas

**Conway's Law & Team Topology**:
- Conway's Law (Melvin Conway) - organizational impact on architecture
- Team Topologies (Skelton & Pais) - team interaction patterns
- Inverse Conway Maneuver - designing teams for desired architecture
- Stream-aligned teams
- Enabling teams and platform teams
- Bounded contexts aligned with team boundaries

**Data Management Patterns**:
- Database per Service pattern
- Shared Database anti-pattern
- Saga pattern (orchestration vs. choreography)
- Event Sourcing pattern
- CQRS (Command Query Responsibility Segregation)
- Outbox pattern for reliable event publishing
- Change Data Capture (CDC) with Debezium
- API Composition for queries across services
- Materialized View pattern

**Migration & Modernization Strategies**:
- Strangler Fig Application (Martin Fowler)
- Branch by Abstraction (Paul Hammant)
- Parallel Run pattern
- Blue-Green Deployment for service migration
- Feature Toggles for gradual rollout
- Anti-Corruption Layer for legacy integration
- Legacy to Microservices migration patterns
- Incremental refactoring strategies

**Service Granularity Guidelines**:
- Single Responsibility Principle (SRP) for services
- High Cohesion, Low Coupling principles
- Goldilocks Principle (not too large, not too small)
- Service granularity trade-offs (nano-services vs. mini-monoliths)
- Business capability alignment
- Transaction boundary analysis
- Aggregate size considerations

**Integration Patterns**:
- Synchronous communication (REST, GraphQL, gRPC)
- Asynchronous messaging (Kafka, RabbitMQ, AWS SNS/SQS)
- Event-Driven Architecture patterns
- Request-Response vs. Publish-Subscribe
- Circuit Breaker for inter-service calls
- Service Mesh (Istio, Linkerd, Consul Connect)
- API Gateway patterns (Kong, Apigee, AWS API Gateway)

**DDD Tools & Techniques**:
- Event Storming workshops
- Domain Storytelling
- Context Mapping exercises
- Bounded Context Canvas
- C4 diagrams (Context, Container, Component, Code)
- Impact Mapping
- User Story Mapping aligned with bounded contexts
- Aggregate design workshops

**Analysis Frameworks**:
- Business Capability Modeling
- Value Stream Mapping
- Domain analysis and modeling
- Dependency analysis (coupling, cohesion metrics)
- Seam identification in legacy code
- Bulkhead analysis for failure isolation
- Transaction boundary identification
- Data flow analysis

**Organizational Patterns**:
- Inverse Conway Maneuver
- Team Topologies patterns
- Platform as a Product
- You Build It You Run It (DevOps culture)
- Two-Pizza Team sizing
- Feature Teams vs. Component Teams
- Ownership and accountability models

**Technology Enablers**:
- API Gateway platforms (Kong, Apigee, AWS API Gateway, Azure APIM)
- Service Mesh (Istio, Linkerd, Consul)
- Event streaming (Apache Kafka, AWS Kinesis, Azure Event Hubs)
- Service discovery (Consul, Eureka, etcd)
- Distributed tracing (Jaeger, Zipkin, AWS X-Ray)
- Containerization (Docker, Kubernetes)

**Industry Best Practices**:
- AWS Well-Architected Framework (microservices lens)
- Azure Architecture Center (microservices guidance)
- Google Cloud Architecture Framework
- Netflix microservices patterns
- Amazon two-pizza teams
- Spotify squad model
- Martin Fowler's microservices resource guide

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
