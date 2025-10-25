#!/usr/bin/env python3
"""
Betty Framework - Certification CLI

CLI tool for managing and auditing component certification.

Usage:
    python3 betty/cert_cli.py check <component_id>
    python3 betty/cert_cli.py list [--certified|--uncertified] [--type agent|skill|hook]
    python3 betty/cert_cli.py audit [--strict]
    python3 betty/cert_cli.py report [--format text|json]

Examples:
    # Check if a component is certified
    python3 betty/cert_cli.py check file.compare

    # List all certified skills
    python3 betty/cert_cli.py list --certified --type skill

    # Audit all components (fail if any uncertified)
    python3 betty/cert_cli.py audit --strict

    # Generate compliance report
    python3 betty/cert_cli.py report --format json
"""

import sys
import json
import argparse
from typing import Dict, Any, List, Optional
from pathlib import Path

# Add parent directory to path
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.certification import get_certifier
from betty.config import BASE_DIR


def cmd_check(args):
    """Check certification status of a component"""
    certifier = get_certifier()

    is_cert = certifier.is_certified(args.component_id)
    details = certifier.get_certification_details(args.component_id)

    if not details:
        print(f"❌ Component '{args.component_id}' not found")
        print(f"\n   No traceability record exists for this component.")
        print(f"   Create the component with requirement linkage to certify it.")
        return 1

    print(f"{'='*70}")
    print(f"Component Certification: {args.component_id}")
    print(f"{'='*70}\n")

    status_icon = "✅" if is_cert else "❌"
    status_text = "CERTIFIED" if is_cert else "NOT CERTIFIED"

    print(f"Status: {status_icon} {status_text}\n")

    if details:
        print(f"Requirement ID:   {details['requirement_id'] or 'N/A'}")
        print(f"Description:      {details['requirement_description'] or 'N/A'}")
        print(f"Verification:     {details['verification_status'] or 'N/A'}")
        print(f"Created By:       {details['created_by'] or 'N/A'}")
        print(f"Created At:       {details['created_at'] or 'N/A'}")
        print(f"Trace ID:         {details['trace_id'] or 'N/A'}")

    print(f"\n{'='*70}")

    if not is_cert:
        print("\n⚠️  This component cannot run in Betty without certification.")
        print("   To certify, recreate with requirement linkage:\n")
        print("   python3 agents/meta.agent/meta_agent.py description.md \\")
        print("     --requirement-id REQ-XXX \\")
        print("     --requirement-description '...'\n")
        return 1

    return 0


def cmd_list(args):
    """List certified or uncertified components"""
    certifier = get_certifier()

    if args.uncertified:
        # List uncertified components found in filesystem
        uncertified = certifier.list_uncertified_components()

        print(f"{'='*70}")
        print(f"Uncertified Components")
        print(f"{'='*70}\n")

        if not uncertified:
            print("✅ No uncertified components found\n")
            return 0

        print(f"Found {len(uncertified)} uncertified components:\n")
        for path in uncertified:
            print(f"  ❌ {path}")

        print(f"\n⚠️  These components lack certification and cannot run in Betty")
        print(f"   Create traceability records for them to enable execution.\n")
        return 1 if uncertified else 0

    else:
        # List certified components
        certified = certifier.list_certified_components(component_type=args.type)

        print(f"{'='*70}")
        title = f"Certified {args.type.title()}s" if args.type else "All Certified Components"
        print(f"{title}")
        print(f"{'='*70}\n")

        if not certified:
            print(f"No certified {args.type or 'components'} found\n")
            return 0

        print(f"Found {len(certified)} certified {args.type or 'component'}(s):\n")

        for comp in certified:
            print(f"  ✅ {comp['component_id']}")
            print(f"     Requirement: {comp['requirement_id']} - {comp['requirement_description'][:50]}...")
            print(f"     Status: {comp['verification_status']}")
            print()

        return 0


def cmd_audit(args):
    """Audit all components for certification"""
    certifier = get_certifier()

    print(f"{'='*70}")
    print(f"Betty Framework Certification Audit")
    print(f"{'='*70}\n")

    # Get certified components
    certified = certifier.list_certified_components()
    print(f"✅ Certified components: {len(certified)}")

    # Get uncertified components
    uncertified = certifier.list_uncertified_components()
    print(f"❌ Uncertified components: {len(uncertified)}\n")

    if uncertified:
        print(f"Uncertified components found:\n")
        for path in uncertified:
            print(f"  ❌ {path}")
        print()

    # Summary
    total = len(certified) + len(uncertified)
    if total > 0:
        cert_percentage = (len(certified) / total) * 100
        print(f"Certification rate: {cert_percentage:.1f}% ({len(certified)}/{total})")

    print(f"\n{'='*70}\n")

    if uncertified:
        if args.strict:
            print("❌ AUDIT FAILED: Uncertified components found")
            print("   Betty Framework requires 100% certification")
            print("   Set BETTY_CERT_MODE=dev to allow uncertified components\n")
            return 1
        else:
            print("⚠️  WARNING: Uncertified components found")
            print("   Use --strict to enforce certification requirement\n")
            return 0
    else:
        print("✅ AUDIT PASSED: All components certified\n")
        return 0


def cmd_report(args):
    """Generate compliance report"""
    certifier = get_certifier()

    certified = certifier.list_certified_components()
    uncertified = certifier.list_uncertified_components()

    report = {
        "audit_type": "betty_framework_certification",
        "total_certified": len(certified),
        "total_uncertified": len(uncertified),
        "certification_rate": (len(certified) / (len(certified) + len(uncertified)) * 100) if (len(certified) + len(uncertified)) > 0 else 0,
        "certified_components": certified,
        "uncertified_components": uncertified
    }

    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        # Text format
        print(f"{'='*70}")
        print(f"Betty Framework Certification Report")
        print(f"{'='*70}\n")
        print(f"Total Certified:    {report['total_certified']}")
        print(f"Total Uncertified:  {report['total_uncertified']}")
        print(f"Certification Rate: {report['certification_rate']:.1f}%\n")

        if certified:
            print(f"Certified Components ({len(certified)}):")
            for comp in certified:
                print(f"  ✅ {comp['component_id']} - {comp['requirement_id']}")
            print()

        if uncertified:
            print(f"Uncertified Components ({len(uncertified)}):")
            for path in uncertified:
                print(f"  ❌ {path}")
            print()

        print(f"{'='*70}\n")

    return 0


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Betty Framework - Certification Management CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check certification status")
    check_parser.add_argument("component_id", help="Component ID to check")

    # List command
    list_parser = subparsers.add_parser("list", help="List components")
    list_parser.add_argument(
        "--certified",
        action="store_true",
        help="List only certified components"
    )
    list_parser.add_argument(
        "--uncertified",
        action="store_true",
        help="List only uncertified components"
    )
    list_parser.add_argument(
        "--type",
        choices=["agent", "skill", "hook"],
        help="Filter by component type"
    )

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Audit all components")
    audit_parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any uncertified components found"
    )

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate compliance report")
    report_parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Route to appropriate command handler
    if args.command == "check":
        return cmd_check(args)
    elif args.command == "list":
        return cmd_list(args)
    elif args.command == "audit":
        return cmd_audit(args)
    elif args.command == "report":
        return cmd_report(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
