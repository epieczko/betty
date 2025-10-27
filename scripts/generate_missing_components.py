#!/usr/bin/env python3
"""
Auto-generate missing components from gaps.json
Creates scaffolds for missing orchestrator agents
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, List

BASE_DIR = Path("/home/user/betty")
GAPS_FILE = BASE_DIR / "registry" / "taxonomy" / "gaps.json"
AGENTS_DIR = BASE_DIR / "agents"
OUTPUT_DIR = BASE_DIR / "registry" / "taxonomy"

# Agent templates for each domain
ORCHESTRATOR_TEMPLATES = {
    "api": {
        "name": "api.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates complete API lifecycle from design through testing and deployment",
        "capabilities": [
            "Coordinate API design, validation, and compatibility checking",
            "Manage API generation and model creation workflows",
            "Orchestrate testing and quality assurance",
            "Handle API versioning and documentation",
            "Coordinate deployment and publishing"
        ],
        "skills_available": [
            "api.define",
            "api.validate",
            "api.compatibility",
            "api.generatemodels",
            "api.test"
        ],
        "reasoning_mode": "iterative",
        "tags": ["api", "orchestration", "workflow", "lifecycle"]
    },
    "data": {
        "name": "data.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates data workflows including transformation, validation, and quality assurance",
        "capabilities": [
            "Coordinate data transformation pipelines",
            "Manage data validation and quality checks",
            "Orchestrate data migration workflows",
            "Handle data governance and compliance",
            "Coordinate analytics and reporting"
        ],
        "skills_available": [
            "data.transform",
            "workflow.validate",
            "workflow.compose"
        ],
        "reasoning_mode": "iterative",
        "tags": ["data", "orchestration", "workflow", "etl"]
    },
    "security": {
        "name": "security.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates security workflows including audits, compliance checks, and vulnerability management",
        "capabilities": [
            "Coordinate security audits and assessments",
            "Manage compliance validation workflows",
            "Orchestrate vulnerability scanning and remediation",
            "Handle security documentation generation",
            "Coordinate access control and policy enforcement"
        ],
        "skills_available": [
            "policy.enforce",
            "artifact.validate",
            "artifact.review",
            "audit.log"
        ],
        "reasoning_mode": "iterative",
        "tags": ["security", "orchestration", "compliance", "audit"]
    },
    "testing": {
        "name": "testing.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates testing workflows across unit, integration, and end-to-end tests",
        "capabilities": [
            "Coordinate test planning and design",
            "Manage test execution and reporting",
            "Orchestrate quality assurance workflows",
            "Handle test data generation and management",
            "Coordinate continuous testing pipelines"
        ],
        "skills_available": [
            "test.example",
            "workflow.validate",
            "api.test"
        ],
        "reasoning_mode": "iterative",
        "tags": ["testing", "orchestration", "qa", "quality"]
    },
    "operations": {
        "name": "operations.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates operational workflows including builds, deployments, and monitoring",
        "capabilities": [
            "Coordinate build and deployment pipelines",
            "Manage infrastructure as code workflows",
            "Orchestrate monitoring and alerting",
            "Handle incident response and remediation",
            "Coordinate release management"
        ],
        "skills_available": [
            "build.optimize",
            "workflow.orchestrate",
            "workflow.compose",
            "workflow.validate",
            "git.createpr",
            "git.cleanupbranches",
            "telemetry.capture"
        ],
        "reasoning_mode": "iterative",
        "tags": ["operations", "orchestration", "devops", "deployment"]
    },
    "ai": {
        "name": "ai.orchestrator",
        "version": "0.1.0",
        "description": "Orchestrates AI/ML workflows including model training, evaluation, and deployment",
        "capabilities": [
            "Coordinate meta-agent creation and composition",
            "Manage skill and agent generation workflows",
            "Orchestrate AI-powered automation",
            "Handle agent compatibility and optimization",
            "Coordinate marketplace publishing"
        ],
        "skills_available": [
            "agent.compose",
            "agent.define",
            "agent.run",
            "generate.docs",
            "generate.marketplace",
            "meta.compatibility"
        ],
        "reasoning_mode": "iterative",
        "tags": ["ai", "orchestration", "meta", "automation"]
    }
}

def create_orchestrator_agent(domain: str, template: Dict) -> str:
    """Create an orchestrator agent scaffold"""
    print(f"  📝 Generating {domain}.orchestrator...")

    agent_dir = AGENTS_DIR / f"{domain}.orchestrator"
    agent_dir.mkdir(parents=True, exist_ok=True)

    # Create agent.yaml
    agent_file = agent_dir / "agent.yaml"

    # Add workflow pattern and example
    agent_data = template.copy()
    agent_data["workflow_pattern"] = f"""1. Analyze incoming request and requirements
2. Identify relevant {domain} skills and workflows
3. Compose multi-step execution plan
4. Execute skills in coordinated sequence
5. Validate intermediate results
6. Handle errors and retry as needed
7. Return comprehensive results"""

    agent_data["example_task"] = f"""Input: "Complete {domain} workflow from start to finish"

Agent will:
1. Break down the task into stages
2. Select appropriate skills for each stage
3. Execute create → validate → review → publish lifecycle
4. Monitor progress and handle failures
5. Generate comprehensive reports"""

    agent_data["error_handling"] = {
        "timeout_seconds": 300,
        "retry_strategy": "exponential_backoff",
        "max_retries": 3
    }

    agent_data["output"] = {
        "success": [
            f"{domain.title()} workflow results",
            "Execution logs and metrics",
            "Validation reports",
            "Generated artifacts"
        ],
        "failure": [
            "Error details and stack traces",
            "Partial results (if available)",
            "Remediation suggestions"
        ]
    }

    agent_data["status"] = "generated"

    with open(agent_file, 'w') as f:
        yaml.dump(agent_data, f, default_flow_style=False, sort_keys=False)

    # Create README.md
    readme_file = agent_dir / "README.md"
    readme_content = f"""# {template['name'].title()} Agent

{template['description']}

## Purpose

This orchestrator agent coordinates complex {domain} workflows by composing and sequencing multiple skills. It handles the complete lifecycle from planning through execution and validation.

## Capabilities

{chr(10).join(f'- {cap}' for cap in template['capabilities'])}

## Available Skills

{chr(10).join(f'- `{skill}`' for skill in template['skills_available'])}

## Usage

This agent uses iterative reasoning to:
1. Analyze requirements
2. Plan execution steps
3. Coordinate skill execution
4. Validate results
5. Handle errors and retries

## Status

**Generated**: Auto-generated from taxonomy gap analysis

## Next Steps

- [ ] Review and refine capabilities
- [ ] Test with real workflows
- [ ] Add domain-specific examples
- [ ] Integrate with existing agents
- [ ] Document best practices
"""

    with open(readme_file, 'w') as f:
        f.write(readme_content)

    print(f"    ✓ Created {agent_dir}")
    return str(agent_dir)


def generate_missing_orchestrators():
    """Generate all missing orchestrator agents"""
    print("🤖 Auto-Generating Missing Orchestrator Agents")
    print("=" * 60)

    # Read gaps
    with open(GAPS_FILE, 'r') as f:
        gaps = json.load(f)

    missing_orchestrators = gaps.get("missing_orchestrators", [])
    print(f"Found {len(missing_orchestrators)} missing orchestrators\n")

    created_agents = []

    for gap in missing_orchestrators:
        domain = gap["domain"]
        if domain in ORCHESTRATOR_TEMPLATES:
            template = ORCHESTRATOR_TEMPLATES[domain]
            agent_dir = create_orchestrator_agent(domain, template)
            created_agents.append({
                "domain": domain,
                "name": template["name"],
                "path": agent_dir,
                "status": "generated"
            })

    # Save generation report
    report = {
        "generated_at": "2025-10-26",
        "total_generated": len(created_agents),
        "agents": created_agents
    }

    report_file = OUTPUT_DIR / "generated_components_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n✅ Generated {len(created_agents)} orchestrator agents")
    print(f"📄 Report saved to {report_file}")

    return created_agents


if __name__ == "__main__":
    generate_missing_orchestrators()
