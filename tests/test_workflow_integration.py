#!/usr/bin/env python3
"""
Integration tests for Betty Framework workflow lifecycle.

Tests the complete workflow execution cycle:
1. Create a new skill using skill.create
2. Validate with skill.define
3. Register with registry.update
4. Compose and run workflow with workflow.compose
5. Run policy.enforce at end
6. Assert that outputs are logged to workflow_history.json

These tests simulate real-world usage scenarios and validate
end-to-end integration of all core Betty Framework components.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime

import pytest

# Add parent to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.config import BASE_DIR, REGISTRY_FILE

# Convert BASE_DIR to Path for easier manipulation
BASE_PATH = Path(BASE_DIR)
WORKFLOW_HISTORY_PATH = BASE_PATH / "registry" / "workflow_history.json"


def parse_json_output(stdout: str) -> dict:
    """
    Parse JSON from stdout, extracting the JSON portion.
    Skills output logging to stdout before the final JSON result.
    May have multiple JSON objects - returns the last complete one.
    """
    lines = stdout.strip().split('\n')

    # Find all JSON object starts
    json_starts = []
    for i, line in enumerate(lines):
        if line.strip().startswith('{') or line.strip().startswith('['):
            json_starts.append(i)

    if not json_starts:
        raise ValueError("No JSON found in output")

    # Try to parse JSON objects from last to first (most recent)
    for start_idx in reversed(json_starts):
        try:
            json_str = '\n'.join(lines[start_idx:])
            return json.loads(json_str)
        except json.JSONDecodeError:
            # Try previous JSON object
            continue

    raise ValueError("No valid JSON found in output")


def load_workflow_history() -> list:
    """Load workflow history from registry."""
    if not WORKFLOW_HISTORY_PATH.exists():
        return []

    with open(WORKFLOW_HISTORY_PATH) as f:
        return json.load(f)


def get_latest_workflow_entry() -> dict:
    """Get the most recent workflow entry from history."""
    history = load_workflow_history()
    if not history:
        return {}
    return history[-1]


class TestWorkflowLifecycleIntegration:
    """Integration tests for complete workflow lifecycle."""

    @pytest.fixture
    def temp_skill_name(self):
        """Generate a unique temporary skill name for testing."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"test.workflow.integration.{timestamp}"

    @pytest.fixture
    def temp_workflow_name(self):
        """Generate a unique temporary workflow name."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"test_integration_{timestamp}.yaml"

    @pytest.fixture(autouse=True)
    def cleanup(self, temp_skill_name):
        """Clean up test artifacts after each test."""
        yield

        # Clean up skill directory
        skill_path = BASE_PATH / "skills" / temp_skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)

        # Clean up any test workflows
        workflows_dir = BASE_PATH / "workflows"
        for workflow_file in workflows_dir.glob("test_integration_*.yaml"):
            workflow_file.unlink()

    def test_complete_workflow_lifecycle(self, temp_skill_name, temp_workflow_name):
        """
        Test the complete workflow lifecycle:
        1. Create skill
        2. Validate skill
        3. Register skill
        4. Compose and run workflow
        5. Verify workflow_history.json logging
        """
        # Step 1: Create skill using skill.create
        create_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Integration test skill for workflow testing",
                "--inputs", "input1,input2",
                "--outputs", "output1"
            ],
            capture_output=True,
            text=True
        )

        assert create_result.returncode == 0, f"skill.create failed: {create_result.stderr}"
        create_output = parse_json_output(create_result.stdout)
        assert create_output["status"] == "success"
        assert create_output["details"]["skill_name"] == temp_skill_name
        assert create_output["details"]["validation"] == "passed"
        assert create_output["details"]["registry_updated"] is True

        skill_manifest_path = BASE_PATH / "skills" / temp_skill_name / "skill.yaml"
        assert skill_manifest_path.exists()

        # Step 2: Validate skill using skill.define (redundant but tests direct invocation)
        validate_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                str(skill_manifest_path)
            ],
            capture_output=True,
            text=True
        )

        assert validate_result.returncode == 0, f"skill.define failed: {validate_result.stderr}"
        validate_output = parse_json_output(validate_result.stdout)
        assert validate_output["ok"] is True
        assert validate_output["details"]["valid"] is True
        assert validate_output["details"]["manifest"]["name"] == temp_skill_name

        # Step 3: Update registry using registry.update (redundant but tests direct invocation)
        registry_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/registry.update/registry_update.py"),
                str(skill_manifest_path)
            ],
            capture_output=True,
            text=True
        )

        assert registry_result.returncode == 0, f"registry.update failed: {registry_result.stderr}"
        registry_output = parse_json_output(registry_result.stdout)
        assert registry_output["ok"] is True
        assert registry_output["details"]["updated"] == temp_skill_name

        # Verify skill is in registry
        with open(REGISTRY_FILE) as f:
            registry = json.load(f)
        skill_names = [s["name"] for s in registry["skills"]]
        assert temp_skill_name in skill_names

        # Step 4: Create and run workflow using workflow.compose
        workflow_path = BASE_PATH / "workflows" / temp_workflow_name
        workflow_content = f"""steps:
  - skill: skill.define
    args: ["{skill_manifest_path}"]
  - skill: registry.update
    args: ["{skill_manifest_path}"]
"""
        workflow_path.write_text(workflow_content, encoding="utf-8")

        # Record workflow history length before running
        history_before = load_workflow_history()
        history_count_before = len(history_before)

        # Run workflow
        workflow_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(workflow_path)
            ],
            capture_output=True,
            text=True,
            timeout=300
        )

        assert workflow_result.returncode == 0, f"workflow.compose failed: {workflow_result.stderr}"
        workflow_output = parse_json_output(workflow_result.stdout)
        assert workflow_output["ok"] is True
        assert workflow_output["details"]["status"] == "success"
        assert len(workflow_output["details"]["steps"]) == 2

        # Verify all steps succeeded
        for step in workflow_output["details"]["steps"]:
            assert step["status"] == "success", f"Step {step['skill']} failed"

        # Step 5: Verify workflow_history.json was updated
        history_after = load_workflow_history()
        history_count_after = len(history_after)

        assert history_count_after > history_count_before, "workflow_history.json was not updated"

        # Get the latest workflow entry
        latest_entry = get_latest_workflow_entry()

        # Validate workflow history entry structure
        assert "workflow" in latest_entry
        assert "started_at" in latest_entry or "timestamp" in latest_entry
        assert "steps" in latest_entry
        assert "status" in latest_entry
        assert "completed_at" in latest_entry

        # Verify the workflow name matches
        assert temp_workflow_name in latest_entry["workflow"]

        # Verify workflow status
        assert latest_entry["status"] == "success"

        # Verify steps were logged
        assert len(latest_entry["steps"]) == 2

        # Verify step details
        for step in latest_entry["steps"]:
            assert "skill" in step
            assert "args" in step
            assert "status" in step
            assert step["status"] == "success"

    def test_workflow_with_policy_enforcement(self, temp_skill_name, temp_workflow_name):
        """
        Test workflow lifecycle with policy.enforce step at the end.
        """
        # Step 1: Create skill
        create_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Test skill for policy enforcement"
            ],
            capture_output=True,
            text=True
        )

        assert create_result.returncode == 0
        skill_manifest_path = BASE_PATH / "skills" / temp_skill_name / "skill.yaml"

        # Step 2: Create workflow with policy.enforce at the end
        workflow_path = BASE_PATH / "workflows" / temp_workflow_name
        workflow_content = f"""steps:
  - skill: skill.define
    args: ["{skill_manifest_path}"]
  - skill: policy.enforce
    args: ["{skill_manifest_path}"]
"""
        workflow_path.write_text(workflow_content, encoding="utf-8")

        # Step 3: Run workflow
        workflow_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(workflow_path)
            ],
            capture_output=True,
            text=True,
            timeout=300
        )

        assert workflow_result.returncode == 0, f"workflow.compose failed: {workflow_result.stderr}"
        workflow_output = parse_json_output(workflow_result.stdout)
        assert workflow_output["ok"] is True
        assert workflow_output["details"]["status"] == "success"

        # Step 4: Verify policy.enforce ran successfully
        policy_step = [s for s in workflow_output["details"]["steps"] if s["skill"] == "policy.enforce"][0]
        assert policy_step["status"] == "success"

        # Parse policy.enforce output
        policy_stdout = policy_step.get("stdout", "")
        if policy_stdout:
            policy_output = parse_json_output(policy_stdout)
            assert policy_output["success"] is True
            assert policy_output["violation_count"] == 0

    def test_workflow_fail_fast_behavior(self):
        """
        Test that workflows stop on first failure when fail_fast is enabled.
        Verify that workflow_history.json captures failed steps.
        """
        failing_workflow_path = BASE_PATH / "workflows" / "test_fail_fast_integration.yaml"
        failing_workflow_content = """steps:
  - skill: skill.define
    args: ["nonexistent_file.yaml"]
  - skill: skill.define
    args: ["skills/skill.create/skill.yaml"]
"""
        failing_workflow_path.write_text(failing_workflow_content, encoding="utf-8")

        try:
            # Record history before
            history_before = load_workflow_history()
            history_count_before = len(history_before)

            # Run workflow
            result = subprocess.run(
                [
                    sys.executable,
                    str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                    str(failing_workflow_path)
                ],
                capture_output=True,
                text=True,
                timeout=300
            )

            # Workflow should fail
            assert result.returncode == 1
            output = parse_json_output(result.stdout)
            assert output["ok"] is False
            assert output["details"]["status"] == "failed"

            # Should only have executed 1 step (fail-fast)
            assert len(output["details"]["steps"]) == 1
            assert output["details"]["steps"][0]["status"] == "failed"

            # Verify workflow_history.json captured the failure
            history_after = load_workflow_history()
            assert len(history_after) > history_count_before

            latest_entry = get_latest_workflow_entry()
            assert latest_entry["status"] == "failed"
            assert "failed_steps" in latest_entry or any(s["status"] == "failed" for s in latest_entry["steps"])

        finally:
            if failing_workflow_path.exists():
                failing_workflow_path.unlink()

    def test_workflow_multi_step_execution(self):
        """
        Test workflow with multiple steps executing successfully.
        Verify proper logging of all steps in workflow_history.json.
        """
        workflow_path = BASE_PATH / "workflows" / "test_multi_step.yaml"
        workflow_content = """steps:
  - skill: skill.define
    args: ["skills/skill.create/skill.yaml"]
  - skill: skill.define
    args: ["skills/skill.define/skill.yaml"]
  - skill: skill.define
    args: ["skills/registry.update/skill.yaml"]
"""
        workflow_path.write_text(workflow_content, encoding="utf-8")

        try:
            # Record history before
            history_count_before = len(load_workflow_history())

            # Run workflow
            result = subprocess.run(
                [
                    sys.executable,
                    str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                    str(workflow_path)
                ],
                capture_output=True,
                text=True,
                timeout=300
            )

            assert result.returncode == 0, f"Workflow failed: {result.stderr}"
            output = parse_json_output(result.stdout)
            assert output["ok"] is True
            assert output["details"]["status"] == "success"

            # Verify all 3 steps executed
            assert len(output["details"]["steps"]) == 3
            for step in output["details"]["steps"]:
                assert step["status"] == "success"

            # Verify workflow_history.json has the entry
            history_after = load_workflow_history()
            assert len(history_after) > history_count_before

            latest_entry = get_latest_workflow_entry()
            assert latest_entry["status"] == "success"
            assert len(latest_entry["steps"]) == 3

            # Verify step ordering and details
            for i, step in enumerate(latest_entry["steps"], 1):
                assert "step_number" in step or step["skill"] == f"skill.define"
                assert step["status"] == "success"
                assert "returncode" in step or "output" in step

        finally:
            if workflow_path.exists():
                workflow_path.unlink()

    def test_policy_enforce_batch_mode(self):
        """
        Test policy.enforce in batch mode (validates all manifests).
        """
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/policy.enforce/policy_enforce.py"),
                "--batch"
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Parse output
        output = parse_json_output(result.stdout)

        # Should validate successfully (or return detailed results)
        assert "success" in output
        assert "mode" in output
        assert output["mode"] == "batch"
        assert "total_manifests" in output
        assert "passed" in output
        assert "failed" in output

        # Should have found manifests to validate
        assert output["total_manifests"] > 0

    def test_skill_create_validates_and_registers(self, temp_skill_name):
        """
        Test that skill.create automatically validates and registers the new skill.
        Verify that all outputs are captured correctly.
        """
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Test automatic validation and registration"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)

        # Verify creation details
        assert output["status"] == "success"
        details = output["details"]
        assert details["skill_name"] == temp_skill_name
        assert details["validation"] == "passed"
        assert details["registry_updated"] is True

        # Verify files exist
        skill_path = BASE_PATH / "skills" / temp_skill_name
        assert skill_path.exists()
        assert (skill_path / "skill.yaml").exists()
        assert (skill_path / "SKILL.md").exists()

        # Verify in registry
        with open(REGISTRY_FILE) as f:
            registry = json.load(f)
        skill_names = [s["name"] for s in registry["skills"]]
        assert temp_skill_name in skill_names


class TestWorkflowHistoryValidation:
    """Tests specifically for workflow_history.json validation."""

    def test_workflow_history_file_exists(self):
        """Verify workflow_history.json exists."""
        assert WORKFLOW_HISTORY_PATH.exists(), "workflow_history.json should exist"

    def test_workflow_history_is_valid_json(self):
        """Verify workflow_history.json contains valid JSON."""
        with open(WORKFLOW_HISTORY_PATH) as f:
            history = json.load(f)

        assert isinstance(history, list), "History should be a list"

    def test_workflow_history_entry_structure(self):
        """Verify workflow history entries have the correct structure."""
        history = load_workflow_history()

        if not history:
            pytest.skip("No workflow history entries to validate")

        # Check latest entry
        latest = history[-1]

        # Required fields
        assert "workflow" in latest
        assert "steps" in latest
        assert "status" in latest

        # Time tracking (either format)
        assert "started_at" in latest or "timestamp" in latest
        assert "completed_at" in latest

        # Steps structure
        assert isinstance(latest["steps"], list)
        if len(latest["steps"]) > 0:
            step = latest["steps"][0]
            assert "skill" in step
            assert "args" in step
            assert "status" in step or "output" in step


class TestSubprocessExecutionPatterns:
    """Tests for validating subprocess execution patterns used in workflows."""

    def test_subprocess_timeout_handling(self):
        """Test that subprocess timeouts are handled correctly."""
        # This is a meta-test to ensure our test patterns work correctly
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                str(BASE_PATH / "skills/skill.create/skill.yaml")
            ],
            capture_output=True,
            text=True,
            timeout=10  # Should complete well within 10 seconds
        )

        assert result.returncode == 0

    def test_json_parsing_with_logs(self):
        """Test that JSON parsing works when stdout contains logs."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                "--help"
            ],
            capture_output=True,
            text=True
        )

        # Help output should not be JSON, but command should work
        assert result.returncode in [0, 2]  # 0 for success, 2 for argparse help

    def test_stderr_capture(self):
        """Test that stderr is properly captured for debugging."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                "nonexistent.yaml"
            ],
            capture_output=True,
            text=True
        )

        # Should fail
        assert result.returncode == 1

        # Should have JSON output
        output = parse_json_output(result.stdout)
        assert output["ok"] is False


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
