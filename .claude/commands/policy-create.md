# Policy: Create Profile

Create a new policy profile from a Markdown specification.

## What to do:

1. **Help user write the specification** (if needed):
   - Explain the Markdown policy spec format:
     ```markdown
     # Policy Name

     ## Rules

     ### Rule Name
     Pattern: `regex-pattern-here`
     Message: Description of what this checks
     Severity: error|warning|info
     Action: block|warn|log
     ```
   - Show examples from existing policies
   - Help them define appropriate rules for their use case

2. **Create/validate the spec file**:
   - If user provides content, write it to a temp file
   - If user provides a path, verify it exists

3. **Run the create command**:
   - Execute: `./bin/betty-policy create <name> <spec-file> [--type security|validation|compliance] [--enforcement blocking|warning|info]`
   - Default type: validation
   - Default enforcement: blocking

4. **Show results**:
   - Display the generated profile location
   - Show number of rules parsed
   - Display any validation errors or warnings
   - Show the profile YAML preview

5. **Verify success**:
   - Run: `./bin/betty-policy show <name>` to confirm
   - Suggest testing: `/policy-test <name> <manifest-path>`

## Arguments:

- Profile name (required)
- Path to Markdown spec file OR inline spec content
- Optional: --type, --enforcement flags

## Success Criteria:

- ✅ Policy profile created successfully
- ✅ Profile validated and saved to registry/policies/
- ✅ User can see and test the new profile
