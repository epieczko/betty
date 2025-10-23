#!/usr/bin/env python3
"""
Integration tests for Betty Framework workflow lifecycle.

Tests the complete skill lifecycle using CLI commands:
1. skill.create - Create a new skill
2. skill.define - Validate the skill manifest
3. registry.update - Register the skill
4. workflow.compose - Execute multi-step workflow
5. policy.enforce - Validate compliance

Validates workflow_history.json is updated with execution details.
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

from betty.config import BASE_DIR, REGISTRY_FILE, WORKFLOW_HISTORY_FILE

# Convert BASE_DIR to Path for easier manipulation
BASE_PATH = Path(BASE_DIR)


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
    """Load workflow history from JSON file."""
    history_path = Path(WORKFLOW_HISTORY_FILE)
    if not history_path.exists():
        return []

    with open(history_path, 'r') as f:
        return json.load(f)


def find_workflow_execution(workflow_name: str, history: list = None) -> dict:
    """Find the most recent workflow execution by workflow name."""
    if history is None:
        history = load_workflow_history()

    # Find entries matching the workflow name
    matches = [entry for entry in history if workflow_name in entry.get("workflow", "")]

    if not matches:
        return None

    # Return the most recent (last entry)
    return matches[-1]


class TestFullWorkflowLifecycle:
    """Integration tests for complete workflow lifecycle."""

    @pytest.fixture
    def temp_skill_name(self):
        """Generate a temporary skill name for testing."""
        return "test.workflow.integration"

    @pytest.fixture
    def temp_workflow_path(self):
        """Generate a temporary workflow file path."""
        return BASE_PATH / "workflows" / "temp_integration_test.yaml"

    @pytest.fixture(autouse=True)
    def cleanup(self, temp_skill_name, temp_workflow_path):
        """Clean up test artifacts after each test."""
        yield

        # Cleanup skill directory
        skill_path = BASE_PATH / "skills" / temp_skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)

        # Cleanup workflow file
        if temp_workflow_path.exists():
            temp_workflow_path.unlink()

    def test_complete_workflow_lifecycle(self, temp_skill_name, temp_workflow_path):
        """
        Test complete skill lifecycle with workflow execution.

        Steps:
        1. skill.create - Create new skill
        2. skill.define - Validate skill manifest
        3. registry.update - Register skill
        4. workflow.compose - Execute workflow with the skill
        5. Verify workflow_history.json updated
        6. policy.enforce - Validate compliance
        """

        # ===== STEP 1: Create skill using skill.create =====
        print("\n=== Step 1: Creating skill ===")
        create_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Integration test skill for workflow lifecycle",
                "--inputs", "test_input",
                "--outputs", "test_output"
            ],
            capture_output=True,
            text=True
        )

        assert create_result.returncode == 0, f"skill.create failed: {create_result.stderr}"
        create_output = parse_json_output(create_result.stdout)
        print(f"Create output: {json.dumps(create_output, indent=2)}")

        assert create_output["ok"] is True
        assert create_output["status"] == "success"
        assert temp_skill_name in create_output["path"]

        # Verify files created
        skill_path = BASE_PATH / "skills" / temp_skill_name
        skill_manifest = skill_path / "skill.yaml"
        assert skill_path.exists(), f"Skill directory not created: {skill_path}"
        assert skill_manifest.exists(), f"Skill manifest not created: {skill_manifest}"
        assert (skill_path / "SKILL.md").exists()

        # ===== STEP 2: Validate with skill.define =====
        print("\n=== Step 2: Validating skill ===")
        define_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                str(skill_manifest)
            ],
            capture_output=True,
            text=True
        )

        assert define_result.returncode == 0, f"skill.define failed: {define_result.stderr}"
        define_output = parse_json_output(define_result.stdout)
        print(f"Define output: {json.dumps(define_output, indent=2)}")

        assert define_output["ok"] is True
        assert define_output["details"]["valid"] is True
        assert define_output["details"]["manifest"]["name"] == temp_skill_name
        assert len(define_output["details"]["missing"]) == 0

        # ===== STEP 3: Register with registry.update =====
        print("\n=== Step 3: Registering skill ===")
        registry_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/registry.update/registry_update.py"),
                str(skill_manifest)
            ],
            capture_output=True,
            text=True
        )

        assert registry_result.returncode == 0, f"registry.update failed: {registry_result.stderr}"
        registry_output = parse_json_output(registry_result.stdout)
        print(f"Registry output: {json.dumps(registry_output, indent=2)}")

        assert registry_output["ok"] is True
        assert registry_output["details"]["status"] == "success"
        assert registry_output["details"]["updated"] == temp_skill_name

        # Verify skill is in registry
        with open(REGISTRY_FILE, 'r') as f:
            registry = json.load(f)
        skill_names = [s["name"] for s in registry["skills"]]
        assert temp_skill_name in skill_names, f"Skill not found in registry: {skill_names}"

        # ===== STEP 4: Create and execute workflow with workflow.compose =====
        print("\n=== Step 4: Creating and executing workflow ===")

        # Create workflow that uses existing skills
        workflow_content = f"""steps:
  - skill: skill.define
    args: ["{skill_manifest}"]
    description: "Validate the newly created skill"
  - skill: registry.update
    args: ["{skill_manifest}"]
    description: "Re-register to test workflow execution"
"""
        temp_workflow_path.write_text(workflow_content, encoding="utf-8")

        # Record number of workflow history entries before execution
        history_before = load_workflow_history()
        history_count_before = len(history_before)

        # Execute workflow
        workflow_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(temp_workflow_path)
            ],
            capture_output=True,
            text=True
        )

        assert workflow_result.returncode == 0, f"workflow.compose failed: {workflow_result.stderr}"
        workflow_output = parse_json_output(workflow_result.stdout)
        print(f"Workflow output: {json.dumps(workflow_output, indent=2)}")

        assert workflow_output["ok"] is True
        assert workflow_output["details"]["status"] == "success"
        assert len(workflow_output["details"]["steps"]) == 2

        # Verify all steps succeeded
        for step in workflow_output["details"]["steps"]:
            assert step["status"] == "success", f"Step {step['step_number']} failed: {step.get('stderr', '')}"
            assert step["returncode"] == 0

        # ===== STEP 5: Verify workflow_history.json updated =====
        print("\n=== Step 5: Verifying workflow history ===")

        # Load workflow history
        history_after = load_workflow_history()
        history_count_after = len(history_after)

        assert history_count_after > history_count_before, "Workflow history not updated"

        # Find the most recent workflow execution
        workflow_name = temp_workflow_path.name
        latest_execution = find_workflow_execution(workflow_name, history_after)

        assert latest_execution is not None, f"Workflow execution not found in history: {workflow_name}"
        print(f"Latest workflow execution: {json.dumps(latest_execution, indent=2)}")

        # Verify workflow execution structure
        assert "workflow" in latest_execution
        assert "started_at" in latest_execution
        assert "completed_at" in latest_execution
        assert "steps" in latest_execution
        assert "status" in latest_execution

        # Verify timestamps are valid ISO format
        started_at = datetime.fromisoformat(latest_execution["started_at"].replace('Z', '+00:00'))
        completed_at = datetime.fromisoformat(latest_execution["completed_at"].replace('Z', '+00:00'))
        assert completed_at >= started_at, "Completed timestamp before started timestamp"

        # Verify steps in history match execution
        assert len(latest_execution["steps"]) == 2
        assert latest_execution["steps"][0]["skill"] == "skill.define"
        assert latest_execution["steps"][1]["skill"] == "registry.update"
        assert latest_execution["status"] == "success"

        # Verify step details
        for step in latest_execution["steps"]:
            assert "step_number" in step
            assert "skill" in step
            assert "status" in step
            assert "returncode" in step
            assert "duration_ms" in step
            assert step["status"] == "success"
            assert step["returncode"] == 0

        # ===== STEP 6: Run policy.enforce =====
        print("\n=== Step 6: Running policy enforcement ===")
        policy_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/policy.enforce/policy_enforce.py"),
                str(skill_manifest)
            ],
            capture_output=True,
            text=True
        )

        assert policy_result.returncode == 0, f"policy.enforce failed: {policy_result.stderr}"
        policy_output = parse_json_output(policy_result.stdout)
        print(f"Policy output: {json.dumps(policy_output, indent=2)}")

        # policy.enforce returns "success" not "ok"
        assert policy_output["success"] is True
        assert policy_output["violation_count"] == 0 or policy_output.get("violations")

        # Verify no critical policy violations (allow warnings)
        if "violations" in policy_output:
            violations = policy_output["violations"]
            # Allow warnings but not errors
            error_violations = [v for v in violations if v.get("severity") == "error"]
            assert len(error_violations) == 0, f"Policy errors found: {error_violations}"

        print("\n=== All steps completed successfully ===")

    def test_workflow_with_multiple_skills(self, temp_workflow_path):
        """Test workflow execution with multiple existing skills."""

        # Create workflow with multiple steps using existing skills
        workflow_content = """steps:
  - skill: skill.define
    args: ["skills/skill.create/skill.yaml"]
    description: "Validate skill.create manifest"
  - skill: skill.define
    args: ["skills/registry.update/skill.yaml"]
    description: "Validate registry.update manifest"
  - skill: policy.enforce
    args: ["skills/skill.create/skill.yaml"]
    description: "Enforce policy on skill.create"
"""
        temp_workflow_path.write_text(workflow_content, encoding="utf-8")

        # Execute workflow
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(temp_workflow_path)
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0, f"Workflow failed: {result.stderr}"
        output = parse_json_output(result.stdout)

        assert output["ok"] is True
        assert output["details"]["status"] == "success"
        assert len(output["details"]["steps"]) == 3

        # Verify all steps completed successfully
        for i, step in enumerate(output["details"]["steps"], 1):
            assert step["status"] == "success", f"Step {i} failed"
            assert step["returncode"] == 0

        # Verify workflow history
        latest_execution = find_workflow_execution(temp_workflow_path.name)
        assert latest_execution is not None
        assert len(latest_execution["steps"]) == 3
        assert latest_execution["status"] == "success"

    def test_workflow_failure_handling(self, temp_workflow_path):
        """Test workflow execution when a step fails."""

        # Create workflow with a failing step
        workflow_content = """steps:
  - skill: skill.define
    args: ["nonexistent_manifest.yaml"]
    description: "This should fail"
  - skill: skill.define
    args: ["skills/skill.create/skill.yaml"]
    description: "This should not run due to fail_fast"
"""
        temp_workflow_path.write_text(workflow_content, encoding="utf-8")

        # Execute workflow
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(temp_workflow_path)
            ],
            capture_output=True,
            text=True
        )

        # Workflow should return non-zero exit code on failure
        assert result.returncode == 1, "Expected workflow to fail"
        output = parse_json_output(result.stdout)

        assert output["ok"] is False
        assert output["details"]["status"] == "failed"

        # Verify only first step executed (fail_fast behavior)
        assert len(output["details"]["steps"]) == 1
        assert output["details"]["steps"][0]["status"] == "failed"
        assert output["details"]["steps"][0]["returncode"] == 1

        # Verify workflow history contains the failure
        latest_execution = find_workflow_execution(temp_workflow_path.name)
        assert latest_execution is not None
        assert latest_execution["status"] == "failed"
        assert len(latest_execution["failed_steps"]) > 0


class TestPolicyEnforcement:
    """Integration tests for policy enforcement."""

    def test_policy_enforce_valid_manifest(self):
        """Test policy enforcement on a valid manifest."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/policy.enforce/policy_enforce.py"),
                str(BASE_PATH / "skills/skill.create/skill.yaml")
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        # policy.enforce returns "success" not "ok"
        assert output["success"] is True
        assert output["violation_count"] >= 0

    def test_policy_enforce_batch_mode(self):
        """Test policy enforcement in batch mode on all skills."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/policy.enforce/policy_enforce.py"),
                "--batch"
            ],
            capture_output=True,
            text=True
        )

        # Batch mode may have warnings but should succeed
        assert result.returncode in [0, 1]  # 0 = pass, 1 = violations found
        output = parse_json_output(result.stdout)
        # policy.enforce returns "success" not "ok"
        assert "success" in output  # Depends on violations

        # Should have scanned multiple skills
        if "violations" in output and output["violations"]:
            # Verify violation structure if any found
            for violation in output["violations"]:
                assert "field" in violation
                assert "rule" in violation
                assert "severity" in violation
                assert violation["severity"] in ["warning", "error"]


class TestWorkflowHistoryValidation:
    """Tests specifically for workflow_history.json structure and content."""

    def test_workflow_history_file_exists(self):
        """Verify workflow history file exists and is valid JSON."""
        history_path = Path(WORKFLOW_HISTORY_FILE)
        assert history_path.exists(), f"Workflow history file not found: {WORKFLOW_HISTORY_FILE}"

        # Verify it's valid JSON
        with open(history_path, 'r') as f:
            history = json.load(f)

        assert isinstance(history, list), "Workflow history should be a list"

    def test_workflow_history_structure(self):
        """Verify workflow history entries have correct structure."""
        history = load_workflow_history()

        if len(history) == 0:
            pytest.skip("No workflow history entries to validate")

        # Check structure of most recent entry
        latest = history[-1]

        # Required fields
        required_fields = [
            "workflow", "workflow_path", "started_at", "completed_at",
            "steps", "status", "fail_fast"
        ]

        for field in required_fields:
            assert field in latest, f"Missing required field: {field}"

        # Verify steps structure
        assert isinstance(latest["steps"], list)
        if len(latest["steps"]) > 0:
            step = latest["steps"][0]
            step_required_fields = [
                "step_number", "skill", "args", "status",
                "returncode", "duration_ms"
            ]
            for field in step_required_fields:
                assert field in step, f"Step missing required field: {field}"

        # Verify timestamps
        assert latest["started_at"]
        assert latest["completed_at"]

        # Verify status values
        assert latest["status"] in ["success", "failed"]


class TestErrorScenarios:
    """Tests for error handling and edge cases."""

    def test_skill_create_invalid_name(self):
        """Test skill creation with invalid name."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                "Invalid Skill Name With Spaces",
                "Test description"
            ],
            capture_output=True,
            text=True
        )

        # Should fail due to invalid name format
        assert result.returncode == 1
        output = parse_json_output(result.stdout)
        assert output["ok"] is False
        assert "errors" in output

    def test_skill_define_missing_file(self):
        """Test skill.define with non-existent file."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                "nonexistent_manifest.yaml"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 1
        output = parse_json_output(result.stdout)
        assert output["ok"] is False
        assert output["status"] == "failed"

    def test_workflow_compose_invalid_workflow(self):
        """Test workflow.compose with invalid workflow file."""
        temp_workflow = BASE_PATH / "workflows" / "temp_invalid.yaml"

        try:
            # Create invalid workflow (missing steps)
            temp_workflow.write_text("invalid: yaml\nno: steps", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                    str(temp_workflow)
                ],
                capture_output=True,
                text=True
            )

            # Should fail validation
            assert result.returncode == 1
            output = parse_json_output(result.stdout)
            assert output["ok"] is False
        finally:
            if temp_workflow.exists():
                temp_workflow.unlink()

    def test_policy_enforce_strict_mode(self):
        """Test policy enforcement in strict mode."""
        # Create a temporary skill with potential policy warnings
        temp_skill = BASE_PATH / "skills" / "test.policy.strict"
        temp_manifest = temp_skill / "skill.yaml"

        try:
            temp_skill.mkdir(exist_ok=True)

            # Create manifest with potential policy issues
            manifest_content = """name: test.policy.strict
version: 1.0.0
description: Test strict policy enforcement
inputs: []
outputs: []
status: draft
dependencies: []
entrypoints: []
"""
            temp_manifest.write_text(manifest_content, encoding="utf-8")

            # Run policy.enforce in strict mode
            result = subprocess.run(
                [
                    sys.executable,
                    str(BASE_PATH / "skills/policy.enforce/policy_enforce.py"),
                    str(temp_manifest),
                    "--strict"
                ],
                capture_output=True,
                text=True
            )

            # In strict mode, warnings may cause failure
            output = parse_json_output(result.stdout)
            # Just verify we get a valid response with policy check
            # policy.enforce returns "success" not "status"
            assert "success" in output
            assert "violations" in output

        finally:
            if temp_skill.exists():
                shutil.rmtree(temp_skill)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
