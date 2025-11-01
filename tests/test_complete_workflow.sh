#!/bin/bash
set -e

echo "==================================="
echo "COMPLETE POLICY SYSTEM TEST"
echo "==================================="
echo

export PYTHONPATH=/home/user/betty:$PYTHONPATH

# Test 1: notify.human skill
echo "Test 1: notify.human skill..."
python3 skills/notify.human/notify_human.py \
  "Test notification from integration test" \
  --severity info \
  --action "No action needed - this is a test" > /dev/null
echo "✓ notify.human works"
echo

# Test 2: policy.define skill
echo "Test 2: policy.define skill..."
cat > /tmp/integration_test_policy.md <<'MD'
# Policy Profile: integration-test

## Rule 1: Test rule
field: test_field
required: true
action: block

Metadata:
version: 1.0.0
MD

python3 skills/policy.define/policy_define.py \
  /tmp/integration_test_policy.md integration-test \
  --output /tmp/integration-test.yaml > /dev/null
echo "✓ policy.define works"
echo

# Test 3: policy.validate skill
echo "Test 3: policy.validate skill..."
python3 skills/policy.validate/policy_validate.py \
  /tmp/integration-test.yaml > /dev/null
echo "✓ policy.validate works"
echo

# Test 4: policy.enforce with profile
echo "Test 4: policy.enforce with profile..."
cat > /tmp/test_manifest.yaml <<'YAML'
name: test.manifest
version: 1.0.0
description: Test manifest
status: active
YAML

python3 skills/policy.enforce/policy_enforce.py \
  /tmp/test_manifest.yaml \
  --profile default > /dev/null
echo "✓ policy.enforce with profile works"
echo

# Test 5: meta.policy.profile agent
echo "Test 5: meta.policy.profile agent orchestration..."
python3 agents/meta.policy.profile/meta_policy_profile.py \
  integration-test-2 \
  /tmp/integration_test_policy.md \
  --type validation > /dev/null
echo "✓ meta.policy.profile agent works"
echo

# Test 6: End-to-end with meta-agent
echo "Test 6: Complete workflow via meta-agent..."
cat > /tmp/e2e_policy.md <<'MD'
# Policy Profile: e2e-test

## Rule 1: Version required
check: version exists
action: block

## Rule 2: Description required
check: description exists
action: warn

Metadata:
version: 2.0.0
tags: ["e2e", "test"]
MD

RESULT=$(python3 agents/meta.policy.profile/meta_policy_profile.py \
  e2e-test \
  /tmp/e2e_policy.md \
  --type validation)

if echo "$RESULT" | grep -q '"success": true'; then
    echo "✓ End-to-end workflow via meta-agent successful"
else
    echo "✗ End-to-end workflow failed"
    echo "$RESULT"
    exit 1
fi
echo

# Test 7: Verify generated profiles
echo "Test 7: Verifying generated policy profiles..."
# Test 2 output to /tmp, tests 5 & 6 output to registry/policies
if [ -f "/tmp/integration-test.yaml" ]; then
    echo "✓ Profile integration-test.yaml created (via policy.define)"
else
    echo "✗ Profile integration-test.yaml NOT found"
    exit 1
fi

for profile in integration-test-2 e2e-test; do
    if [ -f "registry/policies/${profile}.yaml" ]; then
        echo "✓ Profile ${profile}.yaml created (via meta-agent)"
    else
        echo "✗ Profile ${profile}.yaml NOT found"
        exit 1
    fi
done
echo

# Test 8: Enforce a generated policy
echo "Test 8: Enforcing a generated policy..."
cat > /tmp/bad_manifest.yaml <<'YAML'
name: bad.manifest
status: active
YAML

set +e
python3 skills/policy.enforce/policy_enforce.py \
  /tmp/bad_manifest.yaml \
  --profile e2e-test 2>&1 | grep -q "violation"
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -eq 0 ]; then
    echo "✓ Policy enforcement correctly detected violations"
else
    echo "✗ Policy enforcement did not detect expected violations"
    exit 1
fi
echo

# Clean up
rm -f /tmp/integration_test_policy.md /tmp/integration-test.yaml
rm -f /tmp/test_manifest.yaml /tmp/e2e_policy.md /tmp/bad_manifest.yaml

echo "==================================="
echo "ALL TESTS PASSED! ✓"
echo "==================================="
echo
echo "Summary:"
echo "  ✓ notify.human skill"
echo "  ✓ policy.define skill"
echo "  ✓ policy.validate skill"
echo "  ✓ policy.enforce with profiles"
echo "  ✓ meta.policy.profile agent"
echo "  ✓ End-to-end workflow"
echo "  ✓ Generated profiles verified"
echo "  ✓ Policy enforcement working"
echo
echo "The complete policy compliance system is operational!"
