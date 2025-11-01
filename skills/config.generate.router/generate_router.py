#!/usr/bin/env python3
"""
Skill: config.generate.router
Generates Claude Code Router configuration
"""

import json
import sys
from datetime import datetime
from typing import Dict, List, Any


class RouterConfigGenerator:
    """Generates router configuration for Claude Code"""

    CONFIG_VERSION = "1.0.0"

    def generate(
        self,
        llm_backends: List[Dict[str, Any]],
        routing_rules: Dict[str, Any],
        config_options: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Generate router configuration matching Claude Code Router schema

        Args:
            llm_backends: List of backend provider configs
            routing_rules: Dictionary of routing context mappings
            config_options: Optional config settings (LOG, API_TIMEOUT_MS, etc.)

        Returns:
            Complete router configuration in Claude Code Router format
        """
        options = config_options or {}

        config = {
            "Providers": self._format_providers(llm_backends),
            "Router": self._format_router(routing_rules)
        }

        # Add optional configuration fields if provided
        if "LOG" in options:
            config["LOG"] = options["LOG"]
        if "LOG_LEVEL" in options:
            config["LOG_LEVEL"] = options["LOG_LEVEL"]
        if "API_TIMEOUT_MS" in options:
            config["API_TIMEOUT_MS"] = options["API_TIMEOUT_MS"]
        if "NON_INTERACTIVE_MODE" in options:
            config["NON_INTERACTIVE_MODE"] = options["NON_INTERACTIVE_MODE"]
        if "APIKEY" in options:
            config["APIKEY"] = options["APIKEY"]
        if "PROXY_URL" in options:
            config["PROXY_URL"] = options["PROXY_URL"]
        if "CUSTOM_ROUTER_PATH" in options:
            config["CUSTOM_ROUTER_PATH"] = options["CUSTOM_ROUTER_PATH"]
        if "HOST" in options:
            config["HOST"] = options["HOST"]

        return config

    def _format_providers(self, backends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format provider configurations for Claude Code Router"""
        formatted = []
        for backend in backends:
            entry = {
                "name": backend["name"],
                "api_base_url": backend["api_base_url"],
                "models": backend["models"]
            }

            # Only include API key if present (not for local providers)
            if backend.get("api_key"):
                entry["api_key"] = backend["api_key"]

            # Include transformer if specified
            if backend.get("transformer"):
                entry["transformer"] = backend["transformer"]

            # Include any additional provider-specific settings
            for key, value in backend.items():
                if key not in ["name", "api_base_url", "models", "api_key", "transformer"]:
                    entry[key] = value

            formatted.append(entry)

        return formatted

    def _format_router(self, routing_rules: Dict[str, Any]) -> Dict[str, str]:
        """
        Format routing rules for Claude Code Router

        Converts from object format to "provider,model" string format:
        Input:  {"provider": "openrouter", "model": "claude-3.5-sonnet"}
        Output: "openrouter,claude-3.5-sonnet"
        """
        formatted = {}
        for context, rule in routing_rules.items():
            provider = rule["provider"]
            model = rule["model"]
            # Claude Code Router expects "provider,model" string format
            formatted[context] = f"{provider},{model}"

        return formatted


def main():
    """CLI entrypoint"""
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: generate_router.py <input_json>"
        }))
        sys.exit(1)

    try:
        input_data = json.loads(sys.argv[1])

        generator = RouterConfigGenerator()
        config = generator.generate(
            llm_backends=input_data.get("llm_backends", []),
            routing_rules=input_data.get("routing_rules", {}),
            config_options=input_data.get("config_options", {})
        )

        print(json.dumps(config, indent=2))
        sys.exit(0)

    except json.JSONDecodeError as e:
        print(json.dumps({
            "error": f"Invalid JSON: {e}"
        }))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({
            "error": f"Generation error: {e}"
        }))
        sys.exit(1)


if __name__ == "__main__":
    main()
