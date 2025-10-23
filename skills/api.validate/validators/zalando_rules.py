"""
Zalando RESTful API Guidelines validation rules.

Based on: https://opensource.zalando.com/restful-api-guidelines/
"""

from typing import Dict, List, Any, Optional
import re


class ValidationError:
    """Represents a validation error or warning."""

    def __init__(
        self,
        rule_id: str,
        message: str,
        severity: str = "error",
        path: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        self.rule_id = rule_id
        self.message = message
        self.severity = severity  # "error" or "warning"
        self.path = path
        self.suggestion = suggestion

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result = {
            "rule_id": self.rule_id,
            "message": self.message,
            "severity": self.severity
        }
        if self.path:
            result["path"] = self.path
        if self.suggestion:
            result["suggestion"] = self.suggestion
        return result


class ZalandoValidator:
    """Validates OpenAPI specs against Zalando guidelines."""

    def __init__(self, spec: Dict[str, Any], strict: bool = False):
        self.spec = spec
        self.strict = strict
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def validate(self) -> Dict[str, Any]:
        """
        Run all validation rules.

        Returns:
            Validation report with errors and warnings
        """
        # Required metadata
        self._check_required_metadata()

        # Naming conventions
        self._check_naming_conventions()

        # HTTP methods and status codes
        self._check_http_methods()
        self._check_status_codes()

        # Error handling
        self._check_error_responses()

        # Headers
        self._check_required_headers()

        # Security
        self._check_security_schemes()

        return {
            "valid": len(self.errors) == 0 and (not self.strict or len(self.warnings) == 0),
            "errors": [e.to_dict() for e in self.errors],
            "warnings": [w.to_dict() for w in self.warnings],
            "guideline_version": "zalando-1.0",
            "rules_checked": self._get_rules_checked()
        }

    def _add_error(self, rule_id: str, message: str, path: str = None, suggestion: str = None):
        """Add a validation error."""
        self.errors.append(ValidationError(rule_id, message, "error", path, suggestion))

    def _add_warning(self, rule_id: str, message: str, path: str = None, suggestion: str = None):
        """Add a validation warning."""
        if self.strict:
            self.errors.append(ValidationError(rule_id, message, "error", path, suggestion))
        else:
            self.warnings.append(ValidationError(rule_id, message, "warning", path, suggestion))

    def _check_required_metadata(self):
        """
        Check required metadata fields.
        Zalando requires: x-api-id, x-audience
        """
        info = self.spec.get("info", {})

        # Check x-api-id (MUST)
        if "x-api-id" not in info:
            self._add_error(
                "MUST_001",
                "Missing required field 'info.x-api-id'",
                "info.x-api-id",
                "Add a UUID to uniquely identify this API: x-api-id: 'd0184f38-b98d-11e7-9c56-68f728c1ba70'"
            )
        else:
            # Validate UUID format
            api_id = info["x-api-id"]
            uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
            if not re.match(uuid_pattern, str(api_id), re.IGNORECASE):
                self._add_error(
                    "MUST_001",
                    f"'info.x-api-id' must be a valid UUID, got: {api_id}",
                    "info.x-api-id"
                )

        # Check x-audience (MUST)
        if "x-audience" not in info:
            self._add_error(
                "MUST_002",
                "Missing required field 'info.x-audience'",
                "info.x-audience",
                "Specify target audience: x-audience: 'component-internal' | 'company-internal' | 'external-partner' | 'external-public'"
            )
        else:
            valid_audiences = ["component-internal", "company-internal", "external-partner", "external-public"]
            audience = info["x-audience"]
            if audience not in valid_audiences:
                self._add_error(
                    "MUST_002",
                    f"'info.x-audience' must be one of: {', '.join(valid_audiences)}",
                    "info.x-audience"
                )

        # Check contact information (SHOULD)
        if "contact" not in info:
            self._add_warning(
                "SHOULD_001",
                "Missing 'info.contact' - should provide API owner contact information",
                "info.contact",
                "Add contact information: contact: {name: 'Team Name', email: 'team@company.com'}"
            )

    def _check_naming_conventions(self):
        """
        Check naming conventions.
        Zalando requires: snake_case for properties, kebab-case or snake_case for paths
        """
        # Check path naming
        paths = self.spec.get("paths", {})
        for path in paths.keys():
            # Remove path parameters for checking
            path_without_params = re.sub(r'\{[^}]+\}', '', path)
            segments = [s for s in path_without_params.split('/') if s]

            for segment in segments:
                # Should be kebab-case or snake_case
                if not re.match(r'^[a-z0-9_-]+$', segment):
                    self._add_error(
                        "MUST_003",
                        f"Path segment '{segment}' should use lowercase kebab-case or snake_case",
                        f"paths.{path}",
                        f"Use lowercase: {segment.lower()}"
                    )

        # Check schema property naming (should be snake_case)
        schemas = self.spec.get("components", {}).get("schemas", {})
        for schema_name, schema in schemas.items():
            if "properties" in schema and schema["properties"] is not None and isinstance(schema["properties"], dict):
                for prop_name in schema["properties"].keys():
                    if not re.match(r'^[a-z][a-z0-9_]*$', prop_name):
                        self._add_error(
                            "MUST_004",
                            f"Property '{prop_name}' in schema '{schema_name}' should use snake_case",
                            f"components.schemas.{schema_name}.properties.{prop_name}",
                            f"Use snake_case: {self._to_snake_case(prop_name)}"
                        )

    def _check_http_methods(self):
        """
        Check HTTP methods are used correctly.
        """
        paths = self.spec.get("paths", {})
        for path, path_item in paths.items():
            for method in path_item.keys():
                if method.upper() not in ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "PARAMETERS"]:
                    continue

                operation = path_item[method]

                # GET should not have requestBody
                if method.upper() == "GET" and "requestBody" in operation:
                    self._add_error(
                        "MUST_005",
                        f"GET operation should not have requestBody",
                        f"paths.{path}.get.requestBody"
                    )

                # POST should return 201 for resource creation
                if method.upper() == "POST":
                    responses = operation.get("responses", {})
                    if "201" not in responses and "200" not in responses:
                        self._add_warning(
                            "SHOULD_002",
                            "POST operation should return 201 (Created) for resource creation",
                            f"paths.{path}.post.responses"
                        )

    def _check_status_codes(self):
        """
        Check proper use of HTTP status codes.
        """
        paths = self.spec.get("paths", {})
        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.upper() not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                    continue

                responses = operation.get("responses", {})

                # All operations should document error responses
                if "400" not in responses:
                    self._add_warning(
                        "SHOULD_003",
                        f"{method.upper()} operation should document 400 (Bad Request) response",
                        f"paths.{path}.{method}.responses"
                    )

                if "500" not in responses:
                    self._add_warning(
                        "SHOULD_004",
                        f"{method.upper()} operation should document 500 (Internal Error) response",
                        f"paths.{path}.{method}.responses"
                    )

                # Check 201 has Location header
                if "201" in responses:
                    response_201 = responses["201"]
                    headers = response_201.get("headers", {})
                    if "Location" not in headers:
                        self._add_warning(
                            "SHOULD_005",
                            "201 (Created) response should include Location header",
                            f"paths.{path}.{method}.responses.201.headers",
                            "Add: headers: {Location: {schema: {type: string, format: uri}}}"
                        )

    def _check_error_responses(self):
        """
        Check error responses use RFC 7807 Problem JSON.
        Zalando requires: application/problem+json for errors
        """
        # Check if Problem schema exists
        schemas = self.spec.get("components", {}).get("schemas", {})
        has_problem_schema = "Problem" in schemas

        if not has_problem_schema:
            self._add_warning(
                "SHOULD_006",
                "Missing 'Problem' schema for RFC 7807 error responses",
                "components.schemas",
                "Add Problem schema following RFC 7807: https://datatracker.ietf.org/doc/html/rfc7807"
            )

        # Check error responses use application/problem+json
        paths = self.spec.get("paths", {})
        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.upper() not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                    continue

                responses = operation.get("responses", {})
                for status_code, response in responses.items():
                    # Check 4xx and 5xx responses
                    if status_code.startswith("4") or status_code.startswith("5"):
                        content = response.get("content", {})
                        if content and "application/problem+json" not in content:
                            self._add_warning(
                                "SHOULD_007",
                                f"Error response {status_code} should use 'application/problem+json' content type",
                                f"paths.{path}.{method}.responses.{status_code}.content"
                            )

    def _check_required_headers(self):
        """
        Check for required headers.
        Zalando requires: X-Flow-ID for request tracing
        """
        # Check if responses document X-Flow-ID
        paths = self.spec.get("paths", {})
        missing_flow_id = []

        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.upper() not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                    continue

                responses = operation.get("responses", {})
                for status_code, response in responses.items():
                    if status_code.startswith("2"):  # Success responses
                        headers = response.get("headers", {})
                        if "X-Flow-ID" not in headers and "X-Flow-Id" not in headers:
                            missing_flow_id.append(f"paths.{path}.{method}.responses.{status_code}")

        if missing_flow_id and len(missing_flow_id) > 0:
            self._add_warning(
                "SHOULD_008",
                f"Success responses should include X-Flow-ID header for request tracing",
                missing_flow_id[0],
                "Add: headers: {X-Flow-ID: {schema: {type: string, format: uuid}}}"
            )

    def _check_security_schemes(self):
        """
        Check security schemes are defined.
        """
        components = self.spec.get("components", {})
        security_schemes = components.get("securitySchemes", {})

        if not security_schemes:
            self._add_warning(
                "SHOULD_009",
                "No security schemes defined - consider adding authentication",
                "components.securitySchemes",
                "Add security schemes: bearerAuth, oauth2, etc."
            )

    def _get_rules_checked(self) -> List[str]:
        """Get list of rules that were checked."""
        return [
            "MUST_001: Required x-api-id metadata",
            "MUST_002: Required x-audience metadata",
            "MUST_003: Path naming conventions",
            "MUST_004: Property naming conventions (snake_case)",
            "MUST_005: HTTP method usage",
            "SHOULD_001: Contact information",
            "SHOULD_002: POST returns 201",
            "SHOULD_003: Document 400 errors",
            "SHOULD_004: Document 500 errors",
            "SHOULD_005: 201 includes Location header",
            "SHOULD_006: Problem schema for errors",
            "SHOULD_007: Error responses use application/problem+json",
            "SHOULD_008: X-Flow-ID header for tracing",
            "SHOULD_009: Security schemes defined"
        ]

    @staticmethod
    def _to_snake_case(text: str) -> str:
        """Convert text to snake_case."""
        # Insert underscore before uppercase letters
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        # Insert underscore before uppercase letters preceded by lowercase
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
        return s2.lower()
