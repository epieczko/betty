#!/usr/bin/env python3
"""
Betty Framework - Bulk Certification Tool

Retroactively certifies existing components that lack traceability records.

This tool is for migrating legacy components created before the certification
system was implemented. For new components, always use meta-agents with
requirement linkage.

Usage:
    python3 betty/bulk_certify.py [--dry-run] [--requirement-prefix REQ-LEGACY]

Examples:
    # Dry run - show what would be certified
    python3 betty/bulk_certify.py --dry-run

    # Certify all uncertified components
    python3 betty/bulk_certify.py

    # Use custom requirement ID prefix
    python3 betty/bulk_certify.py --requirement-prefix REQ-MIGRATE
"""

import sys
import os
import yaml
import argparse
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.certification import get_certifier
from betty.traceability import get_tracer, RequirementInfo
from betty.config import BASE_DIR


class BulkCertifier:
    """Bulk certification for existing components"""

    def __init__(self, requirement_prefix: str = "REQ-LEGACY"):
        """
        Initialize bulk certifier

        Args:
            requirement_prefix: Prefix for generated requirement IDs
        """
        self.certifier = get_certifier()
        self.tracer = get_tracer()
        self.requirement_prefix = requirement_prefix
        self.base_dir = Path(BASE_DIR)

    def certify_agent(self, agent_yaml_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """
        Certify an agent

        Args:
            agent_yaml_path: Path to agent.yaml
            dry_run: If True, don't create trace record

        Returns:
            Certification result
        """
        # Read agent.yaml
        try:
            with open(agent_yaml_path) as f:
                agent_config = yaml.safe_load(f)
        except Exception as e:
            return {
                "ok": False,
                "path": str(agent_yaml_path),
                "error": f"YAML parse error: {str(e)}"
            }

        agent_name = agent_config.get("name") if agent_config else None
        agent_desc = agent_config.get("description", "") if agent_config else ""

        if not agent_name:
            return {
                "ok": False,
                "path": str(agent_yaml_path),
                "error": "Missing agent name"
            }

        # Check if already certified
        if self.certifier.is_certified(agent_name):
            return {
                "ok": True,
                "path": str(agent_yaml_path),
                "component_id": agent_name,
                "status": "already_certified"
            }

        # Create requirement info for legacy component
        requirement = RequirementInfo(
            id=f"{self.requirement_prefix}-{agent_name.upper().replace('.', '-')}",
            description=f"Legacy agent: {agent_desc[:100] if agent_desc else agent_name}",
            source="Bulk certification - existing component",
            issue_id=f"LEGACY-AGENT-{agent_name}",
            requested_by="betty-framework-migration",
            rationale="Retroactive certification for pre-existing component"
        )

        if dry_run:
            return {
                "ok": True,
                "path": str(agent_yaml_path),
                "component_id": agent_name,
                "status": "would_certify",
                "requirement": requirement.id
            }

        # Create traceability record
        try:
            trace_id = self.tracer.log_creation(
                component_id=agent_name,
                component_name=agent_name.replace(".", " ").title(),
                component_type="agent",
                component_version="legacy",
                component_file_path=str(agent_yaml_path),
                input_source_path="N/A - Pre-existing component",
                created_by_tool="bulk-certification",
                created_by_version="1.0.0",
                requirement=requirement,
                tags=["agent", "legacy", "bulk-certified"],
                project="Betty Framework"
            )

            # Log verification (mark as passed for legacy)
            self.tracer.log_verification(
                component_id=agent_name,
                check_type="validation",
                tool="bulk-certification",
                result="passed",
                details={
                    "checks_performed": [
                        {"name": "legacy_component", "status": "passed",
                         "message": "Pre-existing component retroactively certified"}
                    ]
                }
            )

            return {
                "ok": True,
                "path": str(agent_yaml_path),
                "component_id": agent_name,
                "status": "certified",
                "trace_id": trace_id,
                "requirement": requirement.id
            }

        except Exception as e:
            return {
                "ok": False,
                "path": str(agent_yaml_path),
                "component_id": agent_name,
                "error": str(e)
            }

    def certify_skill(self, skill_yaml_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """
        Certify a skill

        Args:
            skill_yaml_path: Path to skill.yaml
            dry_run: If True, don't create trace record

        Returns:
            Certification result
        """
        # Read skill.yaml
        try:
            with open(skill_yaml_path) as f:
                skill_config = yaml.safe_load(f)
        except Exception as e:
            return {
                "ok": False,
                "path": str(skill_yaml_path),
                "error": f"YAML parse error: {str(e)[:100]}"
            }

        skill_name = skill_config.get("name") if skill_config else None
        skill_desc = skill_config.get("description", "") if skill_config else ""

        if not skill_name:
            return {
                "ok": False,
                "path": str(skill_yaml_path),
                "error": "Missing skill name"
            }

        # Check if already certified
        if self.certifier.is_certified(skill_name):
            return {
                "ok": True,
                "path": str(skill_yaml_path),
                "component_id": skill_name,
                "status": "already_certified"
            }

        # Create requirement info for legacy component
        requirement = RequirementInfo(
            id=f"{self.requirement_prefix}-{skill_name.upper().replace('.', '-')}",
            description=f"Legacy skill: {skill_desc[:100] if skill_desc else skill_name}",
            source="Bulk certification - existing component",
            issue_id=f"LEGACY-SKILL-{skill_name}",
            requested_by="betty-framework-migration",
            rationale="Retroactive certification for pre-existing component"
        )

        if dry_run:
            return {
                "ok": True,
                "path": str(skill_yaml_path),
                "component_id": skill_name,
                "status": "would_certify",
                "requirement": requirement.id
            }

        # Create traceability record
        try:
            trace_id = self.tracer.log_creation(
                component_id=skill_name,
                component_name=skill_name.replace(".", " ").title(),
                component_type="skill",
                component_version="legacy",
                component_file_path=str(skill_yaml_path),
                input_source_path="N/A - Pre-existing component",
                created_by_tool="bulk-certification",
                created_by_version="1.0.0",
                requirement=requirement,
                tags=["skill", "legacy", "bulk-certified"],
                project="Betty Framework"
            )

            # Log verification (mark as passed for legacy)
            self.tracer.log_verification(
                component_id=skill_name,
                check_type="validation",
                tool="bulk-certification",
                result="passed",
                details={
                    "checks_performed": [
                        {"name": "legacy_component", "status": "passed",
                         "message": "Pre-existing component retroactively certified"}
                    ]
                }
            )

            return {
                "ok": True,
                "path": str(skill_yaml_path),
                "component_id": skill_name,
                "status": "certified",
                "trace_id": trace_id,
                "requirement": requirement.id
            }

        except Exception as e:
            return {
                "ok": False,
                "path": str(skill_yaml_path),
                "component_id": skill_name,
                "error": str(e)
            }

    def certify_all(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Certify all uncertified components

        Args:
            dry_run: If True, don't create trace records

        Returns:
            Certification summary
        """
        results = {
            "agents": [],
            "skills": [],
            "summary": {
                "total_processed": 0,
                "certified": 0,
                "already_certified": 0,
                "errors": 0
            }
        }

        # Find all uncertified components
        uncertified = self.certifier.list_uncertified_components()

        for path_str in uncertified:
            path = Path(path_str)

            if path.name == "agent.yaml":
                result = self.certify_agent(path, dry_run)
                results["agents"].append(result)
            elif path.name == "skill.yaml":
                result = self.certify_skill(path, dry_run)
                results["skills"].append(result)

            results["summary"]["total_processed"] += 1

            if result.get("status") == "certified" or result.get("status") == "would_certify":
                results["summary"]["certified"] += 1
            elif result.get("status") == "already_certified":
                results["summary"]["already_certified"] += 1
            elif not result.get("ok"):
                results["summary"]["errors"] += 1

        return results


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Betty Framework - Bulk Component Certification",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be certified without creating records"
    )
    parser.add_argument(
        "--requirement-prefix",
        default="REQ-LEGACY",
        help="Prefix for generated requirement IDs (default: REQ-LEGACY)"
    )

    args = parser.parse_args()

    certifier = BulkCertifier(requirement_prefix=args.requirement_prefix)

    print("="*70)
    print("Betty Framework - Bulk Certification")
    if args.dry_run:
        print("MODE: DRY RUN (no changes will be made)")
    print("="*70)
    print()

    results = certifier.certify_all(dry_run=args.dry_run)

    # Print agent results
    if results["agents"]:
        print(f"Agents ({len(results['agents'])}):")
        for result in results["agents"]:
            status_icon = "✅" if result.get("ok") else "❌"
            status = result.get("status", "error")
            component_id = result.get("component_id", "unknown")

            if status == "certified":
                print(f"  {status_icon} {component_id} - CERTIFIED ({result.get('requirement')})")
            elif status == "would_certify":
                print(f"  ✨ {component_id} - WOULD CERTIFY ({result.get('requirement')})")
            elif status == "already_certified":
                print(f"  ✓  {component_id} - Already certified")
            else:
                print(f"  {status_icon} {component_id} - ERROR: {result.get('error')}")
        print()

    # Print skill results
    if results["skills"]:
        print(f"Skills ({len(results['skills'])}):")
        for result in results["skills"]:
            status_icon = "✅" if result.get("ok") else "❌"
            status = result.get("status", "error")
            component_id = result.get("component_id", "unknown")

            if status == "certified":
                print(f"  {status_icon} {component_id} - CERTIFIED ({result.get('requirement')})")
            elif status == "would_certify":
                print(f"  ✨ {component_id} - WOULD CERTIFY ({result.get('requirement')})")
            elif status == "already_certified":
                print(f"  ✓  {component_id} - Already certified")
            else:
                print(f"  {status_icon} {component_id} - ERROR: {result.get('error')}")
        print()

    # Print summary
    print("="*70)
    print("Summary")
    print("="*70)
    summary = results["summary"]
    print(f"Total Processed:      {summary['total_processed']}")
    print(f"Newly Certified:      {summary['certified']}")
    print(f"Already Certified:    {summary['already_certified']}")
    print(f"Errors:               {summary['errors']}")
    print()

    if args.dry_run:
        print("⚠️  This was a DRY RUN - no changes were made")
        print("   Run without --dry-run to certify components")
    else:
        print("✅ Bulk certification complete")
        print("   Run: python3 betty/cert_cli.py audit")

    print()

    return 0 if summary["errors"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
