# Name: cost-tagging-policy

## Executive Summary

The Cost Tagging Policy establishes mandatory standards for tagging cloud resources (AWS, Azure, GCP) and SaaS applications to enable accurate cost allocation, chargeback/showback, and FinOps optimization. This governance artifact defines required tag keys, allowed values, enforcement mechanisms, and exceptions, ensuring every resource can be attributed to a cost center, team, environment, and business purpose.

Effective cost tagging enables FinOps teams to track cloud spend by team, product, environment (prod/staging/dev), and project using tools like AWS Cost Explorer, Azure Cost Management, GCP Cost Management, CloudHealth, Kubecost, and Datadog Cloud Cost Management. Without consistent tagging, organizations face "unallocated" or "untagged" resource costs that can't be charged back to teams, hindering accountability and optimization efforts. Mature FinOps practices achieve 95%+ tag coverage through automated enforcement (AWS Service Control Policies, Azure Policy, GCP Organization Policy, OPA/Kyverno for Kubernetes).

### Strategic Importance

- **Risk Management**: Mitigates organizational risk through standardized requirements
- **Compliance Assurance**: Ensures adherence to regulatory and legal obligations
- **Consistency**: Drives uniform approach across business units and geographies
- **Accountability**: Establishes clear expectations and consequences
- **Efficiency**: Reduces redundant decision-making through established standards

## Purpose & Scope

### Primary Purpose

This policy defines the mandatory tagging standards for all cloud and SaaS resources to enable accurate cost allocation, financial accountability, and FinOps optimization. It establishes required tags (cost center, environment, team, application), permissible values, tag inheritance rules, enforcement mechanisms (preventive controls, detective monitoring), and the exception approval process. Compliance with this policy ensures every dollar of cloud spend can be attributed to a business owner, enabling data-driven optimization decisions and fair chargeback/showback.

### Scope

**In Scope**:
- AWS resource tagging (EC2, S3, RDS, Lambda, ECS, EKS resources, CloudFormation stacks)
- Azure resource tagging (VMs, Storage, SQL, AKS, resource groups)
- GCP resource tagging (Compute Engine, Cloud Storage, BigQuery, GKE)
- Kubernetes resource labeling (namespaces, deployments, services, pods, PVCs)
- SaaS cost allocation tags (Snowflake resource tags, Databricks cost tags, Datadog tags)
- Required tag keys (CostCenter, Environment, Team, Application, Owner, Project)
- Tag value constraints (allowed values, naming conventions, case sensitivity)
- Tag inheritance (resource groups, CloudFormation stacks, Kubernetes namespaces)
- Enforcement mechanisms (AWS SCPs, Azure Policy, GCP Org Policy, OPA/Kyverno)
- Tag coverage monitoring (tag compliance dashboards, untagged resource reports)
- Chargeback/showback processes (monthly cost allocation, team billing reports)
- Exception approval workflow (temporary exceptions, legacy resource handling)
- Tag lifecycle management (tag deprecation, migration procedures)

**Out of Scope**:
- Actual cloud cost optimization recommendations (see FinOps optimization playbooks)
- Budget alerts and forecasting processes (see Cloud Budget Governance)
- Reserved Instance/Savings Plan purchasing (see FinOps Commitment Management)
- Third-party SaaS contract negotiation (see Vendor Management)
- On-premises infrastructure cost allocation (different tagging mechanisms)

### Target Audience

**Primary Audience**:
- FinOps Teams: Enforce tagging policy, generate chargeback reports, monitor compliance
- Cloud Platform Engineers: Implement tag enforcement (SCPs, policies), provide tagging tooling
- Infrastructure Engineers/SREs: Tag resources correctly, remediate non-compliant resources
- Engineering Managers: Ensure team compliance, review team cost allocation reports

**Secondary Audience**:
- Finance Teams: Use tagged cost data for chargeback/showback, budget tracking
- Executives/Leadership: Review cost allocation by business unit, product, environment
- Compliance/Audit: Verify cost allocation controls for SOC 2, ISO 27001
- Product Managers: Understand product-level cloud spending, optimize product economics

## Document Information

**Format**: Markdown

**File Pattern**: `*.cost-tagging-policy.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal

**Retention**: 7 years (financial records retention requirement)


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

**Mandatory Tag Keys**: Define 5-8 mandatory tags (CostCenter, Environment, Team, Application, Owner, Project, DataClassification); enforce at resource creation
**Environment Tag Standards**: Use standardized values (prod, staging, dev, test, sandbox); avoid custom values like "production-new" or "dev-temp"
**CostCenter Format**: Use numeric cost center codes (e.g., 10234) or department codes (eng-platform, data-analytics); avoid free-form text
**Team Ownership**: Assign every resource to a specific team; use email distribution lists or Slack channels for contact
**Tag Inheritance**: Leverage resource group tags (Azure), CloudFormation stack tags (AWS), namespace labels (Kubernetes) to reduce manual tagging
**Preventive Controls**: Use AWS SCPs, Azure Policy (deny mode), GCP Organization Policy Constraints to block resource creation without required tags
**Detective Monitoring**: Run daily tag compliance scans; generate untagged resource reports; notify resource owners for remediation
**Automation**: Use Infrastructure-as-Code (Terraform, Pulumi, CloudFormation) with required tags in modules/templates; auto-tag via AWS Config Rules, Azure Functions
**Tag Coverage Targets**: Aim for 95%+ tag coverage; track monthly trend; executive dashboard visibility
**Chargeback Cadence**: Generate monthly cost allocation reports; distribute to engineering managers and finance teams
**Tag Case Sensitivity**: Define case standards (camelCase, PascalCase, kebab-case); AWS/Azure/GCP handle tags differently
**Tag Key Length Limits**: AWS (127 chars), Azure (512 chars), GCP (63 chars); design tags to fit minimum limits
**Historical Tag Changes**: Track tag modifications in CloudTrail, Azure Activity Log, GCP Cloud Audit Logs; detect tag tampering
**Exception Process**: Require director+ approval for tag exceptions; exceptions expire after 90 days unless renewed
**Legacy Resource Handling**: Phase in tagging for legacy resources over 6-12 months; prioritize high-cost resources first
**Multi-Cloud Consistency**: Use same tag keys across AWS, Azure, GCP; abstract provider-specific differences in tooling
**Kubernetes Label Standards**: Align Kubernetes labels with cloud tags (environment, team, app); use label selectors for cost allocation
**Reserved Tag Prefixes**: Reserve "aws:", "azure:", "gcp:", "k8s:" prefixes for provider-managed tags
**Tag Validation**: Implement tag validation in CI/CD pipelines; fail deployments with missing/invalid tags
**Cost Anomaly Detection**: Correlate tagged spend with anomaly detection; investigate unexpected team/project spend spikes

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

**Cloud Provider Tagging/Labeling**:
- AWS Tags: EC2, S3, RDS, Lambda, CloudFormation, Resource Groups, Tag Editor, Tag Policies (AWS Organizations)
- Azure Tags: Resource tags, resource group tags, subscription tags, management group tags, Azure Policy
- GCP Labels: Resource labels, project labels, billing labels, label restrictions, Organization Policy
- Kubernetes Labels: Pod labels, deployment labels, namespace labels, label selectors, annotations

**FinOps & Cost Management Platforms**:
- AWS Cost Explorer: Tag-based cost allocation, cost allocation tags, cost categories, Savings Plans utilization
- Azure Cost Management + Billing: Cost analysis by tag, budget alerts, cost allocation rules
- GCP Cloud Billing: Label-based cost breakdown, BigQuery billing export, budget alerts
- CloudHealth by VMware: Multi-cloud cost management, tag-based chargeback, policy enforcement
- Kubecost: Kubernetes cost allocation by namespace/label, cluster cost visibility, Prometheus integration
- Datadog Cloud Cost Management: Tag-based spend analysis, container cost allocation, anomaly detection
- Apptio Cloudability: Multi-cloud FinOps, chargeback/showback, rightsizing recommendations
- CloudCheckr: Cost optimization, tag compliance monitoring, reserved instance management
- Spot.io by NetApp: Cloud cost optimization, tag-based governance, commitment management
- Vantage: Cloud cost transparency, tag-based allocation, vendor-neutral platform

**Tag Enforcement & Governance**:
- AWS Service Control Policies (SCPs): Enforce required tags at organization level, deny resource creation without tags
- AWS Config Rules: Detect untagged resources, auto-remediation with Lambda functions, compliance dashboard
- Azure Policy: Enforce tagging at resource group/subscription level, audit mode vs. deny mode, policy initiatives
- GCP Organization Policy Constraints: Enforce label requirements, deny resource creation without labels
- Open Policy Agent (OPA): Policy-as-code for Kubernetes tagging, Rego policies, admission controller
- Kyverno: Kubernetes-native policy engine, mutate policies to auto-add labels, validation policies
- Terraform Sentinel: Policy-as-code for Terraform, enforce tagging in IaC, cost estimation policies
- Pulumi CrossGuard: Policy-as-code for Pulumi, enforce tagging standards, compliance checks

**Infrastructure-as-Code Tagging**:
- Terraform: Default tags (AWS provider), required tags via modules, policy enforcement with Sentinel
- Pulumi: Auto-tagging with transformations, stack tags, policy packs (CrossGuard)
- CloudFormation: Stack-level tags, parameter-driven tags, nested stack tag propagation
- AWS CDK: Aspects for auto-tagging, Tags.of() method, stack-level tags
- Azure Bicep: Tag parameters, resource group tag inheritance
- Google Cloud Deployment Manager: Label templates, Jinja2 templating for labels

**Chargeback/Showback Frameworks**:
- FinOps Foundation: Cloud Financial Management best practices, chargeback/showback principles
- Technology Business Management (TBM): IT cost allocation, service costing, transparency
- ITIL Financial Management: IT service costing, budgeting, accounting
- SAFe (Scaled Agile Framework): Lean budgeting, cost transparency, value stream funding

**Compliance & Audit Standards**:
- SOC 2 Type II: Cost allocation controls, financial reporting accuracy
- ISO 27001: Asset management, resource ownership accountability
- NIST 800-53: Configuration management (CM-8), baseline configuration, asset tracking
- CIS Controls: Hardware/software asset inventory, asset management (Control 1, 2)

**Industry Best Practices**:
- FinOps Foundation: State of FinOps report, tagging best practices, community guidelines
- AWS Well-Architected Framework: Cost Optimization pillar, tagging strategy guidance
- Azure Well-Architected Framework: Cost optimization pillar, tagging and resource organization
- Google Cloud Architecture Framework: Cost optimization, resource labeling strategies
- Gartner FinOps Research: Cloud cost optimization, chargeback maturity models

**Reference**: Consult organizational FinOps team and cloud platform engineering team for detailed guidance on tag enforcement and cost allocation. For governance controls, see Big Five methodology standards for policy enforcement and compliance monitoring.

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Organization chart and cost center hierarchy (Finance)
- Team roster and ownership mapping (HR/Engineering)
- Application/service catalog (CMDB, service registry)
- Environment naming standards (dev, staging, prod definitions)
- Cloud provider account structure (AWS Organizations, Azure Management Groups, GCP Organization)

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- FinOps cost allocation reports and chargeback processes
- Cloud provider billing systems (AWS Cost Allocation Tags, Azure Cost Management)
- Infrastructure-as-Code templates and modules (Terraform, CloudFormation, Pulumi)
- Policy enforcement engines (AWS SCPs, Azure Policy, GCP Organization Policy, OPA)
- Cost optimization tools (CloudHealth, Kubecost, Datadog Cloud Cost)
- Executive dashboards and financial reporting (Power BI, Tableau, Looker)

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Cloud governance policies (security, compliance, operations)
- Infrastructure-as-Code standards and module libraries
- FinOps playbooks (cost optimization, reserved instance management)
- Budget and forecasting processes (monthly/quarterly budget reviews)
- Asset management and CMDB policies (service ownership, configuration items)

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
- Primary Approver: VP of Engineering or Cloud Platform Lead
- Secondary Approver: CFO or Director of Finance (chargeback/showback impact)
- Governance Approval: FinOps Steering Committee or Cloud Governance Board

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review cadence; annual comprehensive policy update

**Event-Triggered Updates**: Update immediately when:
- New cloud provider adopted (multi-cloud expansion)
- Organizational restructuring (new cost centers, team changes)
- New mandatory tags required (compliance, security, data classification)
- Tag enforcement failures (widespread non-compliance)
- Chargeback/showback process changes

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: New mandatory tags, breaking changes to tag keys/values, enforcement policy changes
- **MINOR**: New optional tags, tag value expansions, clarifications
- **PATCH**: Typo corrections, example updates, minor clarifications

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: 7 years (financial records retention requirement)

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Head of FinOps or Cloud Platform Engineering Lead

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/cost-tagging-policy-template.md`

**Alternative Formats**: Policy document (PDF), wiki page (Confluence)

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/cost-tagging-policy-example-aws.md`, `examples/cost-tagging-policy-example-azure.md`

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

- SOC 2: Cost allocation controls demonstrate operational effectiveness
- ISO 27001: Asset management and resource ownership tracking
- GDPR/Privacy: Cost center data may contain organizational information
- Industry-Specific: Financial services may require cost allocation audit trails

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

- Financial policies (budget management, cost allocation)
- Cloud governance policies (security, compliance, operations)
- Asset management policies (CMDB, service ownership)
- Procurement policies (vendor management, contract terms)

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

**Phase**: Operations

**Category**: FinOps Governance

**Typical Producers**: FinOps Team, Cloud Platform Engineering, Finance

**Typical Consumers**: Infrastructure Engineers, Engineering Managers, Finance Teams

**Effort Estimate**: 3-5 days for initial policy creation; 2-4 hours for quarterly updates

**Complexity Level**: Medium

**Business Criticality**: High (enables cost accountability and optimization)

**Change Frequency**: Quarterly review; event-triggered updates

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Operations - Version 2.0*
