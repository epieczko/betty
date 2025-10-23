"""
File operation utilities for Betty Framework.
Includes safe file locking for concurrent access.
"""

import os
import json
import tempfile
from typing import Dict, Any, Optional
from contextlib import contextmanager

try:  # pragma: no cover - platform specific import
    import fcntl  # type: ignore
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None

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
    directory = os.path.dirname(file_path) or "."
    os.makedirs(directory, exist_ok=True)

    # Create file if it doesn't exist and mode includes writing
    if not os.path.exists(file_path) and ('w' in mode or 'a' in mode or '+' in mode):
        with open(file_path, 'w') as f:
            pass  # Create empty file

    try:
        open_kwargs = {"mode": mode}
        if "b" not in mode:
            open_kwargs["encoding"] = "utf-8"

        with open(file_path, **open_kwargs) as f:
            if fcntl is not None:
                try:
                    # Acquire exclusive lock when supported
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                    logger.debug(f"Acquired lock on {file_path}")
                    yield f
                finally:
                    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                    logger.debug(f"Released lock on {file_path}")
            else:
                # Windows fallback – no-op locking
                logger.debug(f"Locking not supported on this platform for {file_path}")
                yield f
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
    """Atomically write JSON data to ``file_path`` in a cross-platform way."""

    directory = os.path.dirname(file_path) or "."
    os.makedirs(directory, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".betty", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as tmp_file:
            json.dump(data, tmp_file, indent=indent)
            tmp_file.flush()
            os.fsync(tmp_file.fileno())

        os.replace(tmp_path, file_path)
        logger.debug(f"Atomically wrote JSON to {file_path}")
    except Exception:
        # Ensure temporary file is removed on failure
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


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
    directory = os.path.dirname(file_path) or "."
    os.makedirs(directory, exist_ok=True)

    def _load_existing(use_lock: bool = True) -> Dict[str, Any]:
        try:
            if use_lock and fcntl is not None:
                with locked_file(file_path, 'r') as f:
                    return json.load(f)
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, FileLockError, IOError):
            return default if default is not None else {}

    if fcntl is None:
        current_data = _load_existing()
        updated_data = update_fn(current_data)
        safe_write_json(file_path, updated_data)
        return updated_data

    lock_mode = 'r+' if os.path.exists(file_path) else 'w+'
    with locked_file(file_path, lock_mode) as _:
        current_data = _load_existing(use_lock=False)
        updated_data = update_fn(current_data)
        safe_write_json(file_path, updated_data)

    return updated_data
