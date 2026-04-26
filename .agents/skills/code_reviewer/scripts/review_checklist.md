# Code Review Quick Checklist

Use this checklist for rapid reviews. For full review methodology, see `SKILL.md`.

## Pre-Review
- [ ] Read the related spec/ticket
- [ ] Understand the intended behavior

## Correctness
- [ ] Logic matches the specification
- [ ] Edge cases handled (nulls, empty inputs, boundaries)
- [ ] No race conditions or deadlocks
- [ ] Error paths return meaningful messages

## Architecture
- [ ] Follows approved design from `@architect`
- [ ] No unauthorized structural changes
- [ ] Clean separation of concerns

## Performance
- [ ] No unnecessary loops or N+1 queries
- [ ] Expensive operations are lazy/cached
- [ ] Memory-efficient data structures

## Security
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on external inputs
- [ ] SQL/injection vectors checked
- [ ] Auth/authz correctly enforced

## Code Quality
- [ ] Descriptive naming (variables, functions, files)
- [ ] Type hints present
- [ ] Docstrings on public interfaces
- [ ] No dead code or commented-out blocks
- [ ] No duplicated logic

## Tests
- [ ] Unit tests for new functions
- [ ] Error cases tested
- [ ] Tests are readable and maintainable
- [ ] All tests pass locally
