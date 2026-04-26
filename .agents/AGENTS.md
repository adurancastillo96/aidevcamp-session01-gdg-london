# Agent Registry

> This file is an overview. Detailed definitions for each agent live in `agents/<name>.md`.

## Agents

| Handle | Name | Role | Primary Skills |
|--------|------|------|----------------|
| `@pm` | Product Manager | Orchestrator & product authority | `write_specs`, `documentation` |
| `@architect` | Software Architect | System design & architecture decisions | `write_specs`, `code_reviewer` |
| `@engineer` | Full-Stack Engineer | Feature implementation & testing | `generate_code`, `testing` |
| `@cloudengineer` | Cloud Engineer | Cloud infrastructure & IaC | `deploy_cloud`, `deploy_app` |
| `@devsecops` | DevSecOps Engineer | CI/CD, security & compliance | `security_audit`, `deploy_app`, `testing` |

## How Agents Collaborate

1. **`@pm`** is the orchestrator. Workflows begin and end with `@pm` validating deliverables against requirements.
2. **`@architect`** makes binding technical decisions. All structural changes must be reviewed by `@architect`.
3. **`@engineer`** translates approved designs into production-ready code.
4. **`@cloudengineer`** handles infrastructure provisioning and cloud deployment.
5. **`@devsecops`** owns all security concerns and CI/CD pipeline integrity.

## Referencing Agents

- In workflow steps, reference agents by their handle: `@pm`, `@architect`, etc.
- In skill `used_by:` fields, use the agent filename (without extension): `product_manager`, `architect`, etc.
