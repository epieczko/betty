# Policy: Validate Profile YAML

Validate a policy profile YAML file for correctness.

## What to do:

1. **Run validation**:
   - Execute: `python skills/policy.validate/policy_validate.py <policy-file-path> [--strict]`
   - Use --strict flag for production profiles (treats warnings as errors)
   - Output is JSON format

2. **Parse validation results**:
   - Check: valid (true/false)
   - Extract: errors[], warnings[], rule_count, message

3. **Display results clearly**:

   **If valid: true**:
   ```
   ✓ Policy YAML is valid

   Profile: <name>
   Type: <type>
   Rules: <count>
   Scope: <scopes>
   Enforcement: <level>
   ```

   **If valid: false**:
   ```
   ✗ Policy YAML validation failed

   Errors:
   🔴 <error message 1>
   🔴 <error message 2>

   Warnings:
   ⚠️  <warning message 1>
   ```

4. **Provide guidance**:
   - Explain each error in clear terms
   - Show the YAML structure expected
   - Point to examples from existing profiles:
     - `registry/policies/betty-core.yaml` (comprehensive)
     - `registry/policies/default.yaml` (simple)

5. **Suggest fixes**:
   - Common issues:
     - Missing required fields (name, version, rules)
     - Invalid rule structure
     - Incorrect field types
     - Invalid regex patterns
   - Offer to fix automatically if appropriate

6. **Next steps**:
   - If valid: "Profile ready! View it: `/policy-show <name>`"
   - If invalid: "Fix errors and run `/policy-validate <file>` again"

## Arguments:

- Path to policy YAML file (e.g., "registry/policies/custom.yaml")
- Optional: --strict flag for stricter validation

## Success Criteria:

- ✅ Validation executed
- ✅ Results clearly explained
- ✅ Errors have actionable guidance
- ✅ User knows how to fix issues
