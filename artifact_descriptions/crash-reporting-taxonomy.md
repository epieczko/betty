# Name: crash-reporting-taxonomy

## Executive Summary

The Crash Reporting Taxonomy is a structured classification system that standardizes crash categorization, severity assignment, and metadata capture across mobile, web, and backend applications. This taxonomy ensures consistent crash analysis using platforms like Sentry, Bugsnag, Crashlytics, or Rollbar by defining crash types, error codes, stack trace patterns, and impact classifications.

As a cornerstone of application reliability engineering and Site Reliability Engineering (SRE) practices, this artifact enables teams to prioritize remediation efforts, track error budgets, identify platform-specific issues, and measure crash-free user rates. It provides development, QA, and operations teams with a common language for discussing application stability and user experience impact.

### Strategic Importance

- **Prioritization Framework**: Defines P0-P3 severity levels based on user impact, crash frequency, and business criticality
- **Triage Efficiency**: Enables automated routing of crashes to appropriate teams using error fingerprints and stack trace patterns
- **Trend Analysis**: Facilitates identification of systemic issues through standardized crash categorization
- **SLA Alignment**: Maps crash severity to incident response SLAs and MTTR targets
- **Release Quality**: Provides objective criteria for go/no-go decisions based on crash rates and severity distribution

## Purpose & Scope

### Primary Purpose

Establishes a unified taxonomy for classifying application crashes, errors, and exceptions across all platforms to enable consistent reporting, prioritization, and remediation tracking using crash monitoring tools.

### Scope

**In Scope**:
- Mobile crash classification (iOS, Android native crashes, ANR, OOM errors)
- Web application errors (JavaScript exceptions, unhandled promise rejections, network failures)
- Backend service crashes (uncaught exceptions, segmentation faults, OOM kills, panic conditions)
- Crash severity levels with clear user impact definitions (P0: app crash on launch, P1: feature unavailable)
- Error fingerprinting rules for deduplication and grouping
- Platform-specific crash types (iOS signal crashes, Android Native Development Kit crashes, JVM crashes)
- Crash metadata requirements (OS version, app version, device model, user session context)
- Symbolication and deobfuscation taxonomy (iOS dSYMs, Android ProGuard mapping files)
- Crash-free user rate and crash-free session rate definitions
- Network error classification (timeouts, DNS failures, SSL/TLS errors, HTTP status codes)
- Performance issue classification (slow renders, frame drops, memory warnings)
- User-reported errors vs. automatically detected crashes
- Third-party library crash attribution

**Out of Scope**:
- Crash analysis procedures and remediation workflows (covered in crash triage playbooks)
- Crash monitoring tool configuration and implementation
- Code-level debugging techniques and root cause analysis methods
- Performance profiling and optimization strategies
- User feedback collection and sentiment analysis
- Release management and deployment processes

### Target Audience

**Primary Audience**:
- Mobile developers (iOS, Android) classifying and triaging crashes
- Web frontend developers handling JavaScript errors and exceptions
- Backend engineers investigating service crashes and panics
- SRE teams managing error budgets and reliability targets

**Secondary Audience**:
- QA engineers validating crash classification during testing
- Product managers prioritizing bug fixes based on user impact
- Technical support teams escalating critical crash reports
- DevOps engineers configuring crash monitoring alerts and thresholds

## Document Information

**Format**: Markdown

**File Pattern**: `*.crash-reporting-taxonomy.md`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: Internal - Contains application architecture and error patterns

**Retention**: Minimum 3 years for trend analysis; indefinite for taxonomy versioning


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

### Report Overview

**Reporting Period**:
- `reportingPeriod`: Time period covered (e.g., Q2 2024, Jan 2024, etc.)
- `reportDate`: Date report was generated
- `reportType`: Regular | Ad-hoc | Special Investigation | Executive Briefing
- `frequency`: How often this report is generated
- `distribution`: Intended recipients and distribution method

### Executive Summary

**Key Highlights**:
- `criticalFindings`: Top 3-5 most important findings for executive attention
- `trendAnalysis`: Key trends compared to previous periods
- `recommendations`: Priority recommendations requiring executive decision
- `impactAssessment`: Business impact of findings or metrics

### Detailed Analysis

**Metrics & KPIs**:
- `metricName`: Name of each metric or KPI
- `currentValue`: Value for this reporting period
- `targetValue`: Target or goal
- `previousValue`: Value from previous period for trending
- `variance`: Difference from target and trend direction
- `variances`: Explanation of significant variances
- `dataSource`: Where data comes from
- `collectionMethod`: How data is collected and validated

**Analysis by Category**:
- `category`: Grouping for related metrics or findings
- `observations`: What was observed or measured
- `analysis`: Interpretation and meaning
- `rootCauses`: Underlying causes for significant findings
- `impact`: Business or operational impact
- `trends`: Patterns over time
- `comparatives`: Benchmarking against industry or peer data

### Recommendations & Actions

**Priority Actions**:
- `actionId`: Unique identifier
- `actionDescription`: What needs to be done
- `rationale`: Why this action is needed
- `priority`: P0 | P1 | P2 | P3
- `owner`: Who is responsible
- `dueDate`: Target completion date
- `estimatedEffort`: Resource requirement
- `dependencies`: Prerequisites or dependencies
- `successMetrics`: How success will be measured

**Follow-up Items**:
- `openItems`: Items from previous reports still in progress
- `closedItems`: Items completed since last report
- `escalations`: Items requiring escalation to higher authority


## Best Practices

**Severity Standardization**: Define P0 (launch blocker), P1 (core feature failure), P2 (degraded experience), P3 (minor issue) with explicit user impact criteria
**Crash-Free Rate Targets**: Maintain >99.5% crash-free sessions for production; >98% for beta releases
**Fingerprinting Consistency**: Use stable error fingerprints combining exception type, file path, and function name (avoid line numbers)
**Symbolication Requirements**: Upload symbols within 1 hour of release to enable readable stack traces
**Grouping Intelligence**: Configure smart grouping to cluster similar crashes while avoiding over-aggregation
**Platform-Specific Classification**: Separate iOS signal crashes (SIGSEGV, SIGABRT) from Android JNI crashes and JavaScript exceptions
**Breadcrumb Taxonomy**: Standardize breadcrumb categories (navigation, network, user input, state changes) for context
**User Impact Metrics**: Track affected users, not just crash count (10 users with 100 crashes > 100 users with 10 crashes)
**Performance Thresholds**: Define slow startup (>5s), ANR threshold (5s on Android), slow renders (>16ms frame time)
**Release Tagging**: Tag crashes by release version, deployment environment, and feature flag state
**Error Budget**: Allocate error budget as percentage of requests/sessions (e.g., 99.9% reliability = 0.1% error budget)
**Auto-Assignment Rules**: Configure automatic assignment based on file path, team ownership, or error fingerprint
**Regression Detection**: Flag crashes introduced in new releases by comparing fingerprints to historical baselines
**Third-Party Attribution**: Separate crashes in vendor SDKs from first-party code crashes
**Network Error Taxonomy**: Classify by HTTP status (4xx client errors, 5xx server errors, timeouts, DNS failures)
**Memory Issue Classification**: Distinguish OOM kills, memory warnings, and memory leaks
**Handled vs. Unhandled**: Track both caught exceptions (for alerting) and unhandled crashes (for stability)
**Sampling Strategy**: Use 100% sampling for crashes, intelligent sampling (1-10%) for handled errors to manage costs
**PII Redaction**: Automatically redact email addresses, tokens, and sensitive data from crash reports
**Deduplication Windows**: Group crashes within 24-hour windows to track ongoing vs. new issues
**Integration with APM**: Correlate crash events with application performance monitoring (New Relic, Datadog, Dynatrace)
**Alerting Thresholds**: Alert on spike (>2x baseline), new error fingerprint in production, or P0/P1 crashes
**Historical Retention**: Retain crash data for minimum 90 days; aggregated metrics for 2+ years
**Cross-Platform Consistency**: Use unified severity definitions across mobile, web, and backend platforms
**Compliance Requirements**: Follow GDPR/CCPA guidelines for user consent and data retention in crash reports

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

**Crash Monitoring Platforms**:
- Sentry Error Tracking Best Practices
- Firebase Crashlytics Implementation Guide
- Bugsnag Error Monitoring Documentation
- Rollbar Error Tracking Standards
- New Relic Browser Monitoring (JavaScript errors)
- Datadog RUM (Real User Monitoring) Error Tracking
- AppDynamics Crash Analytics
- Instabug Crash Reporting

**Mobile Platform Standards**:
- Apple Crash Reporting and Energy Diagnostics
- Android Vitals and ANR (Application Not Responding) Guidelines
- iOS Human Interface Guidelines - Error Handling
- Android App Quality Guidelines
- React Native Error Boundaries
- Flutter Crash Reporting Integration (Crashlytics, Sentry)
- Xamarin Crash Reporting Best Practices

**Symbolication & Debug**:
- iOS dSYM Files and Symbolication Process
- Android ProGuard/R8 Mapping Files
- JavaScript Source Maps for Minified Code
- DWARF Debugging Format (iOS/macOS)
- Breakpad Crash Reporting Library (cross-platform)
- Crashpad Crash Reporting System (Chromium-based)

**Error Taxonomies & Standards**:
- HTTP Status Code Definitions (RFC 7231)
- POSIX Signal Definitions (SIGSEGV, SIGABRT, SIGBUS, etc.)
- JavaScript Error Types (TypeError, ReferenceError, SyntaxError)
- Java Exception Hierarchy
- .NET Exception Handling Best Practices
- Go Error Handling Conventions
- Python Exception Taxonomy

**Site Reliability Engineering**:
- Google SRE Book - Monitoring Distributed Systems
- Error Budget Policy Templates
- SLI/SLO/SLA Framework for Application Reliability
- Incident Severity Classification (P0-P4)
- On-Call Runbook Standards
- Postmortem Culture and Templates

**Application Performance**:
- Web Vitals (Core Web Vitals, FID, LCP, CLS)
- RAIL Performance Model (Response, Animation, Idle, Load)
- iOS Performance Best Practices
- Android Performance Patterns
- Progressive Web App (PWA) Reliability Guidelines

**Compliance & Privacy**:
- GDPR Article 5 (Data Minimization in Crash Reports)
- CCPA Requirements for Error Data
- COPPA Compliance for Children's Apps
- HIPAA Technical Safeguards (if health data in crashes)
- PCI DSS Requirement 6.5 (Application Vulnerability Management)
- SOC 2 Type II - Availability and Processing Integrity

**Quality Assurance**:
- ISO/IEC 25010 (Software Quality Model - Reliability)
- IEEE 1044 (Classification of Software Anomalies)
- ISTQB Software Testing Defect Management
- Severity vs. Priority Matrix Standards

**DevOps & CI/CD**:
- Shift-Left Testing Principles
- Continuous Monitoring in CI/CD Pipelines
- Release Quality Gates (crash rate thresholds)
- Feature Flag Management with Error Tracking
- Blue-Green Deployment Monitoring

**Open Source Standards**:
- OpenTelemetry Error Tracking Semantics
- W3C Web Application Errors Specification
- OWASP Application Security Verification Standard (ASVS)
- CWE (Common Weakness Enumeration) for Code Vulnerabilities

**Industry Benchmarks**:
- Firebase Performance Monitoring Benchmarks
- App Store Review Guidelines (crash thresholds)
- Google Play Vitals (ANR rate, crash rate requirements)
- Industry Standard Crash-Free Rates (99%+ for consumer apps)

**Platform-Specific**:
- Windows Error Reporting (WER) Documentation
- Linux Core Dump Analysis
- macOS Crash Reporter and Sample Analysis
- Android Native Development Kit (NDK) Crash Handling

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- Application architecture documentation (platforms, tech stack, deployment environments)
- Crash monitoring tool selection and configuration (Sentry, Bugsnag, Crashlytics)
- Team ownership mapping (which teams own which services/features)
- Release management process and version tagging strategy
- Error budget policies and reliability targets
- Incident response procedures and SLA definitions

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- Crash triage playbooks that use taxonomy for routing and prioritization
- Incident response procedures for escalation and communication
- Release quality gates and go/no-go decision criteria
- Error budget tracking and SLO/SLI monitoring dashboards
- Engineering OKRs and reliability improvement initiatives
- Customer support knowledge bases for known error patterns

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- Crash triage playbooks (operational procedures)
- Incident severity matrix (for escalation alignment)
- Application monitoring strategy (APM, logs, traces)
- Release management process (version control, deployment tracking)
- Error budget policy (reliability targets and tolerances)
- On-call runbooks (crash investigation procedures)

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
- Primary Approver: Engineering Manager or Principal Engineer
- Secondary Approver: SRE Lead or Platform Engineering Lead
- Governance Approval: Architecture Review Board for enterprise-wide standards

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: Quarterly review for accuracy and completeness

**Event-Triggered Updates**: Update immediately when:
- New platforms or technologies are adopted (new mobile frameworks, backend languages)
- Crash monitoring tools are changed or upgraded
- Error budget policies are revised
- Major application rewrites or architecture changes occur
- New severity definitions or SLA requirements are introduced
- Regulatory requirements change (GDPR updates, new privacy laws)

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring of severity levels or category definitions
- **MINOR**: New crash types, platforms, or classification rules added
- **PATCH**: Corrections, clarifications, minor updates to examples

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: Minimum 3 years for trend analysis; retain major versions indefinitely

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: Engineering Manager or SRE Lead

**Responsibilities**:
- Ensure taxonomy remains current with platform and tooling changes
- Coordinate quarterly reviews with development and operations teams
- Manage review and approval process for updates
- Respond to stakeholder questions and clarification requests
- Archive superseded versions with change documentation

## Templates & Examples

### Template Access

**Primary Template**: `templates/crash-reporting-taxonomy-template.md`

**Alternative Formats**: JSON schema for programmatic crash classification

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/crash-reporting-taxonomy-example-*.md`

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

- GDPR: Minimize PII in crash reports; provide user consent mechanisms
- CCPA: Allow users to opt-out of crash data collection
- COPPA: Special handling for apps targeting children under 13
- HIPAA: Ensure no PHI in crash reports for healthcare applications
- SOC 2: Demonstrate monitoring and incident response capabilities

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team for reliability and quality assurance
- External audits by third-party auditors for SOC 2, ISO 27001
- Regulatory examinations for privacy compliance (GDPR, CCPA)
- App store compliance reviews (Apple App Store, Google Play)

**Audit Preparation**:
- Maintain complete version history of taxonomy changes
- Document all approvals with evidence
- Keep change log current with rationale
- Ensure accessibility for auditors with appropriate permissions

### Policy Alignment

This artifact must align with:

- Application reliability and error budget policies
- Incident response and escalation procedures
- Data privacy and protection policies (PII handling in crashes)
- Software development lifecycle (SDLC) standards
- Release quality gates and deployment criteria

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Adoption Rate**: Percentage of teams using standardized taxonomy
- **Classification Accuracy**: Percentage of crashes correctly classified on first pass
- **Triage Efficiency**: Reduction in time to assign crashes to appropriate teams
- **Downstream Impact**: Number of processes and tools relying on this taxonomy

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: Development and Operations

**Category**: Application Reliability Engineering, Site Reliability Engineering (SRE)

**Typical Producers**: Engineering Managers, SRE Leads, Principal Engineers, Platform Engineering

**Typical Consumers**: Mobile/Web/Backend Developers, QA Engineers, SRE Teams, DevOps, Technical Support

**Effort Estimate**: 16-24 hours for initial creation; 4-8 hours per quarterly update

**Complexity Level**: Medium to High

**Business Criticality**: High (impacts user experience and application reliability)

**Change Frequency**: Quarterly reviews; ad-hoc updates for new platforms or major changes

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: General - Version 2.0*
