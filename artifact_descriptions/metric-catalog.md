# Name: metric-catalog

## Executive Summary

The Metric Catalog is a comprehensive registry that documents all observability metrics collected across systems, services, and infrastructure. This artifact standardizes metric naming conventions, defines semantic meaning, manages cardinality, and ensures consistent instrumentation using Prometheus, OpenTelemetry, StatsD, and platform-specific metric libraries. It serves as the single source of truth for what metrics exist, how they're instrumented, and their intended use in monitoring, alerting, and SLO tracking.

As a foundational element of observability governance, the Metric Catalog prevents metric sprawl, reduces storage costs, and enables teams to discover and reuse existing metrics rather than creating duplicates. It enforces naming standards (Prometheus conventions, OpenTelemetry semantic conventions), manages high-cardinality labels, and documents metric lifecycles from instrumentation through deprecation.

### Strategic Importance

- **Metric Standardization**: Enforces consistent naming conventions following Prometheus and OpenTelemetry semantic conventions across all services and teams
- **Cardinality Management**: Prevents high-cardinality explosions that degrade query performance and increase storage costs in time-series databases
- **Observability Governance**: Establishes metric ownership, approval workflows, and deprecation policies to maintain metric catalog quality
- **Cost Optimization**: Reduces observability platform costs by eliminating duplicate metrics, optimizing retention, and managing cardinality
- **Discoverability**: Enables engineers to search and discover existing metrics before instrumenting new ones, reducing redundancy
- **SLI Foundation**: Provides curated metrics for Service Level Indicators, error budget calculations, and reliability tracking

## Purpose & Scope

### Primary Purpose

This artifact maintains a centralized registry of all metrics instrumented across applications, services, and infrastructure. It documents metric names, types (counter, gauge, histogram, summary), labels, semantic meaning, data sources, and usage context. The catalog enforces naming conventions (Prometheus snake_case, OpenTelemetry semantic conventions), manages cardinality budgets, and provides metric discovery capabilities for engineers, SREs, and observability platforms.

### Scope

**In Scope**:
- Prometheus metric naming conventions (snake_case, base units, suffixes like _total, _seconds, _bytes)
- OpenTelemetry semantic conventions for metrics (http.server.duration, db.client.connections.usage)
- Metric types: Counter, Gauge, Histogram, Summary (Prometheus); UpDownCounter, Observable metrics (OTEL)
- Label/tag taxonomy and cardinality limits (maximum label count, value cardinality per label)
- Custom application metrics with business context (orders_processed_total, payment_failures_total)
- Infrastructure metrics (CPU, memory, disk, network, container, Kubernetes resources)
- Platform-specific metrics (AWS CloudWatch, Datadog, New Relic, Dynatrace custom metrics)
- Metric lifecycle management (proposal, approval, instrumentation, deprecation, removal)
- Recording rules and aggregations for expensive queries
- Metric retention policies and downsampling strategies
- SLI metric definitions for error rate, latency, availability calculations
- Cardinality estimation and optimization guidelines

**Out of Scope**:
- Dashboard implementations (covered in monitoring-dashboards artifact)
- Alert rule definitions and thresholds (covered in alerting policies)
- Log message formats and structured logging (covered in logging-taxonomy artifact)
- Distributed tracing span attributes (covered in tracing instrumentation)
- Time-series database infrastructure setup (covered in platform architecture)
- Metric ingestion pipelines and collection agents (covered in observability infrastructure)

### Target Audience

**Primary Audience**:
- Observability Engineers: Define metric standards, manage catalog governance, optimize cardinality and storage costs
- SRE Teams: Instrument SLI metrics, create recording rules, define error budget tracking metrics
- Platform Engineers: Instrument infrastructure metrics, Kubernetes metrics, resource utilization tracking
- Application Developers: Discover existing metrics, instrument custom business metrics, follow naming conventions

**Secondary Audience**:
- DevOps Engineers: Instrument deployment metrics, CI/CD pipeline metrics, release tracking
- Engineering Leadership: Review metric coverage, observability maturity, cost allocation
- FinOps Teams: Track metrics-related costs, analyze cardinality impact on billing
- Data Engineers: Export metrics to data warehouses, integrate with BI/analytics platforms

## Document Information

**Format**: Markdown

**File Pattern**: `*.metric-catalog.md`

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

**Prometheus Naming**: Use snake_case with base units (seconds not milliseconds, bytes not megabytes), suffix counters with _total, timers with _seconds/_milliseconds
**OpenTelemetry Conventions**: Follow OTEL semantic conventions for HTTP (http.server.duration), RPC (rpc.server.duration), database (db.client.*)
**Metric Type Selection**: Use Counter for monotonically increasing values, Gauge for up/down values, Histogram for distributions (latency, size)
**Cardinality Limits**: Enforce strict limits on label count (max 10-15 labels) and label value cardinality (max 100-1000 unique values per label)
**Label Consistency**: Use consistent label names across metrics (service, environment, region vs service_name, env, aws_region)
**Avoid High-Cardinality**: Never use user_id, request_id, IP addresses, timestamps, or unbounded strings as label values
**Recording Rules**: Pre-compute expensive aggregations and multi-metric calculations using Prometheus recording rules
**Metric Ownership**: Assign DRI (Directly Responsible Individual) and owning team for each metric with Slack/email contact
**Deprecation Policy**: Mark deprecated metrics, provide migration paths, maintain deprecated metrics for 90 days minimum
**Cost Awareness**: Monitor active time series count; estimate storage costs; set cardinality budgets per team/service
**Documentation Requirements**: Document metric purpose, example queries, related dashboards/alerts, SLO usage
**Base Units Only**: Always use base units (seconds, bytes, ratios 0-1) to enable automatic conversion in dashboards
**Histogram Buckets**: Define sensible histogram buckets (e.g., latency: 0.001, 0.01, 0.1, 0.5, 1, 5, 10 seconds)
**Counter Suffixes**: Always suffix counters with _total (requests_total, errors_total, bytes_processed_total)
**Rate Calculations**: Document that counters require rate() function; never use irate() for alerting (use rate() instead)
**Label Ordering**: Order labels consistently (service before method before status_code) for better query performance
**Catalog Automation**: Auto-discover metrics from Prometheus targets; validate against catalog schema; flag undocumented metrics

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

**Metric Standards**:
- Prometheus Naming Conventions - snake_case, base units, suffixes (_total, _seconds, _bytes, _ratio)
- OpenTelemetry Semantic Conventions - Standardized metric names for HTTP, RPC, database, messaging, runtime
- OpenMetrics - Prometheus exposition format standard with enhanced metadata support
- StatsD Protocol - UDP-based metric aggregation and collection protocol
- Datadog Metrics - Custom metrics API, tags, metric types (gauge, count, rate, histogram)
- CloudWatch Metrics - AWS custom metrics, dimensions, statistics, metric math

**Time-Series Databases**:
- Prometheus - Pull-based monitoring with PromQL query language
- InfluxDB - High-performance time-series database with InfluxQL and Flux
- M3DB - Distributed TSDB with clustering and long-term storage
- VictoriaMetrics - Fast, cost-effective, Prometheus-compatible storage
- Cortex - Multi-tenant, horizontally scalable Prometheus
- Thanos - Prometheus with unlimited retention and global querying
- Graphite - Push-based metrics with Whisper storage engine
- TimescaleDB - PostgreSQL extension for time-series data

**OpenTelemetry**:
- OTEL Metrics SDK - Meter, instruments (Counter, Histogram, Gauge), metric exporters
- OTEL Semantic Conventions - Standard attributes for HTTP, RPC, DB, messaging, K8s, cloud
- OTEL Collector - Metric collection, processing, batching, and export
- OTEL Protocol (OTLP) - gRPC and HTTP/JSON metric transport
- Exemplars - Link metrics to traces for high-cardinality debugging

**Metric Libraries & Instrumentation**:
- Prometheus Client Libraries - Go, Java, Python, Ruby, .NET client libraries
- OpenTelemetry SDKs - Language-specific instrumentation for metrics collection
- Micrometer - Vendor-neutral application metrics facade for JVM
- StatsD Client Libraries - UDP metric submission from applications
- Datadog SDKs - DogStatsD protocol, tracing integration
- New Relic Agents - Language agents with automatic instrumentation

**Cardinality Management**:
- Prometheus Relabeling - Drop high-cardinality labels, normalize values
- Metric Limits - Configure max samples per scrape, label count limits
- Adaptive Metrics - Dynamic sampling, aggregation, and filtering (Datadog, Lightstep)
- Cardinality Estimation - Bloom filters, HyperLogLog for cardinality tracking
- Cost Attribution - Tag-based cost allocation and chargeback

**Query Languages**:
- PromQL - Prometheus Query Language for time-series queries and aggregations
- LogQL - Grafana Loki log query language (similar to PromQL)
- Flux - InfluxDB functional data scripting language
- MetricsQL - VictoriaMetrics query language (PromQL extension)
- M3 Query Language - M3DB query capabilities
- CloudWatch Insights - Metric math, search expressions, anomaly detection

**Metric Exporters**:
- Node Exporter - Hardware and OS metrics from Linux/Unix systems
- kube-state-metrics - Kubernetes object state metrics
- cAdvisor - Container resource usage metrics
- Blackbox Exporter - Probing endpoints (HTTP, HTTPS, DNS, TCP, ICMP)
- Custom Exporters - Application-specific Prometheus exporters

**Standards & Best Practices**:
- Google SRE Book - Monitoring distributed systems chapter
- SLI/SLO Framework - Service level metrics and reliability tracking
- RED Metrics - Rate, Errors, Duration for services
- USE Metrics - Utilization, Saturation, Errors for resources
- Four Golden Signals - Latency, Traffic, Errors, Saturation

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
