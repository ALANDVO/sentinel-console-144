import './App.css'
import { useEffect, useState } from 'react'

function App() {
  const [health, setHealth] = useState(null)
  const [version, setVersion] = useState(null)

  useEffect(() => {
    fetch('/api/health')
      .then(r => r.json())
      .then(d => setHealth(d.status))
      .catch(() => setHealth('error'))
    fetch('/api/version')
      .then(r => r.json())
      .then(d => setVersion(d.version))
      .catch(() => setVersion('error'))
  }, [])

  return (
    <>
      <header className="hero-section">
        <div className="container">
          <h1>Sentinel Console</h1>
          <p className="tagline">Anti-AI-slop design skill for Claude Code, Cursor, and Codex</p>
          <div className="hero-actions">
            <a href="#features" className="btn btn-primary">Explore Features</a>
            <a href="https://github.com/ALANDVO/sentinel-console-144" className="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
          </div>
        </div>
      </header>

      <main>
        <section id="features" className="features-section">
          <div className="container">
            <h2>Design Rules That Catch AI Slop</h2>
            <p className="section-description">
              Sentinel Console encodes design taste as explicit, enforceable rules.
              No more generic AI output — every token, spacing value, and color
              passes through a curated rule set before it reaches your codebase.
            </p>

            <div className="features-grid">
              <article className="feature-card">
                <h3>Token Linting</h3>
                <p>Validates design tokens against a curated allowlist. No magic numbers, no arbitrary hex values — only approved spacing, sizing, and color scales.</p>
              </article>

              <article className="feature-card">
                <h3>Ban List Enforcement</h3>
                <p>Hard bans on sloppy patterns: untyped colors, inconsistent radii, manual px values where tokens should be used, and other AI tells.</p>
              </article>

              <article className="feature-card">
                <h3>Claude Code Skill</h3>
                <p>Install as a skill with <code>npx skills add</code>. Runs in your editor context — no separate tooling, no context switching.</p>
              </article>

              <article className="feature-card">
                <h3>Cursor &amp; Codex Ready</h3>
                <p>Works wherever you write code. Same rule engine, same standards, consistent output across AI assistants.</p>
              </article>

              <article className="feature-card">
                <h3>Extensible Rules</h3>
                <p>Add project-specific rules via config. Your design system, your constraints — encoded once, enforced everywhere.</p>
              </article>

              <article className="feature-card">
                <h3>CI Integration</h3>
                <p>Fail builds on slop. Add <code>sentinel lint</code> to your pipeline and catch regressions before merge.</p>
              </article>
            </div>
          </div>
        </section>

        <section id="how-it-works" className="how-it-works-section">
          <div className="container">
            <h2>How It Works</h2>
            <ol className="steps">
              <li>
                <strong>Install the skill</strong>
                <span><code>npx skills add ALANDVO/sentinel-console-144</code></span>
              </li>
              <li>
                <strong>Configure your tokens</strong>
                <span>Define approved spacing, color, and typography scales in <code>sentinel.config.json</code></span>
              </li>
              <li>
                <strong>Write code with AI</strong>
                <span>Claude Code, Cursor, or Codex generates UI — Sentinel validates every token in context</span>
              </li>
              <li>
                <strong>Ship consistent UI</strong>
                <span>No sloppy values slip through. Every PR meets your design standard.</span>
              </li>
            </ol>
          </div>
        </section>

        <section id="api-status" className="api-status-section">
          <div className="container">
            <h2>Backend API</h2>
            <div className="api-endpoints">
              <div className="endpoint">
                <code>GET /api/health</code>
                <span id="health-status">{health === 'ok' ? '✓ Healthy' : health === 'error' ? '✗ Unreachable' : 'Checking…'}</span>
              </div>
              <div className="endpoint">
                <code>GET /api/version</code>
                <span id="version-status">{version ? `v${version}` : 'Checking…'}</span>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="container">
          <p>Sentinel Console — Anti-AI-slop design skill</p>
          <p><a href="https://github.com/ALANDVO/sentinel-console-144" target="_blank" rel="noopener">GitHub</a> · <a href="https://github.com/ALANDVO/sentinel-console-144/issues" target="_blank" rel="noopener">Issues</a></p>
        </div>
      </footer>
    </>
  )
}

export default App
