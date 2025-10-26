# Name: error-taxonomy

## Executive Summary

The Error Taxonomy defines standardized error classification, error codes, exception hierarchies, and failure handling patterns across distributed systems. This artifact establishes consistent error responses using HTTP status codes (4xx, 5xx), gRPC status codes, application-specific error codes, and structured error messages that enable automated error tracking, SLO measurement, error budget calculations, and effective client retry strategies.

As a critical component of SRE reliability practices, the Error Taxonomy distinguishes user errors from system failures, enables error budget tracking per Google SRE methodology, and supports intelligent error handling including circuit breakers, retries with exponential backoff, and graceful degradation. Consistent error classification powers error rate metrics, SLI calculations, and automated alerting.

### Strategic Importance

- **Error Budget Management**: Classifies errors for SLO tracking, error budget consumption, and burn rate calculations per Google SRE principles
- **Reliability Measurement**: Enables accurate error rate SLIs by distinguishing user errors (4xx) from system failures (5xx) in availability calculations
- **Client Experience**: Provides actionable error messages with error codes, retry guidance, and resolution steps for API consumers
- **Automated Monitoring**: Powers error tracking platforms (Sentry, Rollbar, Bugsnag) with structured exceptions, stack traces, and contextual metadata
- **Incident Response**: Accelerates troubleshooting through error code search, exception aggregation, and historical error pattern analysis
- **API Consistency**: Standardizes error responses across REST APIs, GraphQL, gRPC, and asynchronous messaging systems

## Purpose & Scope

### Primary Purpose

This artifact standardizes error classification, error code formats, exception hierarchies, and error response structures across all services and APIs. It defines HTTP status codes usage, gRPC status codes, custom application error codes (ERR-1001, AUTH-403-01), error message templates, retry semantics, and integration with error tracking platforms like Sentry, Rollbar, and Datadog Error Tracking.

### Scope

**In Scope**:
- HTTP status codes (4xx client errors, 5xx server errors) with semantic usage guidelines
- gRPC status codes (OK, INVALID_ARGUMENT, UNAVAILABLE, INTERNAL, etc.)
- REST API error responses (RFC 7807 Problem Details, JSON:API error format)
- GraphQL error extensions and error codes
- Application error code taxonomy (domain-specific, hierarchical error codes)
- Exception class hierarchies (RetryableException, PermanentException, ValidationException)
- Error SLI classification (which errors count against SLOs, which are excluded)
- Error budget impact scoring (critical vs. minor errors, weight by severity)
- Structured error logging with exception types, stack traces, correlation IDs
- Error tracking platform integration (Sentry, Rollbar, Bugsnag, Datadog APM)
- Retry strategies (exponential backoff, jitter, circuit breaker patterns)
- Error message localization and user-facing error text

**Out of Scope**:
- Application-specific business logic error handling (covered in development standards)
- Infrastructure failure modes and disaster recovery (covered in resilience architecture)
- Security incident classification and threat taxonomy (covered in security artifacts)
- Performance degradation and latency issues (covered in SLO definitions)
- Metric instrumentation for error rates (covered in metric-catalog artifact)
- Alert definitions and escalation policies (covered in alerting workflows)

### Target Audience

**Primary Audience**:
- SRE Teams: Define error budget calculations, classify errors for SLI tracking, set error rate thresholds
- Application Developers: Implement exception handling, return structured errors, integrate error tracking SDKs
- API Engineers: Design consistent error responses, document error codes, implement retry logic
- Platform Engineers: Configure error tracking infrastructure, aggregate errors, define error budgets

**Secondary Audience**:
- DevOps Engineers: Monitor error rates, troubleshoot deployment failures, track rollback triggers
- Support Engineers: Interpret error codes, troubleshoot customer issues, escalate based on error severity
- Engineering Leadership: Review error budgets, reliability trends, incident patterns
- QA Engineers: Validate error handling, test retry logic, verify error messages

## Document Information

**Format**: Markdown

**File Pattern**: `*.error-taxonomy.md`

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

**4xx vs 5xx**: Use 4xx for client errors (bad request, auth failure) that don't count against SLOs; 5xx for system failures that consume error budget
**Specific Status Codes**: Use precise codes (401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests, 503 Service Unavailable)
**gRPC Status Codes**: Map to gRPC canonical codes (INVALID_ARGUMENT, UNAUTHENTICATED, PERMISSION_DENIED, UNAVAILABLE)
**Structured Errors**: Return JSON error objects with code, message, details, request_id, documentation_url
**Error Code Format**: Use hierarchical codes (AUTH-401-001, VAL-400-002, SYS-500-001) for categorization
**Retryable Classification**: Clearly mark errors as retryable (503, 429) or permanent (400, 404, 403)
**Idempotency Keys**: Support idempotency for POST/PUT requests to enable safe retries
**Exponential Backoff**: Implement exponential backoff with jitter (initial 1s, max 60s) for retry logic
**Circuit Breakers**: Use circuit breaker pattern after N consecutive failures to prevent cascade failures
**Error Budget Tracking**: Classify which errors consume error budget (5xx yes, 4xx no, specific exceptions)
**User-Facing Messages**: Provide actionable error messages; avoid stack traces or internal details in API responses
**Correlation IDs**: Include request_id/correlation_id in errors for distributed tracing and log correlation
**Error Grouping**: Use fingerprinting/grouping in Sentry/Rollbar to aggregate similar errors
**Stack Trace Capture**: Capture full stack traces in logs and error tracking; sanitize PII before sending
**Rate Limit Guidance**: Include Retry-After header for 429 responses; document rate limits in API docs
**Graceful Degradation**: Return partial results with warnings rather than hard failures when possible
**Error Documentation**: Maintain error catalog with each error code, meaning, resolution steps, examples

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

**HTTP Standards**:
- RFC 7231 - HTTP/1.1 Semantics (status codes definitions)
- RFC 7807 - Problem Details for HTTP APIs (structured error format)
- RFC 6585 - Additional HTTP Status Codes (428, 429, 431, 511)
- RFC 8288 - Web Linking for error documentation URLs

**gRPC Standards**:
- gRPC Status Codes - Canonical error codes (OK, CANCELLED, UNKNOWN, INVALID_ARGUMENT, etc.)
- gRPC Error Model - Rich error model with details, metadata, retry info
- google.rpc.Status - Protobuf error status format

**API Error Standards**:
- JSON:API Error Format - Standardized JSON error object structure
- OData Error Format - Microsoft OData error response format
- GraphQL Errors - GraphQL error extensions and error codes
- OpenAPI 3.0 - Error response schema definitions

**Error Tracking Platforms**:
- Sentry - Real-time error tracking with stack traces, breadcrumbs, releases
- Rollbar - Error monitoring and alerting with deployment tracking
- Bugsnag - Application stability monitoring with error grouping
- Datadog Error Tracking - APM-integrated error tracking and analytics
- New Relic Errors - Error analytics within APM platform
- Airbrake - Error monitoring with smart error grouping
- Raygun - Error tracking with user tracking and crash reporting

**Resilience Patterns**:
- Circuit Breaker - Netflix Hystrix, Resilience4j circuit breaker pattern
- Retry with Backoff - Exponential backoff with jitter algorithms
- Bulkhead Pattern - Isolate resources to prevent cascading failures
- Timeout Pattern - Fail fast with configurable timeouts
- Fallback Pattern - Graceful degradation and default responses

**SRE & Error Budgets**:
- Google SRE Book - Error budget methodology and SLI/SLO framework
- Error Budget Policy - How errors affect reliability targets
- Burn Rate Alerts - Fast/slow burn rate for SLO violations
- Blameless Postmortems - Root cause analysis without blame

**Exception Monitoring**:
- Sentry SDK - Language-specific error tracking integration
- Rollbar SDKs - Multi-language error reporting
- OpenTelemetry Exception Events - OTEL exception span events
- Application Insights - Azure exception tracking and analytics

**Error Response Frameworks**:
- Spring Boot - @ExceptionHandler, @ControllerAdvice error handling
- Express.js - Error handling middleware patterns
- ASP.NET Core - Exception filters and problem details
- Django REST Framework - Exception handling and error views

**Retry Libraries**:
- Resilience4j - Fault tolerance library for JVM
- Polly - .NET resilience and transient fault handling
- Tenacity - Python retry library with various strategies
- node-retry - Node.js retry library with exponential backoff

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
