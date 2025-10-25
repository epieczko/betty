#!/usr/bin/env python3
"""
Comprehensive Artifact Enhancer
Generates Big Five consulting-quality artifact definitions for all artifact types
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple


# Comprehensive phase and category mappings from the original deliverables
PHASE_CATEGORY_MAP = {
    "portfolio-roadmap": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "initiative-charter": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "epic-charter": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "governance-charter": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "steering-committee-minutes": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "go-no-go-minutes": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "raid-log": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "decision-log": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "adr-index": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "change-log": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "exception-log": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "program-increment-plan": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "sprint-goals": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "velocity-and-burndown-reports": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "resource-plan": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "skills-matrix": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "staffing-plan": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "raci-per-workstream": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "vendor-management-pack": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "third-party-risk-assessments": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "sig-questionnaires": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "vendor-scorecards": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "budget-forecast": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "capitalization-policy": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "time-allocation-worksheets": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "benefits-realization-plan": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),
    "benefits-realization-report": ("0. Portfolio, Governance, and Delivery Ops", "Governance & Planning"),

    "vision-statement": ("1. Inception / Strategy", "Business & Strategy"),
    "mission-statement": ("1. Inception / Strategy", "Business & Strategy"),
    "product-strategy": ("1. Inception / Strategy", "Business & Strategy"),
    "okr-definitions": ("1. Inception / Strategy", "Business & Strategy"),
    "kpi-framework": ("1. Inception / Strategy", "Business & Strategy"),
    "business-case": ("1. Inception / Strategy", "Business & Strategy"),
    "roi-model": ("1. Inception / Strategy", "Business & Strategy"),
    "feasibility-study": ("1. Inception / Strategy", "Business & Strategy"),
    "market-analysis": ("1. Inception / Strategy", "Business & Strategy"),
    "competitive-analysis": ("1. Inception / Strategy", "Business & Strategy"),
    "stakeholder-map": ("1. Inception / Strategy", "Business & Strategy"),
    "engagement-plan": ("1. Inception / Strategy", "Business & Strategy"),
    "communication-plan": ("1. Inception / Strategy", "Business & Strategy"),
    "change-control-plan": ("1. Inception / Strategy", "Business & Strategy"),
    "risk-appetite-statement": ("1. Inception / Strategy", "Business & Strategy"),
    "enterprise-risk-register": ("1. Inception / Strategy", "Business & Strategy"),

    # Add more mappings as needed - this is a starter set
    # The script will use generic templates for unmapped items
}


def generate_executive_summary(artifact_name: str, category: str, phase: str) -> str:
    """Generate comprehensive executive summary based on artifact type"""

    # Clean artifact name for display
    display_name = artifact_name.replace('-', ' ').title()

    # Phase-specific context
    phase_num = phase.split('.')[0] if '.' in phase else ""
    phase_name = phase.split('. ')[1] if '. ' in phase else phase

    executive_summaries = {
        "log": f"""## Executive Summary

The {display_name} is a critical governance and audit artifact that provides a chronological record of {artifact_name.replace('-log', '').replace('-', ' ')} throughout the {phase_name} phase. This structured log serves as both a real-time management tool and a historical record for post-project reviews, audits, and lessons learned activities.

As a cornerstone of program governance, this artifact enables transparency, accountability, and informed decision-making by providing stakeholders with immediate visibility into key events, decisions, and their outcomes. It supports root cause analysis, trend identification, and continuous improvement by maintaining a complete audit trail.

### Strategic Importance

- **Governance Excellence**: Demonstrates rigorous program management and adherence to organizational standards
- **Risk Mitigation**: Early identification of patterns and trends enables proactive intervention
- **Audit Readiness**: Provides comprehensive trail for internal and external audits
- **Knowledge Capture**: Preserves institutional knowledge beyond individual personnel tenure
- **Continuous Improvement**: Enables data-driven process improvements through trend analysis""",

        "plan": f"""## Executive Summary

The {display_name} is a comprehensive planning artifact that establishes the strategic approach, resource allocation, timeline, and success criteria for {artifact_name.replace('-plan', '').replace('-', ' ')} activities within the {phase_name} phase. This forward-looking document serves as the authoritative reference for execution teams, stakeholders, and governance bodies.

As a foundational planning deliverable, it translates strategic objectives into actionable tasks, identifies dependencies and constraints, allocates resources optimally, and establishes measurable outcomes. The plan balances ambition with pragmatism, incorporating risk mitigation strategies and contingency approaches.

### Strategic Importance

- **Strategic Alignment**: Ensures activities directly support organizational objectives and expected outcomes
- **Resource Optimization**: Enables efficient allocation of personnel, budget, and technology resources
- **Risk Management**: Identifies potential obstacles and defines proactive mitigation strategies
- **Stakeholder Alignment**: Creates shared understanding of approach, timeline, and expectations
- **Success Measurement**: Establishes clear metrics and criteria for evaluating outcomes""",

        "matrix": f"""## Executive Summary

The {display_name} is a structured analytical tool that maps relationships, responsibilities, or characteristics across multiple dimensions within the {phase_name} context. This visual decision-support artifact enables rapid assessment, gap identification, and optimization of {artifact_name.replace('-matrix', '').replace('-', ' ')} across the organization.

As both an analytical and communication tool, the matrix format facilitates pattern recognition, highlights interdependencies, and supports data-driven decision-making. It serves as a common reference point for cross-functional teams and enables systematic evaluation of complex, multidimensional challenges.

### Strategic Importance

- **Complexity Management**: Simplifies multidimensional analysis into digestible visual format
- **Gap Analysis**: Rapidly identifies coverage gaps, redundancies, or misalignments
- **Decision Support**: Provides structured framework for evaluating options and trade-offs
- **Communication Excellence**: Enables consistent understanding across diverse stakeholder groups
- **Accountability**: Clearly defines ownership and responsibilities across dimensions""",

        "charter": f"""## Executive Summary

The {display_name} is a formal authorization document that establishes the mandate, scope, authority, and boundaries for {artifact_name.replace('-charter', '').replace('-', ' ')} activities. This foundational governance artifact provides the legitimate basis for resource allocation, decision-making authority, and stakeholder engagement.

As the constitutional document for the initiative, it aligns sponsors, defines success criteria, establishes governance structure, and sets expectations for all participants. The charter serves as the primary reference for resolving scope questions and arbitrating stakeholder disagreements.

### Strategic Importance

- **Formal Authorization**: Provides legitimate mandate from executive sponsors and stakeholders
- **Scope Clarity**: Defines clear boundaries for what is included and excluded
- **Authority Definition**: Establishes decision-making rights and escalation paths
- **Resource Commitment**: Secures commitment of necessary resources and support
- **Stakeholder Alignment**: Creates shared understanding of objectives and approach""",

        "policy": f"""## Executive Summary

The {display_name} is a formal directive that establishes organizational rules, standards, and requirements for {artifact_name.replace('-policy', '').replace('-', ' ')}. This governance artifact provides mandatory guidance that applies across the organization, ensuring consistency, compliance, and risk management.

As a cornerstone of organizational governance, policies translate strategic intent and risk appetite into concrete requirements. They establish the "rules of the road" that guide behavior, decision-making, and operational activities while providing the foundation for controls, procedures, and audit criteria.

### Strategic Importance

- **Risk Management**: Mitigates organizational risk through standardized requirements
- **Compliance Assurance**: Ensures adherence to regulatory and legal obligations
- **Consistency**: Drives uniform approach across business units and geographies
- **Accountability**: Establishes clear expectations and consequences
- **Efficiency**: Reduces redundant decision-making through established standards""",
    }

    # Check for keyword matches
    for keyword, summary in executive_summaries.items():
        if keyword in artifact_name:
            return summary

    # Default executive summary
    return f"""## Executive Summary

The {display_name} is a critical deliverable within the {phase_name} phase, supporting {category} activities across the initiative lifecycle. This artifact provides structured, actionable information that enables stakeholders to make informed decisions, maintain alignment with organizational standards, and deliver consistent, high-quality outcomes.

As a core component of the {category} practice, this artifact serves multiple constituencies—from hands-on practitioners who require detailed technical guidance to executive leadership seeking assurance of appropriate governance and risk management. It balances comprehensiveness with usability, ensuring that information is both thorough and accessible.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement"""


def generate_detailed_structure(artifact_name: str, format_type: str, category: str) -> str:
    """Generate detailed document structure based on artifact type"""

    # Base structure common to most artifacts
    base_structure = """
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
"""

    structure_templates = {
        "assessment": base_structure + """
### Assessment Methodology

**Approach**:
- `assessmentFramework`: Framework or standard used (e.g., NIST, ISO, proprietary)
- `assessmentScope`: Systems, processes, or areas assessed
- `evaluationCriteria`: Specific criteria used for evaluation
- `maturityModel`: Maturity levels if applicable (Initial, Managed, Defined, etc.)
- `scoringMethodology`: How scores or ratings are assigned

**Assessment Execution**:
- `assessmentPeriod`: Time period covered by the assessment
- `dataCollectionMethods`: Interviews, documentation review, testing, observation
- `participantsInterviewed`: Roles and number of people interviewed
- `evidenceReviewed`: Types and volume of evidence examined
- `limitations`: Any limitations or constraints on the assessment

### Findings & Results

**Summary Results**:
- `overallRating`: Aggregate assessment result
- `maturityLevel`: Current maturity level if using maturity model
- `complianceScore`: Percentage compliance if applicable
- `trendAnalysis`: Comparison to previous assessments

**Detailed Findings**:
- `findingId`: Unique identifier for each finding
- `findingCategory`: Category or control area
- `findingTitle`: Concise title
- `description`: Detailed description of finding
- `severity`: Critical | High | Medium | Low
- `evidence`: Supporting evidence for finding
- `impact`: Business or technical impact
- `likelihood`: Probability of occurrence if risk-related
- `currentState`: Current state or practice observed
- `desiredState`: Target state or required practice
- `gap`: Specific gap between current and desired
- `recommendations`: Specific remediation recommendations
- `priority`: Prioritization for remediation
- `estimatedEffort`: Effort required to remediate

### Remediation Plan

**Recommendations Summary**:
- `totalRecommendations`: Count by severity
- `quickWins`: High-value, low-effort improvements
- `strategicInitiatives`: Long-term, high-effort improvements
- `costBenefitAnalysis`: Estimated cost vs. benefit for major recommendations

**Remediation Roadmap**:
- `phase1Immediate`: 0-3 months, critical items
- `phase2NearTerm`: 3-6 months, high priority items
- `phase3MidTerm`: 6-12 months, medium priority items
- `phase4LongTerm`: 12+ months, strategic initiatives

**Implementation Tracking**:
- `recommendationOwner`: Who is responsible for each item
- `targetCompletionDate`: When remediation should be complete
- `statusTracking`: Mechanism for tracking progress
- `successCriteria`: How completion will be verified
""",

        "report": base_structure + """
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
""",

        "specification": base_structure + """
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
""",
    }

    # Determine which template to use
    if 'assessment' in artifact_name or 'audit' in artifact_name or 'evaluation' in artifact_name:
        return structure_templates['assessment']
    elif 'report' in artifact_name or 'analysis' in artifact_name or 'results' in artifact_name:
        return structure_templates['report']
    elif 'specification' in artifact_name or 'schema' in artifact_name or 'model' in artifact_name:
        return structure_templates['specification']
    else:
        return base_structure + """
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
"""


def generate_comprehensive_best_practices(artifact_name: str, category: str, phase: str) -> List[str]:
    """Generate comprehensive best practices tailored to artifact type"""

    # Universal best practices that apply to all artifacts
    universal = [
        "**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback",
        "**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability",
        "**Template Usage**: Use approved templates to ensure completeness and consistency across teams",
        "**Peer Review**: Have at least one qualified peer review before submitting for approval",
        "**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management",
        "**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in",
        "**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon",
        "**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively",
        "**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation",
        "**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes",
        "**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats",
        "**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates",
        "**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy",
    ]

    # Category-specific practices
    category_specific = {
        "Governance & Planning": [
            "**Executive Sponsorship**: Ensure visible executive sponsorship and regular executive review",
            "**Governance Alignment**: Align with organizational governance framework and decision-making bodies",
            "**Metric-Driven**: Include measurable metrics and KPIs to track progress and outcomes",
            "**Dependency Management**: Explicitly identify and track dependencies on other initiatives or resources",
            "**Risk Integration**: Integrate with risk management processes; escalate risks appropriately",
            "**Change Control**: Submit significant changes through formal change control process",
            "**Audit Trail**: Maintain comprehensive audit trail for governance and compliance purposes",
        ],
        "Security": [
            "**Defense in Depth**: Layer multiple controls; don't rely on single security measure",
            "**Least Privilege**: Grant minimum necessary access; default deny",
            "**Zero Trust**: Don't implicitly trust; always verify",
            "**Security by Design**: Incorporate security from the start, not bolted on later",
            "**Threat Intelligence**: Stay current with emerging threats and update controls accordingly",
            "**Incident Integration**: Ensure findings integrate with incident response processes",
            "**Continuous Monitoring**: Implement continuous monitoring rather than point-in-time assessments",
            "**Compliance Mapping**: Map controls to relevant compliance frameworks (SOC 2, ISO 27001, etc.)",
        ],
        "Requirements & Analysis": [
            "**Stakeholder Engagement**: Involve all affected stakeholders in requirements gathering",
            "**User-Centric**: Focus on user needs and use cases, not just technical capabilities",
            "**Testable Requirements**: Ensure all requirements are specific, measurable, and testable",
            "**Traceability Matrix**: Maintain requirements traceability through design, implementation, and testing",
            "**Change Management**: Establish clear process for requirements changes with impact assessment",
            "**Prioritization**: Use techniques like MoSCoW to prioritize requirements",
            "**Acceptance Criteria**: Define clear acceptance criteria for each requirement",
        ],
        "Architecture": [
            "**Standards Alignment**: Align with enterprise architecture standards and patterns",
            "**Framework Usage**: Leverage established frameworks (TOGAF, Zachman, etc.) for structure",
            "**Multiple Views**: Provide different architectural views (logical, physical, deployment, etc.)",
            "**Decision Recording**: Document architectural decisions and rationale using ADRs",
            "**Technology Radar**: Reference organization's technology radar or standards catalog",
            "**Review Process**: Submit for architecture review board approval before implementation",
            "**Future-Proofing**: Design for evolvability; avoid overly rigid solutions",
        ],
    }

    # Phase-specific considerations
    phase_specific = {
        "strategy": [
            "**Market Validation**: Validate assumptions with market research and customer feedback",
            "**Financial Rigor**: Use discounted cash flow, NPV, and scenario analysis for financial projections",
            "**Competitive Intelligence**: Incorporate competitive analysis and market positioning",
        ],
        "design": [
            "**User Research**: Base designs on actual user research, not assumptions",
            "**Accessibility**: Ensure WCAG 2.1 AA compliance for digital interfaces",
            "**Design System**: Leverage organizational design system for consistency",
            "**Prototyping**: Create prototypes for validation before full implementation",
        ],
        "implementation": [
            "**Code Quality**: Maintain high code quality through automated testing and code review",
            "**CI/CD Integration**: Integrate with continuous integration and deployment pipelines",
            "**Security Scanning**: Run automated security scans (SAST, DAST, dependency scanning)",
            "**Documentation**: Maintain comprehensive technical documentation alongside code",
        ],
        "operations": [
            "**SRE Principles**: Apply SRE practices like error budgets and SLOs",
            "**Observability**: Implement comprehensive logging, metrics, and tracing",
            "**Runbook Maintenance**: Keep operational runbooks current and tested",
            "**Incident Learning**: Conduct blameless postmortems and implement learnings",
        ],
    }

    # Combine relevant practices
    practices = universal.copy()

    # Add category-specific
    if category in category_specific:
        practices.extend(category_specific[category])

    # Add phase-specific (match on keywords in phase name)
    phase_lower = phase.lower()
    for phase_key, phase_practices in phase_specific.items():
        if phase_key in phase_lower:
            practices.extend(phase_practices)

    # Add artifact-type-specific practices
    if 'roadmap' in artifact_name:
        practices.extend([
            "**Time Horizons**: Use appropriate time granularity (quarters for 1-2 years, months for shorter periods)",
            "**Dependency Visualization**: Clearly show dependencies between initiatives",
            "**Capacity Overlay**: Show resource capacity constraints alongside demand",
            "**Milestone Tracking**: Highlight critical milestones and decision points",
        ])

    if 'test' in artifact_name or 'testing' in artifact_name:
        practices.extend([
            "**Test Pyramid**: Follow test pyramid pattern (more unit tests, fewer E2E tests)",
            "**Coverage Targets**: Aim for 80%+ code coverage with meaningful tests",
            "**Test Data Management**: Use realistic but sanitized test data",
            "**Continuous Testing**: Integrate testing into CI/CD pipeline",
        ])

    if 'policy' in artifact_name:
        practices.extend([
            "**Legal Review**: Have legal counsel review before approval",
            "**Exception Process**: Define clear exception request and approval process",
            "**Communication Plan**: Communicate policy broadly with training as needed",
            "**Enforcement Mechanism**: Define how compliance is monitored and enforced",
        ])

    return practices


def create_enhanced_artifact(artifact_name: str, phase: str, category: str, format_type: str, file_pattern: str) -> str:
    """Create fully enhanced artifact description"""

    display_name = artifact_name.replace('-', ' ').title()

    content = f"""# Name: {artifact_name}

{generate_executive_summary(artifact_name, category, phase)}

## Purpose & Scope

### Primary Purpose

This artifact serves as [define primary purpose based on artifact type - what problem does it solve, what decision does it support, what information does it provide].

### Scope

**In Scope**:
- [Define what is included in this artifact]
- [Key topics or areas covered]
- [Processes or systems documented]

**Out of Scope**:
- [Explicitly state what is NOT covered]
- [Related topics handled by other artifacts]
- [Boundaries of this artifact's remit]

### Target Audience

**Primary Audience**:
- [Define primary consumers and how they use this artifact]

**Secondary Audience**:
- [Define secondary audiences and their use cases]

## Document Information

**Format**: {format_type}

**File Pattern**: `{file_pattern}`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: [Define typical classification level - Public | Internal | Confidential | Restricted]

**Retention**: [Define retention period per organizational records management policy]

{generate_detailed_structure(artifact_name, format_type, category)}

## Best Practices

{chr(10).join(generate_comprehensive_best_practices(artifact_name, category, phase))}

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

"""

    # Add relevant standards
    standards_map = {
        "architecture": "**Architecture**: TOGAF, Zachman Framework, C4 Model, ArchiMate",
        "security": "**Security**: NIST Cybersecurity Framework, ISO 27001/27002, CIS Controls, MITRE ATT&CK",
        "privacy": "**Privacy**: GDPR, CCPA, ISO 29100, Privacy by Design",
        "risk": "**Risk Management**: ISO 31000, COSO ERM, FAIR, NIST RMF",
        "data": "**Data Management**: DAMA-DMBOK, DCAM, Data Governance Framework",
        "quality": "**Quality**: ISO 9001, CMMI, Six Sigma, TQM",
        "agile": "**Agile**: SAFe, Scrum Guide, Kanban Method, LeSS",
        "compliance": "**Compliance**: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP",
        "testing": "**Testing**: ISTQB, IEEE 829, ISO 29119",
        "project": "**Project Management**: PMBOK, PRINCE2, APM Body of Knowledge",
    }

    # Add relevant standards based on keywords
    added_standards = set()
    for keyword, standard in standards_map.items():
        if keyword in artifact_name or keyword in category.lower():
            content += f"{standard}\n"
            added_standards.add(keyword)

    # Add industry standards
    if not added_standards:
        content += "**General**: ISO 9001 (Quality), PMI Standards, Industry best practices\n"

    content += """
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
"""

    return content


def main():
    """Enhance all artifact descriptions with comprehensive professional content"""

    artifact_dir = Path("artifact_descriptions")

    if not artifact_dir.exists():
        print(f"Error: {artifact_dir} does not exist")
        return 1

    artifact_files = sorted(artifact_dir.glob("*.md"))
    print(f"Enhancing {len(artifact_files)} artifact descriptions with comprehensive professional content...\n")

    success = 0
    failed = 0

    for i, artifact_file in enumerate(artifact_files, 1):
        artifact_name = artifact_file.stem

        # Get phase and category from mapping, or use defaults
        phase, category = PHASE_CATEGORY_MAP.get(artifact_name, ("General", "General"))

        # Read original to get format and file pattern
        try:
            with open(artifact_file, 'r') as f:
                original_content = f.read()

            format_type = "Markdown"
            file_pattern = f"*.{artifact_name}.md"

            for line in original_content.split('\n'):
                if line.startswith('# Format:'):
                    format_type = line.replace('# Format:', '').strip()
                elif line.startswith('# File Pattern:'):
                    file_pattern = line.replace('# File Pattern:', '').strip()

            print(f"[{i}/{len(artifact_files)}] Enhancing: {artifact_name}...", end=" ")

            # Generate enhanced content
            enhanced_content = create_enhanced_artifact(
                artifact_name,
                phase,
                category,
                format_type,
                file_pattern
            )

            # Write enhanced content
            with open(artifact_file, 'w') as f:
                f.write(enhanced_content)

            print("✓")
            success += 1

        except Exception as e:
            print(f"✗ Error: {e}")
            failed += 1

    print(f"\n{'='*70}")
    print(f"Enhancement Complete:")
    print(f"  Successfully enhanced: {success}")
    print(f"  Failed: {failed}")
    print(f"\nAll artifacts now contain Big Five consulting-quality content.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
