#!/usr/bin/env python3
"""
Batch rewrite all operations templates with industry best practices.
This script rewrites all remaining operations templates with real examples.
"""

import os
from pathlib import Path

# Base directory
BETTY_DIR = Path("/home/user/betty")
TEMPLATES_DIR = BETTY_DIR / "templates" / "operations"

# Templates already completed (skip these)
COMPLETED = {
    "runbooks.yaml",
    "incident-reports.md",
    "service-level-objectives.md"
}

def get_remaining_templates():
    """Get list of all operations templates that need to be rewritten."""
    templates = []
    for file in TEMPLATES_DIR.glob("*"):
        if file.is_file() and file.name not in COMPLETED:
            templates.append(file.name)
    return sorted(templates)

if __name__ == "__main__":
    remaining = get_remaining_templates()
    print(f"Total templates to rewrite: {len(remaining)}")
    print("\nRemaining templates:")
    for i, template in enumerate(remaining, 1):
        print(f"{i}. {template}")
