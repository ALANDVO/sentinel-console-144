# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

skeleton

## Roadmap

### skeleton — FastAPI + React skeleton with health check

Status: done

Acceptance:
- FastAPI server starts on port 8000
- React dev server starts on port 3000
- GET /api/health returns 200 with {status: ok}
- Frontend loads and displays basic page

Implementation: `backend/main.py`, `frontend/src/App.jsx`, `frontend/src/App.css`, `frontend/src/index.css`, `frontend/index.html`

Tests: `Manual verification: both servers start, health endpoint returns 200, frontend renders`

### anti-slop-rules — Anti-AI-slop design rule engine

Status: planned

Acceptance:
- Rule definitions loaded from config
- CLI/API to lint design tokens
- Ban list enforcement for sloppy patterns

### skill-package — Claude Code skill package (skills/hallmark/)

Status: planned

Acceptance:
- SKILL.md with absolute GitHub URLs
- References copied into skills/hallmark/references/
- npx skills add works without broken links

### accessibility-fixes — Accessibility fixes for example cards

Status: planned

Acceptance:
- Example cards expose link role to AT
- Cards appear in links rotor

### reduced-motion — Reduced motion support for demo videos

Status: planned

Acceptance:
- Videos pause when prefers-reduced-motion: reduce
- Poster images shown as fallback

---

Alan Vo · [alanvo.net](https://alanvo.net) · [X: @alanvoasi](https://x.com/alanvoasi)
