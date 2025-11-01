# Policy: Show Profile Details

Show detailed information about a specific policy profile.

## What to do:

1. **Load the policy profile**:
   - Read: `registry/policies/<profile-name>.yaml`
   - Parse the YAML structure

2. **Display profile details clearly**:
   - Header: Name, version, type, scope
   - Description
   - Enforcement level
   - **Rules section**: For each rule:
     ```
     Rule: <id or name>
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     Field:    <field>
     Check:    <check type>
     Pattern:  <pattern if applicable>
     Values:   <allowed/forbidden values if applicable>
     Message:  <message>
     Severity: <severity> | Action: <action>
     ```

3. **Provide context**:
   - Explain what the profile validates
   - Highlight strict/blocking rules vs warnings
   - Show which manifest types it applies to (scope)

4. **Suggest next steps**:
   - "Test this profile: `/policy-test <profile> <manifest-path>`"
   - "Enforce on all manifests: `/policy-enforce --all --profile <profile>`"

## Arguments:

The user will provide a policy profile name (e.g., "strict", "betty-core", "default")

## Success Criteria:

- ✅ Profile details clearly displayed
- ✅ Rules explained in user-friendly format
- ✅ User understands what the profile validates
