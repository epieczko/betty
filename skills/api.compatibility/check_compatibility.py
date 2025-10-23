#!/usr/bin/env python3
"""
Detect breaking changes between API specification versions.

This skill analyzes two versions of an API spec and identifies:
- Breaking changes (remove endpoints, change types, etc.)
- Non-breaking changes (add endpoints, add optional fields, etc.)
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Add betty module to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_path

logger = setup_logger(__name__)


class CompatibilityChange:
    """Represents a compatibility change between spec versions."""

    def __init__(
        self,
        change_type: str,
        severity: str,
        path: str,
        description: str,
        old_value: Any = None,
        new_value: Any = None
    ):
        self.change_type = change_type
        self.severity = severity  # "breaking" or "non-breaking"
        self.path = path
        self.description = description
        self.old_value = old_value
        self.new_value = new_value

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        result = {
            "change_type": self.change_type,
            "severity": self.severity,
            "path": self.path,
            "description": self.description
        }
        if self.old_value is not None:
            result["old_value"] = self.old_value
        if self.new_value is not None:
            result["new_value"] = self.new_value
        return result


class CompatibilityChecker:
    """Check compatibility between two API specs."""

    def __init__(self, old_spec: Dict[str, Any], new_spec: Dict[str, Any]):
        self.old_spec = old_spec
        self.new_spec = new_spec
        self.breaking_changes: List[CompatibilityChange] = []
        self.non_breaking_changes: List[CompatibilityChange] = []

    def check(self) -> Dict[str, Any]:
        """
        Run all compatibility checks.

        Returns:
            Compatibility report
        """
        # Check paths (endpoints)
        self._check_paths()

        # Check schemas
        self._check_schemas()

        # Check parameters
        self._check_parameters()

        # Check responses
        self._check_responses()

        return {
            "compatible": len(self.breaking_changes) == 0,
            "breaking_changes": [c.to_dict() for c in self.breaking_changes],
            "non_breaking_changes": [c.to_dict() for c in self.non_breaking_changes],
            "change_summary": {
                "total_breaking": len(self.breaking_changes),
                "total_non_breaking": len(self.non_breaking_changes),
                "total_changes": len(self.breaking_changes) + len(self.non_breaking_changes)
            }
        }

    def _check_paths(self):
        """Check for changes in API paths/endpoints."""
        old_paths = set(self.old_spec.get("paths", {}).keys())
        new_paths = set(self.new_spec.get("paths", {}).keys())

        # Removed paths (BREAKING)
        for removed_path in old_paths - new_paths:
            self.breaking_changes.append(CompatibilityChange(
                change_type="path_removed",
                severity="breaking",
                path=f"paths.{removed_path}",
                description=f"Endpoint '{removed_path}' was removed",
                old_value=removed_path
            ))

        # Added paths (NON-BREAKING)
        for added_path in new_paths - old_paths:
            self.non_breaking_changes.append(CompatibilityChange(
                change_type="path_added",
                severity="non-breaking",
                path=f"paths.{added_path}",
                description=f"New endpoint '{added_path}' was added",
                new_value=added_path
            ))

        # Check operations on existing paths
        for path in old_paths & new_paths:
            self._check_operations(path)

    def _check_operations(self, path: str):
        """Check for changes in HTTP operations on a path."""
        old_operations = set(self.old_spec["paths"][path].keys()) - {"parameters"}
        new_operations = set(self.new_spec["paths"][path].keys()) - {"parameters"}

        # Removed operations (BREAKING)
        for removed_op in old_operations - new_operations:
            self.breaking_changes.append(CompatibilityChange(
                change_type="operation_removed",
                severity="breaking",
                path=f"paths.{path}.{removed_op}",
                description=f"Operation '{removed_op.upper()}' on '{path}' was removed",
                old_value=removed_op
            ))

        # Added operations (NON-BREAKING)
        for added_op in new_operations - old_operations:
            self.non_breaking_changes.append(CompatibilityChange(
                change_type="operation_added",
                severity="non-breaking",
                path=f"paths.{path}.{added_op}",
                description=f"New operation '{added_op.upper()}' on '{path}' was added",
                new_value=added_op
            ))

    def _check_schemas(self):
        """Check for changes in component schemas."""
        old_schemas = self.old_spec.get("components", {}).get("schemas", {})
        new_schemas = self.new_spec.get("components", {}).get("schemas", {})

        old_schema_names = set(old_schemas.keys())
        new_schema_names = set(new_schemas.keys())

        # Removed schemas (BREAKING if they were referenced)
        for removed_schema in old_schema_names - new_schema_names:
            self.breaking_changes.append(CompatibilityChange(
                change_type="schema_removed",
                severity="breaking",
                path=f"components.schemas.{removed_schema}",
                description=f"Schema '{removed_schema}' was removed",
                old_value=removed_schema
            ))

        # Added schemas (NON-BREAKING)
        for added_schema in new_schema_names - old_schema_names:
            self.non_breaking_changes.append(CompatibilityChange(
                change_type="schema_added",
                severity="non-breaking",
                path=f"components.schemas.{added_schema}",
                description=f"New schema '{added_schema}' was added",
                new_value=added_schema
            ))

        # Check properties on existing schemas
        for schema_name in old_schema_names & new_schema_names:
            self._check_schema_properties(schema_name, old_schemas[schema_name], new_schemas[schema_name])

    def _check_schema_properties(self, schema_name: str, old_schema: Dict[str, Any], new_schema: Dict[str, Any]):
        """Check for changes in schema properties."""
        old_props = old_schema.get("properties") or {}
        new_props = new_schema.get("properties") or {}

        old_required = set(old_schema.get("required", []))
        new_required = set(new_schema.get("required", []))

        old_prop_names = set(old_props.keys())
        new_prop_names = set(new_props.keys())

        # Removed properties (BREAKING)
        for removed_prop in old_prop_names - new_prop_names:
            self.breaking_changes.append(CompatibilityChange(
                change_type="property_removed",
                severity="breaking",
                path=f"components.schemas.{schema_name}.properties.{removed_prop}",
                description=f"Property '{removed_prop}' was removed from schema '{schema_name}'",
                old_value=removed_prop
            ))

        # Added required properties (BREAKING)
        for added_required in new_required - old_required:
            if added_required in new_prop_names:
                self.breaking_changes.append(CompatibilityChange(
                    change_type="property_made_required",
                    severity="breaking",
                    path=f"components.schemas.{schema_name}.required",
                    description=f"Property '{added_required}' is now required in schema '{schema_name}'",
                    new_value=added_required
                ))

        # Added optional properties (NON-BREAKING)
        for added_prop in new_prop_names - old_prop_names:
            if added_prop not in new_required:
                self.non_breaking_changes.append(CompatibilityChange(
                    change_type="property_added",
                    severity="non-breaking",
                    path=f"components.schemas.{schema_name}.properties.{added_prop}",
                    description=f"Optional property '{added_prop}' was added to schema '{schema_name}'",
                    new_value=added_prop
                ))

        # Check for type changes on existing properties
        for prop_name in old_prop_names & new_prop_names:
            old_type = old_props[prop_name].get("type")
            new_type = new_props[prop_name].get("type")

            if old_type != new_type:
                self.breaking_changes.append(CompatibilityChange(
                    change_type="property_type_changed",
                    severity="breaking",
                    path=f"components.schemas.{schema_name}.properties.{prop_name}.type",
                    description=f"Property '{prop_name}' type changed from '{old_type}' to '{new_type}' in schema '{schema_name}'",
                    old_value=old_type,
                    new_value=new_type
                ))

    def _check_parameters(self):
        """Check for changes in path/query parameters."""
        # Implementation for parameter checking
        pass

    def _check_responses(self):
        """Check for changes in response schemas."""
        # Implementation for response checking
        pass


def load_spec(spec_path: str) -> Dict[str, Any]:
    """
    Load API specification from file.

    Args:
        spec_path: Path to specification file

    Returns:
        Parsed specification

    Raises:
        BettyError: If file cannot be loaded
    """
    spec_file = Path(spec_path)

    if not spec_file.exists():
        raise BettyError(f"Specification file not found: {spec_path}")

    try:
        import yaml
        with open(spec_file, 'r') as f:
            spec = yaml.safe_load(f)

        if not isinstance(spec, dict):
            raise BettyError("Specification must be a valid YAML/JSON object")

        logger.info(f"Loaded specification from {spec_path}")
        return spec

    except Exception as e:
        raise BettyError(f"Failed to load specification: {e}")


def check_compatibility(
    old_spec_path: str,
    new_spec_path: str,
    fail_on_breaking: bool = True
) -> Dict[str, Any]:
    """
    Check compatibility between two API specifications.

    Args:
        old_spec_path: Path to old specification
        new_spec_path: Path to new specification
        fail_on_breaking: Whether to fail if breaking changes detected

    Returns:
        Compatibility report

    Raises:
        BettyError: If compatibility check fails
    """
    # Load specifications
    old_spec = load_spec(old_spec_path)
    new_spec = load_spec(new_spec_path)

    # Run compatibility check
    checker = CompatibilityChecker(old_spec, new_spec)
    report = checker.check()

    # Add metadata
    report["old_spec_path"] = old_spec_path
    report["new_spec_path"] = new_spec_path

    return report


def format_compatibility_output(report: Dict[str, Any]) -> str:
    """Format compatibility report for human-readable output."""
    lines = []

    lines.append("\n" + "=" * 60)
    lines.append("API Compatibility Report")
    lines.append("=" * 60)
    lines.append(f"Old: {report.get('old_spec_path', 'unknown')}")
    lines.append(f"New: {report.get('new_spec_path', 'unknown')}")
    lines.append("=" * 60 + "\n")

    # Breaking changes
    breaking = report.get("breaking_changes", [])
    if breaking:
        lines.append(f"❌ BREAKING CHANGES ({len(breaking)}):")
        for change in breaking:
            lines.append(f"  [{change.get('change_type', 'UNKNOWN')}] {change.get('description', '')}")
            if change.get('path'):
                lines.append(f"    Path: {change['path']}")
        lines.append("")

    # Non-breaking changes
    non_breaking = report.get("non_breaking_changes", [])
    if non_breaking:
        lines.append(f"✅ NON-BREAKING CHANGES ({len(non_breaking)}):")
        for change in non_breaking:
            lines.append(f"  [{change.get('change_type', 'UNKNOWN')}] {change.get('description', '')}")
        lines.append("")

    # Summary
    lines.append("=" * 60)
    if report.get("compatible"):
        lines.append("✅ BACKWARD COMPATIBLE")
    else:
        lines.append("❌ NOT BACKWARD COMPATIBLE")
    lines.append("=" * 60 + "\n")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Detect breaking changes between API specification versions"
    )
    parser.add_argument(
        "old_spec_path",
        type=str,
        help="Path to the old/previous API specification"
    )
    parser.add_argument(
        "new_spec_path",
        type=str,
        help="Path to the new/current API specification"
    )
    parser.add_argument(
        "--fail-on-breaking",
        action="store_true",
        default=True,
        help="Exit with error code if breaking changes detected (default: true)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "human"],
        default="json",
        help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        # Check if PyYAML is installed
        try:
            import yaml
        except ImportError:
            raise BettyError(
                "PyYAML is required for api.compatibility. Install with: pip install pyyaml"
            )

        # Validate inputs
        validate_path(args.old_spec_path)
        validate_path(args.new_spec_path)

        # Run compatibility check
        logger.info(f"Checking compatibility between {args.old_spec_path} and {args.new_spec_path}")
        report = check_compatibility(
            old_spec_path=args.old_spec_path,
            new_spec_path=args.new_spec_path,
            fail_on_breaking=args.fail_on_breaking
        )

        # Output based on format
        if args.format == "human":
            print(format_compatibility_output(report))
        else:
            output = {
                "status": "success",
                "data": report
            }
            print(json.dumps(output, indent=2))

        # Exit with error if breaking changes and fail_on_breaking is True
        if args.fail_on_breaking and not report["compatible"]:
            sys.exit(1)

    except Exception as e:
        logger.error(f"Compatibility check failed: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
