# Policy: List Profiles

List all available policy profiles in the Betty Framework.

## What to do:

1. **Run the list command**:
   - Execute: `./bin/betty-policy list`
   - Parse the JSON output

2. **Show results to user**:
   - Display a formatted table of profiles with:
     - Name
     - Type (validation/security/compliance)
     - Description
     - Number of rules
     - Enforcement level
   - Sort by type, then name

3. **Suggest next steps**:
   - "Use `/policy-show <name>` to see profile details"
   - "Use `/policy-test <profile> <manifest>` to test a profile"

## Success Criteria:

- ✅ All policy profiles listed
- ✅ Results clearly formatted
- ✅ User knows how to explore further
