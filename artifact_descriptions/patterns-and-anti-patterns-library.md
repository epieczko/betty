# Name: patterns-and-anti-patterns-library

## Executive Summary

The Integration Patterns and Anti-Patterns Library is a curated knowledge base documenting proven integration patterns, microservices patterns, API design patterns, and anti-patterns to avoid when building distributed systems and service-oriented architectures. This artifact catalogs Enterprise Integration Patterns (EIP) from Hohpe & Woolf, cloud-native patterns, resilience patterns (Circuit Breaker, Retry, Bulkhead, Timeout), event-driven patterns, and API gateway patterns alongside common pitfalls and failure modes.

As a cornerstone of architectural guidance and knowledge sharing, this library accelerates solution design by providing reusable templates with concrete implementations using Kong, Apigee, AWS API Gateway, Istio, Spring Cloud, and other integration technologies. It documents when to use each pattern, trade-offs, implementation considerations, and concrete code examples in multiple languages (Java, Python, Node.js, Go). The library includes anti-patterns like Distributed Monolith, Chatty I/O, N+1 queries, and Cascading Failures with guidance on detection and remediation.

### Strategic Importance

- **Design Acceleration**: Reduces time to solution by providing proven patterns rather than reinventing approaches
- **Quality & Consistency**: Promotes architectural consistency across teams through shared pattern vocabulary
- **Risk Reduction**: Prevents common integration failures by documenting anti-patterns and their consequences
- **Knowledge Transfer**: Captures institutional knowledge and battle-tested solutions for new team members
- **Technology Agnostic**: Provides pattern abstractions that apply across technology stacks and platforms
- **Failure Prevention**: Documents failure modes, detection strategies, and recovery patterns
- **Best Practice Sharing**: Disseminates lessons learned from production systems and incident retrospectives

## Purpose & Scope

### Primary Purpose

This library provides architects, engineers, and technical leads with a comprehensive catalog of integration and microservices patterns to apply when designing distributed systems, along with anti-patterns to avoid. It solves the recurring problem of teams reinventing integration solutions by documenting proven approaches, implementation guidance, technology mappings, and real-world examples from organizational experience and industry best practices.

### Scope

**In Scope**:
- Enterprise Integration Patterns (Hohpe & Woolf): Message Channel, Message Router, Content-Based Router, Message Filter, Message Translator, Message Endpoint, Publish-Subscribe, Request-Reply, Correlation Identifier, Dead Letter Channel, Idempotent Receiver, Competing Consumers
- API Gateway Patterns: API Composition, Backends for Frontends (BFF), Rate Limiting, Request/Response Transformation, API Versioning, Circuit Breaking at Gateway
- Microservices Patterns: Service Discovery, Circuit Breaker, Bulkhead, Retry/Backoff, Timeout, Health Check, External Configuration, Saga, CQRS, Event Sourcing, API Gateway, Database per Service, Strangler Fig
- Resilience Patterns: Circuit Breaker (Hystrix, Resilience4j, Polly), Retry with Exponential Backoff, Bulkhead Isolation, Timeout, Fallback, Cache-Aside, Rate Limiting
- Event-Driven Patterns: Event Notification, Event-Carried State Transfer, Event Sourcing, CQRS, Saga (Orchestration vs. Choreography), Outbox Pattern, Change Data Capture
- API Design Patterns: RESTful Resource Design, HATEOAS, GraphQL Schema Design, gRPC Service Design, Pagination Patterns, Filtering/Sorting Patterns, API Versioning Strategies
- Integration Anti-Patterns: Distributed Monolith, Chatty I/O, N+1 Queries, Synchronous Coupling, Shared Database, Point-to-Point Integration Spaghetti, Big Ball of Mud, Golden Hammer, Premature Optimization, Cascading Failures, Split Brain, Thundering Herd
- Pattern catalog format: Problem statement, context, solution, consequences, implementation examples, when to use/avoid, related patterns

**Out of Scope**:
- Detailed implementation code (linked to code repositories)
- Infrastructure patterns (covered in cloud architecture patterns)
- Data modeling patterns (covered in data architecture standards)
- UI/UX patterns (covered in frontend design systems)
- Security patterns (covered in security architecture)

### Target Audience

**Primary Audience**:
- Integration Architects: Select patterns for integration solutions and avoid common pitfalls
- API Engineers: Apply API design patterns and resilience patterns in implementations
- Microservices Developers: Implement distributed system patterns correctly
- Technical Leads: Guide teams on pattern selection and architecture decisions

**Secondary Audience**:
- Application Architects: Understand integration options when designing applications
- Platform Engineers: Implement infrastructure supporting common patterns (service mesh, API gateways)
- DevOps/SRE Teams: Recognize anti-patterns causing operational issues
- Engineering Managers: Understand technical debt associated with anti-patterns
- New Team Members: Learn organizational integration standards and approaches

## Document Information

**Format**: Markdown

**File Pattern**: `*.patterns-and-anti-patterns-library.md`

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

**Structured Pattern Format**: Use consistent template: Problem, Context, Forces, Solution, Consequences, Implementation, Examples, Related Patterns
**Visual Diagrams**: Include sequence diagrams, architecture diagrams, and data flow diagrams for each pattern
**Concrete Examples**: Provide working code examples in organizational primary languages (Java, Python, Node.js, Go)
**Technology Mapping**: Map patterns to specific implementations (Kong plugins, Istio configs, Spring annotations)
**When to Use/Avoid**: Explicitly document applicability criteria and scenarios where pattern should not be used
**Trade-off Analysis**: Document benefits, drawbacks, and trade-offs for each pattern
**Anti-Pattern Detection**: Provide code smells and metrics indicating presence of anti-patterns
**Remediation Guidance**: For anti-patterns, document refactoring strategies and migration paths
**Real-World Examples**: Include organizational case studies and production system examples
**Pattern Relationships**: Cross-reference related patterns, alternatives, and complementary patterns
**Tool Integration**: Link patterns to organizational tools (API gateways, service mesh, message brokers)
**Performance Implications**: Document performance characteristics, latency impacts, throughput considerations
**Scalability Analysis**: Address how patterns behave under scale and load
**Failure Modes**: Document failure scenarios and mitigation strategies for each pattern
**Searchable Catalog**: Tag patterns by category, technology, problem domain for easy discovery
**Living Document**: Update patterns based on production learnings and incident retrospectives
**Organizational Context**: Adapt canonical patterns to organizational constraints and standards
**Pattern Governance**: Require architecture review for deviations from documented patterns
**Success Metrics**: Define how to measure successful pattern application
**Incident Learnings**: Document anti-patterns discovered through production incidents and root cause analyses

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

**Foundational Pattern Books**:
- Enterprise Integration Patterns (Hohpe & Woolf) - canonical EIP reference
- Microservices Patterns (Chris Richardson) - comprehensive microservices pattern catalog
- Building Microservices (Sam Newman) - service design and integration patterns
- Domain-Driven Design (Eric Evans) - bounded context and integration patterns
- Release It! (Michael Nygard) - stability patterns and anti-patterns
- Site Reliability Engineering (Google) - operational patterns and practices

**API & Integration Patterns**:
- RESTful Web Services patterns
- GraphQL schema design patterns
- gRPC service design patterns
- API Gateway patterns (Ambassador, BFF, Aggregation)
- Event-Driven Architecture patterns
- API-led connectivity (MuleSoft)
- Microservices.io pattern catalog
- Azure Cloud Design Patterns
- AWS Well-Architected Framework (Integration pillar)

**Resilience & Fault Tolerance**:
- Circuit Breaker pattern (Michael Nygard)
- Hystrix design patterns (Netflix)
- Resilience4j patterns (circuit breaker, retry, bulkhead, rate limiter, timeout)
- Polly resilience library (.NET patterns)
- Envoy proxy resilience patterns (retries, timeouts, circuit breaking)
- Istio traffic management patterns
- Chaos Engineering patterns (Chaos Monkey, fault injection)

**Microservices Patterns**:
- Service Discovery (Eureka, Consul, etcd)
- External Configuration (Spring Cloud Config, Consul KV)
- Health Check API pattern
- Database per Service pattern
- Saga pattern (orchestration vs. choreography)
- CQRS (Command Query Responsibility Segregation)
- Event Sourcing pattern
- API Gateway and BFF patterns
- Service Mesh pattern (Istio, Linkerd)
- Sidecar pattern
- Strangler Fig pattern
- Anti-Corruption Layer pattern

**Event-Driven Patterns**:
- Event Notification pattern
- Event-Carried State Transfer
- Event Sourcing
- CQRS with events
- Saga pattern for distributed transactions
- Outbox pattern for reliable publishing
- Change Data Capture (CDC) pattern
- Event Streaming patterns (Kafka)
- Pub/Sub patterns (RabbitMQ, SNS/SQS)

**Data Integration Patterns**:
- Database per Service
- Shared Database (anti-pattern in microservices)
- API Composition
- CQRS for read models
- Event Sourcing for audit trails
- Data Lake patterns
- ETL/ELT patterns
- Change Data Capture (Debezium, AWS DMS)

**Messaging Patterns**:
- Message Channel types (point-to-point, pub/sub)
- Message Router patterns (content-based, header-based)
- Message Translator
- Message Filter
- Dead Letter Queue
- Idempotent Consumer
- Competing Consumers
- Message Expiration
- Correlation Identifier
- Request-Reply over messaging

**API Gateway Technologies**:
- Kong Gateway patterns and plugins
- Apigee API proxy patterns
- AWS API Gateway integration patterns
- Azure API Management policies
- Tyk Gateway patterns
- NGINX API Gateway patterns
- Envoy proxy patterns
- Istio ingress gateway patterns

**Service Mesh Patterns**:
- Istio traffic management (routing, splitting, mirroring)
- Linkerd service mesh patterns
- Consul Connect patterns
- AWS App Mesh patterns
- Envoy proxy patterns (load balancing, circuit breaking, retries)
- mTLS authentication patterns
- Observability patterns (distributed tracing, metrics)

**Anti-Pattern References**:
- Distributed Monolith anti-pattern
- Chatty I/O anti-pattern
- N+1 query problem
- Synchronous coupling
- Shared database anti-pattern (microservices)
- God object / Big Ball of Mud
- Golden Hammer (over-reliance on one technology)
- Premature optimization
- Cascading failures
- Split brain problem
- Thundering herd
- Cache stampede
- Two-phase commit in distributed systems
- Distributed transactions anti-pattern

**Implementation Frameworks**:
- Spring Cloud (Netflix OSS patterns: Hystrix, Ribbon, Eureka, Zuul)
- Spring Integration (EIP implementation)
- Apache Camel (EIP framework)
- MassTransit (.NET messaging)
- NServiceBus (enterprise service bus)
- Temporal (workflow orchestration)
- Conductor (Netflix workflow orchestration)

**Pattern Documentation Standards**:
- Gang of Four (GoF) pattern template
- Pattern-Oriented Software Architecture (POSA) format
- Alexandrian pattern form
- Architecture Decision Records (ADR) for pattern decisions

**Industry Best Practices**:
- The Twelve-Factor App methodology
- Netflix OSS architectural patterns
- Amazon API Gateway patterns
- Google Cloud Architecture Framework
- Microsoft Azure Architecture Center patterns
- Martin Fowler's pattern catalog (martinfowler.com)
- Sam Newman's microservices resources

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
