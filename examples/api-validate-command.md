# Name: /api-validate
# Version: 0.1.0
# Description: Validate API specifications against standards

# Execution Type: skill
# Target: api.validate

# Parameters:
- spec_file: string (required) - Path to API specification file
- format: enum (optional, default=openapi, values=[openapi,asyncapi,grpc]) - API specification format
- strict: boolean (optional, default=true) - Enable strict validation mode

# Execution Context:
- format: json
- timeout: 300

# Status: active

# Tags: api, validation, quality
