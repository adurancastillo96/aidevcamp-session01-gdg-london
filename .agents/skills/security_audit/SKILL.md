---
name: Security Audit
description: Security scanning, vulnerability assessment, and hardening recommendations
used_by:
  - devsecops
---

# Security Audit

## Purpose

Perform comprehensive security assessments across the codebase, dependencies, infrastructure, and deployment pipeline.

## When To Use

- Before any production deployment
- During the `/audit` workflow
- When new dependencies are added
- After a security incident
- As part of the `/startcycle` workflow (step 7)

## Instructions

### 1. Dependency Scanning

Check all dependencies for known vulnerabilities:

```bash
# Python
uv run pip-audit
# or
uv run safety check

# Node.js
npm audit

# Container
trivy image <image>:<tag>
```

**Action**: Any critical or high severity CVE must be resolved before deployment.

### 2. Secrets Detection

Scan the repository for accidentally committed secrets:

```bash
# Using truffleHog
trufflehog filesystem . --only-verified

# Using gitleaks
gitleaks detect --source .
```

**Action**: Any detected secret must be rotated immediately and removed from git history.

### 3. Static Analysis (SAST)

Run static analysis tools appropriate to the language:

| Language | Tool |
|----------|------|
| Python | `bandit`, `semgrep` |
| JavaScript | `eslint-plugin-security`, `semgrep` |
| Go | `gosec` |
| General | `semgrep`, `SonarQube` |

### 4. Configuration Review

- [ ] `.env` is in `.gitignore`
- [ ] No default passwords or API keys
- [ ] CORS policy is restrictive (not `*`)
- [ ] CSP headers configured
- [ ] HTTPS enforced
- [ ] Rate limiting enabled on public endpoints
- [ ] Authentication tokens have expiry

### 5. Infrastructure Security

- [ ] IAM roles follow least privilege
- [ ] Network policies restrict unnecessary traffic
- [ ] Encryption at rest and in transit
- [ ] Firewall rules reviewed
- [ ] Logging enabled (no PII in logs)

### 6. Report

```markdown
## Security Audit Report

**Date**: YYYY-MM-DD
**Auditor**: @devsecops

### Summary
| Category | Status | Issues |
|----------|--------|--------|
| Dependencies | ✅/⚠️/❌ | N |
| Secrets | ✅/⚠️/❌ | N |
| SAST | ✅/⚠️/❌ | N |
| Configuration | ✅/⚠️/❌ | N |
| Infrastructure | ✅/⚠️/❌ | N |

### Critical Findings
1. [Finding description and remediation]

### Recommendations
1. [Improvement suggestion]

### Verdict
- [ ] Approved for deployment
- [ ] Blocked — critical issues must be resolved
```

## Quality Gates

- [ ] Zero critical/high CVEs in dependencies
- [ ] No secrets in codebase
- [ ] SAST findings addressed
- [ ] Configuration hardened
- [ ] Report generated and filed
