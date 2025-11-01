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
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Generate router configuration

        Args:
            llm_backends: List of backend provider configs
            routing_rules: Dictionary of routing context mappings
            metadata: Optional metadata for audit/tracking

        Returns:
            Complete router configuration
        """
        config = {
            "version": self.CONFIG_VERSION,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "backends": self._format_backends(llm_backends),
            "routing": self._format_routing(routing_rules),
            "metadata": self._build_metadata(metadata or {})
        }

        return config

    def _format_backends(self, backends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format backend configurations"""
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

            # Include any additional provider-specific settings
            for key, value in backend.items():
                if key not in ["name", "api_base_url", "models", "api_key"]:
                    entry[key] = value

            formatted.append(entry)

        return formatted

    def _format_routing(self, routing_rules: Dict[str, Any]) -> Dict[str, Any]:
        """Format routing rules"""
        formatted = {}
        for context, rule in routing_rules.items():
            formatted[context] = {
                "provider": rule["provider"],
                "model": rule["model"]
            }

            # Include any additional routing settings
            for key, value in rule.items():
                if key not in ["provider", "model"]:
                    formatted[context][key] = value

        return formatted

    def _build_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Build metadata section"""
        meta = {
            "generated_by": "meta.config.router",
            "schema_version": self.CONFIG_VERSION
        }

        # Merge provided metadata
        meta.update(metadata)

        return meta


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
            metadata=input_data.get("metadata", {})
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
