---
name: Improve Skills
trigger: /improveskills
type: operations
description: Read the PRD and create or improve skills to match project needs
agents:
  - product_manager
  - architect
skills:
  - documentation
  - write_specs
---

# /improveskills — Skill Enhancement Pipeline

When the user types `/improveskills`, read the existing Product Requirements Document and analyze whether the current skills are sufficient. Create new skills or improve existing ones to match the project needs.

## Execution Sequence

### Step 1: Read PRD

**Lead: @pm**

1. **@pm** reads `production_artifacts/product-requirement-document.md`.
2. **@pm** extracts the list of capabilities the project requires.
3. **@pm** maps each capability to existing skills in `skills/`.

### Step 2: Gap Analysis

**Lead: @architect**

4. **@architect** compares required capabilities against existing skills.
5. **@architect** identifies:
   - **Missing skills**: Capabilities with no matching skill.
   - **Incomplete skills**: Existing skills that need additional instructions, scripts, or resources.
   - **Outdated skills**: Skills referencing deprecated tools or patterns.
6. **@architect** produces a gap analysis report.

### Step 3: Create/Update Skills

**Lead: @architect**

7. For each **missing skill**:
   - Create `skills/<skill_name>/SKILL.md` with proper YAML frontmatter.
   - Add `scripts/`, `resources/`, or `examples/` directories as needed.
   - Update `used_by:` field with the appropriate agents.

8. For each **incomplete skill**:
   - Add missing instructions, templates, or resources.
   - Update the YAML frontmatter if agent assignments change.

9. For each **outdated skill**:
   - Update tool references and instructions.
   - Verify examples still work.

### Step 4: Update Cross-References

**Lead: @pm**

10. **@pm** updates `AGENTS.md` if new skills are assigned to agents.
11. **@pm** updates agent files (`agents/*.md`) to include new skills in their `skills:` list.
12. **@pm** updates `SYSTEM.md` directory map if new skill directories were created.

### Step 5: Validate

**Lead: @pm**

13. **@pm** verifies all skills referenced in agent files exist.
14. **@pm** verifies all `used_by:` references in skills match agent files.
15. **@pm** confirms no orphaned skills (skills not referenced by any agent).

## Success Criteria

- [ ] PRD read and capabilities extracted
- [ ] Gap analysis completed
- [ ] New skills created with proper SKILL.md + frontmatter
- [ ] Existing skills updated where needed
- [ ] Cross-references consistent (agents ↔ skills)
- [ ] SYSTEM.md directory map updated
