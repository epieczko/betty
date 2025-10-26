# Name: configuration-drift-reports

## Executive Summary

The Configuration Drift Reports artifact defines automated detection of infrastructure configuration drift from Infrastructure as Code (IaC) definitions using tools like Terraform drift detection, CloudFormation drift detection, Pulumi refresh, and compliance scanning with Checkov, tfsec, and Open Policy Agent (OPA). This artifact identifies manual changes, shadow IT, compliance violations, and security misconfigurations that deviate from approved infrastructure state.

As a critical security and compliance control, configuration drift detection prevents unauthorized changes, ensures infrastructure matches IaC definitions (Terraform state, CloudFormation templates), and maintains compliance with security policies (CIS benchmarks, SOC 2, PCI DSS). Integration with GitOps workflows, policy-as-code, and automated remediation enables infrastructure immutability and continuous compliance.

### Strategic Importance

- **Infrastructure Immutability**: Detects manual infrastructure changes that bypass IaC approval workflows, preventing configuration drift
- **Security Compliance**: Identifies security misconfigurations (open security groups, unencrypted storage, public S3 buckets) violating policies
- **Cost Control**: Detects unauthorized resource creation, oversized instances, and shadow IT that increases costs
- **Audit Readiness**: Provides compliance evidence for SOC 2, ISO 27001, PCI DSS audits with drift detection reports
- **Change Accountability**: Tracks who made changes, when, and whether through approved IaC pipelines or manual console access
- **Automated Remediation**: Enables automatic drift correction, policy enforcement, and infrastructure self-healing

## Purpose & Scope

### Primary Purpose

This artifact defines automated infrastructure drift detection, compliance policy scanning, and remediation workflows for IaC-managed infrastructure. It establishes drift detection schedules (hourly, daily), compliance policies (CIS benchmarks, custom OPA policies), reporting formats, and automated remediation strategies using Terraform, CloudFormation, Pulumi, and policy-as-code tools.

### Scope

**In Scope**:
- Terraform drift detection: terraform plan -refresh-only, drift detection in Terraform Cloud/Enterprise
- AWS CloudFormation drift detection: detect-stack-drift, describe-stack-resource-drifts APIs
- Pulumi refresh: pulumi refresh, pulumi preview for state comparison
- Compliance scanning: Checkov (Terraform/CloudFormation), tfsec (Terraform), Terrascan, OPA (Open Policy Agent)
- Policy-as-code: Sentinel (HashiCorp), OPA/Rego policies, AWS Config Rules, Azure Policy
- Security baselines: CIS AWS Foundations Benchmark, CIS Azure Benchmark, CIS GCP Benchmark
- Configuration drift types: resource property changes, resource deletions, new unmanaged resources
- Drift reporting: daily/weekly reports, Slack/email notifications, dashboard visualization
- Automated remediation: Terraform apply to correct drift, AWS Config auto-remediation, Azure Policy remediation
- Change tracking: CloudTrail, Azure Activity Log, GCP Cloud Audit Logs for manual change detection
- GitOps enforcement: Ensure infrastructure changes only through Git commits, block console access
- Compliance frameworks: SOC 2, PCI DSS, HIPAA, ISO 27001, FedRAMP compliance requirements

**Out of Scope**:
- Application configuration management (covered in application deployment artifacts)
- Secret rotation and credential management (covered in secrets management)
- Network security policies (covered in network security architecture)
- Kubernetes configuration drift (covered in K8s governance artifacts)
- Database schema drift (covered in database management)
- Incident response for detected drift (covered in incident management runbooks)

### Target Audience

**Primary Audience**:
- Platform Engineers: Configure drift detection, implement policy-as-code, remediate infrastructure drift
- Security Engineers: Define security compliance policies, review drift for violations, enforce security baselines
- DevOps Engineers: Maintain IaC code, investigate drift causes, coordinate drift remediation
- Compliance Officers: Review drift reports for audit compliance, track policy violations, generate compliance evidence

**Secondary Audience**:
- SRE Teams: Monitor infrastructure stability, correlate drift with incidents, prevent manual changes
- Cloud Architects: Design infrastructure immutability patterns, define IaC standards, approve policy exceptions
- IT Audit: Review drift detection logs for compliance audits, validate controls effectiveness
- Engineering Leadership: Review drift trends, approve remediation priorities, enforce IaC-only changes

## Document Information

**Format**: Markdown

**File Pattern**: `*.configuration-drift-reports.md`

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

### Report Overview

**Reporting Period**:
- `reportingPeriod`: Time period covered (e.g., Q2 2024, Jan 2024, etc.)
- `reportDate`: Date report was generated
- `reportType`: Regular | Ad-hoc | Special Investigation | Executive Briefing
- `frequency`: How often this report is generated
- `distribution`: Intended recipients and distribution method

### Executive Summary

**Key Highlights**:
- `criticalFindings`: Top 3-5 most important findings for executive attention
- `trendAnalysis`: Key trends compared to previous periods
- `recommendations`: Priority recommendations requiring executive decision
- `impactAssessment`: Business impact of findings or metrics

### Detailed Analysis

**Metrics & KPIs**:
- `metricName`: Name of each metric or KPI
- `currentValue`: Value for this reporting period
- `targetValue`: Target or goal
- `previousValue`: Value from previous period for trending
- `variance`: Difference from target and trend direction
- `variances`: Explanation of significant variances
- `dataSource`: Where data comes from
- `collectionMethod`: How data is collected and validated

**Analysis by Category**:
- `category`: Grouping for related metrics or findings
- `observations`: What was observed or measured
- `analysis`: Interpretation and meaning
- `rootCauses`: Underlying causes for significant findings
- `impact`: Business or operational impact
- `trends`: Patterns over time
- `comparatives`: Benchmarking against industry or peer data

### Recommendations & Actions

**Priority Actions**:
- `actionId`: Unique identifier
- `actionDescription`: What needs to be done
- `rationale`: Why this action is needed
- `priority`: P0 | P1 | P2 | P3
- `owner`: Who is responsible
- `dueDate`: Target completion date
- `estimatedEffort`: Resource requirement
- `dependencies`: Prerequisites or dependencies
- `successMetrics`: How success will be measured

**Follow-up Items**:
- `openItems`: Items from previous reports still in progress
- `closedItems`: Items completed since last report
- `escalations`: Items requiring escalation to higher authority


## Best Practices

**Daily Drift Detection**: Run terraform plan daily in CI/CD; alert on any detected drift for immediate investigation
**Block Console Access**: Restrict AWS console, Azure portal access to read-only; enforce infrastructure changes only through IaC
**Automated Remediation**: Auto-apply Terraform to correct benign drift; require approval for security-impacting changes
**Policy-as-Code**: Define security policies in OPA, Sentinel, AWS Config Rules; enforce at plan-time before apply
**CIS Compliance**: Scan IaC with Checkov, tfsec against CIS benchmarks; block non-compliant infrastructure in CI/CD
**State Locking**: Use remote state with locking (S3 + DynamoDB, Terraform Cloud) to prevent concurrent modifications
**Change Attribution**: Correlate drift with CloudTrail/activity logs to identify who made manual changes
**Drift Categories**: Classify drift as: benign (tags), concerning (configs), critical (security groups, encryption)
**Notification Routing**: Alert security team for critical drift (security groups, IAM); ops team for resource changes
**Remediation Workflow**: Investigate drift cause, update IaC if intentional, auto-revert if unauthorized
**Compliance Scanning**: Scan for open security groups, unencrypted storage, public S3 buckets, overprivileged IAM
**GitOps Workflow**: All infrastructure changes via Git PR, automated plan on PR, automated apply on merge to main
**Immutable Infrastructure**: Prefer replacing resources over in-place modification; reduces drift surface
**Drift Metrics**: Track drift detection rate, time to remediation, drift by team/service for accountability
**Exception Management**: Document approved drift exceptions (legacy resources, vendor integrations) with expiration
**Pre-Commit Hooks**: Run tfsec, Checkov in pre-commit hooks; catch policy violations before commit
**Regular Audits**: Weekly drift reports to engineering leads; monthly reports to security/compliance teams

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

**Infrastructure as Code (IaC)**:
- Terraform - HashiCorp IaC with HCL, state management, drift detection
- AWS CloudFormation - AWS-native IaC with JSON/YAML templates
- Pulumi - Multi-language IaC (TypeScript, Python, Go, .NET, Java)
- Azure Resource Manager (ARM) Templates - Azure-native IaC
- Google Cloud Deployment Manager - GCP-native IaC
- Ansible - Configuration management and infrastructure provisioning
- CDK (Cloud Development Kit) - AWS CDK, CDK for Terraform programmatic IaC

**Drift Detection Tools**:
- Terraform Cloud/Enterprise - Built-in drift detection with scheduled runs
- Spacelift - Terraform management platform with drift detection
- env0 - IaC management with drift detection and remediation
- Scalr - Terraform automation with drift detection workflows
- Driftctl - Open-source IaC drift detection tool
- CloudQuery - Cloud asset inventory and drift detection

**Compliance Scanning**:
- Checkov - Static analysis for Terraform, CloudFormation, Kubernetes, Dockerfiles
- tfsec - Terraform security scanner with 1000+ checks
- Terrascan - IaC scanner for security and compliance (500+ policies)
- TFLint - Terraform linter for best practices and errors
- Prowler - AWS security assessment and CIS benchmark scanning
- ScoutSuite - Multi-cloud security auditing tool

**Policy-as-Code**:
- Open Policy Agent (OPA) - CNCF policy engine with Rego language
- HashiCorp Sentinel - Policy-as-code for Terraform Enterprise/Cloud
- AWS Config Rules - Managed and custom rules for AWS resource compliance
- Azure Policy - Azure resource compliance and governance
- GCP Policy Intelligence - GCP policy recommendations and enforcement
- Cloud Custodian - Cloud governance with YAML policies (AWS, Azure, GCP)

**Security Baselines**:
- CIS AWS Foundations Benchmark - Security configuration baseline for AWS
- CIS Microsoft Azure Foundations Benchmark - Azure security baseline
- CIS Google Cloud Platform Benchmark - GCP security baseline
- AWS Security Best Practices - Well-Architected Framework security pillar
- Azure Security Benchmark - Microsoft cloud security baseline
- NIST Cybersecurity Framework - NIST CSF compliance mapping

**Change Tracking**:
- AWS CloudTrail - AWS API call logging and change tracking
- Azure Activity Log - Azure resource change and activity logging
- GCP Cloud Audit Logs - GCP admin activity and data access logs
- AWS Config - Resource configuration history and compliance
- Azure Resource Graph - Azure resource queries and change tracking

**GitOps**:
- ArgoCD - Declarative GitOps CD for Kubernetes
- Flux - GitOps toolkit for Kubernetes
- Atlantis - Terraform pull request automation
- Terragrunt - Terraform wrapper with DRY configurations
- GitHub Actions - CI/CD for IaC workflows
- GitLab CI/CD - Integrated CI/CD for infrastructure pipelines

**Compliance Frameworks**:
- SOC 2 - Service Organization Control compliance (change management controls)
- ISO 27001 - Information security management system requirements
- PCI DSS - Payment card industry security standards
- HIPAA - Healthcare data security requirements
- FedRAMP - Federal cloud security compliance
- GDPR - Data protection and privacy compliance

**Remediation Platforms**:
- AWS Systems Manager - Automated remediation with SSM Automation
- Azure Automation - Runbooks for automated remediation
- AWS Lambda - Event-driven remediation functions
- Azure Functions - Serverless remediation automation

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
