#!/usr/bin/env python3
"""
Validate SKILL.md documentation against skill.yaml manifests.

This skill ensures that SKILL.md files contain all required sections and that
documented fields match the corresponding skill.yaml manifest.
"""

import json
import sys
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import yaml


from betty.errors import BettyError, SkillValidationError
from betty.logging_utils import setup_logger
from betty.validation import validate_path, ValidationError
from betty.telemetry_integration import telemetry_tracked

logger = setup_logger(__name__)

# Required headers in SKILL.md
REQUIRED_HEADERS = [
    "Overview",
    "Purpose",
    "Usage",
    "Inputs",
    "Outputs",
    "Examples",
    "Integration",
    "Errors"
]

# Alternative header variations that are acceptable
HEADER_VARIATIONS = {
    "Overview": ["Overview", "## Overview", "Description"],
    "Purpose": ["Purpose", "## Purpose"],
    "Usage": ["Usage", "## Usage", "How to Use", "## How to Use"],
    "Inputs": ["Inputs", "## Inputs", "Parameters", "## Parameters"],
    "Outputs": ["Outputs", "## Outputs", "Output", "## Output"],
    "Examples": ["Examples", "## Examples", "Example", "## Example"],
    "Integration": ["Integration", "## Integration", "Integration with Hooks", "## Integration with Hooks", "Use in Workflows", "## Use in Workflows"],
    "Errors": ["Errors", "## Errors", "Error Codes", "## Error Codes", "Exit Codes", "## Exit Codes", "Common Errors", "## Common Errors"]
}


class ValidationIssue:
    """Represents a validation issue (error or warning)."""

    def __init__(self, issue_type: str, message: str, severity: str = "error",
                 file_path: Optional[str] = None, suggestion: Optional[str] = None):
        self.issue_type = issue_type
        self.message = message
        self.severity = severity
        self.file_path = file_path
        self.suggestion = suggestion

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result = {
            "type": self.issue_type,
            "message": self.message,
            "severity": self.severity
        }
        if self.file_path:
            result["file"] = self.file_path
        if self.suggestion:
            result["suggestion"] = self.suggestion
        return result


class SkillDocsValidator:
    """Validates SKILL.md documentation against skill.yaml manifest."""

    def __init__(self, skill_path: str, check_headers: bool = True,
                 check_manifest_parity: bool = True):
        self.skill_path = Path(skill_path)
        self.check_headers = check_headers
        self.check_manifest_parity = check_manifest_parity
        self.errors: List[ValidationIssue] = []
        self.warnings: List[ValidationIssue] = []
        self.manifest: Optional[Dict[str, Any]] = None
        self.skill_md_content: Optional[str] = None

    def validate(self) -> Dict[str, Any]:
        """Run all validation checks."""
        try:
            # Load manifest and documentation
            self._load_files()

            # Run checks
            if self.check_headers:
                self._validate_headers()

            if self.check_manifest_parity:
                self._validate_manifest_parity()

            # Build response
            return {
                "valid": len(self.errors) == 0,
                "skill_name": self.manifest.get("name") if self.manifest else "unknown",
                "skill_path": str(self.skill_path),
                "errors": [e.to_dict() for e in self.errors],
                "warnings": [w.to_dict() for w in self.warnings],
                "checks_run": {
                    "headers": self.check_headers,
                    "manifest_parity": self.check_manifest_parity
                }
            }

        except Exception as exc:
            logger.error("Validation failed: %s", exc)
            self.errors.append(ValidationIssue(
                "validation_error",
                str(exc),
                severity="error"
            ))
            return {
                "valid": False,
                "skill_name": "unknown",
                "skill_path": str(self.skill_path),
                "errors": [e.to_dict() for e in self.errors],
                "warnings": [w.to_dict() for w in self.warnings],
                "checks_run": {
                    "headers": self.check_headers,
                    "manifest_parity": self.check_manifest_parity
                }
            }

    def _load_files(self) -> None:
        """Load skill.yaml and SKILL.md files."""
        # Validate skill path
        try:
            validate_path(str(self.skill_path), must_exist=True)
        except ValidationError as exc:
            raise SkillValidationError(f"Invalid skill path: {exc}") from exc

        if not self.skill_path.is_dir():
            raise SkillValidationError(f"Skill path is not a directory: {self.skill_path}")

        # Load skill.yaml
        manifest_path = self.skill_path / "skill.yaml"
        if not manifest_path.exists():
            raise SkillValidationError(f"skill.yaml not found at {manifest_path}")

        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                self.manifest = yaml.safe_load(f)
        except Exception as exc:
            raise SkillValidationError(f"Failed to parse skill.yaml: {exc}") from exc

        # Load SKILL.md
        skill_md_path = self.skill_path / "SKILL.md"
        if not skill_md_path.exists():
            self.errors.append(ValidationIssue(
                "missing_file",
                "SKILL.md file not found",
                severity="error",
                file_path=str(skill_md_path),
                suggestion="Create SKILL.md documentation file"
            ))
            self.skill_md_content = ""
            return

        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                self.skill_md_content = f.read()
        except Exception as exc:
            raise SkillValidationError(f"Failed to read SKILL.md: {exc}") from exc

    def _validate_headers(self) -> None:
        """Validate that SKILL.md contains all required headers."""
        if not self.skill_md_content:
            return

        # Extract all headers from the markdown
        header_pattern = re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)
        found_headers = set()

        for match in header_pattern.finditer(self.skill_md_content):
            header_text = match.group(1).strip()
            found_headers.add(header_text)

        # Check each required header
        for required_header in REQUIRED_HEADERS:
            variations = HEADER_VARIATIONS.get(required_header, [required_header])

            # Check if any variation exists
            found = False
            for variation in variations:
                # Remove markdown prefix for comparison
                clean_variation = variation.replace("#", "").strip()
                if any(clean_variation.lower() in h.lower() for h in found_headers):
                    found = True
                    break

            if not found:
                self.errors.append(ValidationIssue(
                    "missing_header",
                    f"Required header '{required_header}' not found in SKILL.md",
                    severity="error",
                    file_path="SKILL.md",
                    suggestion=f"Add a '## {required_header}' section to SKILL.md"
                ))

    def _validate_manifest_parity(self) -> None:
        """Validate that SKILL.md matches skill.yaml manifest fields."""
        if not self.manifest or not self.skill_md_content:
            return

        # Check skill name
        skill_name = self.manifest.get("name", "")
        if skill_name and skill_name not in self.skill_md_content:
            self.warnings.append(ValidationIssue(
                "missing_skill_name",
                f"Skill name '{skill_name}' not found in SKILL.md",
                severity="warning",
                suggestion=f"Include the skill name '{skill_name}' in the documentation"
            ))

        # Check inputs
        manifest_inputs = self.manifest.get("inputs", [])
        if manifest_inputs:
            self._validate_inputs_documented(manifest_inputs)

        # Check outputs
        manifest_outputs = self.manifest.get("outputs", [])
        if manifest_outputs:
            self._validate_outputs_documented(manifest_outputs)

        # Check status
        status = self.manifest.get("status", "")
        if status and status not in ["active", "deprecated", "experimental"]:
            self.warnings.append(ValidationIssue(
                "invalid_status",
                f"Manifest status '{status}' is not a standard value",
                severity="warning",
                suggestion="Use 'active', 'deprecated', or 'experimental'"
            ))

        # Check tags
        tags = self.manifest.get("tags", [])
        if not tags:
            self.warnings.append(ValidationIssue(
                "missing_tags",
                "No tags defined in skill.yaml manifest",
                severity="warning",
                suggestion="Add relevant tags to improve skill discoverability"
            ))

    def _validate_inputs_documented(self, inputs: List[Any]) -> None:
        """Validate that all manifest inputs are documented in SKILL.md."""
        for input_spec in inputs:
            # Handle both string format and dict format
            if isinstance(input_spec, str):
                # Simple string format: "input_name (optional)"
                input_name = input_spec.split("(")[0].strip()
            elif isinstance(input_spec, dict):
                # Dictionary format with name, type, description
                input_name = input_spec.get("name", "")
            else:
                logger.warning("Unexpected input format: %s", type(input_spec))
                continue

            if not input_name:
                continue

            # Check if input is mentioned in the documentation
            # Look for various patterns: input_name, --input-name, `input_name`, etc.
            patterns = [
                input_name,
                f"`{input_name}`",
                f"--{input_name.replace('_', '-')}",
                f"`--{input_name.replace('_', '-')}`"
            ]

            found = any(pattern in self.skill_md_content for pattern in patterns)

            if not found:
                self.errors.append(ValidationIssue(
                    "undocumented_input",
                    f"Input '{input_name}' from manifest not documented in SKILL.md",
                    severity="error",
                    file_path="SKILL.md",
                    suggestion=f"Document the '{input_name}' input in the Inputs section"
                ))

    def _validate_outputs_documented(self, outputs: List[Any]) -> None:
        """Validate that all manifest outputs are documented in SKILL.md."""
        for output_spec in outputs:
            # Handle both string format and dict format
            if isinstance(output_spec, str):
                # Simple string format: "output_name.json" or just "output_name"
                output_name = output_spec.split(".")[0].strip()
            elif isinstance(output_spec, dict):
                # Dictionary format with name, type, description
                output_name = output_spec.get("name", "")
            else:
                logger.warning("Unexpected output format: %s", type(output_spec))
                continue

            if not output_name:
                continue

            # Check if output is mentioned in the documentation
            patterns = [
                output_name,
                f"`{output_name}`",
                f'"{output_name}"'
            ]

            found = any(pattern in self.skill_md_content for pattern in patterns)

            if not found:
                self.warnings.append(ValidationIssue(
                    "undocumented_output",
                    f"Output '{output_name}' from manifest not documented in SKILL.md",
                    severity="warning",
                    file_path="SKILL.md",
                    suggestion=f"Document the '{output_name}' output in the Outputs section"
                ))


def build_response(ok: bool, skill_path: str, errors: Optional[List[Dict[str, Any]]] = None,
                   warnings: Optional[List[Dict[str, Any]]] = None,
                   details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Build standard response format."""
    return {
        "ok": ok,
        "status": "valid" if ok else "invalid",
        "skill_path": skill_path,
        "errors": errors or [],
        "warnings": warnings or [],
        "details": details or {}
    }


def print_summary_table(results: List[Dict[str, Any]]) -> None:
    """Print a summary table of validation results."""
    print("\n" + "="*80)
    print("SKILL DOCUMENTATION VALIDATION SUMMARY")
    print("="*80)

    if not results:
        print("No skills validated.")
        return

    # Calculate column widths
    max_name_len = max(len(r.get("skill_name", "")) for r in results)
    max_name_len = max(max_name_len, len("Skill Name"))

    # Print header
    print(f"{'Skill Name':<{max_name_len}}  {'Status':<8}  {'Errors':<8}  {'Warnings':<8}")
    print("-" * 80)

    # Print each result
    total_errors = 0
    total_warnings = 0
    valid_count = 0

    for result in results:
        skill_name = result.get("skill_name", "unknown")
        valid = result.get("valid", False)
        error_count = len(result.get("errors", []))
        warning_count = len(result.get("warnings", []))

        status = "VALID" if valid else "INVALID"
        status_color = status

        print(f"{skill_name:<{max_name_len}}  {status:<8}  {error_count:<8}  {warning_count:<8}")

        total_errors += error_count
        total_warnings += warning_count
        if valid:
            valid_count += 1

    # Print summary
    print("-" * 80)
    print(f"Total: {len(results)} skills | Valid: {valid_count} | "
          f"Total Errors: {total_errors} | Total Warnings: {total_warnings}")
    print("="*80 + "\n")


@telemetry_tracked(skill_name="docs.validate.skill_docs", caller="cli")
def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    argv = argv or sys.argv[1:]

    # Parse arguments
    if len(argv) == 0:
        response = build_response(
            False,
            "",
            errors=[{
                "type": "usage_error",
                "message": "Usage: skill_docs_validate.py <skill_path> [--summary] [--no-headers] [--no-manifest-parity]",
                "severity": "error"
            }]
        )
        print(json.dumps(response, indent=2))
        return 1

    skill_path = argv[0]
    summary_mode = "--summary" in argv
    check_headers = "--no-headers" not in argv
    check_manifest_parity = "--no-manifest-parity" not in argv

    try:
        # Handle batch validation of multiple skills if path is parent directory
        skill_dir = Path(skill_path)

        # Check if this is a single skill or batch validation
        if (skill_dir / "skill.yaml").exists():
            # Single skill validation
            validator = SkillDocsValidator(
                skill_path,
                check_headers=check_headers,
                check_manifest_parity=check_manifest_parity
            )
            result = validator.validate()

            if summary_mode:
                print_summary_table([result])
            else:
                response = build_response(
                    result["valid"],
                    skill_path,
                    errors=result["errors"],
                    warnings=result["warnings"],
                    details=result
                )
                print(json.dumps(response, indent=2))

            return 0 if result["valid"] else 1

        else:
            # Batch validation - check if directory contains skill subdirectories
            if not skill_dir.is_dir():
                response = build_response(
                    False,
                    skill_path,
                    errors=[{
                        "type": "invalid_path",
                        "message": f"Path is not a directory: {skill_path}",
                        "severity": "error"
                    }]
                )
                print(json.dumps(response, indent=2))
                return 1

            # Find all skill directories
            results = []
            for subdir in sorted(skill_dir.iterdir()):
                if subdir.is_dir() and (subdir / "skill.yaml").exists():
                    validator = SkillDocsValidator(
                        str(subdir),
                        check_headers=check_headers,
                        check_manifest_parity=check_manifest_parity
                    )
                    result = validator.validate()
                    results.append(result)

            if not results:
                response = build_response(
                    False,
                    skill_path,
                    errors=[{
                        "type": "no_skills_found",
                        "message": f"No skills found in directory: {skill_path}",
                        "severity": "error"
                    }]
                )
                print(json.dumps(response, indent=2))
                return 1

            # Output results
            if summary_mode:
                print_summary_table(results)
            else:
                # Print full JSON for each skill
                for result in results:
                    response = build_response(
                        result["valid"],
                        result["skill_path"],
                        errors=result["errors"],
                        warnings=result["warnings"],
                        details=result
                    )
                    print(json.dumps(response, indent=2))
                    print()  # Blank line between results

            # Return error if any skill is invalid
            any_invalid = any(not r["valid"] for r in results)
            return 1 if any_invalid else 0

    except Exception as exc:
        logger.error("Validation failed: %s", exc, exc_info=True)
        response = build_response(
            False,
            skill_path,
            errors=[{
                "type": "validation_error",
                "message": str(exc),
                "severity": "error"
            }]
        )
        print(json.dumps(response, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
