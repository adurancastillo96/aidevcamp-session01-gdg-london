---
name: Stack Tech
trigger: /stacktech
type: planning
description: Generate a Product Requirements Document with tech stack recommendations
agents:
  - product_manager
  - architect
skills:
  - write_specs
  - documentation
---

# /stacktech — Product Requirements Document Generation

When the user types `/stacktech <idea>`, generate a comprehensive Product Requirements Document (PRD) including tech stack recommendations.

## Execution Sequence

### Step 1: Requirements Interview

**Lead: @pm**

1. **@pm** analyzes the `<idea>` provided by the user.
2. **@pm** identifies functional and non-functional requirements.
3. **@pm** defines user personas and user stories.
4. If requirements are ambiguous, **@pm** asks the user for clarification.

### Step 2: Technical Feasibility

**Lead: @architect**

5. **@architect** evaluates technical feasibility of the requirements.
6. **@architect** recommends a tech stack based on:
   - Project requirements (performance, scale, complexity)
   - Team expertise and ecosystem maturity
   - Cost and licensing considerations
   - Long-term maintainability
7. **@architect** identifies technical risks and constraints.

### Step 3: Write PRD

**Lead: @pm**

8. **@pm** executes the `documentation` skill.
9. **@pm** copies the PRD template from `skills/documentation/resources/prd_template.md`.
10. **@pm** fills in all sections with the gathered requirements and tech stack recommendations.
11. **@pm** saves to `production_artifacts/product-requirement-document.md`.

> ⏸️ **PAUSE** — Present the PRD to the user and wait for explicit approval.

## Success Criteria

- [ ] All PRD sections completed
- [ ] Tech stack recommended with rationale
- [ ] User stories include acceptance criteria
- [ ] Risks and mitigations documented
- [ ] Saved to `production_artifacts/product-requirement-document.md`
- [ ] User approval obtained
