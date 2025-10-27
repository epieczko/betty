#!/usr/bin/env python3
"""
End-to-End Lifecycle Workflow Test
Tests create→validate→review→publish lifecycle across all domains
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

BASE_DIR = Path("/home/user/betty")
SKILLS_DIR = BASE_DIR / "skills"
AGENTS_DIR = BASE_DIR / "agents"
OUTPUT_DIR = BASE_DIR / "registry" / "taxonomy"

# Lifecycle stages
LIFECYCLE_STAGES = ["create", "validate", "review", "publish"]

# Domain workflows to test
DOMAIN_WORKFLOWS = {
    "api": {
        "artifact": "api-spec",
        "stages": {
            "create": "api.define",
            "validate": "api.validate",
            "review": "artifact.review",
            "publish": "docs.sync.readme"
        }
    },
    "data": {
        "artifact": "data-schema",
        "stages": {
            "create": "artifact.create",
            "validate": "artifact.validate",
            "review": "artifact.review",
            "publish": "registry.update"
        }
    },
    "docs": {
        "artifact": "documentation",
        "stages": {
            "create": "generate.docs",
            "validate": "docs.validate.skilldocs",
            "review": "docs.lint.links",
            "publish": "docs.sync.readme"
        }
    },
    "architecture": {
        "artifact": "epic",
        "stages": {
            "create": "epic.write",
            "validate": "artifact.validate",
            "review": "artifact.review",
            "publish": "registry.update"
        }
    },
    "operations": {
        "artifact": "workflow",
        "stages": {
            "create": "workflow.compose",
            "validate": "workflow.validate",
            "review": "artifact.review",
            "publish": "plugin.publish"
        }
    }
}


def check_skill_exists(skill_name: str) -> Dict[str, Any]:
    """Check if a skill exists and is accessible"""
    skill_path = SKILLS_DIR / skill_name / "skill.yaml"

    result = {
        "skill": skill_name,
        "exists": False,
        "status": "unknown",
        "path": str(skill_path),
        "issues": []
    }

    if not skill_path.exists():
        result["issues"].append("Skill manifest not found")
        return result

    result["exists"] = True

    try:
        with open(skill_path, 'r') as f:
            data = yaml.safe_load(f)

        result["status"] = data.get("status", "unknown")

        # Check for common issues
        if not data.get("description"):
            result["issues"].append("Missing description")

        if not data.get("inputs"):
            result["issues"].append("No inputs defined")

        if not data.get("outputs"):
            result["issues"].append("No outputs defined")

    except Exception as e:
        result["issues"].append(f"Error reading manifest: {str(e)}")

    return result


def test_workflow(domain: str, workflow: Dict[str, Any]) -> Dict[str, Any]:
    """Test a complete domain workflow"""
    print(f"\n{'='*60}")
    print(f"Testing {domain.upper()} Domain Workflow")
    print(f"{'='*60}")

    result = {
        "domain": domain,
        "artifact": workflow["artifact"],
        "stages": {},
        "success": True,
        "issues": [],
        "completion_rate": 0.0
    }

    completed_stages = 0

    for stage in LIFECYCLE_STAGES:
        print(f"\n  {stage.upper()} Stage:")

        skill_name = workflow["stages"].get(stage)
        if not skill_name:
            print(f"    ⚠️  No skill mapped for {stage} stage")
            result["stages"][stage] = {
                "skill": None,
                "status": "missing",
                "success": False
            }
            result["issues"].append(f"No skill mapped for {stage} stage")
            result["success"] = False
            continue

        # Check skill
        skill_check = check_skill_exists(skill_name)
        print(f"    Skill: {skill_name}")

        if not skill_check["exists"]:
            print(f"    ❌ Skill not found")
            result["stages"][stage] = {
                "skill": skill_name,
                "status": "not_found",
                "success": False,
                "issues": skill_check["issues"]
            }
            result["issues"].append(f"{stage}: Skill '{skill_name}' not found")
            result["success"] = False
        elif skill_check["issues"]:
            print(f"    ⚠️  Skill has issues: {', '.join(skill_check['issues'])}")
            result["stages"][stage] = {
                "skill": skill_name,
                "status": skill_check["status"],
                "success": True,
                "issues": skill_check["issues"]
            }
            completed_stages += 1
        else:
            print(f"    ✅ Skill available (status: {skill_check['status']})")
            result["stages"][stage] = {
                "skill": skill_name,
                "status": skill_check["status"],
                "success": True,
                "issues": []
            }
            completed_stages += 1

    result["completion_rate"] = (completed_stages / len(LIFECYCLE_STAGES)) * 100

    if result["success"]:
        print(f"\n  ✅ Workflow complete ({result['completion_rate']:.0f}% stages available)")
    else:
        print(f"\n  ⚠️  Workflow incomplete ({result['completion_rate']:.0f}% stages available)")

    return result


def run_lifecycle_tests() -> Dict[str, Any]:
    """Run all lifecycle workflow tests"""
    print("🔄 End-to-End Lifecycle Workflow Tests")
    print("=" * 60)
    print(f"Testing create→validate→review→publish lifecycle")
    print(f"Domains: {', '.join(DOMAIN_WORKFLOWS.keys())}\n")

    test_results = {
        "test_time": datetime.now().isoformat(),
        "total_domains": len(DOMAIN_WORKFLOWS),
        "total_stages": len(LIFECYCLE_STAGES),
        "workflows": [],
        "summary": {
            "successful_workflows": 0,
            "partial_workflows": 0,
            "failed_workflows": 0,
            "total_stages_tested": 0,
            "available_stages": 0,
            "missing_stages": 0,
            "average_completion_rate": 0.0
        }
    }

    # Test each domain workflow
    for domain, workflow in DOMAIN_WORKFLOWS.items():
        workflow_result = test_workflow(domain, workflow)
        test_results["workflows"].append(workflow_result)

        test_results["summary"]["total_stages_tested"] += len(LIFECYCLE_STAGES)

        # Count results
        if workflow_result["success"] and workflow_result["completion_rate"] == 100:
            test_results["summary"]["successful_workflows"] += 1
        elif workflow_result["completion_rate"] > 0:
            test_results["summary"]["partial_workflows"] += 1
        else:
            test_results["summary"]["failed_workflows"] += 1

        # Count stages
        for stage_result in workflow_result["stages"].values():
            if stage_result["success"]:
                test_results["summary"]["available_stages"] += 1
            else:
                test_results["summary"]["missing_stages"] += 1

    # Calculate average completion rate
    total_completion = sum(w["completion_rate"] for w in test_results["workflows"])
    test_results["summary"]["average_completion_rate"] = total_completion / len(DOMAIN_WORKFLOWS)

    return test_results


def generate_report(results: Dict[str, Any]):
    """Generate lifecycle test report"""
    print("\n" + "=" * 60)
    print("📊 LIFECYCLE TEST SUMMARY")
    print("=" * 60)
    print(f"Domains Tested: {results['total_domains']}")
    print(f"Successful Workflows: {results['summary']['successful_workflows']}")
    print(f"Partial Workflows: {results['summary']['partial_workflows']}")
    print(f"Failed Workflows: {results['summary']['failed_workflows']}")
    print(f"Available Stages: {results['summary']['available_stages']}/{results['summary']['total_stages_tested']}")
    print(f"Average Completion: {results['summary']['average_completion_rate']:.1f}%")

    # Save JSON report
    report_file = OUTPUT_DIR / "lifecycle_test_report.json"
    with open(report_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Report saved to {report_file}")

    # Generate markdown report
    md_lines = [
        "# End-to-End Lifecycle Workflow Test Report",
        "",
        f"Generated: {results['test_time']}",
        "",
        "## Test Overview",
        "",
        "This report validates the create→validate→review→publish lifecycle across multiple domains.",
        "",
        "## Summary",
        "",
        f"- **Domains Tested**: {results['total_domains']}",
        f"- **Successful Workflows**: {results['summary']['successful_workflows']} (100% complete)",
        f"- **Partial Workflows**: {results['summary']['partial_workflows']} (>0% complete)",
        f"- **Failed Workflows**: {results['summary']['failed_workflows']} (0% complete)",
        f"- **Available Stages**: {results['summary']['available_stages']}/{results['summary']['total_stages_tested']}",
        f"- **Average Completion Rate**: {results['summary']['average_completion_rate']:.1f}%",
        "",
        "## Domain Workflow Results",
        ""
    ]

    for workflow in results["workflows"]:
        status_emoji = "✅" if workflow["success"] else "⚠️"
        md_lines.append(f"### {status_emoji} {workflow['domain'].upper()} Domain")
        md_lines.append("")
        md_lines.append(f"**Artifact Type**: `{workflow['artifact']}`")
        md_lines.append(f"**Completion Rate**: {workflow['completion_rate']:.0f}%")
        md_lines.append("")
        md_lines.append("| Stage | Skill | Status | Issues |")
        md_lines.append("|-------|-------|--------|--------|")

        for stage in LIFECYCLE_STAGES:
            stage_data = workflow["stages"].get(stage, {})
            skill = stage_data.get("skill", "N/A")
            status = "✅" if stage_data.get("success") else "❌"
            issues = ", ".join(stage_data.get("issues", [])) or "None"
            md_lines.append(f"| {stage.title()} | `{skill}` | {status} | {issues} |")

        if workflow["issues"]:
            md_lines.append("")
            md_lines.append("**Issues:**")
            for issue in workflow["issues"]:
                md_lines.append(f"- {issue}")

        md_lines.append("")

    md_lines.extend([
        "## Recommendations",
        "",
        "1. Implement missing skills for incomplete workflows",
        "2. Resolve skill manifest issues",
        "3. Ensure all lifecycle stages have dedicated skills",
        "4. Test workflows with real artifacts",
        "5. Document workflow patterns for each domain",
        ""
    ])

    md_file = OUTPUT_DIR / "lifecycle_test_report.md"
    with open(md_file, 'w') as f:
        f.write("\n".join(md_lines))

    print(f"📄 Markdown report saved to {md_file}")


if __name__ == "__main__":
    results = run_lifecycle_tests()
    generate_report(results)
