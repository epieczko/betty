# Name: scaling-policies

## Executive Summary

The Scaling Policies artifact defines auto-scaling configuration for Kubernetes HPA/VPA, AWS Auto Scaling Groups, Azure VMSS, or GCP Managed Instance Groups, documenting target utilization thresholds (70% CPU, 80% memory), scale-up/scale-down rules, cooldown periods, and minimum/maximum instance counts. Effective auto-scaling ensures applications maintain performance SLOs during traffic spikes while minimizing infrastructure costs during low-traffic periods through automatic capacity adjustment.

Scaling policies translate capacity models and load profiles into automated infrastructure responses. They specify when to add instances (CPU >70% for 3 minutes), how quickly to scale (add 20% capacity, max 10 instances at once), and when to scale down (CPU <30% for 10 minutes to avoid thrashing). Policies balance responsiveness (scale quickly during spikes), stability (avoid oscillation), and cost (scale down during low traffic), with different strategies for predictable patterns (scheduled scaling) vs. reactive scaling (metric-based).

### Strategic Importance

- **Performance Assurance**: Automatically adds capacity during traffic spikes to maintain response time SLOs
- **Cost Optimization**: Scales down during low-traffic periods to minimize idle resource costs (30-50% savings typical)
- **Availability Protection**: Ensures sufficient capacity for failover scenarios and unexpected traffic surges
- **Operational Efficiency**: Eliminates manual intervention for routine capacity adjustments
- **Predictability**: Scheduled scaling handles known patterns (business hours, batch jobs, seasonal events)
- **Burst Handling**: Reactive scaling responds to unexpected traffic increases within minutes
- **Resource Efficiency**: Maintains target utilization (70% CPU) avoiding both under-utilization and saturation

## Purpose & Scope

### Primary Purpose

This artifact documents auto-scaling policies for Kubernetes (HPA/VPA), AWS (Auto Scaling Groups), Azure (VMSS), or GCP (MIG), defining target metrics (CPU 70%, memory 80%, custom metrics), scale-up/scale-down thresholds, cooldown periods, rate limits, and scheduled scaling to automatically adjust capacity based on load while optimizing costs.

### Scope

**In Scope**:
- Kubernetes HPA: Horizontal Pod Autoscaler configuration, target CPU/memory utilization, custom metrics (RPS, queue depth)
- Kubernetes VPA: Vertical Pod Autoscaler for right-sizing resource requests/limits
- Kubernetes Cluster Autoscaler: Node pool scaling based on pending pods and resource requests
- AWS Auto Scaling Groups: EC2 instance scaling, target tracking, step scaling, scheduled scaling
- Azure VMSS: Virtual Machine Scale Sets auto-scaling based on metrics or schedule
- GCP Autoscaler: Managed Instance Group scaling policies
- KEDA: Kubernetes Event-Driven Autoscaling for queue-based, event-driven scaling
- Target utilization: CPU 60-70%, memory 70-80%, custom metrics (RPS, latency, queue depth)
- Scale-up policies: Threshold (CPU >70%), evaluation periods (3 minutes), increment (20% or 2 instances)
- Scale-down policies: Threshold (CPU <30%), cooldown (10 minutes), decrement (10% or 1 instance)
- Minimum/maximum capacity: Min instances for availability, max for cost control
- Cooldown periods: Prevent thrashing by waiting after scaling actions (5-15 minutes typical)
- Scheduled scaling: Time-based scaling for predictable patterns (business hours, batch jobs)

**Out of Scope**:
- Detailed capacity planning models (covered in capacity-models)
- Infrastructure-as-Code implementation (Terraform, CloudFormation, ARM templates)
- Load balancer configuration and health checks
- Application-level circuit breakers and rate limiting
- Database auto-scaling (separate database scaling policies)

### Target Audience

**Primary Audience**:
- Platform Engineers implementing auto-scaling policies for applications
- SRE Teams ensuring availability and performance through appropriate scaling
- Cloud Architects designing scalable, cost-efficient infrastructure

**Secondary Audience**:
- Development Teams understanding how applications scale under load
- FinOps Teams optimizing infrastructure costs through effective auto-scaling
- Capacity Planners validating scaling policies against growth projections

## Document Information

**Format**: Markdown

**File Pattern**: `*.scaling-policies.md`

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

**Kubernetes Auto-Scaling**:
- Horizontal Pod Autoscaler (HPA): Scale pods based on CPU, memory, or custom metrics
- Vertical Pod Autoscaler (VPA): Adjust resource requests/limits based on actual usage
- Cluster Autoscaler: Add/remove nodes based on pending pods and resource availability
- KEDA: Event-driven autoscaling for queues (SQS, RabbitMQ, Kafka), databases, HTTP traffic
- Metrics Server: Provides resource metrics (CPU, memory) for HPA
- Custom Metrics API: Prometheus adapter for custom metrics (RPS, latency, queue depth)
- External Metrics API: Cloud provider metrics (CloudWatch, Azure Monitor, GCP Monitoring)

**AWS Auto-Scaling**:
- EC2 Auto Scaling Groups: Scale EC2 instances based on CloudWatch metrics
- Target Tracking Scaling: Maintain target metric (CPU 70%, ALB requests per target)
- Step Scaling: Different scaling amounts based on alarm severity
- Scheduled Scaling: Time-based scaling for predictable patterns
- Predictive Scaling: ML-based forecasting for proactive scaling
- Warm Pools: Pre-initialized instances for faster scale-up
- Lifecycle Hooks: Custom actions during instance launch/termination

**Azure Auto-Scaling**:
- Virtual Machine Scale Sets (VMSS): Auto-scaling for Azure VMs
- Azure Monitor Autoscale: Metric-based and schedule-based scaling
- Azure Kubernetes Service (AKS): HPA and cluster autoscaler
- Application Gateway Autoscaling: Scale application gateway instances
- App Service Autoscale: Scale App Service plans based on metrics

**GCP Auto-Scaling**:
- Managed Instance Groups (MIG): Auto-scaling for Compute Engine VMs
- GKE Autoscaling: HPA and cluster autoscaler for Kubernetes
- Cloud Run: Automatic scaling to zero for serverless containers
- App Engine: Automatic scaling for App Engine applications
- Stackdriver Monitoring: Metrics for auto-scaling decisions

**Scaling Metrics**:
- CPU Utilization: Most common, target 60-70% for headroom
- Memory Utilization: Target 70-80%, watch for OOM kills
- Request Rate: Requests per second per instance (e.g., 100 RPS/instance)
- Latency: P95 or P99 response time as scaling trigger
- Queue Depth: Pending items in message queue (SQS, RabbitMQ, Kafka)
- Custom Metrics: Application-specific metrics via Prometheus, CloudWatch, etc.
- Connection Count: Active connections per instance (databases, websockets)

**Scaling Strategies**:
- Reactive Scaling: Scale based on current metrics (CPU, memory, RPS)
- Predictive Scaling: ML-based forecasting and proactive capacity addition
- Scheduled Scaling: Time-based scaling for known patterns (business hours, batch jobs)
- Event-Driven Scaling: KEDA for queue-based workloads, scale to zero when idle
- Hybrid Approach: Scheduled baseline + reactive scaling for bursts
- Scale-to-Zero: Serverless patterns (Cloud Run, Knative, Lambda) for sporadic workloads

**Scaling Configuration Best Practices**:
- Target Utilization: CPU 60-70%, memory 70-80% for headroom
- Minimum Instances: At least 2 for availability, more for high-traffic services
- Maximum Instances: Set based on cost limits and downstream capacity (database connections)
- Scale-Up Speed: Aggressive (add 20-50% capacity) to handle spikes quickly
- Scale-Down Speed: Conservative (remove 10% capacity) to avoid thrashing
- Cooldown Periods: 5-10 minutes for scale-up, 10-15 minutes for scale-down
- Evaluation Periods: 2-3 data points before scaling to avoid noise

**Anti-Thrashing Techniques**:
- Cooldown Periods: Wait after scaling before evaluating again
- Different Up/Down Thresholds: Scale up at 70%, down at 30% (hysteresis)
- Longer Evaluation for Scale-Down: Require sustained low utilization
- Gradual Scale-Down: Remove instances slowly (1 at a time vs. percentage)
- Scheduled Minimums: Maintain baseline during business hours even if metrics low

**Cost Optimization with Auto-Scaling**:
- Reserved Instances/Savings Plans: Cover baseline capacity, auto-scale on-demand instances
- Spot Instances: Use for fault-tolerant workloads in auto-scaling groups (70-90% cost savings)
- Scale-to-Zero: Serverless or KEDA for non-production or sporadic workloads
- Scheduled Scale-Down: Reduce capacity during off-hours (nights, weekends)
- Right-Sizing: Use VPA or monitoring data to optimize resource requests
- Cluster Autoscaler: Remove underutilized nodes automatically

**Monitoring & Observability**:
- Scaling Events: Track scale-up/scale-down actions, timing, reasons
- Capacity Metrics: Current instances vs. min/max, utilization trends
- Latency Impact: Response times before/during/after scaling events
- Cost Metrics: Instance costs correlated with auto-scaling behavior
- Throttling Events: Downstream systems unable to handle scale-up
- Scale-Up Lag: Time from trigger to new capacity serving traffic

**Reference**: Consult platform engineering and SRE teams for auto-scaling configuration and optimization guidance

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
