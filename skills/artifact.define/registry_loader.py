#!/usr/bin/env python3
"""
Artifact Registry Loader - Load artifact types from JSON

This module provides the single source of truth for artifact types.
The registry is loaded from registry/artifact_types.json at runtime.
"""

import json
from pathlib import Path
from typing import Dict, Any
from functools import lru_cache

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


@lru_cache(maxsize=1)
def load_artifact_registry() -> Dict[str, Dict[str, Any]]:
    """
    Load artifact types from JSON registry file.

    Returns:
        Dictionary mapping artifact type names to their metadata

    Raises:
        FileNotFoundError: If registry file doesn't exist
        json.JSONDecodeError: If registry file is invalid JSON
    """
    registry_file = Path(BASE_DIR) / "registry" / "artifact_types.json"

    if not registry_file.exists():
        logger.error(f"Registry file not found: {registry_file}")
        raise FileNotFoundError(f"Artifact registry not found at {registry_file}")

    try:
        with open(registry_file, 'r') as f:
            data = json.load(f)

        # Convert list format to dictionary format
        registry = {}
        for artifact in data.get('artifact_types', []):
            name = artifact.get('name')
            if not name:
                continue

            # Build metadata dictionary (exclude name since it's the key)
            metadata = {}
            if artifact.get('description'):
                metadata['description'] = artifact['description']
            if artifact.get('file_pattern'):
                metadata['file_pattern'] = artifact['file_pattern']
            if artifact.get('content_type'):
                metadata['content_type'] = artifact['content_type']
            if artifact.get('schema'):
                metadata['schema'] = artifact['schema']

            registry[name] = metadata

        logger.info(f"Loaded {len(registry)} artifact types from registry")
        return registry

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in registry file: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading registry: {e}")
        raise


# Load the registry on module import
try:
    KNOWN_ARTIFACT_TYPES = load_artifact_registry()
except Exception as e:
    logger.warning(f"Failed to load artifact registry: {e}")
    logger.warning("Using empty registry as fallback")
    KNOWN_ARTIFACT_TYPES = {}


def reload_registry():
    """
    Reload the artifact registry from disk.

    This clears the cache and forces a fresh load from the JSON file.
    Useful for development and testing.
    """
    load_artifact_registry.cache_clear()
    global KNOWN_ARTIFACT_TYPES
    KNOWN_ARTIFACT_TYPES = load_artifact_registry()
    logger.info("Registry reloaded")
    return KNOWN_ARTIFACT_TYPES


def get_artifact_count() -> int:
    """Get the number of registered artifact types"""
    return len(KNOWN_ARTIFACT_TYPES)


def is_registered(artifact_type: str) -> bool:
    """Check if an artifact type is registered"""
    return artifact_type in KNOWN_ARTIFACT_TYPES


def get_artifact_metadata(artifact_type: str) -> Dict[str, Any]:
    """
    Get metadata for a specific artifact type.

    Args:
        artifact_type: The artifact type identifier

    Returns:
        Dictionary with artifact metadata, or empty dict if not found
    """
    return KNOWN_ARTIFACT_TYPES.get(artifact_type, {})
