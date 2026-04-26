# Global Workspace Rules

These rules apply to **all agents** at all times, regardless of workflow or task.

---

## 1. Code Standards

- Write clean, readable, self-documenting code.
- Use meaningful, descriptive naming for variables, functions, classes, and files.
- Follow **DRY** (Don't Repeat Yourself), **SOLID**, and **KISS** principles.
- Prefer composition over inheritance.
- Keep functions small and focused on a single responsibility.
- Use type hints/annotations where the language supports them.
- Handle errors explicitly — never silently swallow exceptions.

## 2. Documentation

- All public APIs, functions, and classes must have docstrings or equivalent documentation.
- Maintain a `README.md` at the project root with setup instructions, usage, and architecture overview.
- Add inline comments only for non-obvious logic — code should be self-explanatory first.
- Keep documentation up to date when code changes.

## 3. Version Control

- Write commit messages following [Conventional Commits](https://www.conventionalcommits.org/) format.
- Keep pull requests small and focused on a single concern.
- Never commit secrets, API keys, tokens, or credentials to the repository.
- Use `.gitignore` to exclude build artifacts, virtual environments, and sensitive files.

## 4. Testing

- All new features must include tests (unit at minimum).
- Tests must pass before marking any task as complete.
- Aim for meaningful coverage — test behavior, not implementation details.
- Include edge cases and error paths in test suites.

## 5. Security

- Audit dependencies regularly for known vulnerabilities.
- Never hardcode credentials, API keys, or secrets in source code.
- Use environment variables (`.env` file, never committed) for sensitive configuration.
- Validate and sanitize all external inputs.
- Follow the principle of least privilege for all access controls.

## 6. Environment

- Use `uv` for Python package management and virtual environments.
- Store secrets in `.env` (listed in `.gitignore`).
- Pin dependency versions for reproducible builds.
- Document required environment variables in `README.md` or `.env.example`.

## 7. Artifacts

- Generated documents (specs, PRDs, reports) go to `production_artifacts/`.
- Never overwrite an existing artifact without explicit user approval.
- Artifacts must include a header with title, date, author (agent handle), and version.

## 8. Communication

- All outputs must be in **English**.
- Use clear, professional language in all generated documentation.
- When uncertain about requirements, **ask for clarification** rather than making assumptions.
- Report progress and blockers transparently.
