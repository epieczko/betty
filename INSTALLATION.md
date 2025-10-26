# Betty Framework Installation Guide

Complete installation and setup instructions for the Betty Framework.

## Table of Contents

- [System Requirements](#system-requirements)
- [Canonical Setup](#canonical-setup)
  - [Linux and macOS](#linux-and-macos)
  - [Windows (PowerShell)](#windows-powershell)
  - [Persist Environment Variables (Optional)](#persist-environment-variables-optional)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)

## System Requirements

### Required

- **Python**: 3.8 or higher
- **Git**: 2.20 or higher
- **Operating System**: Linux, macOS, or Windows (WSL recommended)

### Optional

- **Claude Code CLI**: For Claude Code integration
- **pytest**: For running tests
- **npm**: For JavaScript/TypeScript skills (if needed)

### Disk Space

- Minimum: 50 MB (framework only)
- Recommended: 200 MB (with examples and documentation)

## Canonical Setup

The commands below are the single source of truth for setting up a local Betty development environment. Every other guide in the repository links back to this sequence—if you keep these steps up to date, the rest of the documentation stays consistent.

Replace `https://github.com/your-org/betty.git` with the URL of your fork or the repository you intend to use.

### Linux and macOS

```bash
# 1. Clone the repository
git clone https://github.com/your-org/betty.git
cd betty

# 2. (Recommended) Create an isolated Python environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Configure environment variables for the current shell
export BETTY_HOME="$(pwd)"
export PYTHONPATH="${PYTHONPATH}:${BETTY_HOME}"

# 5. Verify the installation
python -m betty.validation
```

### Windows (PowerShell)

```powershell
# 1. Clone the repository
git clone https://github.com/your-org/betty.git
cd betty

# 2. (Recommended) Create an isolated Python environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Configure environment variables for the current session
$env:BETTY_HOME = (Get-Location)
$env:PYTHONPATH = "$env:PYTHONPATH;$env:BETTY_HOME"

# 5. Verify the installation
python -m betty.validation
```

### Persist Environment Variables (Optional)

Persisting the environment variables prevents you from having to set them on every new shell session.

**Linux/macOS:**

```bash
echo 'export BETTY_HOME="/absolute/path/to/betty"' >> ~/.bashrc   # or ~/.zshrc
echo 'export PYTHONPATH="${PYTHONPATH}:${BETTY_HOME}"' >> ~/.bashrc
```

Reload your shell profile afterwards:

```bash
source ~/.bashrc  # or ~/.zshrc
```

**Windows (PowerShell):**

```powershell
[System.Environment]::SetEnvironmentVariable("BETTY_HOME", (Get-Location), "User")
$existingPath = [System.Environment]::GetEnvironmentVariable("PYTHONPATH", "User")
[System.Environment]::SetEnvironmentVariable(
    "PYTHONPATH",
    "$existingPath;$((Get-Location).Path)",
    "User"
)
```

Restart PowerShell to load the new values.

---

## Verification

After completing the canonical setup, you can run additional checks to make sure your environment is healthy.

### 1. Verify Framework Installation

```bash
# Check Python imports
python -c "from betty.config import BASE_DIR; print(f'Betty installed at: {BASE_DIR}')"
```

Expected output:
```
Betty installed at: /path/to/betty
```

### 2. Verify Meta-Agents

```bash
# List all meta-agents
ls -la agents/meta.*/

# Test meta.artifact
python agents/meta.artifact/meta_artifact.py check agent-definition
```

Expected output:
```
✅ Artifact type 'agent-definition' exists
```

### 3. Run Integration Tests

```bash
# Run full test suite
bash tests/integration/test_meta_agents.sh
```

Expected output:
```
======================================
Test Summary
======================================
Tests Run:    16
Passed:       16
Failed:       0
======================================
✓ All tests passed!
```

### 4. Test Meta-Agent Creation

```bash
# Create a test artifact type
cat > /tmp/test_artifact.md <<'EOF'
# Name: test-type
# Purpose: Test artifact
# Format: JSON
# File Pattern: *.test.json
# Producers: test.agent
# Consumers: test.consumer
EOF

python agents/meta.artifact/meta_artifact.py create /tmp/test_artifact.md
```

Expected output:
```
✨ Artifact type 'test-type' created successfully!
```

## Troubleshooting

### Common Issues

#### 1. Import Error: "No module named 'betty'"

**Problem**: Python can't find Betty module

**Solution**:
```bash
# Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${BETTY_HOME:-/path/to/betty}"

# Or install in development mode
cd /path/to/betty
pip install -e .
```

#### 2. Permission Denied

**Problem**: Can't execute Python scripts

**Solution**:
```bash
# Make scripts executable
chmod +x agents/*/**.py
chmod +x tests/**/*.sh
```

#### 3. YAML/JSON Schema Errors

**Problem**: Schema validation fails

**Solution**:
```bash
# Verify dependencies
pip install --upgrade pyyaml jsonschema

# Check Python version
python --version  # Should be 3.8+
```

#### 4. Tests Fail

**Problem**: Integration tests don't pass

**Solution**:
```bash
# Clean test artifacts
rm -rf agents/test.* skills/test.* schemas/test-*.json

# Restore clean state
git checkout -- docs/ARTIFACT_STANDARDS.md skills/artifact.define/artifact_define.py

# Run tests again
bash tests/integration/test_meta_agents.sh
```

#### 5. Claude Code Integration Issues

**Problem**: Claude Code doesn't recognize Betty

**Solution**:
```bash
# Verify marketplace.json exists
cat .claude-plugin/marketplace.json

# Regenerate if needed
python skills/plugin.sync/plugin_sync.py
```

### Logs and Debugging

Enable debug logging:

```bash
# Set log level
export BETTY_LOG_LEVEL=DEBUG

# Run with verbose output
python agents/meta.artifact/meta_artifact.py create example.md --verbose
```

Check logs:

```bash
# Betty logs to stdout by default
# Redirect to file for debugging
python agents/meta.agent/meta_agent.py example.md 2>&1 | tee betty.log
```

## Platform-Specific Notes

### macOS

```bash
# Use Homebrew for dependencies
brew install python@3.11 git

# Add to .zshrc (default shell on macOS)
echo 'export BETTY_HOME="/absolute/path/to/betty"' >> ~/.zshrc
echo 'export PYTHONPATH="${PYTHONPATH}:${BETTY_HOME}"' >> ~/.zshrc
source ~/.zshrc
```

### Linux (Ubuntu/Debian)

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip git

# Add to .bashrc
echo 'export BETTY_HOME="/absolute/path/to/betty"' >> ~/.bashrc
echo 'export PYTHONPATH="${PYTHONPATH}:${BETTY_HOME}"' >> ~/.bashrc
source ~/.bashrc
```

### Windows (WSL)

```bash
# Use WSL2 with Ubuntu
wsl --install

# Inside WSL, follow Linux instructions above
```

## Updating Betty

### Pull Latest Changes

```bash
cd /path/to/betty
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Run tests to verify
bash tests/integration/test_meta_agents.sh
```

### Version Check

```bash
# Check current version
cat .claude-plugin/marketplace.json | grep version
```

## Uninstallation

### Remove Betty Framework

```bash
# Remove directory
rm -rf /path/to/betty

# Remove from PYTHONPATH (edit ~/.bashrc or ~/.zshrc)
# Remove line: export PYTHONPATH="${PYTHONPATH}:/path/to/betty"

# Uninstall Python dependencies (if not used elsewhere)
pip uninstall pyyaml jsonschema
```

### Clean Configuration

```bash
# Remove Claude Code integration
rm -rf ~/.claude/betty

# Remove any custom config
rm -f ~/betty_config.yaml
```

## Next Steps

After successful installation:

1. **Read Getting Started Guide**: [GETTING_STARTED.md](GETTING_STARTED.md)
2. **Explore Meta-Agents**: [docs/META_AGENTS.md](docs/META_AGENTS.md)
3. **Review Examples**: [examples/](examples/)
4. **Run Tutorials**: Follow tutorials in META_AGENTS.md

## Support

- **Documentation**: [docs/](docs/)
- **Issues**: https://github.com/your-org/betty/issues
- **Discussions**: https://github.com/your-org/betty/discussions

## License

See [LICENSE](LICENSE) file for details.

---

**Installation complete!** Ready to build agents with Betty Framework.
