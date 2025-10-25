# Name: team-topology-map

## Executive Summary

The Team Topology Map is a strategic organizational design artifact that visualizes team structures, boundaries, and interaction modes based on Team Topologies principles. This living document maps the four fundamental team types (stream-aligned, enabling, platform, and complicated-subsystem teams) and defines how teams interact through collaboration, X-as-a-Service, and facilitation modes.

Built on Conway's Law—that organizations design systems mirroring their communication structures—this artifact enables intentional organizational design through the Inverse Conway Maneuver. It supports the creation of autonomous, loosely-coupled teams with clear ownership boundaries, interaction patterns, and cognitive load management, using visual tools like Miro, Mural, or LucidChart to create shared understanding across Engineering Managers, Product Leaders, and organizational stakeholders.

### Strategic Importance

- **Organizational Design**: Implements Team Topologies principles for fast flow and reduced cognitive load
- **Conway's Law Alignment**: Deliberately structures teams to produce desired software architectures
- **Interaction Clarity**: Defines collaboration, X-as-a-Service, and facilitation patterns between teams
- **Cognitive Load Management**: Ensures teams have appropriate scope and complexity boundaries
- **Autonomous Delivery**: Enables stream-aligned teams to deliver value independently with minimal handoffs
- **Scaling Patterns**: Supports Spotify Model (squads/tribes), two-pizza teams, and other scaling frameworks

## Purpose & Scope

### Primary Purpose

This artifact visualizes organizational team structure using Team Topologies principles to enable fast flow, reduce cognitive load, and optimize for autonomous delivery. It maps the four fundamental team types, their boundaries, dependencies, and interaction modes to support deliberate organizational design and continuous evolution.

### Scope

**In Scope**:
- Four fundamental team types: Stream-aligned, Enabling, Platform, Complicated-subsystem teams
- Three team interaction modes: Collaboration, X-as-a-Service, Facilitation
- Team APIs and boundaries defining what each team owns and provides
- Cognitive load assessment and team sizing (typically 5-9 people per team, two-pizza rule)
- Inter-team dependencies and communication patterns
- Team missions, domain ownership, and service boundaries
- Evolution timeline showing team topology changes over time
- Platform team capabilities and service catalogs

**Out of Scope**:
- Individual role definitions and org chart hierarchies (see ownership-charters)
- Detailed RACI matrices per workstream (see raci-per-workstream)
- Individual skill assessments (see skills-matrix)
- Time allocation and capacity planning (see time-allocation-worksheets)
- Initiative-level governance (see initiative-charter)

### Target Audience

**Primary Audience**:
- Engineering Managers and Directors designing team structures and reporting lines
- VP Engineering and CTOs making organizational design decisions
- Organizational Designers implementing Team Topologies and scaling frameworks
- Platform Engineering Leaders defining platform team boundaries and capabilities

**Secondary Audience**:
- Product Leaders understanding team ownership and product decomposition
- HR/People Teams supporting organizational changes and headcount planning
- Team Leads understanding their team's position in the broader ecosystem
- Architecture teams aligning system architecture with team structure

## Document Information

**Format**: Multiple

**File Pattern**: `*.team-topology-map.*`

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

**Team Topology Design Principles**:
- **Cognitive Load Limits**: Ensure each team owns a manageable domain (typically 1-3 bounded contexts or services)
- **Stream-Aligned Default**: Organize most teams around value streams for fast flow
- **Minimize Handoffs**: Design topologies to reduce dependencies and coordination overhead
- **Clear Team APIs**: Define explicit contracts for how teams interact with each other
- **Right-Sized Platform**: Build platform teams only when multiple stream-aligned teams need shared capabilities
- **Enabling Team Strategy**: Use enabling teams temporarily to build capabilities in stream-aligned teams
- **Complicated-Subsystem Sparingly**: Only create for genuinely complex technical domains requiring specialist skills

**Organizational Design Best Practices**:
- **Inverse Conway Maneuver**: Design team structure to produce desired software architecture
- **Two-Pizza Rule**: Keep teams small enough (5-9 people) for effective communication
- **Stable Teams**: Minimize team membership changes; optimize for team longevity and cohesion
- **Domain-Driven Design Alignment**: Align team boundaries with bounded contexts
- **Product Thinking**: Frame platform capabilities as products with internal customers
- **Sensing Mechanisms**: Regularly assess team cognitive load, flow metrics, and dependencies

**Interaction Mode Guidance**:
- **Collaboration Mode**: Use temporarily for discovering boundaries or building new capabilities (time-boxed)
- **X-as-a-Service Mode**: Use for stable, well-defined interfaces with clear service levels
- **Facilitation Mode**: Use enabling teams to help stream-aligned teams adopt new practices
- **Avoid Permanent Collaboration**: Drives cognitive load up; should evolve to X-as-a-Service
- **Document Interaction Contracts**: Make team APIs explicit and discoverable

**Visualization and Communication**:
- **Visual-First Approach**: Use Miro, Mural, or LucidChart for collaborative mapping sessions
- **Color Coding**: Distinguish team types visually (e.g., stream-aligned=blue, platform=green)
- **Show Evolution**: Capture current state, target state, and transition roadmap
- **Interaction Lines**: Visualize collaboration (thick lines), X-as-a-Service (thin lines), facilitation (dotted)
- **Living Document**: Update topology map as teams evolve and organizational context changes

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use Team Topologies canvas templates and approved organizational templates
**Stakeholder Validation**: Conduct collaborative workshops with Engineering Managers, Product Leaders, and team representatives
**Regular Updates**: Review quarterly or when significant organizational changes occur (acquisitions, major initiatives)
**Change Management**: Communicate topology changes with clear rationale, timeline, and transition support
**Metrics Alignment**: Correlate topology with DORA metrics, flow metrics, and team health indicators

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

**Team Topologies Core Concepts**:
- Four fundamental team types: Stream-aligned, Enabling, Platform, Complicated-subsystem
- Three team interaction modes: Collaboration, X-as-a-Service, Facilitation
- Team API concept: well-defined interfaces for inter-team interaction
- Cognitive load management: Domain, Intrinsic, Extraneous cognitive load
- Team-first architecture: software boundaries aligned with team boundaries
- Fast flow: optimizing for rapid delivery with minimal handoffs
- Thinnest Viable Platform (TVP): right-sized platform capabilities

**Organizational Design Frameworks**:
- Conway's Law: organizations design systems mirroring their communication structure
- Inverse Conway Maneuver: deliberately structure teams to achieve desired architecture
- Spotify Model: Squads, Tribes, Chapters, Guilds organizational pattern
- Two-pizza teams (Amazon): teams sized for 5-9 people for optimal communication
- Matrix organizations: functional vs. product-aligned team structures
- Holocracy and self-organizing team principles
- Sociotechnical systems design: optimizing both social and technical dimensions

**Team Effectiveness Frameworks**:
- Google's Project Aristotle: psychological safety, dependability, structure & clarity
- DORA State of DevOps: Elite performer organizational characteristics
- Westrum organizational culture typology: Pathological, Bureaucratic, Generative
- Tuckman's stages: Forming, Storming, Norming, Performing
- High-trust culture and accountability frameworks

**Scaling Agile Frameworks**:
- SAFe (Scaled Agile Framework): Agile Release Trains (ARTs), Solution Trains
- LeSS (Large-Scale Scrum): feature teams and area product owners
- Scrum@Scale: Scrum of Scrums coordination pattern
- Nexus Framework: integration team and cross-team coordination
- Flight Levels for portfolio-level agile coordination

**Service Ownership Patterns**:
- DevOps and You Build It You Run It principles
- SRE (Site Reliability Engineering) team structures and responsibilities
- Platform Engineering patterns: Internal Developer Platforms (IDP)
- Service mesh and API gateway ownership models
- Microservices team ownership patterns

**Visualization and Mapping Tools**:
- Miro: collaborative online whiteboarding for team topology mapping
- Mural: digital workspace for visual collaboration
- LucidChart: diagramming tool for org charts and team structures
- Team Topologies official canvas templates
- Wardley Mapping: strategic context and evolution mapping
- OrgChart: organizational structure visualization
- Value Stream Mapping: identifying flow and bottlenecks

**Dependency and Communication Analysis**:
- Dependency Structure Matrix (DSM): analyzing team interdependencies
- Communication Flow Analysis: measuring collaboration patterns
- Brooks' Law: adding people to late projects makes them later
- Dunbar's Number: cognitive limits on stable relationships (150 people)
- Critical Chain Project Management: managing dependencies
- Network analysis and social network mapping

**Change Management and Evolution**:
- Kotter's 8-Step Change Model for organizational transformation
- ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement)
- McKinsey 7S Framework: strategy, structure, systems alignment
- Prosci Change Management methodology
- Team Topologies evolution patterns and sensing mechanisms

**Related Standards**:
- ISO 9001 (Quality Management): organizational structure and responsibilities
- ITIL 4: Service Value Streams and organizational design
- COBIT: Governance and organizational structures
- PMI Standards: organizational project management maturity

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
