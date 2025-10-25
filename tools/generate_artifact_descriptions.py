#!/usr/bin/env python3
"""
Generate artifact description files from deliverables JSON
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

# Deliverables data
DELIVERABLES = [
  {
    "phase": "0. Portfolio, Governance, and Delivery Ops",
    "category": "Governance & Planning",
    "deliverables": [
      "Portfolio roadmap",
      "Initiative charter",
      "Epic charter",
      "Governance charter",
      "Steering committee minutes",
      "Go/no-go minutes",
      "RAID log",
      "Decision log",
      "ADR index",
      "Change log",
      "Exception log",
      "Program increment plan",
      "Sprint goals",
      "Velocity and burndown reports",
      "Resource plan",
      "Skills matrix",
      "Staffing plan",
      "RACI per workstream",
      "Vendor management pack",
      "Third-party risk assessments",
      "SIG questionnaires",
      "Vendor scorecards",
      "Budget forecast",
      "Capitalization policy",
      "Time allocation worksheets",
      "Benefits realization plan",
      "Benefits realization report"
    ]
  },
  {
    "phase": "1. Inception / Strategy",
    "category": "Business & Strategy",
    "deliverables": [
      "Vision statement",
      "Mission statement",
      "Product strategy",
      "OKR definitions",
      "KPI framework",
      "Business case",
      "ROI model",
      "Feasibility study",
      "Market analysis",
      "Competitive analysis",
      "Stakeholder map",
      "Engagement plan",
      "Communication plan",
      "Change control plan",
      "Risk appetite statement",
      "Enterprise risk register"
    ]
  },
  {
    "phase": "2. Requirements and Analysis",
    "category": "Requirements & Analysis",
    "deliverables": [
      "Product Requirements Document (PRD)",
      "Functional Requirements Specification (FRS)",
      "System Requirements Specification (SRS)",
      "Non-Functional Requirements (NFR) matrix",
      "User stories",
      "Acceptance criteria",
      "Use-case models",
      "Use-case diagrams",
      "Business process models (BPMN, flowcharts)",
      "Data flow diagrams (DFDs)",
      "Context diagrams",
      "Domain model",
      "Business rules catalog",
      "Requirements traceability matrix",
      "Regulatory mapping (SOC2, ISO, NIST, HIPAA, PCI, FedRAMP)",
      "Privacy Impact Assessment (PIA)",
      "Data Protection Impact Assessment (DPIA)",
      "Records of Processing Activities (RoPA)",
      "Data map",
      "Consent models",
      "Consent receipts",
      "DSAR playbooks",
      "Cookie policy inventory",
      "CMP configurations",
      "Retention schedule",
      "Legal hold procedures",
      "Accessibility requirements",
      "VPAT/ACR results"
    ]
  },
  {
    "phase": "3. Architecture",
    "category": "High-Level and Platform",
    "deliverables": [
      "Architecture vision",
      "Architecture overview",
      "Logical architecture diagram",
      "Physical architecture diagram",
      "Network topology diagram",
      "Deployment topology diagram",
      "Cloud landing zone design",
      "Capability model",
      "Bounded context map",
      "Team topology map",
      "Target-state evolution map",
      "Tenancy and isolation model",
      "Multi-region active-active plan",
      "Technology standards catalog",
      "Patterns and anti-patterns library",
      "Golden path guide",
      "Platform services catalog",
      "Architecture review board minutes",
      "Architecture waivers",
      "Architecture approvals"
    ]
  },
  {
    "phase": "3. Architecture",
    "category": "Application and Integration",
    "deliverables": [
      "Component model",
      "Service decomposition",
      "Service dependency graph",
      "Interface Control Document (ICD)",
      "Data contracts",
      "Schema evolution policy",
      "OpenAPI specification",
      "AsyncAPI specification",
      "GraphQL schema",
      "gRPC proto files",
      "Event schemas (Avro, JSON, Protobuf)",
      "Topic and queue catalog",
      "API versioning policy",
      "Deprecation policy",
      "Rate limiting policy",
      "Idempotency and replay protection policy",
      "Error taxonomy"
    ]
  },
  {
    "phase": "3. Architecture",
    "category": "Data and Information",
    "deliverables": [
      "Enterprise data model",
      "Logical data model",
      "Physical data model",
      "ER diagrams",
      "Data dictionaries",
      "Metadata catalogs",
      "Database schema DDL",
      "Migration scripts (Liquibase/Flyway)",
      "Data lineage maps",
      "Data quality rules",
      "Great Expectations suites",
      "Data freshness SLAs",
      "Data retention plan",
      "Data residency plan",
      "Backup and recovery plan",
      "Semantic layer definitions (dbt, LookML)"
    ]
  },
  {
    "phase": "3. Architecture",
    "category": "Security Architecture",
    "deliverables": [
      "Threat model (STRIDE, attack trees)",
      "Security architecture diagram",
      "Zero trust design",
      "IAM design",
      "RBAC/ABAC matrix",
      "SoD matrix",
      "Access recertification plan",
      "Encryption and key management design",
      "Certificate policy",
      "Key ceremony records",
      "HSM procedures",
      "Security detections catalog (MITRE ATT&CK)",
      "Red team reports",
      "Purple team reports",
      "Adversary emulation documents"
    ]
  },
  {
    "phase": "4. Design",
    "category": "Design & UX",
    "deliverables": [
      "Information architecture",
      "User journeys",
      "Storyboards",
      "Wireframes",
      "High-fidelity mockups",
      "Interactive prototypes",
      "Content strategy",
      "Microcopy guides",
      "Localization plan",
      "Locale files",
      "Pseudo-localization reports",
      "Accessibility audits",
      "Sequence diagrams",
      "State diagrams",
      "Class diagrams",
      "Component diagrams",
      "Configuration design",
      "Deployment diagram",
      "Monitoring and observability design",
      "Performance strategy",
      "Caching strategy",
      "Error budget policy",
      "Service-level objectives (SLOs)"
    ]
  },
  {
    "phase": "5. Implementation",
    "category": "Development",
    "deliverables": [
      "Source code repositories",
      "Coding standards and style guides",
      "Secure coding checklist",
      "Build scripts",
      "Dockerfiles",
      "Docker Compose manifests",
      "Helm charts",
      "Kustomize manifests",
      "Service configuration files",
      "Feature flag registry",
      "Kill-switch designs",
      "Circuit breaker configurations",
      "Static analysis reports",
      "Code coverage reports",
      "Dependency graph",
      "Software Bill of Materials (SBOM)",
      "Provenance attestations (in-toto)",
      "Cosign signatures",
      "Commit logs",
      "Pull request summaries",
      "Code review records",
      "Version tags",
      "Release notes",
      "Changelogs"
    ]
  },
  {
    "phase": "6. Testing",
    "category": "Quality Assurance",
    "deliverables": [
      "Test strategy",
      "Test plan",
      "Test case specifications",
      "Test data specification",
      "Synthetic data generation plan",
      "Automated test scripts",
      "Regression test suite",
      "Performance test plan",
      "Load test report",
      "Security test results (SAST, DAST, IAST)",
      "Penetration testing report",
      "Chaos engineering experiments",
      "UAT plan",
      "UAT sign-off document",
      "Traceability matrix",
      "Defect log",
      "Triage rules"
    ]
  },
  {
    "phase": "7. Deployment and Release",
    "category": "Release Management",
    "deliverables": [
      "Release plan",
      "Cutover checklist",
      "Deployment plan (blue-green, canary, rolling)",
      "Rollback plan",
      "Feature rollback playbooks",
      "Runbooks",
      "Playbooks",
      "CI/CD pipeline definitions",
      "Promotion workflows",
      "Artifact registry policies",
      "SBOM verification reports",
      "CAB approvals",
      "Release risk assessment",
      "Release certification",
      "Post-implementation review"
    ]
  },
  {
    "phase": "8. Operations, SRE, and Maintenance",
    "category": "Operations & Reliability",
    "deliverables": [
      "Operations manual",
      "Standard operating procedures (SOPs)",
      "On-call handbook",
      "Escalation matrix",
      "Monitoring dashboards",
      "Alert catalogs",
      "Runbooks",
      "Telemetry schema",
      "Logging taxonomy",
      "Incident management plan",
      "Incident reports",
      "Root cause analyses (RCA)",
      "Status page communication templates",
      "Capacity plan",
      "Scaling policies",
      "Disaster recovery runbooks",
      "DR test reports",
      "Backup verification logs",
      "Vulnerability management plan",
      "Exception register",
      "Configuration drift reports",
      "Toil reduction plan",
      "Production hygiene checklist"
    ]
  },
  {
    "phase": "9. Data Engineering and Analytics",
    "category": "Data Platform",
    "deliverables": [
      "Data product specification",
      "Ownership charters",
      "ETL/ELT specifications",
      "DAG definitions",
      "Scheduling SLAs",
      "Data lineage tracking",
      "Metric catalog",
      "Reverse ETL playbooks",
      "Sync contracts",
      "Analytics model documentation",
      "Reproducibility checklists"
    ]
  },
  {
    "phase": "10. AI/ML and Model Ops",
    "category": "Model Development & Governance",
    "deliverables": [
      "AI use-case inventory",
      "Model governance policy",
      "AI ethics and bias assessment",
      "Dataset documentation",
      "Training data cards",
      "Experiment tracking logs",
      "Hyperparameter configurations",
      "Model cards",
      "Evaluation protocols",
      "Explainability reports (SHAP, LIME)",
      "Bias and fairness reports",
      "Model registry entries",
      "Model risk assessments",
      "Drift detection reports",
      "Shadow/canary deployment scorecards",
      "Feature store contracts",
      "GenAI safety evaluations",
      "Red-teaming reports",
      "Prompt engineering policy",
      "Safety filter configurations"
    ]
  },
  {
    "phase": "11. Product Management and GTM",
    "category": "Product & Market",
    "deliverables": [
      "Positioning documents",
      "Messaging frameworks",
      "Competitive analysis",
      "Battlecards",
      "Pricing and packaging strategy",
      "Discount guardrails",
      "Price books",
      "ROI/TCO calculators",
      "Product launch plan",
      "GTM checklist",
      "Sales enablement kits",
      "Demo scripts",
      "Reference architectures",
      "Solution briefs",
      "Customer onboarding plan",
      "Success plan templates",
      "QBR templates",
      "Renewal playbooks",
      "Trust center content plan"
    ]
  },
  {
    "phase": "12. CI/CD, Build, and Provenance",
    "category": "Build & Release Automation",
    "deliverables": [
      "Pipeline architecture diagram",
      "Pipeline definitions",
      "Build reproducibility notes",
      "Artifact store policies",
      "SBOM policy",
      "Provenance chain documentation (SLSA)",
      "Environment promotion rules",
      "Automated quality gates"
    ]
  },
  {
    "phase": "13. Infrastructure and Platform Engineering",
    "category": "Platform Engineering",
    "deliverables": [
      "Environment matrix",
      "Promotion rules",
      "IaC module registry",
      "Network policies",
      "Firewall rules",
      "Service mesh configurations",
      "DNS configurations",
      "Load balancer configurations",
      "CDN and WAF configs",
      "DDoS posture assessments",
      "Cost tagging policy",
      "Showback and chargeback reports",
      "FinOps dashboards",
      "Secrets management policy",
      "Secret rotation schedule"
    ]
  },
  {
    "phase": "14. Security, Privacy, Audit, and Compliance",
    "category": "Governance, Risk & Compliance",
    "deliverables": [
      "Security policy library",
      "Baseline hardening guides",
      "Secure coding policy",
      "Vulnerability disclosure policy",
      "Bug bounty brief",
      "SOC 2 control implementation matrix",
      "ISO 27001 mapping",
      "Control test evidence packs",
      "Audit readiness workbook",
      "Remediation tracker",
      "Access review logs",
      "SoD conflict matrices",
      "Export control screening",
      "ECCN classification",
      "IP register",
      "Trademark guidance",
      "Open source license BoM",
      "Contributor License Agreements (CLAs)",
      "Attribution files"
    ]
  },
  {
    "phase": "15. Documentation, Support, and Training",
    "category": "Knowledge & Enablement",
    "deliverables": [
      "README",
      "CONTRIBUTING guide",
      "Developer handbook",
      "Onboarding guide",
      "User manuals",
      "Admin guides",
      "Installation guides",
      "Upgrade guides",
      "Troubleshooting trees",
      "FAQ",
      "Knowledge base articles",
      "Customer communication templates",
      "Training curriculum",
      "Certification exams",
      "Labs and workshops",
      "API catalogs",
      "Glossary and taxonomy index"
    ]
  },
  {
    "phase": "16. Mobile, Desktop, and Distribution",
    "category": "Client Distribution",
    "deliverables": [
      "App store metadata",
      "Privacy labels",
      "Code signing records",
      "Notarization records",
      "Installer manifests",
      "Auto-update policies",
      "Crash reporting taxonomy",
      "Crash triage playbooks"
    ]
  },
  {
    "phase": "17. HR, Access, and Lifecycle",
    "category": "Access & Identity",
    "deliverables": [
      "Role catalog",
      "RBAC/ABAC policy",
      "Onboarding checklist",
      "Offboarding checklist",
      "Joiner-Mover-Leaver workflows",
      "Quarterly access reviews",
      "Approval evidence"
    ]
  },
  {
    "phase": "18. Performance, Capacity, and Cost",
    "category": "Performance & Optimization",
    "deliverables": [
      "Load profiles",
      "Performance test results",
      "Capacity models",
      "Scaling policies",
      "Caching tiers",
      "Eviction policies",
      "Cloud cost optimization reports",
      "Cost anomaly alerts",
      "Sustainability reports",
      "Carbon footprint analysis"
    ]
  },
  {
    "phase": "19. Closure and Archival",
    "category": "Project Closure",
    "deliverables": [
      "Operational acceptance certificate",
      "Lessons learned document",
      "Post-mortem report",
      "Continuous improvement plan",
      "Decommissioning plan",
      "Archival plan",
      "Data export procedures",
      "Customer data return procedures"
    ]
  },
  {
    "phase": "20. Public-Facing and Legal",
    "category": "Legal & External",
    "deliverables": [
      "Terms of Service",
      "Privacy Policy",
      "Cookie Policy",
      "Acceptable Use Policy",
      "SLA/SLO schedules",
      "Uptime methodology",
      "Data Processing Addendum (DPA)",
      "Standard Contractual Clauses (SCCs)",
      "Business Associate Agreement (BAA)",
      "Subprocessor notifications",
      "Trust center evidence summaries",
      "Customer communication templates"
    ]
  }
]


def to_kebab_case(name: str) -> str:
    """Convert deliverable name to kebab-case artifact name"""
    # Remove parenthetical content
    name = re.sub(r'\([^)]*\)', '', name)
    # Remove special characters
    name = re.sub(r'[^\w\s/-]', '', name)
    # Convert to lowercase and replace spaces/slashes with hyphens
    name = name.lower().strip()
    name = re.sub(r'[\s/]+', '-', name)
    # Remove consecutive hyphens
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing hyphens
    name = name.strip('-')
    return name


def infer_format(deliverable: str) -> str:
    """Infer the format based on the deliverable name"""
    lower = deliverable.lower()

    # Check for specific formats
    if any(x in lower for x in ['diagram', 'flowchart', 'graph', 'topology', 'map', 'mockup', 'wireframe', 'storyboard', 'prototype']):
        return "Multiple"
    elif any(x in lower for x in ['yaml', 'helm', 'kustomize', 'docker compose']):
        return "YAML"
    elif any(x in lower for x in ['json', 'sbom', 'package.json']):
        return "JSON"
    elif any(x in lower for x in ['readme', 'guide', 'manual', 'handbook', 'charter', 'statement', 'policy', 'plan', 'playbook', 'template', 'minutes', 'report', 'log', 'index', 'catalog', 'specification', 'document', 'framework', 'assessment', 'analysis', 'study', 'strategy', 'matrix', 'procedures', 'requirements', 'criteria']):
        return "Markdown"
    elif any(x in lower for x in ['openapi', 'asyncapi']):
        return "YAML"
    elif any(x in lower for x in ['graphql', 'proto', 'schema', 'ddl', 'script']):
        return "Text"
    elif any(x in lower for x in ['python', '.py']):
        return "Python"
    elif any(x in lower for x in ['typescript', 'javascript', '.ts', '.js']):
        return "TypeScript"
    elif 'dockerfile' in lower:
        return "Text"
    else:
        return "Markdown"


def infer_file_pattern(artifact_name: str, format_type: str) -> str:
    """Infer file pattern based on artifact name and format"""
    ext_map = {
        "JSON": "json",
        "YAML": "yaml",
        "Markdown": "md",
        "Python": "py",
        "TypeScript": "ts",
        "Text": "txt",
        "Multiple": "*"
    }
    ext = ext_map.get(format_type, "md")

    # Special cases
    if artifact_name == "readme":
        return "README.md"
    elif artifact_name == "contributing-guide":
        return "CONTRIBUTING.md"
    elif artifact_name == "dockerfile":
        return "Dockerfile"
    elif "helm-chart" in artifact_name:
        return "*/Chart.yaml"
    elif format_type == "Multiple":
        return f"*.{artifact_name}.*"
    else:
        return f"*.{artifact_name}.{ext}"


def generate_description(deliverable: str, phase: str, category: str) -> str:
    """Generate a description for the artifact"""
    return f"{deliverable} for {phase.split('. ')[1] if '. ' in phase else phase}. Part of {category} documentation and deliverables."


def infer_schema_properties(deliverable: str, format_type: str) -> Dict[str, Any]:
    """Infer schema properties based on deliverable type"""
    lower = deliverable.lower()

    # Common properties for most artifacts
    props = {}

    if format_type in ["JSON", "YAML"]:
        props = {
            "metadata": {
                "type": "object",
                "description": "Metadata about this artifact including version, author, timestamp"
            },
            "content": {
                "type": "object",
                "description": "Main content of the artifact"
            }
        }

        # Add specific properties based on type
        if 'report' in lower:
            props["findings"] = {"type": "array", "description": "List of findings or results"}
            props["summary"] = {"type": "string", "description": "Executive summary"}
        elif 'plan' in lower:
            props["objectives"] = {"type": "array", "description": "Plan objectives"}
            props["timeline"] = {"type": "object", "description": "Timeline and milestones"}
        elif 'policy' in lower or 'charter' in lower:
            props["scope"] = {"type": "string", "description": "Scope of the policy/charter"}
            props["rules"] = {"type": "array", "description": "Rules and guidelines"}
        elif 'log' in lower or 'register' in lower:
            props["entries"] = {"type": "array", "description": "Log entries"}
            props["lastUpdated"] = {"type": "string", "description": "Last update timestamp"}
        elif 'matrix' in lower:
            props["rows"] = {"type": "array", "description": "Matrix rows"}
            props["columns"] = {"type": "array", "description": "Matrix columns"}
        elif 'catalog' in lower or 'inventory' in lower:
            props["items"] = {"type": "array", "description": "Catalog items"}
        elif 'specification' in lower or 'schema' in lower:
            props["version"] = {"type": "string", "description": "Specification version"}
            props["definitions"] = {"type": "object", "description": "Schema definitions"}

    return props


def generate_artifact_description(
    deliverable: str,
    phase: str,
    category: str,
    output_dir: Path
) -> Path:
    """Generate a single artifact description file"""

    artifact_name = to_kebab_case(deliverable)
    format_type = infer_format(deliverable)
    file_pattern = infer_file_pattern(artifact_name, format_type)
    description = generate_description(deliverable, phase, category)
    schema_props = infer_schema_properties(deliverable, format_type)

    # Build the markdown content
    content = f"""# Name: {artifact_name}

# Purpose:
{description}

# Format: {format_type}

# File Pattern: {file_pattern}
"""

    # Add schema properties if we have them
    if schema_props and format_type in ["JSON", "YAML"]:
        content += "\n# Schema Properties:\n"
        for prop_name, prop_info in schema_props.items():
            content += f"- {prop_name} ({prop_info['type']}): {prop_info['description']}\n"

        content += "\n# Required Fields:\n"
        content += "- metadata\n"
        content += "- content\n"

    # Add producers/consumers placeholders
    content += "\n# Producers:\n"
    content += "- TBD\n"

    content += "\n# Consumers:\n"
    content += "- TBD\n"

    # Add related types
    content += "\n# Related Types:\n"
    content += "- TBD\n"

    # Write file
    output_file = output_dir / f"{artifact_name}.md"
    with open(output_file, 'w') as f:
        f.write(content)

    return output_file


def main():
    """Generate all artifact description files"""

    # Create output directory
    output_dir = Path("artifact_descriptions")
    output_dir.mkdir(exist_ok=True)

    generated_files = []
    artifact_names = set()
    duplicates = []

    print(f"Generating artifact descriptions in {output_dir}/\n")

    for phase_data in DELIVERABLES:
        phase = phase_data["phase"]
        category = phase_data["category"]

        print(f"\nPhase: {phase}")
        print(f"Category: {category}")

        for deliverable in phase_data["deliverables"]:
            artifact_name = to_kebab_case(deliverable)

            # Check for duplicates
            if artifact_name in artifact_names:
                duplicates.append((artifact_name, deliverable, phase))
                print(f"  ⚠️  DUPLICATE: {artifact_name} ({deliverable})")
                continue

            artifact_names.add(artifact_name)

            try:
                output_file = generate_artifact_description(
                    deliverable,
                    phase,
                    category,
                    output_dir
                )
                generated_files.append(output_file)
                print(f"  ✓ {artifact_name}")
            except Exception as e:
                print(f"  ✗ Error generating {artifact_name}: {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total deliverables processed: {sum(len(p['deliverables']) for p in DELIVERABLES)}")
    print(f"  Unique artifacts generated: {len(generated_files)}")
    print(f"  Duplicate names skipped: {len(duplicates)}")

    if duplicates:
        print(f"\nDuplicates:")
        for name, deliverable, phase in duplicates:
            print(f"  - {name} from '{deliverable}' in {phase}")

    print(f"\nGenerated files in: {output_dir}/")
    print(f"Next step: Run meta.artifact create on each file")


if __name__ == "__main__":
    main()
