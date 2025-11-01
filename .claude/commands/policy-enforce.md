# Policy: Enforce

Enforce policy rules on manifest files (single file or all manifests).

## What to do:

1. **Determine scope**:
   - Single manifest: User provides path
   - All manifests: User requests via `--all` flag or "all manifests"
   - Profile: Optional, defaults to betty-core validation

2. **Run enforcement**:

   **For single manifest:**
   - Execute: `./bin/betty-policy enforce <manifest-path> [--profile <name>]`

   **For all manifests:**
   - Execute: `./bin/betty-policy enforce --all [--profile <name>]`
   - This checks all skills/*/skill.yaml and agents/*/agent.yaml

3. **Parse and display results**:

   **Summary format:**
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

4. **Provide actionable guidance**:
   - If all passed: "✓ All manifests comply with policy!"
   - If failures exist:
     - Prioritize errors over warnings
     - Suggest fixing high-impact violations first
     - Offer to fix automatically if patterns are clear
   - Show which specific files need attention

5. **Suggest next steps**:
   - "Fix violations in: <file-paths>"
   - "Re-run enforcement: `/policy-enforce`"
   - "View specific profile: `/policy-show <profile>`"
   - "Create stricter profile: `/policy-create`"

## Arguments:

- **Optional:** Manifest path (if not provided, assumes --all)
- **Optional:** --profile <name> (defaults to betty-core)
- **Optional:** --all flag (check all manifests)

## Success Criteria:

- ✅ Enforcement executed on requested scope
- ✅ Results clearly summarized
- ✅ Violations clearly explained
- ✅ User knows exactly what to fix and where
