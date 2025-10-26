# Cost Tagging Policy

> **See also**: `artifact_descriptions/cost-tagging-policy.md` for complete guidance

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Author** | Author Name |
| **Owner** | Owner Name/Role |
| **Classification** | Internal |

## Executive Summary

<!-- Provide a 2-3 paragraph overview for executive audience -->
<!-- What is this document about and why does it matter? -->

## Purpose

<!-- This policy defines the mandatory tagging standards for all cloud and SaaS resources to enable accurate cost allocation, financial accountability, and FinOps optimization. It establishes required tags... -->

## Scope

### In Scope

- AWS resource tagging (EC2, S3, RDS, Lambda, ECS, EKS resources, CloudFormation stacks)
- Azure resource tagging (VMs, Storage, SQL, AKS, resource groups)
- GCP resource tagging (Compute Engine, Cloud Storage, BigQuery, GKE)
- Kubernetes resource labeling (namespaces, deployments, services, pods, PVCs)
- SaaS cost allocation tags (Snowflake resource tags, Databricks cost tags, Datadog tags)

### Out of Scope

- Items explicitly not covered by this artifact

## Target Audience

### Primary Audience

- FinOps Teams: Enforce tagging policy, generate chargeback reports, monitor compliance
- Cloud Platform Engineers: Implement tag enforcement (SCPs, policies), provide tagging tooling
- Infrastructure Engineers/SREs: Tag resources correctly, remediate non-compliant resources

### Secondary Audience

- Additional stakeholders who may reference this document

## [Main Section 1]

<!-- Complete this section with artifact-specific content -->
<!-- Refer to the artifact description for required structure -->

## [Main Section 2]

<!-- Add additional sections as needed -->

## Best Practices

**Mandatory Tag Keys**: Define 5-8 mandatory tags (CostCenter, Environment, Team, Application, Owner, Project, DataClassification); enforce at resource creation

**Environment Tag Standards**: Use standardized values (prod, staging, dev, test, sandbox); avoid custom values like "production-new" or "dev-temp"

**CostCenter Format**: Use numeric cost center codes (e.g., 10234) or department codes (eng-platform, data-analytics); avoid free-form text

**Team Ownership**: Assign every resource to a specific team; use email distribution lists or Slack channels for contact

**Tag Inheritance**: Leverage resource group tags (Azure), CloudFormation stack tags (AWS), namespace labels (Kubernetes) to reduce manual tagging

## Quality Checklist

Before finalizing this artifact, verify:

- [ ] **Completeness**: All required sections present and adequately detailed
- [ ] **Accuracy**: Information verified and validated by appropriate subject matter experts
- [ ] **Clarity**: Written in clear, unambiguous language appropriate for intended audience
- [ ] **Consistency**: Aligns with organizational standards, templates, and related artifacts
- [ ] **Currency**: Based on current information; outdated content removed or updated

## Related Documents

- [Related Artifact]: Description and relationship

## Approvals

| Role | Name | Date | Status |
|------|------|------|--------|
| Approver | Name | YYYY-MM-DD | Pending |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |
