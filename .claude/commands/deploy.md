# Deploy

Deploy application to target environment with full pipeline orchestration.

## What to do:

1. **Execute the deployment workflow**:
   - Workflow: workflows/deploy-pipeline.yaml
   - Note: This is a WORKFLOW pattern example - orchestrates multiple components

2. **Workflow phases**:
   - **Validate**: Check version tag
   - **Test**: Run test suite (unless skipped)
   - **Build**: Create artifacts in parallel (backend + frontend)
   - **Deploy**: Use agent for intelligent orchestration
   - **Verify**: Validate deployment success
   - **Notify**: Send deployment notifications

3. **Monitor progress**:
   - Show status of each phase
   - Report any failures or warnings
   - Execute rollback if needed

4. **Report results**:
   - Summary of deployment
   - Version deployed
   - Environment target
   - Any issues encountered

## Arguments:

The user must provide:
- environment: Target environment (dev, staging, production)
- version: Version tag to deploy

Optional:
- skip_tests: Skip test execution (default: false)

## Success Criteria:

- ✅ All workflow phases complete successfully
- ✅ Application deployed and verified
- ✅ Stakeholders notified
- ✅ Rollback executed if any phase fails

## Pattern Note:

This command uses the **WORKFLOW** execution pattern because:
- Orchestrates multiple distinct components
- Includes both sequential and parallel execution
- Mixes skills (deterministic tasks) and agents (reasoning)
- Has clear phases with dependencies
- Implements error handling and rollback
