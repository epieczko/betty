# Name: network-policies

## Executive Summary

Network Policies are the fundamental security constructs that implement zero-trust networking principles within Kubernetes clusters by defining granular rules for pod-to-pod, pod-to-external, and ingress/egress traffic flow. Built on Kubernetes NetworkPolicy API and extended by CNI plugins like Calico, Cilium, and Antrea, these policies enforce defense-in-depth by implementing microsegmentation, limiting blast radius, and preventing lateral movement in the event of compromise.

In cloud-native security architectures, network policies serve as a critical control layer that complements service mesh security (L7) by providing robust Layer 3/Layer 4 network segmentation. When combined with policy-as-code frameworks (OPA/Gatekeeper, Kyverno), namespace isolation, and continuous compliance monitoring, network policies form the foundation of a comprehensive zero-trust security posture.

### Strategic Importance

- **Zero-Trust Networking**: Implements "deny-by-default" posture requiring explicit allow rules for all traffic flows
- **Lateral Movement Prevention**: Limits attacker movement by restricting pod-to-pod communication across namespace boundaries
- **Blast Radius Reduction**: Isolates compromised workloads to prevent cluster-wide security incidents
- **Compliance Requirements**: Meets regulatory mandates for network segmentation (PCI-DSS, HIPAA, SOC 2)
- **Multi-Tenancy Security**: Enforces tenant isolation in shared Kubernetes clusters through namespace-scoped policies
- **Defense in Depth**: Provides additional security layer complementing service mesh and application-level security
- **Egress Control**: Prevents data exfiltration by restricting outbound traffic to approved destinations

## Purpose & Scope

### Primary Purpose

This artifact defines Layer 3/Layer 4 network segmentation rules that control traffic flow between pods, namespaces, and external networks within Kubernetes clusters. It implements zero-trust networking principles by specifying which workloads can communicate with each other based on labels, namespaces, IP blocks, and ports.

### Scope

**In Scope**:
- Kubernetes NetworkPolicy resources (Ingress and Egress rules)
- Calico NetworkPolicy and GlobalNetworkPolicy for advanced features
- Cilium NetworkPolicy and CiliumClusterwideNetworkPolicy with L7 awareness
- Antrea ClusterNetworkPolicy and NetworkPolicy extensions
- Pod selector-based policies (label-based targeting)
- Namespace selector-based policies (tenant isolation)
- IP block (CIDR) based policies for external traffic control
- Port and protocol specifications (TCP, UDP, SCTP)
- Named ports for protocol-agnostic policies
- Default deny policies (deny all ingress/egress by default)
- Global network policies for cluster-wide rules
- Egress gateway policies for controlled external access
- DNS-based policies (Cilium FQDN-based rules)
- Network policy priorities and ordering
- Policy enforcement modes (audit, enforce)

**Out of Scope**:
- Service mesh L7 traffic management (covered by service-mesh-configurations)
- Application-level authorization logic (handled within applications)
- Cloud provider security groups and firewall rules (managed by infrastructure IaC)
- Web Application Firewall (WAF) rules for HTTP/HTTPS traffic
- DDoS protection and rate limiting (handled at ingress/service mesh layer)

### Target Audience

**Primary Audience**:
- Security Engineers defining zero-trust networking policies
- Platform Engineers implementing network segmentation strategies
- Kubernetes Administrators managing cluster security posture

**Secondary Audience**:
- Compliance Officers auditing network access controls
- SRE Teams troubleshooting connectivity issues
- Application Developers understanding network constraints for their workloads

## Document Information

**Format**: Markdown

**File Pattern**: `*.network-policies.md`

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

**Default Deny All**: Implement default deny-all policies for both ingress and egress as baseline security posture
**Incremental Rollout**: Deploy network policies incrementally, starting with audit mode before enforcement
**Label Standardization**: Establish consistent labeling conventions for pod and namespace selectors across organization
**Namespace Isolation**: Implement namespace-level isolation to prevent cross-tenant traffic by default
**DNS Allowlisting**: Use FQDN-based policies (Cilium) to control egress to specific external domains
**Avoid Wildcards**: Prefer explicit CIDR blocks and selectors over broad wildcard rules
**Policy Testing**: Test policies in non-production before applying to production environments
**Documentation**: Document the business justification for each allow rule with comments and annotations
**Minimal Scope**: Apply principle of least privilege - grant only necessary access for workload functionality
**GitOps Management**: Store policies in Git and deploy via ArgoCD/Flux with peer review required
**Monitoring**: Enable policy logging to detect violations and inform policy refinements
**Regular Audits**: Periodically review policies to remove stale rules and identify over-permissive access
**Named Ports**: Use named ports in policies to make them protocol-agnostic and easier to maintain
**Egress Control**: Explicitly define egress policies to prevent data exfiltration and unauthorized external access
**Multi-Layer Defense**: Combine network policies with service mesh policies for defense in depth
**Policy Validation**: Use OPA/Gatekeeper or Kyverno to validate policy correctness before deployment
**High Availability**: Ensure CNI plugin is highly available to prevent network policy enforcement failures
**Performance Impact**: Monitor CNI plugin performance and resource usage, especially with many policies
**Policy Ordering**: Understand policy precedence and evaluation order in your CNI plugin
**Break Glass Procedures**: Document emergency procedures for temporarily disabling policies during incidents

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

**Kubernetes Network Policy**:
- Kubernetes NetworkPolicy API (networking.k8s.io/v1)
- Pod selectors (matchLabels, matchExpressions)
- Namespace selectors for cross-namespace policies
- IP blocks (CIDR notation) for external traffic
- Port and protocol specifications
- Policy types (Ingress, Egress)
- Default deny all traffic pattern

**CNI Plugins with Network Policy Support**:
- Calico (Project Calico, Tigera Enterprise)
- Cilium (eBPF-based networking and security)
- Antrea (VMware's Kubernetes networking)
- Weave Net (Weaveworks networking)
- Canal (Calico + Flannel)
- Azure CNI with Network Policy
- AWS VPC CNI with Calico

**Calico Extensions**:
- Calico NetworkPolicy (namespaced advanced policies)
- Calico GlobalNetworkPolicy (cluster-wide policies)
- Calico HostEndpoint policies
- Calico policy tiers and priorities
- Calico policy ordering and precedence
- Application Layer Protocol enforcement
- Service account-based policies
- Egress gateway policies

**Cilium Extensions**:
- CiliumNetworkPolicy (L3-L7 policies)
- CiliumClusterwideNetworkPolicy (global policies)
- FQDN-based policies (DNS-aware)
- HTTP/gRPC/Kafka protocol filtering
- TLS SNI-based policies
- Identity-based policies
- Host firewall policies
- Cluster mesh policies (multi-cluster)

**Antrea Extensions**:
- Antrea ClusterNetworkPolicy (cluster-wide)
- Antrea NetworkPolicy tiers
- FQDN-based egress rules
- Layer 7 NetworkPolicy
- Policy logging and statistics

**Zero-Trust Principles**:
- Default deny-all posture
- Least privilege access
- Microsegmentation
- Explicit allow lists
- Defense in depth
- Trust nothing, verify everything

**Policy-as-Code**:
- OPA (Open Policy Agent) for NetworkPolicy validation
- Gatekeeper constraint templates
- Kyverno policies for NetworkPolicy enforcement
- Conftest for policy testing
- Policy simulation and dry-run testing

**Network Security Standards**:
- PCI-DSS network segmentation requirements
- HIPAA network access controls
- SOC 2 Type II network security controls
- NIST SP 800-53 AC (Access Control) family
- CIS Kubernetes Benchmark network policies
- MITRE ATT&CK lateral movement prevention

**Multi-Tenancy Patterns**:
- Namespace-based tenant isolation
- Network policy-based namespace isolation
- Hierarchical namespaces with policy inheritance
- Virtual clusters (vCluster) with network isolation

**Observability & Compliance**:
- Network policy logging (Calico, Cilium)
- Flow logs for traffic analysis
- Policy violation detection
- Network topology visualization
- Continuous compliance monitoring
- Policy drift detection

**GitOps Integration**:
- ArgoCD for NetworkPolicy deployment
- Flux for policy management
- Automated policy validation pipelines
- Policy versioning and rollback

**Testing & Validation**:
- Network policy testing tools (netpol-tester, kubectl-np)
- Traffic flow simulation
- Policy conflict detection
- Connectivity testing frameworks

**Reference**: Consult organizational security, platform engineering, and compliance teams for detailed guidance on network policy strategy and implementation

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
