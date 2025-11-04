# Name: seed4j.scaffold

# Purpose:
Scaffolds new Seed4j (formerly JHipster Lite) applications with clean architecture and hexagonal architecture patterns. Helps developers bootstrap Java Spring Boot applications with modular code generation following Test-Driven Development (TDD) principles and hexagonal architecture (ports and adapters pattern).

# Inputs:
- project_name
- package_name
- base_path (optional)
- java_version (optional)
- spring_boot_version (optional)
- include_modules (optional)
- architecture_style (optional)

# Outputs:
- project_structure.json
- configuration_files.json
- module_list.json
- setup_instructions.md
- scaffold_result.json

# Permissions:
- filesystem:read
- filesystem:write

# Produces Artifacts:
- architecture-overview
- component-model

# Consumes Artifacts:
None

# Implementation Notes:

Generate Seed4j project structure following hexagonal architecture:

- Validate project_name (no spaces, valid Java identifier conventions)
- Validate package_name (valid Java package naming)
- Create directory structure following Seed4j conventions: src/main/java/{package}/domain/, src/main/java/{package}/application/, src/main/java/{package}/infrastructure/, src/test/java/{package}/
- Generate configuration files: pom.xml or build.gradle, application.yml with sensible defaults, application-dev.yml, application-test.yml
- Generate hexagonal architecture boilerplate: Domain layer (entities, port interfaces, domain services), Application layer (use case implementations, application services), Infrastructure layer (REST controllers, JPA repositories, configuration classes)
- Generate documentation: README.md, ARCHITECTURE.md, docs/component-model.md
- Apply Seed4j modules if specified
- Use templates for common file patterns (pom.xml, application.yml, etc.)
- Follow Seed4j conventions for directory structure and naming
- Generate placeholder domain entities and use cases to demonstrate the architecture
- Include sensible defaults for Spring Boot configuration
- Provide clear next steps for developers in the README
- Ensure all generated code compiles without errors
- Include basic integration tests that demonstrate the hexagonal architecture
- Generate API documentation (if REST module included)
- Support both Maven and Gradle build tools (default to Maven)
- Create .gitignore and other standard project files

# Examples:
- Create a basic todo-app with Java 21
- Create an e-commerce-api with multiple Seed4j modules (rest-api, jpa, postgresql, security, swagger)
- Create a microservice in a custom base path
