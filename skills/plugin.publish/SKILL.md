---
name: Plugin Publish
description: Publish bundled plugin packages to local, remote, or GitHub Releases targets
---

# plugin.publish

## Overview

**plugin.publish** is the publication tool that distributes your bundled Betty Framework plugin packages to various targets. It validates package integrity via SHA256 checksums and handles publication to local directories, remote Claude Marketplace endpoints, or GitHub Releases preparation.

## Purpose

Automates secure plugin distribution by:
- **Validating** SHA256 checksums to ensure package integrity
- **Publishing** to local directories for testing and archival
- **Simulating** remote API uploads to Claude Marketplace (with actual POST support ready)
- **Preparing** GitHub Releases with auto-generated release notes
- **Tracking** publication metadata for auditing and governance
- **Generating** installation instructions and verification commands

This ensures consistent, traceable, and secure plugin distribution across all deployment targets.

## What It Does

1. **Validates Package**: Verifies the .tar.gz file exists and is readable
2. **Calculates Checksums**: Computes MD5 and SHA256 hashes for integrity verification
3. **Validates SHA256**: Compares against expected checksum from manifest.json
4. **Loads Metadata**: Extracts plugin info from manifest.json (name, version, author, etc.)
5. **Publishes to Target**:
   - **Local**: Copies to `dist/published/` with metadata
   - **Remote**: Simulates POST to Claude Marketplace API (actual implementation ready)
   - **Release**: Prepares GitHub Release package with generated release notes
6. **Generates Metadata**: Creates publication records for auditing
7. **Reports Results**: Returns publication status with paths and checksums

## Usage

### Basic Usage (Local Target)

```bash
python skills/plugin.publish/plugin_publish.py dist/betty-framework-1.0.0.tar.gz
```

Publishes with defaults:
- Target: `local` (dist/published/)
- Checksum validation: Auto-detected from manifest.json

### Via Betty CLI

```bash
/plugin/publish dist/betty-framework-1.0.0.tar.gz
```

### Publish to Specific Target

```bash
# Publish to local directory
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=local

# Simulate remote publication
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote

# Prepare GitHub Release
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=release
```

### With Explicit Checksum Validation

```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=local \
  --sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### With Custom Manifest Path

```bash
python skills/plugin.publish/plugin_publish.py \
  /tmp/betty-framework-1.0.0.tar.gz \
  --target=release \
  --manifest=/tmp/manifest.json
```

### With Custom Remote Endpoint

```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote \
  --endpoint=https://api.example.com/plugins/upload
```

## Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `package_path` | Positional | Required | Path to the .tar.gz package file |
| `--target` | Option | `local` | Publication target: `local`, `remote`, or `release` |
| `--sha256` | Option | Auto-detect | Expected SHA256 checksum for validation |
| `--manifest` | Option | Auto-detect | Path to manifest.json |
| `--endpoint` | Option | Claude Marketplace | Remote API endpoint URL |

## Publication Targets

### Local Target

**Purpose**: Copy package to local published directory for testing, archival, or internal distribution.

**Output Location**: `dist/published/`

**Generated Files**:
- `{package-name}.tar.gz` - Copied package file
- `{package-name}.tar.gz.publish.json` - Publication metadata

**Use Cases**:
- Local testing before remote publication
- Internal company archives
- Offline distribution
- Backup copies

**Example**:
```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=local
```

**Output**:
```
dist/published/
├── betty-framework-1.0.0.tar.gz
└── betty-framework-1.0.0.tar.gz.publish.json
```

### Remote Target

**Purpose**: Upload package to Claude Marketplace API endpoint (simulated for now).

**Output Location**: `dist/published/simulations/`

**Generated Files**:
- `{package-name}.tar.gz.remote-publish.json` - Simulation log with request/response

**Use Cases**:
- Publish to Claude Code Marketplace
- Upload to custom plugin repository
- Submit to enterprise plugin registry

**Current Implementation**: SIMULATED
- Generates complete HTTP POST request structure
- Returns mock successful response
- No actual network request made
- Ready for real implementation (uncomment requests library usage)

**Example**:
```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote \
  --endpoint=https://marketplace.claude.ai/api/v1/plugins
```

**Simulated Request Structure**:
```json
{
  "method": "POST",
  "url": "https://marketplace.claude.ai/api/v1/plugins",
  "headers": {
    "Content-Type": "multipart/form-data",
    "X-Package-Name": "betty-framework",
    "X-Package-Version": "1.0.0",
    "X-Package-SHA256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "files": {
    "package": "betty-framework-1.0.0.tar.gz"
  },
  "data": {
    "name": "betty-framework",
    "version": "1.0.0",
    "description": "...",
    "checksums": { "md5": "...", "sha256": "..." }
  }
}
```

### Release Target

**Purpose**: Prepare package for GitHub Releases with auto-generated release notes.

**Output Location**: `dist/published/releases/`

**Generated Files**:
- `{package-name}.tar.gz` - Copied package file
- `RELEASE_NOTES_v{version}.md` - Auto-generated release notes
- `{package-name}.tar.gz.release.json` - Release metadata

**Use Cases**:
- GitHub Releases publication
- Public open-source distribution
- Versioned releases with changelog
- Official product releases

**Example**:
```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=release
```

**Output**:
```
dist/published/releases/
├── betty-framework-1.0.0.tar.gz
├── RELEASE_NOTES_v1.0.0.md
└── betty-framework-1.0.0.tar.gz.release.json
```

## Output Files

### Publication Metadata (Local Target)

**File**: `{package-name}.tar.gz.publish.json`

**Structure**:
```json
{
  "published_at": "2025-10-24T12:00:00.000000+00:00",
  "target": "local",
  "package": {
    "filename": "betty-framework-1.0.0.tar.gz",
    "path": "/home/user/betty/dist/published/betty-framework-1.0.0.tar.gz",
    "size_bytes": 524288,
    "checksums": {
      "md5": "d41d8cd98f00b204e9800998ecf8427e",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  },
  "metadata": {
    "name": "betty-framework",
    "version": "1.0.0",
    "description": "Betty Framework is RiskExec's system...",
    "author": {
      "name": "RiskExec",
      "email": "platform@riskexec.com"
    },
    "license": "MIT"
  }
}
```

### Remote Publication Simulation Log

**File**: `{package-name}.tar.gz.remote-publish.json`

**Structure**:
```json
{
  "simulated_at": "2025-10-24T12:00:00.000000+00:00",
  "target": "remote",
  "endpoint": "https://marketplace.claude.ai/api/v1/plugins",
  "request": {
    "method": "POST",
    "url": "...",
    "headers": { ... },
    "files": { ... },
    "data": { ... }
  },
  "response": {
    "status": 200,
    "response": {
      "ok": true,
      "message": "Plugin published successfully",
      "plugin_id": "betty-framework-1.0.0",
      "published_at": "2025-10-24T12:00:00.000000+00:00",
      "download_url": "...",
      "checksums": { ... }
    }
  },
  "note": "This is a simulated request. No actual HTTP request was made."
}
```

### GitHub Release Notes

**File**: `RELEASE_NOTES_v{version}.md`

**Auto-generated Content**:
```markdown
# betty-framework v1.0.0

## Release Information

- **Version:** 1.0.0
- **Released:** 2025-10-24
- **Package:** `betty-framework-1.0.0.tar.gz`

## Checksums

Verify the integrity of your download:

```
MD5:    d41d8cd98f00b204e9800998ecf8427e
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Installation

1. Download the package: `betty-framework-1.0.0.tar.gz`
2. Verify checksums (see above)
3. Extract: `tar -xzf betty-framework-1.0.0.tar.gz`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: Follow instructions in README.md

## Description

Betty Framework is RiskExec's system for structured, auditable AI-assisted engineering...

## GitHub CLI Commands

To create this release using GitHub CLI:

```bash
# Create release
gh release create v1.0.0 \
  --title "betty-framework v1.0.0" \
  --notes-file RELEASE_NOTES.md \
  betty-framework-1.0.0.tar.gz
```

## Manual Upload

1. Go to: https://github.com/YOUR_ORG/YOUR_REPO/releases/new
2. Tag version: `v1.0.0`
3. Release title: `betty-framework v1.0.0`
4. Upload: `betty-framework-1.0.0.tar.gz`
5. Add checksums to release notes
6. Publish release
```

### Release Metadata

**File**: `{package-name}.tar.gz.release.json`

**Structure**:
```json
{
  "prepared_at": "2025-10-24T12:00:00.000000+00:00",
  "target": "release",
  "version": "1.0.0",
  "name": "betty-framework",
  "package": {
    "filename": "betty-framework-1.0.0.tar.gz",
    "path": "/home/user/betty/dist/published/releases/betty-framework-1.0.0.tar.gz",
    "size_bytes": 524288,
    "checksums": {
      "md5": "...",
      "sha256": "..."
    }
  },
  "release_notes_path": "/home/user/betty/dist/published/releases/RELEASE_NOTES_v1.0.0.md",
  "github_cli_command": "gh release create v1.0.0 --title \"betty-framework v1.0.0\" --notes-file ...",
  "metadata": {
    "name": "betty-framework",
    "version": "1.0.0",
    "description": "...",
    "author": { ... },
    "license": "MIT"
  }
}
```

## Checksum Validation

### Automatic Validation

By default, `plugin.publish` automatically detects and validates checksums from `manifest.json`:

```bash
python skills/plugin.publish/plugin_publish.py dist/betty-framework-1.0.0.tar.gz
```

**Process**:
1. Looks for `dist/manifest.json`
2. Extracts `package.checksums.sha256`
3. Calculates actual SHA256 of package file
4. Compares and validates

### Manual Validation

Explicitly provide expected SHA256:

```bash
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### Validation Output

**Success**:
```
🔍 Validating package checksums...
🔐 Calculating checksums...
  MD5:    d41d8cd98f00b204e9800998ecf8427e
  SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
✅ SHA256 checksum validation: PASSED
```

**Failure**:
```
🔍 Validating package checksums...
🔐 Calculating checksums...
  MD5:    d41d8cd98f00b204e9800998ecf8427e
  SHA256: abc123...
❌ SHA256 checksum validation: FAILED
  Expected: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  Actual:   abc123...
```

## Workflow Integration

### Complete Build and Publish Pipeline

```bash
# Step 1: Build plugin
python skills/plugin.build/plugin_build.py

# Step 2: Publish to local for testing
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=local

# Step 3: Publish to remote marketplace
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote

# Step 4: Prepare GitHub Release
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=release

# Step 5: Create actual GitHub Release
cd dist/published/releases
gh release create v1.0.0 \
  --title "betty-framework v1.0.0" \
  --notes-file RELEASE_NOTES_v1.0.0.md \
  betty-framework-1.0.0.tar.gz
```

### Automated CI/CD Integration

```yaml
# .github/workflows/publish.yml
name: Publish Plugin

on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build plugin
        run: python skills/plugin.build/plugin_build.py

      - name: Validate and publish to remote
        run: |
          python skills/plugin.publish/plugin_publish.py \
            dist/betty-framework-*.tar.gz \
            --target=remote

      - name: Prepare GitHub Release
        run: |
          python skills/plugin.publish/plugin_publish.py \
            dist/betty-framework-*.tar.gz \
            --target=release

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/published/releases/*.tar.gz
          body_path: dist/published/releases/RELEASE_NOTES_*.md
```

## Error Handling

### Package Not Found

```
❌ Package file not found: /path/to/missing.tar.gz
```

**Solution**: Verify package path and run `plugin.build` first.

### Invalid Target

```
❌ Invalid target: prod. Must be 'local', 'remote', or 'release'
```

**Solution**: Use one of the valid target values.

### Checksum Validation Failed

```
❌ SHA256 checksum validation: FAILED
```

**Solution**: Package may be corrupted. Rebuild using `plugin.build`.

### Manifest Not Found

```
⚠️  Manifest not found: /path/to/manifest.json
⚠️  No expected checksum provided - skipping validation
```

**Solution**: Provide `--manifest` path or place manifest.json in package directory.

## Advanced Usage

### Publishing to Multiple Targets

```bash
#!/bin/bash
PACKAGE="dist/betty-framework-1.0.0.tar.gz"

# Publish to all targets
python skills/plugin.publish/plugin_publish.py "$PACKAGE" --target=local
python skills/plugin.publish/plugin_publish.py "$PACKAGE" --target=remote
python skills/plugin.publish/plugin_publish.py "$PACKAGE" --target=release

echo "Published to all targets successfully!"
```

### Custom Endpoint Configuration

```bash
# Development endpoint
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote \
  --endpoint=https://dev.marketplace.claude.ai/api/v1/plugins

# Production endpoint
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --target=remote \
  --endpoint=https://marketplace.claude.ai/api/v1/plugins
```

### Verification After Publication

```bash
# Local verification
cd dist/published
sha256sum -c <<< "e3b0c44... betty-framework-1.0.0.tar.gz"

# Extract and inspect
tar -tzf betty-framework-1.0.0.tar.gz | head -20

# Validate manifest
cat betty-framework-1.0.0.tar.gz.publish.json | jq .
```

## Dependencies

- **Python**: 3.11+
- **Standard Library**: os, sys, json, yaml, hashlib, shutil, pathlib, datetime
- **Betty Modules**: betty.config
- **Future**: requests (for actual remote publication)

## Related Skills

- **plugin.build**: Build plugin packages before publishing
- **plugin.sync**: Synchronize plugin.yaml from skill registry
- **registry.update**: Update skill registry entries
- **audit.log**: Log publication events for governance

## Security Considerations

### Checksum Validation

Always validate SHA256 checksums before publication:
- Detects package corruption
- Prevents tampering
- Ensures integrity across distribution channels

### Publication Tracking

All publications are logged with:
- Timestamp (UTC)
- Target destination
- Checksums
- Package metadata

This creates an audit trail for governance and compliance.

### Remote Publication (When Implemented)

For actual remote publication:
- Use HTTPS endpoints only
- Authenticate with API tokens (not in source code)
- Verify TLS certificates
- Implement retry logic with exponential backoff
- Log all API responses

## Troubleshooting

### Issue: Checksum mismatch after build

**Symptom**: SHA256 validation fails immediately after building

**Causes**:
- Manifest.json not generated by plugin.build
- Package file modified after build
- Incorrect manifest path

**Solution**:
```bash
# Rebuild package
python skills/plugin.build/plugin_build.py

# Verify manifest exists
ls -la dist/manifest.json

# Publish with explicit manifest
python skills/plugin.publish/plugin_publish.py \
  dist/betty-framework-1.0.0.tar.gz \
  --manifest=dist/manifest.json
```

### Issue: Remote publication not actually uploading

**Symptom**: No network error but file not on remote server

**Cause**: Remote publication is currently SIMULATED

**Solution**: This is expected behavior. The simulation creates a complete request structure in:
```
dist/published/simulations/{package}.remote-publish.json
```

For actual HTTP upload, uncomment the requests library implementation in `publish_remote()`.

### Issue: GitHub Release fails

**Symptom**: `gh release create` command fails

**Causes**:
- GitHub CLI not installed
- Not authenticated with GitHub
- Tag already exists
- No write access to repository

**Solutions**:
```bash
# Install GitHub CLI
# macOS: brew install gh
# Linux: sudo apt install gh

# Authenticate
gh auth login

# Check existing releases
gh release list

# Delete existing tag if needed
gh release delete v1.0.0
git push --delete origin v1.0.0
```

## Best Practices

1. **Always validate checksums** before publishing to remote or release targets
2. **Test locally first** using `--target=local` before remote publication
3. **Review release notes** in `dist/published/releases/RELEASE_NOTES_*.md` before GitHub Release
4. **Keep publication metadata** for audit trails and compliance
5. **Use version tags** consistently (e.g., v1.0.0 format)
6. **Automate via CI/CD** for consistent, reproducible releases
7. **Backup published packages** for disaster recovery

## Future Enhancements

- [ ] Actual HTTP POST implementation for remote target
- [ ] Support for multiple remote endpoints (marketplace, private registry)
- [ ] Automatic GitHub Release creation (without manual gh command)
- [ ] Digital signature support for package verification
- [ ] Publication rollback mechanism
- [ ] Automatic changelog generation from git commits
- [ ] Publication analytics and download tracking
- [ ] Multi-target parallel publication
- [ ] Package verification after publication

---

**Generated by**: Betty Framework
**Version**: 0.1.0
**Last Updated**: 2025-10-24
