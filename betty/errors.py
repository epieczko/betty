"""
Exception classes for Betty Framework.
Provides structured error handling across all skills.
"""

from typing import Optional, Dict, Any
import json


class BettyError(Exception):
    """Base exception for all Betty Framework errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        """
        Initialize Betty error.

        Args:
            message: Error message
            details: Additional error details
        """
        self.message = message
        self.details = details or {}
        super().__init__(message)

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary for JSON serialization."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details
        }

    def to_json(self, indent: int = 2) -> str:
        """Convert error to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)


class SkillNotFoundError(BettyError):
    """Raised when a skill cannot be found."""
    pass


class SkillValidationError(BettyError):
    """Raised when skill manifest validation fails."""
    pass


class RegistryError(BettyError):
    """Raised when registry operations fail."""
    pass


class WorkflowError(BettyError):
    """Raised when workflow execution fails."""
    pass


class ManifestError(BettyError):
    """Raised when manifest parsing or creation fails."""
    pass


class AgentValidationError(BettyError):
    """Raised when agent manifest validation fails."""
    pass


class AgentRegistryError(BettyError):
    """Raised when agent registry operations fail."""
    pass


def format_error_response(error: Exception, include_traceback: bool = False) -> Dict[str, Any]:
    """
    Format an exception into a standardized error response.

    Args:
        error: Exception to format
        include_traceback: Whether to include traceback (default: False)

    Returns:
        Dictionary with error information
    """
    if isinstance(error, BettyError):
        return error.to_dict()

    response = {
        "error": type(error).__name__,
        "message": str(error),
        "details": {}
    }

    if include_traceback:
        import traceback
        response["traceback"] = traceback.format_exc()

    return response
