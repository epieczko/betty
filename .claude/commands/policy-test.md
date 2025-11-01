# Policy: Test Profile

Test a policy profile against a specific manifest file.

## What to do:

1. **Validate inputs**:
   - Confirm profile exists: `./bin/betty-policy list` and check
   - Verify manifest file exists
   - Identify manifest type (skill.yaml or agent.yaml)

2. **Run the test**:
   - Execute: `./bin/betty-policy test <profile> <manifest-path>`
   - The tool outputs human-friendly format by default

3. **Show results clearly**:
   - **If passed**:
     - ✓ Show success message
     - Display number of rules checked
     - Congratulate user

   - **If failed**:
     - ✗ Show violation count
     - For each violation:
       - Field that failed
       - Rule violated
       - Clear message explaining the issue
       - Severity (error/warning)
     - Use emojis: 🔴 for errors, ⚠️ for warnings

4. **Provide actionable feedback**:
   - Explain what needs to be fixed
   - Show examples of correct format if applicable
   - Offer to fix automatically if appropriate

5. **Suggest next steps**:
   - If passed: "Ready to commit? Use `/commit`"
   - If failed: "Fix the violations and run `/policy-test <profile> <manifest>` again"
   - For custom profiles: "Adjust the profile rules if needed: `/policy-show <profile>`"

## Arguments:

- Profile name (e.g., "strict", "betty-core", "default")
- Path to manifest file (e.g., "skills/my.skill/skill.yaml")

## Success Criteria:

- ✅ Test executed successfully
- ✅ Results clearly explained
- ✅ User knows exactly what to fix (if violations exist)
- ✅ User knows next steps
