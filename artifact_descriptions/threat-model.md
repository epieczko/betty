# Name: threat-model

## Executive Summary

The Threat Model is a critical security artifact that systematically identifies, analyzes, and prioritizes potential threats to a system, application, or service. Using structured methodologies like STRIDE, PASTA, or attack trees, this artifact enables security teams, architects, and developers to proactively identify vulnerabilities and design appropriate countermeasures before deployment.

As a foundational security engineering deliverable, the threat model bridges the gap between architecture design and security controls implementation. It provides actionable intelligence for security architects who need to design defense-in-depth strategies, developers who must implement secure coding practices, and risk teams who need to understand and communicate the organization's threat landscape to leadership.

### Strategic Importance

- **Proactive Security**: Identifies threats early in the development lifecycle when remediation costs are lowest
- **Risk-Based Prioritization**: Uses frameworks like DREAD or CVSS to prioritize threats by severity and likelihood
- **Regulatory Compliance**: Supports SOC 2, ISO 27001, PCI-DSS, and other frameworks requiring systematic threat analysis
- **Attack Surface Reduction**: Maps entry points, trust boundaries, and data flows to minimize exposure
- **Security Architecture Validation**: Ensures security controls align with identified threats and attack vectors
- **Common Threat Language**: Establishes shared understanding using industry frameworks like MITRE ATT&CK
- **Continuous Security**: Enables threat model updates as systems evolve and new attack patterns emerge

## Purpose & Scope

### Primary Purpose

The Threat Model systematically identifies security threats, attack vectors, and vulnerabilities in a system by analyzing its architecture, data flows, entry points, and trust boundaries. It enables teams to understand "what can go wrong" from an attacker's perspective and prioritize security controls based on realistic threat scenarios and business impact.

### Scope

**In Scope**:
- System architecture decomposition identifying components, data flows, and trust boundaries
- Threat identification using STRIDE, PASTA, or similar methodologies
- Attack vector analysis including threat actors, capabilities, and motivations
- Asset classification and data flow mapping
- Threat prioritization using DREAD, CVSS, or risk matrices
- Security control recommendations mapped to identified threats
- Integration with MITRE ATT&CK framework for common attack patterns

**Out of Scope**:
- Detailed security control implementation (covered in Security Architecture)
- Penetration testing execution (covered in Penetration Testing Report)
- Incident response procedures (covered in Incident Management Plan)
- Compliance audit evidence (covered in Control Test Evidence Packs)
- Code-level vulnerability analysis (covered in Security Test Results)

### Target Audience

**Primary Audience**:
- Security Architects who design defense-in-depth strategies and security controls
- Application Security Engineers who validate security requirements
- Software Developers who implement secure coding practices based on identified threats
- Security Operations teams who configure detection rules for identified attack patterns

**Secondary Audience**:
- Risk Management teams assessing likelihood and impact of security incidents
- Compliance teams demonstrating systematic threat analysis for regulatory frameworks
- Product Managers prioritizing security features based on threat severity
- Executive Leadership understanding the organization's threat landscape and security posture

## Document Information

**Format**: Markdown

**File Pattern**: `*.threat-model.md`

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

**Methodology Selection**: Choose threat modeling methodology based on system type (STRIDE for applications, PASTA for risk-centric analysis, Attack Trees for specific scenarios)
**Early Integration**: Conduct threat modeling during design phase when architecture changes are less costly
**Architecture Decomposition**: Create detailed data flow diagrams (DFDs) showing processes, data stores, data flows, and trust boundaries
**Asset Identification**: Clearly identify and classify assets (data, systems, credentials) by sensitivity and business criticality
**Threat Actor Profiling**: Define realistic threat actors with specific capabilities, motivations, and resources (e.g., nation-state, organized crime, insider, opportunistic)
**STRIDE Coverage**: Systematically apply all STRIDE categories to each trust boundary crossing and data flow
**Attack Tree Development**: Build attack trees for high-value assets showing multiple attack paths and prerequisites
**Prioritization Framework**: Use consistent scoring (DREAD, CVSS, or risk matrix) to prioritize threats objectively
**Control Mapping**: Map each identified threat to existing or proposed security controls (preventive, detective, corrective)
**MITRE ATT&CK Integration**: Reference specific ATT&CK techniques to leverage community threat intelligence
**Collaborative Sessions**: Conduct threat modeling workshops with security, development, and architecture teams
**Tool Support**: Use threat modeling tools (Microsoft Threat Modeling Tool, OWASP Threat Dragon, IriusRisk) for consistency
**Living Document**: Update threat model when architecture changes, new threats emerge, or incidents reveal gaps
**Traceability**: Link threats to security requirements, security controls, and test cases for end-to-end validation

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

**Threat Modeling Methodologies**:
- **STRIDE**: Microsoft's threat classification (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- **PASTA**: Process for Attack Simulation and Threat Analysis (7-stage risk-centric methodology)
- **LINDDUN**: Privacy threat modeling framework complementary to STRIDE
- **Attack Trees**: Hierarchical diagrams representing attack scenarios and paths
- **DREAD**: Risk rating model (Damage, Reproducibility, Exploitability, Affected Users, Discoverability)

**Industry Frameworks**:
- **MITRE ATT&CK**: Knowledge base of adversary tactics, techniques, and procedures (TTPs)
- **OWASP Threat Modeling**: Open-source threat modeling guidance and tools
- **NIST SP 800-30**: Guide for conducting risk assessments
- **ISO 27005**: Information security risk management
- **CVSS**: Common Vulnerability Scoring System for threat severity rating
- **CWE**: Common Weakness Enumeration for categorizing security weaknesses

**Security Architecture**:
- **SABSA**: Sherwood Applied Business Security Architecture
- **NIST Cybersecurity Framework**: Identify, Protect, Detect, Respond, Recover
- **Zero Trust Architecture** (NIST SP 800-207): Never trust, always verify principles

**Reference**: Consult organizational security architecture team for guidance on methodology selection and framework application

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
