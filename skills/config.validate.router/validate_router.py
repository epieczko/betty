#!/usr/bin/env python3
"""
Skill: config.validate.router
Validates Claude Code Router configuration inputs
"""

import json
import sys
from typing import Dict, List, Any


class RouterConfigValidator:
    """Validates router configuration for Claude Code Router"""

    # Claude Code Router supports these routing contexts
    VALID_ROUTING_CONTEXTS = {"default", "think", "background", "longContext", "webSearch", "image"}
    REQUIRED_PROVIDER_FIELDS = {"name", "api_base_url", "models"}
    REQUIRED_ROUTING_FIELDS = {"provider", "model"}

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate(self, llm_backends: List[Dict[str, Any]], routing_rules: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate router configuration

        Args:
            llm_backends: List of backend provider configs
            routing_rules: Dictionary of routing context mappings

        Returns:
            Validation result with status, errors, and warnings
        """
        self.errors = []
        self.warnings = []

        # Validate backends
        self._validate_backends(llm_backends)

        # Validate routing rules
        self._validate_routing_rules(routing_rules, llm_backends)

        return {
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings
        }

    def _validate_backends(self, backends: List[Dict[str, Any]]) -> None:
        """Validate backend provider configurations"""
        if not backends:
            self.errors.append("llm_backends cannot be empty")
            return

        seen_names = set()
        for idx, backend in enumerate(backends):
            # Check required fields
            missing = self.REQUIRED_PROVIDER_FIELDS - set(backend.keys())
            if missing:
                self.errors.append(f"Backend {idx}: missing required fields {missing}")

            # Check name uniqueness
            name = backend.get("name")
            if name:
                if name in seen_names:
                    self.errors.append(f"Duplicate backend name: {name}")
                seen_names.add(name)

            # Validate models list
            models = backend.get("models", [])
            if not isinstance(models, list):
                self.errors.append(f"Backend {name or idx}: 'models' must be a list")
            elif not models:
                self.errors.append(f"Backend {name or idx}: 'models' cannot be empty")

            # Validate API base URL format
            api_base_url = backend.get("api_base_url", "")
            if api_base_url and not (api_base_url.startswith("http://") or
                                     api_base_url.startswith("https://")):
                self.warnings.append(
                    f"Backend {name or idx}: api_base_url should start with http:// or https://"
                )

            # Check for API key in local providers
            if "localhost" in api_base_url or "127.0.0.1" in api_base_url:
                if backend.get("api_key"):
                    self.warnings.append(
                        f"Backend {name or idx}: Local provider has api_key (may be unnecessary)"
                    )
            elif not backend.get("api_key"):
                self.warnings.append(
                    f"Backend {name or idx}: Remote provider missing api_key"
                )

    def _validate_routing_rules(
        self,
        routing_rules: Dict[str, Any],
        backends: List[Dict[str, Any]]
    ) -> None:
        """Validate routing rule mappings"""
        if not routing_rules:
            self.errors.append("routing_rules cannot be empty")
            return

        # Build provider-model map
        provider_models = {}
        for backend in backends:
            name = backend.get("name")
            models = backend.get("models", [])
            if name:
                provider_models[name] = set(models)

        # Validate each routing context
        for context, rule in routing_rules.items():
            # Warn about unknown contexts
            if context not in self.VALID_ROUTING_CONTEXTS:
                self.warnings.append(f"Unknown routing context: {context}")

            # Check required fields
            if not isinstance(rule, dict):
                self.errors.append(f"Routing rule '{context}' must be an object")
                continue

            missing = self.REQUIRED_ROUTING_FIELDS - set(rule.keys())
            if missing:
                self.errors.append(
                    f"Routing rule '{context}': missing required fields {missing}"
                )
                continue

            provider = rule.get("provider")
            model = rule.get("model")

            # Validate provider exists
            if provider not in provider_models:
                self.errors.append(
                    f"Routing rule '{context}': unknown provider '{provider}'"
                )
                continue

            # Validate model exists for provider
            if model not in provider_models[provider]:
                self.errors.append(
                    f"Routing rule '{context}': model '{model}' not available "
                    f"in provider '{provider}'"
                )

        # Check for missing essential contexts
        essential = {"default"}
        missing_essential = essential - set(routing_rules.keys())
        if missing_essential:
            self.errors.append(f"Missing essential routing contexts: {missing_essential}")


def main():
    """CLI entrypoint"""
    if len(sys.argv) < 2:
        print(json.dumps({
            "valid": False,
            "errors": ["Usage: validate_router.py <config_json>"],
            "warnings": []
        }))
        sys.exit(1)

    try:
        config = json.loads(sys.argv[1])

        validator = RouterConfigValidator()
        result = validator.validate(
            llm_backends=config.get("llm_backends", []),
            routing_rules=config.get("routing_rules", {})
        )

        print(json.dumps(result, indent=2))
        sys.exit(0 if result["valid"] else 1)

    except json.JSONDecodeError as e:
        print(json.dumps({
            "valid": False,
            "errors": [f"Invalid JSON: {e}"],
            "warnings": []
        }))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({
            "valid": False,
            "errors": [f"Validation error: {e}"],
            "warnings": []
        }))
        sys.exit(1)


if __name__ == "__main__":
    main()
