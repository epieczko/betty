# Name: network-topology-diagram

## Executive Summary

The Network Topology Diagram artifact provides visual representations of cloud and on-premises network architecture, documenting the logical and physical layout of network infrastructure including VPCs/VNets, subnets, availability zones, regions, routing tables, security boundaries, connectivity patterns, and data flow paths. This artifact establishes comprehensive network architecture diagrams using industry-standard tools (Lucidchart, Draw.io, Visio, CloudCraft, Diagrams.net) to communicate complex network designs to technical and non-technical stakeholders, support security assessments, enable compliance audits (PCI DSS network segmentation, HIPAA data flow), and facilitate incident response and disaster recovery planning.

As a foundational documentation artifact for cloud infrastructure and security architecture, this artifact serves Network Engineers designing network segmentation strategies, Cloud Platform Engineers implementing multi-tier VPC architectures, Security Engineers conducting threat modeling and security assessments, Compliance Officers validating regulatory requirements, and Enterprise Architects communicating infrastructure designs to leadership. It addresses critical architectural patterns including DMZ isolation, multi-tier application segmentation, hub-and-spoke topologies, transit gateway architectures, Zero Trust network boundaries, and hybrid cloud connectivity (Direct Connect, ExpressRoute, Cloud Interconnect).

### Strategic Importance

- **Governance Excellence**: Demonstrates rigorous program management and adherence to organizational standards
- **Risk Mitigation**: Early identification of patterns and trends enables proactive intervention
- **Audit Readiness**: Provides comprehensive trail for internal and external audits
- **Knowledge Capture**: Preserves institutional knowledge beyond individual personnel tenure
- **Continuous Improvement**: Enables data-driven process improvements through trend analysis

## Purpose & Scope

### Primary Purpose

This artifact visually documents network architecture to communicate infrastructure design decisions, support security assessments and threat modeling, demonstrate compliance with network segmentation requirements (PCI DSS, HIPAA, Zero Trust), enable rapid incident response by providing clear data flow documentation, and serve as authoritative reference for network changes and disaster recovery planning.

### Scope

**In Scope**:
- Cloud network architecture (AWS VPC, Azure VNet, GCP VPC, multi-cloud topologies)
- Network segmentation and trust zones (public DMZ, private app tier, data tier, management network)
- Availability zones, regions, and multi-region architectures
- Subnets (public, private, database, management, transit) and CIDR ranges
- Routing tables, internet gateways, NAT gateways, and route propagation
- Security boundaries (security groups, network ACLs, firewalls, WAF)
- Load balancers (ALB, NLB, Application Gateway, Cloud Load Balancing)
- VPN connections (site-to-site VPN, client VPN, OpenVPN, WireGuard)
- Hybrid connectivity (AWS Direct Connect, Azure ExpressRoute, GCP Cloud Interconnect)
- Transit gateways and hub-and-spoke topologies
- Peering connections (VPC peering, VNet peering, VPC Network Peering)
- DNS architecture (Route 53, Azure DNS, Cloud DNS, private hosted zones)
- CDN and edge locations (CloudFront, Akamai, Cloudflare, Azure Front Door)
- Data flow paths (client → CDN → WAF → ALB → application → database)
- Egress points and internet connectivity patterns
- Kubernetes cluster networking (CNI, pod networks, service networks, ingress)
- Service mesh architecture (Istio, Linkerd, control plane, data plane)
- Network monitoring and logging collection points

**Out of Scope**:
- Detailed firewall rule specifications (covered by firewall-rules artifact)
- Load balancer configuration details (covered by load-balancer-configurations)
- Application architecture and microservices design (covered by application architecture artifacts)
- Detailed security group rules (covered by firewall-rules)

### Target Audience

**Primary Audience**:
- Network Engineers designing and implementing network architecture
- Cloud Platform Engineers building cloud infrastructure
- Security Engineers conducting security assessments and threat modeling
- Compliance Officers validating network segmentation requirements
- Enterprise Architects communicating infrastructure to leadership

**Secondary Audience**:
- DevOps Engineers understanding deployment environments
- Site Reliability Engineers troubleshooting connectivity issues
- Incident Response Teams investigating security incidents
- Auditors validating compliance controls

## Document Information

**Format**: Multiple

**File Pattern**: `*.network-topology-diagram.*`

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

**Version Control**: Store diagrams in Git alongside infrastructure-as-code, use semantic versioning, maintain diagram source files (.drawio, .vsdx)
**Multiple View Levels**: Create high-level overview for executives, detailed technical diagrams for engineers, security-focused views for assessments
**Consistent Iconography**: Use official cloud provider icons (AWS Architecture Icons, Azure Icons, GCP Icons) for consistency
**Color Coding**: Use consistent color scheme for trust zones (red=public DMZ, yellow=private app, green=data tier, blue=management)
**Layered Approach**: Separate logical (VPC, subnets, routing) from physical (regions, AZs) to avoid cluttering single diagram
**Data Flow Annotations**: Show traffic flow with directional arrows, label protocols and ports (HTTPS:443, SSH:22)
**CIDR Notation**: Document subnet CIDR ranges and IP addressing schemes for each network segment
**Security Boundaries**: Clearly delineate security group boundaries, firewall inspection points, and trust zone transitions
**Naming Consistency**: Use consistent naming for resources matching actual infrastructure (prod-vpc-us-east-1, web-subnet-1a)
**Legend and Key**: Include legend explaining symbols, colors, line types, and abbreviations
**As-Built Documentation**: Maintain accurate as-built diagrams reflecting current production state, update within 48 hours of changes
**Change Tracking**: Document diagram version, last update date, and change description in diagram metadata
**Tool Selection**: Use diagram-as-code tools (Diagrams Python library, Terraform Graph) for automated diagram generation from IaC
**Accessibility**: Export diagrams as PNG, PDF, and SVG formats for broad accessibility across teams
**Compliance Focus**: Highlight PCI DSS cardholder data environment, HIPAA protected zones, and compliance boundaries
**Incident Response**: Include emergency contact information, escalation paths, and critical system dependencies
**Disaster Recovery**: Show failover paths, backup connectivity, and multi-region disaster recovery architecture
**Zoom Levels**: Design diagrams to be readable when printed on standard paper and when zoomed in for detail
**Network Addressing**: Document IP address allocation, reserved ranges, and DHCP/static assignment patterns
**Load Balancer Placement**: Show load balancer positioning, health check paths, and backend target distribution
**Egress Patterns**: Document all internet egress points (NAT gateways, internet gateways) and outbound filtering
**Hybrid Connectivity**: Clearly show on-premises connections, Direct Connect/ExpressRoute circuits, and VPN tunnels
**Kubernetes Overlay**: For container platforms, show pod networks, service networks, CNI plugin topology
**Regular Updates**: Update diagrams immediately after infrastructure changes, review quarterly for accuracy
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

**Network Architecture Standards**:
- OSI Model (7-Layer Network Model)
- TCP/IP Protocol Suite Standards
- IEEE 802.1Q VLAN Standards
- IEEE 802.3 Ethernet Standards
- RFC 1918 (Private Address Space)
- RFC 4632 (CIDR Notation)

**Cloud Platform Standards**:
- AWS Well-Architected Framework (Reliability, Security Pillars)
- AWS VPC Architecture Best Practices
- Azure Virtual Network Best Practices
- Google Cloud VPC Network Design
- Multi-Cloud Networking Patterns

**Network Segmentation**:
- PCI DSS 4.0 (Requirement 1 - Network Segmentation)
- NIST SP 800-53 (SC-7 Boundary Protection)
- Zero Trust Architecture (NIST SP 800-207)
- Micro-Segmentation Patterns
- DMZ Architecture Best Practices

**Diagram Standards & Notation**:
- UML Deployment Diagrams
- C4 Model for Software Architecture
- ArchiMate Network Notation
- AWS Architecture Icons
- Azure Architecture Icons
- GCP Architecture Diagramming Tool
- Cisco Network Topology Icons

**Compliance & Regulatory**:
- PCI DSS Network Segmentation Guidance
- HIPAA Security Rule (Network Security Requirements)
- SOC 2 Type II (Network Architecture Documentation)
- FedRAMP Network Architecture Requirements
- ISO/IEC 27001:2022 (A.13.1 Network Security Management)
- CMMC Level 2/3 (Network Segmentation Requirements)

**Routing & Connectivity**:
- BGP (Border Gateway Protocol) RFC 4271
- OSPF (Open Shortest Path First) RFC 2328
- Static Routing Best Practices
- Route Propagation Patterns
- Multi-Exit Discriminator (MED) for Path Selection

**Hybrid Cloud Connectivity**:
- AWS Direct Connect Architecture
- Azure ExpressRoute Reference Architecture
- Google Cloud Interconnect Patterns
- SD-WAN Architecture Patterns
- MPLS Network Design

**VPN Standards**:
- IPsec (RFC 4301, ESP, AH)
- WireGuard Protocol
- OpenVPN Best Practices
- Site-to-Site VPN Architecture
- Client VPN Design Patterns

**Load Balancing Architecture**:
- Global Server Load Balancing (GSLB)
- DNS-Based Load Balancing
- Layer 4 vs Layer 7 Load Balancing
- Multi-Region Load Balancing
- Cross-AZ Load Distribution

**CDN Architecture**:
- CDN Edge Location Distribution
- Origin Shield Architecture
- Multi-CDN Failover Patterns
- Edge Computing Topologies

**Kubernetes Networking**:
- Kubernetes Network Model
- Container Network Interface (CNI) Plugins
- Calico, Cilium, Flannel, Weave Net Architecture
- Service Mesh Topology (Istio, Linkerd)
- Ingress Controller Patterns

**DNS Architecture**:
- DNS Hierarchy and Resolution
- Split-Horizon DNS
- Private Hosted Zones
- DNS Failover Patterns
- DNSSEC Implementation

**Security Architecture**:
- Defense in Depth Network Design
- Trust Zone Boundaries
- Bastion Host Placement
- Jump Box Architecture
- Security Group Chaining

**High Availability Patterns**:
- Multi-AZ Architecture
- Multi-Region Active-Active
- Multi-Region Active-Passive
- Disaster Recovery Network Design
- Regional Failover Patterns

**Transit Gateway Architecture**:
- AWS Transit Gateway Hub-and-Spoke
- Azure Virtual WAN Topology
- GCP Network Connectivity Center
- Centralized Egress Architecture

**Network Monitoring**:
- VPC Flow Logs Architecture
- Network Tap Placement
- SPAN/Mirror Port Configuration
- NetFlow/sFlow Collection Points

**Diagramming Tools**:
- Lucidchart for Network Diagrams
- Draw.io/Diagrams.net
- Microsoft Visio Network Templates
- CloudCraft for AWS Architecture
- AWS Architecture Diagrams
- Azure Architecture Center Diagrams

**Documentation Standards**:
- Network Documentation Best Practices
- Change Management Documentation
- As-Built vs As-Designed Documentation
- Version Control for Diagrams

**Industry Best Practices**:
- SANS Network Architecture Best Practices
- Cloud Architecture Patterns (AWS, Azure, GCP)
- Network Design for Cloud Native Applications
- CNCF Networking Patterns

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
