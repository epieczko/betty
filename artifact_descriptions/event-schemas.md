# Name: event-schemas

## Executive Summary

Event Schemas define the structure, format, and contracts for event messages in event-driven architectures. These schemas ensure consistent event production and consumption across distributed systems, microservices, and event streaming platforms like Apache Kafka, RabbitMQ, AWS EventBridge, Azure Event Grid, and Google Cloud Pub/Sub.

Built using schema definition languages including Apache Avro, Protocol Buffers (Protobuf), JSON Schema, CloudEvents specification, and AsyncAPI, event schemas are managed through schema registries such as Confluent Schema Registry, AWS Glue Schema Registry, Azure Schema Registry, and Apicurio Registry. They support schema evolution (backward, forward, and full compatibility), event versioning, event sourcing patterns, CQRS (Command Query Responsibility Segregation), and ensure type safety and validation for event-driven communication across heterogeneous systems.

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

This artifact defines event message schemas for event-driven systems, specifying event structure, data types, required/optional fields, metadata, and versioning strategies. It establishes contracts between event producers and consumers, enabling schema validation, evolution management, and type-safe event processing across distributed architectures.

### Scope

**In Scope**:
- Event payload structure and data types
- Event metadata (event type, timestamp, correlation ID, causation ID)
- CloudEvents specification compliance (type, source, subject, id, time)
- Schema formats: Avro (.avsc), Protobuf (.proto), JSON Schema (.json)
- Schema versioning and compatibility rules (backward, forward, full)
- Event envelope patterns
- Domain events vs. integration events
- Event naming conventions and namespacing
- Schema registry configuration and policies
- Event serialization/deserialization contracts

**Out of Scope**:
- Event streaming platform configuration (Kafka, Kinesis)
- Event processing logic and handlers
- Message routing and topic topology
- Consumer group management
- Event store implementation details
- Infrastructure provisioning

### Target Audience

**Primary Audience**:
- Event Architects designing event-driven systems
- Backend Engineers producing/consuming events
- Integration Engineers building event-based integrations
- Platform Engineers managing schema registries

**Secondary Audience**:
- Software Architects reviewing event contracts
- QA Engineers validating event contracts
- Data Engineers processing event streams
- DevOps Engineers managing event infrastructure

## Document Information

**Format**: JSON

**File Pattern**: `*.event-schemas.json`

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

**Schema Evolution Strategy**:
- **Backward Compatibility**: Always add new fields as optional; never remove or rename existing fields
- **Forward Compatibility**: Use default values for new fields; old consumers can ignore unknown fields
- **Breaking Changes**: Version events (e.g., OrderPlaced.v1, OrderPlaced.v2); support parallel schemas during migration
- **Semantic Versioning**: Use MAJOR.MINOR.PATCH; increment MAJOR for breaking changes
- **Deprecation Policy**: Mark deprecated fields in schema; maintain for minimum 6-12 months before removal

**Event Schema Design**:
- **CloudEvents Compliance**: Follow CloudEvents spec for metadata (id, source, type, time, datacontenttype)
- **Event Type Naming**: Use past-tense verbs (OrderPlaced, PaymentProcessed, not PlaceOrder, ProcessPayment)
- **Namespacing**: Organize events by domain (com.company.orders.OrderPlaced)
- **Required vs Optional**: Mark all fields as optional by default unless truly required; enables evolution
- **Rich Types**: Use specific types (timestamp, UUID, enum) instead of generic strings
- **Avoid Nulls**: Use optional fields or default values instead of null

**CloudEvents Metadata**:
- **Unique ID**: Use UUID v4 for event id; ensures global uniqueness
- **Source**: Identify event producer (service name, URL); enables tracing
- **Type**: Use reverse-DNS notation (com.company.orders.OrderPlaced)
- **Correlation ID**: Include correlation/trace ID for distributed tracing
- **Causation ID**: Link to triggering event for event chains
- **Timestamp**: Always include ISO 8601 timestamp with timezone

**Schema Format Selection**:
- **Avro**: Best for Kafka, schema evolution, code generation; compact binary format
- **Protobuf**: Excellent performance, strong typing, backward/forward compatibility
- **JSON Schema**: Human-readable, good for HTTP/REST events, debugging
- **CloudEvents**: Use as envelope; wrap Avro/Protobuf payload with CloudEvents metadata

**Schema Registry Usage**:
- **Register Before Producing**: Always register schema in registry before producing events
- **Compatibility Mode**: Set appropriate compatibility mode (backward, forward, full, none)
- **Subject Naming**: Use TopicNameStrategy, RecordNameStrategy, or TopicRecordNameStrategy
- **Version Control**: Store .avsc/.proto files in Git; schema registry is deployment artifact
- **Schema Validation**: Enable producer/consumer validation against schema registry

**Event Content Design**:
- **Minimal vs Complete**: Event Notification (minimal payload) vs Event-Carried State Transfer (full state)
- **Self-Contained**: Include enough context so consumers don't need to query other services
- **Sensitive Data**: Avoid PII in events; use references/IDs; consider encryption
- **Event Size**: Keep events under 1MB; large payloads impact performance
- **Immutability**: Events represent facts; never modify published events

**Domain Events vs Integration Events**:
- **Domain Events**: Internal to bounded context; rich business semantics
- **Integration Events**: Cross-context communication; stable contracts; versioned
- **Event Translation**: Use anti-corruption layer to translate between domain/integration events

**Versioning Strategies**:
- **Schema Evolution**: Prefer schema evolution over explicit versioning when possible
- **Event Type Versioning**: Include version in event type (OrderPlaced.v1, OrderPlaced.v2)
- **Header Versioning**: Store version in event metadata/headers
- **Namespace Versioning**: Use namespace (com.company.v1.orders.OrderPlaced)
- **Parallel Versions**: Run multiple versions simultaneously during migration period

**Testing & Validation**:
- **Schema Validation**: Validate all events against registered schemas in CI/CD
- **Contract Testing**: Test producer/consumer compatibility with Pact or similar
- **Schema Evolution Tests**: Test backward/forward compatibility with old/new schemas
- **Compatibility Checks**: Automate compatibility validation in CI pipeline
- **Test Data Generation**: Generate test events from schemas

**Documentation**:
- **Field Descriptions**: Document business meaning of every field in schema
- **Event Purpose**: Explain when and why event is published
- **Consumer Guidance**: Document expected consumer behavior
- **Schema Examples**: Provide valid event examples in documentation
- **Change Log**: Maintain schema change history with migration guides

**Monitoring & Operations**:
- **Schema Registry Metrics**: Monitor schema registration, compatibility checks
- **Validation Errors**: Alert on schema validation failures
- **Version Usage**: Track which schema versions are actively used
- **Deprecation Warnings**: Log warnings for deprecated schema usage

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

**Event Schema Formats**:
- Apache Avro: JSON-based schema with rich data types, schema evolution, code generation
- Protocol Buffers (Protobuf): Google's binary serialization, efficient, strongly typed
- JSON Schema: Draft 7/2019-09/2020-12, validation keywords, OpenAPI integration
- CloudEvents 1.0: CNCF standard for event metadata (type, source, id, time, datacontenttype)
- Apache Thrift: Cross-language serialization (Facebook)
- Cap'n Proto: Evolved from Protobuf, zero-copy serialization

**Schema Registries**:
- Confluent Schema Registry: Kafka-native, Avro/Protobuf/JSON Schema support
- AWS Glue Schema Registry: Integrated with MSK, Kinesis
- Azure Schema Registry (Event Hubs): Avro schema management
- Apicurio Registry: Open-source, multi-format support
- Karapace: Aiven's open-source alternative to Confluent

**Schema Evolution & Compatibility**:
- Backward Compatibility: New schema reads old data (safe to update consumers first)
- Forward Compatibility: Old schema reads new data (safe to update producers first)
- Full Compatibility: Both backward and forward compatible
- Transitive Compatibility: Compatibility across all versions, not just adjacent
- Breaking Changes: Field removal, type changes, required field additions
- Safe Changes: Adding optional fields, removing optional fields, adding enums

**Event-Driven Architecture Patterns**:
- Event Notification: Minimal event payload, consumer pulls details
- Event-Carried State Transfer: Full state in event, no additional queries
- Event Sourcing: Events as source of truth, state derived from event log
- CQRS: Separate read/write models, events synchronize models
- Saga Pattern: Long-running transactions via choreographed events
- Outbox Pattern: Transactional event publishing

**CloudEvents Specification**:
- Required attributes: id, source, specversion, type
- Optional attributes: datacontenttype, dataschema, subject, time
- Extension attributes: Custom metadata
- Event formats: JSON, Avro, Protobuf
- Protocol bindings: HTTP, AMQP, MQTT, Kafka, NATS

**Event Messaging Patterns**:
- Publish-Subscribe (Pub/Sub)
- Point-to-Point (Queue)
- Request-Reply with correlation ID
- Fire-and-Forget
- Competing Consumers
- Message Filtering and Content-Based Routing

**Event Platforms & Brokers**:
- Apache Kafka: Distributed streaming, topics, partitions, consumer groups
- RabbitMQ: AMQP broker, exchanges, queues, routing keys
- AWS EventBridge: Serverless event bus, schema discovery
- Azure Event Grid: Event routing, filtering, dead-lettering
- Google Cloud Pub/Sub: Global messaging, topics, subscriptions
- Apache Pulsar: Multi-tenancy, geo-replication
- NATS: Lightweight, cloud-native messaging

**Serialization Best Practices**:
- Schema-first development (define schemas before code)
- Compact binary formats for high-throughput (Avro, Protobuf)
- Human-readable JSON for debugging/low-volume events
- Schema validation on producer and consumer sides
- Code generation from schemas (type safety)

**Event Design Patterns**:
- Event Versioning: Semantic versioning, namespace versioning, header versioning
- Event Enrichment: Adding contextual data to events
- Event Transformation: Format conversion, field mapping
- Event Filtering: Content-based routing
- Dead Letter Queues: Failed message handling
- Idempotent Consumers: Deduplication strategies

**Tooling**:
- Schema Design: Confluent Schema Registry UI, Apicurio Studio
- Code Generation: Avro Tools, Protoc (Protobuf compiler), QuickType
- Validation: JSON Schema validators, Avro validators
- Testing: Kafka Schema Registry mock, Testcontainers
- Monitoring: Schema Registry metrics, compatibility checks

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application. Refer to CloudEvents specification and Confluent Schema Registry documentation.

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
