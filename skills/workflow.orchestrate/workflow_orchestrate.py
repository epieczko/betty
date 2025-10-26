#!/usr/bin/env python3
"""
workflow.orchestrate skill - Multi-artifact workflow orchestration

Coordinates specialized agents to create complete artifact sets for complex initiatives.
Manages dependencies, sequencing, and validation.
"""

import sys
import os
import argparse
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from betty.skill_executor import execute_skill_in_process


# Workflow definitions
WORKFLOWS = {
    "project-initiation": {
        "description": "Complete project initiation artifact set",
        "artifacts": [
            {"type": "business-case", "agent": "strategy.architect", "priority": 1},
            {"type": "project-charter", "agent": "governance.manager", "priority": 2, "depends_on": ["business-case"]},
            {"type": "raid-log", "agent": "governance.manager", "priority": 3},
            {"type": "stakeholder-analysis", "agent": "governance.manager", "priority": 3},
        ]
    },
    "security-review": {
        "description": "Comprehensive security assessment",
        "artifacts": [
            {"type": "threat-model", "agent": "security.architect", "priority": 1},
            {"type": "security-architecture-diagram", "agent": "security.architect", "priority": 2, "depends_on": ["threat-model"]},
            {"type": "security-assessment", "agent": "security.architect", "priority": 2},
            {"type": "vulnerability-management-plan", "agent": "security.architect", "priority": 3},
        ]
    },
}


def create_artifact(artifact_type: str, context: str, output_path: str, metadata: Optional[Dict] = None) -> Dict[str, Any]:
    """Create a single artifact using artifact.create skill"""
    try:
        args = [artifact_type, context, output_path]

        if metadata and metadata.get('author'):
            args.extend(["--author", metadata['author']])

        result = execute_skill_in_process("artifact.create", args, timeout=30)

        if result["returncode"] == 0:
            return {
                "success": True,
                "artifact_path": output_path,
                "artifact_type": artifact_type
            }
        else:
            return {
                "success": False,
                "error": result["stderr"] or result["stdout"],
                "artifact_type": artifact_type
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "artifact_type": artifact_type
        }


def orchestrate_workflow(
    workflow_type: str,
    context: str,
    output_directory: str,
    author: str = "Workflow Orchestrator"
) -> Dict[str, Any]:
    """
    Orchestrate multi-artifact workflow
    """

    if workflow_type not in WORKFLOWS:
        return {
            "success": False,
            "error": f"Unknown workflow type: {workflow_type}",
            "available_workflows": list(WORKFLOWS.keys())
        }

    workflow = WORKFLOWS[workflow_type]

    # Create output directory
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize workflow report
    workflow_report = {
        "workflow_type": workflow_type,
        "description": workflow.get("description"),
        "started_at": datetime.now().isoformat(),
        "artifacts_created": [],
        "artifacts_failed": [],
    }

    metadata = {"author": author}

    # Sort artifacts by priority
    artifacts_to_create = sorted(workflow["artifacts"], key=lambda x: x.get("priority", 99))

    # Track created artifacts
    created_artifacts = {}

    print(f"\n{'='*70}")
    print(f"🚀 Starting {workflow_type} workflow")
    print(f"{'='*70}\n")

    # Create each artifact
    for i, artifact_spec in enumerate(artifacts_to_create, 1):
        artifact_type = artifact_spec["type"]
        depends_on = artifact_spec.get("depends_on", [])

        print(f"[{i}/{len(artifacts_to_create)}] Creating {artifact_type}...")

        # Check dependencies
        missing_deps = [dep for dep in depends_on if dep not in created_artifacts]
        if missing_deps:
            print(f"  ⚠️  Skipping - missing dependencies: {missing_deps}\n")
            workflow_report["artifacts_failed"].append({
                "artifact_type": artifact_type,
                "reason": f"Missing dependencies: {missing_deps}"
            })
            continue

        # Build context with dependencies
        artifact_context = context
        if depends_on:
            dep_info = ", ".join([f"{dep} at {created_artifacts[dep]}" for dep in depends_on])
            artifact_context += f"\n\nRelated artifacts: {dep_info}"

        output_file = output_path / f"{artifact_type}.yaml"

        # Create artifact
        result = create_artifact(
            artifact_type=artifact_type,
            context=artifact_context,
            output_path=str(output_file),
            metadata=metadata
        )

        if result["success"]:
            print(f"  ✅ Created: {output_file}\n")
            created_artifacts[artifact_type] = str(output_file)

            workflow_report["artifacts_created"].append({
                "artifact_type": artifact_type,
                "artifact_path": str(output_file),
                "created_at": datetime.now().isoformat()
            })
        else:
            print(f"  ❌ Failed: {result.get('error', 'Unknown error')}\n")
            workflow_report["artifacts_failed"].append({
                "artifact_type": artifact_type,
                "reason": result.get("error", "Unknown error")
            })

    # Calculate summary
    total_artifacts = len(artifacts_to_create)
    created_count = len(workflow_report["artifacts_created"])

    workflow_report["completed_at"] = datetime.now().isoformat()
    workflow_report["summary"] = {
        "total_artifacts": total_artifacts,
        "created": created_count,
        "failed": len(workflow_report["artifacts_failed"]),
        "success_rate": f"{(created_count / total_artifacts * 100):.0f}%" if total_artifacts > 0 else "0%"
    }

    # Save workflow report
    report_file = output_path / f"{workflow_type}-workflow-report.yaml"
    with open(report_file, 'w') as f:
        yaml.dump(workflow_report, f, default_flow_style=False, sort_keys=False)

    print(f"{'='*70}")
    print(f"Created:   {created_count}/{total_artifacts} artifacts")
    print(f"📄 Report: {report_file}")
    print(f"{'='*70}\n")

    return {
        "success": created_count > 0,
        "workflow_report": workflow_report,
        "report_file": str(report_file)
    }


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description='Orchestrate multi-artifact workflows')
    parser.add_argument('workflow_type', choices=list(WORKFLOWS.keys()), help='Workflow type')
    parser.add_argument('description', help='Initiative description')
    parser.add_argument('output_directory', help='Output directory')
    parser.add_argument('--author', default='Workflow Orchestrator', help='Author name')

    args = parser.parse_args()

    result = orchestrate_workflow(
        workflow_type=args.workflow_type,
        context=args.description,
        output_directory=args.output_directory,
        author=args.author
    )

    return 0 if result["success"] else 1


if __name__ == '__main__':
    sys.exit(main())
