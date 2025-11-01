# Policy: Validate Profile YAML

Validate a policy profile YAML file for correctness.

## What to do:

1. **Run validation**:
   - Execute: `./bin/betty-policy validate <policy-file-path> [--strict]`
   - Use --strict flag for production profiles

2. **Parse validation results**:
   - Check if valid: true/false
   - Extract errors and warnings
   - Note rule count and structure

3. **Display results clearly**:

   **If valid:**
   ```
   ✓ Policy YAML is valid

   Profile: <name>
   Type: <type>
   Rules: <count>
   Scope: <scopes>
   ```

   **If invalid:**
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
   - If valid: "Profile ready! Use `/policy-show <name>` to preview"
   - If invalid: "Fix the errors and run `/policy-validate` again"

## Arguments:

- Path to policy YAML file (e.g., "registry/policies/custom.yaml")
- Optional: --strict flag for stricter validation

## Success Criteria:

- ✅ Validation executed
- ✅ Results clearly explained
- ✅ Errors have actionable guidance
- ✅ User knows how to fix issues
