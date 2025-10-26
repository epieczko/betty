"""Shared enumerations for the Betty framework."""

from __future__ import annotations

from enum import Enum

__all__ = [
    "SkillStatus",
    "AgentStatus",
    "ReasoningMode",
    "CommandExecutionType",
    "HookEvent",
    "CommandStatus",
    "HookStatus",
    "StatusType",
]


class SkillStatus(str, Enum):
    """Valid skill status values."""

    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class AgentStatus(str, Enum):
    """Valid agent status values."""

    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class ReasoningMode(str, Enum):
    """Valid agent reasoning modes."""

    ITERATIVE = "iterative"
    ONESHOT = "oneshot"


class CommandExecutionType(str, Enum):
    """Valid command execution types."""

    AGENT = "agent"
    SKILL = "skill"
    WORKFLOW = "workflow"


class HookEvent(str, Enum):
    """Valid hook event types."""

    ON_FILE_EDIT = "on_file_edit"
    ON_FILE_SAVE = "on_file_save"
    ON_COMMIT = "on_commit"
    ON_PUSH = "on_push"
    ON_TOOL_USE = "on_tool_use"
    ON_AGENT_START = "on_agent_start"
    ON_WORKFLOW_END = "on_workflow_end"


class CommandStatus(str, Enum):
    """Valid command status values."""

    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class HookStatus(str, Enum):
    """Valid hook status values."""

    DRAFT = "draft"
    ACTIVE = "active"
    DISABLED = "disabled"
    ARCHIVED = "archived"


class StatusType(str, Enum):
    """Generic status values used for manifest validation."""

    DRAFT = "draft"
    ACTIVE = "active"
    BETA = "beta"
    STABLE = "stable"
    DEPRECATED = "deprecated"
    DISABLED = "disabled"
    ARCHIVED = "archived"
