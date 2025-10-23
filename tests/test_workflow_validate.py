"""Unit tests for the workflow.validate skill."""

import importlib.util
import sys
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[1]
MODULE_PATH = BASE_PATH / "skills" / "workflow.validate" / "workflow_validate.py"

spec = importlib.util.spec_from_file_location("workflow_validate", MODULE_PATH)
workflow_validate = importlib.util.module_from_spec(spec)
assert spec and spec.loader  # mypy/runtime guard
sys.modules[spec.name] = workflow_validate
spec.loader.exec_module(workflow_validate)

validate_workflow = workflow_validate.validate_workflow


def test_validate_workflow_with_valid_yaml(tmp_path: Path) -> None:
    workflow_file = tmp_path / "valid_workflow.yaml"
    workflow_file.write_text(
        """steps:\n  - skill: skill.define\n    args: [\"skills/skill.create/skill.yaml\"]\n""",
        encoding="utf-8",
    )

    result = validate_workflow(str(workflow_file))

    assert result["valid"] is True
    assert result["errors"] == []
    assert result["path"] == str(workflow_file)
    assert result["status"] == "validated"


def test_validate_workflow_with_invalid_yaml(tmp_path: Path) -> None:
    workflow_file = tmp_path / "invalid_workflow.yaml"
    workflow_file.write_text(
        """steps:\n  - skill: skill.define\n""",
        encoding="utf-8",
    )

    result = validate_workflow(str(workflow_file))

    assert result["valid"] is False
    assert any("missing 'args'" in error for error in result["errors"])
    assert result["status"] == "failed"
