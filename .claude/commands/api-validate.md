# Validate API Specification

Validate an OpenAPI or AsyncAPI specification against enterprise guidelines.

## What to do:

1. **Validate the specification**:
   - Run: `python skills/api.validate/api_validate.py <spec-path> zalando --format=human`
   - Show the validation results to the user

2. **If there are errors**:
   - Explain each error clearly
   - Suggest fixes with examples
   - Offer to fix them automatically if the user wants

3. **If validation passes**:
   - Congratulate the user
   - Show any warnings that should be addressed
   - Suggest next steps (e.g., generate models, create PR)

## Arguments:

The user will provide a path to an API specification file (e.g., "specs/user-service.openapi.yaml")

## Success Criteria:

- ✅ Specification is validated
- ✅ Results are clearly explained
- ✅ User knows what to do next
