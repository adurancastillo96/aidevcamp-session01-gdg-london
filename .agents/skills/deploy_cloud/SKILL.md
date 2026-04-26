---
name: Deploy Cloud
description: Cloud infrastructure provisioning and management via IaC
used_by:
  - cloudengineer
---

# Deploy Cloud

## Purpose

Provision, update, and manage cloud infrastructure using Infrastructure as Code (IaC) principles.

## When To Use

- Setting up new cloud infrastructure for a project
- Modifying existing infrastructure (scaling, new services)
- Running the `/deploy` workflow
- Migrating between cloud providers

## Instructions

### 1. Assess Requirements

- Identify the compute, storage, networking, and security needs.
- Determine the target cloud provider (GCP, AWS, Azure, other).
- Estimate expected load and scaling requirements.
- Identify compliance or regulatory constraints.

### 2. Define Infrastructure

Choose the appropriate IaC tool and define resources:

#### Terraform Example
```hcl
resource "google_cloud_run_v2_service" "app" {
  name     = var.service_name
  location = var.region

  template {
    containers {
      image = var.container_image
    }
  }
}
```

#### Pulumi Example (Python)
```python
import pulumi_gcp as gcp

service = gcp.cloudrunv2.Service("app",
    location="us-central1",
    template=gcp.cloudrunv2.ServiceTemplateArgs(
        containers=[gcp.cloudrunv2.ServiceTemplateContainerArgs(
            image="gcr.io/project/image:latest",
        )],
    ),
)
```

### 3. Plan & Review

```bash
# Terraform
terraform plan -out=tfplan

# Pulumi
pulumi preview
```

- Review the plan output carefully.
- Confirm no unintended resource deletions or modifications.
- Get approval from `@devsecops` for security-sensitive changes.

### 4. Apply

```bash
# Terraform
terraform apply tfplan

# Pulumi
pulumi up
```

### 5. Verify

- [ ] All resources created/updated successfully
- [ ] Networking and DNS configured correctly
- [ ] IAM permissions follow least privilege
- [ ] Monitoring and logging enabled
- [ ] Cost estimate reviewed

### 6. Document

- Update infrastructure documentation.
- Record any manual steps required.
- Update runbooks if operational procedures changed.

## Quality Gates

- [ ] IaC files version-controlled
- [ ] Plan reviewed before apply
- [ ] No manual console changes in production
- [ ] IAM follows least privilege
- [ ] Monitoring enabled on all resources
