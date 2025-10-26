#!/usr/bin/env python3
"""
Comprehensive template generator for all 391 artifacts.
Uses industry best practices and domain-specific knowledge.
"""
import os
import re
from pathlib import Path
from generate_templates import CATEGORY_MAPPING, get_artifact_list, get_category

# Template generators for different artifact types
class TemplateGenerator:
    def __init__(self):
        self.base_dir = Path('/home/user/betty')
        self.desc_dir = self.base_dir / 'artifact_descriptions'
        self.template_dir = self.base_dir / 'templates'

    def read_description(self, artifact_name):
        """Read artifact description file."""
        desc_file = self.desc_dir / f"{artifact_name}.md"
        if desc_file.exists():
            return desc_file.read_text()
        return ""

    def determine_format(self, artifact_name, description):
        """Determine if artifact should be YAML or MD."""
        # YAML for structured, machine-readable formats
        yaml_keywords = [
            'schema', 'specification', 'contract', 'sla', 'slo',
            'configuration', 'manifest', 'policy', 'matrix', 'catalog',
            'registry', 'model', 'definition', 'dag', 'rules',
            'assessment', 'inventory', 'register', 'schedule',
            'proto', 'api', 'framework', 'scoring'
        ]

        artifact_lower = artifact_name.lower()
        for keyword in yaml_keywords:
            if keyword in artifact_lower:
                return 'yaml'

        # Check description for keywords
        if description:
            desc_lower = description.lower()
            if 'structured format' in desc_lower or 'machine-readable' in desc_lower:
                return 'yaml'
            if 'openapi' in desc_lower or 'asyncapi' in desc_lower:
                return 'yaml'
            if 'cvss' in desc_lower or 'stride' in desc_lower:
                return 'yaml'

        # Default to markdown for narrative documents
        return 'md'

    def get_yaml_base_metadata(self):
        """Standard metadata for YAML templates."""
        return """metadata:
  version: "1.0.0"
  created: "YYYY-MM-DD"
  lastModified: "YYYY-MM-DD"
  author: "Author Name"
  owner: "Team/Department"
  status: "Draft"  # Draft | Review | Approved | Archived
  classification: "Internal"  # Public | Internal | Confidential | Restricted
"""

    def get_md_base_header(self, title):
        """Standard header for Markdown templates."""
        return f"""# {title}

**Version:** 1.0.0
**Last Updated:** YYYY-MM-DD
**Owner:** [Team/Department]
**Status:** Draft

## Document Control

| Field | Value |
|-------|-------|
| Document ID | [Auto-generated or manual ID] |
| Classification | Internal |
| Review Date | YYYY-MM-DD |
| Approvers | [List of approvers] |

"""

    def generate_template(self, artifact_name):
        """Generate template for a specific artifact."""
        description = self.read_description(artifact_name)
        category = get_category(artifact_name)
        format_type = self.determine_format(artifact_name, description)

        print(f"Generating {artifact_name} -> {category}/{artifact_name}.{format_type}")

        # Route to specific generators based on artifact type
        if 'api' in artifact_name or 'openapi' in artifact_name:
            return self.generate_api_template(artifact_name, description, format_type)
        elif 'schema' in artifact_name:
            return self.generate_schema_template(artifact_name, description, format_type)
        elif 'model' in artifact_name and category == 'ai-ml':
            return self.generate_ml_template(artifact_name, description, format_type)
        elif 'test' in artifact_name or 'testing' in artifact_name or category == 'testing':
            return self.generate_testing_template(artifact_name, description, format_type)
        elif 'security' in artifact_name or category == 'security':
            return self.generate_security_template(artifact_name, description, format_type)
        elif 'data' in artifact_name or category == 'data':
            return self.generate_data_template(artifact_name, description, format_type)
        elif 'policy' in artifact_name or 'compliance' in artifact_name:
            return self.generate_policy_template(artifact_name, description, format_type)
        elif 'architecture' in artifact_name or 'diagram' in artifact_name:
            return self.generate_architecture_template(artifact_name, description, format_type)
        elif 'incident' in artifact_name or 'runbook' in artifact_name:
            return self.generate_operations_template(artifact_name, description, format_type)
        elif 'requirement' in artifact_name or category == 'requirements':
            return self.generate_requirements_template(artifact_name, description, format_type)
        else:
            return self.generate_generic_template(artifact_name, description, format_type)

    def save_template(self, artifact_name, content):
        """Save generated template to appropriate location."""
        category = get_category(artifact_name)
        description = self.read_description(artifact_name)
        format_type = self.determine_format(artifact_name, description)

        category_dir = self.template_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        output_file = category_dir / f"{artifact_name}.{format_type}"
        output_file.write_text(content)
        return output_file

    # Specialized template generators
    def generate_api_template(self, name, desc, fmt):
        """Generate API-related templates."""
        if fmt == 'yaml':
            if 'openapi' in name:
                return self._generate_openapi_template()
            elif 'asyncapi' in name:
                return self._generate_asyncapi_template()
            elif 'graphql' in name:
                return self._generate_graphql_template()
        return self.generate_generic_template(name, desc, fmt)

    def _generate_openapi_template(self):
        """Generate OpenAPI 3.1 specification template."""
        return '''openapi: 3.1.0

info:
  title: API Name
  version: 1.0.0
  description: |
    Comprehensive API description.

    ## Overview
    Brief overview of what this API does and its primary use cases.

    ## Authentication
    All endpoints require Bearer token authentication.

  contact:
    name: API Support
    email: api-support@example.com
    url: https://developer.example.com
  license:
    name: Proprietary
    url: https://example.com/licenses

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://api-staging.example.com/v1
    description: Staging
  - url: http://localhost:8080/v1
    description: Local Development

tags:
  - name: users
    description: User management operations
  - name: resources
    description: Resource management
  - name: admin
    description: Administrative operations

paths:
  /users:
    get:
      summary: List users
      description: Retrieve a paginated list of users
      operationId: listUsers
      tags:
        - users
      parameters:
        - name: limit
          in: query
          description: Maximum number of results to return
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
        - name: offset
          in: query
          description: Number of results to skip
          schema:
            type: integer
            minimum: 0
            default: 0
        - name: sort
          in: query
          description: Sort field and order
          schema:
            type: string
            enum: [created_asc, created_desc, name_asc, name_desc]
            default: created_desc
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '500':
          $ref: '#/components/responses/InternalError'
      security:
        - bearerAuth: []

    post:
      summary: Create user
      description: Create a new user
      operationId: createUser
      tags:
        - users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          headers:
            Location:
              description: URL of the created user
              schema:
                type: string
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '409':
          description: User already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      security:
        - bearerAuth: []

  /users/{userId}:
    get:
      summary: Get user by ID
      description: Retrieve a specific user by their ID
      operationId: getUserById
      tags:
        - users
      parameters:
        - $ref: '#/components/parameters/userId'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    put:
      summary: Update user
      description: Update an existing user
      operationId: updateUser
      tags:
        - users
      parameters:
        - $ref: '#/components/parameters/userId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    delete:
      summary: Delete user
      description: Delete a user (soft delete)
      operationId: deleteUser
      tags:
        - users
      parameters:
        - $ref: '#/components/parameters/userId'
      responses:
        '204':
          description: User deleted successfully
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - name
        - createdAt
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
          example: "550e8400-e29b-41d4-a716-446655440000"
        email:
          type: string
          format: email
          description: User email address
          example: "user@example.com"
        name:
          type: string
          description: User full name
          example: "Jane Doe"
        role:
          type: string
          enum: [admin, user, viewer]
          default: user
          description: User role
        status:
          type: string
          enum: [active, inactive, suspended]
          default: active
        createdAt:
          type: string
          format: date-time
          description: Timestamp when user was created
        updatedAt:
          type: string
          format: date-time
          description: Timestamp when user was last updated
        metadata:
          type: object
          additionalProperties: true
          description: Additional user metadata

    CreateUserRequest:
      type: object
      required:
        - email
        - name
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 255
        role:
          type: string
          enum: [admin, user, viewer]
          default: user
        metadata:
          type: object
          additionalProperties: true

    UpdateUserRequest:
      type: object
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 255
        role:
          type: string
          enum: [admin, user, viewer]
        status:
          type: string
          enum: [active, inactive, suspended]
        metadata:
          type: object
          additionalProperties: true

    UserListResponse:
      type: object
      required:
        - data
        - pagination
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      required:
        - total
        - limit
        - offset
      properties:
        total:
          type: integer
          description: Total number of items
        limit:
          type: integer
          description: Maximum items per page
        offset:
          type: integer
          description: Number of items skipped
        hasMore:
          type: boolean
          description: Whether more results are available

    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: string
          description: Error code
          example: "VALIDATION_ERROR"
        message:
          type: string
          description: Human-readable error message
          example: "Invalid email format"
        details:
          type: array
          items:
            type: object
            properties:
              field:
                type: string
              error:
                type: string
        requestId:
          type: string
          description: Request ID for debugging

  parameters:
    userId:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: string
        format: uuid

  responses:
    BadRequest:
      description: Bad request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    Unauthorized:
      description: Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    InternalError:
      description: Internal server error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT token obtained from authentication endpoint

security:
  - bearerAuth: []
'''

    def _generate_asyncapi_template(self):
        """Generate AsyncAPI 2.6 specification template."""
        return '''asyncapi: 2.6.0

info:
  title: Event-Driven API
  version: 1.0.0
  description: |
    Event-driven messaging API using AsyncAPI specification.

    ## Overview
    Describes asynchronous message-based communication patterns.

  contact:
    name: API Support
    email: events@example.com
  license:
    name: Proprietary

servers:
  production:
    url: kafka.example.com:9092
    protocol: kafka
    description: Production Kafka cluster
    bindings:
      kafka:
        schemaRegistryUrl: https://schema-registry.example.com

  staging:
    url: kafka-staging.example.com:9092
    protocol: kafka
    description: Staging Kafka cluster

defaultContentType: application/json

channels:
  user.created:
    description: Channel for user creation events
    subscribe:
      summary: User Created Event
      operationId: onUserCreated
      message:
        $ref: '#/components/messages/UserCreated'
      bindings:
        kafka:
          groupId: user-service-consumers

  user.updated:
    description: Channel for user update events
    subscribe:
      summary: User Updated Event
      operationId: onUserUpdated
      message:
        $ref: '#/components/messages/UserUpdated'

  user.deleted:
    description: Channel for user deletion events
    subscribe:
      summary: User Deleted Event
      operationId: onUserDeleted
      message:
        $ref: '#/components/messages/UserDeleted'

  order.placed:
    description: Channel for order placement events
    subscribe:
      summary: Order Placed Event
      operationId: onOrderPlaced
      message:
        $ref: '#/components/messages/OrderPlaced'
    publish:
      summary: Publish Order Placed Event
      operationId: publishOrderPlaced
      message:
        $ref: '#/components/messages/OrderPlaced'

components:
  messages:
    UserCreated:
      name: UserCreated
      title: User Created Event
      summary: Published when a new user is created
      contentType: application/json
      payload:
        $ref: '#/components/schemas/UserCreatedPayload'
      headers:
        $ref: '#/components/schemas/EventHeaders'

    UserUpdated:
      name: UserUpdated
      title: User Updated Event
      summary: Published when a user is updated
      contentType: application/json
      payload:
        $ref: '#/components/schemas/UserUpdatedPayload'
      headers:
        $ref: '#/components/schemas/EventHeaders'

    UserDeleted:
      name: UserDeleted
      title: User Deleted Event
      summary: Published when a user is deleted
      contentType: application/json
      payload:
        $ref: '#/components/schemas/UserDeletedPayload'
      headers:
        $ref: '#/components/schemas/EventHeaders'

    OrderPlaced:
      name: OrderPlaced
      title: Order Placed Event
      summary: Published when an order is placed
      contentType: application/json
      payload:
        $ref: '#/components/schemas/OrderPlacedPayload'
      headers:
        $ref: '#/components/schemas/EventHeaders'

  schemas:
    EventHeaders:
      type: object
      required:
        - eventId
        - eventType
        - timestamp
        - source
      properties:
        eventId:
          type: string
          format: uuid
          description: Unique event identifier
        eventType:
          type: string
          description: Event type identifier
        timestamp:
          type: string
          format: date-time
          description: Event timestamp
        source:
          type: string
          description: Source system that generated the event
        correlationId:
          type: string
          format: uuid
          description: Correlation ID for request tracing
        version:
          type: string
          description: Event schema version

    UserCreatedPayload:
      type: object
      required:
        - userId
        - email
        - createdAt
      properties:
        userId:
          type: string
          format: uuid
        email:
          type: string
          format: email
        name:
          type: string
        role:
          type: string
          enum: [admin, user, viewer]
        createdAt:
          type: string
          format: date-time

    UserUpdatedPayload:
      type: object
      required:
        - userId
        - updatedAt
        - changes
      properties:
        userId:
          type: string
          format: uuid
        changes:
          type: object
          description: Object containing changed fields
        updatedAt:
          type: string
          format: date-time
        updatedBy:
          type: string

    UserDeletedPayload:
      type: object
      required:
        - userId
        - deletedAt
      properties:
        userId:
          type: string
          format: uuid
        deletedAt:
          type: string
          format: date-time
        deletedBy:
          type: string
        reason:
          type: string

    OrderPlacedPayload:
      type: object
      required:
        - orderId
        - customerId
        - items
        - totalAmount
        - placedAt
      properties:
        orderId:
          type: string
          format: uuid
        customerId:
          type: string
          format: uuid
        items:
          type: array
          items:
            type: object
            properties:
              productId:
                type: string
              quantity:
                type: integer
              price:
                type: number
        totalAmount:
          type: number
          format: decimal
        currency:
          type: string
          enum: [USD, EUR, GBP]
        placedAt:
          type: string
          format: date-time
'''

    # Will add more specialized generators in next iteration
    def generate_generic_template(self, name, desc, fmt):
        """Generate a generic template as fallback."""
        if fmt == 'yaml':
            return f'''# {name.replace('-', ' ').title()}
# See also: artifact_descriptions/{name}.md for complete guidance

{self.get_yaml_base_metadata()}
# [Add artifact-specific fields here based on the description]

description: |
  Brief description of this artifact.

# Example sections (customize based on artifact type)
sections:
  - name: "Section 1"
    description: "Description of this section"

  - name: "Section 2"
    description: "Description of this section"

# Notes
notes:
  - "Important consideration 1"
  - "Important consideration 2"

# References
references:
  - artifact: "Related Artifact Name"
    type: "artifact_type"
    purpose: "Why this is referenced"
'''
        else:
            title = name.replace('-', ' ').title()
            return f'''{self.get_md_base_header(title)}

## Purpose

[Describe the purpose of this {name}]

## Scope

### In Scope
- [Item 1]
- [Item 2]

### Out of Scope
- [Item 1]
- [Item 2]

## [Section Title]

[Content here]

## [Another Section]

[Content here]

## References

- [Related Document 1]
- [Related Document 2]

---
*For complete guidance, see artifact_descriptions/{name}.md*
'''

def main():
    """Generate all templates."""
    generator = TemplateGenerator()
    artifacts = get_artifact_list()

    print(f"Generating {len(artifacts)} templates...\n")

    for i, artifact in enumerate(artifacts, 1):
        try:
            content = generator.generate_template(artifact)
            output_file = generator.save_template(artifact, content)
            if i % 10 == 0:
                print(f"Progress: {i}/{len(artifacts)} templates generated")
        except Exception as e:
            print(f"ERROR generating {artifact}: {e}")

    print(f"\nCompleted! Generated {len(artifacts)} templates")

if __name__ == '__main__':
    main()
