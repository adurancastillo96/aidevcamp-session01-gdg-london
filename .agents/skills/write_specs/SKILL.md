---
name: Write Specs
description: Generate technical specifications, user stories, and acceptance criteria
used_by:
  - product_manager
  - architect
---

# Write Specs

## Purpose

Generate structured technical specifications that translate user requirements into actionable engineering documents.

## When To Use

- A new feature or project is requested
- Requirements need to be formalized before implementation
- User stories and acceptance criteria are needed for sprint planning

## Instructions

### 1. Gather Requirements

- Interview the user (or read provided context) to understand the goal.
- Identify functional requirements (what the system must do).
- Identify non-functional requirements (performance, security, scalability).
- List assumptions and constraints.

### 2. Define Scope

- Clearly state what is **in scope** and **out of scope**.
- Identify dependencies on other systems or services.
- Define success criteria.

### 3. Write the Specification

Structure the document with these sections:

```markdown
# [Feature/Project Name] — Technical Specification

## Executive Summary
Brief overview of what this spec covers.

## Goals
What this feature/project aims to achieve.

## Non-Goals
What is explicitly out of scope.

## Technical Design
### Architecture
### Data Model
### API Contracts
### UI/UX (if applicable)

## User Stories
- As a [role], I want [capability] so that [benefit].

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Milestones
| Phase | Deliverable | Estimated Effort |
|-------|------------|-----------------|
| 1     | ...        | ...             |

## Open Questions
Items needing user clarification.
```

### 4. Output

- Save to `production_artifacts/Technical_Specification.md`
- **PAUSE** and request user approval before any implementation begins.

## Quality Gates

- [ ] All user requirements addressed
- [ ] Non-goals explicitly stated
- [ ] At least 3 acceptance criteria defined
- [ ] Milestones include effort estimates
- [ ] Open questions documented (if any)
