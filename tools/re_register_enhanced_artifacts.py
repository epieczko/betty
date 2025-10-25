#!/usr/bin/env python3
"""
Re-register all enhanced artifacts with meta.artifact using --force
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Re-register all enhanced artifact description files"""

    artifact_dir = Path("artifact_descriptions")

    if not artifact_dir.exists():
        print(f"Error: {artifact_dir} does not exist")
        return 1

    # Get all .md files
    artifact_files = sorted(artifact_dir.glob("*.md"))

    print(f"Re-registering {len(artifact_files)} enhanced artifacts with meta.artifact...\n")
    print("Note: Using --force to overwrite existing registrations with enhanced content\n")

    success = []
    failed = []

    for i, artifact_file in enumerate(artifact_files, 1):
        artifact_name = artifact_file.stem
        print(f"[{i}/{len(artifact_files)}] Re-registering: {artifact_name}...", end=" ")

        try:
            # Run meta.artifact create with --force
            result = subprocess.run(
                [
                    "python3",
                    "agents/meta.artifact/meta_artifact.py",
                    "create",
                    str(artifact_file),
                    "--force"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                print("✓")
                success.append(artifact_name)
            else:
                print("✗")
                print(f"  Error: {result.stderr[:200]}")
                failed.append((artifact_name, result.stderr))

        except subprocess.TimeoutExpired:
            print("✗ (timeout)")
            failed.append((artifact_name, "Timeout"))
        except Exception as e:
            print(f"✗ ({e})")
            failed.append((artifact_name, str(e)))

    # Summary
    print(f"\n{'='*70}")
    print(f"Re-registration Summary:")
    print(f"  Total artifacts: {len(artifact_files)}")
    print(f"  Successfully re-registered: {len(success)}")
    print(f"  Failed: {len(failed)}")

    if failed:
        print(f"\nFailed artifacts:")
        for name, error in failed[:10]:  # Show first 10 failures
            print(f"  - {name}: {error[:100]}")
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
