# Name: api.test

# Purpose:
Test REST API endpoints by executing HTTP requests and validating responses against expected outcomes

# Inputs:
- api_spec_path
- base_url
- test_scenarios_path (optional)
- auth_config_path (optional)

# Outputs:
- test_results.json
- test_report.html

# Permissions:
- network:http
- filesystem:read
- filesystem:write

# Produces Artifacts:
- test-result
- test-report

# Implementation Notes:
Support multiple HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS

Test scenarios should validate:
- Response status codes
- Response headers
- Response body structure and content
- Response time/performance
- Authentication/authorization
- Error handling

Features:
- Load test scenarios from OpenAPI/Swagger specs
- Support various authentication methods (Bearer, Basic, API Key, OAuth2)
- Execute tests in sequence or parallel
- Generate detailed HTML reports with pass/fail visualization
- Support environment variables for configuration
- Retry failed tests with exponential backoff
- Collect performance metrics (response time, throughput)

Output should include:
- Total tests run
- Passed/failed counts
- Individual test results with request/response details
- Performance statistics
- Coverage metrics (% of endpoints tested)
