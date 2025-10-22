"""
File operation utilities for Betty Framework.
Includes safe file locking for concurrent access.
"""

import os
import json
import fcntl
from typing import Dict, Any, Optional
from contextlib import contextmanager

from .logging_utils import get_logger

logger = get_logger(__name__)


class FileLockError(Exception):
    """Raised when file locking fails."""
    pass


@contextmanager
def locked_file(file_path: str, mode: str = 'r+'):
    """
    Context manager for acquiring an exclusive lock on a file.

    Usage:
        with locked_file('/path/to/file.json', 'r+') as f:
            data = json.load(f)
            # ... modify data ...
            f.seek(0)
            json.dump(data, f)
            f.truncate()

    Args:
        file_path: Path to the file to lock
        mode: File open mode (default: 'r+')

    Yields:
        File object with exclusive lock

    Raises:
        FileLockError: If lock cannot be acquired
    """
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Create file if it doesn't exist and mode includes writing
    if not os.path.exists(file_path) and ('w' in mode or 'a' in mode or '+' in mode):
        with open(file_path, 'w') as f:
            pass  # Create empty file

    try:
        with open(file_path, mode) as f:
            try:
                # Acquire exclusive lock
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                logger.debug(f"Acquired lock on {file_path}")
                yield f
            finally:
                # Release lock
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                logger.debug(f"Released lock on {file_path}")
    except IOError as e:
        raise FileLockError(f"Failed to lock file {file_path}: {e}")


def safe_read_json(file_path: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Safely read a JSON file with file locking.

    Args:
        file_path: Path to JSON file
        default: Default value if file doesn't exist or is invalid

    Returns:
        Parsed JSON data or default value
    """
    if not os.path.exists(file_path):
        return default if default is not None else {}

    try:
        with locked_file(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"Failed to read {file_path}: {e}")
        return default if default is not None else {}


def safe_write_json(file_path: str, data: Dict[str, Any], indent: int = 2) -> None:
    """
    Safely write JSON data to a file with file locking.

    Args:
        file_path: Path to JSON file
        data: Data to write
        indent: JSON indentation (default: 2)
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # If file doesn't exist, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=indent)
        return

    # Otherwise, use locked write
    with locked_file(file_path, 'r+') as f:
        f.seek(0)
        json.dump(data, f, indent=indent)
        f.truncate()


def safe_update_json(file_path: str, update_fn, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Safely update a JSON file with file locking.

    Args:
        file_path: Path to JSON file
        update_fn: Function that takes current data and returns updated data
        default: Default value if file doesn't exist

    Returns:
        Updated data
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # If file doesn't exist, start with default
    if not os.path.exists(file_path):
        current_data = default if default is not None else {}
        updated_data = update_fn(current_data)
        with open(file_path, 'w') as f:
            json.dump(updated_data, f, indent=2)
        return updated_data

    # Otherwise, use locked update
    with locked_file(file_path, 'r+') as f:
        try:
            current_data = json.load(f)
        except json.JSONDecodeError:
            current_data = default if default is not None else {}

        updated_data = update_fn(current_data)

        f.seek(0)
        json.dump(updated_data, f, indent=2)
        f.truncate()

    return updated_data
