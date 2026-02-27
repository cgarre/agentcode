# Repository Guidelines

## Project Structure & Module Organization
This repository is in an early stage and currently has no source tree. The top level contains:

- `README.md`: brief project blurb.
- `CLAUDE.md`: guidance for agent tooling.
- `sort_list.py`: a standalone script.

As the project grows, prefer a conventional layout such as `src/` for application code, `tests/` for automated tests, and `assets/` for static resources. Keep new modules grouped by domain (for example, `src/agents/` or `src/utils/`).

## Build, Test, and Development Commands
There is no formal build or test pipeline yet. When adding tooling, document it here and in `README.md`. Example commands to introduce when applicable:

- `python -m pytest`: run unit tests in `tests/`.
- `python -m black .`: format Python code.

## Coding Style & Naming Conventions
Until a formatter is added, follow standard Python conventions:

- Indentation: 4 spaces, no tabs.
- Naming: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.
- Keep scripts in the root minimal; move reusable code into `src/`.

## Testing Guidelines
No testing framework is configured. If you add tests, prefer `pytest` and place files under `tests/` using `test_<module>.py` naming. Keep tests small and deterministic, and include new test commands in this document.

## Commit & Pull Request Guidelines
There is no established commit convention yet. Use clear, imperative commit messages (e.g., "Add agent registry") and keep commits focused. For pull requests, include:

- A short summary of changes.
- Any relevant issue links.
- Manual test notes or screenshots when behavior changes.

## Security & Configuration Tips
Avoid committing secrets or local configuration. If credentials are needed later, use environment variables and document them in `README.md`.
