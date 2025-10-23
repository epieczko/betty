# Check API Compatibility

Check for breaking changes between two versions of an API specification.

## What to do:

1. **Run compatibility check**:
   - Run: `python skills/api.compatibility/check_compatibility.py <old-spec> <new-spec> --format=human`
   - This compares two spec versions

2. **Analyze results**:
   - Clearly explain any breaking changes found
   - Explain why each change is breaking
   - Show non-breaking changes for context

3. **Provide recommendations**:
   - If breaking changes found:
     - Suggest how to make changes non-breaking
     - Explain versioning strategy (e.g., increment major version)
     - Offer to create a migration guide
   - If no breaking changes:
     - Congratulate the user on maintaining compatibility
     - Suggest safe next steps

## Arguments:

- Path to old/previous specification (required)
- Path to new/current specification (required)

## Success Criteria:

- ✅ Compatibility is checked
- ✅ Breaking and non-breaking changes are identified
- ✅ User understands impact and next steps
