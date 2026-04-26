---
name: Testing
trigger: /testing
type: development
description: Run and create tests in the code folder
agents:
  - engineer
  - devsecops
skills:
  - testing
  - code_reviewer
---

# /testing — Test Suite Execution

When the user types `/testing`, analyze the codebase, identify gaps in test coverage, write missing tests, and execute the full test suite.

## Execution Sequence

### Step 1: Analyze Coverage

**Lead: @engineer**

1. **@engineer** scans the codebase to identify all testable code.
2. **@engineer** runs existing tests to establish baseline coverage.
3. **@engineer** identifies untested functions, edge cases, and error paths.

### Step 2: Write Missing Tests

**Lead: @engineer**

4. **@engineer** writes unit tests for uncovered functions using the `testing` skill.
5. **@engineer** writes integration tests for cross-component interactions.
6. **@engineer** adds edge case and error path tests.

### Step 3: Security Test Review

**Lead: @devsecops**

7. **@devsecops** reviews test coverage for security-relevant code:
   - Input validation tests
   - Authentication/authorization tests
   - Injection prevention tests
8. **@devsecops** adds any missing security test cases.

### Step 4: Execute & Report

**Lead: @engineer**

9. **@engineer** runs the full test suite.
10. **@engineer** generates a test report (see `testing` skill for format).
11. Report includes: total tests, pass/fail, coverage percentage, and any failures.

## Success Criteria

- [ ] All existing tests still pass
- [ ] New tests added for uncovered code
- [ ] Security-relevant tests reviewed by @devsecops
- [ ] Coverage does not decrease
- [ ] Test report generated
