# Name: capability-model

## Executive Summary

The Capability Model is a strategic architecture artifact that defines and organizes business capabilities independent of organizational structure, processes, or technology implementation. This artifact provides a business-oriented view of what an organization does or needs to do, enabling strategic planning, investment prioritization, and architecture alignment across enterprise initiatives.

As a foundational element of enterprise architecture, the Capability Model bridges business strategy and technical implementation by decomposing the organization into its fundamental capabilities. It enables stakeholders to assess capability maturity, identify gaps, prioritize investments, and ensure technology initiatives align with business needs. The model supports portfolio management, vendor selection, business process optimization, and digital transformation efforts.

### Strategic Importance

- **Strategic Planning**: Enables capability-based planning that transcends organizational silos and focuses on business outcomes
- **Investment Optimization**: Provides framework for assessing and prioritizing technology investments based on capability gaps and business value
- **Architecture Alignment**: Ensures technology solutions and initiatives support required business capabilities consistently
- **Portfolio Management**: Enables rationalization of applications and services based on capability coverage and redundancy
- **Transformation Enablement**: Supports business and digital transformation by identifying capability gaps and maturity levels

## Purpose & Scope

### Primary Purpose

This artifact serves as the authoritative catalog and hierarchical organization of business capabilities, defining what the organization does or must do to execute its strategy, independent of how capabilities are implemented or organized. It enables capability-based planning, gap analysis, and investment prioritization across the enterprise.

### Scope

**In Scope**:
- Business capability taxonomy and hierarchical decomposition (Level 1 through Level 3+)
- Capability definitions, descriptions, and business value statements
- Capability maturity assessments and target state definitions
- Mapping of capabilities to business processes, organizational units, and strategic objectives
- Capability heat mapping showing performance, risk, or investment levels
- Technology and application mapping to capabilities
- Capability gap analysis and roadmap priorities
- Cross-capability dependencies and relationships
- Capability ownership and governance assignments
- Industry reference models and benchmarking frameworks
- Capability reusability and standardization opportunities
- Digital capability requirements and transformation priorities
- Capability-based budgeting and cost allocation models
- Customer journey mapping to capabilities
- Regulatory and compliance requirements by capability

**Out of Scope**:
- Detailed process flows and procedures (covered in Business Process Models)
- Specific technology implementation details (covered in Solution Architecture)
- Organizational structure and reporting relationships (covered in Organization Design)
- Individual role definitions and job descriptions (covered in HR documentation)
- Detailed application functionality (covered in Application Portfolios)
- Project plans and implementation timelines (covered in Roadmaps)

### Target Audience

**Primary Audience**:
- Enterprise Architects who use capability models to structure architecture practice and align solutions
- Business Architects who leverage capabilities for business transformation and process optimization
- Strategy Teams who utilize capability assessments for strategic planning and investment decisions
- Portfolio Managers who map applications and initiatives to capabilities for rationalization
- Product Owners who define product scope and features based on capability coverage

**Secondary Audience**:
- Business Unit Leaders who assess capability maturity and prioritize improvement investments
- Solution Architects who ensure solution designs support required business capabilities
- IT Leadership who allocate resources and budgets based on capability priorities
- Transformation Leads who identify capability gaps and define transformation roadmaps
- Procurement Teams who evaluate vendor solutions against capability requirements

## Document Information

**Format**: Markdown

**File Pattern**: `*.capability-model.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal (may contain strategic business information)

**Retention**: 7 years minimum (strategic planning artifact with long-term reference value)


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

### Specification Overview

**Specification Purpose**:
- `specificationGoal`: What this specification is defining
- `userStories`: User needs being addressed
- `requirements`: High-level requirements this spec satisfies
- `designPrinciples`: Guiding principles for this specification
- `constraints`: Technical, business, or regulatory constraints

### Technical Specification

**System Components**:
- `componentName`: Name of each system component
- `componentType`: Service | Library | Integration | Data Store | UI Component
- `purpose`: Why this component exists
- `responsibilities`: What this component is responsible for
- `interfaces`: How other components interact with it
- `dependencies`: What this component depends on
- `dataModel`: Data structures used or managed
- `apiEndpoints`: API endpoints exposed (if applicable)

**Functional Requirements**:
- `requirementId`: Unique identifier (e.g., FR-001)
- `requirement`: Detailed requirement statement
- `acceptance Criteria`: How requirement is verified
- `priority`: Must Have | Should Have | Could Have | Won't Have
- `complexity`: Estimation of implementation complexity
- `risks`: Risks associated with this requirement

**Non-Functional Requirements**:
- `performance`: Response time, throughput, capacity targets
- `scalability`: How system scales with load or data volume
- `availability`: Uptime requirements and SLAs
- `reliability`: Error rates, MTBF, MTTR targets
- `security`: Authentication, authorization, encryption requirements
- `compliance`: Regulatory or policy requirements
- `usability`: User experience and accessibility requirements
- `maintainability`: Code quality, documentation, testing standards
- `portability`: Platform independence or migration requirements

### Design Details

**Architecture**:
- `architecturePattern`: Microservices | Monolith | Serverless | Event-Driven
- `componentDiagram`: Visual representation of components and relationships
- `dataFlow`: How data moves through the system
- `integrationPoints`: External system integrations
- `deploymentModel`: How components are deployed and distributed

**Data Model**:
- `entities`: Core data entities
- `relationships`: How entities relate to each other
- `constraints`: Data validation and business rules
- `indexes`: Performance optimization through indexing
- `archival`: Data retention and archival strategy

**Security Design**:
- `authenticationMechanism`: How users/services authenticate
- `authorizationModel`: RBAC | ABAC | ACL approach
- `dataProtection`: Encryption at rest and in transit
- `auditLogging`: What is logged for security audit
- `threatModel`: Key threats and mitigations

### Implementation Guidance

**Development Standards**:
- `codingStandards`: Language-specific coding standards to follow
- `testingRequirements`: Unit test coverage, integration tests required
- `documentationRequirements`: Code comments, API docs, README
- `versionControl`: Branching strategy and commit conventions
- `codeReview`: Review process and criteria

**Quality Gates**:
- `buildRequirements`: Must compile without errors/warnings
- `testRequirements`: All tests must pass, minimum coverage %
- `securityRequirements`: No high/critical vulnerabilities
- `performanceRequirements`: Must meet performance SLAs
- `accessibilityRequirements`: WCAG 2.1 AA compliance (if applicable)


## Best Practices

**Hierarchical Decomposition**: Structure capabilities in 3-4 levels maximum; Level 1 should be strategic, Level 2 operational, Level 3 tactical for manageability
**Business Language**: Use business terminology, not IT jargon; capabilities should be understandable to business stakeholders without technical translation
**Stable Taxonomy**: Design capabilities to be relatively stable over time; they represent what organization does, not how it does it
**Outcome Focused**: Define capabilities based on business outcomes and value delivered, not organizational structure or technology used
**Comprehensive Coverage**: Ensure capability model covers all aspects of business operation including support functions, not just customer-facing capabilities
**Industry Alignment**: Leverage industry reference models (APQC, TM Forum, etc.) as starting point to accelerate development and enable benchmarking
**Unique Capabilities**: Ensure each capability is distinct with no overlap; decompose ambiguous capabilities to clarify scope
**Maturity Assessment**: Conduct regular capability maturity assessments using consistent criteria (people, process, technology, data)
**Heat Mapping**: Use visual heat maps to show capability performance, risk, or investment priority for executive communication
**Application Mapping**: Map all applications to capabilities they support to identify redundancy and rationalization opportunities
**Governance Model**: Establish clear capability ownership with accountable business leaders, not just IT stewards
**Strategic Alignment**: Link capabilities to strategic objectives to prioritize investment and demonstrate business value
**Gap Analysis**: Conduct systematic gap analysis between current and target state capabilities to drive roadmap
**Investment Planning**: Use capability model as basis for portfolio planning, budgeting, and investment prioritization
**Vendor Evaluation**: Use capability requirements as criteria for evaluating vendor solutions and service providers
**Change Impact**: Assess impact of business or technology changes across affected capabilities to manage dependencies
**Documentation Standards**: Maintain consistent structure for capability definitions including name, description, value, KPIs, and relationships
**Stakeholder Engagement**: Involve business leaders in capability definition and validation to ensure buy-in and accuracy
**Regular Reviews**: Review and update capability model quarterly or when significant business changes occur
**Cross-Functional**: Ensure capability model represents enterprise view, not siloed business unit perspectives
**Digital Integration**: Explicitly identify digital capabilities required for transformation initiatives and customer experience
**Metrics Definition**: Define clear KPIs and metrics for each capability to enable performance measurement and benchmarking
**Reusability Focus**: Identify shared capabilities that should be standardized across organization to improve efficiency

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

**Enterprise Architecture Frameworks**:
- TOGAF Business Architecture (Business Capability Framework)
- Zachman Framework (Business Function perspective)
- Federal Enterprise Architecture Framework (FEAF) Business Reference Model
- DoDAF/MODAF Capability Views
- ArchiMate Business Layer (Business Function)
- Gartner Enterprise Architecture Framework
- The Open Group IT4IT Reference Architecture
- APQC Process Classification Framework
- Business Capability Modeling (BCM) standards
- Business Model Canvas (BMC) for capability-strategy alignment

**Industry Reference Models**:
- TM Forum Business Process Framework (eTOM) for telecommunications
- BIAN (Banking Industry Architecture Network) for financial services
- ACORD (Association for Cooperative Operations Research) for insurance
- HL7 FHIR (Fast Healthcare Interoperability Resources) for healthcare
- SCOR (Supply Chain Operations Reference) for supply chain
- ITIL Service Capability Model for IT service management
- CMMI (Capability Maturity Model Integration) for process maturity
- Supply Chain Council Reference Models
- Retail Industry Leaders Association (RILA) frameworks
- Energy Industry Process Association (EIPA) models

**Business Architecture Standards**:
- Business Architecture Guild BIZBOK Guide
- Object Management Group (OMG) Business Architecture standards
- IEEE 1471 Architecture Description standard
- ISO/IEC/IEEE 42010 Architecture description standard
- VDML (Value Delivery Modeling Language) by OMG
- BMM (Business Motivation Model) by OMG
- Business Process Model and Notation (BPMN) 2.0
- Decision Model and Notation (DMN)
- Case Management Model and Notation (CMMN)
- Value Stream Mapping standards

**Strategic Planning Frameworks**:
- Balanced Scorecard for strategy-capability alignment
- OKR (Objectives and Key Results) framework
- Porter's Value Chain Analysis
- McKinsey 7S Framework
- Ansoff Matrix for growth strategies
- Blue Ocean Strategy frameworks
- Lean Canvas for business model design
- Wardley Mapping for capability evolution
- Business Model Generation frameworks
- Strategic Capability Planning methods

**Maturity Assessment Models**:
- CMMI for capability maturity assessment
- Gartner Capability Maturity Models
- Forrester Capability Assessment frameworks
- MIT Center for Information Systems Research (CISR) maturity models
- Digital Maturity Assessment frameworks
- Technology Business Management (TBM) maturity models
- Cloud Maturity Assessment frameworks
- Data Management Maturity (DMM) Model
- Analytics Maturity Models
- DevOps Maturity Models

**Governance Standards**:
- COBIT (Control Objectives for Information and Related Technologies)
- ISO/IEC 38500 IT Governance standard
- ITIL (Information Technology Infrastructure Library)
- Val IT Framework for value governance
- Risk IT Framework
- ISO 31000 Risk Management
- Enterprise Risk Management (ERM) frameworks
- Portfolio, Program, and Project Management (P3M3)
- PRINCE2 for project governance
- PMI Portfolio Management Standard

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Business Strategy and Strategic Plans
- Value Stream Maps and Customer Journeys
- Business Process Models and documentation
- Organizational Structure and operating model
- Current State Application Portfolio
- Technology Stack and platform inventory
- Industry reference models and benchmarks
- Regulatory and compliance requirements
- Customer and market research insights
- Financial and budgeting frameworks

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Application Portfolio Rationalization initiatives
- Solution Architecture and technology selection
- Business Process Optimization programs
- IT Investment and Portfolio Planning
- Enterprise Architecture Roadmaps
- Vendor Selection and RFP processes
- Business Case Development
- Operating Model Design
- Organization Design and restructuring
- Technology Strategy and innovation planning

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Business Architecture (overall business design)
- Application Portfolio (technology supporting capabilities)
- Technology Roadmap (evolution of capability enablement)
- Value Stream Maps (capability flow to deliver value)
- Operating Model (how capabilities are organized and delivered)
- Business Process Models (how capabilities are executed)
- Data Architecture (information supporting capabilities)
- Organization Charts (who owns and operates capabilities)

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: Architecture board review for standards compliance
5. **Business Review**: Business unit leaders validate capability definitions and priorities
6. **Strategy Review**: Strategy team confirms alignment with strategic objectives
7. **Final Approval**: Chief Architect and business sponsor provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: Chief Enterprise Architect or VP Architecture
- Secondary Approver: Chief Strategy Officer or Business Unit Leaders
- Governance Approval: Architecture Review Board

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly for maturity assessments; Annual for comprehensive model review

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur (mergers, acquisitions, divestitures)
- New strategic initiatives launched requiring capability expansion
- Major process transformations impact capability definitions
- Regulatory requirements create new capability needs
- Industry reference models update with relevant changes

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring of capability taxonomy or fundamental redefinition
- **MINOR**: New capabilities added, capability decomposition refined, major maturity changes
- **PATCH**: Corrections to definitions, minor clarifications, metadata updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: 7 years minimum (strategic planning artifact)

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Chief Enterprise Architect or Head of Business Architecture

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates with business stakeholders
- Manage review and approval process
- Facilitate capability maturity assessments
- Support strategic planning and investment decisions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/capability-model-template.md`

**Alternative Formats**: Excel workbook for capability inventory, PowerPoint for heat maps

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/capability-model-example-*.md`

**Annotated Guidance**: See annotated examples showing best practices and common approaches

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified and engaged business unit leaders and process owners
- [ ] Gathered industry reference models for benchmarking
- [ ] Obtained access to strategic plans and business objectives
- [ ] Reviewed current application portfolio and technology inventory
- [ ] Allocated sufficient time for stakeholder workshops
- [ ] Identified Architecture Review Board members
- [ ] Understood applicable industry standards and frameworks

While creating this artifact:

- [ ] Following approved template structure
- [ ] Conducting stakeholder workshops for capability identification
- [ ] Writing capability descriptions in business language
- [ ] Validating with industry reference models
- [ ] Mapping capabilities to applications and processes
- [ ] Conducting maturity assessments with consistent criteria
- [ ] Creating visual heat maps for executive communication
- [ ] Seeking input from business and IT stakeholders

Before submitting for approval:

- [ ] Completed all required sections with 3-4 level hierarchy
- [ ] Verified capability definitions with business leaders
- [ ] Obtained peer review from architecture team
- [ ] Validated alignment with strategic objectives
- [ ] Addressed all review comments and feedback
- [ ] Created supporting visualizations and heat maps
- [ ] Completed all metadata fields
- [ ] Verified compliance with EA standards
- [ ] Ready for Architecture Review Board approval

## Governance & Compliance

### Regulatory Considerations

- SOC 2: Capability model supports control environment documentation
- ISO 27001: Information security capabilities documented in model
- Industry-Specific: Financial services, healthcare, telecom have specific capability requirements
- Data Privacy: Capabilities handling personal data clearly identified

### Audit Requirements

This artifact may be subject to:

- Internal audits for strategic planning processes
- External audits for governance and control frameworks
- Architecture compliance reviews
- Strategic planning assessments

**Audit Preparation**:
- Maintain complete version history showing capability evolution
- Document all approvals with evidence of stakeholder validation
- Keep change log current with business justification
- Ensure accessibility for auditors with appropriate classifications

### Policy Alignment

This artifact must align with:

- Enterprise Architecture Policy and standards
- Strategic Planning and investment policies
- IT Governance and portfolio management policies
- Vendor Management and procurement policies
- Change Management and organizational design policies

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: All business domains covered with 3-4 level decomposition
- **Stakeholder Validation**: 90%+ business leaders validate capability definitions
- **Application Coverage**: 95%+ applications mapped to supporting capabilities
- **Update Currency**: Model reviewed and updated quarterly

### Usage Metrics

- **Strategic Alignment**: Number of initiatives mapped to capability gaps
- **Investment Planning**: Percentage of IT budget allocated using capability priorities
- **Portfolio Decisions**: Number of application rationalization decisions driven by capability analysis
- **Benchmarking**: Maturity scores compared against industry references

### Continuous Improvement

- Gather feedback from strategy and portfolio planning sessions
- Track capability gaps identified and addressed over time
- Measure time-to-decision improvement for architecture choices
- Update taxonomy based on industry evolution and business changes
- Share capability assessment insights across organization

## Metadata Tags

**Phase**: Architecture & Design

**Category**: Business Architecture

**Typical Producers**: Enterprise Architects, Business Architects, Strategy Teams

**Typical Consumers**: Business Leaders, Solution Architects, Portfolio Managers, Product Owners

**Effort Estimate**: 4-8 weeks for initial development; 2-4 days per quarterly update

**Complexity Level**: High (requires deep business understanding and stakeholder engagement)

**Business Criticality**: Mission Critical (foundational for strategy and investment decisions)

**Change Frequency**: Regular (quarterly maturity updates, annual comprehensive review)

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: Architecture & Design - Version 2.0*
