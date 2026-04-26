---
name: Documentation
description: Technical documentation generation and maintenance (PRDs, READMEs, changelogs)
used_by:
  - product_manager
---

# Documentation

## Purpose

Generate and maintain structured project documentation including Product Requirements Documents, READMEs, changelogs, and architectural guides.

## When To Use

- Starting a new project (README, PRD)
- Running the `/stacktech` workflow (PRD generation)
- After completing a feature (changelog update)
- When onboarding documentation is outdated

## Instructions

### 1. Identify Documentation Need

| Document | When | Template |
|----------|------|----------|
| PRD | New project/feature planning | `resources/prd_template.md` |
| README | Project initialization | Standard format |
| Changelog | After each release/feature | Keep-a-Changelog format |
| ADR | After architecture decisions | See `@architect` |
| API Docs | After API changes | OpenAPI/Swagger |

### 2. Write the Document

- Use the appropriate template from `resources/`.
- Follow the structure exactly — consistency across documents is critical.
- Include all required sections; mark optional sections as N/A if not applicable.
- Use clear, professional English.

### 3. PRD Generation (for `/stacktech` workflow)

1. Read user requirements.
2. Copy the PRD template from `resources/prd_template.md`.
3. Fill in all sections with project-specific content.
4. Output to `production_artifacts/product-requirement-document.md`.
5. **PAUSE** for user review.

### 4. README Structure

```markdown
# Project Name

Brief description.

## Quick Start
## Prerequisites
## Installation
## Usage
## Architecture
## Contributing
## License
```

## Resources

- `resources/prd_template.md` — Product Requirements Document template

## Quality Gates

- [ ] All required sections completed
- [ ] Language is clear and professional
- [ ] Technical accuracy verified
- [ ] No placeholder text remaining
- [ ] Saved to correct output location
