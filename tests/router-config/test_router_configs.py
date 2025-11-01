#!/usr/bin/env python3
"""
Test suite for meta.config.router
Validates example configurations and generated outputs
"""

import json
import os
import subprocess
import sys
from pathlib import Path
import yaml

# Add parent directory to path for imports
betty_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(betty_root))


class RouterConfigTester:
    """Test suite for router configuration generation"""

    def __init__(self):
        self.betty_root = betty_root
        self.examples_dir = self.betty_root / "examples" / "router-configs"
        self.agent_script = self.betty_root / "agents" / "meta.config.router" / "meta_config_router.py"
        self.passed = 0
        self.failed = 0
        self.errors = []

    def run_all_tests(self):
        """Run all test suites"""
        print("=" * 80)
        print("🧪 Testing meta.config.router")
        print("=" * 80)
        print()

        # Test 1: Validate all example configs
        self.test_example_configs()

        # Test 2: Test schema compliance
        self.test_schema_compliance()

        # Test 3: Test validation logic
        self.test_validation_logic()

        # Print summary
        self.print_summary()

        return self.failed == 0

    def test_example_configs(self):
        """Test all example configuration files"""
        print("📋 Test Suite: Example Configurations")
        print("-" * 80)

        example_files = list(self.examples_dir.glob("*.yaml"))
        example_files = [f for f in example_files if f.name != "README.md"]

        for example_file in example_files:
            self.test_single_example(example_file)

        print()

    def test_single_example(self, example_file: Path):
        """Test a single example configuration"""
        test_name = f"Generate config from {example_file.name}"

        try:
            # Run the agent with preview mode
            result = subprocess.run(
                [
                    sys.executable,
                    str(self.agent_script),
                    str(example_file),
                    "--output_mode=preview"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                self.fail_test(test_name, f"Agent returned non-zero exit code: {result.returncode}\n{result.stderr}")
                return

            # Check that output contains expected schema fields
            output = result.stdout

            if '"Providers"' not in output:
                self.fail_test(test_name, "Output missing 'Providers' field")
                return

            if '"Router"' not in output:
                self.fail_test(test_name, "Output missing 'Router' field")
                return

            # Try to parse the JSON from output
            # Extract JSON between the preview markers
            lines = output.split('\n')
            json_lines = []
            in_json = False
            for line in lines:
                if '─' * 80 in line:
                    in_json = not in_json
                    continue
                if in_json:
                    json_lines.append(line)

            if json_lines:
                try:
                    config = json.loads('\n'.join(json_lines))
                    self.validate_config_structure(config, test_name)
                except json.JSONDecodeError as e:
                    self.fail_test(test_name, f"Invalid JSON output: {e}")
                    return

            self.pass_test(test_name)

        except subprocess.TimeoutExpired:
            self.fail_test(test_name, "Test timed out after 30 seconds")
        except Exception as e:
            self.fail_test(test_name, f"Unexpected error: {e}")

    def validate_config_structure(self, config: dict, test_name: str):
        """Validate the structure of a generated config"""
        # Check Providers array
        if "Providers" not in config:
            self.fail_test(test_name, "Missing 'Providers' key")
            return

        if not isinstance(config["Providers"], list):
            self.fail_test(test_name, "'Providers' must be a list")
            return

        for idx, provider in enumerate(config["Providers"]):
            if "name" not in provider:
                self.fail_test(test_name, f"Provider {idx} missing 'name' field")
                return
            if "api_base_url" not in provider:
                self.fail_test(test_name, f"Provider {idx} missing 'api_base_url' field")
                return
            if "models" not in provider:
                self.fail_test(test_name, f"Provider {idx} missing 'models' field")
                return

        # Check Router object
        if "Router" not in config:
            self.fail_test(test_name, "Missing 'Router' key")
            return

        if not isinstance(config["Router"], dict):
            self.fail_test(test_name, "'Router' must be an object")
            return

        # Check Router values are "provider,model" strings
        for context, value in config["Router"].items():
            if not isinstance(value, str):
                self.fail_test(test_name, f"Router[{context}] must be a string, got {type(value)}")
                return
            if "," not in value:
                self.fail_test(test_name, f"Router[{context}] must be 'provider,model' format, got '{value}'")
                return

    def test_schema_compliance(self):
        """Test that generated configs match Claude Code Router schema"""
        print("📐 Test Suite: Schema Compliance")
        print("-" * 80)

        # Test with a simple config
        test_config = {
            "llm_backends": [
                {
                    "name": "test-provider",
                    "api_base_url": "https://api.example.com/v1/chat/completions",
                    "api_key": "$TEST_API_KEY",
                    "models": ["test-model-1", "test-model-2"]
                }
            ],
            "routing_rules": {
                "default": {
                    "provider": "test-provider",
                    "model": "test-model-1"
                }
            }
        }

        # Save to temp file
        temp_file = self.betty_root / "test_temp_config.yaml"
        with open(temp_file, 'w') as f:
            yaml.dump(test_config, f)

        try:
            # Generate config
            result = subprocess.run(
                [
                    sys.executable,
                    str(self.agent_script),
                    str(temp_file),
                    "--output_mode=preview"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                self.pass_test("Schema compliance with minimal config")
            else:
                self.fail_test("Schema compliance with minimal config", result.stderr)

        finally:
            if temp_file.exists():
                temp_file.unlink()

        print()

    def test_validation_logic(self):
        """Test validation catches errors"""
        print("🔍 Test Suite: Validation Logic")
        print("-" * 80)

        # Test 1: Missing default routing context
        self.test_validation_error(
            "Missing default routing context",
            {
                "llm_backends": [
                    {
                        "name": "test",
                        "api_base_url": "https://api.example.com",
                        "models": ["model-1"]
                    }
                ],
                "routing_rules": {
                    "background": {"provider": "test", "model": "model-1"}
                }
            }
        )

        # Test 2: Unknown provider in routing
        self.test_validation_error(
            "Unknown provider in routing",
            {
                "llm_backends": [
                    {
                        "name": "test",
                        "api_base_url": "https://api.example.com",
                        "models": ["model-1"]
                    }
                ],
                "routing_rules": {
                    "default": {"provider": "unknown", "model": "model-1"}
                }
            }
        )

        # Test 3: Unknown model for provider
        self.test_validation_error(
            "Unknown model for provider",
            {
                "llm_backends": [
                    {
                        "name": "test",
                        "api_base_url": "https://api.example.com",
                        "models": ["model-1"]
                    }
                ],
                "routing_rules": {
                    "default": {"provider": "test", "model": "unknown-model"}
                }
            }
        )

        print()

    def test_validation_error(self, test_name: str, config: dict):
        """Test that validation catches a specific error"""
        temp_file = self.betty_root / "test_temp_config.yaml"
        with open(temp_file, 'w') as f:
            yaml.dump(config, f)

        try:
            result = subprocess.run(
                [
                    sys.executable,
                    str(self.agent_script),
                    str(temp_file),
                    "--output_mode=preview"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            # Should fail validation
            if result.returncode != 0 or "Validation failed" in result.stdout:
                self.pass_test(test_name)
            else:
                self.fail_test(test_name, "Expected validation to fail, but it passed")

        finally:
            if temp_file.exists():
                temp_file.unlink()

    def pass_test(self, test_name: str):
        """Mark test as passed"""
        self.passed += 1
        print(f"✅ {test_name}")

    def fail_test(self, test_name: str, reason: str):
        """Mark test as failed"""
        self.failed += 1
        self.errors.append((test_name, reason))
        print(f"❌ {test_name}")
        print(f"   Reason: {reason}")

    def print_summary(self):
        """Print test summary"""
        print("=" * 80)
        print("📊 Test Summary")
        print("=" * 80)
        print(f"✅ Passed: {self.passed}")
        print(f"❌ Failed: {self.failed}")
        print(f"📈 Total:  {self.passed + self.failed}")
        print()

        if self.failed > 0:
            print("❌ Failed Tests:")
            for test_name, reason in self.errors:
                print(f"  - {test_name}")
                print(f"    {reason}")
            print()

        if self.failed == 0:
            print("🎉 All tests passed!")
        else:
            print(f"⚠️  {self.failed} test(s) failed")

        print("=" * 80)


def main():
    """Run all tests"""
    tester = RouterConfigTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
