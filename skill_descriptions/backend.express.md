# Name: backend.express

# Purpose:
Generate Express.js backend implementations following Node.js best practices. Creates RESTful API routes, middleware, authentication, database integration, and error handling. Follows Express.js conventions and production-ready patterns.

# Inputs:
- api-specification (OpenAPI spec)
- database-schema
- authentication-requirements

# Outputs:
- express-application (TypeScript/JavaScript code)
- middleware-configuration
- route-definitions
- test-suite

# Dependencies:
- Node.js 18+
- Express.js
- TypeScript (optional)

# Constraints:
- Follow Express.js best practices and conventions
- Include proper error handling and validation
- Implement security middleware (helmet, cors, rate limiting)
- Generate TypeScript type definitions when applicable

# Examples:
- Generate Express API from OpenAPI specification
- Create authentication middleware using JWT
- Implement database integration with Prisma or Mongoose
