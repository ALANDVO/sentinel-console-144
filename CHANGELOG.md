# Changelog

## 1.4.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.3.0 — work-in-progress checkpoint

### Added
- Claude Code skill package: `skills/hallmark/SKILL.md` with absolute GitHub URLs
- Skill references: `skills/hallmark/references/{design-tokens.md, rules.json, README.md}`
- Skill package tests: `backend/tests/test_skill_package.py` (5 passing tests)

### Fixed
- Relative `../` paths in SKILL.md replaced with absolute GitHub URLs, fixing broken links after `npx skills add`

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Added
- Anti-AI-slop design rule engine (`backend/rules/engine.py`)
- Rule configuration with 10 ban patterns and 2 require patterns (`backend/config/rules.json`)
- Lint API endpoints: `GET /api/lint/rules`, `POST /api/lint/css`, `POST /api/lint/file` (`backend/api/lint.py`)
- Unit test for rule engine (`backend/test_lint.py`)

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Added
- FastAPI backend with `/api/health` and `/api/version` endpoints
- React + Vite frontend with Sentinel Console landing page
- CORS configuration for frontend-backend communication
- Project documentation (README, PLAN, STATUS, feature-plan.json)

---

Alan Vo · [alanvo.net](https://alanvo.net) · [X: @alanvoasi](https://x.com/alanvoasi)
