# Name: /api-design
# Version: 0.1.0
# Description: Design a complete API architecture from requirements

# Execution Type: agent
# Target: api.architect

# Parameters:
- requirements: string (required) - Path to requirements document or description
- style: enum (optional, default=rest, values=[rest,graphql,grpc]) - API architectural style
- guidelines: string (optional, default=zalando) - Design guidelines to follow

# Execution Context:
- reasoning_mode: iterative
- max_iterations: 10
- output_format: yaml

# Status: active

# Tags: api, design, architecture, agent
