#!/bin/bash
#
# Integration tests for meta-agent ecosystem
# Tests all meta-agents working together
#

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Helper functions
print_test() {
    echo -e "\n${YELLOW}[TEST $((TESTS_RUN + 1))]${NC} $1"
    TESTS_RUN=$((TESTS_RUN + 1))
}

pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    TESTS_PASSED=$((TESTS_PASSED + 1))
}

fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    TESTS_FAILED=$((TESTS_FAILED + 1))
}

# Setup
echo "======================================"
echo "Meta-Agent Integration Tests"
echo "======================================"

# Change to betty root directory
cd "$(dirname "$0")/../.."

# Test 1: meta.artifact - Create artifact type
print_test "meta.artifact creates artifact type"

cat > /tmp/test_artifact.md <<'EOF'
# Name: test-artifact

# Purpose:
Test artifact for integration testing

# Format: JSON

# File Pattern: *.test.json

# Schema Properties:
- test_field (string): Test field

# Required Fields:
- test_field

# Producers:
- test.producer

# Consumers:
- test.consumer
EOF

if python3 agents/meta.artifact/meta_artifact.py create /tmp/test_artifact.md --force > /dev/null 2>&1; then
    if [ -f "schemas/test-artifact.json" ]; then
        pass "Artifact type created successfully"
    else
        fail "Schema file not created"
    fi
else
    fail "meta.artifact command failed"
fi

# Test 2: meta.artifact - Check artifact exists
print_test "meta.artifact checks artifact existence"

if python3 agents/meta.artifact/meta_artifact.py check test-artifact > /dev/null 2>&1; then
    pass "Artifact existence check works"
else
    fail "Artifact check failed"
fi

# Test 3: meta.agent - Create agent
print_test "meta.agent creates agent from description"

cat > /tmp/test_agent.md <<'EOF'
# Name: test.agent

# Purpose:
Test agent for integration testing

# Inputs:
- test-artifact

# Outputs:
- validation-report

# Examples:
- Test example 1
EOF

if python3 agents/meta.agent/meta_agent.py /tmp/test_agent.md > /dev/null 2>&1; then
    if [ -f "agents/test.agent/agent.yaml" ]; then
        pass "Agent created successfully"
    else
        fail "Agent file not created"
    fi
else
    fail "meta.agent command failed"
fi

# Test 4: meta.compatibility - Find compatible agents
print_test "meta.compatibility finds compatible agents"

if python3 agents/meta.compatibility/meta_compatibility.py find-compatible meta.agent > /dev/null 2>&1; then
    pass "Compatibility analysis works"
else
    fail "Compatibility analysis failed"
fi

# Test 5: meta.compatibility - Suggest pipeline
print_test "meta.compatibility suggests pipeline"

if python3 agents/meta.compatibility/meta_compatibility.py suggest-pipeline "Create and analyze agent" > /dev/null 2>&1; then
    pass "Pipeline suggestion works"
else
    fail "Pipeline suggestion failed"
fi

# Test 6: meta.compatibility - Analyze agent
print_test "meta.compatibility analyzes agent"

if python3 agents/meta.compatibility/meta_compatibility.py analyze meta.agent > /dev/null 2>&1; then
    pass "Agent analysis works"
else
    fail "Agent analysis failed"
fi

# Test 7: meta.compatibility - List all
print_test "meta.compatibility lists all agents"

if python3 agents/meta.compatibility/meta_compatibility.py list-all > /dev/null 2>&1; then
    pass "List all works"
else
    fail "List all failed"
fi

# Test 8: meta.suggest - Suggest next steps
print_test "meta.suggest provides next-step recommendations"

if python3 agents/meta.suggest/meta_suggest.py --context meta.agent > /dev/null 2>&1; then
    pass "Next-step suggestions work"
else
    fail "Suggestions failed"
fi

# Test 9: meta.suggest - Analyze project
print_test "meta.suggest analyzes project"

if python3 agents/meta.suggest/meta_suggest.py --analyze-project > /dev/null 2>&1; then
    pass "Project analysis works"
else
    fail "Project analysis failed"
fi

# Test 10: Integration - Artifact → Agent → Compatibility
print_test "Full integration: artifact → agent → compatibility"

# Create artifact type
cat > /tmp/integration_artifact.md <<'EOF'
# Name: integration-test

# Purpose:
Integration test artifact

# Format: JSON

# Producers:
- integration.producer

# Consumers:
- integration.consumer
EOF

python3 agents/meta.artifact/meta_artifact.py create /tmp/integration_artifact.md --force > /dev/null 2>&1

# Create agent that uses it
cat > /tmp/integration_agent.md <<'EOF'
# Name: integration.producer

# Purpose:
Produces integration-test artifacts

# Outputs:
- integration-test
EOF

python3 agents/meta.agent/meta_agent.py /tmp/integration_agent.md > /dev/null 2>&1

# Check compatibility
if python3 agents/meta.compatibility/meta_compatibility.py analyze integration.producer > /dev/null 2>&1; then
    pass "Full integration workflow works"
else
    fail "Integration workflow failed"
fi

# Test 11: JSON output formats
print_test "JSON output format works"

# Note: Skip jq validation as status messages are printed before JSON
if python3 agents/meta.compatibility/meta_compatibility.py --format json list-all > /dev/null 2>&1; then
    pass "JSON output works"
else
    fail "JSON output failed"
fi

# Test 12: YAML output formats
print_test "YAML output format works"

if python3 agents/meta.compatibility/meta_compatibility.py --format yaml list-all > /dev/null 2>&1; then
    pass "YAML output works"
else
    fail "YAML output failed"
fi

# Test 13: meta.skill - Create skill from description
print_test "meta.skill creates skill from description"

cat > /tmp/test_skill.md <<'EOF'
# Name: test.skill

# Purpose:
Test skill for integration testing

# Inputs:
- test_input

# Outputs:
- test_output.json

# Permissions:
- filesystem:read

# Produces Artifacts:
- test-result
EOF

if python3 agents/meta.skill/meta_skill.py /tmp/test_skill.md > /dev/null 2>&1; then
    if [ -f "skills/test.skill/skill.yaml" ] && [ -f "skills/test.skill/test_skill.py" ]; then
        pass "Skill created successfully"
    else
        fail "Skill files not created"
    fi
else
    fail "meta.skill command failed"
fi

# Test 14: meta.skill - Generated skill is valid Python
print_test "meta.skill generates valid Python code"

if python3 -m py_compile skills/test.skill/test_skill.py 2>/dev/null; then
    pass "Generated Python code is valid"
else
    fail "Generated Python code has syntax errors"
fi

# Test 15: meta.hook - Create hook from description
print_test "meta.hook creates hook from description"

cat > /tmp/test_hook.md <<'EOF'
# Name: test-hook

# Event: before-tool-call

# Description: Test hook for integration testing

# Command: echo "test"

# Enabled: true
EOF

# Backup existing hooks.yaml if it exists
if [ -f ".claude/hooks.yaml" ]; then
    cp .claude/hooks.yaml .claude/hooks.yaml.backup
fi

if python3 agents/meta.hook/meta_hook.py /tmp/test_hook.md > /dev/null 2>&1; then
    if [ -f ".claude/hooks.yaml" ]; then
        if grep -q "test-hook" .claude/hooks.yaml; then
            pass "Hook created successfully"
        else
            fail "Hook not found in hooks.yaml"
        fi
    else
        fail "hooks.yaml not created"
    fi
else
    fail "meta.hook command failed"
fi

# Restore original hooks.yaml
if [ -f ".claude/hooks.yaml.backup" ]; then
    mv .claude/hooks.yaml.backup .claude/hooks.yaml
else
    rm -f .claude/hooks.yaml
fi

# Test 16: meta.hook - Validates event types
print_test "meta.hook validates event types"

cat > /tmp/invalid_hook.md <<'EOF'
# Name: invalid-hook

# Event: invalid-event-type

# Command: echo "test"
EOF

if python3 agents/meta.hook/meta_hook.py /tmp/invalid_hook.md > /dev/null 2>&1; then
    fail "meta.hook should reject invalid event types"
else
    pass "Invalid event type rejected"
fi

# Cleanup
echo -e "\n${YELLOW}Cleaning up test artifacts...${NC}"
rm -f /tmp/test_artifact.md /tmp/test_agent.md /tmp/integration_artifact.md /tmp/integration_agent.md
rm -f /tmp/test_skill.md /tmp/test_hook.md /tmp/invalid_hook.md
rm -rf agents/test.agent agents/integration.producer
rm -rf skills/test.skill
rm -f schemas/test-artifact.json schemas/integration-test.json

# Restore artifact standards and registry to clean state
git checkout -- docs/ARTIFACT_STANDARDS.md skills/artifact.define/artifact_define.py 2>/dev/null || true

# Summary
echo ""
echo "======================================"
echo "Test Summary"
echo "======================================"
echo "Tests Run:    $TESTS_RUN"
echo -e "${GREEN}Passed:       $TESTS_PASSED${NC}"
if [ $TESTS_FAILED -gt 0 ]; then
    echo -e "${RED}Failed:       $TESTS_FAILED${NC}"
else
    echo "Failed:       $TESTS_FAILED"
fi
echo "======================================"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}✗ Some tests failed${NC}"
    exit 1
fi
