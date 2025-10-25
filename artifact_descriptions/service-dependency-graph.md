# Name: service-dependency-graph

## Executive Summary

The Service Dependency Graph is a visual and machine-readable representation of all service-to-service relationships, API dependencies, database connections, message queue subscriptions, and external system integrations across the microservices ecosystem. This artifact maps synchronous dependencies (REST, GraphQL, gRPC calls), asynchronous dependencies (Kafka topics, RabbitMQ queues, SNS/SQS), shared resources (databases, caches, object storage), and third-party integrations to provide complete visibility into the distributed system topology.

As the foundation for impact analysis, failure domain isolation, and operational resilience, this graph enables change impact assessment, blast radius analysis, and failure propagation modeling using service mesh observability (Istio, Linkerd), distributed tracing (Jaeger, Zipkin, AWS X-Ray), and dependency discovery tools. It supports critical capabilities including deployment planning, circuit breaker configuration, capacity planning, disaster recovery, security zone mapping, and incident response by identifying critical paths, circular dependencies, single points of failure, and cascading failure risks.

### Strategic Importance

- **Impact Analysis**: Enables assessment of change impacts and deployment risk before releases
- **Failure Domain Isolation**: Identifies boundaries for bulkhead isolation to prevent cascading failures
- **Operational Resilience**: Reveals critical paths and single points of failure requiring resilience patterns
- **Capacity Planning**: Shows load distribution and dependencies for scaling decisions
- **Incident Response**: Accelerates root cause analysis by mapping failure propagation paths
- **Security Segmentation**: Supports network policy definition and zero-trust architecture implementation
- **Cost Optimization**: Identifies redundant dependencies and opportunities for consolidation

## Purpose & Scope

### Primary Purpose

This artifact provides comprehensive visibility into service dependencies to support impact analysis, failure domain design, deployment orchestration, and operational troubleshooting. It solves the problem of unknown dependencies in distributed systems by automatically discovering, documenting, and visualizing all service relationships, enabling teams to understand blast radius, identify critical paths, plan deployments, and respond to incidents effectively.

### Scope

**In Scope**:
- Synchronous service dependencies: REST API calls, GraphQL queries, gRPC RPCs, SOAP requests
- Asynchronous messaging dependencies: Kafka topics (producers/consumers), RabbitMQ queues/exchanges, AWS SNS/SQS, Azure Service Bus
- Data dependencies: Database connections, cache dependencies (Redis, Memcached), object storage (S3, Blob)
- External dependencies: Third-party APIs, SaaS integrations, partner systems, legacy systems
- Service mesh topology: Istio/Linkerd service graph, Envoy proxy relationships, mTLS connections
- Dependency metadata: Call volumes, latency percentiles, error rates, timeout configurations, retry policies
- Failure domains: Bulkhead boundaries, circuit breaker groupings, availability zones, regions
- Circular dependencies: Detection and documentation of circular service relationships
- Critical path identification: Services on critical user journeys, single points of failure
- Deployment dependencies: Service deployment order requirements, version compatibility constraints
- Network topology: Service-to-service communication paths, API gateway routing, load balancer configurations
- Discovery mechanisms: Service discovery registries (Consul, Eureka), DNS-based discovery, Kubernetes service discovery

**Out of Scope**:
- Detailed API specifications (covered in Interface Control Documents)
- Infrastructure dependencies (covered in infrastructure architecture)
- Code-level dependencies (covered in software architecture diagrams)
- Team organizational dependencies (covered in team topology documentation)
- Business process dependencies (covered in process maps)

### Target Audience

**Primary Audience**:
- Platform Engineers: Manage service mesh, configure traffic routing, implement resilience patterns
- SRE/DevOps Teams: Assess deployment impact, troubleshoot incidents, plan capacity
- Integration Architects: Design integration patterns, assess coupling, plan refactoring
- Security Engineers: Define network policies, implement zero-trust, assess attack surface

**Secondary Audience**:
- Application Architects: Understand system topology, identify refactoring opportunities
- Technical Leads: Plan feature development considering dependencies
- Release Managers: Sequence deployments based on dependency order
- Incident Commanders: Understand failure propagation during incidents
- CTO/Engineering Directors: Assess architectural complexity and technical debt

## Document Information

**Format**: Multiple

**File Pattern**: `*.service-dependency-graph.*`

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

**Automated Discovery**: Use service mesh (Istio/Linkerd) and distributed tracing (Jaeger/X-Ray) for automatic dependency detection
**Real-Time Updates**: Keep graph current through continuous integration with observability platforms
**Multiple Views**: Provide logical view (service-level), physical view (instance-level), and network view (IP/ports)
**Dependency Metadata**: Capture call volumes, latency, error rates, timeout/retry configs for each dependency
**Failure Domain Mapping**: Group services by failure domain boundaries (AZ, region, team, bounded context)
**Critical Path Highlighting**: Visually emphasize services on critical business paths and user journeys
**Circular Dependency Detection**: Implement automated detection and alerting for circular dependencies
**Blast Radius Analysis**: Calculate potential impact of service failures on downstream consumers
**Deployment Ordering**: Use topological sort to determine safe deployment sequence
**Health Status Integration**: Show real-time service health alongside dependency relationships
**Version Compatibility**: Track service version dependencies and breaking change impacts
**Environment Separation**: Maintain separate graphs for dev, staging, production environments
**External Dependency Flagging**: Clearly mark third-party and external system dependencies
**SLI/SLO Integration**: Overlay SLO status on dependency graph for risk assessment
**Change Impact Tooling**: Provide query capability to assess impact of proposed changes
**Incident Correlation**: Link dependency graph to incident management for faster RCA
**Security Zone Visualization**: Show network security boundaries and service communication policies
**Rate Limiting Visibility**: Display rate limit configurations between service dependencies
**Database Connection Tracking**: Monitor and visualize database connection dependencies and patterns
**Message Queue Topology**: Map Kafka topics, RabbitMQ exchanges, and consumer group relationships

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

**Service Mesh Platforms**:
- Istio (traffic management, observability, security, service graph)
- Linkerd (lightweight service mesh with topology visualization)
- Consul Connect (service mesh with service graph)
- AWS App Mesh (managed service mesh)
- Envoy Proxy (data plane for service mesh, dependency tracking)
- NGINX Service Mesh
- Kuma (universal service mesh)
- Open Service Mesh (OSM)

**Distributed Tracing & Observability**:
- OpenTelemetry (distributed tracing standard, dependency tracking)
- Jaeger (distributed tracing, service dependency graph)
- Zipkin (distributed tracing, dependency map)
- AWS X-Ray (service map and dependency analysis)
- Google Cloud Trace (service dependency visualization)
- Azure Application Insights (application map)
- Datadog APM (service map and dependencies)
- New Relic Service Maps
- Dynatrace Smartscape topology
- Lightstep (distributed tracing and service graph)

**Dependency Discovery Tools**:
- Istio Kiali (service mesh topology visualization)
- Consul Service Graph
- Kubernetes Service Topology
- AWS Service Catalog dependency mapping
- Weave Scope (container and service dependencies)
- Netflix Vizceral (traffic flow visualization)
- Spinnaker dependency resolution
- Backstage Software Catalog (dependency tracking)

**API Gateway Observability**:
- Kong Vitals (API dependency tracking)
- Apigee Analytics (API call graphs)
- AWS API Gateway metrics and logging
- Azure API Management analytics
- Tyk Analytics Dashboard
- GraphQL schema introspection and query analysis

**Graph Databases & Visualization**:
- Neo4j (graph database for dependency storage)
- Amazon Neptune (graph database service)
- Azure Cosmos DB (Gremlin API)
- D3.js for dependency graph visualization
- Cytoscape.js for network visualization
- Graphviz for directed graphs
- Gephi for network analysis

**Service Discovery Platforms**:
- Consul (service discovery and health checking)
- Eureka (Netflix service discovery)
- etcd (distributed key-value store for discovery)
- Apache Zookeeper
- Kubernetes Service Discovery (DNS, endpoints)
- AWS Cloud Map (service discovery)
- Azure Service Fabric Naming Service

**Failure Domain Patterns**:
- Bulkhead pattern for failure isolation
- Circuit Breaker pattern (Hystrix, Resilience4j, Polly)
- Failure domain design principles
- Blast radius reduction strategies
- Cascading failure prevention
- Service level isolation
- Availability zone isolation
- Regional failover strategies

**Dependency Analysis Patterns**:
- Critical Path Method (CPM) for deployment sequencing
- Directed Acyclic Graph (DAG) analysis for build/deploy ordering
- Cycle detection algorithms for circular dependencies
- Breadth-First Search (BFS) for dependency traversal
- Topological sorting for deployment order
- Strongly Connected Components (SCC) for circular dependency detection
- PageRank algorithm for service criticality ranking

**Chaos Engineering Tools**:
- Chaos Monkey (Netflix failure injection)
- Gremlin (chaos engineering platform)
- Chaos Mesh (Kubernetes chaos experiments)
- Litmus (chaos engineering for Kubernetes)
- Pumba (Docker chaos testing)
- Failure injection testing guided by dependency graph

**Network Topology & Security**:
- Kubernetes Network Policies
- Istio Authorization Policies
- Calico network policies
- Cilium (eBPF-based networking and security)
- Zero Trust Architecture (service-to-service authentication)
- mTLS (mutual TLS) for service communication
- Service-to-service authentication and authorization

**APM & Monitoring Platforms**:
- Prometheus (metrics and service discovery)
- Grafana (dependency graph visualization)
- Datadog (service dependency map)
- New Relic (service maps and dependencies)
- AppDynamics (flow maps)
- Elastic APM (service maps)
- Splunk (service dependency tracking)

**Infrastructure as Code**:
- Terraform dependency graphs
- Pulumi resource dependencies
- CloudFormation resource dependencies
- Kubernetes resource dependencies (Helm charts)
- Service dependency declarations in manifests

**Deployment & Orchestration**:
- Kubernetes Deployment dependencies
- Helm chart dependencies
- Spinnaker pipeline dependencies
- ArgoCD application dependencies
- Flux GitOps dependency ordering
- Jenkins pipeline dependency management

**Architecture Visualization**:
- C4 Model (Context, Container, Component, Code diagrams)
- PlantUML for architecture diagrams
- Mermaid.js for dependency graphs
- Structurizr for architecture modeling
- draw.io / diagrams.net for manual diagrams
- CloudCraft for cloud architecture diagrams

**Standards & Best Practices**:
- TOGAF dependency management
- ArchiMate dependency relationships
- AWS Well-Architected Framework (reliability pillar)
- Google SRE Book (dependency management)
- Site Reliability Engineering principles
- Microservices dependency management patterns
- Conway's Law implications for dependencies

**Message Brokers & Event Streaming**:
- Apache Kafka (topic dependency tracking, consumer groups)
- RabbitMQ (exchange and queue topology)
- AWS SNS/SQS (pub/sub and queue dependencies)
- Azure Event Hubs (event stream dependencies)
- Google Cloud Pub/Sub
- Redis Streams and Pub/Sub
- NATS messaging topology

**API & Contract Management**:
- OpenAPI specifications for API dependencies
- GraphQL schema stitching and federation
- gRPC service dependencies via Protobuf
- Consumer-Driven Contracts (Pact) for dependency validation
- AsyncAPI for event-driven dependencies

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
