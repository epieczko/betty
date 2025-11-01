# Policy: Enforce

Enforce policy rules on manifest files (single file or all manifests).

## What to do:

1. **Determine scope**:
   - Single manifest: User provides path
   - All manifests: User says "all" or requests batch mode
   - Profile: Optional, defaults to betty-core validation

2. **Run enforcement**:

   **For single manifest:**
   - Execute: `python skills/policy.enforce/policy_enforce.py <manifest-path> [--profile <name>]`
   - Without --profile: Uses default betty-core validation
   - With --profile: Uses specified profile from registry/policies/

   **For all manifests (batch mode):**
   - Execute: `python skills/policy.enforce/policy_enforce.py --batch [--profile <name>]`
   - Checks all skills/*/skill.yaml and agents/*/agent.yaml

3. **Parse and display results**:

   **For batch mode, show summary:**
   ```
   Policy Enforcement Results
   ━━━━━━━━━━━━━━━━━━━━━━━━
   Total: X manifests
   ✓ Passed: X
   ✗ Failed: X
   ```

   **For each failure:**
   - Show manifest path
   - List violations with clear messages
   - Group by severity (errors first, then warnings)
   - Use 🔴 for errors, ⚠️ for warnings

4. **Provide actionable guidance**:
   - If all passed: "✓ All manifests comply with policy!"
   - If failures exist:
     - Prioritize errors over warnings
     - Suggest fixing high-impact violations first
     - Offer to fix automatically if patterns are clear
   - Show which specific files need attention

5. **Suggest next steps**:
   - "Fix violations in: <file-paths>"
   - "Re-run: `/policy-enforce`"
   - "View profile: `/policy-show <profile>`"
   - "Create custom profile: `/policy-create`"

## Arguments:

- **Optional:** Manifest path (if omitted, user must specify "all" or batch)
- **Optional:** --profile <name> (defaults to betty-core validation)
- **Optional:** --batch or "all manifests" (check everything)

## Success Criteria:

- ✅ Enforcement executed on requested scope
- ✅ Results clearly summarized
- ✅ Violations clearly explained
- ✅ User knows exactly what to fix and where
