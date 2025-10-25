# Name: sequence-diagrams

## Executive Summary

Sequence Diagrams are dynamic modeling artifacts that visualize time-ordered interactions between components, services, actors, and systems to accomplish specific use cases or business processes. Using UML 2.5 Sequence Diagram notation, these diagrams show message exchanges, method calls, API requests, event flows, and timing constraints to communicate runtime behavior and interaction patterns.

As essential tools for understanding system dynamics, sequence diagrams support detailed design, API specification, troubleshooting, performance analysis, and distributed system choreography. They document synchronous and asynchronous communication patterns (request-response, publish-subscribe, saga patterns), error handling flows, authentication sequences (OAuth 2.0, SAML), and integration scenarios across microservices, event-driven architectures, and distributed systems.

### Strategic Importance

- **Behavior Documentation**: Captures complex interaction flows using industry-standard UML 2.5 notation for use cases, API workflows, and integration scenarios
- **API Design**: Specifies RESTful API sequences, GraphQL resolvers, gRPC calls, message flows, and event choreography for distributed systems
- **Troubleshooting**: Supports debugging, root cause analysis, and performance optimization by visualizing message flows and timing
- **Testing Guidance**: Provides foundation for integration testing, API testing, contract testing, and end-to-end test scenario development
- **Communication**: Bridges business requirements and technical implementation by showing step-by-step execution flows

## Purpose & Scope

### Primary Purpose

This artifact documents time-ordered interactions using UML 2.5 Sequence Diagrams showing participants (actors, systems, components, services), messages (synchronous calls, asynchronous messages, return values), lifelines, activation boxes, and timing constraints. Created using PlantUML, Mermaid, Lucidchart, draw.io, or Enterprise Architect, it specifies interaction flows for use cases, API operations, integration scenarios, and distributed transactions.

### Scope

**In Scope**:
- Use case scenarios: End-to-end user workflows, business process interactions, system integration flows
- API interaction sequences: RESTful API calls (HTTP GET/POST/PUT/DELETE), GraphQL queries/mutations, gRPC streaming
- Synchronous patterns: Request-response, method invocation, remote procedure calls (RPC)
- Asynchronous patterns: Message queuing (RabbitMQ, AWS SQS, Azure Service Bus), event publishing (Kafka, EventBridge, Pub/Sub)
- Authentication flows: OAuth 2.0 authorization code flow, SAML SSO, OpenID Connect, JWT token validation
- Microservices choreography: Service-to-service communication, saga patterns, distributed transactions, compensation logic
- Event-driven flows: Event sourcing sequences, CQRS command/query separation, event streaming processing
- Error handling: Exception flows, retry logic, circuit breaker activation, fallback mechanisms
- Timing constraints: Response time requirements, timeout specifications, async operation timing
- Diagrams-as-code: PlantUML sequence diagrams, Mermaid sequence diagrams for version control and documentation-as-code

**Out of Scope**:
- Static component structure and dependencies (see Component Diagrams)
- High-level architecture and system context (see Logical Architecture Diagram)
- Detailed class design and object relationships (see Class Diagrams)
- State transitions and lifecycle management (see State Diagrams)
- Business process modeling (see BPMN diagrams)

### Target Audience

**Primary Audience**:
- Software Developers implementing API integrations, service interactions, and distributed workflows
- API Designers specifying RESTful APIs, GraphQL schemas, gRPC services, and message contracts
- Integration Engineers designing system-to-system integration patterns and data exchange flows

**Secondary Audience**:
- QA Engineers developing integration tests, API tests, and end-to-end test scenarios based on interaction flows
- Technical Writers creating API documentation, integration guides, and developer documentation
- Support Engineers troubleshooting production issues, analyzing error scenarios, and understanding system behavior

## Document Information

**Format**: Multiple

**File Pattern**: `*.sequence-diagrams.*`

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

**Diagramming Notations & Standards**:
- UML 2.5 Sequence Diagrams - Lifelines, messages, activation boxes, fragments (alt, opt, loop, par)
- Interaction Overview Diagrams (UML) - High-level overview combining sequence and activity diagrams
- Communication Diagrams (UML) - Alternative to sequence diagrams emphasizing relationships
- Message Sequence Charts (MSC) - ITU-T Z.120 standard for telecommunication protocol specifications
- Timing Diagrams (UML) - Focus on timing constraints and state changes over time

**Diagramming Tools**:
- PlantUML - Text-based sequence diagram generation with comprehensive UML support
- Mermaid - Markdown-based sequence diagrams for documentation-as-code
- Lucidchart - Visual sequence diagram creation with collaboration features
- draw.io / diagrams.net - Open-source sequence diagramming with UML shapes
- Enterprise Architect (Sparx Systems) - Full UML modeling with sequence diagram support
- Visual Paradigm - UML sequence diagrams with code generation
- WebSequenceDiagrams - Online sequence diagram tool with simple syntax
- SequenceDiagram.org - Browser-based sequence diagram editor
- StarUML - Open-source UML tool with sequence diagram support

**Communication Patterns**:
- Enterprise Integration Patterns (Gregor Hohpe) - Messaging patterns, routing, transformation
- Request-Response Pattern - Synchronous communication with immediate response
- Fire-and-Forget Pattern - Asynchronous message without response expectation
- Request-Callback Pattern - Asynchronous request with callback notification
- Publish-Subscribe Pattern - Event broadcasting to multiple subscribers
- Point-to-Point Pattern - Direct message delivery to single consumer

**API Standards & Protocols**:
- OpenAPI Specification (Swagger) - RESTful API documentation with operation sequences
- GraphQL Schema - Query and mutation specifications with resolver chains
- gRPC - Remote procedure call framework with Protocol Buffers
- REST (Representational State Transfer) - HTTP-based architectural style
- SOAP (Simple Object Access Protocol) - XML-based messaging protocol
- WebSockets - Full-duplex communication over single TCP connection
- Server-Sent Events (SSE) - Server push notifications over HTTP

**Message-Oriented Middleware (MOM)**:
- RabbitMQ - AMQP message broker with exchange types (direct, topic, fanout, headers)
- Apache Kafka - Distributed event streaming platform with pub-sub and stream processing
- AWS SQS (Simple Queue Service) - Managed message queuing service
- Azure Service Bus - Enterprise messaging with topics and queues
- Google Cloud Pub/Sub - Global messaging and event ingestion
- Apache ActiveMQ - JMS-compliant message broker
- Redis Pub/Sub - Lightweight message broadcasting

**Distributed System Patterns**:
- Saga Pattern - Long-running distributed transactions with compensation
- Choreography - Event-based coordination without central orchestrator
- Orchestration - Central coordinator directing service interactions
- Circuit Breaker Pattern - Fault tolerance for service failures (Hystrix, Resilience4j)
- Retry Pattern - Automatic retry with exponential backoff
- Bulkhead Pattern - Resource isolation for fault containment
- Two-Phase Commit (2PC) - Distributed transaction protocol
- Event Sourcing - State changes stored as sequence of events

**Authentication & Authorization Flows**:
- OAuth 2.0 - Authorization framework with flows (authorization code, client credentials, implicit, PKCE)
- OpenID Connect (OIDC) - Identity layer on OAuth 2.0 with ID tokens
- SAML 2.0 - XML-based SSO protocol with browser redirects
- JWT (JSON Web Tokens) - Token-based authentication with claims
- API Key Authentication - Simple authentication via API keys
- Basic Authentication - HTTP basic auth with username/password
- Mutual TLS (mTLS) - Certificate-based mutual authentication

**Event-Driven Architecture**:
- Event Sourcing - Storing state changes as immutable events
- CQRS (Command Query Responsibility Segregation) - Separate read and write models
- Event Streaming - Continuous event processing (Kafka Streams, AWS Kinesis)
- Domain Events - Business-significant events in domain-driven design
- Event Notification - Lightweight events for state change notification
- Event-Carried State Transfer - Events containing full state information

**Testing & Validation**:
- Contract Testing - Pact, Spring Cloud Contract for API contract verification
- Integration Testing - Testing service interactions and message flows
- End-to-End Testing - Full user journey testing across services
- Mock Services - WireMock, MockServer for simulating external dependencies
- API Testing - Postman, REST Assured, SoapUI for API validation
- Chaos Engineering - Gremlin, Chaos Monkey for resilience testing

**Performance & Observability**:
- Distributed Tracing - Jaeger, Zipkin, AWS X-Ray for request tracing across services
- OpenTelemetry - Observability framework for traces, metrics, logs
- Application Performance Monitoring (APM) - New Relic, Datadog, Dynatrace
- Correlation IDs - Request tracking across distributed services
- Latency Analysis - Identifying bottlenecks in interaction sequences

**Documentation Standards**:
- OpenAPI (Swagger) - API documentation with example sequences
- AsyncAPI - Event-driven API documentation with message flows
- API Blueprint - API documentation with Markdown-based syntax
- RAML - RESTful API Modeling Language
- Living Documentation - Continuous documentation aligned with code

**Reference**: Consult API architects, integration specialists, and software engineering teams for detailed guidance on interaction patterns, messaging protocols, distributed system choreography, and sequence diagram modeling for your specific technology stack and integration scenarios

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
