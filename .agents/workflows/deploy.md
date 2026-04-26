---
name: Deploy
trigger: /deploy
type: operations
description: Deploy application to target environment with security validation
agents:
  - cloudengineer
  - devsecops
skills:
  - deploy_cloud
  - deploy_app
  - security_audit
  - testing
---

# /deploy — Deployment Pipeline

When the user types `/deploy <target>`, orchestrate the deployment of the application to the specified target environment.

## Execution Sequence

### Step 1: Pre-Deployment Checks

**Lead: @devsecops**

1. **@devsecops** executes the `testing` skill — run the full test suite.
2. **@devsecops** executes the `security_audit` skill — scan for vulnerabilities.
3. If any check fails, **STOP** and report the issues.

### Step 2: Infrastructure Provisioning

**Lead: @cloudengineer**

4. **@cloudengineer** reviews the target environment requirements.
5. **@cloudengineer** executes the `deploy_cloud` skill to provision/update infrastructure.
6. **@cloudengineer** verifies all resources are healthy.

### Step 3: Application Deployment

**Lead: @cloudengineer**

7. **@cloudengineer** executes the `deploy_app` skill:
   - Build the application
   - Deploy to the target environment
   - Run smoke tests

### Step 4: Post-Deployment Validation

**Lead: @devsecops**

8. **@devsecops** verifies:
   - Application is accessible
   - Health check endpoints respond
   - Security headers are configured
   - Monitoring and logging are active
   - No errors in startup logs

### Step 5: Report

**Lead: @cloudengineer**

9. **@cloudengineer** generates a deployment report:
   - Target environment
   - Deployed version/commit
   - Infrastructure changes (if any)
   - Validation results
   - Rollback instructions

## Success Criteria

- [ ] All tests pass
- [ ] Security audit clean
- [ ] Infrastructure provisioned/updated
- [ ] Application deployed and accessible
- [ ] Post-deployment validation passed
- [ ] Deployment report generated
