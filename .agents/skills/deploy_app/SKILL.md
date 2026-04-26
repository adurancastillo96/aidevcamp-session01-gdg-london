---
name: Deploy App
description: Application deployment to any target environment
used_by:
  - cloudengineer
  - devsecops
---

# Deploy App

## Purpose

Deploy an application to a target environment with proper build, validation, and smoke testing.

## When To Use

- Deploying to development, staging, or production environments
- Setting up initial deployment pipelines
- Performing rollback of a failed deployment

## Instructions

### 1. Pre-Deployment Checks

- [ ] All tests pass (invoke `testing` skill)
- [ ] Security audit clean (invoke `security_audit` skill or confirm with `@devsecops`)
- [ ] Build succeeds locally
- [ ] Environment variables configured
- [ ] Dependencies locked (lock file up to date)

### 2. Build

```bash
# Python
uv build

# Node.js
npm run build

# Docker
docker build -t <image>:<tag> .
```

### 3. Deploy

Follow the deployment strategy appropriate for the target:

| Target | Method |
|--------|--------|
| Local | `uv run` / `npm run dev` |
| Docker | `docker compose up` |
| Cloud Run | `gcloud run deploy` |
| Kubernetes | `kubectl apply` / Helm |
| Vercel/Netlify | Git push (auto-deploy) |
| GitHub Pages | GitHub Actions workflow |

### 4. Post-Deployment Validation

- [ ] Application is accessible at the target URL
- [ ] Health check endpoint responds with 200
- [ ] Core functionality smoke test passes
- [ ] Logs show no errors on startup
- [ ] Monitoring/alerting is active

### 5. Rollback Plan

If deployment fails:
1. Identify the failure (logs, health checks)
2. Rollback to previous version
3. Document the failure cause
4. Fix and re-deploy

## Quality Gates

- [ ] Pre-deployment checks pass
- [ ] Build succeeds
- [ ] Post-deployment validation passes
- [ ] Rollback plan documented
