#!/usr/bin/env python3
"""
Validate OpenAPI and AsyncAPI specifications against enterprise guidelines.

Supports:
- OpenAPI 3.x specifications
- AsyncAPI 3.x specifications
- Zalando RESTful API Guidelines
- Custom enterprise guidelines
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional
import urllib.request
import urllib.error

# Add betty module to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_path

logger = setup_logger(__name__)

# Zally server configuration
ZALLY_SERVER_URL = "http://localhost:8000"


def load_spec(spec_path: str) -> Dict[str, Any]:
    """
    Load API specification from file.

    Args:
        spec_path: Path to YAML or JSON specification file

    Returns:
        Parsed specification dictionary

    Raises:
        BettyError: If file cannot be loaded or parsed
    """
    spec_file = Path(spec_path)

    if not spec_file.exists():
        raise BettyError(f"Specification file not found: {spec_path}")

    if not spec_file.is_file():
        raise BettyError(f"Path is not a file: {spec_path}")

    try:
        import yaml
        with open(spec_file, 'r') as f:
            spec = yaml.safe_load(f)

        if not isinstance(spec, dict):
            raise BettyError("Specification must be a valid YAML/JSON object")

        logger.info(f"Loaded specification from {spec_path}")
        return spec

    except yaml.YAMLError as e:
        raise BettyError(f"Failed to parse YAML: {e}")
    except Exception as e:
        raise BettyError(f"Failed to load specification: {e}")


def detect_spec_type(spec: Dict[str, Any]) -> str:
    """
    Detect specification type (OpenAPI or AsyncAPI).

    Args:
        spec: Parsed specification

    Returns:
        Specification type: "openapi" or "asyncapi"

    Raises:
        BettyError: If type cannot be determined
    """
    if "openapi" in spec:
        version = spec["openapi"]
        logger.info(f"Detected OpenAPI {version} specification")
        return "openapi"
    elif "asyncapi" in spec:
        version = spec["asyncapi"]
        logger.info(f"Detected AsyncAPI {version} specification")
        return "asyncapi"
    else:
        raise BettyError(
            "Could not detect specification type. Must contain 'openapi' or 'asyncapi' field."
        )


def is_zally_available(server_url: str = ZALLY_SERVER_URL) -> bool:
    """
    Check if Zally server is running and accessible.

    Args:
        server_url: Zally server URL

    Returns:
        True if Zally server is available, False otherwise
    """
    try:
        # Try to reach Zally health endpoint
        health_url = f"{server_url}/health"
        req = urllib.request.Request(health_url, method="GET")
        with urllib.request.urlopen(req, timeout=2) as response:
            return response.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        return False


def validate_with_zally(spec_path: str, server_url: str = ZALLY_SERVER_URL) -> Dict[str, Any]:
    """
    Validate specification using Zally server.

    Args:
        spec_path: Path to specification file
        server_url: Zally server URL

    Returns:
        Validation report from Zally

    Raises:
        BettyError: If validation fails
    """
    try:
        # Read spec file
        with open(spec_path, 'r') as f:
            spec_content = f.read()

        # Prepare request to Zally
        api_url = f"{server_url}/api-violations"

        # Zally expects the spec as plain text in the request body
        data = spec_content.encode('utf-8')

        headers = {
            'Content-Type': 'application/yaml',
            'Accept': 'application/json'
        }

        req = urllib.request.Request(api_url, data=data, headers=headers, method='POST')

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))

        logger.info("Successfully validated with Zally")

        # Transform Zally response to our format
        return transform_zally_response(result)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        raise BettyError(f"Zally validation failed: {e.code} {e.reason}\n{error_body}")
    except urllib.error.URLError as e:
        raise BettyError(f"Could not connect to Zally server at {server_url}: {e.reason}")
    except Exception as e:
        raise BettyError(f"Zally validation error: {e}")


def transform_zally_response(zally_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transform Zally response to Betty's validation report format.

    Args:
        zally_result: Response from Zally API

    Returns:
        Validation report in Betty format
    """
    violations = zally_result.get('violations', [])

    errors = []
    warnings = []

    for violation in violations:
        violation_type = violation.get('violation_type', 'UNKNOWN')
        title = violation.get('title', 'Unknown violation')
        description = violation.get('description', '')
        paths = violation.get('paths', [])

        item = {
            'rule_id': violation_type,
            'message': title,
            'severity': 'error' if violation_type == 'MUST' else 'warning',
            'description': description
        }

        if paths:
            item['path'] = ', '.join(paths)

        if violation_type == 'MUST':
            errors.append(item)
        else:
            warnings.append(item)

    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'warnings': warnings,
        'validator': 'zally',
        'guideline_version': 'zalando-complete',
        'rules_checked': f"{len(violations)} Zally rules"
    }


def validate_openapi_zalando(spec: Dict[str, Any], strict: bool = False) -> Dict[str, Any]:
    """
    Validate OpenAPI specification against Zalando guidelines.

    Args:
        spec: OpenAPI specification
        strict: Enable strict mode (warnings become errors)

    Returns:
        Validation report
    """
    from validators.zalando_rules import ZalandoValidator

    validator = ZalandoValidator(spec, strict=strict)
    report = validator.validate()

    logger.info(
        f"Validation complete: {len(report['errors'])} errors, "
        f"{len(report['warnings'])} warnings"
    )

    return report


def validate_asyncapi(spec: Dict[str, Any], strict: bool = False) -> Dict[str, Any]:
    """
    Validate AsyncAPI specification.

    Args:
        spec: AsyncAPI specification
        strict: Enable strict mode

    Returns:
        Validation report
    """
    # Basic AsyncAPI validation
    errors = []
    warnings = []

    # Check required fields
    if "info" not in spec:
        errors.append({
            "rule_id": "ASYNCAPI_001",
            "message": "Missing required field 'info'",
            "severity": "error",
            "path": "info"
        })

    if "channels" not in spec:
        errors.append({
            "rule_id": "ASYNCAPI_002",
            "message": "Missing required field 'channels'",
            "severity": "error",
            "path": "channels"
        })

    # Check version
    asyncapi_version = spec.get("asyncapi", "unknown")
    if not asyncapi_version.startswith("3."):
        warnings.append({
            "rule_id": "ASYNCAPI_003",
            "message": f"AsyncAPI version {asyncapi_version} - consider upgrading to 3.x",
            "severity": "warning",
            "path": "asyncapi"
        })

    logger.info(f"AsyncAPI validation complete: {len(errors)} errors, {len(warnings)} warnings")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "spec_version": asyncapi_version,
        "rules_checked": [
            "ASYNCAPI_001: Required info field",
            "ASYNCAPI_002: Required channels field",
            "ASYNCAPI_003: Version check"
        ]
    }


def validate_spec(
    spec_path: str,
    guideline_set: str = "zalando",
    strict: bool = False,
    use_builtin: bool = False
) -> Dict[str, Any]:
    """
    Validate API specification against guidelines.

    Args:
        spec_path: Path to specification file
        guideline_set: Guidelines to validate against
        strict: Enable strict mode
        use_builtin: Force use of built-in validator instead of Zally

    Returns:
        Validation report

    Raises:
        BettyError: If validation fails
    """
    # Load specification
    spec = load_spec(spec_path)

    # Detect type
    spec_type = detect_spec_type(spec)

    # Validate based on type and guidelines
    if spec_type == "openapi":
        if guideline_set == "zalando":
            # Try Zally first (unless explicitly disabled)
            if not use_builtin and is_zally_available():
                logger.info("Using Zally for complete Zalando validation (100+ rules)")
                report = validate_with_zally(spec_path)
            else:
                if not use_builtin:
                    logger.warning(
                        "Zally server not available. Using built-in validator (14 rules). "
                        "For complete validation (100+ rules), install Zally: "
                        "https://github.com/zalando/zally"
                    )
                logger.info("Using built-in validator (14 rules)")
                report = validate_openapi_zalando(spec, strict=strict)
        else:
            raise BettyError(
                f"Guideline set '{guideline_set}' not yet supported for OpenAPI. "
                f"Supported: zalando"
            )
    elif spec_type == "asyncapi":
        report = validate_asyncapi(spec, strict=strict)
    else:
        raise BettyError(f"Unsupported specification type: {spec_type}")

    # Add metadata
    report["spec_path"] = spec_path
    report["spec_type"] = spec_type
    report["guideline_set"] = guideline_set

    return report


def format_validation_output(report: Dict[str, Any]) -> str:
    """
    Format validation report for human-readable output.

    Args:
        report: Validation report

    Returns:
        Formatted output string
    """
    lines = []

    # Header
    spec_path = report.get("spec_path", "unknown")
    spec_type = report.get("spec_type", "unknown").upper()
    lines.append(f"\n{'='*60}")
    lines.append(f"API Validation Report")
    lines.append(f"{'='*60}")
    lines.append(f"Spec: {spec_path}")
    lines.append(f"Type: {spec_type}")
    lines.append(f"Guidelines: {report.get('guideline_set', 'unknown')}")
    lines.append(f"{'='*60}\n")

    # Errors
    errors = report.get("errors", [])
    if errors:
        lines.append(f"❌ ERRORS ({len(errors)}):")
        for error in errors:
            lines.append(f"  [{error.get('rule_id', 'UNKNOWN')}] {error.get('message', '')}")
            if error.get('path'):
                lines.append(f"    Path: {error['path']}")
            if error.get('suggestion'):
                lines.append(f"    💡 {error['suggestion']}")
        lines.append("")

    # Warnings
    warnings = report.get("warnings", [])
    if warnings:
        lines.append(f"⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            lines.append(f"  [{warning.get('rule_id', 'UNKNOWN')}] {warning.get('message', '')}")
            if warning.get('path'):
                lines.append(f"    Path: {warning['path']}")
            if warning.get('suggestion'):
                lines.append(f"    💡 {warning['suggestion']}")
        lines.append("")

    # Summary
    lines.append(f"{'='*60}")
    if report.get("valid"):
        lines.append("✅ Validation PASSED")
    else:
        lines.append("❌ Validation FAILED")
    lines.append(f"{'='*60}\n")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validate API specifications against enterprise guidelines"
    )
    parser.add_argument(
        "spec_path",
        type=str,
        help="Path to the API specification file (YAML or JSON)"
    )
    parser.add_argument(
        "guideline_set",
        type=str,
        nargs="?",
        default="zalando",
        choices=["zalando", "google", "microsoft"],
        help="Guidelines to validate against (default: zalando)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode (warnings become errors)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "human"],
        default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--use-builtin",
        action="store_true",
        help="Use built-in validator instead of Zally (14 rules vs 100+)"
    )

    args = parser.parse_args()

    try:
        # Check if PyYAML is installed
        try:
            import yaml
        except ImportError:
            raise BettyError(
                "PyYAML is required for api.validate. Install with: pip install pyyaml"
            )

        # Validate inputs
        validate_path(args.spec_path)

        # Run validation
        logger.info(f"Validating {args.spec_path} against {args.guideline_set} guidelines")
        report = validate_spec(
            spec_path=args.spec_path,
            guideline_set=args.guideline_set,
            strict=args.strict,
            use_builtin=args.use_builtin
        )

        # Output based on format
        if args.format == "human":
            print(format_validation_output(report))
        else:
            output = {
                "status": "success",
                "data": report
            }
            print(json.dumps(output, indent=2))

        # Exit with error code if validation failed
        if not report["valid"]:
            sys.exit(1)

    except Exception as e:
        logger.error(f"Validation failed: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
