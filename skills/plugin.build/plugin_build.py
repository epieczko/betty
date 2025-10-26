#!/usr/bin/env python3
"""
plugin_build.py - Implementation of the plugin.build Skill
Bundles plugin directory into a deployable Claude Code plugin package.
"""

import os
import sys
import json
import yaml
import tarfile
import zipfile
import hashlib
import shutil
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone
from pathlib import Path
from pydantic import ValidationError as PydanticValidationError

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.telemetry_capture import capture_skill_execution
from betty.models import PluginManifest
from utils.telemetry_utils import capture_telemetry

logger = setup_logger(__name__)


def load_plugin_yaml(plugin_path: str) -> Dict[str, Any]:
    """
    Load and parse plugin.yaml file.

    Args:
        plugin_path: Path to plugin.yaml

    Returns:
        Parsed plugin configuration

    Raises:
        FileNotFoundError: If plugin.yaml doesn't exist
        yaml.YAMLError: If YAML is invalid
        ValueError: If schema validation fails
    """
    try:
        with open(plugin_path) as f:
            config = yaml.safe_load(f)

        # Validate with Pydantic schema
        try:
            PluginManifest.model_validate(config)
            logger.info(f"✅ Loaded and validated plugin.yaml from {plugin_path}")
        except PydanticValidationError as exc:
            errors = []
            for error in exc.errors():
                field = ".".join(str(loc) for loc in error["loc"])
                message = error["msg"]
                errors.append(f"{field}: {message}")
            error_msg = f"Plugin schema validation failed: {'; '.join(errors)}"
            logger.error(f"❌ {error_msg}")
            raise ValueError(error_msg)

        return config
    except FileNotFoundError:
        logger.error(f"❌ plugin.yaml not found: {plugin_path}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"❌ Invalid YAML in {plugin_path}: {e}")
        raise


def validate_entrypoints(config: Dict[str, Any], base_dir: str) -> Tuple[List[Dict], List[str]]:
    """
    Validate that all entrypoint handlers exist on disk.

    Args:
        config: Plugin configuration
        base_dir: Base directory for the plugin

    Returns:
        Tuple of (valid_entrypoints, missing_files)
    """
    valid_entrypoints = []
    missing_files = []

    commands = config.get("commands", [])
    logger.info(f"📝 Validating {len(commands)} command entrypoints...")

    for command in commands:
        name = command.get("name", "unknown")
        handler = command.get("handler", {})
        script_path = handler.get("script", "")

        if not script_path:
            missing_files.append(f"Command '{name}': no handler script specified")
            continue

        full_path = os.path.join(base_dir, script_path)

        if os.path.exists(full_path):
            valid_entrypoints.append({
                "command": name,
                "handler": script_path,
                "runtime": handler.get("runtime", "python"),
                "path": full_path
            })
            logger.debug(f"  ✅ {name}: {script_path}")
        else:
            missing_files.append(f"Command '{name}': handler not found at {script_path}")
            logger.warning(f"  ❌ {name}: {script_path} (not found)")

    return valid_entrypoints, missing_files


def gather_package_files(config: Dict[str, Any], base_dir: str) -> List[Tuple[str, str]]:
    """
    Gather all files that need to be included in the package.

    Args:
        config: Plugin configuration
        base_dir: Base directory for the plugin

    Returns:
        List of (source_path, archive_path) tuples
    """
    files_to_package = []

    # Always include plugin.yaml
    plugin_yaml_path = os.path.join(base_dir, "plugin.yaml")
    if os.path.exists(plugin_yaml_path):
        files_to_package.append((plugin_yaml_path, "plugin.yaml"))
        logger.debug("  + plugin.yaml")

    # Gather all skill directories from commands
    skill_dirs = set()
    commands = config.get("commands", [])

    for command in commands:
        handler = command.get("handler", {})
        script_path = handler.get("script", "")

        if script_path.startswith("skills/"):
            # Extract skill directory (e.g., "skills/api.validate" from "skills/api.validate/api_validate.py")
            parts = script_path.split("/")
            if len(parts) >= 2:
                skill_dir = f"{parts[0]}/{parts[1]}"
                skill_dirs.add(skill_dir)

    # Add all files from skill directories
    logger.info(f"📦 Gathering files from {len(skill_dirs)} skill directories...")
    for skill_dir in sorted(skill_dirs):
        skill_path = os.path.join(base_dir, skill_dir)
        if os.path.isdir(skill_path):
            for root, dirs, files in os.walk(skill_path):
                # Skip __pycache__ and .pyc files
                dirs[:] = [d for d in dirs if d != "__pycache__"]

                for file in files:
                    if file.endswith(".pyc") or file.startswith("."):
                        continue

                    source_path = os.path.join(root, file)
                    rel_path = os.path.relpath(source_path, base_dir)
                    files_to_package.append((source_path, rel_path))
                    logger.debug(f"  + {rel_path}")

    # Add betty/ utility package
    betty_dir = os.path.join(base_dir, "betty")
    if os.path.isdir(betty_dir):
        logger.info("📦 Adding betty/ utility package...")
        for root, dirs, files in os.walk(betty_dir):
            dirs[:] = [d for d in dirs if d != "__pycache__"]

            for file in files:
                if file.endswith(".pyc") or file.startswith("."):
                    continue

                source_path = os.path.join(root, file)
                rel_path = os.path.relpath(source_path, base_dir)
                files_to_package.append((source_path, rel_path))
                logger.debug(f"  + {rel_path}")

    # Add registry/ files
    registry_dir = os.path.join(base_dir, "registry")
    if os.path.isdir(registry_dir):
        logger.info("📦 Adding registry/ files...")
        for file in os.listdir(registry_dir):
            if file.endswith(".json"):
                source_path = os.path.join(registry_dir, file)
                rel_path = f"registry/{file}"
                files_to_package.append((source_path, rel_path))
                logger.debug(f"  + {rel_path}")

    # Add optional files if they exist
    optional_files = [
        "requirements.txt",
        "README.md",
        "LICENSE",
        "CHANGELOG.md"
    ]

    for filename in optional_files:
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            files_to_package.append((file_path, filename))
            logger.debug(f"  + {filename}")

    logger.info(f"📦 Total files to package: {len(files_to_package)}")
    return files_to_package


def create_tarball(files: List[Tuple[str, str]], output_path: str, plugin_name: str) -> str:
    """
    Create a .tar.gz archive.

    Args:
        files: List of (source_path, archive_path) tuples
        output_path: Output directory
        plugin_name: Base name for the archive

    Returns:
        Path to created archive
    """
    archive_path = os.path.join(output_path, f"{plugin_name}.tar.gz")

    logger.info(f"🗜️  Creating tar.gz archive: {archive_path}")

    with tarfile.open(archive_path, "w:gz") as tar:
        for source_path, archive_path_in_tar in files:
            # Add files with plugin name prefix
            arcname = f"{plugin_name}/{archive_path_in_tar}"
            tar.add(source_path, arcname=arcname)
            logger.debug(f"  Added: {arcname}")

    return archive_path


def create_zip(files: List[Tuple[str, str]], output_path: str, plugin_name: str) -> str:
    """
    Create a .zip archive.

    Args:
        files: List of (source_path, archive_path) tuples
        output_path: Output directory
        plugin_name: Base name for the archive

    Returns:
        Path to created archive
    """
    archive_path = os.path.join(output_path, f"{plugin_name}.zip")

    logger.info(f"🗜️  Creating zip archive: {archive_path}")

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for source_path, archive_path_in_zip in files:
            # Add files with plugin name prefix
            arcname = f"{plugin_name}/{archive_path_in_zip}"
            zf.write(source_path, arcname=arcname)
            logger.debug(f"  Added: {arcname}")

    return archive_path


def calculate_checksum(file_path: str) -> Dict[str, str]:
    """
    Calculate checksums for the package file.

    Args:
        file_path: Path to the package file

    Returns:
        Dictionary with md5 and sha256 checksums
    """
    logger.info("🔐 Calculating checksums...")

    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
            sha256_hash.update(chunk)

    checksums = {
        "md5": md5_hash.hexdigest(),
        "sha256": sha256_hash.hexdigest()
    }

    logger.info(f"  MD5:    {checksums['md5']}")
    logger.info(f"  SHA256: {checksums['sha256']}")

    return checksums


def generate_build_report(
    config: Dict[str, Any],
    valid_entrypoints: List[Dict],
    missing_files: List[str],
    package_path: str,
    checksums: Dict[str, str],
    files_count: int
) -> Dict[str, Any]:
    """
    Generate build report JSON.

    Args:
        config: Plugin configuration
        valid_entrypoints: List of validated entrypoints
        missing_files: List of missing files
        package_path: Path to created package
        checksums: Package checksums
        files_count: Number of files packaged

    Returns:
        Build report dictionary
    """
    file_size = os.path.getsize(package_path)

    report = {
        "build_timestamp": datetime.now(timezone.utc).isoformat(),
        "plugin": {
            "name": config.get("name"),
            "version": config.get("version"),
            "description": config.get("description")
        },
        "validation": {
            "total_commands": len(config.get("commands", [])),
            "valid_entrypoints": len(valid_entrypoints),
            "missing_files": missing_files,
            "has_errors": len(missing_files) > 0
        },
        "package": {
            "path": package_path,
            "size_bytes": file_size,
            "size_human": f"{file_size / 1024 / 1024:.2f} MB" if file_size > 1024 * 1024 else f"{file_size / 1024:.2f} KB",
            "files_count": files_count,
            "format": "tar.gz" if package_path.endswith(".tar.gz") else "zip",
            "checksums": checksums
        },
        "entrypoints": valid_entrypoints
    }

    return report


def generate_manifest(
    config: Dict[str, Any],
    valid_entrypoints: List[Dict],
    checksums: Dict[str, str],
    package_path: str
) -> Dict[str, Any]:
    """
    Generate manifest.json for the plugin package.

    Args:
        config: Plugin configuration
        valid_entrypoints: List of validated entrypoints
        checksums: Package checksums
        package_path: Path to created package

    Returns:
        Manifest dictionary
    """
    file_size = os.path.getsize(package_path)
    package_filename = os.path.basename(package_path)

    manifest = {
        "name": config.get("name"),
        "version": config.get("version"),
        "description": config.get("description"),
        "author": config.get("author", {}),
        "license": config.get("license"),
        "metadata": {
            "homepage": config.get("metadata", {}).get("homepage"),
            "repository": config.get("metadata", {}).get("repository"),
            "documentation": config.get("metadata", {}).get("documentation"),
            "tags": config.get("metadata", {}).get("tags", []),
            "generated_at": datetime.now(timezone.utc).isoformat()
        },
        "requirements": {
            "python": config.get("requirements", {}).get("python"),
            "packages": config.get("requirements", {}).get("packages", [])
        },
        "permissions": config.get("permissions", []),
        "package": {
            "filename": package_filename,
            "size_bytes": file_size,
            "checksums": checksums
        },
        "entrypoints": [
            {
                "command": ep["command"],
                "handler": ep["handler"],
                "runtime": ep["runtime"]
            }
            for ep in valid_entrypoints
        ],
        "commands_count": len(valid_entrypoints),
        "agents": [
            {
                "name": agent.get("name"),
                "description": agent.get("description")
            }
            for agent in config.get("agents", [])
        ]
    }

    return manifest


def create_plugin_preview(config: Dict[str, Any], output_path: str) -> Optional[str]:
    """
    Create plugin.preview.yaml with current plugin configuration.
    This allows reviewing changes before overwriting plugin.yaml.

    Args:
        config: Plugin configuration
        output_path: Directory to write preview file

    Returns:
        Path to preview file or None if creation failed
    """
    try:
        preview_path = os.path.join(output_path, "plugin.preview.yaml")

        # Add preview metadata
        preview_config = config.copy()
        if "metadata" not in preview_config:
            preview_config["metadata"] = {}

        preview_config["metadata"]["preview_generated_at"] = datetime.now(timezone.utc).isoformat()
        preview_config["metadata"]["preview_note"] = "Review before applying to plugin.yaml"

        with open(preview_path, "w") as f:
            yaml.dump(preview_config, f, default_flow_style=False, sort_keys=False)

        logger.info(f"📋 Preview file created: {preview_path}")
        return preview_path

    except Exception as e:
        logger.warning(f"⚠️  Failed to create preview file: {e}")
        return None


def build_plugin(
    plugin_path: str = None,
    output_format: str = "tar.gz",
    output_dir: str = None
) -> Dict[str, Any]:
    """
    Main build function.

    Args:
        plugin_path: Path to plugin.yaml (defaults to ./plugin.yaml)
        output_format: Package format (tar.gz or zip)
        output_dir: Output directory (defaults to ./dist)

    Returns:
        Build result dictionary
    """
    # Track execution time for telemetry
    start_time = datetime.now(timezone.utc)

    # Set defaults
    if plugin_path is None:
        plugin_path = os.path.join(BASE_DIR, "plugin.yaml")

    if output_dir is None:
        output_dir = os.path.join(BASE_DIR, "dist")

    # Normalize format
    output_format = output_format.lower()
    if output_format not in ["tar.gz", "zip"]:
        raise ValueError(f"Unsupported output format: {output_format}. Use 'tar.gz' or 'zip'")

    logger.info("🏗️  Starting plugin build...")
    logger.info(f"📄 Plugin: {plugin_path}")
    logger.info(f"📦 Format: {output_format}")
    logger.info(f"📁 Output: {output_dir}")

    # Load plugin.yaml
    config = load_plugin_yaml(plugin_path)

    # Get base directory (parent of plugin.yaml)
    base_dir = os.path.dirname(os.path.abspath(plugin_path))

    # Validate entrypoints
    valid_entrypoints, missing_files = validate_entrypoints(config, base_dir)

    if missing_files:
        logger.warning(f"⚠️  Found {len(missing_files)} missing files:")
        for missing in missing_files:
            logger.warning(f"  - {missing}")

    # Gather files to package
    files_to_package = gather_package_files(config, base_dir)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Generate package name
    plugin_name = config.get("name", "plugin")
    plugin_version = config.get("version", "1.0.0")
    package_basename = f"{plugin_name}-{plugin_version}"

    # Create package
    if output_format == "tar.gz":
        package_path = create_tarball(files_to_package, output_dir, package_basename)
    else:
        package_path = create_zip(files_to_package, output_dir, package_basename)

    # Calculate checksums
    checksums = calculate_checksum(package_path)

    # Generate build report
    build_report = generate_build_report(
        config,
        valid_entrypoints,
        missing_files,
        package_path,
        checksums,
        len(files_to_package)
    )

    # Write build report JSON
    report_path = os.path.join(output_dir, f"{package_basename}-build-report.json")
    with open(report_path, "w") as f:
        json.dump(build_report, f, indent=2)

    logger.info(f"📊 Build report: {report_path}")

    # Generate and write manifest.json
    manifest = generate_manifest(config, valid_entrypoints, checksums, package_path)
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    logger.info(f"📋 Manifest: {manifest_path}")

    # Create plugin preview (optional)
    preview_path = create_plugin_preview(config, output_dir)

    # Build result
    result = {
        "ok": not build_report["validation"]["has_errors"],
        "status": "success" if not missing_files else "success_with_warnings",
        "package_path": package_path,
        "report_path": report_path,
        "manifest_path": manifest_path,
        "preview_path": preview_path,
        "build_report": build_report,
        "manifest": manifest
    }

    # Calculate execution duration and capture telemetry
    end_time = datetime.now(timezone.utc)
    duration_ms = int((end_time - start_time).total_seconds() * 1000)

    capture_skill_execution(
        skill_name="plugin.build",
        inputs={
            "plugin_path": plugin_path,
            "output_format": output_format,
            "output_dir": output_dir
        },
        status="success" if result["ok"] else "success_with_warnings",
        duration_ms=duration_ms,
        caller="cli",
        plugin_name=config.get("name"),
        plugin_version=config.get("version"),
        files_count=len(files_to_package),
        package_size_bytes=os.path.getsize(package_path),
        warnings_count=len(missing_files)
    )

    return result


@capture_telemetry(skill_name="plugin.build", caller="cli")
def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Build deployable Claude Code plugin package"
    )
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=None,
        help="Path to plugin.yaml (defaults to ./plugin.yaml)"
    )
    parser.add_argument(
        "--format",
        choices=["tar.gz", "zip"],
        default="tar.gz",
        help="Package format (default: tar.gz)"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory (default: ./dist)"
    )

    args = parser.parse_args()

    try:
        result = build_plugin(
            plugin_path=args.plugin_path,
            output_format=args.format,
            output_dir=args.output_dir
        )

        # Print summary
        report = result["build_report"]
        logger.info("\n" + "=" * 60)
        logger.info("🎉 BUILD COMPLETE")
        logger.info("=" * 60)
        logger.info(f"📦 Package:  {result['package_path']}")
        logger.info(f"📊 Report:   {result['report_path']}")
        logger.info(f"📋 Manifest: {result['manifest_path']}")
        if result.get('preview_path'):
            logger.info(f"👁️  Preview:  {result['preview_path']}")
        logger.info(f"✅ Commands: {report['validation']['valid_entrypoints']}/{report['validation']['total_commands']}")
        logger.info(f"📏 Size:     {report['package']['size_human']}")
        logger.info(f"📝 Files:    {report['package']['files_count']}")

        if report["validation"]["missing_files"]:
            logger.warning(f"⚠️  Warnings: {len(report['validation']['missing_files'])}")

        logger.info("=" * 60)

        print(json.dumps(result, indent=2))
        sys.exit(0 if result["ok"] else 1)

    except Exception as e:
        logger.error(f"❌ Build failed: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
