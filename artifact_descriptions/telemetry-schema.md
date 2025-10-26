# Name: telemetry-schema

## Executive Summary

Telemetry Schemas define the structure and semantics of observability data including traces, metrics, and logs collected from distributed systems. These schemas ensure consistent telemetry instrumentation, enable correlation across signals, and support effective monitoring, debugging, and performance analysis of cloud-native applications.

Built following OpenTelemetry standards, W3C Trace Context, Prometheus data model, and observability best practices, telemetry schemas leverage frameworks like OpenTelemetry SDK, Jaeger, Zipkin, Prometheus, Grafana, Datadog, New Relic, and AWS X-Ray. They define span attributes, metric dimensions, log fields, semantic conventions, resource attributes, and sampling strategies that enable unified observability, distributed tracing, and SLO/SLI monitoring across microservices and serverless architectures.

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

This artifact defines the structure, semantic conventions, and standards for telemetry data (traces, metrics, logs) collected from distributed systems. It establishes consistent instrumentation patterns, attribute naming, span semantics, metric types, and log fields that enable unified observability, distributed tracing correlation, and effective monitoring across heterogeneous services and infrastructure.

### Scope

**In Scope**:
- OpenTelemetry Trace schema (spans, span attributes, span events, span links)
- OpenTelemetry Metrics schema (counters, gauges, histograms, summaries)
- OpenTelemetry Logs schema (log records, severity, attributes)
- Semantic conventions (HTTP, RPC, database, messaging, FaaS)
- Resource attributes (service.name, service.version, deployment.environment)
- W3C Trace Context (traceparent, tracestate headers)
- Prometheus metric naming conventions and labels
- Span status codes and error attributes
- Sampling strategies and decisions
- Context propagation and baggage

**Out of Scope**:
- Telemetry backend configuration (Jaeger, Prometheus, Grafana)
- Instrumentation library implementations
- Alert rules and dashboard definitions
- Log aggregation pipeline configuration
- APM vendor-specific features
- Infrastructure monitoring agents

### Target Audience

**Primary Audience**:
- SRE Engineers implementing observability
- Platform Engineers managing observability infrastructure
- Backend Engineers instrumenting services
- DevOps Engineers monitoring systems

**Secondary Audience**:
- Software Architects designing observable systems
- Security Engineers analyzing audit logs
- Performance Engineers optimizing applications
- Support Teams troubleshooting production issues

## Document Information

**Format**: Text

**File Pattern**: `*.telemetry-schema.txt`

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

**Semantic Conventions**:
- **Follow OTel Standards**: Use OpenTelemetry semantic conventions for consistency
- **Attribute Naming**: Use snake_case for attribute names; include namespace prefix (http., db., messaging.)
- **Resource Attributes**: Always set service.name, service.version, deployment.environment
- **Standard Attributes**: Prefer standard attributes over custom ones; extends existing conventions when needed

**Trace Instrumentation**:
- **Span Naming**: Use meaningful span names describing operation (HTTP GET /users, db.query users)
- **Span Hierarchy**: Create parent-child relationships reflecting call stack
- **Span Attributes**: Add relevant attributes (http.method, http.status_code, db.statement)
- **Span Events**: Record important events within span lifetime (exception, retry, cache hit)
- **Span Status**: Set span status (OK, ERROR) and status message for failures
- **Error Recording**: Always record exceptions with exception.type, exception.message, exception.stacktrace

**Metrics Instrumentation**:
- **Metric Naming**: Use descriptive names with unit suffixes (http_requests_total, response_time_seconds)
- **Metric Types**: Choose correct type - Counter (monotonic), Gauge (fluctuating), Histogram (distribution)
- **Dimensions**: Add dimensions as labels/attributes (method, status_code, environment)
- **Cardinality**: Avoid high-cardinality labels (user_id, request_id); prevents metric explosion
- **Aggregation**: Design metrics for aggregation (SUM, AVG, P95, P99)

**Structured Logging**:
- **JSON Format**: Use structured JSON logs for machine readability
- **Standard Fields**: Include timestamp, severity, message, trace_id, span_id
- **Log Correlation**: Always include trace_id and span_id for trace-log correlation
- **Severity Levels**: Use appropriate levels (ERROR for errors, WARN for warnings, INFO for informational)
- **Avoid PII**: Sanitize logs to remove sensitive data (passwords, credit cards, SSNs)

**Context Propagation**:
- **W3C Trace Context**: Use traceparent/tracestate headers for HTTP
- **gRPC Metadata**: Propagate context via gRPC metadata
- **Async Operations**: Propagate context to async/background tasks
- **Baggage**: Use baggage sparingly for cross-cutting concerns (user_id, tenant_id)

**Sampling Strategy**:
- **Head-Based Sampling**: Sample at request entry point; consistent sampling decision
- **Adaptive Sampling**: Adjust sampling rates based on traffic volume
- **Error Sampling**: Always sample error traces (100% error sampling)
- **Tail-Based Sampling**: Sample after trace completes based on latency/errors (requires collector)
- **Debug Override**: Allow forcing sampling for debugging (X-Debug header)

**Performance Considerations**:
- **Instrumentation Overhead**: Minimize instrumentation impact (<5% overhead target)
- **Batch Exports**: Export telemetry in batches, not per-event
- **Async Export**: Export asynchronously; don't block request processing
- **Sampling**: Use sampling to reduce data volume for high-traffic services
- **Attribute Limits**: Limit number of attributes per span/metric (avoid unbounded attributes)

**Correlation & Observability**:
- **Trace-Log Correlation**: Include trace_id and span_id in all logs
- **Metric-Trace Exemplars**: Link metrics to traces with exemplars
- **Distributed Context**: Propagate context across all service boundaries
- **Request IDs**: Use consistent correlation IDs across entire request path

**Schema Evolution**:
- **Backward Compatibility**: Additive changes only (new attributes, metrics)
- **Deprecation**: Mark deprecated attributes; maintain for transition period
- **Versioning**: Version telemetry schemas; document changes
- **Migration**: Provide migration guides when changing conventions

**Cardinality Management**:
- **Bounded Dimensions**: Use finite value sets for dimensions (avoid user_id, request_id)
- **Aggregation Labels**: Group low-value dimensions (http status: 2xx, 4xx, 5xx)
- **Cardinality Limits**: Monitor metric cardinality; alert on explosions
- **Drop High-Cardinality**: Drop or aggregate high-cardinality dimensions

**Security & Privacy**:
- **Sensitive Data**: Never log passwords, tokens, API keys, credit cards
- **PII Scrubbing**: Sanitize PII from logs and traces automatically
- **Data Retention**: Define retention policies for telemetry data
- **Access Control**: Restrict access to production telemetry data

**Testing & Validation**:
- **Instrumentation Tests**: Test that instrumentation produces expected telemetry
- **Trace Validation**: Validate trace structure and attributes
- **Metric Validation**: Verify metrics increment correctly
- **End-to-End Tests**: Test telemetry propagation across services

**Documentation**:
- **Semantic Conventions**: Document custom attributes and their meanings
- **Instrumentation Guide**: Provide instrumentation guidelines for teams
- **Troubleshooting**: Document how to use telemetry for debugging
- **SLI/SLO Definitions**: Document SLIs, SLOs, and how they're measured

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

**OpenTelemetry (OTel)**:
- OpenTelemetry Specification 1.x (CNCF standard)
- OpenTelemetry Protocol (OTLP) for data export
- Traces: Spans, span context, span attributes, span events, span links
- Metrics: Instruments (Counter, Gauge, Histogram, UpDownCounter)
- Logs: Log records, severity levels, log attributes
- Resource semantic conventions (service, cloud, container, k8s)
- Instrumentation libraries (auto/manual instrumentation)

**OpenTelemetry Semantic Conventions**:
- HTTP: http.method, http.status_code, http.url, http.route
- RPC: rpc.system, rpc.service, rpc.method, rpc.grpc.status_code
- Database: db.system, db.connection_string, db.statement, db.operation
- Messaging: messaging.system, messaging.destination, messaging.operation
- FaaS: faas.trigger, faas.execution, faas.coldstart
- General: exception.type, exception.message, exception.stacktrace

**W3C Trace Context**:
- traceparent header (version-trace_id-span_id-flags)
- tracestate header (vendor-specific trace state)
- Context propagation across service boundaries
- Baggage for cross-cutting concerns

**Prometheus Data Model**:
- Metric naming conventions (snake_case with unit suffixes)
- Label naming (avoid label cardinality explosion)
- Metric types: Counter, Gauge, Histogram, Summary
- PromQL query language
- Recording rules and aggregation
- Remote write protocol

**Distributed Tracing**:
- Jaeger: Trace collection, storage, and visualization
- Zipkin: Distributed tracing system
- AWS X-Ray: Trace segments and subsegments
- Google Cloud Trace: Latency data collection
- Datadog APM: Application performance monitoring

**Log Standards**:
- Structured logging (JSON format)
- Common log fields: timestamp, severity, message, trace_id, span_id
- Severity levels: TRACE, DEBUG, INFO, WARN, ERROR, FATAL
- ECS (Elastic Common Schema) for log standardization
- Syslog RFC 5424
- GELF (Graylog Extended Log Format)

**Metrics Conventions**:
- RED Method: Rate, Errors, Duration (for requests)
- USE Method: Utilization, Saturation, Errors (for resources)
- Four Golden Signals: Latency, Traffic, Errors, Saturation (Google SRE)
- SLI/SLO/SLA: Service Level Indicators, Objectives, Agreements

**Observability Backends**:
- Jaeger (traces)
- Prometheus + Grafana (metrics + visualization)
- Elasticsearch + Kibana (logs)
- Grafana Loki (log aggregation)
- ClickHouse (high-performance analytics)
- Tempo (distributed tracing backend)

**Commercial APM Platforms**:
- Datadog: Unified observability platform
- New Relic: Application monitoring
- Dynatrace: Full-stack monitoring
- Splunk: Log management and analytics
- Elastic APM: Application Performance Monitoring
- Honeycomb: Observability for production systems

**Sampling Strategies**:
- Always-on sampling (100% of traces)
- Probabilistic sampling (random percentage)
- Rate-limiting sampling (max traces per second)
- Tail-based sampling (sample after trace completion)
- Adaptive sampling (adjust based on load)
- Parent-based sampling (follow parent span decision)

**Context Propagation**:
- Trace context propagation (HTTP headers, gRPC metadata)
- Baggage for cross-cutting concerns
- Span context injection/extraction
- In-process context propagation
- Correlation IDs for request tracing

**Instrumentation Patterns**:
- Auto-instrumentation (bytecode injection, eBPF)
- Manual instrumentation (SDK usage)
- Library instrumentation (middleware, interceptors)
- Custom metrics and traces
- Exemplars (linking metrics to traces)

**Data Export Formats**:
- OTLP (OpenTelemetry Protocol): gRPC, HTTP/Protobuf, HTTP/JSON
- Jaeger Thrift format
- Zipkin JSON format
- Prometheus remote write
- StatsD protocol

**Tooling & SDKs**:
- OpenTelemetry SDKs (Java, .NET, Python, Go, Node.js, Ruby, PHP)
- OpenTelemetry Collector (agent, gateway modes)
- OpenTelemetry Auto-Instrumentation
- Prometheus client libraries
- Grafana (visualization and dashboards)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application. Refer to opentelemetry.io and prometheus.io documentation.

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
