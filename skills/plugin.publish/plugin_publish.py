#!/usr/bin/env python3
"""
Betty Framework - Plugin Publish Skill
Upload bundled plugin (.tar.gz) to local, remote, or release targets.
"""

import os
import sys
import json
import yaml
import hashlib
import shutil
import logging
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
    metadata: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Publish plugin to local dist/published/ directory.

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata

    Returns:
        Result dictionary with publication details
    """
    logger.info("📦 Publishing to local directory...")

    # Create published directory
    published_dir = os.path.join(BASE_DIR, "dist", "published")
    os.makedirs(published_dir, exist_ok=True)

    # Copy package to published directory
    package_filename = os.path.basename(package_path)
    dest_path = os.path.join(published_dir, package_filename)

    logger.info(f"  Copying: {package_path}")
    logger.info(f"  To:      {dest_path}")

    shutil.copy2(package_path, dest_path)

    # Create publication metadata file
    pub_metadata = {
        "published_at": datetime.now(timezone.utc).isoformat(),
        "target": "local",
        "package": {
            "filename": package_filename,
            "path": dest_path,
            "size_bytes": os.path.getsize(dest_path),
            "checksums": checksums
        },
        "metadata": metadata
    }

    metadata_path = os.path.join(
        published_dir,
        f"{package_filename}.publish.json"
    )

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(pub_metadata, f, indent=2)

    logger.info("✅ Successfully published to local directory")
    logger.info(f"  Package:  {dest_path}")
    logger.info(f"  Metadata: {metadata_path}")

    return {
        "ok": True,
        "target": "local",
        "package_path": dest_path,
        "metadata_path": metadata_path,
        "publication_metadata": pub_metadata
    }


def publish_remote(
    package_path: str,
    checksums: Dict[str, str],
    metadata: Dict[str, Any],
    endpoint: str = "https://marketplace.claude.ai/api/v1/plugins"
) -> Dict[str, Any]:
    """
    Simulate publishing plugin to remote Claude Marketplace endpoint.
    (Mocked for now - actual implementation would use requests library)

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata
        endpoint: API endpoint URL

    Returns:
        Result dictionary with publication details
    """
    logger.info("🌐 Publishing to remote endpoint (SIMULATED)...")
    logger.info(f"  Endpoint: {endpoint}")

    # Simulate API request preparation
    package_filename = os.path.basename(package_path)
    package_size = os.path.getsize(package_path)

    simulated_request = {
        "method": "POST",
        "url": endpoint,
        "headers": {
            "Content-Type": "multipart/form-data",
            "X-Package-Name": metadata.get("name", "unknown"),
            "X-Package-Version": metadata.get("version", "unknown"),
            "X-Package-SHA256": checksums["sha256"]
        },
        "files": {
            "package": package_filename
        },
        "data": {
            "name": metadata.get("name"),
            "version": metadata.get("version"),
            "description": metadata.get("description"),
            "author": metadata.get("author"),
            "license": metadata.get("license"),
            "checksums": checksums
        }
    }

    # Simulate successful response
    simulated_response = {
        "status": 200,
        "response": {
            "ok": True,
            "message": "Plugin published successfully",
            "plugin_id": f"{metadata.get('name')}-{metadata.get('version')}",
            "published_at": datetime.now(timezone.utc).isoformat(),
            "download_url": f"{endpoint}/{metadata.get('name')}/{metadata.get('version')}/{package_filename}",
            "checksums": checksums
        }
    }

    # Save simulation log
    sim_log_dir = os.path.join(BASE_DIR, "dist", "published", "simulations")
    os.makedirs(sim_log_dir, exist_ok=True)

    sim_log_path = os.path.join(
        sim_log_dir,
        f"{package_filename}.remote-publish.json"
    )

    simulation_log = {
        "simulated_at": datetime.now(timezone.utc).isoformat(),
        "target": "remote",
        "endpoint": endpoint,
        "request": simulated_request,
        "response": simulated_response,
        "note": "This is a simulated request. No actual HTTP request was made."
    }

    with open(sim_log_path, "w", encoding="utf-8") as f:
        json.dump(simulation_log, f, indent=2)

    logger.info("✅ Remote publication simulated successfully")
    logger.info(f"  Simulation log: {sim_log_path}")
    logger.warning("⚠️  NOTE: This is a SIMULATION. No actual HTTP request was made.")
    logger.info(f"  Would POST to: {endpoint}")
    logger.info(f"  Package size: {package_size:,} bytes")

    return {
        "ok": True,
        "target": "remote",
        "simulated": True,
        "endpoint": endpoint,
        "simulation_log": sim_log_path,
        "simulated_response": simulated_response["response"]
    }


def publish_release(
    package_path: str,
    checksums: Dict[str, str],
    metadata: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Prepare plugin for GitHub Release publication.
    Generates release notes and instructions.

    Args:
        package_path: Path to the package file
        checksums: Checksums dictionary
        metadata: Additional metadata

    Returns:
        Result dictionary with release preparation details
    """
    logger.info("🚀 Preparing GitHub Release publication...")

    # Create releases directory
    releases_dir = os.path.join(BASE_DIR, "dist", "published", "releases")
    os.makedirs(releases_dir, exist_ok=True)

    package_filename = os.path.basename(package_path)
    version = metadata.get("version", "unknown")
    name = metadata.get("name", "unknown")

    # Copy package to releases directory
    dest_path = os.path.join(releases_dir, package_filename)
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

## GitHub CLI Commands

To create this release using GitHub CLI:

```bash
# Create release
gh release create v{version} \\
  --title "{name} v{version}" \\
  --notes-file RELEASE_NOTES.md \\
  {package_filename}

# Or with notes inline
gh release create v{version} \\
  --title "{name} v{version}" \\
  --notes "Release of {name} version {version}" \\
  {package_filename}
```

## Manual Upload

1. Go to: https://github.com/YOUR_ORG/YOUR_REPO/releases/new
2. Tag version: `v{version}`
3. Release title: `{name} v{version}`
4. Upload: `{package_filename}`
5. Add checksums to release notes
6. Publish release

---
*Generated by Betty Framework plugin.publish skill*
"""

    release_notes_path = os.path.join(releases_dir, f"RELEASE_NOTES_v{version}.md")
    with open(release_notes_path, "w", encoding="utf-8") as f:
        f.write(release_notes)

    # Create release metadata
    release_metadata = {
        "prepared_at": datetime.now(timezone.utc).isoformat(),
        "target": "release",
        "version": version,
        "name": name,
        "package": {
            "filename": package_filename,
            "path": dest_path,
            "size_bytes": os.path.getsize(dest_path),
            "checksums": checksums
        },
        "release_notes_path": release_notes_path,
        "github_cli_command": f"gh release create v{version} --title \"{name} v{version}\" --notes-file {release_notes_path} {dest_path}",
        "metadata": metadata
    }

    metadata_path = os.path.join(
        releases_dir,
        f"{package_filename}.release.json"
    )

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(release_metadata, f, indent=2)

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
        "target": "release",
        "package_path": dest_path,
        "release_notes_path": release_notes_path,
        "metadata_path": metadata_path,
        "github_cli_command": release_metadata["github_cli_command"],
        "release_metadata": release_metadata
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
    remote_endpoint: Optional[str] = None
) -> Dict[str, Any]:
    """
    Publish a bundled plugin package.

    Args:
        package_path: Path to the .tar.gz package file
        target: Publication target - 'local', 'remote', or 'release'
        expected_sha256: Expected SHA256 checksum for validation (optional)
        manifest_path: Path to manifest.json (optional, auto-detected)
        remote_endpoint: Remote API endpoint for 'remote' target (optional)

    Returns:
        Dictionary with publication results
    """
    logger.info("=" * 80)
    logger.info("🚀 BETTY PLUGIN PUBLISH")
    logger.info("=" * 80)
    logger.info("")

    # Validate inputs
    if not os.path.exists(package_path):
        error_msg = f"Package file not found: {package_path}"
        logger.error(f"❌ {error_msg}")
        return {
            "ok": False,
            "error": error_msg
        }

    if target not in ["local", "remote", "release"]:
        error_msg = f"Invalid target: {target}. Must be 'local', 'remote', or 'release'"
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
                "license": manifest.get("license")
            }

    # Publish based on target
    if target == "local":
        result = publish_local(package_path, checksums, metadata)
    elif target == "remote":
        endpoint = remote_endpoint or "https://marketplace.claude.ai/api/v1/plugins"
        result = publish_remote(package_path, checksums, metadata, endpoint)
    elif target == "release":
        result = publish_release(package_path, checksums, metadata)

    logger.info("")
    logger.info("=" * 80)
    if result.get("ok"):
        logger.info("✅ PUBLICATION SUCCESSFUL")
    else:
        logger.info("❌ PUBLICATION FAILED")
    logger.info("=" * 80)

    return result


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Publish a bundled Betty plugin package"
    )
    parser.add_argument(
        "package_path",
        help="Path to the .tar.gz package file"
    )
    parser.add_argument(
        "--target",
        choices=["local", "remote", "release"],
        default="local",
        help="Publication target (default: local)"
    )
    parser.add_argument(
        "--sha256",
        help="Expected SHA256 checksum for validation"
    )
    parser.add_argument(
        "--manifest",
        help="Path to manifest.json"
    )
    parser.add_argument(
        "--endpoint",
        help="Remote API endpoint for 'remote' target"
    )

    args = parser.parse_args()

    result = publish_plugin(
        package_path=args.package_path,
        target=args.target,
        expected_sha256=args.sha256,
        manifest_path=args.manifest,
        remote_endpoint=args.endpoint
    )

    # Exit with appropriate code
    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
