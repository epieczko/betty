# Policy: List Profiles

List all available policy profiles in the Betty Framework.

## What to do:

1. **List policy profile files**:
   - Run: `ls -1 registry/policies/*.yaml`
   - Extract profile names (strip .yaml extension)

2. **For each profile, load and display key info**:
   - Run: `python skills/policy.validate/policy_validate.py registry/policies/<name>.yaml`
   - Extract: name, type, description, rule count, enforcement level

3. **Show results to user**:
   - Display a formatted table:
     ```
     Policy Profiles
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     betty-core       validation    Core Betty validation (9 rules)
     default          security      Default security profile (5 rules)
     strict           security      Strict production profile (5 rules)
     ...
     ```
   - Sort by type, then name

4. **Suggest next steps**:
   - "View details: `/policy-show <name>`"
   - "Test a profile: `/policy-test <profile> <manifest>`"

## Success Criteria:

- ✅ All policy profiles listed
- ✅ Results clearly formatted
- ✅ User knows how to explore further
