"""
Sentinel Console - Anti-AI-slop design skill backend.
FastAPI server with health check endpoint.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sentinel Console",
    description="Anti-AI-slop design skill for Claude Code, Cursor, and Codex",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/api/version")
async def version():
    """Version endpoint."""
    return {"version": "0.1.0", "name": "sentinel-console-144"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
