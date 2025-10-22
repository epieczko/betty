"""
Configuration module for Betty Framework.
Centralizes all paths, constants, and configuration settings.
"""

import os
from enum import Enum
from typing import Optional

# Base directory - can be overridden with BETTY_HOME environment variable
BETTY_HOME = os.environ.get('BETTY_HOME', os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Directory paths
BASE_DIR = BETTY_HOME
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
REGISTRY_DIR = os.path.join(BASE_DIR, "registry")
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# File paths
REGISTRY_FILE = os.path.join(REGISTRY_DIR, "skills.json")
WORKFLOW_HISTORY_FILE = os.path.join(REGISTRY_DIR, "workflow_history.json")

# Registry configuration
REGISTRY_VERSION = "1.0.0"

# Skill manifest required fields
REQUIRED_SKILL_FIELDS = ["name", "version", "description", "inputs", "outputs", "status"]


class SkillStatus(Enum):
    """Valid skill status values."""
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
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


def ensure_directories() -> None:
    """Ensure all required Betty directories exist."""
    for directory in [SKILLS_DIR, REGISTRY_DIR, WORKFLOWS_DIR, DOCS_DIR]:
        os.makedirs(directory, exist_ok=True)
