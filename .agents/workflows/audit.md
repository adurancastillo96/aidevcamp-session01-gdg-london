---
name: Audit
trigger: /audit
type: operations
description: Cross-cutting project health check across architecture, security, and documentation
agents:
  - product_manager
  - architect
  - devsecops
skills:
  - code_reviewer
  - security_audit
  - documentation
---

# /audit — Project Health Check

When the user types `/audit`, perform a comprehensive cross-cutting audit of the project covering architecture alignment, security posture, dependency health, and documentation completeness.

## Execution Sequence

### Step 1: Architecture Review

**Lead: @architect**

1. **@architect** reviews the codebase for architecture alignment using the `code_reviewer` skill.
2. **@architect** checks:
   - Component boundaries are respected
   - Separation of concerns is clean
   - No unauthorized architectural drift
   - Design patterns are applied consistently
3. **@architect** documents findings.

### Step 2: Security Audit

**Lead: @devsecops**

4. **@devsecops** executes the `security_audit` skill:
   - Dependency vulnerability scan
   - Secrets detection
   - Static analysis
   - Configuration review
5. **@devsecops** documents findings.

### Step 3: Dependency Health

**Lead: @devsecops**

6. **@devsecops** checks:
   - All dependencies are up to date
   - No deprecated packages in use
   - Lock file is consistent
   - License compliance (no GPL in proprietary projects, etc.)
7. **@devsecops** documents findings.

### Step 4: Documentation Review

**Lead: @pm**

8. **@pm** reviews:
   - README is up to date
   - API documentation matches implementation
   - CHANGELOG reflects recent changes
   - Inline code comments are accurate
9. **@pm** documents findings.

### Step 5: Generate Audit Report

**Lead: @pm**

10. **@pm** consolidates all findings into a report.
11. **@pm** saves to `production_artifacts/audit_report.md`.

```markdown
# Project Audit Report

**Date**: YYYY-MM-DD
**Auditors**: @architect, @devsecops, @pm

## Summary

| Area | Status | Issues |
|------|--------|--------|
| Architecture | ✅/⚠️/❌ | N |
| Security | ✅/⚠️/❌ | N |
| Dependencies | ✅/⚠️/❌ | N |
| Documentation | ✅/⚠️/❌ | N |

## Findings
### Architecture
### Security
### Dependencies
### Documentation

## Action Items
| # | Finding | Severity | Owner | Deadline |
|---|---------|----------|-------|----------|
| 1 | ... | ... | ... | ... |
```

## Success Criteria

- [ ] Architecture review completed
- [ ] Security audit completed
- [ ] Dependency health checked
- [ ] Documentation reviewed
- [ ] Audit report generated in `production_artifacts/audit_report.md`
