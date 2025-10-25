# Name: component-diagrams

## Executive Summary

Component Diagrams are detailed technical artifacts that visualize the internal structure, interfaces, dependencies, and relationships of software components within a system or service. Using UML 2.5 Component Diagrams, C4 Model Component level diagrams, or ArchiMate application components, these diagrams show how software elements are organized, how they communicate, and what external dependencies they rely upon.

As essential tools for detailed design communication, component diagrams bridge high-level architecture and implementation by showing package structures, API contracts, interface specifications, and dependency graphs. They support development teams in understanding module boundaries, guide refactoring decisions, enable dependency analysis, and facilitate microservices decomposition following Domain-Driven Design principles and bounded context patterns.

### Strategic Importance

- **Design Communication**: Provides developers with clear understanding of component structure, responsibilities, and interfaces using industry-standard UML 2.5 or C4 notation
- **Dependency Management**: Enables analysis of coupling, cohesion, and circular dependencies to improve modularity and testability
- **Refactoring Support**: Guides architectural refactoring, microservices decomposition, and technical debt reduction initiatives
- **Onboarding Efficiency**: Accelerates new developer onboarding by visualizing codebase structure and component relationships
- **Code Quality**: Supports architecture compliance checking using tools like ArchUnit, SonarQube architecture rules, or NDepend

## Purpose & Scope

### Primary Purpose

This artifact documents detailed component structure using UML 2.5 Component Diagrams, C4 Model Level 3 (Component) diagrams, or package diagrams showing modules, libraries, interfaces, and dependencies. Created using tools like PlantUML, Mermaid, Structurizr, Enterprise Architect, or Visual Paradigm, it specifies component responsibilities, provided/required interfaces, and dependency relationships to guide implementation and code organization.

### Scope

**In Scope**:
- Component decomposition: Modules, packages, libraries, services within a container or application boundary
- Interface specifications: Provided interfaces, required interfaces, API contracts (REST, GraphQL, gRPC, message contracts)
- Dependency relationships: Component-to-component dependencies, third-party library dependencies, framework dependencies
- Layer organization: Presentation layer, business logic layer, data access layer, cross-cutting concerns (logging, security, configuration)
- Design patterns: Dependency Injection, Repository pattern, Factory pattern, Strategy pattern, Observer pattern, Adapter pattern
- Port and adapter boundaries: Hexagonal architecture ports, adapters for databases, external services, message queues
- Package structure: Java packages, .NET namespaces, Python modules, Node.js modules, Go packages
- Component interfaces: Interface definitions, API specifications (OpenAPI/Swagger), event schemas (Avro, Protobuf)
- Diagrams-as-code: PlantUML component diagrams, Mermaid component diagrams, Structurizr DSL component definitions

**Out of Scope**:
- High-level system architecture and service boundaries (see Logical Architecture Diagram)
- Physical deployment and infrastructure details (see Physical Architecture Diagram)
- Class-level design and object relationships (see Class Diagrams or detailed design documents)
- Runtime behavior and interaction sequences (see Sequence Diagrams)
- Database schema and entity relationships (see Data Model diagrams)

### Target Audience

**Primary Audience**:
- Software Developers implementing components, understanding dependencies, and following architectural patterns
- Technical Leads designing component structure, defining interfaces, and ensuring separation of concerns
- Development Team Leads establishing coding standards, package organization, and module boundaries

**Secondary Audience**:
- Solution Architects validating that detailed design aligns with high-level architecture decisions and patterns
- Code Reviewers checking compliance with component structure, dependency rules, and layering principles
- DevOps Engineers understanding build dependencies, deployment artifacts, and service packaging requirements

## Document Information

**Format**: Multiple

**File Pattern**: `*.component-diagrams.*`

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

**Diagramming Notations & Standards**:
- UML 2.5 Component Diagrams - Components, interfaces, dependencies, ports, connectors
- C4 Model Level 3: Component Diagrams - Component-level decomposition within containers
- ArchiMate 3.1 Application Layer - Application components and interfaces
- Package Diagrams (UML) - Package structure, package dependencies, import relationships
- Module Diagrams - Language-specific module and namespace visualization

**Diagramming Tools**:
- PlantUML - Text-based UML component diagram generation with version control
- Mermaid - Markdown-based component diagram creation for diagrams-as-code
- Structurizr - C4 Model component diagrams with DSL support
- Enterprise Architect (Sparx Systems) - Full-featured UML modeling with code engineering
- Visual Paradigm - UML, SysML modeling with code generation and reverse engineering
- draw.io / diagrams.net - Visual component diagramming with UML shapes
- Lucidchart - Collaborative component diagram creation with UML templates
- StarUML - Open-source UML modeling tool

**Software Architecture Patterns**:
- Layered Architecture (N-Tier) - Presentation, Business, Data Access layers with dependency rules
- Hexagonal Architecture (Ports and Adapters) - Alistair Cockburn's pattern for testable architecture
- Clean Architecture (Robert C. Martin) - Dependency inversion with concentric circles
- Onion Architecture - Similar to Clean Architecture with domain-centric layers
- Domain-Driven Design (DDD) - Bounded contexts, aggregates, domain services, application services
- Model-View-Controller (MVC) - Separation of concerns for UI applications
- Model-View-ViewModel (MVVM) - UI pattern for data-binding frameworks
- Model-View-Presenter (MVP) - Testable UI pattern with presenter layer

**Design Patterns (Gang of Four)**:
- Creational Patterns - Factory, Abstract Factory, Builder, Singleton, Prototype
- Structural Patterns - Adapter, Bridge, Composite, Decorator, Facade, Proxy
- Behavioral Patterns - Observer, Strategy, Command, Template Method, State, Chain of Responsibility

**Dependency Management Principles**:
- SOLID Principles - Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- Dependency Injection (DI) - Constructor injection, property injection, method injection
- Inversion of Control (IoC) - Frameworks: Spring (Java), .NET Core DI, Dagger (Android), Guice (Java)
- Package Principles (Robert C. Martin) - Cohesion principles (REP, CCP, CRP), Coupling principles (ADP, SDP, SAP)

**Code Organization Standards**:
- Java Package Conventions - Package naming, Maven/Gradle module structure
- .NET Namespace Conventions - Assembly organization, project structure
- Python Module Structure - Packages, __init__.py, setup.py, requirements.txt
- Node.js Module Patterns - CommonJS, ES6 modules, package.json structure
- Go Package Organization - Internal packages, cmd/pkg structure
- Monorepo Structure - Nx, Turborepo, Bazel for multi-project repositories

**API & Interface Specifications**:
- OpenAPI Specification (formerly Swagger) - RESTful API documentation and contracts
- GraphQL Schema Definition Language (SDL) - GraphQL API type definitions
- gRPC / Protocol Buffers - RPC interface definitions with .proto files
- Apache Avro - Data serialization with schema evolution
- AsyncAPI - Event-driven API specifications for message-based systems
- RAML (RESTful API Modeling Language) - API design and documentation

**Architecture Testing & Compliance**:
- ArchUnit - Java architecture unit testing framework for enforcing rules
- NDepend - .NET architecture analysis and dependency visualization
- SonarQube - Code quality with architecture rules and dependency analysis
- Structure101 - Software architecture analysis and dependency management
- JDepend - Java package dependency analyzer
- Degraph - Python dependency graph analyzer

**Build & Dependency Management Tools**:
- Maven - Java build automation with dependency management (pom.xml)
- Gradle - Build automation for Java, Kotlin, Android with Groovy/Kotlin DSL
- npm / Yarn / pnpm - Node.js package management
- NuGet - .NET package manager
- pip / Poetry / Pipenv - Python package management
- Go Modules - Go dependency management
- Cargo - Rust package manager and build system

**Documentation Tools**:
- JavaDoc - Java API documentation generation
- Doxygen - Multi-language documentation generator
- Sphinx - Python documentation with reStructuredText
- JSDoc - JavaScript API documentation
- TSDoc - TypeScript documentation standard
- Swagger UI - Interactive API documentation from OpenAPI specs

**Microservices Decomposition**:
- Domain-Driven Design - Bounded contexts as service boundaries
- Event Storming - Collaborative domain modeling for service identification
- Strangler Fig Pattern - Incremental migration from monolith to microservices
- Database per Service - Microservices data autonomy pattern

**Reference**: Consult software architecture team for detailed guidance on component design patterns, package organization standards, dependency management practices, and architecture testing approaches for your technology stack

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
