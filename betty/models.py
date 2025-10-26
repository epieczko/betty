"""
Pydantic models for Betty Framework schema validation.

Provides data models for skill manifests and workflow definitions to ensure
schema compliance before registration or execution.
"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, ValidationError, field_validator

from betty.enums import (
    CommandExecutionType,
    HookEvent,
    ReasoningMode,
    StatusType,
)


# ============================================================================
# Skill Models
# ============================================================================

class SkillManifest(BaseModel):
    """Schema for skill manifest files."""

    name: str = Field(..., description="Skill name in namespace.action format")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    description: str = Field(..., description="Brief description of the skill")
    inputs: List[str] = Field(..., description="List of required inputs")
    outputs: List[str] = Field(..., description="List of outputs produced")
    status: str = Field(default="draft", description="Skill status (draft, beta, stable)")

    # Optional fields that may appear in manifests
    handler: Optional[str] = Field(None, description="Path to skill handler script")
    permissions: Optional[List[str]] = Field(None, description="Required permissions")
    tags: Optional[List[str]] = Field(None, description="Categorization tags")
    updated_at: Optional[str] = Field(None, description="Last update timestamp")
    version_bump_reason: Optional[str] = Field(None, description="Reason for version change")
    capabilities: Optional[List[str]] = Field(None, description="Skill capabilities")
    skills_available: Optional[List[str]] = Field(None, description="Available skills")
    entrypoints: Optional[Dict[str, Any]] = Field(None, description="Skill entrypoints")

    model_config = {
        "extra": "allow",  # Allow additional fields for extensibility
        "str_strip_whitespace": True,
    }


# ============================================================================
# Agent Models
# ============================================================================

class AgentManifest(BaseModel):
    """Schema for agent manifest files."""

    name: str = Field(..., description="Agent name")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    description: str = Field(..., description="Brief description of the agent")
    reasoning_mode: ReasoningMode = Field(..., description="Reasoning mode (iterative or oneshot)")
    capabilities: List[str] = Field(..., min_length=1, description="List of capabilities (must have at least one)")
    skills_available: List[str] = Field(..., min_length=1, description="List of available skills (must have at least one)")

    # Optional fields
    status: str = Field(default="draft", description="Agent status")
    tags: Optional[List[str]] = Field(None, description="Categorization tags")
    dependencies: Optional[List[str]] = Field(None, description="Agent dependencies")

    model_config = {
        "extra": "allow",
        "str_strip_whitespace": True,
    }


# ============================================================================
# Command Models
# ============================================================================

class CommandParameter(BaseModel):
    """Schema for command parameters."""

    name: str = Field(..., description="Parameter name")
    type: str = Field(..., description="Parameter type")
    description: Optional[str] = Field(None, description="Parameter description")
    required: bool = Field(default=False, description="Whether parameter is required")
    default: Optional[Any] = Field(None, description="Default value")

    model_config = {
        "extra": "allow",
    }


class ExecutionConfig(BaseModel):
    """Schema for command execution configuration."""

    type: CommandExecutionType = Field(..., description="Execution type (skill, agent, or workflow)")
    target: str = Field(..., description="Target skill, agent, or workflow name")
    args: Optional[List[str]] = Field(None, description="Execution arguments")
    options: Optional[Dict[str, Any]] = Field(None, description="Execution options")

    model_config = {
        "extra": "allow",
    }


class CommandManifest(BaseModel):
    """Schema for command manifest files."""

    name: str = Field(..., description="Command name")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    description: str = Field(..., description="Brief description of the command")
    execution: ExecutionConfig = Field(..., description="Execution configuration")

    # Optional fields
    parameters: Optional[List[CommandParameter]] = Field(None, description="Command parameters")
    status: str = Field(default="draft", description="Command status")
    tags: Optional[List[str]] = Field(None, description="Categorization tags")

    model_config = {
        "extra": "allow",
        "str_strip_whitespace": True,
    }


# ============================================================================
# Hook Models
# ============================================================================

class HookWhen(BaseModel):
    """Schema for hook condition."""

    pattern: Optional[str] = Field(None, description="Pattern to match")
    glob: Optional[str] = Field(None, description="Glob pattern to match")

    model_config = {
        "extra": "allow",
    }


class HookManifest(BaseModel):
    """Schema for hook manifest files."""

    name: str = Field(..., description="Hook name")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    description: str = Field(..., description="Brief description of the hook")
    event: HookEvent = Field(..., description="Hook event type")
    command: str = Field(..., min_length=1, description="Command to execute (cannot be empty)")

    # Optional fields
    when: Optional[HookWhen] = Field(None, description="Conditional execution pattern")
    blocking: bool = Field(default=False, description="Whether hook is blocking")
    timeout: Optional[int] = Field(30000, gt=0, description="Timeout in milliseconds (must be positive)")
    on_failure: str = Field(default="show_errors", description="Failure handling strategy")
    status: str = Field(default="draft", description="Hook status")
    tags: Optional[List[str]] = Field(None, description="Categorization tags")

    model_config = {
        "extra": "allow",
        "str_strip_whitespace": True,
    }


# ============================================================================
# Workflow Models
# ============================================================================

class WorkflowStep(BaseModel):
    """Schema for a single workflow step."""

    skill: Optional[str] = Field(None, description="Skill to execute in namespace.action format")
    version: Optional[str] = Field(None, description="Version constraint for skill (e.g., '>=1.0.0 <2.0.0', '^1.2.0')")
    inputs: Optional[Dict[str, Any]] = Field(None, description="Input parameters for the skill")
    required: bool = Field(default=False, description="Whether this step is required")

    # Support for agent steps (alternative to skill steps)
    agent: Optional[str] = Field(None, description="Agent to execute instead of skill")
    args: Optional[List[str]] = Field(None, description="Arguments for skill execution")
    input: Optional[str] = Field(None, description="Input for agent")

    model_config = {
        "extra": "allow",  # Allow additional fields for extensibility
    }


class WorkflowDefinition(BaseModel):
    """Schema for workflow definition files."""

    name: str = Field(..., description="Workflow name")
    version: str = Field(..., description="Workflow version")
    steps: List[WorkflowStep] = Field(..., description="List of workflow steps")

    # Optional fields
    description: Optional[str] = Field(None, description="Workflow description")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")

    model_config = {
        "extra": "allow",  # Allow additional fields for extensibility
    }


class ArtifactSpec(BaseModel):
    """Schema for workflow artifact specification."""

    type: str = Field(..., description="Artifact type")
    agent: Optional[str] = Field(None, description="Agent to create artifact")
    priority: int = Field(1, ge=1, description="Execution priority (1=highest)")
    depends_on: Optional[List[str]] = Field(None, description="Dependencies on other artifacts")

    model_config = {
        "extra": "allow",
    }


class WorkflowSpec(BaseModel):
    """Schema for workflow orchestration specification."""

    description: str = Field(..., description="Workflow description")
    artifacts: List[ArtifactSpec] = Field(..., description="List of artifacts to create")

    model_config = {
        "extra": "allow",
    }


# ============================================================================
# Plugin Models
# ============================================================================

class PluginHandler(BaseModel):
    """Schema for plugin command handler."""

    script: str = Field(..., description="Path to handler script")
    runtime: str = Field(default="python", description="Runtime environment")

    model_config = {
        "extra": "allow",
    }


class PluginCommand(BaseModel):
    """Schema for plugin command definition."""

    name: str = Field(..., description="Command name")
    description: Optional[str] = Field(None, description="Command description")
    handler: PluginHandler = Field(..., description="Command handler configuration")

    model_config = {
        "extra": "allow",
    }


class PluginManifest(BaseModel):
    """Schema for plugin.yaml files."""

    name: str = Field(..., description="Plugin name")
    version: str = Field(..., description="Plugin version")
    description: str = Field(..., description="Plugin description")
    commands: List[PluginCommand] = Field(..., description="List of plugin commands")

    # Optional fields
    author: Optional[str] = Field(None, description="Plugin author")
    homepage: Optional[str] = Field(None, description="Plugin homepage URL")
    license: Optional[str] = Field(None, description="Plugin license")

    model_config = {
        "extra": "allow",
        "str_strip_whitespace": True,
    }


# ============================================================================
# Registry Models
# ============================================================================

class SkillsRegistry(BaseModel):
    """Schema for skills.json registry file."""

    registry_version: str = Field(..., description="Registry schema version")
    generated_at: str = Field(..., description="Registry generation timestamp")
    skills: List[Dict[str, Any]] = Field(..., description="List of registered skills")

    model_config = {
        "extra": "allow",
    }


class AgentsRegistry(BaseModel):
    """Schema for agents.json registry file."""

    registry_version: str = Field(..., description="Registry schema version")
    generated_at: str = Field(..., description="Registry generation timestamp")
    agents: List[Dict[str, Any]] = Field(..., description="List of registered agents")

    model_config = {
        "extra": "allow",
    }


class CommandsRegistry(BaseModel):
    """Schema for commands.json registry file."""

    registry_version: str = Field(..., description="Registry schema version")
    generated_at: str = Field(..., description="Registry generation timestamp")
    commands: List[Dict[str, Any]] = Field(..., description="List of registered commands")

    model_config = {
        "extra": "allow",
    }


class HooksRegistry(BaseModel):
    """Schema for hooks.json registry file."""

    registry_version: str = Field(..., description="Registry schema version")
    generated_at: str = Field(..., description="Registry generation timestamp")
    hooks: List[Dict[str, Any]] = Field(..., description="List of registered hooks")

    model_config = {
        "extra": "allow",
    }


# ============================================================================
# Policy Models
# ============================================================================

class PolicyViolation(BaseModel):
    """Schema for policy validation violations."""

    policy: str = Field(..., description="Policy name that was violated")
    severity: str = Field(..., description="Violation severity (error, warning, info)")
    message: str = Field(..., description="Violation description")
    field: Optional[str] = Field(None, description="Field that violated the policy")

    model_config = {
        "extra": "allow",
    }


# ============================================================================
# Exports
# ============================================================================

__all__ = [
    # Enums
    "ReasoningMode",
    "StatusType",
    "CommandExecutionType",
    "HookEvent",
    # Skill models
    "SkillManifest",
    # Agent models
    "AgentManifest",
    # Command models
    "CommandManifest",
    "CommandParameter",
    "ExecutionConfig",
    # Hook models
    "HookManifest",
    "HookWhen",
    # Workflow models
    "WorkflowStep",
    "WorkflowDefinition",
    "ArtifactSpec",
    "WorkflowSpec",
    # Plugin models
    "PluginManifest",
    "PluginCommand",
    "PluginHandler",
    # Registry models
    "SkillsRegistry",
    "AgentsRegistry",
    "CommandsRegistry",
    "HooksRegistry",
    # Policy models
    "PolicyViolation",
    # Pydantic exception
    "ValidationError",
]
