"""
Logging utilities for Betty Framework.
Provides consistent logging across all skills.
"""

import logging
import sys
from typing import Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with consistent formatting.

    Args:
        name: Logger name (typically __name__ from the calling module)
        level: Logging level (default: INFO)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Only add handler if logger doesn't have one already
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name: Logger name

    Returns:
        Logger instance
    """
    return logging.getLogger(name)
