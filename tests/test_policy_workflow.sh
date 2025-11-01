#!/bin/bash
set -e

echo "=== End-to-End Policy Profile Workflow Test ==="
echo

export PYTHONPATH=/home/user/betty:$PYTHONPATH

# Step 1: Create a Markdown policy spec
echo "Step 1: Creating Markdown policy specification..."
cat > /tmp/test_policy.md <<'MD'
# Policy Profile: production

Production-ready policy with strict requirements.

## Rule 1: Require semantic versioning
field: version
pattern: ^\d+\.\d+\.\d+$
action: block

## Rule 2: No test status in production
field: status
forbidden_values: [test, experimental]
action: block

## Rule 3: Description is mandatory
check: description exists
action: warn

Metadata:
version: 2.0.0
environments: [prod]
status: active
tags: ["production", "strict"]
MD

echo "✓ Created policy spec"
echo

# Step 2: Use policy.define to generate YAML
echo "Step 2: Generating YAML policy profile..."
python3 skills/policy.define/policy_define.py /tmp/test_policy.md production \
  --type validation \
  --output registry/policies/production.yaml

echo "✓ Generated YAML profile"
echo

# Step 3: Validate the generated policy
echo "Step 3: Validating generated policy profile..."
python3 skills/policy.validate/policy_validate.py registry/policies/production.yaml

echo "✓ Policy validated successfully"
echo

# Step 4: Test enforcement with a good manifest
echo "Step 4: Testing enforcement with compliant manifest..."
cat > /tmp/good_manifest.yaml <<'YAML'
name: good.skill
version: 1.2.3
description: A well-formed skill manifest
status: active
YAML

python3 skills/policy.enforce/policy_enforce.py /tmp/good_manifest.yaml --profile production
echo "✓ Compliant manifest passed"
echo

# Step 5: Test enforcement with a bad manifest
echo "Step 5: Testing enforcement with non-compliant manifest..."
cat > /tmp/bad_manifest.yaml <<'YAML'
name: bad.skill
version: 1.0
status: experimental
YAML

set +e  # Allow failure
python3 skills/policy.enforce/policy_enforce.py /tmp/bad_manifest.yaml --profile production
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -ne 0 ]; then
    echo "✓ Non-compliant manifest correctly rejected"
else
    echo "✗ ERROR: Non-compliant manifest should have been rejected"
    exit 1
fi
echo

echo "=== All Tests Passed! ==="
echo
echo "Summary:"
echo "  ✓ Markdown → YAML conversion (policy.define)"
echo "  ✓ YAML validation (policy.validate)"
echo "  ✓ Profile-based enforcement (policy.enforce)"
echo "  ✓ Violation detection working"
