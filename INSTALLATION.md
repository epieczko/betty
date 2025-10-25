# Betty Framework Installation Guide

Complete installation and setup instructions for the Betty Framework.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
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

## Installation

### Method 1: Clone from Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/betty.git
cd betty

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python3 -m betty.config
```

### Method 2: Download Release

```bash
# Download latest release
curl -L https://github.com/yourusername/betty/archive/refs/tags/v1.0.0.tar.gz -o betty.tar.gz

# Extract
tar -xzf betty.tar.gz
cd betty-1.0.0

# Install dependencies
pip install -r requirements.txt
```

### Python Dependencies

Betty requires the following Python packages (automatically installed with `requirements.txt`):

```
pyyaml>=6.0
jsonschema>=4.17.0
```

Install manually if needed:

```bash
pip install pyyaml jsonschema
```

## Configuration

### 1. Environment Setup

Add Betty to your Python path:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PYTHONPATH="${PYTHONPATH}:/path/to/betty"
export BETTY_HOME="/path/to/betty"
```

Apply changes:

```bash
source ~/.bashrc  # or ~/.zshrc
```

### 2. Claude Code Integration

If using with Claude Code, configure the plugin marketplace:

```bash
# Betty creates this automatically
cat .claude-plugin/marketplace.json
```

Example output:

```json
{
  "name": "Betty Framework",
  "version": "1.0.0",
  "description": "Plugin-based agent orchestration framework",
  "plugin_dir": ".claude-plugin",
  "plugins": []
}
```

### 3. Directory Structure

Betty uses the following directory structure:

```
betty/
├── agents/          # Agent definitions
├── skills/          # Skill implementations
├── docs/            # Documentation
├── schemas/         # JSON schemas
├── examples/        # Example components
├── tests/           # Test suites
├── betty/           # Core framework code
└── .claude-plugin/  # Claude Code integration
```

### 4. Configuration File (Optional)

Create `betty_config.yaml` for custom settings:

```yaml
# betty_config.yaml
betty:
  base_dir: /path/to/betty
  agents_dir: agents
  skills_dir: skills
  schemas_dir: schemas

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

meta_agents:
  enabled: true
  auto_register: true
```

## Verification

### 1. Verify Framework Installation

```bash
# Check Python imports
python3 -c "from betty.config import BASE_DIR; print(f'Betty installed at: {BASE_DIR}')"
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
python3 agents/meta.artifact/meta_artifact.py check agent-definition
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

python3 agents/meta.artifact/meta_artifact.py create /tmp/test_artifact.md
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
export PYTHONPATH="${PYTHONPATH}:/path/to/betty"

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
python3 --version  # Should be 3.8+
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
python3 skills/plugin.sync/plugin_sync.py
```

### Logs and Debugging

Enable debug logging:

```bash
# Set log level
export BETTY_LOG_LEVEL=DEBUG

# Run with verbose output
python3 agents/meta.artifact/meta_artifact.py create example.md --verbose
```

Check logs:

```bash
# Betty logs to stdout by default
# Redirect to file for debugging
python3 agents/meta.agent/meta_agent.py example.md 2>&1 | tee betty.log
```

## Platform-Specific Notes

### macOS

```bash
# Use Homebrew for dependencies
brew install python@3.11 git

# Add to .zshrc (default shell on macOS)
echo 'export PYTHONPATH="${PYTHONPATH}:/path/to/betty"' >> ~/.zshrc
source ~/.zshrc
```

### Linux (Ubuntu/Debian)

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip git

# Add to .bashrc
echo 'export PYTHONPATH="${PYTHONPATH}:/path/to/betty"' >> ~/.bashrc
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
- **Issues**: https://github.com/yourusername/betty/issues
- **Discussions**: https://github.com/yourusername/betty/discussions

## License

See [LICENSE](LICENSE) file for details.

---

**Installation complete!** Ready to build agents with Betty Framework.
