# Policy: Test Profile

Test a policy profile against a specific manifest file.

## What to do:

1. **Validate inputs**:
   - Confirm profile exists: `ls registry/policies/<profile>.yaml`
   - Verify manifest file exists
   - Identify manifest type (skill.yaml or agent.yaml)

2. **Run policy enforcement with profile**:
   - Execute: `python skills/policy.enforce/policy_enforce.py <manifest-path> --profile <profile-name>`
   - This validates the manifest against the specified profile
   - Output is JSON format

3. **Parse and display results**:
   - **If success: true**:
     ```
     ✓ Policy '<profile>' validation passed
       Manifest: <path>
       Rules checked: <count>
     ```

   - **If success: false**:
     ```
     ✗ Policy '<profile>' validation failed
       Manifest: <path>
       Violations: <count>

       🔴 <field>: <message>
       ⚠️  <field>: <message>
     ```
     - Use 🔴 for errors, ⚠️ for warnings

4. **Provide actionable feedback**:
   - Explain what needs to be fixed
   - Show examples of correct format if applicable
   - Offer to fix automatically if appropriate

5. **Suggest next steps**:
   - If passed: "Ready to commit? Use `/commit`"
   - If failed: "Fix the violations and test again"
   - For custom profiles: "Adjust profile: `/policy-show <profile>`"

## Arguments:

- Profile name (e.g., "strict", "betty-core", "default")
- Path to manifest file (e.g., "skills/my.skill/skill.yaml")

## Success Criteria:

- ✅ Test executed successfully
- ✅ Results clearly explained
- ✅ User knows exactly what to fix (if violations exist)
- ✅ User knows next steps
