---
name: Start Cycle
trigger: /startcycle
type: development
description: Full MVP development pipeline from idea to working local product
agents:
  - product_manager
  - architect
  - engineer
  - devsecops
skills:
  - write_specs
  - generate_code
  - code_reviewer
  - testing
  - security_audit
  - deploy_app
---

# /startcycle — Full MVP Development Pipeline

When the user types `/startcycle <idea>`, orchestrate the full development process using the agents and skills defined in this framework.

## Execution Sequence

### Phase 1: Requirements & Specification

**Lead: @pm**

1. **@pm** analyzes the `<idea>` provided by the user.
2. **@pm** executes the `write_specs` skill to generate a Technical Specification.
3. **@pm** saves the spec to `production_artifacts/Technical_Specification.md`.

> ⏸️ **PAUSE** — Present the spec to the user and wait for explicit approval before continuing.

### Phase 2: Architecture & Design

**Lead: @architect**

4. **@architect** reviews the approved spec.
5. **@architect** designs the system architecture (components, data model, APIs).
6. **@architect** creates an Architecture Decision Record (ADR) if significant decisions are made.
7. **@architect** defines the project structure and file organization.

### Phase 3: Implementation

**Lead: @engineer**

8. **@engineer** reads the approved spec and architecture.
9. **@engineer** executes the `generate_code` skill to implement the features.
10. **@engineer** writes tests alongside implementation using the `testing` skill.
11. **@engineer** ensures all tests pass locally.

### Phase 4: Review & Security

**Lead: @architect** (review) + **@devsecops** (security)

12. **@architect** executes the `code_reviewer` skill on the implementation.
13. **@devsecops** executes the `security_audit` skill.
14. If issues are found, **@engineer** fixes them and re-submits.
15. Repeat until both `@architect` and `@devsecops` approve.

### Phase 5: Local MVP

**Lead: @pm**

16. **@devsecops** sets up any required CI/CD configuration.
17. **@engineer** ensures the application runs locally (`uv run` / `npm run dev`).
18. **@pm** validates the deliverable against the original specification.
19. **@pm** reports completion to the user.

## Success Criteria

- [ ] Technical Specification approved by user
- [ ] Architecture documented
- [ ] All code implemented with tests
- [ ] Code review passed
- [ ] Security audit passed
- [ ] Application runs locally
- [ ] PM validates against spec
