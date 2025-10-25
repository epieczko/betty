# Name: secure-coding-checklist

## Executive Summary

The Secure Coding Checklist is a critical security deliverable that ensures software development practices adhere to industry-recognized secure coding standards, preventing common vulnerabilities before they reach production. This artifact provides systematic verification of secure coding practices aligned with OWASP Top 10, CWE Top 25 Most Dangerous Software Weaknesses, CERT Secure Coding Standards, and SANS/CWE Top 25 Software Errors.

As a foundational component of application security programs, this checklist serves development teams performing security reviews, security engineers conducting code audits, and quality assurance teams verifying compliance with secure coding requirements. It integrates with SAST (Static Application Security Testing) tools like SonarQube, Checkmarx, Veracode, Snyk Code, and CodeQL to provide comprehensive coverage across input validation, authentication/authorization, cryptography, session management, error handling, and secure configuration domains.

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

This artifact serves as a systematic verification checklist ensuring code adheres to secure coding standards, preventing injection attacks (SQL, XSS, Command), broken authentication, security misconfigurations, insecure deserialization, XML External Entity (XXE) attacks, and other OWASP Top 10 vulnerabilities. It provides developers and security teams with actionable verification criteria for input validation, output encoding, cryptographic implementation, access control, and secure error handling.

### Scope

**In Scope**:
- OWASP Top 10 vulnerability prevention (A01-A10 coverage)
- CWE Top 25 Most Dangerous Software Weaknesses mitigation
- Input validation and sanitization (allowlist/denylist patterns)
- Authentication and authorization implementation (OAuth 2.0, OIDC, SAML)
- Cryptographic controls (TLS 1.2+, AES-256, secure random number generation)
- Session management (secure cookies, CSRF tokens, session timeout)
- Error handling and logging (avoiding information disclosure)
- Secure configuration (hardening, least privilege, defense in depth)
- SAST tool integration (SonarQube, Checkmarx, Veracode, Snyk)
- Language-specific security (Python Bandit, JavaScript ESLint security, Java SpotBugs)
- API security (REST, GraphQL, rate limiting, API authentication)

**Out of Scope**:
- Infrastructure security (covered by infrastructure hardening checklists)
- Network security controls (firewalls, IDS/IPS configurations)
- DAST/penetration testing procedures (covered by security testing artifacts)
- Incident response procedures (covered by incident management artifacts)
- Third-party dependency vulnerability management (covered by SCA/dependency scanning)

### Target Audience

**Primary Audience**:
- Software Engineers implementing secure coding practices
- Security Engineers conducting secure code reviews
- Application Security Architects defining security requirements

**Secondary Audience**:
- QA/Test Engineers verifying security controls
- DevOps Engineers integrating SAST tools in CI/CD pipelines
- Compliance Officers ensuring regulatory adherence (PCI-DSS, SOC 2, ISO 27001)

## Document Information

**Format**: Markdown

**File Pattern**: `*.secure-coding-checklist.md`

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

**SAST Integration**: Integrate static analysis tools (SonarQube, Checkmarx, Snyk Code) into CI/CD pipelines with quality gates blocking insecure code
**OWASP Top 10 Mapping**: Map each checklist item to specific OWASP Top 10 and CWE categories for traceability and reporting
**Language-Specific Checks**: Customize checklist per language (Python Bandit rules, JavaScript ESLint security, Java SpotBugs)
**Input Validation First**: Prioritize allowlist-based input validation over denylist approaches; validate all inputs at trust boundaries
**Cryptographic Standards**: Mandate TLS 1.2+ for transport, AES-256 for encryption, secure random generation (java.security.SecureRandom, secrets module)
**Authentication Best Practices**: Enforce MFA, implement OAuth 2.0/OIDC properly, use bcrypt/Argon2 for password hashing (never MD5/SHA1)
**SQL Injection Prevention**: Use parameterized queries/prepared statements exclusively; never string concatenation for SQL
**XSS Prevention**: Context-aware output encoding (HTML entity encoding, JavaScript escaping, URL encoding) using framework functions
**CSRF Protection**: Implement anti-CSRF tokens (synchronizer tokens, double-submit cookies) for state-changing operations
**Security Headers**: Enforce Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security
**Error Handling**: Implement generic error messages externally; log detailed errors securely; never expose stack traces
**Dependency Management**: Use SCA tools (Snyk, OWASP Dependency-Check, GitHub Dependabot) to identify vulnerable dependencies
**Code Review Requirements**: Require security-focused peer review for authentication, authorization, cryptography, input validation code
**Security Testing**: Combine SAST (pre-commit), DAST (staging), and penetration testing (pre-production) for defense in depth
**Version Control**: Store checklists in Git with version history; treat as code (review, branch, merge workflows)
**Continuous Updates**: Update checklist quarterly or when new OWASP Top 10/CWE releases; incorporate lessons from security incidents
**Training Integration**: Link checklist items to secure coding training modules (OWASP Secure Coding Dojo, SANS courses)

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

**Secure Coding Standards**:
- OWASP Top 10 (2021): A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection
- CWE Top 25 Most Dangerous Software Weaknesses (2024)
- SANS/CWE Top 25 Most Dangerous Software Errors
- CERT Secure Coding Standards (C, C++, Java, Perl, Android)
- MISRA C/C++ (automotive/embedded systems secure coding)
- SEI CERT C Coding Standard
- SEI CERT Java Coding Standard
- Microsoft Security Development Lifecycle (SDL)
- Oracle Java Secure Coding Guidelines

**SAST/Code Quality Tools**:
- SonarQube (SonarCloud) with Security Hotspots and Vulnerability detection
- Checkmarx SAST (CxSAST)
- Veracode Static Analysis
- Fortify Static Code Analyzer (SCA)
- Snyk Code (developer-first SAST)
- GitHub Advanced Security (CodeQL)
- Semgrep (lightweight static analysis)
- CodeQL (GitHub's semantic code analysis)
- ESLint security plugins (JavaScript/TypeScript)
- Bandit (Python security linter)
- Brakeman (Ruby on Rails security scanner)
- GoSec (Go security checker)
- SpotBugs with Find Security Bugs plugin (Java)
- Pylint security extensions

**Web Application Security**:
- OWASP Application Security Verification Standard (ASVS) 4.0
- OWASP Software Assurance Maturity Model (SAMM)
- OWASP Proactive Controls (C1-C10)
- OWASP Cheat Sheet Series
- NIST SP 800-53 (Security and Privacy Controls) - SA, SC, SI families
- NIST SP 800-64 (Security Considerations in SDLC)
- PCI-DSS Requirement 6 (Develop and Maintain Secure Systems and Applications)

**API Security**:
- OWASP API Security Top 10
- REST API Security Best Practices
- GraphQL Security Best Practices
- OAuth 2.0 RFC 6749, OpenID Connect (OIDC)
- JSON Web Token (JWT) Best Practices RFC 8725

**Cryptography Standards**:
- NIST FIPS 140-2/140-3 (Cryptographic Module Validation)
- NIST SP 800-57 (Key Management Recommendations)
- NIST SP 800-90A (Random Number Generation)
- TLS 1.2 (RFC 5246), TLS 1.3 (RFC 8446)
- AES-256 encryption, RSA 2048+, ECDSA P-256+

**Language-Specific Security**:
- Python: Bandit, Safety, PyUp
- JavaScript/TypeScript: ESLint security, npm audit, Retire.js
- Java: SpotBugs, Find Security Bugs, OWASP Dependency-Check
- .NET: Security Code Scan, .NET Security Guard
- Ruby: Brakeman, bundler-audit
- Go: GoSec, Nancy
- PHP: RIPS, Psalm security analysis

**Compliance & Regulatory**:
- SOC 2 Type II (CC6.6, CC6.7 - Logical and Physical Access Controls)
- ISO 27001:2013 (A.14.2 Security in Development and Support Processes)
- PCI-DSS v4.0 (Requirement 6 - Secure Software Development)
- GDPR Article 25 (Data Protection by Design and by Default)
- HIPAA Security Rule (Administrative Safeguards - Workforce Security)
- FedRAMP Controls (SA-11, SA-15, SI-10)

**Reference**: Consult organizational AppSec team for detailed guidance on framework application and SAST tool selection

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
