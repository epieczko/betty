#!/usr/bin/env python3
"""
Betty Provenance System

Provides content hashing for artifacts to enable provenance tracking and reproducibility.
All provenance records stored as append-only JSONL log for auditing.
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add parent directory to path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.config import BASE_DIR, REGISTRY_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)

try:  # pragma: no cover - platform specific import
    import fcntl  # type: ignore
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None


def compute_hash(content: Any) -> str:
    """
    Compute SHA-256 hash of content.

    Args:
        content: Any JSON-serializable content (dict, list, str, etc.)

    Returns:
        Hexadecimal hash string
    """
    try:
        # Serialize content to JSON with sorted keys for reproducibility
        json_str = json.dumps(content, sort_keys=True)

        # Compute SHA-256 hash
        hash_obj = hashlib.sha256(json_str.encode("utf-8"))
        return hash_obj.hexdigest()
    except Exception as e:
        logger.error(f"Failed to compute hash: {e}")
        raise


class ProvenanceLogger:
    """
    Records artifact provenance for reproducibility and integrity verification.

    Maintains an append-only JSONL log of all artifact hashes with metadata.
    """

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize provenance logger"""
        self.base_dir = Path(base_dir)
        self.registry_dir = Path(REGISTRY_DIR)
        self.provenance_log = self.registry_dir / "provenance.jsonl"

        # Ensure registry directory exists
        self.registry_dir.mkdir(parents=True, exist_ok=True)

        # Create provenance log if it doesn't exist
        if not self.provenance_log.exists():
            self.provenance_log.touch()
            logger.info(f"Created provenance log: {self.provenance_log}")

    def log_artifact(
        self,
        artifact_id: str,
        version: str,
        content_hash: str,
        artifact_type: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Log artifact hash to provenance log.

        Args:
            artifact_id: Artifact identifier (e.g., "workflow.definition", "skills.json")
            version: Artifact version
            content_hash: SHA-256 hash of artifact content
            artifact_type: Type of artifact (optional)
            metadata: Additional metadata (optional)

        Returns:
            Provenance record that was logged
        """
        try:
            timestamp = datetime.utcnow().isoformat() + "Z"

            # Build provenance record
            record = {
                "artifact": artifact_id,
                "version": version,
                "hash": content_hash,
                "timestamp": timestamp
            }

            # Add optional fields
            if artifact_type:
                record["type"] = artifact_type

            if metadata:
                record["metadata"] = metadata

            # Append to log with file locking for thread-safety
            with open(self.provenance_log, 'a') as f:
                # Acquire exclusive lock if supported
                if fcntl is not None:
                    try:
                        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                        f.write(json.dumps(record) + '\n')
                    finally:
                        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                else:
                    # Windows fallback - no locking
                    f.write(json.dumps(record) + '\n')

            logger.info(f"Logged provenance: {artifact_id} v{version} -> {content_hash[:8]}...")
            return record

        except Exception as e:
            logger.error(f"Failed to log provenance: {e}", exc_info=True)
            raise

    def verify(self, artifact_id: str, expected_hash: str) -> bool:
        """
        Verify artifact hash against provenance log.

        Args:
            artifact_id: Artifact identifier
            expected_hash: Expected SHA-256 hash

        Returns:
            True if hash matches any record for this artifact, False otherwise
        """
        try:
            # Read provenance log
            if not self.provenance_log.exists():
                logger.warning("Provenance log does not exist")
                return False

            with open(self.provenance_log, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue

                    try:
                        record = json.loads(line)
                        if record.get("artifact") == artifact_id:
                            if record.get("hash") == expected_hash:
                                logger.info(f"Hash verification passed: {artifact_id}")
                                return True
                    except json.JSONDecodeError as e:
                        logger.warning(f"Skipping invalid JSON line: {e}")
                        continue

            logger.warning(f"Hash verification failed: {artifact_id} (hash not found in log)")
            return False

        except Exception as e:
            logger.error(f"Failed to verify hash: {e}", exc_info=True)
            return False

    def get_artifact_history(self, artifact_id: str) -> List[Dict[str, Any]]:
        """
        Get complete provenance history for an artifact.

        Args:
            artifact_id: Artifact identifier

        Returns:
            List of provenance records, ordered from oldest to newest
        """
        try:
            history = []

            if not self.provenance_log.exists():
                return history

            with open(self.provenance_log, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue

                    try:
                        record = json.loads(line)
                        if record.get("artifact") == artifact_id:
                            history.append(record)
                    except json.JSONDecodeError as e:
                        logger.warning(f"Skipping invalid JSON line: {e}")
                        continue

            return history

        except Exception as e:
            logger.error(f"Failed to get artifact history: {e}", exc_info=True)
            return []

    def get_latest_hash(self, artifact_id: str) -> Optional[str]:
        """
        Get the most recent hash for an artifact.

        Args:
            artifact_id: Artifact identifier

        Returns:
            Latest hash string, or None if not found
        """
        history = self.get_artifact_history(artifact_id)
        if history:
            return history[-1].get("hash")
        return None

    def verify_integrity(self, artifact_id: str, content: Any) -> bool:
        """
        Verify artifact content integrity against latest logged hash.

        Args:
            artifact_id: Artifact identifier
            content: Artifact content to verify

        Returns:
            True if content hash matches latest logged hash, False otherwise
        """
        try:
            # Compute current content hash
            current_hash = compute_hash(content)

            # Get latest logged hash
            latest_hash = self.get_latest_hash(artifact_id)

            if latest_hash is None:
                logger.warning(f"No provenance record found for {artifact_id}")
                return False

            # Compare hashes
            if current_hash == latest_hash:
                logger.info(f"Integrity verification passed: {artifact_id}")
                return True
            else:
                logger.warning(f"Integrity verification failed: {artifact_id}")
                logger.warning(f"  Current hash: {current_hash}")
                logger.warning(f"  Expected hash: {latest_hash}")
                return False

        except Exception as e:
            logger.error(f"Failed to verify integrity: {e}", exc_info=True)
            return False

    def list_all_artifacts(self) -> List[str]:
        """
        List all unique artifact IDs in the provenance log.

        Returns:
            List of artifact IDs
        """
        try:
            artifacts = set()

            if not self.provenance_log.exists():
                return []

            with open(self.provenance_log, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue

                    try:
                        record = json.loads(line)
                        artifact_id = record.get("artifact")
                        if artifact_id:
                            artifacts.add(artifact_id)
                    except json.JSONDecodeError:
                        continue

            return sorted(list(artifacts))

        except Exception as e:
            logger.error(f"Failed to list artifacts: {e}", exc_info=True)
            return []


# Global instance
_provenance_logger = None

def get_provenance_logger() -> ProvenanceLogger:
    """Get global provenance logger instance"""
    global _provenance_logger
    if _provenance_logger is None:
        _provenance_logger = ProvenanceLogger()
    return _provenance_logger
