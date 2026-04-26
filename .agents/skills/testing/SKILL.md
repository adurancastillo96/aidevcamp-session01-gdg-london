---
name: Testing
description: Test strategy definition, test writing, and test execution
used_by:
  - engineer
  - devsecops
---

# Testing

## Purpose

Define test strategy, write comprehensive tests, and execute test suites to ensure code correctness and reliability.

## When To Use

- After implementing a new feature (`@engineer`)
- When auditing test coverage (`@devsecops`)
- When running the `/testing` workflow
- Before any deployment

## Instructions

### 1. Identify Test Types

| Type | Purpose | When |
|------|---------|------|
| Unit | Test individual functions/methods in isolation | Every function |
| Integration | Test interactions between components | Cross-module features |
| End-to-End | Test complete user flows | Critical paths |
| Security | Test input validation, auth, injection | External interfaces |
| Performance | Test response times, load handling | Before production |

### 2. Write Tests

#### Naming Convention
```
test_<function_name>_<scenario>_<expected_result>
```
Example: `test_create_user_with_duplicate_email_raises_conflict`

#### Test Structure (Arrange-Act-Assert)
```python
def test_example():
    # Arrange — set up test data
    input_data = {"key": "value"}

    # Act — execute the function under test
    result = function_under_test(input_data)

    # Assert — verify the result
    assert result.status == "success"
```

#### What To Test
- **Happy path**: Normal, expected inputs
- **Edge cases**: Empty inputs, boundary values, large inputs
- **Error cases**: Invalid inputs, missing data, network failures
- **Security cases**: Injection attempts, unauthorized access

### 3. Execute Tests

```bash
# Python (pytest)
uv run pytest -v --cov=. --cov-report=term-missing

# JavaScript (Vitest/Jest)
npm test -- --coverage
```

### 4. Report Results

```markdown
## Test Report

**Date**: YYYY-MM-DD
**Runner**: pytest / vitest / jest

| Metric | Value |
|--------|-------|
| Total tests | N |
| Passed | N |
| Failed | N |
| Skipped | N |
| Coverage | N% |

### Failed Tests
- `test_name`: Reason for failure
```

## Quality Gates

- [ ] All new code has corresponding tests
- [ ] Happy path and error cases covered
- [ ] All tests pass locally
- [ ] Coverage does not decrease
- [ ] No flaky tests (tests must be deterministic)
