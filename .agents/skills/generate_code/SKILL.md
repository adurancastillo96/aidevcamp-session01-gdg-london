---
name: Generate Code
description: Code generation following architecture decisions and coding standards
used_by:
  - engineer
---

# Generate Code

## Purpose

Generate production-ready code that follows approved architecture, coding standards, and best practices.

## When To Use

- Implementing a feature from an approved specification
- Scaffolding a new project or component
- Refactoring existing code
- Fixing bugs with proper test coverage

## Instructions

### 1. Read the Spec

- Review the approved Technical Specification.
- Understand the architecture defined by `@architect`.
- Identify the files and components to create or modify.

### 2. Follow Standards

- Apply all rules from `rules/global.md`.
- Use type hints/annotations.
- Write meaningful docstrings/comments for public interfaces.
- Handle errors explicitly — no silent failures.

### 3. Implementation Patterns

#### File Structure
- Group related files by feature or domain, not by type.
- Keep files focused — one class/module per file where practical.
- Use clear, descriptive filenames.

#### Code Quality
- Functions should do one thing and do it well.
- Avoid deep nesting — use early returns.
- Prefer immutability where possible.
- Use constants for magic values.

#### Error Handling
```python
# Good
try:
    result = perform_action()
except SpecificError as e:
    logger.error(f"Action failed: {e}")
    raise

# Bad
try:
    result = perform_action()
except:
    pass
```

### 4. Testing

- Write tests alongside the implementation (not after).
- Each new function/method should have at least one test.
- Test both the happy path and error cases.

### 5. Output

- Place code in the appropriate directory per project structure.
- Include imports, type hints, and docstrings.
- Run linting before marking as complete.

## Quality Gates

- [ ] Follows approved architecture from `@architect`
- [ ] Type hints on all function signatures
- [ ] Docstrings on all public interfaces
- [ ] Error handling on all external calls
- [ ] Tests written and passing
- [ ] Linting passes with zero warnings
- [ ] No hardcoded secrets or magic values
