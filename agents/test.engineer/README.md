# Test.Engineer Agent

## Purpose

Create comprehensive testing artifacts including test plans, test cases, test results, test automation strategies, and quality assurance reports. Applies testing methodologies (TDD, BDD, risk-based testing) and frameworks (ISO 29119, ISTQB) to ensure thorough test coverage and quality validation across all test levels (unit, integration, system, acceptance).

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `Requirements or user stories`
- `System architecture or design`
- `Test scope and objectives`
- `Quality criteria and acceptance thresholds`
- `Testing constraints`
- `Defects or test results`

### Produces

- `test-plan: Comprehensive test strategy with scope, approach, resources, and schedule`
- `test-cases: Detailed test cases with steps, data, and expected results`
- `test-results: Test execution results with pass/fail status and defect tracking`
- `test-automation-strategy: Test automation framework and tool selection`
- `acceptance-criteria: User story acceptance criteria in Given-When-Then format`
- `performance-test-plan: Performance and load testing strategy`
- `integration-test-plan: Integration testing approach with interface validation`
- `regression-test-suite: Regression test suite for continuous integration`
- `quality-assurance-report: QA summary with metrics, defects, and quality assessment`

## Example Use Cases

- Test scope (functional, security, accessibility, performance)
- Test levels (unit, integration, system, UAT)
- Test approach by feature area
- Platform coverage (iOS 14+, Android 10+)
- Test environment and data requirements
- Accessibility testing (WCAG 2.1 AA compliance)
- Entry/exit criteria and quality gates
- Test schedule and resource allocation
- Risk-based testing priorities
- test-cases.yaml with detailed test scenarios for each step
- test-automation-strategy.yaml with framework selection (Selenium, Cypress)
- regression-test-suite.yaml for CI/CD integration
- Test cases include: happy path, error handling, edge cases
- Automation coverage: 80% of critical user journeys
- Performance requirements (throughput, latency, concurrency)
- Load testing scenarios (baseline, peak, stress, soak)
- Performance metrics and SLAs
- Test data and environment sizing
- Monitoring and observability requirements
- Performance acceptance criteria

## Usage

```bash
# Activate the agent
/agent test.engineer

# Or invoke directly
betty agent run test.engineer --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
