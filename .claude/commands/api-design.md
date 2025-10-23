# Design API

Design a complete API following Zalando RESTful API Guidelines with automatic validation and code generation.

## What to do:

1. **Create OpenAPI Specification**:
   - Run: `python skills/api.define/api_define.py <service-name> openapi --template=zalando`
   - This creates a Zalando-compliant OpenAPI 3.1 spec in `specs/<service-name>.openapi.yaml`

2. **Validate Specification**:
   - Run: `python skills/api.validate/api_validate.py specs/<service-name>.openapi.yaml zalando --format=human`
   - This validates against Zalando guidelines
   - Fix any errors that appear

3. **Generate TypeScript Models**:
   - Run: `python skills/api.generate-models/modelina_generate.py specs/<service-name>.openapi.yaml typescript --output-dir=src/models/<service-name>`
   - This generates type-safe TypeScript interfaces

4. **Generate Python Models**:
   - Run: `python skills/api.generate-models/modelina_generate.py specs/<service-name>.openapi.yaml python --output-dir=backend/models/<service-name>`
   - This generates Python dataclasses

5. **Summary**:
   - Show the user what was created
   - List all generated files
   - Provide next steps for implementation

## Arguments:

The user will provide a service name (e.g., "user-service", "order-api", "payment-gateway")

## Success Criteria:

- ✅ OpenAPI spec created and validated with 0 errors
- ✅ TypeScript models generated
- ✅ Python models generated
- ✅ All files ready for development
