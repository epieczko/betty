"""Regression tests ensuring enums share a single source of truth."""

from betty import config, models
from betty import enums


def test_config_uses_shared_enums():
    """All enums exposed via betty.config should come from betty.enums."""

    assert config.SkillStatus is enums.SkillStatus
    assert config.AgentStatus is enums.AgentStatus
    assert config.ReasoningMode is enums.ReasoningMode
    assert config.CommandExecutionType is enums.CommandExecutionType
    assert config.CommandStatus is enums.CommandStatus
    assert config.HookEvent is enums.HookEvent
    assert config.HookStatus is enums.HookStatus


def test_models_use_shared_enums():
    """All enums exposed via betty.models should come from betty.enums."""

    assert models.ReasoningMode is enums.ReasoningMode
    assert models.CommandExecutionType is enums.CommandExecutionType
    assert models.HookEvent is enums.HookEvent
    assert models.StatusType is enums.StatusType
