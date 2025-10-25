#!/usr/bin/env python3
"""
Betty Framework - Component Certification System

Ensures all components have full traceability before execution.
Nothing runs in Betty without certification.

Certification Requirements:
- Component must have a traceability record
- Record must include requirement linkage
- Record must have passed verification checks
"""

import os
import json
import time
import functools
from pathlib import Path
from typing import Dict, Any, Optional, List, Callable
from datetime import datetime
from enum import Enum

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.traceability import get_tracer

logger = setup_logger(__name__)


class CertificationMode(Enum):
    """Certification enforcement modes"""
    STRICT = "strict"      # Enforce certification, block uncertified components
    DEV = "dev"            # Warn about uncertified, but allow execution
    DISABLED = "disabled"  # No certification checks (not recommended)


class CertificationError(Exception):
    """Raised when a component fails certification"""
    pass


class ComponentCertification:
    """
    Handles component certification and validation

    A component is certified if:
    1. It has a traceability record
    2. The record includes requirement information
    3. The record shows passed verification
    """

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize certification system"""
        self.base_dir = Path(base_dir)
        self.tracer = get_tracer()

        # Get certification mode from environment
        mode_str = os.environ.get("BETTY_CERT_MODE", "strict").lower()
        try:
            self.mode = CertificationMode(mode_str)
        except ValueError:
            logger.warning(f"Invalid BETTY_CERT_MODE '{mode_str}', using STRICT")
            self.mode = CertificationMode.STRICT

        if self.mode != CertificationMode.STRICT:
            logger.warning(f"⚠️  Certification mode: {self.mode.value}")

    def is_certified(self, component_id: str) -> bool:
        """
        Check if component is certified

        Args:
            component_id: Component identifier

        Returns:
            True if certified, False otherwise
        """
        try:
            trace = self.tracer.get_trace(component_id)

            if not trace:
                return False

            # Check for requirement linkage
            requirement = trace.get("requirement", {})
            if not requirement or not requirement.get("id") or not requirement.get("description"):
                logger.debug(f"Component {component_id} missing requirement linkage")
                return False

            # Check verification status
            verification = trace.get("verification", {})
            status = verification.get("status", "").lower()

            if status not in ["passed", "partial"]:
                logger.debug(f"Component {component_id} has verification status: {status}")
                return False

            return True

        except Exception as e:
            logger.error(f"Error checking certification for {component_id}: {e}")
            return False

    def get_certification_details(self, component_id: str) -> Optional[Dict[str, Any]]:
        """
        Get certification details for a component

        Args:
            component_id: Component identifier

        Returns:
            Certification details or None if not certified
        """
        trace = self.tracer.get_trace(component_id)

        if not trace:
            return None

        requirement = trace.get("requirement", {})
        verification = trace.get("verification", {})
        creation = trace.get("creation", {})

        return {
            "component_id": component_id,
            "certified": self.is_certified(component_id),
            "requirement_id": requirement.get("id"),
            "requirement_description": requirement.get("description"),
            "verification_status": verification.get("status"),
            "created_by": creation.get("created_by", {}).get("tool"),
            "created_at": creation.get("timestamp"),
            "trace_id": trace.get("trace_id")
        }

    def validate_component(
        self,
        component_id: str,
        component_type: str,
        operation: str = "execution"
    ) -> None:
        """
        Validate component is certified before allowing operation

        Args:
            component_id: Component identifier
            component_type: Type (agent, skill, hook)
            operation: Operation being attempted

        Raises:
            CertificationError: If component is not certified and mode is STRICT
        """
        is_cert = self.is_certified(component_id)

        if not is_cert:
            msg = (
                f"❌ CERTIFICATION FAILED\n"
                f"Component: {component_id} ({component_type})\n"
                f"Operation: {operation}\n"
                f"Reason: Component lacks required traceability certification\n\n"
                f"Betty Framework requires full traceability for all components.\n"
                f"To certify this component, create it with requirement linkage:\n\n"
                f"  For agents:\n"
                f"    python3 agents/atum/atum.py description.md \\\n"
                f"      --requirement-id REQ-XXX \\\n"
                f"      --requirement-description '...'\n\n"
                f"  For skills:\n"
                f"    python3 agents/meta.skill/meta_skill.py description.md \\\n"
                f"      --requirement-id REQ-XXX \\\n"
                f"      --requirement-description '...'\n\n"
                f"  For hooks:\n"
                f"    python3 agents/meta.hook/meta_hook.py description.md \\\n"
                f"      --requirement-id REQ-XXX \\\n"
                f"      --requirement-description '...'\n\n"
                f"To bypass for development: export BETTY_CERT_MODE=dev\n"
            )

            if self.mode == CertificationMode.STRICT:
                logger.error(msg)
                raise CertificationError(msg)
            elif self.mode == CertificationMode.DEV:
                logger.warning(msg)
            # DISABLED mode: do nothing
        else:
            logger.debug(f"✅ Component {component_id} is certified")

    def log_execution(
        self,
        component_id: str,
        operation: str,
        inputs: Optional[Dict[str, Any]] = None,
        result: Optional[str] = None,
        success: bool = True,
        error: Optional[str] = None,
        duration_ms: Optional[float] = None
    ) -> None:
        """
        Log component execution for audit trail

        Args:
            component_id: Component identifier
            operation: Operation performed (e.g., "execute", "invoke")
            inputs: Input parameters
            result: Result status or value
            success: Whether execution succeeded
            error: Error message if failed
            duration_ms: Execution duration in milliseconds
        """
        try:
            # Log as verification check with type "execution"
            details = {
                "operation": operation,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "success": success,
                "inputs": inputs or {},
                "result": result or "completed"
            }

            if error:
                details["error"] = error

            if duration_ms is not None:
                details["duration_ms"] = duration_ms

            self.tracer.log_verification(
                component_id=component_id,
                check_type="execution",
                tool="betty.runtime",
                result="passed" if success else "failed",
                details=details
            )

        except Exception as e:
            logger.error(f"Failed to log execution for {component_id}: {e}")

    def list_certified_components(self, component_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all certified components

        Args:
            component_type: Filter by type (agent, skill, hook) or None for all

        Returns:
            List of certified component details
        """
        all_traces = self.tracer.list_all_traces()
        certified = []

        for trace in all_traces:
            component_id = trace.get("component", {}).get("id")
            comp_type = trace.get("component", {}).get("type")

            # Filter by type if specified
            if component_type and comp_type != component_type:
                continue

            if self.is_certified(component_id):
                details = self.get_certification_details(component_id)
                if details:
                    certified.append(details)

        return certified

    def list_uncertified_components(self) -> List[str]:
        """
        Find components in the filesystem that lack certification

        Returns:
            List of uncertified component paths
        """
        uncertified = []

        # Check agents
        agents_dir = self.base_dir / "agents"
        if agents_dir.exists():
            for agent_yaml in agents_dir.rglob("agent.yaml"):
                # Extract agent ID from path (e.g., agents/code.reviewer/agent.yaml -> code.reviewer)
                agent_dir = agent_yaml.parent.name
                if not self.is_certified(agent_dir):
                    uncertified.append(str(agent_yaml))

        # Check skills
        skills_dir = self.base_dir / "skills"
        if skills_dir.exists():
            for skill_yaml in skills_dir.rglob("skill.yaml"):
                skill_dir = skill_yaml.parent.name
                if not self.is_certified(skill_dir):
                    uncertified.append(str(skill_yaml))

        # Hooks are more complex (multiple in one file), skip for now

        return uncertified


# Global certification instance
_certifier: Optional[ComponentCertification] = None


def get_certifier() -> ComponentCertification:
    """Get global certification instance"""
    global _certifier
    if _certifier is None:
        _certifier = ComponentCertification()
    return _certifier


def require_certification(component_id: str, component_type: str):
    """
    Decorator to enforce certification on component execution

    Usage:
        @require_certification("file.compare", "skill")
        def execute(self, ...):
            ...

    Args:
        component_id: Component identifier
        component_type: Component type (agent, skill, hook)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            certifier = get_certifier()

            # Validate certification before execution
            certifier.validate_component(component_id, component_type, "execution")

            # Track execution time
            start_time = time.time()
            success = True
            error = None
            result = None

            try:
                # Execute the function
                result = func(*args, **kwargs)
                return result

            except Exception as e:
                success = False
                error = str(e)
                raise

            finally:
                # Log execution for audit trail
                duration_ms = (time.time() - start_time) * 1000

                # Extract result status if available
                result_status = None
                if result and isinstance(result, dict):
                    result_status = result.get("status") or ("passed" if result.get("ok") else "failed")

                certifier.log_execution(
                    component_id=component_id,
                    operation="execute",
                    inputs=kwargs,
                    result=result_status,
                    success=success,
                    error=error,
                    duration_ms=duration_ms
                )

        return wrapper
    return decorator


def certified_skill(skill_id: str):
    """
    Decorator for skill execution methods

    Usage:
        @certified_skill("file.compare")
        def execute(self, ...):
            ...
    """
    return require_certification(skill_id, "skill")


def certified_agent(agent_id: str):
    """
    Decorator for agent execution methods

    Usage:
        @certified_agent("code.reviewer")
        def execute(self, ...):
            ...
    """
    return require_certification(agent_id, "agent")


def certified_hook(hook_id: str):
    """
    Decorator for hook execution functions

    Usage:
        @certified_hook("pre-commit-lint")
        def run_hook(...):
            ...
    """
    return require_certification(hook_id, "hook")
