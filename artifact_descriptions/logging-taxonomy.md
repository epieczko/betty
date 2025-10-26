# Name: logging-taxonomy

## Executive Summary

The Logging Taxonomy defines standardized logging practices including structured logging formats (JSON), log levels (TRACE, DEBUG, INFO, WARN, ERROR, FATAL), semantic field naming, and log aggregation patterns using ELK Stack, Splunk, Loki, Fluentd, and OpenTelemetry. This artifact establishes consistent logging conventions that enable efficient log search, correlation with metrics and traces, compliance with retention policies, and actionable insights for troubleshooting and incident response.

As the second pillar of observability (alongside metrics and traces), structured logging provides essential context for debugging production issues, security investigations, compliance audits, and user behavior analysis. The taxonomy ensures logs are machine-parseable, searchable, cost-effective to store, and integrated with distributed tracing through correlation IDs and OpenTelemetry context propagation.

### Strategic Importance

- **Structured Logging**: Enforces JSON log format with consistent field names, enabling programmatic parsing, filtering, and analysis across all services
- **Observability Integration**: Correlates logs with metrics and distributed traces using trace_id, span_id, and OpenTelemetry context propagation
- **Incident Response**: Accelerates troubleshooting through standardized log levels, error messages, stack traces, and contextual metadata
- **Compliance & Audit**: Supports regulatory requirements (SOC 2, GDPR, HIPAA) with audit logs, data classification, PII redaction, and retention policies
- **Cost Optimization**: Reduces log storage costs through appropriate log levels, sampling, retention tiers, and cost-per-GB awareness
- **Security Monitoring**: Enables SIEM integration, threat detection, authentication logging, and security event correlation

## Purpose & Scope

### Primary Purpose

This artifact standardizes log message formats, field names, log levels, and logging patterns across applications and infrastructure. It defines JSON structured logging schemas, required/optional fields (timestamp, level, message, service, trace_id), log level usage guidelines, PII redaction rules, and integration with log aggregation platforms (ELK, Splunk, Loki, CloudWatch Logs, Datadog Logs).

### Scope

**In Scope**:
- JSON structured logging format with standard fields (timestamp, level, logger, message, context)
- Log levels: TRACE, DEBUG, INFO, WARN, ERROR, FATAL with usage guidelines per environment
- OpenTelemetry logs integration with trace_id, span_id for logs-traces correlation
- Common log fields: service_name, environment, version, hostname, pod_name, request_id
- Error logging patterns: exception type, stack trace, error code, user impact
- Security/audit logging: authentication events, authorization failures, data access, admin actions
- PII/sensitive data redaction: credit cards, SSN, passwords, API keys, personal data
- Log aggregation platforms: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk, Grafana Loki
- Log shippers: Fluentd, Fluent Bit, Logstash, Vector, Filebeat, CloudWatch Agent
- Retention policies: production (30-90 days), compliance logs (7 years), debug logs (7 days)
- Log sampling and rate limiting for high-volume events
- Multi-line log handling: stack traces, JSON payloads, SQL queries
- Log parsing patterns (Grok, regex) and field extraction rules

**Out of Scope**:
- Metric instrumentation and metric catalog (covered in metric-catalog artifact)
- Distributed tracing span creation (covered in tracing instrumentation)
- Log-based alerting rules and thresholds (covered in alerting policies)
- Log storage infrastructure and capacity planning (covered in platform architecture)
- Application code logging implementation details (covered in development standards)
- SIEM-specific security rules and threat detection (covered in security artifacts)

### Target Audience

**Primary Audience**:
- Platform Engineers: Deploy log aggregation infrastructure, configure log shippers, manage retention policies
- SRE Teams: Define log-based alerts, troubleshoot production issues, correlate logs with metrics/traces
- Application Developers: Implement structured logging, follow log level guidelines, add contextual fields
- Security Engineers: Configure security/audit logging, implement PII redaction, integrate with SIEM

**Secondary Audience**:
- DevOps Engineers: Configure CI/CD pipeline logging, deployment tracking, build logs
- Compliance Officers: Review audit log requirements, retention policies, data classification
- Support Engineers: Search logs for customer issues, troubleshoot support tickets
- Engineering Leadership: Review logging costs, retention strategies, observability maturity

## Document Information

**Format**: Markdown

**File Pattern**: `*.logging-taxonomy.md`

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

**Structured JSON**: Always use JSON format with consistent field names; never use plain text logs in production
**ISO 8601 Timestamps**: Use RFC3339/ISO 8601 timestamps with UTC timezone (2024-01-15T10:30:00Z)
**Log Level Discipline**: DEBUG/TRACE off in production; INFO for business events; WARN for degraded state; ERROR for failures
**Trace Correlation**: Include trace_id, span_id in all logs when request context available (OpenTelemetry auto-instrumentation)
**Required Fields**: Always include: timestamp, level, service, environment, version, message, logger
**PII Redaction**: Automatically redact credit cards, SSN, passwords, tokens; use [REDACTED] placeholder
**Error Context**: Log exception type, message, stack trace, user_id, request_id, related entity IDs
**Semantic Field Names**: Use snake_case (user_id not userId), consistent names (http_status_code, request_method)
**No Log Injection**: Sanitize user input in log messages to prevent log injection attacks
**Sampling High-Volume**: Sample high-frequency logs (1% or 1 in 100); use dynamic sampling for errors (100%)
**Multi-Line Handling**: Properly format stack traces, SQL queries, JSON payloads as single log events
**Cost Awareness**: Monitor log volume GB/day; set quotas per service; archive cold logs to S3/GCS
**Retention Tiers**: Hot (7-30 days searchable), warm (30-90 days), cold (1-7 years archive), compliance (per regulation)
**Index Optimization**: Use time-based indices (logs-2024-01-15); optimize field mapping; limit analyzed fields
**Context Propagation**: Use logging frameworks with MDC/ThreadLocal for request_id, user_id across call chain
**Avoid Logs for Metrics**: Use metrics for counters/histograms; logs for contextual debugging; don't parse logs for metrics
**Security Logging**: Log authentication (success/failure), authorization decisions, sensitive data access, admin actions

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

**Logging Standards**:
- OpenTelemetry Logs - OTEL logs SDK, log bridge API, logs-traces correlation
- Syslog Protocol (RFC 5424) - Standard message format for logging
- Common Event Format (CEF) - ArcSight log format for SIEM integration
- JSON Schema - Structured logging field validation
- RFC 3339 - Timestamp format standard (ISO 8601 profile)

**Log Aggregation Platforms**:
- ELK Stack - Elasticsearch (storage/search), Logstash (processing), Kibana (visualization)
- Splunk - Enterprise log management, search, analysis, and alerting
- Grafana Loki - Log aggregation optimized for Kubernetes and Grafana
- Datadog Logs - Cloud-native log management with APM integration
- New Relic Logs - Application logs with traces and metrics correlation
- AWS CloudWatch Logs - AWS-native log aggregation and monitoring
- Azure Monitor Logs - Azure Log Analytics and KQL query language
- Google Cloud Logging - GCP-native log management with log router

**Log Shippers & Collectors**:
- Fluentd - Unified logging layer, CNCF graduated project
- Fluent Bit - Lightweight log processor and forwarder
- Logstash - Data processing pipeline for Elastic Stack
- Vector - High-performance observability data pipeline (Datadog)
- Filebeat - Lightweight log shipper (Elastic)
- Promtail - Log aggregator for Grafana Loki
- AWS CloudWatch Agent - Unified metrics and logs collection for AWS
- OpenTelemetry Collector - Vendor-agnostic logs, metrics, traces collector

**Logging Libraries**:
- Logback (Java) - Successor to log4j with SLF4J API
- Log4j 2 (Java) - Advanced logging framework with async appenders
- Winston (Node.js) - Universal logging library for Node applications
- Zap (Go) - Uber's high-performance structured logging
- Serilog (.NET) - Structured logging with sinks for various destinations
- Python logging - Standard library with handlers and formatters
- Bunyan (Node.js) - JSON logging library
- Logrus (Go) - Structured logger for Go

**Structured Logging**:
- JSON Logging - Machine-parseable log format with key-value pairs
- Logfmt - Key-value logging format (Heroku)
- ECS (Elastic Common Schema) - Standardized field names for Elastic
- MozDef Schema - Mozilla Defense Platform log schema
- OCSF (Open Cybersecurity Schema Framework) - Security log standard

**Log Search & Analysis**:
- Elasticsearch - Distributed search and analytics engine
- Splunk SPL - Splunk Search Processing Language
- LogQL - Grafana Loki query language
- KQL (Kusto Query Language) - Azure Log Analytics query language
- CloudWatch Logs Insights - AWS log query and analysis
- BigQuery - Google's serverless data warehouse for log analytics

**Compliance & Security**:
- GDPR - Data privacy and PII protection requirements
- SOC 2 - Audit log requirements for security controls
- HIPAA - Healthcare data logging and retention
- PCI DSS - Payment card industry logging standards
- NIST SP 800-92 - Guide to computer security log management
- CIS Controls - Log collection, retention, and review requirements
- ISO 27001 - Information security logging requirements

**Log Retention & Archival**:
- Amazon S3 - Long-term log archival with lifecycle policies
- Google Cloud Storage - Cold storage for historical logs
- Azure Blob Storage - Archive tier for compliance logs
- Glacier/Deep Archive - Ultra-low-cost archival storage

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
