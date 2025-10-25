"""
Configuration module for Betty Framework.
Centralizes all paths, constants, and configuration settings.
"""

import os
from enum import Enum
from typing import Optional

# Betty Framework version
VERSION = "1.0.0"

# Base directory - can be overridden with BETTY_HOME environment variable
BETTY_HOME = os.environ.get('BETTY_HOME', os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Directory paths
BASE_DIR = BETTY_HOME
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
AGENTS_DIR = os.path.join(BASE_DIR, "agents")
REGISTRY_DIR = os.path.join(BASE_DIR, "registry")
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# File paths
REGISTRY_FILE = os.path.join(REGISTRY_DIR, "skills.json")
AGENTS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "agents.json")
COMMANDS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "commands.json")
HOOKS_REGISTRY_FILE = os.path.join(REGISTRY_DIR, "hooks.json")
WORKFLOW_HISTORY_FILE = os.path.join(REGISTRY_DIR, "workflow_history.json")
TELEMETRY_FILE = os.path.join(REGISTRY_DIR, "telemetry.json")

# Registry configuration
REGISTRY_VERSION = "1.0.0"

# Skill manifest required fields
REQUIRED_SKILL_FIELDS = ["name", "version", "description", "inputs", "outputs", "status"]

# Agent manifest required fields
REQUIRED_AGENT_FIELDS = ["name", "version", "description", "capabilities", "skills_available", "reasoning_mode"]

# Command manifest required fields
REQUIRED_COMMAND_FIELDS = ["name", "version", "description", "execution"]

# Hook manifest required fields
REQUIRED_HOOK_FIELDS = ["name", "version", "description", "event", "command"]


class SkillStatus(Enum):
    """Valid skill status values."""
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class AgentStatus(Enum):
    """Valid agent status values."""
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class ReasoningMode(Enum):
    """Valid agent reasoning modes."""
    ITERATIVE = "iterative"
    ONESHOT = "oneshot"


class CommandExecutionType(Enum):
    """Valid command execution types."""
    AGENT = "agent"
    SKILL = "skill"
    WORKFLOW = "workflow"


class HookEvent(Enum):
    """Valid hook event types."""
    ON_FILE_EDIT = "on_file_edit"
    ON_FILE_SAVE = "on_file_save"
    ON_COMMIT = "on_commit"
    ON_PUSH = "on_push"
    ON_TOOL_USE = "on_tool_use"
    ON_AGENT_START = "on_agent_start"
    ON_WORKFLOW_END = "on_workflow_end"


class CommandStatus(Enum):
    """Valid command status values."""
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class HookStatus(Enum):
    """Valid hook status values."""
    DRAFT = "draft"
    ACTIVE = "active"
    DISABLED = "disabled"
    ARCHIVED = "archived"


def get_skill_path(skill_name: str) -> str:
    """Get the directory path for a skill."""
    return os.path.join(SKILLS_DIR, skill_name)


def get_skill_manifest_path(skill_name: str) -> str:
    """Get the manifest path for a skill."""
    return os.path.join(SKILLS_DIR, skill_name, "skill.yaml")


def get_skill_handler_path(skill_name: str) -> str:
    """Get the handler script path for a skill."""
    handler_name = skill_name.replace('.', '_') + '.py'
    return os.path.join(SKILLS_DIR, skill_name, handler_name)


def get_agent_path(agent_name: str) -> str:
    """Get the directory path for an agent."""
    return os.path.join(AGENTS_DIR, agent_name)


def get_agent_manifest_path(agent_name: str) -> str:
    """Get the manifest path for an agent."""
    return os.path.join(AGENTS_DIR, agent_name, "agent.yaml")


def get_command_path(command_name: str) -> str:
    """Get the file path for a command."""
    # Commands are stored in .claude/commands/ directory
    commands_dir = os.path.join(BASE_DIR, ".claude", "commands")
    return os.path.join(commands_dir, f"{command_name}.yaml")


def get_hook_path(hook_name: str) -> str:
    """Get the file path for a hook."""
    # Hooks are stored in .claude/hooks/ directory
    hooks_dir = os.path.join(BASE_DIR, ".claude", "hooks")
    return os.path.join(hooks_dir, f"{hook_name}.yaml")


def ensure_directories() -> None:
    """Ensure all required Betty directories exist."""
    for directory in [SKILLS_DIR, AGENTS_DIR, REGISTRY_DIR, WORKFLOWS_DIR, DOCS_DIR]:
        os.makedirs(directory, exist_ok=True)

    # Ensure Claude Code directories exist
    claude_dir = os.path.join(BASE_DIR, ".claude")
    os.makedirs(os.path.join(claude_dir, "commands"), exist_ok=True)
    os.makedirs(os.path.join(claude_dir, "hooks"), exist_ok=True)
