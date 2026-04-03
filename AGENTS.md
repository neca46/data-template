# AGENTS.md

## Project Overview

Template for Python repositories using `uv`, `mise`, `ruff`, `ty`, and `pytest`.

## Code Layout

- `src/data_template/`: application code
- `tests/`: test suite
- `.github/workflows/ci.yml`: CI configuration
- `mise.toml`: local developer tasks and environment loading

## Common Commands

- `uv run python src/data_template/main.py`
- `mise run lint`
- `mise run lint-fix`
- `mise run format`
- `mise run format-check`
- `mise run typecheck`
- `mise run test`
- `mise run check`

## Environment

- Environment files live in `.env/<env>/.env`
- Default environment is `staging`
- Override with `MISE_ENV=production mise run test`
- For longer sessions, use `export MISE_ENV=staging`

## Conventions

- Keep the template lightweight and easy to understand
- Prefer small, clear changes over abstraction
- Use conventional PR titles such as `feat:`, `fix:`, and `chore:`
- Keep CI read-only and use `uv` directly there
