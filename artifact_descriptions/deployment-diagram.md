# Name: deployment-diagram

## Executive Summary

The Deployment Diagram (UML Deployment Diagram) illustrates the physical infrastructure topology showing how software artifacts are deployed onto hardware nodes, including servers, containers, virtual machines, and cloud services. This runtime view artifact, aligned with the 4+1 View Model's Physical View and C4 Model supplementary diagrams, documents the production deployment architecture essential for infrastructure provisioning, capacity planning, and disaster recovery.

The deployment diagram shows infrastructure nodes (physical servers, VMs, containers, serverless functions), deployment artifacts (applications, services, databases, message brokers), network topology (availability zones, regions, VPCs, subnets), container orchestration (Kubernetes clusters, ECS tasks, Docker Swarm), load balancing and auto-scaling configurations, and high availability patterns (active-active, active-passive, multi-region). Tools like PlantUML, Structurizr, draw.io, or cloud-specific tools (AWS Architecture Diagrams, Azure Icons, GCP Diagrams) create these diagrams following UML 2.5 deployment diagram notation or cloud architecture diagram standards.

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

This artifact documents runtime deployment architecture enabling infrastructure teams to provision environments, operations teams to understand system topology, and architects to design for high availability, disaster recovery, and scalability. It supports capacity planning, cost estimation, security zone definition, and infrastructure-as-code implementation.

### Scope

**In Scope**:
- Infrastructure nodes: physical servers, virtual machines, containers, serverless functions, managed services
- Deployment environments: production, staging, QA, development with environment-specific configurations
- Container orchestration: Kubernetes clusters with namespaces, pods, deployments, services; ECS tasks; Docker Swarm services
- Network topology: VPCs, subnets, availability zones, regions, CDN edge locations
- Load balancers: application load balancers, network load balancers, reverse proxies (NGINX, HAProxy)
- Auto-scaling: horizontal pod autoscaling (Kubernetes), EC2 auto-scaling groups, Azure VM scale sets
- High availability patterns: active-active, active-passive, multi-AZ, multi-region deployment
- Disaster recovery: backup regions, replication topology, failover mechanisms
- Database deployment: primary-replica, read replicas, database clustering, sharding topology
- Message broker deployment: Kafka clusters, RabbitMQ nodes, managed services (SQS, Kinesis, Event Hubs)
- Cache deployment: Redis clusters, Memcached nodes, CDN caching layers
- Monitoring infrastructure: Prometheus, Grafana, Datadog agents, CloudWatch, Application Insights
- Security zones: DMZ, application tier, data tier, management network
- Network communication: ports, protocols, firewall rules, security groups, network policies
- Cloud services: managed databases (RDS, CosmosDB, Cloud SQL), object storage (S3, Blob, GCS), managed Kubernetes (EKS, AKS, GKE)
- Infrastructure as Code: Terraform, CloudFormation, ARM templates, Pulumi mapping to deployment artifacts
- Deployment artifacts: Docker images, JAR/WAR files, executables, static assets

**Out of Scope**:
- Application logic and business rules (covered in component diagrams)
- Code-level details (covered in code artifacts)
- Data models and schemas (covered in data architecture)
- Detailed API specifications (covered in API documentation)
- Business processes (covered in business process models)
- Development tooling and CI/CD pipelines (covered in DevOps documentation)

### Target Audience

**Primary Audience**:
- Infrastructure Engineers: provision and configure deployment environments following diagram specifications
- Platform Engineers: design and maintain Kubernetes clusters, container orchestration, and cloud infrastructure
- Site Reliability Engineers (SRE): understand system topology for monitoring, alerting, and incident response
- DevOps Engineers: implement infrastructure-as-code matching deployment architecture

**Secondary Audience**:
- Enterprise Architects: validate infrastructure alignment with enterprise standards and cloud strategy
- Solution Architects: design deployment topology for high availability and disaster recovery
- Technical Architects: specify infrastructure requirements for applications and services
- Architecture Review Board (ARB) Members: evaluate infrastructure architecture and cloud resource usage
- Security Architects: assess network segmentation, security zones, and attack surface
- Cost Management: estimate infrastructure costs and identify optimization opportunities

## Document Information

**Format**: Multiple

**File Pattern**: `*.deployment-diagram.*`

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

**Environment-Specific Diagrams**: Create separate diagrams for production, staging, QA environments; production may have multi-region while lower environments single-region
**Multi-AZ for HA**: Deploy across multiple availability zones within region for high availability; show redundant components across AZs
**Cloud-Native Icons**: Use official AWS, Azure, GCP icons for cloud services; maintain visual consistency with cloud provider documentation
**Node Specifications**: Annotate nodes with instance types (t3.large), container specs (CPU: 2, Memory: 4Gi), or serverless configurations
**Network Details**: Document VPC/subnet CIDR blocks, security group rules, network ACLs, routing tables for complete network picture
**Scaling Configuration**: Show auto-scaling groups with min/max instances, horizontal pod autoscaler targets (CPU: 70%, Memory: 80%)
**Load Balancer Details**: Specify load balancer type (ALB, NLB), listener ports, health check configuration, SSL/TLS termination
**Database Topology**: Show primary-replica relationships, read replicas, backup strategies, cross-region replication for databases
**Kubernetes Detail**: Document namespaces, pod counts, resource requests/limits, persistent volume claims, ingress controllers
**Security Zones**: Visually distinguish DMZ, application tier, data tier using colors or grouping; show firewall boundaries
**Disaster Recovery**: Show both primary and DR regions; indicate replication mechanisms, failover processes, RTO/RPO targets
**CDN Configuration**: Include CDN edge locations, origin servers, caching policies for global content delivery
**Infrastructure as Code**: Link diagram elements to IaC modules (Terraform modules, CloudFormation templates) for traceability
**Cost Annotations**: Optionally annotate expensive resources (large instances, managed services) for cost awareness
**Monitoring Coverage**: Show monitoring agents, log collectors, metrics exporters deployed across infrastructure
**Secrets Management**: Document where secrets are stored (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) and how accessed
**Service Mesh**: If using Istio/Linkerd, show control plane components, data plane sidecars, mesh boundaries
**Update Frequency**: Refresh diagram when infrastructure changes; maintain in Git alongside infrastructure-as-code for synchronization
**Validation with IaC**: Ensure diagram matches actual deployed infrastructure; use IaC state files as source of truth
**Capacity Planning**: Use diagram to identify scaling bottlenecks, single points of failure, and capacity constraints
**Disaster Recovery Testing**: Reference diagram during DR drills to validate failover procedures and recovery processes

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

**UML Deployment Diagrams**:
- UML 2.5 Deployment Diagrams - nodes (devices, execution environments), artifacts (deployable units), associations
- UML Notation - 3D boxes for nodes, rectangles for artifacts, communication paths between nodes
- Execution Environment Nodes - application servers, web servers, database servers, container runtime
- Device Nodes - physical hardware, virtual machines, cloud instances
- Deployment Specifications - configuration parameters, environment variables, resource limits

**Architecture Views**:
- 4+1 View Model Physical View (Kruchten) - mapping software to hardware, deployment topology
- C4 Model Deployment Diagrams - supplementary diagrams showing container-to-infrastructure mapping
- ArchiMate Technology Layer - infrastructure elements, system software, communication paths
- TOGAF Technology Architecture - hardware, network, infrastructure services

**Container Orchestration**:
- Kubernetes Architecture - control plane (API server, scheduler, controller manager), worker nodes, pods, services
- Kubernetes Deployment Patterns - DaemonSets, StatefulSets, Deployments, Jobs, CronJobs
- Docker Swarm - manager nodes, worker nodes, services, tasks, overlay networks
- Amazon ECS - clusters, task definitions, services, tasks, Fargate vs. EC2 launch types
- Azure Container Instances - container groups, resource allocation, networking
- Google Cloud Run - serverless containers, traffic splitting, revisions

**Cloud Architecture**:
- AWS Well-Architected Framework - reliability pillar (multi-AZ, auto-scaling, backup/restore)
- AWS Reference Architectures - multi-tier web apps, serverless, microservices, data lakes
- Azure Well-Architected Framework - reliability pillar (availability zones, regions, disaster recovery)
- Google Cloud Architecture Framework - reliability and scalability patterns
- Multi-Cloud Architecture - deploying across AWS, Azure, GCP for redundancy and vendor flexibility

**High Availability Patterns**:
- Active-Active Deployment - multiple active instances serving traffic simultaneously
- Active-Passive Deployment - primary instance active, standby instances for failover
- Multi-AZ Deployment - distributing across availability zones within region
- Multi-Region Deployment - distributing across geographic regions for disaster recovery
- Blue-Green Deployment - parallel environments for zero-downtime deployment
- Canary Deployment - gradual traffic shift to new version

**Load Balancing**:
- Layer 4 Load Balancing - network load balancers (TCP/UDP), AWS NLB, Azure Load Balancer
- Layer 7 Load Balancing - application load balancers (HTTP/HTTPS), AWS ALB, Azure Application Gateway
- Global Load Balancing - AWS Route 53, Azure Traffic Manager, GCP Cloud Load Balancing
- Service Mesh Load Balancing - Istio, Linkerd, Consul Connect for east-west traffic
- Reverse Proxy - NGINX, HAProxy, Envoy for traffic management and SSL termination

**Auto-Scaling**:
- Horizontal Pod Autoscaler (Kubernetes) - scaling based on CPU, memory, custom metrics
- Vertical Pod Autoscaler (Kubernetes) - adjusting resource requests/limits
- Cluster Autoscaler (Kubernetes) - adding/removing nodes based on pending pods
- EC2 Auto Scaling - scaling groups, scaling policies, target tracking, scheduled scaling
- Azure VM Scale Sets - automatic scaling based on metrics, schedule, manual
- Cloud Functions Auto-Scaling - AWS Lambda, Azure Functions, Google Cloud Functions concurrent execution

**Database Deployment**:
- Primary-Replica Replication - PostgreSQL streaming replication, MySQL replication, MongoDB replica sets
- Multi-Primary Replication - active-active database clusters for write scalability
- Read Replicas - Amazon RDS read replicas, Azure SQL read-only replicas
- Database Sharding - horizontal partitioning across multiple database instances
- Managed Database Services - RDS, Aurora, CosmosDB, Cloud SQL, Cloud Spanner

**Network Architecture**:
- VPC/VNet Design - subnets, route tables, internet gateways, NAT gateways
- Security Groups / Network Security Groups - instance-level firewall rules
- Network ACLs - subnet-level firewall rules
- Service Mesh - Istio, Linkerd for service-to-service communication, mTLS, traffic management
- API Gateway - AWS API Gateway, Azure API Management, Kong, Apigee for API routing

**Infrastructure as Code**:
- Terraform - provider-agnostic IaC with state management and modules
- AWS CloudFormation - AWS-native IaC with stack management
- Azure Resource Manager (ARM) Templates - Azure-native IaC
- Google Cloud Deployment Manager - GCP-native IaC
- Pulumi - modern IaC with general-purpose programming languages
- Ansible - configuration management and orchestration
- Chef/Puppet - configuration management for server provisioning

**Disaster Recovery**:
- Recovery Time Objective (RTO) - acceptable downtime duration
- Recovery Point Objective (RPO) - acceptable data loss duration
- Backup and Restore - regular backups with tested restore procedures
- Pilot Light - minimal version running in DR region, scaled up during failover
- Warm Standby - scaled-down version running in DR region
- Multi-Site Active-Active - full deployment in multiple regions

**Security Architecture**:
- Network Segmentation - DMZ, application tier, data tier, management network
- Zero Trust Network - micro-segmentation, mTLS, identity-based access
- Bastion Hosts - jump servers for secure access to private networks
- VPN Connectivity - site-to-site VPN, client VPN for hybrid cloud
- Private Link / PrivateLink - private connectivity to cloud services
- Web Application Firewall (WAF) - AWS WAF, Azure WAF, Cloudflare for application protection

**Monitoring & Observability**:
- Prometheus - metrics collection and alerting for Kubernetes and containers
- Grafana - metrics visualization and dashboards
- ELK Stack - Elasticsearch, Logstash, Kibana for log aggregation and analysis
- Datadog - unified monitoring, metrics, traces, logs
- New Relic - application performance monitoring
- CloudWatch, Azure Monitor, Google Cloud Monitoring - cloud-native monitoring

**Diagram Tools**:
- PlantUML - text-based UML deployment diagrams with deployment and node notation
- Structurizr - deployment diagrams linked to container diagrams
- draw.io - visual diagramming with AWS, Azure, GCP icon libraries
- Lucidchart - collaborative diagramming with cloud architecture templates
- Cloudcraft - AWS architecture diagrams with cost estimation
- Visual Paradigm - UML deployment diagrams with infrastructure modeling

**Cloud Diagram Standards**:
- AWS Architecture Icons - official AWS service icons for architecture diagrams
- Azure Icons - official Azure service icons and patterns
- Google Cloud Icons - official GCP service icons
- CNCF Landscape Icons - Cloud Native Computing Foundation project icons
- Kubernetes Icons - official Kubernetes component icons

**Quality Attributes**:
- ISO 25010 Reliability - availability, fault tolerance, recoverability
- ISO 25010 Performance Efficiency - time behavior, resource utilization, capacity
- Scalability Patterns - horizontal scaling, vertical scaling, auto-scaling
- Resilience Patterns - circuit breakers, bulkheads, retry policies, timeout policies

**Reference**: Consult organizational infrastructure team for deployment standards, cloud architecture patterns, Kubernetes configuration standards, and infrastructure-as-code practices

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
