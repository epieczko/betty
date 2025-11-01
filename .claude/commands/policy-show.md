# Policy: Show Profile Details

Show detailed information about a specific policy profile.

## What to do:

1. **Run the show command**:
   - Execute: `./bin/betty-policy show <profile-name>`
   - Parse the JSON output

2. **Display profile details**:
   - Name, version, type, scope
   - Description
   - Enforcement level
   - List all rules with:
     - Rule ID
     - Field being validated
     - Check type (pattern, allowed_values, etc.)
     - Message
     - Severity and action

3. **Provide context**:
   - Explain what the profile is for
   - Show which scopes it applies to
   - Highlight any strict/blocking rules

4. **Suggest next steps**:
   - "Test this profile: `/policy-test <profile> <manifest-path>`"
   - "Enforce on all manifests: `/policy-enforce --profile <profile>`"

## Arguments:

The user will provide a policy profile name (e.g., "strict", "betty-core", "default")

## Success Criteria:

- ✅ Profile details clearly displayed
- ✅ Rules explained in user-friendly format
- ✅ User understands what the profile validates
