#!/usr/bin/env python3
"""
Betty Framework - Plugin Publish Skill
Upload bundled plugin (.tar.gz) to local, gh-release, or marketplace targets.
Supports --dry-run and --validate-only modes.
"""

import os
import sys
import json
import yaml
import hashlib
import shutil
import logging
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional, Tuple

# Add betty module to path
BETTY_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, BETTY_HOME)

from betty.config import BASE_DIR, REGISTRY_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Global flags
DRY_RUN = False
VALIDATE_ONLY = False


def calculate_file_checksum(file_path: str) -> Dict[str, str]:
    """
    Calculate checksums for a file.

    Args:
        file_path: Path to the file

    Returns:
        Dictionary with md5 and sha256 checksums
    """
    logger.info("🔐 Calculating checksums...")

    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    # Stream reading to handle large files efficiently
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):  # 4KB chunks
            md5_hash.update(chunk)
            sha256_hash.update(chunk)

    checksums = {
        "md5": md5_hash.hexdigest(),
        "sha256": sha256_hash.hexdigest()
    }

    logger.info(f"  MD5:    {checksums['md5']}")
    logger.info(f"  SHA256: {checksums['sha256']}")

    return checksums


def validate_checksum(
    package_path: str,
    expected_sha256: Optional[str] = None,
    manifest_path: Optional[str] = None
) -> Tuple[bool, Dict[str, str]]:
    """
    Validate the SHA256 checksum of a package file.

    Args:
        package_path: Path to the package file
        expected_sha256: Expected SHA256 hash (optional)
        manifest_path: Path to manifest.json containing checksums (optional)

    Returns:
        Tuple of (is_valid, checksums_dict)
    """
    logger.info("🔍 Validating package checksums...")

    # Calculate actual checksums
    actual_checksums = calculate_file_checksum(package_path)

    # Try to get expected checksum from manifest if not provided
    if not expected_sha256 and manifest_path:
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
                expected_sha256 = manifest.get("package", {}).get("checksums", {}).get("sha256")
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            logger.warning(f"⚠️  Could not read checksums from manifest: {manifest_path}")

    # Validate if expected checksum is available
    if expected_sha256:
        is_valid = actual_checksums["sha256"] == expected_sha256
        if is_valid:
            logger.info("✅ SHA256 checksum validation: PASSED")
        else:
            logger.error("❌ SHA256 checksum validation: FAILED")
            logger.error(f"  Expected: {expected_sha256}")
            logger.error(f"  Actual:   {actual_checksums['sha256']}")
        return is_valid, actual_checksums
    else:
        logger.warning("⚠️  No expected checksum provided - skipping validation")
        return True, actual_checksums


def publish_local(
    package_path: str,
    checksums: Dict[str, str],
    metadata: Dict[str, Any],
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Publish plugin to local dist/published/ directory.

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata
        dry_run: If True, only show what would be done

    Returns:
        Result dictionary with publication details
    """
    logger.info("📦 Publishing to local directory...")

    if dry_run:
        logger.info("🔍 DRY RUN MODE - No changes will be made")

    # Create published directory
    published_dir = os.path.join(BASE_DIR, "dist", "published")

    if not dry_run:
        os.makedirs(published_dir, exist_ok=True)
    else:
        logger.info(f"  Would create directory: {published_dir}")

    # Copy package to published directory
    package_filename = os.path.basename(package_path)
    dest_path = os.path.join(published_dir, package_filename)

    logger.info(f"  {'Would copy' if dry_run else 'Copying'}: {package_path}")
    logger.info(f"  To:      {dest_path}")

    if not dry_run:
        shutil.copy2(package_path, dest_path)

    # Create publication metadata file
    pub_metadata = {
        "published_at": datetime.now(timezone.utc).isoformat(),
        "target": "local",
        "package": {
            "filename": package_filename,
            "path": dest_path,
            "size_bytes": os.path.getsize(package_path),
            "checksums": checksums
        },
        "metadata": metadata,
        "dry_run": dry_run
    }

    metadata_path = os.path.join(
        published_dir,
        f"{package_filename}.publish.json"
    )

    if not dry_run:
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(pub_metadata, f, indent=2)
    else:
        logger.info(f"  Would write metadata to: {metadata_path}")

    if dry_run:
        logger.info("✅ Dry run completed successfully")
    else:
        logger.info("✅ Successfully published to local directory")
        logger.info(f"  Package:  {dest_path}")
        logger.info(f"  Metadata: {metadata_path}")

    return {
        "ok": True,
        "target": "local",
        "package_path": dest_path,
        "metadata_path": metadata_path,
        "publication_metadata": pub_metadata,
        "dry_run": dry_run
    }


def publish_marketplace(
    package_path: str,
    checksums: Dict[str, str],
    metadata: Dict[str, Any],
    endpoint: str = "https://marketplace.claude.ai/api/v1/plugins",
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Publish plugin to Claude Marketplace endpoint.
    Currently simulated - actual implementation would use requests library.

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata
        endpoint: API endpoint URL
        dry_run: If True, only show what would be done

    Returns:
        Result dictionary with publication details
    """
    logger.info("🌐 Publishing to Claude Marketplace...")
    logger.info(f"  Endpoint: {endpoint}")

    if dry_run:
        logger.info("🔍 DRY RUN MODE - No actual requests will be made")

    # Prepare API request
    package_filename = os.path.basename(package_path)
    package_size = os.path.getsize(package_path)

    # Prepare JSON metadata payload for marketplace
    marketplace_metadata = {
        "plugin": {
            "name": metadata.get("name", "unknown"),
            "version": metadata.get("version", "unknown"),
            "description": metadata.get("description", ""),
            "author": metadata.get("author", {}),
            "license": metadata.get("license", ""),
            "homepage": metadata.get("homepage", ""),
            "repository": metadata.get("repository", ""),
            "tags": metadata.get("tags", []),
            "betty_version": metadata.get("betty_version", ">=0.1.0")
        },
        "package": {
            "filename": package_filename,
            "size_bytes": package_size,
            "checksums": {
                "md5": checksums["md5"],
                "sha256": checksums["sha256"]
            }
        },
        "submitted_at": datetime.now(timezone.utc).isoformat()
    }

    request_payload = {
        "method": "POST",
        "url": endpoint,
        "headers": {
            "Content-Type": "application/json",
            "X-Plugin-Name": metadata.get("name", "unknown"),
            "X-Plugin-Version": metadata.get("version", "unknown"),
            "X-Package-SHA256": checksums["sha256"]
        },
        "json": marketplace_metadata
    }

    # Simulate successful response
    simulated_response = {
        "status": 200,
        "body": {
            "success": True,
            "message": "Plugin published successfully",
            "plugin": {
                "id": f"{metadata.get('name')}-{metadata.get('version')}",
                "name": metadata.get("name"),
                "version": metadata.get("version"),
                "published_at": datetime.now(timezone.utc).isoformat(),
                "download_url": f"{endpoint.rstrip('/plugins')}/download/{metadata.get('name')}/{metadata.get('version')}/{package_filename}",
                "listing_url": f"https://marketplace.claude.ai/plugins/{metadata.get('name')}"
            },
            "checksums": checksums
        }
    }

    # Save simulation log
    sim_log_dir = os.path.join(BASE_DIR, "dist", "published", "marketplace")

    if not dry_run:
        os.makedirs(sim_log_dir, exist_ok=True)
    else:
        logger.info(f"  Would create directory: {sim_log_dir}")

    sim_log_path = os.path.join(
        sim_log_dir,
        f"{package_filename}.marketplace-publish.json"
    )

    simulation_log = {
        "simulated_at": datetime.now(timezone.utc).isoformat(),
        "target": "marketplace",
        "endpoint": endpoint,
        "request": request_payload,
        "response": simulated_response,
        "dry_run": dry_run,
        "note": "This is a simulated request. No actual HTTP request was made. To enable real publication, add requests library implementation."
    }

    if not dry_run:
        with open(sim_log_path, "w", encoding="utf-8") as f:
            json.dump(simulation_log, f, indent=2)
        logger.info("✅ Marketplace publication simulated successfully")
        logger.info(f"  Simulation log: {sim_log_path}")
    else:
        logger.info("✅ Dry run completed successfully")
        logger.info(f"  Would write simulation log to: {sim_log_path}")

    logger.warning("⚠️  NOTE: This is a SIMULATION. No actual HTTP request was made.")
    logger.info(f"  Would POST JSON metadata to: {endpoint}")
    logger.info(f"  Package size: {package_size:,} bytes")

    return {
        "ok": True,
        "target": "marketplace",
        "simulated": True,
        "endpoint": endpoint,
        "simulation_log": sim_log_path if not dry_run else None,
        "simulated_response": simulated_response["body"],
        "dry_run": dry_run
    }


def check_gh_cli_available() -> bool:
    """
    Check if GitHub CLI (gh) is available.

    Returns:
        True if gh CLI is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["gh", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def publish_gh_release(
    package_path: str,
    checksums: Dict[str, str],
    metadata: Dict[str, Any],
    dry_run: bool = False,
    auto_create: bool = False
) -> Dict[str, Any]:
    """
    Publish plugin to GitHub Release.
    Can either prepare release files or automatically create the release using gh CLI.

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata
        dry_run: If True, only show what would be done
        auto_create: If True, automatically create GitHub Release using gh CLI

    Returns:
        Result dictionary with release details
    """
    logger.info("🚀 Publishing to GitHub Release...")

    if dry_run:
        logger.info("🔍 DRY RUN MODE - No changes will be made")

    # Create releases directory
    releases_dir = os.path.join(BASE_DIR, "dist", "published", "releases")

    if not dry_run:
        os.makedirs(releases_dir, exist_ok=True)
    else:
        logger.info(f"  Would create directory: {releases_dir}")

    package_filename = os.path.basename(package_path)
    version = metadata.get("version", "unknown")
    name = metadata.get("name", "unknown")

    # Copy package to releases directory
    dest_path = os.path.join(releases_dir, package_filename)

    logger.info(f"  {'Would copy' if dry_run else 'Copying'}: {package_path}")
    logger.info(f"  To:      {dest_path}")

    if not dry_run:
        shutil.copy2(package_path, dest_path)

    # Generate release notes
    release_notes = f"""# {name} v{version}

## Release Information

- **Version:** {version}
- **Released:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
- **Package:** `{package_filename}`

## Checksums

Verify the integrity of your download:

```
MD5:    {checksums['md5']}
SHA256: {checksums['sha256']}
```

## Installation

1. Download the package: `{package_filename}`
2. Verify checksums (see above)
3. Extract: `tar -xzf {package_filename}`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: Follow instructions in README.md

## Description

{metadata.get('description', 'No description available.')}

---
*Generated by Betty Framework plugin.publish skill*
"""

    release_notes_path = os.path.join(releases_dir, f"RELEASE_NOTES_v{version}.md")

    if not dry_run:
        with open(release_notes_path, "w", encoding="utf-8") as f:
            f.write(release_notes)
    else:
        logger.info(f"  Would write release notes to: {release_notes_path}")

    # Create release metadata
    release_metadata = {
        "prepared_at": datetime.now(timezone.utc).isoformat(),
        "target": "gh-release",
        "version": version,
        "name": name,
        "package": {
            "filename": package_filename,
            "path": dest_path,
            "size_bytes": os.path.getsize(package_path),
            "checksums": checksums
        },
        "release_notes_path": release_notes_path,
        "github_cli_command": f"gh release create v{version} --title \"{name} v{version}\" --notes-file {release_notes_path} {dest_path}",
        "metadata": metadata,
        "dry_run": dry_run,
        "auto_created": False
    }

    metadata_path = os.path.join(
        releases_dir,
        f"{package_filename}.release.json"
    )

    if not dry_run:
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(release_metadata, f, indent=2)
    else:
        logger.info(f"  Would write metadata to: {metadata_path}")

    # Attempt to create GitHub Release if auto_create is True
    gh_release_created = False
    gh_release_url = None

    if auto_create and not dry_run:
        logger.info("")
        logger.info("🤖 Attempting to create GitHub Release automatically...")

        # Check if gh CLI is available
        if not check_gh_cli_available():
            logger.error("❌ GitHub CLI (gh) not available")
            logger.info("   Install: https://cli.github.com/")
            logger.info("   Falling back to manual instructions")
        else:
            try:
                # Create GitHub Release using gh CLI
                gh_command = [
                    "gh", "release", "create", f"v{version}",
                    "--title", f"{name} v{version}",
                    "--notes-file", release_notes_path,
                    dest_path
                ]

                logger.info(f"  Running: {' '.join(gh_command)}")

                result = subprocess.run(
                    gh_command,
                    cwd=BASE_DIR,
                    capture_output=True,
                    text=True,
                    timeout=60
                )

                if result.returncode == 0:
                    gh_release_created = True
                    # Extract release URL from output
                    gh_release_url = result.stdout.strip()
                    release_metadata["auto_created"] = True
                    release_metadata["github_release_url"] = gh_release_url

                    # Update metadata file with release URL
                    with open(metadata_path, "w", encoding="utf-8") as f:
                        json.dump(release_metadata, f, indent=2)

                    logger.info("✅ GitHub Release created successfully!")
                    logger.info(f"  Release URL: {gh_release_url}")
                else:
                    logger.error("❌ Failed to create GitHub Release")
                    logger.error(f"  Error: {result.stderr}")
                    logger.info("   Falling back to manual instructions")

            except subprocess.TimeoutExpired:
                logger.error("❌ GitHub Release creation timed out")
                logger.info("   Falling back to manual instructions")
            except Exception as e:
                logger.error(f"❌ Error creating GitHub Release: {e}")
                logger.info("   Falling back to manual instructions")

    elif auto_create and dry_run:
        logger.info("")
        logger.info("🤖 Would attempt to create GitHub Release automatically")
        logger.info(f"  Would run: gh release create v{version} --title \"{name} v{version}\" --notes-file {release_notes_path} {dest_path}")

    # Show summary
    if dry_run:
        logger.info("✅ Dry run completed successfully")
    elif gh_release_created:
        logger.info("✅ GitHub Release published successfully")
        logger.info(f"  Package:       {dest_path}")
        logger.info(f"  Release notes: {release_notes_path}")
        logger.info(f"  Metadata:      {metadata_path}")
        logger.info(f"  Release URL:   {gh_release_url}")
    else:
        logger.info("✅ GitHub Release prepared successfully")
        logger.info(f"  Package:       {dest_path}")
        logger.info(f"  Release notes: {release_notes_path}")
        logger.info(f"  Metadata:      {metadata_path}")
        logger.info("")
        logger.info("📋 Next steps:")
        logger.info(f"  1. Review release notes: {release_notes_path}")
        logger.info(f"  2. Create GitHub release:")
        logger.info(f"     gh release create v{version} --title \"{name} v{version}\" \\")
        logger.info(f"       --notes-file {release_notes_path} {dest_path}")

    return {
        "ok": True,
        "target": "gh-release",
        "package_path": dest_path,
        "release_notes_path": release_notes_path,
        "metadata_path": metadata_path,
        "github_cli_command": release_metadata["github_cli_command"],
        "release_metadata": release_metadata,
        "github_release_created": gh_release_created,
        "github_release_url": gh_release_url,
        "dry_run": dry_run
    }


def load_manifest(manifest_path: str) -> Optional[Dict[str, Any]]:
    """
    Load manifest.json to extract metadata.

    Args:
        manifest_path: Path to manifest.json

    Returns:
        Manifest dictionary or None
    """
    if not os.path.exists(manifest_path):
        logger.warning(f"⚠️  Manifest not found: {manifest_path}")
        return None

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"❌ Error parsing manifest: {e}")
        return None


def publish_plugin(
    package_path: str,
    target: str = "local",
    expected_sha256: Optional[str] = None,
    manifest_path: Optional[str] = None,
    marketplace_endpoint: Optional[str] = None,
    dry_run: bool = False,
    validate_only: bool = False,
    auto_create_release: bool = False
) -> Dict[str, Any]:
    """
    Publish a bundled plugin package.

    Args:
        package_path: Path to the .tar.gz package file
        target: Publication target - 'local', 'marketplace', or 'gh-release'
        expected_sha256: Expected SHA256 checksum for validation (optional)
        manifest_path: Path to manifest.json (optional, auto-detected)
        marketplace_endpoint: Marketplace API endpoint for 'marketplace' target (optional)
        dry_run: If True, only show what would be done without making changes
        validate_only: If True, only validate checksums and exit
        auto_create_release: If True and target is 'gh-release', automatically create the release

    Returns:
        Dictionary with publication results
    """
    logger.info("=" * 80)
    logger.info("🚀 BETTY PLUGIN PUBLISH")
    logger.info("=" * 80)
    logger.info("")

    if dry_run:
        logger.info("🔍 DRY RUN MODE ENABLED")
        logger.info("")

    if validate_only:
        logger.info("🔍 VALIDATE ONLY MODE ENABLED")
        logger.info("")

    # Validate inputs
    if not os.path.exists(package_path):
        error_msg = f"Package file not found: {package_path}"
        logger.error(f"❌ {error_msg}")
        return {
            "ok": False,
            "error": error_msg
        }

    valid_targets = ["local", "marketplace", "gh-release"]
    if target not in valid_targets:
        error_msg = f"Invalid target: {target}. Must be one of: {', '.join(valid_targets)}"
        logger.error(f"❌ {error_msg}")
        return {
            "ok": False,
            "error": error_msg
        }

    # Auto-detect manifest path if not provided
    if not manifest_path:
        # Try common locations
        package_dir = os.path.dirname(package_path)
        possible_manifests = [
            os.path.join(package_dir, "manifest.json"),
            os.path.join(BASE_DIR, "dist", "manifest.json")
        ]
        for possible_path in possible_manifests:
            if os.path.exists(possible_path):
                manifest_path = possible_path
                break

    logger.info(f"📦 Package: {package_path}")
    logger.info(f"🎯 Target:  {target}")
    if manifest_path:
        logger.info(f"📄 Manifest: {manifest_path}")
    logger.info("")

    # Validate checksum
    is_valid, checksums = validate_checksum(
        package_path,
        expected_sha256=expected_sha256,
        manifest_path=manifest_path
    )

    if not is_valid:
        return {
            "ok": False,
            "error": "SHA256 checksum validation failed",
            "checksums": checksums
        }

    logger.info("")

    # If validate_only mode, stop here
    if validate_only:
        logger.info("=" * 80)
        logger.info("✅ VALIDATION SUCCESSFUL")
        logger.info("=" * 80)
        logger.info("")
        logger.info("Package is valid and ready for publication.")
        logger.info(f"To publish, run without --validate-only flag:")
        logger.info(f"  python skills/plugin.publish/plugin_publish.py {package_path} --target={target}")
        return {
            "ok": True,
            "validated": True,
            "checksums": checksums,
            "package_path": package_path
        }

    # Load metadata from manifest
    metadata = {}
    if manifest_path:
        manifest = load_manifest(manifest_path)
        if manifest:
            metadata = {
                "name": manifest.get("name"),
                "version": manifest.get("version"),
                "description": manifest.get("description"),
                "author": manifest.get("author"),
                "license": manifest.get("license"),
                "homepage": manifest.get("homepage"),
                "repository": manifest.get("repository"),
                "tags": manifest.get("tags", []),
                "betty_version": manifest.get("betty_version")
            }

    # Publish based on target
    if target == "local":
        result = publish_local(package_path, checksums, metadata, dry_run=dry_run)
    elif target == "marketplace":
        endpoint = marketplace_endpoint or "https://marketplace.claude.ai/api/v1/plugins"
        result = publish_marketplace(package_path, checksums, metadata, endpoint, dry_run=dry_run)
    elif target == "gh-release":
        result = publish_gh_release(package_path, checksums, metadata, dry_run=dry_run, auto_create=auto_create_release)

    logger.info("")
    logger.info("=" * 80)
    if result.get("ok"):
        if dry_run:
            logger.info("✅ DRY RUN COMPLETED SUCCESSFULLY")
        else:
            logger.info("✅ PUBLICATION SUCCESSFUL")
    else:
        logger.info("❌ PUBLICATION FAILED")
    logger.info("=" * 80)

    return result


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Publish a bundled Betty plugin package to various targets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Publish to local directory
  %(prog)s dist/betty-1.0.0.tar.gz --target=local

  # Publish to Claude Marketplace (simulated)
  %(prog)s dist/betty-1.0.0.tar.gz --target=marketplace

  # Prepare GitHub Release
  %(prog)s dist/betty-1.0.0.tar.gz --target=gh-release

  # Create GitHub Release automatically
  %(prog)s dist/betty-1.0.0.tar.gz --target=gh-release --auto-create

  # Dry run (show what would happen)
  %(prog)s dist/betty-1.0.0.tar.gz --target=marketplace --dry-run

  # Validate only (check checksums without publishing)
  %(prog)s dist/betty-1.0.0.tar.gz --validate-only
        """
    )
    parser.add_argument(
        "package_path",
        help="Path to the .tar.gz package file"
    )
    parser.add_argument(
        "--target",
        choices=["local", "marketplace", "gh-release"],
        default="local",
        help="Publication target: local (dist/published/), marketplace (Claude Marketplace API), or gh-release (GitHub Release) (default: local)"
    )
    parser.add_argument(
        "--sha256",
        help="Expected SHA256 checksum for validation (auto-detected from manifest.json if not provided)"
    )
    parser.add_argument(
        "--manifest",
        help="Path to manifest.json (auto-detected if not provided)"
    )
    parser.add_argument(
        "--endpoint",
        help="Marketplace API endpoint for 'marketplace' target (default: https://marketplace.claude.ai/api/v1/plugins)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making any changes"
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate package checksums without publishing"
    )
    parser.add_argument(
        "--auto-create",
        action="store_true",
        help="For gh-release target: automatically create GitHub Release using gh CLI (requires gh CLI installed)"
    )

    args = parser.parse_args()

    # Validate argument combinations
    if args.validate_only and args.dry_run:
        logger.warning("⚠️  Both --validate-only and --dry-run specified. Using --validate-only.")
        logger.warning("    (--dry-run is ignored when --validate-only is set)")
        logger.info("")

    if args.auto_create and args.target != "gh-release":
        logger.warning(f"⚠️  --auto-create only applies to gh-release target (current target: {args.target})")
        logger.info("")

    result = publish_plugin(
        package_path=args.package_path,
        target=args.target,
        expected_sha256=args.sha256,
        manifest_path=args.manifest,
        marketplace_endpoint=args.endpoint,
        dry_run=args.dry_run,
        validate_only=args.validate_only,
        auto_create_release=args.auto_create
    )

    # Exit with appropriate code
    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
