# Contributing to InsaBot for Woosong

Thanks for your interest in contributing! This guide covers how to set up your environment, the standards we follow, and how to get your change merged. By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- 🐛 **Report bugs** — open a [Bug Report](../../issues/new?template=bug_report.yml).
- 💡 **Request features** — open a [Feature Request](../../issues/new?template=feature_request.yml).
- 📝 **Improve docs** — fixes to `docs/`, the README, or code comments are always welcome.
- 🔧 **Submit code** — see the workflow below.

> Found a security vulnerability? **Do not** open a public issue — follow [SECURITY.md](SECURITY.md).

## Development setup

This is a polyglot monorepo: a **FastAPI** backend (`backend/`) and a **React + Vite** frontend (`frontend/`).

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/<repo>.git
cd insabot-for-woosong

# 2. Environment
cp .env.example .env

# 3. Frontend deps (npm workspace)
npm install

# 4. Backend deps (virtual environment recommended)
python -m venv backend/.venv
backend/.venv/Scripts/activate          # Windows
# source backend/.venv/bin/activate     # macOS / Linux
pip install -r backend/requirements.txt -r backend/requirements-dev.txt
```

Run the app:

```bash
uvicorn app.main:app --reload --app-dir backend   # backend → http://localhost:8000
npm run dev                                        # frontend → http://localhost:5173
```

## Branching & commits

- Branch off `main`: `git checkout -b <type>/<short-description>` (e.g., `feat/handoff-email`, `fix/lang-detect-kana`).
- Write clear, imperative commit messages: `Add Vietnamese checklist translations`.
- Keep commits focused; group unrelated changes into separate PRs.

## Coding standards

Run these locally before pushing — CI enforces all of them.

### Frontend (`frontend/`)

```bash
npm run format:check     # Prettier
npm run lint             # ESLint
npm run build            # tsc -b && vite build (typecheck + build)
npm run test:frontend    # Vitest
```

- TypeScript `strict` mode is on — no `any` escape hatches without justification.
- Use the `@/` path alias for `src` imports.
- User-facing strings go through i18n (`frontend/src/i18n`), not hardcoded.

### Backend (`backend/`)

```bash
ruff check .             # Lint
black --check .          # Format
pytest -q                # Tests
```

- Format with **Black**, lint with **Ruff** (line length 100).
- **Answers must stay source-grounded.** Don't introduce outside-knowledge generation paths; weak evidence must hit the verified fallback and office routing. See `app/rag/pipeline.py` and `app/security/policy.py`.
- Add or update tests for behavior changes. Tests must pass against SQLite and the deterministic provider (no Postgres/Ollama required in CI).
- Mirror new settings in `.env.example` **and** `docker-compose.yml`.

## Pull request process

1. Ensure all checks above pass locally.
2. Update relevant docs (`docs/`, `README.md`, `CLAUDE.md`) when behavior or commands change.
3. Open a PR against `main` and fill out the PR template. Link any related issues (`Closes #123`).
4. Keep PRs reviewable — smaller is better. Explain the "why," not just the "what."
5. A maintainer will review; address feedback by pushing follow-up commits.

## Reporting issues

Use the issue templates and include reproduction steps, expected vs. actual behavior, and environment details (OS, Node/Python versions, provider). The more specific, the faster we can help.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
