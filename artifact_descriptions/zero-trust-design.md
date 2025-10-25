# Name: zero-trust-design

## Executive Summary

Zero Trust Design documents define security architectures based on the principle "never trust, always verify," eliminating implicit trust and requiring continuous verification of every user, device, and network flow. This artifact establishes comprehensive security controls that protect resources regardless of network location through identity-based access, micro-segmentation, least privilege enforcement, and continuous monitoring.

As a strategic security architecture deliverable, Zero Trust design implements NIST SP 800-207 guidelines and industry frameworks using technologies such as identity-aware proxies, software-defined perimeters, network segmentation, endpoint security, and continuous authentication. This approach replaces traditional perimeter-based security with defense-in-depth strategies that verify identity, validate device posture, enforce least privilege access, encrypt all traffic, and continuously monitor for anomalies—protecting against modern threats including insider attacks, lateral movement, and compromised credentials while supporting cloud-native, remote-work, and hybrid infrastructure models.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact serves as the architectural blueprint for implementing Zero Trust security principles across networks, applications, and data. It defines how to eliminate implicit trust, enforce continuous verification, implement micro-segmentation, and establish defense-in-depth controls that protect resources from both external and internal threats regardless of network location.

### Scope

**In Scope**:
- Zero Trust Architecture principles based on NIST SP 800-207
- Identity-based access controls and continuous authentication
- Device trust and endpoint security posture validation
- Network micro-segmentation and Software-Defined Perimeter (SDP)
- Identity-Aware Proxy (IAP) and reverse proxy implementations
- Zero Trust Network Access (ZTNA) for remote access
- Least privilege access enforcement and just-in-time (JIT) permissions
- Encryption of data in transit and at rest (TLS 1.3, mTLS)
- Continuous monitoring and behavioral analytics
- Cloud security posture management (CSPM)
- Service mesh security (Istio, Linkerd) for microservices
- API gateway security and rate limiting
- Data loss prevention (DLP) and data classification
- Assume breach mindset and lateral movement prevention
- Security Information and Event Management (SIEM) integration

**Out of Scope**:
- Specific IAM implementation details (handled by IAM design)
- Application code vulnerabilities (handled by secure SDLC)
- Physical security controls (handled by facilities security)
- Incident response procedures (handled by security operations playbooks)
- Detailed compliance mapping (handled by compliance artifacts)

### Target Audience

**Primary Audience**:
- Security Architects who design Zero Trust architectures and security controls
- Network Security Engineers who implement micro-segmentation and network policies
- Cloud Security Engineers who secure cloud workloads and multi-cloud environments
- Chief Information Security Officers (CISOs) who define security strategy

**Secondary Audience**:
- Platform Engineers who integrate Zero Trust controls into infrastructure
- DevSecOps Engineers who embed security into CI/CD pipelines
- SOC Analysts who monitor Zero Trust telemetry and security events
- Compliance Officers who validate security control effectiveness

## Document Information

**Format**: Markdown

**File Pattern**: `*.zero-trust-design.md`

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

**Zero Trust Frameworks & Standards**:
- NIST SP 800-207 (Zero Trust Architecture)
- NIST Cybersecurity Framework (CSF)
- CISA Zero Trust Maturity Model
- Forrester Zero Trust eXtended (ZTX) framework
- Google BeyondCorp Zero Trust model
- Department of Defense (DoD) Zero Trust Reference Architecture
- UK National Cyber Security Centre (NCSC) Zero Trust principles

**Zero Trust Network Access (ZTNA)**:
- Zscaler Private Access (ZPA)
- Cloudflare Access (Zero Trust network access)
- Palo Alto Networks Prisma Access
- Cisco Duo Beyond (secure access)
- Perimeter 81 (ZTNA platform)
- Twingate (modern VPN alternative)
- Tailscale (WireGuard-based mesh VPN)

**Identity-Aware Proxies & Gateways**:
- Google Cloud Identity-Aware Proxy (IAP)
- Azure AD Application Proxy
- AWS Verified Access
- Cloudflare Access
- Pomerium (open-source identity-aware proxy)
- Ory Oathkeeper (cloud-native proxy)

**Network Micro-Segmentation**:
- VMware NSX (software-defined networking)
- Illumio (adaptive security platform)
- Guardicore Centra (breach prevention)
- Cisco ACI (Application Centric Infrastructure)
- HashiCorp Consul (service mesh and segmentation)
- Akamai Guardicore Segmentation

**Service Mesh Security**:
- Istio (mTLS, traffic encryption, policy enforcement)
- Linkerd (lightweight service mesh)
- Consul Connect (HashiCorp service mesh)
- AWS App Mesh
- Azure Service Fabric

**Endpoint Security & Device Trust**:
- CrowdStrike Falcon (endpoint detection and response)
- Microsoft Defender for Endpoint
- SentinelOne (autonomous endpoint protection)
- Carbon Black (VMware endpoint security)
- Jamf (macOS/iOS device management)
- Intune (Microsoft endpoint management)
- Device posture attestation and compliance validation

**Secure Web Gateways (SWG)**:
- Zscaler Internet Access (ZIA)
- Cisco Umbrella
- Netskope (cloud security platform)
- Palo Alto Networks Prisma Access
- Cloudflare Gateway

**Data Security & Classification**:
- Microsoft Purview (data governance and DLP)
- Varonis (data security platform)
- Forcepoint DLP (data loss prevention)
- Digital Guardian (data protection)
- Nightfall AI (cloud DLP)

**Encryption & Certificate Management**:
- TLS 1.3 (Transport Layer Security)
- mTLS (Mutual TLS authentication)
- Let's Encrypt/cert-manager (automated certificates)
- HashiCorp Vault (secrets and PKI management)
- AWS Certificate Manager (ACM)

**Security Monitoring & Analytics**:
- Splunk (SIEM and security analytics)
- Microsoft Sentinel (cloud-native SIEM)
- Datadog Security Monitoring
- Elastic Security
- Sumo Logic (cloud SIEM)
- User and Entity Behavior Analytics (UEBA)

**Cloud Security Posture Management (CSPM)**:
- Wiz (cloud security platform)
- Orca Security (agentless cloud security)
- Prisma Cloud (Palo Alto Networks)
- Lacework (cloud security automation)
- AWS Security Hub
- Azure Defender for Cloud
- Google Security Command Center

**Security Principles**:
- Least Privilege Access
- Defense in Depth
- Assume Breach mindset
- Never Trust, Always Verify
- Verify Explicitly
- Use Least Privileged Access
- Assume Breach

**Compliance & Regulatory**:
- ISO/IEC 27001 (Information Security Management)
- SOC 2 Type II (security controls)
- PCI DSS (network segmentation requirements)
- HIPAA (healthcare security)
- FedRAMP (federal Zero Trust requirements)

**Reference**: Consult organizational security architecture team for approved Zero Trust technologies, implementation roadmap, and maturity model progression

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
