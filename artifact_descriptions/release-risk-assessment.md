# Name: release-risk-assessment

## Executive Summary

The Release Risk Assessment artifact is a structured evaluation document that identifies, analyzes, and mitigates potential risks associated with production deployments. Using Failure Mode and Effects Analysis (FMEA), pre-mortem analysis, and DORA metrics insights, this artifact quantifies deployment risk, estimates blast radius, defines rollback criteria, and establishes mitigation strategies before production release.

Release risk assessment integrates with ITIL 4 Change Enablement processes, deployment readiness reviews, and Change Advisory Board (CAB) decision-making. It evaluates technical risks (performance degradation, data corruption, service outages), operational risks (monitoring gaps, inadequate rollback procedures), security risks (vulnerability introduction, compliance violations), and business risks (customer impact, revenue disruption, SLA breaches). The assessment directly influences deployment strategies (blue-green, canary, rolling), change window selection, and go/no-go decisions.

### Strategic Importance

- **Risk Quantification**: Applies FMEA scoring (Severity x Likelihood) to prioritize risks and inform mitigation strategies
- **Blast Radius Analysis**: Estimates customer impact, service disruption, and recovery time objectives for failure scenarios
- **Deployment Strategy Selection**: Determines appropriate deployment approach (blue-green, canary, rolling) based on risk profile
- **Rollback Readiness**: Defines automated and manual rollback triggers, procedures, and validation criteria
- **Change Advisory Board Input**: Provides structured risk data for CAB approval and change classification decisions
- **DORA Metrics Alignment**: Tracks deployment frequency, lead time, change failure rate, and mean time to recovery
- **Compliance Documentation**: Supports SOC 2, ISO 27001 risk management and audit requirements

## Purpose & Scope

### Primary Purpose

Release risk assessment systematically evaluates potential failure modes, estimates impact severity, calculates likelihood, defines mitigation strategies, and establishes rollback criteria for production deployments. It supports go/no-go decisions, deployment strategy selection, change window approval, and CAB risk evaluation using FMEA methodology and pre-mortem analysis techniques.

### Scope

**In Scope**:
- FMEA risk scoring (Severity x Likelihood x Detection) for technical, operational, security, business risks
- Pre-mortem analysis identifying potential failure scenarios before deployment
- Blast radius estimation (percentage of users affected, services impacted, revenue at risk)
- Rollback criteria definition (automated triggers, manual decision thresholds, success metrics)
- Mean Time to Recovery (MTTR) estimation for various failure scenarios
- Deployment strategy recommendation (blue-green, canary with percentage thresholds, rolling with batch size)
- Technical risk analysis (performance degradation, database migration failures, dependency failures, compatibility issues)
- Operational risk analysis (monitoring gaps, runbook inadequacy, insufficient capacity, configuration errors)
- Security risk analysis (vulnerability introduction, privilege escalation, data exposure, compliance violations)
- Business risk analysis (customer impact, SLA breach likelihood, revenue disruption, competitive disadvantage)
- Change classification (standard, normal, emergency) based on ITIL 4 Change Enablement
- Mitigation strategy documentation (risk avoidance, reduction, transfer, acceptance with justification)
- Feature flag rollback plan (gradual rollout percentages, automated rollback triggers, monitoring thresholds)
- Database rollback validation (forward and backward migration testing, data integrity verification)
- DORA metrics context (deployment frequency, lead time for changes, change failure rate, MTTR trends)

**Out of Scope**:
- Detailed release certification checklist (handled by release-certification.md)
- Actual CAB meeting minutes and voting records (handled by cab-approvals.md)
- Detailed deployment runbooks and procedures (handled by deployment documentation)
- Post-incident root cause analysis (handled by incident postmortem reports)

### Target Audience

**Primary Audience**:
- Release Managers evaluating risk vs. business value tradeoffs and deployment timing
- SRE Teams assessing operational risks, recovery procedures, and monitoring adequacy
- Change Advisory Board (CAB) members making approval decisions based on risk profile
- Engineering Managers prioritizing risk mitigation work and deployment strategy
- DevOps Engineers implementing deployment strategies and rollback automation

**Secondary Audience**:
- Security Teams evaluating security risk exposure and vulnerability impact
- Product Managers balancing feature delivery urgency against deployment risk
- Executive Leadership reviewing high-risk releases and business impact
- Compliance Officers ensuring risk management aligns with regulatory requirements
- Customer Success Teams preparing for potential customer impact communication

## Document Information

**Format**: Markdown

**File Pattern**: `*.release-risk-assessment.md`

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

### Assessment Methodology

**Approach**:
- `assessmentFramework`: Framework or standard used (e.g., NIST, ISO, proprietary)
- `assessmentScope`: Systems, processes, or areas assessed
- `evaluationCriteria`: Specific criteria used for evaluation
- `maturityModel`: Maturity levels if applicable (Initial, Managed, Defined, etc.)
- `scoringMethodology`: How scores or ratings are assigned

**Assessment Execution**:
- `assessmentPeriod`: Time period covered by the assessment
- `dataCollectionMethods`: Interviews, documentation review, testing, observation
- `participantsInterviewed`: Roles and number of people interviewed
- `evidenceReviewed`: Types and volume of evidence examined
- `limitations`: Any limitations or constraints on the assessment

### Findings & Results

**Summary Results**:
- `overallRating`: Aggregate assessment result
- `maturityLevel`: Current maturity level if using maturity model
- `complianceScore`: Percentage compliance if applicable
- `trendAnalysis`: Comparison to previous assessments

**Detailed Findings**:
- `findingId`: Unique identifier for each finding
- `findingCategory`: Category or control area
- `findingTitle`: Concise title
- `description`: Detailed description of finding
- `severity`: Critical | High | Medium | Low
- `evidence`: Supporting evidence for finding
- `impact`: Business or technical impact
- `likelihood`: Probability of occurrence if risk-related
- `currentState`: Current state or practice observed
- `desiredState`: Target state or required practice
- `gap`: Specific gap between current and desired
- `recommendations`: Specific remediation recommendations
- `priority`: Prioritization for remediation
- `estimatedEffort`: Effort required to remediate

### Remediation Plan

**Recommendations Summary**:
- `totalRecommendations`: Count by severity
- `quickWins`: High-value, low-effort improvements
- `strategicInitiatives`: Long-term, high-effort improvements
- `costBenefitAnalysis`: Estimated cost vs. benefit for major recommendations

**Remediation Roadmap**:
- `phase1Immediate`: 0-3 months, critical items
- `phase2NearTerm`: 3-6 months, high priority items
- `phase3MidTerm`: 6-12 months, medium priority items
- `phase4LongTerm`: 12+ months, strategic initiatives

**Implementation Tracking**:
- `recommendationOwner`: Who is responsible for each item
- `targetCompletionDate`: When remediation should be complete
- `statusTracking`: Mechanism for tracking progress
- `successCriteria`: How completion will be verified


## Best Practices

**FMEA Scoring Consistency**: Use standardized scoring scales (1-10) for Severity, Likelihood, Detection to enable risk comparison
**Pre-Mortem Facilitation**: Conduct collaborative pre-mortem sessions with engineering, SRE, security, and product teams
**Quantify Blast Radius**: Estimate specific percentages (e.g., "affects 15% of users", "impacts $50K/hour revenue") not vague terms
**Define Measurable Rollback Triggers**: Specify objective thresholds (error rate > 5%, p95 latency > 500ms, 10 customer complaints)
**Risk Mitigation Accountability**: Assign owners and completion dates for each mitigation action
**Historical Incident Integration**: Reference past incidents and postmortems to identify recurring risk patterns
**Deployment Strategy Alignment**: Match deployment approach to risk score (high risk = canary, low risk = rolling)
**Feature Flag Strategy**: Plan progressive rollout percentages (1% → 5% → 25% → 50% → 100%) with dwell times
**Database Risk Emphasis**: Give special attention to schema changes, data migrations, and rollback complexity
**Dependency Risk Mapping**: Identify external service dependencies and their failure modes
**Load Test Validation**: Require load testing for changes with performance or capacity risk
**Security Risk Prioritization**: Address critical and high severity vulnerabilities before deployment
**DORA Metrics Context**: Review historical change failure rate and MTTR to inform risk assessment
**Stakeholder Risk Tolerance**: Document explicitly accepted risks with business justification
**Monitoring Gap Identification**: Call out missing metrics, alerts, or dashboards as operational risks
**On-Call Preparation**: Ensure on-call engineers briefed on failure scenarios and rollback procedures
**Customer Communication Plan**: Define proactive and reactive customer communication triggers
**Change Window Optimization**: Schedule high-risk deployments during low-traffic periods
**Rollback Testing**: Validate rollback procedures in staging before certifying production readiness
**Post-Deployment Review**: Schedule review meeting 24-48 hours after deployment to validate risk assessment accuracy

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

**Risk Assessment Methodologies**:
- FMEA (Failure Mode and Effects Analysis) - Severity x Likelihood x Detection scoring
- Pre-Mortem Analysis - Prospective hindsight technique for identifying failure scenarios
- ISO 31000 - Risk management guidelines and principles
- NIST Risk Management Framework (RMF) - Federal risk assessment standard
- FAIR (Factor Analysis of Information Risk) - Quantitative risk analysis
- COSO Enterprise Risk Management - Enterprise risk framework
- Bow Tie Analysis - Risk evaluation and barrier identification
- Fault Tree Analysis - Deductive failure analysis technique

**DORA Metrics & Performance**:
- DORA (DevOps Research and Assessment) - Four key metrics framework
- Deployment Frequency - How often code deploys to production
- Lead Time for Changes - Time from commit to production deployment
- Change Failure Rate - Percentage of deployments causing failures
- Mean Time to Recovery (MTTR) - Average time to restore service after failure
- Error Budget - SLO-based allowance for failures and changes
- Availability Targets - SLA/SLO uptime commitments

**Change Management & ITIL**:
- ITIL 4 Change Enablement - Risk-based change classification and approval
- ITIL 4 Risk Management - Service risk identification and mitigation
- Standard Change - Pre-authorized, low-risk changes with documented procedures
- Normal Change - Requires CAB evaluation and approval based on risk
- Emergency Change - High-urgency changes with expedited approval process
- ServiceNow Change Management - Change request workflow and risk scoring
- Jira Service Management - Change tracking and approval workflows

**Deployment Strategies & Risk Mitigation**:
- Blue-Green Deployment - Instant rollback capability via traffic switching
- Canary Deployment - Gradual rollout with progressive percentage increases (1%, 5%, 25%, 50%, 100%)
- Rolling Deployment - Sequential instance updates with batch size optimization
- Shadow Deployment - Production traffic replication for risk-free testing
- A/B Testing - User segmentation for controlled feature exposure
- Dark Launches - Production deployment with feature flags disabled
- Ring Deployment - Progressive rollout to internal → beta → production user rings

**Feature Flag Management**:
- LaunchDarkly - Enterprise feature flag platform with targeting and rollout controls
- Split.io - Feature flags with experimentation and impact analysis
- Unleash - Open-source feature toggle system
- Flagsmith - Remote config and feature flag management
- CloudBees Feature Management - Enterprise feature flag platform
- Optimizely - A/B testing and feature experimentation
- Kill Switch Pattern - Emergency feature disablement capability

**Rollback & Recovery**:
- Automated Rollback Triggers - Metric-based automated deployment reversal
- Manual Rollback Procedures - Step-by-step reversal documentation
- Database Rollback Strategies - Forward-only migrations, expand/contract pattern
- Blue-Green Traffic Shift - Instant rollback via load balancer reconfiguration
- Canary Rollback - Automatic traffic rerouting on error rate threshold breach
- Checkpoint Recovery - Point-in-time restore capabilities
- Chaos Engineering - Resilience validation via Chaos Monkey, Gremlin, LitmusChaos

**Blast Radius Analysis**:
- Customer Impact Estimation - Percentage of users, geographic regions, accounts affected
- Service Dependency Mapping - Upstream and downstream service impact analysis
- Revenue Impact Calculation - Financial exposure from service disruption
- SLA Breach Risk - Likelihood and severity of availability target violations
- Data Integrity Risk - Potential for data corruption, loss, or exposure
- Reputation Risk - Brand and customer trust impact assessment

**Monitoring & Alerting**:
- Golden Signals - Latency, traffic, errors, saturation monitoring
- SLI/SLO/SLA Framework - Service level objectives and error budgets
- Prometheus + Grafana - Metrics collection and visualization
- Datadog - Full-stack monitoring and alerting
- New Relic - Application performance monitoring (APM)
- PagerDuty / Opsgenie - Incident alerting and escalation
- Deployment Markers - Release tracking in monitoring dashboards
- Anomaly Detection - Statistical deviation alerts for deployment impact

**Capacity & Performance**:
- Load Testing - JMeter, Gatling, k6, Locust pre-deployment validation
- Stress Testing - System behavior under extreme load conditions
- Capacity Planning - Resource utilization forecasting and scaling
- Performance Regression Testing - Benchmark comparison across releases
- Auto-Scaling Validation - Horizontal scaling behavior verification
- Database Performance - Query performance, index optimization, connection pooling

**Security & Compliance Risk**:
- Vulnerability Scanning - SAST, DAST, SCA, container scanning
- CVE Risk Scoring - CVSS severity assessment for identified vulnerabilities
- Penetration Testing - Security control validation before release
- Secrets Management - Credential rotation and secure storage validation
- Compliance Controls - SOC 2, ISO 27001, HIPAA, PCI-DSS requirement validation
- Data Privacy Impact - GDPR, CCPA compliance risk assessment

**Business Continuity**:
- Disaster Recovery Testing - DR plan validation and RTO/RPO verification
- Backup Validation - Backup integrity and restore procedure testing
- Failover Testing - Multi-region/multi-AZ failover capability validation
- Business Impact Analysis - Critical service identification and prioritization

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
