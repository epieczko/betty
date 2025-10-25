#!/usr/bin/env python3
"""
Betty Traceability CLI

View and manage traceability records.
"""

import sys
import json
import os
from pathlib import Path
from typing import Optional

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.traceability import get_tracer


def format_timestamp(ts: str) -> str:
    """Format ISO timestamp for display"""
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    except:
        return ts


def show_trace(component_id: str, format: str = "text"):
    """Show traceability record for a component"""
    tracer = get_tracer()
    trace = tracer.get_trace(component_id)

    if not trace:
        print(f"❌ No traceability record found for: {component_id}")
        return 1

    if format == "json":
        print(json.dumps(trace, indent=2))
        return 0

    # Text format
    print(f"\n{'='*70}")
    print(f"Traceability Record: {trace['trace_id']}")
    print(f"{'='*70}\n")

    # Component info
    comp = trace['component']
    print(f"Component:  {comp['name']} ({comp['type']})")
    print(f"ID:         {comp['id']}")
    print(f"Version:    {comp['version']}")
    print(f"Location:   {comp['file_path']}\n")

    # Creation info
    creation = trace['creation']
    print(f"{'─'*70}")
    print("CREATION")
    print(f"{'─'*70}")
    print(f"Created:    {format_timestamp(creation['timestamp'])}")
    print(f"By:         {creation['created_by']['tool']} v{creation['created_by']['version']}")
    if 'user' in creation['created_by']:
        print(f"User:       {creation['created_by']['user']}")
    print(f"From:       {creation['input_source']['path']}")
    print(f"Hash:       {creation['input_source']['hash']}")
    print(f"Betty:      v{creation['betty_version']}\n")

    # Requirement info
    req = trace['requirement']
    print(f"{'─'*70}")
    print("REQUIREMENT")
    print(f"{'─'*70}")
    print(f"ID:          {req['id']}")
    print(f"Description: {req['description']}")
    if req.get('source'):
        print(f"Source:      {req['source']}")
    if req.get('issue_id'):
        print(f"Issue:       {req['issue_id']}")
    if req.get('requested_by'):
        print(f"Requested:   {req['requested_by']}")
    if req.get('rationale'):
        print(f"Rationale:   {req['rationale']}")
    print()

    # Verification info
    verif = trace['verification']
    summary = verif['summary']
    print(f"{'─'*70}")
    print("VERIFICATION")
    print(f"{'─'*70}")
    print(f"Status:      {verif['status'].upper()}")
    print(f"Total Checks: {summary['total_checks']}")
    print(f"  ✅ Passed:   {summary['passed']}")
    print(f"  ❌ Failed:   {summary['failed']}")
    print(f"  ⚠️  Warnings: {summary['warnings']}")
    if summary.get('last_verified'):
        print(f"Last Check:  {format_timestamp(summary['last_verified'])}")
    print()

    if verif['checks']:
        print("Verification Checks:")
        for i, check in enumerate(verif['checks'], 1):
            result_icon = {"passed": "✅", "failed": "❌", "warning": "⚠️", "skipped": "⏭️"}.get(check['result'], "❓")
            print(f"\n  {i}. {check['check_type']} - {result_icon} {check['result'].upper()}")
            print(f"     Tool:      {check['tool']}")
            print(f"     Timestamp: {format_timestamp(check['timestamp'])}")

            if check.get('details'):
                details = check['details']
                if details.get('checks_performed'):
                    print(f"     Details:")
                    for subcheck in details['checks_performed']:
                        status_icon = {"passed": "✅", "failed": "❌", "warning": "⚠️"}.get(subcheck['status'], "❓")
                        print(f"       - {status_icon} {subcheck['name']}")
                        if subcheck.get('message'):
                            print(f"         {subcheck['message']}")

                if details.get('tests_run'):
                    print(f"     Tests: {details['tests_passed']}/{details['tests_run']} passed")

                if details.get('coverage'):
                    print(f"     Coverage: {details['coverage']}")

            if check.get('evidence'):
                print(f"     Evidence: {check['evidence']}")

    # Metadata
    if trace.get('metadata'):
        meta = trace['metadata']
        if meta:
            print(f"\n{'─'*70}")
            print("METADATA")
            print(f"{'─'*70}")
            if meta.get('tags'):
                print(f"Tags:    {', '.join(meta['tags'])}")
            if meta.get('project'):
                print(f"Project: {meta['project']}")
            if meta.get('team'):
                print(f"Team:    {meta['team']}")

    print(f"\n{'='*70}\n")
    return 0


def list_traces(format: str = "text"):
    """List all traceability records"""
    tracer = get_tracer()
    traces = tracer.list_all_traces()

    if not traces:
        print("No traceability records found.")
        return 0

    if format == "json":
        print(json.dumps(traces, indent=2))
        return 0

    # Text format
    print(f"\n{'='*70}")
    print(f"Traceability Records ({len(traces)} total)")
    print(f"{'='*70}\n")

    for trace in traces:
        comp = trace['component']
        req = trace['requirement']
        verif = trace['verification']

        status_icon = {"passed": "✅", "failed": "❌", "partial": "⚠️", "pending": "⏳"}.get(verif['status'], "❓")

        print(f"{status_icon} {comp['name']} ({comp['type']})")
        print(f"   Requirement: {req['id']} - {req['description'][:60]}...")
        print(f"   Created: {format_timestamp(trace['creation']['timestamp'])}")
        print(f"   Verification: {verif['status']} ({verif['summary']['passed']}/{verif['summary']['total_checks']} checks passed)")
        print()

    return 0


def search_by_requirement(requirement_id: str, format: str = "text"):
    """Find all components for a requirement"""
    tracer = get_tracer()
    traces = tracer.search_by_requirement(requirement_id)

    if not traces:
        print(f"No components found for requirement: {requirement_id}")
        return 0

    if format == "json":
        print(json.dumps(traces, indent=2))
        return 0

    # Text format
    print(f"\n{'='*70}")
    print(f"Components for Requirement: {requirement_id}")
    print(f"{'='*70}\n")

    for trace in traces:
        comp = trace['component']
        verif = trace['verification']

        status_icon = {"passed": "✅", "failed": "❌", "partial": "⚠️", "pending": "⏳"}.get(verif['status'], "❓")

        print(f"{status_icon} {comp['name']} ({comp['type']}) - v{comp['version']}")
        print(f"   Location: {comp['file_path']}")
        print(f"   Verification: {verif['status']}")
        print()

    return 0


def export_db(output_file: str):
    """Export all traces for database loading"""
    tracer = get_tracer()
    count = tracer.export_for_database(output_file)

    print(f"✅ Exported {count} traceability records to: {output_file}")
    print(f"\nLoad into MongoDB:")
    print(f"  mongoimport --db betty --collection traces --file {output_file} --jsonArray")
    print(f"\nLoad into CouchDB:")
    print(f"  curl -X POST http://localhost:5984/betty/_bulk_docs -H 'Content-Type: application/json' -d @{output_file}")

    return 0


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Betty Traceability CLI - View and manage traceability records"
    )

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # show command
    show_parser = subparsers.add_parser("show", help="Show traceability record for a component")
    show_parser.add_argument("component_id", help="Component ID (e.g., code.reviewer)")

    # list command
    list_parser = subparsers.add_parser("list", help="List all traceability records")

    # requirement command
    req_parser = subparsers.add_parser("requirement", help="Find components for a requirement")
    req_parser.add_argument("requirement_id", help="Requirement ID (e.g., REQ-2025-001)")

    # export command
    export_parser = subparsers.add_parser("export", help="Export traces for database loading")
    export_parser.add_argument("output_file", help="Output JSON file path")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == "show":
            return show_trace(args.component_id, args.format)
        elif args.command == "list":
            return list_traces(args.format)
        elif args.command == "requirement":
            return search_by_requirement(args.requirement_id, args.format)
        elif args.command == "export":
            return export_db(args.output_file)
        else:
            parser.print_help()
            return 1

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
