# Name: production-hygiene-checklist

## Executive Summary

The Production Hygiene Checklist is a comprehensive pre-deployment validation artifact that ensures production environments maintain operational excellence, security posture, monitoring coverage, runbook readiness, and on-call preparedness before and after releases. This SRE-focused checklist validates infrastructure health, configuration management, observability setup, incident response readiness, and operational best practices to prevent production issues and enable rapid recovery.

Production hygiene integrates with Site Reliability Engineering (SRE) practices, Google SRE principles, DevOps operational excellence, and ITIL 4 Service Operations. It covers monitoring and alerting (Prometheus, Grafana, Datadog), logging and tracing (ELK, Splunk, Jaeger), runbook completeness, on-call schedules (PagerDuty, Opsgenie), backup validation, disaster recovery testing, security configurations (secrets management, network policies), capacity planning, and technical debt tracking. Regular hygiene checks prevent configuration drift, monitoring gaps, and operational readiness degradation.

### Strategic Importance

- **Operational Excellence**: Ensures production environments maintain SRE best practices and operational readiness standards
- **Incident Prevention**: Proactively identifies monitoring gaps, configuration issues, and operational risks before they cause outages
- **Mean Time to Recovery (MTTR)**: Validates runbooks, rollback procedures, and incident response readiness for rapid recovery
- **Observability Coverage**: Confirms comprehensive monitoring, logging, tracing, and alerting across all critical services
- **On-Call Readiness**: Validates on-call schedules, escalation paths, runbook access, and incident response training
- **Security Hygiene**: Ensures secrets rotation, vulnerability patching, access control reviews, and security baseline compliance
- **Compliance Evidence**: Provides operational readiness audit trail for SOC 2, ISO 27001, regulatory requirements

## Purpose & Scope

### Primary Purpose

The production hygiene checklist validates operational readiness, infrastructure health, monitoring coverage, runbook completeness, security posture, and incident response preparedness before deployments and during regular operational reviews. It prevents production issues through proactive validation of SRE best practices, operational excellence standards, and production readiness criteria.

### Scope

**In Scope**:
- Monitoring and alerting validation (Prometheus, Grafana, Datadog, New Relic dashboards and alerts)
- SLI/SLO/SLA tracking (service level indicators, objectives, error budgets, availability targets)
- Logging and log aggregation (ELK Stack, Splunk, CloudWatch Logs, structured logging)
- Distributed tracing (Jaeger, Zipkin, AWS X-Ray, Datadog APM, OpenTelemetry)
- Runbook completeness (deployment procedures, rollback steps, troubleshooting guides, incident response)
- On-call schedule validation (PagerDuty, Opsgenie rotations, escalation policies, coverage gaps)
- Incident response readiness (war room procedures, communication plans, postmortem process)
- Backup and restore validation (database backups, configuration backups, restore testing, RPO/RTO)
- Disaster recovery testing (failover procedures, multi-region setup, DR drills, business continuity)
- Security configuration review (secrets rotation, TLS certificates, IAM policies, network policies, firewall rules)
- Capacity planning and auto-scaling (resource utilization, scaling policies, cost optimization, performance baselines)
- Configuration management (infrastructure as code, configuration drift detection, version control)
- Dependency health checks (third-party service monitoring, API health checks, circuit breakers)
- Technical debt tracking (known issues, workarounds, maintenance windows, deprecation plans)
- Performance monitoring (latency percentiles, throughput, error rates, resource saturation)
- Cost management (cloud cost monitoring, budget alerts, cost allocation tags, optimization opportunities)
- Change freeze compliance (blackout period validation, emergency change procedures)
- Documentation currency (architecture diagrams, API docs, troubleshooting guides, contact information)

**Out of Scope**:
- Application-specific feature testing (handled by QA testing and release certification)
- Code quality and test coverage (handled by release certification checklist)
- Detailed deployment procedures (handled by deployment runbooks)
- Release-specific risk assessment (handled by release-risk-assessment.md)

### Target Audience

**Primary Audience**:
- SRE Teams validating operational readiness and production environment health
- DevOps Engineers ensuring infrastructure and deployment pipeline readiness
- Platform Engineers maintaining shared platform services and operational tooling
- Operations Managers overseeing production environment stability and incident response
- On-Call Engineers confirming runbook availability and incident response preparedness

**Secondary Audience**:
- Release Managers incorporating hygiene checks into release certification
- Engineering Managers ensuring operational excellence within development teams
- Security Teams validating security configuration and secrets management
- Compliance Officers reviewing operational controls for SOC 2, ISO 27001 audits
- Executive Leadership monitoring operational health metrics and SLO performance

## Document Information

**Format**: Markdown

**File Pattern**: `*.production-hygiene-checklist.md`

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

**Regular Hygiene Reviews**: Conduct production hygiene checks weekly or biweekly, not just before major releases
**Automated Validation**: Automate checklist validation where possible (monitoring coverage, backup success, certificate expiration)
**SLI/SLO Tracking**: Define and track service level indicators/objectives for all critical services
**Monitoring Coverage Gaps**: Identify and remediate monitoring blind spots before they cause incidents
**Alert Tuning**: Continuously tune alerts to reduce noise and prevent alert fatigue
**Runbook Testing**: Actually execute runbooks in staging to validate accuracy, don't just maintain documentation
**Backup Restore Testing**: Regularly test backup restores (quarterly minimum), not just backup creation
**On-Call Rotation Balance**: Ensure sustainable on-call rotations with adequate coverage and backup responders
**Incident Response Drills**: Conduct game day exercises to validate incident response procedures
**Configuration Drift Detection**: Implement automated drift detection for infrastructure as code
**Secrets Rotation**: Automate secrets rotation and track expiration dates proactively
**TLS Certificate Monitoring**: Monitor certificate expiration 90 days in advance with alerts
**Dependency Health Checks**: Monitor third-party service health and implement circuit breakers
**Technical Debt Tracking**: Maintain visible technical debt backlog and prioritize remediation
**Cost Optimization Reviews**: Conduct monthly cost reviews and implement right-sizing recommendations
**Capacity Planning**: Review resource utilization trends and forecast scaling needs quarterly
**Documentation Currency**: Review and update documentation during every major incident or change
**Postmortem Action Items**: Track and complete action items from postmortems, don't let them languish
**Change Freeze Compliance**: Respect change freeze periods except for validated emergency changes
**War Room Readiness**: Pre-establish war room bridge details for major deployments and incidents

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

**Site Reliability Engineering (SRE)**:
- Google SRE Book - Site Reliability Engineering principles and practices
- SLI/SLO/SLA Framework - Service level indicators, objectives, and agreements
- Error Budgets - Acceptable failure rate based on SLO targets
- Toil Reduction - Automation of repetitive operational tasks
- Capacity Planning - Resource forecasting and scaling strategies
- On-Call Best Practices - Sustainable on-call rotations and incident response
- Blameless Postmortems - Learning-focused incident retrospectives

**Monitoring & Observability**:
- The Three Pillars of Observability - Metrics, logs, traces
- Prometheus - Metrics collection and alerting (PromQL, alert rules, recording rules)
- Grafana - Visualization dashboards and alerting
- Datadog - Full-stack observability platform (APM, infrastructure, logs, synthetics)
- New Relic - Application performance monitoring and observability
- ELK Stack - Elasticsearch, Logstash, Kibana for log aggregation
- Splunk - Log management and analysis platform
- Jaeger / Zipkin - Distributed tracing systems
- OpenTelemetry - Vendor-neutral observability instrumentation
- Golden Signals - Latency, traffic, errors, saturation (Google SRE)

**Alerting & Incident Management**:
- PagerDuty - Incident management and on-call orchestration
- Opsgenie - Alert management and on-call scheduling
- VictorOps (Splunk On-Call) - Incident response collaboration
- Alert Fatigue Prevention - Alert prioritization and noise reduction
- Escalation Policies - Multi-tier incident escalation
- Runbook Automation - Rundeck, StackStorm, Ansible AWX
- Incident Command System (ICS) - Structured incident response roles

**Logging & Log Management**:
- Structured Logging - JSON logging format for parsing and analysis
- Log Levels - DEBUG, INFO, WARN, ERROR, FATAL standardization
- Log Retention Policies - Storage duration and archival strategies
- Log Correlation - Request ID tracking across distributed systems
- ELK Stack - Elasticsearch, Logstash, Kibana pipeline
- Fluentd / Fluent Bit - Log collection and forwarding
- CloudWatch Logs - AWS native log aggregation
- Google Cloud Logging - GCP log management

**Distributed Tracing**:
- OpenTelemetry - Vendor-neutral tracing instrumentation
- Jaeger - Uber's distributed tracing platform
- Zipkin - Twitter's distributed tracing system
- AWS X-Ray - AWS distributed tracing service
- Datadog APM - Application performance monitoring with tracing
- Trace Context Propagation - W3C Trace Context standard
- Span Attributes - Metadata enrichment for traces

**Backup & Disaster Recovery**:
- 3-2-1 Backup Rule - 3 copies, 2 media types, 1 offsite
- RPO (Recovery Point Objective) - Acceptable data loss in time
- RTO (Recovery Time Objective) - Acceptable downtime duration
- Backup Testing - Regular restore validation
- Disaster Recovery Plans - Failover procedures and DR drills
- Multi-Region Architecture - Geographic redundancy
- Database Replication - Master-replica, multi-master, cross-region
- Backup Automation - Automated backup scheduling and verification

**Security & Compliance**:
- Secrets Management - HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- Secrets Rotation - Automated credential rotation policies
- TLS Certificate Management - Certificate expiration monitoring and auto-renewal
- IAM Policies - Principle of least privilege, role-based access control
- Network Policies - Firewall rules, security groups, network segmentation
- Vulnerability Scanning - Trivy, Clair, Snyk, container and host scanning
- Security Baseline - CIS Benchmarks, NIST guidelines, OWASP standards
- SOC 2 Type 2 - Operational control evidence
- ISO 27001 - ISMS operational requirements

**Infrastructure & Configuration Management**:
- Infrastructure as Code - Terraform, Pulumi, CloudFormation, Ansible
- Configuration Drift Detection - Terraform plan, CloudFormation drift detection
- GitOps - ArgoCD, Flux CD for declarative infrastructure
- Immutable Infrastructure - Container images, AMI baking, immutable deployments
- Configuration Management - Ansible, Chef, Puppet, SaltStack
- Version Control - Git-based infrastructure versioning
- Environment Parity - Dev/staging/production consistency

**Capacity Planning & Performance**:
- Resource Utilization Monitoring - CPU, memory, disk, network metrics
- Auto-Scaling Policies - Horizontal and vertical scaling automation
- Load Testing - JMeter, Gatling, k6, Locust capacity validation
- Performance Baselines - Historical performance data for anomaly detection
- Cost Optimization - Right-sizing, reserved instances, spot instances
- Cloud Cost Management - AWS Cost Explorer, GCP Cost Management, Azure Cost Management
- Capacity Forecasting - Growth projections and resource planning

**Runbooks & Documentation**:
- Runbook Standards - Consistent format for operational procedures
- Deployment Runbooks - Step-by-step deployment procedures
- Rollback Procedures - Detailed rollback instructions with triggers
- Troubleshooting Guides - Common issues and resolution steps
- Architecture Diagrams - System topology and data flow documentation
- On-Call Handbooks - On-call engineer reference materials
- Knowledge Base - Confluence, Notion, GitBook operational wiki

**Change Management & Release**:
- ITIL 4 Change Enablement - Change control integration
- Change Freeze Periods - Blackout windows for changes
- Maintenance Windows - Approved change windows
- Blue-Green Deployment - Zero-downtime deployment strategy
- Canary Deployment - Progressive rollout with monitoring
- Feature Flags - LaunchDarkly, Split.io, Unleash rollout control

**Chaos Engineering**:
- Chaos Monkey - Netflix random instance termination
- Gremlin - Chaos engineering platform
- LitmusChaos - Kubernetes native chaos engineering
- AWS Fault Injection Simulator - Managed chaos experiments
- Chaos Engineering Principles - Steady state, hypothesis, experiments

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
