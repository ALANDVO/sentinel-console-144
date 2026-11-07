# Sentinel Console

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

Sentinel Console encodes design taste as explicit, enforceable rules. No more generic AI output — every token, spacing value, and color passes through a curated rule set before it reaches your codebase.

## Features

- **Token Linting** — Validates design tokens against a curated allowlist
- **Ban List Enforcement** — Hard bans on sloppy patterns: untyped colors, inconsistent radii, manual px values
- **Claude Code Skill** — Install with `npx skills add`, runs in your editor context
- **Cursor & Codex Ready** — Same rule engine, consistent output across AI assistants
- **Extensible Rules** — Add project-specific rules via config
- **CI Integration** — Fail builds on slop with `sentinel lint`

## Quick Start

### Backend (FastAPI)

```bash
cd backend
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
```

Health check: `GET http://localhost:8000/api/health`

### Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Dev server: `http://localhost:3000`

### Production Build

```bash
cd frontend
npm run build
```

## Project Structure

```
sentinel-console-144/
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Landing page component
│   │   ├── App.css          # Landing page styles
│   │   ├── main.jsx         # React entry point
│   │   └── index.css        # Global styles
│   ├── index.html           # HTML template
│   ├── package.json
│   └── vite.config.js
├── feature-plan.json        # Feature roadmap
├── PLAN.md                  # Development plan
├── STATUS.md                # Checkpoint status
└── CHANGELOG.md             # Release notes
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/version` | Version info |

## Development

See [PLAN.md](PLAN.md) for the roadmap and [STATUS.md](STATUS.md) for current checkpoint status.

## License

MIT — see [LICENSE](LICENSE) for details.

Maintainer: Alan Vo <alanvo@gmail.com>

---

Alan Vo · [alanvo.net](https://alanvo.net)
