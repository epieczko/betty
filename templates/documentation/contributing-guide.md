# Contributing to [Project Name]

Thank you for your interest in contributing to [Project Name]! We welcome contributions from the community and appreciate your help in making this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Git Workflow](#git-workflow)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code Review Guidelines](#code-review-guidelines)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Community](#community)
- [Legal](#legal)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to conduct@project.com.

**Key principles:**
- Be respectful and inclusive
- Welcome newcomers warmly
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Finding Issues to Work On

**Good First Issues**: New to the project? Start here!
- Browse issues labeled [`good first issue`](https://github.com/org/project/labels/good%20first%20issue)
- These are well-defined, manageable tasks perfect for first-time contributors

**Help Wanted**: Ready for more?
- Check out [`help wanted`](https://github.com/org/project/labels/help%20wanted) issues
- These are important tasks where we need community support

**Before Starting Work:**
1. Comment on the issue to let others know you're working on it
2. Wait for confirmation from maintainers (especially for large changes)
3. Ask questions if anything is unclear

## How to Contribute

We accept several types of contributions:

### Code Contributions
- Bug fixes
- New features
- Performance improvements
- Refactoring
- Test coverage improvements

### Non-Code Contributions
- Documentation improvements
- Translation/localization
- Issue triage and reproduction
- Answering questions in discussions
- Blog posts and tutorials
- UX/design improvements

**All contributions are valued equally!**

## Development Setup

### Prerequisites

- [Runtime/Language] version X.Y+ ([installation guide](https://example.com))
- Git 2.x+
- [Additional tools as needed]

### Initial Setup

```bash
# 1. Fork the repository on GitHub
# Click the "Fork" button at https://github.com/org/project

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/project.git
cd project

# 3. Add upstream remote
git remote add upstream https://github.com/org/project.git

# 4. Create development environment
# For Python projects:
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev,test]"

# For Node.js projects:
npm install

# For Go projects:
go mod download

# 5. Install pre-commit hooks (auto-formats code before commits)
pre-commit install

# 6. Verify setup
make test  # or: npm test, pytest, go test ./...
```

### Running Locally

```bash
# Start development server
make dev  # or npm run dev, python -m project dev

# Run tests
make test

# Run linter
make lint

# Format code
make format
```

## Git Workflow

We use a **fork-and-pull** workflow:

### 1. Keep Your Fork Synced

```bash
# Fetch latest changes from upstream
git fetch upstream

# Update your main branch
git checkout main
git merge upstream/main

# Push updates to your fork
git push origin main
```

### 2. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes:
git checkout -b fix/issue-123-description

# Branch naming conventions:
# - feature/add-user-authentication
# - fix/resolve-memory-leak
# - docs/update-installation-guide
# - refactor/simplify-api-client
```

### 3. Make Your Changes

```bash
# Make changes to code

# Run tests frequently
make test

# Lint your code
make lint

# Commit changes (see commit guidelines below)
git add .
git commit -m "feat: add user authentication"
```

### 4. Push to Your Fork

```bash
# Push your feature branch to your fork
git push origin feature/your-feature-name
```

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

Must be one of:

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semi-colons, etc.)
- **refactor**: Code refactoring (no functional changes)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (dependencies, build config, etc.)
- **ci**: CI/CD changes

### Scope (Optional)

The scope specifies the area of change (e.g., `api`, `ui`, `auth`, `docs`).

### Subject

- Use imperative mood: "add" not "added" or "adds"
- Don't capitalize first letter
- No period at the end
- Maximum 50 characters

### Body (Optional)

- Explain **what** and **why**, not **how**
- Wrap at 72 characters
- Separate from subject with blank line

### Footer (Optional)

- Reference issues: `Closes #123`, `Fixes #456`
- Note breaking changes: `BREAKING CHANGE: description`

### Examples

**Simple feature:**
```
feat(auth): add OAuth2 authentication

Implement OAuth2 authentication flow using authorization code grant.
Supports Google and GitHub providers.

Closes #234
```

**Bug fix:**
```
fix(api): resolve race condition in user creation

Fix race condition when multiple requests create users simultaneously
by adding database-level unique constraint and retry logic.

Fixes #567
```

**Breaking change:**
```
feat(api)!: change response format to JSON:API

BREAKING CHANGE: API responses now follow JSON:API specification.
Clients must update to handle new response structure.

Migration guide: docs/migration-v2.md

Closes #789
```

## Pull Request Process

### Before Opening a PR

**Checklist:**
- [ ] All tests pass locally (`make test`)
- [ ] Linter passes (`make lint`)
- [ ] Code is formatted (`make format`)
- [ ] Commits follow commit message guidelines
- [ ] Documentation is updated (if applicable)
- [ ] CHANGELOG.md is updated (for user-facing changes)
- [ ] New tests added for new functionality
- [ ] Existing tests updated (if behavior changed)

### Opening a PR

1. **Push your branch** to your fork
2. **Open a pull request** from your branch to `upstream/main`
3. **Fill out the PR template** completely
4. **Link related issues** using keywords: "Closes #123", "Fixes #456"
5. **Add screenshots** for UI changes
6. **Request review** from relevant maintainers

### PR Template

```markdown
## Description
<!-- Describe what this PR does and why -->

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Closes #(issue number)

## How Has This Been Tested?
<!-- Describe the tests you ran -->
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Screenshots (if applicable)
<!-- Add screenshots for UI changes -->

## Checklist
- [ ] My code follows the code style of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published
```

### After Opening a PR

**What to expect:**
- Automated checks will run (CI/CD, linting, tests)
- Maintainers will review within 3-5 business days
- You may be asked to make changes
- Once approved, a maintainer will merge your PR

**Responding to feedback:**
- Be open to suggestions and willing to iterate
- Ask for clarification if feedback is unclear
- Make requested changes in new commits (don't force-push during review)
- Re-request review after addressing feedback
- Thank reviewers for their time

## Code Review Guidelines

### For Contributors

**When receiving reviews:**
- Assume positive intent
- Ask for clarification if feedback is unclear
- Explain your reasoning if you disagree
- Make changes promptly
- Thank reviewers for their time

### For Reviewers

**Provide constructive feedback:**

Good:
```
Consider extracting this into a separate function for better testability.
Example:
  function validateUser(user) { ... }
```

Better than:
```
This function is too long.
```

**Types of feedback:**
- **MUST**: Required changes before merge
- **SHOULD**: Strong suggestions, but negotiable
- **NIT** (nitpick): Minor suggestions, optional
- **QUESTION**: Seeking clarification

**Review checklist:**
- [ ] Code solves the stated problem
- [ ] Implementation follows project standards
- [ ] Tests are adequate and passing
- [ ] No security vulnerabilities introduced
- [ ] Performance impact is acceptable
- [ ] Documentation is updated
- [ ] No unnecessary complexity

## Coding Standards

### General Principles

- **DRY (Don't Repeat Yourself)**: Avoid code duplication
- **KISS (Keep It Simple)**: Prefer simple solutions
- **YAGNI (You Aren't Gonna Need It)**: Don't add features speculatively
- **SOLID Principles**: Follow object-oriented design principles

### Language-Specific Standards

**Python (PEP 8):**
```python
# Use descriptive names
def calculate_total_price(items: list[Item]) -> Decimal:
    """Calculate total price for all items including tax.

    Args:
        items: List of items to price

    Returns:
        Total price as Decimal
    """
    subtotal = sum(item.price for item in items)
    return subtotal * Decimal('1.08')  # 8% tax
```

**JavaScript/TypeScript (Airbnb Style Guide):**
```typescript
// Use const/let, not var
const maxRetries = 3;

// Prefer arrow functions
const users = rawData.map(user => ({
  id: user.id,
  name: user.full_name,
}));

// Use async/await over promises
async function fetchUser(id: string): Promise<User> {
  const response = await api.get(`/users/${id}`);
  return response.data;
}
```

### Automated Enforcement

We use automated tools to enforce standards:

- **Linting**: ESLint, Pylint, RuboCop (catches code issues)
- **Formatting**: Prettier, Black, gofmt (auto-formats code)
- **Type Checking**: TypeScript, MyPy (catches type errors)
- **Pre-commit Hooks**: Runs checks before each commit

```bash
# Run all checks
make lint

# Auto-fix formatting
make format

# Run pre-commit manually
pre-commit run --all-files
```

## Testing Requirements

### Test Coverage

- **Minimum coverage**: 80% for new code
- **Critical paths**: 100% coverage required
- **Test types**: Unit, integration, and E2E tests

### Writing Tests

**Example (Python pytest):**
```python
def test_calculate_total_price():
    """Test total price calculation includes tax."""
    items = [
        Item(price=Decimal('10.00')),
        Item(price=Decimal('20.00')),
    ]

    total = calculate_total_price(items)

    assert total == Decimal('32.40')  # 30.00 * 1.08


def test_calculate_total_price_empty_list():
    """Test that empty list returns zero."""
    assert calculate_total_price([]) == Decimal('0.00')


@pytest.mark.parametrize('price,tax,expected', [
    (Decimal('100.00'), Decimal('0.08'), Decimal('108.00')),
    (Decimal('50.00'), Decimal('0.05'), Decimal('52.50')),
])
def test_tax_calculation(price, tax, expected):
    """Test various tax calculations."""
    # Test implementation
```

**Running tests:**
```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_pricing.py

# Run with coverage
pytest --cov=src --cov-report=html

# Run integration tests only
pytest -m integration
```

### Test Best Practices

- **Test behavior, not implementation**
- **One assertion per test** (when possible)
- **Use descriptive test names**: `test_user_login_fails_with_invalid_password`
- **Arrange-Act-Assert** pattern
- **Mock external dependencies**

## Documentation

### What to Document

**Code-level documentation:**
- Public APIs and functions (docstrings/JSDoc)
- Complex algorithms or business logic
- Non-obvious decisions ("why" not "what")

**User-facing documentation:**
- README updates for new features
- CHANGELOG entries for user-facing changes
- API documentation for new endpoints
- Migration guides for breaking changes

### Documentation Style

**Good documentation:**
```python
def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
) -> Any:
    """Retry a function with exponential backoff.

    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts (default: 3)
        initial_delay: Initial delay in seconds (default: 1.0)
        backoff_factor: Multiplier for each retry (default: 2.0)

    Returns:
        Result of successful function call

    Raises:
        Exception: If all retries are exhausted

    Example:
        >>> result = retry_with_backoff(lambda: api.get_user(123))
    """
```

## Issue Reporting

### Bug Reports

Use the [Bug Report template](https://github.com/org/project/issues/new?template=bug_report.md).

**Include:**
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, version, etc.)
- Relevant logs or screenshots

**Example:**
```markdown
**Describe the bug**
API returns 500 error when creating user with empty email

**To Reproduce**
1. Send POST to /api/users with body: {"email": "", "name": "Test"}
2. Observe 500 response

**Expected behavior**
Should return 400 with validation error

**Environment**
- Version: 2.1.0
- OS: Ubuntu 22.04
- Browser: Chrome 120

**Logs**
```
ERROR: NullPointerException at UserService.java:42
```
```

### Feature Requests

Use the [Feature Request template](https://github.com/org/project/issues/new?template=feature_request.md).

**Include:**
- Problem statement (what need does this address?)
- Proposed solution
- Alternatives considered
- Impact on existing functionality

## Community

### Communication Channels

- **GitHub Discussions**: Questions, ideas, announcements
- **Discord**: Real-time chat ([join here](https://discord.gg/project))
- **Stack Overflow**: Tag questions with `project-name`
- **Twitter**: [@ProjectName](https://twitter.com/projectname)
- **Monthly Community Call**: First Tuesday of each month

### Getting Help

**Stuck? Ask for help!**

1. Check existing documentation
2. Search closed issues
3. Ask in GitHub Discussions or Discord
4. Tag your question with `help wanted` label

**Response times:**
- Critical bugs: Within 24 hours
- Feature requests: Within 1 week
- General questions: Within 3 days

## Legal

### Contributor License Agreement (CLA)

All contributors must sign our [Contributor License Agreement](CLA.md) before their pull request can be merged.

**Why we require a CLA:**
- Ensures we have rights to distribute your contribution
- Protects the project and all users
- Standard practice for open-source projects

**How to sign:**
- CLA bot will comment on your first PR
- Follow the link to sign electronically
- Only needs to be done once

### Developer Certificate of Origin (DCO)

All commits must be signed off to indicate you agree to the [Developer Certificate of Origin](https://developercertificate.org/).

**Sign-off commits:**
```bash
git commit -s -m "feat: add new feature"

# Or configure Git to sign off automatically:
git config --global format.signOff true
```

### License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Recognition

We value all contributions and recognize contributors in several ways:

- **CONTRIBUTORS.md**: All contributors listed
- **Release notes**: Contributors acknowledged in each release
- **All Contributors Bot**: Recognizes all types of contributions
- **Swag**: Top contributors receive project swag (stickers, t-shirts)

## Questions?

Still have questions? We're here to help!

- **GitHub Discussions**: https://github.com/org/project/discussions
- **Discord**: https://discord.gg/project
- **Email**: contribute@project.com

Thank you for contributing to [Project Name]! Every contribution, no matter how small, makes a difference.

---

**Version**: 1.0.0 | **Last Updated**: 2025-01-15 | **Maintained by**: @maintainer-team
