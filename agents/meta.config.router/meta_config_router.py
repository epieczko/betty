#!/usr/bin/env python3
"""
Agent: meta.config.router
Configure Claude Code Router for multi-model LLM support
"""

import json
import sys
import os
import hashlib
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import subprocess
import yaml


class MetaConfigRouter:
    """Configure Claude Code Router for Betty Framework"""

    def __init__(self):
        self.betty_root = Path(__file__).parent.parent.parent
        self.skills_root = self.betty_root / "skills"
        self.audit_log_path = self.betty_root / "registry" / "audit_log.json"

    def run(
        self,
        routing_config_path: str,
        apply_config: bool = False,
        output_mode: str = "preview"
    ) -> Dict[str, Any]:
        """
        Main execution method

        Args:
            routing_config_path: Path to router config input file (YAML or JSON)
            apply_config: Whether to write config to disk
            output_mode: "preview" | "file" | "both"

        Returns:
            Result with routing_config, write_status, and audit_id
        """
        print(f"🔧 meta.config.router v0.1.0")
        print(f"📋 Config input: {routing_config_path}")
        print(f"📝 Output mode: {output_mode}")
        print(f"💾 Apply config: {apply_config}")
        print()

        # Load input config
        config_input = self._load_config_input(routing_config_path)

        # Extract inputs
        llm_backends = config_input.get("llm_backends", [])
        routing_rules = config_input.get("routing_rules", {})
        metadata = config_input.get("metadata", {})

        # Step 1: Validate inputs
        print("🔍 Validating router configuration...")
        validation_result = self._validate_config(llm_backends, routing_rules)

        if not validation_result["valid"]:
            print("❌ Validation failed:")
            for error in validation_result["errors"]:
                print(f"   - {error}")
            return {
                "success": False,
                "errors": validation_result["errors"],
                "warnings": validation_result["warnings"]
            }

        if validation_result["warnings"]:
            print("⚠️  Warnings:")
            for warning in validation_result["warnings"]:
                print(f"   - {warning}")

        print("✅ Validation passed")
        print()

        # Step 2: Generate router config
        print("🏗️  Generating router configuration...")
        router_config = self._generate_config(
            llm_backends,
            routing_rules,
            metadata
        )
        print("✅ Configuration generated")
        print()

        # Step 3: Write config if requested
        write_status = "skipped"
        config_path = None

        if apply_config and output_mode != "preview":
            print("💾 Writing configuration to disk...")
            config_path, write_status = self._write_config(router_config)

            if write_status == "success":
                print(f"✅ Configuration written to: {config_path}")
            else:
                print(f"❌ Failed to write configuration")
            print()

        # Step 4: Log audit record
        print("📝 Logging audit record...")
        audit_id = self._log_audit(
            config_input=config_input,
            write_status=write_status,
            metadata=metadata
        )
        print(f"✅ Audit ID: {audit_id}")
        print()

        # Step 5: Output results
        result = {
            "success": True,
            "routing_config": router_config,
            "write_status": write_status,
            "audit_id": audit_id
        }

        if config_path:
            result["config_path"] = str(config_path)

        # Display preview if requested
        if output_mode in ["preview", "both"]:
            print("📄 Router Configuration Preview:")
            print("─" * 80)
            print(json.dumps(router_config, indent=2))
            print("─" * 80)
            print()

        return result

    def _load_config_input(self, config_path: str) -> Dict[str, Any]:
        """Load router config input from YAML or JSON file"""
        path = Path(config_path)

        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(path, 'r') as f:
            if path.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            else:
                return json.load(f)

    def _validate_config(
        self,
        llm_backends: List[Dict[str, Any]],
        routing_rules: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Validate router configuration using config.validate.router skill"""
        validator_script = self.skills_root / "config.validate.router" / "validate_router.py"

        config_json = json.dumps({
            "llm_backends": llm_backends,
            "routing_rules": routing_rules
        })

        try:
            result = subprocess.run(
                [sys.executable, str(validator_script), config_json],
                capture_output=True,
                text=True,
                check=False
            )

            return json.loads(result.stdout)
        except Exception as e:
            return {
                "valid": False,
                "errors": [f"Validation error: {e}"],
                "warnings": []
            }

    def _generate_config(
        self,
        llm_backends: List[Dict[str, Any]],
        routing_rules: Dict[str, Any],
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate router configuration using config.generate.router skill"""
        generator_script = self.skills_root / "config.generate.router" / "generate_router.py"

        # Add environment fingerprint to metadata
        metadata["environment"] = self._detect_environment()
        metadata["audit_id"] = str(uuid.uuid4())

        input_json = json.dumps({
            "llm_backends": llm_backends,
            "routing_rules": routing_rules,
            "metadata": metadata
        })

        try:
            result = subprocess.run(
                [sys.executable, str(generator_script), input_json],
                capture_output=True,
                text=True,
                check=True
            )

            return json.loads(result.stdout)
        except Exception as e:
            raise RuntimeError(f"Config generation failed: {e}")

    def _write_config(self, router_config: Dict[str, Any]) -> tuple[Path, str]:
        """Write router config to ~/.claude-code-router/config.json"""
        try:
            config_dir = Path.home() / ".claude-code-router"
            config_dir.mkdir(parents=True, exist_ok=True)

            config_path = config_dir / "config.json"

            with open(config_path, 'w') as f:
                json.dump(router_config, f, indent=2)

            return config_path, "success"
        except Exception as e:
            print(f"Error writing config: {e}")
            return None, "error"

    def _log_audit(
        self,
        config_input: Dict[str, Any],
        write_status: str,
        metadata: Dict[str, Any]
    ) -> str:
        """Log audit record for configuration event"""
        audit_id = str(uuid.uuid4())

        # Calculate hash of input
        input_hash = hashlib.sha256(
            json.dumps(config_input, sort_keys=True).encode()
        ).hexdigest()[:16]

        audit_entry = {
            "audit_id": audit_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agent": "meta.config.router",
            "version": "0.1.0",
            "action": "router_config_generated",
            "write_status": write_status,
            "input_hash": input_hash,
            "environment": self._detect_environment(),
            "initiator": metadata.get("initiator", "unknown"),
            "metadata": metadata
        }

        # Append to audit log
        try:
            if self.audit_log_path.exists():
                with open(self.audit_log_path, 'r') as f:
                    audit_log = json.load(f)
            else:
                audit_log = []

            audit_log.append(audit_entry)

            with open(self.audit_log_path, 'w') as f:
                json.dump(audit_log, f, indent=2)
        except Exception as e:
            print(f"Warning: Failed to write audit log: {e}")

        return audit_id

    def _detect_environment(self) -> str:
        """Detect execution environment (local, cloud, ci)"""
        if os.getenv("CI"):
            return "ci"
        elif os.getenv("CLOUD_ENV"):
            return "cloud"
        else:
            return "local"


def main():
    """CLI entrypoint"""
    if len(sys.argv) < 2:
        print("Usage: meta_config_router.py <routing_config_path> [--apply_config] [--output_mode=<mode>]")
        print()
        print("Arguments:")
        print("  routing_config_path    Path to router config input file (YAML or JSON)")
        print("  --apply_config         Write config to ~/.claude-code-router/config.json")
        print("  --output_mode=MODE     Output mode: preview, file, or both (default: preview)")
        sys.exit(1)

    # Parse arguments
    routing_config_path = sys.argv[1]
    apply_config = "--apply_config" in sys.argv or "--apply-config" in sys.argv
    output_mode = "preview"

    for arg in sys.argv[2:]:
        if arg.startswith("--output_mode=") or arg.startswith("--output-mode="):
            output_mode = arg.split("=")[1]

    # Run agent
    agent = MetaConfigRouter()
    try:
        result = agent.run(
            routing_config_path=routing_config_path,
            apply_config=apply_config,
            output_mode=output_mode
        )

        if result["success"]:
            print("✅ meta.config.router completed successfully")
            print(f"📋 Audit ID: {result['audit_id']}")
            print(f"💾 Write status: {result['write_status']}")
            sys.exit(0)
        else:
            print("❌ meta.config.router failed")
            for error in result.get("errors", []):
                print(f"   - {error}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
