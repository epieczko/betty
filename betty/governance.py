"""
Artifact Governance Module

Enforces immutability and retention policies defined in artifact descriptors.
Provides runtime enforcement of artifact lifecycle constraints.
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from pathlib import Path


def get_governance_log_path() -> str:
    """Get the path to the governance log file."""
    registry_dir = Path(__file__).parent.parent / "registry"
    registry_dir.mkdir(exist_ok=True)
    return str(registry_dir / "governance.log")


def log_governance_action(
    artifact_id: str,
    action: str,
    outcome: str,
    message: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> None:
    """
    Log a governance action to the governance log file.

    Args:
        artifact_id: The ID of the artifact
        action: The action being performed (e.g., "write", "modify", "delete")
        outcome: The outcome of the action (e.g., "allowed", "blocked", "error")
        message: Optional message providing additional context
        metadata: Optional metadata about the action
    """
    log_path = get_governance_log_path()

    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "artifact_id": artifact_id,
        "action": action,
        "outcome": outcome,
    }

    if message:
        log_entry["message"] = message

    if metadata:
        log_entry["metadata"] = metadata

    try:
        # Append to log file as JSONL (one JSON object per line)
        with open(log_path, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        # Don't fail the operation if logging fails
        print(f"Warning: Failed to write to governance log: {e}", flush=True)


def enforce_governance(artifact_meta: Dict[str, Any]) -> None:
    """
    Enforce governance policies on an artifact.

    This function checks both immutability and retention policies defined
    in the artifact metadata and raises PermissionError if the artifact
    cannot be modified.

    Args:
        artifact_meta: Dictionary containing artifact metadata with fields:
            - id: Artifact identifier (required)
            - immutability: Boolean indicating if artifact is immutable (optional)
            - status: Current status of the artifact (optional)
            - retention_days: Number of days the artifact should be retained (optional)
            - created_at: ISO format timestamp when artifact was created (required if retention_days is set)

    Raises:
        PermissionError: If the artifact is immutable and not in draft status,
                        or if the artifact has expired based on retention policy
        ValueError: If required fields are missing from artifact_meta

    Examples:
        >>> # Immutable artifact check
        >>> artifact = {
        ...     "id": "artifact-123",
        ...     "immutability": True,
        ...     "status": "published"
        ... }
        >>> enforce_governance(artifact)  # Raises PermissionError

        >>> # Retention policy check
        >>> artifact = {
        ...     "id": "artifact-456",
        ...     "retention_days": 30,
        ...     "created_at": "2020-01-01T00:00:00"
        ... }
        >>> enforce_governance(artifact)  # Raises PermissionError if expired
    """
    # Validate required fields
    if not artifact_meta:
        raise ValueError("Artifact metadata cannot be empty")

    if "id" not in artifact_meta:
        raise ValueError("Artifact metadata must contain 'id' field")

    artifact_id = artifact_meta["id"]

    # Check immutability policy
    if artifact_meta.get("immutability") and artifact_meta.get("status") != "draft":
        error_msg = f"Artifact {artifact_id} is immutable."

        log_governance_action(
            artifact_id=artifact_id,
            action="modify",
            outcome="blocked",
            message=error_msg,
            metadata={
                "policy": "immutability",
                "status": artifact_meta.get("status"),
                "immutability": artifact_meta.get("immutability")
            }
        )

        raise PermissionError(error_msg)

    # Check retention policy
    retention_days = artifact_meta.get("retention_days")
    if retention_days is not None:
        if "created_at" not in artifact_meta:
            raise ValueError(
                f"Artifact {artifact_id} has retention_days set but missing 'created_at' field"
            )

        try:
            created_at_str = artifact_meta["created_at"]
            # Handle both with and without timezone suffix
            if created_at_str.endswith('Z'):
                created_at_str = created_at_str[:-1]

            # Parse the datetime
            created = datetime.fromisoformat(created_at_str)

            # Calculate expiration
            expiration_date = created + timedelta(days=retention_days)
            now = datetime.utcnow()

            if now > expiration_date:
                error_msg = f"Artifact {artifact_id} expired after {retention_days} days."

                log_governance_action(
                    artifact_id=artifact_id,
                    action="access",
                    outcome="blocked",
                    message=error_msg,
                    metadata={
                        "policy": "retention",
                        "retention_days": retention_days,
                        "created_at": artifact_meta["created_at"],
                        "expiration_date": expiration_date.isoformat(),
                        "current_date": now.isoformat()
                    }
                )

                raise PermissionError(error_msg)

        except (ValueError, TypeError) as e:
            raise ValueError(
                f"Invalid created_at format for artifact {artifact_id}: {e}"
            )

    # If we get here, governance checks passed
    log_governance_action(
        artifact_id=artifact_id,
        action="check",
        outcome="allowed",
        message="Governance checks passed",
        metadata={
            "immutability": artifact_meta.get("immutability"),
            "status": artifact_meta.get("status"),
            "retention_days": artifact_meta.get("retention_days")
        }
    )


def check_artifact_accessibility(artifact_meta: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check if an artifact is accessible without raising exceptions.

    This is a non-throwing version of enforce_governance that returns
    a dictionary indicating whether the artifact is accessible and why.

    Args:
        artifact_meta: Dictionary containing artifact metadata

    Returns:
        Dictionary with keys:
            - accessible: Boolean indicating if artifact can be accessed
            - reason: String explaining why access is blocked (if applicable)
            - violations: List of policy violations
    """
    result = {
        "accessible": True,
        "reason": None,
        "violations": []
    }

    try:
        enforce_governance(artifact_meta)
    except PermissionError as e:
        result["accessible"] = False
        result["reason"] = str(e)
        result["violations"].append({
            "type": "PermissionError",
            "message": str(e)
        })
    except ValueError as e:
        result["accessible"] = False
        result["reason"] = str(e)
        result["violations"].append({
            "type": "ValueError",
            "message": str(e)
        })

    return result
