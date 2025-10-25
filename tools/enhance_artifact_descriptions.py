#!/usr/bin/env python3
"""
Enhance artifact descriptions with professional, detailed content
Following Big Five consulting firm standards and industry best practices
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional


# Knowledge base of industry standards and frameworks
STANDARDS_FRAMEWORKS = {
    "architecture": ["TOGAF", "Zachman", "ArchiMate", "C4 Model"],
    "security": ["NIST CSF", "ISO 27001", "CIS Controls", "MITRE ATT&CK", "Zero Trust"],
    "compliance": ["SOC 2", "ISO 27001", "GDPR", "HIPAA", "PCI DSS", "FedRAMP"],
    "agile": ["SAFe", "Scrum", "Kanban", "LeSS"],
    "itil": ["ITIL 4", "ITSM"],
    "data": ["DAMA-DMBOK", "DCAM", "Data Governance Framework"],
    "risk": ["ISO 31000", "COSO ERM", "FAIR"],
    "quality": ["ISO 9001", "CMMI", "Six Sigma"],
    "privacy": ["GDPR", "CCPA", "Privacy by Design", "ISO 29100"],
    "ai": ["NIST AI RMF", "EU AI Act", "Responsible AI", "Model Cards"]
}


def get_comprehensive_purpose(artifact_name: str, basic_purpose: str, category: str, phase: str) -> str:
    """Generate comprehensive purpose section with executive summary"""

    purposes = {
        "portfolio-roadmap": """
## Executive Summary

The Portfolio Roadmap is a strategic planning artifact that provides a comprehensive view of all initiatives, programs, and projects across the organization's portfolio. It serves as the primary communication tool for executive leadership to understand portfolio composition, strategic alignment, resource allocation, and value delivery timelines.

## Purpose

This artifact enables portfolio-level decision-making by visualizing the sequence and interdependencies of strategic initiatives over a multi-year horizon. It integrates financial planning, resource capacity, strategic objectives, and risk considerations into a single cohesive view that supports investment prioritization and portfolio optimization.

## Strategic Value

- **Alignment**: Ensures all initiatives map directly to strategic objectives and business outcomes
- **Transparency**: Provides stakeholders with clear visibility into what's being delivered and when
- **Resource Optimization**: Enables capacity planning and prevents resource conflicts across initiatives
- **Risk Management**: Identifies dependencies, conflicts, and portfolio-level risks early
- **Value Maximization**: Supports data-driven prioritization based on strategic value and ROI
""",
        "business-case": """
## Executive Summary

The Business Case is a comprehensive decision-support document that provides the justification for initiating a project or initiative. It presents a thorough analysis of the business problem or opportunity, evaluates alternative solutions, quantifies expected benefits and costs, and recommends the optimal course of action with supporting evidence.

## Purpose

This artifact serves as the foundation for investment decisions by senior leadership and governance bodies. It establishes the financial and strategic rationale for committing organizational resources, defines success criteria, and creates accountability for benefits realization. The business case evolves throughout the initiative lifecycle as assumptions are validated and actual results are measured.

## Strategic Value

- **Investment Justification**: Provides evidence-based rationale for resource allocation decisions
- **Risk-Adjusted Returns**: Quantifies expected value considering probability and risk factors
- **Strategic Alignment**: Demonstrates contribution to organizational strategy and objectives
- **Benefits Accountability**: Establishes measurable outcomes and ownership for realization
- **Alternative Analysis**: Ensures optimal solution through rigorous evaluation of options
""",
        "threat-model": """
## Executive Summary

The Threat Model is a security engineering artifact that systematically identifies, evaluates, and prioritizes potential security threats to a system, application, or business process. Using structured methodologies like STRIDE, attack trees, or PASTA, it provides a comprehensive assessment of the attack surface, potential threat actors, attack vectors, and appropriate countermeasures.

## Purpose

This artifact enables proactive security by design rather than reactive vulnerability patching. It guides security architecture decisions, informs security control selection, prioritizes remediation efforts, and supports risk acceptance decisions. The threat model serves as a living document that evolves as the system changes or new threat intelligence emerges.

## Strategic Value

- **Proactive Security**: Identifies and mitigates threats before they can be exploited
- **Risk-Based Prioritization**: Focuses security investments on highest-impact vulnerabilities
- **Compliance Support**: Demonstrates due diligence for regulatory and audit requirements
- **Cost Efficiency**: Cheaper to address security in design than remediate post-deployment
- **Stakeholder Communication**: Translates technical risks into business impact for decision-makers
""",
        "openapi-specification": """
## Executive Summary

The OpenAPI Specification (OAS) is a standardized, machine-readable API contract that defines the complete interface of a RESTful API. Following the OpenAPI 3.0+ standard, it serves as both documentation and a source of truth for API design, enabling automated code generation, testing, validation, and integration across the API lifecycle.

## Purpose

This artifact enables API-first development by establishing a formal contract between API producers and consumers before implementation begins. It supports automated tooling for client SDK generation, server stub creation, validation testing, API gateway configuration, and interactive documentation generation. The specification evolves with the API through versioning and change management processes.

## Strategic Value

- **Design-First Approach**: Enables stakeholder validation before expensive implementation
- **Automation**: Drives code generation, testing, and documentation from single source
- **Contract Testing**: Ensures provider and consumer alignment through spec validation
- **Developer Experience**: Provides interactive documentation and client SDKs
- **API Governance**: Enforces consistency and standards across API portfolio
"""
    }

    # Return specific purpose if available, otherwise generate generic
    if artifact_name in purposes:
        return purposes[artifact_name]

    # Generate context-aware purpose based on category/phase
    return f"""
## Executive Summary

{basic_purpose}

## Purpose

This artifact is a critical deliverable within the {phase} phase, specifically supporting {category} activities. It provides structured information that enables stakeholders to make informed decisions, ensures consistency with organizational standards, and creates an auditable record of key decisions and outcomes.

## Strategic Value

- **Standardization**: Ensures consistent approach and quality across the organization
- **Decision Support**: Provides evidence-based inputs for leadership decisions
- **Compliance**: Meets regulatory, audit, and governance requirements
- **Knowledge Management**: Captures institutional knowledge in reusable format
- **Stakeholder Communication**: Facilitates alignment across diverse audiences
"""


def get_detailed_structure(artifact_name: str, format_type: str) -> Dict[str, Any]:
    """Generate detailed structure/schema for artifact"""

    structures = {
        "portfolio-roadmap": {
            "metadata": {
                "type": "object",
                "description": "Document metadata and version control",
                "properties": {
                    "version": "Semantic version (e.g., 1.2.0)",
                    "lastUpdated": "ISO 8601 timestamp of last modification",
                    "author": "Portfolio manager or PMO lead",
                    "reviewers": "Executive sponsors and key stakeholders",
                    "status": "Draft | Under Review | Approved | Published",
                    "approvalDate": "Formal approval date by governance body",
                    "confidentialityLevel": "Public | Internal | Confidential | Restricted"
                }
            },
            "executiveSummary": {
                "type": "object",
                "description": "High-level overview for C-suite consumption",
                "properties": {
                    "portfolioOverview": "Strategic context and portfolio composition",
                    "keyObjectives": "Top 3-5 strategic objectives being addressed",
                    "investmentSummary": "Total portfolio investment and distribution",
                    "criticalMilestones": "Major delivery milestones and dates",
                    "riskSummary": "Top portfolio risks and mitigation status"
                }
            },
            "strategicAlignment": {
                "type": "object",
                "description": "Linkage to organizational strategy",
                "properties": {
                    "strategicPillars": "Enterprise strategic themes or pillars",
                    "okrAlignment": "Mapping to organizational OKRs",
                    "valueStreams": "Affected business value streams",
                    "strategicImpact": "Expected strategic impact and outcomes"
                }
            },
            "initiatives": {
                "type": "array",
                "description": "Collection of portfolio initiatives with detailed information",
                "items": {
                    "initiativeId": "Unique identifier (e.g., INIT-2024-001)",
                    "name": "Initiative name following naming convention",
                    "description": "Business problem, opportunity, or strategic driver",
                    "category": "Strategic | Tactical | Operational | Compliance",
                    "status": "Proposed | Approved | Active | Paused | Completed | Cancelled",
                    "priority": "P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)",
                    "strategicObjectives": "Linked strategic objectives or OKRs",
                    "businessOwner": "Executive sponsor and business owner",
                    "portfolioManager": "PMO or portfolio manager assigned",
                    "timeline": {
                        "plannedStart": "ISO 8601 date",
                        "plannedEnd": "ISO 8601 date",
                        "actualStart": "ISO 8601 date (if started)",
                        "forecastedEnd": "Updated forecast based on progress",
                        "milestones": "Array of key milestone dates"
                    },
                    "financials": {
                        "totalBudget": "Total approved budget",
                        "spentToDate": "Actual spend to date",
                        "forecastToComplete": "Forecast remaining spend",
                        "capitalizationRatio": "Percentage eligible for capitalization",
                        "fundingSource": "Budget source or cost center"
                    },
                    "resources": {
                        "fteRequired": "Full-time equivalent headcount",
                        "keyRoles": "Critical roles and skill sets",
                        "vendorEngagement": "Third-party vendor involvement",
                        "resourceConstraints": "Known resource limitations or conflicts"
                    },
                    "benefits": {
                        "quantifiableBenefits": "NPV, IRR, ROI, cost savings",
                        "qualitativeBenefits": "Strategic, market, or capability benefits",
                        "realizationTimeline": "When benefits expected to materialize",
                        "kpis": "Key performance indicators to track"
                    },
                    "risks": {
                        "topRisks": "Top 5 risks with likelihood and impact",
                        "dependencies": "Critical dependencies on other initiatives",
                        "assumptions": "Key planning assumptions",
                        "constraints": "Known constraints or limitations"
                    }
                }
            },
            "roadmapVisualization": {
                "type": "object",
                "description": "Visual representation configuration",
                "properties": {
                    "timescale": "Monthly | Quarterly | Annual",
                    "horizon": "Planning horizon (e.g., 3 years, 5 years)",
                    "swimlanes": "Grouping strategy (by objective, value stream, etc.)",
                    "colorCoding": "Color scheme for status, priority, or category",
                    "dependencies": "Visualization of initiative dependencies"
                }
            },
            "resourcePlanning": {
                "type": "object",
                "description": "Portfolio-level resource allocation and capacity",
                "properties": {
                    "totalCapacity": "Organization FTE capacity by quarter",
                    "totalDemand": "Sum of initiative resource requirements",
                    "capacityUtilization": "Planned utilization percentage",
                    "overallocation": "Periods where demand exceeds capacity",
                    "skillGaps": "Identified skill shortages or needs"
                }
            },
            "governanceSchedule": {
                "type": "array",
                "description": "Portfolio review and governance events",
                "items": {
                    "reviewDate": "Scheduled review date",
                    "reviewType": "Monthly Review | Quarterly Planning | Annual Planning",
                    "participants": "Required attendees",
                    "scope": "Agenda and decision scope",
                    "decisionAuthority": "Who has approval authority"
                }
            }
        },

        "threat-model": {
            "metadata": {
                "type": "object",
                "description": "Threat model metadata and provenance",
                "properties": {
                    "version": "Semantic version of threat model",
                    "lastUpdated": "ISO 8601 timestamp",
                    "threatModelingMethodology": "STRIDE | PASTA | Attack Trees | OCTAVE",
                    "threatAnalysts": "Security engineers who performed analysis",
                    "reviewers": "Security architects and stakeholders",
                    "status": "Draft | Under Review | Approved | Requires Update",
                    "confidentialityLevel": "Typically Confidential or Restricted"
                }
            },
            "systemOverview": {
                "type": "object",
                "description": "High-level description of system being modeled",
                "properties": {
                    "systemName": "Name of system, application, or service",
                    "systemDescription": "Purpose, functionality, and business context",
                    "systemClassification": "Data classification and criticality level",
                    "deploymentModel": "Cloud | On-premises | Hybrid",
                    "userBase": "Internal | External | Both, estimated user count",
                    "dataTypes": "Types of data processed (PII, PHI, PCI, etc.)",
                    "regulatoryRequirements": "Applicable regulations (GDPR, HIPAA, etc.)"
                }
            },
            "architectureDiagrams": {
                "type": "object",
                "description": "Visual representations of system architecture",
                "properties": {
                    "dataFlowDiagram": "DFD showing data movement and trust boundaries",
                    "componentDiagram": "C4 or similar showing components and interactions",
                    "networkDiagram": "Network topology and security zones",
                    "authenticationFlow": "Authentication and authorization flows",
                    "trustBoundaries": "Clearly marked trust boundary crossings"
                }
            },
            "assets": {
                "type": "array",
                "description": "Assets requiring protection",
                "items": {
                    "assetId": "Unique asset identifier",
                    "assetName": "Human-readable asset name",
                    "assetType": "Data | Service | Infrastructure | Intellectual Property",
                    "description": "Detailed asset description",
                    "sensitivity": "Public | Internal | Confidential | Restricted",
                    "integrityRequirement": "Low | Medium | High | Critical",
                    "availabilityRequirement": "RTO and RPO requirements",
                    "confidentialityRequirement": "Protection level required",
                    "dataClassification": "According to data classification policy",
                    "complianceRequirements": "Regulatory requirements for this asset"
                }
            },
            "threatActors": {
                "type": "array",
                "description": "Potential adversaries and their characteristics",
                "items": {
                    "actorType": "Nation State | Organized Crime | Hacktivist | Insider | Script Kiddie",
                    "motivation": "Financial | Political | Espionage | Disruption | Prestige",
                    "sophistication": "Low | Medium | High | Advanced Persistent",
                    "resources": "Budget, tools, and capabilities available",
                    "likelihood": "Probability this actor targets the system"
                }
            },
            "threats": {
                "type": "array",
                "description": "Identified threats using selected methodology",
                "items": {
                    "threatId": "Unique threat identifier (e.g., THR-001)",
                    "threatName": "Descriptive threat name",
                    "strideCategory": "Spoofing | Tampering | Repudiation | Information Disclosure | Denial of Service | Elevation of Privilege",
                    "description": "Detailed threat scenario description",
                    "targetAsset": "Asset(s) threatened",
                    "threatActor": "Likely threat actor type",
                    "attackVector": "How the attack would be executed",
                    "prerequisites": "Conditions required for exploit",
                    "mitreAttackTechniques": "Mapped MITRE ATT&CK techniques",
                    "likelihood": "Probability of occurrence (1-5)",
                    "impact": "Business impact if exploited (1-5)",
                    "riskScore": "Likelihood × Impact",
                    "existingControls": "Current mitigations in place",
                    "controlEffectiveness": "How effective existing controls are",
                    "residualRisk": "Risk after existing controls",
                    "recommendedControls": "Additional controls to implement",
                    "priority": "P0 | P1 | P2 | P3 based on risk",
                    "status": "Open | In Progress | Mitigated | Accepted | Not Applicable"
                }
            },
            "securityControls": {
                "type": "array",
                "description": "Security controls mapped to threats",
                "items": {
                    "controlId": "Unique control identifier",
                    "controlName": "Security control name",
                    "controlType": "Preventive | Detective | Corrective | Deterrent",
                    "implementationStatus": "Planned | In Progress | Implemented | Verified",
                    "threatsAddressed": "Array of threat IDs mitigated",
                    "controlDescription": "How control works",
                    "implementationOwner": "Team responsible for implementation",
                    "verificationMethod": "How effectiveness is verified",
                    "cost": "Implementation and operational cost estimate",
                    "effectivenessRating": "How effective control is (1-5)"
                }
            },
            "attackScenarios": {
                "type": "array",
                "description": "End-to-end attack chain scenarios",
                "items": {
                    "scenarioName": "Descriptive name",
                    "attackChain": "Sequence of MITRE ATT&CK techniques",
                    "initialAccess": "How attacker gains initial foothold",
                    "escalation": "How privileges are escalated",
                    "impact": "Final impact achieved",
                    "indicatorsOfCompromise": "IOCs that would detect this attack",
                    "detectionCoverage": "Percentage of attack chain detectable"
                }
            },
            "assumptions": {
                "type": "array",
                "description": "Assumptions made during threat modeling",
                "items": "Documented assumptions that may affect threat analysis"
            },
            "outOfScope": {
                "type": "array",
                "description": "Explicitly excluded from threat model scope",
                "items": "Components, threats, or scenarios not covered"
            },
            "reviewSchedule": {
                "type": "object",
                "description": "Threat model maintenance schedule",
                "properties": {
                    "reviewFrequency": "How often to review (e.g., quarterly)",
                    "triggers": "Events requiring immediate review (architecture change, breach, etc.)",
                    "nextReviewDate": "Scheduled next review date",
                    "threatIntelligenceIntegration": "How threat intel feeds into updates"
                }
            }
        }
    }

    # Return specific structure if available
    if artifact_name in structures:
        return structures[artifact_name]

    # Return generic structure based on format
    return get_generic_structure(format_type)


def get_generic_structure(format_type: str) -> Dict[str, Any]:
    """Generate generic structure for artifacts without specific templates"""

    if format_type in ["JSON", "YAML"]:
        return {
            "metadata": {
                "type": "object",
                "description": "Document control and versioning information",
                "properties": {
                    "version": "Document version using semantic versioning",
                    "lastUpdated": "ISO 8601 timestamp of last update",
                    "author": "Primary author name and role",
                    "reviewers": "List of reviewers and approvers",
                    "status": "Draft | Review | Approved | Published | Deprecated",
                    "confidentialityLevel": "Classification level per data policy"
                }
            },
            "content": {
                "type": "object",
                "description": "Primary content of the artifact",
                "properties": {
                    "overview": "Executive summary and purpose",
                    "scope": "What is covered and what is excluded",
                    "details": "Detailed content specific to artifact type",
                    "references": "Related documents and external references"
                }
            },
            "approvals": {
                "type": "array",
                "description": "Approval history and sign-offs",
                "items": {
                    "approver": "Name and role of approver",
                    "date": "ISO 8601 approval date",
                    "comments": "Approval comments or conditions"
                }
            },
            "changeHistory": {
                "type": "array",
                "description": "Audit trail of changes",
                "items": {
                    "version": "Version number",
                    "date": "ISO 8601 change date",
                    "author": "Who made the change",
                    "changes": "Description of changes made",
                    "impact": "Impact assessment of changes"
                }
            }
        }

    return {}


def get_best_practices(artifact_name: str, category: str) -> List[str]:
    """Generate best practices specific to artifact type"""

    practices = {
        "portfolio-roadmap": [
            "Update monthly at minimum; weekly for active planning cycles",
            "Use consistent time scaling (quarters recommended for strategic roadmaps)",
            "Color-code by status, priority, or strategic pillar for quick scanning",
            "Include dependency arrows to show initiative interdependencies",
            "Separate committed vs. planned initiatives visually",
            "Show resource capacity constraints alongside demand",
            "Include financial burn-up/burn-down for each initiative",
            "Tag regulatory or compliance-driven initiatives clearly",
            "Version control roadmap and maintain historical snapshots",
            "Review with executive sponsors before broad distribution",
            "Use swim lanes to group by value stream, business unit, or objective",
            "Include legend explaining symbols, colors, and conventions used",
            "Show critical path and any path-critical initiatives",
            "Maintain separate views for different audiences (board vs. execution teams)",
            "Document assumptions behind timeline and resource estimates"
        ],
        "threat-model": [
            "Perform threat modeling during design phase, not after implementation",
            "Include representatives from security, development, and operations",
            "Use structured methodology (STRIDE recommended for most systems)",
            "Document trust boundaries explicitly in all diagrams",
            "Map threats to MITRE ATT&CK framework for common language",
            "Prioritize threats by risk score (likelihood × impact)",
            "Focus on threats that bypass existing controls",
            "Consider both technical and business/process threats",
            "Review threat model when architecture changes significantly",
            "Integrate with vulnerability management and incident response",
            "Track control implementation status and effectiveness",
            "Use attack trees for complex attack chain analysis",
            "Consider insider threats, not just external actors",
            "Document assumptions and out-of-scope items explicitly",
            "Update based on threat intelligence and actual incidents",
            "Use automated tools to keep data flow diagrams synchronized with code"
        ],
        "business-case": [
            "Start with clear problem statement before jumping to solutions",
            "Include do-nothing/status-quo as one option for comparison",
            "Use NPV and IRR for multi-year financial analysis",
            "Include sensitivity analysis showing impact of assumption changes",
            "Separate one-time costs from ongoing operational costs",
            "Account for opportunity cost of resources and capital",
            "Include risk-adjusted returns, not just best-case scenarios",
            "Map benefits to specific metrics and assign ownership",
            "Define clear success criteria and how they'll be measured",
            "Include benefits realization timeline and tracking plan",
            "Consider total cost of ownership, not just initial investment",
            "Involve finance early to align on assumptions and methodology",
            "Document key assumptions and their confidence levels",
            "Include options analysis with weighted criteria",
            "Plan for regular business case updates as actuals come in",
            "Address regulatory, compliance, or strategic imperatives separately from ROI"
        ]
    }

    # Return specific practices or generic based on category
    if artifact_name in practices:
        return practices[artifact_name]

    # Generic best practices by category
    category_practices = {
        "Governance & Planning": [
            "Maintain version control and change history",
            "Review and update on regular cadence",
            "Ensure executive sponsorship and approval",
            "Distribute to all relevant stakeholders",
            "Use templates for consistency"
        ],
        "Security": [
            "Follow defense-in-depth principles",
            "Map to industry frameworks (NIST, ISO 27001)",
            "Include both preventive and detective controls",
            "Document risk acceptance decisions",
            "Review after security incidents"
        ]
    }

    return category_practices.get(category, [
        "Use industry-standard templates and formats",
        "Review by subject matter experts before finalization",
        "Version control and maintain change history",
        "Ensure appropriate approvals and sign-offs",
        "Store in centralized, accessible repository"
    ])


def get_quality_criteria(artifact_name: str) -> List[str]:
    """Define quality criteria for artifact acceptance"""

    return [
        "**Completeness**: All required sections populated with sufficient detail",
        "**Accuracy**: Information verified and validated by subject matter experts",
        "**Clarity**: Written in clear, unambiguous language appropriate for audience",
        "**Consistency**: Aligns with organizational standards and other artifacts",
        "**Traceability**: References to source documents and related artifacts included",
        "**Timeliness**: Reflects current state; not based on outdated information",
        "**Approval**: Reviewed and approved by designated stakeholders",
        "**Accessibility**: Stored in accessible location with appropriate permissions",
        "**Maintainability**: Can be updated as conditions change",
        "**Compliance**: Meets regulatory and policy requirements"
    ]


def get_common_pitfalls(artifact_name: str) -> List[str]:
    """Document common mistakes and how to avoid them"""

    pitfalls = {
        "portfolio-roadmap": [
            "**Over-optimistic timelines**: Build in buffer for unknowns; use historical data for estimates",
            "**Ignoring dependencies**: Map all cross-initiative dependencies before committing dates",
            "**Resource overallocation**: Don't plan for >85% capacity utilization; leave room for BAU",
            "**Lack of stakeholder buy-in**: Review with sponsors and impacted teams before finalizing",
            "**Static roadmap syndrome**: Roadmaps must be living documents updated regularly",
            "**Too much detail**: Keep strategic roadmaps high-level; detailed plans belong elsewhere",
            "**Ignoring capacity constraints**: Balance initiative demand against available capacity",
            "**Missing governance cadence**: Establish clear review and update schedule",
            "**Unclear priorities**: Every initiative should have clear priority and rationale",
            "**No flexibility**: Build in strategic buffers for emergent opportunities"
        ],
        "threat-model": [
            "**Treating as one-time activity**: Threat modeling is continuous, not point-in-time",
            "**Too much detail too early**: Start high-level, drill down on high-risk areas",
            "**Ignoring business context**: Technical threats must connect to business impact",
            "**Analysis paralysis**: Focus on actionable threats, not theoretical possibilities",
            "**No follow-through**: Identify threats but never implement controls",
            "**Missing trust boundaries**: These are critical for accurate threat identification",
            "**Ignoring insider threats**: Internal actors can be significant threat source",
            "**No threat actor analysis**: Understanding adversaries helps prioritize defenses",
            "**Stale threat models**: Update when architecture changes or new threats emerge",
            "**Lack of executive support**: Security architecture needs leadership backing"
        ]
    }

    return pitfalls.get(artifact_name, [
        "**Insufficient detail**: Artifact lacks enough information to be useful",
        "**Outdated information**: Based on old assumptions or data",
        "**No clear ownership**: Unclear who is responsible for maintenance",
        "**Poor version control**: Changes not tracked, can't revert",
        "**Missing approvals**: Artifact used without proper authorization",
        "**Inconsistent format**: Doesn't follow organizational standards",
        "**Inadequate review**: Not reviewed by appropriate subject matter experts",
        "**Accessibility issues**: Stored where stakeholders can't find or access it"
    ])


def enhance_artifact_file(file_path: Path, category: str, phase: str) -> bool:
    """Enhance a single artifact description file"""

    try:
        # Read existing content
        with open(file_path, 'r') as f:
            content = f.read()

        # Parse existing sections
        artifact_name = None
        basic_purpose = ""
        format_type = ""
        file_pattern = ""

        for line in content.split('\n'):
            if line.startswith('# Name:'):
                artifact_name = line.replace('# Name:', '').strip()
            elif line.startswith('# Purpose:'):
                basic_purpose = content.split('# Purpose:')[1].split('#')[0].strip()
            elif line.startswith('# Format:'):
                format_type = line.replace('# Format:', '').strip()
            elif line.startswith('# File Pattern:'):
                file_pattern = line.replace('# File Pattern:', '').strip()

        if not artifact_name:
            return False

        # Build enhanced content
        enhanced = f"""# Name: {artifact_name}

{get_comprehensive_purpose(artifact_name, basic_purpose, category, phase)}

## Format

**Primary Format**: {format_type}

**File Pattern**: `{file_pattern}`

**Naming Convention**: Follow pattern `{{project}}.{artifact_name}.{{ext}}` or as specified above

**Storage Location**: Centralized document repository with version control

## Document Structure
"""

        # Add structure/schema
        structure = get_detailed_structure(artifact_name, format_type)
        if structure:
            enhanced += "\n### Required Sections\n\n"
            for section_name, section_info in structure.items():
                if isinstance(section_info, dict):
                    enhanced += f"#### {section_name.replace('_', ' ').title()}\n\n"
                    enhanced += f"**Type**: {section_info.get('type', 'object')}\n\n"
                    enhanced += f"**Description**: {section_info.get('description', '')}\n\n"

                    if 'properties' in section_info:
                        enhanced += "**Properties**:\n\n"
                        for prop, desc in section_info['properties'].items():
                            if isinstance(desc, str):
                                enhanced += f"- `{prop}`: {desc}\n"
                            elif isinstance(desc, dict):
                                enhanced += f"- `{prop}`: {desc.get('description', prop)}\n"
                        enhanced += "\n"

                    if 'items' in section_info:
                        enhanced += "**Array Items**:\n\n"
                        items = section_info['items']
                        if isinstance(items, dict):
                            for key, value in items.items():
                                enhanced += f"- `{key}`: {value}\n"
                        else:
                            enhanced += f"{items}\n"
                        enhanced += "\n"

        # Add best practices
        best_practices = get_best_practices(artifact_name, category)
        enhanced += "\n## Best Practices\n\n"
        for practice in best_practices:
            enhanced += f"- {practice}\n"

        # Add quality criteria
        enhanced += "\n## Quality Criteria\n\n"
        for criterion in get_quality_criteria(artifact_name):
            enhanced += f"- {criterion}\n"

        # Add common pitfalls
        pitfalls = get_common_pitfalls(artifact_name)
        enhanced += "\n## Common Pitfalls\n\n"
        for pitfall in pitfalls:
            enhanced += f"- {pitfall}\n"

        # Add related standards
        enhanced += "\n## Related Standards & Frameworks\n\n"
        standards_added = False

        # Map artifact to relevant standards
        if any(x in artifact_name for x in ['architecture', 'design', 'topology']):
            enhanced += f"- **Architecture Frameworks**: {', '.join(STANDARDS_FRAMEWORKS['architecture'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['security', 'threat', 'risk', 'vulnerability']):
            enhanced += f"- **Security Standards**: {', '.join(STANDARDS_FRAMEWORKS['security'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['compliance', 'audit', 'control', 'soc', 'iso']):
            enhanced += f"- **Compliance Frameworks**: {', '.join(STANDARDS_FRAMEWORKS['compliance'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['privacy', 'gdpr', 'consent', 'dpia', 'pia']):
            enhanced += f"- **Privacy Regulations**: {', '.join(STANDARDS_FRAMEWORKS['privacy'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['data', 'model', 'schema', 'lineage']):
            enhanced += f"- **Data Management**: {', '.join(STANDARDS_FRAMEWORKS['data'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['ai', 'ml', 'model-card', 'bias']):
            enhanced += f"- **AI/ML Governance**: {', '.join(STANDARDS_FRAMEWORKS['ai'])}\n"
            standards_added = True
        if any(x in artifact_name for x in ['agile', 'sprint', 'increment']):
            enhanced += f"- **Agile Frameworks**: {', '.join(STANDARDS_FRAMEWORKS['agile'])}\n"
            standards_added = True

        if not standards_added:
            enhanced += "- **ISO 9001**: Quality management systems\n"
            enhanced += "- **Industry Best Practices**: Consult relevant industry standards for this domain\n"

        # Add integration points
        enhanced += "\n## Integration Points\n\n"
        enhanced += "**Upstream Dependencies** (inputs required):\n- TBD - Identify artifacts that must exist before this one\n\n"
        enhanced += "**Downstream Consumers** (who uses this):\n- TBD - Identify artifacts or processes that consume this\n\n"
        enhanced += "**Related Artifacts**:\n- TBD - List closely related artifact types\n\n"

        # Add approval process
        enhanced += "\n## Review & Approval Process\n\n"
        enhanced += "**Reviewers**:\n"
        enhanced += "- Subject Matter Expert: Domain specialist review for accuracy\n"
        enhanced += "- Architecture Review: For alignment with standards and patterns\n"
        enhanced += "- Security Review: For artifacts with security implications\n"
        enhanced += "- Compliance Review: For artifacts subject to regulatory requirements\n\n"
        enhanced += "**Approvers**:\n"
        enhanced += "- Primary Approver: [Role to be defined based on artifact type]\n"
        enhanced += "- Secondary Approver: [For high-impact or cross-functional artifacts]\n\n"
        enhanced += "**Process**:\n"
        enhanced += "1. Author completes draft following template\n"
        enhanced += "2. Self-review against quality criteria checklist\n"
        enhanced += "3. Submit for peer review by SMEs\n"
        enhanced += "4. Incorporate feedback and address comments\n"
        enhanced += "5. Route to designated approvers\n"
        enhanced += "6. Obtain formal approval sign-off\n"
        enhanced += "7. Publish to centralized repository\n"
        enhanced += "8. Communicate availability to stakeholders\n\n"

        # Add templates section
        enhanced += "\n## Templates & Examples\n\n"
        enhanced += f"**Template Location**: `templates/{artifact_name}-template.{format_type.lower()}`\n\n"
        enhanced += f"**Example Artifacts**: `examples/{artifact_name}-example.{format_type.lower()}`\n\n"
        enhanced += "**Starter Checklist**:\n"
        enhanced += "- [ ] Review template and customize for your context\n"
        enhanced += "- [ ] Gather required input information and dependencies\n"
        enhanced += "- [ ] Complete all mandatory sections\n"
        enhanced += "- [ ] Validate against quality criteria\n"
        enhanced += "- [ ] Obtain necessary reviews\n"
        enhanced += "- [ ] Secure formal approvals\n"
        enhanced += "- [ ] Publish and communicate\n\n"

        # Add maintenance section
        enhanced += "\n## Maintenance & Updates\n\n"
        enhanced += "**Update Triggers**:\n"
        enhanced += "- Scheduled reviews (define frequency based on artifact volatility)\n"
        enhanced += "- Significant organizational or project changes\n"
        enhanced += "- Regulatory or compliance requirement changes\n"
        enhanced += "- Stakeholder requests or identified deficiencies\n"
        enhanced += "- Post-implementation reviews revealing needed updates\n\n"
        enhanced += "**Version Control**:\n"
        enhanced += "- Use semantic versioning (MAJOR.MINOR.PATCH)\n"
        enhanced += "- MAJOR: Significant restructuring or scope changes\n"
        enhanced += "- MINOR: New sections or substantial additions\n"
        enhanced += "- PATCH: Corrections, clarifications, minor updates\n\n"
        enhanced += "**Change Log**:\n"
        enhanced += "Maintain detailed change log including:\n"
        enhanced += "- Version number and date\n"
        enhanced += "- Author of changes\n"
        enhanced += "- Description of what changed and why\n"
        enhanced += "- Impact assessment\n"
        enhanced += "- Approver of changes\n\n"

        # Add metadata tags for producers/consumers
        enhanced += "\n## Metadata\n\n"
        enhanced += "**Typical Producers**:\n- TBD - Roles or teams that typically create this artifact\n\n"
        enhanced += "**Typical Consumers**:\n- TBD - Roles or teams that typically use this artifact\n\n"
        enhanced += "**Artifact Category**: " + category + "\n\n"
        enhanced += "**Lifecycle Phase**: " + phase + "\n\n"
        enhanced += "**Confidentiality Classification**: [Define based on content sensitivity]\n\n"
        enhanced += "**Retention Period**: [Define based on regulatory and business requirements]\n\n"

        # Write enhanced content
        with open(file_path, 'w') as f:
            f.write(enhanced)

        return True

    except Exception as e:
        print(f"Error enhancing {file_path}: {e}")
        return False


def main():
    """Enhance all artifact description files"""

    # Map files to their categories and phases
    artifact_metadata = {
        "portfolio-roadmap": {"category": "Governance & Planning", "phase": "0. Portfolio, Governance, and Delivery Ops"},
        "business-case": {"category": "Business & Strategy", "phase": "1. Inception / Strategy"},
        "threat-model": {"category": "Security Architecture", "phase": "3. Architecture"},
        "openapi-specification": {"category": "Application and Integration", "phase": "3. Architecture"},
        # Add more as needed - using these as examples for now
    }

    artifact_dir = Path("artifact_descriptions")

    if not artifact_dir.exists():
        print(f"Error: {artifact_dir} does not exist")
        return 1

    artifact_files = sorted(artifact_dir.glob("*.md"))
    print(f"Enhancing {len(artifact_files)} artifact descriptions...\n")

    success = 0
    failed = 0

    for i, artifact_file in enumerate(artifact_files, 1):
        artifact_name = artifact_file.stem

        # Get metadata or use defaults
        metadata = artifact_metadata.get(artifact_name, {
            "category": "General",
            "phase": "General"
        })

        print(f"[{i}/{len(artifact_files)}] Enhancing: {artifact_name}...", end=" ")

        if enhance_artifact_file(artifact_file, metadata["category"], metadata["phase"]):
            print("✓")
            success += 1
        else:
            print("✗")
            failed += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Successfully enhanced: {success}")
    print(f"  Failed: {failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
