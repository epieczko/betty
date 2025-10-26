# Name: reference-architectures

## Executive Summary

Reference Architectures are proven, reusable architecture blueprints that document best-practice patterns, component selections, and design decisions for common solution types. These artifacts leverage industry frameworks (TOGAF, AWS Well-Architected, Azure Architecture Framework) and established patterns (microservices, event-driven, serverless) to accelerate design, reduce risk, and ensure consistency across similar implementations.

As strategic enablers of architecture standardization, reference architectures provide prescriptive guidance combining logical and physical views, technology stack recommendations, integration patterns, and operational considerations. They serve as starting points for solution architects, templates for RFP responses, and benchmarks for architecture reviews, drawing from cloud provider patterns (AWS Solutions Library, Azure Architecture Center, GCP Architecture Framework) and open-source blueprints.

### Strategic Importance

- **Accelerated Delivery**: Reduces design time by providing pre-validated patterns for common scenarios (e-commerce, data lake, API platform, SaaS application)
- **Consistency & Standards**: Ensures alignment with enterprise architecture principles, technology standards, and architectural patterns across teams
- **Risk Reduction**: Incorporates proven patterns, security best practices, and lessons learned to avoid common pitfalls
- **Knowledge Transfer**: Captures and disseminates architectural expertise across organization through documented patterns and rationale
- **Vendor Evaluation**: Provides objective framework for evaluating cloud platforms, products, and services against reference implementations

## Purpose & Scope

### Primary Purpose

This artifact documents reusable architecture patterns for specific solution domains (microservices platforms, data analytics, API management, IoT, SaaS applications) using industry frameworks and cloud provider reference architectures. Created as comprehensive documentation with diagrams (C4, UML, ArchiMate), technology selections, and implementation guidance, it serves as template for new projects and validation baseline for architecture reviews.

### Scope

**In Scope**:
- Solution domain patterns: Microservices platform, event-driven architecture, data lake/warehouse, API management platform, SaaS multi-tenant application, IoT platform, serverless application
- Cloud provider reference architectures: AWS Solutions Library patterns, Azure Architecture Center blueprints, GCP Architecture Framework solutions
- Architecture views: Logical architecture (C4 Container/Component), physical deployment (infrastructure topology), security architecture (zones, controls), data architecture (flows, storage)
- Technology stack recommendations: Recommended services, products, and open-source components with rationale and alternatives
- Design patterns catalog: Integration patterns (REST, GraphQL, messaging, events), data patterns (CQRS, event sourcing, CDC), resilience patterns (circuit breaker, bulkhead, retry)
- Non-functional requirements guidance: Scalability targets, availability SLOs, performance benchmarks, security baselines, cost models
- Implementation blueprints: Infrastructure-as-code templates (Terraform modules, CloudFormation stacks), configuration samples, deployment guides

**Out of Scope**:
- Project-specific customizations and detailed requirements (see Solution Architecture Document)
- Vendor product comparisons and procurement recommendations (see Technology Evaluation)
- Detailed implementation code and application logic (see Technical Design Document)
- Organization-specific policies and governance processes (see Enterprise Architecture Standards)
- Step-by-step deployment procedures (see Deployment Runbooks)

### Target Audience

**Primary Audience**:
- Solution Architects adapting reference architectures to specific project requirements and constraints
- Enterprise Architects establishing and maintaining portfolio of standard patterns across organization
- Technical Leads evaluating architecture approaches and technology stack options for new initiatives

**Secondary Audience**:
- Cloud Architects selecting cloud services and deployment patterns for AWS, Azure, or GCP implementations
- Product Managers understanding technical approach, capabilities, and trade-offs for product features
- Procurement teams using reference architectures as baseline for RFP requirements and vendor evaluations

## Document Information

**Format**: Markdown

**File Pattern**: `*.reference-architectures.md`

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

**Architecture Frameworks**:
- TOGAF 10 ADM - Enterprise architecture methodology and reference models
- Zachman Framework - Multi-perspective enterprise architecture framework
- C4 Model - Context, Container, Component, Code visualization approach
- ArchiMate 3.1 - Enterprise architecture modeling language
- arc42 - Architecture documentation template structure
- ISO/IEC/IEEE 42010 - Systems and software engineering architecture description

**Cloud Provider Reference Architectures**:
- AWS Solutions Library - Pre-built solutions for common use cases (migration, analytics, security, IoT)
- AWS Well-Architected Framework - Five pillars (operational excellence, security, reliability, performance efficiency, cost optimization)
- Azure Architecture Center - Reference architectures for hybrid, multi-cloud, and Azure-native solutions
- Microsoft Cloud Adoption Framework - Guidance for cloud strategy, planning, and governance
- Google Cloud Architecture Framework - Design principles and best practices for GCP
- GCP Solutions Gallery - Reference implementations for data analytics, machine learning, application modernization
- Oracle Cloud Infrastructure Architecture Center - Enterprise patterns and reference architectures
- IBM Cloud Architecture Center - Hybrid cloud and AI/ML reference architectures

**Architecture Pattern Catalogs**:
- Enterprise Integration Patterns (Gregor Hohpe) - 65+ messaging and integration patterns
- Microservices Patterns (Chris Richardson) - Decomposition, data management, communication patterns
- Cloud Design Patterns (Microsoft) - Resiliency, data management, messaging patterns for cloud
- Martin Fowler's Architecture Patterns - Catalog of software architecture and design patterns
- Domain-Driven Design (Eric Evans) - Bounded contexts, aggregates, domain modeling patterns
- Reactive Design Patterns - Patterns for building responsive, resilient, elastic systems

**Solution Domain Patterns**:
- SaaS Architecture Patterns - Multi-tenancy models (silo, bridge, pool), tenant isolation, metering
- Data Lake / Data Warehouse Patterns - Lambda architecture, Kappa architecture, medallion architecture (bronze/silver/gold)
- API Management Patterns - API Gateway, Backend for Frontend (BFF), API composition, GraphQL gateway
- Event-Driven Architecture - Event sourcing, CQRS, saga pattern, event streaming (Kafka, Kinesis)
- Microservices Architecture - Service decomposition, API Gateway, service mesh, distributed tracing
- Serverless Architecture - Function composition, event-driven workflows, Backend-as-a-Service patterns
- IoT Architecture - Device management, telemetry ingestion, edge computing, digital twin patterns

**Technology Evaluation Frameworks**:
- Gartner Magic Quadrant - Vendor capability and market position analysis
- Forrester Wave - Vendor evaluation across functional and strategic criteria
- Technology Radar (ThoughtWorks) - Technology maturity assessment (adopt, trial, assess, hold)
- CNCF Landscape - Cloud-native technology ecosystem and maturity levels
- OSI Model / TCP/IP Model - Network architecture reference models

**Modeling & Diagramming**:
- UML 2.5 - Component, deployment, sequence, class diagrams
- ArchiMate 3.1 - Application, technology, and motivation layer modeling
- BPMN 2.0 - Business process modeling for process-centric architectures
- Lucidchart - Cloud architecture templates and shape libraries
- draw.io / diagrams.net - Open-source diagramming with extensive template library
- Structurizr - C4 Model tooling and workspace management

**Infrastructure & Deployment**:
- Infrastructure-as-Code - Terraform, CloudFormation, ARM Templates, Pulumi for codified infrastructure
- Container Orchestration - Kubernetes architecture patterns, Helm charts, operators
- CI/CD Reference Architectures - GitLab CI/CD, GitHub Actions, Jenkins pipelines, Azure DevOps
- Observability Patterns - Prometheus + Grafana, ELK Stack, distributed tracing (Jaeger, Zipkin)

**Security & Compliance**:
- NIST Cybersecurity Framework - Security by design principles
- Zero Trust Architecture (NIST SP 800-207) - Identity-centric security model
- Cloud Security Alliance (CSA) - Cloud controls matrix and best practices
- OWASP Architecture Guidance - Secure architecture patterns and anti-patterns

**Industry-Specific References**:
- Financial Services - PSD2 reference architectures, open banking patterns, payment processing
- Healthcare - FHIR-based integration, HL7 messaging, patient data platforms
- Retail / E-commerce - Headless commerce, omnichannel, inventory management architectures
- Manufacturing - Industrial IoT, predictive maintenance, digital twin architectures

**Reference**: Consult organizational enterprise architecture team for approved reference architectures, pattern catalogs, and technology selection criteria specific to your organization's strategic direction and technology roadmap

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
