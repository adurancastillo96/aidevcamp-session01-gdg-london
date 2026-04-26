---
name: Code Reviewer
description: Multi-dimensional code review for correctness, security, performance, and style
used_by:
  - architect
  - devsecops
---

# Code Reviewer

## Purpose

Perform thorough, multi-dimensional code reviews that catch bugs, enforce standards, and improve code quality before merging.

## When To Use

- After `@engineer` completes a feature implementation
- Before merging any code changes
- During architecture reviews of structural changes
- When auditing existing codebases

## Instructions

### Review Dimensions

Evaluate code across these 7 dimensions, scoring each as ✅ Pass, ⚠️ Warning, or ❌ Fail:

#### 1. Correctness
- Does the code do what the spec says?
- Are edge cases handled?
- Are there off-by-one errors, null checks, or race conditions?

#### 2. Architecture Alignment
- Does the implementation follow the approved design?
- Are component boundaries respected?
- Is the separation of concerns clean?

#### 3. Performance
- Are there obvious N+1 queries, unnecessary loops, or memory leaks?
- Is caching used where appropriate?
- Are database queries optimized?

#### 4. Security
- Is input validation present on all external inputs?
- Are there hardcoded secrets or credentials?
- Are SQL injections, XSS, or CSRF vulnerabilities present?
- → Delegate deep security review to `@devsecops` if needed.

#### 5. Readability & Style
- Are variable and function names clear and descriptive?
- Is the code self-documenting?
- Do docstrings and comments add value?
- Is formatting consistent?

#### 6. DRY & Maintainability
- Is there duplicated code?
- Are abstractions appropriate (not over-engineered)?
- Would a new developer understand this code?

#### 7. Test Coverage
- Are tests present for new code?
- Do tests cover happy path and error cases?
- Are tests readable and maintainable?

### Review Output Format

```markdown
## Code Review: [Feature/File Name]

**Reviewer**: @architect / @devsecops
**Date**: YYYY-MM-DD

| Dimension | Score | Notes |
|-----------|-------|-------|
| Correctness | ✅/⚠️/❌ | ... |
| Architecture | ✅/⚠️/❌ | ... |
| Performance | ✅/⚠️/❌ | ... |
| Security | ✅/⚠️/❌ | ... |
| Readability | ✅/⚠️/❌ | ... |
| DRY | ✅/⚠️/❌ | ... |
| Tests | ✅/⚠️/❌ | ... |

### Issues Found
1. [Severity] Description and suggested fix.

### Verdict
- [ ] Approved
- [ ] Approved with minor changes
- [ ] Changes requested
- [ ] Rejected
```

## Scripts

See `scripts/review_checklist.md` for a reusable quick-reference checklist.
