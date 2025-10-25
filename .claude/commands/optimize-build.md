# Optimize Build

Analyze and optimize build processes and speed.

## What to do:

1. **Run the build optimization analysis**:
   - Run: `python skills/build.optimize/build_optimize.py <project-path>`
   - Show the analysis results to the user

2. **Review the analysis**:
   - Display detected build system
   - Show complexity analysis
   - List all recommendations with priorities

3. **Explain recommendations**:
   - For each high-priority recommendation, explain why it matters
   - Provide specific implementation steps
   - Estimate the impact of each optimization

4. **Offer to apply changes**:
   - Ask if the user wants to apply any of the recommendations
   - For TypeScript optimizations: edit tsconfig.json
   - For package.json changes: update dependencies
   - For build config: suggest specific configuration changes

## Arguments:

The user may provide:
- A path to a project directory (default: current directory)
- Specific areas to focus on (caching, dependencies, bundling, etc.)

## Success Criteria:

- ✅ Build system correctly identified
- ✅ Comprehensive analysis performed
- ✅ Prioritized recommendations provided
- ✅ User understands the potential improvements
- ✅ Clear next steps provided
