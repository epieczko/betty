"""
Semantic versioning utilities for Betty Framework.

Provides helpers for parsing, comparing, validating, and manipulating
semantic versions according to SemVer 2.0.0 specification.
"""

import re
from typing import Optional, Tuple


class VersionError(Exception):
    """Raised when version operations fail."""
    pass


class VersionConflictError(Exception):
    """Raised when attempting to overwrite an active version."""
    pass


def parse_version(v: str) -> Tuple[int, int, int, Optional[str]]:
    """
    Parse a semantic version string into components.

    Args:
        v: Version string (e.g., "1.2.3", "0.1.0-alpha", "2.0.0-beta.1")

    Returns:
        Tuple of (major, minor, patch, prerelease) where prerelease is None
        for stable versions or a string like "alpha" or "beta.1"

    Raises:
        VersionError: If version string is invalid

    Examples:
        >>> parse_version("1.2.3")
        (1, 2, 3, None)
        >>> parse_version("0.1.0-alpha")
        (0, 1, 0, "alpha")
        >>> parse_version("2.0.0-beta.1")
        (2, 0, 0, "beta.1")
    """
    if not v:
        raise VersionError("Version string cannot be empty")

    # SemVer 2.0.0 pattern
    # Format: MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
    pattern = r'^(\d+)\.(\d+)\.(\d+)(?:-([a-zA-Z0-9.-]+))?(?:\+[a-zA-Z0-9.-]+)?$'
    match = re.match(pattern, v)

    if not match:
        raise VersionError(
            f"Invalid semantic version: '{v}'. "
            "Must follow format MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]"
        )

    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))
    prerelease = match.group(4)  # None if no prerelease

    return (major, minor, patch, prerelease)


def compare(v1: str, v2: str) -> int:
    """
    Compare two semantic versions.

    Args:
        v1: First version string
        v2: Second version string

    Returns:
        -1 if v1 < v2
         0 if v1 == v2
         1 if v1 > v2

    Raises:
        VersionError: If either version string is invalid

    Examples:
        >>> compare("1.0.0", "2.0.0")
        -1
        >>> compare("2.0.0", "1.0.0")
        1
        >>> compare("1.0.0", "1.0.0")
        0
        >>> compare("1.0.0-alpha", "1.0.0")
        -1
    """
    major1, minor1, patch1, pre1 = parse_version(v1)
    major2, minor2, patch2, pre2 = parse_version(v2)

    # Compare major, minor, patch
    if major1 != major2:
        return -1 if major1 < major2 else 1
    if minor1 != minor2:
        return -1 if minor1 < minor2 else 1
    if patch1 != patch2:
        return -1 if patch1 < patch2 else 1

    # Handle prerelease versions
    # Per SemVer 2.0.0: when major.minor.patch are equal, a pre-release
    # version has lower precedence than a normal version
    if pre1 is None and pre2 is None:
        return 0
    if pre1 is None:  # v1 is stable, v2 is prerelease
        return 1
    if pre2 is None:  # v1 is prerelease, v2 is stable
        return -1

    # Both have prerelease, compare lexicographically
    # (simplified; full SemVer has complex rules for numeric vs alphanumeric)
    if pre1 < pre2:
        return -1
    elif pre1 > pre2:
        return 1
    else:
        return 0


def satisfies(candidate: str, constraint: str) -> bool:
    """
    Check if a candidate version satisfies a version constraint.

    Supports the following constraint operators:
    - "1.2.3" or "=1.2.3" - exact match
    - ">1.2.3" - greater than
    - ">=1.2.3" - greater than or equal
    - "<1.2.3" - less than
    - "<=1.2.3" - less than or equal
    - ">=1.2.0 <2.0.0" - range constraint (space-separated)
    - "^1.2.3" - caret range (compatible with 1.x.x)
    - "~1.2.3" - tilde range (compatible with 1.2.x)

    Args:
        candidate: Version string to check
        constraint: Version constraint expression

    Returns:
        True if candidate satisfies the constraint, False otherwise

    Raises:
        VersionError: If version strings are invalid

    Examples:
        >>> satisfies("1.2.3", "1.2.3")
        True
        >>> satisfies("1.2.3", ">=1.0.0 <2.0.0")
        True
        >>> satisfies("2.0.0", ">=1.0.0 <2.0.0")
        False
        >>> satisfies("1.3.0", "^1.2.0")
        True
        >>> satisfies("1.2.5", "~1.2.3")
        True
    """
    if not constraint:
        raise VersionError("Constraint cannot be empty")

    constraint = constraint.strip()

    # Handle range constraints (e.g., ">=1.0.0 <2.0.0")
    if ' ' in constraint:
        parts = constraint.split()
        return all(satisfies(candidate, part) for part in parts)

    # Handle caret constraint (^x.y.z - compatible with x.y.z, allows y and z to increment)
    if constraint.startswith('^'):
        base_version = constraint[1:]
        major, minor, patch, pre = parse_version(base_version)
        cand_major, cand_minor, cand_patch, cand_pre = parse_version(candidate)

        # Allow changes that don't modify the left-most non-zero digit
        if major > 0:
            # ^1.2.3 allows >=1.2.3 <2.0.0
            return cand_major == major and compare(candidate, base_version) >= 0 and cand_major < major + 1
        elif minor > 0:
            # ^0.2.3 allows >=0.2.3 <0.3.0
            return cand_major == 0 and cand_minor == minor and compare(candidate, base_version) >= 0
        else:
            # ^0.0.3 allows >=0.0.3 <0.0.4
            return cand_major == 0 and cand_minor == 0 and cand_patch == patch and compare(candidate, base_version) >= 0

    # Handle tilde constraint (~x.y.z - compatible with x.y.z, allows z to increment)
    if constraint.startswith('~'):
        base_version = constraint[1:]
        major, minor, patch, pre = parse_version(base_version)
        cand_major, cand_minor, cand_patch, cand_pre = parse_version(candidate)

        # ~1.2.3 allows >=1.2.3 <1.3.0
        return (cand_major == major and cand_minor == minor and
                compare(candidate, base_version) >= 0 and cand_minor < minor + 1)

    # Handle comparison operators
    if constraint.startswith('>='):
        base_version = constraint[2:].strip()
        return compare(candidate, base_version) >= 0
    elif constraint.startswith('<='):
        base_version = constraint[2:].strip()
        return compare(candidate, base_version) <= 0
    elif constraint.startswith('>'):
        base_version = constraint[1:].strip()
        return compare(candidate, base_version) > 0
    elif constraint.startswith('<'):
        base_version = constraint[1:].strip()
        return compare(candidate, base_version) < 0
    elif constraint.startswith('='):
        base_version = constraint[1:].strip()
        return compare(candidate, base_version) == 0
    else:
        # Exact match (no operator)
        return compare(candidate, constraint) == 0


def next_version(old: str, level: str = "patch") -> str:
    """
    Generate the next version by incrementing at the specified level.

    Args:
        old: Current version string
        level: Level to increment ("major", "minor", or "patch")

    Returns:
        Next version string

    Raises:
        VersionError: If version string is invalid or level is unknown

    Examples:
        >>> next_version("1.2.3", "patch")
        '1.2.4'
        >>> next_version("1.2.3", "minor")
        '1.3.0'
        >>> next_version("1.2.3", "major")
        '2.0.0'
        >>> next_version("1.2.3-alpha", "patch")
        '1.2.4'
    """
    major, minor, patch, prerelease = parse_version(old)

    if level == "major":
        return f"{major + 1}.0.0"
    elif level == "minor":
        return f"{major}.{minor + 1}.0"
    elif level == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise VersionError(
            f"Unknown version level: '{level}'. "
            "Must be 'major', 'minor', or 'patch'"
        )


def is_monotonic_increase(old: str, new: str) -> bool:
    """
    Check if new version is a monotonic increase from old version.

    A monotonic increase means the new version is strictly greater than
    the old version according to SemVer precedence rules.

    Args:
        old: Old version string
        new: New version string

    Returns:
        True if new > old, False otherwise

    Examples:
        >>> is_monotonic_increase("0.1.0", "0.2.0")
        True
        >>> is_monotonic_increase("1.0.0", "0.9.0")
        False
        >>> is_monotonic_increase("1.0.0", "1.0.0")
        False
    """
    return compare(new, old) > 0
