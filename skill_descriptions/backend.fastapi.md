# Name: backend.fastapi

# Purpose:
Generate FastAPI backend implementations following Python best practices. Creates async REST APIs, automatic OpenAPI documentation, Pydantic models, database integration, and dependency injection. Follows FastAPI conventions and production-ready patterns.

# Inputs:
- api-specification (OpenAPI spec)
- database-schema
- authentication-requirements

# Outputs:
- fastapi-application (Python code)
- pydantic-models
- route-definitions
- test-suite

# Dependencies:
- Python 3.11+
- FastAPI
- Pydantic
- uvicorn

# Constraints:
- Follow FastAPI best practices and async patterns
- Use Pydantic for data validation
- Include automatic API documentation
- Implement OAuth2/JWT authentication when needed

# Examples:
- Generate FastAPI from OpenAPI specification
- Create async endpoints with database integration
- Implement authentication with OAuth2 password flow
