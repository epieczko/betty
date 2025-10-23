#!/usr/bin/env python3
"""
Integration tests for Betty Framework core skills.
Tests the full lifecycle: create → define → register → workflow compose.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path

import pytest

# Add parent to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.config import BASE_DIR, REGISTRY_FILE

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


class TestSkillCreateIntegration:
    """Integration tests for skill.create."""

    @pytest.fixture
    def temp_skill_name(self):
        """Generate a temporary skill name for testing."""
        return "test.integration.temp"

    @pytest.fixture(autouse=True)
    def cleanup_skill(self, temp_skill_name):
        """Clean up test skill after each test."""
        yield
        skill_path = BASE_PATH / "skills" / temp_skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)

    def test_skill_create_basic(self, temp_skill_name):
        """Test basic skill creation."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Integration test skill"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["status"] == "success"
        assert output["skill_name"] == temp_skill_name
        assert output["validation"] == "passed"
        assert output["registry_updated"] is True

        # Verify files were created
        skill_path = BASE_PATH / "skills" / temp_skill_name
        assert (skill_path / "skill.yaml").exists()
        assert (skill_path / "SKILL.md").exists()

    def test_skill_create_with_inputs_outputs(self, temp_skill_name):
        """Test skill creation with inputs and outputs."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Test skill with IO",
                "--inputs", "input1,input2",
                "--outputs", "output1"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["status"] == "success"


class TestSkillDefineIntegration:
    """Integration tests for skill.define."""

    def test_validate_existing_skill(self):
        """Test validation of existing skill manifest."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                str(BASE_PATH / "skills/skill.create/skill.yaml")
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["valid"] is True
        assert output["manifest"]["name"] == "skill.create"

    def test_validate_nonexistent_file(self):
        """Test validation with non-existent file."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                "nonexistent/skill.yaml"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 1
        output = parse_json_output(result.stdout)
        assert "error" in output


class TestRegistryUpdateIntegration:
    """Integration tests for registry.update."""

    def test_update_registry_with_valid_manifest(self):
        """Test registry update with valid manifest."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/registry.update/registry_update.py"),
                str(BASE_PATH / "skills/workflow.compose/skill.yaml")
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["status"] == "success"
        assert output["updated"] == "workflow.compose"


class TestWorkflowComposeIntegration:
    """Integration tests for workflow.compose."""

    @pytest.fixture
    def temp_workflow_file(self):
        """Create a temporary workflow file."""
        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.yaml', delete=False, dir=str(BASE_PATH / "workflows")
        ) as f:
            f.write("""steps:
  - skill: skill.define
    args: ["skills/skill.create/skill.yaml"]
""")
            temp_path = f.name

        yield Path(temp_path)

        # Cleanup
        if Path(temp_path).exists():
            os.unlink(temp_path)

    def test_workflow_compose_single_step(self, temp_workflow_file):
        """Test workflow execution with single step."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.compose/workflow_compose.py"),
                str(temp_workflow_file)
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["status"] == "success"
        assert len(output["steps"]) == 1
        assert output["steps"][0]["skill"] == "skill.define"
        assert output["steps"][0]["status"] == "success"


class TestWorkflowValidateIntegration:
    """Integration tests for workflow.validate."""

    def test_validate_valid_workflow(self):
        """Test validation of a valid workflow."""
        workflow_file = BASE_PATH / "workflows/create_workflow_validate.yaml"

        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.validate/workflow_validate.py"),
                str(workflow_file)
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = parse_json_output(result.stdout)
        assert output["valid"] is True
        assert output["path"] == str(workflow_file)

    def test_validate_nonexistent_workflow(self):
        """Test validation with non-existent workflow."""
        result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/workflow.validate/workflow_validate.py"),
                "nonexistent_workflow.yaml"
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 1
        output = parse_json_output(result.stdout)
        assert "error" in output or "errors" in output or output.get("valid") is False


class TestFullLifecycleIntegration:
    """Integration tests for complete skill lifecycle."""

    @pytest.fixture
    def temp_skill_name(self):
        """Generate temporary skill name."""
        return "test.lifecycle.complete"

    @pytest.fixture(autouse=True)
    def cleanup(self, temp_skill_name):
        """Clean up test artifacts."""
        yield
        skill_path = BASE_PATH / "skills" / temp_skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)

    def test_complete_lifecycle(self, temp_skill_name):
        """Test complete lifecycle: create → validate → register."""
        # Step 1: Create skill
        create_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.create/skill_create.py"),
                temp_skill_name,
                "Lifecycle test skill"
            ],
            capture_output=True,
            text=True
        )
        assert create_result.returncode == 0
        create_output = parse_json_output(create_result.stdout)
        assert create_output["status"] == "success"

        skill_manifest = BASE_PATH / "skills" / temp_skill_name / "skill.yaml"
        assert skill_manifest.exists()

        # Step 2: Validate skill (redundant but tests skill.define directly)
        validate_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/skill.define/skill_define.py"),
                str(skill_manifest)
            ],
            capture_output=True,
            text=True
        )
        assert validate_result.returncode == 0
        validate_output = parse_json_output(validate_result.stdout)
        assert validate_output["valid"] is True

        # Step 3: Update registry (redundant but tests registry.update directly)
        registry_result = subprocess.run(
            [
                sys.executable,
                str(BASE_PATH / "skills/registry.update/registry_update.py"),
                str(skill_manifest)
            ],
            capture_output=True,
            text=True
        )
        assert registry_result.returncode == 0
        registry_output = parse_json_output(registry_result.stdout)
        assert registry_output["status"] == "success"
        assert registry_output["updated"] == temp_skill_name

        # Verify skill is in registry
        with open(REGISTRY_FILE) as f:
            registry = json.load(f)

        skill_names = [s["name"] for s in registry["skills"]]
        assert temp_skill_name in skill_names


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
