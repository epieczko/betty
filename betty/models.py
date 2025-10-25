"""
Pydantic models for Betty Framework schema validation.

Provides data models for skill manifests and workflow definitions to ensure
schema compliance before registration or execution.
"""

from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any


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


class WorkflowStep(BaseModel):
    """Schema for a single workflow step."""

    skill: str = Field(..., description="Skill to execute in namespace.action format")
    inputs: Optional[Dict[str, Any]] = Field(None, description="Input parameters for the skill")
    required: bool = Field(default=False, description="Whether this step is required")

    # Support for agent steps (alternative to skill steps)
    agent: Optional[str] = Field(None, description="Agent to execute instead of skill")
    args: Optional[List[str]] = Field(None, description="Arguments for skill execution")

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


__all__ = [
    "SkillManifest",
    "WorkflowStep",
    "WorkflowDefinition",
    "ValidationError",
]
