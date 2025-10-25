# Name: promotion-rules

## Executive Summary

The Promotion Rules artifact defines policy-based governance and automated rules for environment promotions, specifying quality gates, approval requirements, security controls, testing thresholds, and compliance validations that must be satisfied before artifacts can progress from development to production environments. This artifact codifies promotion policies as enforceable rules using policy-as-code tools like Open Policy Agent (OPA), Kyverno, or platform-native policy engines.

As organizations implement secure software supply chains and shift-left compliance, this artifact serves Security Architects defining security gates, Compliance Officers ensuring regulatory requirements, Platform Engineers implementing policy enforcement, and DevOps teams understanding promotion criteria. It transforms subjective promotion decisions into objective, automated rule evaluation with consistent enforcement across all deployments.

### Strategic Importance

- **Policy as Code**: Implements promotion rules using Open Policy Agent (OPA/Rego), Kyverno policies, AWS Config Rules, Azure Policy, or GCP Organization Policy
- **Quality Gates**: Defines enforceable thresholds for test coverage (>80%), vulnerability scanning (no critical/high), code quality scores (SonarQube ratings)
- **Security Controls**: Mandates security scanning results, container image signing, secrets scanning pass, SBOM generation, license compliance
- **Compliance Validation**: Enforces regulatory requirements (SOC 2, PCI DSS, HIPAA), audit logging, data residency, encryption standards
- **Approval Policies**: Specifies who can approve (roles/groups), approval quorum, separation of duties, emergency override procedures
- **Automated Enforcement**: Enables CI/CD pipelines to automatically enforce rules, block non-compliant promotions, provide actionable feedback
- **Exception Management**: Documents exception request process, temporary waivers, compensating controls, exception audit trail

## Purpose & Scope

### Primary Purpose

This artifact codifies promotion governance policies as enforceable rules using policy-as-code, defining quality thresholds, security requirements, compliance validations, and approval criteria that gate environment promotions. It enables automated, consistent policy enforcement across all promotion workflows.

### Scope

**In Scope**:
- Quality rules: Test coverage thresholds (unit >80%, integration >70%), test pass rates (100%), code quality gates (SonarQube A rating)
- Security rules: Vulnerability scanning (no critical/high), container image signing required, secrets scanning pass, SBOM attached
- Compliance rules: Regulatory controls (SOC 2, PCI DSS, HIPAA), data classification validation, encryption enforcement
- Approval rules: Required approvers by environment, approval quorum (2 of 3), separation of duties, time-based windows
- Artifact rules: Semantic versioning compliance, artifact signing, provenance verification, immutability enforcement
- Configuration rules: Environment-specific validation, resource limits, cost guardrails, region restrictions
- Policy enforcement: OPA policies, Kyverno rules, admission controllers, CI/CD gate integration
- Exception handling: Waiver request process, temporary exceptions, compensating controls, audit logging

**Out of Scope**:
- Specific implementation of promotion workflows (covered in Promotion Workflows artifact)
- Individual application deployment details (covered in Deployment Specifications)
- Incident response procedures (covered in Incident Runbooks)

### Target Audience

**Primary Audience**:
- Security Architects defining security and compliance gates
- Platform Engineers implementing policy enforcement
- Compliance Officers ensuring regulatory adherence

**Secondary Audience**:
- DevOps teams understanding promotion criteria
- Auditors reviewing policy enforcement evidence
- Engineering leadership setting quality standards

## Document Information

**Format**: Markdown

**File Pattern**: `*.promotion-rules.md`

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

**Policy as Code**: Store promotion rules in Git as OPA policies, Kyverno rules, or platform-specific configurations, version control all changes
**Automated Enforcement**: Integrate policy evaluation into CI/CD pipelines, fail builds/deployments on policy violations
**Clear Feedback**: Provide actionable error messages when rules fail, guide developers to remediation steps
**Graduated Rules**: Apply stricter rules for higher environments (dev → staging → production)
**Risk-Based Rules**: Set thresholds based on risk (critical apps require higher quality gates)
**Separation of Duties**: Different approvers for code changes vs. deployment approval, prevent self-approval
**Audit Logging**: Log all policy evaluations, approval decisions, exceptions granted, enforcement actions
**Regular Review**: Quarterly review of rules for effectiveness, adjust thresholds based on team capability, remove outdated rules
**Exception Process**: Define clear exception criteria, require compensating controls, time-box waivers, track exception debt
**Testing Policies**: Test policy rules in non-production, validate rule logic, avoid overly restrictive rules that block legitimate work
**Documentation**: Document rationale for each rule, link to compliance requirements, provide examples
**Metric Tracking**: Measure policy violation rates, exception frequency, time-to-remediate, adjust rules based on data
**Stakeholder Buy-in**: Collaborate with development teams on rule definition, balance security with developer velocity

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

**Policy as Code Tools**:
- Open Policy Agent (OPA) - General-purpose policy engine with Rego language
- Kyverno - Kubernetes-native policy management
- Gatekeeper - OPA for Kubernetes admission control
- HashiCorp Sentinel - Policy as code for HashiCorp tools
- AWS Config Rules - AWS compliance and governance
- Azure Policy - Azure resource governance
- GCP Organization Policy - GCP resource constraints
- Conftest - Test configuration files using OPA
- Regula - Infrastructure-as-code security validation

**Quality Gates**:
- Test coverage tools: JaCoCo, Istanbul, Coverage.py, Cobertura
- Code quality: SonarQube, CodeClimate, Codacy, DeepSource
- Quality thresholds: >80% coverage, no critical bugs, A rating
- Test frameworks: JUnit, pytest, Jest, Mocha for automated testing

**Security & Compliance**:
- Vulnerability scanning: Snyk, Trivy, Clair, Anchore, Aqua Security
- SAST: SonarQube, Checkmarx, Fortify, CodeQL
- DAST: OWASP ZAP, Burp Suite
- Container signing: Cosign, Notary, Docker Content Trust
- SBOM generation: Syft, CycloneDX, SPDX
- Compliance frameworks: SOC 2, PCI DSS, HIPAA, ISO 27001, FedRAMP

**Approval & Governance**:
- RBAC (Role-Based Access Control) for approvers
- CODEOWNERS file for approval routing
- ServiceNow Change Management integration
- Jira Service Management approval workflows
- Separation of duties enforcement
- Multi-party approval (quorum requirements)

**Artifact Management**:
- Semantic versioning (SemVer 2.0)
- Container image signing and verification
- Artifact provenance (SLSA framework)
- Immutable artifact registries
- Artifact retention policies

**Supply Chain Security**:
- SLSA (Supply-chain Levels for Software Artifacts)
- SBOM (Software Bill of Materials) requirements
- Sigstore (Cosign, Rekor, Fulcio) for signing
- In-toto for supply chain integrity
- OWASP Dependency-Check for SCA

**Compliance Standards**:
- SOC 2 Type II - Change management controls
- PCI DSS - Secure deployment practices
- HIPAA - Protected health information controls
- ISO 27001 - Information security management
- NIST Cybersecurity Framework
- CIS Benchmarks for hardening

**Exception Management**:
- Risk acceptance process
- Compensating controls documentation
- Time-bound waivers with expiration
- Exception tracking and debt metrics
- Audit trail for all exceptions

**Reference**: Consult organizational security, compliance, and platform engineering standards teams for detailed guidance on framework application

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
